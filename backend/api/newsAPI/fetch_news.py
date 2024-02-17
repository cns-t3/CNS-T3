from dotenv import load_dotenv
from news import NewsArticle
import os, requests, threading, time, json

load_dotenv()


def fetch_news_articles(search_query: str):
    url = (
        "http://eventregistry.org/api/v1/article/getArticles?apiKey="
        + os.getenv("NEWS_API_KEY")
        + "&keyword="
        + search_query
        + "&lang=eng&articlesSortBy=rel&articlesCount=20"
    )
    news_articles = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data["articles"]["results"]
            for count, article in enumerate(articles):
                news = NewsArticle(
                    news_id=count,
                    title=article["title"],
                    publisher=article["source"]["title"],
                    content=article["body"],
                    publishedAt=article["dateTimePub"],
                    source_url=article["url"],
                    image_url=article["image"] if article["image"] != None else "",
                    risk_rating="low",
                    summary="",
                    score=0,
                    tag="",
                )
                news_articles.append(news)
            return news_articles
    except Exception as e:
        print("Error: ", e)
