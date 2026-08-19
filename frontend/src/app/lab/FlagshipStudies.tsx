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

export type { Flagship } from "./flagshipData";
import type { Flagship } from "./flagshipData";

// Studies a HUMAN read and rejected. They stay published — the rejection and its reason are
// part of the record, not something to hide. `why` is Duho's stated reason, verbatim in
// substance; `retired` is when he pulled it.
export type Rejected = Flagship & { why: string; retired: string; kept?: string };

// PERSONAL-INTEREST TRACKS — research Duho asked for by name, carried openly as his interest
// rather than dressed up as a corpus-derived frontier (frontier rows carry real cluster paper
// counts; a hand-made one would be invented data). Every number below is measured: arXiv totals
// from a live query on 2026-08-05, archive counts from VizieR TAP_SCHEMA the same day.
export type InterestTrack = {
  title: string; interestOf: string; opened: string; lane: string; currentProbe?: string;
  motivation: string; literature: string; dataFound: string; state: string; priority?: boolean;
};

export const INTEREST_TRACKS: InterestTrack[] = [
  {
    title: "Black-hole-universe cosmology",
    interestOf: "Duho",
    opened: "2026-08-05",
    lane: "spin-parity-census-20260805T1922K",
    currentProbe: "First probe: a galaxy spin-parity test \u2014 chosen because, of the signatures this cosmology predicts, spiral handedness is the one with data reachable in public archives today. It is one probe, not the topic: the CMB hemispherical-asymmetry route and the Einstein\u2013Cartan torsion-bounce line (the larger literature at 516 papers) remain open under this track.",
    priority: true, // Duho, 2026-08-05: "place that as top priority"
    motivation:
      "The hypothesis that our observable universe is the interior of a black hole in a parent universe. If that interior rotates, it inherits a preferred axis \u2014 so the observable signatures are parity and anisotropy ones: a handedness excess among spiral galaxies, a hemispherical asymmetry in the CMB, or the torsion-bounce phenomenology of Einstein\u2013Cartan cosmology.",
    literature:
      "arXiv, measured 2026-08-05: 37 papers on black-hole cosmology / universe-inside-a-black-hole; 516 on the Einstein\u2013Cartan torsion-bounce line, 88 of the last 100 from 2024 onward; 66 on galaxy spin-direction asymmetry; 40 on CMB hemispherical asymmetry.",
    dataFound:
      "VizieR carries no per-object spiral-handedness catalogue. Of 81 catalogues whose descriptions say \u201cclockwise\u201d, nearly all use it as a position-angle convention; 40 name matches are central wavelengths, CatWISE proper motions and neutron-monitor dips; the 4 survivors are two galaxy-CLUSTER rotation tables (42 rows, wrong quantity), one Galaxy Zoo vote fraction that sums handedness away, and one spiral yes/no deposit. The vote fractions do exist outside VizieR \u2014 Galaxy Zoo 1\u2019s own release carries P_CW and P_ACW per object with sky positions.",
    state:
      "The measurement has run under the frozen contract, and it stopped itself. Mirroring the images moves the asymmetry to the other side of zero, clearing the pre-registered three-sigma bar by more than twice; of the objects clearly classified in both conditions, every one changed label \u2014 a pre-registered MIXED reading. What the flip means is undetermined: it depends on a convention neither primary source states (whether archived directions were recorded as the classifier saw them, or corrected back to the sky first), and on data of the same provenance the source study reports no reversal where this lane finds one. This is a classifier mirror-bias reading on the bias-study sample \u2014 not a cosmological asymmetry, not a dipole, not a parity result \u2014 and the contract forbids any result from being phrased as support for the cosmology that motivated it. One correction of record, kept visible: the contract named the Galaxy Zoo mirror bias backwards. Land et al. (2008) report the excess as S-wise \u2014 anticlockwise over-reported, not clockwise \u2014 confirmed against the paper and three further primary sources.",
  },
];

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

export { FLAGSHIP } from "./flagshipData";
import { FLAGSHIP } from "./flagshipData";

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
