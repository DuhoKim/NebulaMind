# TORI BRIEF — Step 3 V2 re-check (fidelity + zones only)

Lane: `c41-baseline-restart-20260803T1253Z`. You are Tori. Goru repaired the span table per your
FAIL (`GORU_STEP3_REPAIR_BRIEF.md`, repair section in `GORU_STEP3_REPORT.md`; table is now
`C41_STEP3_V2`; the failed v1 is preserved in `_tmp_goru_v1_backup/`).

Re-check ONLY the two failed dimensions on the SAME sample (18 records, seed 41 — reuse your
existing machinery and `_tmp_tori3_*` artifacts):

1. **Fidelity**: same 3-per-record seeded spans (re-drawn from V2 rows, seed 41) — every quote
   must be a VERBATIM substring of the cached source text; `truncated: true` rows must still be
   verbatim substrings (no inserted characters). Any non-substring → FAIL.
2. **Zones**: re-check the labels for your sampled spans; the v1 defect class (finding on
   methods/captions/references) must be gone. Isolated defensible-judgment differences are notes,
   systematic mislabeling is FAIL.
3. Recall is NOT re-checked (your 94.19% verdict stands unless V2's span coverage for your 18
   records shrank materially — do a quick count comparison v1 vs v2 for the sample and flag if
   any record lost >20% of its spans).

Deliverable: `TORI_STEP3_RECHECK.md` — verdict **PASS / PASS_WITH_NOTES / FAIL**, the numbers,
brief deltas vs v1. End with marker: `TORI_STEP3_RECHECK_COMPLETE_20260804`.
Constraints unchanged: lane-only writes, read-only elsewhere, no network.
