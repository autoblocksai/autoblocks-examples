import Link from 'next/link';
import { PaperAirplaneIcon } from '@heroicons/react/24/solid';
import { classNames } from '~/utils/classNames';
import { ReactNode, useEffect, useRef, useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { Avatar } from '~/components/Avatar';

enum MessageTypesEnum {
  AI = 'AI',
  HUMAN = 'HUMAN"',
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
    id: uuidv4(),
  },
  {
    type: MessageTypesEnum.AI,
    text: "I'm sorry workflows is not a feature that we support",
    id: uuidv4(),
  },
];

export default function Chat() {
  const chatboxRef = useRef<HTMLDivElement>(null);
  const [messages, setMessages] = useState<Message[]>([
    {
      ...aiMessages[0],
      dateTime: new Date().getTime(),
    },
  ]);
  const [interactionId] = useState(uuidv4());
  const [currentMessage, setCurrentMessage] = useState('');
  useEffect(() => {
    if (chatboxRef.current && currentMessage === '') {
      chatboxRef.current.scrollTop = chatboxRef.current.scrollHeight;
    }
  });

  const onAsk = async () => {
    const usersMessage = currentMessage;
    setMessages((prevMessages) => {
      if (prevMessages.length === 1) {
        return [
          ...prevMessages,
          {
            text: usersMessage,
            type: MessageTypesEnum.HUMAN,
            dateTime: new Date().getTime(),
            id: uuidv4(),
          },
          {
            ...aiMessages[1],
            dateTime: new Date().getTime(),
          },
        ];
      }
      return [
        ...prevMessages,
        {
          text: usersMessage,
          type: MessageTypesEnum.HUMAN,
          dateTime: new Date().getTime(),
          id: uuidv4(),
        },
      ];
    });
    setCurrentMessage('');
    if (messages.length === 1) {
      await fetch('/api/send-event', {
        method: 'POST',
        body: JSON.stringify({
          name: `User message: ${usersMessage}`,
          feature: 'Support Chatbot',
          interactionId,
        }),
      });
      await sleep(100);
      await fetch('/api/send-llm-event', {
        method: 'POST',
        body: JSON.stringify({
          name: `Process user message`,
          feature: 'Support Chatbot',
          interactionId,
          input: usersMessage,
          output: aiMessages[1].text,
          provider: 'OPENAI',
          model: 'gpt-3.5-turbo',
          temperature: '0',
          params: {},
        }),
      });
      await sleep(1000);
      await fetch('/api/send-event', {
        method: 'POST',
        body: JSON.stringify({
          name: `AI message: ${aiMessages[1].text}`,
          feature: 'Support Chatbot',
          interactionId,
        }),
      });
    } else {
      await fetch('/api/send-event', {
        method: 'POST',
        body: JSON.stringify({
          name: `User message: ${usersMessage}`,
          feature: 'Support Chatbot',
          interactionId,
        }),
      });
    }
  };
  return (
    <main className="flex flex-col items-center p-8">
      <h1 className="text-2xl mb-4">Autoblocks Chat Example</h1>
      <ul className="text-blue-700 text-lg list-disc">
        <li>
          <Link href="/chat">Chat Example</Link>
        </li>
        <li>
          <Link href="/email">Email Example</Link>
        </li>
      </ul>
      <div className="max-w-6xl w-full mx-auto">
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
        </div>
        <div className="flex">
          <input
            id="ask-anything"
            type="search"
            placeholder="How to come up with recipes"
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
            <span className="px-4 py-2 rounded-lg inline-block rounded-br-none bg-orange-600 text-white text-sm md:text-base">
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
          <span className="px-4 py-2 rounded-lg inline-block rounded-bl-none bg-gray-300 text-gray-900 text-sm md:text-base">
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
