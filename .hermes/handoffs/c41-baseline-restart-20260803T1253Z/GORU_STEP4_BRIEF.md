# GORU BRIEF — C41 Step 4: claim/status ledger build (campaign lane L-A)

Lane: `c41-baseline-restart-20260803T1253Z`. You are Goru. Campaign gate (Duho, 2026-08-03 23:31
KST): "APPROVE PAPERS OVERNIGHT — …" constitutes `APPROVE C41 STEP 4`. Precondition: Tori's V2
re-check verdict is PASS (Hwao confirms at dispatch; the span table you build from is
`C41_STEP3_V2`).

## Goal

Distill the V2 span table (16,177 candidates / 180 records) into the **C41 claim/status ledger**
per contract v1. Quality over count: target is HONEST COVERAGE of the frozen question's three axes
— the most contested, best-evidenced material first — not a big number. The AGN pilot yielded 16
entries from 26 papers; C41 at 180 papers should land somewhere in the dozens-to-low-hundreds.
A partial ledger with a stated shortfall beats a padded one (shrink-before-quality).

## Schema ground truth (read-only)

- `docs/claim_ledger_contract_v1_agn_20260703T0830Z/CLAIM_LEDGER_CONTRACT_V1.md` + 
  `artifacts/ledger_enums.json` (ALL vocabularies: certainty_level, modality, zones, link types,
  status fields) + `artifacts/claim_status_ledger.jsonl` (16 worked examples — match their field
  structure exactly).
- Entry IDs: `c41_NNN` (zero-padded, deterministic order of creation).
- `verification_status`: **`pending` on every entry** — Step 5 (Kun) flips it; you never do.

## Method (hybrid: mechanical grouping + batch composition + validation)

1. `step4_group.py` (lane dir): deterministic pre-grouping of V2 spans — per record, rank spans
   (finding/interpretation zones first, strict-tension triggers first, then axis density), take
   the top ≤12 per record; group across records by (axis, trigger-term families) into candidate
   claim clusters. Emit `_tmp_goru_step4_groups.jsonl`.
2. Compose ledger entries batch-by-batch from the groups: each entry = assertion (in the source's
   modality, NEVER stronger than its spans), axis, entry-level certainty per the enum definitions,
   bound `span_id`s (≥1, must exist in V2 table), source identities, links (`same_axis` /
   `qualifies` / `contradicts` / `specializes` / `generalizes`) where the span evidence makes them
   evident — do not force links.
3. `step4_validate.py`: machine checks — enum membership for every field, span references resolve
   into the V2 table, no duplicate assertions, every axis has entries, link targets exist, JSONL
   parses. The build is not done until validation passes clean.

## Deliverables (lane dir)

`C41_LEDGER.jsonl` · `step4_group.py` · `step4_validate.py` · `STEP4_VALIDATION_RECEIPT.json`
(counts per axis/certainty/zone-source, validator PASS output, input-manifest sha block pinning
the V2 table + Step-2 manifest) · `GORU_STEP4_REPORT.md` (method notes, coverage honesty — which
contested areas did NOT make it in and why, runtime) ending with marker:
`GORU_STEP4_COMPLETE_20260804`.

Constraints: lane-only writes; no network; no git/DB; do not read the AGN prose lane, the f_esc
dirs, or Tori's independent files. Lana runs a no-overclaim pass after you; Kun stance-verifies
after her — write for reviewers who want to catch you overclaiming.
