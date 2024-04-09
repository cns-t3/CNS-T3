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
def get_analytics_summary(summaries: List[str]):
    try:
        if len(summaries) == 0:
            return ""

        input = "Summarise the following articles in less than 150 words in a clear and concise manner. The summary should be written to show what had happened./n"

        for summary in summaries:
            input += f"{summary}\n"

        response = openAI_client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system",
                    "content": input,
                },
            ],
        )
        return response.choices[0].message.content
    except Exception:
        return ""
