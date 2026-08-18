# D-ω — vorticity evolution ω(a) and the bound mapping (Track B step 3)

**Lana (science seat), 2026-08-19, under frozen `MODEL_SPEC.md` (PASS_MODELSPEC).** Scope label:
black-hole-universe cosmology is Duho's personal side-interest, not a NebulaMind research
programme. Receipts: `receipts/omega_evolution_receipt.py` (R6),
`receipts/bound_mapping_receipt.py` (R9). Pinned source: Malik & Wands, Phys. Rep. 475, 1
(2009), `sources/0809.4944.html` SHA-256 `2a9d652e…` (Goru item 1).

## 1. Governing equation, pinned

Verbatim from the source (§8.3, extracted from the saved full text tonight):

> "The divergence-free part of the 3-momentum […] **δq_i = (ρ+P)(v_vec i − S_i)** (8.61) obeys
> the momentum conservation equation **δq_i′ + 4ℋ δq_i = −∇²Π_i** (8.62)"
> "vector metric perturbations can be supported only by divergence-free momenta, but even then
> equation (8.62) shows that the vector perturbations are redshifted away by the Hubble
> expansion on large scales unless they are driven by an anisotropic stress."

**Gauge statement (explicit):** we adopt the vector gauge S_i = 0, so δq_i = (ρ+P)v_i with v_i
the transverse velocity perturbation; in Malik–Wands conformal coordinates v_i is the physical
peculiar velocity. Spec A7 sets Π_i = 0 (no anisotropic stress — the generous direction: stress
would decohere, not amplify).

## 2. Derivation of ω(a) per era

With Π_i = 0, (8.62) integrates to **δq_i ∝ a⁻⁴** — solved symbolically in R6 (sympy dsolve:
δq = C₁/a⁴). Then v = δq/(ρ+P), and the angular velocity of a fluid patch about a comoving axis
at comoving radius x is ω = v/(a x):

| Era | ρ+P | v ∝ | **ω ∝** | Receipt |
|---|---|---|---|---|
| Radiation (P = ρ/3) | ∝ a⁻⁴ | a⁰ | **a⁻¹** (n_rad = 1) | R6 |
| Matter (P = 0) | ∝ a⁻³ | a⁻¹ | **a⁻²** (n_mat = 2) | R6 |
| Λ-dominated (rotating component is still the matter) | ∝ a⁻³ | a⁻¹ | **a⁻²** | R6 (same bookkeeping) |
| Torsion inflation | **not covered by any pinned source** | — | **a^(−n_inf), n_inf ∈ [1, 2] parameterized** per spec A6 | — |

Cross-check (R6): matter-era angular momentum of a comoving patch, L ∝ (ρa³)(ax)(v) ∝ const —
the a⁻² law is exactly angular-momentum conservation, consistent with Track A's audit device
(receipt R5) and with the source paper's own qualitative claim (its T 214).

**Inflation-era honesty (spec A6):** whether the bounced fermion fluid is radiation-like
(n_inf = 1) or matter-like (n_inf = 2) during torsion inflation is not determined by any pinned
source; Goru's sweep (items 1–2) found none covering vorticity through an ECSK bounce phase.
n_inf stays a named parameter and enters only the inversion (D-C §3), not the confrontation.

## 3. Mapping the present-day bounds to the spin-acquisition epoch

Through matter+Λ domination, ω ∝ a⁻² = ω₀(1+z)², and H(z) = H₀E(z), E(z) =
√(Ω_m(1+z)³ + Ω_Λ) (flat; Ω_m = 0.315, Phase 0 pin S3). Hence

  **(ω/H)(z) = (ω/H)₀ · (1+z)²/E(z)**,  → (ω/H)₀ (1+z)^{1/2}/√Ω_m for z ≫ 1.

The bounds map forward-in-redshift as *growing*: the allowed vorticity at spin acquisition is
larger than today's bound by only a factor of a few — the mapping is mild, and this is the
reason the strict confrontation cannot be rescued by epoch choice.

**z_ta — the epoch, stated and sourced.** The epoch at which the comparison is made is
turnaround, pinned to the Schäfer review (`sources/0808.0203.html`, SHA-256 `b84bc0c5…`,
Goru item 2), verbatim:

> "Tidal torquing is effective until the moment of turn-around in the spherical collapse
> picture, because the collapse dramatically reduces the lever arms. After the collapse, the
> halo conserves the angular momentum it has accumulated until turn-around."

The *numerical* z_ta is halo-mass dependent and is NOT pinned to a single value — per the
kickoff, the mapping is given as a range (R9), fiducial z_ta = 3 for a galaxy-scale halo,
swept over z_ta ∈ [0.5, 10]:

| z_ta | (ω/H) at S2 bound | at S1 bound |
|---|---|---|
| 0.5 | 1.29×10⁻⁹ | 8.0×10⁻¹¹ |
| 1 | 1.70×10⁻⁹ | 1.05×10⁻¹⁰ |
| 2 | 2.26×10⁻⁹ | 1.39×10⁻¹⁰ |
| **3** | **2.66×10⁻⁹** | **1.65×10⁻¹⁰** |
| 5 | 3.30×10⁻⁹ | 2.04×10⁻¹⁰ |
| 10 | 4.49×10⁻⁹ | 2.77×10⁻¹⁰ |

(R9; S2 = Planck Bianchi VII_h 7.6×10⁻¹⁰, S1 = Saadeh 4.7×10⁻¹¹, Phase 0 pins.) Across the
full sweep the allowed (ω/H)(z_ta) varies by ×3.5 — z_ta is not a lever that changes any
conclusion.

**Assumption flagged for the error budget (D-C §4):** mapping the *bound* back with our ω ∝ a⁻²
assumes the bound's underlying analyses evolve vorticity compatibly (Bianchi VII_h internal
evolution is model-specific). The factor-few uncertainty this could introduce is absorbed in the
final error budget and cannot bridge a 5.7-order gap.

## 4. Chain summary (feeds D-T and D-C)

ω(z_ta) = ω₀(1+z_ta)²; ω₀ = ε·Ω_H·f_b·[Z_inf^{n_inf} Z_rad Z_mat²]⁻¹ (spec §2 frozen form with
tonight's derived n_rad = 1, n_mat = 2). Forward confrontation uses only the bound-allowed
ω(z_ta) (no bounce parameters needed); the inversion (D-C §3) uses the full chain.

— Lana, D-ω, 2026-08-19. Gate: `KUN_P1_OMEGA_GATE.md` expected.
