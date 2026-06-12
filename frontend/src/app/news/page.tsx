"use client";

import React, { useEffect, useState, useMemo } from "react";

interface NewsItem {
  id: number;
  slug: string;
  title: string;
  kind: string;
  track: string;
  summary: string | null;
  occurs_at: string | null;
  occurs_at_confidence: string;
  occurrence_status: string;
  source_url: string | null;
  data_portal_urls: string | null;
  featured: boolean;
  credibility_score: number | null;
  facility_slug: string | null;
  facility_name: string | null;
  facility_operator: string | null;
  facility_url: string | null;
}

const FACILITY_COLORS: Record<string, { bg: string; text: string; border: string }> = {
  desi:         { bg: "rgba(251,146,60,0.15)",  text: "#fb923c", border: "rgba(251,146,60,0.4)" },
  jwst:         { bg: "rgba(96,165,250,0.15)",  text: "#60a5fa", border: "rgba(96,165,250,0.4)" },
  euclid:       { bg: "rgba(74,222,128,0.15)",  text: "#4ade80", border: "rgba(74,222,128,0.4)" },
  "lsst-rubin": { bg: "rgba(167,139,250,0.15)", text: "#a78bfa", border: "rgba(167,139,250,0.4)" },
  rubin:        { bg: "rgba(167,139,250,0.15)", text: "#a78bfa", border: "rgba(167,139,250,0.4)" },
  alma:         { bg: "rgba(248,113,113,0.15)", text: "#f87171", border: "rgba(248,113,113,0.4)" },
  vla:          { bg: "rgba(45,212,191,0.15)",  text: "#2dd4bf", border: "rgba(45,212,191,0.4)" },
};
const DEFAULT_FAC = { bg: "rgba(148,163,184,0.15)", text: "#94a3b8", border: "rgba(148,163,184,0.4)" };

const KIND_CONFIG: Record<string, { label: string; bg: string; text: string }> = {
  release:       { label: "Data Release",  bg: "rgba(96,165,250,0.15)",  text: "#60a5fa" },
  proposal_call: { label: "Proposal Call", bg: "rgba(251,191,36,0.15)",  text: "#fbbf24" },
  milestone:     { label: "Milestone",     bg: "rgba(167,139,250,0.15)", text: "#a78bfa" },
  facility_news: { label: "Facility News", bg: "rgba(74,222,128,0.15)",  text: "#4ade80" },
  news:          { label: "Facility News", bg: "rgba(74,222,128,0.15)",  text: "#4ade80" },
};
const DEFAULT_KIND = { label: "News", bg: "rgba(148,163,184,0.15)", text: "#94a3b8" };

// 3-track definitions (Data → Tools → Results)
const TRACKS = [
  {
    id: "data",
    label: "Data",
    icon: "📦",
    desc: "Survey data releases and new datasets from observatories",
    color: "#60a5fa",
    border: "rgba(96,165,250,0.25)",
    kinds: ["release", "first_light"],
  },
  {
    id: "tools",
    label: "Tools",
    icon: "🔧",
    desc: "Proposal deadlines, instrument milestones, and facility updates",
    color: "#fbbf24",
    border: "rgba(251,191,36,0.25)",
    kinds: ["proposal_call", "milestone"],
  },
  {
    id: "results",
    label: "Results",
    icon: "🔭",
    desc: "Science announcements, discoveries, and facility news",
    color: "#4ade80",
    border: "rgba(74,222,128,0.25)",
    kinds: ["facility_news", "news"],
  },
] as const;

const ALL_TRACK_KINDS = new Set(TRACKS.flatMap(t => t.kinds as readonly string[]));

type TrackId = "data" | "tools" | "results" | "all";

function facilityColor(slug: string | null) {
  if (!slug) return DEFAULT_FAC;
  return FACILITY_COLORS[slug.toLowerCase()] ?? DEFAULT_FAC;
}

function kindConfig(kind: string) {
  return KIND_CONFIG[kind] ?? DEFAULT_KIND;
}

function credBadge(score: number | null) {
  if (score === null) return null;
  if (score >= 0.8) return { label: "✓ Verified",  bg: "rgba(74,222,128,0.15)",  text: "#4ade80" };
  if (score >= 0.5) return { label: "Reviewed",    bg: "rgba(251,191,36,0.15)",  text: "#fbbf24" };
  return              { label: "Unverified",   bg: "rgba(248,113,113,0.15)", text: "#f87171" };
}

function timeAgo(iso: string): string {
  const diff = Date.now() - new Date(iso).getTime();
  const h = Math.floor(diff / 3_600_000);
  if (h < 1) return "just now";
  if (h < 24) return `${h}h ago`;
  const d = Math.floor(h / 24);
  if (d < 30) return `${d}d ago`;
  return new Date(iso).toLocaleDateString("en-US", { month: "short", day: "numeric" });
}

function FeaturedCard({ item }: { item: NewsItem }) {
  const fc = facilityColor(item.facility_slug);
  const kc = kindConfig(item.kind);
  const cb = credBadge(item.credibility_score);

  return (
    <div style={{
      background: "#1e293b",
      border: `1px solid ${fc.border}`,
      borderRadius: "10px",
      padding: "1.25rem",
      position: "relative",
      boxShadow: `0 0 20px ${fc.bg}`,
    }}>
      <div style={{ position: "absolute", top: "10px", right: "10px", fontSize: "0.65rem", fontWeight: 600, color: "#fbbf24", background: "rgba(251,191,36,0.12)", border: "1px solid rgba(251,191,36,0.3)", borderRadius: "999px", padding: "2px 8px" }}>
        ★ Featured
      </div>

      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "0.75rem", flexWrap: "wrap" }}>
        {item.facility_name && (
          <span style={{ fontSize: "0.7rem", fontWeight: 600, color: fc.text, background: fc.bg, border: `1px solid ${fc.border}`, borderRadius: "4px", padding: "2px 8px" }}>
            {item.facility_name}
          </span>
        )}
        <span style={{ fontSize: "0.7rem", fontWeight: 600, color: kc.text, background: kc.bg, borderRadius: "4px", padding: "2px 8px" }}>
          {kc.label}
        </span>
        {cb && (
          <span style={{ fontSize: "0.7rem", fontWeight: 600, color: cb.text, background: cb.bg, borderRadius: "4px", padding: "2px 8px" }}>
            {cb.label}
          </span>
        )}
      </div>

      <h3 style={{ fontSize: "0.95rem", fontWeight: 600, color: "#f8fafc", margin: "0 0 0.6rem", lineHeight: 1.4 }}>
        {item.source_url ? (
          <a href={item.source_url} target="_blank" rel="noopener noreferrer" style={{ color: "inherit", textDecoration: "none" }}
            onMouseEnter={e => (e.currentTarget.style.color = "#a5b4fc")}
            onMouseLeave={e => (e.currentTarget.style.color = "#f8fafc")}>
            {item.title}
          </a>
        ) : item.title}
      </h3>

      {item.summary && (
        <p style={{ fontSize: "0.825rem", color: "#94a3b8", margin: "0 0 0.75rem", lineHeight: 1.6 }}>
          {item.summary}
        </p>
      )}

      {item.source_url && (
        <a href={item.source_url} target="_blank" rel="noopener noreferrer"
          style={{ fontSize: "0.75rem", color: "#6366f1", textDecoration: "none", fontWeight: 500 }}
          onMouseEnter={e => (e.currentTarget.style.color = "#a5b4fc")}
          onMouseLeave={e => (e.currentTarget.style.color = "#6366f1")}>
          Read source →
        </a>
      )}
    </div>
  );
}

function NewsCard({ item }: { item: NewsItem }) {
  const fc = facilityColor(item.facility_slug);
  const kc = kindConfig(item.kind);
  const cb = credBadge(item.credibility_score);

  return (
    <div
      style={{
        background: "#1e293b",
        border: "1px solid #334155",
        borderRadius: "8px",
        padding: "1rem",
        transition: "border-color 0.15s",
      }}
      onMouseEnter={e => ((e.currentTarget as HTMLElement).style.borderColor = "#475569")}
      onMouseLeave={e => ((e.currentTarget as HTMLElement).style.borderColor = "#334155")}
    >
      <div style={{ display: "flex", gap: "0.4rem", marginBottom: "0.6rem", flexWrap: "wrap" }}>
        {item.facility_name && (
          <span style={{ fontSize: "0.65rem", fontWeight: 600, color: fc.text, background: fc.bg, border: `1px solid ${fc.border}`, borderRadius: "4px", padding: "1px 6px" }}>
            {item.facility_name}
          </span>
        )}
        <span style={{ fontSize: "0.65rem", fontWeight: 600, color: kc.text, background: kc.bg, borderRadius: "4px", padding: "1px 6px" }}>
          {kc.label}
        </span>
        {cb && (
          <span style={{ fontSize: "0.65rem", fontWeight: 600, color: cb.text, background: cb.bg, borderRadius: "4px", padding: "1px 6px" }}>
            {cb.label}
          </span>
        )}
      </div>

      <h3 style={{ fontSize: "0.875rem", fontWeight: 600, color: "#f1f5f9", margin: "0 0 0.5rem", lineHeight: 1.4 }}>
        {item.source_url ? (
          <a href={item.source_url} target="_blank" rel="noopener noreferrer" style={{ color: "inherit", textDecoration: "none" }}
            onMouseEnter={e => (e.currentTarget.style.color = "#a5b4fc")}
            onMouseLeave={e => (e.currentTarget.style.color = "#f1f5f9")}>
            {item.title}
          </a>
        ) : item.title}
      </h3>

      {item.summary && (
        <p style={{ fontSize: "0.8rem", color: "#94a3b8", margin: "0 0 0.75rem", lineHeight: 1.55,
          display: "-webkit-box", WebkitLineClamp: 3, WebkitBoxOrient: "vertical", overflow: "hidden" } as React.CSSProperties}>
          {item.summary}
        </p>
      )}

      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        {item.source_url && (
          <a href={item.source_url} target="_blank" rel="noopener noreferrer"
            style={{ fontSize: "0.72rem", color: "#6366f1", textDecoration: "none", fontWeight: 500 }}
            onMouseEnter={e => (e.currentTarget.style.color = "#a5b4fc")}
            onMouseLeave={e => (e.currentTarget.style.color = "#6366f1")}>
            Source →
          </a>
        )}
        {item.occurs_at && (
          <span style={{ fontSize: "0.7rem", color: "#475569" }}>
            {timeAgo(item.occurs_at)}
          </span>
        )}
      </div>
    </div>
  );
}

function TrackSection({
  track, items, collapsed, onToggle,
}: {
  track: typeof TRACKS[number];
  items: NewsItem[];
  collapsed: boolean;
  onToggle: () => void;
}) {
  return (
    <section style={{ marginBottom: "2.5rem" }}>
      {/* Track header */}
      <button
        onClick={onToggle}
        style={{
          display: "flex", alignItems: "center", gap: "0.75rem",
          width: "100%", textAlign: "left", background: "transparent",
          border: "none", cursor: "pointer", padding: 0, marginBottom: "1rem",
        }}
      >
        <div style={{
          display: "flex", alignItems: "center", gap: "0.5rem", flex: 1,
          borderBottom: `2px solid ${track.border}`, paddingBottom: "0.5rem",
        }}>
          <span style={{ fontSize: "1.1rem" }}>{track.icon}</span>
          <h2 style={{ fontSize: "1rem", fontWeight: 700, color: track.color, margin: 0 }}>
            {track.label}
          </h2>
          <span style={{
            fontSize: "0.7rem", fontWeight: 600, color: track.color,
            background: `${track.color}18`, border: `1px solid ${track.border}`,
            borderRadius: "999px", padding: "1px 8px",
          }}>
            {items.length}
          </span>
          <span style={{ fontSize: "0.8rem", color: "#475569", fontWeight: 400, marginLeft: "0.25rem" }}>
            {track.desc}
          </span>
        </div>
        <span style={{ fontSize: "0.75rem", color: "#475569", paddingBottom: "0.5rem" }}>
          {collapsed ? "▶" : "▼"}
        </span>
      </button>

      {!collapsed && (
        items.length === 0 ? (
          <div style={{ color: "#475569", fontSize: "0.85rem", padding: "1rem 0" }}>
            No {track.label.toLowerCase()} items available.
          </div>
        ) : (
          <div style={{ display: "grid", gap: "0.875rem", gridTemplateColumns: "repeat(auto-fill, minmax(290px, 1fr))" }}>
            {items.map(item => <NewsCard key={item.id} item={item} />)}
          </div>
        )
      )}
    </section>
  );
}

type NewsTab = "editorial" | "arxiv" | "newsletter";

function EditorialContent() {
  const [items, setItems] = useState<NewsItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<TrackId>("all");
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({});

  const API = process.env.NEXT_PUBLIC_API_URL || "";

  useEffect(() => {
    fetch(`${API}/api/calendar/?limit=100&past_days=180&upcoming_days=730`)
      .then(r => r.json())
      .then((data: NewsItem[]) => {
        const sorted = [...data].sort((a, b) => {
          if (a.featured && !b.featured) return -1;
          if (!a.featured && b.featured) return 1;
          const ta = a.occurs_at ? new Date(a.occurs_at).getTime() : 0;
          const tb = b.occurs_at ? new Date(b.occurs_at).getTime() : 0;
          return tb - ta;
        });
        setItems(sorted);
      })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [API]);

  const featured = useMemo(() => items.filter(i => i.featured), [items]);

  const trackItems = useMemo(() => {
    const nonFeatured = items.filter(i => !i.featured);
    const mapped = Object.fromEntries(
      TRACKS.map(t => [t.id, nonFeatured.filter(i => t.kinds.includes(i.kind as never))])
    ) as Record<string, NewsItem[]>;
    mapped["more"] = nonFeatured.filter(i => !ALL_TRACK_KINDS.has(i.kind));
    return mapped;
  }, [items]);

  const toggleCollapsed = (id: string) => {
    setCollapsed(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const visibleTracks = activeTab === "all" ? TRACKS : TRACKS.filter(t => t.id === activeTab);

  return (
    <div>

        {/* Header */}
        <div style={{ marginBottom: "2rem" }}>
          <p style={{ color: "#64748b", fontSize: "0.9rem", margin: 0 }}>
            Curated daily for professional astronomers. AI-reviewed across Data, Tools, and Results.
          </p>
        </div>

        {/* Track tabs */}
        <div style={{ display: "flex", gap: "0.4rem", marginBottom: "2rem", flexWrap: "wrap" }}>
          <button
            onClick={() => setActiveTab("all")}
            style={{
              padding: "6px 16px", borderRadius: "999px", border: "1px solid",
              borderColor: activeTab === "all" ? "#6366f1" : "#334155",
              background: activeTab === "all" ? "rgba(99,102,241,0.15)" : "transparent",
              color: activeTab === "all" ? "#a5b4fc" : "#64748b",
              fontSize: "0.82rem", fontWeight: 500, cursor: "pointer", transition: "all 0.15s",
            }}
          >
            All
          </button>
          {TRACKS.map(t => (
            <button
              key={t.id}
              onClick={() => setActiveTab(t.id)}
              style={{
                padding: "6px 16px", borderRadius: "999px", border: "1px solid",
                borderColor: activeTab === t.id ? t.color : "#334155",
                background: activeTab === t.id ? `${t.color}18` : "transparent",
                color: activeTab === t.id ? t.color : "#64748b",
                fontSize: "0.82rem", fontWeight: 500, cursor: "pointer", transition: "all 0.15s",
              }}
            >
              {t.icon} {t.label}
              {trackItems[t.id]?.length > 0 && (
                <span style={{ marginLeft: "5px", opacity: 0.7, fontSize: "0.72rem" }}>
                  ({trackItems[t.id].length})
                </span>
              )}
            </button>
          ))}
        </div>

        {loading ? (
          <div style={{ textAlign: "center", padding: "4rem", color: "#475569" }}>Loading news…</div>
        ) : (
          <>
            {/* Featured section — shown in All view or when viewing any specific track */}
            {featured.length > 0 && (
              <div style={{ marginBottom: "2.5rem" }}>
                <h2 style={{
                  fontSize: "0.72rem", fontWeight: 600, color: "#64748b",
                  textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: "1rem",
                }}>
                  Featured Today
                </h2>
                <div style={{ display: "grid", gap: "1rem", gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))" }}>
                  {featured
                    .filter(i => activeTab === "all" || TRACKS.find(t => t.id === activeTab)?.kinds.includes(i.kind as never))
                    .map(item => <FeaturedCard key={item.id} item={item} />)}
                </div>
              </div>
            )}

            {/* 3-track sections: Data → Tools → Results */}
            {visibleTracks.map(track => (
              <TrackSection
                key={track.id}
                track={track}
                items={trackItems[track.id] || []}
                collapsed={!!collapsed[track.id]}
                onToggle={() => toggleCollapsed(track.id)}
              />
            ))}

            {/* Uncategorized items (other, unknown kinds) */}
            {activeTab === "all" && trackItems["more"]?.length > 0 && (
              <div style={{ marginTop: "2rem" }}>
                <h2 style={{ fontSize: "0.72rem", fontWeight: 600, color: "#475569", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: "1rem" }}>
                  More
                </h2>
                <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
                  {trackItems["more"].map(item => (
                    <a key={item.id} href={item.source_url || "#"} target="_blank" rel="noopener noreferrer"
                      style={{ display: "block", padding: "0.75rem 1rem", borderRadius: "8px", background: "rgba(30,41,59,0.6)", border: "1px solid #1e293b", textDecoration: "none", color: "inherit" }}>
                      <div style={{ fontSize: "0.85rem", fontWeight: 600, color: "#cbd5e1" }}>{item.title}</div>
                      {item.summary && <div style={{ fontSize: "0.78rem", color: "#64748b", marginTop: "0.25rem" }}>{item.summary}</div>}
                    </a>
                  ))}
                </div>
              </div>
            )}
          </>
        )}
    </div>
  );
}

export default function NewsPage() {
  const [newsTab, setNewsTab] = useState<NewsTab>("editorial");
  const [ResearchPage, setResearchPage] = useState<React.ComponentType | null>(null);
  const [NewsletterPage, setNewsletterPage] = useState<React.ComponentType | null>(null);

  useEffect(() => {
    if (newsTab === "arxiv" && !ResearchPage) {
      import("../research/page").then((m) => setResearchPage(() => m.default));
    }
    if (newsTab === "newsletter" && !NewsletterPage) {
      import("../newsletter/page").then((m) => setNewsletterPage(() => m.default));
    }
  }, [newsTab, ResearchPage, NewsletterPage]);

  return (
    <div>
      {/* Page header */}
      <div style={{ marginBottom: "1rem" }}>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 700, color: "#f8fafc", margin: 0 }}>
          🌌 News
        </h1>
      </div>

      {/* Tab bar */}
      <div
        style={{
          display: "flex",
          gap: 0,
          borderBottom: "1px solid #334155",
          marginBottom: "1.5rem",
        }}
      >
        {(["editorial", "arxiv", "newsletter"] as NewsTab[]).map((t) => (
          <button
            key={t}
            onClick={() => setNewsTab(t)}
            style={{
              padding: "0.5rem 1.25rem",
              fontSize: "0.875rem",
              fontWeight: 500,
              background: "transparent",
              border: "none",
              borderBottom: newsTab === t ? "2px solid #6366f1" : "2px solid transparent",
              color: newsTab === t ? "#f8fafc" : "#64748b",
              cursor: "pointer",
              marginBottom: "-1px",
              transition: "all 0.15s",
            }}
          >
            {t === "editorial" ? "Editorial" : t === "arxiv" ? "arXiv" : "Newsletter"}
          </button>
        ))}
      </div>

      {newsTab === "editorial" && <EditorialContent />}
      {newsTab === "arxiv" && (ResearchPage ? <ResearchPage /> : <div style={{ color: "#64748b", padding: "3rem", textAlign: "center" }}>Loading…</div>)}
      {newsTab === "newsletter" && (NewsletterPage ? <NewsletterPage /> : <div style={{ color: "#64748b", padding: "3rem", textAlign: "center" }}>Loading…</div>)}
    </div>
  );
}
