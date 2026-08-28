# The sensitivity-gradient control — design, with the propagation kernel computed

**Principal's authorisation, 2026-08-28:** *"unrelated cutouts are fine, build the gain control."*
This authorises instrument characterisation on **non-sample** DR10 cutouts. **It does not authorise
any fetch of this study's footprint. BS-6 and the first image byte remain blocked**, and every cutout
used here must be provably outside the 49,211-object mask or it is a study fetch by another name.

## Why this is not the antisymmetry receipt

The instruction that produced this design was *"stratify the receipt in cos θ."* **That is not
constructible, and the reason is arithmetic rather than judgement.** From
`paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md` §2.1:

    mirror(·) = pure index reversal on the analysis raster (np.fliplr; no resampling)
    χ(x)      = (w(x) − w(mirror(x))) / 2

so `χ(mirror(x)) = −χ(x)` **algebraically, for any weights `w` and any input raster** — both sides
reduce to the same two floating-point values. §2 records the receipt: `max|χ(mirror(x)) + χ(x)| =
0.0` exactly, 1000/1000 synthetic spirals.

Therefore `d(g) = χ(g) + χ(Mg) ≡ 0`. **Stratifying it in cos θ returns 0.0 in every bin, at every
sample size, forever.** It cannot bound a gradient because it is not a measurement — it is an
identity. BS-3's `antisymmetry_receipt` verifies that identity holds in the implementation (and §3.1
requires a canary that substitutes a resampling mirror and asserts the identity *fails*). That is a
real check. It is not this one.

**This corrects `gates/MIRROR_TEST_DESIGN_20260828.md` Q2**, which proposed stratifying `⟨d⟩` in 8
`cos θ` bins. The stratification *principle* there was right; the *statistic* was identically zero.

## What actually threatens the estimator

The architecture removes the parity-even response entirely, so the Galaxy-Zoo class of bias — a
classifier that prefers one winding sense, uniformly or in poor seeing — **cannot occur**: acceptance
is handedness-blind (`|χ(mirror x)| = |χ(x)|`) and a biased `w` *"attenuates a real signal but cannot
create one."* §2.3 names what survives:

| route | bounded by this control? |
|---|---|
| (a) chirality introduced **upstream** of the analysis raster | **no** |
| (b) global offset × **sky gradient in sensitivity** | **yes — this is the target** |
| (c) sample selection by a non-equivariant process | **no** |

Sensitivity is a **gain**, not an offset. Gain is measurable, varies with image quality, and image
quality tracks the tested axis. That is the whole mechanism.

## The measured coupling — computed, not asserted

Using the **frozen** axis (`ref/successor_ref_v9.py:100`) and v9's own `cos_theta()`, on the real
sample:

| sample | N | `corr(psfsize_r, cos θ)` |
|---|---:|---:|
| parent, pre-cut | 65,060 | **+0.3659** |
| **retained, post-cut** | **49,211** | **+0.4188** |
| excluded | 15,849 | +0.0964 |

The pre-cut value reproduces the figure already carried in `ref/bs2a_quality_gate.py`, which confirms
the convention. **The new fact is the second row: today's catalogue-quality cut *raised* the
seeing–position coupling in the analysed sample, from +0.3659 to +0.4188.** The cut preferentially
removed objects whose seeing did not track position, leaving a remainder that is more coupled, not
less. **The systematic this control exists to bound got worse under the cut adopted today**, and that
should be stated wherever the cut is justified.

Hemisphere contrast of the tested axis, retained sample, in units of 1σ of `psfsize_r`:

    +cos θ  (n = 20,063):  +0.4800
    −cos θ  (n = 29,148):  −0.3304
    Δ = 0.8104 σ

## The propagation kernel `K`

Let `s` be `psfsize_r` normalised to zero mean and unit variance on the retained sample, and let the
instrument's fractional gain vary as `g/ḡ − 1 = β·s`. The induced fractional gain gradient along the
tested axis is the regression slope of `g/ḡ − 1` on `cos θ`:

    γ = β · K,      K ≡ Cov(s, cos θ) / Var(cos θ)

Computed on the retained sample with the frozen axis:

    K(psfsize_r)   = +0.483014
    K(flux_ivar_r) = −0.270181
    Var(cos θ)     =  0.751761        mean cos θ = −0.158388

**`K` needs no images.** It is catalogue metadata and frozen geometry, so the conversion from a
gain-versus-quality measurement to a gradient along the tested axis is fixed *before* any cutout is
fetched. Only `β` requires images.

## The statistic, frozen

1. **Injection.** Synthetic spirals of known handedness and known amplitude, injected into
   **non-sample** DR10 cutout backgrounds spanning the retained sample's range of `psfsize_r` and
   `flux_ivar_r`.
2. **Recovery.** Run the pinned instrument (`weights_sha256`, `τ`) on each injected cutout; recover
   amplitude `Â`. Gain `ĝ = Â / A_inj`.
3. **Fit.** Weighted least squares of `ĝ/ḡ − 1` on `s`, giving `β̂` and `σ_β`.
4. **Report** `β̂`, `σ_β`, per-bin `ĝ_b` and `n_b`, and the derived `γ̂ = β̂ · K`.

**Binning, frozen and non-tunable:** the headline is the **two-hemisphere contrast** of the tested
axis — the minimum that measures a gradient at all, and unchoosable after the fact. The **8
equal-count `cos θ` bins** already frozen for the parity test are reported alongside for shape only;
**the acceptance decision reads the hemisphere contrast, not the 8-bin fit**, so bin choice cannot be
revisited to change a verdict.

## What it bounds, stated as a bound

To first order the spurious dipole injected by this route is

    A_spurious ≈ |μ| · |γ| = |μ| · |β| · K

where `μ` is the global monopole in `χ`. **The control bounds `β`; it does not measure `μ`.** The
preregistered ceiling is `|μ|_max = 0.10` — generous, since it exceeds both Land's normalised
asymmetry (~0.07) and this lane's own GZ1 flip-imbalance statistic (~0.095), and since the
instrument's parity-even response is architecturally zero, leaving only genuine population asymmetry
or route (a).

**Acceptance rule (frozen):**

    |μ|_max · (|β̂| + 1.96·σ_β) · K  ≤  0.011

with `|μ|_max = 0.10` and `K = 0.483014`. The right-hand side is **Longo's own published 1σ on the
amplitude** — an external anchor, not a number chosen here. A systematic smaller than the published
uncertainty of the quantity under test cannot flip the verdict at the tested amplitude.

Equivalently, on the frozen constants: `|β̂| + 1.96·σ_β ≤ 0.2277`.

**Failure consequence (terminated branch, per §6.3 clause 10):** if the inequality fails, the run
emits `INCONCLUSIVE-BY-SENSITIVITY-GRADIENT` and **no dipole detection is reported**. There is no
retry, no rebinning, and no recalibration of `|μ|_max` after the measurement.

## Blindness

Every input is a synthetic injection of **known** amplitude into a **non-sample** cutout, plus
catalogue metadata. **No real `χ` enters the statistic**, so this runs pre-unblinding without
touching the sealed mask. This is a stronger blindness property than the mirror test's, which needed
a parity argument; here the real sky is simply absent.

## What this does NOT do

- **It does not close conditional independence.** Independence of the quality predicate from
  handedness given position remains the stated open limitation (§2.7). This bounds one route by
  which a violation could reach the estimator.
- **It does not bound routes (a) or (c)** — upstream chirality and non-equivariant selection.
- **It measures per position; it selects nothing.** No positional cut is introduced. Tightening
  selection on a position-correlated systematic is the shape that produced the leverage confusion,
  and it is deliberately not what this does.
- **`|μ|_max` is an assumption, not a measurement.** It is preregistered and falsifiable at
  unblinding; if the realised monopole exceeds it, the bound is void and must be recomputed with the
  measured value **before** any verdict is read.

## Open, for the gate

1. **`SLOT_SCHEMA` is frozen.** Whether this receipt lives as structure inside BS-3's
   `antisymmetry_receipt` or as a new field is a **gate matter, not an edit** — `successor_ref_v9.py`
   is not to be modified.
2. **Provenance of the non-sample cutouts** must be receipted: each must be shown outside the 49,211
   mask by exact key comparison, not by assertion.
3. `β` is unmeasured. Until it is, the control is **DESIGN, defined, UNFILLED**, and the
   preregistration must say so rather than crediting it with a bound it has not produced.
