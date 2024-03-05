import requests
from fastapi import HTTPException
from backend.api.searchAPI.pydantic_models import SearchResult

def search_service(search_query: str):
    params = {"name": search_query}

    # Get person's profile
    person_endpoint = "http://127.0.0.1:8001/persons/search/"
    response = requests.get(person_endpoint, params=params)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404, detail="No person found with the provided name"
        )
    person = response.json()

    # Get news articles
    news_endpoint = "http://127.0.0.1:8002/news/" + person["name"]
    response = requests.get(news_endpoint)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404, detail="No news articles found for the person"
        )

    news_articles = response.json()
    search_result = SearchResult(person=person, newsArticles=news_articles)

    # Get identity matching score
    identity_endpoint = "http://127.0.0.1:8003/identity"
    response = requests.post(
        identity_endpoint, data=(search_result.model_dump_json()).encode("utf-8")
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=500, detail="Error occurred during identity verification"
        )

    return_object = SearchResult(**response.json())
    return return_object