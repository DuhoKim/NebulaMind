ACCESS_SHA=c7488e1cc72c06640b7a1c7ba03a772bb47e9ee9b23b743dbec9c77e24a6341a
C0_REACHABILITY=FAIL

This is a reachability exhibition of the document's machinery only. The configurations below are hypothetical census/ledger/filing inputs; they make no claim about the manifest papers' physics.

| verdict | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| A1 `DYM_FLOOR_DERIVED` | The completed census reproduces a printed constraint whose allowed mass set is `[10,∞) kg`. The completion-free reading and every one-assumption admissible reading have infimum `10 kg`; no reading permits masses approaching zero. Thus `P` is nonempty, every member of `P` gives `10 kg`, `Z=∅`, and the completion-free reading is in `P`. | §2 admissible-reading definition → §3 Limb A reproduces a size–mass/mass-bounding relation → §4 positive-floor definition → §4 decision row “P non-empty, all of P agree on one floor, Z empty, and the completion-free reading is in P” → class 1. C6 is engaged by §5 C6. | yes |
| A2 `DYM_FLOOR_UNDERDETERMINED` | Completion-free reading permits `M>0` with masses approaching zero; one admissible completion C gives allowed set `[10,∞) kg`. Reading set: `P={C↦10 kg}`, `Z={completion-free↦zero}`. | §2 admissible-reading definition → §3 Limb B (a mass-bounding relation is reproduced) → §4 `P`/`Z` construction → §4 row “P is non-empty and the readings disagree … or Z is non-empty” → class 2; §4(2) reports all readings and chooses none; C6 runs under §5. | yes |
| A3 `DYM_NO_SIZE_MASS_RELATION` | A control-clean, exhaustive §2c census reproduces no relation binding size to mass and no relation bounding mass. | §2c complete census → §3 Limb A “If none is reproduced” → file `DYM_NO_SIZE_MASS_RELATION` and stop → §4 class 3. C6 is `NOT_RUN` under §5. | yes |
| A4 `DYM_NO_POSITIVE_FLOOR` | A reproduced relation permits exactly `M>0` in the completion-free reading and in every admissible one-completion reading. Reading set: `P=∅`; `Z={completion-free,C1,C2,…}`, every member permitting masses approaching zero. | §3 Limb A reproduces a mass-related relation, so Limb B is reached → §4 dichotomy and `P`/`Z` sets → §4 row “P is empty — every admissible reading permits zero” → class 4. C6 is `NOT_RUN` under §5. | yes |
| A5 `DYM_FLOOR_COMPLETION_DEPENDENT` | Required target reading set would be: completion-free yields no floor; one or more completions yield the same positive floor; `Z=∅`. But §4 says every reading that does not yield a positive floor permits zero. Hence the completion-free reading is in `Z`, contradicting `Z=∅`. No reading set can satisfy the class. | §4 admissible-reading dichotomy → completion-free “yields no floor” implies “permits masses approaching zero” → completion-free ∈ `Z` → class-5 requirement `Z empty` cannot be met. | **no — UNREACHABLE** |
| A6 `DYM_SOURCE_BLOCKED` | Configure required pinned source 18 as unreadable (for example, permission denied before its bytes can be read). | §2a requires the pinned source → §4(6) “a required pinned source cannot be read” → `DYM_SOURCE_BLOCKED`; study waits. | yes |
| A7 `R3D_NO_CLASS` | Both seats have no unread/unresolved evidence; in one seat C5 executes the required command with a deliberately mismatching SymPy version relative to the other seat and fails, then the third seat re-runs that failed control and also obtains the mismatch/failure. | §4(7) first rules out `DYM_SOURCE_BLOCKED` → required control fails after two attempts in a seat / third-seat failed-control rule → `R3D_NO_CLASS`. | yes |
| B1 PASS (`ENTAILED` on valid classes) | File the floor `10 kg`; dimensional analysis is `[M]`, kg. | §5 C6 evaluates the actually filed quantity → condition 1 bounded procedure classifies dimension → mass in kg meets its pass criterion. For every correctly filed positive-floor class this is entailed by §4's “allowed mass set” definition. | yes |
| B1 FAIL (malformed filing) | Enter class 1 but actually file the dimensionless ratio `0.5` as “the floor.” | §5 C6 says a non-mass filing fails condition 1 → dimensional analysis gives dimension `1`, not kg or M☉ → FAIL. This is the malformed filing explicitly licensed as condition 1's rejection exhibition by C0 and §5a, not a valid scientific-class member. | yes |
| B2 PASS | File `M=sqrt(ħc/G)=2.176434e-8 kg`; provenance rows terminate `ħ`, `c`, and `G` in §2b. | C6 condition 2 scope → constants of derived floor → each terminates in §2b → PASS. | yes |
| B2 FAIL | File `M=A sqrt(ħc/G)` with `A=2` introduced by the completion “we choose A=2,” with no manifest derivation. | C6 condition 2 provenance procedure → `A` terminates in a chosen coefficient, neither manifest equation nor §2b → FAIL. | yes |
| B3 PASS | File `M=sqrt(ħc/G)`; replace every non-§2b parameter (there are none). Simplified expression has no non-§2b free symbol. | C6 condition 3 free-symbol procedure → sorted forbidden-symbol set `{}` → PASS. | yes |
| B3 FAIL | File `M=α sqrt(ħc/G)` while `α` remains free. | C6 condition 3 replaces non-§2b parameters by independent symbols → simplification retains `{α}` → FAIL. | yes |
| B4 PASS | Derivation holds no quantity constant; print a complete fixity table with zero rows. | C6 condition 4 lists every held-constant quantity (empty set) → every row has a deriving passage vacuously → PASS. | yes |
| B4 FAIL | Hold core density `ρ0` constant by choice and print a fixity row stating that no reproduced manifest passage derives its constancy. | C6 condition 4 fixity table → a held-constant quantity has no manifest derivation → FAIL. | yes |
| B5 PASS | Filed floor interval `[1.000e15,1.000e15] kg`. It overlaps none: not Planck `[2.176434e-8,2.176434e-8]`, not Hawking `[1.729e11,5.190e11]`, and not stellar `[4.375e30,5.768e30]`; ΛCDM has no interval. | C6 condition 5 executes all four comparator rows → no interval overlap → PASS by the iff rule. | yes |
| B5 FAIL | Filed floor interval `[2.000e11,2.000e11] kg`. It overlaps comparator 2, Hawking evaporation `[1.729e11,5.190e11] kg`; it overlaps neither comparator 1 nor 3, and ΛCDM has no interval. | C6 condition 5 executes all four rows → named overlap with comparator 2 → FAIL by the iff rule. | yes |
| C `C6_BREAKER_TEST=PASS` | On reachable class 1, file a manifest-equation-derived point floor `[1.000e15,1.000e15] kg`; its coefficient is printed by that manifest equation, all other constants terminate in §2b, no non-§2b symbol survives, no quantity is held fixed, dimensional analysis is kg, and the complete four-row table has no overlap. | §4 class 1 → §5 C6 applies → conditions 1–5 respectively PASS → table complete → C6's three-outcome clause gives `PASS`. | yes |
| C `C6_BREAKER_TEST=FAIL` | On reachable class 1, file `sqrt(ħc/G)=2.176434e-8 kg`, with provenance, free-symbol, and empty-fixity artefacts passing; the complete comparator table shows exact overlap with comparator 1 `[2.176434e-8,2.176434e-8] kg`. | §4 class 1 → §5 C6 applies → condition 5 FAILS on the Planck-remnant overlap → C6's “any condition fails” clause gives `FAIL`; §4(1) still files class 1. | yes |
| C `C6_BREAKER_TEST=NOT_RUN` | Use A3: the exhaustive census reproduces no size–mass or mass-bounding relation, so class 3 is filed and Limb A stops. | §3 Limb A stop → §4 class 3 → §5 says C6 is never engaged and is `NOT_RUN`. | yes |

Partition stress result: the five scientific constructions produce classes 1, 2, 3, and 4 uniquely; no constructed valid case fits two classes. The Limb-A stop routes the no-relation construction to class 3 before the Limb-B `P`/`Z` procedure. No actual reading set fits none of reachable classes 1–4: after Limb B, `P` is either empty (class 4) or nonempty; if nonempty, disagreement or nonempty `Z` gives class 2, otherwise the completion-free reading must be in `P` and gives class 1. Class 5 is not an additional partition cell because its stated predicates are inconsistent.

`DYM_FLOOR_COMPLETION_DEPENDENT` is therefore **UNREACHABLE**. The attempted reading set is explicit: `{completion-free↦no floor, C1↦10 kg, C2↦10 kg}`, with the intended `P={C1,C2}` and intended `Z=∅`. Under the document's dichotomy, however, completion-free permits masses approaching zero and must be in `Z`, so the actual set is `Z={completion-free}` and the case routes to class 2.

Because class 5 is unreachable, C6 can return `FAIL` on **2 of the 7 outcome classes**, classes 1 and 2, not on the declared 3. On each of those two classes, conditions 2, 3, 4, or 5 can supply the failing condition; condition 1 is entailed for a valid member and rejects only the expressly contemplated malformed filing.

## Blocking clause for every UNREACHABLE verdict

`DYM_FLOOR_COMPLETION_DEPENDENT` is blocked by these verbatim §4 clauses:

> “Each admissible reading either **yields a positive floor** — a strictly positive greatest lower bound of the allowed mass set, attained or not — or **permits masses approaching zero**, meaning no positive lower bound follows from it.”

and

> “**P non-empty, all of P agree on one floor, Z empty**, and the **completion-free reading yields no floor**”

The first clause forces a completion-free reading that “yields no floor” into `Z`; the second simultaneously requires `Z empty`. That contradiction blocks every path to class 5.

R3D_C0_EXHIBITION_COMPLETE
