# S2b receipt — the opaque branch excludes too. The knife edge cuts both ways.
(2026-08-25, stamped from mtime at commit. s2b_photosphere.py, log _tmp_s2b_run.txt, 5/5
limiting cases. Run on Duho's instruction to carry BOTH branches through S2, since S0's
τ ≈ 0.3 sits on the knife edge rather than cleanly in either.)

## How the absolute-temperature problem was avoided

The brief parked the cap's ABSOLUTE brightness behind K4 because the metric fixes the
exterior's energy density but not its temperature. The CONTRAST against the surrounding sky,
however, is anchor-free: if the exterior's energy is carried by radiation, both sides'
temperatures follow from their own densities, so **T̄/T_FRW = v^(1/4)** with v = ρ̄/ρ gated
from A1. No absolute temperature is needed, and K4 is not breached.

## Result — radiation sub-case

- v = 0.42997 at the crossing → **T̄/T_FRW = 0.8098**: the exterior is 19% cooler.
- Partial opacity (τ = 0.34) mixes exterior emission with whatever lies beyond. That unknown
  is BOUNDED — the beyond-term is between nothing and the same bath — so
  **T_eff/T_FRW ∈ [0.593, 0.810]** without knowing it.
- With S1's Doppler factor applied, the contrast against the surrounding sky runs from
  **−61% to +23%** depending on viewing angle: worst |contrast| = **0.608**, which is
  **6.1 × 10⁴ times** the observed CMB anisotropy.

## Result — ideal-gas sub-case

If instead the exterior is a non-relativistic ideal gas, kT̄ = (u/v)·μ·m_H c² = **138 MeV**
(1.6 × 10¹² K) — excluded by many further orders. Both sub-cases point the same way.

## The structural finding

**Transparent and opaque both exclude.** S2's kinematic branch gives an anisotropy span of
2.593 × (offset fraction); S2b's emitting branch gives an order-0.6 contrast. The knife-edge
τ ≈ 0.3 does not rescue the model — it lands between two branches that both fail against the
observed sky by four to five orders of magnitude. This is the robustness the "carry both"
instruction was for: the conclusion no longer depends on which side of τ = 1 the exterior sits.

## Limits

σ = 1/3, pre-horizon, photon channel; the radiation sub-case assumes the exterior's energy is
radiation-carried (stated, not derived — the metric fixes ρ̄, not its composition); the
Doppler sign convention caveat from S2 carries over; and the monopole remains excluded from
every contrast quoted.
