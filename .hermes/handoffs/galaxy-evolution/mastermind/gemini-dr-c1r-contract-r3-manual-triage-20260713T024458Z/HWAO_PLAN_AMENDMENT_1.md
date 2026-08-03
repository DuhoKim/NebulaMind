# HWAO_PLAN_AMENDMENT_1 — zero-count lanes, non-empty-lane sampling, D3 crosswalk scope

Ref: `receipts/TORI_PRECLASSIFICATION_SHAPE_NOTE.md` (accepted in full) · Amends `HWAO_PLAN.md` §1-P2, §1-P3, and the §0 rules via the logged-amendment path in §3.3. Everything else in the plan, including all stop conditions and hard boundaries, is unchanged. No new work is started by this amendment; P2 may begin only after Tori relays it.

## A1. Zero-count lanes are valid

The §0 lanes are available categories, not quotas. A lane with zero entries is a legitimate outcome when no source entry fits its definition — expressly anticipated for `CONTRACT_R3_CHANGE` and `IGNORE_FOR_THIS_CONTRACT_TEST` given the verified queue composition (18 × C3:UNCERTAINTY_CHECK, 40 × C4:CITED_CELL_CLAIM_REVIEW, 5 × C4:CITED_CLAIM_REVIEW, 1 × C4:CITATION_QUALITY_REVIEW, 1 × C4:SOURCE_FIDELITY_REVIEW, 8 × C6:COMPARISON_LABEL_REVIEW = 73). **No entry may be classified into a lane to satisfy a sampling or optics expectation.** For each zero lane, Lana adds one line to `TRIAGE_LEDGER.md`: `ZERO_LANE <name>: no entry fit because <reason>`.

## A2. P3 sampling rule (replaces "≥2 from every lane")

Tori's spot verification samples **min(2, lane size) entries from every non-empty lane**, total sample ≥15 entries (the 73-entry queue always permits this), with the balance drawn proportionally from the largest clause:code groups. **Zero lanes are audited as zero:** Tori independently confirms no sampled or scanned entry plausibly belonged to the zero lane and countersigns each `ZERO_LANE` line; Kun's arithmetic receipt must reproduce the clause:code composition table above and show lane sums + zero-lane claims reconciling to exactly 73.

## A3. D3 crosswalk scope (deterministic vs manual custody)

Confirmed: the eight Section-2 `UNCITED_CELL_CLAIM` findings that D3 re-types are **deterministic FAIL findings in the 17-finding residue, not members of the 73-entry manual queue**, and must NOT be inserted into `TRIAGE_LEDGER.*` (exactly-73 source-order custody stands, stop condition 2 unchanged). Instead, `design/CONTRACT_R3_DRAFT.md` carries the crosswalk: each D-item's change record cites the findings it resolves **from either population**, referencing deterministic entries by their FAIL identity in `validator_result_v2.json`/`RESIDUE_REPORT.md` (for D3: the 8 Result-cell failures; likewise D2 ↔ the SIMBA ∼10% `MISSING_QUALIFIER`, D4 ↔ the C7 integrity finding, D5 ↔ the GAP-granularity history, D1 ↔ the 6 `UNLABELED_COMPARISON`) and manual entries by their queue index. The P2 requirement "cross-map for each `CONTRACT_R3_CHANGE` entry" applies only to manual entries actually classified into that lane — which may be none (A1).

HWAO_PLAN_AMENDMENT_1_DONE_20260713T024458Z
