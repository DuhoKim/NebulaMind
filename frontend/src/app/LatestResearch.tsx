"use client";
import { useEffect, useState } from "react";
import Link from "next/link";

interface Paper {
  arxiv_id: string;
  title: string;
  authors: string[];
  abstract_summary: string;
  submitted: string;
  related_pages: string[];
  url: string;
  category: string;
}

function timeAgo(dateStr: string): string {
  const diff = Date.now() - new Date(dateStr).getTime();
  const days = Math.floor(diff / 86400000);
  if (days === 0) return "today";
  if (days === 1) return "yesterday";
  return `${days}d ago`;
}

const CATEGORY_LABELS: Record<string, string> = {
  "astro-ph.GA": "Galaxies",
  "astro-ph.CO": "Cosmology",
  "astro-ph.HE": "High Energy",
  "astro-ph.SR": "Stellar",
};

export default function LatestResearch() {
  const [papers, setPapers] = useState<Paper[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch from multiple categories and combine
    Promise.all([
      fetch("/api/research/arxiv?limit=3&category=astro-ph.CO").then(r => r.json()),
      fetch("/api/research/arxiv?limit=2&category=astro-ph.GA").then(r => r.json()),
    ])
      .then(([co, ga]) => {
        const combined = [...(Array.isArray(co) ? co : []), ...(Array.isArray(ga) ? ga : [])];
        // Sort by submitted date, take top 5
        combined.sort((a, b) => b.submitted.localeCompare(a.submitted));
        setPapers(combined.slice(0, 5));
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "0.75rem" }}>
        <h3 style={{ fontSize: "1.1rem", fontWeight: 700, margin: 0 }}>📡 Latest Research</h3>
        <Link href="/research" style={{ fontSize: "0.85rem", color: "#4f46e5" }}>View all →</Link>
      </div>

      {loading ? (
        <div style={{ color: "#9ca3af", fontSize: "0.85rem", padding: "1rem 0" }}>Loading...</div>
      ) : papers.length === 0 ? (
        <div style={{ color: "#9ca3af", fontSize: "0.85rem", padding: "1rem 0" }}>No papers yet.</div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "0.6rem" }}>
          {papers.map(paper => (
            <div key={paper.arxiv_id} style={{ border: "1px solid #e5e7eb", borderRadius: "0.65rem", padding: "0.75rem", background: "#fff" }}>
              <div style={{ display: "flex", gap: "0.4rem", marginBottom: "0.3rem", alignItems: "center", flexWrap: "wrap" }}>
                <span style={{ fontSize: "0.68rem", background: "#eef2ff", color: "#4f46e5", padding: "0.1rem 0.4rem", borderRadius: "9999px", fontWeight: 600 }}>
                  {CATEGORY_LABELS[paper.category] || paper.category}
                </span>
                <span style={{ fontSize: "0.7rem", color: "#9ca3af" }}>{timeAgo(paper.submitted)}</span>
              </div>
              <a href={paper.url} target="_blank" rel="noopener noreferrer"
                style={{ fontWeight: 600, fontSize: "0.82rem", color: "#1f2937", textDecoration: "none", lineHeight: 1.4, display: "block", marginBottom: "0.25rem" }}>
                {paper.title.length > 90 ? paper.title.slice(0, 90) + "..." : paper.title}
              </a>
              {paper.abstract_summary && (
                <p style={{ margin: "0 0 0.3rem", fontSize: "0.76rem", color: "#6b7280", lineHeight: 1.4 }}>
                  {paper.abstract_summary.length > 100 ? paper.abstract_summary.slice(0, 100) + "..." : paper.abstract_summary}
                </p>
              )}
              {paper.related_pages.length > 0 && (
                <div style={{ display: "flex", gap: "0.3rem", flexWrap: "wrap" }}>
                  {paper.related_pages.slice(0, 2).map(slug => (
                    <Link key={slug} href={`/wiki/${slug}`}
                      style={{ fontSize: "0.7rem", color: "#4f46e5", background: "#eef2ff", padding: "0.1rem 0.35rem", borderRadius: "9999px", textDecoration: "none" }}>
                      🔗 {slug}
                    </Link>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
