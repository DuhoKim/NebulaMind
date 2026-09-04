ACCESS_SHA=a441c7c97213df66dc7f80ca346e398eff0ad8afcd492069b440410ea9b4f3eb
C0_REACHABILITY=PASS

# C0 REACHABILITY EXHIBITION — R3D V10

Scope: this exhibition uses only `R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md` and the numbers printed in it. The constructions below are test inputs to the document's classification machinery, not claims about Dymnikova physics.

The seven outcome classes, both directions of all five C6 conditions, and all three C6 outcomes are covered below. “C2 clean” means the stipulated frozen census and ledger are complete, readable, mutually consistent, and contain no `UNRESOLVED` row; it is a stated input configuration, not a claim about the real sources.

| verdict | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| A1 `DYM_FLOOR_DERIVED` | C2-clean printed relations give allowed masses `M ∈ [1.000e15 kg, ∞)` without a completion; every admissible one-assumption completion preserves that set. | §3 Limb A reproduces a size–mass/bounding relation → §4 definition gives unique positive infimum `1.000e15 kg` → §4.1: no added completion, no different completion floor, none approaches zero → file class 1; §5 C6 runs. | yes |
| A2 `DYM_FLOOR_UNDERDETERMINED` | Completion-free set is `M ∈ [1.000e15 kg, ∞)`; one admissible named completion, consistent with all printed relations, strengthens it to `M ∈ [2.000e15 kg, ∞)`; no admitted set approaches zero. | §3 Limb A reproduces a bound → §4 definition supplies floors `1.000e15` and `2.000e15 kg` → §4.2: completion-free positive floor plus a different positive completion floor, with neither approaching zero → class 2; §5 C6 runs. | yes |
| A3 `DYM_NO_SIZE_MASS_RELATION` | After a complete C2-clean census, no included printed relation binds size to mass or bounds mass. | §2c complete census → §3 Limb A says the relation was unreproduced and stops → §4.3 files class 3 → §5 C6 is `NOT_RUN`. | yes |
| A4 `DYM_NO_POSITIVE_FLOOR` | A reproduced printed relation permits exactly `M ∈ (0, 1.000e15 kg]`. | §3 Limb A reproduces a mass-bounding relation → the set has infimum `0`, so by §4's definition it has no positive floor and permits masses approaching zero → §4.4 files class 4, with its stated precedence over class 2 → §5 C6 is `NOT_RUN`. | yes |
| A5 `DYM_FLOOR_COMPLETION_DEPENDENT` | Printed relation permits `M ∈ (0,∞)` and hence gives no positive floor. The sole admissible named completion adds `M ≥ 1.000e15 kg`, giving unique floor `1.000e15 kg`; no admissible completion permits approach to zero. | §3 Limb A reproduces a mass-binding relation → §4.5: no floor from printed relations alone, one named admissible completion gives a positive floor, and no admissible completion permits zero → file class 5; §5 C6 runs. **Finding:** the same input also satisfies §4.4 because the printed relation alone permits zero. Class 4 is stated to take precedence only over class 2, not class 5, so the document accepts both classes and supplies no tie-breaker. | yes (also accepted by A4) |
| A6 `DYM_SOURCE_BLOCKED` | Manifest entry 18 at its pinned path cannot be read. | §2a/C1: a needed pinned source cannot be read → §4.6 says the study waits and files `DYM_SOURCE_BLOCKED`; §4.7 is ruled out by its ordering; §5 C6 is `NOT_RUN`. | yes |
| A7 `R3D_NO_CLASS` | All evidence is readable/resolved, but in one seat C3's required deleted-state execution fails on attempt 1 and again when the required control is rerun; the seat-split rule has been applied and no source is unread. | Rule out §4.6 → §4.7: required control fails after two attempts in a seat after the §9 seat-split rule → file `R3D_NO_CLASS`; §5 C6 is `NOT_RUN`. | yes |
| B1 PASS | Use A1 and file `1.000e15 kg`; dimensional analysis is `[M] = kg`. | §5 C6 applicability on class 1 → condition 1 bounded procedure classifies dimension → mass in kg satisfies its pass criterion. | yes |
| B1 FAIL | Use the A2 underlying mass sets, but the seat actually files the dimensionless number `2.0` as “its floor.” | §4.2 supplies a positive-floor outcome → C6 runs → C6's “quantity the seat actually FILED” clause applies → condition 1 expressly fails when the filed quantity is not a mass. | yes |
| B2 PASS | A1 floor formula is `M_min = sqrt(hbar*c/G) = 2.176434e-8 kg`; its only constants are `hbar`, `c`, and `G`, all in §2b. | Class 1 → C6 → condition 2 scope is constants of the derived floor → each provenance-table row terminates in §2b → PASS. | yes |
| B2 FAIL | A2 completion files `M_min = alpha × 1.000e15 kg = 2.000e15 kg` with chosen `alpha = 2.0`; `alpha` terminates in the named added completion, not a manifest equation or §2b. | Class 2 → C6 → condition 2 provenance chain for `alpha` terminates outside the permitted endpoints → its exact criterion says FAIL. | yes |
| B3 PASS | A1 formula `sqrt(hbar*c/G)` contains only §2b constants; replacing every non-§2b parameter leaves the empty free-symbol set `{}` and the same printed number. | Class 1 → C6 → condition 3 one-shot simplification/free-symbol rule → no non-§2b symbol remains → PASS. | yes |
| B3 FAIL | A2 files the completion floor `M_min = alpha × 1.000e15 kg`; replace `alpha` by an algebraically independent symbol. The simplified expression retains free-symbol set `{alpha}` and yields the printed `2.000e15 kg` only when `alpha=2.0` is chosen. | Class 2 → C6 → condition 3 says recovery only after choosing a parameter means a free normalisation survives → FAIL. | yes |
| B4 PASS | In A1 the only held-constant quantities are `hbar`, `c`, and `G`, and the fixity table identifies §2b for every row (or equivalently a C2-reproduced manifest deriving passage for any source quantity). | Class 1 → C6 → condition 4 fixity table → every held constant has the required deriving line → PASS. | yes |
| B4 FAIL | In A2's completion floor, hold `q=2.0` constant by choice and provide no deriving passage for `q` in the C2-reproduced manifest passages. | Class 2 → C6 → condition 4: a held-constant quantity with no manifest derivation fails → FAIL. | yes |
| B5 PASS | File point floor `[1.000e15, 1.000e15] kg` and complete all four comparison rows. It overlaps none of `[2.176434e-8, 2.176434e-8]`, `[1.729e11, 5.190e11]`, or `[4.375e30, 5.768e30]` kg; ΛCDM has no interval. | A1 → C6 → condition 5 interval-overlap rule → no comparator overlap → PASS. | yes |
| B5 FAIL | File point floor `[2.000e11, 2.000e11] kg` and complete all four rows. It lies inside and therefore overlaps the Hawking interval `[1.729e11, 5.190e11] kg`; it overlaps neither the Planck point nor the stellar interval, and ΛCDM has no interval. | A1 instantiated with unique completion-free floor `2.000e11 kg` → C6 → condition 5 “FAILS iff” overlap disjunction → named comparator 2 overlap → FAIL. | yes |
| C `C6_BREAKER_TEST=PASS` | A1 with filed floor `[1.000e15,1.000e15] kg`; mass dimensional analysis passes; all constants terminate in §2b/manifest equations; free-symbol set is empty; all fixed quantities have deriving passages; completed comparator table has no overlap. | §4.1 → §5 C6 applies → conditions 1–5 each satisfy their rules and table is complete → explicit C6 PASS definition. | yes |
| C `C6_BREAKER_TEST=FAIL` | A1 with unique floor `[2.000e11,2.000e11] kg`, all artefacts complete, conditions 1–4 passing; condition 5 overlaps Hawking `[1.729e11,5.190e11] kg`. | §4.1 still files the floor even when a breaker condition fails → C6 applies → condition 5 FAIL → explicit C6 FAIL definition. | yes |
| C `C6_BREAKER_TEST=NOT_RUN` | A3: complete census but no reproduced size–mass or mass-bounding relation, hence no positive floor. | §3 Limb A stop → §4.3 → C6's applicability clause and explicit outcome list assign `NOT_RUN`. | yes |

## Comparator-overlap arithmetic

- Planck point: `[2.176434e-8, 2.176434e-8] kg`.
- Hawking interval: `[1.729e11, 5.190e11] kg`. Since `1.729e11 <= 2.000e11 <= 5.190e11`, the B5-FAIL point overlaps comparator 2.
- Stellar interval: `[4.375e30, 5.768e30] kg`.
- The B5-PASS point `1.000e15 kg` is greater than `5.190e11 kg` and less than `4.375e30 kg`, so it overlaps none of the three finite comparator intervals. ΛCDM supplies no interval and can never match under the document's rule.

## C6 FAIL path count

On the declared class paths, C6 can return FAIL on **3 of the 7 outcome classes**: `DYM_FLOOR_DERIVED`, `DYM_FLOOR_UNDERDETERMINED`, and `DYM_FLOOR_COMPLETION_DEPENDENT`. It is mandated `NOT_RUN` on classes 3, 4, 6, and 7. Every individual breaker condition can FAIL on at least one of these positive-floor paths, as rows B1–B5 exhibit. Class 5's construction is also accepted by class 4, but that overlap does not make the declared class-5 verdict impossible; it exposes non-exclusive routing.

## Unreachable verdicts

None. Every requested verdict and condition direction has a concrete exhibition. The A5 construction is a routing overlap, not an unreachable verdict: it is accepted by both classes 4 and 5, and the document states no precedence between those two classes.

R3D_C0_EXHIBITION_COMPLETE
