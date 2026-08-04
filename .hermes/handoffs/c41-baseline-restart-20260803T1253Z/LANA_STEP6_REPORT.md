# LANA STEP-6 REPORT — C41 status/debate map v1 + condensation report

Lane: `c41-baseline-restart-20260803T1253Z` · Lana (Claude, no-overclaim lane) · 2026-08-04
14:10–14:26 KST. Role: AUTHOR only — Hwao synthesis-reviews, Kun red-teams, Tori receipts; I
certify nothing I write.

## Deliverables (lane-only writes)

- `C41_STATUS_DEBATE_MAP_V1.md` — sha256 `79a3ebe944361b7ce8a61bd6f691bf453238187f45bd8b5f5abe589a5b3d9e21`
- `C41_CONDENSATION_REPORT.md` — sha256 `7cf8fd1d47a642da8adbb8300587bee5373c83a7e529d44bc7ef7d0b16cedc3e`
- This report. Lane temps: `_tmp_lana_step6_extract.py`, `_tmp_lana_step6_graph.py`,
  `_tmp_lana_step6_check.py`, `_tmp_lana_step6_view.md` (all in lane dir per scoped-lane rules).

**Headline: K = 7 named axes** from 80 stance-verified entries — A1 bright-end pace
(`actively_debated`, the flagship dispute), A2 efficiency physics, A3 calibration validity (22
entries, clearest cross-paper contradiction cluster), A4 FMR/MZR survival, A5 early enrichment
(one-sided-plus-open), A6 reionization budget (no direct f_esc measurement at the epoch exists
in-corpus — said plainly), A7 AGN boundary (one-sided by frozen-question scope rule). Four axes
contain live cross-paper conflicts with stance-verified entries on both sides; the map's
"disputed" verdicts bind to exactly those, per the interpretation contract.

## AGN-pilot red-team lessons imported (all five patches, by design not repair)

1. **Patch #5 (machine-checkable traces):** every trace-table row is a field predicate or a
   verbatim assertion-substring; a checker re-executes all 84 rows without semantic reads.
   Executed pre-ship: **0 failures** (`_tmp_lana_step6_check.py`).
2. **Patch #2 (determinism scoped honestly):** deterministic rules R0–R4 vs judgment layer J1–J7
   split explicitly; the C41 link graph is degenerate (149/149 tag-derived `same_axis`, identical
   description string), so the whole sub-axis partition is declared judgment — the honest
   opposite of overclaiming pilot-style topology derivation. R3 (marker anchoring) bounds K from
   below mechanically.
3. **Patch #3 (verification state up top):** the map's header leads with the Step-5 census (76
   `verified_consistent` + 4 `verified_no_claim`, zero failures), the 4 placeholders, the 8
   binding-note nits, and the on-disk defect below.
4. **Pilot F1-class silent-swallow:** structurally excluded — checker fails on any unplaced claim
   entry; coverage 76/76 + 4 placeholders, one declared dual (c41_065).
5. **Pilot F4 (per-side status cells):** only A1 carries a mixed-enum membership; its summary
   cell says so explicitly.

## Incident: ledger mutated mid-Step-6 (disclosed, not fixed)

Timeline (all `date`-stamped during the run): my extraction at ~14:10 KST read
`verification_status` = 76 `verified_consistent` + 4 `verified_no_claim` on disk;
`step4_v8_applier.py` ran at 14:11 KST; my checker at ~14:16 found all 80 entries reading
`"validated"` — an off-enum value; the applier's code hardcodes it and ignores the patch's
per-row `new` values, collapsing Kun's census. Byte-diff vs `_tmp_goru_v7_backup/C41_LEDGER.jsonl`
confirms v8 touched only `verification_status`, `verification_note`, `binding_note`, and the
c41_004/c41_005 span zone/stance (→ `unknown`/`qualifies`, diverging from the stance matrix's
`supports`). All condensation-relevant fields are byte-identical, so the map is unaffected in
content; both deliverables disclose the defect prominently and bind the verification census to
Kun's pinned artifacts instead of the ledger field. **Action for the applier lane (Goru/Hwao):
re-land `VERIFICATION_STATUS_PATCH.jsonl` honoring `new` per row; receipt the 004/005 stance
override or reconcile with the matrix.** I did not edit the ledger (report-don't-fix; composer
never lands patches). Map compiled against post-v8 sha `e2938298…`; if the ledger moves again,
the sha discloses it.

## Requirements check against the brief

- Condensation report: 80 entries + 149 links + the 146-hit signal → K=7, K an output; merge
  rules stated as rules; trace machine-checkable; judgment named and argued per-case. ✓
- Header discloses verification state, 4 placeholders, 8 nits (c41_007/016/019/024/031/042/053/079). ✓
- Per axis: sides with entry IDs; best evidence with source-strength; ledger-carried dispersions
  (engine dispersion_v2 context only in labeled brackets); v1.1-enum statuses, per-side where
  mixed (A1); countercase quota translated honestly — no `widely_supported` exists in this
  ledger, so the quota becomes "every side names its in-corpus opposition, and one-sided axes
  declare the missing counterparty" (A5, A6-few-side, A7). "What would settle it" per axis,
  concrete and honest about existence (A6: the direct settling measurement does not exist
  in-corpus). ✓
- Modality law: every side statement written at its carrier entry's modality tier; the
  sim-vs-obs section carries an explicit modality note. No content beyond ledger + stance matrix
  (+ labeled engine context + frozen question). ✓
- Information firewall: the f_esc paper lane and sweep dirs were not read; inputs were ledger,
  stance matrix, patch, frozen question + receipt, plan roadmap, AGN pilot artifacts, dispersion
  engine file. The map picks the study; it does not know what studies exist. ✓

## Uncertainties / flags for Hwao and Kun

- Sub-axis membership is judgment throughout (link graph carries no structure); weakest
  placements, flagged in-map: c41_019 (gas-supply case in A5), c41_034 (local anchor in A3 vs
  A4), c41_048 (anchor in A4). K could defensibly be 6 or 8 under a different judgment layer;
  the R3 floor is 5.
- A1's axis-level `actively_debated` rests on c41_004 alone being enum-carried; all other members
  are ESL. Stated in the map; reviewable.
- The 004/005 span-stance `qualifies` (v8) vs stance-matrix `supports` divergence is unresolved
  upstream; the map used the conservative reading.
- Engine dispersion context (dispersion_v2.json, corpus-wide) is quarantined in labeled brackets;
  if Kun prefers zero external context in v1, those brackets excise cleanly.

LANA_C41_STEP6_COMPLETE_20260804
