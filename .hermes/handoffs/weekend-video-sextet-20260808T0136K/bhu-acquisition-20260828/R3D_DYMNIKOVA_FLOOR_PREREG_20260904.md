# FROZEN — ORDERED — R3-D pre-registration: does the Dymnikova regular-core branch fix a minimum black-hole mass?

**Tori, 2026-09-04 21:02 KST. Version 8 (see §8). FROZEN pending the fresh referee gate. ORDERED by Duho, "run r3c and r3d", 2026-09-04 21:02 KST.**
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

**A completion is ADMISSIBLE if and only if it introduces exactly one named assumption and is consistent with every
printed relation of the manifest sources.** A completion that contradicts a printed relation is **inadmissible** and
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
evaluation — and only after `DYM_FLOOR_DERIVED` has been reached on other grounds. C2 passes only if this census is printed in
full. *(Without it a seat could report a relation absent, omit the contrary row, and let the lane's own pattern become
indirect support for its own confirmation: C3 tests an injected relation only after the seat has already selected the
source-pinned equations, so it cannot see a relation excluded before that selection.)*

## 3. Limb structure

**Limb A (~1 seat-day):** attempt to reproduce, from the stated inputs, a printed relation binding size to mass.
If none is reproduced after the complete census of §2, report that **a size–mass relation was unreproduced from the
stated inputs**, file `DYM_NO_SIZE_MASS_RELATION` and stop. *(The wording matters: the class records what this lane
could not reproduce, not a claim that the branch contains no such relation.)*
**Limb B:** if it does, derive the floor and test it against the five breaker conditions.

## 4. Outcome classes — declared now

1. **DYM_FLOOR_DERIVED** — a unique positive floor follows from the printed relations **with no added completion**,
   **no admissible completion yields a different floor, and none permits masses approaching zero.**
   Report the formula and value, **and test it against all five breaker conditions**; if it passes them, this is a
   counterexample to the pattern and the pattern record must be amended.
   **If any breaker condition FAILS under its stated decision rule, `DYM_FLOOR_DERIVED` is still filed** and the
   failed condition is reported with its artefact: **the floor stands, it is not a counterexample, and the pattern
   record is not amended.** *(A breaker condition failing on its own decision rule — the derived floor overlapping a
   comparator, say — is a **substantive physics result, not a control failure**, and does not engage the
   control-clean rule of `R3D_NO_CLASS`. C6 is reached exactly when this class is reached, so without this sentence
   the one path the study exists to produce had no correctly fileable outcome: the report would not be
   control-clean, class 1 could not be filed from it, and a real result would have been recorded as a control
   stall.)*
2. **DYM_FLOOR_UNDERDETERMINED** — **a completion-free positive floor follows from the printed relations**, and at
   least one admissible completion yields a **different** positive floor — so, counting the completion-free
   derivation among the admitted floors, there are **at least two positive but unequal floors** — and **none permits
   masses approaching zero**. Report the freedom; choose none.
3. **DYM_NO_SIZE_MASS_RELATION** — limb A's exit: **a relation binding size to mass, or bounding the mass, was
   unreproduced from the stated inputs** after the frozen census of §2 was completed.
4. **DYM_NO_POSITIVE_FLOOR** — **at least one printed relation binds size to mass or bounds the mass**, and those
   relations, alone or under **at least one** admissible completion, **permit** masses approaching zero — where
   **"permit" means no positive lower bound on the mass follows.** If the printed relations are mutually
   inconsistent, **report that a consistent solution, and hence a positive lower bound, were unreproduced from the
   stated inputs**, file here, and **reproduce the contradiction**. *(The previous wording concluded that no lower
   bound "exists" — a nonexistence claim about the branch, the wording this lane forbids — and it entered in the
   very round that repaired the same defect in limb A.)* **This class takes precedence over `DYM_FLOOR_UNDERDETERMINED`.** Report the family, or the contradiction.
   *(Two repairs. One completion giving a positive floor while another permits masses approaching zero satisfied
   both 2 and 4 with no rule to choose. Separately, with no relations printed at all the vacuous reading of
   "permit" made class 4 true as well as class 3, and §3 and §4 then gave two obedient seats contradictory orders;
   requiring a printed relation confines the empty case to class 3, which is exactly limb A's test.)*
5. **DYM_FLOOR_COMPLETION_DEPENDENT** — **no positive floor follows from the printed relations alone**, at least one
   named admissible completion yields a positive floor, and none permits masses approaching zero. **Report, for
   every admissible completion, whether it yields a unique floor, a set or range of positive floors, or no attained
   minimum**, with every resulting value or freedom, and name the completion(s) relied on.
   *(Classes 1, 2 and 5 are separated by a single discriminator — whether a completion-free floor exists. It exists
   and every completion agrees: class 1. It exists and some completion differs: class 2. It does not exist: class 5.
   The earlier wording required **every** completion to yield the **same** floor, so a mixed family — one completion
   determinate, another leaving a range — fitted no class at all.)* **The breaker test is `NOT_RUN` and the
   pattern record is not amended, because the floor is not completion-free.** *(This state was reachable and fitted
   no class: not 1, a completion was required; not 2, the floors are not unequal; not 3, a relation exists; not 4,
   nothing permits zero. A terminal scientific result with nowhere to file is the stall the design claims to close.)*
6. **DYM_SOURCE_BLOCKED** — a pinned source the branch needs cannot be read. The study **waits**; this is not a
   scientific verdict and must never be reported as one. **This class exists because the gate found §7's
   "reports BLOCKED if not" had no class behind it, so the run would have stalled.**
7. **R3D_NO_CLASS** — **only after ruling out `DYM_SOURCE_BLOCKED`:** if **no** evidence is unread or unresolved
   and, after applying the seat-split rule of §9, a required control still fails after two attempts **in any seat**,
   file `R3D_NO_CLASS`; **otherwise file `DYM_SOURCE_BLOCKED`.** *(Class 6 said only that a source "cannot be read",
   which is narrower than the failure it causes, so an unread source satisfied both classes.)* **A scientific class may be filed only from a seat report in which every reached
   control passed**; if the two seats return the same scientific class but exactly one report is control-clean, that
   class is filed **unless** the third seat re-runs the failed control and also fails it, in which case
   `R3D_NO_CLASS` is filed. *(The old wording said "in both seats", so a control failing persistently in one seat,
   with the seats otherwise agreeing, had no rule and two readings of the document diverged at the terminal step.)*

## 5. Controls, each with an exact named code

- **C1 — source identity, bound to the frozen manifest of §2a.** The seat prints the computed SHA-256 of the raw
  bytes of **every** file it reads, with `repr()` of the extracted text where the pinned text is PDF-extracted.
  **Each printed digest must equal its manifest value**; a mismatch, or any read of a source outside the manifest,
  files `DYM_SOURCE_BLOCKED`. The printed digests are the artefact; a claimed pass without them fails.
  `C1_SOURCE_IDENTITY=PASS`. *(Previously "source identity" was identity to nothing named: the document bound no
  path and no expected hash, so a seat could pass having read a different extraction, edition or truncation — and
  choosing which artefact counts as the source chooses which relations exist.)*
- **C2 — completion ledger, printed in full.** The seat prints **a row for every candidate premise or relation
  considered**, with status `SOURCE_DERIVED`, `ADDED_COMPLETION` or `UNRESOLVED`. Every `SOURCE_DERIVED` row carries
  the **pinned source path, page/line locator and verbatim supporting text**; every `ADDED_COMPLETION` row names the
  assumption added. **The full printed ledger is the artefact required for the pass; a summary assertion fails.** An
  `UNRESOLVED` row may not be excluded and forces `DYM_SOURCE_BLOCKED`. `C2_COMPLETION_LEDGER=PASS`.
  *(As written, C2 could be passed by saying it had been done. That is fatal here specifically: relabelling or
  omitting one candidate relation manufactures the no-relation or underdetermined result.)*
- **C3 — deletion probe, K6's corrected form:** delete the **source-pinned field equations**; if a unique floor
  survives on an injected relation alone, that relation is circular and no derived-floor class may be filed.
  **The harness must execute the deleted state and print its captured output**; a claimed pass without that output
  fails. `C3_DELETION_PROBE=PASS`.
- **C4 — GR benchmark.** For every relation used, the seat **prints the stated-limit algebra** showing equality with
  the Schwarzschild form in the exterior limit, **and prints the premise list** for that algebra showing that no
  interior premise entered. The printed algebra and premise list are the artefact; a claimed pass without them
  fails. `C4_GR_BENCHMARK=PASS`.
- **C5 — harness, LIVE.** Execute and print the three commands of §9. `C5_HARNESS_PINNED=PASS`.
- **C5b — path list.** Print every opened path and, **for each path, print `IN_SCOPE` or `OUT_OF_SCOPE` together
  with the exact §9 scope-rule clause applied.** Any `OUT_OF_SCOPE` row **fails** the control. **The complete
  per-path table is the required artefact; a claimed pass without it fails.** `C5B_PATH_LIST=PASS`. *("Check it"
  named no printed comparison, so the check itself was assertion.)*
  Unreached C5/C5b are recorded `NOT_RUN`, never `PASS`. *(Both codes were previously implicit in "as R3A/R3B";
  a control whose code is not named in the document it governs cannot be checked against it.)*
- **C6 — breaker test.** Applies **only if `DYM_FLOOR_DERIVED` is reached**; otherwise `NOT_RUN`, never a
  pass. The five conditions are **copied verbatim below** from `SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md`,
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

  **Comparator endpoints are rounded OUTWARD throughout the table.** *(V6 rounded them inward, so the printed
  interval `[1.730e11, 5.189e11]` did not contain its own computed lower value `1.7298245e11`. Inward rounding
  narrows a comparator, which makes an overlap — and therefore a condition-5 failure — marginally less likely, i.e.
  it biases the study toward declaring a counterexample. The bias was small and unintentional; the convention is
  now stated so it cannot recur silently.)*

  | # | comparator hypothesis | interval (kg) | derived here from §2b by |
  |---|---|---|---|
  | 1 | semiclassical GR + QM: a Planck-scale remnant | `[2.176434e-8, 2.176434e-8]` | `m_P = sqrt(ħc/G)`; a point value, so the interval is degenerate |
  | 2 | Hawking evaporation: the mass just evaporating at the present epoch | `[1.729e11, 5.190e11]` | lower end `M = (t_0 ħ c⁴ / 5120π G²)^(1/3) = 1.7298e11` kg, **rounded down**, from the single-species lifetime `τ = 5120π G² M³/(ħc⁴)` set to `t_0`. **Upper end = 3.0 × the unrounded lower = 5.1895e11 kg, rounded up.** The factor 3.0 is an **asserted bound**, not a derivation: emission into additional species shortens the lifetime at fixed mass and so raises the surviving mass, and the interval is widened to contain that case rather than a single figure being asserted |
  | 3 | stellar collapse: the TOV / neutron-star maximum mass | `[4.375e30, 5.768e30]` | `[2.2, 2.9] M_☉`, an **asserted span** over which the TOV maximum is contested; `2.2 × 1.98892e30 = 4.375624e30` **rounded down to 4.375e30**, `2.9 × 1.98892e30 = 5.767868e30` **rounded up to 5.768e30** |
  | — | ΛCDM | *no interval — predicts no minimum black-hole mass* | recorded so the null case is explicit rather than silently skipped; **it can never match, and that is stated rather than left to be inferred** |

  **Decision rule.** The seat states its derived floor as an interval (a point value is a degenerate interval).
  **"Shared" means that interval OVERLAPS a comparator interval above.** Any overlap **fails** condition 5 and
  therefore fails C6. **Additionally**, if the floor lies within one decade of a comparator interval without
  overlapping it, the seat prints `NEAR_MATCH` with the comparator named — **reported, never decisive**, because a
  decade is a reporting convenience on a scale spanning sixty and must not be allowed to decide a falsification.

  **All four rows are compared and printed, including ΛCDM.** `C6_BREAKER_TEST=PASS` only on a completed table with
  no overlap; or `NOT_RUN` if `DYM_FLOOR_DERIVED` is not reached.
  *(Third round on this condition, and it is worth being exact about how it failed twice. V3 required a comparator
  set to be fixed "before the run is frozen" — but this document IS the frozen artefact, so the requirement was
  satisfied nowhere. V4 supplied values while citing two source files that §2a forbids reading, and labelled one of
  them as being in the manifest when it is not: a seat that read them violated §2a and filed `DYM_SOURCE_BLOCKED`,
  and a seat that did not read them hit "an unread comparator source files `DYM_SOURCE_BLOCKED`". Both paths
  blocked, so the decisive test was pre-disabled a second time in a new form. The fix is not another requirement:
  every value above is computed from §2b here, so there is nothing left to read.)*

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
- **Path list**: every seat prints every path it opened; this lane's own reading tree
  (`../bhu-reading-20260823/sources/`) is **in scope**, another lane's files are not. That distinction is stated
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
  `DYM_SOURCE_BLOCKED` or `R3D_NO_CLASS` — **the third seat adjudicates exactly that split from the printed
  artefacts**, **re-executing any blocked read once before ruling**; its class is filed **only if it agrees with one
  of the two**. If all three differ, or the third seat cannot decide, file `DYM_SOURCE_BLOCKED`. **Every terminal
  path files exactly one declared class.** *(The rule previously engaged only on "different scientific classes", so
  one seat scientific and one blocked was a terminal disagreement that convened nobody and filed nothing.)*
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

R3D_PREREG_V8_READY_FOR_REGATE
