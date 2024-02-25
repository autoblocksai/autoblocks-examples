import os
import uuid

import dotenv
from autoblocks.tracer import AutoblocksTracer
from openai import OpenAI

dotenv.load_dotenv(".env")

client = OpenAI()

tracer = AutoblocksTracer(
    os.environ["AUTOBLOCKS_INGESTION_KEY"],
    trace_id=str(uuid.uuid4()),
    properties=dict(provider="openai"),
)


def main():

    assistant_create_params = dict(name="Math Tutor",
        instructions="You are a personal math tutor. Write and run code to answer math questions.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo-preview")
    tracer.send_event('ai.assistant.create', properties=assistant_create_params)
    assistant = client.beta.assistants.create(**assistant_create_params)
    tracer.update_properties(dict(assistant_id=assistant.id, model=assistant.model))
    tracer.send_event('ai.assistant.created')

    tracer.send_event('ai.assistant.thread.create')
    thread = client.beta.threads.create()
    tracer.update_properties(dict(thread_id=thread.id))
    tracer.send_event('ai.assistant.thread.created')

    message_create_params = dict(thread_id=thread.id,
        role="user",
        content="I need to solve the equation `3x + 11 = 14`. Can you help me?")
    tracer.send_event('ai.assistant.thread.message.create', properties=message_create_params)
    message = client.beta.threads.messages.create(
        **message_create_params
    )
    tracer.send_event('ai.assistant.thread.message.created', properties=dict(message_id=message.id))

    run_params = dict(thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="You are a personal math tutor. Write and run code to answer math questions.")
    tracer.send_event('ai.assistant.thread.run.create', properties=run_params)
    run = client.beta.threads.runs.create(
        **run_params
    )
    tracer.update_properties(dict(run_id=run.id))
    tracer.send_event('ai.assistant.thread.run.created')

    run_completed = False

    while not run_completed:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run.status == "completed":
            run_completed = True

    run_steps = client.beta.threads.runs.steps.list(
        thread_id=thread.id,
        run_id=run.id
    )

    for step in run_steps:
        tracer.send_event(f'ai.assistant.thread.run.step.{step.type}', properties=dict(run_id=step.id, parent_run_id=step.run_id))

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    tracer.send_event('ai.assistant.thread.run.completed', properties=dict(response=messages.model_dump_json()))

    print(f"View your trace: https://app.autoblocks.ai/explore/trace/{tracer.trace_id}")

