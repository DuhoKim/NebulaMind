# DRAFT — NOT ORDERED — R3-C pre-registration: does ANY construction in the corpus fix an observable magnitude?

**Tori, 2026-09-04 20:57 KST.** Round-3 cluster #3 (proposed independently by two blind seats). Drafted per Blanc's
20:56 note so it is ready the moment Duho rules. **Drafting is not starting. No derivation has been run.**

## 0. Why this would exist

`SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md` now records **six** instances of one shape — the construction fixes a
shape, the magnitude a measurement would test stays free — and, at Blanc's insistence, **the five conditions that would
break it**. This study is the systematic search for a construction that satisfies those five.

**It is the breaker test, run deliberately rather than waited for.** Its value does not depend on which way it comes
out: a counterexample refutes a pattern the lane has been building all week; no counterexample converts an impression
into a measured statement with a denominator.

## 1. The question, exactly

**Over every quantitative claim in the 51-row corpus, does any construction compute an observable magnitude satisfying
all five breaker conditions of the pattern record?**

Restated as the conditions, which are the prereg's, not the seat's to soften:

1. an observable **magnitude** is computed — not a shape, scale, frequency, sign, ratio or functional form;
2. **every constant traces** to the construction's own equations or to measured fundamental constants, **with the
   citation chain followed to its end** (the R3A test);
3. **no free normalisation survives** a free-symbol probe;
4. **no fixity is assumed** where falsifiability depends on it (the R3B test);
5. the number is **not shared with ΛCDM** or another standard model predicting it for unrelated reasons.

## 2. Limb structure — cheap first

**Limb A (~1 seat-day):** screen all 51 rows on condition 1 alone, from the warrant table's existing claim cells plus
the pinned sources. Most rows will fail condition 1 without any derivation work. **Print the surviving shortlist.**
If the shortlist is empty, file `CENSUS_NO_CANDIDATE` and stop — the pattern holds trivially and no deep work is done.

**Limb B (2–3 seat-days):** apply conditions 2–5 to each survivor, in order, stopping each candidate at its first
failure. Report the failure condition per candidate.

## 3. Outcome classes — declared now

1. **CENSUS_COUNTEREXAMPLE** — at least one construction satisfies all five. **The pattern is broken.** Report it, and
   the pattern record must be amended to say so.
2. **CENSUS_PATTERN_HOLDS** — every candidate fails at a named condition. Report the count, the denominator, and which
   condition each failed at.
3. **CENSUS_NO_CANDIDATE** — nothing survives limb A. The pattern holds, and the record must say it held *trivially*,
   which is weaker than class 2.
4. **CENSUS_CLASSIFICATION_ARTEFACT** — the outcome depends on how "observable magnitude" is drawn. **INCONCLUSIVE**;
   state the boundary cases exactly. **This self-critical class must be reachable and must not be quietly avoided.**
5. **R3C_NO_CLASS** — a control fails in both seats after two attempts.

## 4. Controls, each with an exact named code

- **C1 — denominator stated.** The count of rows screened, rows excluded, and why, printed before any verdict.
  `C1_DENOMINATOR_PRINTED=PASS`.
- **C2 — condition-1 screen is mechanical.** Each exclusion cites the row's claim cell and names which of shape /
  scale / frequency / sign / ratio / form it is. `C2_SCREEN_MECHANICAL=PASS`.
- **C3 — citation chains opened.** For every survivor, each cited coefficient is chased to a derivation or marked
  `BLOCKED`, **printing exact text and line numbers** — the wording R3A's gate forced. `C3_CHAINS_OPENED=PASS`.
- **C4 — free-symbol probe** on every survivor. `C4_FREE_SYMBOL_PROBE=PASS`.
- **C5 — harness, LIVE.** Executed, not transcribed. `C5_HARNESS_PINNED=PASS`.
- **C5b — path list.** Every path opened printed; any outside this lane fails. `C5b_NO_CROSS_LANE_ACCESS=PASS`.
- **C6 — adversarial re-screen.** A second seat re-screens the **excluded** rows looking for a wrongly-excluded
  candidate, **printing an independent list of exclusions for automated diffing against the first seat's list**;
  any row on one list and not the other is reported, not reconciled silently. A census that only checks its
  survivors is not a census. `C6_EXCLUSIONS_RECHECKED=PASS`.

Controls in an unreached limb are `NOT RUN`, never passes.

## 5. Non-circularity

**The pattern record is the hypothesis under test and may not be used as evidence.** No row may be excluded because
the pattern predicts it will fail; **to make this mechanical, every exclusion must quote the exact source text and
line number that justifies it, and a seat whose exclusion carries no quotation fails C2.** An exclusion justified
by reference to the pattern, rather than to the row's own content, is void. The five conditions are fixed here
before any screening and may not be adjusted after seeing which rows survive.

## 6. Seats, discipline, scope

Blind double, third seat via `nm_referee_dispatch.sh` on a split with **ACCESS_SHA proof** (Duho's 20:48 rule),
independent second route, Kimi on arithmetic with a no-fallback control, one-page check sheet, Tori re-runs every
script, critic note before any ruling. Executable and harness discipline as R3A/R3B. Published sources only; nothing
from another lane; no tier, token, standing or stamp moves. Paper HOLD; **the record's wording for any negative finding must be
"unreproduced from the stated inputs," not "error."**

## 7. Cost

Limb A ~1 seat-day; limb B 2–3 more. No data acquisition.

## 8. Gate record

`R3CD_DRAFT_GATE_20260904_agy.md`: `GATE_C=PREREG_SOUND_WITH_REPAIRS`, **three repairs applied**. The load-bearing one
was the circularity prohibition — the gate called it "the most rotten part" because it was **stated, not enforced**.
Exclusions must now quote source text and line numbers, and an exclusion justified by the pattern is void.

**One warning carried, not repaired away.** The gate judged **breaker condition 5 not decidable as written** —
"not shared with ΛCDM or another standard model predicting it for unrelated reasons" requires a judgement about other
models. **Any run of this study must report condition 5 separately from 1–4 and state the models it compared against**,
rather than folding it into a single verdict. This is recorded here so a future run inherits the warning; the condition
is not silently dropped, because dropping it would make a counterexample too easy to claim.

R3C_PREREG_DRAFT_READY_FOR_GATE — NOT ORDERED
