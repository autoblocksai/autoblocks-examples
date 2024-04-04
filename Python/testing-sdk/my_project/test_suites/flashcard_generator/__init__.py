from typing import List

from autoblocks.api.client import AutoblocksAPIClient
from autoblocks.testing.run import run_test_suite

from my_project.tasks.flashcard_generator import Flashcard
from my_project.tasks.flashcard_generator import gen_flashcards_from_notes
from my_project.test_suites.flashcard_generator.evaluators import IsProfessionalTone
from my_project.test_suites.flashcard_generator.evaluators import IsSupportedByNotes
from my_project.test_suites.flashcard_generator.test_cases import TestCase
from my_project.test_suites.flashcard_generator.test_cases import gen_test_cases


def test_fn(test_case: TestCase) -> List[Flashcard]:
    return gen_flashcards_from_notes(test_case.notes)


def run():
    run_test_suite(
        id="flashcard-generator",
        test_cases=gen_test_cases(),
        evaluators=[
            IsSupportedByNotes(),
            IsProfessionalTone(),
        ],
        fn=test_fn,
        max_test_case_concurrency=5,
    )


def run_with_managed_test_cases():
    # Instantiate API client
    client = AutoblocksAPIClient()

    # Fetch test cases
    test_cases_response = client.get_test_cases(test_suite_id="flashcard-generator")

    # Build test cases array
    test_cases = [
        TestCase(**test_case.body) for test_case in test_cases_response.test_cases
    ]

    # Run test suite with managed test cases
    run_test_suite(
        id="flashcard-generator-managed",
        test_cases=test_cases,
        evaluators=[
            IsSupportedByNotes(),
            IsProfessionalTone(),
        ],
        fn=test_fn,
        max_test_case_concurrency=5,
    )
