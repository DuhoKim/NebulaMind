GPT1_TJCENSUS_COMPLETE total_junction_segments=359607 bricks_with_at_least_one_junction=60308 area_fraction=2.0614381359289613e-05

# DR10 South working-set T-junction census — brick geometry only

## Headline

- Total T-junction boundary segments in the working set: **359,607**.
- Working-set bricks with at least one T-junction on their boundary: **60,308** of 60,308.
- Fraction of summed working-brick `AREA` inside the round-5 tested offset band: **2.0614381359289613e-05** (20.614381359 ppm).

“Segment” is counted as one per-working-brick boundary incidence at a unique three-cell meet. The total above is therefore the sum of the per-brick `tjunction_boundary_segment_count` column. There are **132,108 unique T-junction events** having at least one working-set brick among their three incident cells; this separate number is reported to prevent incidence/event ambiguity.

## Geometry and band definition

A T-junction is detected only where two available contiguous bricks in one declination row share an RA boundary, that boundary is not a boundary of the adjacent 0.25-degree row, and it lies strictly inside an available brick in that adjacent row. Thus exactly three sidecar cells meet. Coincident boundaries are excluded as four-cell crossings.

The band is taken directly from the SHA-pinned round-5 fixture ladder in `boundary_fixtures/make_boundary_fixtures_round5.py:176-186` and its contract at `boundary_fixtures/make_boundary_fixtures_round5.py:613-617`: requested east/north offsets include -10, -0.25, 0, +0.25, and +1 pixels. The area calculation uses their axis-aligned envelope, **[-10,+1] pixels on each axis**, at the fixture pixel scale **0.262 arcsec/pixel** (`boundary_fixtures/make_boundary_fixtures.py:24`). Each local tangent-plane band rectangle is clipped to each incident working brick; clipped areas are summed and divided by the FITS `AREA` sum.

- Tested-band area in working bricks: `0.077151439871071259` deg^2.
- Summed working-brick FITS `AREA`: `3742.6027260480428` deg^2.
- Ratio: `2.0614381359289613e-05`.

## Custody and scope ceiling

The geometry sidecar was located through `_tori_transfer_20260819/execution_package/SIDECAR_CUSTODY_20260819.md:7-13` and rehashed before FITS open. Observed SHA-256: `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`. It matches the custody record and the survey-published digest quoted there. The working-set CSV has 60,308 rows, 60,308 unique brick names, 60,308 unique brick IDs, and every name/ID pair matches the FITS geometry table.

**Object-level touching counts are NOT derivable: parent-object positions were deleted by design.** No attempt was made to re-derive or re-fetch them. This brick-level census is the manifest-gate answer's ceiling, not an object count. The round-5 gate itself left the real-parent touching question to the manifest stage (`KUN_ROUND5_TJUNCTION_GATE_20260817.md:194-204`); this result answers only the geometry-level portion now possible under the deletion rule.

No network operation, real image read, object-position read, object reconstruction, or object count was performed.

## Receipts

- `compute_tjunction_census.py` — executable census and validation logic.
- `working_brick_tjunction_census.csv` — one row per working-set brick.
- `working_set_tjunction_events.csv` — one row per unique selected three-cell meet.
- `tjunction_census_summary.json` — machine-readable definitions, counts, areas, input hashes, and limits.
- `OUTPUT_SHA256.json` — output inventory hashes.
