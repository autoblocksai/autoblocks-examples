from autoblocks.testing.models import BaseTestEvaluator
from autoblocks.testing.models import Evaluation
from autoblocks.testing.models import Threshold
from autoblocks_pinecone.data.search import MedicalRecord
from autoblocks_pinecone.test_suites.retrieval.test_cases import TestCase
from openai import AsyncOpenAI
from autoblocks_pinecone import prompt_managers
import json

openai_client = AsyncOpenAI()


class Relevancy(BaseTestEvaluator):
    id = "relevancy"
    max_concurrency = 5
    threshold = Threshold(gte=0.8)

    async def evaluate_test_case(
        self, test_case: TestCase, output: list[MedicalRecord]
    ) -> Evaluation:
        scores = []
        for record in output:
            with prompt_managers.eval_relevancy.exec() as prompt:
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
                                treatment_plan=test_case.treatment_plan,
                                medical_record=record.text,
                            ),
                        },
                    ],
                    n=1,
                    response_format=dict(type="json_object"),
                )
                response = await openai_client.chat.completions.create(**params)
                parsed_response = json.loads(
                    response.choices[0].message.content.strip()
                )
                scores.append(parsed_response["score"])

        mean_score = sum(scores) / len(scores) if scores else 0

        return Evaluation(score=mean_score, threshold=self.threshold)
