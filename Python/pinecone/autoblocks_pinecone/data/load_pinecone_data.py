import os
from dataclasses import dataclass

from openai import OpenAI
from pinecone import Pinecone

client = OpenAI()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])


@dataclass
class MedicalRecord:
    id: str
    text: str


def read_files_from_directory():
    directory = "autoblocks_pinecone/data/medical_records_raw_files/patient-1"
    file_data_list = []
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):  # Check if it is a file
            with open(filepath, "r", encoding="utf-8") as file:
                contents = file.read()
                # Create an instance of FileData and append it to the list
                file_data = MedicalRecord(
                    id=filename.replace(".txt", ""), text=contents
                )
                file_data_list.append(file_data)
    return file_data_list


sample_medical_records = read_files_from_directory()


def load_data():
    # pc.create_index(
    #     name="autoblocks-pinecone-example-index-cosine",
    #     dimension=1536,  # Replace with your model dimensions
    #     metric="cosine",  # Replace with your model metric
    #     spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    # )
    # pc.create_index(
    #     name="autoblocks-pinecone-example-index-euclidean",
    #     dimension=1536,  # Replace with your model dimensions
    #     metric="euclidean",  # Replace with your model metric
    #     spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    # )
    # pc.create_index(
    #     name="autoblocks-pinecone-example-index-dotproduct",
    #     dimension=1536,  # Replace with your model dimensions
    #     metric="dotproduct",  # Replace with your model metric
    #     spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    # )
    cosine_index = pc.Index("autoblocks-pinecone-example-index-cosine")
    euclidean_index = pc.Index("autoblocks-pinecone-example-index-euclidean")
    dotproduct_index = pc.Index("autoblocks-pinecone-example-index-dotproduct")
    embeddings = []
    for record in sample_medical_records:
        res = client.embeddings.create(
            input=record.text, model="text-embedding-3-small"
        )
        embeddings.append({"id": record.id, "vectors": res.data[0].embedding})

    for i in range(1, 21):
        namespace = f"patient-{i}"
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
