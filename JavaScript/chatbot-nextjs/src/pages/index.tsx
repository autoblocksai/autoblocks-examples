import { PaperAirplaneIcon } from '@heroicons/react/24/solid';
import { classNames } from '~/utils/classNames';
import { ReactNode, useEffect, useRef, useState } from 'react';
import { Avatar } from '~/components/Avatar';
import { createId } from '@paralleldrive/cuid2';
import { v4 as uuidv4 } from 'uuid';
import { AutoblocksTracer } from '@autoblocks/client';
import Link from 'next/link';

enum MessageTypesEnum {
  AI = 'AI',
  HUMAN = 'HUMAN',
}

interface Message {
  text: ReactNode;
  dateTime: number;
  type: MessageTypesEnum;
  id: string;
}

const aiMessages = [
  {
    type: MessageTypesEnum.AI,
    text: 'Hi, how can I help you today?',
    id: createId(),
  },
];

export default function Chat() {
  const chatboxRef = useRef<HTMLDivElement>(null);
  const [gaveFeedback, setGaveFeedback] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    {
      ...aiMessages[0],
      dateTime: new Date().getTime(),
    },
  ]);
  const [traceId, setTraceId] = useState(uuidv4());
  const [autoblocksIngestionKey, setAutoblocksIngestionKey] = useState('');
  const [currentMessage, setCurrentMessage] = useState('');
  useEffect(() => {
    if (chatboxRef.current && currentMessage === '') {
      chatboxRef.current.scrollTop = chatboxRef.current.scrollHeight;
    }
  });

  const onAsk = async () => {
    setIsLoading(true);
    try {
      const pastMessages = [...messages];
      const usersMessage = currentMessage;
      setMessages((prevMessages) => {
        return [
          ...prevMessages,
          {
            text: usersMessage,
            type: MessageTypesEnum.HUMAN,
            dateTime: new Date().getTime(),
            id: createId(),
          },
        ];
      });
      setCurrentMessage('');
      const res = await fetch('/api/chat', {
        method: 'POST',
        body: JSON.stringify({
          userInput: usersMessage,
          pastMessages: pastMessages.map((message) => ({
            role: message.type === MessageTypesEnum.AI ? 'assistant' : 'user',
            content: message.text,
          })),
          traceId,
          autoblocksIngestionKey,
        }),
      });
      const { message } = await res.json();
      setMessages((prevMessages) => {
        return [
          ...prevMessages,
          {
            text: message,
            type: MessageTypesEnum.AI,
            dateTime: new Date().getTime(),
            id: createId(),
          },
        ];
      });
    } finally {
      setIsLoading(false);
    }
  };

  const onFeedback = async (feedback: 'positive' | 'negative') => {
    const tracer = new AutoblocksTracer(autoblocksIngestionKey, {
      traceId,
    });
    await tracer.sendEvent('user.feedback', {
      properties: {
        feedback,
      },
    });
    setGaveFeedback(true);
  };

  return (
    <>
      <main className="flex flex-col items-center mt-8">
        <h1 className="text-2xl mb-4">Autoblocks Chatbot Example</h1>
        <Link
          href="https://app.autoblocks.ai/settings/api-keys"
          target="_blank"
          className="text-blue-600 hover:underline"
        >
          {'Get your ingestion key ->'}
        </Link>
        <div className="flex gap-2 items-center mb-4 mt-1">
          <div className="whitespace-nowrap">
            Autoblocks Ingestion Key (required):
          </div>
          <input
            type="text"
            className="block w-[315px] rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            value={autoblocksIngestionKey}
            onChange={(ev) => setAutoblocksIngestionKey(ev.currentTarget.value)}
          />
        </div>
        <div className="flex gap-2 items-center mb-4">
          <div className="whitespace-nowrap">Trace ID (auto generated):</div>
          <input
            type="text"
            className="block w-[315px] rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            value={traceId}
            readOnly
          />
        </div>
        <div className="mb-4">
          <Button
            onClick={() => {
              setTraceId(uuidv4());
              setMessages([
                {
                  ...aiMessages[0],
                  dateTime: new Date().getTime(),
                },
              ]);
              setGaveFeedback(false);
            }}
          >
            Reset
          </Button>
        </div>
        <div
          className={`max-w-6xl w-full mx-auto ${
            autoblocksIngestionKey === ''
              ? 'opacity-25 pointer-events-none'
              : ''
          }`}
        >
          <div
            className="border-2 border-black rounded-t-lg border-b-0 p-4 h-[600px] flex flex-col space-y-4 overflow-y-auto scrollbar-thumb-blue scrollbar-thumb-rounded scrollbar-track-blue-lighter scrollbar-w-2 scrolling-touch"
            ref={chatboxRef}
          >
            {messages.map((message, index) => {
              return (
                <Message
                  key={message.id}
                  message={message}
                  nextMessageType={messages[index + 1]?.type}
                />
              );
            })}
            {isLoading && (
              <Message
                message={{
                  text: 'Thinking...',
                  type: MessageTypesEnum.AI,
                  id: createId(),
                  dateTime: new Date().getTime(),
                }}
              />
            )}
          </div>
          <div className="flex">
            <input
              id="ask-anything"
              type="search"
              placeholder="Ask me anything..."
              value={currentMessage}
              onChange={(e) => setCurrentMessage(e.currentTarget.value)}
              onKeyDown={(ev) => {
                if (ev.key === 'Enter') {
                  onAsk();
                }
              }}
              className="block w-full border-black rounded-bl-lg border-2 shadow-sm focus:border-black focus:ring-0 text-base text-gray-900 bg-white"
            />
            <button
              onClick={onAsk}
              disabled={currentMessage === ''}
              className="inline-flex items-center rounded-br-lg border-black border-2 border-l-0 px-4 py-2 text-base text-orange-600 hover:text-orange-700 flex-shrink-0 disabled:hover:text-orange-400 disabled:text-orange-400 bg-white"
            >
              <PaperAirplaneIcon className="h-6 w-6" />
            </button>
          </div>
        </div>
        {autoblocksIngestionKey && (
          <div className="mt-4">
            {gaveFeedback ? (
              <div>Thanks for your feedback!</div>
            ) : (
              <div className="flex flex-col gap-2 items-center">
                <div className="text-lg">Was this chatbot helpful?</div>
                <FeedbackButtons onClick={onFeedback} />
              </div>
            )}
          </div>
        )}
      </main>
      <div className="fixed top-2 right-2">
        <div className="flex gap-2">
          <LinkButton href="https://app.autoblocks.ai">App</LinkButton>
          <LinkButton href="https://docs.autoblocks.ai">Docs</LinkButton>
        </div>
      </div>
    </>
  );
}

function Message({
  message,
  nextMessageType,
}: {
  message: Message;
  nextMessageType?: MessageTypesEnum;
}) {
  if (message.type === MessageTypesEnum.HUMAN) {
    const showAvatar =
      nextMessageType === undefined ||
      nextMessageType !== MessageTypesEnum.HUMAN;
    return (
      <div className="flex items-end justify-end">
        <div className="flex flex-col space-y-2 text-md max-w-xs mx-2 order-1 items-end">
          <div>
            <span className="px-4 py-2 rounded-lg inline-block rounded-br-none bg-orange-600 text-white text-sm md:text-base whitespace-pre-line">
              {message.text}
            </span>
          </div>
        </div>
        <div
          className={classNames(
            'order-2',
            showAvatar ? 'visible' : 'invisible'
          )}
        >
          <Avatar firstName={'Adam'} lastName={'Nolte'} />
        </div>
      </div>
    );
  }
  const showAvatar =
    nextMessageType === undefined || nextMessageType !== MessageTypesEnum.AI;
  return (
    <div className="flex items-end">
      <div className="flex flex-col space-y-2 text-md max-w-xs mx-2 order-2 items-start">
        <div>
          <span className="px-4 py-2 rounded-lg inline-block rounded-bl-none bg-gray-300 text-gray-900 text-sm md:text-base whitespace-pre-line">
            {message.text}
          </span>
        </div>
      </div>
      <div
        className={classNames(
          'text-2xl order-1',
          showAvatar ? 'visible' : 'invisible'
        )}
      >
        🤖
      </div>
    </div>
  );
}

function Button(props: { onClick: () => void; children: ReactNode }) {
  return (
    <button
      type="button"
      className="rounded-md bg-orange-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-orange-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      onClick={props.onClick}
    >
      {props.children}
    </button>
  );
}

function LinkButton(props: { href: string; children: ReactNode }) {
  return (
    <Link
      href={props.href}
      className="rounded-md bg-orange-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-orange-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
    >
      {props.children}
    </Link>
  );
}

function FeedbackButtons(props: {
  onClick: (feedback: 'positive' | 'negative') => void;
}) {
  return (
    <span className="isolate inline-flex rounded-md shadow-sm">
      <button
        type="button"
        onClick={() => props.onClick('positive')}
        className="relative inline-flex items-center rounded-l-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-10"
      >
        Yes
      </button>
      <button
        type="button"
        onClick={() => props.onClick('negative')}
        className="relative -ml-px inline-flex items-center rounded-r-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-10"
      >
        No
      </button>
    </span>
  );
}
