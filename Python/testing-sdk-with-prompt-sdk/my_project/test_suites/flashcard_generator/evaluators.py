import asyncio
from typing import List

from autoblocks.testing.models import BaseTestEvaluator
from autoblocks.testing.models import Evaluation
from openai import AsyncOpenAI

from my_project import prompt_managers
from my_project.tasks.flashcard_generator import Flashcard
from my_project.test_suites.flashcard_generator.test_cases import TestCase

openai_client = AsyncOpenAI()


class IsProfessionalTone(BaseTestEvaluator):
    id = "is-professional-tone"

    async def score_flashcard(self, flashcard: Flashcard) -> int:
        content = f"{flashcard.front}\n{flashcard.back}"

        with prompt_managers.is_professional_tone.exec() as prompt:
            response = await openai_client.chat.completions.create(
                model=prompt.params.model,
                temperature=prompt.params.temperature,
                max_tokens=prompt.params.max_tokens,
                top_p=prompt.params.top_p,
                presence_penalty=prompt.params.presence_penalty,
                frequency_penalty=prompt.params.frequency_penalty,
                messages=[
                    dict(
                        role="system",
                        content=prompt.render.system(),
                    ),
                    dict(
                        role="user",
                        content=prompt.render.user(output=content),
                    ),
                ],
            )
            raw_content = response.choices[0].message.content.strip()
            if raw_content == "0":
                return 0
            elif raw_content == "1":
                return 1

            raise ValueError(f"Unexpected response: {raw_content}")

    async def evaluate_test_case(
        self, test_case: TestCase, output: List[Flashcard]
    ) -> Evaluation:
        # Score each flashcard asynchronously
        scores = await asyncio.gather(
            *[self.score_flashcard(flashcard) for flashcard in output]
        )
        if not scores:
            raise RuntimeError("No scores were returned")

        # Return the average score as the evaluation score
        return Evaluation(score=sum(scores) / len(scores))


class IsSupportedByNotes(BaseTestEvaluator):
    id = "is-supported-by-notes"

    async def score_flashcard(self, test_case: TestCase, flashcard: Flashcard) -> int:
        with prompt_managers.is_supported_by_notes.exec() as prompt:
            response = await openai_client.chat.completions.create(
                model=prompt.params.model,
                temperature=prompt.params.temperature,
                max_tokens=prompt.params.max_tokens,
                top_p=prompt.params.top_p,
                presence_penalty=prompt.params.presence_penalty,
                frequency_penalty=prompt.params.frequency_penalty,
                n=1,
                messages=[
                    dict(
                        role="system",
                        content=prompt.render.system(),
                    ),
                    dict(
                        role="user",
                        content=prompt.render.user(
                            notes=test_case.notes,
                            question=flashcard.front,
                            answer=flashcard.back,
                        ),
                    ),
                ],
            )
            raw_content = response.choices[0].message.content.strip()
            if raw_content == "0":
                return 0
            elif raw_content == "1":
                return 1

            raise ValueError(f"Unexpected response: {raw_content}")

    async def evaluate_test_case(
        self, test_case: TestCase, output: List[Flashcard]
    ) -> Evaluation:
        """
        Return the percent of flashcards whose questions and answers are supported by the notes.
        """
        # Score each flashcard asynchronously
        scores = await asyncio.gather(
            *[self.score_flashcard(test_case, flashcard) for flashcard in output]
        )
        if not scores:
            raise RuntimeError("No scores were returned")

        # Return the average score as the evaluation score
        return Evaluation(score=sum(scores) / len(scores))
