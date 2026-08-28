# HARNESS AUDIT — CODEX

## Verdict

**NOT CLEAR.** The exact V34 correction citations are real and V34 exits clean under the strengthened linter: both `CODEX-V11 3` and `GPT56-V11 F3` resolve to actual finding 3s, so neither V34 correction citation was passing only because the old report-existence predicate was weak. The fabricated `GPT56-V11 F97` is also rejected and reports the real finding numbers 1–6. However, the repair is not a sound finding-existence check: it accepts unrelated numbered section headings as findings, uses a substring version match that lets a nonexistent V1 borrow V11 reports, and rejects real list-form findings. Two other claimed harness repairs also remain name/predicate mismatches: `prereg_trace.self_test()` does not run the checker under its three mutations, and the verdict orphan scan recognizes only literal bracket emissions, not `refuse("T##", ...)`. The void-registry public contract is honestly narrowed to NAME-completeness, but its self-test still prints the old overclaiming word “coverage.”

## Exact subject identities

All four supplied SHA-256 pins were recomputed from the live bytes before adjudication; all four compare **MATCH** by exact 64-hex equality:

| subject | supplied | recomputed | comparison |
|---|---|---|---|
| `/Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py` | `5090a694690446ade672bcc8d35e523425bac2660514d7a5ed586524b5a99d48` | `5090a694690446ade672bcc8d35e523425bac2660514d7a5ed586524b5a99d48` | MATCH |
| `/Users/duhokim/NebulaMind/NebulaMind/tools/void_registry.py` | `b8ef412e3df842068a5105d8f0f72a4e01bacef3aa82f6a11b1e717b60aaa658` | `b8ef412e3df842068a5105d8f0f72a4e01bacef3aa82f6a11b1e717b60aaa658` | MATCH |
| `../ref/verdict_breakpoints.py` | `2fcd43a121ced22a34262dafd3020d90989ea8e36fa240b1589ddd3a2505ed1f` | `2fcd43a121ced22a34262dafd3020d90989ea8e36fa240b1589ddd3a2505ed1f` | MATCH |
| `../PREREG_SUCCESSOR_DRAFT_V34_20260828.md` | `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` | `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` | MATCH |

For the six-harness sweep, the additionally inspected live scripts recomputed as: `prereg_trace.py` `b4fab3158d413fe1d4680c078c6cfbd971fd0c5f2a92dedbbef936f045e7bd2b`; `bs2a_quality_gate.py` `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`; `gain_gradient_estimator.py` `e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd`.

## Findings

### 1. HIGH — `check_repair_citations` still does not establish that the cited finding exists

The strengthened predicate at `prereg_lint.py:253-269` has three independent counterexamples.

1. **Unrelated numbered headings certify nonexistent findings.** The accepted-heading regex is `^#+\s*F?N\b`; it treats every numeric Markdown heading as a finding. `V21_WHOLE_REVIEW_CODEX.md` has actual findings written as `### Finding 1`, `### Finding 2`, and `### Finding 3` at lines 23, 39, and 57, which that regex does not parse. The same report also has ordinary numbered section headings. Direct calls to the shipped function produced:
   - `CODEX-V21 F1` — ACCEPTED;
   - `CODEX-V21 F4` — ACCEPTED;
   - `CODEX-V21 F7` — ACCEPTED;
   - `CODEX-V21 F8` — ACCEPTED.

   The report has only three actual findings. Thus at least F4/F7/F8 are fabricated citations accepted by the strengthened check. F1 happens to be real but is accepted for the wrong predicate witness.

2. **Version lookup is substring-based.** The hit rule uses `f"V{ver}" in p.name`, without a version boundary. A direct test of nonexistent `GPT56-V1 F3` was ACCEPTED by borrowing V11-family report files. This is the old envelope weakness in a narrower form: the check can still find the number in the wrong report version.

3. **Real report syntax is rejected.** `PREREG_TEXT_V12_CODEX.md` has four real findings as top-level numbered-list items (`1. **BLOCKING ...**` through `4. ...` at lines 7, 15, 23, 31). Directly citing real `CODEX-V12 F1` was rejected as “no finding 1 and no parseable numbered findings.” The gate corpus contains many other list-form findings and `### Finding N` headings. The strengthened pattern remains narrower than the data.

The explicit-ID alternative does not repair these cases: it searches for `SEAT-Vn-N` anywhere in the report, not in a finding declaration, so any incidental mention can also satisfy it.

**Smallest sufficient repair:** parse only declared finding blocks, but support the actual declaration grammar: `### N.`, `### FN`, `### Finding N`, and numbered-list finding items under a findings section. Match the report version with a numeric boundary or extract it structurally from the filename. Do not count generic numbered section headings. Add positive controls for every real declaration shape and negative controls for (a) a generic `## 8. Evidence` section, (b) V1 versus V11, and (c) incidental in-body `SEAT-Vn-N` text.

### 2. HIGH — `prereg_trace.self_test()` names behavioral negative controls but does not exercise the checker

`prereg_trace.py:223-290` says it will “Assert each scope rule can fail.” Its three predicates do not do that:

- “in-band presence” removes a row only from a local `table` list and checks `len(stripped) < len(table)` (`:241-248`). It never feeds the stripped table to the production `--check` logic and never verifies that `MISSING` or a nonzero result is produced.
- “sidecar” does not remove or corrupt a mapping; it only checks that the current mapping already exists (`:253-263`).
- “out-of-scope” constructs a future draft and proves that `build(tmp)` sees it (`:265-285`). It never runs the subject checker against that future draft and never proves the unchanged subject remains clean.

The command therefore printed `3 scope rules, 0 failure(s)`, but those predicates prove only that test fixtures can be constructed, not that the named checker behavior fires or stays quiet. This is the same NAME-asserts-more-than-PREDICATE shape the audit was meant to eliminate, and it was missed among the six harnesses.

**Smallest sufficient repair:** factor the production check into a callable returning findings/status, then have each self-test mutate copied inputs and invoke that exact callable. Assert the exact expected finding for the missing in-band row and missing sidecar mapping, and assert zero new findings for the synthetic future draft.

### 3. HIGH — the verdict orphan check does not hold across both emission idioms required by the brief

`verdict_breakpoints.py:271-274` discovers emissions with only:

`re.findall(r"\[\{?(T\d{2})", src)`

Independent application of that exact regex returned:

- `bad.append("[T03] direct")` → `T03` found;
- `refuse("T03", "via helper")` → nothing found;
- `bad.append(f"[{code}] variable")` → nothing found.

The present T01/T02 happen to be literal bracket strings, so the current declared set has no orphan. But a legitimate helper emission would be falsely called orphaned, contrary to the assigned both-idiom attack and the comment that every declared code must be “emittable by some runtime path.” The current self-test passing does not establish that broader claim.

**Smallest sufficient repair:** use the AST to collect literal code arguments to `refuse(...)` plus literal bracket-code strings, or centralize all emissions through one helper and inspect/test that call surface. Add one synthetic emitted code in each idiom and one genuinely orphaned code.

### 4. LOW — void-registry semantics are honestly narrowed, but the rename is incomplete in its own control output

The substantive repair holds. `void_registry.py:21-31` explicitly defines NAME-completeness and disclaims semantic coverage; CODES V05/V06 at `:84-88` say “names”; and the predicates at `:192-197` test only the `VOID-6.1<ROW>-` ID prefix. That is an honest, smaller claim and does not re-litigate semantic completeness.

However, `_mut_drop_row` still says “its §6.1 row loses coverage” and the control is named `row loses coverage` (`:203-205`, `:231-233`). The shipped self-test consequently prints `OK row loses coverage`, even though the module now correctly says coverage is not computable. The internal variable remains `covered`. This is a residual user-facing overclaim, albeit not a predicate defect in V05/V06 themselves.

**Smallest sufficient repair:** rename the mutator docstring/control/output and internal set to “named,” e.g. `row is no longer named` / `named_rows`.

## V34 correction adjudication

V34 contains one correction block at lines 358-363 with two citations:

- `CODEX-V11 3` resolves to `PREREG_TEXT_V11_CODEX.md:43`, `### 3. BLOCKING — §2.7 closes the reason vocabulary but not the truth of a reason`. Lines 45-51 state the operator-label replay defect and prescribe recomputing every predicate from immutable evidence.
- `GPT56-V11 F3` resolves to `PREREG_TEXT_V11_GPT56.md:25`, `### F3 — BLOCKER ...`, with the acceptance-design, evidence, and confidence-threshold gap and its pre-BS-6 repair at lines 27-31.

V34 lines 350-375 contain the corresponding evidence-bound recomputation and class-P acceptance-design requirements. Therefore:

- **Does V34 exit clean under the strengthened check?** Yes: exit 0.
- **Are its cited findings real?** Yes, both finding 3s are real and materially support the correction.
- **Did either V34 correction citation pass only under the old weak check?** No. The old report-existence predicate and the strengthened number predicate both succeed for these exact two citations, and independent content reading confirms them.
- **Is the strengthened harness therefore trustworthy for other citations?** No; Finding 1 gives both false accepts and false rejects.

## Required executions

All named checks and every self-test in the six inspected harnesses were run from the assigned gate directory with `PYTHONDONTWRITEBYTECODE=1`:

- `prereg_lint.py V34 --gates .` — exit 0; 23 §7 rows (15 P, 8 E), 22 BS identifiers; no inconsistencies.
- `prereg_lint.py V34 --gates . --self-test` — exit 0; 6 controls, 0 failures.
- `prereg_trace.py .. --check V34` — exit 0; 33 computed transitions, 0 problems.
- `prereg_trace.py .. --check V34 --self-test` — exit 0; 3 reported scope controls, 0 failures; Finding 2 explains why this is not probative.
- `void_registry.py V34` — exit 0; 52 antecedents, 20 defined rows, digest `bd55490ea4290895996bbb12c1e4c81f8a7076c7220a3f2df68971b52c2a50bb`; five explicitly advisory compound candidates.
- `void_registry.py V34 --self-test` — exit 0; 6 controls, 0 failures.
- `verdict_breakpoints.py --self-test` — exit 0; 48 transcription points, 10 breakpoints including 5 p-gate points, T01/T02 fired, reported 0 failures; Finding 3 bounds what the orphan line proves.
- `bs2a_quality_gate.py --self-test` — exit 0; 36 controls, all 26 checks exercised, 0 failures.
- `gain_gradient_estimator.py --self-test` — exit 0; five recovery fixtures, three old-normalization regressions, all G01-G09 codes exercised, 0 failures. Expected deliberate overflow warnings occurred in the denormal/overflow controls.
- Direct citation attacks: V34 baseline clean; `GPT56-V11 F97` rejected with real numbers `1, 2, 3, 4, 5, 6`; `CODEX-V12 F1` falsely rejected; `CODEX-V21 F4/F7/F8` falsely accepted; `GPT56-V1 F3` falsely accepted.

## Failed attacks / what held

- All four pinned subject identities held exactly.
- The exact V34 correction citations survived independent report-content verification; no correction claim depended on the old weakness.
- The fabricated V11 F97 attack was correctly rejected and the diagnostic truthfully named 1–6.
- V11's `### F3 — BLOCKER` shape is now accepted; the first-attempt `### 3.`-only false negative is repaired for that specific shape.
- The void-registry V05/V06 predicate and public CODES now make only the NAME-completeness claim they can establish.
- Current verdict codes T01/T02 are both directly emitted and exercised; T03 is absent from the declared surface.
- The bs2a and gain-gradient self-tests showed no additional name/predicate mismatch in their declared refusal-code coverage during this bounded audit.

## Scope and parked decisions

I did not re-litigate `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` or `OPEN_QUESTION_T_COMPLETENESS.md`. Nothing here fills a slot, touches BS-6, authorizes data access, or adjudicates either principal decision. I inspected only the four pinned subjects, the other two harnesses needed for the six-harness sweep, V34's cited V11 reports, and report syntax needed to attack the citation parser. No source artifact was modified; this report is the sole intended write.

**NOT CLEAR**