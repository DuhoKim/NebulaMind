# Geometry-sidecar route-B custody — 2026-08-19

SIDECAR_CUSTODY_COMPLETE

The retained adapter-lane custody record satisfies every field mandated by frozen binding §4.3: source URL, survey-published source digest, size, and local SHA-256. No network operation was needed or performed for M5.

## Retained custody record and local object

- custody record: `_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/STATIC_PRODUCT_CUSTODY.json`
  - SHA-256: `5e969bf623ec07a0366355fb5f723b31e4365fd7e03ccc07e1addd32f379881a`
- local object: `_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/static/survey-bricks-dr10-south.fits.gz`
  - byte size: `104480980`
  - recomputed local SHA-256: `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`

## §4.3 fields, quoted exactly from the retained record

> `"source_url": "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/survey-bricks-dr10-south.fits.gz"`
>
> `"official_checksum_index_url": "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/legacysurvey_dr10_south.sha256sum"`
>
> `"published_checksum_line": "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a  survey-bricks-dr10-south.fits.gz"`
>
> `"download_sha256": "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a"`
>
> `"published_checksum_matches": true`
>
> `"content_length_bytes": 104480980`
>
> `"download_bytes": 104480980`
>
> `"content_length_matches": true`
>
> `"last_modified": "Fri, 15 Dec 2023 19:26:48 GMT"`

The recomputed local object hash equals both the quoted survey-published digest and quoted download SHA-256. Missing §4.3 fields: **none**.

This is a custody packaging receipt, not a new retrieval, manifest seal, or transfer authorization.
