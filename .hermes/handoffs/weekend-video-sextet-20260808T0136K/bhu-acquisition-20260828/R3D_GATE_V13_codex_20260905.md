ACCESS_SHA=61adc801f873c7dca12117d312a89fab9a1476445fa3228bf7290fb2db878ddf
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES

Not exhaustive as written. The completion-free printed relations can be mutually inconsistent. Such a reading has no allowed masses, so it neither “yields a positive floor” under the stated finite-mass filing scheme nor “permits masses approaching zero.” It therefore belongs to neither P nor Z, despite the class-4 row claiming to include it. This is a real no-class result. By contrast, `DYM_FLOOR_UNDERDETERMINED` is genuinely reachable: for example, the completion-free reading permits masses approaching zero while one admissible one-assumption completion yields a 10 kg floor, giving nonempty P and Z.

Verbatim: “Each admissible reading either **yields a positive floor** — a strictly positive greatest lower bound of the allowed mass set, attained or not — or **permits masses approaching zero**, meaning no positive lower bound follows from it.”

Defect: this asserted dichotomy excludes an inconsistent reading whose allowed mass set is empty.

Exact replacement: “Each consistent admissible reading either **yields a positive floor** — a strictly positive greatest lower bound of its nonempty allowed mass set, attained or not — or **permits masses approaching zero**, meaning no positive lower bound follows from it. An admissible reading whose printed relations are mutually inconsistent is placed in a separate set **I**.”

Verbatim: “| **P is empty** — every admissible reading permits zero, including the case of mutually inconsistent relations | **4** `DYM_NO_POSITIVE_FLOOR` |”

Defect: mutually inconsistent relations do not permit masses approaching zero, so the condition contradicts its gloss and does not route that case.

Exact replacement: “| **P is empty** and either **Z is non-empty** or **I is non-empty** — no consistent admissible reading yields a positive floor | **4** `DYM_NO_POSITIVE_FLOOR` |”

With those replacements, class 3 is selected before limb B, classes 1/2/4 partition limb B, and classes 5/6 are ordered non-scientific states. Without them, the advertised mutual exclusivity does not cure the uncovered inconsistent case.

2. CONTROLS

The control framework generally requires printed artefacts, names exact `PASS|FAIL|NOT_RUN` codes for C0–C6, and gives a general rule that unreached controls record `NOT_RUN`. The three literal commands in §9 are executable as written: `python3 --version`, `python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 $(command -v python3)`.

One live assertion defect remains.

Verbatim: “The exhibition table is the artefact. **The exhibitions are authored by a seat and only verified by Tori** — deciding what counts as reachable is where an author's prior would enter, so the author does not decide it. `C0_REACHABILITY=PASS`.”

Defect: this prints PASS in the preregistration without printing the required V13 exhibition table; §8e later says “C0 must be re-run on V13.” Thus C0 is simultaneously asserted PASS and acknowledged not yet run.

Exact replacement: “The exhibition table is the artefact. **The exhibitions are authored by a seat and only verified by Tori** — deciding what counts as reachable is where an author's prior would enter, so the author does not decide it. Until the V13 exhibition table is printed and verified, record `C0_REACHABILITY=NOT_RUN`; thereafter record `C0_REACHABILITY=PASS` or `C0_REACHABILITY=FAIL` from that artefact.”

3. CIRCULARITY

Sound. The pattern is barred from inclusion, exclusion, and class selection; every nonblank source line receives a disposition, every displayed/numbered equation receives its own row, exclusions require a fixed reason supported by source text, and unresolved material blocks. A contrary relation therefore cannot be quietly omitted while still passing C2. C6 receives the pattern only after a scientific class is selected.

4. THE FALSIFIER — C6

As declared, C6 can return FAIL on 2 outcome classes: `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`. As executable under the current text, only the first has a determinate evaluation object; the second is internally contradictory because it says “choose none” while C6 evaluates “the quantity the seat actually FILED as its floor.”

Condition 1: PASS input — a correctly filed point floor of 10 kg. FAIL input — a malformed filing of the dimensionless ratio 2. It cannot fail on any valid positive-floor-class path; it is `ENTAILED` substantively and can fail only as a filing-integrity check.

Condition 2: PASS input — `M_min = sqrt(ħc/G)`, with every constant in §2b. FAIL input — `M_min = a sqrt(ħc/G)` where `a=2` terminates in an unsupported “we choose” premise.

Condition 3: PASS input — `M_min = sqrt(ħc/G)`, whose simplified expression has no non-§2b symbol. FAIL input — `M_min = α sqrt(ħc/G)` with free `α` surviving.

Condition 4: PASS input — the derivation holds no quantity constant, producing an empty fixity table, or every held constant has a manifest deriving passage. FAIL input — hold core density `ρ0` constant without any manifest passage deriving that fixity.

Condition 5: PASS input — filed interval `[1.0e15, 1.0e15]` kg, which overlaps none of the three numerical comparators. FAIL input — `[2.0e11, 2.0e11]` kg, which overlaps the Hawking interval.

Verbatim: “Report the freedom and **choose none**. **C6 is RUN on this class** and its result reported”.

Verbatim: “**The conditions are evaluated on the quantity the seat actually FILED as its floor, not on an idealised one.**”

Defect: class 2 supplies no single filed floor for the mandated C6 evaluation. Multiple candidate floors, or a mixture of a floor-producing reading and a zero-permitting reading, cannot be evaluated by the singular rule. The claim that condition 3 is expected to fail is also not generally true: two discrete, fully fixed readings can yield 10 kg and 20 kg while each has no surviving free symbol.

Exact replacement for the class-2 instruction: “Report every admissible reading and what it yields, including any that permits zero, and name every completion on which a floor depends; select no scientific estimate. Run conditions 1–5 separately on every positive floor in P, identifying the reading that produced each one. Record class-2 `C6_BREAKER_TEST=PASS` only if exactly one completion-free positive floor exists and its five conditions pass; otherwise record `C6_BREAKER_TEST=FAIL`, naming `UNDERDETERMINED_READING_SET` and printing the full per-reading C6 artefacts.”

Exact replacement for the singular evaluation rule: “For class 1, evaluate the conditions on the filed floor. For class 2, evaluate them on every positive floor in P under the class-2 aggregation rule above; a reading in Z or I is printed as part of the underdetermination artefact and makes the aggregate C6 result FAIL.”

5. RE-RUN GUARD

Sound. §6 expressly forbids assuming K6 repeats, and class 1 is genuinely reachable—for example, completion-free printed relations whose allowed mass set is `[10 kg, ∞)` place their sole agreed floor in P with Z empty.

6. FAIRNESS

Not held in every operative clause.

Verbatim: “| no printed relation binds size to mass or bounds the mass at all | **3** `DYM_NO_SIZE_MASS_RELATION` |”

Defect: this is a branch-level nonexistence claim, while the mandated fair finding is only that the relation was unreproduced from the stated inputs.

Exact replacement: “| after the complete §2 census, a printed relation binding size to mass or bounding mass was **unreproduced from the stated inputs** | **3** `DYM_NO_SIZE_MASS_RELATION` |”

Verbatim: “| **P is empty** — every admissible reading permits zero, including the case of mutually inconsistent relations | **4** `DYM_NO_POSITIVE_FLOOR` |”

Defect: “every admissible reading permits zero” is an affirmative universal physics claim rather than the prescribed reproduction-limited wording.

Exact replacement: “| no consistent admissible reading in the completed ledger reproduces a positive floor from the stated inputs (`P` is empty; route inconsistent readings through `I` as specified above) | **4** `DYM_NO_POSITIVE_FLOOR` |”

The later class-3 and inconsistent-class-4 reporting clauses use the fair wording and are sound.

7. STALL

The scientific run’s read, unresolved-proposition, symbolic-timeout, control-failure, and seat-split paths all have terminal routing to `DYM_SOURCE_BLOCKED` or `R3D_NO_CLASS`. However, the inconsistent-reading hole in finding 1 permits a completed, control-clean limb-B run with no scientific class, so the run can presently reach a terminal point with no fileable class. The replacements in finding 1 close that stall. Separately, V13 cannot freeze until C0 is actually exhibited; finding 2 prevents that pre-run state from being falsely recorded as PASS.

R3D_V13_GATE_COMPLETE
