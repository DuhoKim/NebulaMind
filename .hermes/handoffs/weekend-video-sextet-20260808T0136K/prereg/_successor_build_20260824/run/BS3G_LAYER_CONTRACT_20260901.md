# BS-3g SUCCESSOR-LAYER CONTRACT — 2026-09-01 05:50 KST (Hwao's judgment; codex builds)

Grounded in the frozen bytes read this morning: BS-3g blocks BS-6; its receipt
may be emitted ONLY through the successor layer's `receipt_strict()` reading a
pinned `SLOT_SCHEMA['BS-3g']` of EXACTLY twenty fields (v9 is frozen and cannot
carry the entry; a `v9.receipt()` emission is a protocol deviation that VOIDS
the run); the sweep's run-time calibration is V3-pred's HC-1H measurement
carried by quotation at freeze (a_hat family at V3-pred F-5, the N = 49,211
sealed mask).

## Build 1 — `run/receipt_strict.py`
- `SLOT_SCHEMA_SUCCESSOR = {"BS-3g": (…the twenty, verbatim order…)}`:
  mask_sha256 · calibration_sha256 · perturbation_manifest_sha256 ·
  kernel_sha256 · estimator_sha256 · verifier_sha256 · mapping_id · gamma_hat ·
  sigma_gamma · gamma_bound · invariance_outcome · n_perturbations · n_draws ·
  draw_generator_id · draw_master_seed · draw_verdict_digest ·
  baseline_verdict · delta_gamma_max · counterfactual_path_sha256 ·
  replay_harness_sha256
- `receipt_strict(slot, fields)`: exactness like v9's `receipt()` (missing,
  extra, empty → refuse with exact codes), slots outside the successor schema
  refused (this layer carries ONLY what v9 cannot), the envelope canonical-JSON
  digested. Mirror v9's refusal discipline; quote the frozen twenty-field
  sentence in the docstring.
- Fixtures: exact-set acceptance; each of missing/extra/empty refused; a
  v9-slot name refused here; digest determinism.

## Build 2 — `run/bs3g_sweep_runner.py` (the runner the architecture ruling made owner)
- Owns the 99×51 verdict matrix + the HELD reduction (within-draw comparison to
  the draw's own γ=0 cell; worst case over draws) — MappingA stays a one-draw
  primitive. Grid exactly as the rehearsal: γ_j = (j−25)·Γ/25, Γ = 0.25,
  j₀ exactly zero, n_perm = 200 production.
- INPUTS (the run-time calibration artifacts, materialized and digested):
  locate the predecessor mask + calibration from the acquire/ receipts
  (`acquire/positions_receipts.json`, v9-pinned) and the V3-pred quotation
  values in the frozen §-text; construct the REAL mask (v9.FixtureMask over the
  real N = 49,211 positions/signs if the acquire artifacts carry them — READ
  what acquire/ actually holds first and build from what exists; if the full
  mask cannot be constructed from on-disk artifacts, STOP and report BLOCKED
  with what is missing, never synthesize) and the real calibration record
  (a_hat/a_lb/per-bin from the frozen quotation, schema-matching gcp._CAL).
- Verdict-category law from the rehearsal: adjudicated verdicts compare;
  INCONCLUSIVE-BY-CALIBRATION cells are the admissibility boundary, never
  flips; any other refusal FAILS the run(ner) loudly. The γ=0 baseline must be
  adjudicated in every draw.
- OUTPUT: the twenty-field receipt THROUGH `receipt_strict("BS-3g", …)` —
  every sha real (mask/calibration/kernel/estimator/verifier/counterfactual-
  path/replay-harness from disk; mapping_id the confirmed literal; gamma_bound
  0.25; n_perturbations 51; n_draws 99; draw_generator_id
  numpy-1.26.4-PCG64-default_rng; draw_master_seed 20260830;
  draw_verdict_digest = sha over the canonical matrix; baseline_verdict;
  delta_gamma_max = the largest |γ| that stayed adjudicated; gamma_hat/
  sigma_gamma — READ the frozen text for what these mean pre-measurement (γ̂ is
  unmeasured and unauthorized: if the schema demands values, the frozen text
  must say what goes there — find it and follow it exactly; if it is silent,
  STOP and report BLOCKED rather than invent).
- DO NOT emit the receipt into any store yet — write it as
  `run/BS3G_RECEIPT_CANDIDATE.json` + a full run report; emission into the
  live chain is a separate later step after the ladder.

Fixtures for the runner: grid exactness (j₀ zero, endpoints), category law,
receipt-through-strict only, matrix digest determinism on a fixed draw subset.
Stay in run/; no imagery, no BS-6, nothing live-store-touching.
