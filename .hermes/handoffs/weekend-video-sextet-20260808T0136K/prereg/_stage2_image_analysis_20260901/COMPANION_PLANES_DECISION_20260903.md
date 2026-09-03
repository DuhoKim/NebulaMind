# COMPANION PLANES — a gap between the signed text and the acquisitions (Hwao, 2026-09-03 13:1x KST)
For Duho, via Blanc. Plain words; digits. Nothing here starts a download; this is a decision request.

## The gap
Signed mini-prereg V10 says two things the acquisitions do not satisfy:
* §7.7: "Required maskbits and R-band inverse-variance companions are included in the manifest and
  verified to their published hashes under the same rule."
* §8.12: "Every output pixel requires valid image, maskbits, and inverse-variance coverage … any missing
  or non-finite required value yields DATA-INTEGRITY-FAIL for the study."
The Tier-C manifest (17,947 bricks) and the fetch script fetched ONLY the R-band **image** file per brick.
On disk today (counted, not estimated): `bricks_tier_c/` 17,947 files, all `-image-r`; the flagship's
`bricks/` (direction #52) 12,117 files, all `-image-r`. No maskbits, no inverse-variance, anywhere.
The seal gate that passed at 12:02 verified the image files it was told about; §7.7's companion rule was
never exercised because no companion was ever listed. The referee (agy R3, 13:02) caught it from the
renderer side: a renderer that obeys §8.12 must REFUSE on these directories as they stand.

## Sizes, measured by HEAD request on NERSC (2 real bricks), not guessed
| file per brick | bytes (2 samples) | ratio to image |
|---|---:|---:|
| image-r (already on disk) | 12,058,560 / 13,602,240 | 1.00 |
| invvar-r | 11,280,960 / 11,312,640 | ~0.90 |
| maskbits | 293,760 / 400,320 | ~0.03 |

| acquisition | bricks | on disk now | companions to add (est.) | time at the observed ~1,000 files/h |
|---|---:|---:|---:|---:|
| Tier-C (this study) | 17,947 | 222 GiB | invvar ~200 GiB + maskbits ~6 GiB ≈ **206 GiB** | ~36 h for 35,894 files (invvar dominates; ~18 h with the same 4 workers if NERSC allows) |
| Flagship Tier-A (#52) | 12,117 | 143 GiB | invvar ~129 GiB + maskbits ~4 GiB ≈ **133 GiB** | ~24 h |

Disk: the Studio holds both today; +339 GiB total needs checking against free space before "go".

## What it blocks
* Tier-C: BS-4 step (b) and every real cutout — the study cannot open a pixel without companions unless
  §8.12 is amended (which would weaken integrity; not recommended).
* Flagship: V134 §2.5 acquisition and the frozen cutout planner will need the same planes; better known
  now than at BS-6.

## Your options
(a) **Authorize both companion acquisitions now**, same script family, same receipt journal discipline,
    same seal-gate re-run afterwards (~+339 GiB, ~2.5 days wall at polite pacing; Tier-C first).
(b) **Tier-C companions only now** (~+206 GiB, ~36 h; ~18 h if 4 workers); flagship companions decided
    with BS-6.
(c) **Hold** — nothing downloads; the Tier-C study stops at the completeness receipt.
Recommendation: (b), then (a)'s second half when BS-6 is in sight. Either way the Tier-C manifest gets a
v2 listing the companions, the seal gate verifies all three planes per brick, and V10 itself needs NO
amendment (its text already requires this; the acquisition was short).

## Provenance of the miss
The Tier-C acquisition GO (TIER_C_ACQUISITION_GO_20260902.md) and the ~210 GiB cost estimate counted
R-band image bricks only; §7.7 entered the mini-prereg text later the same day (V1, 14:00 KST) and the
GO was not re-read against it. Hwao's error; recorded here.
