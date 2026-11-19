from contextlib import closing
from pathlib import Path
import os
import sqlite3

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException


def create_app(database=None):
    app = Flask(__name__)
    app.config.update(MAX_CONTENT_LENGTH=8192)
    db = Path(database or os.environ.get("QA_DB", "data/tickets.sqlite3"))
    db.parent.mkdir(parents=True, exist_ok=True)

    with closing(sqlite3.connect(db)) as connection, connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                state TEXT NOT NULL DEFAULT 'open' CHECK(state IN ('open', 'closed'))
            )
        """)

    @app.errorhandler(HTTPException)
    def http_error(error):
        return jsonify(error=error.name), error.code

    @app.after_request
    def no_cache(response):
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

    @app.get("/")
    def index():
        return jsonify(service="MesaQA", health="/health", tickets="/tickets")

    @app.get("/health")
    def health():
        with closing(sqlite3.connect(db)) as connection:
            connection.execute("SELECT 1").fetchone()
        return jsonify(status="ok")

    @app.get("/tickets")
    def list_tickets():
        with closing(sqlite3.connect(db)) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                "SELECT id, title, state FROM tickets ORDER BY id DESC LIMIT 100"
            ).fetchall()
        return jsonify(items=[dict(row) for row in rows])

    @app.post("/tickets")
    def create_ticket():
        if not request.is_json:
            return jsonify(error="Se requiere application/json"), 415

        payload = request.get_json(silent=True)
        title = payload.get("title") if isinstance(payload, dict) else None
        if not isinstance(title, str) or not 1 <= len(title.strip()) <= 120:
            return jsonify(error="El título debe tener entre 1 y 120 caracteres"), 400

        title = title.strip()
        with closing(sqlite3.connect(db)) as connection, connection:
            cursor = connection.execute("INSERT INTO tickets(title) VALUES (?)", (title,))
            ticket_id = cursor.lastrowid
        response = jsonify(id=ticket_id, title=title, state="open")
        response.headers["Location"] = f"/tickets/{ticket_id}"
        return response, 201

    @app.get("/tickets/<int:ticket_id>")
    def get_ticket(ticket_id):
        with closing(sqlite3.connect(db)) as connection:
            connection.row_factory = sqlite3.Row
            row = connection.execute(
                "SELECT id, title, state FROM tickets WHERE id = ?", (ticket_id,)
            ).fetchone()
        if row is None:
            return jsonify(error="Incidencia no encontrada"), 404
        return jsonify(dict(row))

    @app.patch("/tickets/<int:ticket_id>/close")
    def close_ticket(ticket_id):
        with closing(sqlite3.connect(db)) as connection, connection:
            cursor = connection.execute("UPDATE tickets SET state = 'closed' WHERE id = ?", (ticket_id,))
            if cursor.rowcount == 0:
                return jsonify(error="Incidencia no encontrada"), 404
        return jsonify(id=ticket_id, state="closed")

    return app
