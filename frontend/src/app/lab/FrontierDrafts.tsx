"use client";

// Frontier-study drafts from the autonomous research pipeline — multi-page AASTeX
// manuscripts, one per top frontier. More developed than the single-measurement
// pipeline runs, but still descriptive drafts (no human sign-off). Hosted under
// /agent-reports/research-frontiers/. Curated list.
import { PB_CSS } from "./PipelineBoard";

type Draft = { title: string; sub: string; pages: string; pdf: string };

const FRONTIER: Draft[] = [
  {
    title: "Galaxy scaling relations from z≈0 to the JWST frontier",
    sub: "The star-forming main sequence and the mass–metallicity relation anchored on ~5×10⁵ SDSS galaxies, then confronted with JWST out to the frontier.",
    pages: "3 pp",
    pdf: "/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf",
  },
  {
    title: "Does IllustrisTNG make enough massive galaxies early enough?",
    sub: "A stellar-mass-function stress test of the flagship simulation against JWST at z=4–6 — the ‘too massive, too early’ tension with ΛCDM.",
    pages: "6 pp",
    pdf: "/agent-reports/research-frontiers/galaxy-evolution-massive-galaxies-draft.pdf",
  },
  {
    title: "The stellar mass–metallicity relation in SDSS and the aperture sensitivity of the FMR",
    sub: "The MZR from 202,968 SDSS star-forming galaxies, and whether the fundamental metallicity relation is physical or an aperture artifact.",
    pages: "3 pp",
    pdf: "/agent-reports/research-frontiers/galaxy-evolution-mzr-fmr-draft.pdf",
  },
  {
    title: "Calibration is not validation: confronting IllustrisTNG with observed scaling-relation evolution",
    sub: "Testing the simulation by its predictions away from its z≈0 calibration point, from SDSS to JWST.",
    pages: "3 pp",
    pdf: "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf",
  },
];

export default function FrontierDrafts() {
  return (
    <div className="pb">
      <style>{PB_CSS}</style>
      <p className="pb-lede">
        Multi-page manuscript drafts from the <b>autonomous research pipeline</b>, one per top frontier —
        more developed than the single-measurement runs, but <b>descriptive drafts</b>: no human has cleared any of them,
        and they carry no logged referee verdict here.
      </p>
      <div className="pb-runs">
        {FRONTIER.map((f) => (
          <div className="pb-run" key={f.pdf}>
            <div className="pb-run-top">
              <span className="pb-run-title">{f.title}</span>
              <span className="pb-chip" style={{ borderColor: "#e0a458", color: "#e0a458" }}>draft</span>
            </div>
            <p className="pb-run-summary">{f.sub}</p>
            <div className="pb-run-chips"><span className="pb-src">AASTeX · {f.pages}</span></div>
            <div className="pb-run-links"><a href={f.pdf} target="_blank" rel="noopener noreferrer">read the draft (PDF) ↗</a></div>
            <p className="pb-tag">descriptive draft — not validated, not published</p>
          </div>
        ))}
      </div>
      <p className="pb-flag-note">{FRONTIER.length} frontier drafts. The hand-guided study lives under <b>Flagship studies</b>; the fully-automated runs under <b>Pipeline runs</b>.</p>
    </div>
  );
}
