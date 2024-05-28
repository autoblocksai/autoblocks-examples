import os

from openai import OpenAI
from pinecone import Pinecone

from autoblocks_pinecone.data.load_pinecone_data import MedicalRecord
from autoblocks_pinecone.data.load_pinecone_data import sample_medical_records
from autoblocks_pinecone.config import config

client = OpenAI()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])


def search_for_query(query: str) -> list[MedicalRecord]:
    res = client.embeddings.create(input=query, model="text-embedding-3-small")

    index = pc.Index("autoblocks-pinecone-example-index-dotproduct")
    if config.value.similarity_metric == "cosine":
        index = pc.Index("autoblocks-pinecone-example-index-cosine")
    elif config.value.similarity_metric == "euclidean":
        index = pc.Index("autoblocks-pinecone-example-index-euclidean")

    query_res = index.query(
        vector=res.data[0].embedding, top_k=config.value.top_k, namespace="patient-1"
    )
    # Collect IDs from the matches
    ids = [match["id"] for match in query_res["matches"]]

    # Return all records that have an ID in the matches
    return [record for record in sample_medical_records if record.id in ids]


def search_medical_records(plan: str) -> list[MedicalRecord]:
    return search_for_query(plan)
