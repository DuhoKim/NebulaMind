"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

interface Card {
  id: number;
  title: string;
  slug: string;
  summary: string;
  category: string;
  edit_count: number;
}

const CATEGORIES = ["all", "stellar", "blackhole", "galaxy", "cosmology", "solarsystem"];

const CATEGORY_EMOJI: Record<string, string> = {
  blackhole: "\uD83D\uDD73\uFE0F",
  stellar: "\u2B50",
  galaxy: "\uD83C\uDF0C",
  cosmology: "\uD83D\uDD2D",
  solarsystem: "\uD83E\uDE90",
  general: "\uD83D\uDCD6",
};

const CATEGORY_COLOR: Record<string, string> = {
  blackhole: "#7c3aed",
  stellar: "#d97706",
  galaxy: "#2563eb",
  cosmology: "#4338ca",
  solarsystem: "#16a34a",
  general: "#6b7280",
};

export default function CardsPage() {
  const router = useRouter();
  const [cards, setCards] = useState<Card[]>([]);
  const [filter, setFilter] = useState("all");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    const params = new URLSearchParams();
    if (filter !== "all") params.set("category", filter);
    fetch(`/api/explore/cards?${params}`)
      .then((r) => r.json())
      .then((data) => {
        setCards(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [filter]);

  return (
    <div>
      <h2 style={{ fontSize: "1.3rem", margin: "0 0 1rem" }}>Knowledge Cards</h2>

      <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap", marginBottom: "1.5rem" }}>
        {CATEGORIES.map((cat) => (
          <button
            key={cat}
            onClick={() => setFilter(cat)}
            style={{
              padding: "0.35rem 0.75rem",
              border: filter === cat ? "2px solid #4f46e5" : "1px solid #d1d5db",
              borderRadius: "9999px",
              background: filter === cat ? "#eef2ff" : "#fff",
              color: filter === cat ? "#4f46e5" : "#374151",
              cursor: "pointer",
              fontSize: "0.85rem",
              fontWeight: filter === cat ? 600 : 400,
            }}
          >
            {cat === "all" ? "All" : `${CATEGORY_EMOJI[cat] || ""} ${cat}`}
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
              }}
              onMouseOver={(e) => (e.currentTarget.style.boxShadow = "0 4px 12px rgba(0,0,0,0.08)")}
              onMouseOut={(e) => (e.currentTarget.style.boxShadow = "none")}
            >
              <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "0.5rem" }}>
                <span style={{ fontSize: "1.3rem" }}>{CATEGORY_EMOJI[card.category] || "\uD83D\uDCD6"}</span>
                <span style={{ fontWeight: 600, fontSize: "1rem" }}>{card.title}</span>
              </div>
              <p style={{ fontSize: "0.85rem", color: "#4b5563", margin: "0 0 0.75rem", lineHeight: 1.4 }}>
                {card.summary || "No content yet."}
              </p>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
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
                <span style={{ fontSize: "0.75rem", color: "#9ca3af" }}>
                  {card.edit_count} edits
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
