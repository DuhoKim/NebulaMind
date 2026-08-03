# HWAO_SAMPLE_REVIEW — B-P5 unblinded review of the precommitted fixed 10

Unblinding performed only now, per `receipts/HWAO_B_P5_FIXED_SAMPLE_RULE.md`. Inputs: VERDICTS.jsonl (sha256 `a4821a54…7b3f` per Kun audit), VERDICT_LEDGER context via Kun/Tori receipts, ROUTE_MAP, corrected catalog + contamination manifest, active evidence texts, `KUN_VERDICT_AUDIT.md` (GREEN), `TORI_QUOTATION_NORMALIZATION_AUDIT.md`. Offline read-only; no network/live/browser/DB/dashboard/deploy/cron/git/publication action.

## 1. Supplement rule outcome

Ledger verdict distribution: `SUPPORTED` 17 · `SUPPORTED_WITH_SCOPE_NOTE` 17 · `AMBIGUOUS_NEEDS_EXPERT` 38 · `SOURCE_UNRESOLVED` 1 · `NOT_SUPPORTED` 0 · `EVIDENCE_INSUFFICIENT_ABSTRACT_ONLY` 0. The fixed 10 already covers all four classes present in the ledger ⇒ **zero supplements required** (precommitted rule satisfied as written; no post-hoc additions).

## 2. Independent custody checks (recomputed by Hwao, not receipt-trust)

- **Quarantined-contamination sweep:** none of the 73 verdicts references any quarantined path from `SUPPLEMENTAL_CONTAMINATION_CORRECTION.json` — variance/contamination condition 1 holds (matches Kun's audit).
- **Quotation-in-evidence:** all 7 non-empty sampled quotations verified present in their active evidence texts under deterministic normalization (dehyphenation + NFKD + alphanumeric collapse) — consistent with Tori's 59/59 normalization audit; Kun's 29 disclosed substring exceptions are confirmed to be ellipsis/PDF-extraction representation, not custody failures.
- **Span length:** sampled spans are uniformly 51 words — trivially over the plan's soft "≤~50" figure; cosmetic, recorded, no action.

## 3. Fixed-10 outcomes (checklist §4 of the precommitted rule applied to each)

| ID | Verdict | Checklist result | Notes |
|---|---|---|---|
| M018 | `SOURCE_UNRESOLVED` | **PASS** | No-borrow condition exactly honored: no indices, no paths, tier NONE, rationale cites the no-borrow rule; stays quarantined |
| M050 | `SUPPORTED_WITH_SCOPE_NOTE` | **PASS** | Cap honored; evidence from idx-33 full text as required; mapping note present ("32->33 same-work bibliographic mapping; byte identity unproven" — ASCII arrow variant of the required note, accepted as verbatim-equivalent); quotation verified in idx33 text |
| M064 | `AMBIGUOUS_NEEDS_EXPERT` | **PASS** | Document-level limit respected: refuses single-span certification of 37 sources; names idx 27 aggregator and idx 2/8/13 project pages as quality risks. Cosmetic: two duplicate entries in its 45-item path list (idx14, idx33) |
| M065 | `AMBIGUOUS_NEEDS_EXPERT` | **PASS** | Same document-level discipline for source fidelity; explicitly deferred to expert pass |
| M019 | `AMBIGUOUS_NEEDS_EXPERT` | **PASS** | Contaminated-index-1 case: evidences from the CORRECTED authoritative text (`idx01_ads_arxiv_pdf_53e97c8f…`), not the quarantined supplemental; honest doubt-downward (span shows comparison focus, not explicit target designation) |
| M023 | `SUPPORTED` | **PASS with observation O1** | Contaminated-index-4 case: corrected authoritative text used; quotation verified (EAGLE "calibrated to reproduce the observed z=0.1 GSMF and the relation…"). O1: the claim cell's third element (galaxy sizes "statistically similar") is not covered by the recorded span — under strictest doubt-downward this could have been `SUPPORTED_WITH_SCOPE_NOTE`; counted as 1 minor verdict-level observation, no custody/policy violation (T2 full text read; rationale span-faithful). Expert pass should confirm the sizes clause |
| M072 | `AMBIGUOUS_NEEDS_EXPERT` | **PASS** | The FLAMINGO kSZ suspect handled exactly right: token uncorroborated, semantic assessment present, and the shared source-index-30 problem with the BAHAMAS row (M073) explicitly called out — matching the original investigation's mis-citation flag |
| M001 | `AMBIGUOUS_NEEDS_EXPERT` | **PASS** | Contaminated-index-3 case: corrected text used; honest scope split (mass-range context supported; emergent-vs-calibrated status deferred) |
| M009 | `SUPPORTED_WITH_SCOPE_NOTE` | **PASS** | Scope note draws precisely the right validated-vs-calibrated distinction for ASTRID |
| M066 | `AMBIGUOUS_NEEDS_EXPERT` | **PASS** | Comparability token uncorroborated; assessment explicitly names the uniform-`MATCHED_SELECTIONS` token-satisficing pattern |

**Sample result: 10/10 checklist PASS; disagreements = 1 minor (O1, verdict-shade on M023), far below the >2 re-review threshold. Custody violations = 0. Entry-specific conditions (M018 no-borrow, M050 cap/note/idx-33, M064/65 document-level limits + tier honesty for 2/8/13, M072 suspect assessment, three contaminated-index cases on corrected texts) = all satisfied.**

Cosmetic notes for the record, no action required: 51-word spans (§2); M050 note's ASCII "->"; duplicate path-list entries in M064/M065.

HWAO_GATE_B_SAMPLE_REVIEW_DONE_20260713T034742Z
