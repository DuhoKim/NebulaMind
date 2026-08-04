# KUN BRIEF — C41 Step-1 refutation + decoy test

Lane: `c41-baseline-restart-20260803T1253Z`. You are Kun (Kimi K3). FINDINGS ONLY, plus the
mechanical decoy exercise below. Temps as `_tmp_kun_*` in this lane dir only.

## Target

Tori's Step-1 package: `STEP1_CORPUS_PROTOCOL.md`, `step1_filter.py`, `SELECTION_INCLUDED.json`
(180 records), `SELECTION_EXCLUDED.json` (11 rule classes), `SELECTION_SHAS.txt`,
`TORI_STEP1_REPORT.md`. Ground truth: the engine files its input_manifest sha-pins, and the frozen
question `STEP0_FROZEN_QUESTION.md` (sha 9ac5ca1f…).

## Attacks required

1. **Determinism** — re-run `step1_filter.py` yourself (outputs to `_tmp_kun_rerun/`); byte-compare
   against Tori's outputs. Any nondeterminism (ordering, set iteration, missing seed) is a finding.
2. **Rules-vs-outputs fidelity** — do the 11 exclusion rule classes in the protocol match what the
   code actually implements? Any exclusion without a named rule? Any rule in prose absent in code?
3. **DECOY TEST (per plan, Kun F7)** — select ≥4 decoys from the C41 membership yourself: papers a
   motivated selector would want gone (e.g., ones cutting AGAINST an expected map outcome on the
   three axes; borderline-LRD papers; low-cite contrarian entries). Determine each decoy's fate
   under the filter. PASS = every decoy is either included, or excluded by a rule that would
   exclude it regardless of its conclusion (rule-based, conclusion-blind). FAIL = any path where
   conclusion-aware exclusion is possible. Document decoy IDs, fates, rules.
4. **Ordering sanity** — the priority tiers (contested-dispersion-first) and the within-priority
   weights (0.75 recency + 0.23 log-cite + 0.02 review): do they implement the plan's
   "contested-measurement-first, recency-weighted, review-aware"? Does the review cap (24) or
   anchor cap (8) silently distort the top-180 in a way the protocol doesn't disclose?
5. **LRD boundary rule** — does the filter implement the frozen question's rule (in only as
   bearing on the three axes; nature-of-LRDs not a fourth axis), or approximate it? How?
6. **Peek-log honesty** — is the "no candidate-record peeks" claim consistent with what the
   protocol's rules could have been written from?

## Deliverable

`KUN_STEP1_REFUTATION.md` in this lane dir: verdict (SEALED / SEALED_WITH_PATCHES / REJECTED),
ranked findings w/ evidence, decoy table, failed attacks, evidence ledger. End with marker:
`KUN_C41_STEP1_REFUTATION_COMPLETE_20260803`.
