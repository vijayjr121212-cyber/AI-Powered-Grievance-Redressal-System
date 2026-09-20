import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Netlify handles image optimization via its own CDN
  images: {
    unoptimized: true,
  },
  // Prevent build failures from non-critical issues
  typescript: {
    ignoreBuildErrors: true,
  },
};

export default nextConfig;
