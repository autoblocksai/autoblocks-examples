from autoblocks.testing.run import run_test_suite
from autoblocks_pinecone.app import run
from autoblocks_pinecone.test_suites.e2e.evaluators import Correctness
from autoblocks_pinecone.test_suites.e2e.test_cases import TestCase
from autoblocks_pinecone.test_suites.e2e.test_cases import gen_test_cases


def test_fn(test_case: TestCase) -> str:
    return run(
        transcript=test_case.transcript,
    )


def run_test():
    run_test_suite(
        id="health-copilot-e2e",
        test_cases=gen_test_cases(),
        evaluators=[Correctness()],
        fn=test_fn,
    )
