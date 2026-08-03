# MOTIVATION — Is the z>7 mass–metallicity offset physical, or a mass-mismatch + calibration artifact?

**Phase:** P1 (Design) · **Lane:** overnight-z7-mzr-20260720 · **Author:** Hwao (Trikitear)
**Grounding rule:** every claim below is tied to a real source in
`wiki-expansion-20260715/area1_mass_metallicity_DR_PACKET.md` (author-year + packet ID).
Where the packet lacks something it is marked **[not in packet — flag for human/DR]**.
No fabrication; nothing here assumes the analysis result.

---

## 1. The contested claim

The literature agrees the gas-phase MZR **normalization falls toward higher redshift**: at fixed
stellar mass, galaxies are more metal-poor earlier. This is measured and consistent through
z~3.3 — Sanders et al. (2021) report `dlog(O/H)/dz = -0.11 ± 0.02` at fixed mass over z=0–3.3
(MZR-E05, MZR-N04). That part is **not** contested.

What **is** contested is the **amplitude and interpretation of the offset in the z>7 (JWST) regime**:

- **Amplitude.** Langeroodi et al. (2023) infer an MZR normalization at z~8 that is **~0.9 dex
  lower than local** — roughly eight-times-lower enrichment at fixed stellar mass — from **11
  lensed galaxies at 7.2<z<9.5** (MZR-N05, packet trust `0.78`, explicitly flagged "early
  small-sample constraint, not yet a universal z~8 zero point"). Whether the true z>7 offset is
  this large, or substantially smaller once scales and masses are matched, is open.
- **Slope.** Sanders et al. (2021) find a low-mass slope near `0.30` invariant to z~3.3;
  Curti et al. (2024, JADES) fit a **shallower** `0.17 ± 0.03` for a low-mass sample spanning
  3<z<10 (MZR-D02, MZR-N06). The two do not agree at the high-z end.
- **FMR validity.** Sanders et al. (2021) find **no** FMR evolution to z~3.3; Curti et al. (2024)
  find a **median FMR offset of ~0.5 dex, especially above z~6**; Garcia et al. (2024) simulations
  predict an **evolving "weak FMR"** rather than an invariant one (MZR-D01). So even the claim
  "early galaxies are metal-poor exactly as the local FMR predicts" is disputed at z>6–7.

**Crux:** are z>7 galaxies metal-poor *as the low-z relation extrapolated predicts* (offset is the
smooth continuation of `dlog(O/H)/dz`), or **anomalously** deficient/enriched relative to that
extrapolation — i.e., is there a genuine z>7 break in normalization, slope, or FMR beyond what
z<3.3 physics forecasts?

---

## 2. Why it matters (what physics rides on it)

- **Early enrichment timescale.** The z>7 normalization sets how fast the first ~500 Myr of star
  formation locked metals into the ISM. A real ~0.9 dex deficit (Langeroodi 2023) implies galaxies
  caught before equilibrium enrichment; a much smaller offset implies rapid early metal build-up.
- **The baryon cycle (outflow / inflow / retention).** The MZR encodes the balance of metal
  production, pristine-gas dilution, gas consumption, and metal-loaded winds; an observed MZR does
  **not** uniquely identify a wind law (MZR-D04; Finlator & Davé 2008). The z>7 offset amplitude is
  the observational lever that constrains how mass-loaded early outflows must be — but only if the
  offset is physical.
- **FMR universality at high-z.** If a single mass–SFR–metallicity surface survives to z>7 with
  fixed coefficients, early ISM physics is a smooth continuation of local regulation; if it breaks
  (Curti 2024's ~0.5 dex offset, Garcia 2024's evolving weak FMR), bursty early galaxies need a
  qualitatively different description (MZR-D01, MZR-U02). This is the #1 JWST high-z frontier.

---

## 3. Why it is genuinely open, not settled

The disagreement survives precisely because the **z>7 offset amplitude (~0.9 dex) is the same size
as, or smaller than, the known systematic budget** — so a real offset and a pure artifact are not
yet separable:

- **Calibration scale (the dominant systematic).** Different strong-line / direct-Te calibration
  families shift `12+log(O/H)` by **up to ~0.7 dex** (Kewley & Ellison 2008; MZR-E02, MZR-N02). Te-
  anchored scales sit at a *lower* normalization than photoionization-model scales (Curti et al.
  2020; MZR-D03). Cross-study MZR zero points are explicitly labeled "unsafe unless the abundance
  scales are matched." A z~8-vs-z~0 comparison that mixes scales can manufacture ~0.5–0.7 dex of
  the claimed offset with no physics.
- **z=0 calibrations mis-applied at high-z.** Hirschmann et al. (2023) show, in cosmological
  simulations, that applying some z=0 strong-line calibrations to early-galaxy ISM conditions can
  **bias O/H downward by up to ~1 dex** (MZR-D03). This is *larger* than the Langeroodi offset — so
  a naive high-z MZR built on local calibrations can look metal-poor for a purely calibration
  reason. This is the single most dangerous confound for the target claim.
- **Small, selected, lensed samples.** The strongest z~8 constraint rests on 11 lensed galaxies
  (Langeroodi 2023, trust `0.78`); the JWST census (Nakajima et al. 2023) has **135 galaxies at
  z=4–10 but direct-method (auroral-line) metallicities for only 10** — the rest use strong-line
  calibrations extrapolated far from where they were derived (MZR-E06, MZR-D03). Slope, zero point,
  and intrinsic scatter at z>6 remain "selection- and calibration-sensitive" (MZR-E06, MZR-U01).
- **Aperture / co-spatiality.** Central-fiber metallicities and total (aperture-corrected) SFRs are
  not co-spatial; the prior in-lane SDSS study (`mzr_draft.tex`, `mzr_results.json`) shows a naive
  FMR residual test flips sign (r=+0.11) from this mismatch alone. Mass and metallicity apertures
  must be treated consistently before any cross-epoch offset is trusted.
- **Mass mismatch.** JWST z>7 samples occupy low stellar masses (~10^8 M_sun) where the local MZR
  is steepest (MZR-E01); comparing to an SDSS anchor that lives at 10^9–10^10.5 without matching in
  mass compares galaxies on different parts of a steep, non-linear relation, inflating any apparent
  offset. Controversy scoring found the disagreement is real **only after mass-control and only at
  z>7** (S 7.76→2.65; run brief), which is exactly why mass-matching is load-bearing.

Additional specifics **[not in packet — flag for human/DR]**:
- The **~+0.24 dex high** offset of SDSS-Tremonti `oh_p50` vs a Te/PP04-O3N2 scale (run brief +
  project memory `reference_metallicity_calibration_scale`) is *not* quantified in the DR packet;
  the packet gives the ≤0.7 dex Kewley & Ellison envelope and Curti 2020's lower Te normalization,
  but the exact +0.24 dex number must be re-derived in-lane (galSpecLine O3N2), not cited to the
  packet.
- **IllustrisTNG** as the specific simulation comparator (run brief P2) is not in the packet; the
  packet's simulation anchors are Garcia et al. (2024) and Hirschmann et al. (2023). Treat TNG as a
  local asset, not a packet-cited claim.

---

## 4. The non-circular framing

State the question so the analysis cannot assume its own answer:

> **Once SDSS and JWST z>7 galaxies are placed on one common abundance scale and matched in stellar
> mass, does a z>7 MZR offset survive — and is that residual offset larger than the calibration +
> aperture systematic budget (up to ~0.7 dex scale, up to ~1 dex for z=0 calibrations applied at
> high-z)?**

Why this is non-circular:
- It **does not presuppose** the offset is physical (Langeroodi's ~0.9 dex) or an artifact — both
  are admissible outcomes. If the offset vanishes on a matched scale, *that null is the result*
  (run brief). If it survives above the systematic floor, that is positive evidence for real early
  metal deficiency.
- It **reconciles calibration first** (make-or-break in the run brief): SDSS-Tremonti and JWST are
  forced onto one scale *before* any evolution is claimed, defeating the Kewley & Ellison / Hirschmann
  confounds up front.
- It **controls mass** before comparing, defeating the steep-slope mismatch that the controversy
  score identified as the thing that makes the disagreement real.
- The **decision criterion is pre-committed and quantitative**: the surviving offset is only called
  physical if it exceeds the independently-estimated systematic envelope — a falsifiable bar, not a
  narrative.

**Referee-facing honesty:** small-N (11–135 galaxies, few auroral), lensing selection, and the
strong-line extrapolation mean even a surviving offset is a *constraint*, not a precision MZR
(MZR-U01). The paper's claim ceiling is "an offset of size X survives matched-scale mass-matched
comparison, above/below the Y-dex systematic floor," never "the z>7 MZR is Z."

---

### Source ledger (all from DR packet; 19/19 identity-verified)
Tremonti+2004 (MZR-E01/N01) · Kewley & Ellison 2008 (MZR-E02/N02) · Mannucci+2010 (MZR-E03/N03/D01) ·
Curti+2020 (MZR-E02/D03) · Sanders+2021 (MZR-E05/N04/D01/D02) · Langeroodi+2023 (MZR-E06/N05/D02) ·
Nakajima+2023 (MZR-E06/D03) · Hirschmann+2023 (MZR-D03) · Curti+2024 JADES (MZR-E06/N06/D01/D02) ·
Garcia+2024 (MZR-D01) · Finlator & Davé 2008 (MZR-D04). In-lane priors: mzr_draft.tex, mzr_results.json.
