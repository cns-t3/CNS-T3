from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
if os.getenv("OPENAI_API_KEY"):
    openAI_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_embedding(content: str):
    response = openAI_client.embeddings.create(
        input=content,
        model="text-embedding-3-large",
    )

    return response.data[0].embedding
