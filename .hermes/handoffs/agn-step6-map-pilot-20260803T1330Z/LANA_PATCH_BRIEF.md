# LANA PATCH BRIEF — apply Kun's red-team patches to your AGN Step-6 map

Lane: `agn-step6-map-pilot-20260803T1330Z`. You are Lana; these are YOUR artifacts — patch them.
Kun's full review: `KUN_MAP_REDTEAM.md` (verdict PASS_WITH_PATCHES). Apply exactly his five
requested patches plus the two nits, log each in `PATCH_LOG.md`:

1. Fix R5's trace citations for `clc_agn_009`/`clc_agn_010` (drop the phantom `same_axis→seed`
   leg; placements rest on the `qualifies` leg) and restate `clc_agn_008`'s placement provenance
   as ledger-only (`qualifies→2299_003`; the stance-matrix row is corroboration, not basis).
2. Reword the condensation header: determinism holds for R1/R2/R3/R5/R6; **R4's distinct-question
   test is argued per-case and reviewable** — say so plainly.
3. Move the `verification_status = pending` disclosure into the MAP's header block (keep the
   footnote too).
4. Finding 5(b): re-read the full span quotes for 002b spans `_02`/`_03` in the ledger. If
   "≥100 km/s" appears verbatim, footnote the span; if not, STRIKE the threshold and keep only the
   ledger-carried wording.
5. Finding 4 nit: Axis A's summary-table Status cell → "per-side (see axis)".
6. Finding 6 nit: reword R1's text so only 011 is described as seeding Axis E (004 joins by R6).

Constraints unchanged: ledger is read-only ground truth; no content beyond it; write only in this
lane dir. Update `CONDENSATION_REPORT.md` + `AGN_STATUS_DEBATE_MAP_V1.md` in place, add
`PATCH_LOG.md` (patch → files touched → one-line diff summary). End the log with marker:
`LANA_AGN_STEP6_PATCHED_20260803`.
