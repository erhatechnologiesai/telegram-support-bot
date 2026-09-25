import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_start_command(self):
        payload = {"update_id": 1, "message": {"chat": {"id": 1001}, "text": "/start"}}
        res = self.client.post("/telegram-webhook", json=payload)
        self.assertEqual(res.status_code, 200)
        self.assertIn("Welcome", res.json()["text"])

    def test_ticket_command(self):
        payload = {"update_id": 2, "message": {"chat": {"id": 1001}, "text": "/ticket"}}
        res = self.client.post("/telegram-webhook", json=payload)
        self.assertEqual(res.status_code, 200)
        self.assertIn("Support ticket", res.json()["text"])

    def test_natural_language_query(self):
        payload = {"update_id": 3, "message": {"chat": {"id": 1001}, "text": "Tell me about multi-agent pipelines"}}
        res = self.client.post("/telegram-webhook", json=payload)
        self.assertEqual(res.status_code, 200)
        self.assertIn("autonomous multi-agent", res.json()["text"])

if __name__ == "__main__":
    unittest.main()
