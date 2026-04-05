"use client";

import { useEffect, useState, useCallback } from "react";
import Link from "next/link";

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
  { id: "astro-ph.GA", label: "🌀 Galaxies", full: "Astrophysics of Galaxies" },
  { id: "astro-ph.HE", label: "⚡ High Energy", full: "High Energy Astrophysical Phenomena" },
  { id: "astro-ph.CO", label: "🔵 Cosmology", full: "Cosmology and Nongalactic Astrophysics" },
  { id: "astro-ph.SR", label: "☀️ Solar & Stellar", full: "Solar and Stellar Astrophysics" },
];

const REFRESH_MS = 30 * 60 * 1000; // 30 minutes

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
      <div className="mb-6">
        <h2 className="text-2xl font-bold mb-1">🔭 Research Frontier</h2>
        <p className="text-sm text-gray-500">
          Latest papers from arXiv astro-ph — matched to NebulaMind wiki pages.
          {lastRefresh && (
            <span className="ml-2 text-gray-400">
              Last updated: {lastRefresh.toLocaleTimeString()} · auto-refreshes every 30 min
            </span>
          )}
        </p>
      </div>

      {/* Category tabs */}
      <div className="flex flex-wrap gap-2 mb-6">
        {CATEGORIES.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setCategory(cat.id)}
            title={cat.full}
            className={`px-4 py-2 text-sm rounded-lg font-medium transition-colors ${
              category === cat.id
                ? "bg-indigo-600 text-white"
                : "bg-white border border-gray-200 text-gray-600 hover:bg-gray-50"
            }`}
          >
            {cat.label}
          </button>
        ))}
        <button
          onClick={() => fetchPapers(category)}
          className="px-3 py-2 text-sm rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200 transition-colors"
          title="Refresh now"
        >
          🔄 Refresh
        </button>
      </div>

      {/* Papers */}
      {loading ? (
        <div className="text-center py-16 text-gray-400">
          <div className="text-4xl mb-3">📡</div>
          <p>Contacting arXiv...</p>
        </div>
      ) : papers.length === 0 ? (
        <div className="text-center py-16 text-gray-400">
          <p>No papers found. arXiv may be temporarily unavailable.</p>
        </div>
      ) : (
        <div className="space-y-4">
          {papers.map((paper) => (
            <div key={paper.arxiv_id} className="bg-white border border-gray-200 rounded-xl p-5 hover:border-indigo-300 transition-colors">
              <div className="flex items-start justify-between gap-4">
                <div className="flex-1 min-w-0">
                  {/* Title + date */}
                  <div className="flex items-start gap-2 mb-2">
                    <div className="flex-1">
                      <a
                        href={paper.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="font-semibold text-gray-900 hover:text-indigo-700 transition-colors no-underline"
                      >
                        {paper.title}
                      </a>
                    </div>
                    <span className="text-xs text-gray-400 whitespace-nowrap flex-shrink-0 mt-0.5">
                      {paper.submitted}
                    </span>
                  </div>

                  {/* Authors */}
                  <p className="text-xs text-gray-500 mb-2 line-clamp-1">
                    {paper.authors.slice(0, 5).join(", ")}
                    {paper.authors.length > 5 && ` + ${paper.authors.length - 5} more`}
                  </p>

                  {/* Abstract summary */}
                  <p className="text-sm text-gray-600 leading-relaxed mb-3">
                    {paper.abstract_summary}
                  </p>

                  {/* Footer row */}
                  <div className="flex items-center gap-3 flex-wrap">
                    <a
                      href={paper.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-xs font-medium text-indigo-600 hover:text-indigo-800 no-underline flex items-center gap-1"
                    >
                      🔗 arXiv:{paper.arxiv_id}
                    </a>

                    {paper.related_pages.length > 0 && (
                      <div className="flex items-center gap-1.5 flex-wrap">
                        <span className="text-xs text-gray-400">Related:</span>
                        {paper.related_pages.map((slug) => (
                          <Link
                            key={slug}
                            href={`/wiki/${slug}`}
                            className="text-xs px-2 py-0.5 bg-indigo-50 text-indigo-700 rounded-full hover:bg-indigo-100 no-underline transition-colors"
                          >
                            📄 {slug.replace(/-/g, " ")}
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
    </div>
  );
}
