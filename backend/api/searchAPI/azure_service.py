import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()


def upload_to_azure(blob_name, blob_file):
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(
        container="fyp2024g01cns", blob=blob_name
    )
    blob_client.upload_blob(blob_file)


def download_from_azure(blob_name):
    print(blob_name)
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    try:
        blob_client = blob_service_client.get_blob_client(
            container="fyp2024g01cns", blob=blob_name
        )
        downloader = blob_client.download_blob(max_concurrency=1, encoding="UTF-8")
        blob_text = downloader.readall()
        return blob_text
    except Exception as e:
        print("error")
        print(e)
