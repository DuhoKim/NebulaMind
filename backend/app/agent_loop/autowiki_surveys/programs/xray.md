# AutoWiki Surveys Program — X-ray band

## Reader persona
An X-ray astronomer or high-energy astrophysicist selecting a survey for AGN demographics,
galaxy clusters, X-ray binaries, or transient follow-up.

## Priorities
1. `wavelength_range` MUST cite keV range (e.g. "0.5–7 keV" for Chandra soft/hard bands).
   Include the equivalent Å range if useful for spectroscopy context.
2. `sky_coverage_deg2`: X-ray surveys range from pencil-beam (CDF-S 0.13 deg²) to all-sky
   (ROSAT, eROSITA). State flux limit AND coverage together for usability.
3. `current_data_release`: for Chandra, cite the source catalog version (CSC 2.1 as of 2023);
   for XMM cite 4XMM-DRxx; for eROSITA-DE cite eRASS1; for ROSAT cite 2RXS (2016).
4. `flagship_programs` MUST name the actual survey programs (e.g. CXO CSC, XMM-COSMOS,
   XMM-XXL, eROSITA All-Sky Survey, ROSAT All-Sky Survey).
5. Sensitivity: state flux limit in erg/cm²/s (0.5–2 keV soft or 2–10 keV hard).

## Hard rules
- Distinguish the telescope from its serendipitous survey products vs pointed surveys.
- eROSITA: cite only the eROSITA-DE (western hemisphere) half that is publicly available;
  eROSITA-RU (eastern half) is under Russian embargo.
- Angular resolution (arcsec HEW) is critical context for source confusion.

## Banned moves
- Citing optical magnitudes for X-ray sources without context.
- Conflating eROSITA with ROSAT (they are separate missions with different epochs).
- Using "counts" as a sensitivity unit without exposure time context.
