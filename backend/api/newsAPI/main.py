from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from openai import OpenAI
from summarise_data import get_summarised_news_articles


load_dotenv()
app = FastAPI()
openAI_client = OpenAI()


class NewsArticle(BaseModel):
    news_id: int
    title: str
    content: str
    publisher: str
    publishedAt: str
    image_url: str = ""
    source_url: str
    risk_rating: str
    summary: str
    score: int
    tag: str


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
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
