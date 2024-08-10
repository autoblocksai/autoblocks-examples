import json

from openai import AsyncOpenAI

from autoblocks.testing.models import BaseTestEvaluator
from autoblocks.testing.models import Evaluation
from autoblocks.testing.models import Threshold
from autoblocks_pinecone import prompt_managers
from autoblocks_pinecone.test_suites.e2e.test_cases import TestCase

openai_client = AsyncOpenAI()


class Correctness(BaseTestEvaluator):
    id = "correctness"
    max_concurrency = 5
    threshold = Threshold(gte=0.5)

    async def evaluate_test_case(self, test_case: TestCase, output: str) -> Evaluation:
        with prompt_managers.eval_correctness.exec() as prompt:
            params = dict(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": prompt.render.system(),
                    },
                    {
                        "role": "user",
                        "content": prompt.render.user(
                            transcript=test_case.transcript,
                            treatment_plan=output,
                        ),
                    },
                ],
                n=1,
                response_format=dict(type="json_object"),
            )
            response = await openai_client.chat.completions.create(**params)
            parsed_response = json.loads(response.choices[0].message.content.strip())
            score = parsed_response["score"]
            reason = parsed_response["reason"]
            return Evaluation(
                score=score, threshold=self.threshold, metadata=dict(reason=reason)
            )
