import os

from autoblocks_pinecone.data.model import MedicalRecord
from autoblocks_pinecone.data.constants import namespace
from autoblocks_pinecone.data.constants import cosine_index_name
from autoblocks_pinecone.data.constants import euclidean_index_name
from autoblocks_pinecone.data.constants import dotproduct_index_name
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec

openai_client = OpenAI()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])


def read_files_from_directory():
    directory = (
        os.getcwd() + "/autoblocks_pinecone/data/medical_records_raw_files/patient-1"
    )
    file_data_list = []
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):  # Check if it is a file
            with open(filepath, "r", encoding="utf-8") as file:
                contents = file.read()
                # Create an instance of MedicalRecord and append it to the list
                file_data = MedicalRecord(
                    id=filename.replace(".txt", ""), text=contents
                )
                file_data_list.append(file_data)
    return file_data_list


sample_medical_records = read_files_from_directory()


def load_data():
    pc.create_index(
        name=cosine_index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    pc.create_index(
        name=cosine_index_name,
        dimension=1536,
        metric="euclidean",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    pc.create_index(
        name=dotproduct_index_name,
        dimension=1536,
        metric="dotproduct",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    cosine_index = pc.Index(cosine_index_name)
    euclidean_index = pc.Index(euclidean_index_name)
    dotproduct_index = pc.Index(dotproduct_index_name)
    embeddings = []
    for record in sample_medical_records:
        res = openai_client.embeddings.create(
            input=record.text, model="text-embedding-3-small"
        )
        embeddings.append({"id": record.id, "vectors": res.data[0].embedding})

    cosine_index.upsert(
        vectors=[{"id": emb["id"], "values": emb["vectors"]} for emb in embeddings],
        namespace=namespace,
    )
    euclidean_index.upsert(
        vectors=[{"id": emb["id"], "values": emb["vectors"]} for emb in embeddings],
        namespace=namespace,
    )
    dotproduct_index.upsert(
        vectors=[{"id": emb["id"], "values": emb["vectors"]} for emb in embeddings],
        namespace=namespace,
    )
