import unittest
from fastapi.testclient import TestClient
from backend.api.newsAPI.main import app

class TestNewsAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_get_news(self):
        response = self.client.get("/news/anthony%20tan")
        self.assertEqual(response.status_code, 200)
