# AutoWiki Surveys Program — multi-wavelength band

## Reader persona
An astronomer using a broad-wavelength facility (UV+optical+NIR for HST; optical+NIR for
Euclid; optical+IR for Rubin) for panchromatic photometry or galaxy SED fitting.

## Priorities
1. `wavelength_range` MUST cite the full range AND break it into sub-ranges by instrument
   or channel (e.g. for HST: "0.12–2.5 μm: ACS 0.2–1.1 μm, WFC3 0.2–1.7 μm, STIS UV").
2. `sky_coverage_deg2`: for HST, coverage is per-program and not a single number; describe
   the flagship survey coverage (e.g. HFF: 6 cluster fields; CANDELS: ~800 arcmin²).
3. For Euclid (multi: optical VIS + NIR NISP), cite Q1/DR coverage at the cited DR, not
   the 15,000 deg² final survey goal.
4. `flagship_programs` MUST name cross-wavelength recognized programs: for HST — CANDELS,
   HFF, 3D-HST, COSMOS-HST; for Euclid — Q1, Q2; for Rubin/LSST — LSST main survey, DDFs.
5. If the facility is both an imager and spectrograph, distinguish imaging vs spectroscopic
   wavelength ranges explicitly.

## Hard rules
- "Multi" band means the facility genuinely spans ≥2 non-contiguous wavelength regimes.
  Do not use multi for a survey that spans 0.4–1.0 μm (that is optical).
- For future surveys (Roman, Rubin), `status` must match reality (Roman: planned 2027;
  Rubin: commissioning 2026).
- `redshift_range` for photometric surveys: state the photo-z calibration range, not the
  theoretical detection limit.

## Banned moves
- Listing HST as "all-sky" — it is a pointing facility with discrete program footprints.
- Marketing voice ("the Swiss army knife of space telescopes").
- Citing planned capabilities as current.
