from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
from backend.api.newsAPI.pydantic_models import NewsArticle
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)
import os
import requests
import threading
import json

load_dotenv()

if os.getenv("OPENAI_API_KEY"):
    openAI_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_categories():
    with open("backend/api/newsAPI/categories.json", "r") as file:
        data = json.load(file)
    formatted_categories = [category.title() for category in data["categories"]]

    final_string = ", ".join(formatted_categories)
    return final_string


def get_prompt():
    with open("backend/api/newsAPI/prompt.txt", "r") as file:
        data = file.read()
    return data


def get_search_patterns():
    with open("backend/api/newsAPI/categories.json", "r") as file:
        data = json.load(file)
    formatted_string = ", ".join(
        [
            f"{category} - search pattern: {', '.join(patterns)}"
            for category, patterns in data["categories"].items()
            if patterns
        ]
    )
    return formatted_string


# New function to get reputable news sources from JSON
def get_reputable_news_sources():
    with open("backend/api/newsAPI/news_sources.json", "r") as file:
        data = json.load(file)
    return data["sources"]


def get_summarised_news_articles(search_query: str):
    """
    Retrieves and summarises news articles using NewsAI API and GPT-3.5 API.
    """
    today = datetime.today().strftime('%Y-%m-%d')

    url = (
        "http://eventregistry.org/api/v1/article/getArticles?apiKey="
        + os.getenv("NEWS_API_KEY")
        + "&keyword="
        + search_query
        + "&lang=eng&articlesSortBy=rel&articlesCount=20&isDuplicateFilter=skipDuplicates&dateStart=2023-01-01&dateEnd="
        + today
    )

    reputable_sources = get_reputable_news_sources()  # Get reputable sources

    news_articles = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json()["articles"]["results"]
            # Filter articles by reputable sources
            articles = [
                article
                for article in articles
                if article["source"]["title"] in reputable_sources
            ]
            threads = []
            summaries = [""] * len(articles)
            categories = [""] * len(articles)
            risks = [""] * len(articles)
            subject_summaries = [""] * len(articles)
            justifications = [""] * len(articles)
            # the summaries are not returned in the same order as the articles, so we need to keep track of the order
            for count, article in enumerate(articles):
                thread = threading.Thread(
                    target=handle_body,
                    args=(
                        article["body"],
                        count,
                        summaries,
                        categories,
                        risks,
                        subject_summaries,
                        justifications
                    ),
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
                    image_url=article["image"] if article["image"] is not None else "",
                    risk_rating="",
                    risk_justification="",
                    summary="",
                    score=0,
                    category="",
                    subject_summary="",
                )
                news_articles.append(news)
            for thread in threads:
                thread.join()
            for i in range(len(news_articles)):
                news_articles[i].summary = summaries[i]
                news_articles[i].category = categories[i]
                news_articles[i].risk_rating = risks[i]
                news_articles[i].subject_summary = subject_summaries[i]
                news_articles[i].risk_justification = justifications[i]
            return news_articles
    except Exception as e:
        print("Error: ", e)


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def summarise_article(article_body, client):
    input = "Summarise this article for me: " + article_body
    prompt = get_prompt()
    categories = get_categories()
    search_patterns = get_search_patterns()
    prompt = prompt.replace("{{ categories }}", categories)
    prompt = prompt.replace("{{ search_patterns }}", search_patterns)

    completion = client.chat.completions.create(
        temperature=0.6,
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {"role": "user", "content": input},
        ],
    )
    try:
        result = json.loads(completion.choices[0].message.content)
    except Exception as e:
        print("Error: ", e)
        result = {
            "summary": "",
            "category": "",
            "risk_rating": "",
            "subject_summary": "",
            "risk_justification": "",
        }
    return result


def handle_body(article_body, news_id, summaries, categories, risks, subject_summaries, justifications):
    result = summarise_article(article_body, openAI_client)
    summaries[news_id] = result["summary"]
    categories[news_id] = result["category"]
    risks[news_id] = result["risk_rating"]
    subject_summaries[news_id] = result["subject_summary"]
    justifications[news_id] = result["risk_justification"]