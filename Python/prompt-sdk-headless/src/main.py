import uuid

import dotenv
from autoblocks.tracer import AutoblocksTracer
from autoblocks.vendor.openai import serialize_completion
from openai import OpenAI

from src.prompts import TextSummarizationMinorVersion
from src.prompts import TextSummarizationPromptManager

dotenv.load_dotenv(".env")

openai = OpenAI()
manager = TextSummarizationPromptManager(TextSummarizationMinorVersion.v0)


def main():
    with manager.exec() as prompt:
        tracer = AutoblocksTracer(trace_id=str(uuid.uuid4()))

        params = dict(
            model=prompt.params.model,
            temperature=prompt.params.temperature,
            messages=[
                dict(
                    role="system",
                    content=prompt.render.system(
                        language_requirement=prompt.render.util_language(
                            lang="Spanish",
                        ),
                        tone_requirement=prompt.render.util_tone(
                            tone="formal",
                        ),
                    ),
                ),
                dict(
                    role="user",
                    content="\n\n".join(
                        [
                            prompt.render.user(document=document)
                            for document in ("doc1", "doc2", "etc")
                        ],
                    ),
                ),
            ],
        )

        tracer.send_event(
            "ai.request",
            properties=params,
        )

        response = openai.chat.completions.create(**params)

        tracer.send_event(
            "ai.response",
            properties=dict(
                response=serialize_completion(response),
                promptTracking=prompt.track(),
            ),
        )

        print(response)
