from datetime import datetime
from backend.api.searchAPI.search_service import search_persons_service
from backend.api.searchAPI.azure_service import upload_to_azure


def get_daily_data():
    try:
        # Get all the news articles for each person
        response = search_persons_service()
        # upload the JSON for each person in the format id_YYYYMMDD where the date is the date of retrieval
        for search_result in response:
            current_date = datetime.now().strftime("%Y-%m-%d")
            file_name = str(search_result.person.person_id) + "_" + current_date
            json = search_result.model_dump_json()
            upload_to_azure(file_name, json)
    except Exception as e:
        print("Exception")
        print(e)
