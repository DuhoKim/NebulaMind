# Lana brief — C1r v2 design review

Read first:
- `HWAO_IMPLEMENTATION_DIRECTION.md`
- `ROLE_TABLE.md`
- immutable contract `../gemini-dr-revised-canary-20260712T045317Z/prompt/C1r.md`
- immutable capture/validator source and tests in that sealed packet
- corrected root-cause reports in `../dr-c1r-root-cause-20260712T163156Z/`

Role: high-reasoning design reviewer only. Do not implement code.

Allowed writes only:
- `design/LANA_ACK`
- `design/LANA_DESIGN_REVIEW.md`
- `design/LANA_SIGNOFF`

First write ACK containing exactly `LANA_C1R_REPAIR_ACK_20260713T010203Z`.

Review and specify testable behavior for:
1. per-logical-unit native citation extraction and fail-closed index→URL mapping;
2. literal same-cell citation semantics under C1r.md:86-92;
3. typed claim-bearing cells for C4;
4. per-cell C6 comparison detection and numerical fraction/incidence gating;
5. exact sentinels and GAP unit splitting;
6. C7 bidirectionality, duplicates, blank names, normalization, near-duplicates;
7. manual-review boundary and expected T14 residue.

Write concrete schemas/field names and stop conditions that Tori can implement without guessing. End the review with exactly:
`LANA_C1R_REPAIR_DESIGN_DONE_20260713T010203Z`

Write `design/LANA_SIGNOFF` only if the proposed T0–T15 contract is internally consistent; it must contain exactly:
`LANA_C1R_REPAIR_SIGNOFF_20260713T010203Z`

Hard scope: local/offline; packet-only writes; sealed inputs immutable; no browser/network/live Gemini/DB/wiki/product/deploy/restart/git/cron/dashboard/public-cockpit action.
