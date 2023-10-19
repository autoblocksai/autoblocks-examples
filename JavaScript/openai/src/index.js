import crypto from 'crypto';
import OpenAI from 'openai';
import { AutoblocksTracer } from '@autoblocks/client';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const traceId = crypto.randomUUID();
const ab = new AutoblocksTracer(process.env.AUTOBLOCKS_INGESTION_KEY, {
  // These apply to every call of ab.sendEvent() so we don't have to repeat them
  traceId,
  properties: {
    provider: 'openai',
    source: 'NODE_EXAMPLE',
  },
});

async function run() {
  console.log('Running example...');

  const openAIRequest = {
    model: 'gpt-3.5-turbo',
    messages: [
      {
        role: 'system',
        content:
          'You are a helpful assistant.' +
          'You answer questions about a software product named Acme.',
      },
      {
        role: 'user',
        content: 'How do I sign up?',
      },
    ],
    temperature: 0.7,
    top_p: 1,
    frequency_penalty: 0,
    presence_penalty: 0,
    stream: false,
    n: 1,
  };

  await ab.sendEvent('ai.request', {
    properties: openAIRequest,
  });

  try {
    const now = Date.now();
    const response = await openai.chat.completions.create(openAIRequest);
    await ab.sendEvent('ai.response', {
      properties: {
        response,
        latency: Date.now() - now,
      },
    });
  } catch (error) {
    await ab.sendEvent('ai.error', {
      properties: {
        error,
      },
    });
  }

  console.log(
    `Finished running example. View the trace at https://app.autoblocks.ai/explore/trace/${traceId}`
  );
}

run();
