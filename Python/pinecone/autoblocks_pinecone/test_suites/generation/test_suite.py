from autoblocks.testing.run import run_test_suite
from autoblocks_pinecone.app import generate_personalized_treatment_plan
from autoblocks_pinecone.test_suites.generation.evaluators import Comprehensiveness
from autoblocks_pinecone.test_suites.generation.evaluators import Faithfulness
from autoblocks_pinecone.test_suites.generation.test_cases import TestCase
from autoblocks_pinecone.test_suites.generation.test_cases import gen_test_cases


def test_fn(test_case: TestCase) -> str:
    return generate_personalized_treatment_plan(
        existing_treatment_plan=test_case.existing_treatment_plan,
        medical_records=test_case.medical_records,
    )


def run_test():
    run_test_suite(
        id="health-copilot-generation",
        test_cases=gen_test_cases(),
        evaluators=[Comprehensiveness(), Faithfulness()],
        fn=test_fn,
    )
