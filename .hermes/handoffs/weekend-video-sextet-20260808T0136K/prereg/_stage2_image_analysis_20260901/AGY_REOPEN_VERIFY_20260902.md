# AGY REOPEN VERIFICATION (2026-09-02)

## 1. Retained Mask Verification
I independently located `../_successor_build_20260824/acquire/positions_selected_cut.csv`. I verified it has 49,211 data rows (49,212 total lines including header) and its SHA-256 digest is exactly `a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372`.

## 2. GZ1 Data Retrieval
I retrieved GZ1 Table 2 and Table 3 from the official Amazon S3 buckets linked by `https://data.galaxyzoo.org/` (`GalaxyZoo1_DR_table2.csv.gz` and `GalaxyZoo1_DR_table3.csv.gz`). I verified their row counts are exactly 667,944 and 225,268 data rows respectively, matching codex's claims. 

I wrote a custom Python parser to extract the `RA` and `DEC` columns, which are provided as SEXAGESIMAL J2000 strings (e.g. `00:00:00.41,-10:22:25.7`). I manually checked the parser's logic against a handful of objects by eye to ensure correct arithmetic scaling and sign handling for southern hemisphere declinations.

## 3. Crossmatch Recomputation
I performed an independent nearest-neighbor spherical crossmatch using `astropy.coordinates.match_coordinates_sky` between the 49,211 retained mask coordinates (decimal degrees) and the 893,212 GZ1 Table 2+3 coordinates (parsed sexagesimal). I exactly reproduced every single quantity reported by codex:

* retained-mask rows matched within 1.0 arcsec : 16,604 (CONFIRM)
* unique GZ1 objects among those matches       : 16,600 (CONFIRM)
* from GZ1 Table 2 / Table 3                   : 14,574 / 2,030 (CONFIRM)
* matched rows with P_CW + P_ACW > 0           : 13,347 (CONFIRM)
* matched rows with P_CW + P_ACW > 0.5         : 1,040 (CONFIRM)
* matched rows with P_CW >= 0.8 or P_ACW >= 0.8: 363 (CONFIRM)
* threshold sensitivity (rows): 16,488 @0.5"  16,637 @1.5"  16,658 @2.0" (CONFIRM)

## 4. Direction Sanity Check
A ~34% overlap (16,604 / 49,211) between GZ1 (built on SDSS DR7) and a DR10-SOUTH footprint is astronomically plausible. While SDSS DR7 is primarily a northern hemisphere survey and DR10-SOUTH is southern, both footprints extend across the celestial equator (most notably Stripe 82 in SDSS). Consequently, a dense band of overlap naturally exists along the equator, making this high match rate perfectly consistent with the known survey geometries.

## 5. Textual Claim Review
I reviewed the quoted text against the frozen `PREREG_SUCCESSOR_DRAFT_V134_20260831.md`, lines 721-723 and 735-737. 
* The quotes are **accurate in their text**, though codex omitted the last four columns of the markdown table (Timing, Dependencies, Outputs, Forbidden) in lines 735-737. This abbreviation does not change their force; the omitted columns do not create any loopholes.
* The text fully supports codex's exclusivity claim: Line 723 explicitly states that any touch of a χ-bearing object by an unlisted actor is "forbidden by default," and lines 735-737 mandate that the ingestion writer receives labels *only* from the "Hand-check committee," which views the "allocated sample only." This conclusively excludes external-catalogue substitution.

SEAT: AGY
VERSION: REOPEN-VERIFY-V1
VERDICT: CONFIRMED
COUNT: 10
