# K1 stage-1 pre-registration — does black-hole production fall when the neutron-star bar or the primordial amplitude moves? A semi-analytic sign test of the cosmological-natural-selection premise (entries 6, 7, 31)

**Tori, 2026-09-03 16:26 KST. Ordered by Duho ("a", relay via Blanc 16:24 KST). Written and committed BEFORE any derivation. Gated by a fresh seat via `nm_referee_dispatch.sh` (agy, ACCESS PROVEN, `K1S1_PREREG_GATE_agy.md`: PREREG_SOUND_WITH_REPAIRS, four repairs applied 2026-09-03 16:36 KST; the saddle/minimum gap became the class K1_STATIONARY_NOT_MAX). Paper HOLD; nothing outward; tier/standing stamps remain Duho's.**

## 0. Why this exists
Cosmological natural selection (entry 6, Smolin 1992; entry 31, Smolin 2004) asserts that our universe sits at "a local maximum
of R(p), the expected number of black holes", so that "modifications in the parameters … lead to decreases in the expected
number of black holes" (`smolin_1992_clean.txt` L233, L238; R(A_m, p) named at L589). The corpus's one live calibrated falsifier
(entry 31: no neutron star above 2.5 M☉, synthesis L60–66) tests one consequence of that premise. The premise itself is
DISPUTED and pinned: Rothman & Ellis 1993 — every parameter change must reduce black holes, and excluding primordial black
holes is "the primary requirement", recorded as unanswered (synthesis L67–68; `WARRANT_TABLE_20260903.md` row 31); Harrison
1995; Silk 1997 (L69–70). Entry 6's direction is `W_DIRECTION_ASSUMED` (row 6, ruled (a) 09-03). No paper in the corpus
computes the sign of ∂N_BH/∂θ for any parameter θ. Stage 1 computes it semi-analytically for two parameters.

## 1. Objects, every symbol bound
- **θ₁ = ln A_s**, the primordial scalar amplitude. Value and error to be QUOTED at step 1 with a line receipt from the pinned
  Planck 2018 parameters text `1807.06209_clean.txt` (the record carries n_s = 0.9649 ± 0.0042, synthesis L46; A_s is named
  here, not quoted).
- **θ₂ = M_NS,max**, the maximum neutron-star mass; the study varies it across Smolin's 2.5 M☉ bar (synthesis L60).
- **N_BH(θ) = N_st(θ) + N_PBH(θ)** per comoving volume at the present epoch.
  - N_st: halo-collapse abundance (Press–Schechter; the variance scales with the amplitude as in standard linear theory, exponent pinned with a receipt at step 1; fixed transfer function) × a star-formation
    efficiency × the initial-mass-function fraction of stars whose remnant exceeds M_NS,max. The IMF and the remnant-mass
    relation are NUISANCE inputs with named published ranges (pinned at step 1 with receipts), not single values.
  - N_PBH: threshold-collapse abundance β(A_s) from the primordial spectrum at the PBH scale, with the collapse threshold
    δ_c as a nuisance range (pinned at step 1). PBHs are INCLUDED because Rothman & Ellis's "primary requirement" is exactly
    their exclusion (synthesis L67–68).
- **The premise, as a testable statement:** ∂N_BH/∂θ_i = 0 and ∂²N_BH/∂θ_i² < 0 at the observed θ_i, for i = 1, 2 (a local
  maximum, Smolin 1992 L233).

## 2. The question, exactly
At the observed values, what is the SIGN of ∂N_BH/∂ ln A_s and of ∂N_BH/∂M_NS,max, marginalised over the named nuisance
ranges? Is either a local maximum?

## 3. Outcome classes — declared now
- **K1_MAX:** both partials cross zero at the observed values with negative curvature across the whole nuisance range —
  the premise survives stage 1 (stage 2, population synthesis, then tests the stellar channel properly).
- **K1_MONOTONE_UP:** N_BH increases with A_s (or is non-decreasing across the 2.5 M☉ bar) across the whole nuisance range —
  the premise is refuted for that parameter, and the falsifier under entry 31 loses its motivation (a finding for the
  record; the tier/standing stamp stays Duho's).
- **K1_STATIONARY_NOT_MAX:** a partial crosses zero at the observed value but the curvature is positive or indefinite (a local minimum or saddle) across the nuisance range — the premise is refuted for that parameter exactly as under K1_MONOTONE_UP (the premise asserts a maximum, Smolin 1992 L233).
- **K1_MONOTONE_DOWN:** N_BH decreases with the parameter at the observed value — consistent with, but not a maximum; report.
- **K1_UNIDENTIFIED:** the sign flips within the nuisance range → INCONCLUSIVE; name the nuisance responsible and the range
  that would fix it (this is the risk all three proposing seats flagged).

## 4. What counts as a verdict either way
A closed-form or tabulated N_BH(θ) with the partials evaluated at the observed values for the corners and the centre of the
nuisance box, the sign agreeing across the box (K1_MAX / UP / DOWN) or not (K1_UNIDENTIFIED). Every input carries a receipt.

## 5. Controls (must pass before any class is filed)
- **C1:** the stellar black-hole count at the observed θ must land within the order of magnitude of one independent published
  estimate (named and pinned at step 1; failure = model wrong, stop).
- **C2:** the PBH abundance at the observed A_s must respect the published abundance constraints at the chosen mass scale
  (named and pinned at step 1); a model that violates them is discarded, not tuned.
- **C3 deletion probe:** with PBHs removed, confirm the sign of ∂N_BH/∂ ln A_s changes or not, and report it — this isolates
  Rothman & Ellis's requirement. Failure = the stellar-only sign cannot be computed or disagrees between the two derivative methods of C4; then no class is filed.
- **C4:** the derivative is computed two ways (analytic and finite-difference) and must agree in sign.

## 6. Seat plan, blind double, cost
- Two seats build the semi-analytic model independently from this prereg (Claude seat and agy; each its own script and pin
  sheet; results written only when complete). Codex gates the pin sheets (every number receipted) before either seat computes.
  A split on the class → third seat via `nm_referee_dispatch.sh`; Kimi (`--provider moonshot`, log checked, no fallback
  line) is the fourth seat on the pin-sheet audit only.
- Cost (seat planning estimate, not a corpus number): about five seat-days; public Planck values already pinned; laptop compute.

## 7. What would make it INCONCLUSIVE
K1_UNIDENTIFIED; or C1/C2 failing after two model attempts; or the PBH channel depending on a small-scale spectrum shape the
record cannot pin (then stage 1 reports the stellar channel alone, labelled as such, and the PBH question passes to stage 2).

## 8. Non-circularity
The measured A_s and the 2.5 M☉ bar are the POINTS at which the derivative is evaluated, not inputs to the premise. No
selection argument enters the model; the model is ordinary structure formation plus threshold collapse.
