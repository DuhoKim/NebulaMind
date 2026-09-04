# DRAFT — NOT ORDERED — R3-D pre-registration: does the Dymnikova regular-core branch fix a minimum black-hole mass?

**Tori, 2026-09-04 20:57 KST.** Round-3 cluster #4 (proposed by the agy seat; scored 3 × 5). Drafted per Blanc's
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

## 3. Limb structure

**Limb A (~1 seat-day):** does the branch print a size–mass relation at all? If it does not, the K6 obstruction
repeats and the answer follows without deep work — file `DYM_NO_SIZE_MASS_RELATION` and stop.
**Limb B:** if it does, derive the floor and test it against the five breaker conditions.

## 4. Outcome classes — declared now

1. **DYM_FLOOR_DERIVED** — a unique positive floor follows from the printed relations with no added completion.
   Report the formula and value, **and test it against all five breaker conditions**; if it passes them, this is a
   counterexample to the pattern and the pattern record must be amended.
2. **DYM_FLOOR_UNDERDETERMINED** — admissible completions give different floors. Report the freedom; choose none.
3. **DYM_NO_SIZE_MASS_RELATION** — limb A's exit: the branch supplies no relation binding size to mass.
4. **DYM_NO_POSITIVE_FLOOR** — the relations exist and permit masses approaching zero. Report the family.
5. **R3D_NO_CLASS** — a control fails in both seats after two attempts.

## 5. Controls, each with an exact named code

- **C1 — source identity**, on raw bytes with `repr()` if the pinned text is PDF-extracted. `C1_SOURCE_IDENTITY=PASS`.
- **C2 — completion ledger.** Every added completion named as such, never as source-derived.
  `C2_COMPLETION_LEDGER=PASS`.
- **C3 — deletion probe, K6's corrected form:** delete the **source-pinned field equations**; if a unique floor
  survives on an injected relation alone, that relation is circular and no derived-floor class may be filed.
  **The harness must execute the deleted state and print its captured output**; a claimed pass without that output
  fails. `C3_DELETION_PROBE=PASS`.
- **C4 — GR benchmark** as algebra only, supplying no interior premise. `C4_GR_BENCHMARK=PASS`.
- **C5 — harness, LIVE**; **C5b — path list.** As R3A/R3B.
- **C6 — breaker test.** If class 1 is reached, all five pattern-breaker conditions are evaluated and printed
  individually. `C6_BREAKER_TEST=PASS` or `NOT_RUN` if class 1 is not reached.

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

R3D_PREREG_DRAFT_READY_FOR_GATE — NOT ORDERED
