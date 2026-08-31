# CODEX BS-3g successor-layer build — 2026-09-01

Built `run/receipt_strict.py` and `run/bs3g_sweep_runner.py` from the frozen
V134 and layer-contract bytes. No receipt candidate or store entry was emitted;
the production 99×51 sweep is disabled in this build round.

## Verification

- `python3 run/receipt_strict.py`: **6/6 PASS** — exact-set acceptance,
  RS03 missing, RS04 extra, RS02 empty, RS01 v9-slot refusal, deterministic
  digest.
- `python3 run/bs3g_sweep_runner.py --selfcheck`: **8/8 fixture PASS**, then
  correctly **BLOCKED** before the requested 2-draw × 5-gamma real smoke.
- Total fixtures: **14/14 PASS**.

## Exact blockers

- **BLK01 — real sealed mask cannot be constructed.**
  `acquire/positions_receipts.json` authenticates the 65,060-row acquisition
  and chunk/query digests. `acquire/positions_selected_cut.csv` contains 49,211
  cut positions. Neither carries accepted signs, sealed calibration
  boundaries, or the BS-2f `mask_digest`; those are required for the real
  v9 mask binding.
- **BLK02 — real calibration is absent.** Frozen V134 quotes the inherited
  estimator and validity semantics — `a = (raw − ε)/(1 − 2ε)`, the shared-ε
  covariance, scalar/profile law, and per-bin lower-bound rule — but supplies
  no measured BS-8f `a_hat`, `sigma_a`, `a_lb`, `a_b`, `sigma_ab`, `a_lb_b`,
  or `cov_a` record. The on-disk `_CAL` is explicitly fixture-only.
- **BLK03 — the receipt's gradient fields have no authorized value.** The
  frozen text requires “`gamma_hat`, `sigma_gamma` — finite IEEE-754 doubles,
  decimal, the estimated gradient and its standard error,” while also stating:
  **“γ̂ remains unmeasured, and no measurement of it is authorised here.”** It
  specifies no placeholder, so zero, null, NaN, or fixture values would be an
  invention.

The missing artifacts must be supplied as frozen/authenticated run-time inputs,
and the gamma-field contradiction must be resolved by authorized frozen text,
before a real smoke or receipt candidate can exist.

SEAT: CODEX
VERSION: BS3G-V1
VERDICT: BLOCKED
COUNT: 14
