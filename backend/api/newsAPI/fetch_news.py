from openai import OpenAI
from dotenv import load_dotenv
from pydantic_models import NewsArticle
import os, requests, time, threading, json

load_dotenv()
openAI_client = OpenAI()


def get_summarised_news_articles(search_query: str):
    """
    Get news articles from the Event Registry API and summarise them using the
    OpenAI GPT-3.5 API
    """
    url = (
        "http://eventregistry.org/api/v1/article/getArticles?apiKey="
        + os.getenv("NEWS_API_KEY")
        + "&keyword="
        + search_query
        + "&lang=eng&articlesSortBy=rel&articlesCount=15"
    )
    news_articles = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data["articles"]["results"]
            threads = []
            summaries = [""] * len(articles)
            tags = [""] * len(articles)
            # the summaries are not returned in the same order as the articles, so we need to keep track of the order
            for count, article in enumerate(articles):
                thread = threading.Thread(
                    target=handle_body,
                    args=(article["body"], count, summaries, tags),
                )
                thread.start()
                threads.append(thread)
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
            for thread in threads:
                thread.join()
            for i in range(len(news_articles)):
                news_articles[i].summary = summaries[i]
                news_articles[i].tag = tags[i]
            return news_articles
    except Exception as e:
        print("Error: ", e)


def summarise_article(article_body, client):
    input = "Summarise this article for me: " + article_body
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": 'Given a news article, summarize its content in less than 100 words and provide a tag for the article (e.g., business, finance, lifestyle, politics, economics, investment). Return the data in JSON format: {"summary": "", "tag": ""}.',
            },
            {"role": "user", "content": input},
        ],
    )
    try:
        result = json.loads(completion.choices[0].message.content)
    except Exception as e:
        print("Error: ", e)
        result = {"summary": "", "tag": ""}
    return result


def handle_body(article_body, news_id, summaries, tags):
    result = summarise_article(article_body, openAI_client)
    summaries[news_id] = result["summary"]
    tags[news_id] = result["tag"]
