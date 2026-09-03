# DR10-south sweep cost note — 2026-09-03

Using the pinned GZ1 positions and exact DR10-south assigned-brick rectangle rule, plus all 65,060 flagship-parent positions, the published DR10-south 10.0 sweep subset totals **854.547 GiB** across **710** files. Sizes are HTTP HEAD `Content-Length` values paced at least 0.5 s apart; no FITS payload was downloaded. At the observed brick rate, the union would imply 1.29 h at 550 files/h with two workers, but the relevant large-file estimate is **61.04 h** at 14 GiB/h aggregate. The current volume has 13,019.6 GiB free (`df` equivalent). NERSC publishes SHA-256 hashes in [`legacysurvey_dr10_south_sweep_10.0.sha256sum`](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/legacysurvey_dr10_south_sweep_10.0.sha256sum); each selected hash and HEAD size is recorded. One geometric GZ1 box (`sweep-230p035-235p040.fits`) is absent from the published index and is recorded as such in the manifest.

| Footprint | Files | Total GiB | Hours @ 550 files/h | Hours @ 14 GiB/h |
|---|---:|---:|---:|---:|
| (a) GZ1 ∩ DR10-south | 352 | 405.117 | 0.64 | 28.94 |
| (b) flagship parent | 565 | 694.415 | 1.03 | 49.60 |
| (a) ∪ (b) | 710 | 854.547 | 1.29 | 61.04 |

TOTAL > 200 GiB → STOP for Duho
