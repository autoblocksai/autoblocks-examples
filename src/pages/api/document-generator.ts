import type { NextApiRequest, NextApiResponse } from 'next';
import {
  ChatCompletionRequestMessageRoleEnum,
  Configuration,
  OpenAIApi,
} from 'openai';

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});

export const openai = new OpenAIApi(configuration);

const autoblocksUrl = 'https://ingest-event.autoblocks.ai';
const feature = 'DOCUMENT_GENERATOR';

const systemPrompt = `
You are a helpful assistant that writes business documents.
When asked you create a template for the requested document.
Only respond with the document template and nothing else.
`;
export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const { userInput, traceId, apiKey } = JSON.parse(req.body);
  if (!userInput) {
    return res.status(400).json({ error: 'Missing user input' });
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
      message: 'user.input',
      feature,
      userInput,
      traceId,
    }),
  });

  const messages = [
    {
      role: ChatCompletionRequestMessageRoleEnum.System,
      content: systemPrompt,
    },
    { role: ChatCompletionRequestMessageRoleEnum.User, content: userInput },
  ];

  const startTime = performance.now();
  const openAIResponse = await openai.createChatCompletion({
    model: 'gpt-3.5-turbo',
    messages,
    temperature: 1,
    max_tokens: 2048,
  });
  const endTime = performance.now();

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
        message: 'foundation-model.error',
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
      message: 'foundation-model.response',
      traceId,
      input: messages,
      output: openAIResponseMessage.content,
      model: 'gpt-3.5-turbo',
      temperature: '1',
      maxTokens: '2048',
      provider: 'OPENAI',
      latency: `${endTime - startTime}`,
    }),
  });

  return res.status(200).json({
    message: openAIResponseMessage.content,
  });
}
