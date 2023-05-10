import type { NextApiRequest, NextApiResponse } from 'next';
import { Configuration, OpenAIApi } from 'openai';

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});

export const openai = new OpenAIApi(configuration);

const autoblocksUrl = 'https://ingest-event.autoblocks.ai';
const feature = 'Chat';

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
  const { userInput, pastMessages, traceId, apiKey } = JSON.parse(req.body);
  if (!userInput) {
    return res.status(400).json({ error: 'Missing user input' });
  }
  if (!pastMessages) {
    return res.status(400).json({ error: 'Missing past messages' });
  }
  if (!traceId) {
    return res.status(400).json({ error: 'Missing traceId' });
  }
  if (!apiKey) {
    return res.status(400).json({ error: 'Missing API Key' });
  }

  await fetch(autoblocksUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({
      feature,
      message: 'Chat User Message',
      userInput,
      traceId,
    }),
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
    await fetch(autoblocksUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        feature,
        message: 'No response from OpenAI',
        traceId,
      }),
    });
    return res.status(500).json({ error: 'No response from OpenAI' });
  }
  const openAIResponseMessage = openAIResponse.data.choices[0].message;

  await fetch(autoblocksUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({
      feature,
      message: 'Chat Completion',
      traceId,
      input: messages,
      output: openAIResponseMessage.content,
      model: 'gpt-3.5-turbo',
      temperature: '1',
      provider: 'OPENAI',
      params: {},
    }),
  });

  return res.status(200).json({
    message: openAIResponseMessage.content,
  });
}
