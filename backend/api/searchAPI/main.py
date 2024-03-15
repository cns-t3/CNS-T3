import threading
import schedule
import time
from fastapi import FastAPI, Query, HTTPException
from backend.api.searchAPI.pydantic_models import SearchResult
from backend.api.searchAPI.search_service import search_person_service
from backend.api.searchAPI.caching_service import get_daily_data

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
    response = search_person_service(search_query)
    return response


# Scheduler to get data everyday at 00:00
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule.every().day.at("00:00").do(get_daily_data)
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()
