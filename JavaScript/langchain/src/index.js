import { AutoblocksCallbackHandler } from '@autoblocks/client/langchain';

import { LLMChain } from 'langchain/chains';
import { OpenAI } from 'langchain/llms/openai';
import { PromptTemplate } from 'langchain/prompts';

const main = async () => {
  const llm = new OpenAI({ temperature: 0 });
  const prompt = PromptTemplate.fromTemplate('2 + {number} =');
  const chain = new LLMChain({ prompt, llm });
  
  const handler = new AutoblocksCallbackHandler();
  await chain.call({ number: 2 }, { callbacks: [handler] });
}

main();
