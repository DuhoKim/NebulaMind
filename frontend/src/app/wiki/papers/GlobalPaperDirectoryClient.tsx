"use client";

import Link from "next/link";
import { FormEvent, useEffect, useMemo, useState } from "react";
import { buildGlobalPaperDirectoryDeck, type GlobalPaperDirectoryPayload } from "./globalPaperDirectory";

type GlobalPaperDirectoryClientProps = {
  testOnlyFixtureData?: GlobalPaperDirectoryPayload;
};

const STATUS_COLOR = {
  needs_adjudication: "#fb923c",
  needs_source: "#facc15",
  ready_to_review: "#86efac",
} as const;

export default function GlobalPaperDirectoryClient({ testOnlyFixtureData }: GlobalPaperDirectoryClientProps = {}) {
  const [query, setQuery] = useState("");
  const [submittedQuery, setSubmittedQuery] = useState("");
  const [payload, setPayload] = useState<GlobalPaperDirectoryPayload | null>(testOnlyFixtureData || null);
  const [loading, setLoading] = useState(!testOnlyFixtureData);
  const [error, setError] = useState<string | null>(null);
  const [retryNonce, setRetryNonce] = useState(0);

  useEffect(() => {
    if (testOnlyFixtureData) {
      setPayload(testOnlyFixtureData);
      setLoading(false);
      setError(null);
      return;
    }
    const params = new URLSearchParams({ limit: "25" });
    if (submittedQuery.trim()) params.set("q", submittedQuery.trim());
    setLoading(true);
    setError(null);
    fetch(`/api/pages/paper-directory?${params.toString()}`)
      .then((response) => {
        if (!response.ok) throw new Error(`paper-directory ${response.status}`);
        return response.json();
      })
      .then((data) => {
        setPayload(data);
        setLoading(false);
      })
      .catch(() => {
        setError("Couldn't load global paper directory. Retry.");
        setLoading(false);
      });
  }, [submittedQuery, retryNonce, testOnlyFixtureData]);

  const deck = useMemo(
    () => buildGlobalPaperDirectoryDeck(payload, testOnlyFixtureData ? submittedQuery : ""),
    [payload, submittedQuery, testOnlyFixtureData],
  );

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setSubmittedQuery(query.trim());
  };

  return (
    <main data-testid="global-paper-directory" style={{ minHeight: "100vh", background: "#020617", color: "#e2e8f0" }}>
      <div style={{ maxWidth: "72rem", margin: "0 auto", padding: "3rem 1rem" }}>
        <div style={{ marginBottom: "1.5rem" }}>
          <Link href="/wiki" style={{ color: "#93c5fd", fontSize: "0.82rem", textDecoration: "none", fontWeight: 750 }}>
            ← Wiki directory
          </Link>
        </div>

        <section style={{ background: "linear-gradient(135deg, rgba(15,23,42,0.98), rgba(30,41,59,0.86))", border: "1px solid rgba(56,189,248,0.24)", borderRadius: "18px", padding: "1.25rem", marginBottom: "1.25rem" }}>
          <div style={{ color: "#67e8f9", fontSize: "0.72rem", letterSpacing: "0.14em", textTransform: "uppercase", fontWeight: 900 }}>
            wiki-wide evidence map
          </div>
          <h1 style={{ color: "#f8fafc", fontSize: "2rem", lineHeight: 1.1, margin: "0.35rem 0" }}>
            Global paper directory
          </h1>
          <p data-testid="global-paper-scope-caveat" style={{ color: "#94a3b8", maxWidth: "52rem", lineHeight: 1.55, margin: 0 }}>
            Across indexed wiki evidence rows; directory/search, not a final verdict. No labels are written.
          </p>

          <form onSubmit={onSubmit} role="search" style={{ display: "flex", gap: "0.65rem", flexWrap: "wrap", marginTop: "1rem" }}>
            <label style={{ position: "absolute", left: "-10000px" }} htmlFor="global-paper-search">
              Search indexed papers
            </label>
            <input
              id="global-paper-search"
              data-testid="global-paper-search-input"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="Search title, arXiv ID, author, or wiki page…"
              style={{ flex: "1 1 18rem", minWidth: 0, border: "1px solid rgba(148,163,184,0.32)", borderRadius: "999px", background: "rgba(2,6,23,0.78)", color: "#f8fafc", padding: "0.7rem 0.95rem", fontSize: "0.92rem" }}
            />
            <button
              type="submit"
              data-testid="global-paper-search-submit"
              style={{ border: "1px solid rgba(56,189,248,0.45)", borderRadius: "999px", background: "rgba(56,189,248,0.16)", color: "#bae6fd", fontWeight: 850, padding: "0.7rem 1rem", cursor: "pointer" }}
            >
              Search papers
            </button>
          </form>
        </section>

        <div data-testid="global-paper-search-summary" style={{ color: "#cbd5e1", fontSize: "0.86rem", marginBottom: "1rem" }}>
          {loading ? "Loading global paper directory…" : error ? "Paper directory unavailable" : deck.summary}
        </div>
        {!loading && !error && deck.truncationDisclosure && (
          <p data-testid="global-paper-truncation-disclosure" style={{ color: "#94a3b8", fontSize: "0.78rem", lineHeight: 1.45, marginTop: "-0.55rem", marginBottom: "1rem" }}>
            {deck.truncationDisclosure}
          </p>
        )}

        {error && !loading && (
          <p data-testid="global-paper-error" style={{ color: "#fb923c", fontSize: "0.86rem" }}>
            {error}{" "}
            <button type="button" onClick={() => setRetryNonce((nonce) => nonce + 1)} style={{ color: "#93c5fd", background: "transparent", border: 0, padding: 0, font: "inherit", fontWeight: 850, cursor: "pointer" }}>
              Retry
            </button>
          </p>
        )}

        {!loading && !error && !deck.hasResults && (
          <p data-testid="global-paper-empty" style={{ color: "#64748b", border: "1px solid rgba(51,65,85,0.8)", borderRadius: "14px", padding: "1rem", background: "rgba(15,23,42,0.65)" }}>
            {deck.emptyMessage} Try an arXiv ID, author surname, paper title, or wiki page title.
          </p>
        )}

        {!loading && !error && deck.hasResults && (
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: "0.85rem" }}>
            {deck.items.map((item) => (
              <article key={item.id} data-testid="global-paper-card" aria-label={item.accessibleSummary} style={{ background: "rgba(15,23,42,0.9)", border: "1px solid rgba(51,65,85,0.92)", borderLeft: `4px solid ${STATUS_COLOR[item.status]}`, borderRadius: "14px", padding: "1rem" }}>
                <div style={{ display: "flex", justifyContent: "space-between", gap: "0.75rem", alignItems: "flex-start" }}>
                  <div>
                    <h2 style={{ color: "#f8fafc", fontSize: "1rem", margin: 0 }}>{item.paperLabel}</h2>
                    <p style={{ color: "#cbd5e1", fontSize: "0.82rem", margin: "0.2rem 0 0", lineHeight: 1.45 }}>{item.title}</p>
                  </div>
                  <span style={{ color: STATUS_COLOR[item.status], fontSize: "0.72rem", fontWeight: 900, whiteSpace: "nowrap" }}>
                    {item.statusLabel}
                  </span>
                </div>

                <p style={{ color: "#94a3b8", fontSize: "0.76rem", lineHeight: 1.45, minHeight: "2.1rem" }}>
                  {item.summary || "No abstract summary is available in the evidence index yet."}
                </p>

                <div style={{ color: item.counterCount > 0 ? "#fb923c" : "#86efac", fontSize: "0.78rem", fontWeight: 850 }}>
                  {item.impactLabel}
                </div>
                <div style={{ color: "#64748b", fontSize: "0.72rem", marginTop: "0.25rem" }}>
                  {item.supportCount} support · {item.counterCount} counter · {item.neutralCount} neutral · {item.evidenceCount} evidence rows
                </div>

                <div style={{ display: "flex", flexWrap: "wrap", gap: "0.5rem", marginTop: "0.75rem" }}>
                  <Link
                    data-testid="global-paper-footprint-link"
                    href={item.footprintHref}
                    aria-label={item.accessibleSummary}
                    style={{ color: "#93c5fd", fontSize: "0.78rem", fontWeight: 850, textDecoration: "none" }}
                  >
                    Open footprint context →
                  </Link>
                  {item.externalHref && (
                    <a href={item.externalHref} target="_blank" rel="noopener noreferrer" style={{ color: "#a5b4fc", fontSize: "0.78rem", fontWeight: 850, textDecoration: "none" }}>
                      Paper ↗
                    </a>
                  )}
                </div>

                <div style={{ borderTop: "1px solid rgba(51,65,85,0.75)", marginTop: "0.75rem", paddingTop: "0.65rem", display: "grid", gap: "0.35rem" }}>
                  {item.pages.slice(0, 3).map((page) => (
                    <Link key={page.slug} href={page.href} style={{ color: "#cbd5e1", textDecoration: "none", fontSize: "0.74rem" }}>
                      {page.title} <span style={{ color: "#64748b" }}>· {page.claim_count} claims · {page.counter_count} countering</span>
                    </Link>
                  ))}
                </div>
              </article>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
