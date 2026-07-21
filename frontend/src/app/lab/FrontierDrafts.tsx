"use client";

// Frontier-study drafts from the autonomous research pipeline — multi-page AASTeX
// manuscripts, one per top frontier. More developed than the single-measurement
// pipeline runs, but still descriptive drafts (no human sign-off). Hosted under
// /agent-reports/research-frontiers/. Curated list.
import { PB_CSS } from "./PipelineBoard";
import { MethodChips } from "./methodLinks";

export type Draft = { title: string; sub: string; pages: string; pdf: string; updated: string; verdict?: string; review?: string; methods?: string[] };

export const FRONTIER: Draft[] = [
  {
    title: "Galaxy scaling relations from z≈0 to the JWST frontier",
    sub: "The star-forming main sequence and the mass–metallicity relation anchored on ~5×10⁵ SDSS galaxies, then confronted with JWST out to the frontier.",
    pages: "3 pp",
    pdf: "/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf",
    updated: "2026-07-19 23:10",
    methods: ["ms", "mzr"],
  },
  {
    title: "The z≈4–6 massive-galaxy abundance is consistent with IllustrisTNG once stellar-mass systematics are budgeted",
    sub: "The z>4 “too massive, too early” excess over ΛCDM re-examined: at z≈5–6 the ~2.7× excess in n(>10¹⁰·⁵ M⊙) is erased by a 0.28 dex stellar-mass shift — inside the ~1 dex systematic budget. No robust tension; the harder residual is spectroscopic quiescent galaxies at z>6.",
    pages: "6 pp",
    pdf: "/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf",
    updated: "2026-07-21 12:51",
    verdict: "REVIEW-READY",
    review: "/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics_review_loop.md",
    methods: ["smf", "simobs"],
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
  },
  {
    title: "Calibration is not validation: confronting IllustrisTNG with observed scaling-relation evolution",
    sub: "Testing the simulation by its predictions away from its z≈0 calibration point, from SDSS to JWST.",
    pages: "3 pp",
    pdf: "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf",
    updated: "2026-07-19 23:10",
    methods: ["simobs", "ms", "mzr"],
  },
];

export default function FrontierDrafts() {
  return (
    <div className="pb">
      <style>{PB_CSS}</style>
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
            <div className="pb-run-links"><a href={f.pdf} target="_blank" rel="noopener noreferrer">read the draft (PDF) ↗</a></div>
            <p className="pb-tag">descriptive draft — not validated, not published</p>
          </div>
        ))}
      </div>
      <p className="pb-flag-note">{FRONTIER.length} frontier drafts. The hand-guided study lives under <b>Flagship studies</b>; the fully-automated runs under <b>Pipeline runs</b>.</p>
    </div>
  );
}
