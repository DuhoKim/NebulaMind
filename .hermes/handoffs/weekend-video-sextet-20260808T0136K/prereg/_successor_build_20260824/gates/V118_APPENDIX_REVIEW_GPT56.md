# V118 APPENDIX RE-READ — GPT56

## Verdict

**DEFECTIVE.** I verified the required hashes before reading: `gates/KNOWN_DEBT_APPENDIX.md` is `0727c126d40f3b89835bf616fe419bc7f7e78a9997d8f9ffd2078e6e4eff491a`, and `PREREG_SUCCESSOR_DRAFT_V118_20260831.md` is `fb07f3f975ec0bccbddb345455e39b59015c265aa009f42923faa099c99ce5d0`. V118 repairs the history row, the real §11 inventory omission, the map's 400→900 mismatch, the population counts, and the blanket echo-description error, but it still does not satisfy the stopping ruling's full-quotation requirement and its claimed form-echo hardening remains defeatable.

## 1. Re-examination of all nine mini-round findings

| Prior finding | V118 result | Verification |
|---|---|---|
| GPT56 F1 | **NOT REPAIRED IN FULL** | The generator now parses `REPAIR_LEDGER.md`, and independent recount gives 177 REPAIRED + 192 MAPPED-BY-CITATION + 334 PRE-CONVENTION = 703 across 84 version-rounds with both seats. All 63 pre-convention ledger summary lines are reproduced byte-for-byte. But the appendix contains 63 per-seat count summaries and **zero individual pre-convention finding IDs or finding texts**. The stopping ruling requires every remaining finding to be “enumerated” and “quoted in full”; saying `V40/GPT56: ... 7 finding(s)` does not enumerate or quote those seven findings. The 334-item population is no longer hidden numerically, but its contents remain hidden behind report-level counts. |
| GPT56 F2 | **NOT REPAIRED** | Five eligibility paragraphs are exact source substrings; GPT56 F3 is not. Source `gates/V116_WHOLE_REVIEW_GPT56.md:67` says `form’s fields`, while appendix line 97 says `form's fields`. The appendix labels the paragraph “verbatim and in full,” so the one-byte-normalization defense is unavailable. |
| GPT56 F3 | **PARTIAL, NOT COMPLETE** | Appendix line 114 now names all four omitted limitations: numerical route, caller-pair authorization, count-only sample guard, and dual-valued Stage-P. It only paraphrases them and points to approximate draft lines; it does not quote any limitation in full, contrary to the same stopping-rule sentence governing findings and acknowledged limitations. |
| GPT56 F4 | **REPAIRED AS WORDING, BUT UNDERLYING CONTRACT OVERSTATED** | The blanket “every echo is demoted” statement is gone and line 116 gives per-echo contracts/non-claims. However its FORM claim that every kind-adjacent tuple-shaped string must equal the mapped tuple is stronger than the shipped predicate, which ignores divergent tuples that omit the form's first non-`kind` field. |
| GPT56 F5 | **REPAIRED** | `gates/FINDINGS_MAP.md:325–327` retains the historical 400-byte wording and explicitly corrects it to the shipped 900-byte window; the V117→V118 entry repeats that correction. |
| GPT56 F6 | **REPAIRED** | The V118 `V99 → V100` row is byte-for-byte equal to the V116 row (2,318 characters); the V117-only count-harness sentence is removed. |
| CODEX F1 | **NOT REPAIRED IN FULL** | Same population defect as GPT56 F1: the 192 mapped population is honestly counted and the 334 debt total is live, but the 334 findings themselves are neither individually enumerated nor quoted. |
| CODEX F2 | **REPAIRED** | V118 §11 line 1280 genuinely registers `count_oracle_harness_sha256` beside the replay-harness inventory discipline, marks it REQUIRED/DOES NOT EXIST/class P, gives the §2.3 contract, and keeps BS-2c DESIGN-gated. This is the real inventory, not the reverted historical row. |
| CODEX F3 | **NOT REPAIRED** | The changed generator adds a proximity guard and tests, but the guard is incomplete and the advertised all-four coverage is false; the concrete counterexamples are in F4 below. |

Generator checks themselves currently pass: `gen_known_debt.py --check` is byte-equal, its self-test reports 3/3, and `gen_repair_ledger.py --check` is complete and byte-equal. Those checks establish regeneration, not compliance with the ruling's full-quotation requirement.

## 2. Changed-region attacks (V117→V118 and appendix v1→v2)

The V117→V118 draft has six changed line regions: heading; §2.3 inventory claim; V99→V100 reversion; the inserted V116→V117 trace row; §11 inventory registration; and the FORM-echo description. The first five held the scoped attacks. The appendix population arithmetic, exact 63-line ledger reproduction, four limitation names, per-echo separation, and open-build inventory also held their direct checks.

The changed FORM-echo region did not hold:

1. **The “boundary-aware” kind pattern is not boundary-aware.** `_kpat = re.escape(_kind) + r"(?!-)"` rejects `successor-export-prelock` for the shorter kind, but accepts both `successor-exportX` and `fake-successor-export` as mentions of `successor-export`; it has neither a left boundary nor a general right identifier boundary.
2. **The decoy guard still accepts a corrupted declaration.** For `successor-export`, a nearby corrupt tuple ``(kind, continuation_segment_digest, terminal_head, freeze_signature_digest, flagged_keys)`` plus a clean exact tuple in the 900-byte window yields `_pair = True` and no divergent-tuple error. The guard's `_first in _cand` condition excludes the corrupt tuple precisely because `sealed_enumeration_digest`, the first non-kind field, was deleted. This disproves the draft/appendix claim that every adjacent tuple-shaped string is compared.
3. **The controls are not all-four-form controls.** Rename runs over all four forms, but the adjacent-corruption/distant-decoy and cross-form substitution probes run only with `forms=FORM_SCHEMAS[:1]`; there is no separate tuple-deletion probe. V118 §11 nevertheless says rename, deletion, adjacent corruption, and cross-form substitution run through shipped logic for all four forms.

No additional changed-region defect was found beyond the four findings below.

## 3. Signature question

Yes—the appendix does not name that its FORM contract can still be satisfied by non-boundary kind substrings and by a corrupted adjacent tuple shadowed by a clean decoy, while its claimed all-four control coverage is not implemented.

## Evidence and scope

Read-only inspection covered the two pinned artifacts, both V117 mini-round reports, both V116 source reports, the stopping ruling, `REPAIR_LEDGER.md`, `FINDINGS_MAP.md`, `gen_known_debt.py`, the V117/V118 draft diff, the V116/V117/V118 historical-row bytes, and the changed FORM logic/self-tests in `ref/gen_string_field_registry.py`. I wrote only this required report file.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V118-APPENDIX
VERDICT: DEFECTIVE
COUNT: 4
F1 | HIGH | KNOWN_DEBT_APPENDIX.md §1:11–81 / STOPPING_RULE_RULING:16–19 | The appendix reproduces 63 report-level count lines but zero individual IDs or full texts for the 334 standing pre-convention findings, so the debt population is counted rather than enumerated and quoted in full.
F2 | MEDIUM | KNOWN_DEBT_APPENDIX.md §3:114 / STOPPING_RULE_RULING:16–19 | The four newly acknowledged limitations are paraphrased with approximate pointers, not quoted in full as the signing ruling requires.
F3 | MEDIUM | KNOWN_DEBT_APPENDIX.md §2:95–97 / V116_WHOLE_REVIEW_GPT56.md:67 | The claimed-verbatim GPT56 F3 paragraph changes source `form’s` to `form's`, leaving the prior quotation-fidelity repair incomplete.
F4 | HIGH | ref/gen_string_field_registry.py:569–614,805–848 / V118 §11:1566 / appendix §3:116 | The FORM repair accepts non-boundary kind substrings and a corrupt adjacent tuple missing its first field, while decoy/cross-form probes cover only form 1 and no tuple-deletion probe exists despite the all-four claim.
<!-- END FINDINGS-BLOCK -->