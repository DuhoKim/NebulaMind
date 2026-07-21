"use client";

// Flagship, human-guided studies (hosted under /studies/) — the curated papers
// that went the full distance: real forward-model + referee loop, orchestrated by
// the crew, not the automated pipeline. Still descriptive until a human clears them.
// Curated list; add an entry per published study.
import { PB_CSS } from "./PipelineBoard";

export type Flagship = { title: string; summary: string; meta: string; verdict: string; pdf: string; updated: string };

export const FLAGSHIP: Flagship[] = [
  {
    title: "An Independent, Unlensed Gas-Phase Metallicity Deficit at z≈9–10",
    summary: "On a single Te-consistent scale, the strictly unlensed z=9.3–9.9 field sample (Pollock+26, N=5 direct-Te) sits −0.69±0.03 dex below the local mass–metallicity relation — robust to leave-one-out (0.04 dex) and to the local anchor choice (Curti+20 vs Andrews–Martini, Δ0.04 dex). Explicitly NOT a formal statistical detection.",
    meta: "Nakajima+23 direct-Te subset · Pollock+26 unlensed CAPERS/JADES · cross-checked vs Isobe+26 (~1500 gal) · abs. Te scale ±0.1–0.2 dex is the dominant systematic",
    verdict: "REVIEW-READY",
    pdf: "/studies/z9-10-unlensed-metallicity-deficit.pdf",
    updated: "2026-07-21 13:40",
  },
];

const vcolor = (v: string) => ({ ACCEPT: "#4ad6c4", MINOR: "#e0a458", MAJOR: "#e0774f", REJECT: "#f47272" }[v.toUpperCase()] ?? "#9aa3b8");

export default function FlagshipStudies() {
  return (
    <div className="pb">
      <style>{PB_CSS}</style>
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
            <div className="pb-run-links"><a href={f.pdf} target="_blank" rel="noopener noreferrer">read the manuscript (PDF) ↗</a></div>
            <p className="pb-tag">descriptive — not validated, not published</p>
          </div>
        ))}
      </div>
      <p className="pb-flag-note">{FLAGSHIP.length} published so far. The fully-automated runs — the fast, high-attrition track — live under <b>Pipeline runs</b>.</p>
    </div>
  );
}
