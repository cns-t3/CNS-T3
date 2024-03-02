from openai import OpenAI
from dotenv import load_dotenv
from backend.api.newsAPI.pydantic_models import NewsArticle
import os
import requests
import threading
import json

load_dotenv()

if os.getenv("OPENAI_API_KEY"):
    openAI_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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
        + "&lang=eng&articlesSortBy=rel&articlesCount=5"
    )
    news_articles = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data["articles"]["results"]
            threads = []
            summaries = [""] * len(articles)
            categories = [""] * len(articles)
            relations = [True] * len(articles)
            risks = [""] * len(articles)
            # the summaries are not returned in the same order as the articles, so we need to keep track of the order
            for count, article in enumerate(articles):
                thread = threading.Thread(
                    target=handle_body,
                    args=(
                        article["body"],
                        count,
                        summaries,
                        categories,
                        relations,
                        risks,
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
                    summary="",
                    score=0,
                    category="",
                    is_related=True,
                )
                news_articles.append(news)
            for thread in threads:
                thread.join()
            for i in range(len(news_articles)):
                news_articles[i].summary = summaries[i]
                news_articles[i].category = categories[i]
                news_articles[i].is_related = relations[i]
                news_articles[i].risk_rating = risks[i]
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
                "content": """Given a news article, complete the following actions

1. Summarize the news content in less than 100 words

2. Provide a category(ies) for the article (Source of Wealth, Family Circumstances, Sanctioned Countries, Sensitive industries). If none of the categories provided fits the article’s content, return Others as the category. It should only be one of these 5 categories: Source of Wealth, Family Circumstances, Sanctioned Countries, Sensitive industries, Others.
- To determine the category, these are the search patterns for each category:
- Source of wealth – search patterns : net worth, worth, income, inherit, inheritance, receive, gifted, settlement, sale proceeds, merger & acquisition, M&A, leveraged buyout
- Family circumstances – search patterns:  Marry, marriage, divorce, separation, children, child
- Sanctioned countries – search patterns (limited set): Cuba, Iran, North Korea, Syria, Crimea, Russia, Ukraine, Afghanistan, Albania, Algeria, Angola, Bahamas, Bangladesh, Barbados, Belarus, Belize, Bolivia, Botswana, Burkina Faso, Burundi, Cambodia, Cameroon, Central African Republic, Chad, Cayman Islands, Comoros, Congo, Democratic Republic of Côte d'Ivoire, Djibouti, Dominican Republic, Ecuador, Egypt
- Sensitive industries – search patterns: Casinos, Arms Dealer, Arms Material, Private Military Service Provider, Diamond, Precious stones, Money Remittance Business 

It should only be one of these 5 categories: Source of Wealth, Family Circumstances, Sanctioned Countries, Sensitive industries, Others.

3. Determine whether the article focuses on an individual engaging in the action rather than their associated company, and provide a true or false response. For example, ascertain if the article is about Tim Cook investing personally, not Apple as a company.

4. Give me a risk rating (low, medium or high) based on the following cases:
High Risk Rating Cases:
- Legal Issues: Scandals or legal troubles involving the client, News about the client being involved in fraud or money laundering investigations.
- Financial Distress: Reports of the client facing bankruptcy or financial instability, Significant debt or default issues.
- Sanctions and Embargoes: News indicating that the client or their associated entities are subject to sanctions or embargoes, News indicating that the client is investing in a sanctioned country (given above).
- Politically Exposed Persons (PEP): Identification of the client as a PEP, News about the client's involvement with politically sensitive activities.
Industry-specific Risks: Regulatory violations or controversies within the client's industry, Any news indicating non-compliance with industry standards.

Medium-Risk Cases:
- Change in Business Activities: Reports of significant changes in the client's business model or activities.
- Mergers and Acquisitions: News about the client being involved in mergers, acquisitions, or significant corporate restructuring.
- Market Performance: Fluctuations in the client's stock prices or financial performance.
- Management Changes: Significant changes in the client's leadership or management team.
- Partnerships and Alliances: News about the client forming partnerships or alliances that may pose moderate risks.

If the news does not belong to any of the above cases, return Low for its risk rating.

Return the data in JSON format: {"summary": "", "category": "", "is_related": "", "risk_rating":""}""",
            },
            {"role": "user", "content": input},
        ],
    )
    try:
        result = json.loads(completion.choices[0].message.content)
    except Exception as e:
        print("Error: ", e)
        result = {"summary": "", "category": "", "is_related": "", "risk_rating": ""}
    return result


def handle_body(article_body, news_id, summaries, categories, relations, risks):
    result = summarise_article(article_body, openAI_client)
    summaries[news_id] = result["summary"]
    categories[news_id] = result["category"]
    relations[news_id] = result["is_related"]
    risks[news_id] = result["risk_rating"]
