import os

from openai import OpenAI
from pinecone import Pinecone

from autoblocks_pinecone.data.model import MedicalRecord
from autoblocks_pinecone.data.load_pinecone_data import sample_medical_records
from autoblocks_pinecone.data.constants import namespace
from autoblocks_pinecone.data.constants import cosine_index_name
from autoblocks_pinecone.data.constants import euclidean_index_name
from autoblocks_pinecone.data.constants import dotproduct_index_name
from autoblocks_pinecone.config import config

openai_client = OpenAI()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])


def search_medical_records(plan: str) -> list[MedicalRecord]:
    res = openai_client.embeddings.create(input=plan, model="text-embedding-3-small")

    index = pc.Index(dotproduct_index_name)
    if config.value.similarity_metric == "cosine":
        index = pc.Index(cosine_index_name)
    elif config.value.similarity_metric == "euclidean":
        index = pc.Index(euclidean_index_name)

    query_res = index.query(
        vector=res.data[0].embedding, top_k=config.value.top_k, namespace=namespace
    )
    # Collect IDs from the matches
    ids = [match["id"] for match in query_res["matches"]]

    # Return all records that have an ID in the matches
    return [record for record in sample_medical_records if record.id in ids]
