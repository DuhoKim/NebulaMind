export const CATEGORIES: Record<string, {
  emoji: string;
  label: string;
  description: string;
  color: string;
}> = {
  cosmology: {
    emoji: "🔭",
    label: "Cosmology",
    description: "The origin, structure, and fate of the universe — from the Big Bang to dark energy.",
    color: "#6366f1",
  },
  stellar: {
    emoji: "⭐",
    label: "Stars",
    description: "Stellar evolution, binary systems, neutron stars, white dwarfs, and the stellar lifecycle.",
    color: "#eab308",
  },
  blackhole: {
    emoji: "🕳️",
    label: "Black Holes",
    description: "Event horizons, Hawking radiation, mergers, and the physics of extreme gravity.",
    color: "#8b5cf6",
  },
  highenergy: {
    emoji: "⚡",
    label: "High-Energy",
    description: "Gamma-ray bursts, fast radio bursts, pulsars, magnetars, and extreme astrophysical events.",
    color: "#ef4444",
  },
  solarsystem: {
    emoji: "🪐",
    label: "Solar System",
    description: "Planets, moons, asteroids, the Kuiper Belt, Oort Cloud, and planetary formation.",
    color: "#22c55e",
  },
  galaxy: {
    emoji: "🌀",
    label: "Galaxies",
    description: "Galaxy formation, the Milky Way, clusters, active galactic nuclei, and the cosmic web.",
    color: "#06b6d4",
  },
};

export const CATEGORY_ORDER = ["cosmology", "blackhole", "stellar", "galaxy", "highenergy", "solarsystem"];
