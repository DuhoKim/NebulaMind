"use client";

// Frontier-study drafts from the autonomous research pipeline — multi-page AASTeX
// manuscripts, one per top frontier. More developed than the single-measurement
// pipeline runs, but still descriptive drafts (no human sign-off). Hosted under
// /agent-reports/research-frontiers/. Curated list.
import { PB_CSS } from "./PipelineBoard";
import { MethodChips } from "./methodLinks";
import { PaperVideo } from "./PaperVideo";
import { PAPER_VIDEOS } from "./paperVideos";
import { RawStyle } from "./rawStyle";

export type Draft = { title: string; sub: string; pages: string; pdf: string; updated: string; verdict?: string; review?: string; methods?: string[]; frontier?: number };

export const FRONTIER: Draft[] = [
  {
    title: "The reionization photon-budget “crisis” is set by ξ_ion and the star-formation-rate density, not the data",
    sub: "Solving for the LyC escape fraction required of star-forming galaxies to close the reionization ionizing budget across a 232-point (z=5–12 × 8 systematic-corner) grid. The required f_esc rises steeply with redshift and crosses the proxy-inferred value (~6%) at a crisis-onset redshift spanning z≈5–8.75 across defensible assumptions, exceeding the physical ceiling f_esc=1 anywhere from z≈8.5 to never. Both literature positions — “crisis” and “galaxies suffice” — fall out of the same envelope, so the verdict is dominated by ξ_ion and the SFRD, not the data.",
    pages: "synthesis",
    pdf: "/agent-reports/research-frontiers/reionization-fesc-budget-landscape.pdf",
    updated: "2026-07-23 03:00",
    verdict: "REVIEW-READY",
    review: "/agent-reports/research-frontiers/reionization-fesc-budget-landscape_review_loop.md",
    frontier: 16,
  },
  {
    title: "Galaxy scaling relations from z≈0 to the JWST frontier",
    sub: "Reframed — the paper’s main claim is withdrawn. On regeneration the crew showed the apparent z<6 star-forming-main-sequence “elevation” is largely an emission-line selection artifact (~40–60% at z<6; pure selection not excluded below z≈6), so the “rapid early enrichment” reading is not earned. Only the z>6 residual survives; the metallicity deficit defers to the flagship z≈9–10 study, and the selection forward-model is folded into the TNG confrontation below. Not a standalone result.",
    pages: "4 pp",
    pdf: "/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf",
    updated: "2026-07-23 20:35",
    verdict: "WITHDRAWN",
    review: "/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft_review_loop.md",
    methods: ["ms", "mzr"],
    frontier: 41,
  },
  {
    title: "The z≈4–6 massive-galaxy abundance is consistent with IllustrisTNG once the stellar-mass budget and aperture basis are accounted for",
    sub: "The z>4 “too massive, too early” excess, re-examined like-for-like. Pinning the TNG aperture to the observed total-mass basis (+0.13 dex, from real TNG100-1 catalogs) leaves a 0.31 dex excess erased by a 0.20 dex shift — ~0.4× an itemized 0.46–0.55 dex systematic budget, so no robust tension at z≈5; the unshifted abundance already sits at the fiducial ΛCDM efficiency (ε≈0.20), making this a test of TNG’s calibration, not ΛCDM. z≈7–9 is honestly outside budget (0.72 dex, photometric), and the spectroscopic quiescent z>6 excess (~2 dex) is the one genuine residual.",
    pages: "4 pp",
    pdf: "/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf",
    updated: "2026-07-23 20:14",
    verdict: "REVIEW-READY",
    review: "/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics_review_loop.md",
    methods: ["smf", "simobs"],
    frontier: 41,
  },
  {
    title: "Disentangling aperture and calibration systematics in the gas-phase MZR: a practitioner’s framework",
    sub: "A methods/review synthesis separating the two systematics that get conflated in MZR comparisons: calibration-scale offsets (up to ~0.7 dex) and aperture bias (>0.15 dex below ~20% covering fraction), plus DIG contamination. Recommends single-scale reporting, covering-fraction floors, and IFS ground truth.",
    pages: "review",
    pdf: "/agent-reports/research-frontiers/mzr-aperture-calibration-framework.pdf",
    updated: "2026-07-21 12:41",
    verdict: "REVIEW-CLEARED",
    review: "/agent-reports/research-frontiers/mzr-aperture-calibration-framework_review_loop.md",
    methods: ["mzr"],
    frontier: 41,
  },
  {
    title: "Calibration is not validation: confronting IllustrisTNG with observed scaling-relation evolution",
    sub: "The simulation tested by its predictions away from its z≈0 calibration point, SDSS→JWST. TNG over-evolves the star-forming main sequence — a +0.41/+0.49 dex gap at z≈4.7/5.4 that is a conservative lower bound: de-biasing the emission-line selection can only widen it (to +0.46/+0.83 dex, up to ~+1.1 in the aggressive corner; sign robust across all 9 configs). Placing TNG on the observed total-mass basis (+0.13 dex aperture correction) cancels in the internal-evolution differencing, so the result is robust to it; the apparent metallicity discrepancy dissolves on a matched Te scale.",
    pages: "4 pp",
    pdf: "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf",
    updated: "2026-07-23 20:29",
    review: "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft_review_loop.md",
    methods: ["simobs", "ms", "mzr"],
    frontier: 41,
  },
];

export default function FrontierDrafts() {
  return (
    <div className="pb">
      <RawStyle css={PB_CSS} />
      <p className="pb-lede">
        Multi-page manuscript drafts from the <b>autonomous research pipeline</b>, one per top frontier —
        more developed than the single-measurement runs, but <b>descriptive drafts</b>: no human has cleared any of them.
        Two now carry an <b>automated-referee verdict</b> (advisory — not a human or journal referee, so the paper stays <b>not validated</b>).
      </p>
      <div className="pb-runs">
        {FRONTIER.map((f) => (
          <div className="pb-run" key={f.pdf}>
            <div className="pb-run-top">
              <span className="pb-run-title">{f.title}</span>
              <span style={{ display: "flex", gap: ".4rem", alignItems: "center", flexShrink: 0 }}>
                {f.verdict && <span className="pb-chip" style={{ borderColor: "#9aa3b8", color: "#9aa3b8" }}>{f.verdict}</span>}
                <span className="pb-chip" style={{ borderColor: "#e0a458", color: "#e0a458" }}>draft</span>
              </span>
            </div>
            <p className="pb-run-summary">{f.sub}</p>
            <div className="pb-run-chips"><span className="pb-src">AASTeX · {f.pages}</span></div>
            <MethodChips methods={f.methods} />
            <PaperVideo videoId={PAPER_VIDEOS[f.pdf]} title={f.title} />
            <div className="pb-run-links"><a href={f.pdf} target="_blank" rel="noopener noreferrer">read the draft (PDF) ↗</a></div>
            <p className="pb-tag">descriptive draft — not validated, not published</p>
          </div>
        ))}
      </div>
      <p className="pb-flag-note">{FRONTIER.length} frontier drafts. The hand-guided study lives under <b>Flagship studies</b>; the fully-automated runs under <b>Pipeline runs</b>.</p>
    </div>
  );
}
