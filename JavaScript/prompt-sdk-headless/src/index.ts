import * as crypto from 'crypto';
import OpenAI from 'openai';
import { AutoblocksTracer } from '@autoblocks/client';
import { AutoblocksPromptManager } from '@autoblocks/client/prompts';
import { ChatCompletionCreateParamsNonStreaming } from 'openai/resources';

const openai = new OpenAI();

const manager = new AutoblocksPromptManager({
  id: 'text-summarization',
  version: {
    major: '1',
    minor: '0',
  },
});

async function run() {
  await manager.init();

  const response = await manager.exec(async ({ prompt }) => {
    const tracer = new AutoblocksTracer({
      traceId: crypto.randomUUID(),
    });

    const params: ChatCompletionCreateParamsNonStreaming = {
      model: prompt.params.model,
      temperature: prompt.params.temperature,
      messages: [
        {
          role: 'system',
          content: prompt.render({
            template: 'system',
            params: {
              languageRequirement: prompt.render({
                template: 'util/language',
                params: {
                  language: 'Spanish',
                },
              }),
              toneRequirement: prompt.render({
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
              return prompt.render({
                template: 'user',
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
      properties: params,
    });

    const response = await openai.chat.completions.create(params);

    await tracer.sendEvent('ai.response', {
      properties: {
        response,
      },
      promptTracking: prompt.track(),
    });

    return response;
  });

  console.log(response);
}

run();
