ACCESS_SHA=bbcb4a894957de620f978357dd0a4c2099f8302925db878694348cd6a743ae79
C0_REACHABILITY=PASS

# C0 REACHABILITY EXHIBITION — V14

Scope: this exhibition uses only `R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md` and the numbers printed in it. No Dymnikova source was read. The constructions below are inputs to the document's decision machinery; a “source passage” in a construction means a stipulated row in the required frozen-C2 artefact, not a claim about what any real source contains.

Section 4 declares six current outcome classes: four scientific classes and two non-scientific terminal states. Its phrase “five scientific classes” is a repair scar: the fifth scientific label, `DYM_FLOOR_COMPLETION_DEPENDENT`, is expressly retired and is not tested here, as instructed.

| verdict | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| `DYM_FLOOR_DERIVED` | Clean/readable sources and passed controls. The completion-free reading has allowed masses `M >= 4.352868e-8 kg` (`2 m_P`); every one-assumption admissible completion has the same allowed set. Thus `P` is non-empty and contains one floor, while `Z=I=empty`. | §2 admissible reading → §3 size–mass relation reproduced, Limb B → §4 definition of positive/unique floor → §4 partition: “P non-empty, all of P agree on one floor, Z AND I both empty” → class 1. C6 is engaged by §5. | yes |
| `DYM_FLOOR_UNDERDETERMINED` | Clean/readable sources and passed controls. Completion-free reading allows `M >= 10 kg`; one admissible completion allows `M >= 20 kg`. Hence `P` contains two different floors and `Z=I=empty`. | §2 two admissible readings → §3 Limb B → §4 `P` non-empty and “P holds two different floors” → class 2; report both, name the completion, choose none. C6 is engaged by §5. | yes |
| `DYM_NO_SIZE_MASS_RELATION` | Completed exhaustive §2c census, with every nonblank line and equation reconciled, but no included relation binds size to mass or bounds mass. | §2c census complete → §3 Limb A cannot reproduce a size–mass or mass-bounding relation → stop and file `DYM_NO_SIZE_MASS_RELATION` → §4 class 3. C6 is not engaged under §5. | yes |
| `DYM_NO_POSITIVE_FLOOR` | Clean/readable sources and passed controls. A reproduced relation gives allowed masses `M > 0 kg` with no other bound; every admissible completion also permits arbitrarily small positive masses. Therefore `P=I=empty`, `Z` non-empty. | §3 relation reproduced, Limb B → §4 “permits masses approaching zero” → partition condition `P` empty and `Z` non-empty → class 4. C6 is not engaged under §5. | yes |
| `DYM_SOURCE_BLOCKED` | The required entry-18 pinned file cannot be read (alternatively, its computed digest differs from `2f3ca3e10ec016eed83104750d11d2428d5523c712814f68d559724d8b2c6b6f`). | §2a required manifest source → §4 class 5 unread/mismatched-source limb → study waits. C6 is `NOT_RUN` because filing occurs before evaluation (§5). | yes |
| `R3D_NO_CLASS` | All source identities match and no proposition is unresolved, so `DYM_SOURCE_BLOCKED` is ruled out; in seat A, required C3 deletion-probe execution fails on the first attempt and again on its mandated re-run, while seat B is control-clean; the third seat re-runs the failed control and it fails again. | §4 class 6: blocked ruled out + required control fails after two attempts in a seat → §4 control-clean/third-seat rule confirms persistent failure → §9 seat split rule → `R3D_NO_CLASS`. File before C6 evaluation, so C6 is `NOT_RUN`. | yes |
| C6 condition 1 — PASS | Filed floor `4.352868e-8 kg`; dimensional analysis prints `[M]`. | §5 C6 evaluates quantity actually filed → condition 1 bounded procedure classifies dimension → mass in kg satisfies criterion. | yes |
| C6 condition 1 — FAIL (filing-integrity case) | Malformed filing puts the dimensionless ratio `M/m_P = 2` in the floor field. | §5 says a filed non-mass makes condition 1 fail → dimensional analysis gives `1`, not kg/M☉ → FAIL. For a correctly filed positive-floor class, PASS is entailed; §5 C0 expressly licenses this malformed-filing rejection as the required opposite exhibition. | yes |
| C6 condition 2 — PASS | Floor `2 m_P = 4.352868e-8 kg`; the construction's equation supplies coefficient `2`, and `m_P=sqrt(hbar c/G)` terminates solely in §2b constants. A complete provenance row is printed for each constant. | Condition 2 scope → trace `2` to construction equation and `hbar,c,G` to §2b → every chain terminates in a manifest equation or §2b → PASS. | yes |
| C6 condition 2 — FAIL | Floor `2 m_P`, but the ledger says coefficient `2` was introduced as “we choose 2,” with no manifest derivation. | Condition 2 bounded trace → coefficient terminates in a chosen assumption, one of the explicitly failing termini → FAIL. | yes |
| C6 condition 3 — PASS | Final floor expression `2 sqrt(hbar c/G)` contains no non-§2b parameter after the required one-shot simplification. | Replace non-§2b parameters by independent symbols (there are none) → simplified free-symbol set outside §2b is `{}` → PASS. | yes |
| C6 condition 3 — FAIL | Final floor `alpha sqrt(hbar c/G)` with free dimensionless normalization `alpha`; simplification leaves `{alpha}`. | Replace parameters by independent symbols → `alpha` survives → printed number requires choosing `alpha` → FAIL. | yes |
| C6 condition 4 — PASS | Frozen derivation holds only `hbar`, `c`, and `G` constant, and the fixity table points each row to §2b (with the reproduced source-derived coefficient `2` not treated as a freely held quantity). | List every held-constant quantity → each has its permitted deriving entry/passage → PASS criterion met. | yes |
| C6 condition 4 — FAIL | Derivation of a floor holds a core density `rho_0` constant; its fixity-table row has no deriving passage in the frozen C2 artefact. | Condition 4 list → missing manifest derivation for a held-constant quantity → FAIL. | yes |
| C6 condition 5 — PASS | Filed floor interval `[1,1] kg`. It overlaps none of `[2.176434e-8,2.176434e-8]`, `[1.729e11,5.190e11]`, or `[4.375e30,5.768e30]`; ΛCDM has no interval. | Complete four-row comparison table → no finite comparator overlap → condition 5 PASS by the iff rule. | yes |
| C6 condition 5 — FAIL | Filed floor interval `[2.176434e-8,2.176434e-8] kg`. It overlaps comparator 1, the Planck-remnant interval, at exactly `2.176434e-8 kg`; it overlaps neither comparator 2 nor 3, and ΛCDM has no interval. | Complete four-row comparison table → overlap with comparator 1 → condition 5 FAIL by the iff rule. | yes |
| `C6_BREAKER_TEST=PASS` | A class-1 construction files `2 m_P = 4.352868e-8 kg`; condition 1 sees mass, condition 2 traces `2` to the construction equation and `hbar,c,G` to §2b, condition 3 has no non-§2b free symbol, condition 4's complete fixity table has a deriving entry for every row, and condition 5's complete table finds no overlap (it is above the Planck point and far below comparator 2). | §4 class 1 → §5 C6 applies → complete artefacts + conditions 1–5 each PASS → stated C6 outcome rule → PASS. | yes |
| `C6_BREAKER_TEST=FAIL` | A class-1 construction files `m_P = 2.176434e-8 kg`; conditions 1–4 pass, but the complete condition-5 table finds exact overlap with comparator 1. | §4 class 1 → §5 C6 applies → condition 5 FAIL → stated C6 outcome rule (“any condition fails”) → FAIL; §4 says class 1 is still filed. | yes |
| `C6_BREAKER_TEST=NOT_RUN` | Use the class-3 construction: the completed census reproduces no size–mass or mass-bounding relation, so Limb A stops before any floor exists. | §3 Limb A stop → §4 class 3 → §5 C6 applicability clause says `NOT_RUN` where no positive-floor class was entered → NOT_RUN. | yes |

## Partition and overlap findings

- All six declared current classes have a reachable input.
- The four current scientific classes are mutually exclusive for the constructed cases. Class 3 exits at Limb A. Once Limb B is reached, the exact `P/Z/I` tests route the examples uniquely to class 1, 2, or 4.
- No constructed case fits two scientific classes, and no constructed admissible-reading case fits none. In particular, the inconsistent-only case `P=Z=empty, I non-empty` goes to class 4; a completion-only floor has `P` and `Z` both non-empty and goes to class 2.
- The two terminal states are operational overrides, not additional members of the `P/Z/I` scientific partition: unread/unresolved evidence routes to class 5, while persistent control failure after blocked is ruled out routes to class 6.
- `DYM_FLOOR_COMPLETION_DEPENDENT` is retired and is not a seventh class. Its former state remains reachable but routes to class 2.

## Condition-5 arithmetic

- PASS example `[1,1] kg`: `1 > 2.176434e-8`, `1 < 1.729e11`, and `1 < 4.375e30`; therefore there is no overlap with any of the three finite intervals.
- FAIL example `[2.176434e-8,2.176434e-8] kg`: intersection with comparator 1 is the same singleton interval; intersections with comparators 2 and 3 are empty.
- The C6 PASS example `[4.352868e-8,4.352868e-8] kg` has no overlap: it is not equal to the comparator-1 singleton and is below comparators 2 and 3. It may be reported as a non-decisive near-match to comparator 1, but the document's decisive rule is overlap only.

## Breaker-failure path count

`C6_BREAKER_TEST=FAIL` can return on **2 of the 6 outcome classes**: `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`, exactly the two classes on which C6 applies. On class 2, for example, the free-normalization construction `alpha m_P` makes condition 3 fail after C6 is engaged. It is `NOT_RUN` on the other four classes when they are filed before any C6 evaluation.

## Unreachable verdicts and blocking clauses

None. Every required current class, each direction of every breaker condition (with condition 1's expressly authorized malformed-filing rejection), and every C6 outcome has a concrete exhibition. Therefore there is no blocking clause to quote.

R3D_C0_EXHIBITION_COMPLETE
