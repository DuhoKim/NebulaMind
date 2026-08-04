# GORU BRIEF — Step 4 V2: repair the starved ledger (4 entries is a stub, not coverage)

Read your own V1 receipt: 4 entries from 180 papers / 16,103 spans, all from `finding`-zone spans.
Root cause (coordinator's diagnosis, not your fault): V3 zones deliberately collapsed most classes
to `unknown`, so zone-gated eligibility starves. The AGN pilot: 16 entries from 26 papers — C41
should land in the honest DOZENS.

## Design change

1. Entry eligibility is CONTENT-based, zone-agnostic: rank spans by (strict-tension triggers,
   contested-quantity dispersion hits, numeric/comparative density), regardless of zone; zone is
   recorded metadata, never a filter. `caption`/`references` zones stay excluded.
2. Coverage floor: process the Step-1 priority cohort first — every p4 paper (58) and p3 paper
   (10) must yield either ≥1 ledger entry or an explicit per-paper no-entry reason in the report.
   Then p2 as budget allows.
3. Modality/certainty discipline unchanged (that part of V1 was right): assertion never stronger
   than its spans, enums exact, `verification_status: pending`, links only where evident.
4. Back up V1 (`_tmp_goru_step4_v1_backup/`), rebuild as `C41_LEDGER.jsonl` v2, re-validate
   (validator unchanged), regenerate the receipt, append `## Repair round (V2)` to your report
   with the entry count, axis/certainty histograms, and the p4/p3 no-entry reason list. Marker:
   `GORU_STEP4_V2_COMPLETE_20260804`.
Same constraints as V1.
