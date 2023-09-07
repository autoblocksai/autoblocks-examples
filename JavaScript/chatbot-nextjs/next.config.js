const removeImports = require('next-remove-imports')();

/** @type {import('next').NextConfig} */
const nextConfig = removeImports({
  experimental: { esmExternals: true },
  reactStrictMode: true,
  webpack: (config) => {
    config.resolve.fallback = { fs: false, child_process: false };
    return config;
  },
});

module.exports = nextConfig;
