# P2 Track B step 2 — parent-to-interior inheritance: what ECSK actually determines

**claude-seat (science seat), 2026-08-19, under `PHASE2_BRIEF.md` Track B(2).** Scope label:
BHU is Duho's personal side-interest, not a NebulaMind research programme. External-theorist
review required before any publication claim. Gates honored: `MIRU_P2_STAGE1_GATE.md`
conditions 1–5 and `MIRU_P2_BOUNCE_GATE.md` flags 1–4 (each cited where it bites). Sources:
pinned copies under `sources/` and this lane's gated documents only; Goru sections 1/2/4
remain excluded; **zero new fetches**; portal.nersc.gov untouched.

**Receipts (fresh, prefix p2b2, outputs alongside):** `p2b2_mass_channel.py` (B2-R1),
`p2b2_spin_channel.py` (B2-R2), `p2b2_shear_frozen.py` (B2-R3).

## 0. Result, up front

The published chain determines **exactly one inheritance channel — mass — and this step
derives it through both bounce treatments.** For the parent-spin channel there is no
published equation (both audits + Gate 1 adjudication); what ECSK first principles *do*
yield, derived here, are three original results: **(i)** the parent's macroscopic J has **no
torsion channel at all** (torsion couples to intrinsic spin only), so spin inheritance is a
GR vorticity-transport problem the chain never solves; **(ii)** a **self-consistency ceiling**
on Phase 1's inheritance parameter: the homogeneous bounce can occur only if the interior
sheds all but **ε ≤ ~10⁻²⁷–10⁻²⁶** of the parent's angular momentum (10 M☉, a★ = 0.7;
treatment-bracketed; ∝ M^(−2/3), so supermassive parents are *more* constrained, down to
~10⁻³²); **(iii)** a **frozen-ratio theorem for shear**: the shear and torsion terms both
scale a⁻⁶, so the bounce itself performs no isotropization — axis/anisotropy memory is
neither erased nor transmitted by any derived mechanism, leaving shear survival UNDETERMINED
exactly as the published chain's heuristic left it. Everything else stays parameterized and
is named as such (§4 table). No transfer function is manufactured.

## 1. The M channel — derived through both treatments (requirement 1)

**The map, re-derived from its two defining relations** (B2-R1; source: A2 rows B-8/B-9,
gate-certified; Paper B = `sources/1410.3881`): from the closed-FLRW turnaround condition
(κ/3)ε₀ = 1/a₀² and the patch-mass relation Mc² = (4π/3)r₀³ε₀ with r₀ = a₀ sinR₀:

  **a₀ = (r₀³/r_g)^½, sinR₀ = (r_g/r₀)^½, T₀ = [3Mc²/(4πh★r₀³)]^¼**, r_g = 2GM/c² —

all three reproduced symbolically (B2-R1: True/True + closed form). Inputs: M **and** the
collapse-onset radius r₀ (a second initial datum — M alone does not fix the map; stated
plainly).

**What follows from M alone, treatment by treatment:**
- The **bounce state is M-independent in both treatments** — Treatment I: T_max = 1.152×10³²
  K (A2-certified, gate-confirmed); Treatment II: T_cr = 0.785 m_P (B1-receipted). Both are
  functions of (g★, g_n, κ) only. Bounce densities: ε_b = 7.1×10¹¹⁴ (I) / 9.8×10¹¹¹ (II)
  J/m³ (B2-R2) — the treatments disagree on the bounce state by ~×730 in density (Gate-flag 1
  honored: treatment named per quantity).
- M enters the interior initial data **only through size**: a₀T₀ ∝ χ^(3/4) M^(1/2) at fixed
  compactness χ = r₀/r_g (derived, B2-R1) — bigger parents make bigger baby universes, with
  the comoving invariant aT set at formation.
- The chain's own numerics (A2 row A-18, audited) say even this washes out of the interior
  *dynamics*: cycle behavior depends on the production coefficient β, not a_i. So from M
  alone: existence, size, and cycle count — **no observable fingerprint beyond those**.

## 2. The a★ channel — first principles, honestly bounded (requirement 2)

**No published equation exists** (A1 §3 item 3; A2 focus 2.3: "no parent-spin variable, no
Kerr collapse, no angular-momentum transport"; Gate 1 conflict adjudication excluded the
unattributed HRDCC claim). What ECSK mechanics itself says, derived here:

**2.1 The structural fact: no torsion channel for J.** Torsion is sourced by the *intrinsic*
spin tensor of fermions (pinned: PLB main.tex 88–98 — Dirac fields couple minimally to
torsion; the Cartan equation's source is s_ijk), **not** by orbital angular momentum. The
parent's J is orbital. Therefore the celebrated ECSK ingredient — torsion — is a spectator
to spin inheritance: J enters the interior as ordinary fluid vorticity in the metric sector,
exactly as in GR, and the inheritance question reduces to GR vorticity transport through a
bounce — precisely what the published chain never computes. (This is why Phase 1's
parameterization cannot be superseded from these papers: the mechanism that would supersede
it is absent by structure, not by omission.)

**2.2 The self-consistency ceiling (derived, order-of-magnitude, assumptions named).** The
published bounce solutions (both treatments) assume a homogeneous, non-rotating interior.
For that solution to apply at the bounce, rotation at the bounce patch must be
sub-relativistic: v_rot = J_b/(ξMR_b) < c, with R_b = (3M/4πρ_b)^(1/3) the patch radius at
the treatment's bounce density and ξ the inertia prefactor (ξ = 2/5 uniform sphere; bracket
0.2–0.5; rigid rotation assumed — all named). If instead the parent's full
J = a★GM²/c were conserved to the bounce, the implied rotation rate exceeds the causal limit
c/R_b by **6.6×10²⁶** (10 M☉, a★ = 0.7, Treatment I; B2-R2) — the homogeneous collapse
cannot carry the parent's spin. Hence the ceiling:

  **ε ≡ J_b/J_parent ≤ ξMcR_b/(a★GM²/c) = ξc²R_b/(a★GM)**  (B2-R2):

| parent | Treatment I | Treatment II |
|---|---|---|
| 10 M☉, a★ = 0.7 | **1.5×10⁻²⁷** | **1.4×10⁻²⁶** |
| 10⁹ M☉, a★ = 0.7 | 7.0×10⁻³³ | 6.3×10⁻³² |

with the exact scaling ε_max ∝ M^(−2/3) verified (B2-R2: ratio 4.642×10⁻⁶ = (10⁸)^(−2/3)).
**Two readings, both stated:** (Reading 1) if the published homogeneous bounce is demanded,
Phase 1's ε is bounded above by ~10⁻²⁷–10⁻²⁶ (stellar) — the first quantitative constraint
on that parameter from the chain's own mechanics; (Reading 2) more conservatively, a rotating
parent simply never reaches the homogeneous ECSK bounce, and what actually happens is
UNDERIVED — the published chain's one sentence on rotating collapse (A2 row B-17) is
unsupported. Either way, **near-total shedding is required and no mechanism for it is
derived anywhere in the chain.** This is a ceiling, not a transfer function; the value of ε
below the ceiling remains STILL-PARAMETERIZED (MODEL_SPEC row A4).

**2.3 The torsion-visible sliver (polarization), estimated and dismissed.** The only way
parent rotation could reach the *torsion* sector is by polarizing fermion spins (a nonzero
⟨s_ij⟩, reactivating the term both papers drop). Rotational polarization is of order
ħΩ/k_BT; even at the maximal sub-relativistic rotation Ω = c/R_b it is **≤ 5×10⁻¹³ (I) /
3×10⁻¹² (II)** at the bounce (B2-R2) — negligible. The torsion sector stays effectively
unpolarized; assumption A7-adjacent physics unchanged.

**2.4 Axis direction.** A ceiling on magnitude says nothing against direction: whatever
angular momentum survives (ε ≤ ε_max) still defines n̂. Phase 1's A3 (direction survives; by
symmetry, uncomputed) is neither derived nor refuted here — see §3.

## 3. Shear and axis memory (requirement 3): the frozen-ratio theorem

Published state: torsion + particle production "defeats" shear — heuristic (A2 row B-13);
later cycles "isotropize" — assertion. Derived here (B2-R3, sympy): in the effective
Friedmann equation the shear term (+Σ²a⁻⁶) and the spin-fluid torsion term (−(κ²C/12)n₀²a⁻⁶,
using the B1-derived n ∝ a⁻³) scale **identically**. Therefore:
1. **the shear/torsion ratio is frozen** — a-independent through collapse and bounce;
2. **a bounce exists at all only if shear is already subdominant** (Σ² < κ²Cn₀²/12 — derived
   as the positivity condition of the bounce root);
3. **the bounce mechanism itself performs zero isotropization** — any erasure must come from
   particle production, which is exactly the heuristic, underived step (B-13).

**Verdict: shear survival UNDETERMINED** — the derived result cuts *against* the chain's
"isotropization at the bounce" language (the bounce can't do it) but derives no bound on what
production does. **Axis-memory consequence:** no derived erasure and no derived survival;
any axis-memory claim in this chain rests entirely on the underived production step.
Phase 1's A3 stays a named assumption with this sharper statement attached. (V2 note: the
torsion side of the frozen ratio inherits the n²-averaging assumption and its ×6 coherence
bracket; the *theorem* — equal scaling — is bracket-independent since both edges scale a⁻⁶.)

## 4. Cross-reference table against Phase 1 `MODEL_SPEC.md` (requirement 5)

| Spec row | Content | Status after this step |
|---|---|---|
| A0 | parent Q = 0 | NOT-APPLICABLE (unchanged) |
| A1 | closed FRW patch forms | STILL-ASSERTED — Paper B's exact interior is a cap (sinR₀ = √(r_g/r₀), derived B2-R1); its closure to a full 3-sphere is the audited B-14 ERROR; not derivable from the pinned chain |
| A2 | no post-bounce net-J accretion | NOT-APPLICABLE here (unchanged convenience assumption) |
| A3 | axis direction survives bounce | STILL-PARAMETERIZED — sharpened by §3: the bounce itself neither erases nor transmits anisotropy (frozen ratio, B2-R3); everything rides on underived production |
| A4 | J-inheritance amplitude → ε ∈ [0,1] | **STILL-PARAMETERIZED, NOW BOUNDED**: ε ∈ [0, ε_max] with ε_max = ξc²R_b/(a★GM) ≈ 10⁻²⁷–10⁻²⁶ (stellar) / 10⁻³³–10⁻³² (supermassive), derived (B2-R2), conditional on Reading 1 (§2.2); value within the range underived |
| A5 | ω_ref anchored to Ω_H; f_b | STILL-PARAMETERIZED — the anchor stands; §2.2's ceiling gives f_b·ε a physical roof; no transfer derived |
| A6 | Z_inf·Z_rad·Z_mat history | PARTIALLY-DERIVED-ELSEWHERE — bounce states now treatment-explicit (B1); the β-window for finite inflation is A2-certified (exact); Z_inf's value stays [ECSK]-parameterized |
| A7 | passive vorticity evolution | UNCHANGED — reinforced by §2.3: the torsion sector cannot torque the fluid (polarization ≤ 10⁻¹²) |
| A8 | flatness compatibility | SUPPORTED (consistency-only) — A2-certified Ω̃ results |
| A9 | ΛCDM + vorticity structure formation | NOT-APPLICABLE here (downstream of this step) |

**Net:** one Phase 1 parameter gained a derived ceiling (A4); none was eliminated. The honest
summary the brief asked for: **ECSK mechanics, as published, cannot derive the inheritance —
it can only forbid most of it.**

## 5. Validity limits (requirement 4 — all quantities above)

- **V1 (Planck regime):** every bounce-state quantity used (ε_b, R_b, T_max, T_cr) sits at or
  near the Planck scale under classical equations (Gate-flag 2: the incoherent edges are the
  better-motivated ones and make this worse; carried, not dropped). The ε_max ceiling
  inherits V1 through R_b — its order of magnitude, not its exact coefficient, is the claim.
- **V2 (n² averaging):** enters ε_b via h★-normalization? No — ε_b is thermal (γ + ν +
  fermions), not spin-squared; V2 enters only the *torsion side* of §3's frozen ratio and the
  bounce existence itself (B1). Marked there; the ×6 coherence bracket shifts ε_b^(I,II)
  thresholds but not the frozen-ratio theorem or the ε_max scaling (R_b ∝ ρ_b^(−1/3): a ×6
  density shift moves ε_max by 6^(1/3) ≈ 1.8 — inside the treatment bracket already shown).
- **V3 (Treatment II cusp):** any inheritance statement using Treatment II's bounce state
  inherits the cusp-prescription caveat (Gate-flag 3).
- **V5 (erratum):** metadata-only, unchanged; no quantity here descends from the quarantined
  printed numbers (all bounce states from certified/receipted values).

## 6. Handoff to Track B step 3 (confrontation)

Derived observables to confront: **none new with finite amplitude.** The M channel yields
consistency-class quantities only (size, cycle count — no sky statistic); the a★ channel
yields a *ceiling* (ε ≤ 10⁻²⁷–10⁻²⁶ stellar), which combined with Phase 1's chain
(ω_i = ε·Ω_H·f_b, then D > 10³⁰ dilution already required by the CMB) makes the rotating-
parent signal budget strictly smaller than Phase 1 assumed — the confrontation step should
quantify how much smaller and state whether any finite-amplitude signature survives (the
brief's honest headline). Shear/axis memory enters confrontation only through the underived
production step and must be carried as UNDETERMINED, not as a signal.

— claude-seat, Track B step 2, 2026-08-19. Receipts p2b2_* all run clean this session.
Gate: `MIRU_P2_INHERIT_GATE.md` expected next. Zero fetches; portal.nersc.gov untouched.
