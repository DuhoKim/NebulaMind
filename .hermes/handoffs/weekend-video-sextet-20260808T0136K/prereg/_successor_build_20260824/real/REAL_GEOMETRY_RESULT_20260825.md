# REAL-GEOMETRY RESULT — the successor design, measured on DR10

Hwao, 2026-08-25. Authorized by Duho this afternoon as a catalog-only data step (no images,
no χ). **In the event no fetch was needed:** both inputs were already on disk from the
predecessor's authorized work, so this used strictly less than was authorized.

## Inputs (already acquired, digests recomputed today)

| artifact | sha256 |
|---|---|
| `survey-bricks-dr10-south.fits.gz` (release brick universe + geometry) | `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a` |
| `combined_per_brick_counts.csv` (grouped TAP counts) | `4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0` |

Provenance of the counts: NOIRLab Astro Data Lab async TAP, `https://datalab.noirlab.edu/tap/async`,
tables `ls_dr10.tractor_s` / `ls_dr10.photo_z` / `ls_dr10.bricks_s`, verbatim ADQL archived in
`_tori_parent_row_count_evidence/*.adql`. Submission is CLOSED in that runner.

## Count oracle (BS-2c) on real data

- universe **366,912** bricks; **270,577** with objects; **96,335** zero rows materialized
- objects placed **832,393 / 832,393**, zero count keys outside the universe
- **count-weighted Var(cosθ) = 0.445201**, independently reproducing the scope note's frozen
  full-keyspace 0.4452
- `validate_count_table()` PASSED: `{"rows": 366912, "zero_rows": 96335, "universe": 366912,
  "total": 832393}`

## Selection (BS-2o/2s) at the frozen requirement

The vectorized greedy used here is not a second definition: its order is proven identical to
the pinned `greedy_ledger()` on 40 random cases before use. (The pinned implementation is
O(n²) in Python and will not run at 270,577 bricks — a finding to carry into the prereg.)

| | dead run | successor, real geometry |
|---|---:|---:|
| bricks | 60,308 | **6,446** |
| objects (raw) | 208,407 | **65,062** |
| Var(cos θ) | 0.0580 | **0.7547** |
| N_eq | 36,253 | **120,006** |
| image bytes | 735.9 GB | **~77 GB** |

|cos θ| over the selected set spans 0.3764 → 1.0000: the polar selection the design asked for.

## Stage P on the real geometry — the decisive number

Measured null: 20,000 permutations, **z\* = 3.0200** (normal reference 3.0902 — again
anti-conservative on real polar geometry, as the fixture family predicted).

**Successes 997 / 1000** at the frozen labelling floor a = 0.85 with A = 0.0408 injected.
Pass rule x ≥ 962. **PASS.**

**Re-run under the self-verifying gate (v4), because the first run used calibrated decisions
alone — the logic both round-6 gates called unsound.** Stage P now re-tests every
near-boundary success against an independent 20,000-permutation run and fails closed on a
single unconfirmed one. On this geometry: **77 boundary trials, 77 confirmed, 0 refuted,
verdict PASS** (629 s). The headline was not wrong; it had not been audited. It has been now.
For contrast, on a fixture sized to sit at ~50% power the same mechanism refuted 2 of 7
boundary successes and failed the stage closed — the defect is real, this geometry simply
does not exhibit it.

The dead run's power at the same floor was ~52% and no accepted subset of its footprint could
reach 95%. This footprint reaches **99.7%** with about a tenth of the download.

## What this does NOT establish

No image byte was fetched; no χ was read; nothing is frozen. This is Branch B (DR10) geometry;
Branch A (DR11) would need its own counts. The prereg's remaining gate findings still stand —
this fills the class-P inputs those findings said could not be closed by writing alone.
