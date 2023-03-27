import Link from 'next/link';

export const Nav = () => {
  return (
    <ul className="text-blue-700 text-lg flex gap-4 mb-8">
      <li>
        <Link href="/chat">Chat Example</Link>
      </li>
      <li>
        <Link href="/auto-assign">Auto Assign Example</Link>
      </li>
    </ul>
  );
};
