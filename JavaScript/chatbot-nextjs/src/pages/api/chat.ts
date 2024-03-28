import crypto from 'crypto';
import type { NextApiRequest, NextApiResponse } from 'next';
import OpenAI from 'openai';
import { AutoblocksTracer } from '@autoblocks/client';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const systemPrompt = `
You are a helpful assistant.
You answer questions about a software product named Acme.
You can make up answers.
Sometimes you do not know the answer.
`;

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse,
) {
  const { userInput, pastMessages, traceId, autoblocksIngestionKey } =
    JSON.parse(req.body);
  if (!userInput) {
    return res.status(400).json({ error: 'Missing user input' });
  }
  if (!pastMessages) {
    return res.status(400).json({ error: 'Missing past messages' });
  }
  if (!traceId) {
    return res.status(400).json({ error: 'Missing traceId' });
  }
  if (!autoblocksIngestionKey) {
    return res.status(400).json({ error: 'Missing Autoblocks Ingestion Key' });
  }

  // Substitute this for process.env.AUTOBLOCKS_INGESTION_KEY in a production environment
  // You can also initialize this outside of the handler in that case
  const tracer = new AutoblocksTracer({
    ingestionKey: autoblocksIngestionKey,
    traceId,
    properties: {
      provider: 'openai',
    },
  });

  // Use a span ID to group together the request + response/error events
  const spanId = crypto.randomUUID();

  const params = {
    model: 'gpt-3.5-turbo',
    messages: [
      { role: 'system', content: systemPrompt },
      ...pastMessages,
      { role: 'user', content: userInput },
    ],
    temperature: 1,
  };

  tracer.sendEvent('ai.request', {
    spanId,
    properties: params,
  });

  try {
    const now = Date.now();
    const response = await openai.chat.completions.create(params);
    tracer.sendEvent('ai.response', {
      spanId,
      properties: {
        response,
        latencyMs: Date.now() - now,
      },
    });
    return res.status(200).json({
      message: response.choices[0].message.content,
    });
  } catch (error) {
    tracer.sendEvent('ai.error', {
      spanId,
      properties: {
        error,
      },
    });
    return res.status(500).json({
      error: 'Internal Server Error',
    });
  }
}
