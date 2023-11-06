const crypto = require('crypto');
const OpenAI = require('openai');
const { AutoblocksTracer } = require('@autoblocks/client');

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const tracer = new AutoblocksTracer(process.env.AUTOBLOCKS_INGESTION_KEY, {
  properties: {
    provider: 'openai',
  },
});

const run = async ({ input, traceId }) => {
  // Set the traceId to the one given, or fall back to a random UUID.
  // When we call this function from the test suite we will pass in a
  // traceId so that it is stable across replay runs, but in production
  // we'll only pass in an input, like run({ input }), so that we generate
  // a random traceId while in production.
  tracer.setTraceId(traceId || crypto.randomUUID());

  // Use a span ID to group together the request + response/error events
  const spanId = crypto.randomUUID();

  const request = {
    model: 'gpt-3.5-turbo',
    messages: [
      {
        role: 'system',
        content:
          'You are a helpful assistant. ' +
          'You answer questions about a software product named Acme. ' +
          'Your answers should be in a friendly tone and include a bulleted or numbered list where appopriate. ' +
          'You should also include a link to the relevant page in the Acme documentation.',
      },
      {
        role: 'user',
        content: input,
      },
    ],
    temperature: 0.3,
  };

  await tracer.sendEvent('ai.request', {
    spanId,
    properties: request,
  });

  try {
    const now = Date.now();
    const response = await openai.chat.completions.create(request);
    await tracer.sendEvent('ai.response', {
      spanId,
      properties: {
        response,
        latencyMs: Date.now() - now,
      },
    });
    return response.choices[0].message.content;
  } catch (error) {
    await tracer.sendEvent('ai.error', {
      spanId,
      properties: {
        error,
      },
    });
    throw error;
  }
};

module.exports = { run };
