import asyncio
import os

import httpx

prompts = [
    dict(
        id="eval-comprehensiveness",
        params=dict(
            model="gpt-4-turbo",
        ),
        templates=[
            dict(
                id="system",
                template="""You are an expert doctor. Your job is to take a given personalized treatment plan and evaluate how comprehensive it is compared to the given medical records and existing treatment plan.
You evaluate as a score between 0 and 1. The number can be any decimal number between 0 and 1.
If there is any missing information, you should give a score below 0.5. If it is comprehensive, the score should be above 0.5.
You should also give a reason for the score.

Output in the following json format:

{
     "score": 0.3,
     "reason": "The output is mostly correct, but it is missing some important details."
}""",
            ),
            dict(
                id="user",
                template="""Existing Treatment Plan: {{ existing_treatment_plan }}

Medical Records: {{ medical_records }}""",
            ),
        ],
    ),
    dict(
        id="eval-correctness",
        params=dict(
            model="gpt-4-turbo",
        ),
        templates=[
            dict(
                id="system",
                template="""You are an expert doctor. Your job is to take a given treatment plan and evaluate how correct it is based on the transcript provided
You evaluate as a score between 0 and 1. The number can be any decimal number between 0 and 1.
If there is any false, missing, or hallucinated information, you should give a score below 0.5. If everything is accurate, the score should be above 0.5.
You should also give a reason for the score.

Output in the following json format:

{
     "score": 0.3,
     "reason": "The output is mostly correct, but it is missing some important details."
}""",
            ),
            dict(
                id="user",
                template="""Transcript: {{ transcript }}

Treatment Plan: {{ treatment_plan }}""",
            ),
        ],
    ),
    dict(
        id="eval-faithfulness",
        params=dict(
            model="gpt-4-turbo",
        ),
        templates=[
            dict(
                id="system",
                template="""You are an expert doctor. Your job is to take a given personalized treatment plan and evaluate how faithful it is to the given medical records and existing treatment plan.
You evaluate as a score between 0 and 1. The number can be any decimal number between 0 and 1.
If there is any false or hallucinated information, you should give a score below 0.5. If everything is accurate, the score should be above 0.5.
You should also give a reason for the score.

Output in the following json format:

{
     "score": 0.3,
     "reason": "The output is mostly correct, but it is missing some important details."
}""",
            ),
            dict(
                id="user",
                template="""Existing Treatment Plan: {{ existing_treatment_plan }}

Medical Records: {{ medical_records }}

Generated Plan: {{ generated_plan }}""",
            ),
        ],
    ),
    dict(
        id="eval-relevancy",
        params=dict(
            model="gpt-4-turbo",
        ),
        templates=[
            dict(
                id="system",
                template="""You are an expert doctor. Your job is to take a given treatment plan determine how relevant the medical record is to being able to personalize it.
Not all medical records are relevant for certain treatment plans.
You evaluate as a score between 0 and 1. The number can be any decimal number between 0 and 1.
If it is not relevant, you should give a score below 0.5. If everything is relevant and needed to determine the final treatment plan, the score should be above 0.5.

Output in the following json format:

{
     "score": 0.3,
}""",
            ),
            dict(
                id="user",
                template="""Treatment Plan: {{ treatment_plan }}

Medical Record: {{ medical_record }}""",
            ),
        ],
    ),
    dict(
        id="gen-personalized-treatment-plan",
        params=dict(
            model="gpt-3.5-turbo",
        ),
        templates=[
            dict(
                id="system",
                template="""You are a world class doctor. You personalize a treatment plan using information from the patients medical records. Only return the treatment plan and be detailed.""",
            ),
            dict(
                id="user",
                template="""Existing Treatment Plan: {{ existing_treatment_plan }}

Medical Records: {{ medical_records }}""",
            ),
        ],
    ),
    dict(
        id="gen-treatment-plan",
        params=dict(
            model="gpt-4p",
        ),
        templates=[
            dict(
                id="system",
                template="""You are a world class doctor. You produce a plan for a patient based on a transcript of a conversation between a doctor and a patient. Only return the treatment plan and be detailed.""",
            ),
            dict(
                id="user",
                template="""{{ transcript }}""",
            ),
        ],
    ),
]


async def create_prompts():
    async with httpx.AsyncClient() as client:
        promises = []
        for prompt in prompts:
            response = client.post(
                "https://api.autoblocks.ai/prompts",
                json=prompt,
                headers={
                    "Authorization": f"Bearer {os.environ['AUTOBLOCKS_API_KEY']}",
                },
            )
            promises.append(response)

        for response in await asyncio.gather(*promises):
            print(f"Prompt created: {response.json()}")


def main():
    asyncio.run(create_prompts())
