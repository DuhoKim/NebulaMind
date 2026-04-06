"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

interface Card {
  id: number;
  title: string;
  slug: string;
  summary: string;
  category: string;
  difficulty: string | null;
  thumbnail_emoji: string | null;
  edit_count: number;
  is_featured: boolean;
}

const CATEGORIES = ["all", "stellar", "blackhole", "galaxy", "cosmology", "solarsystem", "general"];
const DIFFICULTIES = ["all", "beginner", "intermediate", "advanced"];

const CATEGORY_EMOJI: Record<string, string> = {
  blackhole: "🕳️",
  stellar: "⭐",
  galaxy: "🌌",
  cosmology: "🔭",
  solarsystem: "🪐",
  general: "📖",
};

const CATEGORY_COLOR: Record<string, string> = {
  blackhole: "#7c3aed",
  stellar: "#d97706",
  galaxy: "#2563eb",
  cosmology: "#4338ca",
  solarsystem: "#16a34a",
  general: "#6b7280",
};

const DIFFICULTY_COLOR: Record<string, string> = {
  beginner: "#16a34a",
  intermediate: "#d97706",
  advanced: "#dc2626",
};

export default function CardsPage() {
  const router = useRouter();
  const [cards, setCards] = useState<Card[]>([]);
  const [categoryFilter, setCategoryFilter] = useState("all");
  const [difficultyFilter, setDifficultyFilter] = useState("all");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    const params = new URLSearchParams();
    if (categoryFilter !== "all") params.set("category", categoryFilter);
    if (difficultyFilter !== "all") params.set("difficulty", difficultyFilter);
    fetch(`/api/explore/cards?${params}`)
      .then((r) => r.json())
      .then((data) => {
        setCards(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [categoryFilter, difficultyFilter]);

  return (
    <div>
      <h2 style={{ fontSize: "1.3rem", margin: "0 0 1rem" }}>Knowledge Cards</h2>

      {/* Category filters */}
      <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap", marginBottom: "0.75rem" }}>
        {CATEGORIES.map((cat) => (
          <button
            key={cat}
            onClick={() => setCategoryFilter(cat)}
            style={{
              padding: "0.35rem 0.75rem",
              border: categoryFilter === cat ? "2px solid #4f46e5" : "1px solid #d1d5db",
              borderRadius: "9999px",
              background: categoryFilter === cat ? "#eef2ff" : "#fff",
              color: categoryFilter === cat ? "#4f46e5" : "#374151",
              cursor: "pointer",
              fontSize: "0.85rem",
              fontWeight: categoryFilter === cat ? 600 : 400,
            }}
          >
            {cat === "all" ? "All" : `${CATEGORY_EMOJI[cat] || ""} ${cat}`}
          </button>
        ))}
      </div>

      {/* Difficulty filters */}
      <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap", marginBottom: "1.5rem", alignItems: "center" }}>
        <span style={{ fontSize: "0.8rem", color: "#6b7280", fontWeight: 500 }}>Difficulty:</span>
        {DIFFICULTIES.map((diff) => (
          <button
            key={diff}
            onClick={() => setDifficultyFilter(diff)}
            style={{
              padding: "0.25rem 0.6rem",
              border: difficultyFilter === diff ? `2px solid ${DIFFICULTY_COLOR[diff] || "#4f46e5"}` : "1px solid #d1d5db",
              borderRadius: "9999px",
              background: difficultyFilter === diff ? `${DIFFICULTY_COLOR[diff] || "#4f46e5"}15` : "#fff",
              color: difficultyFilter === diff ? (DIFFICULTY_COLOR[diff] || "#4f46e5") : "#374151",
              cursor: "pointer",
              fontSize: "0.8rem",
              fontWeight: difficultyFilter === diff ? 600 : 400,
            }}
          >
            {diff === "all" ? "All Levels" : diff.charAt(0).toUpperCase() + diff.slice(1)}
          </button>
        ))}
      </div>

      {loading ? (
        <p style={{ color: "#9ca3af" }}>Loading cards...</p>
      ) : cards.length === 0 ? (
        <p style={{ color: "#9ca3af" }}>No cards found.</p>
      ) : (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))",
            gap: "1rem",
          }}
        >
          {cards.map((card) => (
            <div
              key={card.id}
              onClick={() => router.push(`/wiki/${card.slug}`)}
              style={{
                border: "1px solid #e5e7eb",
                borderRadius: "0.75rem",
                padding: "1rem",
                cursor: "pointer",
                transition: "box-shadow 0.15s",
                position: "relative",
              }}
              onMouseOver={(e) => (e.currentTarget.style.boxShadow = "0 4px 12px rgba(0,0,0,0.08)")}
              onMouseOut={(e) => (e.currentTarget.style.boxShadow = "none")}
            >
              {/* Featured badge */}
              {card.is_featured && (
                <span
                  style={{
                    position: "absolute",
                    top: "0.5rem",
                    right: "0.5rem",
                    fontSize: "0.7rem",
                    background: "#fef3c7",
                    color: "#d97706",
                    border: "1px solid #fde68a",
                    borderRadius: "9999px",
                    padding: "0.1rem 0.4rem",
                    fontWeight: 600,
                  }}
                >
                  ⭐ Featured
                </span>
              )}

              {/* Thumbnail emoji (big) */}
              <div style={{ fontSize: "2.5rem", marginBottom: "0.5rem", lineHeight: 1 }}>
                {card.thumbnail_emoji || CATEGORY_EMOJI[card.category] || "📖"}
              </div>

              {/* Title */}
              <div style={{ fontWeight: 600, fontSize: "1rem", marginBottom: "0.4rem" }}>
                {card.title}
              </div>

              {/* Summary */}
              <p style={{ fontSize: "0.85rem", color: "#4b5563", margin: "0 0 0.75rem", lineHeight: 1.4 }}>
                {card.summary || "No content yet."}
              </p>

              {/* Footer */}
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: "0.25rem" }}>
                <span
                  style={{
                    fontSize: "0.75rem",
                    padding: "0.15rem 0.5rem",
                    borderRadius: "9999px",
                    background: `${CATEGORY_COLOR[card.category] || "#6b7280"}20`,
                    color: CATEGORY_COLOR[card.category] || "#6b7280",
                    fontWeight: 500,
                  }}
                >
                  {card.category}
                </span>
                <div style={{ display: "flex", gap: "0.4rem", alignItems: "center" }}>
                  {card.difficulty && (
                    <span
                      style={{
                        fontSize: "0.7rem",
                        padding: "0.1rem 0.4rem",
                        borderRadius: "9999px",
                        background: `${DIFFICULTY_COLOR[card.difficulty] || "#6b7280"}15`,
                        color: DIFFICULTY_COLOR[card.difficulty] || "#6b7280",
                        fontWeight: 500,
                        textTransform: "capitalize",
                      }}
                    >
                      {card.difficulty}
                    </span>
                  )}
                  <span style={{ fontSize: "0.75rem", color: "#9ca3af" }}>
                    {card.edit_count} edits
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
