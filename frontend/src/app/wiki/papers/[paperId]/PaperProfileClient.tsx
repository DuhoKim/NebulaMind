"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import type { CrossPagePaperFootprintResponse } from "../../[slug]/sources/crossPagePaperFootprint";
import PaperFootprintPanel from "./PaperFootprintPanel";
import { buildPaperProfileDeck, type PaperProfilePayload } from "./paperProfile";
import { buildPaperFootprintQuery } from "./paperFootprintQuery";

type PaperProfileClientProps = {
  paperId: string;
  testOnlyFixtureData?: PaperProfilePayload;
  testOnlyFootprintData?: CrossPagePaperFootprintResponse | null;
};

const STATUS_COLOR = {
  needs_adjudication: "#fb923c",
  needs_source: "#facc15",
  ready_to_review: "#86efac",
} as const;

const TONE_COLOR = {
  counter: "#fb923c",
  support: "#86efac",
  neutral: "#cbd5e1",
} as const;

export default function PaperProfileClient({ paperId, testOnlyFixtureData, testOnlyFootprintData }: PaperProfileClientProps) {
  const [payload, setPayload] = useState<PaperProfilePayload | null>(testOnlyFixtureData || null);
  const [loading, setLoading] = useState(!testOnlyFixtureData);
  const [error, setError] = useState<string | null>(null);
  const [retryNonce, setRetryNonce] = useState(0);
  const [footprintPayload, setFootprintPayload] = useState<CrossPagePaperFootprintResponse | null>(testOnlyFootprintData || null);
  const [footprintLoading, setFootprintLoading] = useState(false);
  const [footprintError, setFootprintError] = useState<string | null>(null);
  const [footprintRetryNonce, setFootprintRetryNonce] = useState(0);

  useEffect(() => {
    if (testOnlyFixtureData) {
      setPayload(testOnlyFixtureData);
      setLoading(false);
      setError(null);
      return;
    }
    setLoading(true);
    setError(null);
    fetch(`/api/pages/paper-profile?paper_id=${encodeURIComponent(paperId)}`)
      .then((response) => {
        if (!response.ok) throw new Error(`paper-profile ${response.status}`);
        return response.json();
      })
      .then((data) => {
        setPayload(data);
        setLoading(false);
      })
      .catch(() => {
        setError("Couldn't load paper profile. Retry.");
        setLoading(false);
      });
  }, [paperId, retryNonce, testOnlyFixtureData]);

  useEffect(() => {
    if (testOnlyFootprintData !== undefined) {
      setFootprintPayload(testOnlyFootprintData || null);
      setFootprintLoading(false);
      setFootprintError(null);
      return;
    }
    if (!payload || loading || error) {
      setFootprintPayload(null);
      setFootprintLoading(false);
      setFootprintError(null);
      return;
    }
    const query = buildPaperFootprintQuery(paperId, payload);
    if (!query) {
      setFootprintPayload(null);
      setFootprintLoading(false);
      setFootprintError(null);
      return;
    }
    setFootprintLoading(true);
    setFootprintError(null);
    fetch(`/api/pages/paper-footprint?${query}`)
      .then((response) => {
        if (response.status === 404) return null;
        if (!response.ok) throw new Error(`paper-footprint ${response.status}`);
        return response.json();
      })
      .then((data) => {
        setFootprintPayload(data);
        setFootprintLoading(false);
      })
      .catch(() => {
        setFootprintPayload(null);
        setFootprintError("Couldn't load Cited across NebulaMind footprint. Retry.");
        setFootprintLoading(false);
      });
  }, [paperId, payload, loading, error, footprintRetryNonce, testOnlyFootprintData]);

  const deck = useMemo(() => buildPaperProfileDeck(payload), [payload]);

  return (
    <main data-testid="paper-profile-detail" style={{ minHeight: "100vh", background: "#020617", color: "#e2e8f0" }}>
      <div style={{ maxWidth: "78rem", margin: "0 auto", padding: "3rem 1rem" }}>
        <div style={{ marginBottom: "1.25rem", display: "flex", gap: "0.8rem", flexWrap: "wrap" }}>
          <Link data-testid="paper-profile-directory-link" href="/wiki/papers" style={{ color: "#93c5fd", fontSize: "0.82rem", textDecoration: "none", fontWeight: 750 }}>
            ← Paper directory
          </Link>
          <Link data-testid="paper-profile-backlink" href="/wiki" style={{ color: "#64748b", fontSize: "0.82rem", textDecoration: "none", fontWeight: 750 }}>
            Wiki index
          </Link>
        </div>

        <section style={{ background: "linear-gradient(135deg, rgba(15,23,42,0.98), rgba(30,41,59,0.86))", border: "1px solid rgba(56,189,248,0.24)", borderRadius: "18px", padding: "1.25rem", marginBottom: "1rem" }}>
          <div style={{ color: "#67e8f9", fontSize: "0.72rem", letterSpacing: "0.14em", textTransform: "uppercase", fontWeight: 900 }}>
            paper profile · wiki-wide footprint
          </div>
          <div style={{ display: "flex", justifyContent: "space-between", gap: "1rem", alignItems: "flex-start", flexWrap: "wrap" }}>
            <div>
              <h1 style={{ color: "#f8fafc", fontSize: "2rem", lineHeight: 1.1, margin: "0.35rem 0 0" }}>
                {loading ? "Loading paper profile…" : deck.paperLabel}
              </h1>
              {!loading && <p style={{ color: "#cbd5e1", margin: "0.35rem 0 0", lineHeight: 1.45 }}>{deck.title}</p>}
            </div>
            {!loading && (
              <span data-testid="paper-profile-status-chip" style={{ color: STATUS_COLOR[deck.status], border: `1px solid ${STATUS_COLOR[deck.status]}66`, background: `${STATUS_COLOR[deck.status]}18`, borderRadius: "999px", padding: "0.35rem 0.7rem", fontSize: "0.72rem", fontWeight: 900 }}>
                {deck.statusLabel}
              </span>
            )}
          </div>
          <p data-testid="paper-profile-scope-caveat" style={{ color: "#94a3b8", maxWidth: "56rem", lineHeight: 1.55, margin: "0.75rem 0 0" }}>
            {deck.scopeCaveat} Paper profile is a footprint map, not a final verdict. No labels are written from this surface.
          </p>
          {!loading && deck.summaryText && (
            <p style={{ color: "#cbd5e1", maxWidth: "56rem", lineHeight: 1.55, margin: "0.75rem 0 0" }}>{deck.summaryText}</p>
          )}
          {!loading && (
            <div style={{ display: "flex", flexWrap: "wrap", gap: "0.55rem", marginTop: "1rem", color: "#cbd5e1", fontSize: "0.78rem" }}>
              <span>{deck.summary}</span>
              <span>{deck.supportCount} support</span>
              <span>{deck.counterCount} counter</span>
              <span>{deck.neutralCount} neutral</span>
              <span>{deck.voteDisagreeCount} disagree votes</span>
              <span>{deck.sourceGapCount} source gaps</span>
            </div>
          )}
          {!loading && deck.externalHref && (
            <a href={deck.externalHref} target="_blank" rel="noopener noreferrer" style={{ display: "inline-block", color: "#a5b4fc", fontSize: "0.8rem", fontWeight: 850, marginTop: "0.85rem", textDecoration: "none" }}>
              Open external paper ↗
            </a>
          )}
        </section>

        {deck.truncationDisclosure && !loading && !error && (
          <p data-testid="paper-profile-truncation-disclosure" style={{ color: "#94a3b8", fontSize: "0.8rem", lineHeight: 1.45, margin: "0 0 1rem" }}>
            {deck.truncationDisclosure}
          </p>
        )}

        {!error && (
          <PaperFootprintPanel
            payload={footprintPayload}
            loading={loading || footprintLoading}
            error={footprintError}
            onRetry={() => setFootprintRetryNonce((nonce) => nonce + 1)}
          />
        )}

        {error && !loading && (
          <p data-testid="paper-profile-error" style={{ color: "#fb923c", fontSize: "0.88rem" }}>
            {error}{" "}
            <button type="button" onClick={() => setRetryNonce((nonce) => nonce + 1)} style={{ color: "#93c5fd", background: "transparent", border: 0, padding: 0, font: "inherit", fontWeight: 850, cursor: "pointer" }}>
              Retry
            </button>
          </p>
        )}

        {!loading && !error && !deck.hasProfile && (
          <p data-testid="paper-profile-empty" style={{ color: "#64748b", border: "1px solid rgba(51,65,85,0.8)", borderRadius: "14px", padding: "1rem", background: "rgba(15,23,42,0.65)" }}>
            {deck.emptyMessage}
          </p>
        )}

        {!loading && !error && deck.hasProfile && (
          <div style={{ display: "grid", gap: "0.9rem" }}>
            {deck.pages.map((page) => (
              <section key={page.slug} data-testid="paper-profile-page-card" aria-label={page.accessibleSummary} style={{ background: "rgba(15,23,42,0.92)", border: "1px solid rgba(51,65,85,0.92)", borderLeft: `4px solid ${page.counter_count > 0 ? "#fb923c" : "#86efac"}`, borderRadius: "14px", padding: "1rem" }}>
                <div style={{ display: "flex", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap" }}>
                  <div>
                    <h2 style={{ margin: 0, color: "#f8fafc", fontSize: "1.05rem" }}>
                      <Link href={page.href} style={{ color: "inherit", textDecoration: "none" }}>{page.title}</Link>
                    </h2>
                    <p style={{ margin: "0.25rem 0 0", color: "#64748b", fontSize: "0.76rem" }}>
                      {page.claim_count} claims · {page.evidence_count} evidence rows · {page.counter_count} countering
                    </p>
                  </div>
                  <Link href={page.href} aria-label={page.accessibleSummary} style={{ color: "#93c5fd", fontSize: "0.78rem", fontWeight: 850, textDecoration: "none" }}>
                    Open page →
                  </Link>
                </div>

                <div style={{ display: "grid", gap: "0.5rem", marginTop: "0.85rem" }}>
                  {page.claims.map((claim) => (
                    <a key={`${page.slug}-${claim.claim_id}-${claim.evidence_id ?? "evidence"}`} data-testid="paper-profile-claim-row" href={claim.href} aria-label={claim.accessibleSummary} style={{ display: "block", textDecoration: "none", color: "#e2e8f0", border: "1px solid rgba(51,65,85,0.72)", borderRadius: "12px", padding: "0.75rem", background: "rgba(2,6,23,0.48)" }}>
                      <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap", alignItems: "center", marginBottom: "0.35rem" }}>
                        <span style={{ color: TONE_COLOR[claim.tone], fontSize: "0.72rem", fontWeight: 900 }}>{claim.toneLabel}</span>
                        <span style={{ color: "#94a3b8", fontSize: "0.72rem" }}>{claim.trustLabel}</span>
                        <span style={{ color: "#64748b", fontSize: "0.72rem" }}>{claim.votesAgree} agree · {claim.votesDisagree} disagree</span>
                      </div>
                      <div style={{ color: "#f8fafc", fontSize: "0.86rem", lineHeight: 1.45 }}>{claim.claimText}</div>
                      {claim.section && <div style={{ color: "#64748b", fontSize: "0.72rem", marginTop: "0.3rem" }}>{claim.section}</div>}
                    </a>
                  ))}
                </div>
              </section>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
