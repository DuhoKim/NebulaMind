"use client";

import { useState } from "react";

interface Nominee {
  id: number;
  arxiv_id: string;
  title: string;
  authors: string;
  summary: string;
  why_funny: string;
  emoji: string;
  url: string;
  votes: number;
}

const NOMINEES: Nominee[] = [
  {
    id: 1,
    arxiv_id: "2604.01277",
    title: "Lights, Camera, Axion: Tracing Axions from Supernovae in the Diffuse γ-ray Sky",
    authors: "et al.",
    summary: "Axions produced in supernova explosions could convert into photons in magnetic fields. This paper tracks the cumulative γ-ray glow from every supernova in cosmic history to constrain axion properties.",
    why_funny: '🎬 The title is a perfect "Lights, Camera, Action" pun — as if axions are starring in their own blockbuster movie, with supernovae as the stage.',
    emoji: "🎬",
    url: "https://arxiv.org/abs/2604.01277",
    votes: 0,
  },
  {
    id: 2,
    arxiv_id: "2604.01283",
    title: "Is Gravity Always Enough to Yield a Classical Universe?",
    authors: "et al.",
    summary: "Cosmic structure originated from quantum fluctuations, yet the universe looks classical today. This paper questions whether gravity alone can explain this quantum-to-classical transition.",
    why_funny: "🤔 Reads like an existential crisis in physics form. Gravity is having an identity crisis — 'Am I enough?'",
    emoji: "🤔",
    url: "https://arxiv.org/abs/2604.01283",
    votes: 0,
  },
  {
    id: 3,
    arxiv_id: "2604.00535",
    title: "Three-Dimensional Ocean Dynamics and Detectability of Tidally Locked Lava Worlds",
    authors: "et al.",
    summary: "Tidally locked lava planets have a permanent molten dayside. This paper simulates 3D magma ocean circulation and asks: can JWST actually detect these lava seas?",
    why_funny: "🌋 3D ocean simulation... but it's LAVA. Imagine surfing on a planet where the ocean is 1,500°C molten rock. Extreme watersports, cosmic edition.",
    emoji: "🌋",
    url: "https://arxiv.org/abs/2604.00535",
    votes: 0,
  },
  {
    id: 4,
    arxiv_id: "2604.00679",
    title: "Arches of Chaos, Heteroclinic Connections of First-Order MMRs and the Chaotic Transport of Small Bodies in the Sun-Jupiter System",
    authors: "et al.",
    summary: "Invisible 'arches' of gravitational chaos connect orbital resonances in the Sun-Jupiter system, acting as cosmic highways that fling asteroids across the solar system.",
    why_funny: "⚡ 'Arches of Chaos' sounds like a Marvel villain's lair or a metal band album. In reality it's about asteroids hitchhiking on invisible gravitational highways.",
    emoji: "⚡",
    url: "https://arxiv.org/abs/2604.00679",
    votes: 0,
  },
  {
    id: 5,
    arxiv_id: "2604.00604",
    title: "Misaligned Rings Around Minor Planets with Moons",
    authors: "et al.",
    summary: "Some small solar system bodies have rings AND moons. This paper analyzes how the moon's gravity can tilt and warp these delicate ring systems.",
    why_funny: "💍 Cosmic jewelry problems: when your rings just won't sit straight because your moon keeps bumping them. Relatable, honestly.",
    emoji: "💍",
    url: "https://arxiv.org/abs/2604.00604",
    votes: 0,
  },
];

export default function AprilFoolsPage() {
  const [votes, setVotes] = useState<Record<number, number>>({});
  const [voted, setVoted] = useState<number | null>(null);
  const [totalVotes, setTotalVotes] = useState<Record<number, number>>({});

  const handleVote = async (id: number) => {
    if (voted) return;
    setVoted(id);
    setTotalVotes((prev) => ({ ...prev, [id]: (prev[id] || 0) + 1 }));

    try {
      await fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: `April Fools Vote: ${id}`,
          message: `Voted for nominee #${id} in April Fools Award 2026`,
          is_ai: false,
        }),
      });
    } catch {}
  };

  const sorted = [...NOMINEES].sort(
    (a, b) => (totalVotes[b.id] || 0) - (totalVotes[a.id] || 0)
  );

  return (
    <div className="max-w-3xl mx-auto">
      {/* Header */}
      <div className="text-center mb-10">
        <div className="text-6xl mb-4">🤡</div>
        <h1 className="text-3xl font-bold mb-2">
          April Fools Award 2026
        </h1>
        <p className="text-gray-500">
          The best (unintentionally) funny paper titles from arXiv astro-ph on April 1st, 2026
        </p>
        <p className="text-sm text-gray-400 mt-2">
          All real papers. All serious science. All hilarious titles.
        </p>
      </div>

      {/* Nominees */}
      <div className="space-y-4">
        {sorted.map((nom, idx) => {
          const isWinner = idx === 0 && voted;
          const voteCount = totalVotes[nom.id] || 0;

          return (
            <div
              key={nom.id}
              className={`border rounded-xl p-5 transition-all ${
                voted === nom.id
                  ? "border-yellow-400 bg-yellow-50 shadow-md"
                  : "border-gray-200 bg-white hover:border-indigo-300"
              } ${isWinner && voted ? "ring-2 ring-yellow-400" : ""}`}
            >
              <div className="flex items-start gap-4">
                <div className="text-3xl flex-shrink-0 mt-1">{nom.emoji}</div>
                <div className="flex-1 min-w-0">
                  <a
                    href={nom.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="font-semibold text-gray-900 hover:text-indigo-700 no-underline text-lg leading-tight block"
                  >
                    {nom.title}
                  </a>
                  <p className="text-sm text-gray-600 mt-2">{nom.summary}</p>
                  <p className="text-sm text-indigo-600 mt-1 font-medium">{nom.why_funny}</p>
                  <p className="text-xs text-gray-400 mt-1">
                    arXiv:{nom.arxiv_id}
                  </p>
                </div>
                <div className="flex flex-col items-center gap-1 flex-shrink-0">
                  <button
                    onClick={() => handleVote(nom.id)}
                    disabled={voted !== null}
                    className={`px-4 py-2 rounded-lg font-medium text-sm transition-all ${
                      voted === nom.id
                        ? "bg-yellow-400 text-yellow-900"
                        : voted
                        ? "bg-gray-100 text-gray-400 cursor-not-allowed"
                        : "bg-indigo-600 text-white hover:bg-indigo-700"
                    }`}
                  >
                    {voted === nom.id ? "🏆 Voted!" : voted ? "—" : "Vote"}
                  </button>
                  {voted && (
                    <span className="text-xs text-gray-400">
                      {voteCount} vote{voteCount !== 1 ? "s" : ""}
                    </span>
                  )}
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Footer */}
      {voted && (
        <div className="text-center mt-8 p-4 bg-gray-50 rounded-xl">
          <p className="text-gray-600">
            Thanks for voting! 🎉 Results will be announced in the next newsletter.
          </p>
        </div>
      )}

      <div className="text-center mt-8 text-sm text-gray-400">
        <p>
          🌌 NebulaMind celebrates the lighter side of science.
          <br />
          All nominees are real, peer-worthy research papers.
        </p>
      </div>
    </div>
  );
}
