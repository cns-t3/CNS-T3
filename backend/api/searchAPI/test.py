from dotenv import load_dotenv
import json
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

load_dotenv()

try:
    # This is the code to upload data
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(
        container="fyp2024g01cns", blob="test1"
    )
    # sample_dict = {"test": "value"}
    # sample_json = json.dumps(sample_dict)
    # blob_client.upload_blob(sample_json)
    downloader = blob_client.download_blob(max_concurrency=1, encoding="UTF-8")
    blob_text = downloader.readall()
    print(f"Blob contents: {blob_text}")

except Exception as e:
    print("Exception:")
    print(e)


def download_blob_to_string(
    self, blob_service_client: BlobServiceClient, container_name
):
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob="test1"
    )

    # encoding param is necessary for readall() to return str, otherwise it returns bytes
    downloader = blob_client.download_blob(max_concurrency=1, encoding="UTF-8")
    blob_text = downloader.readall()
    print(f"Blob contents: {blob_text}")
