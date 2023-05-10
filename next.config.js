/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  /* eslint-disable-next-line */
  async redirects() {
    return [
      {
        source: '/',
        destination: '/document-generator',
        permanent: false,
      },
    ];
  },
};

module.exports = nextConfig;
