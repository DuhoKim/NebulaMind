# Global-rotation bounds preclude an observable galaxy-handedness asymmetry in the rotating-parent black-hole-universe scenario — a closure note

**Lana (science seat), 2026-08-18 22:34 KST.** Authored per `CLOSURE_NOTE_BRIEF.md` (Hwao,
22:00 KST; Duho, verbatim: "go ahead with the closure note if the gate passes"), active because
`KUN_PHASE0_GATE.md` first line is `PASS_PHASE0_SCOPING`.

**Class of this document, stated up front per Duho's bar:** this is a **research-note-class
closure document, not a flagship paper and not a study.** Under the flagship standard (original
content required; assembly of published values plus commentary is not a study), this note carries
exactly one original element — the explicit confrontation of the allowed global-rotation
amplitude with a galaxy-survey statistical floor — and everything else in it is published
material, quoted with its source. Kun's Phase 0 gate adjudicated the novelty claim to exactly
that scope: **the rotation→galaxy-spin mechanics are Li 1998's (S5); the computed bound-to-floor
amplitude confrontation is the novel element**, not located in print at the title/abstract sweep
depth of Phase 0 (see §7 for the depth caveat).

**Scope label:** black-hole-universe (BHU) cosmology is Duho's personal side-interest, not a
NebulaMind research programme. Where this note goes after gating is Duho's separate decision;
nothing is published, uploaded, or committed by this document.

**Source tags.** S1–S7 are the Phase 0 pins of `LANA_PHASE0_SCOPING.md` §1, fetched 2026-08-18
from arXiv abstract pages, quoted verbatim there, and independently re-fetched and confirmed at
Kun's gate (`KUN_PHASE0_GATE.md` §2). The arithmetic below was independently recomputed at that
gate (§3 there) with no errors found.

- **S1** Saadeh et al. 2016, PRL 117, 131302 (arXiv:1605.07178)
- **S2** Planck 2015 XVIII, A&A 594, A18 (arXiv:1502.01593)
- **S3** Planck 2018 VI, A&A 641, A6 (arXiv:1807.06209)
- **S4** Reid et al. 2019, ApJ (arXiv:1910.03357)
- **S5** Li 1998, Gen. Rel. Grav. 30, 497 (arXiv:astro-ph/9703082)
- **S6** Popławski 2010, Phys. Lett. B 694, 181 (arXiv:1007.0587)
- **S7** Conselice et al. 2016, ApJ (arXiv:1607.03909)
- **Packet** = `../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md`, SHA-256 verified at
  Phase 0 and re-verified at Kun's gate
  (`b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516`).

---

## 1. The claim as published

The rotating-parent axis scenario (arXiv:1910.10819v2, characterized at packet §1.3 from Tori's
full-text custody audit) proposes that if our universe was born inside a rotating black hole, the
parent's rotation axis becomes a preferred axis, and states explicitly: *"Consequently, the
numbers of clockwise- and counterclockwise-spinning galaxies in a rotating universe should be
different."* What the source supplies is mechanics without calibration: a Kerr-radius correction
to the FLRW metric (a = M/mc), rotating-frame force laws, Λ = 3Ω²/c² — and what it never
supplies, per the packet's audited characterization, is **any calibrated model prediction for the
amplitude, scale, or redshift dependence of the handedness statistic, any independently predicted
axis direction, any finite lower bound, or any numerical acceptance region.** The source's own
language on the driving forces is that they are "small" and that galaxies "tend to align"
(packet §1.3). The claim, as published, is an explicit, source-backed qualitative claim — not a
calibrated or pre-data forecast (packet §0).

This note asks the question the source leaves open: **if the effect exists, how large is it
allowed to be — and could any survey ever see it?**

## 2. The mapping that exists in print

The chain "global rotation → galaxy rotation" was derived by Li (S5) in 1998. The S5 abstract,
verbatim in part: *"the global rotation provides a natural origin for the rotation of galaxies …
The global rotation gives a natural explanation of the empirical relation between the angular
momentum and mass of galaxies: J ∝ M^{5/3}. The present angular velocity of the universe is
estimated, which is ∼10⁻¹³ rad yr⁻¹."*

Two properties of S5 matter here. First, it supplies a **normalization**: a present universal
angular velocity ω_Li ~ 10⁻¹³ rad yr⁻¹ = 3.2×10⁻²¹ s⁻¹ is what it takes for global rotation to
be the *dominant* origin of galaxy rotation — i.e., order-unity spin coherence. Second, per
Kun's gate adjudication: S5 derives galaxy rotation (angular momentum, the J–M relation), **not**
a handedness-asymmetry amplitude A(Ω), and it predates the modern CMB bounds by two decades, so
no confrontation with those bounds exists in it. That confrontation is what follows.

## 3. The modern bounds, quoted verbatim

Two published 95%-confidence limits on present-day global rotation exist at different levels of
model generality:

- **S1 (general vector mode, tighter):** *"For the vector mode (associated with vorticity), we
  obtain a limit on the anisotropic expansion of (σ_V/H)₀ < 4.7 × 10⁻¹¹ (95% CI), which is an
  order of magnitude tighter than previous Planck results that used CMB temperature only."*
- **S2 (Bianchi VII_h-specific, looser):** *"In the physical setting where the Bianchi
  parameters are fit simultaneously with the standard cosmological parameters, we find no
  evidence for a Bianchi VII_h cosmology and constrain the vorticity of such models to
  (ω/H)₀ < 7.6×10⁻¹⁰ (95% CL)."*

With H₀ = (67.4 ± 0.5) km/s/Mpc (S3) = 2.18×10⁻¹⁸ s⁻¹ (1 Mpc = 3.086×10¹⁹ km), these give:

- ω_max(S2) = 7.6×10⁻¹⁰ × H₀ ≈ **1.7×10⁻²⁷ s⁻¹**
- ω_max(S1) = 4.7×10⁻¹¹ × H₀ ≈ **1.0×10⁻²⁸ s⁻¹**

The headline numbers below use the **looser S2 bound — the generous choice for the model**; the
S1 bound tightens every conclusion by a further order of magnitude.

## 4. The confrontation

**Allowed asymmetry amplitude, bracketed by two labeled coupling assumptions:**

- **Generous branch (Li-normalized; assumes linear scaling of the imprint in Ω below ω_Li and
  that tidal randomization does not wash out the coherence):**
  A(ω_max) ≈ ω_max/ω_Li ≈ 1.7×10⁻²⁷ / 3.2×10⁻²¹ ≈ **5×10⁻⁷** (S2 bound; 3×10⁻⁸ under S1).
  Because ω_Li is S5's *present-day* angular velocity, the collapse-era amplification is already
  inside this normalization; no additional (1+z) factor is available to the model.
- **Conservative branch (direct admixture into a present-day disk):** with the Milky Way values
  Θ₀ = 236 ± 7 km/s and R₀ = 8.15 ± 0.15 kpc (S4), ω_disk = Θ₀/R₀ ≈ 9.4×10⁻¹⁶ s⁻¹, giving
  A ≈ ω_max/ω_disk ≈ **1.8×10⁻¹²**.

The allowed amplitude therefore lies in the bracket **A ∈ [~10⁻¹², ~5×10⁻⁷]**, with the upper
edge requiring every assumption to break in the model's favor.

**Survey floor.** For a handedness asymmetry A = (N_cw − N_ccw)/N, the statistical floor is
σ_A = 1/√N. At the N = 10⁵ accepted-galaxy scale of our own Kun-certified spin-parity design
(`../prereg/KUN_FEASIBILITY_REGATE_20260812.md`), σ_A ≈ 3.2×10⁻³ and a 3σ detection requires
A ≳ 1×10⁻².

**The sample-complete kill.** Even the generous branch sits **4.3 orders of magnitude below**
the 3σ floor. Closing that gap statistically requires N = 9/A² ≈ **3.6×10¹³ galaxies** — about
**18 times more galaxies than exist**: the observable universe contains *"2.0^{+0.7}_{−0.6} ×
10¹² (two trillion)"* galaxies to z = 8 (S7, verbatim). Perfectly classifying every galaxy that
exists gives σ_A ≈ 7×10⁻⁷, at which the generous-branch signal is still below 1σ (Kun's
recomputation: 0.74σ). The conclusion is not that the measurement is expensive; it is that
**under linear coupling, no galaxy survey that can ever be built reaches the allowed
amplitude.** The kill is sample-complete, not sensitivity-limited.

## 5. The stated escape, and why it is out of scope

The single escape from this conclusion is a **nonlinear spin-locking amplifier**: a mechanism —
an instability, a resonance — that locks galaxy spins to the axis with a gain exceeding ~10⁴
over linear coupling. No such mechanism exists in the axis source: its own published language is
that the non-inertial forces are "small" and that galaxies "tend to align" — a perturbative
statement, not a locking one (packet §1.3). Positing such an amplifier would therefore be **new
model-building, not a derivation of the existing model's prediction**, and is out of scope for a
closure note whose subject is what the published scenario, as published, allows.

## 6. What this closes — and what it does not

**Closes:** C15's first arm (`../bhu-closing-video-20260812T2322K/CLAIM_LINE_LEDGER_V11.md`) for
the axis-model class under linear coupling. C15 asks for a magnitude/scale/redshift derivation
with a pass-or-fail range; the derivation now exists and its result is negative — the allowed
range lies entirely below every floor any survey can reach, so no pass-or-fail test can be
constructed from galaxy handedness. Phase 0's Route C finding (gated the same evening) closes
the second arm — no reachable BHU-unique birth fingerprint — separately.

**Does not falsify BHU.** The family boundary, restated from the packet §3: "BHU" is at least
five distinct programmes (Pathria's identification, Popławski's torsion bounce — whose
black-hole parent enters as "suggests / may correspond / could explain", S6 verbatim — the
rotating-parent axis scenario, Smolin's CNS, and the baby-universe branch). This note constrains
the observability of one qualitative claim of one member. It says nothing about the others, and
a sub-threshold effect is not a refuted effect: A ≲ 5×10⁻⁷ is consistent with the scenario being
true and forever unmeasurable by this channel.

**Does not touch the spin-parity measurement.** The spin-parity lane measures a galaxy-spin
handedness asymmetry as an observational question about galaxies and their classification
systematics. That measurement stands on its own merits, independent of BHU: this note removes
its BHU *interpretation* under linear coupling — any asymmetry it detects at its ~10⁻³ floor
would be ~4 orders too large to be the global-rotation imprint allowed here, and would therefore
point at astrophysics or systematics, not at a rotating parent. Nothing in this note alters that
lane's design, floors, or preregistration.

## 7. Limits

1. **The bracket is an order-of-magnitude device, not a transfer function.** The generous branch
   rests on S5's ω_Li normalization plus an assumed linear scaling of handedness coherence in Ω;
   the conservative branch is a naive present-day admixture. A Phase-1-style derivation of the
   true transfer function was deliberately not performed (and, given a ≥4.3-order gap bounded
   above by a sample-complete limit, could only change the verdict via the §5 amplifier, which
   is out of scope).
2. **Model specificity of the bounds.** S2's limit is specific to Bianchi VII_h; S1's vector-mode
   limit is more general and an order of magnitude tighter. The looser bound was used throughout;
   any model escaping *both* would need a rotation history outside the classes either analysis
   constrains, which no BHU source on record supplies.
3. **Novelty rests on a title/abstract-level sweep.** Goru's Phase 0 prior-art sweep
   (`GORU_PHASE0_PRIORART.md`, adjudicated at Kun's gate) found no explicit published A(Ω)
   bound-to-floor confrontation, and Kun's adjudication assigns this note's original element
   exactly there. Per the gate's carried caveat, that sweep is title/abstract-depth: **before
   any sentence of this note is cited outside the lane, a full text-level sweep of the Li-line
   and Shamir-line literature is required.** "Not located at Phase 0 sweep depth" is the claim;
   "appears nowhere in print" is not claimed.
4. **The Milky Way as fiducial disk.** S4's Θ₀ and R₀ enter only the conservative branch; the
   verdict is carried by the generous branch and is insensitive to order-unity changes in either.

---

**Provenance.** All quoted numbers: S1–S7 as pinned at `LANA_PHASE0_SCOPING.md` §1 and
re-verified at `KUN_PHASE0_GATE.md` §2; arithmetic recomputed independently at that gate §3
("No arithmetic errors found"). Packet hash re-verified at the gate. No new numbers were
introduced in this note beyond the gated scoping. `portal.nersc.gov` untouched.

— Lana, 2026-08-18 22:34 KST. Research-note-class closure; nothing published, nothing committed;
Kun gates next (`KUN_CLOSURE_GATE.md`).
