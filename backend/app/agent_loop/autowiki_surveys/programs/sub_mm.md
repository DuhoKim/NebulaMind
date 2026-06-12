# AutoWiki Surveys Program — sub-mm / mm band

## Reader persona
A submillimeter/mm observer selecting a facility for cold-gas science, dust continuum,
CMB, or molecular-line surveys at 60 GHz–1 THz.

## Priorities
1. `wavelength_range` MUST cite both GHz/THz range AND the canonical band label (Band 3–10 for ALMA,
   220/150/90 GHz for SPT/ACT/CMB-S4).
2. Angular resolution AND primary beam size are critical for ALMA vs single-dish distinction.
3. `current_data_release` for ALMA: cite the Cycle number AND the ALMA Science Archive data as of
   that cycle (e.g. "Cycle 11 (2024–2025); all data public after 12-month proprietary period").
4. For CMB experiments (ACT, SPT, CMB-S4), `current_data_release` MUST include
   the map/catalog release (e.g. "ACT DR6, 2023 — CMB lensing + temperature maps").
5. Sensitivity: state map depth (μK·arcmin for CMB, mJy/beam for ALMA continuum).

## Hard rules
- Distinguish interferometric (ALMA, NOEMA) from single-dish (SPT, ACT, JCMT) clearly.
- For non-operational future surveys (CMB-S4, ngVLA), `status` must be "planned" or
  "under_construction"; do not list non-existent DRs.
- SKA and ngVLA: construction milestones ≠ data releases.

## Banned moves
- Calling ALMA a "survey" without qualifying which ALMA survey/program is meant.
- Marketing voice ("unprecedented sensitivity").
- Celsius-based units for CMB temperatures.
