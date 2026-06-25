"use client";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import { emptyTrustHistoryText, formatTrustHistoryStats } from "../trustHistoryCopy";

interface ClaimSummary {
  id: number;
  text: string;
  trust_level: string;
  section: string;
}

interface TimelineEvent {
  kind: string;
  icon: string;
  color: string;
  started_at: string;
  level_before: string | null;
  level_after: string;
  score_before: number | null;
  score_after: number;
  summary: string;
  detail: string | null;
  raw_count: number;
}

interface ClaimHistory {
  claim_id: number;
  current: { trust_level: string; trust_score: number; claim_text: string };
  events: TimelineEvent[];
  stats: { total_raw_rows: number; events_returned: number; noise_filtered: number };
}

const TRUST_COLOR: Record<string, string> = {
  consensus: "#22c55e", accepted: "#94a3b8",
  debated: "#f97316", challenged: "#ef4444", unverified: "#475569",
};

const COLOR_MAP: Record<string, { dot: string; text: string }> = {
  gray:   { dot: "#64748b", text: "#64748b" },
  blue:   { dot: "#3b82f6", text: "#3b82f6" },
  purple: { dot: "#a855f7", text: "#a855f7" },
  gold:   { dot: "#eab308", text: "#ca8a04" },
  orange: { dot: "#f97316", text: "#ea580c" },
  brown:  { dot: "#b45309", text: "#92400e" },
};

function fmtDate(iso: string) {
  return new Date(iso).toLocaleDateString("en-US", { month: "short", day: "numeric" });
}

export default function WikiHistoryPage() {
  const params = useParams();
  const slug = params?.slug as string;
  const [claims, setClaims] = useState<ClaimSummary[]>([]);
  const [histories, setHistories] = useState<Record<number, ClaimHistory>>({});
  const [pageTitle, setPageTitle] = useState("");
  const [loading, setLoading] = useState(true);
  const [loadingClaims, setLoadingClaims] = useState<Set<number>>(new Set());

  useEffect(() => {
    if (!slug) return;
    Promise.all([
      fetch(`/api/pages/${slug}`).then(r => r.json()),
      fetch(`/api/pages/${slug}/claims`).then(r => r.json()),
    ]).then(([page, claimsData]) => {
      setPageTitle(page?.title || slug);
      const allClaims: ClaimSummary[] = [];
      for (const section of claimsData?.sections || []) {
        for (const c of section.claims || []) {
          allClaims.push({ ...c, section: section.name });
        }
      }
      setClaims(allClaims.filter((c: any) => c.trust_level !== "unverified").slice(0, 30));
      setLoading(false);
    }).catch(() => setLoading(false));
  }, [slug]);

  const loadHistory = async (claimId: number) => {
    if (histories[claimId] || loadingClaims.has(claimId)) return;
    setLoadingClaims(prev => new Set([...prev, claimId]));
    try {
      const r = await fetch(`/api/claims/${claimId}/trust-history?limit=10`);
      const d = await r.json();
      setHistories(prev => ({ ...prev, [claimId]: d }));
    } catch {}
    setLoadingClaims(prev => { const s = new Set(prev); s.delete(claimId); return s; });
  };

  if (loading) return <p style={{ color: "#64748b", padding: "2rem" }}>Loading...</p>;

  return (
    <div style={{ maxWidth: "56rem", margin: "0 auto" }}>
      <div style={{ marginBottom: "2rem" }}>
        <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.5rem" }}>
          <Link href={`/wiki/${slug}`} style={{ color: "#6366f1", textDecoration: "none" }}>
            ← {pageTitle}
          </Link>
        </div>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 800, color: "#f8fafc", marginBottom: "0.5rem" }}>
          📜 Trust History — {pageTitle}
        </h1>
        <p style={{ color: "#64748b", fontSize: "0.875rem" }}>
          {claims.length} sourced claims · click any claim to expand its trust timeline
        </p>
      </div>

      {claims.length === 0 && (
        <p style={{ color: "#475569" }}>No sourced claims found for this page.</p>
      )}

      <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
        {claims.map((claim: any) => {
          const hist = histories[claim.id];
          const isLoading = loadingClaims.has(claim.id);
          return (
            <div key={claim.id} style={{ background: "#1e293b", border: "1px solid #334155",
              borderRadius: "10px", overflow: "hidden" }}>
              <button onClick={() => loadHistory(claim.id)}
                style={{ width: "100%", background: "transparent", border: "none", cursor: "pointer",
                  padding: "0.875rem 1.125rem", textAlign: "left", display: "flex",
                  alignItems: "flex-start", gap: "0.75rem" }}>
                <span style={{ fontSize: "0.7rem", padding: "2px 6px", borderRadius: "99px", flexShrink: 0,
                  marginTop: "2px",
                  background: `${TRUST_COLOR[claim.trust_level] || "#64748b"}20`,
                  color: TRUST_COLOR[claim.trust_level] || "#64748b", fontWeight: 600 }}>
                  {claim.trust_level}
                </span>
                <span style={{ fontSize: "0.875rem", color: "#f8fafc", lineHeight: 1.5 }}>
                  {claim.text.slice(0, 120)}{claim.text.length > 120 ? "…" : ""}
                </span>
                <span style={{ marginLeft: "auto", fontSize: "0.72rem", color: "#475569", flexShrink: 0 }}>
                  {isLoading ? "⏳" : hist ? "▾" : "🕒"}
                </span>
              </button>

              {hist && (
                <div style={{ borderTop: "1px solid #1e293b", padding: "0.75rem 1.125rem",
                  background: "#0f172a" }}>
                  <div style={{ fontSize: "0.7rem", color: "#475569", marginBottom: "0.5rem" }}>
                    {formatTrustHistoryStats(hist.stats)}
                  </div>
                  {hist.events.length === 0 ? (
                    <p style={{ color: "#334155", fontSize: "0.78rem" }}>{emptyTrustHistoryText}</p>
                  ) : (
                    <div style={{ display: "flex", flexDirection: "column", gap: 0 }}>
                      {hist.events.map((ev, i) => {
                        const c = COLOR_MAP[ev.color] || COLOR_MAP.gray;
                        const isLast = i === hist.events.length - 1;
                        return (
                          <div key={i} style={{ display: "flex", gap: "0.6rem", paddingBottom: isLast ? 0 : "0.5rem" }}>
                            <div style={{ display: "flex", flexDirection: "column", alignItems: "center", flexShrink: 0 }}>
                              <div style={{ width: "8px", height: "8px", borderRadius: "50%",
                                background: c.dot, marginTop: "3px" }} />
                              {!isLast && <div style={{ width: "1px", flex: 1, background: "#1e293b",
                                minHeight: "16px", marginTop: "2px" }} />}
                            </div>
                            <div style={{ flex: 1 }}>
                              <div style={{ display: "flex", gap: "0.4rem", alignItems: "baseline", flexWrap: "wrap" }}>
                                <span style={{ fontSize: "0.72rem" }}>{ev.icon}</span>
                                <span style={{ fontSize: "0.75rem", color: "#f8fafc" }}>{ev.summary}</span>
                                {ev.level_before && ev.level_after && ev.level_before !== ev.level_after && (
                                  <span style={{ fontSize: "0.65rem", padding: "1px 4px", borderRadius: "4px",
                                    background: `${c.dot}20`, color: c.text }}>
                                    {ev.level_before} → {ev.level_after}
                                  </span>
                                )}
                              </div>
                              {ev.detail && <div style={{ fontSize: "0.67rem", color: "#64748b" }}>{ev.detail}</div>}
                              <div style={{ fontSize: "0.63rem", color: "#334155" }}>{fmtDate(ev.started_at)}</div>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
