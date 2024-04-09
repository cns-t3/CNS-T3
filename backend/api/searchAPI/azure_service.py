import os
from datetime import datetime
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()


def upload_to_azure(blob_name, blob_file):
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(
        container="fyp2024g01cns", blob=blob_name
    )
    blob_client.upload_blob(blob_file, overwrite=True)


def download_from_azure(blob_name):
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    try:
        blob_client = blob_service_client.get_blob_client(
            container="fyp2024g01cns", blob=blob_name
        )
        downloader = blob_client.download_blob(max_concurrency=1, encoding="UTF-8")
        last_modified = blob_client.get_blob_properties().last_modified
        last_modified_readable = datetime.strftime(last_modified, "%Y-%m-%d")
        blob_text = downloader.readall()
        return blob_text, last_modified_readable
    except Exception as e:
        print("error")
        print(e)
