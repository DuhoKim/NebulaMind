# GORU BRIEF — Step 4 V3: Lana's FAIL_WITH_CORRECTIONS (read LANA_STEP4_PASS.md in full first)

Her rulings are binding for this round:
1. **Zone recast = metadata falsification — REVERT.** Every ledger span returns to its V3
   ground-truth zone (`unknown` for all 80). Since the contract enum lacks `unknown`, apply her
   disposition 2 (the within-gates path): **per-span zone adjudication with receipts** — for each
   span whose entry claims a `supports` stance, adjudicate the zone from the quote + surrounding
   context (the Tori-recheck pattern), one receipt line per span (`span_id → adjudicated zone →
   one-line justification`) in `STEP4_ZONE_ADJUDICATION.jsonl`. A span you cannot honestly place
   stays `unknown` and its stance falls back per contract rule 7 (qualifies/mixed/no_info — NOT
   supports). No blanket casts of any kind.
2. **Certainty rebuilt per enum DEFINITIONS.** `widely_supported` only with genuine cross-source
   corroboration; expect `actively_debated`/`emerging_sample_limited` to dominate this cluster.
   Apply every per-entry correction in her findings table.
3. **Countercases**: her pass found critics/countercases in ZERO entries — the contract's
   countercase representation is mandatory. Mine the V3 table's strict-tension spans for the
   contradicting side of each major claim; entries for the countercase positions are first-class.
4. Rebuild → re-validate → receipt v3 → append `## Repair round (V3)` with the new histograms +
   adjudication stats. Marker: `GORU_STEP4_V3_COMPLETE_20260804`.
The structural fix (enum extension adding `unknown`) is queued for Duho as a contract gate — you
do NOT touch the contract.
