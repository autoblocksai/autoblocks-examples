import dataclasses
import json
from typing import List

from openai import OpenAI
from openai.types.chat.completion_create_params import ResponseFormat

from my_project.prompts import (
    FlashcardGeneratorPromptManager,
    FlashcardGeneratorMinorVersion,
)

manager = FlashcardGeneratorPromptManager(FlashcardGeneratorMinorVersion.LATEST)

openai_client = OpenAI()


@dataclasses.dataclass()
class Flashcard:
    front: str
    back: str


def gen_flashcards_from_notes(notes: str) -> List[Flashcard]:
    """
    Generates flashcards based on a user's notes.
    """
    with manager.exec() as prompt:
        response = openai_client.chat.completions.create(
            model=prompt.params.model,
            temperature=prompt.params.temperature,
            max_tokens=prompt.params.max_tokens,
            top_p=prompt.params.top_p,
            presence_penalty=prompt.params.presence_penalty,
            frequency_penalty=prompt.params.frequency_penalty,
            response_format=ResponseFormat(type="json_object"),
            messages=[
                dict(
                    role="system",
                    content=prompt.render.system(),
                ),
                dict(
                    role="user",
                    content=prompt.render.user(notes=notes),
                ),
            ],
        )
        raw_content = response.choices[0].message.content.strip()
        parsed_content = json.loads(raw_content)
        return [
            Flashcard(
                front=parsed_content["front"],
                back=parsed_content["back"],
            )
            for parsed_content in parsed_content["cards"]
        ]
