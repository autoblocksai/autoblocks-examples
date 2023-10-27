import crypto from 'crypto';
import { AutoblocksTracer } from '@autoblocks/client';

const tracer = new AutoblocksTracer(process.env.AUTOBLOCKS_INGESTION_KEY, {
  traceId: crypto.randomUUID(),
  properties: {
    provider: 'openai',
  },
});

const spanStack = [];

function startSpan() {
  spanStack.push(crypto.randomUUID());
  setSpanIds();
}

function endSpan() {
  if (spanStack.length > 0) {
    spanStack.pop();
    setSpanIds();
  }
}

function setSpanIds() {
  let spanId = undefined;
  let parentSpanId = undefined;

  if (spanStack.length >= 2) {
    spanId = spanStack[spanStack.length - 1];
    parentSpanId = spanStack[spanStack.length - 2];
  } else if (spanStack.length === 1) {
    spanId = spanStack[0];
  }

  tracer.updateProperties({ spanId, parentSpanId });
}

const spanFunction = async (fn) => {
  startSpan();
  await fn();
  endSpan();
};

async function makeEmbeddingRequest() {
  await tracer.sendEvent('ai.embedding.request');

  // Make embedding request...

  await tracer.sendEvent('ai.embedding.response');
}

async function startRAGPipeline() {
  await tracer.sendEvent('ai.rag.start');

  // Simulate making multiple embedding requests within a RAG pipeline
  await spanFunction(makeEmbeddingRequest);
  await spanFunction(makeEmbeddingRequest);

  await tracer.sendEvent('ai.rag.end');
}

async function makeLLMRequest() {
  // Here we would use the RAG response to generate a prompt for the LLM

  await tracer.sendEvent('ai.completion.request', {
    properties: {
      temperature: 0.5,
      topP: 1,
    },
  });

  await tracer.sendEvent('ai.completion.response', {
    properties: {
      totalTokens: 123,
    },
  });
}

async function run() {
  await spanFunction(startRAGPipeline);
  await spanFunction(makeLLMRequest);
}

run();
