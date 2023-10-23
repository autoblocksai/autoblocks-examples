import { AutoblocksCallbackHandler } from '@autoblocks/client/langchain';

import { SimpleSequentialChain, LLMChain } from "langchain/chains";
import { OpenAI } from "langchain/llms/openai";
import { PromptTemplate } from "langchain/prompts";

const main = async () => {
  // This is an LLMChain to write a synopsis given a title of a play.
  const synopsisLLM = new OpenAI({ temperature: 0.7 });
  const titleTemplate = `You are a playwright. Given the title of a play, it is your job to write a synopsis for that title.
  
Title: {title}
Playwright: This is a synopsis for the above play:`;
  const synopsisTemplate = new PromptTemplate({
    template: titleTemplate,
    inputVariables: ["title"],
  });
  const synopsisChain = new LLMChain({ llm: synopsisLLM, prompt: synopsisTemplate });

  // This is an LLMChain to write a review of a play given a synopsis.
  const reviewLLM = new OpenAI({ temperature: 0.7 });
  const reviewTemplate = `You are a play critic from the New York Times. Given the synopsis of a play, it is your job to write a review for that play.
  
Play Synopsis:
{synopsis}
Review from a New York Times play critic of the above play:`;
  const reviewPromptTemplate = new PromptTemplate({
    template: reviewTemplate,
    inputVariables: ["synopsis"],
  });
  const reviewChain = new LLMChain({
    llm: reviewLLM,
    prompt: reviewPromptTemplate,
  });

  // This is the overall chain where we run these two chains in sequence.
  const overallChain = new SimpleSequentialChain({
    chains: [synopsisChain, reviewChain],
  });

  // Run the chain
  const handler = new AutoblocksCallbackHandler();
  const review = await overallChain.run("Tragedy at sunset on the beach", { callbacks: [handler] });

  console.log('Review:');
  console.log(review);
}

main();
