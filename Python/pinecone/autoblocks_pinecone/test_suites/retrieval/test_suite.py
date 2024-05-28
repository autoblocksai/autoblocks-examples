from autoblocks.testing.run import run_test_suite
from autoblocks_pinecone.app import retrieve_relevant_medical_records
from autoblocks_pinecone.data.medical_records import MedicalRecord
from autoblocks_pinecone.test_suites.retrieval.evaluators import Relevancy
from autoblocks_pinecone.test_suites.retrieval.test_cases import TestCase
from autoblocks_pinecone.test_suites.retrieval.test_cases import gen_test_cases


def test_fn(test_case: TestCase) -> list[MedicalRecord]:
    return retrieve_relevant_medical_records(treatment_plan=test_case.treatment_plan)


def run_test():
    run_test_suite(
        id="health-copilot-retrieval",
        test_cases=gen_test_cases(),
        evaluators=[Relevancy()],
        fn=test_fn,
    )
