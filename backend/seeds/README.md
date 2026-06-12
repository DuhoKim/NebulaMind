# Survey Detail Page seeds (survey_detail_page_v1.md §3)

Hand-curated by Kun, 2026-06-12. All bibcodes/DOIs verified against the ADS API
(56/56 resolved; bibcodes are ADS-canonical, DOIs auto-filled from ADS).
Release facts for Rubin DP1, SDSS DR19, DESI DR2, Gaia DR4, Euclid Q2/DR1 and
KiDS DR5 were web-verified 2026-06-12 (several supersede stale
`surveys.current_data_release` strings).

**Do not apply by hand — Tori's seed loader (Step 3) consumes these.**

## `survey_releases/{survey_slug}.json` → table `survey_data_releases`

```json
{ "survey_slug": "desi",
  "releases": [ { "label", "release_date", "release_year", "summary",
                  "n_objects", "sky_coverage_deg2", "data_volume_tb",
                  "doi", "bibcode", "url", "status" } ] }
```

- Upsert key: `(survey_id, label)`; resolve `survey_id` from `surveys.slug`.
- `status` ∈ `planned | released | superseded | final`.
- 50 files (one per survey). 22 are hand-curated (12 T1 flagships + sdss-v +
  9 T3 planned-only facilities); the remaining 28 are mechanical bootstrap rows
  derived from `surveys.current_data_release` by
  `scripts/gen_bootstrap_release_seeds.py` (T2 enrichment is a rolling follow-up).

## `catalog_fields/{dataset_slug}.json` → table `survey_catalog_fields`

```json
{ "dataset_slug": "desi-dr1-bgs", "source_url": "<official datamodel page>",
  "fields": [ { "name", "dtype", "unit", "description", "example",
                "is_key", "sort_order" } ] }
```

- Upsert key: `(dataset_id, name)`; resolve `dataset_id` from
  `survey_datasets.slug`. Apply file-level `source_url` to every row.
- Load **after** the datasets backfill: 6 of the 13 files target dataset slugs
  created by `survey_datasets_backfill.json` (des-dr2, kids-dr5, hsc-pdr3,
  erosita-erass1, gama-dr4, cosmos2020-classic).

## `survey_datasets_backfill.json` → table `survey_datasets`

- `new`: 25 rows, upsert by `slug` (resolve `survey_id` from `survey_slug`).
- `updates`: 23 patches `{slug, bibcode, doi}` for existing rows — patch only
  these two columns, only when currently NULL.

## Gaps / known issues (for v1.1 or T2 pass)

- No catalog fields yet for: euclid-q1 (ESA datamodel column names not
  confidently transcribable without the Q1 docs), rubin-dp1, all jwst-* and
  alma-* datasets, unions-dr1, euclid-edf, hst-* (imaging products — column
  tables less meaningful). UI must render the honest empty state.
- KiDS DR5 / H-ATLAS DR2 / MIGHTEE release-paper bibcodes not confirmed → left
  null rather than guessed.
- 9 pre-data facilities have planned-only rows and no datasets: 4most, cmb-s4,
  elt, ngvla, pfs, roman, ska1, spherex, weave.
- T2 surveys (28 bootstrap files) have a single mechanical release row;
  enrichment is a rolling Kun task per design doc §3.3.
