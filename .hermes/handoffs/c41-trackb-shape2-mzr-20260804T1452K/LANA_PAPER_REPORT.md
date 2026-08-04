# LANA PAPER REPORT — the anchor-gap paper drafted

Lane: `c41-trackb-shape2-mzr-20260804T1452K` · Author: Lana
Drafted: 2026-08-04 18:33–18:44 KST (stamped via `date`)
Brief: `LANA_PAPER_BRIEF.md` (Duho: "okay draft the anchor-gap paper")

## Deliverables (all written, lane-only)

| File | What it is |
|---|---|
| `ANCHOR_GAP_PAPER.tex` | The paper: "The Public-Archive Direct-Te Anchor Gap at z>3: A Contract-Grade Census". AASTeX 6.3.1, twocolumn; abstract, contract, method, results (anchor table + exclusion-taxonomy table + null), discussion, mandatory Uncertainties section, summary. Every number sourced. |
| `ANCHOR_GAP_FIGURE.png` / `.pdf` | Two-panel paper figure: (a) the 5 anchors vs the AM13 frame with the below-bin-floor region marked; (b) forecast v1 (25) / v2 (87) / actual (2/1/0, +2 below floor) per bin with the 3-anchor minimum line. |
| `make_paper_figure.py` | Figure generator; reads ONLY `T3_REAL_SAMPLE.jsonl` + `T3_REAL_RESULTS.json`, asserts the 5-anchor count and the frozen AM13 form string before drawing. Colorblind-validated palette; forecasts hatched; all bars direct-labeled. |
| `PAPER_CHANGELOG.md` | The number-by-number source → section map (the audit trail for every value in the .tex). |

## What the paper says (and refuses to say)

- **The number**: 5 contract-grade public direct-Te anchors at z>3 (3 ERO + 2 GLASS,
  z=4.015–8.496), each reproduced to the printed digit in Kun's T4-real forensics; bins
  2/1/0 with 2 verified anchors below the frozen logM=8 bin edge (Kun C1 accounting closes
  3+2=5).
- **The gap**: frozen forecast v1 conservatively expected ~25 (v2, licensed pre-fetch
  re-freeze, expected 87; its 0.12-dex precision claim disclosed as Kun-flagged
  unachievable). Realized public yield: short of even v1 by roughly an order of magnitude.
- **The null**: quoted verbatim from `T3_REAL_RESULTS.json`'s §6-template instantiation with
  the v1→v2 supersession disclosure (Kun C2 honored). No bin reaches the 3-anchor minimum
  → no deficit verdict of any size or direction; A3's resolution currently rests on data
  not publicly quotable at uniform rigor.
- **The census substance**: full 90-row exclusion taxonomy from the archived sample file —
  64 S/N-floor kills (14 zero-flux; 5 near-misses at S/N 4.76–4.84 incl. the ERO_06355 4.8
  case), 12 no-Hβ (killing every z>9 survivor), 6 missing-flux, 8 Te-failures; JADES
  contributes 85/95 candidate rows and zero anchors — joins, not photons, are the binding
  constraint.
- **Modality law enforced**: census + null only. Fig. 1a's caption explicitly de-licenses
  the visual offsets; Kun's per-object offsets stay provenance-only; the anchor-frame
  0.14-dex discrepancy note is carried VERBATIM in §5.2 and flagged again in Uncertainties.
- **F2 differentiation** (§5.3): what z9-10 established (sign; −0.69±0.03 stat; ±0.16 dex
  systematic-limited, NOT a detection) vs what this census adds (survey-wide public-archive
  scope, uniform contract floor, the N=5 quotability measurement); both studies' honest
  shared absence stated — FMR untouched there, not-computable here. Bonus census fact: the
  two anchor sets don't overlap (no z≳9 candidate survived the public joins).
- **Discussion** names the closing acts: flux tables WITH errors + linked masses + archived
  Hβ; the S/N-4.8 near-miss class as the cheapest growth path; per-object μ publication
  (Ruling-2 re-entry path); the 12 unreachable tables as unreachable-not-absent.

## Honest notes for T4/panel

1. **Recount nit**: Kun's forensics prose says 58 S/N-floor exclusions; direct recount of
   `T3_REAL_SAMPLE.jsonl` gives 64 (only 64 closes the 95-row total). Paper uses the
   archived file; flagged in `PAPER_CHANGELOG.md`. All of Kun's other counts reproduce.
2. **Compile status**: `.tex` is syntactically complete AASTeX 6.3.1, but compilation was
   NOT run — the lane bars network and non-lane writes, and the local `tectonic` would
   fetch the AASTeX bundle + write caches outside the lane. First compile should happen
   outside lane constraints.
3. **New uncertainty surfaced while drafting** (in §6 of the paper): per-object MC O/H
   uncertainties are specified in `APRIME_PIPELINE_FROZEN.md` (seed 42, 1000 draws) but not
   tabulated in the v1 outputs; immaterial now (nothing was compared), mandatory before any
   populated-bin analysis. Also disclosed: PyNeb 1.1.18-in-freeze-doc vs 1.1.32-at-runtime
   seam, and the missing per-object μ metadata for the five ERO/GLASS anchors (z9-10
   lens-contamination precedent).
4. Enumeration channel scope (λ4363-only; 1666/5755-class A′-eligible anchors not
   enumerated in v1) stated as a conservative-direction scope limit.

No DB writes, no network, no files outside the lane. Paper history untouched (no human
interaction occurred during drafting; the log stays human-only per standing rule).

LANA_ANCHORGAP_PAPER_COMPLETE_20260804
