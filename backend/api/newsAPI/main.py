from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from openai import OpenAI

# from fetch_news import get_summarised_news_articles
from backend.api.newsAPI.fetch_news import get_summarised_news_articles
from backend.api.newsAPI.pydantic_models import NewsArticle

load_dotenv()
app = FastAPI()
openAI_client = OpenAI()


@app.get(
    "/news/{search_query}",
    response_model=List[NewsArticle],
    tags=["news"],
    summary="Get news articles",
    description="Returns an array of news articles",
)
async def get_news_articles(search_query: str):
    try:
        return get_summarised_news_articles(search_query)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
