ACCESS_SHA=4e12ef211eea02808b36f1d9c0c756f7f5986459bb333aee8aa7f1cddcb4d708
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES

The six declared terminal classes are not mutually exclusive. A real overlap is: the manifest prints no relation binding size to mass and no direct mass bound; the completion-free reading therefore permits masses approaching zero; one admissible one-assumption completion states `M >= 10 kg` and is consistent with every printed relation. This satisfies class 3's condition, while `P` is non-empty and `Z` is non-empty, satisfying class 2. Limb A routes it to class 3, but the purported partition routes it to both. The table calls itself a decision procedure, yet the document expressly says no precedence rule exists.

VERBATIM: “no printed relation binds size to mass or bounds the mass at all”

Defect: this condition is not exclusive of the later conditions, which quantify over completion-added readings.

EXACT REPLACEMENT: “no printed relation binds size to mass or bounds the mass at all, AND no admissible completion yields a positive floor”

VERBATIM: “These five are mutually exclusive and cover every case in which limb B is reached, by construction — so NO precedence rule between them is needed, and none is stated.”

Defect: only four scientific classes are listed, and they are not mutually exclusive as written.

EXACT REPLACEMENT: “These four are mutually exclusive and cover every case in which a scientific outcome is reached, by construction — so NO precedence rule between them is needed, and none is stated.”

An inconclusive scientific result is genuinely reachable: for example, the completion-free reading permits masses approaching zero while a consistent one-assumption completion yields a 10 kg floor; that reaches `DYM_FLOOR_UNDERDETERMINED`. The two non-scientific terminal classes are also distinct after the source-blocked-first rule. Exhaustiveness is nevertheless not established because of the overlap and the open completion universe discussed in finding 3.

2. CONTROLS

C0, C1, C2, C3, C4, C5, C5b and C6 each name exact `PASS|FAIL|NOT_RUN` codes. C0 requires an exhibition table; C1 computed digests; C2 the complete census and ledger; C3 executed deleted-state output; C4 printed algebra and premises; C5 live command output; C5b a complete per-path table; and C6 its per-condition artefacts and comparison table. None can validly pass by bare assertion. The three literal shell commands in §9 are executable as written.

The unreached-control policy is incomplete for the no-positive-floor path. C6 is explicitly `NOT_RUN` there, but C3 is defined as a probe governing derived-floor filing and the document neither runs it nor explicitly makes it unreached for class 4. Because §9 permits `NOT_RUN` only when expressly authorized, an obedient seat has no valid C3 status on this path. (C4 remains runnable for relations used.)

VERBATIM: “C6 — breaker test. Applies on EVERY outcome that yields a positive floor — `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED` — and is `NOT_RUN`, never a pass, only where C6 was never engaged — `DYM_NO_SIZE_MASS_RELATION`, `DYM_NO_POSITIVE_FLOOR`, or a `DYM_SOURCE_BLOCKED` / `R3D_NO_CLASS` filed before any C6 evaluation.”

Defect: this disposes C6 but leaves C3 undisposed on `DYM_NO_POSITIVE_FLOOR`.

EXACT REPLACEMENT: “C3 is `NOT_RUN` on `DYM_NO_SIZE_MASS_RELATION` and `DYM_NO_POSITIVE_FLOOR`, because no derived floor exists to test; it records its actual result on every positive-floor path. C6 — breaker test. Applies on EVERY outcome that yields a positive floor — `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED` — and is `NOT_RUN`, never a pass, only where C6 was never engaged — `DYM_NO_SIZE_MASS_RELATION`, `DYM_NO_POSITIVE_FLOOR`, or a `DYM_SOURCE_BLOCKED` / `R3D_NO_CLASS` filed before any C6 evaluation.”

3. CIRCULARITY

The source census itself is strong: it accounts for every nonblank source line and every displayed equation, constrains exclusions to named codes, preserves `UNRESOLVED`, and forbids the lane pattern in inclusion, exclusion, and class selection. A contrary printed relation cannot quietly be omitted without falsifying the reconciliation artefact.

But the outcome is quantified over all admissible one-assumption completions, while C2 requires rows only for candidates “considered.” There is no frozen, exhaustive completion manifest and no bounded enumeration rule for all assumptions consistent with the sources. A lane-friendly completion can therefore be considered while a contrary completion is quietly never considered; that changes `P`, `Z`, and the selected class without violating the printed ledger. The pattern can reach the evidence through which completion-added relations are enumerated.

VERBATIM: “An admissible reading is either the completion-free derivation (the printed relations with nothing added) or the printed relations plus exactly one admissible completion.”

Defect: this creates an unbounded class-determining universe that the design never exhaustively enumerates.

EXACT REPLACEMENT: “Scientific class selection is determined only by the completion-free reading. Named one-assumption completions may be reported as sensitivity analyses, but they do not alter the scientific class and may not supply evidence for or against the lane pattern.”

VERBATIM: “The seat prints a row for every candidate premise or relation considered, with status `SOURCE_DERIVED`, `ADDED_COMPLETION` or `UNRESOLVED`.”

Defect: “considered” permits silent non-consideration of a contrary completion.

EXACT REPLACEMENT: “The seat prints a row for every source-derived candidate premise or relation identified by the exhaustive §2c census, and for every added completion actually used in a separately labelled sensitivity analysis, with status `SOURCE_DERIVED`, `ADDED_COMPLETION` or `UNRESOLVED`; added completions do not determine the scientific outcome class.”

The §4 `P`/`Z`/`I` decision table must then be rewritten to classify the completion-free reading alone; the two quoted sentence replacements cannot by themselves leave the existing completion-dependent table operative.

4. THE FALSIFIER

NUMBER OF DECLARED OUTCOME CLASSES ON WHICH C6 CAN RETURN FAIL: 2 — `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`.

Condition 1: PASS is possible with a filed floor of `10 kg`. FAIL is possible only as a filing-integrity failure, for example filing the dimensionless ratio `M/m_P = 2` as the floor. It cannot fail substantively on any valid declared positive-floor path, because membership already requires a mass floor.

Condition 2: PASS is possible for `M_floor = sqrt(ħc/G)` when every constant terminates in §2b (with the construction relation reproduced in C2). FAIL is possible for `M_floor = A sqrt(ħc/G)` where `A=2` is merely chosen and has no manifest derivation.

Condition 3: PASS is possible for `M_floor = sqrt(ħc/G)`, whose simplified expression has no non-§2b symbol. FAIL is possible for `M_floor = λ sqrt(ħc/G)` with free `λ`; the free-symbol set contains `λ`.

Condition 4: PASS is possible when no non-fundamental model quantity is held fixed by choice, so the fixity table has no offending row. FAIL is possible when a core density `ρ0` is held constant although no reproduced manifest passage derives its constancy.

Condition 5: PASS is possible for the point floor `[1.0e15, 1.0e15] kg`, which overlaps none of the three numerical comparator intervals. FAIL is possible for `[2.0e11, 2.0e11] kg`, which overlaps the Hawking interval `[1.729e11, 5.190e11] kg`.

Thus conditions 2–5 can each pass and fail substantively. Condition 1 cannot fail on any valid scientific path; its only FAIL example is a malformed filing.

5. RE-RUN GUARD

Sound. The operative sentence, “K6's outcome may not be assumed to repeat: this is a different branch and the study must be able to return `DYM_FLOOR_DERIVED`,” expressly bars assuming the earlier outcome. The positive class is reachable, for example where the completion-free consistent allowed mass set is `[10 kg, infinity)`, all admissible readings agree on that floor, and `Z=I=empty`.

6. FAIRNESS

The governing fairness sentence is sound, and the operative limb-A and inconsistency clauses use “unreproduced from the stated inputs.” But the general class-4 instruction does not require that wording for an ordinary consistent `Z` case; it merely says “Report the family,” leaving an operative negative filing free to say that no positive floor exists.

VERBATIM: “DYM_NO_POSITIVE_FLOOR — as partitioned above. Report the family.”

Defect: the filing instruction does not bind a consistent no-floor result to the mandated reproduction-limited wording.

EXACT REPLACEMENT: “DYM_NO_POSITIVE_FLOOR — as partitioned above. Report the family and state that a positive floor was unreproduced from the stated inputs; do not state that the branch is in error or that no positive floor exists.”

7. STALL

Every source/read/unresolved/undecidable fallback path maps to `DYM_SOURCE_BLOCKED`; persistent non-source control failure maps to `R3D_NO_CLASS`; symbolic procedures have capped fallbacks; and seat splits have a third-seat rule plus a blocked fallback. Those stall provisions are sound. However, the missing C3 disposition identified in finding 2 means the class-4 run can reach a terminal scientific result with no legal status for every control, so it cannot produce a control-clean fileable class under the current text. The exact replacement in finding 2 closes that stall.

R3D_V15_GATE_COMPLETE
