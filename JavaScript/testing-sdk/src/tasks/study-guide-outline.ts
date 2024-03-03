import OpenAI from 'openai';

const openai = new OpenAI();

const systemPrompt = `Generate a study guide outline for a given topic.
It should be a bulleted list with just the title of each category.
The top level bullets should be stars: *
The second level bullets should be dashes: -
The second level dashes should have two spaces before them.
The study guide should be no more than two levels deep.
There should be between five and ten top-level categories.`;

export async function genStudyGuideOutline(topic: string): Promise<string> {
  const resp = await openai.chat.completions.create({
    model: 'gpt-3.5-turbo-1106',
    temperature: 0.5,
    max_tokens: 1_000,
    n: 1,
    messages: [
      {
        role: 'system',
        content: systemPrompt,
      },
      {
        role: 'user',
        content: `Topic: ${topic}`,
      },
    ],
  });

  return resp.choices[0].message.content.trim();
}
