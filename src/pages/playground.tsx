import { ArrowPathIcon } from '@heroicons/react/24/solid';
import { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import dynamic from 'next/dynamic';
import '@uiw/react-textarea-code-editor/dist.css';

const CodeEditor = dynamic(
  () => import('@uiw/react-textarea-code-editor').then((mod) => mod.default),
  { ssr: false }
);

export default function DocumentGenerator() {
  const [response, setResponse] = useState('');
  const [traceId, setTraceId] = useState(uuidv4());
  const [input, setInput] = useState('');
  const [apiKey, setApiKey] = useState('');

  const onSendEvent = async () => {
    try {
      const res = await fetch('https://ingest-event.autoblocks.ai', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${apiKey}`,
        },
        body: input,
      });
      const json = await res.json();
      setResponse(
        JSON.stringify({ statusCode: res.status, responseBody: json }, null, 2)
      );
    } catch (error) {
      setResponse(JSON.stringify(error, null, 2));
    }
  };

  return (
    <main className="flex flex-col items-center">
      <h1 className="text-2xl mb-4">Autoblocks Document Generator Example</h1>
      <div className="flex gap-2 items-center mb-4">
        <div className="whitespace-nowrap">Autoblocks API Key (required):</div>
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
        <button onClick={() => setTraceId(uuidv4())}>
          <ArrowPathIcon className="h-5 w-5" />
        </button>
      </div>
      <div
        className={`flex flex-col w-full max-w-4xl px-8 ${
          apiKey === '' ? 'opacity-25 pointer-events-none' : ''
        }`}
      >
        <div>Event JSON:</div>
        <CodeEditor
          value={input}
          language="json"
          placeholder="Please enter event json."
          onChange={(evn) => setInput(evn.target.value)}
          padding={15}
          style={{
            minHeight: 200,
            fontSize: 14,
            backgroundColor: '#f3f4f6',
            borderRadius: '.375rem',
            fontFamily:
              'ui-monospace,SFMono-Regular,SF Mono,Consolas,Liberation Mono,Menlo,monospace',
          }}
        />
        <div className="mt-2 self-end">
          <button
            onClick={onSendEvent}
            className="rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Send Event
          </button>
        </div>
        {response !== '' && (
          <>
            <div className="mt-4">Response:</div>
            <pre className="border border-gray-200 p-4 rounded-md">
              {response}
            </pre>
          </>
        )}
      </div>
    </main>
  );
}
