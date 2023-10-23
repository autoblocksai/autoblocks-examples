import OpenAI from 'openai';
import { traceOpenAI } from '@autoblocks/client/openai';

async function main() {
  await traceOpenAI();
  console.log('Automatically tracing all calls to OpenAI...');

  const openai = new OpenAI();

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

  console.log('Calling OpenAI...');
  await openai.chat.completions.create(openAIRequest);
  console.log('Finished calling OpenAI');

  console.log('View the trace at https://app.autoblocks.ai/explore')
}

main();
