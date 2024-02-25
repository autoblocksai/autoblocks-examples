import * as crypto from 'crypto';
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
    source: 'NODE_ASSISTANTS_EXAMPLE',
  },
});

async function run() {
  console.log('Running example...');

  // Create the assistant
  const assistantCreateParams: OpenAI.Beta.AssistantCreateParams = {
    name: 'Math Tutor',
    instructions:
      'You are a personal math tutor. Write and run code to answer math questions.',
    tools: [{ type: 'code_interpreter' }],
    model: 'gpt-4-turbo-preview',
  };
  await tracer.sendEvent('ai.assistant.create', {
    properties: assistantCreateParams,
  });
  const assistant = await openai.beta.assistants.create(assistantCreateParams);
  // All future events will have the assistantId and model property
  tracer.updateProperties({
    assistantId: assistant.id,
    model: assistantCreateParams.model,
  });
  await tracer.sendEvent('ai.assistant.created');

  // Create a new thread
  await tracer.sendEvent('ai.assistant.thread.create');
  const thread = await openai.beta.threads.create();
  // All future events will have the threadId property
  tracer.updateProperties({
    threadId: thread.id,
  });
  await tracer.sendEvent('ai.assistant.thread.created');

  // Create a user messge
  const messageCreateParams: OpenAI.Beta.Threads.MessageCreateParams = {
    role: 'user',
    content: 'I need to solve the equation `3x + 11 = 14`. Can you help me?',
  };
  await tracer.sendEvent('ai.assistant.thread.message.create', {
    properties: {
      message: messageCreateParams,
    },
  });
  const message = await openai.beta.threads.messages.create(
    thread.id,
    messageCreateParams,
  );
  await tracer.sendEvent('ai.assistant.thread.message.created', {
    properties: {
      messageId: message.id,
    },
  });

  // Run the assistant
  const runParams = {
    assistant_id: assistant.id,
    instructions:
      'Please address the user as Jane Doe. The user has a premium account.',
  };

  await tracer.sendEvent('ai.assistant.thread.run.create', {
    properties: {
      runParams,
    },
  });
  const run = await openai.beta.threads.runs.create(thread.id, runParams);
  // All future events will have the runId property
  tracer.updateProperties({
    runId: run.id,
  });
  await tracer.sendEvent('ai.assistant.thread.run.created');

  // Wait for run to complete
  let runCompleted = false;
  while (!runCompleted) {
    const runStatus = await openai.beta.threads.runs.retrieve(
      thread.id,
      run.id,
    );
    if (runStatus.status === 'completed') {
      runCompleted = true;
    }
    // Can expand this to handle other statuses like 'failed' and log them to Autoblocks
  }

  // Log the steps of the run
  const runSteps = await openai.beta.threads.runs.steps.list(thread.id, run.id);
  for (const step of runSteps.data) {
    await tracer.sendEvent(`ai.assistant.thread.run.step.${step.type}`, {
      properties: {
        ...step,
        // Autoblocks uses runIds and parentRunIds to construct the trace tree view
        runId: step.id,
        parentRunId: step.run_id,
      },
    });
  }

  // Log the output of the run
  const messages = await openai.beta.threads.messages.list(thread.id);
  await tracer.sendEvent('ai.assistant.thread.run.completed', {
    properties: {
      response:
        messages.data[0].content[0].type === 'text'
          ? messages.data[0].content[0].text.value
          : messages.data[0].content[0].image_file.file_id,
    },
  });

  console.log(
    `Finished running example. View the trace at https://app.autoblocks.ai/explore/trace/${tracer.traceId}`,
  );
}

run();
