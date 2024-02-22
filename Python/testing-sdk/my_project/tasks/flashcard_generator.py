import dataclasses
import json
from typing import List

from openai import OpenAI
from openai.types.chat.completion_create_params import ResponseFormat

openai_client = OpenAI()


@dataclasses.dataclass()
class Flashcard:
    front: str
    back: str


system_prompt = """Given a user's notes, generate flashcards that will allow the user to study those notes.

Your first task is to identify the facts or key points in the notes.
Then, create a flashcard for each fact or key point.
The front of the flashcard should be a question, and the back of the flashcard should be the answer to that question.
Each flashcard should be supported by content from the notes.
Ignore the tone of the notes and always make the flashcards in a professional tone.
Ignore any subjective commentary in the notes and only focus on the facts or key points.
Return the results as JSON in the below format:

```
{
  "cards": [
    {
      "front": "What is the capital of France?",
      "back": "Paris"
    },
    {
      "front": "Who painted the Mona Lisa?",
      "back": "Leonardo da Vinci"
    }
  ]
}
```

Only return JSON in your response, nothing else. Do not include the backticks.

Example:

Notes:

'''
Am. History Notes 🇺🇸
Beginnings & Stuff
Columbus 1492, "found" America but actually not the first.
Native Americans were here first, tons of diff cultures.
Colonies & Things
13 Colonies cuz Brits wanted $ and land.
Taxation w/o Representation = Colonists mad at British taxes, no say in gov.
Boston Tea Party = Tea in the harbor, major protest.
Revolution Time
Declaration of Independence, 1776, basically "we're breaking up with you, Britain".
George Washington = First pres, war hero.
Moving West
Manifest Destiny = Idea that the US was supposed to own all land coast to coast.
Louisiana Purchase, 1803, Thomas Jefferson bought a ton of land from France.
'''

Flashcards:

{
  "cards": [
    {
      "front": "Who was the first president of the United States?",
      "back": "George Washington"
    },
    {
      "front": "What was the idea that the US was supposed to own all land coast to coast?",
      "back": "Manifest Destiny"
    },
    {
      "front": "What was the year of the Louisiana Purchase?",
      "back": "1803"
    }
  ]
}
"""

user_prompt = """Notes:

'''
{notes}
'''

Flashcards:"""


def gen_flashcards_from_notes(notes: str) -> List[Flashcard]:
    """
    Generates flashcards based on a user's notes.
    """
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0.0,
        response_format=ResponseFormat(type="json_object"),
        messages=[
            dict(
                role="system",
                content=system_prompt,
            ),
            dict(
                role="user",
                content=user_prompt.format(notes=notes),
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
