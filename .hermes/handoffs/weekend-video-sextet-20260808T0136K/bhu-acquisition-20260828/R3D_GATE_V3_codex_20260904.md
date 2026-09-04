ACCESS_SHA=872d4978b73cabc6257328776fe9c7ffc7890b2268dffd160eb0284ee341080a
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES

The six classes are not mutually exclusive, and their exhaustiveness is not secured by an effective terminal rule. A real overlap between classes 2 and 3 is: the printed branch has no size–mass relation; two admissible added completions bind size to mass differently and yield unequal positive floors; and the declared admissible-completion set contains no zero-approaching family. That result satisfies both `DYM_FLOOR_UNDERDETERMINED` and `DYM_NO_SIZE_MASS_RELATION`. The stated precedence of class 4 does not resolve the 2/3 overlap. In addition, unread evidence can both force class 5 and make a control fail twice, satisfying class 6, with no precedence between them. Operationally inconclusive results are reachable through classes 5 and 6, but they are not uniquely classifiable.

Verbatim: “**DYM_FLOOR_UNDERDETERMINED** — the printed relations admit **at least two positive but unequal floors** under admissible completions, **and no admissible completion permits masses approaching zero**.”

Defect: this includes the no-printed-size–mass-relation case and therefore overlaps class 3.

Exact replacement: “**DYM_FLOOR_UNDERDETERMINED** — at least one printed relation binds size to mass, the printed relations admit at least two positive but unequal floors under admissible completions, and no admissible completion permits masses approaching zero.”

Verbatim: “**R3D_NO_CLASS** — a control fails in both seats after two attempts.”

Defect: it overlaps `DYM_SOURCE_BLOCKED` when unread or unresolved evidence causes the failed control, and it does not cover a persistent failure confined to one seat.

Exact replacement: “**R3D_NO_CLASS** — after applying the source-blocked rule and the seat-split rule, any required control that still fails after two attempts in any seat files this class; `DYM_SOURCE_BLOCKED` takes precedence whenever unread or unresolved evidence caused the failure.”

2. CONTROLS

C2, C3, C5, C5b and C6 demand printed artefacts, and every control has an exact result code. C1 and C4 can still be passed by assertion: neither sentence requires the identity comparison or benchmark algebra and result to be printed. Unreached controls are generally covered by §9’s `NOT RUN` rule, although §5 inconsistently spells C5/C5b’s token `NOT_RUN` with an underscore.

Verbatim: “**C1 — source identity**, on raw bytes with `repr()` if the pinned text is PDF-extracted. `C1_SOURCE_IDENTITY=PASS`.”

Defect: no printed artefact is required.

Exact replacement: “**C1 — source identity.** Print the pinned path, byte length, full SHA-256, and, for PDF-extracted text, the exact compared spans with `repr()`; a bare assertion fails. `C1_SOURCE_IDENTITY=PASS`.”

Verbatim: “**C4 — GR benchmark** as algebra only, supplying no interior premise. `C4_GR_BENCHMARK=PASS`.”

Defect: no execution or printed algebra artefact is required.

Exact replacement: “**C4 — GR benchmark** as algebra only, supplying no interior premise; execute and print every substitution, free symbol, intermediate equality and final equality, and treat a bare assertion as failure. `C4_GR_BENCHMARK=PASS`.”

Verbatim: “Unreached C5/C5b are recorded `NOT_RUN`, never `PASS`.”

Defect: this conflicts with §9’s exact token `NOT RUN`, making the required recorded code ambiguous.

Exact replacement: “Unreached C5/C5b are recorded `NOT_RUN`, never `PASS`; this exact underscore spelling applies to every unreached control throughout the document.”

3. CIRCULARITY

The pattern is verbally forbidden from selecting evidence, which is good, but the census cannot demonstrate its own exhaustiveness. No frozen source manifest, source hashes, search vocabulary/normalization, page-by-page reconciliation, or expected row count exists. A seat can quietly omit a contrary row and still print a ledger called exhaustive. C3 occurs only after this selection and cannot recover the omitted row. The lane-authored pattern can therefore still influence what the seat notices or omits.

Verbatim: “**Before choosing a limb or an outcome, each seat constructs and prints an exhaustive census** of every equation or sentence in the pinned Dymnikova sources that mentions or relates **core scale, density, mass, mass function, radius, horizon, matching surface, regularity, or the de Sitter limit**.”

Defect: “exhaustive” is an assertion, not a bounded reproducible census procedure.

Exact replacement: “Before choosing a limb or outcome, each seat independently hashes every file in a frozen path-and-page source manifest, extracts every page, prints every hit from a frozen case-insensitive search over `core`, `scale`, `density`, `mass`, `mass function`, `radius`, `horizon`, `matching`, `surface`, `regular`, and `de Sitter` (including formula-adjacent sentences), then performs and prints a page-by-page zero-hit attestation; the union of search hits and page-audit additions is the census, and any manifest, extraction, or reconciliation failure forces `DYM_SOURCE_BLOCKED`.”

4. THE FALSIFIER

None of the five conditions is decidable from this frozen document. Conditions 1–4 are never enumerated as propositions: naming “the stated calculation,” a provenance table, a free-symbol probe and a fixity derivation does not define pass/fail predicates, inputs, tolerances, or bounded algorithms. Condition 5 explicitly depended on a comparator set to be fixed before freezing, but this already-frozen version contains no finite comparator list, observable, tolerance, or permitted source corpus.

Verbatim: “**C6 — breaker test.** If class 1 is reached, conditions 1–4 are evaluated by the stated calculation, a full citation-chain provenance table, a free-symbol probe, and a fixity derivation.”

Defect: the four conditions and their decision rules are absent.

Exact replacement: “**C6 — breaker test.** Before freezing, enumerate conditions 1–4 verbatim as Boolean propositions and, for each, specify its frozen inputs, exact pass/fail criterion, bounded algorithm, timeout result, and required printed artefact; an unspecified or undecidable condition forces `DYM_SOURCE_BLOCKED` and cannot pass C6.”

Verbatim: “**So before the run is frozen, a finite named comparator set, the observable and tolerance that define "shared", and the permitted source corpus are fixed in writing**; every comparison is executed and printed.”

Defect: the promised material is not present before the freeze, so condition 5 remains undecidable.

Exact replacement: “Condition 5 compares [INSERT THE COMPLETE FINITE LIST OF NAMED MODELS HERE] using observable [INSERT ONE DEFINED OBSERVABLE], tolerance [INSERT A NUMERIC TOLERANCE AND COMPARISON RULE], and only sources [INSERT A COMPLETE FROZEN PATH/DOI LIST]; the frozen table is complete only when every listed comparator has a printed value and comparison result.”

5. RE-RUN GUARD

Sound. The design expressly forbids assuming K6 repeats, permits the Dymnikova branch to supply a relation, and makes `DYM_FLOOR_DERIVED` genuinely reachable. No replacement.

6. FAIRNESS

The rule is stated once but not held everywhere. Operative negative classes and limb instructions use categorical “supplies no relation” / “does not” language rather than the required epistemic wording.

Verbatim: “**Limb A (~1 seat-day):** does the branch print a size–mass relation at all? If it does not, the K6 obstruction repeats and the answer follows without deep work — file `DYM_NO_SIZE_MASS_RELATION` and stop.”

Defect: this reports absence as a branch fact and says the prior obstruction “repeats,” rather than reporting non-reproduction from the stated inputs.

Exact replacement: “**Limb A (~1 seat-day):** attempt to reproduce a printed size–mass relation from the stated inputs; if none is reproduced after the complete census, report ‘a size–mass relation was unreproduced from the stated inputs,’ file `DYM_NO_SIZE_MASS_RELATION`, and stop.”

Verbatim: “**DYM_NO_SIZE_MASS_RELATION** — limb A's exit: the branch supplies no relation binding size to mass.”

Defect: the class label text makes an ontological negative claim rather than the mandated reproducibility claim.

Exact replacement: “**DYM_NO_SIZE_MASS_RELATION** — limb A’s exit: a relation binding size to mass was unreproduced from the stated inputs after completion of the frozen census.”

7. STALL

The seat-split rule provides a fileable class, but the fallback is called “named” without naming any numerical/substitution method, domain, sampling set, precision, or decision threshold. A symbolic timeout therefore reaches an instruction that cannot be executed reproducibly, so the run can stall before its purported second timeout and terminal class. The class-6 one-seat gap identified in finding 1 is a second terminal ambiguity.

Verbatim: “On timeout print `SYMBOLIC_TIMEOUT` and execute the **named numerical/substitution fallback under a second 120-second cap**.”

Defect: no fallback is actually named or specified anywhere in the document.

Exact replacement: “For each symbolic operation, a frozen fallback table shall name the exact executable command, substitutions or numerical domain, finite sample set, precision, decision threshold and expected proposition; on `SYMBOLIC_TIMEOUT`, execute and print that row under a second 120-second cap, and if the row is absent or does not decide the proposition, immediately file `DYM_SOURCE_BLOCKED` without passing the affected control.”

R3D_V3_GATE_COMPLETE
