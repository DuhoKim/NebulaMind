ACCESS_SHA=b7883c25784cdbc2617ac7f17ae9accf90f75785866b8849cec4a272111387d2
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES

Defect. The document has seven declared classes, not six. The heading says “## 4. Outcome classes — declared now”, and the list runs through “7. **R3D_NO_CLASS**”. Thus the requested six-class partition does not exist as stated.

Exact replacement sentence: “## 4. Outcome classes — seven declared classes: five scientific outcomes and two non-scientific terminal states”.

Defect. The discriminator between classes 1/2 and 5 is not well-defined because “floor” alternates between a lower bound and an attained minimum. Class 4 defines permit as “where **\"permit\" means no positive lower bound on the mass follows.**”, while class 5 requires reporting “or no attained minimum”. A printed solution set such as `M ∈ (1,2) kg`, plus an admissible completion selecting `M=1.5 kg`, has a positive lower bound but no attained minimum. If “floor” means lower bound, a completion-free floor follows and class 5 is false; if it means attained minimum, class 5 is true. Two obedient seats can select different classes.

Exact replacement sentence (insert before the list): “Throughout §4, a positive floor means a strictly positive greatest lower bound, whether or not that bound is attained; ‘unique floor’ means the unique infimum of the allowed mass set.”

With that definition, the scientific classes can be made exhaustive and exclusive: no binding relation is class 3; a binding relation permitting infimum zero or inconsistency is class 4; otherwise a completion-free positive infimum gives class 1 or 2, and no completion-free positive infimum but a positive infimum under at least one completion gives class 5. `DYM_SOURCE_BLOCKED` and `R3D_NO_CLASS` remain non-scientific terminal states. An inconclusive terminal result is genuinely reachable through either of those states.

2. CONTROLS

Defect. C0 can be passed by an unbounded judgement and names only a PASS code. The text says: “**The exhibitions are authored by a seat and only verified by Tori** — deciding what counts as reachable is where an author's prior would enter, so the author does not decide it. `C0_REACHABILITY=PASS`.” It supplies neither a bounded verification algorithm nor a printed rejection code, and it gives no rule for disagreement. C0 can therefore fail in ordinary language, but cannot fail under an exact named code.

Exact replacement sentence: “Tori executes every exhibited input through a finite decision table containing one row for every §4 class and both condition-5 polarities, prints the traversed predicates and terminal result for each row, and records `C0_REACHABILITY=PASS` iff every advertised result is reproduced; otherwise Tori records `C0_REACHABILITY=FAIL` with the first unreproduced row, and the preregistration remains unfreezable.”

Defect. C3 requires execution but supplies no executable harness or exact invocation. It says: “**The harness must execute the deleted state and print its captured output**; a claimed pass without that output fails. `C3_DELETION_PROBE=PASS`.” No harness path, input format, deleted-state construction, command, or FAIL/NOT_RUN spelling is supplied. This control still depends on a seat asserting that its own construction is the required probe.

Exact replacement sentence: “C3 uses the checked-in script and invocation `<SUPPLY AN ACTUAL RELATIVE SCRIPT PATH AND COMPLETE COMMAND HERE>`; the script prints the retained and deleted relation identifiers, injected relation, exit status, and captured output, and records exactly one of `C3_DELETION_PROBE=PASS`, `C3_DELETION_PROBE=FAIL`, or `C3_DELETION_PROBE=NOT_RUN`.”

This is a substantive unsoundness: the placeholder must be replaced by supplied executable content before freezing; merely requiring a future harness would again defer content.

Defect. C4 can be passed by self-authored algebra without an independent executable check. It says: “For every relation used, the seat **prints the stated-limit algebra** showing equality with the Schwarzschild form in the exterior limit, **and prints the premise list** for that algebra showing that no interior premise entered.” Printing a claimed equality is still an assertion unless the equality and premise membership are mechanically checked.

Exact replacement sentence: “For every relation used, the seat prints the symbolic difference from the pinned Schwarzschild exterior expression after the stated limit, executes the supplied symbolic checker under the §9 cap, requires the simplified difference to be exactly zero, and prints both the checker output and the source-located premise list; otherwise record `C4_GR_BENCHMARK=FAIL`.”

C1, C2, C5, and C5b require printed artefacts and cannot formally pass by mere summary assertion. The three literal C5 commands are executable as written; I executed all three successfully (`Python 3.9.6`, SymPy `1.14.0`, and a SHA-256 for `/usr/bin/python3`). Unreached C5/C5b are expressly `NOT_RUN`. Across the controls generally, however, only PASS spellings are consistently declared; a complete exact-code scheme should give PASS/FAIL/NOT_RUN for every control.

Exact replacement sentence (global control rule): “Every control records exactly one of `<CONTROL_CODE>=PASS`, `<CONTROL_CODE>=FAIL`, or `<CONTROL_CODE>=NOT_RUN`; `NOT_RUN` is permitted only when the document explicitly makes that control unreached.”

3. CIRCULARITY

Defect. The line census makes literal omission visible only if its accounting is internally coherent, but its counting rule is contradictory. It says: “**An equation and its defining or context lines may be treated as one explicitly bounded block** with a single disposition” and then “the count of non-blank lines and the count of assigned dispositions; the two must be equal”. One disposition for a multi-line block cannot equal the number of its non-blank lines. It also separately requires every displayed equation to be its own row, which can double-dispose a line despite “exactly one census disposition”. A quiet omission can consequently be hidden as a counting interpretation, and a contrary relation can still be mislabeled `DUPLICATE` or excluded under a subjective code.

Exact replacement sentence: “Assign every non-blank line exactly one disposition identifier; a bounded multi-line block has one row but its identifier is repeated in the machine-readable line map for every covered line, reconciliation compares non-blank line numbers with mapped line numbers (not row counts), and each displayed equation has a distinct equation-row identifier cross-linked to—rather than counted in addition to—its line disposition.”

Exact replacement sentence: “A `DUPLICATE` or exclusion row must name the included row and print a machine-checkable normalized-text comparison or a source-located branch predicate that entails the code; absent that demonstration it is `UNRESOLVED`.”

The ban on using the lane pattern before C6 is otherwise explicit and sound. The full-text/equation requirement is directionally strong, but as frozen it does not yet make OMITTED versus EXCLUDED mechanically distinguishable in all cases, including bare displays.

4. THE FALSIFIER

Conditions 1, 2, 4, and 5 have finite stated procedures once their input inventories are complete. Condition 3 has a 120-second primary procedure and a finite tree-traversal fallback. The arithmetic independently reproduces all supplied comparator values: Planck mass `2.176434342051127e-8 kg`; Hawking lower value `1.7298245132213727e11 kg` and upper value `5.189473539664118e11 kg`; TOV endpoints `4.375624e30 kg` and `5.767868e30 kg`. The printed outward-rounded intervals are correct.

Condition 5 can PASS and FAIL. A completion-free derived point floor of `1.0e15 kg` overlaps none of the three intervals, so condition 5 PASSes; if conditions 1–4 pass and the four-row artefact is complete, C6 PASSes and class `DYM_FLOOR_DERIVED` is filed as a counterexample. A point floor of `2.0e11 kg` overlaps the Hawking interval, so condition 5 FAILs; C6 FAILs but class `DYM_FLOOR_DERIVED` is still filed and the pattern is not amended. A Planck-mass floor likewise FAILs against comparator 1. Thus no comparator content is deferred, and condition 5 itself has no hidden provenance precondition.

Defect. C6's PASS/FAIL/NOT_RUN set is not exhaustive because condition 3 explicitly creates `UNDECIDED`, while the C6 definition assigns FAIL only when a table is incomplete or a condition “fails its decision rule.” The quoted sentence is: “if that row is absent, times out, or cannot parse the expression, condition 3 is `UNDECIDED`, C6 does not pass, and the run files `DYM_SOURCE_BLOCKED`”. “Does not pass” is not one of the three C6 codes, and UNDECIDED is not FAIL under the stated condition rule.

Exact replacement sentence: “If condition 3 is `UNDECIDED`, record `C6_BREAKER_TEST=FAIL` with the failed primary and fallback artefacts, then file `DYM_SOURCE_BLOCKED`; thus PASS, FAIL, and NOT_RUN are exhaustive and mutually exclusive.”

Defect. The explanatory history directly contradicts the operative incomplete-table rule: “The cost is stated rather than hidden: a lazy comparison now yields a PASS”. Operatively, the document instead says an incomplete table fails C6. Leaving the contradiction invites a seat to record an incomplete comparison as a counterexample.

Exact replacement sentence: “The completeness artefact prevents a lazy or incomplete comparison from yielding C6 PASS: any missing comparator row records `C6_BREAKER_TEST=FAIL`, and the pattern record is not amended.”

5. RE-RUN GUARD

Sound. “K6's outcome may **not** be assumed to repeat” is explicit, the positive class is reachable, and both the matching and non-matching condition-5 paths still file `DYM_FLOOR_DERIVED`. No replacement.

6. FAIRNESS

Sound for operative outcome wording. Limb A and class 3 use “unreproduced from the stated inputs”; class 4 uses the same construction for inconsistency. Historical discussion of earlier wording does not direct a negative scientific finding. No replacement.

7. STALL

Defect. C0 is ordered “run BEFORE the freeze” and says the preregistration “does not freeze” if an exhibition is unreachable, but this target is already labelled “FROZEN pending the fresh referee gate”; C0 has no terminal class, failure code, retry bound, or Tori/seat disagreement rule. It therefore creates exactly a no-file terminal stall before the otherwise comprehensive §9 seat-split guard applies.

Exact replacement sentence: “C0 is a preregistration gate, not a study outcome: before the `FROZEN` label is applied, one seat supplies the table, Tori performs one verification, and any failed or disputed row records `C0_REACHABILITY=FAIL` and files `R3D_NO_CLASS`; only `C0_REACHABILITY=PASS` permits freezing.”

The post-freeze symbolic timeout and seat-disagreement paths otherwise file `DYM_SOURCE_BLOCKED` or `R3D_NO_CLASS`. No other terminal no-class path was found.

Bottom line: condition 5's previous content-deferral failure is repaired—the comparator inputs and intervals are actually supplied, both polarities are reachable, and incomplete comparison is operatively a C6 failure. The preregistration remains unsound because C0 itself is undefined on failure, C3 still defers the executable probe, the census accounting is inconsistent, “floor” is ambiguous at a class boundary, and C6 omits its `UNDECIDED` mapping.

R3D_V9_GATE_COMPLETE
