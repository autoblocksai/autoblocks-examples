from typing import List

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
