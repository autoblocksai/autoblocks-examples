import json
from typing import Any
from typing import Optional

from autoblocks.testing.models import BaseEvaluator
from autoblocks.testing.models import BaseTestCase
from autoblocks.testing.models import Evaluation
from autoblocks.testing.models import Threshold


class IsValidJson(BaseEvaluator):
    id = "is-valid-json"

    """
    Can be overriden by subclassing and changing this threshold. For example:

    class MyEvaluator(IsValidJson):
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

    def output_as_str(self, output: Any) -> str:
        """
        Can be overriden by the subclass to change how the output is converted to a string.

        For example:

        class MyEvaluator(IsValidJson):
            def output_as_str(self, output: SomeCustomOutputType) -> str:
                return output.as_json()
        """
        return str(output)

    def evaluate(self, test_case: BaseTestCase, output: Any) -> Evaluation:
        try:
            json.loads(self.output_as_str(output))
            return Evaluation(score=1, threshold=self.threshold)
        except json.JSONDecodeError:
            return Evaluation(score=0, threshold=self.threshold)
