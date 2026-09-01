# BRICK ACQUISITION — COMPLETE

**Finished** 2026-09-01T21:24Z (2026-09-02 06:24 KST).
**Authorization** direction #52 (Duho, 2026-09-01, option 1): a new scoped
authorization superseding the single-probe limit of ruling R-C. Scope:
**acquisition only** — no cutouts, no instrument, no χ, no handedness label.
That boundary is intact; nothing in this lane has read a pixel.

## Result

| quantity | value |
|---|---|
| bricks in the authorized closure | 12,117 |
| bricks on disk | **12,117** |
| missing | 0 |
| unexpected extra files | 0 |
| bytes on disk | **143.37 GiB** |
| SHA-256 verified against the published checksum | **12,117 (all)** |
| checksum mismatches / quarantined | **0** |
| fetch failures | **0** |
| stray partial files | 0 |

## Provenance

* Source: the ruled NERSC path (R-A, direction #31) —
  `portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/<AAA>/<brick>/legacysurvey-<brick>-image-r.fits.fz`
* Set: `required_manifest_v5.json`
  sha256 `932e8118bba6c694a64b3d2162ced00e684097a013f1036d93cf9c017158b5e5`
  — the 12,117-brick closure over the 49,211-object retained mask.
* Fetcher: `fetch_bricks.py`
  sha256 `29d3df33317ed8d1e6ce14217f957384177f7803601addb47e0cc765281927b3`
* Journal: `fetch_bricks_receipts.jsonl`, 12,119 lines — one per brick outcome
  plus the two corrections below. Each line carries brick, URL, byte count,
  published sha256, computed sha256, verdict and UTC time.
* Pacing: 4 concurrent fetchers, 0.5 s inter-brick delay, ~3.8 s/brick wall.
  Concurrency was held at 4 because NERSC publishes no rate limit for this host
  and absence of a limit is not permission.

## Two corrected receipts, disclosed

Bricks `0001m250` and `0001m252` were fetched by the pre-correction smoke probe,
when the checksum-filename pattern in the fetcher was still wrong. They were
journalled `OK-NO-PUBLISHED-SHA` — downloaded but **unverified**. After the run
finished, both were re-hashed on disk and matched against the published
`legacysurvey_dr10_south_coadd_000_<brick>.sha256sum`:

* `0001m250` — disk `15a025cf…` = published `15a025cf…` — MATCH
* `0001m252` — disk `cf284dc2…` = published `cf284dc2…` — MATCH

Corrected receipts were **appended**; the original `OK-NO-PUBLISHED-SHA` lines
remain in the journal as history and were not rewritten. The bytes on disk were
never touched. This is why the journal has 12,119 lines for 12,117 bricks.

Had that filename bug not been caught before the bulk run, all 143 GiB would
have arrived unverified.

## What is NOT done

The bricks are bytes on disk. Every downstream step remains behind its own gate:
cutout extraction, the frozen 128×128 geometry, the instrument, χ, and the
handedness label. Stage one is banked and terminal (`run/STAGE_ONE_TERMINAL_20260901.md`);
the image half is closed at the calibration wall
(`_stage2_image_analysis_20260901/STAGE2_CLOSED_20260901.md`).
