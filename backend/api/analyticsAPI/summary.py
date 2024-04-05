from openai import OpenAI
from dotenv import load_dotenv
from typing import List
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)
import os


load_dotenv()

if os.getenv("OPENAI_API_KEY"):
    openAI_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def get_analytics_summary(summaries: List[str], client):
    prompt = "Summarise the following articles in less than 150 words in a clear and concise manner."
    input = ""
    count = 1
    
    for summary in summaries:
        input += count + ": " + summary + "\n"

    analytics_summary = client.chat.completions.create(
        temperature=0.6,
        model="gpt-3.5-turbo-0125",
        response_format={"type": "text"},
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {"role": "user", "content": input},
        ],
    )
    return analytics_summary