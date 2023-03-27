import { Listbox, Transition } from '@headlessui/react';

import {
  CalendarIcon,
  PaperClipIcon,
  TagIcon,
  UserCircleIcon,
} from '@heroicons/react/20/solid';
import { useState, Fragment } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { Nav } from '~/components/Nav';
import { classNames } from '~/utils/classNames';

const assignees = [
  { name: 'Unassigned', value: null },
  {
    name: 'Wade Cooper',
    value: 'wade-cooper',
    avatar:
      'https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
  },
  {
    name: 'Olivia Rhye',
    value: 'olivia-rhye',
    avatar:
      'https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
  },
  {
    name: 'Jack Frost',
    value: 'jack-frost',
    avatar:
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80',
  },
];

export default function Task() {
  const [assigned, setAssigned] = useState(assignees[0]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [interactionId] = useState(uuidv4());

  const sendEvents = async (selectedVal: {
    name: string;
    value: null;
    avatar?: string;
  }) => {
    await fetch('/api/send-event', {
      method: 'POST',
      body: JSON.stringify({
        name: `Entered Title: ${title}`,
        feature: 'Auto Assign Ticket',
        interactionId,
      }),
    });
    await sleep(100);
    await fetch('/api/send-event', {
      method: 'POST',
      body: JSON.stringify({
        name: `Entered Description: ${description}`,
        feature: 'Auto Assign Ticket',
        interactionId,
      }),
    });
    await sleep(100);
    await fetch('/api/send-llm-event', {
      method: 'POST',
      body: JSON.stringify({
        name: `Summarize Title and Description`,
        feature: 'Auto Assign Ticket',
        interactionId,
        input: `A user is creating a bug ticket. This is the title "${title}" and this is the description "${description}". Provide a summary of the bug ticket.`,
        output: 'A bug ticket about auto assign.',
        provider: 'OPENAI',
        model: 'gpt-3.5-turbo',
        temperature: '0',
        params: {},
      }),
    });
    await sleep(100);
    await fetch('/api/send-event', {
      method: 'POST',
      body: JSON.stringify({
        name: `Search Vector DB with query: Assignes who work on tasks similar to "A bug ticket about auto assign".`,
        feature: 'Auto Assign Ticket',
        interactionId,
      }),
    });
    await sleep(100);
    await fetch('/api/send-event', {
      method: 'POST',
      body: JSON.stringify({
        name: `Vector DB Results: [Wade Cooper, Olivia Rhye]`,
        feature: 'Auto Assign Ticket',
        interactionId,
      }),
    });
    await sleep(100);
    await fetch('/api/send-llm-event', {
      method: 'POST',
      body: JSON.stringify({
        name: 'Find relevant ticket.',
        feature: 'Auto Assign Ticket',
        interactionId,
        input: `With the following tickets which is more similar to "A bug ticket about auto assign". ""Ticket 1=Fix description auto complete when changing assignee. Assignee=Wade Cooper."" ""Ticket 2=Assignee Dropdowns are the wrong size. Assignee Olivia Rhye.""`,
        output: 'Ticket 1.',
        provider: 'OPENAI',
        model: 'gpt-3.5-turbo',
        temperature: '0',
        params: {},
      }),
    });
    await sleep(100);
    await fetch('/api/send-event', {
      method: 'POST',
      body: JSON.stringify({
        name: `Auto set assignee to "Wade Cooper"`,
        feature: 'Auto Assign Ticket',
        interactionId,
      }),
    });
    await sleep(100);
    await fetch('/api/send-event', {
      method: 'POST',
      body: JSON.stringify({
        name: `User Overrode Assignee to ${selectedVal.name}`,
        feature: 'Auto Assign Ticket',
        interactionId,
      }),
    });
  };
  return (
    <main className="flex flex-col items-center p-8 max-w-4xl mx-auto">
      <h1 className="text-2xl mb-4">Autoblocks Auto Assign Example</h1>
      <Nav />
      <form action="#" className="relative w-full">
        <div className="overflow-hidden rounded-lg border border-gray-300 shadow-sm focus-within:border-indigo-500 focus-within:ring-1 focus-within:ring-indigo-500">
          <label htmlFor="title" className="sr-only">
            Title
          </label>
          <input
            type="text"
            name="title"
            id="title"
            className="block w-full border-0 pt-2.5 text-lg font-medium placeholder:text-gray-400 focus:ring-0"
            placeholder="Title"
            value={title}
            onChange={(ev) => setTitle(ev.target.value)}
          />
          <label htmlFor="description" className="sr-only">
            Description
          </label>
          <textarea
            rows={2}
            name="description"
            id="description"
            className="block w-full resize-none border-0 py-0 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
            placeholder="Write a description..."
            value={description}
            onChange={(ev) => {
              if (ev.target.value.length > 20) {
                setAssigned(assignees[1]);
              }
              setDescription(ev.target.value);
            }}
          />

          {/* Spacer element to match the height of the toolbar */}
          <div aria-hidden="true">
            <div className="py-2">
              <div className="h-9" />
            </div>
            <div className="h-px" />
            <div className="py-2">
              <div className="py-px">
                <div className="h-9" />
              </div>
            </div>
          </div>
        </div>

        <div className="absolute inset-x-px bottom-0">
          {/* Actions: These are just examples to demonstrate the concept, replace/wire these up however makes sense for your project. */}
          <div className="flex flex-nowrap justify-end space-x-2 py-2 px-2 sm:px-3">
            <Listbox
              as="div"
              value={assigned}
              onChange={(selectedVal) => {
                setAssigned(selectedVal);
                // @ts-expect-error this is ok
                sendEvents(selectedVal);
              }}
              className="flex-shrink-0"
            >
              {({ open }) => (
                <>
                  <Listbox.Label className="sr-only"> Assign </Listbox.Label>
                  <div className="relative">
                    <Listbox.Button className="relative inline-flex items-center whitespace-nowrap rounded-full bg-gray-50 py-2 px-2 text-sm font-medium text-gray-500 hover:bg-gray-100 sm:px-3">
                      {assigned.value === null ? (
                        <UserCircleIcon
                          className="h-5 w-5 flex-shrink-0 text-gray-300 sm:-ml-1"
                          aria-hidden="true"
                        />
                      ) : (
                        <img
                          src={assigned.avatar}
                          alt=""
                          className="h-5 w-5 flex-shrink-0 rounded-full"
                        />
                      )}

                      <span
                        className={classNames(
                          assigned.value === null ? '' : 'text-gray-900',
                          'hidden truncate sm:ml-2 sm:block'
                        )}
                      >
                        {assigned.value === null ? 'Assign' : assigned.name}
                      </span>
                    </Listbox.Button>

                    <Transition
                      show={open}
                      as={Fragment}
                      leave="transition ease-in duration-100"
                      leaveFrom="opacity-100"
                      leaveTo="opacity-0"
                    >
                      <Listbox.Options className="absolute right-0 z-10 mt-1 max-h-56 w-52 overflow-auto rounded-lg bg-white py-3 text-base shadow ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                        {assignees.map((assignee) => (
                          <Listbox.Option
                            key={assignee.value}
                            className={({ active }) =>
                              classNames(
                                active ? 'bg-gray-100' : 'bg-white',
                                'relative cursor-default select-none py-2 px-3'
                              )
                            }
                            value={assignee}
                          >
                            <div className="flex items-center">
                              {assignee.avatar ? (
                                <img
                                  src={assignee.avatar}
                                  alt=""
                                  className="h-5 w-5 flex-shrink-0 rounded-full"
                                />
                              ) : (
                                <UserCircleIcon
                                  className="h-5 w-5 flex-shrink-0 text-gray-400"
                                  aria-hidden="true"
                                />
                              )}

                              <span className="ml-3 block truncate font-medium">
                                {assignee.name}
                              </span>
                            </div>
                          </Listbox.Option>
                        ))}
                      </Listbox.Options>
                    </Transition>
                  </div>
                </>
              )}
            </Listbox>
          </div>
          <div className="flex items-center justify-between space-x-3 border-t border-gray-200 px-2 py-2 sm:px-3">
            <div className="flex">
              <button
                type="button"
                className="group -my-2 -ml-2 inline-flex items-center rounded-full px-3 py-2 text-left text-gray-400"
              >
                <PaperClipIcon
                  className="-ml-1 mr-2 h-5 w-5 group-hover:text-gray-500"
                  aria-hidden="true"
                />
                <span className="text-sm italic text-gray-500 group-hover:text-gray-600">
                  Attach a file
                </span>
              </button>
            </div>
            <div className="flex-shrink-0">
              <button
                type="submit"
                className="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Create
              </button>
            </div>
          </div>
        </div>
      </form>
    </main>
  );
}

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
