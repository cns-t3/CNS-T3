import numpy as np
import os
from openai import OpenAI
from dotenv import load_dotenv
from backend.api.identityAPI.embedding import get_embedding

load_dotenv()

if os.getenv("OPENAI_API_KEY"):
    openAI_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_profile_summary(profile: dict):
    response = openAI_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Provide a concise 100-word summary using the provided JSON data, excluding the photo and LinkedIn link. Focus on text only and aim for simplicity and clarity in communication.",
            },
        ],
    )
    return response.choices[0].message.content


def get_cosine_similarity(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vector dimensions must be the same")

    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    return dot_product / (norm_a * norm_b)


def identity_matching(searchData: dict):
    # get profile summary
    profile_summary = get_profile_summary(searchData["person"])

    # get profile summary embedding
    profile_vector = get_embedding(profile_summary)
    for newsArticle in searchData["newsArticles"]:
        # get subject summary embedding
        subject_vector = get_embedding(newsArticle["subject_summary"])

        # cosine similarity
        similarity = get_cosine_similarity(profile_vector, subject_vector)
        # update searchData dict
        newsArticle["score"] = round(similarity * 100, 0)
