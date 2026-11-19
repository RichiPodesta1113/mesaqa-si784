import tempfile
import unittest
from pathlib import Path

from qa.app import create_app


class TicketsTest(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.database = Path(directory.name) / "qa.sqlite"
        self.client = create_app(self.database).test_client()

    def create_ticket(self, title="Validar formulario"):
        return self.client.post("/tickets", json={"title": title})

    def test_health_and_headers(self):
        response = self.client.get("/health")
        self.assertEqual(response.json, {"status": "ok"})
        self.assertEqual(response.headers["Cache-Control"], "no-store")
        self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")

    def test_create_and_read(self):
        created = self.create_ticket("  Revisar documentación  ")
        self.assertEqual(created.status_code, 201)
        self.assertEqual(created.json["state"], "open")
        self.assertEqual(created.json["title"], "Revisar documentación")
        self.assertEqual(self.client.get(created.headers["Location"]).json, created.json)

    def test_list_is_newest_first(self):
        first = self.create_ticket("Primera").json
        second = self.create_ticket("Segunda").json
        self.assertEqual(self.client.get("/tickets").json["items"], [second, first])

    def test_invalid_payload_does_not_write(self):
        for payload in ({}, [], {"title": " "}, {"title": 2}, {"title": "X" * 121}):
            with self.subTest(payload=payload):
                self.assertEqual(self.client.post("/tickets", json=payload).status_code, 400)
        self.assertEqual(self.client.get("/tickets").json["items"], [])

    def test_invalid_media_type_and_json(self):
        self.assertEqual(self.client.post("/tickets", data="texto").status_code, 415)
        response = self.client.post("/tickets", data="{", content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_large_body_is_rejected(self):
        response = self.create_ticket("X" * 9000)
        self.assertEqual(response.status_code, 413)
        self.assertEqual(response.content_type, "application/json")

    def test_missing_ticket_returns_404(self):
        self.assertEqual(self.client.get("/tickets/99").status_code, 404)
        self.assertEqual(self.client.patch("/tickets/99/close").status_code, 404)

    def test_close_is_idempotent_and_persistent(self):
        created = self.create_ticket()
        location = created.headers["Location"]
        for _ in range(2):
            response = self.client.patch(location + "/close")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["state"], "closed")
        fresh_client = create_app(self.database).test_client()
        self.assertEqual(fresh_client.get(location).json["state"], "closed")

    def test_index_discovery(self):
        self.assertEqual(self.client.get("/").json["tickets"], "/tickets")


if __name__ == "__main__":
    unittest.main()
