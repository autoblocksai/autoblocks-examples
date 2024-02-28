from openai import OpenAI

from my_project.prompts import (
    StudyGuideOutlinePromptManager,
    StudyGuideOutlineMinorVersion,
)

manager = StudyGuideOutlinePromptManager(StudyGuideOutlineMinorVersion.LATEST)

openai_client = OpenAI()


def gen_study_guide_outline(topic: str) -> str:
    """
    Generates a bulleted study guide outline for a given topic.
    """
    with manager.exec() as prompt:
        response = openai_client.chat.completions.create(
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
                dict(role="user", content=prompt.render.user(topic=topic)),
            ],
        )
        return response.choices[0].message.content.strip()
