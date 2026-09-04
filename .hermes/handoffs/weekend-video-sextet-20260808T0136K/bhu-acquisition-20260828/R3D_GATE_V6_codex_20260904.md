ACCESS_SHA=14db4dfbdc660fb3d6852f68dcf399adf8724ab8a4b3ef2a3a959760669e3f9e
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES

The classes are mutually exclusive where their predicates decide a result, but they are not exhaustive. A real uncovered result is: the printed relations bind size and mass and imply a positive lower bound; completion A fixes a unique attained floor F; completion B, also admissible, leaves a range of positive floors (or a non-attained positive infimum); and no admissible completion permits masses approaching zero. This is not class 1 (the printed relations do not give a unique floor), class 2 (there need not be two unequal floors yielded by completions), class 3 (a binding relation exists), class 4 (zero is not permitted), or class 5 (not every completion yields the same floor).

VERBATIM: “**DYM_FLOOR_COMPLETION_DEPENDENT** — a unique positive floor follows **only under one or more named admissible completions**, **every** admissible completion yields **the same** floor, and none permits masses approaching zero.”

DEFECT: This leaves mixed determinate/underdetermined admissible-completion families unclassified.

EXACT REPLACEMENT: “**DYM_FLOOR_COMPLETION_DEPENDENT** — at least one named admissible completion yields a positive floor, no unique positive floor follows from the printed relations alone, and no admissible completion permits masses approaching zero; report for every admissible completion whether it yields a unique floor, a set or range of positive floors, or no attained minimum, and report every resulting value or freedom.”

An inconclusive terminal result is genuinely reachable through `DYM_SOURCE_BLOCKED`, and a control-exhaustion result through `R3D_NO_CLASS`; neither is mislabelled as a scientific conclusion.

2. CONTROLS

C1, C2, C3, C4, C5, and C6 name exact codes and require printed artefacts. The global unreached-control rule is sound. C5b remains passable partly by assertion.

VERBATIM: “**C5b — path list.** Print every opened path and check it against §9's scope rule. `C5B_PATH_LIST=PASS`.”

DEFECT: Printing the paths is an artefact, but “check it” supplies no required printed comparison or per-path disposition; a seat can assert the pass.

EXACT REPLACEMENT: “**C5b — path list.** Print every opened path and, for each path, print `IN_SCOPE` or `OUT_OF_SCOPE` plus the exact §9 scope-rule clause applied; any `OUT_OF_SCOPE` row fails the control. The complete per-path table is the required artefact, and a claimed pass without it fails. `C5B_PATH_LIST=PASS`.”

The three commands in §9 are executable as written in the specified shell. I executed them: Python 3.9.6, SymPy 1.14.0, and a SHA-256 for `/usr/bin/python3` were printed. No command repair is needed.

3. CIRCULARITY

This section is sound. The pattern is barred from enumeration, exclusion, and selection until C6. The complete nonblank-line disposition, full extracted text, stable locators, and separate row for every numbered or displayed equation make an omitted relation distinguishable from an excluded one, including a bare displayed equation. A quietly missing row produces an uncovered line or display rather than an exclusion code. C2 also requires the source text and disposition artefacts; this is not merely a keyword census.

4. THE FALSIFIER

Conditions 1, 2, 4, and 5 have bounded decision rules. Condition 3 does not have the promised executable fallback.

VERBATIM: “On timeout, run the §9 fallback row; if it does not decide, file the applicable non-scientific class.”

DEFECT: Section 9 has fallback rows only for solving horizons, curvature limits, and mass extremisation. It has no row for the condition-3 operation “replace every non-§2b parameter … [and] simplify.” Thus the instruction points to an absent row. Content has again been deferred rather than supplied, although this time the defect is condition 3 rather than condition 5.

EXACT REPLACEMENT: “On timeout, expand the final expression into a frozen expression tree, traverse every node once under a second 120-second cap, and print the sorted set of free symbols found by syntactic occurrence after substituting only §2b constants; PASS exactly if that printed set contains no non-§2b symbol, FAIL if it contains one, and file `DYM_SOURCE_BLOCKED` if traversal times out or cannot parse the expression.”

Condition 5 can now operationally PASS: for a completion-free derived point floor of, for example, `1 kg`, its interval overlaps none of the three numerical intervals, the ΛCDM row cannot match under the frozen rule, so condition 5 passes; if conditions 1–4 also pass, the run files `DYM_FLOOR_DERIVED`. For a derived point floor `2.176434e-8 kg`, the Planck interval overlaps, so condition 5 fails; after the prescribed second failed-control attempt the run files `R3D_NO_CLASS`, rather than a scientific class. Thus matching and non-matching paths are both routed.

However, the claim that every comparator interval is computed only from §2b is false, so condition 5 is not evidentially self-contained as claimed.

VERBATIM: “**Every comparator interval is derived from §2b inside this document.**”

DEFECT: The Hawking upper endpoint introduces an asserted factor `3.0`, and the TOV endpoints introduce asserted coefficients `2.2` and `2.9`; none is in §2b or derived from its constants. The Hawking row itself concedes that its factor “is stated as a bound, not derived here.” The TOV range is likewise supplied rather than derived. Consequently a seat can pass C6 using values transcribed elsewhere in this document, despite the global “No transcription, anywhere” rule. This is precisely deferred provenance, even though the numerical table itself is present.

EXACT REPLACEMENT: “The Planck comparator and the single-species Hawking comparator are derived only from §2b; the coefficients `3.0`, `2.2`, and `2.9` are frozen comparator assumptions, not measured constants or §2b derivations, and each is recorded as an `ADDED_COMPLETION` in the C2 ledger. Condition 5 may pass only if C6 condition 2 independently accepts those comparator assumptions under its provenance rule; otherwise C6 fails.”

Independent arithmetic gives: `sqrt(ħc/G) = 2.1764343420511267e-8 kg`, so the printed Planck value `2.176434e-8` reproduces at its shown precision. The Hawking formula gives `1.7298245132213753e11 kg`, reproducing `1.730e11`; multiplying the ungrounded factor 3 gives `5.189473539664126e11 kg`, reproducing `5.189e11`. The TOV multiplications give `4.375624e30 kg` and `5.767868e30 kg`, reproducing the printed rounded endpoints `4.376e30` and `5.768e30`. The arithmetic reproduces; the provenance of the factor and interval does not.

5. RE-RUN GUARD

Sound. The design explicitly forbids assuming the earlier branch repeats, and `DYM_FLOOR_DERIVED` is genuinely reachable on a completion-free derivation whose controls, including a non-matching C6 table, pass.

6. FAIRNESS

The operative prose is not fair everywhere. It uses categorical negative-existence language outside the protected limb-A wording.

VERBATIM: “If the printed relations are mutually inconsistent, so that no solution and hence no positive lower bound exists, **file here and report the contradiction.**”

DEFECT: “No positive lower bound exists” is a conclusion of nonexistence, not the required lane-limited wording.

EXACT REPLACEMENT: “If the printed relations are mutually inconsistent, report that a consistent solution and a positive lower bound were unreproduced from the stated inputs, file here, and reproduce the contradiction.”

The outcome codes themselves may remain stable identifiers, but narrative negative findings must use the stipulated wording.

7. STALL

The seat-split rule, unread/unresolved routing, repeated-control-failure rule, and second-timeout rule all lead to declared terminal classes. No disagreement path lacks a class. The missing condition-3 fallback does not create a no-file stall because §9 routes an absent fallback to `DYM_SOURCE_BLOCKED`, but it makes a reachable scientific test block non-scientifically and is therefore a substantive preregistration defect.

R3D_V6_GATE_COMPLETE
