# §11.4d HEAD-only size sample — 2026-08-19

SIZE_SAMPLE_COMPLETE

- manifest URLs sampled: **1,024 exactly**
- method: **HEAD only**
- HTTP 200: **1,024**
- non-200: **0 (0.000000%)**
- body bytes transferred: **0**
- AAA strata represented: **360/360**
- required minimum request-start spacing: **1.0 s**
- observed minimum request-start spacing: **1.0000550746917725 s**
- valid Content-Length observations: **1,024**
- Content-Length sum: **12,529,362,240 bytes**
- sample mean: **195771285/16 = 12,235,705.3125 bytes**
- standard error: **30,620.065000018778 bytes**

## Sampling rule

The frozen binding requires a sample “stratified across the `AAA` keyspace” but does not prescribe stratum allocation or within-stratum selection. The executed deterministic rule was: represent every AAA stratum once; allocate the remaining slots by Hamilton proportional allocation using stratum population; select uniformly without replacement inside each stratum with seed `20260819`; order requests round-robin across AAA. The plan contains 1,024 unique manifest URLs and represents all 360 AAA strata.

## Frozen §5.1.1.2 arithmetic

`approved_byte_ceiling = sample mean × required file count × 1.25`

`= (12,529,362,240 / 1,024) × 60,308 × (5 / 4)`

`= 14,758,218,319,725 / 16`

`= 922,388,644,982.8125 bytes`

An enforceable integer byte limit cannot contain a fraction of a byte, so the exact result is rounded upward, never downward:

**approved byte ceiling = 922,388,644,983 bytes**

## Receipt artifacts

- `run_size_sample.py` — executable sampling and arithmetic receipt; contains the formula and exact rational derivation.
- `size_sample_plan.json` — deterministic 1,024-URL stratified plan.
- `receipts.jsonl` — one receipt per request with `url`, `status`, `content-length`, and `last-modified`, plus method/body/pacing/TLS fields.
- `SIZE_SAMPLE_SUMMARY.json` — machine-readable statistics and ceiling.

No image GET was issued. This M1 operation does not authorize the transfer.
