ACCESS_SHA=4c8d0d3256134f8ac45bed4fdf5e222d1475ef01d8247cc1716723a379c95dde
C0_REACHABILITY=PASS

# C0 reachability exhibition — R3D V24

This is a reachability test of the preregistration's printed machinery only. The constructions below are synthetic inputs/configurations; they do not assert anything about the Dymnikova sources or judge the physics.

| verdict | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| §4 class 1 `DYM_FLOOR_DERIVED` | Limb-B census reproduces a printed relation with allowed set `M ∈ [10,∞) kg`. The completion-free reading is the only admissible reading; there are no candidate one-assumption completions. Thus `P={10 kg}`, `Z=I=∅`. | §3: a mass-bounding relation is reproduced, so enter limb B → §4 definition: the non-empty allowed set has positive GLB 10 kg → §4 class-1 row: `P` non-empty, all `P` agree, `Z` and `I` empty → class 1. C6 then runs under §4(1)/§5 C6. | yes |
| §4 class 2 `DYM_FLOOR_UNDERDETERMINED` | Limb-B printed relations give completion-free `M ∈ [10,∞) kg`; one admissible completion operating on those relations gives `M ∈ [20,∞) kg`. Thus `P` contains the distinct floors 10 kg and 20 kg. | §3 limb B → §4 assigns both consistent readings to `P` → class-2 row, because `P` holds two different floors → §4(2) reports both, chooses none, and runs C6 separately on both floors. | yes |
| §4 class 3 `DYM_NO_SIZE_MASS_RELATION` | Completed §2 census reproduces neither a size–mass relation nor any mass bound. | §2 census complete → §3 limb A: “a relation binding size to mass, or bounding the mass, was unreproduced” → stop and file class 3 → §4 says class 3 is reached ONLY from limb A; C6=`NOT_RUN`. | yes |
| §4 class 4 `DYM_NO_POSITIVE_FLOOR` | Limb-B census reproduces the mass relation `M > 0 kg`, whose allowed masses approach zero. No other admissible reading exists. Thus `P=I=∅`, `Z={completion-free}`. | §3: a relation bounds mass, so limb B → §4 puts the reading in `Z` → class-4 row (`P` empty and `Z` non-empty) → §4(4), with C3 and C6 `NOT_RUN`. | yes |
| §4 class 5 `DYM_SOURCE_BLOCKED` | The required entry-18 pinned source cannot be read. | §2a requires the frozen manifest source → §4(5): “a required pinned source cannot be read” → study waits and files `DYM_SOURCE_BLOCKED`; later unengaged controls are `NOT_RUN` under §9. | yes |
| §4 class 6 `R3D_NO_CLASS` | All evidence is readable/resolved. Both seats otherwise agree on class 1 and a 10 kg floor, but one seat has `C4_GR_BENCHMARK=FAIL`; the third seat reruns that failed control and it fails again. | Rule out class 5 because nothing is unread/unresolved → §4(6) control-clean rule invokes the third-seat rerun → the same reached control fails on the second attempt → persistent failure → `R3D_NO_CLASS`. | yes |
| C6 condition 1 PASS | Filed floor is the point interval `[10,10] kg`. | §5 C6 quantity actually filed → condition-1 dimensional classification → dimension is mass in kg → PASS. | yes |
| C6 condition 1 FAIL (filing-integrity exhibition) | Malformed filing: a seat enters the dimensionless ratio `r_h/r_0=2` as its “floor.” | §5 C0's `ENTAILED` exception applies: every valid positive-floor class requires a mass, so substantive FAIL is entailed away; §5 C6 nevertheless tests the quantity actually filed → dimensionless ratio is not mass → condition 1 FAIL. | yes (malformed filing, as expressly required by the `ENTAILED` route) |
| C6 condition 2 PASS | Positive floor `M_min=sqrt(ħc/G)=2.176434e-8 kg`; its only constants are `ħ`, `c`, and `G`. | §5 C6 condition 2 → provenance table terminates each constant in §2b → every constant traces → PASS. | yes |
| C6 condition 2 FAIL | Positive floor `M_min=a sqrt(ħc/G)` with `a=7` introduced as “we choose 7,” with no manifest derivation. | §5 C6 condition 2 scopes constants of the floor → `ħ,c,G` terminate in §2b, but `a` terminates in a chosen coefficient outside a manifest equation/§2b → FAIL. | yes |
| C6 condition 3 PASS | `M_min=sqrt(ħc/G)` with all non-§2b parameters replaced; none occur. | §5 C6 condition 3 → one simplification/free-symbol traversal → sorted non-§2b free-symbol set is `{}` → PASS. | yes |
| C6 condition 3 FAIL | `M_min=λ sqrt(ħc/G)`, with `λ` an algebraically independent unfixed normalization. | §5 C6 condition 3 → replace non-§2b parameters by independent symbols → simplified expression still contains `{λ}` → printed number requires choosing `λ` → FAIL. This can file class 2 when different `λ` readings yield different positive floors. | yes |
| C6 condition 4 PASS | `M_min=sqrt(ħc/G)` and the fixity table has only `ħ,c,G`, each identified directly in §2b; no other quantity is held fixed. | §5 C6 condition 4 → every held-constant row has an allowed deriving terminus → PASS. | yes |
| C6 condition 4 FAIL | `M_min=q sqrt(ħc/G)` with `q` held fixed at 2 solely by choice and with no reproduced manifest passage deriving its constancy. | §5 C6 condition 4 → fixity table row `q=2` has no manifest derivation → FAIL. | yes |
| C6 condition 5 PASS | Filed floor interval `[1.000e15,1.000e15] kg`. | Compare under §5 condition 5 with all rows: no overlap with Planck `[2.176433e-8,2.176435e-8]`, Hawking `[1.729e11,5.190e11]`, or TOV `[4.375e30,5.768e30]`; ΛCDM has no interval and cannot match → PASS. | yes |
| C6 condition 5 FAIL — Planck row | Filed floor interval `[2.176434e-8,2.176434e-8] kg`. | Its intersection with Planck `[2.176433e-8,2.176435e-8]` is `[2.176434e-8,2.176434e-8]` kg; it overlaps Planck only → condition-5 iff rule → FAIL, comparator named Planck. | yes |
| C6 condition 5 FAIL — Hawking row | Filed floor interval `[2.000e11,2.000e11] kg`. | Its intersection with Hawking `[1.729e11,5.190e11]` is `[2.000e11,2.000e11]` kg; it overlaps Hawking only → condition-5 iff rule → FAIL, comparator named Hawking. | yes |
| C6 condition 5 FAIL — TOV row | Filed floor interval `[5.000e30,5.000e30] kg`. | Its intersection with TOV `[4.375e30,5.768e30]` is `[5.000e30,5.000e30]` kg; it overlaps TOV only → condition-5 iff rule → FAIL, comparator named TOV. | yes |
| `C6_BREAKER_TEST=PASS` | Class-1 construction with a manifest-derived point floor `[1.000e15,1.000e15] kg`, dimension kg; every floor constant traces, no non-§2b free symbol remains, no underived fixity exists, and the complete four-row comparison table shows no overlap. | §3 limb B → §4 class 1 → §5 C6 engaged → conditions 1–5 each PASS and table complete → the stated three-outcome rule emits `C6_BREAKER_TEST=PASS`. | yes |
| `C6_BREAKER_TEST=FAIL` | Class-1 construction with floor `[2.000e11,2.000e11] kg`; conditions 1–4 pass, while condition 5 overlaps the Hawking interval. | §3 limb B → §4 class 1 → C6 engaged → condition 5 FAIL by overlap → §5 says any condition failure emits `C6_BREAKER_TEST=FAIL`; class 1 still files under §4(1). | yes |
| `C6_BREAKER_TEST=NOT_RUN` | The class-3 no-relation/no-bound construction above. | §3 limb-A exit → §4 class 3 → §5 C6 says C6 was never engaged where no positive-floor class was entered → `NOT_RUN`. | yes |

## Partition stress test

All six declared classes have a reachable input. Each valid outcome construction above files exactly one class; none fits two declared classes and none fits no declared class.

The required hard case is the class-3 construction: the census reproduces no printed size–mass relation and no printed mass bound. Semantically, that absence means the completion-free reading permits masses approaching zero, but the document does not send the case into the limb-B reading partition. Section 3 stops in limb A, and §4 states verbatim: **“Class 3 is reached ONLY from limb A; classes 1, 2 and 4 ONLY from limb B.”** It therefore files the single class `DYM_NO_SIZE_MASS_RELATION` and cannot also file `DYM_NO_POSITIVE_FLOOR`. The separation is by procedural limb, not by the underlying predicate.

The four scientific classes are also a complete operational partition: limb A files class 3; limb B files class 4 for `P=∅` and `Z∪I≠∅`, class 2 for non-empty `P` with disagreement, and class 1 for non-empty unanimous `P` with `Z=I=∅`. The remaining two declared classes are non-scientific terminal routes. (The request's phrase “five scientific classes” conflicts with §4's operative heading and enumeration, which declare four scientific classes and two non-scientific states; this exhibition tests all six declared classes and does not resurrect the retired class.)

## C6 path count

C6 is initially engaged on 2 of the 6 classes: `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`. Once engaged, `C6_BREAKER_TEST=FAIL` can be recorded in **4 of the 6 terminal classes**: those two; `DYM_SOURCE_BLOCKED` if condition 3 is `UNDECIDED` after its fallback; and `R3D_NO_CLASS` if an engaged C6 run is followed by a persistently failing reached control. Thus the requested number of six outcome classes on which C6 can return/record FAIL is **4**.

## Unreachable verdicts

None. Condition 1 has no valid substantive FAIL because positive-floor membership entails a mass, but §5 C0 expressly supplies the `ENTAILED` route: prove that entailment and exhibit the malformed filing rejected by the condition. That required integrity-check exhibition is provided above, so it is not an unreachable C0 row.

R3D_C0_EXHIBITION_COMPLETE
