# HARNESS AUDIT — CODEX R2

## Verdict

**NOT CLEAR.** The `prereg_trace.py` refactor is sound: the production predicates are unchanged, all four production refusal branches behaved identically before and after factoring, all three repaired controls invoke `check_trace()` and produce the exact named result, and V34's zero is supported by 18 exercised in-band row checks, 18 matching result digests, 16/16 mapped normative transitions, and the present V33→V34 sidecar mapping. The exact V34 correction citations also remain real and germane. But the rebuilt citation parser is unsound in both directions. It accepts the requested non-finding numbered item, accepts a real false citation to failed-attack item 12 in a report with only three findings, and cannot compose its four claimed grammars in one report. Its built-in canary still tests only report absence, so it cannot detect either defect. Two smaller R1 repair residues also remain: `void_registry` still prints the old “row loses coverage” overclaim, and the verdict orphan scan's `refuse()` arm is unexercised and recognizes only double-quoted calls.

## Exact subject identities

All five supplied SHA-256 pins were recomputed from the live bytes before adjudication. Every comparison is an exact 64-hex **MATCH**.

| subject | supplied | recomputed | comparison |
|---|---|---|---|
| `/Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py` | `522356f1b1d82894b97cd17d98026eb6488c99f6f382e27324777236f9cf4f38` | `522356f1b1d82894b97cd17d98026eb6488c99f6f382e27324777236f9cf4f38` | MATCH |
| `/Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py` | `9bd194b96a4feeb22e85d07b2a2860a11f6c37bfeeebc3fa891bf55d3f877ae8` | `9bd194b96a4feeb22e85d07b2a2860a11f6c37bfeeebc3fa891bf55d3f877ae8` | MATCH |
| `/Users/duhokim/NebulaMind/NebulaMind/tools/void_registry.py` | `f494e5b858a4518bf9299023603e5e82e87eca2bca18a02317ce07790976f1a4` | `f494e5b858a4518bf9299023603e5e82e87eca2bca18a02317ce07790976f1a4` | MATCH |
| `../ref/verdict_breakpoints.py` | `5ed290a61d54a771ff2a346abe867725e40a5373ff37fbbca4a6f4f9a25af93b` | `5ed290a61d54a771ff2a346abe867725e40a5373ff37fbbca4a6f4f9a25af93b` | MATCH |
| `../PREREG_SUCCESSOR_DRAFT_V34_20260828.md` | `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` | `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` | MATCH |

## Findings

### F1 — BLOCKER — the citation parser accepts numbered non-findings, including a false citation against a real report

The requested adversarial construction is accepted. With this report body:

```markdown
## Findings
1. **Method and scope reviewed**
```

`_declared_findings()` returned `{1}`. A full `check_repair_citations()` call against a temporary `PREREG_TEXT_V99_CODEX.md` containing those bytes accepted `CODEX-V99 F1` with no finding. The parser also returned `{1}` when the same item was placed under `## Methods`, so the false acceptance is broader than the requested case.

There is a live-corpus witness, not merely a synthetic one. `V33_WHOLE_REVIEW_GPT56.md` begins its numbered-findings surface at line 50 and declares exactly three findings at lines 52, 62, and 79. Its separate failed-attacks section begins at line 121 and contains items 1–12 at lines 123–134. `_declared_findings()` returned `{1,2,...,12}`, and the full citation checker **ACCEPTED** synthetic citation `GPT56-V33 F12`. Item 12 is “Mechanical checker failure — failed,” not Finding 12.

The root is `prereg_lint.py:324-339`. When the explicit-heading pass found nothing, the fallback anchors once at a heading containing “finding,” scans numeric headings to the end without closing the section, and then unconditionally adds every top-level `N. **...**` item in the entire body at lines 337–338. It therefore absorbs failed attacks, methods, held checks, and any other top-level numbered list as findings. The earlier line-state parser at lines 305–317 independently accepts a bold numbered item merely because the latest heading contains the substring `finding`; it does not establish that the item is a finding declaration.

The requested narrower negative controls did hold: generic `## 8. Evidence` alone returned no finding, and `GPT56-V1 F3` was rejected because the numeric version boundary did not borrow V11. Those successes do not cover the live F12 false acceptance.

Smallest sufficient repair: parse one bounded findings section structurally, stop at the next heading of equal or shallower depth, and admit only declarations at the section's declared item depth. Do not run a whole-document list fallback. Add the exact requested non-finding item and the live V33 failed-attacks F12 case as negative controls.

### F2 — HIGH — the four claimed citation grammars are not composable, and the canary still does not test finding existence

A single fixture containing all four documented forms:

```markdown
## Findings
### F1 — blocker
### Finding 2 — blocker
### 3. blocker
4. **BLOCKING — blocker**
```

should declare `{1,2,3,4}`. The shipped `_declared_findings()` returned only `{1,2}`. A smaller mixed fixture (`### F1` followed by `### 2.` under the same Findings heading) returned only `{1}`.

This is the fifth narrower-than-data pattern. `prereg_lint.py:301-303` first collects the `F1` / `Finding 2` forms globally. Because `found` is then nonempty, the `if not found:` gate at line 324 suppresses both the bare-numbered-heading parser and the top-level-list parser. The implementation supports four grammars only as mutually exclusive report-wide modes, not as declaration grammars that may coexist.

The built-in canary remains unable to catch this or F1. `_mut_repair_citations()` at lines 386–388 still cites `CODEX-V98 7`, whose report does not exist. Its observed finding was exactly “no report for CODEX V98 exists.” That exercises the old report-existence branch and never invokes finding parsing against an existing report. The parser could return every positive integer, or reject every real declaration, and this canary would remain green. This is why the required lint self-test reported six controls and zero failures while both parser defects above were live.

Smallest sufficient repair: make the grammar union composable in one bounded section and replace the canary with at least (a) existing report / nonexistent finding, (b) one positive for each grammar, (c) a mixed-grammar positive, and (d) non-finding numbered items both under and outside the findings heading.

### F3 — LOW — the R1 void-registry control-label repair is still incomplete

The substantive narrowing holds: `void_registry.py:21-35`, CODES V05/V06 at lines 84–88, and refusal messages at lines 192–197 correctly say the predicate establishes naming, not semantic coverage. The new summary at lines 266–268 also explicitly says “control coverage, NOT semantic coverage.”

But the exact R1 residue remains in the pinned bytes. `_mut_drop_row()` still says “its §6.1 row loses coverage” at lines 203–205, and `CONTROLS` still names the public control `row loses coverage` at line 232. The required self-test consequently printed:

```text
OK   row loses coverage: ['V05']
```

The brief says all four converged findings were repaired; this one was only partially repaired. Rename the mutator/control to “row is no longer named” (and preferably `covered` to `named_rows`) so the user-visible test says exactly what V05 proves.

### F4 — LOW — the verdict orphan repair recognizes one spelling of `refuse()` but does not prove that parser arm

`verdict_breakpoints.py:276-277` now unions direct bracket emissions with `refuse("T##", ...)`, so the exact double-quoted sample is recognized. But the `refuse()` regex accepts only double-quoted Python calls. Applying the shipped union produced:

- `bad.append("[T03] direct")` → `T03`;
- `refuse("T03", "x")` → `T03`;
- `refuse('T03', 'x')` → nothing.

More importantly, the self-test scans only its own current source, where T01/T02 are both emitted through direct bracket strings. Removing the new `refuse()` regex arm would leave the self-test green. Thus the summary claim that both idioms are “proved in both directions” is stronger than the control: one arm is implemented for one quoting style but has no positive synthetic witness. An AST walk over literal first arguments, plus one synthetic positive per idiom and one orphan negative, would close both the syntax and regression gap.

## `prereg_trace` refactor adjudication — held

I compared commit `03c686b85^` (the R1-era inline checker) against the pinned refactor. The diff preserves every production loop, threshold, scope comparison, regex, bookkeeping exemption, and sidecar/normative predicate. The material transformations are:

- `print(...)` + `bad += 1` became `out.append(...)`;
- `Path(args.check).name` became the equivalent `subject_name` supplied by `main()`;
- the resulting list is printed and counted by `main()`;
- `self_test()` now calls that callable.

I then ran the old inline checker and new callable-backed CLI against the same independently mutated inputs. Every result was identical:

| attack | old | new |
|---|---|---|
| delete V15→V16 §10 row | exit 1, exact `MISSING` | exit 1, same exact `MISSING` |
| corrupt V15→V16 result digest | exit 1, exact `UNPINNED` | exit 1, same exact `UNPINNED` |
| remove V32→V33 normative finding map | exit 1, exact `NO FINDING CITED` naming §2.7 | exit 1, same exact finding |
| remove V33→V34 current sidecar map | exit 1, exact `SIDECAR MISSING` | exit 1, same exact finding |
| add unmapped synthetic V34→V35 | exit 0, no finding | exit 0, no finding |

V34's zero is not branch silence. Independent branch accounting over the pinned bytes found:

- 33 computed transitions total;
- 18 in-band transitions V15→V16 through V32→V33 entered the written-row branch;
- all 18 rows were present;
- all 18 carried the right computed result-digest prefix;
- 16 in-band transitions touched normative sections and all 16 had findings-map entries;
- two in-band transitions were bookkeeping-only under the declared exemption;
- the current V33→V34 transition was present in `FINDINGS_MAP.md`;
- `check_trace()` returned `[]`.

The repaired self-test also produced the exact intended named outcomes: deleting V15→V16 produced `MISSING`; removing V33→V34 produced `SIDECAR MISSING`; and synthetic V34→V35 did not bind V34. The first reverted indentation-corruption attempt left no runtime or syntax residue in the pinned file; both normal and self-test executions completed.

## V34 correction citation adjudication — held for the right reasons

V34 lines 358–363 cite `CODEX-V11 3` and `GPT56-V11 F3`.

- `PREREG_TEXT_V11_CODEX.md:43-51` declares Finding 3 and identifies the exact defect: replaying supplied acceptance labels rather than recomputing exclusion predicates from immutable evidence. V34 lines 350–363 require evidence-bound predicate recomputation and refusal of any status/reason/evidence disagreement.
- `PREREG_TEXT_V11_GPT56.md:25-31` declares F3 and identifies the missing pre-data acceptance-design slot, confidence threshold, schema, code and fixtures. V34 lines 372–377 create BS-2a as that Class-P design slot before BS-6 and leave BS-2f as the value-only realized partition.

The full citation checker accepted the exact pair, and independent content reading confirms both are real and germane. Neither V34 citation depends on the parser's false-positive paths. V34 lint and trace both exit 0 for substantive reasons stated above.

## Required executions

All required invocations were run independently from the assigned gate directory with `PYTHONDONTWRITEBYTECODE=1` where applicable.

- `prereg_lint.py V34 --gates .` — exit 0; 23 §7 rows (15 P, 8 E), 22 BS identifiers; no reported inconsistencies.
- `prereg_lint.py V34 --gates . --self-test` — exit 0; 6 controls, 0 failures. F2 explains why the citation control is not probative.
- `prereg_trace.py .. --check V34` — exit 0; 33 computed transitions, 0 problems.
- `prereg_trace.py .. --check V34 --self-test` — exit 0; baseline clean; three named scope controls, 0 failures.
- `void_registry.py V34` — exit 0; 52 antecedents, 20 rows, digest `bd55490ea4290895996bbb12c1e4c81f8a7076c7220a3f2df68971b52c2a50bb`; five explicitly advisory candidates.
- `void_registry.py V34 --self-test` — exit 0; 6 controls, 0 failures; F3 records the surviving label overclaim.
- `bs2a_quality_gate.py --self-test` — exit 0; 36 controls, all 26 checks exercised, 0 failures.
- `gain_gradient_estimator.py --self-test` — exit 0; five exact recovery fixtures, three old-normalization regressions, all G01–G09 exercised, 0 failures. The deliberate hostile numeric controls emitted the expected NumPy overflow warnings and then the expected refusal codes.
- `verdict_breakpoints.py --self-test` — exit 0; 48 production-transcription points, 10 breakpoints including five p-gate points, T01/T02 fired, 0 failures. F4 bounds what its orphan line proves.

## Failed attacks / what held

- All five subject digest pins held exactly.
- The trace refactor preserved production behavior across baseline, all four finding families, and the future-transition scope case.
- All three trace controls now invoke the production callable and demand their own named result.
- V34's zero has nonzero branch witnesses and complete in-scope closure; it is not explained by a skipped branch.
- The V34 correction's two cited finding 3s are real and materially support the text.
- Numeric version matching correctly refused V1 rather than borrowing V11.
- A generic `## 8. Evidence` heading alone was not parsed as a finding.
- `void_registry`'s actual V05/V06 semantics and its new summary correctly disclaim semantic coverage.
- The exact double-quoted `refuse("T03", ...)` and direct-bracket idioms are both recognized by the current orphan regex union.
- Every required executable and self-test completed with exit 0; the blockers are harness meaning and regression coverage, not red commands.

## Scope, parked decisions, and write custody

I did not re-litigate `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` or `OPEN_QUESTION_T_COMPLETENESS.md`. Nothing in this audit fills a slot, touches BS-6, authorizes data access, or adjudicates either principal decision.

Before writing, targeted `git status --short` over all five subjects and this report path was empty. I did not modify any pinned subject, report under test, findings map, parked-question file, reference artifact, or data. Temporary adversarial fixtures were created only in automatically removed temporary directories/in memory. This report is the sole intended write.

**NOT CLEAR**