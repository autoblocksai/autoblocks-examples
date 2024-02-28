import dataclasses
from typing import List

from autoblocks.testing.models import BaseTestCase

from my_project.test_suites.util import md5


@dataclasses.dataclass()
class TestCase(BaseTestCase):
    topic: str
    expected_substrings: List[str]

    def hash(self) -> str:
        """
        This hash serves as a unique identifier for a test case throughout its lifetime.
        """
        return md5(self.topic)


def gen_test_cases() -> List[TestCase]:
    return [
        TestCase(
            topic="Introduction to Organic Chemistry",
            expected_substrings=[
                "Functional Groups",
            ],
        ),
        TestCase(
            topic="Fundamentals of Calculus",
            expected_substrings=[
                "Derivatives",
                "Differentiation",
            ],
        ),
        TestCase(
            topic="World History: Ancient Civilizations",
            expected_substrings=[
                "Mesopotamia",
                "Egypt",
            ],
        ),
        TestCase(
            topic="Basics of Programming in Python",
            expected_substrings=[
                "Syntax",
                "Variables",
                "Functions",
            ],
        ),
        TestCase(
            topic="Principles of Economics",
            expected_substrings=[
                "Microeconomics",
                "Macroeconomics",
            ],
        ),
    ]
