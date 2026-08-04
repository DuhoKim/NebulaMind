"use client";

// Flagship, human-guided studies (hosted under /studies/) — the curated papers
// that went the full distance: real forward-model + referee loop, orchestrated by
// the crew, not the automated pipeline. Still descriptive until a human clears them.
// Curated list; add an entry per published study.
import { PB_CSS } from "./PipelineBoard";
import { MethodChips } from "./methodLinks";
import { PaperVideo } from "./PaperVideo";
import { PAPER_VIDEOS } from "./paperVideos";
import { RawStyle } from "./rawStyle";

export type Flagship = { title: string; summary: string; meta: string; verdict: string; pdf: string; updated: string; review?: string; methods?: string[]; frontier?: number };

export const FLAGSHIP: Flagship[] = [
  {
    title: "A Systematics-Bounded Redshift Sweep of the Reionization Ionizing-Photon Budget",
    summary: "Under frozen literature anchors, the required-vs-inferred escape-fraction mismatch becomes robust to the stated systematics only above z\u22488 (crossing z_c=8.05, bootstrap 8.03\u20138.06); removing the JWST-motivated SFRD boost strengthens the shortfall (z_c\u21927.62). Proxy transport is named as the only remaining escape route.",
    meta: "z=6\u201310 sweep (\u0394z=0.5, 40k-draw systematic MC each, fixed seed) \u00b7 referee MINOR \u2192 all four revisions applied \u00b7 referee-reproduced numbers (max dev 2.2e-16) \u00b7 4-seat merit mean 5.4 (DR abstained)",
    verdict: "REVIEW-READY",
    pdf: "/studies/fesc-zsweep-photon-budget.pdf",
    updated: "2026-08-04 21:39",
    review: "/studies/fesc-zsweep-photon-budget_review_loop.md",
    methods: ["fesc"],
    frontier: 16,
  },
  {
    title: "The Public-Archive Direct-Te Anchor Gap at z>3: A Contract-Grade Census",
    summary: "A frozen-contract census of every public VizieR table yields five contract-grade direct-Te metallicity anchors at z>3 (vs ~25 conservatively forecast) \u2014 no mass bin reaches the pre-committed minimum, so no deficit verdict is possible at contract-grade public statistics. The debate's resolution currently rests on data not publicly quotable at uniform rigor.",
    meta: "79 tables \u2192 748 z>3 auroral rows \u2192 5 anchors (S/N\u22655, source-tabulated errors, joined masses) \u00b7 reviewed-script protocol (1 review + 6 micro-deltas) \u00b7 forensics: all 5 anchors reproduced to the digit \u00b7 referee MINOR \u2192 fixed",
    verdict: "REVIEW-READY",
    pdf: "/studies/c41-highz-mzr-calibration-anchored.pdf",
    updated: "2026-08-04 21:39",
    review: "/studies/c41-highz-mzr-calibration-anchored_review_loop.md",
    methods: ["mzr"],
    frontier: 41,
  },
  {
    title: "An Independent, Unlensed Gas-Phase Metallicity Deficit at z≈9–10",
    summary: "An unlensed z≈9–10 field sample sits −0.68 dex below the local mass–metallicity relation on a single Te scale — a robust normalization deficit, explicitly not a formal detection.",
    meta: "Nakajima+23 direct-Te subset · Pollock+26 unlensed CAPERS/JADES + GN-z11 (z=10.6) · cross-checked vs Isobe+26 (~1500 gal) · systematic error budget ±0.16 dex, abs. Te scale (0.15) dominant",
    verdict: "REVIEW-READY",
    pdf: "/studies/z9-10-unlensed-metallicity-deficit.pdf",
    updated: "2026-07-22 11:26",
    review: "/studies/z9-10-unlensed-metallicity-deficit_review_loop.md",
    methods: ["mzr"],
    frontier: 41,
  },
];

const vcolor = (v: string) => ({ ACCEPT: "#4ad6c4", MINOR: "#e0a458", MAJOR: "#e0774f", REJECT: "#f47272" }[v.toUpperCase()] ?? "#9aa3b8");

export default function FlagshipStudies() {
  return (
    <div className="pb">
      <RawStyle css={PB_CSS} />
      <p className="pb-lede">
        These are the <b>hand-guided</b> studies — orchestrated by the crew, not the automated pipeline. Each went the
        <b> full distance</b> (a real forward-model and referee loop) and is the most complete work the Lab produces.
        They are still <b>descriptive, not validated</b>: a human hasn&rsquo;t cleared any of them either.
      </p>
      <div className="pb-runs">
        {FLAGSHIP.map((f) => (
          <div className="pb-run pb-flag" key={f.pdf}>
            <div className="pb-run-top">
              <span className="pb-run-title">{f.title}</span>
              <span className="pb-chip" style={{ borderColor: vcolor(f.verdict), color: vcolor(f.verdict) }}>{f.verdict} · not accepted</span>
            </div>
            <p className="pb-run-summary">{f.summary}</p>
            <div className="pb-run-chips"><span className="pb-src pb-src-flag">flagship · hand-guided</span></div>
            <p className="pb-run-meta">{f.meta}</p>
            <MethodChips methods={f.methods} />
            <PaperVideo videoId={PAPER_VIDEOS[f.pdf]} title={f.title} />
            <div className="pb-run-links"><a href={f.pdf} target="_blank" rel="noopener noreferrer">read the manuscript (PDF) ↗</a></div>
            <p className="pb-tag">descriptive — not validated, not published</p>
          </div>
        ))}
      </div>
      <p className="pb-flag-note">{FLAGSHIP.length} published so far. The fully-automated runs — the fast, high-attrition track — live under <b>Pipeline runs</b>.</p>
    </div>
  );
}
