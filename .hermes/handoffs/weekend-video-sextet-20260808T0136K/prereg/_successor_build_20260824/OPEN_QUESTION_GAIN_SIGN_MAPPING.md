**STATUS: RULED — option A (position-dependent accuracy, redrawn), with WORST CASE OVER DRAWS as the
reduction policy. Principal, 2026-08-29, relayed by Blanc.** B is discarded as the gate
mapping. **B is not yet retired from the record** — see constraint 3. What remains before BS-3g can be
filled is the **draw set**: its count, its generator and its stopping rule, specified below and not
yet frozen.

# THE γ → COUNTERFACTUAL SIGN-VECTOR MAPPING — raised, tested, ruled

**Raised 2026-08-29 11:2x KST by Hwao, at exactly the point the standing orders said to stop.** The
orders attached a condition: *"when you reach the counterfactual sign-vector mapping for a given γ,
stop and raise it as its own question. Do not choose that mapping quietly."* This is that stop, and
this section is now the record of what happened after it — **the file sat unchanged from 14:58 while
two rulings and two feasibility runs went past it, which is the same staleness this lane has been
clearing everywhere else, in the file that documents the decision itself (Blanc, 22:15).**

## History, in order

**A NOTE ON THE TIMES, because this table would otherwise carry known-wrong ones.** Blanc's relay
headers this evening were stamped from estimate rather than from the clock and ran **ahead** of it —
the relay headed 22:15 was sent at 21:56 (his correction, 21:57, read from `date`). **The ORDER of the
rulings is correct and he confirms every one of them was given; the absolute times in relay headers
are not usable.** Every time below is therefore either a **file mtime** or a `date` reading in this
lane, and rulings — which arrive by relay and produce no file of their own — are recorded by
**position**, anchored between the artifacts that precede and follow them.

| when (KST) | source of the time | what |
|---|---|---|
| ~11:2x | lane record | Question raised. Three candidates: **A** redrawn under position-dependent accuracy, **B** deterministic adversarial flip, **C** analytic propagation (rejected on sight — option (a) wearing a new hat). |
| 14:58 | file mtime (Blanc) | My reading filed: **B for the gate, A as a reported diagnostic.** My stated doubt: *"whether B can pass at all… that should be checked before B is frozen."* |
| 19:54 | file mtime | **First feasibility attempt — INVALID, and I say so before quoting it.** `n_perm = 400` put the p floor at `2.5e-3`, foreclosing `REPRODUCED-LONGO` (needs `p < 0.001`) outright; the baseline was `INCONCLUSIVE`, the **absorbing** outcome, so no verdict change was detectable however fragile the gate was. **It could not have answered the question it was run to answer.** |
| between 19:57 and 20:25 | position | **Principal ruling 1: retry it properly, with the positive control stated first.** |
| 20:25 | file mtime + commit | `FEASIBILITY_PRECOMMIT_2_GAIN_OPTION_B.md` **committed blind at `13e48e3c4`**, before the sweep ran, carrying the reading table and the abort conditions. |
| 20:27 | file mtime | **Valid run.** `f*` between **0.000406 and 0.000996** — between **20 and 49 flipped signs out of 49,211**. Pre-registered reading at `f* < 0.01`: **B is not a gate; A becomes the live candidate.** |
| between 20:27 and 21:58 | position | **Principal ruling 2: option A, with WORST CASE OVER DRAWS.** |

## What made the retry valid, recorded because it is the difference between the two runs

Blanc asked for these specifics by name.

- **A baseline that was not the absorbing outcome** — `REJECTED-AT-LONGO-AMPLITUDE` on a null sky
  (`A_inj = 0`) at the production `N = 49,211`.
- **An `n_perm` whose p floor foreclosed nothing** — `n_perm = 5000`, floor `2.0e-4`, **five times
  below** the tightest threshold in the table.
- **A deletion probe that PASSED BEFORE ANYTHING WAS READ** — baseline `REJECTED-AT-LONGO-AMPLITUDE`
  against a probe fixture at `INCONCLUSIVE`, demonstrating the harness reports verdict changes at all.
- **A seed chosen by the pre-committed ascending rule, blind to the sweep** — first seed whose
  *baseline* met the criterion. Seed 1, the first tried.

**The first attempt had none of these.** That is what a positive control buys, and it is why the
invalid run is recorded above rather than deleted.

## The near-miss, and the correction that came out of it

Blanc asked whether `|Â| + 3σ = 0.04152` against `A_LONGO = 0.0408` meant something about the design,
and read it as ordinary null-fixture behaviour. **My answer was that the two observations are one
observation.** The rejection branch needs `|Â| + 3σ < A_LONGO`, the baseline sits at 0.03531 against
0.0408 — **a margin of 0.0055** — and each adversarially flipped sign moves `|Â|` by roughly
`2/(N·Var(c))` in the worst direction. The near-miss and the cheapness of the adversarial construction
are the same thin margin seen twice. **A gate built on that margin is fragile by construction, not by
accident.** Blanc has recorded that his reading was wrong and told the principal, in the relay carrying ruling 2.

## THE RULING, AND WHAT IT STILL NEEDS

**Option A: `a(c) = a₀ + γ·(c − c̄)`, signs redrawn under the position-dependent accuracy — the same
shape production already uses in `inject_signs`, where `s = −lat` with probability `1 − a_b`.
Reduction to a single verdict: WORST CASE OVER DRAWS.**

A is **stochastic**: the counterfactual is a distribution over sign vectors, not a vector. The ruling
fixes the reduction. It does **not** by itself make the gate well-posed, and the three constraints
below are the conditions the principal attached.

### Constraint 1 — the draw set is defined BEFORE the worst case

**"Worst case over draws" is only well-posed once the draws are preregistered**, because the worst
case is monotone in the number of draws: with an unfixed count the gate deepens the longer it runs and
becomes a function of how long I ran it rather than of the design. **This is the same defect as an
unpinned harness constant, one level up** — it is the strictness of the gate, not just a parameter.

Three things must be frozen together, and each must be checkable from the receipt alone:

1. **COUNT `D` — one fixed integer, frozen before any draw is generated.** `D` must be stated with
   **what it means**: the maximum of `D` exchangeable draws sits at the `D/(D+1)` expected quantile of
   the draw distribution, so `D` **is** the gate's strictness and must be chosen as such rather than
   for convenience. **Proposed: `D = 99`, targeting the 99th percentile**, consistent with this
   study's conservatism elsewhere. **The value is a preregistered parameter and the principal may set
   a different one; the requirement that it be one fixed, meaning-stated integer is not negotiable.**
2. **GENERATOR — named algorithm, named seed sequence, fixed in advance.** Draw `i ∈ [1, D]` uses a
   seed derived from a single frozen master seed by a stated rule, so the entire draw set is
   reproducible from the receipt. **No seed may be selected after seeing any verdict**, which is the
   thing I called innocuous-looking and outcome-deciding when I raised this question.
3. **STOPPING RULE — exactly `D` draws, all evaluated, no early stop and no continuation.** Not
   "until it fails" (which always fails eventually) and not "until it passes" (which is worse). **A
   run that evaluates fewer or more than `D` draws is void, not a smaller or larger gate.**

**Checkability:** the BS-3g receipt must carry `n_draws`, the generator identifier, the master seed,
and a digest over the **per-draw verdict sequence** — so a verifier who did not write the harness can
replay the draw set and confirm the worst case is the worst of exactly those `D` verdicts. **A
worst-case claim whose draw set cannot be replayed is an assertion, not a measurement.**

### Constraint 2 — what happens if worst-case fails as reliably as B did

**Stated now, before the run, so it cannot be chosen after seeing the answer.** The margin is thin
enough that ~30 signs out of 49,211 cross it; an adversarial worst case over a distribution may be no
kinder.

**If the worst case over `D` draws crosses a verdict boundary at any γ within the bound, that is
EVIDENCE ABOUT THE DESIGN and is reported as such.** Specifically: that the rejection margin
`A_LONGO − 3σ` is too thin at this `N` and this calibration for **any** adversarial-family gate to
pass, which is a property of the study, not of the mapping. **It is not a third mapping failure and it
does not send me to a fourth candidate.** The report quotes the margin, the `N` and the calibration it
was measured at, and the design question — whether `N` or the calibration accuracy must change — goes
to the principal. **I will not respond to a failure here by searching for a mapping that passes.**

### Constraint 3 — B is discarded as the gate mapping, NOT retired from the record

**The principal ruled on the mapping, not on retiring B.** The feasibility result rests on **one
fixture at one calibration**, and the margin `A_LONGO − 3σ` depends on `N` and on calibration
accuracy. **The margin must be re-derived at the real calibration before B is finally discarded in the
text.** Until that re-derivation exists, the draft says B was discarded **by ruling**, with the
evidence and its stated limit, and does not claim B is impossible.

## What this unblocks and what it does not

**Unblocks:** the mapping family is chosen, so `ref/gain_counterfactual_path.py` — which ships **no**
mapping and raises `MappingNotFrozen` rather than defaulting — now has a named target to implement.
The `_TEST_ONLY_flip_fraction_mapping` in its self-test **still encodes no claim about the instrument
and must never be promoted**; it is used only where it is already used.

**Does not unblock BS-3g.** The slot stays **DESIGN/UNFILLED** and `mapping_id` stays at the literal
`MAPPING-NOT-PREREGISTERED`, because **a mapping family is not a preregistered mapping**: constraint 1
makes the draw set part of the mapping's identity, and the draw set is not yet frozen. A `mapping_id`
naming A before `D`, the generator and the stopping rule are pinned would name something that does not
yet exist.

**Unchanged:** option C stays rejected and visible. **γ̂ remains unmeasured and no measurement of it is
authorised here.** **v9 stays frozen at `6a9abbbd`.** **BS-6 and the first image byte remain blocked.**
Nothing here is evidence about the sky — synthetic fixtures, no real χ.
