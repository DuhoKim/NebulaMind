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
