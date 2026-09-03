# TIER-C COMPANION PLANES — GO (Duho via Blanc, 2026-09-03 13:23 KST, verbatim "b, 4 workers")

Scope: maskbits + R-band inverse-variance (`legacysurvey-<brick>-maskbits.fits.fz`,
`legacysurvey-<brick>-invvar-r.fits.fz`) for all 17,947 bricks of `tier_c_manifest_v1.json`, ~206 GiB,
4 workers, same script family as the pinned `fetch_bricks.py` (sha 35fd6c24…, which stays untouched),
same receipt discipline (V10 §7.9 shapes: OK 7 keys / FETCH-FAILED 5 keys), one journal per plane,
published-hash verification per §7.7, destination `bricks_tier_c/` beside the image files.
Then: `tier_c_manifest_v2.json` listing the three planes; seal gate V4 re-run over all three planes.
NOT authorized: flagship (Tier-A) companions — decided with BS-6. No pixel is opened. V10 unchanged.
Recorded as human direction #59.
