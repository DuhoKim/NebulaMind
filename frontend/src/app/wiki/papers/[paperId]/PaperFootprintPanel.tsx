import Link from "next/link";
import { buildCrossPagePaperFootprintDeck, type CrossPagePaperFootprintResponse, type CrossPagePaperTone } from "../../[slug]/sources/crossPagePaperFootprint";

type PaperFootprintPanelProps = {
  payload: CrossPagePaperFootprintResponse | null;
  loading: boolean;
  error: string | null;
  onRetry: () => void;
};

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

export default function PaperFootprintPanel({ payload, loading, error, onRetry }: PaperFootprintPanelProps) {
  const deck = buildCrossPagePaperFootprintDeck(payload ? [payload] : []);
  const item = deck.items[0] || null;

  return (
    <section data-testid="paper-footprint-panel" style={{ background: "rgba(8,13,31,0.94)", border: "1px solid rgba(125,211,252,0.28)", borderRadius: "16px", padding: "1rem", marginBottom: "1rem" }}>
      <div style={{ color: "#7dd3fc", fontSize: "0.72rem", letterSpacing: "0.14em", textTransform: "uppercase", fontWeight: 900 }}>
        cited across nebulamind
      </div>
      <div style={{ display: "flex", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap", alignItems: "flex-start" }}>
        <div>
          <h2 style={{ color: "#f8fafc", fontSize: "1.2rem", margin: "0.25rem 0" }}>Cited across NebulaMind</h2>
          <p data-testid="paper-footprint-summary" style={{ color: "#cbd5e1", margin: 0, lineHeight: 1.5 }}>
            {loading ? "Loading wiki-wide citation footprint…" : deck.summary}
          </p>
        </div>
        {item && (
          <div style={{ display: "flex", gap: "0.45rem", flexWrap: "wrap", color: "#cbd5e1", fontSize: "0.74rem" }}>
            <span>{item.pageCount} pages</span>
            <span>{item.claimCount} claims</span>
            <span>{item.supportCount} support</span>
            <span>{item.counterCount} counter</span>
            <span>{item.neutralCount} neutral</span>
          </div>
        )}
      </div>
      <p style={{ color: "#94a3b8", fontSize: "0.8rem", lineHeight: 1.45, margin: "0.75rem 0 0" }}>
        {deck.scopeCaveat} This panel is not a final verdict. No labels are written from this panel.
      </p>

      {error && !loading && (
        <p data-testid="paper-footprint-error" style={{ color: "#fb923c", fontSize: "0.86rem", margin: "0.85rem 0 0" }}>
          {error}{" "}
          <button data-testid="paper-footprint-retry" type="button" onClick={onRetry} style={{ color: "#93c5fd", background: "transparent", border: 0, padding: 0, font: "inherit", fontWeight: 850, cursor: "pointer" }}>
            Retry
          </button>
        </p>
      )}

      {!loading && !error && !deck.hasCrossPageFootprint && (
        <p style={{ color: "#64748b", fontSize: "0.85rem", margin: "0.85rem 0 0" }}>No wiki-wide citation footprint is available for this paper yet.</p>
      )}

      {item && !loading && !error && (
        <div style={{ display: "grid", gap: "0.75rem", marginTop: "0.9rem" }}>
          {item.pages.map((page) => {
            const pageHref = `/wiki/${page.slug}`;
            const pageTone = numberValue(page.counter_count) > 0 ? "counter" : numberValue(page.support_count) > 0 ? "support" : "neutral";
            return (
              <article key={page.page_id ?? page.slug} data-testid="paper-footprint-page-card" aria-label={`${page.title}: ${numberValue(page.claim_count)} claims and ${numberValue(page.evidence_count)} evidence rows cite this paper.`} style={{ border: "1px solid rgba(51,65,85,0.85)", borderLeft: `4px solid ${TONE_COLOR[pageTone]}`, borderRadius: "14px", padding: "0.85rem", background: "rgba(15,23,42,0.82)" }}>
                <div style={{ display: "flex", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap" }}>
                  <div>
                    <h3 style={{ color: "#f8fafc", fontSize: "1rem", margin: 0 }}>
                      <Link href={pageHref} style={{ color: "inherit", textDecoration: "none" }}>{page.title}</Link>
                    </h3>
                    <p style={{ color: "#64748b", fontSize: "0.75rem", margin: "0.25rem 0 0" }}>
                      {numberValue(page.claim_count)} claims · {numberValue(page.evidence_count)} evidence rows · {numberValue(page.counter_count)} countering
                    </p>
                  </div>
                  <Link href={pageHref} aria-label={`${page.title} — open cited wiki page`} style={{ color: "#93c5fd", fontSize: "0.78rem", fontWeight: 850, textDecoration: "none" }}>
                    Open page →
                  </Link>
                </div>

                <div style={{ display: "grid", gap: "0.45rem", marginTop: "0.75rem" }}>
                  {page.claims.map((claim) => {
                    const tone = (claim.tone === "counter" || claim.tone === "support" || claim.tone === "neutral") ? claim.tone : "neutral";
                    const claimHref = claim.href || `${pageHref}#claim-${claim.claim_id}`;
                    return (
                      <a key={`${page.slug}-${claim.claim_id}-${claim.evidence_id ?? "evidence"}`} data-testid="paper-footprint-claim-row" href={claimHref} aria-label={`${page.title}: ${toneLabel(tone)} evidence for ${claim.trust_level || "unverified"} claim. ${claim.claim_text}`} style={{ display: "block", color: "#e2e8f0", textDecoration: "none", border: "1px solid rgba(51,65,85,0.72)", borderRadius: "12px", padding: "0.7rem", background: "rgba(2,6,23,0.45)" }}>
                        <div style={{ display: "flex", gap: "0.45rem", flexWrap: "wrap", alignItems: "center", marginBottom: "0.3rem" }}>
                          <span style={{ color: TONE_COLOR[tone], fontSize: "0.72rem", fontWeight: 900 }}>{toneLabel(tone)}</span>
                          <span style={{ color: "#94a3b8", fontSize: "0.72rem" }}>{claim.trust_level || "unverified"}</span>
                          <span style={{ color: "#64748b", fontSize: "0.72rem" }}>{numberValue(claim.votes_agree)} agree · {numberValue(claim.votes_disagree)} disagree</span>
                        </div>
                        <div style={{ color: "#f8fafc", fontSize: "0.84rem", lineHeight: 1.45 }}>{claim.claim_text}</div>
                        {claim.section && <div style={{ color: "#64748b", fontSize: "0.72rem", marginTop: "0.3rem" }}>{claim.section}</div>}
                      </a>
                    );
                  })}
                </div>
              </article>
            );
          })}
        </div>
      )}
    </section>
  );
}
