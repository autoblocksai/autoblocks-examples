from openai import OpenAI

openai_client = OpenAI()

system_prompt = """Generate a study guide outline for a given topic.
It should be a bulleted list with just the title of each category.
The top level bullets should be stars: *
The second level bullets should be dashes: -
The second level dashes should have two spaces before them.
The study guide should be no more than two levels deep.
There should be between five and ten top-level categories."""


def gen_study_guide_outline(topic: str) -> str:
    """
    Generates a bulleted study guide outline for a given topic.
    """
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0.5,
        max_tokens=1_000,
        n=1,
        messages=[
            dict(
                role="system",
                content=system_prompt,
            ),
            dict(
                role="user",
                content=f"Topic: {topic}",
            ),
        ],
    )
    return response.choices[0].message.content.strip()
