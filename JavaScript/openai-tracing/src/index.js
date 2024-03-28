import crypto from 'crypto';
import OpenAI from 'openai';
import { AutoblocksTracer } from '@autoblocks/client';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const tracer = new AutoblocksTracer({
  // These apply to every call of tracer.sendEvent() so we don't have to repeat them
  traceId: crypto.randomUUID(),
  properties: {
    provider: 'openai',
    source: 'NODE_EXAMPLE',
  },
});

async function run() {
  console.log('Running example...');

  // Use a span ID to group together the request + response/error events
  const spanId = crypto.randomUUID();

  const params = {
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
        latency: Date.now() - now,
      },
    });
  } catch (error) {
    tracer.sendEvent('ai.error', {
      spanId,
      properties: {
        error,
      },
    });
    throw error;
  }

  console.log(
    `Finished running example. View the trace at https://app.autoblocks.ai/explore/trace/${tracer.traceId}`,
  );
}

run();
