> # ⚠️ FALSE NEGATIVE — CAUSED BY A STALE BRIEF, NOT BY A DEFECT IN V13. PRESERVED, NOT DELETED.
> This exhibition's `C0_REACHABILITY=FAIL` is an artefact of MY brief, which still asked for SEVEN outcome
> classes after Duho's ruling retired one. The seat flagged it in its own scope note — *"§4 actually declares six
> outcome classes … not seven"* — tested the retired `DYM_FLOOR_COMPLETION_DEPENDENT` as row A7 to honour the
> request, found it unreachable (which is what retirement means), and that single row set the verdict.
> **Every one of §4's six live classes exhibited cleanly here.** Superseded by the corrected re-run.
> **Kept as evidence about the brief, and as the control's first FALSE NEGATIVE beside its three true positives.**

ACCESS_SHA=61adc801f873c7dca12117d312a89fab9a1476445fa3228bf7290fb2db878ddf
C0_REACHABILITY=FAIL

Scope note: §4 actually declares six outcome classes—four scientific classes and two non-scientific terminal states—not seven. To honor the requested seven-row test, row A7 tests the retired `DYM_FLOOR_COMPLETION_DEPENDENT` label discussed in §4. It is not a presently declared class and cannot be filed. All six classes that §4 does declare have reachable inputs.

| verdict | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| A1 `DYM_FLOOR_DERIVED` | A complete, control-clean census reproduces a printed size–mass binding whose completion-free allowed set is `M ∈ [10,∞) kg`; the only admissible reading is completion-free (equivalently, every enumerated admissible reading gives the same 10 kg infimum), so `P={10 kg}` and `Z=∅`. | §2 admissible-reading definition → §3 Limb A reproduces the binding and reaches Limb B → §4 positive-floor definition (strictly positive GLB; attainment immaterial) → decision row “P non-empty, all of P agree on one floor, Z empty” → class 1. C6 is then engaged by §5 C6. | yes |
| A2 `DYM_FLOOR_UNDERDETERMINED` | Completion-free reading permits `M>0` with masses approaching zero; one admissible completion `M≥10 kg` supplies a 10 kg floor. Thus `P={10 kg}` and `Z` contains the completion-free reading. | §2 exactly-one-named-assumption completion is admissible → §3 reproduced binding reaches Limb B → §4 `P` non-empty and `Z` non-empty → class 2; the completion-dependent state is expressly carried by class 2. C6 is engaged because this outcome yields a positive floor. | yes |
| A3 `DYM_NO_SIZE_MASS_RELATION` | After the complete §2c census, no printed relation binds size to mass or bounds mass. | §2c complete/reconciled census → §3 Limb A cannot reproduce the required relation → files `DYM_NO_SIZE_MASS_RELATION` and stops → §4 class 3. C6 is not engaged. | yes |
| A4 `DYM_NO_POSITIVE_FLOOR` | A reproduced binding permits exactly `M∈(0,10] kg` in the completion-free reading and in every admissible completion. Every reading permits masses approaching zero, so `P=∅`. | §3 relation reproduced, so Limb B → §4 positive-floor definition → decision row “P is empty” → class 4. C6 is not engaged. | yes |
| A5 `DYM_SOURCE_BLOCKED` | Required manifest file entry 18 is unreadable (alternatively its computed digest is `0000000000000000000000000000000000000000000000000000000000000000`, not the §2a digest). | §2a/C1 requires readable, identity-matching pinned sources → §4 class 5 says an unread required pinned source or identity mismatch files `DYM_SOURCE_BLOCKED` and waits. C6 was not evaluated, hence `NOT_RUN`. | yes |
| A6 `R3D_NO_CLASS` | All sources are readable and resolved, so `DYM_SOURCE_BLOCKED` is ruled out; in one seat the same required control fails on its initial run and its prescribed second attempt. | §4 class 6: rule out source blocking → apply §9 seat-split/two-attempt rule → persistent required-control failure → `R3D_NO_CLASS`. If filed before any C6 evaluation, C6 is `NOT_RUN`. | yes |
| A7 retired `DYM_FLOOR_COMPLETION_DEPENDENT` | Candidate construction: completion-free reading permits masses approaching zero, while every admissible completion gives the same 10 kg floor. This is the former class-5 state. | §4 makes the completion-free reading an admissible reading; it lies in `Z`, while completions put 10 kg in `P` → `P` non-empty and `Z` non-empty → class 2 `DYM_FLOOR_UNDERDETERMINED`; §4 expressly says the former label is retired. | **no — UNREACHABLE** |
| B1 PASS — condition 1 | Filed floor is the point interval `[10,10] kg`. | C6 evaluates the actually filed quantity → dimensional analysis returns mass in kg → condition 1 PASS. | yes |
| B1 FAIL — condition 1 | Malformed filing names the dimensionless ratio `2` as “the floor.” | C6 evaluates the actually filed quantity → dimensionless, not mass → condition 1 FAIL. For a correctly filed positive-floor class, failure is `ENTAILED` away; this is the malformed filing §5 C0 and §5a expressly require as the rejection exhibit. | yes, as a filing-integrity failure; no substantive valid-class failure |
| B2 PASS — condition 2 | Filed floor `10 kg`; its only magnitude constant, `10`, is reproduced by an equation in a verbatim §2a C2 passage, and kg is the mass dimension. | C6 condition 2 provenance table → every floor constant terminates in a manifest-source equation or §2b → PASS. | yes |
| B2 FAIL — condition 2 | Filed floor `M_floor=α kg` with `α=10` introduced by the completion “we choose α=10,” with no manifest derivation. | C6 condition 2 follows `α` in the C2 passages → terminus is a chosen completion rather than §2a equation/§2b constant → FAIL. | yes |
| B3 PASS — condition 3 | Final expression simplifies to `10 kg` and contains no non-§2b symbol. | Replace every non-§2b parameter by independent symbols → simplify once → sorted surviving set `{}` → condition 3 PASS. | yes |
| B3 FAIL — condition 3 | Final expression is `α kg`, with free non-§2b `α`. | Symbol replacement/simplification (or §9 tree fallback) → sorted surviving set `{α}` → condition 3 FAIL. | yes |
| B4 PASS — condition 4 | The frozen derivation holds no quantity constant; its completed fixity table therefore has zero rows. | Enumerate every held-constant quantity → empty set, so every row vacuously has the required manifest derivation → condition 4 PASS. | yes |
| B4 FAIL — condition 4 | A core density `ρ0` is held fixed by choice, and the C2 artefact contains no manifest passage deriving its constancy. | Fixity table row `ρ0` has no manifest derivation → condition 4 FAIL. | yes |
| B5 PASS — condition 5 | Explicit filed floor interval `[10,10] kg`. It overlaps none of `[2.176434e-8,2.176434e-8]`, `[1.729e11,5.190e11]`, or `[4.375e30,5.768e30]` kg; ΛCDM has no interval. | Complete four-row table → apply the iff overlap disjunction → no overlap → condition 5 PASS. | yes |
| B5 FAIL — condition 5 | Explicit filed floor interval `[2.176434e-8,2.176434e-8] kg`. It overlaps comparator 1, the identical Planck-remnant interval; it overlaps neither comparator 2 nor 3, and ΛCDM has no interval. | Complete four-row table → overlap with comparator 1 → condition 5 FAIL. | yes |
| C `C6_BREAKER_TEST=PASS` | Use A1’s `[10,10] kg` floor, source-derived constants, no free symbols, no underived held-fixed quantity, and a complete comparator table; conditions 1–5 all take their PASS constructions above. | §4 class 1 → §5 C6 engaged → complete artefacts and every condition satisfies its decision rule → C6 PASS. | yes |
| C `C6_BREAKER_TEST=FAIL` | Use an otherwise clean A1 floor `[2.176434e-8,2.176434e-8] kg`; conditions 1–4 pass, but condition 5 overlaps comparator 1. | §4 class 1 → C6 engaged → condition 5 FAIL → “any condition fails” rule → C6 FAIL; class 1 is still filed. | yes |
| C `C6_BREAKER_TEST=NOT_RUN` | Use A3: the completed census reproduces no size–mass relation and the study stops in Limb A. | §3 Limb A stop → §4 class 3 → §5 says C6 is not engaged for `DYM_NO_SIZE_MASS_RELATION` → NOT_RUN. | yes |

Partition findings: among the six presently declared classes, every class has a reachable input. Among the four presently defined scientific classes, A1–A4 each fit exactly one decision branch; none of these constructions fits two classes or none. The prompt’s “five scientific classes” does not match §4: the fifth scientific label was retired, and its candidate case A7 necessarily fits current class 2. The two terminal states are separated by class 6’s instruction to rule out `DYM_SOURCE_BLOCKED` first, so A5 and A6 do not overlap.

C6 can return FAIL on **2 of the 7 rows requested here**: A1 and A2. In the document’s own current denominator, it can return FAIL on **2 of the 6 declared outcome classes**. It is not engaged on A3–A6, and A7 has no filing path of its own. Each breaker condition has both polarities exhibited; condition 1’s FAIL is only the expressly authorized malformed-filing integrity case because valid positive-floor membership entails a mass quantity.

UNREACHABLE blocking clause for A7, quoted verbatim:

> **That state still occurs and still files — as `DYM_FLOOR_UNDERDETERMINED` (class 2) — and that is correct, not a place to hide it.**

The associated retirement clause is also explicit:

> A floor that exists **only under completions, with every completion agreeing**, was formerly class 5, `DYM_FLOOR_COMPLETION_DEPENDENT`.

Because the requested seventh verdict is unreachable (and is not actually declared by current §4), the requested all-verdict criterion makes `C0_REACHABILITY=FAIL`, even though every one of §4’s six actually declared classes, every required breaker polarity (using the condition-1 `ENTAILED`/malformed route), and all three C6 outcomes are reachable.

R3D_C0_EXHIBITION_COMPLETE
