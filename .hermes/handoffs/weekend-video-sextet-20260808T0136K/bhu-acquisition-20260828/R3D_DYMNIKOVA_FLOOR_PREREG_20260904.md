# FROZEN — ORDERED — R3-D pre-registration: does the Dymnikova regular-core branch fix a minimum black-hole mass?

**Tori, 2026-09-04 21:02 KST. Version 3 (see §8). FROZEN pending the fresh referee gate. ORDERED by Duho, "run r3c and r3d", 2026-09-04 21:02 KST.**
20:56 note. **Drafting is not starting. No derivation has been run.**

## 0. Why this would exist

K6 found entry 51's ECKS mass floor `K6_FLOOR_UNDERDETERMINED`: the density ceiling cannot bound a mass without a
size–mass relation `V(M)` the source never supplies. **The obvious next question is whether the corpus's *other*
regular-interior branch — Dymnikova's de Sitter core (entries 18–20, 55) — does supply one.**

It is also, per the pattern record, one of the two places a **breaker** is most likely: a regular-core metric is
explicit, so if any branch fixes a mass scale from its own geometry, this is it.

## 1. The question, exactly

Do the Dymnikova regular-core metrics, as printed, determine a **closed relation between the core scale, the mass and
the horizon** sufficient to imply a positive minimum black-hole mass — and if so, what is it?

## 2. Objects to bind before arithmetic, or mark ABSENT

The metric and its stated stress-energy; the core scale parameter and what fixes it; which mass (ADM, Misner–Sharp,
Komar); which surface; the regularity conditions; and the de Sitter-limit condition. **No Euclidean volume, uniform
interior, order-unity coefficient or GR exterior may enter silently** — each is an added completion, named and tested
separately, exactly as K6 required.

**Before choosing a limb or an outcome, each seat constructs and prints an exhaustive census** of every equation or
sentence in the pinned Dymnikova sources that mentions or relates **core scale, density, mass, mass function, radius,
horizon, matching surface, regularity, or the de Sitter limit**. Every row, included or excluded, carries source path,
page/line locator and verbatim text. **Exclusion is permitted only for a predeclared reason code** —
`WRONG_BRANCH`, `DEFINITION_ONLY`, `NO_MASS_OR_SIZE_CONTENT`, `DUPLICATE` — **demonstrated by that independent source
text**. Disagreement or missing evidence is `UNRESOLVED`, **may not be treated as absence**, and forces
`DYM_SOURCE_BLOCKED`. **The shape/magnitude pattern record and every prior lane conclusion are forbidden as evidence
for inclusion, exclusion or outcome selection**; the pattern enters this study at exactly one point — C6's breaker
evaluation — and only after class 1 has been reached on other grounds. C2 passes only if this census is printed in
full. *(Without it a seat could report a relation absent, omit the contrary row, and let the lane's own pattern become
indirect support for its own confirmation: C3 tests an injected relation only after the seat has already selected the
source-pinned equations, so it cannot see a relation excluded before that selection.)*

## 3. Limb structure

**Limb A (~1 seat-day):** does the branch print a size–mass relation at all? If it does not, the K6 obstruction
repeats and the answer follows without deep work — file `DYM_NO_SIZE_MASS_RELATION` and stop.
**Limb B:** if it does, derive the floor and test it against the five breaker conditions.

## 4. Outcome classes — declared now

1. **DYM_FLOOR_DERIVED** — a unique positive floor follows from the printed relations with no added completion.
   Report the formula and value, **and test it against all five breaker conditions**; if it passes them, this is a
   counterexample to the pattern and the pattern record must be amended.
2. **DYM_FLOOR_UNDERDETERMINED** — the printed relations admit **at least two positive but unequal floors** under
   admissible completions, **and no admissible completion permits masses approaching zero**. Report the freedom;
   choose none.
3. **DYM_NO_SIZE_MASS_RELATION** — limb A's exit: the branch supplies no relation binding size to mass.
4. **DYM_NO_POSITIVE_FLOOR** — the printed relations, alone or under **at least one** admissible completion, permit
   masses approaching zero. **This class takes precedence over classes 2 and 3.** Report the family.
   *(Precedence is stated because one completion giving a positive floor while another permits masses approaching
   zero satisfied both 2 and 4 with no rule to choose — the classes were not exclusive.)*
5. **DYM_SOURCE_BLOCKED** — a pinned source the branch needs cannot be read. The study **waits**; this is not a
   scientific verdict and must never be reported as one. **This class exists because the gate found §7's
   "reports BLOCKED if not" had no class behind it, so the run would have stalled.**
6. **R3D_NO_CLASS** — a control fails in both seats after two attempts.

## 5. Controls, each with an exact named code

- **C1 — source identity**, on raw bytes with `repr()` if the pinned text is PDF-extracted. `C1_SOURCE_IDENTITY=PASS`.
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
- **C4 — GR benchmark** as algebra only, supplying no interior premise. `C4_GR_BENCHMARK=PASS`.
- **C5 — harness, LIVE.** Execute and print the three commands of §9. `C5_HARNESS_PINNED=PASS`.
- **C5b — path list.** Print every opened path and check it against §9's scope rule. `C5B_PATH_LIST=PASS`.
  Unreached C5/C5b are recorded `NOT_RUN`, never `PASS`. *(Both codes were previously implicit in "as R3A/R3B";
  a control whose code is not named in the document it governs cannot be checked against it.)*
- **C6 — breaker test.** If class 1 is reached, conditions 1–4 are evaluated by the stated calculation, a full
  citation-chain provenance table, a free-symbol probe, and a fixity derivation. **Condition 5 is not decidable as
  written** — a seat cannot establish that a number is "not shared with any standard model" without a bounded
  comparator set. **So before the run is frozen, a finite named comparator set, the observable and tolerance that
  define "shared", and the permitted source corpus are fixed in writing**; every comparison is executed and printed.
  A match fails condition 5; an unread comparator or an incomplete frozen set yields `DYM_SOURCE_BLOCKED`; **only a
  completed no-match table passes it.** All five results and their artefacts are printed.
  `C6_BREAKER_TEST=PASS`, or `NOT_RUN` if class 1 is not reached.

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
gate confirmed D does **not** assume K6's outcome and that `DYM_FLOOR_DERIVED` is genuinely reachable, and judged the
branch "the corpus's most likely candidate to break the pattern".

**V3, this version.** `R3D_GATE_codex_20260904.md` gated `1ecb7ac7…6748f5` as `PREREG_UNSOUND` with five substantive
findings, **all applied**: outcome classes 2/3/4 made exclusive with an explicit precedence; C2 turned from an
assertion into a printed artefact; **an exhaustive printed census of candidate relations required before any limb or
outcome is chosen**, exclusion allowed only on a predeclared reason code shown from source text, and the pattern
record forbidden as evidence for inclusion, exclusion or outcome selection; C6 condition 5 given a bounded frozen
comparator set in place of an undecidable universal negative; the stall fallback and the two-seat split each given a
fileable class. codex found **no defect** in the re-run guard (§6) or the fairness wording and said so, and those are
unchanged. **Also fixed: the completion token sat before §9, so the document ran past its own terminator** — the same
defect found in R3C2's version history the same evening.

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
  the **named numerical/substitution fallback under a second 120-second cap**. If that fallback also times out or
  cannot decide the required proposition, file `DYM_SOURCE_BLOCKED` and **do not pass the affected control**.
- **Seat split**: if the two blind seats return different scientific classes, **the third seat adjudicates exactly
  that split from the printed artefacts**; its class is filed **only if it agrees with one of the two**. If all three
  differ, or the third seat cannot decide, file `DYM_SOURCE_BLOCKED`. **Every terminal path files exactly one
  declared class.** *(Neither the fallback nor the split had a fileable outcome, so either could stop the run with no
  class.)*
- **Unreached limbs**: controls recorded `NOT RUN`, never as passes.

R3D_PREREG_V3_READY_FOR_REGATE
