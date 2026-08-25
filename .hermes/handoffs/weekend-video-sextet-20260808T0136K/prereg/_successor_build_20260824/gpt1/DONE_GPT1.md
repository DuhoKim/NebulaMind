# DONE_GPT1 — DR10.1 south sweep catalog inventory receipt

Status: COMPLETE for the core FITS sweep catalogs exposed by the portal's `10.0/` and `10.1/` listings.

## Result and scope

The portal root lists these subdirectories:

- `10.0/` and `10.1/`: core sweep FITS catalog directories; both were inventoried.
- `10.0-extra/`, `10.0-lightcurves/`, `10.1-extra/`, `10.1-lightcurves/`, and `10.1-photo-z/`: separately named ancillary product directories, not core sweep catalog directories, so they are not rows in this inventory.

The DR10.1-photometry core catalog directory is `10.1/`; `10.0/` is the prior version-labeled core directory. Per the directory listings, both core directories expose the same FITS filename set. Each also exposes a version-specific `legacysurvey_dr10_south_sweep_10.x.sha256sum` manifest; those checksum manifests are not catalog FITS files and were excluded.

Verified inventory accounting:

- `10.0/`: 1436 FITS catalog files.
- `10.1/`: 1436 FITS catalog files.
- `sweep_inventory.jsonl`: 2872 rows and 2872 unique URLs.
- The inventory exactly matches every `.fits` link in both saved listings.

The listings expose filenames but no sizes. Following the brief's polite cap, exactly 10 sequential HEAD spot-checks were made, about one second apart: 5 in each core directory. Therefore:

- `10.0/`: 5 known sizes totaling 6182763840 bytes; 1431 rows have `size_bytes: null`.
- `10.1/`: 5 known sizes totaling 6182763840 bytes; 1431 rows have `size_bytes: null`.
- Across known rows only: 12365527680 bytes.

All file URLs and filenames were enumerated. Sizes were deliberately not enumerated for the remaining 2862 rows because the listing omitted sizes and per-file HEAD requests would violate the brief's anti-hammering rule. No catalog file body was fetched.

## Commands and captured output

### Listing-only fetch

```text
$ python3 _tmp_fetch_listings.py
200 706 https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/ -> _tmp_listing_root.html
200 112504 https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/ -> _tmp_listing_10.0.html
200 112504 https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.1/ -> _tmp_listing_10.1.html
```

The helper used sequential `urllib.request` GETs with a descriptive user agent and a 1.05-second delay between listing requests.

### Parse listings, perform capped HEAD spot-check, and write JSONL

```text
$ python3 _tmp_build_inventory.py
HEAD 01/10 status=200 size_bytes=1865471040 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/sweep-000m005-005p000.fits
HEAD 02/10 status=200 size_bytes=1740055680 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/sweep-075m035-080m030.fits
HEAD 03/10 status=200 size_bytes=1060649280 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/sweep-175p015-180p020.fits
HEAD 04/10 status=200 size_bytes=819460800 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/sweep-275m070-280m065.fits
HEAD 05/10 status=200 size_bytes=697127040 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/sweep-355p030-360p035.fits
HEAD 06/10 status=200 size_bytes=1865471040 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.1/sweep-000m005-005p000.fits
HEAD 07/10 status=200 size_bytes=1740055680 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.1/sweep-075m035-080m030.fits
HEAD 08/10 status=200 size_bytes=1060649280 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.1/sweep-175p015-180p020.fits
HEAD 09/10 status=200 size_bytes=819460800 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.1/sweep-275m070-280m065.fits
HEAD 10/10 status=200 size_bytes=697127040 url=https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.1/sweep-355p030-360p035.fits
inventory_written=sweep_inventory.jsonl
listing_file_count[10.0]=1436
listing_file_count[10.1]=1436
listing_filename_sets_equal=True
known_size_rows=10
```

### Independent JSONL/listing cross-check, line count, and checksum

```text
$ python3 _tmp_verify_inventory.py
json_rows=2872
unique_urls=2872
unique_version_filename_pairs=2872
schema_valid=True
file_count[10.0]=1436
known_size_rows[10.0]=5
null_size_rows[10.0]=1431
known_size_total_bytes[10.0]=6182763840
file_count[10.1]=1436
known_size_rows[10.1]=5
null_size_rows[10.1]=1431
known_size_total_bytes[10.1]=6182763840
known_size_total_bytes[all]=12365527680
filename_sets_equal=True
exact_listing_match[10.0]=True
exact_listing_match[10.1]=True
root_subdirectories=10.0-extra/,10.0-lightcurves/,10.0/,10.1-extra/,10.1-lightcurves/,10.1-photo-z/,10.1/
core_version_directories=10.0/,10.1/
$ wc -l sweep_inventory.jsonl
    2872 sweep_inventory.jsonl
$ shasum -a 256 sweep_inventory.jsonl
2df3a22065344a3378e069b022d316f39164ddc908f73d0fb4cfcf40323e0550  sweep_inventory.jsonl
```

An earlier inline `python3 -c` form of the cross-check stopped with a Python `SyntaxError` before changing any file; the successful standalone verification command and its complete output are shown above.

### Temporary-file cleanup

```text
$ rm -f _tmp_fetch_listings.py _tmp_build_inventory.py _tmp_verify_inventory.py _tmp_listing_root.html _tmp_listing_10.0.html _tmp_listing_10.1.html
$ printf '%s\n' 'temporary listing and helper files removed'
temporary listing and helper files removed
```

## Final checksum

```text
2df3a22065344a3378e069b022d316f39164ddc908f73d0fb4cfcf40323e0550  sweep_inventory.jsonl
```
