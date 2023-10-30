import crypto from 'crypto';
import OpenAI from 'openai';
import { AutoblocksTracer } from '@autoblocks/client';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const tracer = new AutoblocksTracer(process.env.AUTOBLOCKS_INGESTION_KEY, {
  // These apply to every call of tracer.sendEvent() so we don't have to repeat them
  traceId: crypto.randomUUID(),
  properties: {
    provider: 'openai',
    source: 'NODE_EXAMPLE',
  },
});

async function run() {
  console.log('Running example...');

  // Use a spanId to group together the request + response/error events
  const spanId = crypto.randomUUID();

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

  await tracer.sendEvent('ai.request', {
    properties: { ...openAIRequest, spanId },
  });

  try {
    const now = Date.now();
    const response = await openai.chat.completions.create(openAIRequest);
    await tracer.sendEvent('ai.response', {
      properties: {
        response,
        latency: Date.now() - now,
        spanId,
      },
    });
  } catch (error) {
    await tracer.sendEvent('ai.error', {
      properties: {
        error,
        spanId,
      },
    });
  }

  console.log(
    `Finished running example. View the trace at https://app.autoblocks.ai/explore/trace/${tracer.traceId}`,
  );
}

run();
