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
- Optional top-level `retire_labels: [..]` (added in the T2 enrichment pass,
  2026-06-12): labels of previously loaded bootstrap rows that the enriched
  rows replace. The loader must `DELETE FROM survey_data_releases WHERE
  survey_id = :sid AND label = ANY(:retire_labels)` **before** upserting,
  since bootstrap rows are already live in the DB and upsert alone would
  strand them (e.g. chandra "Cycle 27" → "CSC 2.0"/"CSC 2.1").
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
- Load **after** the datasets backfill: 7 of the 21 files target dataset slugs
  created by `survey_datasets_backfill.json` (des-dr2, kids-dr5, hsc-pdr3,
  erosita-erass1, gama-dr4, cosmos2020-classic, 5xmm-dr15).

## `survey_datasets_backfill.json` → table `survey_datasets`

- `new`: 26 rows, upsert by `slug` (resolve `survey_id` from `survey_slug`).
  Row 26 (`5xmm-dr15`, added in T2 batch 2) carries the 5XMM-DR15 catalogue
  released by ESA on 2026-06-09.
- `updates`: 23 patches `{slug, bibcode, doi}` for existing rows — patch only
  these two columns, only when currently NULL (T2 batch 2 filled the
  `wise-allwise` DOI 10.26131/IRSA1 in its existing patch entry).

## Gaps / known issues (for v1.1 or T2 pass)

- No catalog fields yet for: euclid-q1 (ESA datamodel column names not
  confidently transcribable without the Q1 docs), rubin-dp1, all jwst-* and
  alma-* datasets, unions-dr1, euclid-edf, hst-* (imaging products — column
  tables less meaningful). UI must render the honest empty state.
- KiDS DR5 / H-ATLAS DR2 / MIGHTEE release-paper bibcodes not confirmed → left
  null rather than guessed.
- 9 pre-data facilities have planned-only rows and no datasets: 4most, cmb-s4,
  elt, ngvla, pfs, roman, ska1, spherex, weave.
- T2 surveys: 11 enriched as of 2026-06-12. Batch 1: alma, hst, chandra, vla,
  2mass, galex, rosat (releases web-verified against official archive pages;
  5 catalog-field files: chandra-csc21, vla-first, 2mass-xsc, galex-gr67,
  rosat-2rxs). Batch 2: planck, wise, panstarrs, xmm (releases web-verified +
  ADS-verified bibcodes; 3 catalog-field files: wise-allwise, ps1-dr2,
  5xmm-dr15). 17 remaining bootstrap-only files (act, askap-emu, cdf-n,
  cdf-s, deep2, fermi-lat, h-atlas, hetdex, hipass, lofar, meerkat, spt,
  ukidss, unions, viking, vipers, zcosmos) still have a single mechanical
  release row; enrichment continues as a rolling Kun task per design doc §3.3.
- T2 batch 2 notes (2026-06-12): **5XMM-DR15 was released by ESA on
  2026-06-09** (818,656 unique sources; provenance: HEASARC XMMSSC table) —
  the xmm seed promotes it from planned to released and supersedes 4XMM-DR14;
  its reference paper is not yet on ADS, so doi/bibcode are null. The SSC site
  (xmmssc.irap.omp.eu) was returning 503 at seed time; 5xmm-dr15 catalog
  fields were transcribed from the live HEASARC parameter docs instead, and
  no 4xmm-dr13 field file was written (two generations stale). planck-pr3 is
  a `cmb_map` product — no catalog-field file (honest empty state). PS1 key
  columns span two MAST datamodel pages (ObjectThin: astrometry/flags;
  MeanObject: photometry); file-level source_url points to the umbrella
  "PS1 Database object and detection tables" page. Planck PR3/PR4 exact
  release days not stated on archive pages → release_date left null with
  year + month in summary.
- GALEX GR6/GR7 release date and HSC v3.1 / GUVcat source counts not stated
  on the official pages → left null rather than guessed.
