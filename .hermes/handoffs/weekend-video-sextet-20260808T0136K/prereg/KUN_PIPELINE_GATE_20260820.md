PASS_CUTOUT_PIPELINE

# KUN PIPELINE GATE — 2026-08-20 (cutout runner + IC rerun pair; last gate before real cutout production)

## Verdict

**PASS_CUTOUT_PIPELINE.** I read the code, re-ran the runner test suite, re-ran the
stdlib independent verifier (byte-identical output), reran the identity witness and the
full-path mirror antisymmetry myself on the seeded 200-probe prefix through the
hash-pinned production IC functions, recomputed every retention/R1–R5 number from the
preserved rows, and verified every hash pin against the bytes on disk. All four kickoff
checks hold. Three non-blocking observations are recorded in §6. No repairs required.

## What I ran myself (not just read)

1. `python3 -m unittest -v test_cutout_runner.py` in `_cutout_runner_20260820/`:
   **5/5 passed in 2.933s** (DONE doc: 5/5 in 3.307s), including
   `test_null_slots_refuse_real_sky` and the full synthetic fixture through the
   compressed-FITS read path + certified adapter + IC-1..IC-7.
2. `python3 _icrerun_20260820/independent_verify.py` (stdlib-only): exit 0,
   `PASS_INDEPENDENT_ICRERUN_REDUCTION`, **32/32** checks true; the rewritten
   `INDEPENDENT_VERIFICATION.json` is byte-identical to the pinned artifact
   (`bca40882b4efb62955ff40c4bf99f478acfb09c29ffb58d749c0da51df736acd` before and after).
3. My own witness `prereg/KUN_PIPELINE_GATE_WITNESS_20260820.py` (venv_torch python 3.9.6,
   numpy 1.26.4, torch 2.8.0, deterministic algorithms, 1 thread — the receipted
   environment): loads the hash-pinned frozen generator, old R4/R5 runner, and the
   hash-pinned PRODUCTION `cutout_runner.py`, recomputes source indices 3,000,000–3,000,199:
   **PASS_KUN_PIPELINE_WITNESS**, all seven counts 200/200, max residual 0.0, prefix
   manifest `ab75d5f2ec08ad44fbcf1198d1612c23759f8d3aac29db044a181346ac43f9b2` reproduced,
   canonical weights `1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589`
   reproduced, and my per-probe chi bits match the preserved rerun rows 200/200.
4. Stdlib recompute over all 13,000 preserved rows (12,000 retention + 1,000 R1–R5):
   every receipted number reproduced exactly, and each matches the old-path receipt
   exactly (quotes in §4).
5. Every artifact hash in `ICRERUN_RECEIPT_20260820.md` recomputed against disk:
   16/16 match, plus the receipt itself
   (`shasum -a 256 ICRERUN_RECEIPT_20260820.md` =
   `050500f9ec420ccdd053ff4161ae71345e230ab5577dc8724407db458e010da9`, matching
   `ICRERUN_RECEIPT_20260820.sha256` and `GPT1_RERUN_DONE.md`), and both preserved
   attempt row-files hash to the final `65fa6dfe8ab43ea28053c3840126c98406a10ce137329446d1a3e5d38747ef1a`.

## 1. Cutout runner implements IC-1..IC-7 letter-for-letter

File: `_cutout_runner_20260820/cutout_runner.py` (SHA-256
`ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc`, 454 lines, read in
full). Each A3 clause quoted beside its implementation:

- **IC-1** "*The delivered product must contain exactly one 2-D image plane of shape
  128×128 … If the delivery contains any other shape, extra plane, or extra image HDU,
  the object FAILS CLOSED (logged, excluded by the frozen abstention rule — never
  silently reduced).*" → lines 202–207: `plane.ndim != 2 or plane.shape != (128,128)`
  raises `FAILED_IC1_SINGLE_PLANE`; failure is logged to the per-object receipt with
  `status: FAIL` (lines 384–391). Upstream, the gated reader opens exactly HDU 1 and
  rejects non-`CompImageHDU`/wrong-shape/3-D sources
  (`production_readpath.py:146–153,176–184`); the hash-pinned certified adapter emits
  exactly one 128×128 raster. "Band r only": the runner has no band parameter at all —
  it consumes an explicit manifest of receipt-accepted r-band bricks. The A3 HDU-index
  BINDING SLOT belongs to Tori's successor route binding (service side), not to this
  local-brick runner; see observation O2.
- **IC-2** "*pixel values are consumed in the delivered survey units (nanomaggies), with
  no unit conversion before the frozen scaling map.*" → lines 226–229: the raster is
  passed whole to the frozen scaler (comment: "the delivered nanomaggies are passed to
  the frozen map whole"); receipt fields `"delivered_units": "nanomaggies"`,
  `"unit_operation_before_scaling": "NONE"` (lines 251–252). No conversion code exists
  anywhere in the module.
- **IC-3** "*no background estimation or subtraction beyond what the survey pipeline
  already applied*" → no background/subtraction operation exists in the runner (grep:
  none); receipt field `"background_operation": "NONE"` (line 253). The A3-required
  synthetic-background equivalence was exercised by the rerun, not assumed: 13,000/13,000
  natural frozen-generator images entered the production scaler and came out byte-equal
  (`IC_SLOT_VALIDATION_RECEIPT.json`: `"old_new_input_bytes_exact": 13000`).
- **IC-4** "*NaN/Inf pixels are replaced by 0.0 after the scaling map, and the invalid
  fraction is logged per object; an object with invalid fraction above the frozen cap …
  FAILS CLOSED to abstention.*" → lines 209–224: invalid fraction computed, cap schema
  checked, `invalid_fraction > cap` raises `FAILED_IC4_INVALID_FRACTION_CAP`; replacement
  is explicitly ordered after scaling (lines 236–237: "# IC-4 ordering is binding:
  replacement occurs only after scaling." / `scaled[invalid] = 0.0`); logged per object
  (receipt lines 247–249). The cap is a slot (`FAILED_IC4_UNFILLED` if null), now filled
  at `0.0` — any invalid pixel abstains.
- **IC-5** "*a fixed monotone function with all constants frozen (BINDING SLOT …) No
  per-object, per-stratum, or data-dependent normalization of any kind*" → lines 179–191
  `_load_scaler`: the function is a hash-pinned external module + callable + constants
  read from the slot file; the runner chooses nothing. Filled value: identity affine map
  `tensor = float32(nanomaggy)`, gain 1.0, offset 0.0; `ic5_scaler.py` (SHA-256
  `21b66eda899b5e48034be2b2d92ee2c77f262b156eb59d680eb1b80763d12621`) hard-rejects any
  other constants and applies no normalization. Monotonicity validated on a 16,384-value
  grid and 13,000/13,000 byte-exact images (recorded justification, §4 below).
- **IC-6** "*float32, little-endian, C-order (row-major), a single channel tensor of
  shape (1, 128, 128); FITS big-endian source values are converted once at ingest.*" →
  line 242: `np.array(scaled, dtype=np.dtype("<f4"), order="C", copy=True).reshape((1,128,128))`
  with a postcondition check (lines 243–244); the once-at-ingest big-endian conversion is
  owned by the gated reader's `np.array(data, dtype=np.float32, order="C")`
  (`production_readpath.py:162`, recorded at runner line 258).
- **IC-7** "*mirror is the pure index reversal on the width axis of the consumed raster
  (np.fliplr semantics) … applied in tensor space after IC-1…IC-6, and nowhere else in
  the χ path.*" → `mirror_tensor` lines 263–268: refuses anything but an IC-6 tensor
  (shape/dtype/C-contiguous), then `np.fliplr(value[0])`; in `compose_object` it is
  invoked only after `apply_input_contract` (lines 340–347). Grep confirms no flip/mirror
  exists in the gated reader or the certified adapter — nowhere else in the χ path. This
  matches the estimator appendix HARD RULE ("`mirror` inside the wrapper is pure index
  reversal (`np.fliplr` / tensor flip on the width axis). Never a resampling, affine, or
  interpolation operation anywhere in the χ path").

## 2. Composition imports the gated read path and gated adapter without reimplementation

- `cutout_runner.py:104–129` loads both modules only through `_load_module` with exact
  hash pins: adapter `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
  (the resampler-gate-certified adapter per `KUN_RESAMPLER_GATE_20260816.md`), read path
  `105bd0c6858f27166fecee5ff7ece42c0e993eab8e3bc15b517f9bc9b5418d56` (the gated
  production read path per `KUN_READPATH_GATE_20260819.md`, PASS_PRODUCTION_READPATH).
  I recomputed both file hashes: exact match. The runner also re-verifies the frozen
  prereg V3 hash + mode 444 and the amendment hash before every composition
  (`verify_frozen_dependencies`, lines 77–101); I recomputed those too
  (`b06901c8…` mode 444; amendment `519ab5ba…`).
- The 454-line runner contains no WCS, FITS, decompression, or resampling code (full
  read; no astropy import); composition is `reader.ProductionBrickSource(...)` +
  `adapter.render_cutout(...)` at lines 329–337. Runtime proof: the full-path synthetic
  fixture test passed through the real compressed-FITS read path and adapter (§ above,
  test 1 of 5).

## 3. Null-slot refusal existed before the rerun filled the slots

Cryptographic and test evidence, not claims:

1. `GPT2_CUTOUTRUNNER_DONE.md` (written 07:39, before the fill) pins the production
   `ic_slots.json` at SHA-256 `263099856f3d3523179dfdccfe40e7a0b9ddbd9b21fa31824b2eafee94588952`.
   I reconstructed the byte string `{\n  "ic4_invalid_fraction_cap": null,\n
   "ic5_scaling_map": null\n}\n`; it hashes to exactly that value. The production slot
   file was therefore null-filled at 07:39.
2. The refusal code is in `cutout_runner.py` lines 169–175
   (`REFUSED_REAL_SKY_UNFILLED_SLOTS`) and is invoked in `compose_object` at line 328,
   before any `ProductionBrickSource` open (lines 331–336) — the comment at line 327:
   "This refusal precedes all real brick opens and therefore all real raster reads."
   The runner file's hash (`ccb9b8fe…`, mtime 07:35) is unchanged since the DONE
   receipt, so the refusal predates the fill (slot file mtime 07:43).
3. The DONE receipt records 5/5 tests passing pre-fill, including "IC-4/IC-5 null-slot
   real-sky refusal"; that test (`test_null_slots_refuse_real_sky`) is present in the
   current suite and passed in my run. Both handoff dirs are git-untracked, so file
   history rests on these hash pins and mtimes — which are sufficient and mutually
   consistent.
4. Current production `ic_slots.json` (filled by the rerun) hashes to
   `10d24a6e1c5dd64eef8e1ada7e3d222f2e168bab288b1438792db7ff6a848372` — the exact pin
   the kickoff and the rerun receipt demand.

## 4. The IC rerun: byte-identical production path, pins, recomputes

**Code-path evidence (not claims).** `_icrerun_20260820/run_icrerun.py` (SHA-256
`65014032cce0578db8f18c11d9ab037d241874ba0407457ff8186e3119485d1a`, 594 lines, read in
full) imports the production module with a hard hash check
(`load_module(CUTOUT_PATH, "ccb9b8fe…")`, line 91) and calls
`cutout.apply_input_contract` / `cutout.mirror_tensor` for every IC stage (lines
143–149, 241–251, 325–330, 430, 437). It contains no reimplemented IC-1..IC-7 logic.
`verify_pins()` re-hashes all 13 frozen inputs before AND after the run and aborts on
any drift (lines 116–140, 524–526). I recomputed all 13 hashes against disk: all match.

**BS-3 generator hash.** `spike/yui_identity/w_chi.py` on disk hashes to
`89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75`, matching the rerun's
pin and its prior pins: `KUN_REGATE_BS1_BS3_20260814.md` line 100 ("full generator-code
hash present: `89da33ec…`"), and the old identity/R4-R5/retention receipts.

**Identity witness, my own rerun (seeded 200-probe prefix).** Old-path chi vs
full-IC-path chi: **200/200 float32-bit-identical**; IC-5 input-byte identity 200/200;
and my per-probe bits equal the preserved rerun rows 200/200. The receipt's full
1,000/1,000 witness is independently confirmed by the stdlib verifier over the rows
(`identity_witness` sum = 1000) and by my recompute.

**Retention, recomputed from `retention_records.jsonl` (12,000 rows, sequence
2,000,000–2,011,999 verified):** accepted **10,349/12,000**; retention
**0.8624166666666667**; one-sided 95% Wilson lower bound (Z = 1.6448536269514722)
**0.8571626782674123**; accepted-sign accuracy 10,349/10,349 = **1.0**; invalid pixels 0;
input-bytes-equal-old-path 12,000/12,000; image manifest `bb60b69b…` == tensor manifest
== old receipt manifest.

Exact old-path agreement, old receipt values quoted beside the new
(`yui_inclination_retention_remeasure_20260812/results.json` vs
`_icrerun_20260820/RETENTION_RECEIPT.json`):

| Quantity | Old-path receipt | New full-IC receipt | My recompute |
|---|---:|---:|---:|
| accepted / n | 10,349 / 12,000 | 10,349 / 12,000 | 10,349 / 12,000 |
| retention | 0.8624166666666667 | 0.8624166666666667 | 0.8624166666666667 |
| lower 95% Wilson | 0.8571626782674123 | 0.8571626782674123 | 0.8571626782674123 |
| accepted-sign accuracy | 1.0 | 1.0 | 1.0 |
| 0–15° | 602/630, 0.9555555555555556, LB 0.9399913956399034 | identical | identical |
| 15–30° | 1,785/1,831, 0.9748771163298744, LB 0.9681244113355228 | identical | identical |
| 30–45° | 2,909/2,970, 0.9794612794612795, LB 0.9747238195819057 | identical | identical |
| 45–60° | 3,652/3,842, 0.950546590317543, LB 0.9444693134261581 | identical | identical |
| 60–65° | 1,072/1,427, 0.7512263489838823, LB 0.7319391366831476 | identical | identical |
| 65–69.3° | 329/1,300, 0.2530769230769231, LB 0.23376928784859147 | identical | identical |
| S/N 2–5 | 2,591/3,452, 0.7505793742757821, LB 0.7382731582361939 | identical | identical |
| S/N 5–10 | 2,310/2,594, 0.8905165767154973, LB 0.8800226298695049 | identical | identical |
| S/N 10–20 | 2,347/2,592, 0.9054783950617284, LB 0.8955992721825667 | identical | identical |
| S/N 20–50 | 3,101/3,362, 0.9223676383105295, LB 0.9144324208557847 | identical | identical |

R1–R5 rows recomputed likewise: R1 1,000/1,000; R2 value- and bit-exact 1,000/1,000, max
residual 0.0; R3 signed-zero fixture (chi +0.0 bits `0x00000000`, −chi `0x80000000`,
value-equal, bit-unequal, ordered rejection) matching the old identity receipt; R4
200/200 > 0.01 with min 0.010587692260742188 / max 1.5070748329162598 / mean
0.3970843741297722 — exactly the old canary values; R5 sum 3.0, dA_raw 0.015, counts
{0.0: 197, 1.0: 3}, 0 acceptance mismatches — exactly the old values; manifests
`35d679d4…` / `ab75d5f2…` reproduced.

**IC-4 = 0.0 and IC-5 identity map: justifications and pins.** Both choices carry
recorded synthetic-only justifications: `IC_SLOT_VALIDATION_RECEIPT.json`
("All 13,000 frozen-generator natural synthetic images had invalid fraction 0.0. No
synthetic evidence supports tolerance above zero, so the conservative cap is 0.0") and
the rerun receipt §IC-5 ("the weights and tau were frozen on the generator's float32
scale … no real image or real-data statistic was used to choose it"), plus the edge
fixture (one NaN in 16,384 pixels fails closed with `FAILED_IC4_INVALID_FRACTION_CAP`).
Both values are pinned in `_cutout_runner_20260820/ic_slots.json`, whose bytes hash to
**`10d24a6e1c5dd64eef8e1ada7e3d222f2e168bab288b1438792db7ff6a848372`** (verified), and
that exact pin is referenced by the rerun receipt `ICRERUN_RECEIPT_20260820.md`, whose
bytes hash to **`050500f9ec420ccdd053ff4161ae71345e230ab5577dc8724407db458e010da9`**
(verified against the `.sha256` sidecar and `GPT1_RERUN_DONE.md`). The slot file's
scaler pin `21b66eda…` matches the scaler bytes on disk.

**Attempt custody.** `attempt1_terminated/` (transport failure, no verdict) and
`attempt2_code_error/` (wrong module namespace for `synth_disk`; traceback preserved)
retain their partial rows; both row-files hash to the final
`65fa6dfe8ab43ea28053c3840126c98406a10ce137329446d1a3e5d38747ef1a` — no probe was
dropped, replaced, or retried under a different definition. The attempt-2 repair
(import the same hash-pinned generator directly) is visible at line 323.

## 5. Mirror antisymmetry — my own full-path rerun on the 200 seeded synthetics

Through the production IC functions and frozen model (canonical weights hash verified):
`chi(mirror(x)) == -chi(x)` value-exact **200/200** and float32-bit-exact **200/200**;
max `abs(chi(mirror(x)) + chi(x))` = **0.0**; IC-7 placement (mirror-after-IC bytes ==
IC-of-raw-mirror bytes) 200/200; R1 involution 200/200. The receipt's 1,000/1,000
claims reproduce on the seeded prefix I ran.

## 6. Never-touched-real-data claim

`grep -rn 'NebulaMindData' _cutout_runner_20260820 _icrerun_20260820` → **zero matches**
(exit 1) across code and receipts. The runner imports are clean (no socket/requests/
urllib/httpx/astropy in production code; the verifier's AST scan agrees); the rerun
imports only hash-pinned local synthetic/frozen artifacts. For completeness: the string
`/Users/duhokim/NebulaMindData/dr10_south_image_r/.../legacysurvey-0001m395-image-r.fits.fz`
appears only in the previously gated 2026-08-19 read-path artifacts
(`_production_readpath_20260819/real_verification_receipt.json`, PASS/ACCEPTED/
digest-verified) and their gate documents — the runner's 07:37 NON_SCIENCE smoke read
that one receipt-accepted brick read-only, produced no IC processing and no science
tensor, and deleted its staged raster in the same run
(`NON_SCIENCE_SMOKE_RECEIPT.json`, hash verified). The rerun pair itself never touched
real data.

## Observations (non-blocking; no repair demanded)

- **O1 — stale test-file pin in the DONE receipt.** `test_cutout_runner.py` on disk
  hashes to `45d69939b3310512dd065fcb5f1e148b40710148f42cc4606424f29ce56bcdd3`, not the
  `da40f8c0…` pinned in `GPT2_CUTOUTRUNNER_DONE.md` (file mtime 08:01, after the 07:39
  receipt; the directory is git-untracked so the old bytes are unrecoverable). The
  current suite contains exactly the five receipted behaviors including the null-slot
  refusal, and passed in my run; the 08:01 README documents the filled slot pin
  `10d24a6e…`. Impact: record hygiene only — the DONE receipt's artifact list is stale
  for this one file. The pipeline artifacts themselves are all hash-consistent.
- **O2 — IC-1 plane check sits after a layout-only reshape.** `compose_object` line 338
  reshapes the adapter's flat 16,384-value output to (128,128) before the IC-1 check.
  A wrong-size output raises (fail-closed, logged FAIL); a reduction is impossible
  because reshape preserves element count. The "exactly one plane / band r only / HDU
  index" service-side clauses remain owned by the gated reader (HDU 1 only) and Tori's
  successor route binding per A3 — not by this local-brick runner. Intent is met.
- **O3 — smoke receipt's refusal string is a recorded annotation.**
  `NON_SCIENCE_SMOKE_RECEIPT.json`'s `"real_sky_runner_status":
  "REFUSED_WHILE_IC_SLOTS_NULL"` is hardcoded in the smoke script, not an executed
  refusal. The executed-refusal evidence stands independently on §3 items 1–3
  (reconstructed null-file hash, unchanged code hash, pre-fill passing test).

## Boundary

Findings only. I read files, grepped, recomputed, and ran tests/witnesses locally; I
trained, tuned, fetched, published, committed, deployed, and authorized nothing. My
witness script (`prereg/KUN_PIPELINE_GATE_WITNESS_20260820.py`) reads only synthetic
generator artifacts and frozen local weights. **Sky access and real cutout production
remain subject to Hwao/Duho's separate explicit go; this gate only certifies that the
cutout runner + IC rerun pair is internally consistent, hash-pinned, and
evidence-complete against `LANA_PC1_INPUT_AMENDMENT_20260815.md` §3 A3.**

— Kun (kimi gate seat), 2026-08-20.
