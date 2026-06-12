# AutoWiki Surveys Program — optical band

## Reader persona
A working observational astronomer (postdoc-level) selecting a survey for galaxy
clustering at z<2, weak lensing, stellar populations, or spectroscopic redshifts.

## Priorities
1. `wavelength_range` MUST cite μm or nm with both endpoints; SDSS-style "ugriz" is
   acceptable IF the filter set is named AND effective wavelengths cited.
2. `sky_coverage_deg2` MUST be the **public footprint at the cited DR**, not the planned
   final survey area. For imaging+spectroscopic surveys, state both if they differ.
3. `current_data_release` MUST contain: DR version + release year + URL to release notes.
   Example: "DR1 (Mar 2025) — data.desi.lbl.gov".
4. `flagship_programs` MUST list the main sub-programs astronomers cite
   (e.g. BOSS / eBOSS / MaNGA for SDSS; BGS / LRG / ELG / QSO / LyA for DESI;
   Wide / Deep / UltraDeep for HSC-SSP).
5. Imaging-only surveys: state typical depth (e.g. "i~26 mag at 5σ in HSC-SSP Deep").
   Spectroscopic surveys: state wavelength resolution R and multiplexing (fibers or slits).

## Hard rules
- `redshift_range` is only meaningful for spectroscopic surveys. For imaging-only, prefer
  `null` over a guessed photometric range.
- Never use "approximately" before a numeric — give the number or omit it.
- DR strings must contain a version number, not just a year ("DR2", not "the 2024 release").

## Banned moves
- Marketing voice ("the world's most ambitious spectroscopic survey").
- Listing instruments by generic class only ("optical cameras") instead of by name
  (Mosaic-3, Mayall-DESI FPS, Hyper Suprime-Cam).
- Citing a survey's planned sky coverage as its current DR coverage.
