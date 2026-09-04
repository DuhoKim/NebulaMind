ACCESS_SHA=2aba32d013ed8fc6ed5bcbc63cfd95a32b6e98ce79b43d54f8c3d4d172afd2e1
C0_REACHABILITY=FAIL

This exhibition tests only the machinery printed in `R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md`. The hypothetical relations and ledgers below are concrete inputs to its decision rules; they are not claims about the Dymnikova sources.

| verdict | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| `DYM_FLOOR_DERIVED` | A completed, control-clean census reproduces the source-pinned allowed set `M >= 10 kg`; no completion is added, every admissible completion preserves `10 kg`, and none permits `M -> 0`. Result: unique floor `10 kg`. | §2c complete census -> §3 Limb A reproduces a size–mass/bounding relation -> §4 definition gives a strictly positive unique infimum -> §4.1 (completion-free; no differing or zero-permitting completion) -> C6 runs under §5. | yes |
| `DYM_FLOOR_UNDERDETERMINED` | Printed relations give `M >= 10 kg`; the one named admissible completion `surface radius R = 1.2 times the printed reference radius` is consistent with every printed relation and changes the allowed set to `M >= 12 kg`; neither case permits `M -> 0`. | §2 admissibility rule -> §2c census -> §3 Limb A -> §4 definition -> §4.2: completion-free floor `10 kg` plus unequal admitted floor `12 kg`, with no zero approach -> C6 runs. | yes |
| `DYM_NO_SIZE_MASS_RELATION` | All four pinned files are readable and identity-matched; the exhaustive, reconciled §2c census contains no reproducible relation binding size to mass or bounding mass, with every line and equation disposed and no `UNRESOLVED` row. | §2a/C1 pass -> §2c/C2 complete -> §3 Limb A fails to reproduce the required relation and expressly stops -> §4.3. | yes |
| `DYM_NO_POSITIVE_FLOOR` | Census reproduces `M = (1 kg/m) R` with allowed `R > 0` and no lower bound on `R`; take `R_n = 1/n m`, hence `M_n = 1/n kg -> 0`. | §2c census -> §3 Limb A reproduces a size–mass relation -> §4.4: a printed relation binds size to mass and permits masses approaching zero -> precedence over §4.2. | yes |
| `DYM_FLOOR_COMPLETION_DEPENDENT` | No input can satisfy it. If printed relations alone have no positive lower bound, they “permit” masses approaching zero under §4.4's express definition. If at least one printed relation binds size to mass or bounds mass, §4.4 applies and takes precedence; if none does, §3/§4.3 requires `DYM_NO_SIZE_MASS_RELATION`. | Candidate -> either (i) no binding/bounding relation -> §3 stop and §4.3, or (ii) such a relation exists and no completion-free positive floor follows -> §4.4, whose definition of “permit” is exactly “no positive lower bound on the mass follows”; §4.4 precedence blocks §4.5. | **no — UNREACHABLE** |
| `DYM_SOURCE_BLOCKED` | The computed SHA-256 of required entry 18 is `0000000000000000000000000000000000000000000000000000000000000000`, not its §2a manifest digest. | §2a required source -> C1 digest mismatch -> §4.6 expressly files `DYM_SOURCE_BLOCKED`; the study waits. | yes |
| `R3D_NO_CLASS` | All evidence is readable, identity-matched, and resolved; one seat's reached C3 deletion-probe control fails on its first execution and again on the required third-seat rerun. | Rule out §4.6 -> §4.7 required control fails after two attempts in a seat -> §9 seat-split/re-run procedure -> `R3D_NO_CLASS`. | yes |
| C6 condition 1 PASS | Filed floor is `10 kg`. | Positive-floor class -> §5 C6 evaluates the actually filed quantity -> condition 1 dimensional analysis gives mass in kg. | yes |
| C6 condition 1 FAIL | Malformed filing: the seat enters the dimensionless ratio `M/M_sun = 0.5` as “the floor.” | §5 says C6 evaluates what was actually filed and explicitly says a non-mass fails condition 1 -> dimensional analysis gives dimensionless ratio -> FAIL. This is the malformed filing demanded by C0's `ENTAILED` route, not a valid substantive member of a positive-floor class. | yes (filing-integrity failure); substantive FAIL is `ENTAILED` impossible |
| C6 condition 2 PASS | Filed floor formula `M_f = c^3 t_0/G = 1.757659861333842e53 kg`; provenance rows terminate `c`, `t_0`, and `G` in §2b. | C6 condition 2 scope -> full provenance table -> every floor constant terminates in §2b -> PASS. | yes |
| C6 condition 2 FAIL | Filed floor `M_f = A c^3 t_0/G`, with `A = 2` introduced only by “we choose A=2” and absent from manifest equations and §2b. | C6 condition 2 trace -> `A` terminates at a chosen coefficient, not a manifest equation or §2b -> FAIL. | yes |
| C6 condition 3 PASS | `M_f = c^3 t_0/G = 1.757659861333842e53 kg`, with no non-§2b parameter. | Replace every non-§2b parameter (empty set) -> one SymPy simplification -> no non-§2b free symbol remains -> PASS. | yes |
| C6 condition 3 FAIL | `M_f = alpha c^3 t_0/G`, with algebraically independent non-§2b `alpha`; choose `alpha=1` only to print `1.757659861333842e53 kg`. | Replace `alpha` by a free symbol -> simplified expression still contains `alpha`; printed number is recovered only after choosing it -> condition 3 FAIL. This can route through §4.2's surviving completion freedom and C6. | yes |
| C6 condition 4 PASS | The frozen derivation holds no non-§2b quantity constant; its fixity table is complete and has zero held-constant rows. | Condition 4 bounded procedure -> complete empty fixity table -> every row (vacuously) has a deriving passage -> PASS. | yes |
| C6 condition 4 FAIL | Derivation fixes a core density at `rho_0 = 1.0e18 kg/m^3`, while the C2 passages contain no derivation of that constancy. | Condition 4 fixity table lists `rho_0` -> no manifest deriving passage in the C2 artefact -> FAIL. | yes |
| C6 condition 5 PASS | Filed floor interval `[1.000000e15, 1.000000e15] kg`. It overlaps none of `[2.176434e-8, 2.176434e-8]`, `[1.729e11, 5.190e11]`, or `[4.375e30, 5.768e30]` kg; ΛCDM has no interval. | Complete four-row comparison table -> apply the stated iff overlap disjunction -> no overlap -> condition 5 PASS. | yes |
| C6 condition 5 FAIL | Filed floor interval `[2.000000e11, 2.000000e11] kg`. It overlaps comparator 2, Hawking evaporation `[1.729e11, 5.190e11] kg`; it overlaps neither comparator 1 nor 3, and ΛCDM has no interval. | Complete four-row comparison table -> point `2.0e11` lies inside comparator 2 -> stated iff rule -> condition 5 FAIL, comparator 2 named. | yes |
| `C6_BREAKER_TEST=PASS` | In a §4.1 filing, use `M_f = c^3 t_0/G = 1.757659861333842e53 kg`; dimension is mass, all constants trace to §2b, no free symbol or assumed fixity survives, and its point interval overlaps no comparator; print every required artefact and the complete four-row table. | §4.1 -> §5 C6 engaged -> conditions 1–5 each PASS -> complete table -> C6 outcome definition `PASS`. | yes |
| `C6_BREAKER_TEST=FAIL` | In a §4.1 filing, use floor `[2.000000e11, 2.000000e11] kg` with conditions 1–4 passing and a complete table. | §4.1 -> C6 engaged -> condition 5 overlaps Hawking comparator 2 -> any condition failure -> C6 outcome definition `FAIL`; §4.1 says the scientific class is still filed. | yes |
| `C6_BREAKER_TEST=NOT_RUN` | Use the complete-census/no-binding-relation configuration for `DYM_NO_SIZE_MASS_RELATION`. | §3 Limb A stop -> §4.3 -> §5 says C6 is never engaged on this class -> C6 outcome definition `NOT_RUN`. | yes |

Blocking clause for the sole unreachable verdict

`DYM_FLOOR_COMPLETION_DEPENDENT` is blocked by §4.4's definition and precedence (verbatim):

> **DYM_NO_POSITIVE_FLOOR** — **at least one printed relation binds size to mass or bounds the mass**, and those relations, alone or under **at least one** admissible completion, **permit** masses approaching zero — where **"permit" means no positive lower bound on the mass follows.**

> **This class takes precedence over `DYM_FLOOR_UNDERDETERMINED`.**

The second sentence names only class 2, but the first sentence necessarily captures every class-5 candidate having a printed binding/bounding relation: class 5 requires that no positive floor follow from the printed relations alone, which is exactly §4.4's defined zero-approach test. With no such relation, §3's mandatory stop instead routes to class 3. Thus §4.5 has no remaining input domain.

C6 FAIL path count

The document's §5a says “3 of the 7,” but the executable clauses do not support that as the final-class count. On reachable paths, `C6_BREAKER_TEST=FAIL` can accompany **4 of the 7 outcome classes**:

1. `DYM_FLOOR_DERIVED` (any failed condition; §4.1 preserves the class);
2. `DYM_FLOOR_UNDERDETERMINED` (C6 runs and may fail);
3. `DYM_SOURCE_BLOCKED` after C6 condition 3 is `UNDECIDED` (the C6 outcome clause explicitly says record FAIL, then file this class);
4. `R3D_NO_CLASS` when an engaged C6 control defect such as a missing comparison table fails again under §4.7's two-attempt rule.

The nominal fifth candidate, `DYM_FLOOR_COMPLETION_DEPENDENT`, is itself unreachable for the reason above. C6 is `NOT_RUN` on classes 3 and 4. If “on how many classes does §5 initially declare C6 applicable?” is intended instead, the printed answer is 3, but one of those three classes is unreachable and the later post-engagement terminal rules add classes 6 and 7. The actual reachable final-class count is therefore **4**, not 3.

Because one of the seven declared outcome verdicts is unreachable, the required all-verdict criterion is not met.

R3D_C0_EXHIBITION_COMPLETE
