import json
import os
import time
import traceback
import uuid

from openai import AsyncOpenAI

from autoblocks.tracer import AutoblocksTracer
from autoblocks_pinecone import prompt_managers
from autoblocks_pinecone.data.load_pinecone_data import MedicalRecord
from autoblocks_pinecone.data.medical_records import search_medical_records

client = AsyncOpenAI()

tracer = AutoblocksTracer(
    os.environ["AUTOBLOCKS_INGESTION_KEY"],
    trace_id=str(uuid.uuid4()),
    properties=dict(provider="openai"),
)


async def generate_plan_from_transcript(transcript: str) -> str:
    with prompt_managers.gen_treatment_plan.exec() as prompt:
        params = dict(
            model=prompt.params.model,
            messages=[
                {
                    "role": "system",
                    "content": prompt.render.system(),
                },
                {"role": "user", "content": prompt.render.user(transcript=transcript)},
            ],
            temperature=prompt.params.temperature,
            n=1,
        )
        span_id = str(uuid.uuid4())
        tracer.send_event("ai.request", span_id=span_id, properties=params)
        try:
            start_time = time.time()
            completion = await client.chat.completions.create(**params)
            tracer.send_event(
                "ai.response",
                span_id=span_id,
                prompt_tracking=prompt.track(),
                properties=dict(
                    # OpenAI v1 returns pydantic models, which have a model_dump
                    # method for converting to a dictionary.
                    response=completion.model_dump(),
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

    return completion.choices[0].message.content


async def generate_personalized_treatment_plan(
    existing_treatment_plan: str, medical_records: list[MedicalRecord]
) -> str:
    with prompt_managers.gen_personalized_treatment_plan.exec() as prompt:
        params = dict(
            model=prompt.params.model,
            messages=[
                {
                    "role": "system",
                    "content": prompt.render.system(),
                },
                {
                    "role": "user",
                    "content": prompt.render.user(
                        existing_treatment_plan=existing_treatment_plan,
                        medical_records="\n".join(
                            [record.text for record in medical_records]
                        ),
                    ),
                },
            ],
            temperature=prompt.params.temperature,
            n=1,
        )
        span_id = str(uuid.uuid4())
        tracer.send_event("ai.request", span_id=span_id, properties=params)
        try:
            start_time = time.time()
            completion = await client.chat.completions.create(**params)
            tracer.send_event(
                "ai.response",
                span_id=span_id,
                prompt_tracking=prompt.track(),
                properties=dict(
                    # OpenAI v1 returns pydantic models, which have a model_dump
                    # method for converting to a dictionary.
                    response=completion.model_dump(),
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

    return completion.choices[0].message.content


def retrieve_relevant_medical_records(treatment_plan: str) -> list[MedicalRecord]:
    return search_medical_records(plan=treatment_plan)


async def run(transcript: str) -> str:
    unpersonalized_plan = generate_plan_from_transcript(transcript=transcript)
    medical_records = retrieve_relevant_medical_records(
        treatment_plan=unpersonalized_plan
    )
    personalized_treatment_plan = generate_personalized_treatment_plan(
        existing_treatment_plan=unpersonalized_plan, medical_records=medical_records
    )
    return personalized_treatment_plan
