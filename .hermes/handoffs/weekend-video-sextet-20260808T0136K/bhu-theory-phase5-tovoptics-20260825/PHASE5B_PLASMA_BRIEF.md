# Phase 5b brief — the exterior plasma model (scoping; needs its own go)
(2026-08-25, on Duho's decision to commission it after K4 fired.)

## 0. Why this brief exists

The S0–S2 gate (HOLD_S0_OPTICAL_DEPTH_AND_S2_EXCLUSION_UNDERIVED) established two things:

- **A geometry error, mine, and NOT an assumption problem:** r̄ is timelike inside the horizon,
  so it is not a spatial column length. The optical depth must be the invariant
  τ = ∫ σ_T n_e (−u·k) dλ along the actual null path. That is a derivation to be done
  correctly, not a modelling choice, and it belongs in this brief's stage P1.
- **A genuine K4 boundary:** n_e is not fixed by the matched stress-energy. At the crossing
  p̄/ρ̄ = 0.246, so the exterior is relativistic, not a cold proton fluid; the pinned matching
  fixes ρ̄ and p̄ and nothing about composition, baryon loading, pair content, or temperature.

## 1. The minimal assumption set — enumerated, and carried as RANGES not values

Each item is required, is NOT derivable from the pinned metric, and will be declared as an
assumption in every downstream statement:

| # | assumption | why needed | range to carry |
|---|---|---|---|
| A1 | baryon rest-mass fraction of ρ̄ | fixes n_baryon | 0 (pure radiation) → 1 (cold matter) |
| A2 | electrons per baryon | fixes n_e from n_baryon | 1 (ionized H) → 0.5 (helium-rich) |
| A3 | thermal pair content | adds e± scatterers when kT̄ ≳ m_e c² | none → full LTE pairs at T̄ |
| A4 | source function | the emission term in the transfer | LTE blackbody at T̄ → pure scattering |
| A5 | T̄ from the EOS | brightness; also A3 | radiation-carried (T̄/T = v^¼) → ideal-gas |

**Rule for this phase: no single choice is adopted.** Every deliverable is reported over the
assumption ranges, and the phase's finding is whatever survives ALL of them. If nothing
survives, that is the finding.

## 2. Stages

- **P1 — the invariant optical depth (derivation, not assumption).** Build the null geodesic
  through the junction with r̄ timelike, and compute τ = ∫σ_T n_e (−u·k) dλ. Deliverable: τ as
  a function of the anchor AND of the A1–A3 ranges.
- **P2 — the transfer integral.** Absorption plus emission along the path (the thing S2 was
  labelled but did not do): I_obs = I_bg e^{−τ} + ∫S e^{−τ'} dτ', with S from A4/A5.
- **P3 — pattern, monopole removal, multipoles.** Fix the Doppler orientation physically
  (gate objection 5), normalize after monopole removal (objection 4), project onto ℓ.
- **P4 — confrontation** against the gated freeze rows only (B2.2 intrinsic dipole binds; B2.1
  context only; B3 for ℓ≥2), reported per assumption range.

## 3. The question P4 must answer

**Is the exclusion assumption-robust?** S2b hinted that transparent and opaque branches both
exclude, which would make the plasma unknowns non-load-bearing. That hint is now withdrawn as
computed, but it is the hypothesis this phase exists to test properly. Outcomes:
- exclusion survives across A1–A5 → a real, assumption-robust result;
- exclusion holds only for some assumption ranges → report the ranges, claim nothing beyond;
- exclusion fails → the branch keeps its Phase 4 status and this phase says so.

## 4. Immediate fixes owed regardless of this brief's go (gate objections 5–7)

1. **Derive the relativistic Rankine–Hugoniot relation in-lane** rather than citing Landau &
   Lifshitz generically. The identity v₁v₂ = (p₂−p₁)/(e₂−e₁) follows from the Taub junction
   conditions and should be DERIVED here, removing the uncited-textbook dependency entirely.
2. **Replace S1's LC1 with a real no-jump test** — the current one passes on |β|<1 and tests
   nothing. The correct test: as the shock strength → 0, β_rel → 0.
3. **Fix the PINNED/DERIVED labels**: z_c = √N and the crossing geometry are Phase-4 DERIVED,
   not pinned; the "photon 4-momentum continuous ⇒ all the shift is fluid-velocity" step is an
   adapted optics claim and must be labelled DERIVED.

## 5. Verification regime

Unchanged from Phase 5 and reinforced: blind double PRIMARY on P1 and P2; limiting cases must
include recovery of Phase 4's optically-thin pure-geometry result; cross-engine gates per
stage; DERIVED/PINNED labels audited before each gate rather than after.

## 6. Sequence

Brief → Duho's go (freezes it, sha-pinned) → item-4 fixes → P1 → P2 → P3 → P4 → gates.
Ping Duho only at a stop condition or a decision only he can make.
