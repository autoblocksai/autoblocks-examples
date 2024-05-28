from autoblocks_pinecone.test_suites.generation.test_suite import (
    run_test as run_generation_test,
)
from autoblocks_pinecone.test_suites.retrieval.test_suite import (
    run_test as run_retrieval_test,
)
from autoblocks_pinecone.test_suites.e2e.test_suite import run_test as run_e2e_test


def run_tests():
    run_retrieval_test()
    run_generation_test()
    run_e2e_test()
