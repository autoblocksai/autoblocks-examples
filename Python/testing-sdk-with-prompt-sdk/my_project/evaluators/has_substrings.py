import abc
from typing import Any
from typing import List
from typing import Optional

from autoblocks.testing.models import BaseTestEvaluator
from autoblocks.testing.models import BaseTestCase
from autoblocks.testing.models import Evaluation
from autoblocks.testing.models import Threshold


class BaseHasSubstrings(BaseTestEvaluator, abc.ABC):
    id = "has-substrings"

    """
    Can be overriden by subclassing and changing this threshold. For example:

    class MyEvaluator(HasSubstrings):
         threshold = None

    run_test_suite(
        ...
        evaluators=[
            MyEvaluator()
        ],
        ...
    )
    """
    threshold: Optional[Threshold] = Threshold(gte=1)

    @abc.abstractmethod
    def expected_substrings(self, test_case: BaseTestCase) -> List[str]:
        """
        Required to be implemented by the subclass.

        In most cases this will just return the field from the test case that contains the expected substrings,
        but since it's a method, it can be used to calculate the expected substrings in a more complex way
        if appropriate.

        For example:

        class MyEvaluator(HasSubstrings):
            def expected_substrings(self, test_case: MyTestCase) -> List[str]:
                return test_case.expected_substrings
        """
        ...

    def output_as_str(self, output: Any) -> str:
        """
        Can be overriden by the subclass to change how the output is converted to a string.
        """
        return str(output)

    def evaluate_test_case(self, test_case: BaseTestCase, output: Any) -> Evaluation:
        expected_substrings = self.expected_substrings(test_case)
        output_as_str = self.output_as_str(output)

        for substring in expected_substrings:
            if substring not in output_as_str:
                return Evaluation(score=0, threshold=self.threshold)
        return Evaluation(score=1, threshold=self.threshold)
