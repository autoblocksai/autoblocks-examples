import * as crypto from 'crypto';
import OpenAI from 'openai';
import { AutoblocksTracer } from '@autoblocks/client';
import { AutoblocksPromptBuilder } from '@autoblocks/client/prompts';
import { ChatCompletionCreateParamsNonStreaming } from 'openai/resources';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const tracer = new AutoblocksTracer(process.env.AUTOBLOCKS_INGESTION_KEY, {
  traceId: crypto.randomUUID(),
});

enum PromptTrackingId {
  FEATURE_A = 'feature-a',
}

async function run() {
  // Use a span ID to group together the request + response/error events
  const spanId = crypto.randomUUID();

  const builder = new AutoblocksPromptBuilder(PromptTrackingId.FEATURE_A);

  const params: ChatCompletionCreateParamsNonStreaming = {
    model: 'gpt-3.5-turbo',
    messages: [
      {
        role: 'system',
        content: builder.build('text-summarization/system', {
          languageRequirement: builder.build('common/language', {
            language: 'Spanish',
          }),
          toneRequirement: builder.build('common/tone', {
            tone: 'formal',
          }),
        }),
      },
      {
        role: 'user',
        content: ['doc1', 'doc2', 'etc']
          .map((doc) => {
            return builder.build('text-summarization/document', {
              document: doc,
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
    promptTracking: builder.usage(),
  });
}

run();
