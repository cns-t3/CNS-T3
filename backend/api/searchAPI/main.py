from fastapi import FastAPI, Query, HTTPException
import requests
from backend.api.searchAPI.pydantic_models import SearchResult, NewsArticle
from backend.api.searchAPI.search_service import search_service

app = FastAPI()


@app.get(
    "/search",
    tags=["search"],
    summary="Get relevant news articles and social media posts by search query",
    description="Returns person's profile and an array of news articles",
    response_model=SearchResult,
)
async def get_articles_by_query(
    search_query: str = Query(
        ..., description="Search query of the articles to return"
    ),
):
    response = search_service(search_query)
    return response
