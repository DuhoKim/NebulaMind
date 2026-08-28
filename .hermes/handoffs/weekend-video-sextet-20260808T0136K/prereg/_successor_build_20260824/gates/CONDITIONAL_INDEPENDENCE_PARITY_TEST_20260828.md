# Conditional independence, attacked directly: a label-free parity test on the quality cut

**Duho's instruction, relayed 2026-08-28: attack conditional independence rather than carry it as a
stated assumption.** This is the first attack. It does not close the question; it bounds one part of
it with a computation instead of an argument.

## The circularity, and the way past it

Blanc: *"the direct test — at fixed cos θ, does the pass rate differ between the two chiralities —
needs the labels, and the labels are exactly what is sealed."* Correct, and unavoidable **for that
test**.

But the estimator does not need chirality itself. It needs to know whether the cut is **parity-odd**.
And there is a parity-odd quantity already measured by the survey, already on disk, under no seal:

**`shape_e2`.** Under the mirror operation that flips handedness, **`e1` is invariant and `e2` changes
sign** — the same fact that made the selection ADQL use `e1² + e2²` rather than `e2` alone.

So: **if the quality cut is parity-even, `⟨e2⟩` must not shift between retained and excluded objects
at fixed position.** `e1` is the built-in null control — a generic selection effect moves both, a
parity-odd one moves only `e2`. No labels, no images, no seal touched.

## Result — 8 equal-count `cos θ` bins, 49,211 retained vs 15,849 excluded

    parity-odd  (e2):  max|z| = 1.80    χ² = 7.5  on 7 dof    (p ≈ 0.38)
    null control(e1):  max|z| = 1.36    χ² = 4.3  on 7 dof    (p ≈ 0.74)

**No parity-odd selection detected, and the null control behaves the same** — which is what makes the
null readable rather than merely quiet.

## The bound, established by injection rather than asserted

A test that has not shown it can fire proves nothing. Injecting a synthetic parity-odd selection —
dropping a fraction `f` of objects with `e2 > 0` — 20 trials per point, χ² critical 14.07:

    f = 0.00%    median χ²  7.5    detected  0%      ← the real cut sits here, χ² = 7.5
    f = 0.25%    median χ²  7.2    detected  0%
    f = 0.50%    median χ²  8.5    detected  0%
    f = 0.75%    median χ² 11.9    detected 45%
    f = 1.00%    median χ² 32.8    detected 100%

**The test reliably detects a 1% parity-odd differential removal and is blind below ~0.5%.** So the
result is: **any parity-odd component of this cut is below roughly 0.5–0.75% differential removal.**

For scale, the signal being tested is a **4%** amplitude. A sub-0.75% parity-odd selection is not
negligible against that, but it is bounded and quantified rather than assumed away.

## What this does NOT establish — stated, not buried

1. **`e2` is a proxy for parity-oddness, not chirality.** A cut could in principle be chirality-odd
   while leaving `⟨e2⟩` unmoved. This is a **necessary-condition test**: it can refute parity-evenness,
   not prove it.
2. **It tests the SELECTION, not the classifier.** A classifier that prefers one chirality is a
   different systematic, untouched here. Blanc's mirror-reclassification route addresses that one and
   needs images, which are blocked.
3. **It does not license the cut.** V29 §2.7 line 378 still records conditional independence as **not
   established**, and this bound does not change that wording. It narrows the space in which a
   violation could hide.

## The caution Blanc gave, honoured

*"The fix cannot be another positional cut."* Nothing here proposes one. The test is diagnostic only,
adds no selection, and changes no frozen quantity.

## Suggested next, in order of value

1. **Blanc's route 2 — the excluded population.** The 15,849 removed rows never enter the estimator,
   so examining their chirality distribution may be permissible without breaking the seal on the
   retained 49,211. **That is a gate question, not mine to decide.** If permitted, it converts this
   proxy test into a direct one.
2. **Blanc's route 3 — null axes.** Cheap, label-free, runnable now: the same slope along axes where
   no signal is expected. Selection-induced structure should appear there too; a real dipole should
   not.
3. **Blanc's route 1 — the mirror test.** Strongest for classifier bias, but needs images. Galaxy Zoo
   published mirrored-subset results; a literature amplitude may substitute for a commissioned
   measurement.
