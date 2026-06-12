# AutoWiki Surveys Program — default (fallback for any band)

## Reader persona
A working astronomer planning a proposal or paper who needs to quickly assess whether
this survey is the right tool for their science case.

## Priorities
1. `wavelength_range` MUST cite both endpoints with units (μm, nm, GHz, keV, etc.).
2. `sky_coverage_deg2` MUST reflect the public footprint at the cited DR.
3. `current_data_release` MUST contain the version string + release year + direct URL.
4. `flagship_programs` MUST list the programs an astronomer would actually cite in a paper.
5. `primary_science_goals` MUST name specific astrophysics targets, not category-level goals.

## Hard rules
- Never use vague quantities (approximately, around) before a number — cite the number or omit.
- `status` must reflect the actual operational state (operational, commissioning, planned, retired).
- DR strings must contain a version number, not just a year.

## Banned moves
- Marketing voice ("revolutionary", "unprecedented", "groundbreaking").
- Hallucinating DR strings or paper references not confirmed by a source URL.
- Citing the telescope aperture as the survey's sky coverage.
