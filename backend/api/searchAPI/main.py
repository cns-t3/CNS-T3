from fastapi import FastAPI, Query
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()


class NewsArticle(BaseModel):
    news_id: int
    title: str
    content: str
    publishedAt: str
    image_url: str
    source_url: str
    risk_rating: str
    summary: str
    score: int
    tag: str


class Profile(BaseModel):
    person_id: int
    occupation: str
    dob: str
    nationality: str
    description: str
    company: str
    img_url: str


class SearchResult(BaseModel):
    profile: Profile
    newsArticles: List[NewsArticle]


@app.get(
    "/search",
    response_model=SearchResult,
    tags=["search"],
    summary="Get relevant news articles and social media posts by search query",
    description="Returns person's profile and an array of news articles",
)
async def get_articles_by_query(
    search_query: str = Query(..., description="Search query of the articles to return")
):
    #this is the sample data
    profile = Profile(
        person_id=123,
        occupation="Software Engineer",
        dob="1990-01-01T00:00:00Z",
        nationality="American",
        description="A passionate software engineer.",
        company="ABC Inc.",
        img_url="https://example.com/profile_image",
    )
    news_articles = [
        NewsArticle(
            news_id=1,
            title="News Article 1",
            content="Content of News Article 1",
            publishedAt="2024-01-21T10:00:00Z",
            image_url="https://example.com/news_article_1.jpg",
            source_url="https://example.com/news_article_1",
            risk_rating="medium",
            summary="Summary of News Article 1",
            score=70,
            tag="business",
        ),
        NewsArticle(
            news_id=2,
            title="News Article 2",
            content="Content of News Article 2",
            publishedAt="2024-01-21T11:30:00Z",
            image_url="https://example.com/news_article_2.jpg",
            source_url="https://example.com/news_article_2",
            risk_rating="high",
            summary="Summary of News Article 2",
            score=85,
            tag="politics",
        ),
    ]

    return {"profile": profile, "newsArticles": news_articles}
