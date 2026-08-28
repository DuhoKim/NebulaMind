# Yui — identity unit-test receipt (feasibility spike, §10 item 1)

2026-08-12 11:04–11:18 KST. Authorized by Duho ("authorize the feasibility spike") under
Kun's gate (PASS AS A DESIGN BRIEF; NO EMPIRICAL SKY RUN YET). Binding spec:
`reviews/LANA_SPIN_DESIGN_BRIEF_20260812.md` §10 item 1.

## Boundary compliance

**No sky statistic on real data.** Every image in this work is synthetic, generated
analytically on the pixel grid by `spike/yui_identity/w_chi.py`. Nothing reads, fetches, or
references any survey catalogue, sky position, or real image — including Tori's retained
5,760-byte test cutout, which was not touched. No bulk acquisition. The natural next step
(running w on real galaxies) is NOT taken: that is the boundary, and reaching it cleanly is
the outcome.

## What was built

- `spike/yui_identity/w_chi.py` — `mirror(x) := np.fliplr(x)` (pure index reversal);
  `chi(x) := (w(x) − w(mirror(x)))/2`; a deterministic, training-free Ganalyzer-class
  `w(x)`: nearest-neighbour polar binning (no interpolation anywhere), per-radius azimuthal
  intensity peak by argmax, arm-agnostic (period-π) unwrap, least-squares slope of θ against
  ln r. No network, no training set.
- A synthetic generator: two-armed log-spiral disks, both parities, pitch 10–40°,
  inclination 0–60° (analytic squeeze, no resampling), peak S/N 2–50, seeded noise;
  plus armless disks as the chirality-free null. 1,000 spiral images in the test grid.
- `spike/yui_identity/run_identity_test.py` → `spike/yui_identity/results.json`.

## THE IDENTITY RESULT — exact statement

**χ(mirror(x)) = −χ(x) held BIT-EXACTLY on 1000 of 1000 synthetic spirals**: for every
image, the 64-bit IEEE-754 pattern of χ(mirror(x)) is identical to the pattern of −χ(x),
and max over the grid of |χ(mirror(x)) + χ(x)| is exactly 0.0. Supporting bit-level facts,
each verified on the same grid: `mirror(mirror(x))` is byte-identical to `x` in 1000/1000
cases, and `w` is bit-deterministic on repeated evaluation.

Why it is exact and not merely close: with a pure index-reversal mirror, both sides reduce
to the SAME two evaluations w(x)=a and w(mirror(x))=b — one side computes fl((a−b)/2), the
other fl((b−a)/2) — and IEEE-754 subtraction, negation, and halving all commute with sign,
so the two results are the same bit pattern whenever a ≠ b.

**The one bit-level caveat — signed zero (a real finding, bounded):** on an exactly
mirror-symmetric image, a = b, so χ(x) = +0.0 and χ(mirror(x)) = +0.0, while −χ(x) = −0.0.
Measured: χ(mirror) bits `0x0000000000000000` vs −χ bits `0x8000000000000000` — **equal as
values (+0.0 == −0.0), different as bit patterns.** Consequence for the design: any
downstream code that branches on the sign BIT of χ (copysign, signbit, bit-level
comparison) rather than on ordered comparison with τ could treat the two zeros differently.
Since acceptance is |χ| > τ with τ > 0, exact zeros abstain and the ambiguity is inert —
but the prereg should state "comparisons on values, never on sign bits" explicitly.

## Where the identity FAILS in practice — demonstrated, with cause

Replacing the index-reversal mirror with an interpolating reflection (affine transform,
reflection axis displaced 0.25 px from the grid centreline, bilinear interpolation) breaks
the identity by **|χ(mirror(x)) + χ(x)| between 0.058 and 0.944** on test spirals — order
1–20% of the χ scale, i.e. a sorter with only-approximate antisymmetry CAN manufacture a
small asymmetry. Cause: under resampling, mirror(mirror(x)) ≠ x, so the two sides no longer
share their w evaluations. Design consequence (constrains §4 pixel-path custody): **the
mirror used in χ must be pure index reversal on the pixel grid — never a resampling
operation — and the pipeline must verify mirror∘mirror ≡ identity byte-exactly.**

## A second practical finding — the identity survives even a broken w

The first w implementation had a real bug: a naive (−π, π] circular unwrap under the
two-armed (period-π) profile mapped every +π inter-arm jump to −π, systematically
inverting the recovered winding sign (100% sign inversion on accepted spirals). **Even with
that pathological w, the identity held bit-exactly 1000/1000** — a concrete demonstration
of "for ANY w". The bug cost accuracy, never antisymmetry — precisely the brief's
sensitivity-not-validity claim. The fix (arm-agnostic mod-π unwrap) is documented in the
code; the broken-version numbers are preserved in this receipt's history paragraph.

## τ calibration and abstention (synthetics only; τ never touches sky data)

τ = **4.198** — 99.5th percentile of |χ| over 240 armless-disk nulls (inclination 0–60°,
S/N 2–50). On the 1,000-spiral grid, acceptance |χ| > τ gives:

| peak S/N | abstention | sign accuracy of accepted |
|---|---|---|
| 2 | 93.5% | 69.2% |
| 5 | 94.5% | 100% |
| 10 | 92.0% | 100% |
| 25 | 90.5% | 100% |
| 50 | 90.5% | 100% |

Overall: abstention 92.2%, accepted-sign accuracy 94.9%. Read honestly: the crude argmax
tracer is noisy on nulls, which inflates τ and buys the high abstention — the identity
guarantees this costs sensitivity, not validity. A better (still deterministic) w — peak
prominence weighting, multi-arm consensus — would lower τ and abstention; that is a
sensitivity tuning question for the prereg, not a validity question.

**dA_raw** (brief §3: the raw estimator's own flip-imbalance, the analogue of GZ1's
dA_paired = 0.095): mean(sign(w(x)) + sign(w(mirror(x))))/2 over all 1,000 spirals =
**0.0 exactly** for the fixed estimator on this synthetic set.

## Files (all under `spike/`, absolute paths in code)

- `yui_identity/w_chi.py` — implementation (sha256 below)
- `yui_identity/run_identity_test.py` — runner
- `yui_identity/results.json` — full machine-readable results incl. per-image records

## Boundary reached — stopping

The next natural step is running w(x) on real galaxy cutouts. **Stopped at that line, as
ordered.** An empirical run stays BLOCKED until a separate preregistration artifact freezes
every open value (w's exact algorithm, τ, the mirror definition, sample cuts). This receipt
gives the freeze decision what it needs: the identity is architecturally sound bit-for-bit
under an index-reversal mirror; its two practical hazards (interpolating mirrors, sign-bit
branching on zeros) are named and controllable.

Nothing published, accepted, or committed.
