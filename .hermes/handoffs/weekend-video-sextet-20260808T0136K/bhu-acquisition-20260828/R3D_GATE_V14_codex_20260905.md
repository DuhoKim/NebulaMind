ACCESS_SHA=bbcb4a894957de620f978357dd0a4c2099f8302925db878694348cd6a743ae79
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES

The six terminal classes are exhaustive and mutually exclusive when the limb rule is applied: limb A files class 3 and stops; limb B partitions admissible readings by P, Z, and I into classes 1, 2, and 4; source/evidence blockage goes to class 5; persistent control failure after source blockage is excluded goes to class 6. A result with a completion-free 10 kg floor and a completion permitting masses approaching zero fits only class 2. An inconsistent completion-free reading fits only class 4. I find no real result that fits two terminal classes or none.

An inconclusive result is genuinely reachable: unreadable or identity-mismatched source material, an UNRESOLVED source proposition, or an undecidable bounded procedure files DYM_SOURCE_BLOCKED; persistent non-source control failure can file R3D_NO_CLASS. DYM_FLOOR_UNDERDETERMINED is also a reachable scientific result rather than a stall.

The sentence “How the five scientific classes partition the cases — a decision procedure, not five descriptions.” miscounts the design: there are four scientific outcomes and two non-scientific terminal states. This is a documentation defect, not a partition defect. Exact replacement: “How the four scientific classes partition the cases — a decision procedure, not four descriptions.”

2. CONTROLS

C0, C1, C2, C3, C4, C5, C5b, and C6 each have an exact code with PASS/FAIL/NOT_RUN vocabulary. C0 requires an exhibition; C1 computed digests; C2 a full census and ledger; C3 captured execution; C4 printed algebra and premises; C5 command output; C5b a per-path table; and C6 condition artefacts. None can validly pass by a bare assertion. Unreached controls are directed to NOT_RUN, not PASS. The three literal shell commands in §9 are executable as written: `python3 --version`, `python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 $(command -v python3)`.

Defect: the design does not state which of C1–C4 are reached on the limb-A exit, although it says NOT_RUN is allowed only where the document explicitly makes a control unreached. The operative text is: “`NOT_RUN` is permitted only where this document explicitly makes that control unreached.” Limb A says only “file `DYM_NO_SIZE_MASS_RELATION` and stop.” Thus two obedient seats can disagree over whether C3 and C4 must run or be marked NOT_RUN, and the control-clean filing rule can change the terminal class.

Exact replacement for the limb-A stop sentence: “If none is reproduced after the complete census of §2, report that a size–mass relation was unreproduced from the stated inputs, file `DYM_NO_SIZE_MASS_RELATION`, record C3, C4 and C6 as `NOT_RUN`, and stop; C0, C1, C2, C5 and C5b remain reached and must carry their actual results.”

3. CIRCULARITY

The live scientific mechanism is substantially protected: every nonblank source line and every displayed equation must receive a printed disposition; exclusions use a closed reason-code list; UNRESOLVED blocks; C2 prints provenance; C3 executes a deletion probe; and the pattern is forbidden as evidence for inclusion, exclusion, and class selection. A contrary relation cannot be quietly omitted without breaking the line reconciliation/equation census.

However, the lane-authored pattern still reaches the seat before the census and outcome through the preregistration itself. The operative sentence says: “The five conditions are copied verbatim below from `SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md`, V2, sha256 `5232201acfdca850c7e8a4d345aad145a3d91fdb750fdbb9a77fb43fec8d4647`, so that evaluation does not depend on an unpinned lane-authored text that may drift between seats.” Copying the pattern into the document makes it visible before the seat selects relations and a class; the prohibition is procedural but not blind. The extensive gate history likewise exposes prior expectations and outcomes. This does not permit an unlogged omission, but it leaves motivated use of `WRONG_BRANCH`, `DEFINITION_ONLY`, and block boundaries possible before C6.

Exact replacement: “Before freezing, a custodian creates a separate pinned C6 packet containing the five condition texts and hash. Derivation seats receive only §§1–4, §§5 C0–C5b, §6’s fairness and re-run rules, §7, and §9; they do not receive C6, §5a, §8, or any pattern/gate history. After each seat has frozen and signed its complete C2 census, ledger, derivation, and provisional class, the custodian releases the pinned C6 packet and the seat evaluates it without changing the frozen census, ledger, derivation, or class. Any post-release change to those artefacts fails C6 and files `R3D_NO_CLASS` after the §4 retry rule.”

4. THE FALSIFIER

As the operative routing is written, C6 can return FAIL on 4 declared terminal classes: `DYM_FLOOR_DERIVED`, `DYM_FLOOR_UNDERDETERMINED`, `DYM_SOURCE_BLOCKED` (condition 3 UNDECIDED after C6 has engaged), and `R3D_NO_CLASS` (for example, a repeatedly missing required C6 table after C6 has engaged). Therefore §5a’s numeric claim of 2 is false; 2 is only the number of scientific positive-floor classes on which C6 initially applies.

Condition 1: PASS is possible with a filed floor of 10 kg. FAIL is possible only as a filing-integrity failure, e.g. filing the dimensionless ratio 0.5 as the floor. It cannot fail on any valid scientific path because positive-floor membership requires a mass.

Condition 2: PASS is possible for `sqrt(ħc/G)`, whose constants terminate in §2b. FAIL is possible for `A sqrt(ħc/G)` where A is introduced by “we choose A=2” and has no manifest derivation.

Condition 3: PASS is possible for `sqrt(ħc/G)`, which has no non-§2b free symbol. FAIL is possible for `α sqrt(ħc/G)` with free α.

Condition 4: PASS is possible when the derivation holds no quantity fixed by choice (or every fixed quantity has a manifest deriving passage). FAIL is possible when core density `ρ0` is held constant without a manifest derivation of that constancy.

Condition 5: PASS is possible for the point floor `1.0e15 kg`, which overlaps no enumerated comparator. FAIL is possible for `2.0e11 kg`, which overlaps the Hawking interval `[1.729e11, 5.190e11] kg`.

Condition 1 is the only condition that cannot fail on any valid path.

Defect sentence: “C6 applies on 2 of the 6 outcome classes — `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`, every class that yields a positive floor. Declared and reachable are now the same number, which is the point of stating both.” Exact replacement: “C6 is initially engaged by the 2 positive-floor scientific classes, `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`; after engagement it can return FAIL in reports ultimately filed under either of those classes, `DYM_SOURCE_BLOCKED`, or `R3D_NO_CLASS`, so C6 FAIL can coexist with 4 of the 6 terminal classes.”

Defect sentence: “It is `NOT_RUN` on the other 4, and that is correct rather than a gap.” Exact replacement: “It is `NOT_RUN` on `DYM_NO_SIZE_MASS_RELATION` and `DYM_NO_POSITIVE_FLOOR`, and on `DYM_SOURCE_BLOCKED` or `R3D_NO_CLASS` only when either is filed before C6 engages; if C6 engages and later causes either non-scientific filing, its recorded result is `FAIL`.”

5. RE-RUN GUARD

Sound. “K6's outcome may not be assumed to repeat: this is a different branch and the study must be able to return `DYM_FLOOR_DERIVED`.” The completion-free P-only configuration reaches class 1, so the positive class is genuinely reachable. No replacement.

6. FAIRNESS

The limb-A and class-3 operative wording correctly says “unreproduced from the stated inputs,” and the inconsistency branch of class 4 does too. But the consistent Z-only branch of class 4 does not impose that wording, while its class label and partition prose state an ontological negative.

Defect sentence: “`P` is empty and `Z` or `I` is non-empty — no consistent admissible reading yields a positive floor.” Exact replacement: “`P` is empty and `Z` or `I` is non-empty — a positive floor was unreproduced from the stated inputs in every consistent admissible reading.”

Defect sentence: “4. **DYM_NO_POSITIVE_FLOOR** — as partitioned above. Report the family.” Exact replacement: “4. **DYM_NO_POSITIVE_FLOOR** — as partitioned above. Report the family and state that a positive floor was unreproduced from the stated inputs; do not state that the source branch is in error or that no positive floor exists.”

7. STALL

Sound. Source/evidence/timeout indeterminacy files DYM_SOURCE_BLOCKED; persistent non-source control failure files R3D_NO_CLASS; seat disagreement invokes a third seat and all-three disagreement or inability to decide files DYM_SOURCE_BLOCKED. Every run can reach exactly one declared terminal class. No replacement.

R3D_V14_GATE_COMPLETE
