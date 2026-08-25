# REAL-GEOMETRY RESULT — the successor design, measured on DR10

Hwao, 2026-08-25. Authorized by Duho this afternoon as a catalog-only data step (no images,
no χ). **In the event no fetch was needed:** both inputs were already on disk from the
predecessor's authorized work, so this used strictly less than was authorized.

## Inputs (already acquired, digests recomputed today)

| artifact | sha256 |
|---|---|
| `survey-bricks-dr10-south.fits.gz` (release brick universe + geometry) | `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a` |
| `combined_per_brick_counts.csv` (grouped TAP counts) | `4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0` |

Provenance of the counts: NOIRLab Astro Data Lab async TAP, `https://datalab.noirlab.edu/tap/async`,
tables `ls_dr10.tractor_s` / `ls_dr10.photo_z` / `ls_dr10.bricks_s`, verbatim ADQL archived in
`_tori_parent_row_count_evidence/*.adql`. Submission is CLOSED in that runner.

## Count oracle (BS-2c) on real data

- universe **366,912** bricks; **270,577** with objects; **96,335** zero rows materialized
- objects placed **832,393 / 832,393**, zero count keys outside the universe
- **count-weighted Var(cosθ) = 0.445201**, independently reproducing the scope note's frozen
  full-keyspace 0.4452
- `validate_count_table()` PASSED: `{"rows": 366912, "zero_rows": 96335, "universe": 366912,
  "total": 832393}`

## Selection (BS-2o/2s) at the frozen requirement

The vectorized greedy used here is not a second definition: its order is proven identical to
the pinned `greedy_ledger()` on 40 random cases before use. (The pinned implementation is
O(n²) in Python and will not run at 270,577 bricks — a finding to carry into the prereg.)

| | dead run | successor, real geometry |
|---|---:|---:|
| bricks | 60,308 | **6,446** |
| objects (raw) | 208,407 | **65,062** |
| Var(cos θ) | 0.0580 | **0.7547** |
| N_eq | 36,253 | **120,006** |
| image bytes | 735.9 GB | **~77 GB** |

|cos θ| over the selected set spans 0.3764 → 1.0000: the polar selection the design asked for.

## Stage P on the real geometry — the decisive number

Measured null: 20,000 permutations, **z\* = 3.0200** (normal reference 3.0902 — again
anti-conservative on real polar geometry, as the fixture family predicted).

**Successes 997 / 1000** at the frozen labelling floor a = 0.85 with A = 0.0408 injected.
Pass rule x ≥ 962. **PASS.**

**Re-run under the self-verifying gate (v4), because the first run used calibrated decisions
alone — the logic both round-6 gates called unsound.** Stage P now re-tests every
near-boundary success against an independent 20,000-permutation run and fails closed on a
single unconfirmed one. On this geometry: **77 boundary trials, 77 confirmed, 0 refuted,
verdict PASS** (629 s). The headline was not wrong; it had not been audited. It has been now.
For contrast, on a fixture sized to sit at ~50% power the same mechanism refuted 2 of 7
boundary successes and failed the stage closed — the defect is real, this geometry simply
does not exhibit it.

The dead run's power at the same floor was ~52% and no accepted subset of its footprint could
reach 95%. This footprint reaches **99.7%** with about a tenth of the download.

## What this does NOT establish

No image byte was fetched; no χ was read; nothing is frozen. This is Branch B (DR10) geometry;
Branch A (DR11) would need its own counts. The prereg's remaining gate findings still stand —
this fills the class-P inputs those findings said could not be closed by writing alone.

---

## CORRECTION, 2026-08-25 (round-7 gate, verified independently by me)

The codex round-7 gate reproduced the Stage-P result exactly — 997/1000, 77/77 boundary
confirmations, PASS — and then found two defects in how the geometry above was produced. I
re-ran both checks myself; **both are confirmed, and both correct numbers reported earlier.**

**1. The 6,446-brick figure is a greedy PREFIX, not the frozen selection.**
`run_real_selection.py` stopped the greedy at the leverage target and never ran the reduction
pass. Verified: brick **155487** is removable while the set still meets the target
(L_ret 40,001.9 against a 40,000.0 target). The frozen `local_pass()` would reduce further, so
**6,446 bricks and ~77 GB are upper bounds, not the frozen algorithm's output.** The direction
is favourable — the real selection is smaller — but it is not the number I claimed it was.

**2. The planner in `successor_ref_v4.py` is NOT the frozen planner, and against the real
brick table it reproduces the very defect it claims to prevent.** Verified on the actual
`survey-bricks-dr10-south` table (712 bricks in the dec ≤ −86.5 band):

| object | my planner returns | needs |
|---|---|---|
| 10997315463551936 (dec −88.59) | `['3385m885']` | also **3471m885** |
| 10995116744378804 (dec −87.13) | `['2894m872']` | also **2857m870** |

It returns the home brick only — exactly the enumeration failure that produced the
60,308-vs-60,310 gap. The closure fixtures passed only because they ran on a synthetic grid
whose neighbour relationships I had constructed.

**Why this happened, plainly:** round 6 asked me to "pin and implement the cutout planner as
code." I implemented a *new* planner instead of pinning the *existing frozen* one. The frozen
planner is in the lane and is correct — called directly earlier today it returned
`['3385m885', '3471m885']` and `['2857m870', '2894m872', '2902m870']`, both complete.

**The repair** is therefore to delete my reimplementation and bind BS-2m to
`_objmanifest_20260820/build_object_manifest.py::plan_candidate_bricks` with its adapter and
geometry sidecar digests, and to re-run the selection through `local_pass()`. Not done yet.

**What survives unchanged:** the count oracle (366,912 universe, 832,393 placed,
Var = 0.445201) and the Stage-P power result on the geometry actually used — independently
reproduced by the gate. The power conclusion is sound for that geometry; the geometry was not
produced by the frozen chain.

---

## BOTH CORRECTIONS APPLIED, 2026-08-25 16:4x KST

**1. The planner is now the frozen one.** My reimplementation is RETIRED — it raises if
called — and BS-2m binds to `_objmanifest_20260820/build_object_manifest.py`'s
`plan_candidate_bricks` with its pinned adapter (`frozen_planner_digest()` =
`36bbbf250215…`). Verified against the real survey-bricks sidecar:

| object | frozen planner returns |
|---|---|
| 10997315463551936 (dec −88.59) | `['3385m885', '3471m885']` ✔ |
| 10995116744378804 (dec −87.13) | `['2857m870', '2894m872', '2902m870']` ✔ |

The closure fixtures now run against the real brick table and the real historical objects
instead of a synthetic grid, and a manifest omitting those two neighbours is refused **by
name**: `['2857m870', '3471m885']`.

**2. The selection now runs through the frozen reduction pass.** The reduction removes
exactly **one** brick — so the earlier figure was off by one, not materially wrong, but it is
now the frozen algorithm's output rather than an unreduced prefix. The fast reduction used at
scale is proven equal to `local_pass()` on 30 random cases (an earlier version reduced from
the whole ordered set instead of the greedy prefix and disagreed on 1 of 30 — the prefix cut
is part of the rule, not an optimisation).

**Corrected selection (Branch B, DR10):**

| | declined run | successor (corrected) |
|---|---:|---:|
| bricks | 60,308 | **6,445** |
| raw objects | 208,407 | **65,060** |
| retained objects | — | 53,005 |
| Var(cos θ) | 0.0580 | **0.754664** |
| N_eq | 36,253 | **120,002.9** |
| image bytes | 735.9 GB | **~76.8 GB** |

Stage P was measured on the pre-reduction geometry (53,006 planning objects); the reduced set
differs by one brick and one retained object, so that result is not restated here as if it
had been re-measured. It will be re-run on the reduced set before any freeze.

---

## ROUND-8 CORRECTION: the reduction was missing a phase (2026-08-25 17:5x KST)

The codex round-8 referee reproduced this receipt's NPZ exactly and then found that the fast
reduction implemented only `local_pass()`'s **removal** loop — it omitted the
**swap-then-removal** phase entirely. Their counterexample (27 bricks, seed 2026082509, trial
47) gets **six** bricks from the frozen rule and **seven** from removal-only. My "proven equal
on 30 random cases" was insufficient: 30 cases never fired a swap.

**Repaired and re-verified.** The swap phase is implemented (`_swap_then_remove`): accepted
bricks ascending by brickid × unaccepted positive-count bricks ascending by brickid, commit the
first swap after which a removal becomes legal. It now reproduces the referee's counterexample
exactly (`[1003, 1015, 1017, 1018, 1021, 1022]`, L = 165.7433) and matches the frozen
`local_pass()` on **400 cases in the referee's own seed and regime, zero mismatches**.

**Effect on the real selection: none.** Re-running with the swap phase gives the same
**6,445 bricks**, the same single removed brick `155487`, the same L_ret = 40,000.960 — the
swap scan finds no legal improving swap on this geometry. The number did not move, but the
equivalence claim behind it was false and is now true. `real_selection_swapped.npz` records the
full-algorithm result.

Also repaired this round: the count-oracle completeness proof no longer compares a caller's
total with itself — the ungrouped total must equal the **pinned release total 832,393**, and
omitting the proof input is refused; and Stage P now confirms a deterministic sample of
non-boundary successes as well as the boundary band, and measures whether the shared reference
null is conservative against individual trials' own nulls, failing closed if it is not.

---

## STAGE P ON THE REDUCED SET: **FAIL** (2026-08-25 18:2x KST) — and what that retracts

Run on the set the frozen chain actually produces (6,445 bricks, 53,005 planning objects,
N_eq 120,003), under the widened audit added in round 8. Result, verbatim:

    calibrated successes   : 995/1000   (rule x >= 962)
    audited trials         : 81 (boundary band + sampled far)
    confirmed / refuted    : 81 / 0
    reference z*           : 3.1220
    non-conservative nulls : 2
       t35:  ref 3.1220  own 3.1672
       t275: ref 3.1220  own 3.1957
    VERDICT                : FAIL

**It did not fail on power.** 995 of 1000 clears the 962 rule comfortably, and every one of
the 81 audited successes — boundary band plus sampled far-field — was confirmed by an
independent permutation run. Zero refutations.

**It failed on the assumption underneath the method.** Stage P measures ONE reference null per
prefix and applies it to all 1,000 trials. Round 8's referees said that had never been shown
conservative; the check added in response now measures it, and on this geometry it is
**false**: 2 of 8 sampled trials have their own standardized critical value ABOVE the shared
reference (3.1672 and 3.1957 against 3.1220, up to +2.36%), while the residual margin
`PWR_CONSERVATISM` is 1.01. For those trials the shared null sets a threshold that is too
low, so a success could be counted that its own null would not grant.

**What this retracts.** The earlier **997/1000 PASS** on the pre-reduction geometry was
measured *before* this check existed. It reported no conservatism test because none was run.
On the evidence here it would very likely fail the same check. **The successor's power claim
is therefore not currently established** — not refuted either; unestablished. It should not be
cited as 997/1000 PASS without this qualification, and this receipt's earlier sections must be
read with this section attached.

**What would establish it,** in order of preference: (a) take the reference null as an ENVELOPE
— the maximum standardized critical value over a sampled set of trials, not trial 1's — with a
margin above that; (b) per-trial nulls for every counted success, which is exact and
expensive; (c) raising the deflation to cover the measured spread, which is fitting a constant
to this geometry and is the weakest of the three. Not yet chosen, not yet implemented.

The audit catching its own author's method is the reason it was built. It is working.
