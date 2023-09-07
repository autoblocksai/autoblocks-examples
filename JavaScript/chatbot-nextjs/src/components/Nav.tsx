import Link from 'next/link';

export const Nav = () => {
  return (
    <ul className="text-blue-700 text-lg flex gap-4 mb-8">
      <li>
        <Link href="/chat">Chat Example</Link>
      </li>
      <li>
        <Link href="/document-generator">Document Generator</Link>
      </li>
      <li>
        <Link href="/playground">Playground</Link>
      </li>
    </ul>
  );
};
