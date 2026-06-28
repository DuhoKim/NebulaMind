"use client";
import { useEffect, useMemo, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import { buildCrossPagePaperFootprintDeck, type CrossPagePaperFootprintResponse } from "./crossPagePaperFootprint";
import { buildEvidenceTriageQueueView, buildEvidenceTriageStudioDeck, type EvidenceTriageLaneFilter } from "./evidenceTriageStudio";

export interface FactSource {
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

export interface PageCitation {
  evidence_id: number;
  author_year_key?: string | null;
  title?: string | null;
  arxiv_id?: string | null;
  url?: string | null;
}

export interface WikiSourcesClientTestOnlyFixtureData {
  page: { title?: string | null; slug?: string | null };
  sources?: FactSource[];
  citations?: PageCitation[];
  crossPageFootprints?: CrossPagePaperFootprintResponse[];
}

type WikiSourcesClientProps = {
  testOnlyFixtureSlug?: string;
  testOnlyFixtureData?: WikiSourcesClientTestOnlyFixtureData;
};

const TIER_COLOR: Record<string, { bg: string; text: string; label: string }> = {
  authoritative: { bg: "rgba(129,140,248,0.1)", text: "#818cf8", label: "📐 Authoritative" },
  claim:         { bg: "rgba(34,197,94,0.1)",   text: "#22c55e", label: "📄 Wiki-grounded" },
  ai_estimate:   { bg: "rgba(245,158,11,0.1)",  text: "#f59e0b", label: "⚠️ AI estimate" },
};

const TRUST_COLOR: Record<string, string> = {
  consensus: "#22c55e", accepted: "#94a3b8",
  debated: "#f97316", challenged: "#ef4444", unverified: "#475569",
};

export default function WikiSourcesPage({ testOnlyFixtureSlug, testOnlyFixtureData }: WikiSourcesClientProps = {}) {
  const params = useParams();
  const slug = testOnlyFixtureSlug || (params?.slug as string);
  const [sources, setSources] = useState<FactSource[]>([]);
  const [citations, setCitations] = useState<PageCitation[]>([]);
  const [crossPageFootprints, setCrossPageFootprints] = useState<CrossPagePaperFootprintResponse[]>([]);
  const [pageTitle, setPageTitle] = useState("");
  const [loading, setLoading] = useState(true);
  const [footprintsLoading, setFootprintsLoading] = useState(false);
  const [footprintError, setFootprintError] = useState<string | null>(null);
  const [footprintRetryNonce, setFootprintRetryNonce] = useState(0);
  const [activeTriageLaneFilter, setActiveTriageLaneFilter] = useState<EvidenceTriageLaneFilter>("all");
  const [triagePage, setTriagePage] = useState(0);

  useEffect(() => {
    if (!slug) return;
    if (testOnlyFixtureData) {
      setPageTitle(testOnlyFixtureData.page?.title || slug);
      setSources(Array.isArray(testOnlyFixtureData.sources) ? testOnlyFixtureData.sources : []);
      setCitations(Array.isArray(testOnlyFixtureData.citations) ? testOnlyFixtureData.citations : []);
      setCrossPageFootprints(Array.isArray(testOnlyFixtureData.crossPageFootprints) ? testOnlyFixtureData.crossPageFootprints : []);
      setLoading(false);
      setFootprintsLoading(false);
      setFootprintError(null);
      return;
    }
    setLoading(true);
    setFootprintsLoading(true);
    setFootprintError(null);
    Promise.all([
      fetch(`/api/pages/${slug}`).then(r => r.json()),
      fetch(`/api/pages/${slug}/fact-sources`).then(r => r.ok ? r.json() : []).catch(() => []),
      fetch(`/api/pages/${slug}/citations`).then(r => r.ok ? r.json() : { citations: [] }).catch(() => ({ citations: [] })),
    ]).then(async ([page, srcs, citationPayload]) => {
      const citationList = Array.isArray(citationPayload?.citations) ? citationPayload.citations : [];
      setPageTitle(page?.title || slug);
      setSources(Array.isArray(srcs) ? srcs : []);
      setCitations(citationList);
      setLoading(false);

      const byArxiv = new Map<string, PageCitation>();
      for (const citation of citationList) {
        const arxivId = String(citation?.arxiv_id || "").replace(/^arXiv:/, "").trim();
        if (arxivId && !byArxiv.has(arxivId)) byArxiv.set(arxivId, { ...citation, arxiv_id: arxivId });
      }
      const footprintTargets = [...byArxiv.values()].slice(0, 4);
      const footprintResults = await Promise.all(
        footprintTargets.map(async (citation) => {
          const query = new URLSearchParams({ arxiv_id: String(citation.arxiv_id || "") });
          try {
            const response = await fetch(`/api/pages/paper-footprint?${query.toString()}`);
            if (response.status === 404) return { data: null, failed: false };
            if (!response.ok) return { data: null, failed: true };
            return { data: await response.json(), failed: false };
          } catch {
            return { data: null, failed: true };
          }
        }),
      );
      setCrossPageFootprints(footprintResults.map(result => result.data).filter(Boolean) as CrossPagePaperFootprintResponse[]);
      setFootprintError(footprintResults.some(result => result.failed) ? "Couldn't load wiki-wide paper footprint. Retry." : null);
      setFootprintsLoading(false);
    }).catch(() => {
      setFootprintError("Couldn't load wiki-wide paper footprint. Retry.");
      setLoading(false);
      setFootprintsLoading(false);
    });
  }, [slug, testOnlyFixtureData, footprintRetryNonce]);

  const crossPageFootprintDeck = useMemo(
    () => buildCrossPagePaperFootprintDeck(crossPageFootprints),
    [crossPageFootprints],
  );

  const evidenceTriageDeck = useMemo(
    () => buildEvidenceTriageStudioDeck({ sources, citations, crossPageFootprints, pageSlug: slug, pageTitle }),
    [sources, citations, crossPageFootprints, slug, pageTitle],
  );

  useEffect(() => {
    setTriagePage(0);
  }, [activeTriageLaneFilter, evidenceTriageDeck.items.length]);

  const evidenceTriageQueueView = useMemo(
    () => buildEvidenceTriageQueueView(evidenceTriageDeck, { laneFilter: activeTriageLaneFilter, page: triagePage }),
    [activeTriageLaneFilter, evidenceTriageDeck, triagePage],
  );


  const heroSources = sources.filter(s => s.fact_kind === "hero");

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

  const renderEvidenceTriageStudio = () => {
    const deck = evidenceTriageDeck;
    const queueView = evidenceTriageQueueView;
    const laneFilters = [
      { key: "all", label: "All lanes", count: queueView.totalCount, color: "#cbd5e1" },
      { key: "needs_adjudication", label: "Adjudication", count: deck.laneCounts.needs_adjudication, color: "#fb923c" },
      { key: "needs_source", label: "Source gaps", count: deck.laneCounts.needs_source, color: "#facc15" },
      { key: "ready_to_review", label: "Synthesis-ready", count: deck.laneCounts.ready_to_review, color: "#86efac" },
    ] as const;
    return (
      <section data-testid="evidence-triage-studio" style={{ marginBottom: "2rem", background: "linear-gradient(135deg, rgba(30,41,59,0.96), rgba(15,23,42,0.9))", border: "1px solid rgba(251,146,60,0.24)", borderRadius: "14px", padding: "1rem" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: "1rem", flexWrap: "wrap" }}>
          <div>
            <div style={{ color: "#fb923c", fontSize: "0.68rem", fontWeight: 900, letterSpacing: "0.12em", textTransform: "uppercase" }}>
              review cockpit
            </div>
            <h2 style={{ fontSize: "1.1rem", fontWeight: 850, color: "#f8fafc", margin: "0.25rem 0" }}>
              Evidence triage studio
            </h2>
            <p data-testid="evidence-triage-caveat" style={{ color: "#94a3b8", fontSize: "0.78rem", margin: 0, maxWidth: "45rem", lineHeight: 1.55 }}>
              Evidence triage is a review queue, not a final verdict. No labels are written from this surface.
            </p>
          </div>
          <div style={{ color: "#cbd5e1", fontSize: "0.74rem", border: "1px solid rgba(148,163,184,0.24)", borderRadius: "999px", padding: "0.32rem 0.65rem" }}>
            {deck.summary}
          </div>
        </div>

        <div style={{ display: "flex", gap: "0.45rem", flexWrap: "wrap", marginTop: "0.85rem" }}>
          {laneFilters.map((filter) => (
            <button
              key={filter.key}
              type="button"
              data-testid="evidence-triage-filter"
              aria-pressed={activeTriageLaneFilter === filter.key}
              onClick={() => {
                setActiveTriageLaneFilter(filter.key);
                setTriagePage(0);
              }}
              style={{ border: `1px solid ${filter.color}55`, color: filter.color, background: activeTriageLaneFilter === filter.key ? `${filter.color}28` : `${filter.color}12`, borderRadius: "999px", padding: "0.25rem 0.58rem", fontSize: "0.72rem", fontWeight: 850, cursor: "pointer" }}
            >
              <span data-testid="evidence-triage-lane-chip">{filter.label}: {filter.count.toLocaleString()}</span>
            </button>
          ))}
        </div>

        {!deck.hasTriageSignal ? (
          <p data-testid="evidence-triage-empty" style={{ color: "#64748b", fontSize: "0.8rem", marginTop: "0.85rem" }}>
            No evidence triage signals yet. Add paper-backed evidence or source flags before readiness review.
          </p>
        ) : (
          <>
            <p data-testid="evidence-triage-overflow-disclosure" style={{ color: "#94a3b8", fontSize: "0.74rem", lineHeight: 1.45, margin: "0.78rem 0 0" }}>
              {queueView.overflowDisclosure}
            </p>
            {queueView.visibleItems.length === 0 ? (
              <p data-testid="evidence-triage-empty" style={{ color: "#64748b", fontSize: "0.8rem", marginTop: "0.85rem" }}>
                {queueView.emptyFilterMessage}
              </p>
            ) : (
              <div style={{ display: "grid", gap: "0.65rem", marginTop: "0.9rem" }}>
                {queueView.visibleItems.map((item) => (
                  <article key={item.id} data-testid="evidence-triage-card" style={{ background: "rgba(2,6,23,0.74)", border: "1px solid rgba(51,65,85,0.92)", borderRadius: "12px", padding: "0.82rem" }}>
                    <div style={{ display: "flex", justifyContent: "space-between", gap: "0.85rem", flexWrap: "wrap" }}>
                      <div>
                        <div style={{ color: "#f8fafc", fontWeight: 850, fontSize: "0.86rem" }}>{item.actionLabel}</div>
                        <div style={{ color: "#94a3b8", fontSize: "0.74rem", marginTop: "0.12rem" }}>
                          {item.paperLabel} · {item.pageTitle} · {item.claimLabel}
                        </div>
                      </div>
                      <div style={{ color: item.lane === "needs_adjudication" ? "#fb923c" : item.lane === "needs_source" ? "#facc15" : "#86efac", fontSize: "0.72rem", fontWeight: 900 }}>
                        {item.laneLabel}
                      </div>
                    </div>
                    <p style={{ color: "#cbd5e1", fontSize: "0.76rem", lineHeight: 1.45, margin: "0.55rem 0 0" }}>{item.claimText}</p>
                    <div style={{ color: "#64748b", fontSize: "0.72rem", marginTop: "0.45rem" }}>
                      {item.reasonText} · {item.votesSummary}
                    </div>
                    <Link
                      data-testid="evidence-triage-action-link"
                      href={item.href}
                      aria-label={`Review ${item.claimLabel} in ${item.pageTitle}`}
                      style={{ display: "inline-flex", marginTop: "0.55rem", color: "#93c5fd", textDecoration: "none", fontSize: "0.74rem", fontWeight: 850 }}
                    >
                      Open review context →
                    </Link>
                  </article>
                ))}
              </div>
            )}
            {queueView.pageCount > 1 && (
              <div data-testid="evidence-triage-page-control" style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap", marginTop: "0.85rem", color: "#94a3b8", fontSize: "0.74rem" }}>
                <button type="button" disabled={queueView.currentPage === 0} onClick={() => setTriagePage(Math.max(0, queueView.currentPage - 1))} style={{ border: "1px solid rgba(148,163,184,0.3)", background: "rgba(15,23,42,0.92)", color: queueView.currentPage === 0 ? "#475569" : "#cbd5e1", borderRadius: "999px", padding: "0.28rem 0.7rem", cursor: queueView.currentPage === 0 ? "not-allowed" : "pointer" }}>
                  Previous
                </button>
                <span>Page {queueView.currentPage + 1} of {queueView.pageCount}</span>
                <button type="button" disabled={queueView.currentPage + 1 >= queueView.pageCount} onClick={() => setTriagePage(Math.min(queueView.pageCount - 1, queueView.currentPage + 1))} style={{ border: "1px solid rgba(148,163,184,0.3)", background: "rgba(15,23,42,0.92)", color: queueView.currentPage + 1 >= queueView.pageCount ? "#475569" : "#cbd5e1", borderRadius: "999px", padding: "0.28rem 0.7rem", cursor: queueView.currentPage + 1 >= queueView.pageCount ? "not-allowed" : "pointer" }}>
                  Next
                </button>
              </div>
            )}
          </>
        )}
      </section>
    );
  };

  const renderCrossPagePaperFootprint = () => {
    const deck = crossPageFootprintDeck;
    return (
      <section data-testid="cross-page-paper-footprint" style={{ marginBottom: "2rem", background: "linear-gradient(135deg, rgba(15,23,42,0.94), rgba(17,24,39,0.82))", border: "1px solid rgba(56,189,248,0.22)", borderRadius: "14px", padding: "1rem" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: "1rem", flexWrap: "wrap" }}>
          <div>
            <div style={{ color: "#67e8f9", fontSize: "0.68rem", fontWeight: 900, letterSpacing: "0.12em", textTransform: "uppercase" }}>
              wiki-wide paper footprint
            </div>
            <h2 style={{ fontSize: "1.1rem", fontWeight: 800, color: "#f8fafc", margin: "0.25rem 0" }}>
              Cross-page paper footprint
            </h2>
            <p data-testid="cross-page-paper-footprint-scope" style={{ color: "#94a3b8", fontSize: "0.78rem", margin: 0, maxWidth: "44rem", lineHeight: 1.55 }}>
              Across indexed wiki evidence rows; this is not a final verdict about which claim is correct.
            </p>
          </div>
          <div style={{ color: "#cbd5e1", fontSize: "0.74rem", border: "1px solid rgba(148,163,184,0.24)", borderRadius: "999px", padding: "0.32rem 0.65rem" }}>
            {deck.hasCrossPageFootprint ? `${deck.paperCount} papers · ${deck.pageCount} page touches · ${deck.claimCount} claims` : `${citations.filter(c => c.arxiv_id).length} arXiv-indexed papers scanned`}
          </div>
        </div>

        {footprintsLoading && (
          <p style={{ color: "#64748b", fontSize: "0.8rem", marginTop: "0.85rem" }}>Loading cross-page paper footprint…</p>
        )}

        {!footprintsLoading && footprintError && (
          <p data-testid="cross-page-paper-footprint-error" style={{ color: "#fb923c", fontSize: "0.8rem", marginTop: "0.85rem" }}>
            {footprintError}{" "}
            <button
              type="button"
              data-testid="cross-page-paper-footprint-retry"
              onClick={() => setFootprintRetryNonce(nonce => nonce + 1)}
              style={{ color: "#93c5fd", background: "transparent", border: "0", padding: 0, font: "inherit", fontWeight: 800, cursor: "pointer" }}
            >
              Retry
            </button>
          </p>
        )}

        {!footprintsLoading && !footprintError && !deck.hasCrossPageFootprint && (
          <p style={{ color: "#64748b", fontSize: "0.8rem", marginTop: "0.85rem" }}>
            {deck.summary} Papers appear here after citation records include an arXiv ID and the wiki evidence index has matching rows.
          </p>
        )}

        {!footprintsLoading && deck.hasCrossPageFootprint && (
          <div style={{ display: "grid", gap: "0.75rem", marginTop: "0.9rem" }}>
            {deck.items.map((item) => (
              <article key={item.arxivId || item.paperLabel} data-testid="cross-page-paper-card" style={{ background: "rgba(2,6,23,0.72)", border: "1px solid rgba(51,65,85,0.92)", borderRadius: "12px", padding: "0.85rem" }}>
                <div style={{ display: "flex", justifyContent: "space-between", gap: "1rem", flexWrap: "wrap" }}>
                  <div>
                    <div style={{ color: "#f8fafc", fontWeight: 800, fontSize: "0.92rem" }}>{item.paperLabel}</div>
                    <div style={{ color: "#cbd5e1", fontSize: "0.78rem", marginTop: "0.15rem" }}>{item.title}</div>
                  </div>
                  <div style={{ color: item.counterCount > 0 ? "#fb923c" : "#86efac", fontSize: "0.74rem", fontWeight: 800 }}>
                    {item.impactLabel}
                  </div>
                </div>
                <div style={{ display: "grid", gap: "0.55rem", marginTop: "0.75rem" }}>
                  {item.pages.slice(0, 4).map((page) => (
                    <div key={page.slug} style={{ borderTop: "1px solid rgba(30,41,59,0.95)", paddingTop: "0.55rem" }}>
                      <Link data-testid="cross-page-paper-page-link" href={`/wiki/${page.slug}`} aria-label={`${page.title} — ${page.claim_count || page.claims.length} claims, ${page.counter_count || 0} countering`} style={{ color: "#93c5fd", fontWeight: 800, fontSize: "0.78rem", textDecoration: "none" }}>
                        {page.title}
                      </Link>
                      <span style={{ color: "#64748b", fontSize: "0.72rem", marginLeft: "0.45rem" }}>
                        {page.claim_count || page.claims.length} claims · {page.counter_count || 0} countering
                      </span>
                      <div style={{ display: "grid", gap: "0.35rem", marginTop: "0.4rem" }}>
                        {page.claims.slice(0, 3).map((claim) => (
                          <Link key={`${page.slug}-${claim.claim_id}-${claim.evidence_id}`} data-testid="cross-page-paper-claim-row" href={claim.href || `/wiki/${page.slug}#claim-${claim.claim_id}`} style={{ display: "block", color: "#cbd5e1", textDecoration: "none", fontSize: "0.74rem", lineHeight: 1.45 }}>
                            <span style={{ color: claim.tone === "counter" ? "#fb923c" : claim.tone === "support" ? "#86efac" : "#94a3b8", fontWeight: 850 }}>
                              {claim.tone === "counter" ? "Counters" : claim.tone === "support" ? "Supports" : "Neutral"}
                            </span>
                            <span style={{ color: "#64748b" }}> · {claim.trust_level || "unverified"} · </span>
                            {claim.claim_text}
                          </Link>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              </article>
            ))}
          </div>
        )}
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

      {renderEvidenceTriageStudio()}
      {renderCrossPagePaperFootprint()}

      {sources.length === 0 ? (
        <p style={{ color: "#475569" }}>No source records found for this page.</p>
      ) : (
        <>
          {renderSources(heroSources, "Hero Facts")}
        </>
      )}
    </div>
  );
}
