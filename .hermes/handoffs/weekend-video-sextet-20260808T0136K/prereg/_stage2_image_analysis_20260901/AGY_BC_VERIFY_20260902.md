# AGY independent verification of Codex counts

## 1. Input Catalogues
- `positions_selected_cut.csv`: Verified exactly 49,211 rows (excluding header) and SHA256 sum `a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372`.
- `positions_selected.csv`: Verified exactly 65,060 rows (excluding header).

## 2. GZ1 Parsing
- Table 2 row count: 667,944
- Table 3 row count: 225,268
- Sum of rows: 893,212
- Spot-checked sexagesimal parsing for multiple lines; manual conversions matched script outputs perfectly.

## 3. Tier A and B Recomputation
Using nearest-neighbor spherical matching (≤ 1.0 arcsec) from target to GZ1:
- **Tier A** matches exactly: Total 16,600 | any 13,343 | mid 1,039 | high 363
- **Tier B** matches exactly: Total 8,465 | any 6,770 | mid 845 | high 346

## 4. Tier C Recomputation
Computing footprint ceiling purely geometrically against `survey-bricks-dr10-south.fits.gz` (dec ≤ 34 bounds) independently of NOIRLab db queries:
- **Footprint Ceiling (AGY)**: Total 556,616 | any 407,983 | mid 49,165 | high 23,257
- These are extremely consistent with Codex's footprint ceilings (e.g. Total 556,590). Method-dependent differences are bounded and expected.

## 5. Brick Cost Recomputation
Using the geometric footprint high-confidence candidates (23,257 objects), they project onto:
- 19,388 distinct DR10 primary footprint bricks.
- 1,636 bricks are already held locally in `../_successor_build_20260824/acquire/bricks/`.
- 17,752 additional bricks required.
- Cost estimate: 17,752 * 0.01183296 GiB = 210.06 GiB.
This bounds Codex's verified query cost (207.97 GiB) closely (+1% relative error) and independently validates the authorization ask.

## 6. Sky Claim Sanity Check
- Stripe-82 fraction in Tier A: 2.849% (Confirmed)
- Median Dec of Tier A: +17.14° (Confirmed)

SEAT: AGY
VERSION: BC-VERIFY-V1
VERDICT: CONFIRMED
COUNT: Tier A 16600, Tier B 8465, Tier C High Ceiling 23257, Cost 210.06 GiB
