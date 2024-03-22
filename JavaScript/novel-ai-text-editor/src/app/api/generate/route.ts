import OpenAI from 'openai';
import { OpenAIStream, StreamingTextResponse } from 'ai';

// Create an OpenAI API client (that's edge friendly!)
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY || '',
});

// IMPORTANT! Set the runtime to edge: https://vercel.com/docs/functions/edge-functions/edge-runtime
export const runtime = 'edge';

export async function POST(req: Request): Promise<Response> {
  // Check if the OPENAI_API_KEY is set, if not return 400
  if (!process.env.OPENAI_API_KEY || process.env.OPENAI_API_KEY === '') {
    return new Response(
      'Missing OPENAI_API_KEY – make sure to add it to your .env file.',
      {
        status: 400,
      },
    );
  }
  // Start the timer for duration tracking till the end of the stream
  const startTimer = Date.now();

  let { prompt } = await req.json();

  const params: OpenAI.Chat.Completions.ChatCompletionCreateParamsStreaming = {
    model: 'gpt-3.5-turbo',
    messages: [
      {
        role: 'system',
        content:
          'You are an AI writing assistant that continues existing text based on context from prior text. ' +
          'Give more weight/priority to the later characters than the beginning ones. ' +
          'Limit your response to no more than 200 characters, but make sure to construct complete sentences.',
        // we're disabling markdown for now until we can figure out a way to stream markdown text with proper formatting: https://github.com/steven-tey/novel/discussions/7
        // "Use Markdown formatting when appropriate.",
      },
      {
        role: 'user',
        content: prompt,
      },
    ],
    temperature: 0.7,
    top_p: 1,
    frequency_penalty: 0,
    presence_penalty: 0,
    stream: true,
    n: 1,
  };

  const traceId = Math.random().toString(36).substring(7);
  await sendEventToAutoblocks({
    eventName: 'ai.request',
    properties: { ...params, provider: 'openai' },
    traceId,
  });

  try {
    const response = await openai.chat.completions.create(params);

    // Convert the response into a friendly text-stream
    const stream = OpenAIStream(response, {
      onStart: async () => {
        await sendEventToAutoblocks({
          eventName: 'ai.stream.start',
          traceId,
        });
      },
      onCompletion: async (completion) => {
        await sendEventToAutoblocks({
          eventName: 'ai.stream.completion',
          traceId,
          properties: {
            durationMs: Date.now() - startTimer,
            completion,
          },
        });
      },
    });

    // Respond with the stream
    return new StreamingTextResponse(stream);
  } catch (error) {
    await sendEventToAutoblocks({
      eventName: 'ai.request.error',
      traceId,
      properties: {
        error,
      },
    });
    return new Response(undefined, {
      status: 500,
    });
  }
}

const sendEventToAutoblocks = async (args: {
  eventName: string;
  traceId: string;
  properties?: Record<string, any>;
}) => {
  try {
    await fetch('https://ingest-event.autoblocks.ai', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.AUTOBLOCKS_INGESTION_KEY || ''}`,
      },
      body: JSON.stringify({
        traceId: args.traceId,
        message: args.eventName,
        properties: args.properties,
      }),
      signal: AbortSignal.timeout(1_000),
    });
  } catch (err) {
    console.error('Failed to send event to Autoblocks:', err);
  }
};
