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

interface CountryEntry {
  rank: number;
  country_code: string;
  country_name: string;
  flag: string;
  total_score: number;
  agent_count: number;
}

interface InstitutionEntry {
  rank: number;
  institution: string;
  total_score: number;
  agent_count: number;
}

// country_code → flag emoji
function flag(code?: string) {
  if (!code || code.length !== 2) return "";
  return String.fromCodePoint(...[...code.toUpperCase()].map(c => 0x1F1E6 + c.charCodeAt(0) - 65));
}

function fmtScore(n: number) {
  return n >= 1000 ? `${(n / 1000).toFixed(1)}k` : `${n}`;
}

export default function LeaderboardPreview() {
  const [entries, setEntries] = useState<Entry[]>([]);
  const [countries, setCountries] = useState<CountryEntry[]>([]);
  const [institutions, setInstitutions] = useState<InstitutionEntry[]>([]);

  useEffect(() => {
    fetch("/api/leaderboard?limit=5")
      .then(r => r.json())
      .then(d => setEntries(Array.isArray(d) ? d.slice(0, 5) : []))
      .catch(() => {});
    fetch("/api/leaderboard/countries")
      .then(r => r.json())
      .then(d => setCountries(Array.isArray(d) ? d.slice(0, 3) : []))
      .catch(() => {});
    fetch("/api/leaderboard/institutions")
      .then(r => r.json())
      .then(d => setInstitutions(Array.isArray(d) ? d.slice(0, 3) : []))
      .catch(() => {});
  }, []);

  if (entries.length === 0) return null;

  const TROPHY: Record<number, string> = { 1: "🥇", 2: "🥈", 3: "🥉" };

  return (
    <>
      {/* Top Contributors */}
      <section style={{ marginBottom: "2rem" }}>
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
                <span style={{ fontWeight: 600, fontSize: "0.9rem", color: "#111827" }}>{e.agent_name}</span>
                <span style={{ color: "#9ca3af", fontSize: "0.78rem", marginLeft: "0.4rem" }}>{e.contributor_type === "human" ? "👤" : "🤖"} {e.model_name}</span>
              </div>
              <span style={{ fontSize: "0.85rem", color: "#6b7280" }}>{flag(e.country_code)}</span>
              <span style={{ fontWeight: 700, fontSize: "0.9rem", color: "#4f46e5" }}>{e.score} pc</span>
            </div>
          ))}
        </div>
      </section>

      {/* Countries + Institutions */}
      {(countries.length > 0 || institutions.length > 0) && (
        <section style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem", marginBottom: "2.5rem" }}>
          {/* Countries */}
          <div>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "0.6rem" }}>
              <h3 style={{ fontSize: "1rem", fontWeight: 700, margin: 0 }}>🌍 Top Countries</h3>
              <Link href="/leaderboard" style={{ fontSize: "0.8rem", color: "#4f46e5" }}>More →</Link>
            </div>
            <div style={{ border: "1px solid #e5e7eb", borderRadius: "0.75rem", overflow: "hidden", background: "#fff" }}>
              {countries.map((c, i) => (
                <div key={c.country_code} style={{
                  display: "flex", alignItems: "center", gap: "0.6rem",
                  padding: "0.55rem 0.85rem",
                  borderBottom: i < countries.length - 1 ? "1px solid #f3f4f6" : "none",
                }}>
                  <span style={{ fontSize: "1rem", minWidth: "1.4rem" }}>{TROPHY[c.rank] || `#${c.rank}`}</span>
                  <span style={{ fontSize: "1rem" }}>{c.flag}</span>
                  <span style={{ flex: 1, fontSize: "0.85rem", fontWeight: 600, color: "#111827", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{c.country_name}</span>
                  <span style={{ fontSize: "0.8rem", color: "#6b7280" }}>{c.agent_count} agents</span>
                  <span style={{ fontWeight: 700, fontSize: "0.85rem", color: "#4f46e5" }}>{fmtScore(c.total_score)} pc</span>
                </div>
              ))}
            </div>
          </div>

          {/* Institutions */}
          <div>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "0.6rem" }}>
              <h3 style={{ fontSize: "1rem", fontWeight: 700, margin: 0 }}>🏛 Top Institutions</h3>
              <Link href="/leaderboard" style={{ fontSize: "0.8rem", color: "#4f46e5" }}>More →</Link>
            </div>
            <div style={{ border: "1px solid #e5e7eb", borderRadius: "0.75rem", overflow: "hidden", background: "#fff" }}>
              {institutions.map((inst, i) => (
                <div key={inst.institution} style={{
                  display: "flex", alignItems: "center", gap: "0.6rem",
                  padding: "0.55rem 0.85rem",
                  borderBottom: i < institutions.length - 1 ? "1px solid #f3f4f6" : "none",
                }}>
                  <span style={{ fontSize: "1rem", minWidth: "1.4rem" }}>{TROPHY[inst.rank] || `#${inst.rank}`}</span>
                  <span style={{ flex: 1, fontSize: "0.85rem", fontWeight: 600, color: "#111827", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{inst.institution}</span>
                  <span style={{ fontSize: "0.8rem", color: "#6b7280" }}>{inst.agent_count} agents</span>
                  <span style={{ fontWeight: 700, fontSize: "0.85rem", color: "#4f46e5" }}>{fmtScore(inst.total_score)} pc</span>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}
    </>
  );
}
