# A3 receipt — the three observables, and what the strict model actually predicts
(2026-08-24 ~09:45 KST, Tori. Script `a3_observables.py`, output `a3_window.csv`, 4/4 checks.)

## The analytic backbone (derived by hand, verified against the A2 solver to 1e-6)

In the exact FRW interior, 1+z = η_obs/η_e. The center-crossing condition collapses to
**z_c(center) = √N(η_e)** — the boundary's redshift equals its distance in Hubble lengths at
emission. For the nearest direction with offset x:
**x_max(z; t_obs) = η_obs[(1+√N(η_e))/(1+z) − 1]**, η_e = η_obs/(1+z).

## Observable (b) — expansion-rate anisotropy: exactly NULL. The brief's claim partially falls.

By A0 the interior is exact FRW, so the redshift–distance relation for any source whose photons
stay inside is standard and isotropic AT ANY OFFSET. **The strict model predicts NO H₀ dipole,
no expansion anisotropy, for interior sources — not small: zero.** The brief's motivating claim
("the geometry generically implies … an anisotropy in the locally inferred expansion rate") is
REFUTED by the exact solution for this observable. Consequence for Track B: the H₀-anisotropy
bounds (agy's harvest) CANNOT constrain this model; that limb of the confrontation closes as
NOT-A-DISCRIMINANT. This is the kind of result the strict-model discipline exists to force.

## Observable (c) — non-kinematic dipole: not predicted.

For interior signals the model adds nothing beyond the FRW-free peculiar-velocity dipole. A
structured dipole could arise only on boundary-crossed lines of sight, whose appearance depends
on unmodeled TOV-side optics. NOT CALIBRATED; recorded as such.

## Observable (a) — CMB / sky isotropy: the surviving discriminant, now quantified.

The observed sky is uniform (to the known anomalies) out to z_ls ≈ 1100, which in-model
requires the last-scattering sphere to lie inside the shock in every direction: z_c(μ) > z_ls
for all μ — or an unmodeled TOV-side conspiracy that mimics FRW (non-generic; recorded as the
only escape). Three regimes in t_obs (units of t_crit; σ = 1/3 model):

1. **t_obs < t_vis = 0.27644**: the shock has never entered the past light cone. The sky is
   pure FRW, perfectly isotropic, ANY offset allowed. The model is CONSISTENT AND UNTESTABLE
   by this observable — the boundary is hidden with no future-visible signature (K2-flavored).
2. **t_vis ≤ t_obs ≤ t_1100 = 0.27744**: the marginal band — the boundary is inside the past
   cone but beyond last scattering. Fractional width **W = (t_1100−t_vis)/(t_crit−t_vis) =
   1.39×10⁻³**. Within it the offset is bounded: x_max/r_* runs from **1.1×10⁻³** at the
   band's bottom to 0 at its top (table in a3_window.csv). Both tunings are ~10⁻³.
3. **t_obs > t_1100**: the boundary crosses inside z_ls somewhere on the sky; a generic
   TOV side produces order-unity sky differences (A2's z_c tables). EXCLUDED by observed
   isotropy, absent the conspiracy.

**The calibrated statement Track C inherits:** the observable-scale version of this branch —
boundary inside the past light cone — survives only in a temporal band of width ~1.4×10⁻³ with
offset ≤ 10⁻³ of the boundary radius; otherwise it is either excluded (visible regime) or
strictly untestable (hidden regime). The only in-model reading that PREDICTS something visible
is the marginal band, whose signature would live at the largest angular scales — whether the
observed low-ℓ anomalies can be read as that signature is Track C's question, on gpt2's frozen
CMB bounds, and nothing here presumes the answer.

## Caveats that transfer verbatim

- σ = 1/3 throughout (radiation): all specific numbers (t_vis, W, x_max) are internal to that
  model. S1: these are "only rough qualitative models." The STRUCTURE (hidden / marginal /
  excluded trichotomy, z_c = √N law) is the robust content; the digits are not.
- The TOV-side optics are not modeled by the source papers; every statement above about the
  visible regime assumes only that a generic TOV side differs observably from FRW.
