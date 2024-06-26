import threading
import schedule
import time
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from backend.api.searchAPI.pydantic_models import SearchResult
from backend.api.searchAPI.search_service import get_person_by_id
from backend.api.searchAPI.caching_service import get_daily_data

load_dotenv()
app = FastAPI()


@app.get(
    "/search",
    tags=["search"],
    summary="Get profile, summary analytics and relevant news articles by search query",
    description="Returns person's profile, summary analytics and an array of news articles",
    response_model=SearchResult,
)
async def get_articles_by_query(
    person_id: int = Query(..., description="Search query of the articles to return"),
):
    response = get_person_by_id(person_id)
    return response


if os.getenv("PROD"):

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    schedule.every().day.at("00:00").do(get_daily_data)
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
