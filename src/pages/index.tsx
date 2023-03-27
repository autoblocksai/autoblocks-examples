import { Nav } from '~/components/Nav';

export default function Home() {
  return (
    <main className="flex flex-col items-center p-8 max-w-6xl w-full mx-auto">
      <h1 className="text-2xl mb-4">Autoblocks Examples</h1>
      <Nav />
    </main>
  );
}
