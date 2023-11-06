import os
import time
import traceback
import uuid
from typing import Optional

import dotenv
import openai
from autoblocks.tracer import AutoblocksTracer

dotenv.load_dotenv(".env")

openai.api_key = os.environ["OPENAI_API_KEY"]

tracer = AutoblocksTracer(
    os.environ["AUTOBLOCKS_INGESTION_KEY"],
    properties=dict(provider="openai"),
)


def run(content: str, trace_id: Optional[str] = None):
    # Set the trace ID to the one given, or fall back to a random UUID.
    # When we call this function from the test suite we will pass in a
    # trace_id so that it is stable across replay runs, but in production
    # we'll only pass in the content, like run(content), so that we generate
    # a random trace_id while in production.
    tracer.set_trace_id(trace_id or str(uuid.uuid4()))

    # Use a span ID to group together the request + response/error events
    span_id = str(uuid.uuid4())

    params = dict(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. "
                + "You answer questions about a software product named Acme. "
                + "Your answers should be in a friendly tone and include a bulleted or numbered list where appopriate. "
                + "You should also include a link to the relevant page in the Acme documentation.",
            },
            {"role": "user", "content": content},
        ],
        temperature=0.3,
    )

    tracer.send_event("ai.request", span_id=span_id, properties=params)

    try:
        start_time = time.time()
        response = openai.ChatCompletion.create(**params)
        tracer.send_event(
            "ai.response",
            span_id=span_id,
            properties=dict(
                response=response,
                latency_ms=(time.time() - start_time) * 1000,
            ),
        )
        return response.choices[0].message
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
        raise error


if __name__ == "__main__":
    # Simulate running the `run` function in a production setting,
    # i.e. without passing in a trace_id from a test case (one will
    # be auto-generated).
    run(content="How do I sign up?")
