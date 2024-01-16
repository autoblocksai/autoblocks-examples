import * as crypto from 'crypto';
import OpenAI from 'openai';
import { AutoblocksTracer } from '@autoblocks/client';
import { AutoblocksLocalPromptManager } from '@autoblocks/client/prompts';
import { ChatCompletionCreateParamsNonStreaming } from 'openai/resources';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const tracer = new AutoblocksTracer({
  traceId: crypto.randomUUID(),
});

async function run() {
  // Use a span ID to group together the request + response/error events
  const spanId = crypto.randomUUID();

  const manager = new AutoblocksLocalPromptManager({
    id: 'text-summarization',
  });

  const params: ChatCompletionCreateParamsNonStreaming = {
    model: 'gpt-3.5-turbo',
    messages: [
      {
        role: 'system',
        content: manager.render({
          template: 'system',
          params: {
            languageRequirement: manager.render({
              template: 'util/language',
              params: {
                language: 'Spanish',
              },
            }),
            toneRequirement: manager.render({
              template: 'util/tone',
              params: {
                tone: 'formal',
              },
            }),
          },
        }),
      },
      {
        role: 'user',
        content: ['doc1', 'doc2', 'etc']
          .map((doc) => {
            return manager.render({
              template: 'document',
              params: {
                document: doc,
              },
            });
          })
          .join('\n\n'),
      },
    ],
  };

  await tracer.sendEvent('ai.request', {
    spanId,
    properties: {
      ...params,
    },
  });

  const response = await openai.chat.completions.create(params);
  await tracer.sendEvent('ai.response', {
    spanId,
    properties: {
      response,
    },
    promptTracking: manager.track(),
  });
}

run();
