# GORU: BS-3 Instrument Freeze Inventory

**Status:** INCOMPLETE (Yui required for missing production receipts).

Below is the verification of Kun's 11 blockers for the BS-3 preregistration freeze. The operative values and full hashes have been gathered and verified against the artifacts.

## Collected and Verified Items

**1. Full generator-code hash (Not truncated):**
- **Present:** `89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75`
- *Verified by directly hashing `spike/yui_identity/w_chi.py`.*

**2. Master seed M:**
- **Present:** `LONGO-AMPLITUDE-FREEZE-M1`

**3. Materialized training-set manifest and its hash:**
- **Present:** `498a505c84bb6d70058299e05c78d3ac1f025042ec173c405b404743d2742872` (Tag: `train-20000`, N=20,000)

**4. Exact training implementation details OR explicit statement on weights:**
- **Present:** The exact training recipe (optimizer, learning rate, loss) is not recorded. However, `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` (§4 Weights-freeze policy) provides the explicit statement that the serialized weights and canonical flat-parameter serialization are the sole reproducibility objects, stating: *"Inference reproducibility receipt: the frozen weights + frozen generator must reproduce χ_net bit-identically... After the freeze the weights are never touched."*

**5. Final weights file hash and canonical flat-parameter hash:**
- **Present (File Hash):** `83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d` (Verified directly on `weights_frozen.pt`)
- **Present (Canonical Hash):** `1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589`

**6. Numeric tau and null-set manifest hash:**
- **Present (Tau):** `4.4006456017494235`
- **Present (Null-set hash):** `1963132f2f36e7aa42b08012aad02d2c541d6c0973740a5bbce6a6e7a2904bd1` (Tag: `null-8000`, N=8000)

**7. Measured retention at tau with lower 95% bound:**
- **Present:** Retention is **86.24%** (10,349 / 12,000) with a one-sided lower 95% bound of **85.72%**. 
- *Note: This correctly reflects the full-inclination remeasurement, discarding the obsolete 96.15% average.*

**8. Production identity test receipts on the final raster and dtype:**
- **Present:** `R1_mirror_involution_byte_exact` (200/200) and `R2_antisymmetry_bit_exact` (200/200).

**9. Signed-zero test receipt:**
- **Present:** `R3_signed_zero`. `chi_sym`: 0.0, `chi_mirror_bits`: "0x0", `neg_chi_bits`: "0x80000000". `value_equal`: true, `bit_equal`: false.

## Missing Items (Requires Yui)

**10. Interpolating-mirror canary receipt (R4):**
- **GENUINELY MISSING.** The appendix (§6) defines this test, and the feasibility spike proved the canary fails under an affine mirror. However, `receipt_results.json` only contains R1, R2, and R3. Yui needs to generate and commit the R4 receipt for the production estimator.

**11. Per-object paired probe outputs / flip-imbalance receipt (R5):**
- **GENUINELY MISSING.** The flip-imbalance (`dA_raw`) is not reported for the production estimator in the current artifacts (only R1–R3 are logged). Yui needs to generate the R5 receipt on the production probe set.
