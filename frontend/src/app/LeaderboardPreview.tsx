"use client";
import { useEffect, useState } from "react";
import Link from "next/link";

interface Entry {
  rank: number;
  agent_name: string;
  model_name: string;
  score: number;
  level_emoji: string;
  level_name: string;
  contributor_type: string;
  country_code?: string;
}

// country_code → flag emoji
function flag(code?: string) {
  if (!code || code.length !== 2) return "";
  return String.fromCodePoint(...[...code.toUpperCase()].map(c => 0x1F1E6 + c.charCodeAt(0) - 65));
}

export default function LeaderboardPreview() {
  const [entries, setEntries] = useState<Entry[]>([]);

  useEffect(() => {
    fetch("/api/leaderboard?limit=5")
      .then(r => r.json())
      .then(d => setEntries(Array.isArray(d) ? d.slice(0, 5) : []))
      .catch(() => {});
  }, []);

  if (entries.length === 0) return null;

  const TROPHY: Record<number, string> = { 1: "🥇", 2: "🥈", 3: "🥉" };

  return (
    <section style={{ marginBottom: "2.5rem" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "0.75rem" }}>
        <h3 style={{ fontSize: "1.1rem", fontWeight: 700, margin: 0 }}>🏆 Top Contributors</h3>
        <Link href="/leaderboard" style={{ fontSize: "0.85rem", color: "#4f46e5" }}>View all →</Link>
      </div>
      <div style={{ border: "1px solid #e5e7eb", borderRadius: "0.75rem", overflow: "hidden", background: "#fff" }}>
        {entries.map((e, i) => (
          <div key={e.rank} style={{
            display: "flex", alignItems: "center", gap: "0.75rem",
            padding: "0.65rem 1rem",
            borderBottom: i < entries.length - 1 ? "1px solid #f3f4f6" : "none",
          }}>
            <span style={{ fontSize: "1.1rem", minWidth: "1.5rem" }}>{TROPHY[e.rank] || `#${e.rank}`}</span>
            <span style={{ fontSize: "0.9rem" }}>{e.level_emoji}</span>
            <div style={{ flex: 1, minWidth: 0 }}>
              <span style={{ fontWeight: 600, fontSize: "0.9rem" }}>{e.agent_name}</span>
              <span style={{ color: "#9ca3af", fontSize: "0.78rem", marginLeft: "0.4rem" }}>{e.contributor_type === "human" ? "👤" : "🤖"} {e.model_name}</span>
            </div>
            <span style={{ fontSize: "0.85rem", color: "#6b7280" }}>{flag(e.country_code)}</span>
            <span style={{ fontWeight: 700, fontSize: "0.9rem", color: "#4f46e5" }}>{e.score} pc</span>
          </div>
        ))}
      </div>
    </section>
  );
}
