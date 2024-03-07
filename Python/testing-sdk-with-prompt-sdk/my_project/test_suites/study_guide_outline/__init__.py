from autoblocks.testing.run import run_test_suite

from my_project.tasks.study_guide_outline import gen_study_guide_outline
from my_project.test_suites.study_guide_outline.evaluators import Formatting
from my_project.test_suites.study_guide_outline.evaluators import HasSubstrings
from my_project.test_suites.study_guide_outline.evaluators import NumCategories
from my_project.test_suites.study_guide_outline.test_cases import TestCase
from my_project.test_suites.study_guide_outline.test_cases import gen_test_cases


def test_fn(test_case: TestCase) -> str:
    return gen_study_guide_outline(test_case.topic)


def run():
    run_test_suite(
        id="study-guide-outline",
        test_cases=gen_test_cases(),
        evaluators=[
            Formatting(),
            NumCategories(),
            HasSubstrings(),
        ],
        fn=test_fn,
        max_test_case_concurrency=5,
    )
