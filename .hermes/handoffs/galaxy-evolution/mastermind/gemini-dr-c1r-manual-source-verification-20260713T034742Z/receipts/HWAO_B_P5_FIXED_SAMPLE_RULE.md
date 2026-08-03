# HWAO_B_P5_FIXED_SAMPLE_RULE — pre-registered fixed 10-entry Hwao sample (blinded)

Written BEFORE reading any verdict deliverable. Blinding attestation: `verification/VERDICTS.jsonl` and `verification/VERDICT_LEDGER.md` were NOT opened; the P2/P3 correction briefs (`GORU_B_P2_CORRECTION_BRIEF.md`, `LANA_B_P3_CORRECTION_BRIEF.md`) were deliberately left unread because they are verdict-adjacent. Files read for this pre-registration, only: `HWAO_PARALLEL_PLAN.md` (own plan), `sources/ROUTE_MAP.json` (routing summarized programmatically — manual_id → lane / source_refs / source_indices only), `sources/SUPPLEMENTAL_CONTAMINATION_CORRECTION.json`, plus directory listings. This pre-registration supersedes the plan's B-P5 "≥15, min(2, lane)" sampling clause by Duho's direction (logged amendment); no verdict is assessed in this file.

## 1. Selection rationale (all criteria are pre-verdict facts: routing, custody, and previously documented risk)

Seven **risk-pinned** picks target every known custody pressure point: the only citation-less entry (rule-application test); the sole claim-level entry routed to contested index 32 (network-variance conditions); both document-level aggregates (they span all 37 indices, including the three non-T1/T2 sources 2/8/13, the contaminated 1/3/4, and the 14↔29 near-duplicate); one entry each on contamination-affected indices 1 and 4 (the idx-3 exposure is covered by an algorithmic pick, below); and the FLAMINGO kSZ comparability cell flagged as semantically suspect since `HWAO_ROOT_CAUSE.md`. Three **algorithmic** picks are fixed arithmetic (lowest lane ID / median lane position) with zero discretion. Resulting lane coverage — 3 uncertainty / 5 source-fidelity / 2 comparability — is exactly proportional to the 18/47/8 lane sizes.

## 2. Exact fixed sample (10 IDs, final)

| # | ID | Lane | Pre-verdict selection basis |
|---|---|---|---|
| 1 | **M018** | UNCERTAINTY_OR_SCOPE | only entry with no citation bound in its unit (`gap_line_4`, `source_indices=[]`) — fail-closed rule-application check |
| 2 | **M050** | SOURCE_FIDELITY | sole claim-level entry routed to index 32 (`bullet_23`) — variance-disposition conditions apply |
| 3 | **M064** | SOURCE_FIDELITY | document-level citation-quality aggregate, all 37 indices |
| 4 | **M065** | SOURCE_FIDELITY | document-level source-fidelity aggregate, all 37 indices |
| 5 | **M019** | SOURCE_FIDELITY | lowest source-fidelity ID **and** routed to contaminated index 1 |
| 6 | **M023** | SOURCE_FIDELITY | lowest source-fidelity ID routed to contaminated index 4 |
| 7 | **M072** | SCIENTIFIC_COMPARABILITY | FLAMINGO kSZ COMPARABILITY cell (`table_row_20:3`) — pre-documented suspect token |
| 8 | **M001** | UNCERTAINTY_OR_SCOPE | algorithmic: lowest uncertainty-lane ID (incidentally covers contaminated index 3) |
| 9 | **M009** | UNCERTAINTY_OR_SCOPE | algorithmic: 9th of the 18 uncertainty entries (median position) |
| 10 | **M066** | SCIENTIFIC_COMPARABILITY | algorithmic: lowest comparability-lane ID (`table_row_14:3`; source 27, the aggregator-resolved chip) |

## 3. Pre-registered supplement rule (verdict-class coverage, decided now)

After unblinding: if any verdict class of the pinned six-term vocabulary that is present in the ledger has zero representation among the fixed 10, add the lowest-manual_id entry bearing that verdict — maximum 2 supplements. If more than 2 classes would remain uncovered, that is itself a finding: escalate to a full review of the uncovered classes (plan B5 posture) instead of enlarging the sample ad hoc. No other additions, substitutions, or removals are permitted post-unblinding.

## 4. Pre-registered per-entry assessment checklist (applied identically to all sampled entries)

(1) exactly one verdict, from the pinned vocabulary; (2) recorded evidence tier consistent with the B2 hierarchy, with the abstract-only cap enforced (`EVIDENCE_INSUFFICIENT_ABSTRACT_ONLY` can never be `SUPPORTED*`); (3) evidence span ≤50 words with location, from a sha256-verified stored artifact on an approved route; (4) evidence path absent from the contamination-correction quarantine lists (binding for M019/M023/M001/M064/M065 and any idx-1/3/4 dependency); (5) doubt-resolves-downward respected on the face of the record; (6) entry-specific conditions — M050: evidence artifact is index-33's persisted full text, verbatim "32→33 same-work bibliographic mapping; byte identity unproven" note present, verdict capped at `SUPPORTED_WITH_SCOPE_NOTE`; M018: no borrowed source, verdict consistent with unresolved/fail-closed handling; M064/M065: sources 2/8/13 held at their true tier, never promoted; M072/M066: one-line semantic token assessment present. Disagreement handling: >2 disagreements across the sample (incl. supplements) ⇒ full re-review of the affected class(es) before B-P5 close.

HWAO_GATE_B_FIXED_SAMPLE_PRECOMMITTED_20260713T034742Z
