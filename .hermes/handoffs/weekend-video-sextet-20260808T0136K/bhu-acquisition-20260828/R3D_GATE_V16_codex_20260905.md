ACCESS_SHA=81898e2599888ed14da82ea26220be98d51796a0c4a479e6b9966004565b3cfd
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES — UNSOUND.

The four scientific classes are not mutually exclusive. A real result with a complete census but no printed size–mass relation and no printed mass bound fits class 3. Its completion-free allowed mass set also permits masses approaching zero, so `P` is empty and `Z` is non-empty; it therefore simultaneously fits class 4. The prose calls the first row a “domain restriction,” but neither the class-4 predicate nor an explicit decision order excludes the class-3 domain. Because the document expressly says that no precedence rule exists, the run has no unique scientific class for this result.

Verbatim: “| **`P` is empty** and **`Z` or `I` is non-empty** — no consistent admissible reading yields a positive floor | **4** `DYM_NO_POSITIVE_FLOOR` |”

Defect: this predicate also accepts every ordinary class-3 case whose completion-free reading permits masses approaching zero.

Exact replacement: “| **the class-3 condition does not hold**, **`P` is empty**, and **`Z` or `I` is non-empty** — at least one printed relation binds size to mass or bounds mass, but no consistent admissible reading yields a positive floor | **4** `DYM_NO_POSITIVE_FLOOR` |”

With that repair, the scientific partition is exhaustive: class 3 takes the no-printed-binding/no-printed-bound domain, and the `P`/`Z`/`I` predicates partition the remaining domain. An inconclusive result is genuinely reachable: for example, a completion-free printed derivation yielding `M_min = 10 kg` plus one admissible completion operating on that relation and yielding `M_min = 20 kg` gives two floors in `P` and files `DYM_FLOOR_UNDERDETERMINED`. The two non-scientific states cover unread/unresolved/undecidable evidence and persistent control failure, subject to finding 2.

2. CONTROLS — UNSOUND.

No reached control can pass by assertion: C0 requires an exhibition table; C1 computed digests (and `repr()` for entry 18); C2 the full census and ledger; C3 captured execution output; C4 algebra and premise lists; C5 executed command output; C5b a complete per-path scope table; and C6 the condition artefacts and completed comparison table. Every control has an exact `PASS|FAIL|NOT_RUN` code. The three literal C5 commands are executable as written; direct execution returned Python 3.9.6, SymPy 1.14.0, and a SHA-256 for `/usr/bin/python3`.

Unreached controls are not fully handled. Limb A explicitly dispositions C3, C4, and C6, and C6 separately defines its unreached cases, but an early `DYM_SOURCE_BLOCKED` event can prevent later controls from running without any clause explicitly authorizing their `NOT_RUN` results. Example: an unread first manifest source makes C1 fail and immediately files `DYM_SOURCE_BLOCKED`; C2, C3, and C4 are then unreached, while the global rule forbids `NOT_RUN` unless explicitly authorized.

Verbatim: “**`NOT_RUN` is permitted only where this document explicitly makes that control unreached.**”

Defect: the document does not explicitly disposition every control made unreachable by an earlier source-blocking or terminal event, so an obedient seat cannot emit the required exact token for every control.

Exact replacement: “**`NOT_RUN` is required for any control not reached because an earlier event has already selected a declared terminal class; the report must name that earlier event and the first control it prevented from running. Every control reached before that event retains its actual `PASS` or `FAIL` result. In all other circumstances, `NOT_RUN` is permitted only where this document explicitly makes that control unreached.**”

3. CIRCULARITY — SOUND.

The lane pattern cannot select the evidence or outcome: every non-blank source line receives a disposition, every displayed or numbered equation receives its own row, exclusions require a predeclared reason demonstrated from source text, unresolved evidence blocks, and the pattern is expressly barred until C6 after a positive-floor class is selected. A contrary mass/size relation cannot quietly receive `NO_MASS_OR_SIZE_CONTENT`; omission also breaks the line reconciliation and equation list. No replacement.

4. THE FALSIFIER — SOUND AS TO REACHABILITY, WITH ONE ENTAILED CONDITION.

As a number, C6 can return `FAIL` on **2** of the 6 declared outcome classes: `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`.

- Condition 1: PASS — file `M_min = 10 kg`. FAIL — file the dimensionless ratio `M/r_0 = 2` as though it were the floor. It cannot fail on any valid class path because positive-floor membership already requires a mass; it fails only on a malformed filing and is correctly marked `ENTAILED`.
- Condition 2: PASS — `M_min = sqrt(ħc/G)`, with every constant terminating in §2b. FAIL — `M_min = α sqrt(ħc/G)` where asserted `α = 2` has no manifest or §2b terminus.
- Condition 3: PASS — `M_min = sqrt(ħc/G)`, which contains no non-§2b symbol. FAIL — `M_min = λ sqrt(ħc/G)` with free `λ` surviving simplification.
- Condition 4: PASS — a derivation with no quantity held fixed by choice (an empty fixity table). FAIL — hold `r_0 = 1 m` constant without a manifest passage deriving that constancy.
- Condition 5: PASS — the point floor `1.0e15 kg`, which overlaps none of the three finite comparator intervals. FAIL — `2.1764343e-8 kg` overlaps the Planck interval; `2.0e11 kg` overlaps the Hawking interval; and `5.0e30 kg` overlaps the stellar-collapse interval.

Thus conditions 2–5 can pass and fail substantively. Condition 1 cannot fail on any valid outcome path.

5. RE-RUN GUARD — SOUND.

The design expressly forbids assuming K6 repeats, and `DYM_FLOOR_DERIVED` is genuinely reachable: a consistent completion-free allowed mass set with a unique positive infimum, with every admissible reading agreeing and `Z = I = ∅`, reaches it. No replacement.

6. FAIRNESS — SOUND.

The operative negative findings use “unreproduced from the stated inputs,” including limb A/class 3 and the inconsistent-relations branch of class 4; no operative clause labels non-reproduction an error. No replacement.

7. STALL — UNSOUND.

The bounded symbolic procedures have explicit timeouts and fallbacks, and unresolved execution can file `DYM_SOURCE_BLOCKED`. Nevertheless, the overlapping class-3/class-4 result in finding 1 reaches a terminal scientific state with no uniquely fileable class because the document denies any precedence rule. Independently, the unreached-control gap in finding 2 prevents a conforming report from assigning all mandatory status tokens after some early blocked states. The exact replacements in findings 1 and 2 repair both terminal gaps.

R3D_V16_GATE_COMPLETE
