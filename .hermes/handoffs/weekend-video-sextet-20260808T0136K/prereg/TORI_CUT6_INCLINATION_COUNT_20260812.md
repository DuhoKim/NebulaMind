# Cut 6 inclination count — fixed-range aggregate receipt

**Status: COMPLETE FIXED-RANGE LOWER BOUND.**

## Scope and interpretation

- This sibling receipt appends one catalogue-native inclination cut after Cut 5 and does not modify the accepted Cut-5 receipt.
- Frozen predicate: `POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551`.
- This is `e^2 < 9/49`, specified by Lana as equivalent to `b/a > 0.4` under `b/a = (1 - |e|)/(1 + |e|)`.
- Objects with `e >= 1` fail this threshold directly; no separate assumed inclination fraction is applied.
- Frozen range: `BRICKID 1…121000`, the same frozen coverage as the Cut 5 certificate. This does not reopen or extend the stopped sweep.
- Coverage: `121000/662174 = 18.273143%` of the documented BRICKID keyspace, not sky area.
- Landed contiguous range in this receipt: `BRICKID 1…121000` across `13/13` blocks.
- Every total is a **LOWER BOUND** over only the named keyspace. No density, keyspace, or sky-area extrapolation is performed.
- Cut 6 / Cut 5 percentages below are measured same-block catalogue survival ratios, not external spiral, inclination, or Yui-retention assumptions.

## Running totals

| Branch | Cut 5 parent LOWER BOUND | Cut 6 inclination LOWER BOUND | Measured Cut 6/Cut 5 |
|---|---:|---:|---:|
| raw `mag_r` | 185,345 | 154,420 | 83.314899% |
| dered `dered_mag_r` | 208,407 | 171,737 | 82.404622% |

## Per-block aggregates

| BRICKID block | Elapsed seconds | Cut 5 raw | Cut 6 raw | Raw survival | Cut 5 dered | Cut 6 dered | Dered survival |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1…1000 | 114.0 | 2,111 | 1,861 | 88.157271% | 3,002 | 2,583 | 86.042638% |
| 1001…11000 | 876.0 | 20,579 | 17,145 | 83.313086% | 29,096 | 23,881 | 82.076574% |
| 11001…21000 | 782.0 | 15,232 | 12,549 | 82.385767% | 17,708 | 14,339 | 80.974701% |
| 21001…31000 | 599.0 | 13,253 | 11,012 | 83.090621% | 14,696 | 12,051 | 82.001905% |
| 31001…41000 | 599.0 | 15,130 | 12,574 | 83.106411% | 16,379 | 13,483 | 82.318823% |
| 41001…51000 | 521.0 | 14,889 | 12,340 | 82.879979% | 16,170 | 13,267 | 82.047001% |
| 51001…61000 | 537.0 | 15,192 | 12,677 | 83.445234% | 16,373 | 13,512 | 82.526110% |
| 61001…71000 | 537.0 | 16,227 | 13,507 | 83.237814% | 17,317 | 14,267 | 82.387250% |
| 71001…81000 | 506.0 | 14,536 | 12,137 | 83.496147% | 15,451 | 12,801 | 82.849007% |
| 81001…91000 | 521.0 | 13,991 | 11,694 | 83.582303% | 14,908 | 12,362 | 82.921921% |
| 91001…101000 | 521.0 | 14,262 | 11,966 | 83.901276% | 15,012 | 12,488 | 83.186784% |
| 101001…111000 | 553.0 | 14,512 | 12,122 | 83.530871% | 15,458 | 12,817 | 82.914995% |
| 111001…121000 | 615.0 | 15,431 | 12,836 | 83.183203% | 16,837 | 13,886 | 82.473125% |

## Boundary and custody

- server-side aggregate rows returned: one per landed block
- sample rows exported: **0**
- positions exported: **0**
- images requested: **0**
- chirality/handedness computed: **0**
- sky statistics computed: **0**
- trigonometric or axis-relative terms: **0**
- bulk downloads: **0**
- publication/acceptance/commit/push: **0**

This count does not decide accepted yield. It applies only the specified catalogue inclination cut. Spiral classification, image/WCS availability, Yui retention, and user acceptance remain separate gates.

## Hash custody

- Original Cut-5 receipt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/TORI_PARENT_ROW_COUNT_20260812.md` — SHA-256 `df9357085d4cfd35320ab34346a1fb3080dc1e5ba1e3d86e2dc6231dbbf534f3`.
- Cut 6 manifest: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/cut6_fixed_000001_121000/manifest.json` — SHA-256 `b157e6c84ed91e77612caa6c0ada173324d9a42193f69777829a60354fd9fc89`.
- Independent reconstruction: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/cut6_fixed_000001_121000/FINAL_CUT6_INDEPENDENT_RECONSTRUCTION_20260812.json` — SHA-256 `74541ec868f99ef95456d7e3ed89c3101bd9ae99b71ed63b90aa33b919ce487a`. This reconstruction sums the 13 hash-matched one-row results and checks each Cut 5 block against its original result without trusting status or Markdown totals.
- Fixed-range pass finished at `2026-08-12T11:57:09Z` with reason `fixed_range_1_121000_complete`.
