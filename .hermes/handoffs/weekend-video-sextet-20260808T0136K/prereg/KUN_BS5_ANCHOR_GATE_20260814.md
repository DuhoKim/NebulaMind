# KUN_BS5_ANCHOR_GATE_20260814

Timestamp: 2026-08-14 KST

Brief: `prereg/_tmp_KUN_SIGN_ANCHOR_GATE_BRIEF.md`

Input inspected:

- `prereg/YUI_BS5_SIGN_ANCHOR_20260814.md`
- `prereg/yui_bs5_sign_anchor_20260814/`

Boundary: documentation/gate only. I did not inspect sky data, rows, positions, real images,
chirality labels, or sky statistics. I did not freeze, publish, accept, commit, push, or authorize
a real-image run. Duho owns acceptance.

## Artifact Hashes

- `YUI_BS5_SIGN_ANCHOR_20260814.md` —
  `292a5fcf3298aa05afb02a649034fe6937898c42a9df0ef55177ef17794a48de`
- `results.json` —
  `7c98eea5dbc92301b0900fa9b3ce09f1ed31c3e9751b599944008e35e91e0038`
- `pre_correction_probe_records.jsonl` —
  `cd02451070f0bbd16326439ed963dc07a5593da7b1505ef277307d4571019dc2`
- `wcs_parity.json` —
  `14deff60b3462f99ec2daae6412e9d370313990e9303a2186f4faf48242e6169`
- `attempt1_partial_probe_records.jsonl` —
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `attempt1_pre_correction_stderr.log` —
  `4753ae9d8806d56a98adff5fe9c008a512f0843faae2d95f71a58809e8cd508d`

## Verdict

**PASS_BS5_SYNTHETIC_ABSOLUTE_SIGN_ANCHOR.**

The BS-5 anchor passed in the sense it was designed to test: known synthetic counter-clockwise
spirals in the frozen East-of-North convention produced positive uncorrected primary-estimator
`chi`, and their pure pixel mirrors produced negative `chi`. The frozen convention was not flipped
to match the estimator.

What this licenses: BS-5's synthetic absolute-sign prerequisite is cleared for this preregistered
Longo-amplitude design.

What it does not license: real-image execution, sky-statistic computation, publication, freeze,
acceptance, or any claim that future real-image WCS/parity receipts will pass. The STOP rule still
binds at the next step that would touch a real galaxy.

## 1. Frozen Convention Was Not Quietly Flipped

The decisive fields in `results.json` are:

- `frozen_sign_convention`: `CCW apparent winding East-of-North => chi > 0`
- `convention_changed`: `false`
- `estimator_sign_multiplier`: `1`
- `estimator_corrected_after_precheck`: `false`
- `boundaries.convention_change`: `false`

The runner code also hard-codes:

- `ESTIMATOR_SIGN_MULTIPLIER = 1`
- `FROZEN_SIGN_CONVENTION = "CCW apparent winding East-of-North => chi > 0"`
- `apply_estimator_sign()` only accepts `+1` or `-1`, and the executed value was `+1`.

The probe records agree with the summary. I independently parsed `pre_correction_probe_records.jsonl`:

- rows: `32`
- estimator multipliers present: `{1}`
- base-sign pass: `32/32`
- estimator-sign pass: `32/32`
- rendered CCW original + CW mirror pass: `32/32`
- estimator `chi(CCW)` range: `+4.513615131378174` to `+10.054704666137695`

This is not a case where the convention was rewritten after the model produced the opposite sign.
The base estimator already matched the frozen polarity.

## 2. Parity Ordering

The parity artifact itself is clean:

- `validate_wcs_parity.py` contains no model import and no image generator.
- `wcs_parity.json` says `PASS_WCS_PARITY_FIRST`.
- The WCS is position-free: no `CRVAL`, sky position, survey row, or real object.
- The receipt records North-up/East-left with combined pixel-to-sky determinant
  `-7.71604938271605e-08`, i.e. reversing parity.

The runner enforces the receipt before model construction:

1. `run()` calls `verify_parity_first()`.
2. Only after that does it call `verify_frozen_inputs()`, set torch determinism, and
   `build_and_load_model()`.
3. It generates anchor spirals only inside the later probe loop.

Nuance: `run_bs5_sign_anchor.py` imports `torch` at module import time, so a literal rule that the
runner process may not import the torch library before checking parity is not satisfied. I do not
treat that as a blocker because the parity receipt is produced by a separate no-model/no-generator
validator, and the runner refuses model construction or spiral generation unless that receipt
already passed. The parity result is not estimator-contaminated.

## 3. Crashed First Attempt

The preserved first-attempt stderr shows:

> `TypeError: Object of type bool_ is not JSON serializable`

`attempt1_partial_probe_records.jsonl` is zero bytes and `attempt1_pre_correction_stdout.log` is
empty. That supports Yui's account that the failed attempt died while writing the first JSON record,
not after producing an inspectable sign-result receipt.

The final run records:

- `technical_execution_rerun_after_pre_result_serialization_error`: `true`
- `probe_selection_tuning_or_replacement`: `false`
- `threshold_tuning`: `false`
- `convention_change`: `false`

The preserved contract-suite log reports 11/11 pass, including the test that the serialization fix
returns JSON-native booleans and the test that the first failure is disclosed as a pre-result rerun.

I attempted to rerun the model-dependent unit suite locally, but this shell cannot import `torch`
(`ModuleNotFoundError: No module named 'torch'`). I therefore did not claim a fresh model-dependent
rerun. I did run model-free checks directly over the landed JSON/JSONL and used the preserved
contract logs for the torch-dependent tests.

## 4. Probe Custody

The seed schedule is fixed by:

- master seed: `LONGO-AMPLITUDE-BS5-ABSOLUTE-SIGN-V1`
- source indices: `5,000,000` through `5,000,031`
- seed derivation: first eight bytes of `SHA-256(master_seed || source_index)` modulo `2^63`

I recomputed the 32 seeds from that rule and compared them to `results.json`; they match exactly.
The first three recomputed seeds are:

- `2473273849244718098`
- `8789019505398510286`
- `1526912716211634484`

The last three are:

- `996386341571357895`
- `925931966215780766`
- `3812471434965937345`

The probe record has exactly 32 rows, with probe indices `0..31` and source indices
`5000000..5000031`. I see no evidence of probe selection, replacement, or dropping.

## 5. Is 32 Enough?

**Yes, for this specific BS-5 anchor.**

The anchor is not estimating a population rate; it is checking whether the frozen absolute polarity
of a deterministic estimator agrees with a fixed set of known synthetic CCW images and their
mirrors. If the sign were random per probe, a one-sided 32/32 pass has chance probability
`2^-32` before considering the mirrored-pair requirement. If the estimator had a global opposite
polarity, it would have failed 0/32 rather than passed.

The weakest numeric margin is the minimum accepted `chi`, `4.513615131378174`, only about `0.113`
above the frozen `tau = 4.4006456017494235`. That is worth recording, but it is not a BS-5 blocker
because the BS-5 predicate is absolute sign on known images, not retuning the acceptance threshold.
All 32 are nevertheless above tau.

More probes would add comfort, but I do not require them before BS-5 clears. The set already spans
hash-derived pitch, inclination, and S/N values inside the frozen support and has an independent
rendered-winding verification.

## 6. Real-Sky Boundary

The artifacts consistently report zero real-sky inputs:

- real sky data: `false`
- real object rows: `false`
- real images: `false`
- sky positions: `false`
- sky statistic: `false`
- network/survey catalogue imports: absent in the independent verifier's check

This receipt is synthetic only. It cannot substitute for future per-object PC-3 WCS/parity receipts
on any real-image run.

## Plain Answer

Yui's BS-5 synthetic absolute-sign anchor passes. The frozen convention remained
**CCW East-of-North => `chi > 0`**, and the estimator matched it with multiplier `+1`; no polarity
correction or convention flip was applied. This clears the synthetic sign-anchor prerequisite only.
It does not authorize real images, a sky run, publication, freeze, acceptance, commit, or push.
