import type { NextApiRequest, NextApiResponse } from 'next';
import { Configuration, OpenAIApi } from 'openai';

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});

export const openai = new OpenAIApi(configuration);

const systemPrompt = `
You are a helpful assistant.
You answer questions about a software product named Acme.
You can make up answers.
Sometimes you do not know the answer.
`;
export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const { userInput, pastMessages, traceId } = JSON.parse(req.body);
  if (!userInput) {
    return res.status(400).json({ error: 'Missing user input' });
  }
  if (!pastMessages) {
    return res.status(400).json({ error: 'Missing past messages' });
  }
  if (!traceId) {
    return res.status(400).json({ error: 'Missing traceId' });
  }

  setImmediate(async () => {
    await fetch('https://api.autoblocks.ai/v1/events/user-input', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.AUTOBLOCKS_API_KEY}`,
      },
      body: JSON.stringify({
        featureId: 'clglc6t620000mx0g5ladrfnq',
        name: 'User Message',
        input: userInput,
        traceId,
      }),
    });
  });

  const messages = [
    { role: 'system', content: systemPrompt },
    ...pastMessages,
    { role: 'user', content: userInput },
  ];

  const openAIResponse = await openai.createChatCompletion({
    model: 'gpt-3.5-turbo',
    messages,
    temperature: 1,
  });

  if (
    !openAIResponse.data.choices ||
    !openAIResponse.data.choices[0]?.message
  ) {
    res.status(500).json({ error: 'No response from OpenAI' });
    await fetch('https://api.autoblocks.ai/v1/events', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.AUTOBLOCKS_API_KEY}`,
      },
      body: JSON.stringify({
        featureId: 'clglc6t620000mx0g5ladrfnq',
        name: 'No response from OpenAI',
        traceId,
      }),
    });
  } else {
    const openAIResponseMessage = openAIResponse.data.choices[0].message;

    res.status(200).json({
      message: openAIResponseMessage.content,
    });

    console.log('Sending LLM event to autoblocks');
    await fetch('https://api.autoblocks.ai/v1/events/llm', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.AUTOBLOCKS_API_KEY}`,
      },
      body: JSON.stringify({
        featureId: 'clglc6t620000mx0g5ladrfnq',
        name: 'Chat Completion',
        traceId,
        input: messages
          .map((message) => `${message.role}: ${message.content}`)
          .join('\n'),
        output: openAIResponseMessage.content,
        model: 'gpt-3.5-turbo',
        temperature: '1',
        provider: 'OPENAI',
        params: {},
      }),
    });
  }
}
