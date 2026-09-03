# K1 stage-2 pre-registration — does black-hole production fall when the neutron-star mass cap moves? A binary-population-synthesis test of the cosmological-natural-selection premise (entries 6, 7, 31)

**Tori, 2026-09-03 17:20 KST. Ordered by Duho (verbatim "as Tori's rec, both a", relay via Blanc 17:17 KST) on the K1 stage-1 packet. Written
and committed BEFORE any derivation. Gated by a fresh seat via `nm_referee_dispatch.sh` (agy, ACCESS PROVEN, `K1S2_PREREG_GATE_agy.md`: PREREG_SOUND_WITH_REPAIRS, one wording repair on C4 applied 2026-09-03 17:25 KST). Paper HOLD; nothing
outward; tier/standing stamps remain Duho's.**

## 0. Why this exists
Stage 1 (`K1S1_RESULT_20260903.md`) found, with two blind seats and a semi-analytic model, that black-hole production rises
monotonically with the primordial amplitude (K1_MONOTONE_UP) and falls monotonically with the neutron-star mass cap across
Smolin's 2.5 M☉ bar (K1_MONOTONE_DOWN). Its stated limit: no binary evolution. Smolin's own mechanism for the bar runs through
stellar and binary channels (entry 31; the bar itself at synthesis L60). Stage 2 tests the mass-cap parameter with a public
binary population-synthesis code, keeping stage 1's amplitude result as is (the amplitude enters only through the
star-forming-mass normalisation, which cancels in a per-unit-mass yield).

## 1. Objects, every symbol bound
- **θ₂ = M_NS,max**, the maximum neutron-star mass, varied on a grid that brackets the bar: the values are declared at step 1
  from the pinned remnant prescription's own cap (Fryer et al. 2012 adopt 2.5 M☉ as their source bar; master sheet
  `K1S1_PIN_GATE_codex.md` row 4) — one value below, one at, one above 2.5 M☉ (their numerals pinned at step 1, not here).
- **Y_BH(θ₂)** — black holes formed per unit star-forming mass, integrated over the initial-mass function (Kroupa 2001, master
  sheet row 3, slope range [1.6, 3.0]) and the binary population, at a declared metallicity grid (Z ∈ [0, Z☉], Z☉ = 0.02,
  `K1S1_PIN_ROW2_REPAIR_20260903.md`, Fryer L436–437, L1786).
- **The code:** COMPAS — "a public rapid binary population synthesis code" (`2109.10352_clean.txt` L48), "publicly available
  via the github repository" (L52–53). The exact git commit hash, the remnant-mass prescription switch (Fryer delayed / rapid,
  master row 4) and the neutron-star cap parameter are recorded in the step-1 pin sheet; both seats run the same hash.
- **Public posteriors for the controls:** GWTC-3 population paper (`2111.03634_clean.txt`): binary-black-hole merger rate
  17.9–44 Gpc⁻³ yr⁻¹ at z = 0.2 allowing redshift evolution (L17–18); neutron-star–black-hole rate 7.8–140 Gpc⁻³ yr⁻¹ (L15–16).
  Neutron-star mass catalogue, Özel & Freire 2016 (`1603.02698_clean.txt`, the pulsar-mass tables from L311 on; the
  equation-of-state dependence of the maximum mass stated at L103).
- **The premise, as a testable statement:** ∂Y_BH/∂θ₂ = 0 with negative curvature at the observed cap (a local maximum, Smolin
  1992 L233), or at least ∂Y_BH/∂θ₂ < 0 (the direction Smolin needs; stage 1's finding).

## 2. The question, exactly
With binary evolution included, what is the SIGN of ∂Y_BH/∂M_NS,max across the 2.5 M☉ bar, marginalised over the declared
nuisance box (IMF slope; delayed vs rapid engine; metallicity grid; the code's default common-envelope and kick prescriptions
as one fixed setting plus one declared alternative)? Does binary physics keep, kill, or invert stage 1's sign?

## 3. Outcome classes — declared now
- **K1S2_MONOTONE_DOWN:** Y_BH falls across the bar at every box point — stage 1's direction survives binary physics; still not a
  maximum (report the curvature).
- **K1S2_MAX:** ∂Y_BH/∂θ₂ crosses zero at the bar with negative curvature across the box — the premise survives for θ₂.
- **K1S2_MONOTONE_UP** / **K1S2_STATIONARY_NOT_MAX:** the premise is refuted for θ₂ (as in stage 1's vocabulary).
- **K1S2_SIGN_INVERTS:** binary physics reverses stage 1's sign at some box points but not others → INCONCLUSIVE on the sign;
  name the channel (e.g., accretion-induced collapse, mass transfer pushing remnants across the cap) responsible.
- **K1S2_UNIDENTIFIED:** the sign flips within the box for reasons the seats cannot attribute → INCONCLUSIVE.

## 4. What counts as a verdict either way
A tabulated Y_BH at the three cap values for the centre and every corner of the box, with the finite-difference derivative and
its Monte-Carlo error (declared number of binaries per point and seeds, pinned at step 1); a class is filed only when the
derivative's sign is the same at every box point beyond its Monte-Carlo error, else INCONCLUSIVE by the classes above.

## 5. Controls (must pass before any class is filed)
- **C1 (rate):** at the fiducial setting and cap, the code's binary-black-hole merger rate at z = 0.2 must fall inside the GWTC-3
  interval 17.9–44 Gpc⁻³ yr⁻¹ (L17–18) after the declared star-formation-history convolution (its source pinned at step 1).
  Failure after two declared settings = the pipeline is not calibrated; stop; no class is filed.
- **C2 (neutron-star masses):** the code's neutron-star mass distribution at the fiducial cap must be consistent with the
  Özel & Freire catalogue at a declared two-sample test level (level and test pinned at step 1). Failure = stop; no class.
- **C3 (deletion probe):** rerun with binary interactions switched off (single-star evolution only) and confirm the derivative's
  sign is recovered as stage 1's; report whether binary physics changes it. Failure = the single-star sign cannot be
  computed; then no class is filed.
- **C4 (Monte-Carlo control):** doubling the number of binaries at the centre point must not change the derivative's sign;
  failure = increase N until the sign stabilises, or file INCONCLUSIVE.

## 6. Seat plan, blind double, cost
- Two seats run the grid independently from this prereg (codex and the Claude seat; each installs the pinned COMPAS commit in
  its own environment, writes its own pin sheet and driver script, and writes its result only when complete). Kimi
  (`--provider moonshot`, log checked for no fallback line) audits the pin sheets; agy via `nm_referee_dispatch.sh` gates
  the pin sheets before either seat computes, and is the third seat on any class split.
- Cost (seat planning estimate, not a corpus number): about twenty seat-days; compute: COMPAS grids on the lab machines; data:
  the pinned GWTC-3 and Özel & Freire texts, no proprietary inputs.

## 7. What would make it INCONCLUSIVE
K1S2_SIGN_INVERTS or K1S2_UNIDENTIFIED; C1 or C2 failing after two declared settings; the pinned COMPAS commit failing to build
on both seats' machines (then a second pinned commit is tried once and the outcome reported).

## 8. Non-circularity
The GWTC-3 rates and the pulsar-mass catalogue calibrate the CODE, not the premise; the cap value is the point at which the
derivative is evaluated; no selection argument enters the model. Stage 1's sign is a control (C3), not an input.
