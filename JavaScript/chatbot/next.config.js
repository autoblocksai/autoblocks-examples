const removeImports = require('next-remove-imports')();

/** @type {import('next').NextConfig} */
const nextConfig = removeImports({
  experimental: { esmExternals: true },
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
});

module.exports = nextConfig;
