# P4 conditional-start packet

Marker: `TORI_FABLE_BURN_P4_CONDITION_MET_20260711T021637Z`
Plan: `HWAO_FABLE_WEEKLY_BURN_PLAN_20260711T010503Z.md`
Approval: `approve fable burn 20260711T010503Z`

## Core packet completion

- P1 done marker exists: `p1-rp1-invariants/FABLE_BURN_P1_DONE_20260711T010503Z`
- P2 done marker exists: `p2-cycle7-source-ledger/FABLE_BURN_P2_DONE_20260711T010503Z`
- P3 done marker exists: `p3-m3-rt-baseline/FABLE_BURN_P3_DONE_20260711T010503Z`
- All three receipts report `status: COMPLETE` and end with their required done markers.

## Condition check

- Check time: `2026-07-11T02:16:37Z`.
- Fable weekly last-visible meter: `9% used`, reset shown in about 2 hours.
- Fable 5-hour last-visible meter: `27% used`.
- Clock is before the plan's `03:15Z` P4 latest-start condition.
- Weekly use is below the plan's `60%` P4 threshold.
- No `GLOBAL_STOP_20260711T010503Z.md` or `HOLD_5H_20260711T010503Z.md` is present.
- Runner PID 45665 is healthy, cycle 8, waiting; runner/candidates remain read-only and untouched by burn lanes.

## Hwao action requested

Review the P1/P2/P3 receipts and this condition packet. If the approved P4 condition is satisfied, write one exact self-contained brief under `briefs/P4_BRIEF_DERIVED_CLAIMS_20260711T010503Z.md` for a single fresh Fable lane with a 30-minute hard cap. Confine all writes to `p4-derived-claims/`; source material is the clean cycle-5 package and P1 manifest/reference only; produce `CLAIM_EVIDENCE_CANDIDATES.md`, `P4_RECEIPT.md`, and the exact empty marker `FABLE_BURN_P4_DONE_20260711T010503Z`. Preserve all existing safety gates: no runner/candidate writes, no network/browser, no DB/API/wiki publish, no deploy/restart, no git, no cron/launchd, no billing/account/credentials, no cloud/GCP. Do not perform P4 substance or dispatch the lane. If the condition does not pass, write `P4_DROPPED.md` instead.
