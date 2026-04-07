"use client";

import { useEffect, useState, useCallback } from "react";
import Link from "next/link";
import { RefreshCw } from "lucide-react";
import CommunitySpotlight from "../CommunitySpotlight";
import SubscribeWidget from "../SubscribeWidget";

interface ArxivPaper {
  arxiv_id: string;
  title: string;
  authors: string[];
  abstract_summary: string;
  submitted: string;
  related_pages: string[];
  url: string;
}

const CATEGORIES = [
  { id: "astro-ph.GA", label: "Galaxies", full: "Astrophysics of Galaxies" },
  { id: "astro-ph.HE", label: "High Energy", full: "High Energy Astrophysical Phenomena" },
  { id: "astro-ph.CO", label: "Cosmology", full: "Cosmology and Nongalactic Astrophysics" },
  { id: "astro-ph.SR", label: "Solar & Stellar", full: "Solar and Stellar Astrophysics" },
];

const REFRESH_MS = 30 * 60 * 1000;

export default function ResearchPage() {
  const [category, setCategory] = useState("astro-ph.GA");
  const [papers, setPapers] = useState<ArxivPaper[]>([]);
  const [loading, setLoading] = useState(true);
  const [lastRefresh, setLastRefresh] = useState<Date | null>(null);

  const fetchPapers = useCallback(async (cat: string) => {
    setLoading(true);
    try {
      const res = await fetch(`/api/research/arxiv?category=${cat}&limit=10`);
      const data = await res.json();
      setPapers(Array.isArray(data) ? data : []);
      setLastRefresh(new Date());
    } catch {
      setPapers([]);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchPapers(category);
    const interval = setInterval(() => fetchPapers(category), REFRESH_MS);
    return () => clearInterval(interval);
  }, [category, fetchPapers]);

  return (
    <div>
      {/* Header */}
      <div style={{ marginBottom: "1.5rem" }}>
        <h2 style={{ fontSize: "1.5rem", fontWeight: 600, color: "#f8fafc", marginBottom: "0.25rem" }}>Research Frontier</h2>
        <p style={{ fontSize: "0.875rem", color: "#94a3b8", margin: 0 }}>
          Latest papers from arXiv astro-ph, matched to NebulaMind wiki pages.
          {lastRefresh && (
            <span style={{ marginLeft: "0.5rem", color: "#64748b" }}>
              Updated {lastRefresh.toLocaleTimeString()} · auto-refreshes every 30 min
            </span>
          )}
        </p>
      </div>

      {/* Category tabs */}
      <div style={{ display: "flex", flexWrap: "wrap", gap: "0.5rem", marginBottom: "1.5rem" }}>
        {CATEGORIES.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setCategory(cat.id)}
            title={cat.full}
            style={{
              padding: "0.5rem 1rem",
              fontSize: "0.875rem",
              borderRadius: "4px",
              fontWeight: 500,
              border: category === cat.id ? "1px solid #6366f1" : "1px solid #334155",
              background: category === cat.id ? "#6366f1" : "#1e293b",
              color: category === cat.id ? "#ffffff" : "#94a3b8",
              cursor: "pointer",
              transition: "all 0.15s",
            }}
          >
            {cat.label}
          </button>
        ))}
        <button
          onClick={() => fetchPapers(category)}
          style={{
            padding: "0.5rem 0.75rem",
            fontSize: "0.875rem",
            borderRadius: "4px",
            background: "#1e293b",
            border: "1px solid #334155",
            color: "#94a3b8",
            cursor: "pointer",
            display: "inline-flex",
            alignItems: "center",
            gap: "0.35rem",
          }}
          title="Refresh now"
        >
          <RefreshCw size={14} />
          Refresh
        </button>
      </div>

      {/* Papers */}
      {loading ? (
        <div style={{ textAlign: "center", padding: "4rem 0", color: "#64748b" }}>
          <p>Contacting arXiv...</p>
        </div>
      ) : papers.length === 0 ? (
        <div style={{ textAlign: "center", padding: "4rem 0", color: "#64748b" }}>
          <p>No papers found. arXiv may be temporarily unavailable.</p>
        </div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
          {papers.map((paper) => (
            <div key={paper.arxiv_id} style={{ background: "#1e293b", border: "1px solid #334155", borderRadius: "8px", padding: "1.25rem", transition: "border-color 0.15s" }}
              onMouseEnter={(e: any) => e.currentTarget.style.borderColor = "#6366f1"}
              onMouseLeave={(e: any) => e.currentTarget.style.borderColor = "#334155"}>
              <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: "1rem" }}>
                <div style={{ flex: 1, minWidth: 0 }}>
                  {/* Title + date */}
                  <div style={{ display: "flex", alignItems: "flex-start", gap: "0.5rem", marginBottom: "0.5rem" }}>
                    <div style={{ flex: 1 }}>
                      <a
                        href={paper.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        style={{ fontWeight: 600, color: "#f8fafc", textDecoration: "none", transition: "color 0.15s" }}
                        onMouseEnter={(e: any) => e.currentTarget.style.color = "#818cf8"}
                        onMouseLeave={(e: any) => e.currentTarget.style.color = "#f8fafc"}
                      >
                        {paper.title}
                      </a>
                    </div>
                    <span style={{ fontSize: "0.75rem", color: "#64748b", whiteSpace: "nowrap", flexShrink: 0, marginTop: "2px" }}>
                      {paper.submitted}
                    </span>
                  </div>

                  {/* Authors */}
                  <p style={{ fontSize: "0.75rem", color: "#64748b", marginBottom: "0.5rem", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                    {paper.authors.slice(0, 5).join(", ")}
                    {paper.authors.length > 5 && ` + ${paper.authors.length - 5} more`}
                  </p>

                  {/* Abstract summary */}
                  <p style={{ fontSize: "0.875rem", color: "#94a3b8", lineHeight: 1.7, marginBottom: "0.75rem" }}>
                    {paper.abstract_summary}
                  </p>

                  {/* Footer row */}
                  <div style={{ display: "flex", alignItems: "center", gap: "0.75rem", flexWrap: "wrap" }}>
                    <a
                      href={paper.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      style={{ fontSize: "0.75rem", fontWeight: 500, color: "#6366f1", textDecoration: "none" }}
                    >
                      arXiv:{paper.arxiv_id} ↗
                    </a>

                    {paper.related_pages.length > 0 && (
                      <div style={{ display: "flex", alignItems: "center", gap: "0.375rem", flexWrap: "wrap" }}>
                        <span style={{ fontSize: "0.75rem", color: "#64748b" }}>Related:</span>
                        {paper.related_pages.map((slug) => (
                          <Link
                            key={slug}
                            href={`/wiki/${slug}`}
                            style={{ fontSize: "0.75rem", padding: "2px 8px", background: "rgba(99, 102, 241, 0.1)", color: "#818cf8", borderRadius: "4px", textDecoration: "none", transition: "background 0.15s" }}
                          >
                            {slug.replace(/-/g, " ")}
                          </Link>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Community Spotlight */}
      <CommunitySpotlight />

      {/* Subscribe Widget */}
      <SubscribeWidget />
    </div>
  );
}
