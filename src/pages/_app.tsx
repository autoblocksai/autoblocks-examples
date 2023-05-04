import '~/styles/globals.css';
import type { AppProps } from 'next/app';
import Head from 'next/head';
import { Nav } from '~/components/Nav';

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>Autoblocks Example</title>
        <meta name="description" content="Examples of how to use autoblocks" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className="flex justify-around mt-8">
        <Nav />
      </div>
      <Component {...pageProps} />
    </>
  );
}
