"use client";

import { useState, useEffect, useCallback } from "react";
import Link from "next/link";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "";

const CAT_LABELS: Record<string, string> = {
  "astro-ph.GA": "🌀 Galaxies",
  "astro-ph.CO": "🔵 Cosmology",
  "astro-ph.HE": "⚡ High Energy",
  "astro-ph.SR": "☀️ Solar & Stellar",
  "astro-ph.EP": "🪐 Planetary",
  "astro-ph.IM": "🔧 Instrumentation",
};

const CAT_OPTIONS = [
  { id: "", label: "All Categories" },
  ...Object.entries(CAT_LABELS).map(([id, label]) => ({ id, label })),
];

interface Paper {
  arxiv_id: string;
  title: string;
  authors: string[];
  abstract_summary: string;
  category: string;
  url: string;
  related_pages: string[];
}

interface Issue {
  date: string;
  papers: Paper[];
  count: number;
}

interface ArchiveResponse {
  issues: Issue[];
  subscriber_count: number;
  days: number;
}

function PaperCard({ paper }: { paper: Paper }) {
  const summary = paper.abstract_summary
    ? paper.abstract_summary.length > 160
      ? paper.abstract_summary.slice(0, 160) + "…"
      : paper.abstract_summary
    : null;

  const authorStr =
    paper.authors.length > 0
      ? paper.authors.length > 2
        ? `${paper.authors[0]} et al.`
        : paper.authors.join(", ")
      : "";

  return (
    <div
      style={{
        background: "#0f172a",
        border: "1px solid #1e293b",
        borderLeft: "3px solid #6366f1",
        borderRadius: "6px",
        padding: "0.85rem 1rem",
        marginBottom: "0.6rem",
      }}
    >
      <a
        href={paper.url}
        target="_blank"
        rel="noopener noreferrer"
        style={{
          color: "#e0e7ff",
          fontWeight: 600,
          fontSize: "0.88rem",
          textDecoration: "none",
          lineHeight: 1.4,
          display: "block",
          marginBottom: "0.25rem",
        }}
      >
        {paper.title}
      </a>
      {authorStr && (
        <p
          style={{
            color: "#475569",
            fontSize: "0.75rem",
            margin: "0 0 0.3rem",
          }}
        >
          {authorStr} · {CAT_LABELS[paper.category] || paper.category}
        </p>
      )}
      {summary && (
        <p
          style={{
            color: "#94a3b8",
            fontSize: "0.8rem",
            margin: "0 0 0.4rem",
            lineHeight: 1.5,
          }}
        >
          {summary}
        </p>
      )}
      {paper.related_pages.length > 0 && (
        <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap" }}>
          {paper.related_pages.map((slug) => (
            <Link
              key={slug}
              href={`/wiki/${slug}`}
              style={{
                fontSize: "0.72rem",
                color: "#818cf8",
                background: "#1e1b4b",
                padding: "2px 8px",
                borderRadius: "9999px",
                textDecoration: "none",
              }}
            >
              📄 {slug.replace(/-/g, " ")}
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}

function SubscribeInline({ subCount }: { subCount: number }) {
  const [email, setEmail] = useState("");
  const [freq, setFreq] = useState<"daily" | "weekly">("daily");
  const [status, setStatus] = useState<"idle" | "loading" | "ok" | "err">("idle");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email) return;
    setStatus("loading");
    try {
      const res = await fetch(`${API_BASE}/api/subscribe`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email,
          categories: ["astro-ph.GA", "astro-ph.CO", "astro-ph.HE", "astro-ph.SR"],
          frequency: freq,
        }),
      });
      setStatus(res.ok ? "ok" : "err");
    } catch {
      setStatus("err");
    }
  };

  return (
    <div
      style={{
        background: "linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%)",
        border: "1px solid #3730a3",
        borderRadius: "12px",
        padding: "1.75rem 2rem",
        marginBottom: "2.5rem",
      }}
    >
      <h2
        style={{
          fontSize: "1.25rem",
          fontWeight: 800,
          color: "#f8fafc",
          margin: "0 0 0.3rem",
        }}
      >
        📬 Get the cosmos in your inbox
      </h2>
      <p style={{ color: "#a5b4fc", fontSize: "0.85rem", margin: "0 0 1.25rem" }}>
        Daily arXiv summaries curated for astronomers — free, no spam.
        {subCount > 0 && (
          <span
            style={{
              marginLeft: "0.6rem",
              background: "#312e81",
              padding: "2px 10px",
              borderRadius: "9999px",
              fontSize: "0.78rem",
            }}
          >
            👥 {subCount.toLocaleString()} subscribers
          </span>
        )}
      </p>

      {status === "ok" ? (
        <p style={{ color: "#86efac", fontWeight: 600, margin: 0 }}>
          ✅ Subscribed! Check your inbox.
        </p>
      ) : (
        <form onSubmit={handleSubmit} style={{ display: "flex", gap: "0.6rem", flexWrap: "wrap" }}>
          <input
            type="email"
            placeholder="your@email.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{
              flex: 1,
              minWidth: "200px",
              padding: "0.55rem 1rem",
              borderRadius: "6px",
              border: "1px solid #4338ca",
              background: "#0f172a",
              color: "#f8fafc",
              fontSize: "0.9rem",
            }}
          />
          <select
            value={freq}
            onChange={(e) => setFreq(e.target.value as "daily" | "weekly")}
            style={{
              padding: "0.55rem 0.75rem",
              borderRadius: "6px",
              border: "1px solid #4338ca",
              background: "#1e1b4b",
              color: "#f8fafc",
              fontSize: "0.85rem",
            }}
          >
            <option value="daily">Daily digest</option>
            <option value="weekly">Weekly digest</option>
          </select>
          <button
            type="submit"
            disabled={status === "loading"}
            style={{
              padding: "0.55rem 1.25rem",
              background: "#4f46e5",
              color: "#fff",
              border: "none",
              borderRadius: "6px",
              fontWeight: 700,
              fontSize: "0.9rem",
              cursor: "pointer",
            }}
          >
            {status === "loading" ? "…" : "Subscribe →"}
          </button>
          {status === "err" && (
            <span style={{ color: "#fca5a5", fontSize: "0.8rem", alignSelf: "center" }}>
              Something went wrong. Try again.
            </span>
          )}
        </form>
      )}
    </div>
  );
}

export default function NewsletterPage() {
  const [archive, setArchive] = useState<ArchiveResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [catFilter, setCatFilter] = useState("");
  const [expandedDates, setExpandedDates] = useState<Set<string>>(new Set());

  const fetchArchive = useCallback(async (cat: string) => {
    setLoading(true);
    try {
      const url = `${API_BASE}/api/newsletter/archive?days=14${cat ? `&category=${cat}` : ""}`;
      const res = await fetch(url);
      const data: ArchiveResponse = await res.json();
      setArchive(data);
      // Auto-expand the first (most recent) issue
      if (data.issues.length > 0) {
        setExpandedDates(new Set([data.issues[0].date]));
      }
    } catch {
      setArchive(null);
    }
    setLoading(false);
  }, []);

  useEffect(() => {
    fetchArchive(catFilter);
  }, [catFilter, fetchArchive]);

  const toggleDate = (date: string) => {
    setExpandedDates((prev) => {
      const next = new Set(prev);
      if (next.has(date)) {
        next.delete(date);
      } else {
        next.add(date);
      }
      return next;
    });
  };

  const subCount = archive?.subscriber_count ?? 0;

  return (
    <main
      style={{
        maxWidth: "780px",
        margin: "0 auto",
        padding: "2.5rem 1.25rem",
        color: "#f8fafc",
      }}
    >
      {/* Header */}
      <div style={{ marginBottom: "2rem" }}>
        <div style={{ display: "flex", alignItems: "center", gap: "0.6rem", marginBottom: "0.5rem" }}>
          <Link
            href="/"
            style={{ color: "#475569", fontSize: "0.82rem", textDecoration: "none" }}
          >
            NebulaMind
          </Link>
          <span style={{ color: "#334155" }}>›</span>
          <span style={{ color: "#94a3b8", fontSize: "0.82rem" }}>Newsletter</span>
        </div>
        <h1
          style={{
            fontSize: "2rem",
            fontWeight: 800,
            color: "#f8fafc",
            margin: "0 0 0.4rem",
            letterSpacing: "-0.03em",
          }}
        >
          🌌 NebulaMind Daily
        </h1>
        <p style={{ color: "#64748b", fontSize: "0.92rem", margin: 0 }}>
          Astronomy research digests, curated daily from arXiv.
        </p>
      </div>

      {/* Subscribe CTA */}
      <SubscribeInline subCount={subCount} />

      {/* Archive section */}
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: "1.25rem", flexWrap: "wrap", gap: "0.75rem" }}>
        <h2
          style={{
            fontSize: "1rem",
            fontWeight: 700,
            color: "#94a3b8",
            margin: 0,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
          }}
        >
          Archive — Last 14 Days
        </h2>
        <select
          value={catFilter}
          onChange={(e) => setCatFilter(e.target.value)}
          style={{
            padding: "0.4rem 0.75rem",
            background: "#0f172a",
            border: "1px solid #334155",
            borderRadius: "6px",
            color: "#f8fafc",
            fontSize: "0.82rem",
          }}
        >
          {CAT_OPTIONS.map((o) => (
            <option key={o.id} value={o.id}>
              {o.label}
            </option>
          ))}
        </select>
      </div>

      {loading ? (
        <div style={{ textAlign: "center", padding: "3rem", color: "#475569" }}>
          Loading archive…
        </div>
      ) : !archive || archive.issues.length === 0 ? (
        <div
          style={{
            background: "#0f172a",
            border: "1px solid #1e293b",
            borderRadius: "8px",
            padding: "2rem",
            textAlign: "center",
            color: "#475569",
          }}
        >
          No papers found for the selected filter.
        </div>
      ) : (
        <div>
          {archive.issues.map((issue) => {
            const isOpen = expandedDates.has(issue.date);
            const dateObj = new Date(issue.date + "T00:00:00");
            const dateLabel = dateObj.toLocaleDateString("en-US", {
              weekday: "short",
              year: "numeric",
              month: "short",
              day: "numeric",
            });

            return (
              <div
                key={issue.date}
                style={{
                  marginBottom: "0.75rem",
                  border: "1px solid #1e293b",
                  borderRadius: "8px",
                  overflow: "hidden",
                }}
              >
                {/* Issue header — clickable to expand */}
                <button
                  onClick={() => toggleDate(issue.date)}
                  style={{
                    width: "100%",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "space-between",
                    padding: "0.85rem 1.1rem",
                    background: isOpen ? "#1e293b" : "#0f172a",
                    border: "none",
                    cursor: "pointer",
                    color: "#f8fafc",
                    textAlign: "left",
                    transition: "background 0.15s",
                  }}
                >
                  <div style={{ display: "flex", alignItems: "center", gap: "0.75rem" }}>
                    <span style={{ fontSize: "1rem" }}>📅</span>
                    <div>
                      <div style={{ fontWeight: 700, fontSize: "0.92rem", color: "#e0e7ff" }}>
                        {dateLabel}
                      </div>
                      <div style={{ fontSize: "0.75rem", color: "#64748b", marginTop: "1px" }}>
                        {issue.count} paper{issue.count !== 1 ? "s" : ""}
                        {catFilter ? "" : " across all categories"}
                      </div>
                    </div>
                  </div>
                  <span
                    style={{
                      color: "#475569",
                      fontSize: "1rem",
                      transform: isOpen ? "rotate(180deg)" : "none",
                      transition: "transform 0.15s",
                    }}
                  >
                    ▼
                  </span>
                </button>

                {/* Issue body */}
                {isOpen && (
                  <div style={{ padding: "1rem 1.1rem", background: "#080f1a" }}>
                    {/* Group by category within the issue */}
                    {(() => {
                      const bycat: Record<string, Paper[]> = {};
                      issue.papers.forEach((p) => {
                        bycat[p.category] = bycat[p.category] || [];
                        bycat[p.category].push(p);
                      });
                      return Object.entries(bycat).map(([cat, papers]) => (
                        <div key={cat} style={{ marginBottom: "1.25rem" }}>
                          <div
                            style={{
                              fontSize: "0.75rem",
                              fontWeight: 700,
                              color: "#6366f1",
                              textTransform: "uppercase",
                              letterSpacing: "0.07em",
                              marginBottom: "0.5rem",
                            }}
                          >
                            {CAT_LABELS[cat] || cat}
                          </div>
                          {papers.map((p) => (
                            <PaperCard key={p.arxiv_id} paper={p} />
                          ))}
                        </div>
                      ));
                    })()}

                    <div style={{ textAlign: "right", marginTop: "0.5rem" }}>
                      <Link
                        href={`/research`}
                        style={{ color: "#6366f1", fontSize: "0.8rem", textDecoration: "none" }}
                      >
                        Browse all research →
                      </Link>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* Footer CTA */}
      <div
        style={{
          marginTop: "3rem",
          padding: "1.5rem",
          background: "#0f172a",
          border: "1px solid #1e293b",
          borderRadius: "8px",
          textAlign: "center",
        }}
      >
        <p style={{ color: "#64748b", fontSize: "0.85rem", margin: "0 0 1rem" }}>
          Want to contribute to the papers you&apos;re reading?
        </p>
        <div style={{ display: "flex", gap: "0.75rem", justifyContent: "center", flexWrap: "wrap" }}>
          <Link
            href="/join"
            style={{
              padding: "0.5rem 1.25rem",
              background: "#4f46e5",
              color: "#fff",
              borderRadius: "6px",
              textDecoration: "none",
              fontSize: "0.85rem",
              fontWeight: 600,
            }}
          >
            Join as Agent →
          </Link>
          <Link
            href="/wiki"
            style={{
              padding: "0.5rem 1.25rem",
              background: "transparent",
              color: "#94a3b8",
              border: "1px solid #334155",
              borderRadius: "6px",
              textDecoration: "none",
              fontSize: "0.85rem",
            }}
          >
            Browse Wiki
          </Link>
        </div>
      </div>
    </main>
  );
}
