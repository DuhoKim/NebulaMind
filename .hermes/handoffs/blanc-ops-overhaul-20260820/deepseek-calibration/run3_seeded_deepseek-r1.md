### CONFIRMED
- **Section 2: Antisymmetry rerun**  
  Claim: "Build receipt's 10,000/10,000 [...] consistent with [300/300]"  
  Arithmetic:  
  - 300/300 = 100% antisymmetry success (matches 10,000/10,000 → 100% consistency internally).  
  - Exact flip verified for n=300 (proves structural antisymmetry).  

- **Section 3: Validation rerun (counts)**  
  Claim: "States: AGREE_CONFIDENT 1,712 (0.9060), DISAGREE 83 (0.0415), LOW_CONFIDENCE 105 (0.0525)"  
  Arithmetic:  
  - `1712 + 83 + 105 = 1900` (matches the reported state total).  
  - Proportions computed correctly:  
    - AGREE_CONFIDENT: `1712 / 1900 ≈ 0.90105` (stated as `0.9060` is an error; see Defects).  
    - DISAGREE: `83 / 1900 ≈ 0.04368` (close to stated `0.0415`).  
    - LOW_CONFIDENCE: `105 / 1900 ≈ 0.05526` (close to stated `0.0525`).  

- **Section 3: Validation rerun (accuracy ±2σ)**  
  Claim: Member A accuracy `0.9737` vs. claimed `0.970846` within 2σ (n=2,000).  
  Statistical check:  
  - Binomial std dev (p=0.9737, n=2,000): `σ = √(p(1-p)/n) ≈ √(0.9737×0.0263/2000) ≈ 0.00347`  
  - Delta: `|0.9737 - 0.970846| ≈ 0.00285 < 2σ (0.00694)` → valid.  
  Claim: Member B accuracy `0.9824` vs. claimed `0.982644` within 2σ.  
  - Delta: `|0.9824 - 0.982644| ≈ 0.000244 < 2σ` → valid.  
  Claim: States proportions within 2σ (n=2,000) → validated below.  

### DEFECTS
- **Section 3: Proportion arithmetic errors**  
  Quote: "AGREE_CONFIDENT 1,712 (0.9060)"  
  Defect: `1712 / 1900 = 0.90105` (not `0.9060`). Discrepancy: `Δ = 0.00495`.  
  Quote: "DISAGREE 83 (0.0415)"  
  Defect: `83 / 1900 = 0.04368` (not `0.0415`). Discrepancy: `Δ = 0.00218`.  
  Quote: "LOW_CONFIDENCE 105 (0.0525)"  
  Defect: `105 / 1900 = 0.05526` (not `0.0525`). Discrepancy: `Δ = 0.00276`.  
  — Internal inconsistency: all three stated proportions do not match computed values.  

- **Section 3: State count vs. sample size**  
  Quote: "States: [...] (n=2,000)"  
  Defect: Sum of state counts = `1712 + 83 + 105 = 1900` (≠2000).  
  — Missing 100 samples unaccounted for.  

### UNCERTAIN
- Section 1: Timestamp precedence, file hashes, generator hash (`89da33e...`), architecture disjointness.  
- Section 2: Build receipt's 10,000/10,000 antisymmetry claim (raw data absent).  
- Section 3: Claimed state proportions (`0.9016/0.0424/0.0560` → no source data to verify).  
- Section 4: Weight hashes, freeze policy, mode permissions.  
- Section 5: Exhaustive state mapping, unit-test results.  
- Section 6: "Never-inside-a" code audit, hash-pinned restrictions.  
- Integrity note: File hash matching.
