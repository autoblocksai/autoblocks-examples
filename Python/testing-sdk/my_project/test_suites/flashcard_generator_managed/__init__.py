from typing import List

from autoblocks.testing.run import run_test_suite

from my_project.tasks.flashcard_generator import Flashcard
from my_project.tasks.flashcard_generator import gen_flashcards_from_notes

from my_project.test_suites.flashcard_generator.evaluators import IsProfessionalTone
from my_project.test_suites.flashcard_generator.evaluators import IsSupportedByNotes
from my_project.test_suites.flashcard_generator.test_cases import TestCase


def test_fn(test_case: TestCase) -> List[Flashcard]:
    return gen_flashcards_from_notes(test_case.notes)


def run():
    # Uncomment following block to start using managed test cases
    """client = AutoblocksAPIClient()
    test_cases_response = client.get_test_cases(test_suite_id="flashcard-generator-managed")
    test_cases = [
        TestCase(**test_case.body) for test_case in test_cases_response.test_cases
    ]"""

    # Comment this line once you have created test cases for
    # this test suite
    test_cases = [TestCase(notes="Initial test case")]

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
