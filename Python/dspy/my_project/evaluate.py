from autoblocks.testing.run import run_test_suite
from my_project.run import run
from autoblocks.testing.models import BaseTestEvaluator
from dspy.primitives import Prediction
from dataclasses import dataclass
from autoblocks.testing.models import BaseTestCase

from autoblocks.testing.util import md5
from autoblocks.testing.models import Evaluation
from autoblocks.testing.models import Threshold
from my_project.datasets import devset
from my_project.datasets import metric


@dataclass
class Output:
    answer: str
    rationale: str


@dataclass
class TestCase(BaseTestCase):
    question: str
    answer: str

    def hash(self) -> str:
        """
        This hash serves as a unique identifier for a test case throughout its lifetime.
        """
        return md5(f"{self.question}")


class Correctness(BaseTestEvaluator):
    id = "correctness"
    threshold = Threshold(gte=1)

    async def evaluate_test_case(
        self, test_case: TestCase, output: Output
    ) -> Evaluation:
        metric_result = metric(gold=test_case, pred=Prediction(answer=output))
        return Evaluation(score=1 if metric_result else 0, threshold=self.threshold)


def test_fn(test_case: TestCase) -> Output:
    prediction = run(question=test_case.question)
    return Output(answer=prediction.answer, rationale=prediction.rationale)


def run_test():
    run_test_suite(
        id="dspy",
        test_cases=[
            TestCase(question=item["question"], answer=item["answer"])
            for item in devset
        ],
        evaluators=[Correctness()],
        fn=test_fn,
    )
