# V119 APPENDIX THIRD READ — CODEX

## Verdict

**DEFECTIVE.** I verified the two required identities before reading: `gates/KNOWN_DEBT_APPENDIX.md` is `c2a5cacacac5f059964932b27c0f170db0677c9794320072e6200a5a22cc4bf7`, and `PREREG_SUCCESSOR_DRAFT_V119_20260831.md` is `b2cad7fa875b3e0e8388a8e409611c3c480d40363d9f112a4357d7c1b1b7256a`. The 334-item enumeration, U+2019 restoration, normalized-substring refusal, closing-total refusal, boundaries, divergence predicate, and four-form mutation coverage all hold on the current bytes. Three disclosure/control defects remain: the Stage-P “full passage” is only a context-dependent tail fragment; the appendix still states a broader FORM predicate than the implementation and V119 sentence; and the new form controls exercise a duplicated test predicate rather than the shipped production branch while the draft says otherwise.

## 1. The eight V118 findings

| V118 finding | V119 result | Independent verification |
|---|---|---|
| CODEX F1 | **REPAIRED** | The 63 pre-convention ledger rows sum to 334. Their 63 named era reports contain exactly 334 FINDINGS-BLOCK F-lines; every report has one well-ordered marker pair, global F-lines equal in-block F-lines, and all 334 appendix quotations equal their source F-lines exactly. There are no absent reports, pre-block reports, or count mismatches in the current population. |
| CODEX F2 | **REPAIRED** | The GPT56-F3 appendix quote contains `form’s` with U+2019 and is a whitespace-normalized substring of `V116_WHOLE_REVIEW_GPT56.md`. All six eligibility excerpts similarly verify 6/6. A planted false quote is refused. |
| CODEX F3 | **PARTIAL** | Production now uses `(?<![\w-])…(?![\w-])`, detects a candidate sharing at least two current-form fields when it equals no mapped form, and has four per-form loops for prefix rename, tuple deletion, first-field corruption plus distant decoy, and cross-form substitution. But the controls call the separately implemented `_form_probs()` twin at lines 571–591, not the production FORM branch at lines 820–862; and the appendix still describes the broader “every kind-adjacent tuple-shaped string” predicate. |
| CODEX F4 | **REPAIRED** | `parse_ledger()` compares the closing line’s pre-convention number to the parsed row sum and refuses 334 against a synthetic sum of 7. The explicit contradiction probe and the generator’s 6/6 self-test both pass. |
| GPT56 F1 | **REPAIRED** | Same independent 334/334 exact per-finding enumeration result as CODEX F1. |
| GPT56 F2 | **NOT REPAIRED IN FULL** | The four new excerpts are genuine normalized substrings (4/4), but substring membership is not passage completeness. Most clearly, the Stage-P entry quotes only `this is an open blocker … either way.`—a 105-character, lower-case, pronoun-dependent tail from a 3,820-character draft block. It omits the block’s two operative definitions (exact per-trial versus shared-null), the precedence conflict, and the reason no wording change closes it. It therefore cannot be the claimed full passage and is not independently intelligible as the named dual-valued limitation. |
| GPT56 F3 | **REPAIRED** | Same U+2019 and 6/6 source-verification result as CODEX F2. |
| GPT56 F4 | **PARTIAL** | The V119 §11 sentence accurately states the production predicate’s ≥2-shared-field threshold, SOME-mapped-form allowance, word boundaries, and per-form mutation list. The appendix does not: §4 still says every kind-adjacent tuple-shaped string must be byte-equal to “the mapped form,” omitting both the ≥2 relevance threshold and the legitimate-neighbour/SOME-mapped-form rule. The draft’s further statement that controls run “through the shipped logic” is also false because the synthetic controls use `_form_probs()`, a duplicated implementation. |

## 2. Changed-region review

The V118→V119 draft diff has exactly three line-level chunks: the title, insertion of the V117→V118 history row, and replacement of the §11 FORM sentence. The title and history insertion are internally consistent. The replacement sentence correctly describes the present production predicate, but its control-path claim is false: `_domain_echo_selftest()` implements and invokes `_form_probs()` separately, while `main()` later reimplements the production check. Current textual equivalence makes the tests green today; it does not make them tests of the shipped branch, and either copy can drift while all advertised controls remain green.

The appendix-generation changes correctly enumerate 334 exact source F-lines, restore U+2019, verify all six eligibility excerpts and four limitation excerpts as normalized substrings, and refuse contradictory closing totals. The new verifier proves only that an excerpt occurs somewhere in the draft; it has no paragraph/block boundary or completeness contract. Consequently it certifies the 105-character Stage-P tail as a “full passage.”

The current appendix’s FORM residue remains inconsistent with both changed production code and the repaired V119 sentence: production limits divergent-candidate checking to backticked `(kind, …)` candidates of 10–400 interior characters sharing at least two fields of the current form, and accepts a candidate equal to any mapped form; appendix §4 claims every adjacent tuple-shaped string must equal the singular mapped form.

## Failed attacks that held

- Hash pins matched before inspection.
- Ledger closure independently reconciled: 63 rows, 334 stated findings, 334 source FINDINGS-BLOCK F-lines, 334 exact appendix quotations, zero report/marker/count anomalies.
- All six V116 eligibility excerpts and all four limitation excerpts are normalized source substrings; the GPT56-F3 U+2019 byte is restored.
- A synthetic false-verbatim quote refused, and a synthetic closing total of 334 against a parsed sum of 7 refused.
- `gates/gen_known_debt.py --check` reported byte equality; its self-test reported 6/6.
- The FORM word boundaries reject prefixed/suffixed word or hyphen continuations; the current production and test-twin predicates are textually aligned; `_domain_echo_selftest()` returned no failures across all four forms.
- No additional defect was found in the V119 title or V117→V118 history-row insertion.

## 3. Signature question

Yes: the appendix does not disclose that its FORM guarantee is broader than the shipped ≥2-field/SOME-mapped-form predicate, and its purported full Stage-P passage omits the two conflicting definitions that make that limitation intelligible.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V119-APPENDIX
VERDICT: DEFECTIVE
COUNT: 3
F1 | HIGH | KNOWN_DEBT_APPENDIX.md §3 lines 589–591; PREREG_SUCCESSOR_DRAFT_V119_20260831.md §2.6 | The claimed full-verbatim Stage-P passage is only a 105-character context-dependent tail and omits the two operative definitions, precedence conflict, and explanation of the dual-valued blocker.
F2 | MEDIUM | KNOWN_DEBT_APPENDIX.md §4 line 597; ref/gen_string_field_registry.py lines 847–862; V119 §11 line 1567 | The appendix says every kind-adjacent tuple-shaped string must equal the mapped form, but production checks only backticked candidates sharing at least two current-form fields and accepts equality to any mapped form; V119 states that narrower contract correctly, leaving the signed appendix false.
F3 | MEDIUM | ref/gen_string_field_registry.py lines 571–625 and 820–862; V119 §11 line 1567 | The all-four mutation controls run against the duplicated `_form_probs()` test predicate, not the shipped production FORM branch, so the draft’s “through the shipped logic” claim is false and future branch drift can leave all controls green.
<!-- END FINDINGS-BLOCK -->