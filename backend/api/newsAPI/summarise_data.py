# from openai import OpenAI
# from pydantic import BaseModel
# import requests, threading, time
# from azure.identity import DefaultAzureCredential
# from azure.keyvault.secrets import SecretClient
# import os

# #def get_secret_client():
# #    credential = DefaultAzureCredential()
# #    secret_client = SecretClient(vault_url="https://cnst3.vault.azure.net/", credential=credential)
# #    return secret_client

# #def get_news_api_key():
# #    secret_client = get_secret_client()
# #    return secret_client.get_secret("NEWS-API-KEY").value

# def get_news_api_key():
#     return os.getenv("NEWSAPIKEY")

# openAI_client = OpenAI()

# class NewsArticle(BaseModel):
#     news_id: int
#     title: str
#     content: str
#     publisher: str
#     publishedAt: str
#     image_url: str = ""
#     source_url: str
#     risk_rating: str
#     summary: str
#     score: int
#     tag: str


# def get_summarised_news_articles(search_query: str):
#     """
#     Get news articles from the Event Registry API and summarise them using the
#     OpenAI GPT-3.5 API
#     """
#     url = (
#         "http://eventregistry.org/api/v1/article/getArticles?apiKey="
#         + get_news_api_key()
#         + "&keyword="
#         + search_query
#         + "&lang=eng&articlesSortBy=rel&articlesCount=20"
#     )
#     news_articles = []
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             count = 0
#             threads = []
#             summaries = [""] * len(data["articles"]["results"])
#             # the summaries are not returned in the same order as the articles, so we need to keep track of the order
#             for article in data["articles"]["results"]:
#                 thread = threading.Thread(
#                     target=handle_body,
#                     args=(
#                         article["body"],
#                         count,
#                         summaries,
#                     ),
#                 )
#                 thread.start()
#                 threads.append(thread)
#                 news = NewsArticle(
#                     news_id=count,
#                     title=article["title"],
#                     publisher=article["source"]["title"],
#                     content=article["body"],
#                     publishedAt=article["dateTimePub"],
#                     source_url=article["url"],
#                     image_url=article["image"] if article["image"] != None else "",
#                     risk_rating="low",
#                     summary="",
#                     score=0,
#                     tag="",
#                 )
#                 news_articles.append(news)
#                 count += 1
#             for thread in threads:
#                 thread.join()
#             for i in range(len(news_articles)):
#                 news_articles[i].summary = summaries[i]
#             return news_articles
#     except Exception as e:
#         print("Error: ", e)


# def summarise_article(article_body, client):
#     input = "Summarise this article for me: " + article_body
#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo-0125",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are an assistant that can summarise news articles to 100 words or less",
#             },
#             {"role": "user", "content": input},
#         ],
#     )
#     summary = completion.choices[0].message.content
#     return summary


# def handle_body(article_body, news_id, summaries):
#     summary = summarise_article(article_body, openAI_client)
#     summaries[news_id] = summary
#     time.sleep(0.001)
