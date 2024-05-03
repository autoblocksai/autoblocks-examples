import asyncio
import os

import httpx

prompts = [
    dict(
        id="study-guide-outline",
        params=dict(
            model="gpt-3.5-turbo",
            maxTokens=2_000,
        ),
        templates=[
            dict(
                id="system",
                template="""Generate a study guide outline for a given topic.
It should be a bulleted list with just the title of each category.
The top level bullets should be stars: *
The second level bullets should be dashes: -
The second level dashes should have two spaces before them.
The study guide should be no more than two levels deep.
There should be between five and ten top-level categories.""",
            ),
            dict(
                id="user",
                template="Topic: {{ topic }}",
            ),
        ],
    ),
    dict(
        id="flashcard-generator",
        params=dict(
            model="gpt-3.5-turbo",
            maxTokens=2_000,
        ),
        templates=[
            dict(
                id="system",
                template="""Given a user's notes, generate flashcards that will allow the user to study those notes.

Your first task is to identify the facts or key points in the notes.
Then, create a flashcard for each fact or key point.
The front of the flashcard should be a question, and the back of the flashcard should be the answer to that question.
Each flashcard should be supported by content from the notes.
Ignore the tone of the notes and always make the flashcards in a professional tone.
Ignore any subjective commentary in the notes and only focus on the facts or key points.
Return the results as JSON in the below format:

'''
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
'''

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
}""",
            ),
            dict(
                id="user",
                template="""Notes:

'''
{{ notes }}
'''

Flashcards:""",
            ),
        ],
    ),
    dict(
        id="is-supported-by-notes-eval",
        params=dict(
            model="gpt-3.5-turbo",
            maxTokens=2_000,
        ),
        templates=[
            dict(
                id="system",
                template="""Given some notes by a student and a flashcard in the form of a question and answer, evaluate whether the flashcard's question and answer are supported by the notes.
It's possible the question and answer aren't in the notes verbatim.
If the notes provide enough context or information to support the question and answer, consider that sufficient support.
Based on these criteria, provide a binary response where:
0 indicates the flashcard's question and answer are not supported by the notes.
1 indicates the flashcard's question and answer are supported by the notes.
No further explanation or summary is required; just provide the number that represents your assessment.""",
            ),
            dict(
                id="user",
                template="""Notes:

'''
{{ notes }}
'''

Flashcard:

Question: {{ question }}
Answer: {{ answer }}""",
            ),
        ],
    ),
    dict(
        id="is-professional-tone-eval",
        params=dict(
            model="gpt-3.5-turbo",
            maxTokens=2_000,
        ),
        templates=[
            dict(
                id="system",
                template="""Please evaluate the provided text for its professionalism in the context of formal communication.
Consider the following criteria in your assessment:

Language Use: Formality, clarity, and precision of language without slang or casual expressions.
Sentence Structure: Logical and well-formed sentence construction without run-ons or fragments.
Tone and Style: Respectful, objective, and appropriately formal tone without bias or excessive emotionality.
Grammar and Punctuation: Correct grammar, punctuation, and capitalization.
Based on these criteria, provide a binary response where:

0 indicates the text does not maintain a professional tone.
1 indicates the text maintains a professional tone.
No further explanation or summary is required; just provide the number that represents your assessment.""",
            ),
            dict(
                id="user",
                template="{{ output }}",
            ),
        ],
    ),
]


async def create_prompts():
    async with httpx.AsyncClient() as client:
        promises = []
        for prompt in prompts:
            response = client.post(
                "https://api.autoblocks.ai/prompts",
                json=prompt,
                headers={
                    "Authorization": f"Bearer {os.environ['AUTOBLOCKS_API_KEY']}",
                },
            )
            promises.append(response)

        for response in await asyncio.gather(*promises):
            print(f"Prompt created: {response.json()['id']}")


def main():
    asyncio.run(create_prompts())
