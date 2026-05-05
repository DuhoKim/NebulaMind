"use client";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";

interface FactSource {
  id: number;
  fact_kind: string;
  fact_index: number;
  source_tier: string;
  authority: string | null;
  reference_url: string | null;
  reference_title: string | null;
  retrieval_year: number | null;
  claim_id: number | null;
  trust_level_snapshot: string | null;
  evidence_count_snapshot: number | null;
  representative_arxiv_id: string | null;
  attribution: string;
  flagged: boolean;
  reason: string | null;
}

const TIER_COLOR: Record<string, { bg: string; text: string; label: string }> = {
  authoritative: { bg: "rgba(129,140,248,0.1)", text: "#818cf8", label: "📐 Authoritative" },
  claim:         { bg: "rgba(34,197,94,0.1)",   text: "#22c55e", label: "📄 Wiki-grounded" },
  ai_estimate:   { bg: "rgba(245,158,11,0.1)",  text: "#f59e0b", label: "⚠️ AI estimate" },
};

const TRUST_COLOR: Record<string, string> = {
  consensus: "#22c55e", accepted: "#94a3b8",
  debated: "#f97316", challenged: "#ef4444", unverified: "#475569",
};

export default function WikiSourcesPage() {
  const params = useParams();
  const slug = params?.slug as string;
  const [sources, setSources] = useState<FactSource[]>([]);
  const [pageTitle, setPageTitle] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!slug) return;
    Promise.all([
      fetch(`/api/pages/${slug}`).then(r => r.json()),
      fetch(`/api/pages/${slug}/fact-sources`).then(r => r.ok ? r.json() : []).catch(() => []),
    ]).then(([page, srcs]) => {
      setPageTitle(page?.title || slug);
      setSources(Array.isArray(srcs) ? srcs : []);
      setLoading(false);
    }).catch(() => setLoading(false));
  }, [slug]);

  const heroSources = sources.filter(s => s.fact_kind === "hero");
  const dykSources = sources.filter(s => s.fact_kind === "did_you_know");

  const byTier = (list: FactSource[]) => {
    const groups: Record<string, FactSource[]> = { authoritative: [], claim: [], ai_estimate: [] };
    list.forEach(s => { (groups[s.source_tier] = groups[s.source_tier] || []).push(s); });
    return groups;
  };

  if (loading) return <p style={{ color: "#64748b", padding: "2rem" }}>Loading...</p>;

  const renderSources = (list: FactSource[], title: string) => {
    const groups = byTier(list);
    const total = list.length;
    if (total === 0) return null;
    return (
      <section style={{ marginBottom: "2rem" }}>
        <h2 style={{ fontSize: "1.1rem", fontWeight: 700, color: "#f8fafc", marginBottom: "1rem" }}>{title}</h2>
        {(["authoritative", "claim", "ai_estimate"] as const).map(tier => {
          const items = groups[tier] || [];
          if (!items.length) return null;
          const tc = TIER_COLOR[tier];
          return (
            <div key={tier} style={{ marginBottom: "1rem" }}>
              <div style={{ fontSize: "0.78rem", fontWeight: 600, color: tc.text,
                marginBottom: "0.5rem", padding: "0.25rem 0.75rem",
                background: tc.bg, borderRadius: "99px", display: "inline-block" }}>
                {tc.label} ({items.length})
              </div>
              <div style={{ display: "flex", flexDirection: "column", gap: "0.4rem" }}>
                {items.map((s, i) => (
                  <div key={i} style={{ background: "#1e293b", border: "1px solid #334155",
                    borderRadius: "6px", padding: "0.6rem 0.875rem", fontSize: "0.8rem" }}>
                    {s.source_tier === "authoritative" && s.reference_url && (
                      <a href={s.reference_url} target="_blank" rel="noopener noreferrer"
                        style={{ color: "#818cf8", textDecoration: "none", fontWeight: 500 }}>
                        {s.reference_title || s.attribution}
                      </a>
                    )}
                    {s.source_tier === "authoritative" && !s.reference_url && (
                      <span style={{ color: "#f8fafc" }}>{s.attribution}</span>
                    )}
                    {s.source_tier === "claim" && (
                      <div>
                        <span style={{ color: "#94a3b8" }}>Linked to </span>
                        <Link href={`/wiki/${slug}`}
                          style={{ color: "#22c55e", textDecoration: "none" }}>
                          claim #{s.claim_id}
                        </Link>
                        <span style={{ color: "#475569" }}> · </span>
                        <span style={{ color: TRUST_COLOR[s.trust_level_snapshot || ""] || "#94a3b8",
                          fontSize: "0.72rem" }}>
                          {s.trust_level_snapshot}
                        </span>
                        {s.evidence_count_snapshot && (
                          <span style={{ color: "#64748b", fontSize: "0.7rem" }}>
                            {" "}· {s.evidence_count_snapshot} papers
                          </span>
                        )}
                        {s.representative_arxiv_id && (
                          <a href={`https://arxiv.org/abs/${s.representative_arxiv_id}`}
                            target="_blank" rel="noopener noreferrer"
                            style={{ color: "#6366f1", textDecoration: "none", fontSize: "0.7rem",
                              marginLeft: "0.5rem" }}>
                            arXiv:{s.representative_arxiv_id}
                          </a>
                        )}
                      </div>
                    )}
                    {s.source_tier === "ai_estimate" && (
                      <span style={{ color: "#64748b" }}>
                        {s.flagged ? "🚩 " : "⚠️ "}{s.reason || "No peer-reviewed source linked"}
                      </span>
                    )}
                    {s.retrieval_year && s.source_tier === "authoritative" && (
                      <span style={{ color: "#475569", fontSize: "0.7rem", marginLeft: "0.5rem" }}>
                        ({s.retrieval_year})
                      </span>
                    )}
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </section>
    );
  };

  return (
    <div style={{ maxWidth: "56rem", margin: "0 auto" }}>
      <div style={{ marginBottom: "2rem" }}>
        <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.5rem" }}>
          <Link href={`/wiki/${slug}`} style={{ color: "#6366f1", textDecoration: "none" }}>
            ← {pageTitle}
          </Link>
        </div>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 800, color: "#f8fafc", marginBottom: "0.5rem" }}>
          📚 Sources — {pageTitle}
        </h1>
        <p style={{ color: "#64748b", fontSize: "0.875rem" }}>
          {sources.length} sourced facts ·{" "}
          {sources.filter(s => s.source_tier === "authoritative").length} authoritative ·{" "}
          {sources.filter(s => s.source_tier === "claim").length} wiki-grounded ·{" "}
          {sources.filter(s => s.source_tier === "ai_estimate").length} AI estimate
        </p>
      </div>

      {sources.length === 0 ? (
        <p style={{ color: "#475569" }}>No source records found for this page.</p>
      ) : (
        <>
          {renderSources(heroSources, "Hero Facts")}
          {renderSources(dykSources, "Did You Know")}
        </>
      )}
    </div>
  );
}
