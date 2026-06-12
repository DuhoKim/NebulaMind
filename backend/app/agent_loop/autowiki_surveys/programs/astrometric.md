# AutoWiki Surveys Program — astrometric band

## Reader persona
An astronomer using astrometry, parallax, proper motions, or photometry for Galactic
structure, stellar kinematics, or calibration reference frames.

## Priorities
1. `wavelength_range`: Gaia covers ~330–1050 nm (G-band) with RP/BP strips and RVS at
   845–872 nm. Cite the full range AND the RVS spectroscopic range separately.
2. `sky_coverage_deg2`: Gaia is all-sky (~41,253 deg²); note the Galactic-plane density
   limits on completeness (G<~19–20 mag depending on crowding).
3. `current_data_release` for Gaia MUST include: DR number (DR3), release date (June 2022),
   source count (~1.46 billion), and reference the planned DR4 timeline (~2026).
4. `flagship_programs`: Gaia has no traditional sub-programs; name the key data products
   (5-parameter astrometry, radial velocities, astrophysical parameters, variability, NSS).
5. Proper-motion precision (μas/yr at G=15) and parallax precision are critical planner fields.

## Hard rules
- Gaia is an ESA mission; do not cite NASA/NOAO as operator.
- DR3 is the current public release as of 2026; do not anticipate DR4 as "available".
- `instruments_json` must name the actual focal-plane instruments (Astrometric Field, BP/RP
  photometers, RVS spectrometer, Sky Mapper) not just "telescopes".

## Banned moves
- Conflating photometric and astrometric precision (different error regimes).
- Implying Gaia measures redshifts (it doesn't; it measures radial velocities for bright stars).
