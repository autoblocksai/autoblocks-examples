import os
import time
import traceback
import uuid

import dotenv
import openai
from autoblocks.tracer import AutoblocksTracer

dotenv.load_dotenv(".env")

openai.api_key = os.environ["OPENAI_API_KEY"]

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. You answer questions about a software product named Acme."
    },
    {
        "role": "user",
        "content": "How do I sign up?"
    }
]
request_params = dict(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.7,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    n=1
)

tracer = AutoblocksTracer(
    os.environ["AUTOBLOCKS_INGESTION_KEY"],
    trace_id=str(uuid.uuid4()),
    properties=dict(
        provider="openai"
    )
)


def main():
    tracer.send_event(
        "ai.request",
        properties=request_params
    )
    try:
        start_time = time.time()
        openai_response = openai.ChatCompletion.create(**request_params)
        tracer.send_event(
            "ai.response",
            properties=dict(
                response=openai_response,
                latency=(time.time() - start_time) * 1000,
            )
        )
    except Exception as error:
        tracer.send_event(
            "ai.error",
            properties=dict(
                error=dict(
                    type=type(error).__name__,
                    message=str(error),
                    stacktrace=traceback.format_exc(),
                ),
            )
        )

    print(f"View your trace: https://app.autoblocks.ai/explore/trace/{tracer.trace_id}")


if __name__ == "__main__":
    main()
