import os
import time
import traceback
import uuid

import dotenv
from autoblocks.tracer import AutoblocksTracer
from openai import OpenAI

dotenv.load_dotenv(".env")

client = OpenAI()

params = dict(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. You answer questions about a software product named Acme.",
        },
        {"role": "user", "content": "How do I sign up?"},
    ],
    temperature=0.7,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    n=1,
)

tracer = AutoblocksTracer(
    os.environ["AUTOBLOCKS_INGESTION_KEY"],
    trace_id=str(uuid.uuid4()),
    properties=dict(provider="openai"),
)


def main():
    # Use a span ID to group together the request + response/error events
    span_id = str(uuid.uuid4())

    tracer.send_event("ai.request", span_id=span_id, properties=params)
    try:
        start_time = time.time()
        completion = client.chat.completions.create(**params)
        tracer.send_event(
            "ai.response",
            span_id=span_id,
            properties=dict(
                # OpenAI v1 returns pydantic models, which have a model_dump_json
                # method for converting to JSON.
                response=completion.model_dump_json(),
                latency=(time.time() - start_time) * 1000,
            ),
        )
    except Exception as error:
        tracer.send_event(
            "ai.error",
            span_id=span_id,
            properties=dict(
                error=dict(
                    type=type(error).__name__,
                    message=str(error),
                    stacktrace=traceback.format_exc(),
                ),
            ),
        )
        raise

    print(f"View your trace: https://app.autoblocks.ai/explore/trace/{tracer.trace_id}")
