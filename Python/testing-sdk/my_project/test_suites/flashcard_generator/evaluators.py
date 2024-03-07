import asyncio
from typing import List

from autoblocks.testing.models import BaseTestEvaluator
from autoblocks.testing.models import Evaluation
from openai import AsyncOpenAI

from my_project.tasks.flashcard_generator import Flashcard
from my_project.test_suites.flashcard_generator.test_cases import TestCase

openai_client = AsyncOpenAI()


class IsProfessionalTone(BaseTestEvaluator):
    id = "is-professional-tone"

    max_concurrency = 2

    prompt = """Please evaluate the provided text for its professionalism in the context of formal communication.
Consider the following criteria in your assessment:

Language Use: Formality, clarity, and precision of language without slang or casual expressions.
Sentence Structure: Logical and well-formed sentence construction without run-ons or fragments.
Tone and Style: Respectful, objective, and appropriately formal tone without bias or excessive emotionality.
Grammar and Punctuation: Correct grammar, punctuation, and capitalization.
Based on these criteria, provide a binary response where:

0 indicates the text does not maintain a professional tone.
1 indicates the text maintains a professional tone.
No further explanation or summary is required; just provide the number that represents your assessment.
"""

    async def score_flashcard(self, flashcard: Flashcard) -> int:
        content = f"{flashcard.front}\n{flashcard.back}"

        response = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            temperature=0.0,
            n=1,
            max_tokens=1,
            messages=[
                dict(
                    role="system",
                    content=self.prompt,
                ),
                dict(
                    role="user",
                    content=content,
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

    max_concurrency = 2

    prompt = """Given some notes by a student and a flashcard in the form of a question and answer, evaluate whether the flashcard's question and answer are supported by the notes.
It's possible the question and answer aren't in the notes verbatim.
If the notes provide enough context or information to support the question and answer, consider that sufficient support.
Based on these criteria, provide a binary response where:
0 indicates the flashcard's question and answer are not supported by the notes.
1 indicates the flashcard's question and answer are supported by the notes.
No further explanation or summary is required; just provide the number that represents your assessment."""  # noqa: E501

    async def score_flashcard(self, test_case: TestCase, flashcard: Flashcard) -> int:
        content = f"""Notes:

        '''
        {test_case.notes}
        '''

        Flashcard:

        Question: {flashcard.front}
        Answer: {flashcard.back}
        """

        response = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            temperature=0.0,
            n=1,
            max_tokens=1,
            messages=[
                dict(
                    role="system",
                    content=self.prompt,
                ),
                dict(
                    role="user",
                    content=content,
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
