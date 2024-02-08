from fastapi import FastAPI, Query, HTTPException
import requests
from pydantic_models import SearchResult

app = FastAPI()


@app.get(
    "/search",
    # response_model=SearchResult,
    tags=["search"],
    summary="Get relevant news articles and social media posts by search query",
    description="Returns person's profile and an array of news articles",
    response_model=SearchResult
)
async def get_articles_by_query(
    search_query: str = Query(..., description="Search query of the articles to return"),
):
    # get person data first
    params = {"name": search_query}
    person_endpoint = "http://127.0.0.1:8001/persons/search/"
    response = requests.get(person_endpoint, params=params)
    if response.status_code == 200:
        person = response.json()
    else:
        raise HTTPException(
            status_code=404, detail="No person found with the provided name"
        )

    news_endpoint = "http://127.0.0.1:8002/news/" + search_query
    response = requests.get(news_endpoint)
    if response.status_code == 200:
        news_articles = response.json()
        search_result = SearchResult(person=person, newsArticles=news_articles)
        return search_result
