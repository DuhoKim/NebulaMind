# LANA BRIEF — C41 Step 6: the status/debate map (Duho gate: "APPROVE C41 STEP 6")

Lane: `c41-baseline-restart-20260803T1253Z`. You are Lana, AUTHOR (Hwao synthesis-reviews before
Kun red-teams; Tori receipts; you certify nothing you write). This is the flagship deliverable the
Baseline board has awaited since 2026-07-03 — and your AGN pilot map was the dress rehearsal.
Import every lesson from its red-team (`agn-step6-map-pilot-20260803T1330Z/KUN_MAP_REDTEAM.md`).

## Inputs (read-only)

- `C41_LEDGER.jsonl` — 80 entries, **all stance-verified** (76 `verified_consistent` + 4
  `verified_no_claim`), 149 links, Kun's stance matrix `C41_STANCE_MATRIX.jsonl` beside it.
- The frozen question (`STEP0_FROZEN_QUESTION.md`, sha 9ac5ca1f…) — the map ANSWERS this.
- Roadmap Step-6 definition; the AGN pilot map (patched) as the format precedent.
- Dispersion context: engine `dispersion_v2.json` for the contested quantities.

## Requirements (pilot lessons are binding)

1. **Condensation report**: 80 entries + 149 links + the 146-lexicon-hit signal → K named debate
   axes. K is an OUTPUT. Merge rules stated as rules; **trace-table citations machine-checkable**
   (entry_id, rule, link type, target — Kun's pilot patch #5: a checker must be able to re-execute
   without semantic reads). Deterministic rules scoped honestly; judgment calls named as such,
   argued per-case (pilot patch #2).
2. **Header discloses verification state** (pilot patch #3 inverted into a strength): every status
   label binds to stance-VERIFIED entries — say so up top, plus the 4 no-claim placeholders and
   the 8 binding-note nits.
3. Per axis: sides with entry IDs; best evidence with source-strength; measurement dispersions
   where the ledger carries numbers; current status in v1.1 enums (per-side where sides differ —
   pilot patch on Axis A); countercases represented (the quota survives translation); **"what
   would settle it"** — concrete, falsifiable, honest about whether the settling measurement
   exists yet. The three frozen axes (formation efficiency / chemical enrichment / ionizing
   output) are super-structure, not a limit on K.
4. Modality law unchanged: map statements never exceed ledger certainty. No content beyond
   ledger + stance matrix.

## Deliverables (lane dir)

`C41_STATUS_DEBATE_MAP_V1.md` · `C41_CONDENSATION_REPORT.md` · `LANA_STEP6_REPORT.md` ending with
marker `LANA_C41_STEP6_COMPLETE_20260804`. Lane-only writes; no network; do not read the f_esc
paper lane or the sweep dirs (the map must not know what studies exist — it PICKS the study).
