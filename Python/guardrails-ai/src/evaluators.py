from guardrails import Guard
from guardrails.hub import ProfanityFree as ProfanityFreeGuard

from autoblocks.testing.models import BaseEvaluator
from autoblocks.testing.models import Evaluation
from autoblocks.testing.models import Threshold
from autoblocks.testing.models import TracerEvent
from src.test_cases import TestCase


class ProfanityFree(BaseEvaluator):
    id = "profanity-free"
    threshold = Threshold(gte=1)

    def check_profanity(self, text: str) -> Evaluation:
        """
        This currently will run in a background thread and report the result to Autoblocks.
        It can also be updated to throw and block so you can handle the error in your application
        """
        try:
            guard = Guard().use(ProfanityFreeGuard, on_fail="exception")
            guard.parse(llm_output=text)
            return Evaluation(score=1, threshold=self.threshold)
        except Exception as error:
            return Evaluation(
                score=0, threshold=self.threshold, metadata=dict(error=str(error))
            )

    def evaluate_event(self, event: TracerEvent) -> Evaluation | None:
        if event.message == "ai.request":
            # The user input
            return self.check_profanity(event.properties["messages"][1]["content"])
        elif event.message == "ai.response":
            # The AI response
            return self.check_profanity(
                event.properties["response"]["choices"][0]["message"]["content"]
            )
        else:
            return None

    def evaluate_test_case(self, test_case: TestCase, output: str) -> Evaluation:
        return self.check_profanity(text=output)
