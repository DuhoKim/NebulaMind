# HARNESS AUDIT R2 — GPT56

## Verdict

**NOT CLEAR.** The `prereg_trace.check_trace()` refactor itself holds: comparison with its immediate parent shows that only reporting/callability changed, every production predicate remains equivalent, every trace branch was independently forced, and V34's zero-problem result is supported by 18 present-and-pinned in-band rows, 16/16 mapped normative transitions, and the mapped V33→V34 sidecar. All five subject digests match their pins and all six required self-tests exit 0. The gate still fails because the rebuilt citation parser is unsound in both directions on one mixed-grammar report: it accepted a numbered test-protocol item as finding 2 while failing to recognize the actual bare-heading finding 1. Its own self-test remains unable to catch deletion of the finding parser. A smaller residue also remains in `void_registry`: the old reader-facing control label “row loses coverage” is still present and still printed.

## Subject identity — all five pins verified

I recomputed SHA-256 over the exact live bytes before adjudication. Every comparison is exact 64-hex equality:

| subject | brief pin | recomputed | comparison |
|---|---|---|---|
| `tools/prereg_lint.py` | `522356f1b1d82894b97cd17d98026eb6488c99f6f382e27324777236f9cf4f38` | `522356f1b1d82894b97cd17d98026eb6488c99f6f382e27324777236f9cf4f38` | MATCH |
| `tools/prereg_trace.py` | `9bd194b96a4feeb22e85d07b2a2860a11f6c37bfeeebc3fa891bf55d3f877ae8` | `9bd194b96a4feeb22e85d07b2a2860a11f6c37bfeeebc3fa891bf55d3f877ae8` | MATCH |
| `tools/void_registry.py` | `f494e5b858a4518bf9299023603e5e82e87eca2bca18a02317ce07790976f1a4` | `f494e5b858a4518bf9299023603e5e82e87eca2bca18a02317ce07790976f1a4` | MATCH |
| `../ref/verdict_breakpoints.py` | `5ed290a61d54a771ff2a346abe867725e40a5373ff37fbbca4a6f4f9a25af93b` | `5ed290a61d54a771ff2a346abe867725e40a5373ff37fbbca4a6f4f9a25af93b` | MATCH |
| `../PREREG_SUCCESSOR_DRAFT_V34_20260828.md` | `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` | `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` | MATCH |

## Findings

### F1 — HIGH — the four-grammar citation parser is too permissive and, when grammars are mixed, still narrower than the data

The required constructed report was:

```markdown
# Synthetic audit

## Findings

### 1. HIGH — a real finding
Evidence.

2. **Test protocol (not a finding).** This is only a numbered method item.
```

I saved that as the only `PREREG_TEXT_V99_GPT56.md` in an isolated temporary gates directory and ran the full public `check_repair_citations()` path on `V99 CORRECTION (GPT56-V99 F2)`. The result was **ACCEPTED**. Direct `_declared_findings()` returned `{2}`: it certified the non-finding protocol item and omitted the actual finding 1.

This is caused by the interaction of two predicates in `prereg_lint.py:301-339`:

- Lines 305-317 set `in_findings` from any heading containing “finding” and accept every subsequent top-level `N. **…**` item while that flag remains true. There is no declaration-vs-method distinction, so a numbered protocol/checklist/failed-attack item under that heading becomes a finding.
- Lines 324-338 parse bare `### N.` headings only under `if not found`. Once the non-finding list item has put `2` in `found`, the fallback that could recognize the real `### 1.` never runs. The four accepted grammars are therefore alternatives for an entire report, not composable declaration forms.

A second constructed body proved the section-boundary defect: `## Findings; ### 1. real; ## Evidence appendix; ### 2. numbered evidence item` produced `{1, 2}`. The fallback anchors once and scans to end at the first numeric-heading depth; it does not stop when the findings section closes. This is the fifth narrower-than-data shape: fixing the earlier truncation by scanning to end changed a false negative into an unbounded false-positive surface.

The four isolated positive shapes do individually work (`### F3`, `### Finding 3`, bare `### 3.` under a findings section, and `3. **…**` each returned `{3}`), and the V1/V11 numeric-boundary attack now correctly reported no V1 report. Those held controls do not rescue mixed reports.

Smallest sufficient repair: parse a bounded findings section structurally, permit all four declaration forms within that bounded section in one pass, and stop at the section's closing heading depth. Do not treat arbitrary numbered bold list items as declarations merely because they occur under a findings heading; require a declaration-specific form or a structurally isolated finding list. Add the exact mixed report above and the post-section numbered heading as negative controls.

### F2 — HIGH — the linter self-test remains green when finding parsing is deleted

`_mut_repair_citations()` at `prereg_lint.py:386-388` still cites `CODEX-V98 7`, for which no report exists. It therefore exercises only the report-existence branch at lines 253-257, before `_declared_findings()` is called. It does not test the predicate repaired in this round.

I monkeypatched `_declared_findings` to always return `set()` and ran the shipped `self_test()` on V34. It returned **0** and printed all six controls `OK`, including `check_repair_citations: control fires`. Thus the declaration parser can be removed entirely while the harness still claims that check demonstrated it can fail. This is the same surviving sub-defect identified in round 1: the control's name covers more than its predicate reaches.

Smallest sufficient repair: make the repair-citation control cite an existing exact-version report and a nonexistent finding, then add positive controls for every supported grammar and the mixed-grammar/ordinary-numbered-item negatives from F1. The missing-report branch needs its own separately named control if it is also claimed covered.

### F3 — LOW — `void_registry` still prints the old overclaiming control label

The substantive output repair holds: `void_registry.py:266-268` now explicitly says “control coverage, NOT semantic coverage of §6.1's forbidden columns” and accurately explains that V05/V06 match a naming convention.

But the exact round-1 residue remains unchanged:

- `_mut_drop_row` still says “its §6.1 row loses coverage” at lines 203-205;
- `CONTROLS` still names it `row loses coverage` at line 232;
- the required self-test still printed `OK row loses coverage: ['V05']`.

V05 proves only that no antecedent ID **names** the row. The later disclaimer narrows the aggregate claim but does not make this individual reader-facing control label true. Rename it to “row loses naming antecedent” (and preferably `covered`/`coverage` internals to `named`/`naming`) so every emitted surface agrees with the predicate.

## `check_trace()` refactor adjudication — held

I compared commit `03c686b85` against its immediate parent, the round-1 implementation with the check inline in `main()`. In the moved production body:

- both loop bounds and every branch predicate are unchanged;
- `DRAFT.search(Path(args.check).name)` became `DRAFT.search(subject_name)`, while `main()` passes exactly `Path(args.check).name`;
- each `print(...)` plus `bad += 1` became `out.append(...)`;
- final `bad` became `len(out)` after `main()` prints each returned finding.

No threshold, comparison operator, exemption, table lookup, digest-width check, normative-section extraction, sidecar test, or mapping predicate changed. The first corrupted-indentation attempt left no residue in the pinned bytes; `py_compile` succeeded for all six harness scripts.

I then exercised the callable independently rather than relying on the shipped self-test:

- baseline: `check_trace(...) == []`;
- 33 computed transitions; V34 contains 32 §10 transition rows because its current V33→V34 transition is sidecar-owned;
- all 18 in-band transitions V15→V16 through V32→V33 were found in the §10 table and carried the computed result digest;
- all 16 in-band transitions that touched a non-bookkeeping normative section had a findings-map entry;
- current V33→V34 had its sidecar mapping;
- deleting the exact V15→V16 table row returned exactly `MISSING: no §10 table row for V15 → V16`;
- corrupting that row's result digest returned exactly `UNPINNED: V15 → V16 row does not carry its result digest`;
- deleting V33→V34's sidecar entry returned exactly `SIDECAR MISSING: V33 → V34 ...`;
- deleting the normative V15→V16 finding map returned exactly `NO FINDING CITED: V15 → V16 changed §6.1, §6.2, §2.7, §6.3 ...`;
- appending synthetic normative V34→V35 with no mapping returned `[]`, proving the post-subject branch is actually excluded.

Therefore V34's `33 computed transition(s); 0 problem(s)` is zero for the right reasons, not because an in-band, digest, normative-map, current-sidecar, or future-scope branch stopped running. The shipped three controls also produced the intended exact outcomes: MISSING for deleted V15→V16, SIDECAR MISSING for removed V33→V34, and no V34→V35 finding for the unchanged subject.

## Other repaired surfaces — held

- The verdict orphan extractor now unions the literal bracket idiom with literal `refuse("T##", ...)`; direct isolated probes recognized each idiom, and an absent code remained absent. Current T01/T02 both have real bracket emissions, and the self-test reported no orphan.
- Exact version matching held: with only a V11 report present, a V1 citation was rejected as having no V1 report.
- V34's current correction citations remained clean. `PREREG_TEXT_V11_CODEX.md` parsed finding 3 and `PREREG_TEXT_V11_GPT56.md` parsed F3; the full V34 citation check returned no finding. This confirms the document did not depend on the old envelope-only weakness.
- `bs2a_quality_gate` and `gain_gradient_estimator` self-tests exposed all their claimed refusal-code controls and returned zero failures in this bounded rerun. The estimator's deliberate hostile numeric cases emitted expected NumPy overflow warnings before producing the required refusal codes.

## Required executions

All required invocations were run from the assigned absolute gate directory. Test invocations used `PYTHONDONTWRITEBYTECODE=1` except the separate `py_compile` syntax check.

- `prereg_lint.py ...V34... --gates .` — exit 0; 23 §7 rows (15 P, 8 E), 22 BS identifiers, no inconsistencies.
- `prereg_lint.py ...V34... --gates . --self-test` — exit 0; 6 controls, 0 failures. F2 shows why the citation control is not probative.
- `prereg_trace.py .. --check ...V34...` — exit 0; 33 transitions, 0 problems.
- `prereg_trace.py .. --check ...V34... --self-test` — exit 0; clean baseline and 3 scope rules, 0 failures.
- `void_registry.py ...V34...` — exit 0; 52 antecedents, 20 defined rows, digest `bd55490ea4290895996bbb12c1e4c81f8a7076c7220a3f2df68971b52c2a50bb`, five explicitly advisory candidates.
- `void_registry.py ...V34... --self-test` — exit 0; 6 controls, 0 failures; it printed the stale label in F3.
- `bs2a_quality_gate.py --self-test` — exit 0; 36 controls, all 26 checks exercised, 0 failures.
- `gain_gradient_estimator.py --self-test` — exit 0; five recovery fixtures, three normalization regressions, 9/9 codes exercised, 0 failures.
- `verdict_breakpoints.py --self-test` — exit 0; 48 production-transcription points, 10 breakpoints including five p-gate points, T01/T02 controls, no orphan, 0 failures.
- `python3 -m py_compile` over all six scripts — exit 0.

## Failed attacks / what held

- All five pinned identities matched exactly.
- The trace refactor did not alter a production predicate; all reporting-equivalent branches were forced and returned their exact named finding.
- V34's zero trace count survived independent row, digest, normative-map, sidecar, and out-of-scope accounting.
- Each of the four citation declaration grammars worked in isolation.
- The numeric version boundary rejected V1 borrowing V11.
- V34's two actual V11 finding-3 citations remain real and germane; no correction claim relied on the old weak parser.
- The verdict orphan scanner recognized both stated literal idioms under direct probes.
- Every required self-test and syntax check exited 0.

## Scope, parked decisions, and write custody

I did not read or adjudicate the contents of `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` or `OPEN_QUESTION_T_COMPLETENESS.md`; neither parked principal decision is re-litigated here. Nothing in this report fills a slot, touches BS-6, authorizes execution, or changes V34. No pinned subject was edited. Temporary citation attacks used isolated temporary directories and left no gate artifact. This report is the sole intended repository write from this audit.

**NOT CLEAR**