from autoblocks.testing.run import run_test_suite
from src.evaluators import ProfanityFree

from src.main import run
from src.test_cases import TestCase
from src.test_cases import gen_test_cases


def test_fn(test_case: TestCase) -> str:
    return run(question=test_case.question)


def run_test():
    run_test_suite(
        id="guardrails-ai",
        test_cases=gen_test_cases(),
        evaluators=[ProfanityFree()],
        fn=test_fn,
    )
