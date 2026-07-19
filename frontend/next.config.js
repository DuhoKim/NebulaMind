/** @type {import('next').NextConfig} */

// Canonical slug redirects — singular/variant forms that 404 but map to real pages.
// Using permanent: true (308) so Google drops the old URL quickly.
const WIKI_SLUG_REDIRECTS = [
  // Singular → plural
  ["black-hole",          "black-holes"],
  ["neutron-star",        "neutron-stars"],
  ["exoplanet",           "exoplanets"],
  ["pulsar",              "pulsars"],
  ["gravitational-wave",  "gravitational-waves"],
  ["gamma-ray-burst",     "gamma-ray-bursts"],
  ["white-dwarf",         "white-dwarfs"],
  ["binary-star",         "binary-stars"],
  ["galaxy-cluster",      "galaxy-clusters"],
  ["wormhole",            "wormholes"],
  ["red-giant",           "red-giants"],
  ["magnetar",            "magnetars"],
  ["fast-radio-burst",    "fast-radio-bursts"],
  ["nebula",              "nebulae"],
  // Latin plural
  ["supernova",           "supernovae"],
  ["planetary-nebula",    "planetary-nebulae"],
  // Common alias slugs
  ["hubble-tension",      "hubble-constant"],
  ["exoplanet-detection", "exoplanet-detection-methods"],
  ["star-formation",      "stellar-evolution"],
  ["supermassive-black-holes", "black-holes"],
].map(([from, to]) => ({
  source: `/wiki/${from}`,
  destination: `/wiki/${to}`,
  permanent: true,
}));

const nextConfig = {
  async redirects() {
    return [...WIKI_SLUG_REDIRECTS, { source: "/ideas", destination: "/research", permanent: false }];
  },
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: "http://localhost:8000/api/:path*",
      },
    ];
  },
};

module.exports = nextConfig;
