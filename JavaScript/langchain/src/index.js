import { AutoblocksCallbackHandler } from '@autoblocks/client/langchain';
import { OpenAI } from "langchain/llms/openai";
import { DynamicTool } from "langchain/tools";
import { Calculator } from "langchain/tools/calculator";
import { initializeAgentExecutorWithOptions } from "langchain/agents";

const main = async () => {
  const model = new OpenAI({ temperature: 0 });
  const tools = [
    new Calculator(),
    new DynamicTool({
      name: "Today's Date",
      description:
        "call this to get today's date. input should be an empty string.",
      func: () => new Date().getDate(),
    }),
  ];

  const executor = await initializeAgentExecutorWithOptions(tools, model, {
    agentType: 'structured-chat-zero-shot-react-description',
  });

  const handler = new AutoblocksCallbackHandler();
  const output = await executor.run(
    "What is today's date? What is that date divided by 2?",
    { callbacks: [handler]
  });

  console.log(`Output: ${output}`);
  console.log('\n');
  console.log('View your trace: https://app.autoblocks.ai/explore')
}

main();
