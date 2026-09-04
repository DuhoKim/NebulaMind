# FROZEN — ORDERED — R3-D pre-registration: does the Dymnikova regular-core branch fix a minimum black-hole mass?

**Tori, 2026-09-04 21:02 KST. Version 5 (see §8). FROZEN pending the fresh referee gate. ORDERED by Duho, "run r3c and r3d", 2026-09-04 21:02 KST.**
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

`G`, `c`, `ħ`, `k_B`, and the Planck mass `m_P = 2.176434e-8 kg` (CODATA 2018). **No other value may be introduced
as "standard"**; anything else is an added completion under C2.

### 2c. The census, and how its exhaustiveness is demonstrated

**Before choosing a limb or an outcome, each seat constructs and prints an exhaustive census** of every equation or
sentence in the pinned Dymnikova sources that mentions or relates **core scale, density, mass, mass function, radius,
horizon, matching surface, regularity, or the de Sitter limit**. Every row, included or excluded, carries source path,
page/line locator and verbatim text. **Exclusion is permitted only for a predeclared reason code** —
`WRONG_BRANCH`, `DEFINITION_ONLY`, `NO_MASS_OR_SIZE_CONTENT`, `DUPLICATE` — **demonstrated by that independent source
text**. Disagreement or missing evidence is `UNRESOLVED`, **may not be treated as absence**, and forces
`DYM_SOURCE_BLOCKED`.

**Exhaustiveness is demonstrated mechanically, not asserted.** For each manifest source the seat **prints the
complete output of a literal, case-insensitive string search** of that source's extracted text for each of these
eleven terms — `core`, `scale`, `density`, `mass`, `mass function`, `radius`, `horizon`, `matching`, `surface`,
`regular`, `de Sitter` — and **every hit appears either as its own census row, or is cited inside a `DUPLICATE` row
naming the row that covers it.** That search output is part of the C2 artefact. **A relation that was never listed
is therefore mechanically distinguishable from one excluded under a reason code** — which the reason codes alone
could not do, since they govern only rows that were surfaced in the first place. *(Both blind seats are lane seats;
a shared blind spot reproduces in both, so blind doubling does not catch an omission. Only an enumeration key a
reviewer can re-run does.)*

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

1. **DYM_FLOOR_DERIVED** — a unique positive floor follows from the printed relations with no added completion.
   Report the formula and value, **and test it against all five breaker conditions**; if it passes them, this is a
   counterexample to the pattern and the pattern record must be amended.
2. **DYM_FLOOR_UNDERDETERMINED** — the printed relations admit **at least two positive but unequal floors** under
   admissible completions, **and no admissible completion permits masses approaching zero**. Report the freedom;
   choose none.
3. **DYM_NO_SIZE_MASS_RELATION** — limb A's exit: **a relation binding size to mass, or bounding the mass, was
   unreproduced from the stated inputs** after the frozen census of §2 was completed.
4. **DYM_NO_POSITIVE_FLOOR** — **at least one printed relation binds size to mass or bounds the mass**, and those
   relations, alone or under **at least one** admissible completion, **permit** masses approaching zero — where
   **"permit" means no positive lower bound on the mass follows.** If the printed relations are mutually
   inconsistent, so that no solution and hence no positive lower bound exists, **file here and report the
   contradiction.** **This class takes precedence over `DYM_FLOOR_UNDERDETERMINED`.** Report the family, or the contradiction.
   *(Two repairs. One completion giving a positive floor while another permits masses approaching zero satisfied
   both 2 and 4 with no rule to choose. Separately, with no relations printed at all the vacuous reading of
   "permit" made class 4 true as well as class 3, and §3 and §4 then gave two obedient seats contradictory orders;
   requiring a printed relation confines the empty case to class 3, which is exactly limb A's test.)*
5. **DYM_FLOOR_COMPLETION_DEPENDENT** — a unique positive floor follows **only under one or more named admissible
   completions**, **every** admissible completion yields **the same** floor, and none permits masses approaching
   zero. Report the formula, **the completion(s) relied on**, and the value. **The breaker test is `NOT_RUN` and the
   pattern record is not amended, because the floor is not completion-free.** *(This state was reachable and fitted
   no class: not 1, a completion was required; not 2, the floors are not unequal; not 3, a relation exists; not 4,
   nothing permits zero. A terminal scientific result with nowhere to file is the stall the design claims to close.)*
6. **DYM_SOURCE_BLOCKED** — a pinned source the branch needs cannot be read. The study **waits**; this is not a
   scientific verdict and must never be reported as one. **This class exists because the gate found §7's
   "reports BLOCKED if not" had no class behind it, so the run would have stalled.**
7. **R3D_NO_CLASS** — after applying `DYM_SOURCE_BLOCKED` and the seat-split rule of §9, a required control still
   fails after two attempts **in any seat**. **`DYM_SOURCE_BLOCKED` takes precedence whenever unread or unresolved
   evidence caused the failure.** **A scientific class may be filed only from a seat report in which every reached
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
- **C5b — path list.** Print every opened path and check it against §9's scope rule. `C5B_PATH_LIST=PASS`.
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
  | 2 | every constant traces | build the citation chain for each constant to its origin | every constant terminates in a source equation or in the §2b constant list; any `we assume/choose/simplest form` terminus fails | the full provenance table, one row per constant |
  | 3 | no free normalisation survives | replace every non-§2b parameter by an algebraically independent free symbol and attempt to recover the printed number | **the printed number IS recovered with no non-§2b parameter chosen** | the printed free-symbol run and its outcome |
  | 4 | no fixity is assumed | list each quantity held constant and locate its derivation | each is derived, not chosen | the fixity table with source line per row |
  | 5 | a measurement could falsify it | the comparator table below, executed in full | **no** comparator matches within tolerance | the completed comparison table |

  **Condition 5's comparator set, observable, tolerance and corpus — fixed here, in the frozen document.** The
  observable is **the minimum black-hole mass, in kilograms**. "Shared" means
  **|log₁₀(M_R3D / M_comparator)| ≤ 1.0** — agreement within one order of magnitude on a scale that spans about
  sixty. **Any match fails condition 5**, and therefore fails C6.

  | comparator (named standard model) | predicted minimum BH mass | value (kg) | source |
  |---|---|---|---|
  | semiclassical GR + QM: Planck-scale remnant | Planck mass | `2.176434e-8` | CODATA 2018 measured constant, §2b |
  | Hawking evaporation: mass surviving to the present epoch | PBH evaporation floor | `≈5.1e11` | `2026_PBH_constraints_evidence_prospects_arXiv_2601.06024.clean.txt` (manifest §2a) |
  | stellar collapse: TOV / neutron-star maximum mass | astrophysical BH floor, 2.5 M☉ | `≈4.97e30` | entry 31's bar, `NS_MASS_WATCH_PREREG_20260902.md` |
  | ΛCDM | **predicts no minimum black-hole mass** | *n/a — cannot match* | recorded so the null case is explicit, not silently skipped |

  **Every comparator is compared and printed, including the ΛCDM row, which is recorded as a non-match by
  construction rather than omitted.** An unread comparator source files `DYM_SOURCE_BLOCKED`; **only a completed
  no-match table passes condition 5.** `C6_BREAKER_TEST=PASS`, or `NOT_RUN` if `DYM_FLOOR_DERIVED` is not reached.
  *(Both seats found condition 5 undecidable in round 1. Round 3 "repaired" it by requiring the comparator set to be
  fixed before the freeze — but this document IS the frozen artefact, so the requirement was satisfied nowhere and
  the decisive test stayed pre-disabled. The content is therefore supplied here rather than demanded.)*

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

- **Harness, LIVE**: every seat executes and prints `python3 --version`, `sympy.__version__`, and
  `shasum -a 256 $(command -v python3)`. Transcribing expected values fails `C5_HARNESS_PINNED`.
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
  | solve `g_tt(r)=0` for horizon radii | bracketed bisection on sign changes (`mpmath.findroot`) | `r/r_g ∈ [1e-3, 1e3]`, 10⁴ log-spaced samples | `mp.dps=30` | root accepted if a sign change brackets it and `abs(g_tt) < 1e-20` there | "the metric has ≥1 horizon for given (M, r₀)" |
  | `r→0` limit of curvature invariants | direct evaluation at `r = 10^-k`, `k = 1…20` | as listed | `mp.dps=30` | finite if `abs(value) < 1e6` and monotone-convergent over the last five `k` | "the core is regular" |
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

R3D_PREREG_V5_PIN_UPDATED_STILL_UNSOUND
