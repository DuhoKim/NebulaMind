# Production-estimator receipt — Longo-amplitude test (FILLED; supersedes prior version)

Yui, 2026-08-12. Synthetics only; the torch install (authorized by Duho) covered software
only — no sky data, catalogue, or astronomical download was touched.

## Feasibility verdict, first

**Measured primary retention: central 96.44%, one-sided lower 95% bound 96.15%**
(n=12,000 held-out synthetics). Kun's freeze arithmetic uses the LOWER BOUND: at 0.9615,
N_accepted ≥ 100,000 needs a parent of only ≈104,000 spirals — **this route is feasible on
retention**, pending the blocked DR10.1 parent count. **No S/N inversion**: retention RISES
with S/N (89.1% at S/N 2–5 → 99.1% → 99.7% → 99.4%), and sign accuracy of accepted objects
is 100% in every bin — acceptances are detections, not noise excursions. The secondary
tracer's pathology does not appear. Caveat that must survive into the prereg: these are
synthetic S/N bins; the DR10.1-south r<17.7 S/N distribution must be mapped onto them
before the yield multiplication, and real-image characteristics (PSF, blends, artifacts)
are not simulated here.

## Filled freeze items (machine record: prereg/train_results.json; log: train_log.txt)

- Stack: isolated venv `prereg/venv_torch` — torch 2.8.0, numpy 1.26.4, ~439 MB, MPS train
  / single-thread CPU eval. Training 10.6 min.
- Training set: 20,000 images, master seed `LONGO-AMPLITUDE-FREEZE-M1`, per-image seeds
  SHA-256(M‖i); regenerable byte-exactly (manifests in receipt_results.json).
- Architecture: Appendix A shared-trunk ResNet-18-class, χ_net=(f(x)−f(mirror(x)))/2,
  index-reversal mirror only.
- Weights FROZEN: file `weights_frozen.pt` sha256 `83008c1cbdae511a…`; canonical
  serialization sha256 `1075a4d91c295d7f…`. Never touched after sky data, per policy.
- τ = 4.4006456017494235 — 99.5th pct of |χ_net| on 8,000 frozen nulls, calibrated before
  any retention measurement.
- Receipts on the production raster (128×128 float32): R1 mirror∘mirror byte-exact 200/200;
  R2 antisymmetry bit-exact 200/200; R3 signed zero `0x0` vs `0x80000000`, value-equal,
  ordered comparison in the acceptance path.

Retention by peak S/N: 2–5: 89.11% (n=3452) · 5–10: 99.07% (n=2594) · 10–20: 99.69%
(n=2592) · 20–50: 99.43% (n=3362). All with 100% sign accuracy of accepted.

Nothing published, accepted, or run against sky. Kun gates this receipt.
