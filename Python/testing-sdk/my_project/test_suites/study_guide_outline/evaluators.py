from typing import List

from autoblocks.testing.models import BaseTestEvaluator
from autoblocks.testing.models import Evaluation
from autoblocks.testing.models import Threshold

from my_project.evaluators.has_substrings import BaseHasSubstrings
from my_project.test_suites.study_guide_outline.test_cases import TestCase


class Formatting(BaseTestEvaluator):
    id = "formatting"

    @staticmethod
    def score(output: str) -> int:
        """
        Every line should either be blank or start with "* " or "  - "
        """
        for line in output.splitlines():
            if not (line.strip() == "" or line.startswith(("* ", "  - "))):
                return 0
        return 1

    def evaluate_test_case(self, test_case: TestCase, output: str) -> Evaluation:
        return Evaluation(score=self.score(output), threshold=Threshold(gte=1))


class NumCategories(BaseTestEvaluator):
    id = "num-categories"

    min_categories: int = 5
    max_categories: int = 10

    def score(self, output: str) -> int:
        return int(self.min_categories <= output.count("* ") <= self.max_categories)

    def evaluate_test_case(self, test_case: TestCase, output: str) -> Evaluation:
        return Evaluation(score=self.score(output), threshold=Threshold(gte=1))


class HasSubstrings(BaseHasSubstrings):
    def expected_substrings(self, test_case: TestCase) -> List[str]:
        return test_case.expected_substrings
