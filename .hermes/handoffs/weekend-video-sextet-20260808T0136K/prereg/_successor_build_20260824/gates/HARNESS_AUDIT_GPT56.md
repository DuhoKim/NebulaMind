# HARNESS AUDIT — GPT56

## Verdict

**NOT CLEAR.** V34 itself still certifies honestly under a manual application of the strengthened requirement: its sole correction block cites two real V11 finding 3s, and neither citation depended on the old report-exists-only weakness. However, `check_repair_citations` is still unsound in both directions, its negative control does not exercise the strengthened predicate, the `void_registry` self-test still prints an overclaiming control name, and the breakpoint orphan-source scan recognizes only one of the two required emission idioms.

## Subject identity — all four pins verified

I recomputed SHA-256 over the named bytes before judging them. All four equal the brief pins exactly:

| subject | recomputed sha256 | comparison |
|---|---|---|
| `/Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py` | `5090a694690446ade672bcc8d35e523425bac2660514d7a5ed586524b5a99d48` | exact match |
| `/Users/duhokim/NebulaMind/NebulaMind/tools/void_registry.py` | `b8ef412e3df842068a5105d8f0f72a4e01bacef3aa82f6a11b1e717b60aaa658` | exact match |
| `../ref/verdict_breakpoints.py` | `2fcd43a121ced22a34262dafd3020d90989ea8e36fa240b1589ddd3a2505ed1f` | exact match |
| `../PREREG_SUCCESSOR_DRAFT_V34_20260828.md` | `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` | exact match |

## Findings

### F1 — BLOCKER — the strengthened citation predicate still accepts nonexistent findings and is also narrower than real report headings

`prereg_lint.py:253-255` selects reports with the substring test `f"V{ver}" in p.name`, not a version-token match. Thus a claimed `V2` report can bind `V21_WHOLE_REVIEW_CODEX.md`. `prereg_lint.py:268-269` then accepts any Markdown heading beginning with the number, not specifically a finding heading.

The concrete false acceptance is stronger than a theoretical regex complaint:

- Synthetic `V99 CORRECTION (CODEX-V2 F8)` was **ACCEPTED**.
- There is no selected CODEX V2 report. The checker selected `V21_WHOLE_REVIEW_CODEX.md` because `V2` is a substring of `V21`.
- It then treated `## 8. Testimony / unverified assertions` as finding 8.

The same finding parser is also too strict against a real report shape. `V21_WHOLE_REVIEW_CODEX.md:23,39,57` numbers its findings as `### Finding 1`, `### Finding 2`, and `### Finding 3`. The parser at line 268 does not recognize `Finding` between the hashes and number. Synthetic `CODEX-V21 F1` and `CODEX-V21 F2` nevertheless passed, but for the wrong reason: the body also has ordinary section headings `## 1. Subject identity` and `## 2. Numbered findings`. This is precisely a check passing without proving what its name says.

The requested high-number fabrication does fail: synthetic `GPT56-V11 F97` was rejected with `that report has no finding 97 (it has 1, 2, 3, 4, 5, 6)`. That control is useful but insufficient; low fabricated numbers can collide with ordinary section headings, and short versions can collide with later report filenames.

The built-in negative control does not cover the repair. `_mut_repair_citations()` at `prereg_lint.py:322-324` cites `CODEX-V98 7`, for which no report exists. It therefore exercised the pre-existing report-existence branch before and after the strengthening. The six-control self-test can remain green if the finding-existence predicate is deleted again. A proper control must cite a real report and a nonexistent finding number, and another must exercise each accepted real heading form.

Smallest sufficient repair: token-bound the version in filenames; parse findings only inside the report's numbered-findings surface (or extract explicit finding headings/IDs); support `### Finding 1` in addition to `### 1.` and `### F1`; and add exact negative controls for existing-report/missing-finding, real `Finding N`, and ordinary-numbered-section non-acceptance.

### F2 — HIGH — `verdict_breakpoints` orphan detection does not cover both emission idioms

`verdict_breakpoints.py:271-274` computes emitted codes with only:

```python
re.findall(r"\[\{?(T\d{2})", src)
```

That recognizes direct bracket construction such as `bad.append(f"[T01] ...")`. It does not recognize `refuse("T01", ...)`. I applied the exact pattern to both required idioms: the direct sample returned `T01`; the `refuse("T01", ...)` sample returned no code.

For the pinned file's present bytes, the result is incidentally correct: T01 and T02 are both emitted by direct bracket appends, T03 is absent from `CODES`, and the self-test reports no current orphan. But the self-test's source parser does not satisfy the brief's two-idiom requirement and will produce a false orphan when a legitimate `refuse()` emission is introduced. The repair should extract the union of direct bracket codes and literal first arguments to `refuse()`, preferably via AST rather than another source regex, and should carry a synthetic control for each idiom.

### F3 — MEDIUM — the `void_registry` public code names are honest, but its self-test control name still says “coverage”

The actual V05/V06 refusal descriptions at `void_registry.py:84-88`, predicate messages at lines 192-197, and module limits at lines 21-39 are honestly narrowed to **naming**. They do not claim semantic antecedent coverage, and the advisory heuristic explicitly denies completeness. That part of the rename is sound and does not re-litigate the principal's parked completeness decision.

But the visible control tuple at `void_registry.py:231-236` still names `_mut_drop_row` as `"row loses coverage"`; `_mut_drop_row`'s docstring at lines 203-205 says the same. The executed self-test printed `OK row loses coverage: ['V05']`, even though V05 proves only that no antecedent ID names the row. This is the same NAME-over-PREDICATE residue under audit. Rename the control/output to `row loses naming antecedent` (and preferably internal `covered` to `named`) so every reader-facing surface preserves the narrowed claim.

## V34 correction adjudication

V34 contains one `V## CORRECTION` block, at lines 358-363:

- `CODEX-V11 3` exists. `PREREG_TEXT_V11_CODEX.md:43` is `### 3. BLOCKING — §2.7 closes the reason vocabulary but not the truth of a reason`.
- `GPT56-V11 F3` exists. `PREREG_TEXT_V11_GPT56.md:25` is `### F3 — BLOCKER — §2.7 fixes the conceptual exclusion rule but leaves its pre-data design gate and confidence threshold unbound`.

The V34 correction text addresses the common substance: it requires evidence-backed predicate recomputation and refusal of status/reason/evidence disagreement, then separately creates and locates the pre-data acceptance-design slot. Therefore:

- **Does V34 still certify honestly under the strengthened requirement? Yes.**
- **Did any V34 correction claim pass only because the old check checked report existence? No.** Both cited finding numbers are real and substantively germane.

This document-level answer does not rescue the generic harness, whose false positives are demonstrated in F1.

## Six-harness sweep

I inspected the claim/control surfaces of all six named harnesses:

1. `prereg_lint.py` — F1; normal and self-test executions otherwise clean.
2. `prereg_trace.py` — no additional name/predicate overclaim found; its check and three-rule self-test both passed on V34.
3. `void_registry.py` — narrowed refusal semantics are honest; reader-facing control-label residue is F3.
4. `bs2a_quality_gate.py` — no additional instance found. Its refusal identities are explicit E01-E26, controls compare exact code sets, and `uncontrolled()` computes code/control closure. The authenticated-fixture self-test exercised all 26 codes with 36 controls.
5. `gain_gradient_estimator.py` — no additional instance found. Its claims are explicitly bounded, exact recovery and regression controls ran, and all G01-G09 codes were exercised. NumPy emitted expected overflow warnings during hostile numeric controls, but the controls converted those cases to the expected refusal codes and the process exited 0.
6. `verdict_breakpoints.py` — current T01/T02 runtime surface is honest, but the source-level two-idiom orphan claim fails as F2.

I did not revisit either `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` or `OPEN_QUESTION_T_COMPLETENESS.md`.

## Commands run and observed results

All Python invocations used `PYTHONDONTWRITEBYTECODE=1`.

- `shasum -a 256 <four subjects>` — four exact pin matches.
- `python3 tools/prereg_lint.py V34 --gates .` — exit 0; 23 §7 rows (15 P, 8 E), 22 BS identifiers; no inconsistencies; six checks claimed controlled.
- Same with `--self-test` — six controls, zero failures.
- `python3 tools/prereg_trace.py .. --check V34` — 33 computed transitions, zero problems.
- Same with `--self-test` — three scope rules, zero failures.
- `python3 tools/void_registry.py V34` — exit 0; 52 antecedents, 20 defined §6.1 rows; five explicitly advisory heuristic candidates.
- Same with `--self-test` — six controls, zero failures.
- `python3 ../ref/verdict_breakpoints.py --self-test` — 48 production-transcription points, 10 breakpoints, refusal controls clean, zero failures.
- `python3 ../ref/gain_gradient_estimator.py --self-test` — all recovery/regression/refusal controls clean; 9/9 codes exercised; zero failures.
- `python3 ../ref/bs2a_quality_gate.py --self-test` — authenticated receipt clean; 36 controls; 26/26 checks exercised; zero failures.
- Direct `check_repair_citations` probes — V34 clean; `GPT56-V11 F97` and `CODEX-V11 F97` rejected with their real numbered sets; `CODEX-V21 F1`, `CODEX-V21 F2`, `CODEX-V2 F1`, and `CODEX-V2 F8` accepted, establishing the wrong-heading and version-substring defects.
- Exact orphan regex probes — direct bracket sample recognized; `refuse("T01", ...)` sample not recognized.

## Failed attacks / what held

- All four digest pins held.
- V34's two cited findings both existed and matched the claimed correction; the old weakness did not affect V34's correction block.
- High fabricated finding 97 was rejected and reported the real finding numbers.
- `void_registry`'s actual V05/V06 refusal text and module-level semantic limits held; only the public control label remained overstated.
- No fourth overclaim was found in `prereg_trace`, `bs2a_quality_gate`, or `gain_gradient_estimator`.
- Every named executable/self-test completed with exit 0; the blocker is test meaning, not a red command.

## Write-scope note

Before writing this report, targeted `git status --short` over the report and four subjects was empty. I made no edits to the pinned subjects or parked-question files. The only intended audit write is this report.

**NOT CLEAR**