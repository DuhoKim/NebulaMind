# R3C / R3D gate reconciliation — a second seat, and what it settles

**Tori, 2026-09-04 21:17 KST.** Duho's 21:11 order: re-gate with a different seat, verify the hash myself, give the
new seat the frozen texts only, keep every filing, and reconcile in writing.

## What was done

- **Seat:** `codex`, not agy, dispatched **through `nm_referee_dispatch.sh`** via a shim
  (`_tmp_codex_gate_shim.sh`) so the wrapper's own access-proof computation and quarantine logic were preserved
  unchanged; only the engine differs.
- **Blind:** the brief barred it from opening any file whose name contains `GATE`. It saw no agy verdict, no repair
  list, and no note.
- **Verification:** Tori recomputed each target's sha256 **after** the run and compared it to the returned line, rather
  than trusting the seat.

| target | sha256 of the file | ACCESS_SHA returned | match |
|---|---|---|---|
| R3C V4 | `c5e9462000f57bf8bb160734fa78859235c39e936e09a545fd44193003572381` | identical | **yes** |
| R3D V2 | `1ecb7ac7ae80352ea72bf2ab3c46faf699fe0c1f1e84761f72e4e54bd76748f5` | identical | **yes** |

## The verdicts

| | agy | codex (independent, blind) |
|---|---|---|
| R3C | `PREREG_UNSOUND` (×3 rounds) | **`PREREG_UNSOUND`** |
| R3D | `SOUND` → `UNSOUND` → `SOUND_WITH_REPAIRS` | **`PREREG_UNSOUND`** |

**The second seat did not pass what agy failed. It failed both, independently, quoting each sentence and confirming
its presence in the file it hashed.**

## Where they agree, and where they differ

**Agree (R3C):** the design is unsound. Both reach it through the same soft spot — that a census testing a
lane-authored pattern can smuggle the pattern into its own exclusions.

**Differ (R3C):** codex found defects agy did not, and they are real:
- **C2 still points at the warrant table's claim cell** while §5 rule 1 now requires quoting the *pinned source*. That
  is an internal contradiction **I introduced** in the V3 repair and did not propagate. codex caught it; agy did not.
- **`R3C_NO_CLASS` is not exhaustive**: "a control fails in both seats after two attempts" leaves a control that fails
  twice in one seat and passes in the other with no class.
- Condition 5's `NOT APPLICABLE` path and class 4's reachability need tightening.

**Differ (R3D):** agy's last word was `SOUND_WITH_REPAIRS`; codex says `UNSOUND` on the completion ledger, the breaker
test's conditional invocation, and the object-binding list.

## What this settles about the referee question

Duho asked whether a wider re-examination of agy-gated work is indicated. **On this evidence, no — and I say that
against my own interest**, since a referee problem would have excused four failed rounds.

- On **verdicts**, an independent engine reached the same bottom line on R3C. Agreement between engines is evidence
  the verdicts were tracking the text.
- On **presentation**, Blanc's findings stand and are real: agy quoted un-repaired sentences that were repaired, and
  flipped R3D on unchanged text. Both are defects in how the verdict was justified, not in the verdict itself.
- The `ACCESS_SHA` anomaly was **mine**, not agy's: I edited a frozen document between rounds
  (`R3C_GATE_ANOMALY_EVIDENCE_20260904.md`).

**I have not re-opened any previously passed gate and will not.** If Duho wants a wider look, that is his call.

## My judgement, which is the part he should read

**I have patched these two preregistrations through four gate rounds and they are still unsound.** Each round fixed
what was named and exposed something adjacent. That is no longer convergence; it is grinding.

**I am stopping the patch cycle rather than starting a fifth round**, because the failures are no longer clerical:

- **R3C's problem is structural.** A census that tests a pattern its own author wrote needs its exclusion criteria to
  come from somewhere other than the author. Three rounds tried to fix that with quoting rules; the fourth found the
  rules pointing at two different sources at once. **The design likely needs an external criterion — outcome classes
  defined before the pattern was, or a seat that has never read the pattern record — not another clause.**
- **R3D's problem is smaller** and probably one honest round from sound, but it inherits R3C's breaker test and should
  not be finalised while that is unsettled.

**Recommendation: neither runs tonight.** R3C needs redesigning, not repairing. I would rather report that than hand
Duho a study whose gate I eventually wore down.

## Filings preserved, none deleted

`R3CD_DRAFT_GATE_20260904_agy.md`, `R3CD_FROZEN_GATE_20260904_agy.md`,
`R3CD_FROZEN_GATE_V2_20260904_agy.md` (+ `.note` identifying its bound target),
`R3CD_FROZEN_GATE_V3_20260904_agy.md`, `R3C_GATE_codex_20260904.md`, `R3D_GATE_codex_20260904.md`. Marked, not
rewritten.

R3CD_GATE_RECONCILIATION_COMPLETE
