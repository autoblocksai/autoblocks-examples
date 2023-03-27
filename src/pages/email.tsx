import Link from 'next/link';

export default function Email() {
  return (
    <main className="flex flex-col items-center p-8">
      <h1 className="text-2xl mb-4">Autoblocks Email Example</h1>
      <ul className="text-blue-700 text-lg list-disc">
        <li>
          <Link href="/chat">Chat Example</Link>
        </li>
        <li>
          <Link href="/email">Email Example</Link>
        </li>
      </ul>
    </main>
  );
}
