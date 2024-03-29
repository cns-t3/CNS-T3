import requests
import json
from fastapi import HTTPException
from backend.api.searchAPI.pydantic_models import SearchResult
from backend.api.searchAPI.azure_service import download_from_azure

from dotenv import load_dotenv
import os

load_dotenv()

if os.getenv("PERSON_DNS"):
    person_hostname = os.getenv("PERSON_DNS")
else:
    person_hostname = "127.0.0.1"

if os.getenv("NEWS_DNS"):
    news_hostname = os.getenv("NEWS_DNS")
else:
    news_hostname = "127.0.0.1"

if os.getenv("IDENTITY_DNS"):
    identity_hostname = os.getenv("IDENTITY_DNS")
else:
    identity_hostname = "127.0.0.1"

def search_person_service(search_query: str):
    params = {"name": search_query}

    # Get person's profile
    person_endpoint = f"http://{person_hostname}:8001/persons/search/"
    response = requests.get(person_endpoint, params=params)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404, detail="No person found with the provided name"
        )
    person = response.json()
    return get_search_result_from_person(person)


# To get all persons in the database
def search_persons_service():
    person_all_endpoint = "http://{person_hostname}:8001/persons/"
    response = requests.get(person_all_endpoint)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="No persons found")
    persons = response.json()
    search_result_arr = []
    for person in persons:
        search_result_arr.append(get_search_result_from_person(person, True))
    return search_result_arr

def get_person_by_id(person_id):
    params = {"person_id": person_id}

    # Get person's profile
    person_endpoint = f"http://{person_hostname}:8001/persons/id"
    response = requests.get(person_endpoint, params=params)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404, detail="No person found with the provided name"
        )
    person = response.json()
    return get_search_result_from_person(person)


def get_search_result_from_person(person, daily_job=False):
    # get data from azure
    if not daily_job:
        try:
            return get_search_result_azure(person)
        except Exception as e:
            print("Not found in cache")
            print(e)

    news_endpoint = f"http://{news_hostname}:8002/news/" + person["name"]
    response = requests.get(news_endpoint)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404, detail="No news articles found for the person"
        )

    news_articles = response.json()
    search_result = SearchResult(person=person, newsArticles=news_articles)

    # Get identity matching score
    identity_endpoint = f"http://{identity_hostname}:8003/identity"
    response = requests.post(
        identity_endpoint, data=(search_result.model_dump_json()).encode("utf-8")
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=500, detail="Error occurred during identity verification"
        )

    return_object = SearchResult(**response.json())
    return return_object


def get_search_result_azure(person):
    blob_name = str(person["person_id"])
    json_data = json.loads(download_from_azure(blob_name))
    result = SearchResult(**json_data)
    return result
