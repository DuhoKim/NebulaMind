import Link from "next/link";
import { buildCrossPagePaperFootprintDeck, type CrossPagePaperFootprintResponse, type CrossPagePaperTone } from "../../[slug]/sources/crossPagePaperFootprint";

type PaperFootprintPanelProps = {
  payload: CrossPagePaperFootprintResponse | null;
  loading: boolean;
  error: string | null;
  onRetry: () => void;
};

const MAX_VISIBLE_PAGES = 3;
const MAX_VISIBLE_CLAIMS_PER_PAGE = 2;

const TONE_COLOR: Record<CrossPagePaperTone, string> = {
  counter: "#fb923c",
  support: "#86efac",
  neutral: "#cbd5e1",
};

function toneLabel(tone?: string | null): string {
  if (tone === "counter") return "Countering";
  if (tone === "support") return "Supporting";
  return "Neutral";
}

function numberValue(value: unknown): number {
  const n = Number(value ?? 0);
  return Number.isFinite(n) ? n : 0;
}

function statChip(label: string, value: number, color = "#cbd5e1") {
  return (
    <span style={{ display: "inline-flex", alignItems: "center", gap: "0.25rem", border: "1px solid rgba(148,163,184,0.22)", borderRadius: "999px", padding: "0.25rem 0.45rem", color: "#94a3b8", background: "rgba(15,23,42,0.62)" }}>
      <strong style={{ color }}>{value.toLocaleString()}</strong> {label}
    </span>
  );
}

function compactClaimText(text: string): string {
  const clean = text.replace(/\s+/g, " ").trim();
  return clean.length > 170 ? `${clean.slice(0, 167)}…` : clean;
}

export default function PaperFootprintPanel({ payload, loading, error, onRetry }: PaperFootprintPanelProps) {
  const deck = buildCrossPagePaperFootprintDeck(payload ? [payload] : []);
  const item = deck.items[0] || null;
  const visiblePages = item ? item.pages.slice(0, MAX_VISIBLE_PAGES) : [];
  const hiddenPageCount = item ? Math.max(0, item.pages.length - visiblePages.length) : 0;
  const summary = loading
    ? "Loading wiki-wide citation footprint…"
    : item
      ? `${item.pageCount.toLocaleString()} wiki pages cite this paper across ${item.claimCount.toLocaleString()} linked claims.`
      : deck.summary;

  return (
    <section data-testid="paper-footprint-panel" style={{ background: "rgba(8,13,31,0.94)", border: "1px solid rgba(125,211,252,0.28)", borderRadius: "16px", padding: "0.85rem", marginBottom: "1rem" }}>
      <div style={{ display: "flex", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap", alignItems: "flex-start" }}>
        <div style={{ minWidth: "16rem", flex: "1 1 18rem" }}>
          <div style={{ color: "#7dd3fc", fontSize: "0.68rem", letterSpacing: "0.14em", textTransform: "uppercase", fontWeight: 900 }}>
            cited across nebulamind
          </div>
          <h2 style={{ color: "#f8fafc", fontSize: "1.08rem", margin: "0.18rem 0" }}>Cited across NebulaMind</h2>
          <p data-testid="paper-footprint-summary" style={{ color: "#cbd5e1", margin: 0, lineHeight: 1.42, fontSize: "0.88rem" }}>
            {summary}
          </p>
        </div>
        {item && (
          <div style={{ display: "flex", gap: "0.35rem", flexWrap: "wrap", justifyContent: "flex-end", color: "#cbd5e1", fontSize: "0.72rem", maxWidth: "23rem" }}>
            {statChip("pages", item.pageCount, "#7dd3fc")}
            {statChip("claims", item.claimCount, "#f8fafc")}
            {statChip("support", item.supportCount, TONE_COLOR.support)}
            {statChip("counter", item.counterCount, TONE_COLOR.counter)}
            {statChip("neutral", item.neutralCount, TONE_COLOR.neutral)}
          </div>
        )}
      </div>

      <p style={{ color: "#94a3b8", fontSize: "0.76rem", lineHeight: 1.4, margin: "0.55rem 0 0" }}>
        {deck.scopeCaveat} This panel is not a final verdict. No labels are written from this panel.
      </p>

      {error && !loading && (
        <p data-testid="paper-footprint-error" style={{ color: "#fb923c", fontSize: "0.84rem", margin: "0.65rem 0 0" }}>
          {error}{" "}
          <button data-testid="paper-footprint-retry" type="button" onClick={onRetry} style={{ color: "#93c5fd", background: "transparent", border: 0, padding: 0, font: "inherit", fontWeight: 850, cursor: "pointer" }}>
            Retry
          </button>
        </p>
      )}

      {!loading && !error && !deck.hasCrossPageFootprint && (
        <p style={{ color: "#64748b", fontSize: "0.84rem", margin: "0.65rem 0 0" }}>No wiki-wide citation footprint is available for this paper yet.</p>
      )}

      {item && !loading && !error && (
        <div style={{ display: "grid", gap: "0.55rem", marginTop: "0.7rem" }}>
          {visiblePages.map((page) => {
            const pageHref = `/wiki/${page.slug}`;
            const pageTone = numberValue(page.counter_count) > 0 ? "counter" : numberValue(page.support_count) > 0 ? "support" : "neutral";
            const visibleClaims = page.claims.slice(0, MAX_VISIBLE_CLAIMS_PER_PAGE);
            const hiddenClaims = Math.max(0, page.claims.length - visibleClaims.length);
            return (
              <article key={page.page_id ?? page.slug} data-testid="paper-footprint-page-card" aria-label={`${page.title}: ${numberValue(page.claim_count)} claims and ${numberValue(page.evidence_count)} evidence rows cite this paper.`} style={{ border: "1px solid rgba(51,65,85,0.78)", borderLeft: `3px solid ${TONE_COLOR[pageTone]}`, borderRadius: "12px", padding: "0.7rem", background: "rgba(15,23,42,0.7)" }}>
                <div style={{ display: "flex", justifyContent: "space-between", gap: "0.6rem", flexWrap: "wrap", alignItems: "baseline" }}>
                  <div>
                    <h3 style={{ color: "#f8fafc", fontSize: "0.95rem", margin: 0 }}>
                      <Link href={pageHref} style={{ color: "inherit", textDecoration: "none" }}>{page.title}</Link>
                    </h3>
                    <p style={{ color: "#64748b", fontSize: "0.72rem", margin: "0.18rem 0 0" }}>
                      {numberValue(page.claim_count)} claims · {numberValue(page.evidence_count)} evidence · {numberValue(page.counter_count)} countering
                    </p>
                  </div>
                  <Link href={pageHref} aria-label={`${page.title} — open cited wiki page`} style={{ color: "#93c5fd", fontSize: "0.76rem", fontWeight: 850, textDecoration: "none" }}>
                    Open page →
                  </Link>
                </div>

                {visibleClaims.length > 0 && (
                  <div style={{ display: "grid", gap: "0.35rem", marginTop: "0.55rem" }}>
                    {visibleClaims.map((claim) => {
                      const tone = (claim.tone === "counter" || claim.tone === "support" || claim.tone === "neutral") ? claim.tone : "neutral";
                      const claimHref = claim.href || `${pageHref}#claim-${claim.claim_id}`;
                      return (
                        <a key={`${page.slug}-${claim.claim_id}-${claim.evidence_id ?? "evidence"}`} data-testid="paper-footprint-claim-row" href={claimHref} aria-label={`${page.title}: ${toneLabel(tone)} evidence for ${claim.trust_level || "unverified"} claim. ${claim.claim_text}`} style={{ display: "block", color: "#e2e8f0", textDecoration: "none", border: "1px solid rgba(51,65,85,0.58)", borderRadius: "10px", padding: "0.52rem 0.6rem", background: "rgba(2,6,23,0.36)" }}>
                          <div style={{ display: "flex", gap: "0.38rem", flexWrap: "wrap", alignItems: "center", marginBottom: "0.22rem" }}>
                            <span style={{ color: TONE_COLOR[tone], fontSize: "0.7rem", fontWeight: 900 }}>{toneLabel(tone)}</span>
                            <span style={{ color: "#94a3b8", fontSize: "0.7rem" }}>{claim.trust_level || "unverified"}</span>
                            <span style={{ color: "#64748b", fontSize: "0.7rem" }}>{numberValue(claim.votes_agree)} agree · {numberValue(claim.votes_disagree)} disagree</span>
                          </div>
                          <div style={{ color: "#f8fafc", fontSize: "0.8rem", lineHeight: 1.36 }}>{compactClaimText(claim.claim_text)}</div>
                        </a>
                      );
                    })}
                    {hiddenClaims > 0 && <div style={{ color: "#64748b", fontSize: "0.72rem" }}>+{hiddenClaims} more linked claims on this page.</div>}
                  </div>
                )}
              </article>
            );
          })}
          {hiddenPageCount > 0 && <div style={{ color: "#64748b", fontSize: "0.76rem" }}>+{hiddenPageCount} more cited wiki pages available through the paper-footprint endpoint.</div>}
        </div>
      )}
    </section>
  );
}
