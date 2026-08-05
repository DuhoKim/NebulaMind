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

// Studies a HUMAN read and rejected. They stay published — the rejection and its reason are
// part of the record, not something to hide. `why` is Duho's stated reason, verbatim in
// substance; `retired` is when he pulled it.
export type Rejected = Flagship & { why: string; retired: string; kept?: string };

export const HUMAN_REJECTED: Rejected[] = [
  {
    title: "An Independent, Unlensed Gas-Phase Metallicity Deficit at z\u22489\u201310",
    summary: "An unlensed z\u22489\u201310 field sample sits \u22120.68 dex below the local mass\u2013metallicity relation on a single Te scale \u2014 a normalization deficit, explicitly not a formal detection.",
    meta: "Nakajima+23 direct-Te subset \u00b7 Pollock+26 unlensed field + GN-z11 \u00b7 cross-checked vs Isobe+26 (~1500 gal) \u00b7 systematic budget \u00b10.16 dex",
    verdict: "REJECT",
    pdf: "/studies/z9-10-unlensed-metallicity-deficit.pdf",
    updated: "2026-07-22 11:26",
    review: "/studies/z9-10-unlensed-metallicity-deficit_review_loop.md",
    methods: ["mzr"],
    frontier: 41,
    retired: "2026-08-05",
    why: "No original work. Every abundance and stellar mass is adopted from published papers (Nakajima+2023, Pollock+2026, Isobe+2026), both local anchors are published parametrizations (Curti+2020, Andrews & Martini 2013), and the result is a subtraction \u0394 = (12+log O/H)obs \u2212 MZR(logM\u2605) over N=5\u20136 galaxies. Nothing was measured. The conclusion was already published by the ~1500-galaxy stacked-Te sample the paper itself cites.",
    kept: "The systematics work is real and was kept: the single-Te-scale restriction, the unlensed-only cut after Deep Research caught lens contamination in the \u201cclean\u201d subset, the local-anchor swap quantifying that systematic at 0.042 dex, and the Te-scale Monte Carlo that deflated a formal ~22\u03c3 to ~4.5\u03c3. Those methods are the direct ancestors of the anchor-gap census\u2019s contract-grade discipline.",
  },
];

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
