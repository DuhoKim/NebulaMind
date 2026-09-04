# FROZEN — ORDERED — R3-C pre-registration: does ANY construction in the corpus fix an observable magnitude?

**Tori, 2026-09-04 21:02 KST. Version 1. FROZEN pending the fresh referee gate. ORDERED by Duho, "run r3c and r3d", 2026-09-04 21:02 KST.**
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
5. the number **differs from both named comparators** of §8 — flat ΛCDM at Planck 2018, and the same
   construction stripped of its BHU-specific element — by more than its own stated uncertainty.

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
5. **CENSUS_AUDIT_FAILED** — the third seat's 20% re-derivation cannot reproduce a sampled exclusion. The census
   is void: report which exclusion failed and stop. **This class exists because the gate found the stop rule had
   none, so the run would have stalled without a verdict.**
6. **R3C_NO_CLASS** — a control fails in both seats after two attempts.

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
the pattern predicts it will fail. **Three mechanical requirements, because the gate showed that merely requiring a
quotation lets a seat append any source text and pass:**

1. every exclusion names **which** of {shape, scale, frequency, sign, ratio, functional form} the row's claimed
   quantity is, and quotes the establishing phrase **from the PINNED SOURCE PAPER, with file name and line
   number — NOT from the warrant table's claim cell.** The gate's decisive point: the claim cells were authored
   by this lane, so a seat quoting one is still quoting us, and the circularity survives. **A script verifies
   BOTH that each quoted string actually occurs at the cited line of the cited file, AND that the citation
   contains no reference to the pattern** — no occurrence of "pattern", "shape/magnitude", or a citation of
   `SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md`. A citation that fails either check voids the exclusion and
   fails C2;
2. the two seats' exclusion lists are **diffed automatically** (C6); every disagreement is reported, never
   reconciled silently;
3. a **random 20% sample of exclusions is re-derived from the pinned source by the third seat**, which does not
   see the first seats' justifications. A sampled exclusion the third seat cannot reproduce **fails the census**
   and the run stops.

An exclusion justified by reference to the pattern rather than the row's own content is void. The five conditions are fixed here
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

**Condition 5 REWRITTEN to be decidable.** The first gate warned it was not decidable as written — "not shared with
ΛCDM or another standard model predicting it for unrelated reasons" needs a judgement about unnamed models — and the
second gate ruled that *carrying* the warning was not an acceptable resolution, because "separating an undecidable
condition just yields a separate undecidable result." **Both are right, so the condition is replaced rather than
hedged.**

**Condition 5 (operational):** the candidate's computed magnitude must differ, by more than its own stated
uncertainty, from **both** of two named comparators:
  (a) **flat ΛCDM with Planck 2018 parameters**, and
  (b) **the same construction with its BHU-specific element removed** — the boundary, the torsion term, or the
      regular core, whichever the construction adds — evaluated with the identical inputs.

Two named comparators, one numerical test each. **If a seat cannot evaluate (b) because removing the BHU element
leaves no defined model, condition 5 is recorded as `NOT APPLICABLE` for that candidate and conditions 1–4 decide**;
that outcome is reported, never silently treated as a pass.

## 10. Version history — recorded because this document was frozen and then edited three times

A "frozen" preregistration that is silently rewritten is not frozen. Each gate round changed the text, so each round
is listed with the hash the referee actually bound to, and what changed. **The apparent anomaly Blanc raised — an
ACCESS_SHA matching no file in the lane — is explained here: the referee hashed the target at dispatch, and the lane
then edited the target before the sweep.** The proof was valid when made; the file moved underneath it.

| version | sha256 at dispatch | what the gate found, and what changed |
|---|---|---|
| V1 | `acdaa075…26bf0c` | `PREREG_UNSOUND`: circularity prohibition merely stated; condition 5 undecidable |
| V2 | `ece4c6d9…4dbce7` | `PREREG_UNSOUND`: quoting the lane's own claim cells is still self-referential; stop rule with no class |
| V3 | `5c7480b7…4c27a78` | `PREREG_UNSOUND`: the script must also verify citations contain no reference to the pattern |
| V4 | *this version* | that check added |

**The lesson is the lane's, not the referee's:** three gates in twelve minutes each bound correctly to what was in
front of them, and the confusion came from editing a frozen file between rounds. Future rounds amend with a new
version number and hash rather than overwriting in place.

R3C_PREREG_V4_READY_FOR_REGATE

## 9. Inherited discipline, stated so no seat has to infer it

- **Harness, LIVE**: every seat executes and prints `python3 --version`, `sympy.__version__`, and
  `shasum -a 256 $(command -v python3)`. Transcribing expected values fails `C5_HARNESS_PINNED`.
- **Access proof** (Duho's 2026-09-04 20:48 rule): any seat auditing a pinned source prints
  `ACCESS_SHA=<full 64 hex of that file>` as its first line. **No proof, no verdict** — the report is quarantined,
  exactly as `nm_referee_dispatch.sh` does.
- **Path list**: every seat prints every path it opened; this lane's own reading tree
  (`../bhu-reading-20260823/sources/`) is **in scope**, another lane's files are not. That distinction is stated
  because getting it wrong once already produced a spurious `UNDETERMINED` (R3B §5).
- **Stall guard**: every symbolic operation under a 120-second cap; on timeout print `SYMBOLIC_TIMEOUT` and fall back.
- **Unreached limbs**: controls recorded `NOT RUN`, never as passes.
