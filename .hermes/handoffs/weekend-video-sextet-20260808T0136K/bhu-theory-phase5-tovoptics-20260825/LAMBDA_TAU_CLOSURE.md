# Closing the λ-vs-τ gap — it was never a labelling mismatch
(2026-08-26. Measurement in this file's run log; scripts p6_path_transfer.py and the seat's
platoon/gpt1_blind_p6/.)

## The suspicion, and why it was wrong

I expected the residual ~20% between my dipole coefficient (0.506) and the seat's (0.627) to be
a definitional mismatch: their grey-opacity λ versus my equation-of-state-derived τ denoting
different physical quantities under the same name. It is not.

## What the measurement shows

Their dipole coefficient is **flat across eight orders of magnitude in λ** — 0.6272 at
λ = 10⁻⁴ to 0.6153 at λ = 10⁴, a 2% drift — while their crossing temperature swings from 0.08
to 1.51 over the same range. So in their treatment opacity is a **common factor** across
directions and divides out of the sky-mean normalisation, leaving the pure-Doppler dipole.

Measuring the same thing in mine, at x_off/r_* = 10⁻³ and the junction closure:

| μ | crossing η | τ_tot | emergent T/T_bg |
|---|---|---|---|
| −1.0 | 0.5624468 | 0.13280 | 0.312039 |
| 0.0 | 0.5633892 | 0.13214 | 0.311689 |
| +1.0 | 0.5643307 | 0.13148 | 0.311340 |

**The exterior is not a common factor.** Its fractional spread across directions is
**2.24×10⁻³**, against a Doppler modulation of ~8×10⁻⁴ — nearly three times larger. And it
runs the *opposite* way: the emergent factor falls with μ while D(μ) rises, so the two
partially cancel.

## The resolution

**The two computations differ in physics, not in naming.** Their λ-family holds the exterior's
structure fixed and varies only its opacity, so their dipole is the pure-Doppler value by
construction. Mine lets each direction cross at its own epoch and therefore see its own
exterior — different ρ̄, N, τ and profile — and that variation partially cancels the Doppler
dipole.

That is exactly the 20%: my 0.506 sits below the pure-Doppler 0.615 because the exterior's
direction-dependence subtracts from it. **Mine is the more complete treatment; theirs is the
cleaner control**, and the two now agree on why they differ.

## Consequence — a claim of theirs does NOT carry over

Their surface implies the bound is essentially opacity-independent (2.164e-3 to 2.206e-3
across 10⁸ in λ). That holds only when the exterior is held fixed. Once the exterior varies
with crossing epoch, the bound moves substantially with the closure — my 1.1e-3 to 8.3e-3 —
because two comparable effects compete and their balance depends on w. At w = 0.01 the
coefficient rises to 1.227, above the pure-Doppler value, so **the cancellation appears to
reverse sign somewhere in the range**; I have not characterised where, and I am not claiming a
trend.

## Status

- λ-vs-τ: **CLOSED** — no mismatch existed; the difference is the epoch-varying exterior.
- P6's numbers: still not confirmed, but the divergence from the double is now *explained*
  rather than outstanding, and the explanation favours the more complete treatment.
- Opacity-independence of the bound: **does not hold** in the epoch-varying treatment.
