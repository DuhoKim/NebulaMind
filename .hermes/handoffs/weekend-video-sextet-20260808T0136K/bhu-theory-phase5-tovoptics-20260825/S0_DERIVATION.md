# S0 derivation — optical depth of the TOV exterior (2026-08-25, Tori)

Labels per the brief: **PINNED** = traceable to pinned source text; **DERIVED** = no published
source, ours, checkable only by limiting cases and blind double.

## Inputs

- **PINNED** (astro-ph/0210105 eqs. 5.2–5.3, σ constant): ρ = 4/(3κ(1+σ)²) · 1/t².
- **DERIVED** (algebra on the above, κ = 8πG, σ = 1/3): ρ(t) = 3/(32πG t²) — the standard
  radiation-era FRW density. This is limiting-case test LC1: the pinned formula must reproduce
  the textbook result, and it does exactly.
- **PINNED** (same source, §4): at the shock, u = p̄/ρ and v = ρ̄/ρ; the A1 solution tabulates
  both over ten decades of S (a1_results.csv, gated PASS, blind-double-confirmed).
- **PINNED** (same source, §6 and A1's verified identity): r̄ = 2 c t √N, with √N the shock
  distance in Hubble lengths.
- **PINNED** (Phase 4 A2/A3, gated): our past light cone DOES reach the shock — the crossing
  redshift is z_c(center) = √N(η_e). Causal access is therefore not in question at S0; only
  opacity is.

## The quantity

**DERIVED.** Thomson opacity of fully ionized hydrogen κ_T = σ_T/m_p (declared assumption:
the exterior is ionized ordinary matter — the equations fix its equation of state, not its
composition, so this is a stated modelling choice, flagged under K3). Optical depth over the
one length scale the crossing supplies, the shock's areal radius:

  τ_R = κ_T · ρ̄ · r̄ = κ_T · v(q) · [3/(32πG t²)] · 2 c t √N
      = (3 κ_T c / 16πG) · v(q) √N / t

**The anchor dependence falls out exactly: τ_R ∝ 1/t.** Since the A1 table is in units of
t_crit, τ_R ∝ 1/t_crit — the model's single free scale. That is the function S0 was briefed to
produce, rather than one order-of-magnitude number.

## Limiting-case tests (mandatory, no source to audit against)

- LC1: ρ(t) reduces to the textbook radiation-era 3/(32πG t²). [algebraic, exact]
- LC2: v → 0 as S → 1 (the TOV side goes dust-like at horizon crossing), so τ_R → 0 there —
  the transparency limit must appear on its own from the gated A1 solution, not by hand.
- LC3: τ_R must scale exactly as 1/t_crit under a change of anchor (numerical check).
- LC4: dimensional closure — cm²/g × g/cm³ × cm = dimensionless.
