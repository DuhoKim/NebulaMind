"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

interface WikiPage {
  id: number;
  title: string;
  slug: string;
  content: string;
}

interface EditRecord {
  id: number;
  page_id: number;
  agent_id: number;
  status: string;
}

interface FeaturedPage {
  id: number;
  title: string;
  slug: string;
  content: string;
  editCount: number;
}

const TOPIC_EMOJIS: Record<string, string> = {
  "black hole": "🕳️",
  "galaxy": "🌌",
  "star": "⭐",
  "planet": "🪐",
  "nebula": "🌫️",
  "supernova": "💥",
  "neutron": "⚛️",
  "pulsar": "📡",
  "quasar": "✨",
  "dark matter": "🌑",
  "dark energy": "⚡",
  "exoplanet": "🌍",
  "comet": "☄️",
  "asteroid": "🪨",
  "kuiper": "🧊",
  "oort": "❄️",
  "cosmic": "🌠",
  "universe": "🔭",
  "solar": "☀️",
  "moon": "🌙",
  "mars": "🔴",
  "jupiter": "🟠",
  "saturn": "💍",
  "binary": "👥",
  "gravitational": "🌊",
  "telescope": "🔭",
  "hubble": "🛰️",
  "james webb": "🛸",
};

function getEmoji(title: string): string {
  const lower = title.toLowerCase();
  for (const [key, emoji] of Object.entries(TOPIC_EMOJIS)) {
    if (lower.includes(key)) return emoji;
  }
  return "🔭";
}

function getDescription(content: string): string {
  if (!content) return "Explore this fascinating astronomical topic.";
  // Remove markdown headers and get first meaningful sentence
  const cleaned = content
    .replace(/^#+\s+.+$/gm, "")
    .replace(/\*\*/g, "")
    .replace(/\*/g, "")
    .trim();
  const firstPara = cleaned.split("\n").find((l) => l.trim().length > 30) || "";
  return firstPara.slice(0, 110) + (firstPara.length > 110 ? "..." : "");
}

export default function FeaturedTopics() {
  const [featured, setFeatured] = useState<FeaturedPage[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const API_BASE = process.env.NEXT_PUBLIC_API_URL || "";
    fetch(`${API_BASE}/api/explore/cards?featured=true`)
      .then((r) => r.json())
      .then((cards: any[]) => {
        const enriched: FeaturedPage[] = cards.map((c: any) => ({
          id: c.id,
          title: c.title,
          slug: c.slug,
          content: c.summary || "",
          editCount: c.edit_count || 0,
        }));
        setFeatured(enriched.slice(0, 10));
      })
      .catch(() => setFeatured([]))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <section className="mb-12">
        <h2 className="text-2xl font-bold mb-6">🔥 Featured Topics</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {[...Array(6)].map((_, i) => (
            <div
              key={i}
              className="h-36 bg-gray-100 rounded-xl animate-pulse"
            />
          ))}
        </div>
      </section>
    );
  }

  if (featured.length === 0) return null;

  return (
    <section className="mb-12">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold">🔥 Featured Topics</h2>
        <Link
          href="/explore"
          className="text-indigo-600 text-sm font-medium hover:text-indigo-800"
        >
          View all →
        </Link>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {featured.map((page) => (
          <Link
            key={page.slug}
            href={`/wiki/${page.slug}`}
            className="group block p-5 bg-white rounded-xl border border-gray-200 hover:border-indigo-300 hover:shadow-lg transition-all no-underline text-inherit"
          >
            <div className="flex items-start justify-between mb-2">
              <span className="text-3xl">{getEmoji(page.title)}</span>
              <span className="text-xs font-semibold bg-indigo-100 text-indigo-700 px-2 py-0.5 rounded-full">
                {page.editCount} edits
              </span>
            </div>
            <h3 className="font-bold text-base mb-1 text-gray-900 group-hover:text-indigo-700 transition-colors">
              {page.title}
            </h3>
            <p className="text-gray-500 text-sm leading-relaxed">
              {getDescription(page.content)}
            </p>
          </Link>
        ))}
      </div>
    </section>
  );
}
