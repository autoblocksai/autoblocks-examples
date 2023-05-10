import { HandThumbDownIcon, HandThumbUpIcon } from '@heroicons/react/24/solid';
import { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';

export default function DocumentGenerator() {
  const [input, setInput] = useState('');
  const [document, setDocument] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [traceId, setTraceId] = useState(uuidv4());
  const [apiKey, setApiKey] = useState('');

  const onSubmit = async () => {
    setDocument('');
    setIsLoading(true);
    const newTraceId = uuidv4();
    setTraceId(newTraceId);
    const res = await fetch('/api/document-generator', {
      method: 'POST',
      body: JSON.stringify({
        userInput: input,
        traceId: newTraceId,
        apiKey,
      }),
    });
    const { message } = await res.json();
    setIsLoading(false);
    setDocument(message);
  };

  const onThumbUp = async () => {
    await fetch('https://ingest-event.autoblocks.ai', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        traceId,
        userFeedback: 'APPROVE',
        message: 'User Feedback',
        feature: 'Document Generator',
      }),
    });
  };

  const onThumbDown = async () => {
    await fetch('https://ingest-event.autoblocks.ai', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        traceId,
        userFeedback: 'DISAPPROVE',
        message: 'User Feedback',
        feature: 'Document Generator',
      }),
    });
  };

  const onSave = async () => {
    await fetch('https://ingest-event.autoblocks.ai', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        traceId,
        message: 'Document Saved',
        feature: 'Document Generator',
      }),
    });
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
      </div>
      <div
        className={`flex flex-col w-full max-w-4xl px-8 ${
          apiKey === '' ? 'opacity-25 pointer-events-none' : ''
        }`}
      >
        <div className="flex gap-2">
          <input
            type="email"
            name="email"
            id="email"
            className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            placeholder="Write me a budget report..."
            value={input}
            onChange={(ev) => setInput(ev.currentTarget.value)}
          />
          <button
            onClick={onSubmit}
            className="rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Submit
          </button>
        </div>
        {document !== '' && (
          <>
            <div className="mt-4 flex items-center gap-2 justify-end">
              <button
                onClick={onThumbUp}
                className="rounded-md bg-white px-2.5 py-1.5 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
              >
                <HandThumbUpIcon className="h-4 w-4" />
              </button>
              <button
                onClick={onThumbDown}
                className="rounded-md bg-white px-2.5 py-1.5 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
              >
                <HandThumbDownIcon className="h-4 w-4" />
              </button>
              <button
                onClick={onSave}
                className="rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Save Document
              </button>
            </div>
            <div className="w-full border border-gray-300 mt-8 p-4 whitespace-pre-line">
              {document}
            </div>
          </>
        )}
        {isLoading && <div className="mt-8">Creating document...</div>}
      </div>
    </main>
  );
}
