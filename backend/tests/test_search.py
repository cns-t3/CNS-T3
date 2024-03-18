import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from backend.api.searchAPI.main import app


class TestSearchAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    @patch("backend.api.searchAPI.main.search_person_service")
    def test_search_query(self, mock_get):
        person_data = {
            "person_id": 4,
            "name": "Helen Wong",
            "role": "CEO",
            "occupation": "CEO",
            "dob": "1961-06-01",
            "nationality": None,
            "description": None,
            "company": "OCBC",
            "country_of_residency": "Singapore",
            "pep_status": None,
            "source_of_wealth": "Banking and Finance",
            "img_url": None,
        }
        news_data = [
            {
                "news_id": 4,
                "title": "AC Ventures closes its new $210M Indonesia-focused fund",
                "content": "In the middle of a long funding winter, AC Ventures' latest news will give Southeast Asian startups hope.\\n\\nThe Jakarta, Indonesia-based venture firm announced today it has raised $210 million, finishing the final close on its fifth fund, called ACV Fund V. Limited partners include the World's Bank's IFC and investors from the United States, the Middle East and north Asia. More than 50% of the fund came from returning LPs and institutional capital makes up over 90% of its total.",
                "publisher": "Yahoo News",
                "publishedAt": "2024-01-23T02:00:33Z",
                "image_url": "https://s.yimg.com/ny/api/res/1.2/k9CWikJ4u6pbuoJhjs0WvQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA7Y2Y9d2VicA--/https://media.zenfs.com/en/techcrunch_350/46b1f5a3f001ab7511a238ce81c05e54",
                "source_url": "https://news.yahoo.com/ac-ventures-closes-210m-indonesia-020033546.html?guccounter=1&guce_referrer=aHR0cDovL3Jzcy5uZXdzLnlhaG9vLmNvbS9yc3MvYnVzaW5lc3M&guce_referrer_sig=AQAAAIs1aP3gI3MbJGyy2kSB9iMziY24GMROefOvLPsx7zTUhtyPpagS7CGbDpIbSjG5ugBb4VBslI6CvfJBJU9PPViLxYsJ6wcQNJXzdeSHgHoZo38CWvH_hDDCsW78F9uyAtRkZvp4bOiPeP7BZInbNHtS_Z9fAOslC9AphaChubHH",
                "risk_rating": "low",
                "summary": "AC Ventures, based in Jakarta, Indonesia, raised $210 million for its fifth fund, attracting investors from various regions. The firm targets Southeast Asian startups for investment, with a focus on Indonesia's growing economy. Fund V will support startups in fintech, e-commerce, health tech, and climate sectors, prioritizing those with social and environmental impacts. AC Ventures stresses gender parity and inclusive leadership in its portfolio and offers support to startups in business development, partnerships, and fundraising.",
                "score": 0,
                "category": "business",
                "subject_summary": "",
            }
        ]

        mock_get.return_value = {
            "person": person_data,
            "newsArticles": news_data,
        }
        response = self.client.get("search?search_query=helen%20wong")
        expected_response = {
            "person": person_data,
            "newsArticles": news_data,
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)
