# AutoWiki Surveys Program — UV band

## Reader persona
A UV astronomer selecting a mission for star-formation rates, hot star populations,
AGN variability, or circumgalactic medium absorption studies.

## Priorities
1. `wavelength_range` MUST cite nm or Å for both UV channels (NUV: 177–283 nm, FUV: 135–175 nm
   for GALEX); distinguish FUV/NUV where applicable.
2. `sky_coverage_deg2`: GALEX GR6/7 covers ~26,000 deg² in NUV (all-sky minus exclusion zone);
   cite NUV and FUV separately since FUV coverage is smaller.
3. `current_data_release` for GALEX: "GR6/7 (2012) — MAST CasJobs" is the final release.
   The mission is retired; note the archive remains fully public.
4. For future UV missions (ULTRASAT, UVEX), `status` must be "planned" or "under_construction".
5. Depth: state typical NUV/FUV AB limiting magnitudes for All-sky Survey (AIS), Medium Imaging
   Survey (MIS), and Deep Imaging Survey (DIS) separately for GALEX.

## Hard rules
- GALEX is retired (2013); do not imply ongoing observations.
- `redshift_range` for UV surveys is meaningful only for quasar absorption-line science;
  do not invent a galaxy redshift range for GALEX.
- UV wavelengths must be cited in nm or Å, not μm.

## Banned moves
- Conflating UV with optical wavelengths.
- Citing FUV and NUV combined as a single coverage figure without breakdown.
