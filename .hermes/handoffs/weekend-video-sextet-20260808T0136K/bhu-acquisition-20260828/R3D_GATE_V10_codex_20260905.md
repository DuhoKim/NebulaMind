ACCESS_SHA=a441c7c97213df66dc7f80ca346e398eff0ad8afcd492069b440410ea9b4f3eb
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES

Defect 1 — the scientific classes are mutually exclusive on their stated discriminators, but the terminal classes are not exhaustive as defined. A readable pinned file whose computed digest differs from the manifest is expressly routed by C1 to `DYM_SOURCE_BLOCKED`, while class 6 defines that class only as unreadability. This is a real result fitting none of the seven class definitions: all files are readable, one digest mismatches, no evidence is unread or unresolved, and no control has yet failed twice; it satisfies neither class 6 nor class 7 and cannot support a scientific class. An inconclusive result is otherwise genuinely reachable through unread/unresolved evidence (class 6) and persistent control failure (class 7).

Verbatim: “**DYM_SOURCE_BLOCKED** — a pinned source the branch needs cannot be read.”

Exact replacement: “**DYM_SOURCE_BLOCKED** — a required pinned source cannot be read, its computed identity does not match the frozen manifest, a required source-dependent proposition is unresolved, or a required bounded procedure is undecidable after its specified fallback. The study waits; this is not a scientific verdict and must never be reported as one.”

With that repair, classes 1, 2, 4 and 5 are separated by (i) whether a printed binding relation exists, (ii) whether a completion-free positive floor follows, (iii) whether any admissible completion differs, and (iv) whether the printed relations or any admissible completion permit approach to zero; class 4's precedence removes its potential overlap with class 2. Class 3 covers the no-binding-relation limb.

2. CONTROLS

Defect 2 — C0 can be passed by assertion in this document. It declares `C0_REACHABILITY=PASS`, but the required exhibition table is not printed here; moreover, §8b records the prior exhibition as FAIL and says a fresh PASS is still required. The asserted PASS is therefore unsupported and contradicted by the document's own live state.

Verbatim: “The exhibition table is the artefact. **The exhibitions are authored by a seat and only verified by Tori** — deciding what counts as reachable is where an author's prior would enter, so the author does not decide it. `C0_REACHABILITY=PASS`.”

Exact replacement: “The exhibition table is the artefact. **The exhibitions are authored by an independent seat and only verified by Tori** — deciding what counts as reachable is where an author's prior would enter, so the lane author does not decide it. A claimed pass without the complete table and Tori's printed verification fails. Record exactly one of `C0_REACHABILITY=PASS`, `C0_REACHABILITY=FAIL`, or `C0_REACHABILITY=NOT_RUN`; this version remains `C0_REACHABILITY=NOT_RUN` until the fresh exhibition is attached.”

Defect 3 — C0–C5b do not each define exact PASS/FAIL/NOT_RUN codes. Most bullets print only a PASS token; C1 even routes mismatch straight to a class without requiring its own FAIL status. The global unreached rule does require `NOT_RUN`, but it does not supply each control's exact full code, and reached failures are not uniformly named. This prevents the requested mechanical three-state accounting.

Verbatim: “**Unreached limbs**: controls recorded `NOT_RUN`, never as passes. **This exact underscore spelling applies to every unreached control throughout this document.**”

Exact replacement: “**Control status vocabulary:** every control records exactly one of the following fully spelled tokens: `C0_REACHABILITY=PASS|FAIL|NOT_RUN`, `C1_SOURCE_IDENTITY=PASS|FAIL|NOT_RUN`, `C2_COMPLETION_LEDGER=PASS|FAIL|NOT_RUN`, `C3_DELETION_PROBE=PASS|FAIL|NOT_RUN`, `C4_GR_BENCHMARK=PASS|FAIL|NOT_RUN`, `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN`, `C5B_PATH_LIST=PASS|FAIL|NOT_RUN`, and `C6_BREAKER_TEST=PASS|FAIL|NOT_RUN`. Any reached control that does not satisfy its pass criterion records `FAIL`; every unreached control records `NOT_RUN`, never `PASS`.”

The artefact-bearing controls C1–C5b cannot otherwise be passed by mere assertion: C1, C2, C3, C4 and C5b explicitly require printed artefacts, while C5 requires execution and printed output. Unreached controls are handled by §9. The three literal C5 commands are executable as written: `python3 --version`, `python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 $(command -v python3)`.

3. CIRCULARITY

Sound. The lane pattern is expressly barred from census inclusion, exclusion and class selection; every nonblank source line receives a disposition, every displayed equation gets its own row, exclusion is restricted to four predeclared codes with source evidence, unresolved disagreements block, and C2 prints the complete ledger. A contrary relation cannot be quietly omitted without breaking line reconciliation/equation accounting, though an exposed exclusion can still be challenged. C3 separately executes the deletion probe. No replacement.

4. THE FALSIFIER

C6 can return FAIL on **3** of the 7 declared outcome classes: `DYM_FLOOR_DERIVED`, `DYM_FLOOR_UNDERDETERMINED`, and `DYM_FLOOR_COMPLETION_DEPENDENT`.

- Condition 1: PASS is possible with a filed point floor of `1 kg`. FAIL is not possible on any valid path: a dimensionless input such as `M/m_P = 1` would fail the dimensional test, but it is not a positive floor of an allowed mass set and therefore cannot validly enter any of the three C6-reached classes.
- Condition 2: PASS is possible for `M_min = sqrt(ħc/G)`, with every constant terminating in §2b. FAIL is possible for `M_min = α sqrt(ħc/G)` where `α` is introduced by an admissible completion and has no manifest or §2b terminus.
- Condition 3: PASS is possible for `M_min = sqrt(ħc/G)`, whose substituted expression has no non-§2b free symbol. FAIL is possible for `M_min = λ sqrt(ħc/G)`, whose free-symbol set contains `λ`.
- Condition 4: PASS is possible when the floor contains no held-by-choice quantity (again `sqrt(ħc/G)`). FAIL is possible for `M_min = f(ρ_0)` with `ρ_0` held constant but no manifest passage deriving its fixity.
- Condition 5: PASS is possible for the point interval `[1.0e15, 1.0e15] kg`, which overlaps none of the three finite comparator intervals. FAIL is possible for `[2.176434e-8, 2.176434e-8] kg`, which overlaps the Planck-remnant comparator.

Thus condition 1 is the condition that cannot fail on any valid path. The V10 repair merely makes malformed filing fail; it does not make that malformed filing a member of a declared positive-floor class.

Defect 4 — C0's all-five-reachable claim is false, so the preregistration cannot freeze under its own rule.

Verbatim: “**after (V10)** | **3 paths** — `DYM_FLOOR_DERIVED`, `DYM_FLOOR_UNDERDETERMINED`, `DYM_FLOOR_COMPLETION_DEPENDENT`, i.e. every outcome that yields a positive floor | **5 of 5**”

Exact replacement: “**after (V10)** | **3 paths** — `DYM_FLOOR_DERIVED`, `DYM_FLOOR_UNDERDETERMINED`, `DYM_FLOOR_COMPLETION_DEPENDENT`, i.e. every outcome that yields a positive floor | **4 of 5 can FAIL** — condition 1 is entailed by valid membership in every C6-reached class and is retained as a filing-integrity check, not claimed as a reachable substantive failure.”

Defect 5 — C0 incorrectly requires reachability of a logically entailed integrity condition and therefore makes a sound freeze impossible unless invalid class filing is treated as a scientific input.

Verbatim: “For **every declared outcome class of §4**, and for **every C6 breaker condition whose failure would refute this lane's own expectation**, **exhibit a concrete input that produces it**”

Exact replacement: “For **every declared outcome class of §4**, exhibit a concrete valid input that produces it. For every C6 breaker condition, exhibit concrete valid inputs producing PASS and FAIL, except that a condition logically entailed by the entry criteria of every class on which C6 runs is instead marked `ENTAILED`; prove the entailment and exhibit a malformed filing that the condition rejects as an integrity check. An `ENTAILED` condition is not counted as a reachable substantive FAIL.”

5. RE-RUN GUARD

Sound. §6 expressly forbids assuming K6 repeats, and classes 1 and 5 plus C6 permit a positive floor and a pattern-breaking PASS. No replacement.

6. FAIRNESS

Sound. The operative negative claims use “unreproduced from the stated inputs”: limb A and class 3 use it directly, and the inconsistent-relations branch of class 4 does too. The zero-approach branch reports a reproduced permitted family rather than branding the source an error. No replacement.

7. STALL

Defective as frozen. The readable-digest-mismatch case in finding 1 has no class matching its facts, and C0 is presently unsupported while the document simultaneously asserts PASS; therefore the run can lack a valid fileable class/status. Apply replacements 1–3. Once source identity failure is included in class 6 and every control has an exact three-state token, the timeout fallbacks and seat-split rule otherwise provide terminal routing.

R3D_V10_GATE_COMPLETE
