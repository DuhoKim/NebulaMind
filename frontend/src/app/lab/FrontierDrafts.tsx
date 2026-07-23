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
    sub: "Across a 232-point grid, the LyC escape fraction needed to close reionization is set by ξ_ion and the SFRD, not the data — both the “crisis” and “galaxies suffice” camps fall out of the same envelope.",
    pages: "synthesis",
    pdf: "/agent-reports/research-frontiers/reionization-fesc-budget-landscape.pdf",
    updated: "2026-07-23 03:00",
    verdict: "REVIEW-READY",
    review: "/agent-reports/research-frontiers/reionization-fesc-budget-landscape_review_loop.md",
    frontier: 16,
  },
  {
    title: "Galaxy scaling relations from z≈0 to the JWST frontier",
    sub: "Main claim withdrawn: the apparent z<6 main-sequence elevation is largely an emission-line selection artifact. Folded into #6 / #1 — not a standalone result.",
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
    sub: "On a matched total-mass basis the JWST massive-galaxy excess needs only a 0.20 dex shift and already sits at the fiducial ΛCDM efficiency — a test of TNG’s calibration, not new physics.",
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
    sub: "A practitioner’s framework separating calibration-scale offsets from aperture bias in gas-phase MZR comparisons — single-scale reporting, covering-fraction floors, IFS ground truth.",
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
    sub: "TNG over-evolves the star-forming main sequence — a discrepancy that de-biasing the emission-line selection only widens (a conservative lower bound), and that is robust to the +0.13 dex mass-basis fix.",
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
