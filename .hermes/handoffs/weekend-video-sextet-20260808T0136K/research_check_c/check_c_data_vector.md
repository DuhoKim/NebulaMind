# Check C — Is the measured BOSS parity-odd 4PCF data vector uncontested?

## Verdict

**Substantively yes, literally no.** The two direct BOSS 4PCF reanalyses recompute the odd-parity statistic and reproduce the excess in the measured BOSS vector under the original-style weighting.[1][3] Neither concludes that the ENCORE 4PCF estimator, survey-window correction, or a parity-odd observational systematic fabricated the measured vector.[1][3] Their null conclusions instead come from changing the **reference/noise distribution** (Philcox–Ereza) or changing the **statistic used to interpret the same measured 4PCFs** so that parity signal and data–mock covariance mismatch separate (Krolewski et al.).[1][3]

The qualification is important: there is no single byte-identical vector that every paper simply imports.[3] Krolewski et al. independently recompute the 4PCFs and document small sample, radial-bin, random-catalogue, and weighting differences; their exact 18-bin χ² values differ from Hou et al.[3] But they explicitly say they reproduce the “essential features” of both original analyses.[3] Thus the defensible wording is:

> **The odd-parity BOSS 4PCF excess is independently reproduced and is not the central disputed fact; its claimed parity-violation significance is disputed because the covariance/noise model and χ² statistic are not robust. Exact vector entries are analysis-definition dependent, so “uncontested” should not be taken to mean numerically identical across pipelines.**

## Primary-source paper-by-paper classification

### 1. Philcox & Ereza, *Could sample variance be responsible…?* — covariance/noise-distribution reanalysis

**Classification:** Recomputes the Philcox-style 10-bin BOSS 4PCF, holds the BOSS result fixed while changing the mock/noise distribution; **does not attack the measurement estimator or window correction.**[1] It is not a direct rerun of Hou et al.’s full 18-bin vector.[1]

Primary records:

- arXiv **v1** only: [arXiv:2401.09523v1](https://arxiv.org/abs/2401.09523v1).[2]
- Published version: *Phil. Trans. R. Soc. A* **383** (2025) 20240034, [DOI 10.1098/rsta.2024.0034](https://doi.org/10.1098/rsta.2024.0034); [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12169525/).[1]
- Version caveat: arXiv v1 included CMASS+LOWZ and reported a 1.4σ baseline; the published paper focuses on CMASS and reports 1.0σ.[1][2] The logic below is unchanged.

**Exact evidence:**

1. **They recompute, rather than merely download, the BOSS vector with the established estimator.**[1] Section 2, published PDF p. 3: “**Given the datasets, 4PCFs are obtained using the encore code [17,61].**”[1] The same paragraph says “**Our binning follows**” (paper ref. 9); it uses ten radial bins and discards ℓ=5 “due to residual leakage from the window function.”[1] Footnote 3 says they use a “**Landy–Szalay-type estimator … to remove the window function, as described in [17,61].**” These are continuity statements, not allegations of an estimator/window error.[1]

2. **The original Philcox-style result is recovered with the old mocks.**[1] Table 1, p. 4, labels the MultiDark-Patchy values “**obtained also in previous work**” and gives the combined CMASS result as **99.6%, 2.9σ**, versus **69.5%, 1.0σ** with GLAM-Uchuu.[1] Figure 2, p. 5, describes the “**BOSS result shown as a vertical red line**” against the two mock histograms and states: “**Using the GLAM-UCHUU catalogues, we find no evidence for parity-violation in BOSS, but a strong preference when the 4PCF noise distribution is modelled with the MultiDark-Patchy suite.**”[1] This is an unusually clear same-data/different-null comparison.[1]

3. **Their explicit target is sample variance/covariance.**[1] Section 3, p. 7: “**the BOSS data have larger χ̃² than 99.6% of the MultiDark-Patchy catalogues but only 69.5% of the GLAM-Uchuu suite**”; the paper says the detection “disappears” if GLAM-Uchuu better represents the survey.[1] The observed BOSS line has not vanished; the null PDF broadened/shifted.[1]

4. **Scope limit for the Hou 7.1σ vector.**[1] Section 4, pp. 7–8, calls its conclusions for Hou et al. implications, then says the enhanced excess from using more bins “**would be interesting to investigate further with the GLAM-Uchuu catalogues**.”[1] Therefore this paper alone does **not** establish a direct reproduction of Hou et al.’s 18-bin, 18,768-component measurement.[1]

**Check-C reading:** For the Philcox 10-bin vector, the measurement is accepted/reproduced and covariance is disputed.[1] For the Hou fine-binned vector, this paper is indirect.[1]

### 2. Krolewski, May, Smith & Hopkins, *No evidence for parity violation in BOSS* — independent full remeasurement plus a new significance statistic

**Classification:** Independently recomputes both the 10-bin Philcox-style and 18-bin Hou-style 4PCFs.[3] Exact pipeline choices are not identical, but the measured excess is reproduced.[3] The rebuttal then targets χ²’s data–mock covariance/8PCF bias, not the existence of the odd 4PCF vector.[3]

Primary records:

- arXiv **v1** only: [arXiv:2407.03397v1](https://arxiv.org/abs/2407.03397v1).[4]
- Published: *JCAP* 08 (2024) 044, [DOI 10.1088/1475-7516/2024/08/044](https://doi.org/10.1088/1475-7516/2024/08/044).[3]

**Exact evidence:**

1. **Direct declared reproduction.**[3][4] Section 3, p. 9: “**In this section we will define the χ² statistic, and reproduce the ∼7σ and ∼3σ results from [1, 2].**”[3] The next sentence says the purpose is “**to establish consistency between our pipeline and previous results**.”[3][4]

2. **Independent estimator/window implementation.**[3] Section 3.1, p. 10, says realistic geometry is handled with the “**edge correction procedure described in section 2 of [1] or section II.C of [2]**,” implemented in the public **ENCORE** software.[3] Page 11 says “**To compute Ê, we run the public ENCORE software**.”[3] Thus this is a fresh catalogue-level computation with the established edge/window method, not reuse of a frozen published vector.[3]

3. **Measured excess reproduced.**[3] Figure 2, p. 15, is headed “**Reproducing results**”; the caption reports **2.8σ/1.9σ** for the 10-bin NGC/SGC cases and **7.3σ/6.9σ** for the 18-bin NGC/SGC cases.[3] Section 3.3, p. 17, concludes that they “**agree nearly perfectly with the 10-bin results**” and “**agree qualitatively with the 18-bin results**.”[3] It adds: “**we are confident that we have reproduced the essential features of the analysis**.”[3]

4. **Why “literally uncontested” is too strong.** The independent pipeline is not numerically identical:[3]
   - Section 3.1, p. 11: its 18-bin case uses [20,160] h⁻¹ Mpc and “**differs slightly from the setup in [1], which uses bins in [20,164] h⁻¹ Mpc**.”[3]
   - Section 2.2, pp. 8–9: its baseline uses CMASS-NGC and CMASSLOWZTOT-SGC; it says the NGC selection matches Hou et al., and it separately tests alternate sample definitions.[3]
   - Section 3.3, pp. 16–17, says the 18-bin reproduction is “**quite sensitive to various analysis choices**.”[3] Turning off the redshift-failure weight drops the NGC result from **7.32σ to 4.26σ**; turning off the fibre-collision correction changes the data χ² strongly and raises the significance to **8.9σ**.[3] Yet the authors’ summary says the high χ² persists and agrees with the original validation tests.[3]

   These are genuine estimator-input/systematics sensitivities, so the exact data vector/statistic is analysis-definition dependent. But the authors do not use them to claim the original odd-vector measurement is erroneous.[3]

5. **The actual rebuttal reuses the measured per-patch 4PCFs and changes the statistic.**[3] Section 4.3, p. 20, explicitly assumes the per-patch odd-4PCF estimator “**is still unbiased**.”[3] Figure 4, p. 22, applies χ²× and χ²null to those measurements: χ²× is consistent with zero, whereas χ²null fails and indicates “**data–mock mismatch**.”[3] Section 5, pp. 26–27, says the original ∼7σ χ² contains a parity term plus a mismatch term caused when the mocks’ parity-even 8PCF gives a biased odd-4PCF covariance; the new statistics separate them.[3]

6. **They do allow a residual systematics possibility, but at the covariance/null-statistic level.**[3] Section 4.5, p. 26, speculates that tension among cross-patch summaries may reflect “undiagnosed systematics” associated with BOSS weights or underestimated error bars.[3] This is not a demonstrated alternative parity-odd vector produced by a corrected window/estimator.[3]

**Check-C reading:** This is the decisive direct replication for Hou’s fine-binned measurement.[3] It establishes that the large original χ² excess is real as a pipeline output; what fails is the inference “large χ² ⇒ parity violation.”[3]

## Original-paper anchors

- Hou, Slepian & Cahn: [arXiv:2206.03625v2](https://arxiv.org/abs/2206.03625v2), *MNRAS* **522** (2023) 5701, [DOI 10.1093/mnras/stad1062](https://doi.org/10.1093/mnras/stad1062).[5]
- Philcox: [arXiv:2206.04227v3](https://arxiv.org/abs/2206.04227v3), *Phys. Rev. D* **106** (2022) 063501, [DOI 10.1103/PhysRevD.106.063501](https://doi.org/10.1103/PhysRevD.106.063501).[6]

Both originals already framed covariance fidelity as a possible failure mode. Hou et al.’s abstract says: “**Our reported significances presume that the mock catalogs used to calculate the covariance sufficiently capture the covariance of the true data.**” Philcox’s abstract similarly says: “**we cannot exclude the possibility that our detection is caused by the simulations not faithfully representing the statistical properties of the BOSS data.**”[5][6]

## Scope boundary: later BOSS parity analysis with a different observable

Gao et al., [arXiv:2604.06021v1](https://arxiv.org/abs/2604.06021v1), is an independent BOSS/DESI **kurto-spectrum** analysis, not a reproduction or correction of the 4PCF data vector.[7] It calls its measurement an “**alternative … approach … than previous 4PCF analyses**” and constructs a much lower-dimensional, physically compressed observable.[7] It therefore supplies a later null cross-check of parity, but it cannot adjudicate whether the original 4PCF vector entries were measured correctly.[7] As of v1 it was prepared for JCAP and had no related journal DOI; its registered arXiv DOI is [10.48550/arXiv.2604.06021](https://doi.org/10.48550/arXiv.2604.06021).[7]

## Bottom-line label for the parent status map

- **Measurement/data vector:** `RECOMPUTED_AND_QUALITATIVELY_REPRODUCED; NOT_BYTE_IDENTICAL`.
- **Central dispute:** `COVARIANCE / MOCK FIDELITY / SIGNIFICANCE STATISTIC`.
- **Secondary caveat:** `ANALYSIS CHOICES AND BOSS WEIGHTS MOVE EXACT χ²; NO PRIMARY PAPER DEMONSTRATES A WINDOW/ESTIMATOR ERROR THAT ERASES THE ODD VECTOR`.
- **Safe prose:** “Follow-up work reproduced the BOSS parity-odd 4PCF excess but found that its nominal significance was not robust to the mock covariance and test statistic.”
- **Unsafe prose:** “Everyone used exactly the same data vector,” or “the measurement itself is completely uncontested.”

## Sources

[1] https://pmc.ncbi.nlm.nih.gov/articles/PMC12169525 — Philcox & Ereza (2025), Could sample variance be responsible...
    > "Given the datasets, 4PCFs are obtained using the encore code [17,61]."
    > "Using the GLAM-UCHUU catalogues, we find no evidence for parity-violation in BOSS, but a strong preference when the 4PCF noise distribution is modelled with the MultiDark-Patchy suite."
[2] https://arxiv.org/abs/2401.09523v1 — Philcox & Ereza, arXiv:2401.09523v1
    > "In this Letter, we test the above assumption."
[3] https://doi.org/10.1088/1475-7516/2024/08/044 — Krolewski et al. (2024), No evidence for parity violation in BOSS
    > "In this section we will define the χ2 statistic, and reproduce the ∼ 7σ and ∼ 3σ results from [1, 2]."
    > "Summarizing, we agree nearly perfectly with the 10-bin results from [2], and agree qualitatively with the 18-bin results from [1]."
[4] https://arxiv.org/abs/2407.03397v1 — Krolewski et al., arXiv:2407.03397v1
    > "This section mostly reviews results from previous papers, especially [1, 2, 4, 34], but is included to establish consistency between our pipeline and previous results, and to make our paper self-contained."
[5] https://arxiv.org/abs/2206.03625v2 — Hou, Slepian & Cahn, arXiv:2206.03625v2
    > "Underestimation of the noise could also lead to a spurious detection."
[6] https://arxiv.org/abs/2206.04227v3 — Philcox, arXiv:2206.04227v3
    > "We cannot exclude the possibility that our detection is caused by the simulations not faithfully representing the statistical properties of the BOSS data."
[7] https://arxiv.org/abs/2604.06021v1 — Gao et al., arXiv:2604.06021v1
    > "In this work, we measure the parity-odd kurto spectra in both BOSS-DR12 and DESI-DR1, together with the corresponding mock catalogues, providing an alternative and potentially more robust approach to searching for parity-violating signatures than previous 4PCF analyses."
