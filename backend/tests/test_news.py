import unittest
from fastapi.testclient import TestClient
from backend.api.newsAPI.main import app
from unittest.mock import patch
import os


class TestNewsAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"})
    @patch("backend.api.newsAPI.fetch_news.requests.get")
    def test_get_news(self, mock_get):
        mock_news_data = {
            "articles": {
                "results": [
                    {
                        "uri": "7987660397",
                        "lang": "eng",
                        "isDuplicate": False,
                        "date": "2024-02-19",
                        "time": "16:23:42",
                        "dateTime": "2024-02-19T16:23:42Z",
                        "dateTimePub": "2024-02-19T16:13:10Z",
                        "dataType": "news",
                        "sim": 0,
                        "url": "https://www.sunstar.com.ph/davao/feature/estrella-golingays-reflections-on-writing",
                        "title": "Estrella Golingay's reflections on writing",
                        "body": 'WHEN I had the opportunity to interview the veteran writer, Estrella Taño Golingay, I did not receive an immediate confirmation. Curious about her initial reluctance, I asked her why. She candidly admitted feeling somewhat disconnected from the writing community in Soccsksargen.\n\nDespite her veteran status, she confessed to feeling like she did not quite fit into the vibrant tapestry of writers that make up the region\'s literary scene.\n\nMotivated by a strong desire to capture the wisdom of our seasoned literary writers, I embarked on a mission to reach out to them and arrange interviews at their convenience. Fortunately, Golingay agreed to my request, and we found ourselves engaged in a profound dialogue within the comforting confines of her modest home in Surallah, South Cotabato.\n\nIt was a powerful demonstration of how words can bridge the generational gap and foster a deeper understanding of our shared literary heritage.\n\nIn the 1950s, Golingay\'s family found a new home in Norala, South Cotabato, through the Philippine government\'s migration program. They originally came from Catanduanes in the Bicol Region.\n\nHowever, due to the turmoil in Norala at the time, they eventually moved to the nearby town of Surallah. This cultural shift from being Bicolanos to being in an Ilonggo-dominated community added a new dimension to Golingay\'s experiences, enriching her narrative as a writer.\n\nIt was a testament to their adaptability and resilience, a story that became a part of their family history.\n\nThis unique experience brought its own set of challenges, particularly in terms of identity and language. Golingay struggled with a sense of \'ambivalent rootedness" in her linguistic heritage.\n\nDespite her Bicolano roots, she admitted to not fully mastering the language. At the same time, she was still finding her place in the Hiligaynon language, highlighting the complex linguistic landscape she navigated daily. It was a delicate dance between two cultures, a balancing act on the tightrope of identity.\n\n"I felt incomplete," she confessed. "At times, I would reach out to family members, seeking to fill the gaps in my Bicol vocabulary. Who cares if I don\'t write in pure Bicolano? I wanted to write in SOX Bicol," she shared, her words reflecting her determination to carve out her own linguistic identity.\n\nThis conundrum reflects the experiences of many writers in the region, whose narratives are influenced by the various ethnolinguistic groups residing in Soccsksargen (SOX). This cultural melting pot has given rise to a unique linguistic fusion, a harmonious blend of diverse languages that has developed and matured over time, much like the region itself.\n\nThe American educational system in the country, placing great emphasis on the English language played a crucial role in shaping Golingay\'s linguistic skills.\n\nAs a young student, she found herself drawn to the abundance of English reading materials in her school library, a haven where she could fully immerse herself in the world of words.\n\nThis fascination with the English language eventually guided her academic journey. She pursued a Bachelor of Arts in English at Notre Dame of Marbel University (NDMU) and continued her studies at the University of Mindanao in Davao City from 1971 to 1974.\n\nIt was a testament to her dedication and passion for the language that had captivated her since her early years.\n\nGolingay\'s relationship with writing fluctuated like the ebb and flow of tides. During her school years, she actively participated in literary contests and campus journalism, her words flowing freely onto the page. However, as life unfolded and brought the joys of marriage and motherhood, the once-prominent spark in her writing seemed to diminish. Her academic career further complicated matters, leaving little room for indulging in the creation of literary pieces.\n\n"I found myself caught in a delicate dance, trying to balance the demands of writing, family life, and an academic career," she confessed. "Amid this juggling act, I somehow lost my way; my writing went into a long hibernation."\n\nHer words painted a vivid picture of the challenges faced by many individuals striving to balance their passions with life\'s responsibilities.\n\nThe heartbreaking loss of her third child to illness awakened a dormant fire within Golingay, reigniting her love for writing. This devastating experience as a mother inspired her to write "Si Nene at Ako sa Pagitan ng Gabi at Liwanag" -- more than just a piece of writing, it was an emotional release, a way for her to navigate the turbulent sea of grief.\n\nAs a testament to her talent and resilience, she submitted this deeply personal piece to Home Life Magazine. The literary world recognized the raw emotion and compelling narrative in her work, awarding it the coveted first prize in 1994. It was a silver lining in the storm, a beacon of hope in the darkness.\n\nThis recognition served as a springboard, propelling her into prestigious writing workshops across the country. Her journey included the Cultural Center of the Philippines (CCP)-sponsored workshop in 1994, followed by the esteemed Iligan National Writers Workshop in 1995.\n\nShe also attended a University of the Philippines (UP) Diliman-funded workshop on the idyllic Samal Island, where she had the privilege of learning from literary luminaries such as Anthony Tan, Jaime Ann Lim, and N.V.M. Gonzales.\n\nGolingay likened her writing journey to a thrilling roller coaster ride -- a thrilling adventure filled with unexpected twists and turns. The opportunities it presented exceeded her wildest expectations, a testament to the unpredictable yet rewarding nature of the literary world.',
                        "source": {
                            "uri": "sunstar.com.ph",
                            "dataType": "news",
                            "title": "Sun.Star Network Online",
                        },
                        "authors": [],
                        "image": "https://media.assettype.com/sunstar%2F2024-02%2F179db7ac-60f2-41ec-ac2e-f772d885e8ce%2FUntitled_design___2024_02_19T235531_760.png?w=1200&ar=40%3A21&auto=format%2Ccompress&ogImage=true&mode=crop&enlarge=true&overlay=false&overlay_position=bottom&overlay_width=100",
                        "eventUri": None,
                        "sentiment": 0.3254901960784313,
                        "wgt": 1,
                        "relevance": 1,
                    }
                ],
                "totalResults": 14,
                "page": 1,
                "count": 1,
                "pages": 14,
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_news_data
        response = self.client.get("/news/anthony%20tan")
        self.assertEqual(response.status_code, 200)
