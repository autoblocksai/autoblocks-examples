from autoblocks.tracer import init_auto_tracer
from autoblocks.tracer import trace_app
from autoblocks.testing.run import start_run, end_run
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from openai import AsyncOpenAI
import asyncio

init_auto_tracer()
OpenAIInstrumentor().instrument()

openai = AsyncOpenAI()


async def sub_generate(text: str):
    response = await openai.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": text}]
    )
    return response


@trace_app("<app_id>", "<environment>")
async def generate():
    response = await openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello, how are you doing?"}],
    )
    return await sub_generate(response.choices[0].message.content)


def run():
    asyncio.run(generate())
