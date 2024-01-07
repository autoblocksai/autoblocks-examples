import random

from myapp.tracer import tracer

# Mock data simulating a set of documents
DOCUMENTS = [
    {
        "id": 1,
        "content": "Document about space exploration, covering Mars missions, satellites, and astronaut training.",
    },
    {
        "id": 2,
        "content": "Article on renewable energy, focusing on solar panels, wind turbines, and sustainable practices.",
    },
    {
        "id": 3,
        "content": "Blog post about healthy eating, discussing diets, nutrition, and meal planning.",
    },
    {
        "id": 4,
        "content": "News report on advances in AI, with insights into machine learning, neural networks, and robotics.",
    },
    {
        "id": 5,
        "content": "Guide to gardening, with tips on plant care, landscaping, and organic farming.",
    },
]


def retrieve_documents(user_input: str, n: int):
    """
    Simulates the retrieval of the most relevant documents based on the user's input.
    This is a mock function; in a real scenario, this would involve more complex logic like Vector DBs.

    Parameters:
    user_input (str): The user's input or query.
    n (int): Number of documents to retrieve.

    Returns:
    list: A list of the most 'relevant' documents (mocked for this example).
    """
    # Mock logic for document retrieval (random selection for this example)
    with tracer().start_span():
        tracer().send_event(
            "ai.rag.request",
            properties=dict(
                user_input=user_input,
                n=n,
            ),
        )
        documents = random.sample(DOCUMENTS, min(n, len(DOCUMENTS)))
        tracer().send_event(
            "ai.rag.retrieved",
            properties=dict(
                documents=documents,
            ),
        )
        return documents


def augmented_generation(user_input: str, n: int):
    """
    Demonstrates a retrieval-augmented generation process.

    Parameters:
    user_input (str): The user's input or query.
    n (int): Number of documents to retrieve.

    Returns:
    str: A simulated response from an LLM, considering the retrieved documents.
    """

    # Retrieve relevant documents
    relevant_docs = retrieve_documents(user_input, n=n)
    context = "\n".join(d["content"] for d in relevant_docs)

    with tracer().start_span():
        prompt = f"""Answer the user's question using the given context:
Question: {user_input}
Context: {context}
"""
        tracer().send_event(
            "ai.llm.request",
            properties=dict(
                prompt=prompt,
            ),
        )

        response = "Mock LLM Response"

        tracer().send_event(
            "ai.llm.response",
            properties=dict(
                response=response,
            ),
        )

        return response
