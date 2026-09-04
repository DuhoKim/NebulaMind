# ORDERED — R3-D pre-registration: does the Dymnikova regular-core branch fix a minimum black-hole mass?

**Tori, 2026-09-05. Version 22 (see §8). NOT FROZEN and NOT RUN: C0 must return `C0_REACHABILITY=PASS` from a
fresh seat exhibition on this version's bytes, and the two-seat referee gate must follow, before any freeze. ORDERED by Duho, "run r3c and r3d", 2026-09-04 21:02 KST.**
20:56 note. **Drafting is not starting. No derivation has been run.**

## 0. Why this would exist

K6 found entry 51's ECKS mass floor `K6_FLOOR_UNDERDETERMINED`: the density ceiling cannot bound a mass without a
size–mass relation `V(M)` the source never supplies. **The obvious next question is whether the corpus's *other*
regular-interior branch — Dymnikova's de Sitter core (entries 18–20, 55) — does supply one.**

A regular-core metric is explicit, so this branch is **in principle able** to fix a mass scale from its own
geometry; **whether it does is decided only by the census and the C2 ledger.** No prior lane conclusion — including
any prediction about where a breaker is likely — is a reason for inclusion, exclusion or outcome anywhere in this
document. *(This paragraph previously restated the pattern record's own verdict that this branch is the most likely
breaker. A seat citing §0 would not formally be citing the pattern record, so the §2 prohibition was bypassed
through this document's own text, and the expectancy pointed at exactly the outcome the study is meant to decide.)*

## 1. The question, exactly

Do the Dymnikova regular-core metrics, as printed, determine a **closed relation between the core scale, the mass and
the horizon** sufficient to imply a positive minimum black-hole mass — and if so, what is it?

## 2. Objects to bind before arithmetic, or mark ABSENT

The metric and its stated stress-energy; the core scale parameter and what fixes it; which mass (ADM, Misner–Sharp,
Komar); which surface; the regularity conditions; and the de Sitter-limit condition. **No Euclidean volume, uniform
interior, order-unity coefficient or GR exterior may enter silently** — each is an added completion, named and tested
separately, exactly as K6 required.

**A completion is ADMISSIBLE if and only if it introduces exactly one named assumption, is consistent with every
printed relation of the manifest sources, AND operates on at least one printed relation — a completion that is
itself the sole source of a mass bound is NOT admissible, because it supplies the content rather than completing
it.** A completion that contradicts a printed relation is **inadmissible** and
may not be considered. **The completion-free derivation — the one that adds nothing — is not itself a completion**,
but where §4 counts admitted floors it **is counted among them**, so that a printed floor and a differing
completion's floor are two floors and not one. *(The term carried the whole class structure while being defined nowhere, so whether an
"order-unity coefficient" counted as admissible when the printed relations already fixed a floor was a seat's
judgement, and two obedient seats could file different classes for the same physics.)*

### 2a. The frozen source manifest — the only sources this study may read

Digests are of the raw bytes, computed 2026-09-04 in this lane. **Every source below was confirmed by its own
content, not by its filename**; the bibliography's own file references would have bound entry 55 to a different
paper. Paths are relative to this document.

| entry | paper | path | sha256 | bytes |
|---|---|---|---|---|
| 18 | Dymnikova (1992), *Vacuum nonsingular black hole*, GRG 24, 235 | `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` | `2f3ca3e10ec016eed83104750d11d2428d5523c712814f68d559724d8b2c6b6f` | 18761 |
| 19 | Dymnikova (2019), *Universes Inside a Black Hole with the de Sitter Interior*, Universe 5, 111 | `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` | `ded87358184a4239d9f5bd0ffe8c5aee7732e992fc00be8f97370e73cbc7af47` | 34214 |
| 20 | Bronnikov, Melnikov & Dehnen (2007), *Regular black holes and black universes*, GRG 39, 973 | `../bhu-reading-20260823/sources/gr-qc_0611022_clean.txt` | `6616e3115dbdabd3173656320b86a3ca8e32d320b34f7e39402946f8fb765c92` | 47876 |
| 55 | *Asymptotically de Sitter universe inside a Schwarzschild black hole*, PRD 102, 066010 (2020) | `../bhu-reading-20260823/sources/2007.06664_clean.txt` | `b34183bf58eb36d6745262816a6736e8f43c9f7ed11c852c80c7a3e7a378d8be` | 194150 |

**A read outside this manifest files `DYM_SOURCE_BLOCKED`.** Entry 18's text is a PDF extraction, so C1 compares it
with `repr()`. *(Entry 18 also has an author restatement at `ar5iv_gr-qc_0201058_dymnikova_restatement.html`; it is
**not** in the manifest and may not be read as a source for this study, because a restatement is a different
artefact and admitting it would let the choice of artefact choose which relations exist.)*

### 2b. Measured constants — the closed list

`G = 6.67430e-11` m³ kg⁻¹ s⁻², `c = 2.99792458e8` m s⁻¹, `ħ = 1.054571817e-34` J s,
`k_B = 1.380649e-23` J K⁻¹, the solar mass `M_☉ = 1.98892e30` kg, and the age of the universe
`t_0 = 13.797` Gyr `= 4.3539e17` s, **using the Gregorian year of 365.2425 × 86400 s** *(the Julian year gives
4.3540e17; the convention was unstated, and the year length is a value not otherwise in this list)*. **No other value may be
introduced as "standard"**; anything else is an added completion under C2.

The **Planck mass** is not listed separately because it is derived from the above:
`m_P = sqrt(ħc/G) = 2.176434e-8 kg`. **Every comparator value in C6 is likewise computed from this list inside this
document**, which is what makes condition 5 executable without reading anything outside the manifest.

### 2c. The census, and how its exhaustiveness is demonstrated

**Before choosing a limb or an outcome, each seat constructs and prints an exhaustive census** of every equation or
sentence in the pinned Dymnikova sources that mentions or relates **core scale, density, mass, mass function, radius,
horizon, matching surface, regularity, or the de Sitter limit**. Every row, included or excluded, carries source path,
page/line locator and verbatim text. **Exclusion is permitted only for a predeclared reason code** —
`WRONG_BRANCH`, `DEFINITION_ONLY`, `NO_MASS_OR_SIZE_CONTENT`, `DUPLICATE` — **demonstrated by that independent source
text**. Disagreement or missing evidence is `UNRESOLVED`, **may not be treated as absence**, and forces
`DYM_SOURCE_BLOCKED`.

**Exhaustiveness is demonstrated by accounting for every line, not by a keyword search.** For each manifest source
the seat **prints the complete extracted text with stable line numbers and assigns every non-blank line exactly one
census disposition**: its own included row, its own excluded row under a predeclared reason code, or a `DUPLICATE`
row naming the covering row. **An equation and its defining or context lines may be treated as one explicitly
bounded block** with a single disposition, provided the block's line range is printed. **The seat prints a
reconciliation line per source giving the count of non-blank lines and the count of assigned dispositions; the two
must be equal, and a source whose counts differ fails C2.** *(Without the count, an omitted line is invisible in an
artefact that is otherwise enormous; with it, omission shows up as arithmetic.)*

**In addition, and as a cross-check on the blocking, every numbered or displayed equation in each manifest source
appears as its own census row** — cited by equation number, or by page/line locator where the display is unnumbered
— **and the seat prints each source's full equation list as part of the same C2 artefact.**

The eleven terms `core`, `scale`, `density`, `mass`, `mass function`, `radius`, `horizon`, `matching`, `surface`,
`regular`, `de Sitter` are retained **only as a search whose output is printed for the reviewer's convenience. They
are not the enumeration key, and no row may be justified by their absence.** *(They were the key in V4, and every
one of them is an English word. A size–mass binding in a gravitation paper is overwhelmingly likely to be a bare
displayed equation — `r_0² = 3/Λ`, `m(r) = …` — which contains none of the eleven strings, produces zero hits and
never becomes a row. Both blind seats are lane seats, so a shared blind spot reproduces in both, and a re-runnable
key blind in the same place reproduces it a third time. The omitted-versus-excluded distinction the design claimed
to have mechanised held only for prose — precisely not for the relations this study exists to find.)*

**The shape/magnitude pattern record and every prior lane conclusion are forbidden as evidence
for inclusion, exclusion or outcome selection**; the pattern enters this study at exactly one point — C6's breaker
evaluation — and only after a **positive-floor class** has been reached on other grounds
(`DYM_FLOOR_DERIVED` or `DYM_FLOOR_UNDERDETERMINED`).
*(This sentence still described the single-class gating that V10 removed — a repair scar. The whole
document was swept for others; §8b's account of the prior state is history and stays as written.)* C2 passes only if this census is printed in
full. *(Without it a seat could report a relation absent, omit the contrary row, and let the lane's own pattern become
indirect support for its own confirmation: C3 tests an injected relation only after the seat has already selected the
source-pinned equations, so it cannot see a relation excluded before that selection.)*

## 3. Limb structure

**Limb A (~1 seat-day):** attempt to reproduce, from the stated inputs, a printed relation **binding size to mass
OR bounding the mass at all**. If none is reproduced after the complete census of §2, report that **a relation
binding size to mass, or bounding the mass, was unreproduced from the stated inputs**, file
`DYM_NO_SIZE_MASS_RELATION`, **record C3, C4 and C6 as `NOT_RUN` while C0, C1, C2, C5 and C5b remain reached and
carry their actual results**, and stop. *(Two defects, one from each seat. kimi: §3 stopped whenever no SIZE–MASS
relation was reproduced, while §4's table and class 3 both required that NO mass bound of any kind was reproduced —
so a printed direct mass bound with no `V(M)` was routed to opposite places by clauses that were supposed to agree.
codex: the limb-A exit named no control dispositions, while §9 permits `NOT_RUN` only where the document explicitly
makes a control unreached.)* *(The wording matters: the class records what this lane
could not reproduce, not a claim that the branch contains no such relation.)*
**Limb B:** if it does, derive the floor and test it against the five breaker conditions.

## 4. Outcome classes — six declared: four scientific outcomes and two non-scientific terminal states

**Definition, so classes 1, 2 and 4 have a common discriminator:** a **positive floor** means a **strictly positive
greatest lower bound of the allowed mass set, whether or not that bound is attained**; a **unique floor** means the
unique infimum of that set. *(Both seats found this: "floor" alternated between a lower bound and an attained
minimum, so a solution set like `M ∈ (1,2) kg` sat in class 5 under one reading and class 1 or 2 under the other,
and two obedient seats could file differently on identical physics.)*

**How the four scientific classes partition the cases — a decision procedure, not four descriptions.**
An **admissible reading** is either the **completion-free derivation** (the printed relations with nothing added)
or **the printed relations plus exactly one admissible completion**. Each **consistent** admissible reading either **yields a
positive floor** — a strictly positive greatest lower bound of its **non-empty** allowed mass set, attained or not
— or **permits masses approaching zero**, meaning no positive lower bound follows from it. **An admissible reading
whose printed relations are mutually inconsistent has an EMPTY allowed mass set: it is neither of those, and it
goes in a third set `I`.** *(The dichotomy previously admitted no third case, so an inconsistent reading — a paper
whose printed relations contradict each other, which is not hypothetical in this corpus — belonged to neither `P`
nor `Z` and fell out of the partition entirely.)*

Let **`P`** be the admissible readings that yield a positive floor, **`Z`** those that permit zero, and **`I`**
those that are inconsistent — empty allowed mass set. **Every admissible reading lies in exactly one of `P`, `Z`,
`I`.** Then:

| condition | class |
|---|---|
| **LIMB A EXIT.** After the frozen census of §2, **a relation binding size to mass, or bounding the mass, was unreproduced from the stated inputs**, so limb B is never entered | **3** `DYM_NO_SIZE_MASS_RELATION` |
| **LIMB B ONLY — at least one relation IS printed.** `P` is empty and `Z` or `I` is non-empty: **a positive floor was unreproduced from the stated inputs** | **4** `DYM_NO_POSITIVE_FLOOR` |
| **`P` is non-empty** and the readings **disagree** — `P` holds two different floors, or **`Z` is non-empty**, or **`I` is non-empty** | **2** `DYM_FLOOR_UNDERDETERMINED` |
| **`P` non-empty, all of `P` agree on one floor, `Z` AND `I` both empty** — which requires the completion-free reading to be in `P` | **1** `DYM_FLOOR_DERIVED` |

**Note on the state that has no class of its own.** A floor that exists **only under completions, with every
completion agreeing**, was formerly class 5, `DYM_FLOOR_COMPLETION_DEPENDENT`. **That state still occurs and still
files — as `DYM_FLOOR_UNDERDETERMINED` (class 2) — and that is correct, not a place to hide it.** If the
completion-free reading yields no floor while completions yield 10 kg, the admissible readings **genuinely
disagree**: one says no positive bound follows, the others say 10 kg. Disagreement among admissible readings **is**
underdetermination, which is what class 2 records. **The seat must still report every reading and what it yields**,
so the completion-dependence is visible in the filing even though it no longer has its own label.
*(Retired by Duho's ruling — see §8e. The state is not homeless: it is named here and routed.)*

**Class 3 is reached ONLY from limb A; classes 1, 2 and 4 ONLY from limb B. They are therefore disjoint by the
limb that files them, not by any predicate — and classes 1, 2, 4 partition limb B exhaustively. NO precedence rule
is needed, and none is stated.**

> ### Why this boundary kept failing, stated as a finding rather than repaired again
>
> **`DYM_NO_SIZE_MASS_RELATION` and `DYM_NO_POSITIVE_FLOOR` are not two physical states.** If nothing is printed
> constraining the mass, then the completion-free reading imposes no lower bound, so it lies in `Z`, `P` is empty,
> and class 4's predicate is **satisfied**. **Class 3 entails class 4 — by meaning, not by wording.** "No relation
> printed" is a *reason* no floor follows; "permits zero" is the *consequence*. Cause and effect, not alternatives.
>
> **And they are different KINDS of thing.** Class 3 is **procedural** — limb A's exit, decided before any
> completion is considered. Class 4 is a **state predicate** over readings that include completions. **Mixing a
> procedural exit into a state partition is the category error**, and it is why three predicate-level repairs
> failed in succession: **you cannot separate by predicate two things that differ only in when you stopped
> looking.** The repair above therefore separates them by **limb**, which is the actual difference.
>
> **The structural alternative is to retire class 3** and fold it into class 4 with a required reason field
> (`NO_RELATION_PRINTED` / `RELATIONS_PERMIT_ZERO`). **That is not done here: retiring a class is Duho's ruling,
> not mine**, and it is flagged for him as the candidate structural fix if the limb separation does not hold.
>
> **This is attempt three on this specific defect.** If a gate finds this same overlap again, the third-failure
> rule fires: **stop, file a diagnosis, and wait** — no fourth repair. *(V11 carried one, and it was the defect: class 4's
"permit" was written as "no positive lower bound follows", which is **exactly** class 5's own precondition, so
every class-5 case also satisfied class 4 and class 4's precedence took it — **making class 5 unreachable**. The
repair that widened C6 to three positive-floor classes had left one of the three dead. Requiring **P to be empty**
for class 4 — no admissible reading rescues a positive floor — separates them, and the mixed case, where one
reading gives a floor and another permits zero, now lands in class 2 where the genuine freedom belongs.)*

1. **DYM_FLOOR_DERIVED** — as partitioned above. Report the formula and value, **and test it against all five
   breaker conditions**; if it passes them, this is a counterexample to the pattern and the pattern record must be
   amended. **If any breaker condition FAILS under its stated decision rule, `DYM_FLOOR_DERIVED` is still filed**
   and the failed condition is reported with its artefact: **the floor stands, it is not a counterexample, and the
   pattern record is not amended.** *(A breaker condition failing on its own decision rule is a **substantive
   physics result, not a control failure**, and does not engage the control-clean rule of `R3D_NO_CLASS`.)*
2. **DYM_FLOOR_UNDERDETERMINED** — as partitioned above. **This class also carries the completion-dependent state**
   formerly held by the retired class 5: a floor arising only under completions. **Report every admissible reading
   and what it yields**, including any that permits zero, and **name any completion a floor depends on**; report the freedom and **choose none**. **Where `P` holds more than one floor, C6 is evaluated SEPARATELY ON EACH
   floor in `P`, the per-floor artefacts are printed, and `C6_BREAKER_TEST=PASS` exactly when every per-floor
   evaluation satisfies all five decision rules.** *("The quantity the seat actually FILED" otherwise had no unique
   referent here, since the seat is told to choose none — two obedient seats could evaluate different floors, split
   C6 inside one class, and send a case with a scientific answer to `DYM_SOURCE_BLOCKED`.)* **C6 is RUN on this class** and its
   result reported: a surviving freedom is what condition 3 rejects, so it is expected to fail — but the failure
   must be **exhibited**, not assumed. **If `C6_BREAKER_TEST=PASS` results here instead — every per-floor
   evaluation satisfying all five decision rules while the readings still disagree — then EACH floor in `P`
   independently passes the breaker, and the study reports that outcome with all floors named. It is NOT a single
   counterexample and the pattern record is NOT amended on it, because no unique magnitude was fixed: what passed
   is a family, and the pattern concerns a construction fixing A magnitude. The result is reported as
   `C6 PASS under an underdetermined floor` and referred to Duho.** *(The class previously stated only what a C6
   FAIL meant here and left a reachable `PASS` with no stated consequence.)*
3. **DYM_NO_SIZE_MASS_RELATION** — limb A's exit: **a relation binding size to mass, or bounding the mass, was
   unreproduced from the stated inputs** after the frozen census of §2 was completed.
4. **DYM_NO_POSITIVE_FLOOR** — as partitioned above. Report the family. If the printed relations are mutually
   inconsistent, **report that a consistent solution, and hence a positive lower bound, were unreproduced from the
   stated inputs**, file here, and **reproduce the contradiction.**
5. **DYM_SOURCE_BLOCKED** — a required pinned source **cannot be read, or its computed identity does not match the
   frozen manifest of §2a, or a required source-dependent proposition is `UNRESOLVED`, or a required bounded
   procedure remains undecidable after its specified fallback.** The study **waits**; this is not a
   scientific verdict and must never be reported as one. **This class exists because the gate found §7's
   "reports BLOCKED if not" had no class behind it, so the run would have stalled.**
6. **R3D_NO_CLASS** — **only after ruling out `DYM_SOURCE_BLOCKED`:** if **no** evidence is unread or unresolved
   and, after applying the seat-split rule of §9, a required control still fails after two attempts **in any seat**,
   file `R3D_NO_CLASS`; **otherwise file `DYM_SOURCE_BLOCKED`.** *(Class 6 said only that a source "cannot be read",
   which is narrower than the failure it causes, so an unread source satisfied both classes.)* **A scientific class may be filed only from a seat report in which every reached
   control passed**; if the two seats return the same scientific class but **at least one** report is not control-clean —
   **or if, after a different-class split, the third seat's adjudication agrees with a seat whose report is not
   control-clean** — **the third seat re-runs each failed control of that report once. If any re-run control fails again, that is the persistent
   failure named above and `R3D_NO_CLASS` is filed. If every re-run control passes, that class is filed.**
   *(The rule previously covered "exactly one" clean report, so the zero-clean case — both seats agreeing on class,
   floor and C6 outcome while each fails a DIFFERENT control — convened no split, exhibited no persistently failing
   control, and fell through to `DYM_SOURCE_BLOCKED`, whose definition would have been false of it.)* *(The old wording said "in both seats", so a control failing persistently in one seat,
   with the seats otherwise agreeing, had no rule and two readings of the document diverged at the terminal step.)*

## 5. Controls, each with an exact named code

- **C0 — reachability, run BEFORE the freeze.** For **every declared outcome class of §4**, **exhibit a concrete
  input that produces it**: a specific numeric value or stated configuration, and the path it takes through this
  document to that verdict. For **every C6 breaker condition**, **exhibit valid inputs producing PASS and FAIL** —
  **Condition 5's FAIL exhibitions must include one input per comparator row, the Planck row included** — an
  exhibition touching only one comparator would not have seen a degenerate interval excluding its own value.
  **Except that a condition logically ENTAILED by the entry criteria of every class on which C6 runs is marked
  `ENTAILED` instead: prove the entailment, and exhibit a malformed filing that the condition rejects.**
  *(Without the `ENTAILED` route, C0 demanded a reachable substantive failure for a condition that valid membership
  makes impossible, so a sound document could never freeze — a defect in the control itself, found by a gate.)* **A class or condition for which no such input can be exhibited is UNREACHABLE, and this
  preregistration does not freeze until it is.** The exhibition table is the artefact.
  **The exhibitions are authored by a seat and only verified by Tori** — deciding what counts as reachable is where
  an author's prior would enter, so the author does not decide it. **This control emits
  `C0_REACHABILITY=PASS|FAIL|NOT_RUN` from the exhibition actually run against this version; the token is a result
  to be recorded, not a claim this document makes about itself.** *(It previously ended with a bare
  `C0_REACHABILITY=PASS`, which reads as the document certifying its own pass — and did so while §8 recorded a
  failing exhibition. A control cannot certify itself in its own text.)*

  *(Added V9 by Duho's order. This control exists because three consecutive repairs left condition 5 unable to
  return PASS on any path, each time in a different way, and no other control here could see it: every other
  control checks that something is **done correctly**, and none checks that an outcome **can happen at all**. The
  check is not speculative — it is exactly what both seats did when asked to trace a matching and a non-matching
  case, which is how V6's soundness and V7's defect were established. It was being run by referees after dispatch
  instead of by the lane before it.)*

- **C1 — source identity, bound to the frozen manifest of §2a.** The seat prints the computed SHA-256 of the raw
  bytes of **every** file it reads, with `repr()` of the extracted text where the pinned text is PDF-extracted.
  **Each printed digest must equal its manifest value**; a mismatch, or any read of a source outside the manifest,
  files `DYM_SOURCE_BLOCKED`. The printed digests are the artefact; a claimed pass without them fails.
  This control emits `C1_SOURCE_IDENTITY=PASS|FAIL|NOT_RUN` from the run actually executed; the token is a result to be recorded, not a claim this document makes about itself. *(Previously "source identity" was identity to nothing named: the document bound no
  path and no expected hash, so a seat could pass having read a different extraction, edition or truncation — and
  choosing which artefact counts as the source chooses which relations exist.)*
- **C2 — completion ledger, printed in full.** The seat prints **a row for every candidate premise or relation
  considered**, with status `SOURCE_DERIVED`, `ADDED_COMPLETION` or `UNRESOLVED`. Every `SOURCE_DERIVED` row carries
  the **pinned source path, page/line locator and verbatim supporting text**; every `ADDED_COMPLETION` row names the
  assumption added. **The full printed ledger is the artefact required for the pass; a summary assertion fails.** An
  `UNRESOLVED` row may not be excluded and forces `DYM_SOURCE_BLOCKED`. This control emits `C2_COMPLETION_LEDGER=PASS|FAIL|NOT_RUN` from the run actually executed; the token is a result to be recorded, not a claim this document makes about itself.
  *(As written, C2 could be passed by saying it had been done. That is fatal here specifically: relabelling or
  omitting one candidate relation manufactures the no-relation or underdetermined result.)*
- **C3 — deletion probe, K6's corrected form:** delete the **source-pinned field equations**; if a unique floor
  survives on an injected relation alone, that relation is circular and no derived-floor class may be filed.
  **The harness must execute the deleted state and print its captured output**; a claimed pass without that output
  fails. This control emits `C3_DELETION_PROBE=PASS|FAIL|NOT_RUN` from the run actually executed; the token is a result to be recorded, not a claim this document makes about itself. **The probe is the committed script `r3d_c3_deletion_probe.py`, invoked as
  `python3 r3d_c3_deletion_probe.py relations.json`** — the JSON file `relations.json` carries `target`, `symbols`, the §2b `constants`
  list, and one record per relation with `id`, `origin` (`SOURCE_PINNED` or `INJECTED`) and `expr`. It prints the
  retained ids, the deleted ids, the injected relations, and the solve result with and without the pinned
  equations, exiting **0 on PASS, 1 on FAIL, 2 on NOT_RUN**. **A floor is DETERMINATE when its free symbols all lie
  in §2b**; the probe files FAIL — circular — when a determinate floor still follows from the injected relation
  alone. *(Supplied rather than promised, with a passing positive control — injected `M = 3·sqrt(ħc/G)` alone fixes
  the floor, FAIL, exit 1 — and negative control — injected `r₀ = 2GM/c²` alone leaves `M` free in `r₀`, PASS,
  exit 0. The probe's first version failed its own positive control by demanding zero free symbols, which scored a
  determinate Planck-scale floor as indeterminate and would have left it blind to circularity; the control caught
  that before the script was cited here.)*
- **C4 — GR benchmark.** For every relation used, the seat **prints the stated-limit algebra** showing equality with
  the Schwarzschild form in the exterior limit, **and prints the premise list** for that algebra showing that no
  interior premise entered. The printed algebra and premise list are the artefact; a claimed pass without them
  fails. This control emits `C4_GR_BENCHMARK=PASS|FAIL|NOT_RUN` from the run actually executed; the token is a result to be recorded, not a claim this document makes about itself.
- **C5 — harness, LIVE.** Execute and print the three commands of §9. This control emits `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN` from the run actually executed; the token is a result to be recorded, not a claim this document makes about itself.
- **C5b — path list.** Print every opened path and, **for each path, print `IN_SCOPE` or `OUT_OF_SCOPE` together
  with the exact §9 scope-rule clause applied.** Any `OUT_OF_SCOPE` row **fails** the control. **The complete
  per-path table is the required artefact; a claimed pass without it fails.** This control emits `C5B_PATH_LIST=PASS|FAIL|NOT_RUN` from the run actually executed; the token is a result to be recorded, not a claim this document makes about itself. *("Check it"
  named no printed comparison, so the check itself was assertion.)*
  Unreached C5/C5b are recorded `NOT_RUN`, never `PASS`. *(Both codes were previously implicit in "as R3A/R3B";
  a control whose code is not named in the document it governs cannot be checked against it.)*
- **C6 — breaker test.** **Applies on EVERY outcome that yields a positive floor — `DYM_FLOOR_DERIVED`
  and `DYM_FLOOR_UNDERDETERMINED`** — and is `NOT_RUN`, never a pass, **only where C6 was never
  engaged** — `DYM_NO_SIZE_MASS_RELATION`, `DYM_NO_POSITIVE_FLOOR`, or a `DYM_SOURCE_BLOCKED` / `R3D_NO_CLASS`
  filed **before any C6 evaluation**.

  **The conditions are evaluated on the quantity the seat actually FILED as its floor, not on an idealised one.**
  If a seat files a quantity that is not a mass, condition 1 **fails** — that is the check, and it is why condition
  1 is evaluated rather than assumed.

  *(V10, and this is the repair of the C0 failure. Gating C6 behind a single class meant the breaker test could
  return FAIL on **one path out of seven**, and `NOT_RUN` on every other — so counterexample status was decided by
  **class assignment** rather than by the falsifier. `DYM_FLOOR_COMPLETION_DEPENDENT` said outright that "the
  pattern record is not amended, because the floor is not completion-free" **without the conditions ever being
  evaluated**. That is a verdict about the pattern reached by fiat. Under V10 the same conclusion must be **earned
  by condition 2 or 3 failing**, on the record, with its artefact.)* The five conditions are **copied verbatim below** from `SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md`,
  **V2**, sha256 `5232201acfdca850c7e8a4d345aad145a3d91fdb750fdbb9a77fb43fec8d4647`, so that evaluation does not depend on an
  unpinned lane-authored text that may drift between seats. **Evaluation against any condition text not pinned here
  fails C6.**

  > 1. **An observable magnitude is computed** — a strain, an amplitude, a power, a mass, a percentile — not a shape,
  >    scale, frequency, sign, ratio or functional form.
  > 2. **Every constant in it traces** to the construction's own equations or to measured fundamental constants. No
  >    coefficient introduced as "the simplest form", "we assume", "we choose", or "following [ref]" without that
  >    reference itself deriving it — the R3A test, run to the end of the citation chain.
  > 3. **No free normalisation survives** the derivation: replacing every parameter by a free symbol and demanding
  >    the printed number back **must SUCCEED with no parameter chosen**. **If the number can be recovered only once
  >    a parameter is chosen, a free normalisation survives and this condition FAILS** — the C4 free-symbol probe.
  > 4. **No fixity is assumed** where the falsifiability depends on it — the R3B test. If the prediction is rigid
  >    only because a quantity is held constant by choice, the constancy must itself be derived.
  > 5. **A measurement could falsify it**: the number is not shared with ΛCDM or with any standard model that would
  >    make the same prediction for unrelated reasons.

  **Decision rules, one per condition, each with its artefact:**

  | # | proposition | bounded procedure | pass criterion | artefact |
  |---|---|---|---|---|
  | 1 | the derived floor is an observable magnitude | classify the derived quantity's dimension | dimension is mass (kg or M☉), not dimensionless and not a shape/scale/ratio | the printed dimensional analysis |
  | 2 | every constant **of the derived floor** traces | **Scope: the constants appearing in the construction's own derived magnitude. The frozen comparator conventions of condition 5 are not constants of the derived floor and are not tested here.** Trace each such constant **using only the verbatim source passages reproduced in the frozen C2 artefact**, through at most the relations in those passages | every constant terminates in an equation of a §2a manifest source or in the §2b list. **The chain is followed only within the manifest: a terminus outside it fails, exactly as a `we assume / we choose / simplest form` terminus fails** | the full provenance table, one row per constant |
  | 3 | no free normalisation survives | replace every non-§2b parameter by an **algebraically independent symbol**, simplify the final expression **once** with **the seat's SymPy, whose printed version is part of the C5 artefact and must match between the two seats or C5 fails**, under the 120-second cap | **PASS exactly when the simplified expression contains none of those symbols** — i.e. the printed number is recovered with no non-§2b parameter chosen. On timeout, run **§9's fallback row "free-symbol survival"**, which decides this condition's own proposition; if that row is absent, times out, or cannot parse the expression, condition 3 is `UNDECIDED`, C6 does not pass, and the run files `DYM_SOURCE_BLOCKED` | the printed free-symbol run and its outcome |
  | 4 | no fixity is assumed | list every quantity held constant in the frozen derivation and identify its deriving passage **using only the verbatim source passages reproduced in the C2 artefact** | **every row has such a passage**; a held-constant quantity with no manifest derivation fails | the fixity table with a source line per row |
  | 5 | a measurement could falsify it | the comparator table below, executed in full | **no** comparator matches within tolerance | the completed comparison table |

  **Condition 5's comparator set, observable, tolerance and corpus — supplied here, computed here, and read from
  nowhere.** The observable is **the minimum black-hole mass, in kilograms**.

  **Condition 5 quantifies ONLY over the three finite numerical comparators enumerated below**, not over "any
  standard model" — a universal negative over an unbounded set is not decidable and is not claimed.

  **Every comparator interval is computed in this document from §2b constants together with the stated
  dimensionless inputs** — the single-species lifetime coefficient `5120π`, row 2's upper-end factor `3.0`, row 3's
  span `[2.2, 2.9] M_☉`, and the Gregorian year length inside `t_0`. **Those four are frozen COMPARATOR
  CONVENTIONS — not constants in the derived floor, and not derivations from §2b.** Each is **printed in the
  completed condition-5 comparison artefact**, **does not enter the C2 completion ledger**, and is **outside C6
  condition 2's provenance test**, which tests the provenance of the constants in *the construction's own derived
  magnitude*, not of the scaffolding that magnitude is compared against. No comparator source file
  is in the manifest, none may be read, and **none needs to be read**: the numbers below are the frozen artefact.
  *(V6 claimed every interval was "derived from §2b". That was false — three coefficients and a year convention are
  asserted — and both seats caught it. The values were supplied rather than deferred, which was the point, but
  calling an assertion a derivation is the same overclaim in smaller form, so the assertions are now named and
  routed through the provenance rule that governs every other constant in this study.)*

  **Comparator endpoints are rounded OUTWARD throughout the table. For a DEGENERATE interval, "outward" widens the
  point one unit in the last printed digit on each side** — a point cannot be rounded outward, and the convention
  silently failed at exactly that row. *(V6 rounded them inward, so the printed
  interval `[1.730e11, 5.189e11]` did not contain its own computed lower value `1.7298245e11`. Inward rounding
  narrows a comparator, which makes an overlap — and therefore a condition-5 failure — marginally less likely, i.e.
  it biases the study toward declaring a counterexample. The bias was small and unintentional; the convention is
  now stated so it cannot recur silently.)*

  | # | comparator hypothesis | interval (kg) | derived here from §2b by |
  |---|---|---|---|
  | 1 | semiclassical GR + QM: a Planck-scale remnant | `[2.176433e-8, 2.176435e-8]` | `m_P = sqrt(ħc/G) = 2.1764343e-8` kg at §2b's precision; **a point cannot be rounded outward, so the printed point is widened one unit in the last printed digit each side** |
  | 2 | Hawking evaporation: the mass just evaporating at the present epoch | `[1.729e11, 5.190e11]` | lower end `M = (t_0 ħ c⁴ / 5120π G²)^(1/3) = 1.7298e11` kg, **rounded down**, from the single-species lifetime `τ = 5120π G² M³/(ħc⁴)` set to `t_0`. **Upper end = 3.0 × the unrounded lower = 5.1895e11 kg, rounded up.** The factor 3.0 is an **asserted bound**, not a derivation: emission into additional species shortens the lifetime at fixed mass and so raises the surviving mass, and the interval is widened to contain that case rather than a single figure being asserted |
  | 3 | stellar collapse: the TOV / neutron-star maximum mass | `[4.375e30, 5.768e30]` | `[2.2, 2.9] M_☉`, an **asserted span** over which the TOV maximum is contested; `2.2 × 1.98892e30 = 4.375624e30` **rounded down to 4.375e30**, `2.9 × 1.98892e30 = 5.767868e30` **rounded up to 5.768e30** |
  | — | ΛCDM | *no interval — predicts no minimum black-hole mass* | recorded so the null case is explicit rather than silently skipped; **it can never match, and that is stated rather than left to be inferred** |

  **Decision rule — stated as a single disjunction, deliberately.** The seat states its derived floor as an
  interval (a point value is a degenerate interval).

  > **Condition 5 FAILS if, and only if, that interval OVERLAPS one of the comparator intervals above — and the
  > seat names the comparator it overlaps. Otherwise condition 5 PASSES.**

  **There is no other precondition on the pass.** If the floor lies within one decade of a comparator without
  overlapping it, the seat prints `NEAR_MATCH` with the comparator named — **reported, never decisive**, since a
  decade is a reporting convenience on a scale spanning sixty and must not decide a falsification.

  **The completed four-row comparison table, including ΛCDM, is required as a C6 ARTEFACT — not as a precondition
  of the pass.** An incomplete or missing table **fails C6 as a control**, loudly and by name
  (`C6_BREAKER_TEST=FAIL`, reported with what is missing).

  **C6's three outcomes, stated in full so the pass is not left implicit:**
  **`C6_BREAKER_TEST=PASS`** — the table is complete and **every one of conditions 1–5 satisfies its own stated
  decision rule**. **`C6_BREAKER_TEST=FAIL`** — the table is incomplete or missing, **or** any condition fails its
  decision rule; **name the condition and print its artefact**. **`C6_BREAKER_TEST=NOT_RUN`** — **C6 was never engaged**: no
  positive-floor class was entered (`DYM_NO_SIZE_MASS_RELATION`, `DYM_NO_POSITIVE_FLOOR`), or
  `DYM_SOURCE_BLOCKED` / `R3D_NO_CLASS` was filed **before any C6 evaluation**. *(A run that entered C6 and hit
  condition 3's `UNDECIDED` produced a positive floor and DID engage C6, so it records `FAIL`, not `NOT_RUN`,
  even though its filed class is `DYM_SOURCE_BLOCKED`. Two clauses previously assigned opposite codes to that one
  path.)* **If condition 3 is `UNDECIDED`, record
  `C6_BREAKER_TEST=FAIL`** with the failed primary and fallback artefacts, then file `DYM_SOURCE_BLOCKED` — so
  PASS, FAIL and NOT_RUN are exhaustive and mutually exclusive, and "does not pass" is never a fourth state.
  *(Recall that a condition failing its decision rule is a **substantive result**: under §4 class 1
  the floor still stands and is filed, it is simply not a counterexample.)*

  *(This polarity is the V9 redesign, ordered after the diagnosis in
  `R3D_FALSIFIER_DISABLING_DIAGNOSIS_20260904.md`. Condition 5's pass was previously a **conjunction** — a complete
  table, every comparator derived, every provenance accepted, no overlap — while its failure was a **disjunction**,
  one overlap. A conjunction has far more surface area, so a drafting error anywhere in the document landed on the
  pass, and the test that can refute this lane's own pattern came out of three consecutive repairs unable to fire,
  in three different ways. **Making the pass a disjunction leaves nothing for a drafting error to break.** The
  completeness requirement is not dropped: it moves from a place where an unmet requirement is silent — an
  unreachable pass — to a place where it is loud — a failed control. Every one of the three disablings was silent.
  The cost is stated rather than hidden: a lazy comparison now yields a PASS, and PASS is the high-stakes
  direction. That risk is accepted because it is **inspectable** — it produces a printed table that the second
  seat, the audit and the principal can all check — whereas a disabled falsifier survived four rounds unnoticed.)*
  *(Third round on this condition, and it is worth being exact about how it failed twice. V3 required a comparator
  set to be fixed "before the run is frozen" — but this document IS the frozen artefact, so the requirement was
  satisfied nowhere. V4 supplied values while citing two source files that §2a forbids reading, and labelled one of
  them as being in the manifest when it is not: a seat that read them violated §2a and filed `DYM_SOURCE_BLOCKED`,
  and a seat that did not read them hit "an unread comparator source files `DYM_SOURCE_BLOCKED`". Both paths
  blocked, so the decisive test was pre-disabled a second time in a new form. The fix is not another requirement:
  every value above is computed from §2b here, so there is nothing left to read.)*

### 5a. On how many paths can the falsifier fail — stated here, not left to a gate report

**Two numbers, because one of them was wrong and the difference is the point.**

**Two different numbers, and conflating them was the defect both V17 seats found.**

**C6 is INITIALLY ENGAGED on 2 of the 6 outcome classes** — `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`,
the classes that yield a positive floor.

**Once engaged, `C6_BREAKER_TEST=FAIL` can be recorded in 4 terminal classes:** those two, **plus
`DYM_SOURCE_BLOCKED`** when condition 3 remains `UNDECIDED` after its fallback, **plus `R3D_NO_CLASS`** when an
engaged C6 is followed by a persistent control failure. *(§5a previously counted only the positive scientific
classes and called that the number of classes on which C6 can fail — but C6, once engaged, travels with the run
into a terminal class that is not one of the two it engaged from. Engagement and filing are different events.)*

**Reachable: 2. `DYM_FLOOR_COMPLETION_DEPENDENT` IS A DEAD CLASS** — shown unreachable by seat exhibitions on
**both V11 and V12**, for two different reasons.

On V11, class 4's "permit" was defined as "no positive lower bound follows", which is exactly class 5's own
precondition, so class 4 swallowed every class-5 case and its precedence took them. **V12's partition did not
revive it:** §4's dichotomy makes "yields no floor" identical to "permits zero", so a completion-free reading that
yields nothing is necessarily in `Z`, and class 5's requirement that `Z` be empty can never hold.

**The document therefore claimed a falsifiability it does not have — three declared routes to a breaker failure,
two that any case can actually travel.** The live pair is `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`.
**It is NOT repaired a third time**: see `R3D_C0_THIRD_FAILURE_FILING_20260905.md`, filed under the standing
instruction that a third failure in this direction stops the repair loop.

**That overstatement is exactly the fault this study exists to detect in other people's papers**, committed here,
which is why both numbers are printed rather than the flattering one.

**It is `NOT_RUN` on `DYM_NO_SIZE_MASS_RELATION` and `DYM_NO_POSITIVE_FLOOR`, and that is correct rather than a
gap:** those classes produce **no number to test**, so there is no candidate counterexample to evaluate — **a
breaker test run where there is nothing to test would report on nothing.** *(This sentence previously said
`NOT_RUN` on "the other 4" and named `DYM_SOURCE_BLOCKED` and `R3D_NO_CLASS` among them — contradicting the
paragraph three above it, which correctly says an ENGAGED C6 can travel INTO those two classes and record `FAIL`
there. The V18 repair corrected the count where the count was stated and left the consequence sentence saying the
old thing.)*

**Per condition, 4 of the 5 can fail substantively** — conditions 2, 3, 4 and 5 each have a concrete failing input.
**Condition 1 is different, and is labelled honestly rather than counted:** it is **`ENTAILED`** for any correctly
filed floor, since every positive-floor class requires a mass and a correctly filed floor therefore passes a
dimensional test. It is **retained as a filing-integrity check, not claimed as a reachable substantive failure**,
and fails only on a **malformed filing** — a seat entering a dimensionless ratio as its floor — which §5 catches
because the conditions are evaluated on the quantity actually filed.

*(This number is written here because it is the answer to the question that produced
`R3D_FALSIFIER_DISABLING_DIAGNOSIS_20260904.md`, and it should be checkable in the text rather than only in a gate
report. The two V10 seats split on condition 1 alone — one counted 4 of 5, the other 5 of 5 — and the split was
over whether a malformed filing counts as a reachable path. Both readings are recorded above rather than one being
chosen silently.)*

## 6. Non-circularity and fairness

K6's outcome may **not** be assumed to repeat: this is a different branch and the study must be able to return
`DYM_FLOOR_DERIVED`. The record's wording for any negative finding is **"unreproduced from the stated inputs," not
"error."** No tier, token, standing or stamp moves.

## 7. Seats, cost, scope

Blind double, third seat via the wrapper with ACCESS_SHA proof, independent second route, Kimi arithmetic with a
no-fallback control, check sheet, Tori re-runs everything, critic note before any ruling. Two to four seat-days;
sources believed in the lane — **limb A confirms that first and reports BLOCKED if not.** Paper HOLD; nothing outward.

## 8. Gate record

`R3CD_DRAFT_GATE_20260904_agy.md`: `GATE_D=PREREG_SOUND_WITH_REPAIRS`, **one repair applied** — C3 could have been
waved through without executing the deleted state, so the harness must now run it and print the captured output. The
gate confirmed D does **not** assume K6's outcome and that `DYM_FLOOR_DERIVED` is genuinely reachable. **That gate's
expectation about the branch is not evidence and is not carried into this document.**

**V3, this version.** `R3D_GATE_codex_20260904.md` gated `1ecb7ac7…6748f5` as `PREREG_UNSOUND` with five substantive
findings, **all applied**: outcome classes 2/3/4 made exclusive with an explicit precedence; C2 turned from an
assertion into a printed artefact; **an exhaustive printed census of candidate relations required before any limb or
outcome is chosen**, exclusion allowed only on a predeclared reason code shown from source text, and the pattern
record forbidden as evidence for inclusion, exclusion or outcome selection; C6 condition 5 given a bounded frozen
comparator set in place of an undecidable universal negative; the stall fallback and the two-seat split each given a
fileable class. codex found **no defect** in the re-run guard (§6) or the fairness wording and said so, and those are
unchanged. **Also fixed: the completion token sat before §9, so the document ran past its own terminator** — the same
defect found in R3C2's version history the same evening.

**V4. Both seats gated `872d4978…41080a`; neither read a moving file.** `R3D_GATE_V3_codex…` returned
`PREREG_UNSOUND`, `R3D_GATE_V3_kimi…` `PREREG_SOUND_WITH_REPAIRS` — **a split in label, not in content**: the two
agreed on class overlaps, on C1 and C4 being passable by assertion, on the census being an assertion, on C6's
conditions being unstated, and on the stall gaps.

**Two of those findings were my own repair failing in a specific way, and it is named here rather than absorbed:
V3 repaired condition 5 and the symbolic fallback by REQUIRING content instead of SUPPLYING it** — "before the run
is frozen, a comparator set is fixed in writing" — while this document *is* the frozen artefact. So V4 supplies:
a source manifest with real digests (§2a), the measured-constant list (§2b), a mechanical string-search
demonstration of census exhaustiveness (§2c), the five breaker conditions copied verbatim with the pattern
record's own hash, per-condition decision rules, a comparator table with values, tolerance and sources, and a
fallback table naming method, domain, precision and threshold.

**kimi additionally found two things codex did not**, both adopted: a **reachable result that fitted no class** —
a unique positive floor arising only under named admissible completions that all agree — now
`DYM_FLOOR_COMPLETION_DEPENDENT`; and that **§0 and §8 restated the pattern record's own verdict inside the frozen
document**, so a seat citing §0 bypassed the §2 prohibition without formally citing the record. Both sections are
de-patterned.

codex found no defect in the re-run guard; kimi found none in the re-run guard or the fairness wording, though
codex did find the fairness rule broken in limb A and in class 3's label. Both are repaired.

## 9. Inherited discipline, stated so no seat has to infer it

- **Harness, LIVE**: every seat executes and prints `python3 --version`,
  `python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 $(command -v python3)`.
  Transcribing expected values fails `C5_HARNESS_PINNED`. *(`sympy.__version__` was written as though it were a
  shell command; run literally it fails with "command not found", so C5 as frozen could not be executed as frozen
  and each seat had to either fail it or silently substitute something that worked.)*
- **No transcription, anywhere.** Transcribing expected values fails the control that required them. **This applies
  to C1 as well as C5**: §2a prints the expected digests in this same document, so **a digest copied from §2a rather
  than computed from the file's bytes in the seat's own run fails `C1_SOURCE_IDENTITY`.** *(The anti-transcription
  rule existed but was scoped to one control, while C1's artefact — "the printed digests" — sat next to the answers.)*
- **Access proof** (Duho's 2026-09-04 20:48 rule): any seat auditing a pinned source prints
  `ACCESS_SHA=<full 64 hex of that file>` as its first line. **No proof, no verdict** — the report is quarantined,
  exactly as `nm_referee_dispatch.sh` does.
- **Path list**: every seat prints every path it opened. **IN SCOPE:** this lane's own reading tree
  (`../bhu-reading-20260823/sources/`); **this preregistration**; **the committed script
  `r3d_c3_deletion_probe.py` and the JSON input the seat writes for it**; and **the seat's own working directory
  and artefacts**. **OUT OF SCOPE:** another lane's files, and any path not named above. *(The rule previously
  named only the reading tree as in-scope, while the design itself requires a seat to open this document, the probe
  and its input — so every mandated read would have been marked `OUT_OF_SCOPE` and failed C5b. A control that fails
  on the paths its own design requires is not a scope rule.)* That distinction is stated
  because getting it wrong once already produced a spurious `UNDETERMINED` (R3B §5).
- **Stall guard**: every symbolic operation under a 120-second cap. On timeout print `SYMBOLIC_TIMEOUT` and execute
  **the fallback row below** under a second 120-second cap. If the row is absent, times out, or does not decide its
  proposition, file `DYM_SOURCE_BLOCKED` and **do not pass the affected control**.

  | symbolic operation | fallback | domain and sample | precision | decision threshold | proposition decided |
  |---|---|---|---|---|---|
  | solve `g_tt(r)=0` for horizon radii | bracketed root-finding on detected sign changes — bisection on each bracketing interval, or `mpmath.findroot` seeded from the bracket | `r/r_g ∈ [1e-3, 1e3]`, 10⁴ log-spaced samples | `mp.dps=30` | root accepted if a sign change brackets it and `abs(g_tt) < 1e-20` there | "the metric has ≥1 horizon for given (M, r₀)" |
  | `r→0` limit of curvature invariants | direct evaluation at `r = 10^-k`, `k = 1…20` | as listed | `mp.dps=30` | finite if `abs(value) < 1e6` and monotone-convergent over the last five `k` | "the core is regular" |
  | **free-symbol survival** (condition 3) | expand the final expression into a frozen expression tree and traverse every node once, substituting only §2b constants | the whole expression; no sampling | exact, symbolic | **PASS iff the printed sorted set of free symbols contains no non-§2b symbol**; FAIL if it contains one | "no free normalisation survives" |
  | extremise the mass over the core scale | grid minimisation then local refinement | `r₀ ∈ [1e-3, 1e3] r_g`, 10⁴ log-spaced | `mp.dps=30` | positive floor accepted if the grid minimum is `> 0` and stable to `1e-6` relative under a 2× refinement | "a positive minimum mass exists" |

  *(The fallback was previously called "named" while naming nothing, so a timeout reached an instruction that could
  not be executed and the run could stall before its own second timeout.)*
- **Seat split**: if the two blind seats return **different terminal classes of any kind** — scientific,
  `DYM_SOURCE_BLOCKED` or `R3D_NO_CLASS` — **or the same scientific class with different `C6_BREAKER_TEST`
  outcomes, or with different reported floor formulas or values (classes 1 and 2), or different reported families
  (class 4)** *(reachable because conditions 2 and 4 are bounded by each seat's own C2 artefact and no rule forces
  the two ledgers to agree — so two control-clean seats could file one class while one certifies a counterexample
  and the other does not)* — **the third seat adjudicates exactly that split from the printed
  artefacts**, **re-executing any blocked read once before ruling**; its class is filed **only if it agrees with one
  of the two**. If all three differ, or the third seat cannot decide, file `DYM_SOURCE_BLOCKED`. **Every terminal
  path files exactly one declared class.** *(The rule previously engaged only on "different scientific classes", so
  one seat scientific and one blocked was a terminal disagreement that convened nobody and filed nothing.)*
- **Control status vocabulary — every control emits exactly one of its three exact tokens**, never a bare PASS:
  `C0_REACHABILITY=PASS|FAIL|NOT_RUN`, `C1_SOURCE_IDENTITY=PASS|FAIL|NOT_RUN`,
  `C2_COMPLETION_LEDGER=PASS|FAIL|NOT_RUN`, `C3_DELETION_PROBE=PASS|FAIL|NOT_RUN`,
  `C4_GR_BENCHMARK=PASS|FAIL|NOT_RUN`, `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN`,
  `C5B_PATH_LIST=PASS|FAIL|NOT_RUN`, `C6_BREAKER_TEST=PASS|FAIL|NOT_RUN`. **`NOT_RUN` is permitted only where this
  document explicitly makes that control unreached. A control IS explicitly unreached when an earlier control has
  already forced `DYM_SOURCE_BLOCKED` or `R3D_NO_CLASS` and the later control was never engaged: every such later
  control is recorded `NOT_RUN`, and every control that WAS engaged before the block carries its actual result.**
  *(An early terminal block — C1 finding a digest mismatch, C2 an `UNRESOLVED` row, a bounded procedure undecidable
  after fallback — previously left every later control's status unstated, while the global rule allowed `NOT_RUN`
  only where the document said so explicitly. It now says so explicitly.)* *(Most controls previously printed only a PASS token. A
  control that can only say PASS is not a control — this lane's own principle, applied to itself.)*
- **Unreached limbs**: controls recorded `NOT_RUN`, never as passes. **This exact underscore spelling applies to
  every unreached control throughout this document.**

**V5, this version. ORDERED by Duho: "fix condition 3 and re-check the six instances".** The pattern record is
amended to V2 (`5232201a…c8d4647`), so V4's pin `fff1f1a8…` went stale the moment the source was corrected. C6's
verbatim block, its pinned hash, and its condition-3 decision rule are updated to match — **the decision rule was
carrying the same inversion**, since it was transcribed faithfully from a defective source. `BREAKER_C3_RECHECK_20260904.md`
records the six-instance re-check: no instance's status changes.

**Nothing else is repaired.** codex's and kimi's V4 findings both stand: `admissible completion` is never defined;
two comparator sources sit outside the frozen manifest and one is falsely labelled as inside it, so condition 5
files `DYM_SOURCE_BLOCKED` on every path; the keyword census is blind exactly where physics relations live, because
a relation written only in symbols contains none of the eleven terms; conditions 2 and 4 still reach outside this
document. **R3D remains `PREREG_UNSOUND` and is NOT run.**

**V6, this version. ORDERED by Duho: "fix the three remaining defects and re-gate".** Both V4 seats returned
`PREREG_UNSOUND` on `19843627…`, neither read a moving file, and between them they raised more than three — all are
applied here.

**The decisive one, failed twice before.** V4's comparator table supplied values but cited two files that §2a
forbids reading, and labelled one of them as being *in* the manifest when it is not. A seat that read them violated
§2a and filed `DYM_SOURCE_BLOCKED`; a seat that did not hit "an unread comparator source files
`DYM_SOURCE_BLOCKED`". **Both paths blocked, so condition 5 could never pass and the study's own decisive test was
pre-disabled for the second consecutive round, in a new form.** V6 removes the reads entirely: **every comparator
interval is computed from §2b inside this document.** Condition 5 is also narrowed to the three enumerated numerical
comparators — a universal negative over "any standard model" is not decidable and is no longer claimed — and the
arbitrary one-decade tolerance is replaced by **interval overlap**, with a `NEAR_MATCH` flag that is reported and
never decisive.

**The census key was blind exactly where the physics is.** V4 enumerated by eleven English search terms, so a
relation printed only as symbols — `r_0² = 3/Λ`, `m(r) = …` — produced zero hits and never became a row, in both
blind seats and in the re-runnable key alike. **V6 accounts for every non-blank line** with an explicit disposition,
allows bounded equation blocks, and additionally requires **every numbered or displayed equation as its own row**.
The eleven terms survive only as a printed convenience and may not justify any row.

**`admissible completion` was never defined** while carrying the entire class structure, so two obedient seats could
file different classes for the same physics; it is now defined, and class 1 is guarded against an admissible
completion that yields a different floor. Classes 6 and 7 are ordered.

**Two executability defects, both kimi's:** C1's artefact is "the printed digests" while §2a prints the expected
digests in the same document, so the anti-transcription rule — scoped to C5 alone — is extended to C1; and
`sympy.__version__` was written as a shell command, which fails with "command not found", meaning **C5 as frozen
could not be executed as frozen**. Conditions 2 and 4 are confined to the C2 artefact's reproduced passages, and
condition 3 is given a bounded operation and decision.

codex found the re-run guard sound; kimi found the re-run guard, fairness and stall all sound, and noted that the
positive class's consequence was unreachable only because of the comparator defect now fixed. **R3D remains NOT
run.**

**V7, this version. ORDERED by Duho: "apply both and re-gate".** V6 (`14db4dfb…9e3f9e`) was gated by both seats
without the file moving: codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`. **Both independently
re-derived every comparator number and both reproduced all five**, and both confirmed the §9 commands execute.
codex found circularity **sound**; kimi found controls, re-run guard, fairness and stall **sound**. Both traced a
matching and a non-matching path through condition 5 and confirmed **the twice-blocked decisive test can now pass**.

**The overclaim, caught by both.** V6 said *"Every comparator interval is derived from §2b inside this document."*
**False**: the lifetime coefficient `5120π`, row 2's factor `3.0`, row 3's span `[2.2, 2.9] M_☉` and the Gregorian
year inside `t_0` are asserted, not derived — and V6's own row 2 admitted the factor was "stated as a bound, not
derived here" while the heading above it said "every". The values were supplied rather than deferred, which was the
repair's point, but **calling an assertion a derivation is the same overclaim in smaller form.** All four are now
named as asserted, recorded as `ADDED_COMPLETION` in the C2 ledger, and routed through C6 condition 2's provenance
rule like every other constant.

**A bias, small and unintentional, found by kimi.** V6's comparator endpoints were rounded **inward**, so
`[1.730e11, 5.189e11]` did not contain its own computed value `1.7298245e11`. A narrowed comparator makes overlap —
and therefore a condition-5 **failure** — less likely, biasing the study **toward** declaring a counterexample.
Endpoints are now rounded outward, and the convention is stated so it cannot recur silently.

**The deferral migrated again, and is now closed.** Condition 3's timeout branch pointed at "the §9 fallback row"
when §9 had three rows and none decided condition 3's proposition. **§9 now carries a fourth row, "free-symbol
survival", which decides exactly that proposition**, and condition 3 names it.

**Also applied:** classes 1, 2 and 5 separated by one discriminator — whether a completion-free floor exists — which
closes both codex's mixed determinate/underdetermined family and kimi's single-differing-completion construct;
**a substantive C6 failure now files `DYM_FLOOR_DERIVED` with the failed condition reported**, since a breaker
condition failing on its decision rule is a physics result and not a control failure — without it, the one path
this study exists to produce had no correctly fileable outcome; C5b given a per-path `IN_SCOPE`/`OUT_OF_SCOPE`
table; the census given a non-blank-line/disposition reconciliation count; `k_B` given its value and `t_0` its year
convention; SymPy determinism required across seats; and the class-4 fairness slip repaired — *"no positive lower
bound exists"* was a nonexistence claim about the branch, and it entered in the very round that repaired the same
defect in limb A.

**One defect neither seat reported, found here while applying their findings:** the header still read
**"Version 5"** while §8 documented V6 — a retry after a failed edit assertion dropped the bump, and **both seats
gated the document without noticing its own version was wrong.** Corrected, and noted because a version table is
only as good as the header it agrees with.

**R3D remains NOT run.**

**V8, this version. Blanc 23:32: apply codex's V7 repair now rather than waiting idle for kimi; V7 stays frozen at
`02c2495b…f211ad11` in commit `f41a6125a` while kimi reads it.**

codex returned **`PREREG_SOUND_WITH_REPAIRS` on V7 — the first time this seat has not refused R3D in seven rounds.**
Five of seven sections came back sound with no replacement (outcome classes, circularity, re-run guard, fairness,
stall), and codex verified the rest by execution: it **ran** the three C5 commands, and it **re-derived every
comparator number** — `2.1764343420511267e-8`, `1.7298245132213753e11`, `5.189473539664126e11`, `4.375624e30`,
`5.767868e30` — confirming the outward intervals reproduce and stating that **no comparator number is deferred**.
The overclaim and the rounding bias are closed.

**The single remaining defect, and its origin.** V7 routed the four asserted comparator conventions through C6
condition 2's provenance rule. **That deadlocks:** condition 2 passes only when a constant terminates in a manifest
equation or in §2b, and an asserted convention terminates in neither — so condition 2 could never accept them,
condition 5 could never pass, and C6 was blocked on every path. The same functional failure as the previous rounds,
reached from the opposite direction.

**This defect came from applying codex's own V6 replacement text verbatim.** Its V6 fix said condition 5 "may pass
only if C6 condition 2 accepts those comparator assumptions under its provenance rule"; adopted faithfully, it
deadlocked two clauses the referee had not been asked to check together. **A referee's exact-replacement text is not
pre-verified against the rest of the document**, and adopting one verbatim is not the same as adopting it — the
interaction has to be traced. That is recorded here because it cost a round.

**V8's repair, traced rather than transcribed.** The four conventions are **comparator scaffolding, not constants of
the derived floor**: they are printed in the condition-5 artefact, do not enter the C2 completion ledger, and lie
outside condition 2's test. **And condition 2's own row now names that scope**, so the decoupling is stated where
the rule is, not only in a sentence twelve lines away — which is how the V7 version of this defect survived.

**kimi's V7 verdict is still outstanding**; it binds to V7's bytes as committed. Anything new it raises is folded in
and both seats re-gate against the result. **R3D remains NOT run.**

## 8a. Gate record, re-verified against the reports on disk

**Re-verified 2026-09-04 (Blanc 23:32, item 3).** Every hash below is the `ACCESS_SHA=` the seat itself printed in
the report named beside it — not my recollection. Each row is checkable with `shasum -a 256` on that report.

| version | sha256 gated | seat | report | verdict |
|---|---|---|---|---|
| V2 | `1ecb7ac7ae80352e…` | codex | `R3D_GATE_codex_20260904.md` | `PREREG_UNSOUND` |
| V3 | `872d4978b73cabc6…` | codex | `R3D_GATE_V3_codex_20260904.md` | `PREREG_UNSOUND` |
| V3 | `872d4978b73cabc6…` | kimi | `R3D_GATE_V3_kimi_20260904.md` | `PREREG_SOUND_WITH_REPAIRS` |
| V4 | `19843627fd6b3ce7…` | codex | `R3D_GATE_V4_codex_20260904.md` | `PREREG_UNSOUND` |
| V4 | `19843627fd6b3ce7…` | kimi | `R3D_GATE_V4_kimi_20260904.md` | `PREREG_UNSOUND` |
| V5 | *(not dispatched)* | — | pin-update only, after the pattern record was amended to V2 | — |
| V6 | `14db4dfbdc660fb3…` | codex | `R3D_GATE_V6_codex_20260904.md` | `PREREG_UNSOUND` |
| V6 | `14db4dfbdc660fb3…` | kimi | `R3D_GATE_V6_kimi_20260904.md` | `PREREG_SOUND_WITH_REPAIRS` |
| V7 | `02c2495b14c6a0cd…` | codex | `R3D_GATE_V7_codex_20260904.md` | **`PREREG_SOUND_WITH_REPAIRS`** |
| V7 | `02c2495b14c6a0cd…` | kimi | `R3D_GATE_V7_kimi_20260904.md` | *outstanding at the time of writing* |
| V8 | *this version* | — | not yet dispatched | — |

**Eight dispatched gate runs on R3D.** The trajectory is the point: codex refused V2, V3, V4 and V6 and returned
`SOUND_WITH_REPAIRS` on V7, its first non-refusal in seven rounds; kimi's verdicts moved
`SOUND_WITH_REPAIRS → UNSOUND → SOUND_WITH_REPAIRS`. **No round has yet produced a clean `PREREG_SOUND` from either
seat, and that is reported rather than smoothed.**

**V9, this version. ORDERED by Duho: "redesign condition 5 and add C0 to every prereg", after the diagnosis in
`R3D_FALSIFIER_DISABLING_DIAGNOSIS_20260904.md`.** This is the structural change the diagnosis recommended, not a
fourth repair of an instance.

**Condition 5's polarity is inverted.** It now **FAILS on a demonstrated overlap with a named comparator and PASSES
otherwise** — a disjunction, where it was a conjunction requiring a complete table, every comparator derived, every
provenance accepted and no overlap. **Three consecutive repairs (V3, V4, V7) each left that conjunction unable to
return PASS on any path, in three different ways**, because a conjunction has far more surface area and every
drafting error landed on it. **There is now nothing left for a drafting error to break.** The completeness
requirement is not dropped: the four-row table, ΛCDM included, is required as a **C6 artefact**, so an unmet
requirement fails **loudly** as a control instead of **silently** as an unreachable pass. **C6's three outcomes are
now stated in full**, because the redesign's first draft removed the only line defining `C6_BREAKER_TEST=PASS` and
left the pass implicit — caught by tracing the change rather than by a referee.

**The accepted cost, stated rather than hidden:** a lazy or incomplete comparison now yields a PASS, and PASS is the
high-stakes direction — it declares a counterexample and would amend a reported record. That risk is taken because
it is **inspectable**: it leaves a printed table the second seat, the audit and the principal can all check.
A disabled falsifier left nothing to inspect and survived four rounds.

**C0 — reachability is added as a control**, and it is the general fix: no other control here checks that an
outcome *can occur*. Its exhibitions are **authored by a seat and only verified by Tori**, because deciding what
counts as reachable is where an author's prior would enter. Reachability of the redesigned condition 5 was
self-checked at V9 (`1.0e15 kg` → PASS, `2.0e11 kg` → FAIL overlapping Hawking, `m_P` → FAIL overlapping Planck,
`3.0e30 kg` → PASS), **but that is my check and does not satisfy C0**, which requires the seat's exhibition.

**R3D remains NOT run.**

## 8b. V10 — REPAIR NOTE A: the C0 reachability failure

**Kept separate from the design-gate repair, per Blanc 00:06, so it stays visible which change was made for which
reason. This note covers ONLY the C0 failure.** ORDERED by Duho: *"fix the two unreachable verdicts and
re-exhibit."*

**The exhibition's finding.** `R3D_C0_EXHIBITION_codex_20260904.md`, `C0_REACHABILITY=FAIL`, 18 reachable and
**2 UNREACHABLE** — C6 condition 1 FAIL and condition 3 FAIL — both blocked by the same pair of clauses: C6 applied
only after `DYM_FLOOR_DERIVED`, and a candidate that would fail either condition cannot reach that class.

**The mechanism, not the two rows.** Blanc's test is the right one: *on how many paths through this document can
the breaker test return FAIL?*

| | C6 FAIL reachable on | conditions able to fail |
|---|---|---|
| **before (V9)** | **1 path of 7** — `DYM_FLOOR_DERIVED` only; every other class returned `NOT_RUN` | **3 of 5** — conditions 1 and 3 entailed by the gating class |
| **after (V10)** | **3 paths CLAIMED** — `DYM_FLOOR_DERIVED`, `DYM_FLOOR_UNDERDETERMINED`, `DYM_FLOOR_COMPLETION_DEPENDENT` | **claimed 5 of 5** |
| **corrected on the V12 definitions** | **2 paths ACTUAL** — the third, `DYM_FLOOR_COMPLETION_DEPENDENT`, is a **DEAD CLASS**, unreachable on V11 and V12 alike | **4 of 5 substantive**; condition 1 `ENTAILED` |

**The worse thing the gating was doing.** With C6 reachable from one class only, **counterexample status was being
decided by class assignment rather than by the falsifier.** `DYM_FLOOR_COMPLETION_DEPENDENT` stated outright that
"the pattern record is not amended, because the floor is not completion-free" — **a verdict about the lane's own
pattern, reached by fiat, with the breaker conditions never evaluated.** Under V10 that same conclusion must be
**earned**: C6 runs, and condition 2 or 3 must actually fail, with its artefact printed.

**How the two rows become reachable.** Condition 3 FAIL is now reachable via `DYM_FLOOR_UNDERDETERMINED`, whose
surviving freedom is exactly what condition 3 rejects. Condition 1 FAIL is now reachable because **the conditions
are evaluated on the quantity the seat actually FILED**, not on an idealised one — so a seat filing a dimensionless
ratio as its floor is caught by condition 1 rather than assumed impossible. **Neither row was made reachable by
deleting an outcome, widening a class, or arguing the case unphysical.**

**DIRECTION — checked, and stated as required.** This repair makes the falsifying verdict `C6_BREAKER_TEST=PASS`
**available on more paths than before, and harder on none.** A counterexample can now be certified from three
classes rather than one. **It does not move the boundary toward preserving the pattern**, which is the direction
the diagnosis warned about; it moves the other way, and it removes a place where the pattern was being preserved
without a test.

**Also in this note, because both are C0-adjacent:** "floor" is now defined once, at the class boundary, as a
strictly positive greatest lower bound whether or not attained — both seats found it ambiguous, and C0 could not
flag it because a seat resolving an ambiguity favourably still produces a path. And condition 3's `UNDECIDED` state
now maps to `C6_BREAKER_TEST=FAIL`, so C6's three codes are exhaustive and "does not pass" is never a fourth state.

**R3D is NOT frozen and NOT run.** C0 must return `PASS` from a fresh seat exhibition before either.

## 8c. V11 — REPAIR NOTE B: the two design-gate lists

**ORDERED by Duho: "fix both lists and re-gate."** V10 (`a441c7c9…`) was gated by two engines, both hash-verified
and both read only after their seats exited: **codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`.**

**Where they AGREE — including on the thing that mattered.** Both counted the paths independently and both got
**C6 FAIL reachable on 3 of the 7 classes** — **a count since shown wrong**: one of those three,
`DYM_FLOOR_COMPLETION_DEPENDENT`, is unreachable, so the true figure is **2**. Both seats counted the *declared*
routes; neither tested whether each route was itself reachable. **That gap is exactly what C0 exists for, and C0
caught it.** Neither found the breaker unable to fail, and that remains true of the two live classes. **The defect that recurred
four times in four forms is gone**, and it was confirmed by two seats that were not told to look for it. Both found
the **re-run guard** and **fairness** sound; codex additionally found **circularity** sound.

**Where they DISAGREE — one point, recorded rather than settled by me.** codex: condition 1 *"cannot fail on any
valid path"*, since a dimensionless quantity is not a member of any positive-floor class, so **4 of 5** conditions
can fail. kimi: condition 1 **can** fail because §5 evaluates *the quantity actually filed*, so a mis-filed ratio is
caught — **5 of 5**. Both are defensible and the split is over whether a malformed filing counts as a reachable
path. **V11 adopts codex's label and kimi's behaviour**: condition 1 is marked `ENTAILED`, with the entailment
stated, and it still fails on a malformed filing. §5a records both readings.

**codex's list, applied:** `DYM_SOURCE_BLOCKED` widened from unreadability alone to cover a manifest digest
mismatch, an `UNRESOLVED` proposition and an undecidable-after-fallback procedure — the terminal classes were not
exhaustive. Every control now carries **`PASS|FAIL|NOT_RUN`**; most printed only a PASS token, and **a control that
can only say PASS is not a control** — this lane's own principle, applied to itself. C0 gains the `ENTAILED` route,
because as written it demanded a reachable substantive failure for a condition that valid membership makes
impossible, so a sound document could never freeze — **a defect in the control I wrote, found by a gate.**

**kimi's list, applied:** R1, the §2c sentence still describing the old single-class gating — **a repair scar**. The
whole document was swept rather than the quoted line fixed; that was the only live scar, and §8b's account of the
prior state is history and stays. R2, `NOT_RUN` was defined so that a condition-3 `UNDECIDED` run — which produced
a floor and *did* engage C6 — was assigned both `FAIL` and `NOT_RUN` by different clauses; `NOT_RUN` now means
**C6 was never engaged**. R3, the seat-split rule was blind to two seats filing the **same** class with **opposite**
`C6_BREAKER_TEST` outcomes, reachable because conditions 2 and 4 are bounded by each seat's own C2 artefact with no
rule forcing the ledgers to agree — one seat could certify a counterexample while the other did not, with nothing
convened.

**And the path count now lives in the document (§5a), not only in a gate report** — it is the answer to the
question that produced the diagnosis, and it should be checkable in the text.

**C0 must be re-run:** these repairs touch outcome-class membership and control reachability, and **a passed
exhibition is about the version it was run on.** V10's `PASS` does not carry to V11.

**R3D is NOT frozen and NOT run.**

## 8d. V12 — the second C0 failure, and what it cost

**C0 on V11 returned `FAIL`.** `DYM_FLOOR_COMPLETION_DEPENDENT` was **UNREACHABLE**: no input could satisfy it,
because class 4's definition of "permit" — *"no positive lower bound on the mass follows"* — **is** class 5's own
precondition, and class 4 carried precedence. **V10's repair, which widened C6 from one positive-floor class to
three, had created a dead class among the very three it widened to.** Nominally three routes to a breaker failure;
actually two.

**This is the same family one level down** — not a disabled falsifier, but a **declared route to it that no case
can travel** — and it is the second C0 failure in that direction. **If a third occurs, the standing instruction is
to stop and file rather than repair.**

**The repair is to the definitions, not to the exhibition.** §4's then-five scientific classes were restated as a
single **decision procedure over admissible readings**: a reading yields a positive floor or permits zero; `P` is
the set that yields one, `Z` the set that permits zero. Class 4 requires **`P` empty** — *no* admissible reading
rescues a positive floor — which is strictly stronger than "some reading permits zero" and no longer swallows
class 5. The **mixed case**, where one reading gives a floor and another permits zero, now lands in class 2, where
the genuine freedom belongs. **The five are exclusive and total by construction, so no precedence rule is needed
and none is stated** — the precedence rule was the mechanism of the defect.

**§5a now prints two numbers, declared and reachable**, and records that V11 declared three while only two were
reachable. A document that claims more falsifiability than it has is the precise fault this study exists to detect
in the corpus; it is recorded here rather than quietly corrected.

**C0 must be re-run on V12 before any gate.** R3D is NOT frozen and NOT run.

## 8e. V13 — a class RETIRED, not repaired a fourth time

**ORDERED by Duho, 2026-09-05 00:59 KST: "retire the class and set the count to two."**

**`DYM_FLOOR_COMPLETION_DEPENDENT` is retired as a declared outcome class.** Its history stays here rather than
being deleted:

- It was **added at V7** to close a real gap: a reachable result — a positive floor arising only under named
  admissible completions — that fitted no class at all.
- **Three seat exhibitions could not produce an input that reaches it.** On **V10** it was reachable only through
  a routing overlap; on **V11** class 4's "permit" was word-for-word its own precondition, so class 4 swallowed it;
  on **V12** the partition's dichotomy made "yields no floor" identical to "permits zero", so the completion-free
  reading was always in `Z` and its requirement that `Z` be empty could never hold.
- **Evidence for the retirement:** `R3D_C0_EXHIBITION_V12_codex_20260905.md`,
  sha256 `9c8180b6b0502e03f52ed66c757272e95a9cc57682212556f6a32d985e46bc91`, access-proven against V13's
  predecessor `c7488e1c…`. The seat constructed the exact reading set the class would need — completion-free yields
  no floor, two completions agree on one positive floor — and showed §4 routes it elsewhere.

**Three locally-sensible repairs failing to make one class reachable is evidence the class did not name a
distinguishable state.** It is retired on that evidence, not abandoned in frustration.

**WHAT THE RETIREMENT COSTS, stated plainly.** The class described something real: a floor that exists only under
completions, with every completion agreeing. **That state still occurs, and it now files as
`DYM_FLOOR_UNDERDETERMINED`.** That is correct rather than a hiding place: if the completion-free reading yields no
floor while the completions yield 10 kg, the admissible readings **genuinely disagree** — one says no positive
bound follows, the others say 10 kg — and disagreement among admissible readings **is** underdetermination.
**The seat must still report every reading and name any completion a floor depends on**, so the completion-
dependence remains visible in the filing; only the separate label is gone. **The state is not homeless, and §4
says where it goes.**

**THE COUNT IS NOW TWO, AND DECLARED EQUALS REACHABLE.** `C6_BREAKER_TEST=FAIL` is reachable on **2 of the 6**
classes — `DYM_FLOOR_DERIVED` and `DYM_FLOOR_UNDERDETERMINED`. Every earlier claim of three is corrected in place
and marked, in §5a, in §8b's table and in §8c.

**How to read this episode.** **This is the first time the reachability control ended a class rather than repairing
one, and that is the control working.** Three attempts, each locally correct, and the evidence eventually said the
target was not there. A design that had claimed three routes to a breaker failure now claims two and has two — and
a preregistration that overstates its own falsifiability is the precise fault this study exists to detect in the
corpus.

**C0 must be re-run on V13: retiring a class changes the partition. R3D is NOT frozen and NOT run.**

## 8f. V14 — the empty-set case, and a deliberate check on whether condition 1 is the old mechanism

**codex gated V13 `61adc801…` `PREREG_UNSOUND`** (seat exited, `ACCESS PROVEN`, hash verified by me). It found
**circularity, the re-run guard and fairness SOUND**, and one real coverage defect.

**The defect: an inconsistent reading has an EMPTY allowed mass set.** §4's dichotomy said every admissible
reading either yields a positive floor or permits masses approaching zero. **An inconsistent reading does
neither** — with no allowed masses there is no greatest lower bound to be positive, and nothing approaches zero
either. It fell out of the partition entirely. **And class 4's gloss claimed to cover "the case of mutually
inconsistent relations" while its condition did not route it** — the gloss and the rule disagreed.

**This is not hypothetical for this corpus.** A paper whose printed relations contradict each other is exactly the
kind of thing a reproduction-minded audit turns up, and §4 elsewhere already anticipated it in the fairness wording
for inconsistency. The dichotomy simply had no box for it.

**Repaired** by restricting the dichotomy to **consistent** readings and adding a third set **`I`**: every
admissible reading now lies in exactly one of `P`, `Z`, `I`. Class 4 fires when `P` is empty and `Z` or `I` is
non-empty; class 2 when `P` is non-empty and the readings disagree — including when `I` is non-empty; class 1
requires `Z` **and** `I` both empty. The partition is total and exclusive again.

### Is condition 1's unfailability the diagnosed mechanism recurring? — checked deliberately, as asked

codex notes that **C6 condition 1 cannot fail on any valid positive-floor path**, only on a malformed filing.

**Same SHAPE, opposite DIRECTION, and already disclosed. My judgement: it is not the diagnosed mechanism.**

- **Shape — yes, it is the same family.** A declared outcome that no valid case reaches is exactly what the retired
  `DYM_FLOOR_COMPLETION_DEPENDENT` was. Declared-versus-actual mismatch is this design's recurring weakness and it
  is worth naming rather than absorbing.
- **Direction — no, it runs the other way.** The diagnosed mechanism blocked the falsifier's PASS, so a
  counterexample to this lane's pattern could never be certified: errors landing on the side that **protects the
  pattern**. A condition that cannot fail makes the breaker **easier** to pass, so a counterexample becomes
  **easier** to certify. It weakens the test **against** the lane's own interest, not for it.
- **Status — already labelled, not hidden.** §5a marks condition 1 **`ENTAILED`**, states the entailment (every
  positive-floor class requires a mass, so a correctly filed floor passes a dimensional test), and counts **4 of 5**
  conditions as substantively failable rather than claiming five. C0's clause carries the `ENTAILED` route
  explicitly. **A disclosed entailment is a property; an undisclosed one would be the defect.**

**Flagged rather than absorbed, per Blanc:** this is the **second declared-versus-actual mismatch since the
redesign** — the retired class was the first. **Both were found by C0, neither by a design gate**, which is the
argument for keeping the reachability control on every preregistration this lane writes.

**Also repaired:** C0's clause ended with a bare `C0_REACHABILITY=PASS`, which reads as the document certifying its
own pass — and it did so while §8 recorded a *failing* exhibition. **A control cannot certify itself in its own
text**; it now names the token it emits from the exhibition actually run.

**C0 must be re-run on V14: the partition changed. R3D is NOT frozen and NOT run.**

## 8g. V15 — the V14 reconciliation, and the scar family's fifth appearance

**Both V14 seats returned `PREREG_UNSOUND` on `bbcb4a89…`; both hashes verified by me after each seat exited.**

**WHERE THEY AGREE.** Both found the **partition itself sound** — `P`/`Z`/`I` is exhaustive and mutually exclusive,
and an inconclusive result is genuinely reachable. Both found **circularity, the re-run guard and fairness sound**.
Both independently found **the class-count scar**: §4's heading said "six declared: four scientific" while the very
next line said "five scientific classes partition the cases". Both traced condition 5's PASS and FAIL to concrete
floors and confirmed the falsifier still bites.

**WHERE THEY DIFFER — and it is complementary, not contradictory.**
codex found the **limb-A exit named no control dispositions**, while §9 permits `NOT_RUN` only where the document
explicitly makes a control unreached. kimi found the **limb-A entry condition disagreed with §4** — §3 stopped
whenever no *size–mass* relation was reproduced, while §4's table and class 3 required that *no mass bound of any
kind* was reproduced, so **a printed direct mass bound with no `V(M)` was routed to opposite places by clauses meant
to agree**. Both are real; both are applied; **each seat found what the other missed.**

**THE SCAR FAMILY, FIFTH APPEARANCE — and this one is mine twice over.** kimi found that **six controls still ended
with a bare `PASS` literal** — `C1` through `C5b` — *"the exact form this document diagnosed and repaired at C0 one
round ago."* I fixed the site the referee quoted and not the class. **That is the one-site-not-the-class failure
this lane's own rules forbid, committed in the round that repaired it elsewhere.** All six are now converted to the
C0 form. kimi also caught the **header still saying `FROZEN`** while §8f said the document was not frozen and C0 was
`NOT_RUN` — and that the header's timestamp predated the ruling that produced V13.

**ON THE KIMI SEAT'S ENVIRONMENT LIMIT, and why it is the right behaviour.** kimi reported plainly that **script
execution was blocked in its mode** and verified the comparator arithmetic **by hand** instead, printing its
intermediates. I re-checked all four: `ħc = 3.16152677e-26`, `m_P = 2.1764343e-8`, `t_0 = 4.353913e17`,
Hawking lower `1.729826e11`. **Every one is exact.**

**What the hand-verification covers, and what it does not.** It fully covers the **comparator arithmetic**, which is
pure computation on printed constants — a script would have added nothing. It does **not** cover the **executability
claims**: that §9's three harness commands run as written, that the C3 deletion probe executes, that the free-symbol
probe terminates. **codex executed those; kimi could not.** So the two seats together cover what neither covered
alone — which is an argument for the blind double beyond disagreement-detection.

**A seat that reports its limitation and works around it is doing the thing this lane needs.** The contrast worth
recording: a seat blocked from its sources earlier in this programme returned a verdict anyway, and that filing had
to be set aside. **Stating the limit is what makes the rest of the report usable.**

**R3D is NOT frozen and NOT run. C0 must be re-run on V15.**

## 8h. V16 — the V15 reconciliation, and what eleven versions have actually settled

**codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`, both on `4e12ef21…`, both hash-verified after exit.**

### What is settled — worth stating, because it is the difference between a design that is wrong and one that needs sharpening

Across V2→V16, and now across two engines reading independently:

- **No seat says the falsifier is disabled.** Both V15 seats traced condition 5 to concrete PASS and FAIL floors.
- **No seat finds a class unreachable.** C0 has passed on V13, V14 and V15 with zero unreachable rows.
- **No seat finds circularity.** Both called §2c and the pattern bar **SOUND**, with no replacement.
- **The re-run guard and fairness are sound**, on both lists, repeatedly.
- **The counts are consistent and every control carries `PASS|FAIL|NOT_RUN`.**

**The remaining objections are boundary sharpness and arithmetic precision — not whether the study can answer its
question.** That progression is the record: the design was wrong in V3–V12 and is now being sharpened.

### The two findings, and each seat again caught what the other missed

**codex — class 3 was not exclusive.** A manifest printing no size–mass relation and no mass bound satisfies the
no-relation class, while the later classes quantify over **completion-added** readings, so a completion supplying
`M ≥ 10 kg` put the same case in two classes. **Repaired at the cause, not the row:** a completion must now
**operate on at least one printed relation** — one that is *itself* the sole source of a mass bound supplies the
content rather than completing it, and is inadmissible. The row states the consequence as well, so it reads
self-contained.

**kimi — the comparator that excluded its own value, and it is the serious one.** Comparator 1 was the degenerate
interval `[2.176434e-8, 2.176434e-8]` while §2b's constants give `m_P = 2.1764343e-8`, which is **larger**. **A
point cannot be rounded outward, so the outward convention failed silently at exactly that row.** A seat deriving a
Planck-mass floor would find **no overlap**, condition 5 would **PASS**, and **the canonical semiclassical-remnant
case — the one input that comparator exists to catch — would escape**, letting C6 certify a counterexample the
pinned condition-5 text exists to reject. **I re-computed it: `2.1764343421e-8` is outside the printed interval.**
Widened to `[2.176433e-8, 2.176435e-8]`, which contains it, with the degenerate-interval rule stated and **C0 now
required to exhibit a condition-5 FAIL per comparator row** — an exhibition touching only the Hawking row would
never have seen this.

**This is the V6 inward-rounding bias recurring at the one site the outward rule could not reach, and it biases in
the high-stakes direction: toward amending the pattern record.**

**kimi also found the count scar's SIXTH appearance** — "These **five** are mutually exclusive" survived lower in
the same section whose heading V15 repaired — and **the title still read `FROZEN`** while the version line beneath
it said the document is not frozen. Both were one-site fixes of mine that did not reach their siblings.

**And a per-floor gap:** on class 2 the seat is told to **choose none**, so "the quantity the seat actually FILED"
had no unique referent; C6 is now evaluated **separately on each floor in `P`**.

### The partition-boundary family, counted honestly

This is the **fourth** partition-boundary defect in R3D: V10's routing overlap, V11/V12's dead class, V14's
limb-A entry mismatch, and now V15's class-3 overlap. **Each was a different boundary and each repair fixed the one
it addressed, so the third-failure rule has not fired** — that rule is for one defect surviving three repairs in the
same direction. **But the family is the most expensive thing in this chain**, which is why this repair changed the
**definition of an admissible completion** rather than adding a conjunct to one row. **If a fifth boundary defect
appears, I will stop and file rather than patch a fifth boundary.**

**R3D is NOT frozen and NOT run. C0 must be re-run on V16.**

## 8i. V17 — the same boundary, attempt three, and the finding underneath it

**codex gated V16 `81898e25…` `PREREG_UNSOUND`, hash verified after exit.** Its defect is **the same class 3 /
class 4 overlap** found in V15 and repaired in V16. **Counted honestly: this is attempt three on this specific
defect, in the same direction. The round counter does not reset because the wording changed.**

**So the rule's actual purpose was served first: I asked why the partition keeps failing, before repairing it
again.** The answer is in §4 and it is a finding rather than a defect —

- **Class 3 entails class 4, by meaning.** Nothing printed ⇒ the completion-free reading imposes no lower bound
  ⇒ it lies in `Z`, `P` is empty ⇒ class 4's predicate is satisfied. **"No relation printed" is a *reason* no floor
  follows; "permits zero" is the *consequence*.** They are cause and effect, not alternatives.
- **They are different kinds of thing.** Class 3 is **procedural** — limb A's exit, decided before any completion
  exists. Class 4 is a **state predicate** over readings including completions. **A procedural exit inside a state
  partition is a category error**, which is exactly why three predicate-level repairs failed in succession.

**The repair follows from the finding rather than patching around it:** the two classes are now separated **by
limb** — class 3 is filed only from limb A, classes 1, 2 and 4 only from limb B — which is the difference that
actually exists between them. **No predicate conjunct was added.**

**The structural alternative, flagged for Duho and NOT taken:** retire class 3 and fold it into class 4 with a
required reason field. **Retiring a class is his ruling, not mine.** If the limb separation does not hold, that is
the candidate fix.

**If a gate finds this overlap a fourth time, the third-failure rule fires: stop, file, wait. No fourth repair.**

**R3D is NOT frozen and NOT run. C0 must be re-run on V17.**

## 8j. V18 — the boundary that failed three times is SOUND in both seats, and the third-failure rule did not fire

**codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`, both on `498faefc…`, both hash-verified after exit.**

### The recurring overlap is closed — stated first, because it is the round's result

**Neither seat found the class 3 / class 4 overlap.** codex, unprompted: *"The six terminal classes are exhaustive
and mutually exclusive as an operational decision procedure. Class 3 is selected only by the limb-A exit; classes
1, 2, and 4 partition limb B by the disjoint `P`/`Z`/`I` cases."* kimi filed **FINDING 1 — OUTCOME CLASSES: SOUND.**

**The attempt-three repair held, and so did the finding under it.** Separating by **limb** rather than by predicate
was the right move because the difference was never a predicate: class 3 entails class 4 by meaning, and a
procedural exit cannot be split from a state predicate by adding conditions to either. **Three predicate-level
repairs failed; the first structural one passed both seats and the exhibition.** The third-failure rule stood ready
and was not needed.

### How much of this design is now settled

**kimi found SIX of seven sections SOUND** — outcome classes, controls, circularity, re-run guard, fairness, stall
— with one defect. **codex found circularity and the class partition sound**, with three. **Both seats' single
shared defect is the same one**, which is what convergence looks like.

### The shared defect: engagement and filing are different events

**§5a said "C6 applies on 2 of the 6 outcome classes" and treated that as the number of classes in which C6 can
fail.** But **C6, once engaged, travels with the run into a terminal class that is not one of the two it engaged
from.** Both seats found it independently.

**Corrected to two numbers:** C6 is **initially engaged** on 2 classes; once engaged, `C6_BREAKER_TEST=FAIL` can be
recorded in **4 terminal classes** — those two, plus `DYM_SOURCE_BLOCKED` when condition 3 stays `UNDECIDED` after
its fallback, plus `R3D_NO_CLASS` when an engaged C6 meets a persistent control failure.

**Also from codex, both applied:** an early terminal block left every later control's status unstated while the
global rule permitted `NOT_RUN` only where the document says so explicitly — it now says so explicitly, and
distinguishes controls engaged before the block (which carry their real result) from those never engaged. And
class 4's table row still read *"no consistent admissible reading yields a positive floor"* — **a nonexistence
claim in an operative clause**, now *"a positive floor was unreproduced from the stated inputs."* kimi called
fairness sound; codex found this row; **the row is codex's catch and it is right.**

**C0 must be re-run on V18. R3D is NOT frozen and NOT run.**

## 8k. V18 was a TWO-SEAT CLEAR — the reconciliation, and why V19 does not inherit it

**V18 (`74f8e0c3…`) passed a two-seat design gate: codex `PREREG_SOUND` — all seven sections sound, no
replacement, no caveat — and kimi `PREREG_SOUND_WITH_REPAIRS`. Both hashes verified after each seat exited, and
C0 passed on V18 independently.** After eighteen versions, that is the first clean gate.

### WHAT THE GATE CERTIFIES, AND WHAT IT DOES NOT

**It certifies the DESIGN.** It does not start the study. **R3D does not run without Duho's word — no limb, no
seat, no derivation, no census.** A clear changes nothing about that.

### Where the seats agree

Outcome classes, controls, circularity, the re-run guard and the stall analysis: **sound in both**. Both counted
the falsifier the same way — **`C6_BREAKER_TEST=FAIL` reachable in 4 of the 6 declared classes** — and kimi
**executed** the comparator arithmetic, confirming `m_P = 2.1764343421e-8` now lies inside the widened degenerate
row `[2.176433e-8, 2.176435e-8]`, the Hawking bounds round outward as claimed, and all three comparator overlaps
behave as printed.

### kimi's repairs, each with its disposition — because a `SOUND_WITH_REPAIRS` whose repairs are neither applied nor answered is not a clear

| # | repair | disposition |
|---|---|---|
| F4 | the count is 4 of 6, not 2 | **Already applied at V18** — this was the shared V17 defect; kimi's number confirms the repair rather than asking for one. No change. |
| F6 | class 3's row asserts *"No printed relation binds size to mass or bounds the mass at all"* — a nonexistence claim in an operative clause | **APPLIED.** Now *"a relation … was unreproduced from the stated inputs"*. **This is the identical form V18 repaired in class 4's row and missed in class 3's, in the same version** — the scar family's seventh appearance, and mine. |
| F7 | the split rule does not convene when two seats file the **same** class with the **same** C6 outcome but **different reported floors or families** | **APPLIED.** Reachable precisely because the document states no rule forcing the two C2 ledgers to agree — so the filed class could be unambiguous while the study's central quantity was not. |

**No repair is answered-and-declined; both stand and both are applied.**

### Also in V19, and it is not a repair

**The C3 deletion probe is wired in.** `r3d_c3_deletion_probe.py` is now named in C3 with its exact invocation,
input schema, printed artefacts and exit codes. It was written and control-tested hours ago and has been carried as
outstanding work since; **a control that names a script nobody has run is the failure mode this lane already paid
for.** Its positive control fails as circular (exit 1) and its negative control passes (exit 0) — **and its first
version failed its own positive control**, which is recorded in C3 because a probe blind to circularity would have
been worse than none.

### V19 does not inherit V18's clear

**A repaired document is a new document.** The clear belongs to `74f8e0c3…`. V19 must earn its own: **C0 re-run,
then a fresh two-seat gate.** Nothing here carries forward silently.

**R3D is NOT frozen and NOT run.**

## 8l. V20 — both V19 seats SOUND_WITH_REPAIRS; three defects, two of them from V19's own repairs

**codex `PREREG_SOUND_WITH_REPAIRS`, kimi `PREREG_SOUND_WITH_REPAIRS`, both on `28a97c1a…`, both hash-verified
after exit. No `UNSOUND` from either engine.**

**Both found sound, independently:** outcome classes, circularity, the re-run guard and fairness. Both counted the
falsifier identically — **FAIL reachable in 4 of 6 terminal classes** — and both traced every condition's PASS and
FAIL to concrete inputs, agreeing that **condition 1 is `ENTAILED`** with no valid substantive FAIL, exactly as the
document discloses. kimi verified the Planck-row closure numerically and states the V16 escape is closed.

### The three repairs, each applied

| # | seat | defect | disposition |
|---|---|---|---|
| 1 | codex | C3's printed invocation `python3 … <relations.json>` — **the angle brackets are shell syntax**, so a seat running it literally redirects stdin and passes no filename | **APPLIED.** Now `python3 r3d_c3_deletion_probe.py relations.json`. |
| 2 | kimi | **C5b's scope rule fails the paths the design itself mandates** — it named only the reading tree as in-scope, so opening this document, the probe, or the probe's input would each be `OUT_OF_SCOPE` and fail the control | **APPLIED.** In-scope now names the reading tree, this document, the script and its JSON input, and the seat's own working artefacts. |
| 3 | kimi | **§5a contradicted itself** — it says an engaged C6 can travel into `DYM_SOURCE_BLOCKED` and `R3D_NO_CLASS` and record `FAIL`, then three paragraphs later says C6 is `NOT_RUN` on "the other 4", naming those same two | **APPLIED.** |

**Two of the three are V19's own repairs biting back, and both are mine.** Defect 1 arrived *with* the C3 wiring —
I cited a command in placeholder notation inside a document that tells seats to execute it literally. Defect 3 is
the **eighth appearance of the scar family**: V18 corrected the count where the count was stated and left the
consequence sentence asserting the old thing three paragraphs down.

**What that says about the sweep, plainly:** I have been sweeping for the *phrasing* I just changed rather than for
every sentence that *depends on* what I changed. A count and its consequence are different sentences with no shared
wording. **The rule this adds: after changing a number or a rule, find the sentences that reason FROM it, not the
ones that repeat it.**

**V20 does not inherit V19's verdicts. C0 re-run, then a fresh two-seat gate. R3D is NOT frozen and NOT run.**

## 8m. V21 — the stopping criterion applied for the first time. V20 is NOT final.

**Both V20 seats returned `PREREG_SOUND_WITH_REPAIRS` on `301cba9b…`, hash-verified after exit.** Both found
**outcome classes, controls, circularity and the re-run guard SOUND**; both counted the falsifier identically —
FAIL reachable in 4 of 6 terminal classes — and both confirmed condition 1 is correctly marked `ENTAILED`. kimi
found **fairness and stall sound**; codex found **fairness defective**.

**The stopping criterion of `R3D_STOPPING_CRITERION_20260905.md` was declared at 06:18, before this gate was
dispatched and before any finding existed. Applied to four findings made blind to it:**

| finding | seat | classification | disposition |
|---|---|---|---|
| class 2 states **no consequence for `C6_BREAKER_TEST=PASS`**, and the state is reachable | kimi R2 | **SUBSTANTIVE** — criterion (4): *what the study can conclude* is undefined on a reachable path | **REPAIRED** |
| **zero-control-clean agreement**: both seats agree on class, floor and C6 outcome while each fails a *different* control — no split convenes, no control persistently fails, and `DYM_SOURCE_BLOCKED` would be filed on a case its definition does not describe | kimi R3 | **SUBSTANTIVE** — criterion (1): *which class a run files*, on a reachable terminal state | **REPAIRED** |
| *"classes 1, 2 and **5** have a common discriminator"* — stale since V13 retired the old class 5 | kimi R1 | **COSMETIC** — the partition **table** does the filing; this sentence misroutes no procedure | **folded in, and said so** — V21 exists for the two substantive repairs, so a one-token correction rides along. It did **not** cause a version. |
| the tokens `DYM_NO_SIZE_MASS_RELATION` and `DYM_NO_POSITIVE_FLOOR` **assert absence** while their own definitions say *"unreproduced from the stated inputs"* | codex | **SUBSTANTIVE** — criterion (4): a token quoted as a nonexistence finding misstates the result | **ESCALATED, NOT REPAIRED — see below** |

### The escalation: codex is right, and the fix is beyond my authority

codex proposes renaming the tokens, e.g. `DYM_NO_SIZE_MASS_RELATION` → `DYM_SIZE_MASS_RELATION_UNREPRODUCED`.
**The objection is correct**: this lane's own rule is that a negative finding is *"unreproduced from the stated
inputs,"* never a claim of absence — and a class **name** travels into reports and summaries stripped of the
definition that qualifies it.

**But renaming an outcome class is redefining one, and that is Duho's ruling, not mine.** The standing boundary is
explicit: no class retired, added or redefined beyond his ruling. **So it is recorded here as a substantive,
seat-found defect that I am declining to repair on authority grounds, not on merit** — the distinction matters, and
a later reader should not mistake this for a judgement that codex was wrong.

**For his decision:** rename both tokens to the `…_UNREPRODUCED` form, or leave them and accept that the class
names overstate what the study found. Cost of renaming: every reference in this document and in any downstream
record. Cost of leaving: the study's own fairness rule is violated by its outcome vocabulary.

### Consequence for the stopping rule

**V20 is NOT final.** Two substantive findings required repair, so V21 exists and must earn its own C0 and its own
two-seat gate. **The criterion did the work it was declared for: it forced a per-finding test instead of letting a
second `SOUND_WITH_REPAIRS` be read as a finish line.**

**R3D is NOT frozen and NOT run.**

## 8n. V22 — the fourth clear, one substantive finding DEMONSTRATED, and the token defect now raised by BOTH seats

**Both V21 seats `PREREG_SOUND_WITH_REPAIRS` on `82e89d5c…`, hash-verified after exit; C0 passed on V21
independently.** codex found **six of seven sections SOUND** — classes, controls, circularity, the falsifier,
the re-run guard, stall — with fairness its only defect. kimi found classes (as a partition), controls,
circularity and the re-run guard **SOUND**.

### The decision under the criterion declared at 06:19

| finding | seat(s) | classification | disposition |
|---|---|---|---|
| **adjudicated-to-non-clean-report routing gap**: after a *different-class* split the third seat may agree with a seat whose report is **not** control-clean; nothing then authorises re-running that seat's failed control, `R3D_NO_CLASS` needs two attempts and only one exists, and the fall-through files `DYM_SOURCE_BLOCKED` on a state its definition does not describe | kimi F7 | **SUBSTANTIVE — demonstrated below**, criterion (1) | **REPAIRED** |
| the class **tokens** `DYM_NO_SIZE_MASS_RELATION` and `DYM_NO_POSITIVE_FLOOR` assert absence while their definitions say *"unreproduced from the stated inputs"* | **codex AND kimi, independently** | **SUBSTANTIVE**, criterion (4) | **ESCALATED, NOT REPAIRED — authority, not merit** |

**Demonstration of the substantive finding, traced against V21's own text rather than argued:**
seat A files `DYM_FLOOR_DERIVED` with `C4_GR_BENCHMARK=FAIL`; seat B files `DYM_FLOOR_UNDERDETERMINED`,
control-clean. **(1)** Different classes ⇒ the split rule convenes the third seat. **(2)** It agrees with A's class.
**(3)** *"A scientific class may be filed only from a seat report in which every reached control passed"* — present
in V21, so filing class 1 from A's report is **barred**. **(4)** The same-class branch authorises re-running failed
controls; **the different-class branch authorises re-executing blocked READS only**. **(5)** `R3D_NO_CLASS` needs a
control failing after **two** attempts; only one exists. **(6)** The fall-through files `DYM_SOURCE_BLOCKED`, whose
definition requires an unreadable source, a digest mismatch, an `UNRESOLVED` proposition or an
undecidable-after-fallback procedure — **none true of a run whose only fault is one seat's benchmark.**

**It is the same defect shape V21 repaired for the same-class branch and left standing in the different-class
branch** — the scar family's ninth appearance, and mine again. The repair extends the existing rule rather than
adding machinery.

### Why V21 is not final, and what that costs

**One substantive finding means V21 is not the design of record.** The criterion did what it was declared for a
second time: a fourth consecutive two-seat clear was not allowed to stand as a finish line on the strength of the
verdict tokens alone.

### The escalation, now raised by BOTH engines independently

**codex and kimi separately reached the same conclusion**: a class **name** that asserts absence travels into
reports stripped of the definition qualifying it, and this lane forbids claiming absence for a negative finding.
**Renaming a class is redefining one — Duho's ruling, not mine.** Two independent seats agreeing raises the weight
of the escalation; it does not transfer the authority. **Options and costs are unchanged and stated in §8m.**

**R3D is NOT frozen and NOT run. V22 requires its own C0 and its own two-seat gate.**

R3D_PREREG_V22_READY_FOR_REEXHIBITION
