import os
import uuid

import dotenv
from autoblocks.tracer import AutoblocksTracer
from openai import OpenAI
from src.prompts import OpenaiAssistantsExamplePromptManager
from src.prompts import OpenaiAssistantsExampleMinorVersion

dotenv.load_dotenv(".env")

client = OpenAI()

tracer = AutoblocksTracer(
    os.environ["AUTOBLOCKS_INGESTION_KEY"],
    trace_id=str(uuid.uuid4()),
    properties=dict(provider="openai"),
)

manager = OpenaiAssistantsExamplePromptManager(OpenaiAssistantsExampleMinorVersion.v0)


def main_with_prompt_sdk():
    print("Running example...")

    with manager.exec() as prompt:
        # Create the assistant
        assistant_create_params = dict(
            name="Math Tutor",
            instructions=prompt.render.base_instructions(),
            tools=[{"type": "code_interpreter"}],
            model="gpt-4-turbo-preview",
        )
        tracer.send_event("ai.assistant.create", properties=assistant_create_params)
        assistant = client.beta.assistants.create(**assistant_create_params)
        # All future events will have the assistant_id and model properties
        tracer.update_properties(dict(assistant_id=assistant.id, model=assistant.model))
        tracer.send_event("ai.assistant.created")

        # Create a new thread
        tracer.send_event("ai.assistant.thread.create")
        thread = client.beta.threads.create()
        # All future events will have the thread_id property
        tracer.update_properties(dict(thread_id=thread.id))
        tracer.send_event("ai.assistant.thread.created")

        # Create a user message
        message_create_params = dict(
            thread_id=thread.id,
            role="user",
            content=prompt.render.user(
                question="I need to solve the equation `3x + 11 = 14`. Can you help me?"
            ),
        )
        tracer.send_event(
            "ai.assistant.thread.message.create", properties=message_create_params
        )
        message = client.beta.threads.messages.create(**message_create_params)
        tracer.send_event(
            "ai.assistant.thread.message.created",
            properties=dict(message_id=message.id),
        )

        # Run the assistant
        run_params = dict(
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions=prompt.render.response_instructions(
                name="Jane Doe", account_level="premium"
            ),
        )
        tracer.send_event("ai.assistant.thread.run.create", properties=run_params)
        run = client.beta.threads.runs.create(**run_params)
        # All future events will have the run_id property
        tracer.update_properties(dict(run_id=run.id))
        tracer.send_event("ai.assistant.thread.run.created")

        run_completed = False

        # Wait for run to complete
        while not run_completed:
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            if run.status == "completed":
                run_completed = True

        # Log the steps of the run
        run_steps = client.beta.threads.runs.steps.list(
            thread_id=thread.id, run_id=run.id
        )
        for step in run_steps:
            tracer.send_event(
                f"ai.assistant.thread.run.step.{step.type}",
                span_id=step.id,
                parent_span_id=step.run_id,
            )

        # Log the output of the run
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        tracer.send_event(
            "ai.assistant.thread.run.completed",
            span_id=run.id,
            prompt_tracking=prompt.track(),
            properties=dict(response=messages.data[0].content[0].text.value),
        )

    print(f"View your trace: https://app.autoblocks.ai/explore/trace/{tracer.trace_id}")
