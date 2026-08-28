# HARNESS AUDIT R3 — GPT56

## Verdict

**NOT CLEAR.** The ternary vocabulary is directionally honest only when the parser admits that it failed. The implementation still overclaims recognition: a contiguous recognised prefix can make a real later finding `FABRICATED`, and an unbounded same-grammar non-finding can make a fabricated citation `VERIFIED`. Conversely, a fabricated citation against a mixed or holed report is sheltered as `UNVERIFIABLE`. The pinned specification also explicitly requires mixed-grammar verification while the code rejects every mixed grammar, a narrower `PREREG_TEXT*.md` preflight can silently bypass the wider report discovery path, and one citation control still asserts only the shared category rather than its missing-report outcome. All four pins match and all six required self-tests exit 0, but those green commands do not cover these counterexamples.

## Subject identity — all four pins verified

I recomputed SHA-256 over the exact live bytes before adjudication. Every comparison is exact 64-hex equality:

| subject | pinned | recomputed | comparison |
|---|---|---|---|
| `/Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py` | `1b1f84b8537ef5bc11650b76061094056cd85d4c36ff7d4a14a940c1a4a0de9f` | `1b1f84b8537ef5bc11650b76061094056cd85d4c36ff7d4a14a940c1a4a0de9f` | MATCH |
| `../CITATION_CHECK_SPEC.md` | `5db2cf1cc3c2c23ba020ab2d13b87d6a4714ef3842b505de9c2fcb5d41570149` | `5db2cf1cc3c2c23ba020ab2d13b87d6a4714ef3842b505de9c2fcb5d41570149` | MATCH |
| `/Users/duhokim/NebulaMind/NebulaMind/tools/void_registry.py` | `4980701ce8695985d106f840ce8ebe6a9a5d06c15d51f40aff9544bc59046185` | `4980701ce8695985d106f840ce8ebe6a9a5d06c15d51f40aff9544bc59046185` | MATCH |
| `../ref/verdict_breakpoints.py` | `bd248c93984ffa2ed39cae16173df7b9535163e02c325109bfbb680bfcf39e56` | `bd248c93984ffa2ed39cae16173df7b9535163e02c325109bfbb680bfcf39e56` | MATCH |

## Findings

### F1 — BLOCKER — `UNVERIFIABLE` does not prevent either false document defects or fabricated citations from hiding

`declared_findings()` (`prereg_lint.py:296-317`) calls a report recognised when exactly one regex grammar produces a set contiguous from 1. That does not establish complete parsing.

I exercised the public `citation_outcome()` path with isolated exact-version reports:

1. **Recognised prefix, missed real suffix.** A report containing `### F1`, `### F2`, then a real declaration `### Issue 3 — ...` returned `('recognised', {1, 2})`. Citation to the real finding 3 returned `('FABRICATED', {1, 2})`. This is the generating defect again: the `F` regex is narrow, but the contiguous prefix lets its miss become an absence claim and a document defect.
2. **Unbounded same-grammar non-finding.** A report containing `## Findings; ### F1`, then `## Failed attacks; ### F2 — method item, not a finding` returned `('recognised', {1, 2})`. Citation to fabricated F2 returned `VERIFIED`. `region = body[m.end():]` at line 306 is never closed at the findings section boundary, and contiguity cannot distinguish a later same-grammar numbered item from a declaration.
3. **Fabrication hidden by mixed grammar.** A complete report containing real `### F1` and real `### Finding 2` returned `UNVERIFIABLE`; citation to nonexistent F99 also returned `UNVERIFIABLE`. This directly answers the load-bearing question: a real fabricated citation can hide behind “unrecognisable grammar.”
4. **Fabrication hidden by a hole.** A report containing `### F1` and `### F3` returned `UNVERIFIABLE`; citation to nonexistent F99 remained `UNVERIFIABLE`.

The third outcome is honest as a statement about parser uncertainty, but it is not an effective anti-fabrication gate on reports the implementation declines to recognise. Worse, the same implementation still emits false `FABRICATED` and false `VERIFIED` outcomes whenever its incomplete match happens to look contiguous.

Smallest sufficient conclusion for this round: the stated goal cannot be achieved by this contiguity proxy over the present regex surface. Either finding IDs must be machine-encoded/bound in the report format, or every non-`VERIFIED` citation must gate the correction claim without converting parser failure into a document accusation. The current distinction is useful diagnostically but does not make the check sound.

### F2 — HIGH — the pinned specification and code diverge on mixed grammar, outcome count, and required guards

The pre-code specification is binding and the discrepancies are direct:

- Spec lines 39-40 require acceptance when the report declares the finding in any grammar it actually uses, “including a report mixing grammars.” Spec lines 71-75 again require a mixed-grammar report to `VERIFY` and require each control to assert its outcome. Code lines 299-313 instead require **exactly one** grammar and return `UNVERIFIABLE` for every mixed report. The synthetic real F1/Finding-2 report above demonstrates the divergence.
- Spec lines 46-56 define exactly three outcomes and say only `FABRICATED` may be reported as a document defect. Code lines 320-334 add a fourth `NO-REPORT` outcome, and lines 255-257 emit it as a `repair-citations` finding rather than classifying it within the pinned three-outcome contract.
- Spec lines 66-73 require positive guards for each grammar, a mixed-grammar positive, a numbered-non-finding negative, and an unverifiable path. The shipped controls at lines 397-405 contain only one corpus-dependent fabricated probe and one corpus-dependent unverifiable probe; there is no synthetic per-grammar positive, mixed positive, or same-grammar post-section non-finding guard. The false `VERIFIED` construction in F1 therefore remains green.

The spec is also internally tense: lines 55-56 permit mixed forms “inconsistently” to be unverifiable, while lines 39-40 and 71-72 positively require a mixed-grammar declaration to verify. The implementation resolves that tension in the stricter direction, but that resolution contradicts the spec's explicit mixed positive and is not permitted by the pinned bytes.

### F3 — HIGH — the fifth narrower-than-data instance silently bypasses citation checking before report discovery

`check_repair_citations()` lines 240-242 first builds `corpus` from only `gates.glob("PREREG_TEXT*.md")` and returns silently if that narrow filename family is absent. But `_reports_for()` lines 275-285 deliberately supports wider historical report names, including any name with `REVIEW` and an exact seat/version token.

I created an isolated gate directory containing only `V99_WHOLE_REVIEW_GPT56.md`, with a recognised F1/F2 findings section, and checked a correction citing nonexistent `GPT56-V99 F99`. `check_repair_citations()` returned `[]`: neither `FABRICATED` nor `UNVERIFIABLE` nor `NO-REPORT` was emitted. The wider resolver was never called.

This is the fifth narrower-than-data instance: a narrow presence preflight over `PREREG_TEXT*` is being used to establish that there is no citation corpus, even though the implementation's own resolver says `*_WHOLE_REVIEW_*` and other review names are valid data. It is a silent-clean bypass of the ternary design.

### F4 — HIGH — one citation control still asserts the category rather than the outcome

`CONTROLS[0]` at line 398 is:

```python
("check_repair_citations", _mut_repair_citations, "repair-citations")
```

It has no `want` outcome substring, so `self_test()` lines 455-468 accepts any `repair-citations` message. I monkeypatched the missing-report path so `NO-REPORT` was wrongly converted to `UNVERIFIABLE`. The result still printed:

```text
OK   check_repair_citations: control fires
self-test: 8 controls, 0 failure(s)
```

and returned 0. Thus the two newer controls correctly assert `declares findings` and `UNVERIFIABLE`, but the original missing-report control still asserts only the category. This is exactly the category-versus-outcome residue named in the brief.

### F5 — MEDIUM — contiguity is neither a completeness proof nor a full internal-consistency check

The prefix and post-section attacks in F1 show contiguity can be true while parsing is incomplete or polluted. A second direct construction shows the inverse limitation of the set-based implementation: `F1, F2, F2` returns `('recognised', {1, 2})`. Duplicate declarations disappear in the set at lines 309 and 314, so a report that is not internally consistent still satisfies the claimed consistency proxy.

The rule does correctly decline a visible `F1, F3` hole, but that safety is one-sided: it converts the report to `UNVERIFIABLE` and shelters every actually absent number. It does not make absence decidable. Contiguity is a useful alarm on one class of parse miss; it cannot bear the stated complete-parsing inference.

## Canary deletion probes — repaired controls held

I independently monkeypatched the live module and ran its full `self_test()` each time:

| probe | observed result |
|---|---|
| baseline | return 0; 8 controls, 0 failures |
| membership test deleted (`FABRICATED` changed to `VERIFIED`) | return 1; `citation fabricated: control SILENT` |
| parser neutered (recognises all positive integers) | return 1; fabricated and unverifiable controls SILENT |
| unverifiable branch cut (`UNVERIFIABLE` changed to `VERIFIED`) | return 1; `citation unverifiable: control SILENT` |
| grammar guard removed (all regex hits unioned and called recognised) | return 1; `citation unverifiable: control SILENT` |

Therefore the four deletion probes requested in the brief do turn the battery red. This repair held. It does not cover F1-F5.

## Required self-test executions

Every named self-test was run independently from the assigned absolute gate directory with `PYTHONDONTWRITEBYTECODE=1`:

1. `prereg_lint.py ...V34... --gates . --self-test` — exit 0; 8 controls, 0 failures.
2. `prereg_trace.py .. --check ...V34... --self-test` — exit 0; clean baseline, 3 scope rules, 0 failures.
3. `void_registry.py ...V34... --self-test` — exit 0; 52 antecedents; 6 controls, 0 failures. The public control now prints `row loses its naming antecedent`.
4. `bs2a_quality_gate.py --self-test` — exit 0; 36 controls, all 26 checks exercised, 0 failures.
5. `gain_gradient_estimator.py --self-test` — exit 0; five exact recovery fixtures, three normalization regressions, 9/9 codes exercised, 0 failures. The deliberate hostile numeric cases emitted expected NumPy overflow warnings before the required refusal outcomes.
6. `verdict_breakpoints.py --self-test` — exit 0; 48 production-transcription points, 10 breakpoints including five p-gate points, T01/T02 controls, no reported orphan, 0 failures.

I also ran normal V34 lint: exit 0; 23 §7 rows (15 P, 8 E), 22 BS identifiers, no reported inconsistency. Per the brief, I did not redo the already-cleared `prereg_trace` refactor or independently re-adjudicate V34's citation reality.

## Failed attacks / what held

- All four pinned digests match exactly.
- All six required self-tests complete with exit 0.
- The four requested citation-canary deletion probes each make the lint self-test return 1.
- Exact version matching remains numeric-boundary aware in `_reports_for()`.
- The visible `void_registry` control label is narrowed to naming, and its self-test compares exact refusal-code sets.
- The verdict orphan regex now recognises both quote styles for literal `refuse('T##', ...)` / `refuse("T##", ...)` as well as the direct bracket idiom.
- A visible numbering hole does produce `UNVERIFIABLE` rather than a fabricated absence claim.

## Scope, parked decisions, and write custody

I did not re-litigate `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` or `OPEN_QUESTION_T_COMPLETENESS.md`. Nothing here fills a slot, touches BS-6, authorises execution, or changes V34. I treated the R1/R2 reports as inputs to attack, not ground truth. Temporary adversarial reports existed only in automatically removed temporary directories or memory. Before this report write, targeted `git status --short` over the four pinned subjects and report path was empty. No pinned subject, parked-question file, preregistration draft, report under test, or reference artifact was edited; this report is the sole intended repository write.

**NOT CLEAR**