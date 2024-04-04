from typing import List

from autoblocks.testing.run import run_test_suite
from autoblocks.api.client import AutoblocksAPIClient

from my_project.tasks.flashcard_generator import Flashcard
from my_project.tasks.flashcard_generator import gen_flashcards_from_notes

from my_project.test_suites.flashcard_generator.evaluators import IsProfessionalTone
from my_project.test_suites.flashcard_generator.evaluators import IsSupportedByNotes
from my_project.test_suites.flashcard_generator.test_cases import TestCase

TEST_SUITE_ID = "flashcard-generator-managed"


def test_fn(test_case: TestCase) -> List[Flashcard]:
    return gen_flashcards_from_notes(test_case.notes)


def run():
    in_code_test_cases = [TestCase(notes="Initial test case")]
    managed_test_cases = []

    try:
        client = AutoblocksAPIClient()
        test_cases_response = client.get_test_cases(test_suite_id=TEST_SUITE_ID)
        managed_test_cases = [
            TestCase(**test_case.body) for test_case in test_cases_response.test_cases
        ]
    except:
        print("Test suite does not exist yet.")

    # Run test suite with managed test cases
    run_test_suite(
        id=TEST_SUITE_ID,
        test_cases=managed_test_cases + in_code_test_cases,
        evaluators=[
            IsSupportedByNotes(),
            IsProfessionalTone(),
        ],
        fn=test_fn,
        max_test_case_concurrency=5,
    )
