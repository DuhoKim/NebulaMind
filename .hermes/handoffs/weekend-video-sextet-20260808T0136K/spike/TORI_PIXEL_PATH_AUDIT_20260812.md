# TORI pixel-path audit feasibility spike

**Seat:** Tori — pixel-path custody / verification  
**Timestamp:** 2026-08-12T11:38:25+0900  
**Status:** `PASS_FEASIBILITY_WITH_BOUNDARY`  
**Scope:** Lana §10 item 2 only. No empirical sky run. Not a preregistration freeze.

## 1. Binding authority and boundary

This receipt implements the only authorised next step under:

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_SPIN_DESIGN_BRIEF_20260812.md` — 20,778 bytes; SHA-256 `8f60b811b67c2373be5c88369302351705fa5376638f49142ca891b6359ab1da`.
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/KUN_SPIN_DESIGN_BRIEF_GATE_20260812.md` — 9,385 bytes; SHA-256 `acd3b2f5ad5dad3bbce77beaf59a77e07a11bdcf4d31027ca18d2a2b3ed2e5d2`.

Kun's binding verdict is: **PASS AS A DESIGN BRIEF; NOT A PREREGISTRATION FREEZE; NO EMPIRICAL SKY RUN YET.** Lana §10 permits pixel-path audit tooling on synthetic and public calibration frames only. Sections 4.4–4.5 require known-chirality injections through the pixel path and a deliberately parity-flipped WCS null.

Hard boundary applied throughout:

- no catalogue was opened;
- no survey position list was opened;
- no real-galaxy handedness was computed;
- no anisotropy, monopole, dipole, fixed-axis, free-axis, or other sky statistic was computed;
- no network request or acquisition occurred;
- the retained 5,760-byte Legacy DR10 cutout was not refetched;
- no publication, acceptance, commit, or push occurred.

The original pixels in the retained Legacy cutout were used only for byte-preserving conversion checks. The chirality harness refuses non-synthetic FITS and was never called on those original real pixels. For the calibration-frame injection test, the tool made new files by **replacing** the retained frame's 16×16 pixel plane with synthetic known-sign pixels while retaining and hashing the WCS cards. This is full-frame synthetic substitution, not a label or statistic on the original image.

## 2. Concrete answer

### Can the checker determine parity with certainty?

**Yes, for a supported, non-singular, undistorted two-dimensional celestial FITS WCS whose first two axes are celestial longitude and latitude and whose linear transform is represented by a complete `CD` matrix or by `PC × CDELT`.**

The checker forms the two-dimensional linear pixel-to-sky matrix `M` and computes `det(M)`:

- `det(M) > 0` → `PRESERVING`;
- `det(M) < 0` → `REVERSING`;
- zero, non-finite, or numerically indeterminate determinant → fail closed;
- partial `CD`, non-celestial axis order, absent matrix/scale, or recognized distortion keywords → fail closed rather than overclaim.

This is certainty about the sign of the accepted header's local linear transform, not a certificate for unrecorded upstream survey reduction choices. For a distorted WCS, the current spike deliberately refuses to replace the required local Jacobian with the linear determinant.

### What did it determine for the retained Legacy frame?

The exact retained input is 5,760 bytes with SHA-256 `601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a`.

Its matrix is:

`[[-7.27777777777778e-05, 0.0], [0.0, 7.27777777777778e-05]]`

The determinant is exactly reported by the checker as `-5.2966049382716104e-09`, so the mapping is `REVERSING` in FITS-native row order.

### Does our conversion preserve that parity?

Yes, when the converter is used in its default FITS-native mode:

- decoded pixel dtype and values round-trip byte-for-byte through `.npy`;
- array-transform determinant is `+1`;
- combined pixel-to-output-sky sign remains `-1` for the retained Legacy frame.

The explicit top-left mode performs one vertical row flip:

- decoded pixel values still round-trip byte-for-byte after that declared transform;
- array-transform determinant is `-1`;
- combined sign becomes `+1`.

The synthetic control proves why this receipt is required: when the top-left flip is honored, the known sky sign recovers correctly; when the same flip is applied but its determinant is silently ignored, the harness reports `FAIL_SILENT_ROW_FLIP_DETECTED` and recovers the opposite sign.

## 3. Tooling built

All Tori deliverables are under the authorised absolute spike directory.

- `pixel_path_audit.py` — WCS checker, lossless decoded-pixel converter, synthetic generator, calibration-frame synthetic substitution, mirror control, scrambled-WCS control, and CLI. SHA-256 `f51d7868b9604533fd964660d1e66316494671d41bf7cd53e3c6d1dd84d6a623`.
- `tests/test_pixel_path_audit.py` — 21 tests. SHA-256 `83bb3798b491b0524b2a3feb29665adf5cdfa52ec975f37b5bdbe105925ea517`.
- `artifacts/final-v2/` — frozen final execution outputs for this receipt.
- `artifacts/final-v2/checker-outputs/` — one exact JSON checker stdout file for every tested FITS frame.

Runtime used: Python 3.9.6, NumPy 1.26.4, Astropy 6.0.1.

The CLI surfaces are:

- `audit INPUT [--row-order fits-native|top-left]` — WCS/row-order audit only; always states `chirality_computed: false`;
- `convert INPUT OUTPUT [--row-order ...]` — lossless decoded-pixel `.npy` plus transform receipt;
- `harness --output-dir DIR` — synthetic known-parity and known-sign controls;
- `inject BASE OUTPUT --sky-chirality -1|1` — replace calibration pixels with a known synthetic sign while retaining and hashing WCS cards;
- `scramble-wcs INPUT OUTPUT` — deliberately flip one WCS axis on a synthetic calibration frame and demand fault detection.

## 4. Test receipt

Exact final test stdout:

```text
.....................                                                    [100%]
21 passed in 1.26s
```

Result: 21/21 pass. The tests cover positive and negative `CD` determinants; `PC × CDELT`; singular and numerically indeterminate matrices; partial `CD`; non-celestial axes; recognized distortions; FITS-native and top-left row order; decoded-value/dtype round trips; synthetic known-sign recovery under both WCS parities; explicit versus silent row flips; exact mirror swap; calibration-frame synthetic substitution; scrambled-WCS detection; non-synthetic chirality refusal; and all CLI paths.

## 5. Synthetic harness results

The synthetic set contains both signs under parity-preserving and parity-reversing WCS. All four known sky signs recovered exactly:

| Frame | Expected sky sign | Pixel-array sign | WCS parity | Recovered sky sign | Result |
|---|---:|---:|---|---:|---|
| synthetic_preserving_minus | -1 | -1 | PRESERVING | -1 | PASS |
| synthetic_preserving_plus | +1 | +1 | PRESERVING | +1 | PASS |
| synthetic_reversing_minus | -1 | +1 | REVERSING | -1 | PASS |
| synthetic_reversing_plus | +1 | -1 | REVERSING | +1 | PASS |

Additional controls:

- explicit top-left flip: expected `+1`, output-array sign `-1`, transform determinant `-1`, recovered `+1`, `PASS`;
- silent top-left flip: expected `+1`, output-array sign `-1`, transform determinant deliberately ignored, recovered `-1`, `FAIL_SILENT_ROW_FLIP_DETECTED`;
- exact horizontal mirror: pixel raster equals the exact horizontal flip, WCS header unchanged, recovered sign swaps from `-1` to `+1`, `PASS_EXACT_MIRROR_SWAP`;
- scrambled WCS: pixels are byte-equal, WCS parity changes from `PRESERVING` to `REVERSING`, recovered sign changes from expected `-1` to `+1`, `PASS_FAULT_DETECTED`;
- overall machine result: `PASS_SYNTHETIC_PIXEL_PATH_AUDIT`.

The full machine output is at `artifacts/final-v2/synthetic_harness_output.json`, SHA-256 `3474e01ff88e82b9492842207e3be29b6f41ab5fd6da38e0357918e0a50544e3`.

## 6. Retained Legacy calibration-frame exercise

### 6.1 Original retained frame — audit only, no chirality

- identity: 5,760 bytes, SHA-256 `601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a`;
- 16×16, `>f4`, `RA---TAN` / `DEC--TAN`;
- `CD` determinant `-5.2966049382716104e-09`;
- FITS-native mapping: `REVERSING`;
- `chirality_computed: false`.

### 6.2 Lossless conversion of original retained pixels

Exact native conversion stdout:

```json
{
  "array_transform_determinant": 1,
  "combined_pixel_to_output_sky_determinant_sign": -1,
  "dtype": ">f4",
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/_tori_spin_access_evidence/legacy_dr10_one_test_cutout_r_16px.fits",
  "input_sha256": "601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a",
  "lossless_byte_equal": true,
  "output_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_dr10_one_test_cutout_r_16px.fits-native.npy",
  "output_sha256": "101f4be0f9dd644d4215c6ad6b16448e36bfa61955bd195a7c18b34eaba78c01",
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    16,
    16
  ],
  "wcs_determinant": -5.2966049382716104e-09,
  "wcs_matrix_source": "CD",
  "wcs_parity": "REVERSING"
}
```

Exact explicit top-left conversion stdout:

```json
{
  "array_transform_determinant": -1,
  "combined_pixel_to_output_sky_determinant_sign": 1,
  "dtype": ">f4",
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/_tori_spin_access_evidence/legacy_dr10_one_test_cutout_r_16px.fits",
  "input_sha256": "601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a",
  "lossless_byte_equal": true,
  "output_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_dr10_one_test_cutout_r_16px.top-left.npy",
  "output_sha256": "0255c5f15c84d4d376bc54b0c3600e31d39fc755e352feb237dcc51292b8414c",
  "row_order": "TOP_LEFT_VERTICAL_FLIP_FROM_FITS_NATIVE",
  "shape": [
    16,
    16
  ],
  "wcs_determinant": -5.2966049382716104e-09,
  "wcs_matrix_source": "CD",
  "wcs_parity": "REVERSING"
}
```

Both decoded-pixel conversions report `lossless_byte_equal: true`. Native mode preserves the WCS parity sign; explicit top-left mode changes it exactly once and logs determinant `-1`.

### 6.3 Synthetic substitution using the retained WCS

Two new calibration files replaced the original pixel plane with known synthetic signs while retaining the WCS-card digest exactly:

- before/after WCS digest for both: `53959fbfbf4daacb7aaf1df4458957537ae40f37559568437599daabd42c0fd1`;
- declared sky `-1` required injected pixel sign `+1` under the reversing WCS and recovered sky `-1`, `PASS`;
- declared sky `+1` required injected pixel sign `-1` and recovered sky `+1`, `PASS`;
- native conversion of each substituted frame reports `lossless_byte_equal: true`.

Exact minus-sign injection stdout:

```json
{
  "audit": {
    "array_transform_determinant": 1,
    "certainty": "DETERMINATE_LINEAR_WCS",
    "chirality_computed": false,
    "combined_mapping_parity": "REVERSING",
    "combined_pixel_to_output_sky_determinant_sign": -1,
    "ctype": [
      "RA---TAN",
      "DEC--TAN"
    ],
    "dtype": ">f4",
    "input_bytes": 5760,
    "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_minus.fits",
    "input_sha256": "05b35b057db4f6db4899d93098d5fd2e088383668ddd001d2462d68e017f6199",
    "linear_matrix": [
      [
        -7.27777777777778e-05,
        0.0
      ],
      [
        0.0,
        7.27777777777778e-05
      ]
    ],
    "matrix_source": "CD",
    "radesys": null,
    "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
    "shape": [
      16,
      16
    ],
    "wcs_determinant": -5.2966049382716104e-09,
    "wcs_parity": "REVERSING"
  },
  "injection": {
    "base_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/_tori_spin_access_evidence/legacy_dr10_one_test_cutout_r_16px.fits",
    "base_sha256": "601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a",
    "base_shape": [
      16,
      16
    ],
    "declared_sky_chirality": -1,
    "injected_pixel_chirality": 1,
    "output_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_minus.fits",
    "output_sha256": "05b35b057db4f6db4899d93098d5fd2e088383668ddd001d2462d68e017f6199",
    "status": "PASS_SYNTHETIC_INJECTION",
    "wcs_cards_sha256_after": "53959fbfbf4daacb7aaf1df4458957537ae40f37559568437599daabd42c0fd1",
    "wcs_cards_sha256_before": "53959fbfbf4daacb7aaf1df4458957537ae40f37559568437599daabd42c0fd1",
    "wcs_cards_unchanged": true,
    "wcs_parity": "REVERSING"
  },
  "recovery": {
    "array_transform_determinant": 1,
    "estimated_output_array_chirality": 1,
    "expected_sky_chirality": -1,
    "honored_array_transform": true,
    "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_minus.fits",
    "recovered_sky_chirality": -1,
    "status": "PASS",
    "wcs_parity": "REVERSING"
  }
}
```

Exact plus-sign injection stdout:

```json
{
  "audit": {
    "array_transform_determinant": 1,
    "certainty": "DETERMINATE_LINEAR_WCS",
    "chirality_computed": false,
    "combined_mapping_parity": "REVERSING",
    "combined_pixel_to_output_sky_determinant_sign": -1,
    "ctype": [
      "RA---TAN",
      "DEC--TAN"
    ],
    "dtype": ">f4",
    "input_bytes": 5760,
    "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_plus.fits",
    "input_sha256": "ceca5f6a84a1286606e94de86f32b92c70053d8e2190976bbd1d4228af45c44b",
    "linear_matrix": [
      [
        -7.27777777777778e-05,
        0.0
      ],
      [
        0.0,
        7.27777777777778e-05
      ]
    ],
    "matrix_source": "CD",
    "radesys": null,
    "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
    "shape": [
      16,
      16
    ],
    "wcs_determinant": -5.2966049382716104e-09,
    "wcs_parity": "REVERSING"
  },
  "injection": {
    "base_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/_tori_spin_access_evidence/legacy_dr10_one_test_cutout_r_16px.fits",
    "base_sha256": "601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a",
    "base_shape": [
      16,
      16
    ],
    "declared_sky_chirality": 1,
    "injected_pixel_chirality": -1,
    "output_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_plus.fits",
    "output_sha256": "ceca5f6a84a1286606e94de86f32b92c70053d8e2190976bbd1d4228af45c44b",
    "status": "PASS_SYNTHETIC_INJECTION",
    "wcs_cards_sha256_after": "53959fbfbf4daacb7aaf1df4458957537ae40f37559568437599daabd42c0fd1",
    "wcs_cards_sha256_before": "53959fbfbf4daacb7aaf1df4458957537ae40f37559568437599daabd42c0fd1",
    "wcs_cards_unchanged": true,
    "wcs_parity": "REVERSING"
  },
  "recovery": {
    "array_transform_determinant": 1,
    "estimated_output_array_chirality": -1,
    "expected_sky_chirality": 1,
    "honored_array_transform": true,
    "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_plus.fits",
    "recovered_sky_chirality": 1,
    "status": "PASS",
    "wcs_parity": "REVERSING"
  }
}
```

### 6.4 Scrambled-WCS null on the synthetic substitution

The plus-sign substituted frame was copied with pixels byte-equal and one WCS axis deliberately sign-flipped. The checker changed its classification from `REVERSING` to `PRESERVING`; the recovered sign changed from expected `+1` to `-1`; the harness returned `PASS_FAULT_DETECTED`.

Exact scrambled-WCS harness stdout:

```json
{
  "expected_sky_chirality": 1,
  "original_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_plus.fits",
  "original_wcs_parity": "REVERSING",
  "pixels_byte_equal": true,
  "recovered_sky_chirality": -1,
  "scrambled_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_plus_scrambled_wcs.fits",
  "scrambled_wcs_parity": "PRESERVING",
  "status": "PASS_FAULT_DETECTED"
}
```

## 7. Exact checker stdout for every tested FITS frame

The following ten blocks are the complete, unedited JSON stdout from the checker for every FITS frame in the final exercise. The checker computes no chirality; every block states `chirality_computed: false`.

### 01_synthetic_preserving_minus

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "PRESERVING",
  "combined_pixel_to_output_sky_determinant_sign": 1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 20160,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/synthetic/synthetic_preserving_minus.fits",
  "input_sha256": "adbcdefd57bb46025bf16aaa6ebbc4885486a589fbbc02236a8c1808dadabf73",
  "linear_matrix": [
    [
      0.0001,
      0.0
    ],
    [
      0.0,
      0.0001
    ]
  ],
  "matrix_source": "CD",
  "radesys": "ICRS",
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    65,
    65
  ],
  "wcs_determinant": 1.0000000000000018e-08,
  "wcs_parity": "PRESERVING"
}
```
### 02_synthetic_preserving_plus

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "PRESERVING",
  "combined_pixel_to_output_sky_determinant_sign": 1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 20160,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/synthetic/synthetic_preserving_plus.fits",
  "input_sha256": "8044cc3a32da171fd0aca75fe3b4de559b6483634af9d6c0cecb1633223f94b2",
  "linear_matrix": [
    [
      0.0001,
      0.0
    ],
    [
      0.0,
      0.0001
    ]
  ],
  "matrix_source": "CD",
  "radesys": "ICRS",
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    65,
    65
  ],
  "wcs_determinant": 1.0000000000000018e-08,
  "wcs_parity": "PRESERVING"
}
```
### 03_synthetic_reversing_minus

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "REVERSING",
  "combined_pixel_to_output_sky_determinant_sign": -1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 20160,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/synthetic/synthetic_reversing_minus.fits",
  "input_sha256": "860f1bd35c3156535601a07dc9c3900b822efaa487dbcbc1b5d3ed150ec8c39c",
  "linear_matrix": [
    [
      -0.0001,
      0.0
    ],
    [
      0.0,
      0.0001
    ]
  ],
  "matrix_source": "CD",
  "radesys": "ICRS",
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    65,
    65
  ],
  "wcs_determinant": -1.0000000000000018e-08,
  "wcs_parity": "REVERSING"
}
```
### 04_synthetic_reversing_plus

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "REVERSING",
  "combined_pixel_to_output_sky_determinant_sign": -1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 20160,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/synthetic/synthetic_reversing_plus.fits",
  "input_sha256": "ae49312f6e1adcd5686657bc7d5fa7fbf2c7ab23ea2b8d90985a93f8bed2cf86",
  "linear_matrix": [
    [
      -0.0001,
      0.0
    ],
    [
      0.0,
      0.0001
    ]
  ],
  "matrix_source": "CD",
  "radesys": "ICRS",
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    65,
    65
  ],
  "wcs_determinant": -1.0000000000000018e-08,
  "wcs_parity": "REVERSING"
}
```
### 05_synthetic_preserving_minus_scrambled_wcs

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "REVERSING",
  "combined_pixel_to_output_sky_determinant_sign": -1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 20160,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/synthetic/synthetic_preserving_minus_scrambled_wcs.fits",
  "input_sha256": "557db533e051264af784d455758523cce973b311b7009a6e35b9d0e483f17e86",
  "linear_matrix": [
    [
      -0.0001,
      0.0
    ],
    [
      0.0,
      0.0001
    ]
  ],
  "matrix_source": "CD",
  "radesys": "ICRS",
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    65,
    65
  ],
  "wcs_determinant": -1.0000000000000018e-08,
  "wcs_parity": "REVERSING"
}
```
### 06_synthetic_reversing_minus_mirrored

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "REVERSING",
  "combined_pixel_to_output_sky_determinant_sign": -1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 20160,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/synthetic/synthetic_reversing_minus_mirrored.fits",
  "input_sha256": "798a796fedfa2bcf74d6f7b1867db9a023b68ea2ec31ae7740c5154c595090a8",
  "linear_matrix": [
    [
      -0.0001,
      0.0
    ],
    [
      0.0,
      0.0001
    ]
  ],
  "matrix_source": "CD",
  "radesys": "ICRS",
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    65,
    65
  ],
  "wcs_determinant": -1.0000000000000018e-08,
  "wcs_parity": "REVERSING"
}
```
### 07_legacy_retained_original

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "REVERSING",
  "combined_pixel_to_output_sky_determinant_sign": -1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 5760,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/_tori_spin_access_evidence/legacy_dr10_one_test_cutout_r_16px.fits",
  "input_sha256": "601c309771ed5da0a15defc0b4ccfc1063ee8422a89fbc969d916bba6c1f257a",
  "linear_matrix": [
    [
      -7.27777777777778e-05,
      0.0
    ],
    [
      0.0,
      7.27777777777778e-05
    ]
  ],
  "matrix_source": "CD",
  "radesys": null,
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    16,
    16
  ],
  "wcs_determinant": -5.2966049382716104e-09,
  "wcs_parity": "REVERSING"
}
```
### 08_legacy_header_synthetic_minus

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "REVERSING",
  "combined_pixel_to_output_sky_determinant_sign": -1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 5760,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_minus.fits",
  "input_sha256": "05b35b057db4f6db4899d93098d5fd2e088383668ddd001d2462d68e017f6199",
  "linear_matrix": [
    [
      -7.27777777777778e-05,
      0.0
    ],
    [
      0.0,
      7.27777777777778e-05
    ]
  ],
  "matrix_source": "CD",
  "radesys": null,
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    16,
    16
  ],
  "wcs_determinant": -5.2966049382716104e-09,
  "wcs_parity": "REVERSING"
}
```
### 09_legacy_header_synthetic_plus

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "REVERSING",
  "combined_pixel_to_output_sky_determinant_sign": -1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 5760,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_plus.fits",
  "input_sha256": "ceca5f6a84a1286606e94de86f32b92c70053d8e2190976bbd1d4228af45c44b",
  "linear_matrix": [
    [
      -7.27777777777778e-05,
      0.0
    ],
    [
      0.0,
      7.27777777777778e-05
    ]
  ],
  "matrix_source": "CD",
  "radesys": null,
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    16,
    16
  ],
  "wcs_determinant": -5.2966049382716104e-09,
  "wcs_parity": "REVERSING"
}
```
### 10_legacy_header_synthetic_plus_scrambled_wcs

Exact checker stdout:

```json
{
  "array_transform_determinant": 1,
  "certainty": "DETERMINATE_LINEAR_WCS",
  "chirality_computed": false,
  "combined_mapping_parity": "PRESERVING",
  "combined_pixel_to_output_sky_determinant_sign": 1,
  "ctype": [
    "RA---TAN",
    "DEC--TAN"
  ],
  "dtype": ">f4",
  "input_bytes": 5760,
  "input_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/artifacts/final-v2/legacy_header_synthetic_plus_scrambled_wcs.fits",
  "input_sha256": "aa1c60fe6aad033a8cb6badb585d743f8f17efccdb1cb7cbe2b9f05dcde31c68",
  "linear_matrix": [
    [
      7.27777777777778e-05,
      0.0
    ],
    [
      0.0,
      7.27777777777778e-05
    ]
  ],
  "matrix_source": "CD",
  "radesys": null,
  "row_order": "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
  "shape": [
    16,
    16
  ],
  "wcs_determinant": 5.2966049382716104e-09,
  "wcs_parity": "PRESERVING"
}
```

## 8. Interpretation and custody grade

### What passed

- The WCS checker gives an explicit, deterministic parity grade for all supported linear celestial fixtures tested.
- It fails closed on unsupported/ambiguous cases covered by the tests.
- The converter preserves decoded pixels and dtype exactly in both modes and records row order plus transform determinant.
- Known synthetic sky signs recover correctly under both WCS parities.
- The explicit top-left row transform is corrected; the deliberately silent row transform is detected.
- Exact mirroring swaps recovered sign.
- Both pure-synthetic and retained-Legacy-WCS scrambled-header nulls detect the injected fault.
- The one retained Legacy file has a determinate `REVERSING` linear WCS mapping, and no original real-pixel chirality was computed.

### What did not pass because it was not authorised or not attempted

- No survey sample was tested.
- No real-galaxy label was produced.
- No sky statistic was produced.
- No footprint-wide position injection was attempted.
- No classifier intended for an empirical run was selected or frozen.
- No preregistration values were frozen.
- No claim of complete survey-side reduction custody is made.

Accordingly, this is a **feasibility pass for the local FITS → WCS-parity → explicit-row-order → lossless-array → synthetic-sign-recovery path on the tested fixtures**. It does not upgrade any survey or empirical study to end-to-end parity custody. The retained Legacy delivery/header receipt remains exactly that; this spike adds a successful local parity/conversion/injection receipt for that one frozen header and for synthetic fixtures.

## 9. Boundary reached

The tooling is now at the point where the natural next step would be to run the path on additional real images, a catalogue, or real sky positions. That step is **BLOCKED**. Reaching this boundary is the successful endpoint of the authorised feasibility spike.

Re-entry requires a separate SHA-pinned preregistration artifact that freezes every open value and a distinct empirical-run authorisation. Neither exists in this receipt.

## 10. Side-effect ledger

- Files created: only under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/`.
- Existing retained Legacy FITS: read only; identity unchanged.
- Network fetches: 0.
- Bulk acquisition: 0.
- Real sky statistics: 0.
- Real cutout chirality computations: 0.
- Publication/acceptance: none.
- Git commit/push: none.

— Tori, custody / verification seat.
