"""Pruebas de contrato por HTTP contra Waitress en loopback."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Thread
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from waitress import create_server
from qa.app import create_app


class HttpContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        directory = TemporaryDirectory()
        cls.addClassCleanup(directory.cleanup)
        server = create_server(
            create_app(Path(directory.name) / "http.sqlite"),
            host="127.0.0.1",
            port=0,
        )
        runner = Thread(target=server.run, name="http-contract", daemon=True)
        runner.start()
        cls.addClassCleanup(runner.join, 3)
        cls.addClassCleanup(server.close)
        cls.addClassCleanup(server.task_dispatcher.shutdown)
        cls.base = f"http://127.0.0.1:{server.effective_port}"

    def request(self, method, path, payload=None):
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        request = Request(self.base + path, data=body, method=method)
        if body is not None:
            request.add_header("Content-Type", "application/json")
        try:
            response = urlopen(request, timeout=5)
        except HTTPError as error:
            response = error
        with response:
            return response.status, response.headers, json.load(response)

    def test_ticket_lifecycle_over_http(self):
        code, _, health = self.request("GET", "/health")
        self.assertEqual((code, health), (200, {"status": "ok"}))
        code, headers, ticket = self.request("POST", "/tickets", {"title": "Prueba HTTP"})
        self.assertEqual(code, 201)
        self.assertEqual(ticket["state"], "open")
        path = headers["Location"]
        self.assertEqual(self.request("GET", path)[2], ticket)
        for _ in range(2):
            code, _, closed = self.request("PATCH", path + "/close")
            self.assertEqual((code, closed["state"]), (200, "closed"))
        self.assertEqual(self.request("GET", path)[2]["state"], "closed")

    def test_invalid_title_leaves_collection_unchanged(self):
        before = self.request("GET", "/tickets")[2]
        code, _, error = self.request("POST", "/tickets", {"title": " "})
        self.assertEqual(code, 400)
        self.assertIn("error", error)
        self.assertEqual(self.request("GET", "/tickets")[2], before)


if __name__ == "__main__":
    unittest.main()
