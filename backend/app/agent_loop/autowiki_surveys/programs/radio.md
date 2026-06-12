# AutoWiki Surveys Program — radio band

## Reader persona
A radio astronomer or multi-wavelength researcher selecting a facility for cm/m-wave science:
continuum imaging, HI 21-cm surveys, radio transients, or synchrotron emission studies.

## Priorities
1. `wavelength_range` MUST cite GHz or MHz with both endpoints (e.g. "1–2 GHz (L-band)").
2. `sky_coverage_deg2` MUST reflect the public footprint at the cited DR.
   State survey coverage separately from full-sky or all-sky where applicable.
3. `current_data_release` MUST contain: version/epoch label + release year + URL.
   Example: "VLASS Epoch 1–3 Quick-Look (2024) — data.nrao.edu".
4. `flagship_programs` MUST name the actual survey programs (e.g. VLASS, MGCLS, ThunderKAT,
   MIGHTEE for MeerKAT; LoTSS, LoLSS for LOFAR; EMU, POSSUM for ASKAP).
5. Resolution, sensitivity (RMS in μJy/beam), and angular resolution (arcsec) are
   high-value planner fields; include in `description` when available.

## Hard rules
- `redshift_range` is only meaningful if the survey targets spectral lines (HI, OH).
  For pure continuum, prefer `null`.
- Frequency coverage must be from the operating receiver set, not the planned future range.
- Never conflate the telescope aperture with the survey coverage.

## Banned moves
- Marketing voice ("the most sensitive radio telescope ever built").
- Citing MJy/sr units for radio — use Jy/beam or mJy/beam.
- Listing "radio" as a flagship program — name the actual survey program.
