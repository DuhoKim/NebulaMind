# Lana — Phase 0 physics scoping: can a calibrated BHU observable be derived?

**Lana (science seat), 2026-08-18 21:42 KST.** Per `PHASE0_BRIEF.md` (Hwao, authorized by Duho:
"go ahead with phase 0"). Scope label, restated: black-hole-universe cosmology is Duho's personal
side-interest, not a NebulaMind research programme. This file is order-of-magnitude scoping only;
no full derivation is performed. Verdicts are mine alone; Kun adjudicates at the gate and Goru's
prior-art sweep may override my novelty notes.

**Derivation packet custody.** `../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` verified
before use: computed SHA-256
`b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516` — matches the pin in the brief.
All references to "the packet" below are to that Rev 5 file.

**Method.** Every load-bearing number below was fetched today (2026-08-18) from an allowed host
(arXiv abstract pages) and is quoted verbatim in §1, or is a certified count from a named local
lane receipt. Unit conversions and arithmetic are my own and are shown. `portal.nersc.gov` was not
touched. Kill criteria are stated at the top of each route, before the evidence is weighed.

---

## 1. Pinned sources (fetched 2026-08-18, verbatim)

**S1 — Saadeh et al. 2016**, *How isotropic is the Universe?*, Phys. Rev. Lett. 117, 131302,
arXiv:1605.07178, abstract:
> "For the vector mode (associated with vorticity), we obtain a limit on the anisotropic expansion
> of $(\sigma_V/H)_0 < 4.7 \times 10^{-11}$ (95% CI), which is an order of magnitude tighter than
> previous Planck results that used CMB temperature only."

**S2 — Planck 2015 results. XVIII. Background geometry & topology**, A&A 594, A18 (2016),
arXiv:1502.01593, abstract:
> "In the physical setting where the Bianchi parameters are fit simultaneously with the standard
> cosmological parameters, we find no evidence for a Bianchi VII_h cosmology and constrain the
> vorticity of such models to (ω/H)_0 < 7.6×10^{-10} (95% CL)."

**S3 — Planck 2018 results. VI. Cosmological parameters**, A&A 641, A6 (2020), arXiv:1807.06209,
abstract: "Hubble constant $H_0 = (67.4\pm 0.5)$ km/s/Mpc" and "matter density parameter
$\Omega_m = 0.315\pm 0.007$".

**S4 — Reid et al. 2019**, *Trigonometric Parallaxes of High-Mass Star Forming Regions: Our View
of the Milky Way*, ApJ (DOI 10.3847/1538-4357/ab4a11), arXiv:1910.03357, abstract:
> "the distance to the Galactic center, Ro = 8.15 +/- 0.15 kpc, the circular rotation speed at the
> Sun's position, To = 236 +/- 7 km/s"

**S5 — Li-Xin Li**, *Effect of the Global Rotation of the Universe on the Formation of Galaxies*,
Gen. Rel. Grav. 30 (1998) 497, arXiv:astro-ph/9703082, abstract (in part):
> "the global rotation provides a natural origin for the rotation of galaxies … The global
> rotation gives a natural explanation of the empirical relation between the angular momentum and
> mass of galaxies: $J \propto M^{5/3}$. The present angular velocity of the universe is
> estimated, which is $\sim 10^{-13}\, rad\, yr^{-1}$."

**S6 — Popławski 2010**, *Cosmology with torsion: An alternative to cosmic inflation*, Phys. Lett.
B 694, 181–185 (Erratum: B 701, 672), arXiv:1007.0587, abstract (in part):
> "the dynamics of the closed Universe immediately after this state naturally solves the flatness
> and horizon problems in cosmology because of an extremely small and negative torsion density
> parameter, $\Omega_S \approx -10^{-69}$. … This scenario also suggests that the contraction of
> our Universe preceding the bounce at the minimum radius may correspond to the dynamics of matter
> inside a collapsing black hole existing in another universe, which could explain the origin of
> the Big Bang."
Full-text value, pinned at Tori's custody audit and carried in the packet (Rev 4):
**Ω_S = −8.6×10⁻⁷⁰**, with "no sensitivity floor and no forecast amplitude" defined for the
verification route.

**S7 — Conselice et al. 2016**, *The Evolution of Galaxy Number Density at z < 8 and its
Implications*, ApJ, arXiv:1607.03909, abstract:
> "the total number of galaxies in the universe up to z = 8 is 2.0^{+0.7}_{-0.6} × 10^{12}
> (two trillion)"

**Local certified counts (named receipts, not re-derived here):**
- `../prereg/KUN_FEASIBILITY_REGATE_20260812.md`: "the 100,000 accepted-galaxy requirement is
  reachable if more DR10.1 South keyspace is counted"; primary floor
  `has-spiral-arms_total-votes >= 5`; restricted spiral fraction 18.23% vs 13.06% break-even;
  Cut-6 survival 82.404622%; one-sided lower retention 85.72%.
- `../../bhu-track-20260805T2000K/BHU_LITERATURE_BASELINE.json`: torsion-bounce category total
  **516** papers; 2026 entries include arXiv:2606.09786 (*Neutron stars in Poincaré gauge gravity
  with quadratic torsion*) and arXiv:2606.23418 (*Spacetime torsion fixes the mass and spin of
  gravitationally produced dark matter*).

**Unit conversions used throughout (mine):** 1 Mpc = 3.086×10¹⁹ km; 1 kpc = 3.086×10¹⁶ km;
1 yr = 3.156×10⁷ s. Hence H₀ = 67.4 km/s/Mpc = **2.18×10⁻¹⁸ s⁻¹** (S3).

---

## 2. Route A — axis-model handedness amplitude

### Kill criteria (stated before evidence)
- **K-A1 (DEAD-ON-ARRIVAL):** if the handedness asymmetry A(Ω_max), evaluated at the tightest
  published rotation bound under the *most generous* published or defensible coupling, falls ≥2
  orders of magnitude below the spin-parity design's 3σ statistical floor, AND no galaxy sample
  physically obtainable (N ≤ the ~2×10¹² galaxies in the observable universe, S7) closes the gap.
- **K-A2 (ALREADY-DONE):** if a published derivation already maps global rotation to a galaxy
  handedness/spin amplitude AND confronts it with modern rotation bounds.
- **PROCEED-TO-PHASE1** otherwise: a live gap between the allowed amplitude and a reachable floor.

### Derivation chain being scoped
Parent-spin/interior rotation Ω → present-day global vorticity ω₀ (bounded by CMB) → coupling
into protogalactic angular momentum during tidal-torque spin-up → coherent handedness bias →
asymmetry A(Ω) in CW/CCW counts, with scale/redshift dependence.

### Order-of-magnitude arithmetic
**Allowed present-day rotation.** From S2 (model-specific, Bianchi VII_h):
ω_max = 7.6×10⁻¹⁰ × H₀ = 7.6×10⁻¹⁰ × 2.18×10⁻¹⁸ s⁻¹ ≈ **1.7×10⁻²⁷ s⁻¹**.
From S1 (general vector mode, the tighter and more model-agnostic limit):
ω_max = 4.7×10⁻¹¹ × H₀ ≈ **1.0×10⁻²⁸ s⁻¹**. I use the *looser* S2 number below — the generous
choice for the model.

**Generous branch (Li-normalized).** S5 estimates that a universal rotation of
ω_Li ~ 10⁻¹³ rad/yr = 3.2×10⁻²¹ s⁻¹ suffices for global rotation to be the *dominant* origin of
galaxy rotation (order-unity spin coherence, i.e. A ~ 1). Assuming the imprint scales linearly in
Ω below that (generous — it also assumes tidal randomization does not wash the coherence out):
A(ω_max) ≈ ω_max/ω_Li ≈ 1.7×10⁻²⁷ / 3.2×10⁻²¹ ≈ **5×10⁻⁷** (S2 bound), or **3×10⁻⁸** (S1 bound).
Note ω_Li is Li's *present* angular velocity, so the collapse-era amplification is already inside
this normalization; no extra (1+z) factor is available to the model.

**Conservative branch (direct spin comparison).** Present disk angular velocity of a Milky-Way
galaxy (S4): ω_disk = Θ₀/R₀ = 236 km/s ÷ (8.15 × 3.086×10¹⁶ km) ≈ **9.4×10⁻¹⁶ s⁻¹**. A naive
linear admixture gives A ≈ ω_max/ω_disk ≈ 1.7×10⁻²⁷/9.4×10⁻¹⁶ ≈ **1.8×10⁻¹²**.

So the bracket, spanning the most generous to the most naive coupling: **A ∈ [~10⁻¹², ~5×10⁻⁷]**.

**Survey floor (our own design as yardstick).** The Kun-certified spin-parity design requires
N = 10⁵ accepted galaxies (receipt above; the dered Cut-5 parent carries a certified
contiguous partial-coverage lower bound of 208,407 rows per
`../prereg/TORI_PARENT_ROW_COUNT_20260812.md`). For A = (N_cw−N_ccw)/N, σ_A = 1/√N ≈ **3.2×10⁻³**;
a 3σ detection needs A ≳ **1×10⁻²**.

**The gap.** Even the generous branch sits **4.3 orders of magnitude** below the 3σ floor
(5×10⁻⁷ vs 1×10⁻²). Closing it statistically needs N = 9/A² ≈ 3.6×10¹³ galaxies — **~18× more
galaxies than exist** in the observable universe (2.0×10¹², S7). Perfectly classifying every
galaxy that exists gives σ_A ≈ 7×10⁻⁷, i.e. the generous-branch signal would still be <1σ. The
kill is therefore *sample-complete*: under any linear coupling, no survey that can ever be built
reaches A(Ω_max). The only escape is a nonlinear amplifier (an instability locking spins to the
axis, gain >10⁴); arXiv:1910.10819v2 itself calls the non-inertial forces "small" and has
galaxies "tend to align" — a perturbative, not locking, mechanism (packet §1.3). Inventing an
amplifier would be new model-building, not derivation of the existing model's prediction.

### Novelty note (Goru adjudicates)
The chain's core mapping **already exists in print**: S5 (Li 1998) derives galaxy rotation from
global rotation, gets J ∝ M^{5/3}, and estimates the required ω. What does *not* appear to exist
is the confrontation of that mapping with the modern S1/S2 bounds and a survey floor — i.e., the
closure calculation itself. So the route is not novel as mechanics, only as a null-forecast.

### Verdict: **DEAD-ON-ARRIVAL** (K-A1 satisfied; sample-complete kill). Confidence: high (~0.9).
The residual 0.1 covers a published nonlinear amplification mechanism Goru's sweep might surface.
Note for the merged verdict: this DOA is the *publishable-closure-note* kind the brief
anticipates — see §5 for the bar it would have to meet.

---

## 3. Route B — torsion-bounce (Popławski) observables

### Kill criteria (stated before evidence)
- **K-B1 (DEAD-ON-ARRIVAL):** if every quantitative observable attached to the black-hole-parent
  element sits ≥3 orders below current/funded instrument sensitivity — or the source defines no
  sensitivity floor and the natural precision yardstick shows a deficit ≥10 orders.
- **K-B2 (route-out):** an observable that is reachable but derivable only as *generic*
  torsion-bounce cosmology (parent-BH element not load-bearing) cannot rescue Route B as a BHU
  observable; it transfers to Route C's uniqueness question.
- **K-B3 (ALREADY-DONE):** the magnitude derivation exists in print — cite it.
- **PROCEED-TO-PHASE1** if any BHU-attached observable has a derivable magnitude within ~3 orders
  of a real instrument.

### Enumeration of quantitative observable statements (per the brief)
1. **Present-day torsion density, Ω_S ≈ −10⁻⁶⁹** (S6 abstract, verbatim; full text −8.6×10⁻⁷⁰,
   Tori-pinned). This is the only number the source attaches to the "verify whether our Universe
   was born in a black hole" route, and the source "defines no sensitivity floor and no forecast
   amplitude" for it (packet §1.2). Yardstick: the best current density-parameter precision is
   σ(Ω_m) = 0.007 (S3). Deficit: **~66 orders of magnitude**. For calibration, forty years of CMB
   experiments (COBE→Planck→CMB-S4-class) bought ~3 orders in sensitivity; 66 orders is not an
   instrument roadmap, it is a category error. No conceivable near-future data reaches it.
2. **Expansion-history contribution near the bounce.** Torsion repulsion operates at
   Cartan-density scales; the model's *own selling point* (S6: "naturally solves the flatness and
   horizon problems") is precisely the statement that the post-bounce expansion dilutes torsion
   relics to the Ω_S level. The mechanism that makes the model viable is the mechanism that hides
   it. Same 66-order class as (1).
3. **Spin-spin contact interaction relics (ECKS four-fermion term).** No published present-day
   magnitude with a sensitivity floor located (packet §1.2, Q1); the natural suppression is the
   same torsion coupling emblematized by Ω_S.
4. **Parity-violation relics.** No published magnitude located in the packet or the corpus
   baseline; same suppression class.
5. **Bounce-driven inflation numerics** (the ApJ 832, 96 line: particle production, "a finite
   period of exponential expansion (inflation) … without a scalar field", possible multiple
   bounces — packet §1.2). This channel *is* potentially reachable by CMB data (spectral
   quantities are derivable in principle). But it fails **K-B2**: in S6 the black-hole parent
   enters as "suggests / may correspond / could explain" — an interpretation attached to a generic
   torsion-bounce, so any n_s/r-type derivation tests ECKS bounce cosmology, not black-hole
   parentage (packet: any such signature "would be a prediction of torsion-bounce inflation
   generally, not of the black-hole-parent interpretation specifically"). It is also an active
   field owned by others — the local corpus's 2026 entries include Einstein–Cartan pseudoscalaron
   inflation (2605.09571) and Einstein–Cartan Higgs-inflation oscillons (2603.19178) — so Phase 1
   here would be entering an existing programme, not deriving a BHU test.
6. **Adjacent 2026 torsion entries, noted per the brief as instrument-bound and not BHU tests:**
   neutron stars in Poincaré gauge gravity with quadratic torsion (2606.09786); torsion-fixed
   dark-matter mass/spin (2606.23418). They show the torsion field is alive (516-paper corpus
   category) but neither derives a birth observable.

### Verdict: **DEAD-ON-ARRIVAL** (K-B1: the only BHU-attached number is ~66 orders below the
best density-parameter precision, with no sensitivity floor even defined by the source; the one
reachable sub-channel fails K-B2 as non-BHU-specific). Confidence: high (~0.85). The residual
covers a Popławski-line paper with a calibrated reachable observable that Goru's sweep might
surface; title-level inspection of the 516-paper category's 2026 entries shows none.

---

## 4. Route C — the birth fingerprint

### Kill criteria (stated before evidence)
- **K-C1 (DEAD-ON-ARRIVAL / closure):** if every candidate carrier of parent-specific information
  across the bounce either (a) reduces to a Route A/B quantity already killed by magnitude, or
  (b) is reproducible by a parentless bounce with suitably chosen initial conditions — then no
  BHU-unique fingerprint is conceivable in current frameworks, and C15's second arm closes.
- **K-C2 (PROCEED-TO-PHASE1):** a concrete mechanism exists (citable physics) whose imprint only
  a parent-black-hole birth produces, with a magnitude plausibly reachable by real data.
- **K-C3 (ALREADY-DONE):** such a fingerprint is already derived in print.

### The candidate carriers, enumerated
Everything our universe can inherit from a parent must cross the bounce hypersurface inside the
horizon. The classes:

**(a) Parent angular momentum → axis.** The one carrier the Kerr matching specifically supplies —
v2's Kerr-radius correction a = M/mc and Λ = 3Ω²/c² (packet §1.3). Its observable is exactly
Route A's handedness/alignment statistic, which §2 kills at ≥4.3 orders below any buildable
survey. It is also non-unique: Bianchi-type models and primordial vorticity produce the same
phenomenology with no parent hole (packet Q2).

**(b) Parent mass/entropy → size and curvature of the closed universe.** A measured closed
geometry is consistent with *any* closed FRW; the value carries no parent tag. A *joint*
prediction — the Kerr matching locking the rotation amplitude to the curvature scale (a = M/mc
ties Ω to the closure radius) — is the only structurally BHU-unique correlation on offer, and it
inherits Route A's amplitude on its rotation arm, i.e. it is unmeasurable at the same ≥4-order
margin.

**(c) Pre-bounce fluctuation spectra → super-horizon features, low-ℓ anomalies.** Generic to
every bounce cosmology; the packet's finding stands: "no published observable that differs from
generic bounce cosmology" (packet Q2), and any measured anomaly is equally claimable by a dozen
parentless models.

**(d) GW echoes and PBH populations (the §1.6 branch).** These are observables of black-hole
interiors *elsewhere in our universe* — tests of "black holes spawn universes" in the outbound
direction. They cannot fingerprint *our own* birth even in principle: detecting them would not
tell us whether we ourselves sit inside a parent's horizon.

### The sharp reason (what the interior-FRW matching erases and why)
The parent's event horizon is a causal boundary: by construction, the only parent data available
to the interior is the state of the collapsing matter itself, and after the bounce that state is
expressible entirely as initial conditions on an FRW/Bianchi patch — a density, a spin, a shear,
a fluctuation spectrum. A parentless bounce model is free to posit *identical* initial
conditions. Therefore "born in a black hole" differs from "generic bounce" only by the *story*
attached to the initial conditions, never by a dynamical channel — unless a matching condition
enforces a correlation among observables that free initial conditions cannot mimic. The Kerr
matching does supply exactly one such correlation (carrier (b)), and its measurable arm is the
rotation amplitude that §2 shows is below every floor that can ever be built. The post-bounce
quasi-exponential expansion — the model's own explanation of flatness and isotropy (S6) — is
simultaneously the eraser: whatever crossed the bounce is diluted to the Ω_S ≈ −10⁻⁶⁹ level.

### Verdict: **DEAD-ON-ARRIVAL** — K-C1 satisfied; no reachable BHU-unique channel is conceivable
in the current frameworks, *for the stated reason* (causal-boundary + initial-condition
degeneracy, with the single structural exception killed by magnitude). This confirms the packet
and, if Kun concurs, **closes C15's second arm**. Confidence: moderate-high (~0.75) — lower than
A/B because "none is conceivable" is a framework-level argument, not arithmetic; a future
calibrated parity-odd relic mechanism (K-C2) would reopen it, and Goru's sweep should check for
any claimed-unique-signature paper I have not seen.

---

## 5. Summary and what Phase 1 would cost

| Route | Verdict | Margin | Confidence |
|---|---|---|---|
| A — handedness amplitude | DEAD-ON-ARRIVAL | ≥4.3 orders below 3σ floor; sample-complete (needs ~18× all galaxies) | ~0.9 |
| B — torsion-bounce observables | DEAD-ON-ARRIVAL | ~66 orders below σ(Ω_m); reachable sub-channel not BHU-specific | ~0.85 |
| C — birth fingerprint | DEAD-ON-ARRIVAL (closure) | no channel survives K-C1; sole structural candidate inherits A's kill | ~0.75 |

**No route earns Phase 1 as a derivation night.** The only defensible Phase-1-shaped product is
the **Route A closure note**: combine S1/S2 bounds with the S5 mapping and survey statistics into
a formal statement — "under linear coupling, the allowed global rotation caps the galaxy
handedness asymmetry at A ≲ 5×10⁻⁷, below the reach of any galaxy survey that can exist." Cost:
one evening, arithmetic already 90% done above. **The bar, stated per the brief's no-overclaim
rule:** Duho's flagship standard says assembly of published values plus commentary is not a
study; this note has one original element (the bound→floor confrontation appears nowhere in
print — Goru to confirm), which makes it at best a short comment/research-note-class closure
document, not a flagship paper. It is a way to *end* the line with a citable reason, not to
continue it.

**Caveats, openly:** (i) the A-route coupling bracket rests on Li 1998's normalization plus a
linearity assumption — generous in the model's favor, but an order-of-magnitude device, not a
transfer function; (ii) S2's bound is Bianchi VII_h-specific and S1's is the general vector mode
— I used the looser one; (iii) title-level corpus checks are not full-text sweeps — Goru's
`GORU_PHASE0_PRIORART.md` is the authority on novelty; (iv) verdicts here were not harmonized
with any other seat.

— Lana, 2026-08-18 21:42 KST. Phase 0 scoping only; nothing derived in full, nothing committed.
Kun gates next.
