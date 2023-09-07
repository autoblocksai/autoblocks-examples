import { PaperAirplaneIcon } from '@heroicons/react/24/solid';
import { classNames } from '~/utils/classNames';
import { ReactNode, useEffect, useRef, useState } from 'react';
import { Avatar } from '~/components/Avatar';
import { createId } from '@paralleldrive/cuid2';
import { v4 as uuidv4 } from 'uuid';

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
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    {
      ...aiMessages[0],
      dateTime: new Date().getTime(),
    },
  ]);
  const [openAIMessages, setOpenAIMessages] = useState<
    { role: 'user' | 'assistant'; content: string }[]
  >([
    {
      role: 'assistant',
      content: aiMessages[0].text,
    },
  ]);
  const [traceId] = useState(uuidv4());
  const [apiKey, setApiKey] = useState('');
  const [currentMessage, setCurrentMessage] = useState('');
  useEffect(() => {
    if (chatboxRef.current && currentMessage === '') {
      chatboxRef.current.scrollTop = chatboxRef.current.scrollHeight;
    }
  });

  const onAsk = async () => {
    setIsLoading(true);
    try {
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
          pastMessages: openAIMessages,
          traceId,
          apiKey,
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
      setOpenAIMessages((prevMessages) => {
        return [
          ...prevMessages,
          {
            role: 'user',
            content: usersMessage,
          },
          {
            role: 'assistant',
            content: message,
          },
        ];
      });
    } finally {
      setIsLoading(false);
    }
  };
  return (
    <main className="flex flex-col items-center">
      <h1 className="text-2xl mb-4">Autoblocks Chat Example</h1>
      <div className="flex gap-2 items-center mb-4">
        <div className="whitespace-nowrap">
          Autoblocks Ingestion Key (required):
        </div>
        <input
          type="text"
          className="block w-[315px] rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
          value={apiKey}
          onChange={(ev) => setApiKey(ev.currentTarget.value)}
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
      <div
        className={`max-w-6xl w-full mx-auto ${
          apiKey === '' ? 'opacity-25 pointer-events-none' : ''
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
    </main>
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

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
