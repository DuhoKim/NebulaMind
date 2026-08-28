# Check B — Has the BOSS parity-odd 4PCF multi-covariance significance comparison already been published?

**Checked:** 2026-08-11  
**Scope:** primary claim/reanalysis papers and their appendices/supplements; same BOSS parity-odd galaxy 4PCF measured vector under analytic, sample, and/or multiple-mock-suite covariance treatments.

## Bottom line

**Yes for the broad comparison; only partial for the strict all-covariances-on-one-full-vector design.**

1. **The broad result is already peer-reviewed and published.** Philcox & Ereza apply the same measured BOSS CMASS parity-odd 4PCF vector and the same cuts to two independently constructed mock suites, MultiDark-Patchy and GLAM-Uchuu. Their published **Table 1** gives the fixed-statistic rank comparison, while **Figure 4 and §3** give a compressed empirical-sample-covariance comparison. The inferred combined CMASS significance changes from **2.9σ (Patchy) to 1.0σ (GLAM-Uchuu)** in the rank test, and from **1.9σ to 0.5σ** using the empirical compressed-`T²` distributions. This is the direct published precedent for “hold the BOSS measurement/conventions fixed and change the mock/covariance construction.”
2. **Hou, Slepian & Cahn had already published a three-method covariance check using one mock suite.** Their **§5.1.5 and Figure 14** apply compressed sample covariance, direct sample covariance, and analytic covariance to the same *restricted* low-`ℓmax`, 10-radial-bin BOSS vectors; the caption reports good agreement specifically between the direct mock covariance and fitted analytic covariance. Their full 18,760-element vector could not be treated with a direct sample covariance.
3. **I did not find a single peer-reviewed table that applies all of the following as interchangeable covariance matrices to the identical uncompressed 1,288-element BOSS vector under one fixed statistic/projection:** raw analytic Gaussian covariance, Patchy sample covariance, and GLAM-Uchuu sample covariance. The published literature splits that stricter design across the two papers above. In Philcox & Ereza, the analytic covariance is a common fiducial metric/projection; the final null significances come from mock distributions or mock-estimated compressed covariances. In Hou et al., the direct analytic-vs-sample comparison is restricted in dimensionality and contains Patchy only.

Thus, if “Lana’s proposed comparison” means **the same BOSS 4PCF measurement under multiple mock/covariance suites**, it already exists. If it means the narrower **one-table, full-vector, strictly fixed-convention three-way analytic/Patchy/GLAM covariance substitution**, I found only partial precedents, not that exact complete matrix.

---

## Direct published precedent: Philcox & Ereza

**O. H. E. Philcox & J. Ereza, “Could sample variance be responsible for the parity-violating signal seen in the Baryon Oscillation Spectroscopic Survey?”**  
*Philosophical Transactions of the Royal Society A* **383**, 20240034 (2025), published online 13 Feb 2025.  
DOI: [10.1098/rsta.2024.0034](https://doi.org/10.1098/rsta.2024.0034)  
arXiv: [2401.09523v1](https://arxiv.org/abs/2401.09523v1), submitted 17 Jan 2024. **Version warning:** the only arXiv version is not numerically identical to the later journal article; see below.

### Identical data vector/conventions

Published **§2, “Methods”**:

- Both analyses use the same BOSS CMASS-N and CMASS-S parity-odd 4PCF measurement, **23 angular multiplets × 56 radial-bin triplets = 1,288 elements per sky region**, with the same 10 radial bins covering 20–160 `h⁻¹ Mpc`.
- MultiDark-Patchy: 2,042 usable mocks in the journal analysis.
- GLAM-Uchuu: 2,000 mocks.
- The paper’s statistical tests assess whether the measured BOSS 4PCF is consistent with the empirical null distribution supplied by a given mock suite.

### Fixed-statistic mock-suite comparison

Published **§2**, eq. (2.1), **Figures 1–2**, and **Table 1**:

- A common analytic covariance `C_fid` is used only as the fixed metric in `\tildeχ² = ζᵀ C_fid⁻¹ ζ` for BOSS and every realization from each suite.
- The BOSS value is held fixed while the empirical null distribution is changed. The **Figure 2** caption states: **“Using the GLAM-Uchuu catalogues, we find no evidence for parity-violation in BOSS, but a strong preference when the 4PCF noise distribution is modelled with the MultiDark-Patchy suite.”**
- **Figure 1** measures the mock-suite variance difference. After the required CMASS-N effective-volume rescaling, its caption says that **GLAM-Uchuu variance exceeds MultiDark-Patchy by 10–20% in both samples**.

**Table 1 rank-test significances** (`GLAM-Uchuu`, `MultiDark-Patchy`):

| BOSS subset | GLAM-Uchuu | MultiDark-Patchy |
|---|---:|---:|
| CMASS-N | 1.0σ | 2.5σ |
| CMASS-S | 0.9σ | 2.2σ |
| **CMASS N+S combined** | **1.0σ** | **2.9σ** |

The combined result uses the paper’s effective-volume-weighted combination of the N and S statistics; it is not a concatenated 2,576-element inversion.

### Sample-covariance comparison after identical compression

Published **§2**, eq. (2.2), **Figure 4**, and **§3**:

- For each BOSS sky chunk, a 250-mode projection `Π` is defined from the same fiducial analytic-covariance prescription and used in both mock-suite analyses.
- For each suite separately, **800 mocks** estimate the covariance of the same projected BOSS vector; the remaining mocks form the empirical null distribution.
- This is a direct comparison of **two sample covariance matrices** on the same 250-dimensional compressed BOSS vector with one fixed projection.

**Figure 4 / §3 compressed empirical-`T²` result:** **0.5σ (GLAM-Uchuu) versus 1.9σ (MultiDark-Patchy)** for combined CMASS. The journal article does not tabulate per-chunk `T²` values.

Published **§3, “Results”** says that Figure 4 compares the projected BOSS vector with empirical `T²` distributions built from the GLAM-Uchuu and MultiDark-Patchy covariances; it gives **0.5σ** and **1.9σ**, respectively, and concludes that the GLAM-Uchuu analysis has no significant parity-violation evidence. Published **§4** summarizes the baseline as **1.0σ** with GLAM-Uchuu and explicitly treats the variation between two differently produced but similarly calibrated mock catalogues as evidence that the pipeline’s significance is mock-sensitive.

### ArXiv-v1/journal numerical difference

Do not cite the arXiv abstract’s **1.4σ** as the journal result. In [arXiv:2401.09523v1](https://arxiv.org/html/2401.09523v1), **Table 1** combines CMASS and LOWZ and gives:

- Rank test, all four data chunks: **1.4σ (GLAM-Uchuu) vs >3.5σ (Patchy)**.
- Empirical `T²`, all four chunks: **2.1σ vs 2.7σ**.

The peer-reviewed journal article restricts its final table to CMASS and gives **1.0σ vs 2.9σ** (rank) and **0.5σ vs 1.9σ** (empirical `T²`). The arXiv record still lists only v1.

---

## Earlier partial precedent: Hou, Slepian & Cahn

**J. Hou, Z. Slepian & R. N. Cahn, “Measurement of parity-odd modes in the large-scale 4-point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies.”**  
*MNRAS* **522**, 5701–5739 (2023).  
DOI: [10.1093/mnras/stad1062](https://doi.org/10.1093/mnras/stad1062)  
arXiv: [2206.03625v2](https://arxiv.org/abs/2206.03625v2), revised 8 Feb 2023.

### Three covariance constructions are explicitly compared

- **§4.3.1 / §5.1.1 / Table 2:** full 18,760-element BOSS vectors analyzed with a fitted analytic Gaussian covariance. `Table 2` gives the headline combined analytic-covariance significances: **CMASS 7.1σ** and **LOWZ 5.8σ** (`C_tot`; their final conservative headline later reports LOWZ 3.1σ after compressed analysis).
- **§4.3.3 / §5.1.4 / Figure 13:** theoretical-eigenbasis compression followed by Patchy sample covariance. With 100 eigenmodes, the text reports **CMASS N+S 4.0σ (`T²`) / 3.9σ (Gaussian fit)** and **LOWZ N+S 3.1σ / 3.5σ**.
- **§4.3.4 / §5.1.5 / Figure 14:** dimension is reduced to 10 radial bins and `ℓmax = 1` or `2`, allowing the Patchy covariance to be inverted directly. The figure’s columns are explicitly: **left, compressed sample covariance; centre, direct mock covariance; right, fitted analytic covariance**. Caption quote: **“There is overall good agreement in detection significance between the purely mock-based covariance (central column) and the analytic covariance (right column).”**

This is an actual same-vector multi-covariance check *within each row of Figure 14*, but it is not the full vector and it has only one empirical suite (Patchy). Also, the analytic covariance is fitted to Patchy through effective-volume/power-spectrum/shot-noise parameters, so it is not wholly mock-independent.

---

## Other primary claim/rebuttal papers

### Philcox 2022 claim: two covariance roles, one suite

**O. H. E. Philcox, “Probing parity violation with the four-point correlation function of BOSS galaxies.”**  
*Phys. Rev. D* **106**, 063501 (2022). DOI: [10.1103/PhysRevD.106.063501](https://doi.org/10.1103/PhysRevD.106.063501). arXiv: [2206.04227v3](https://arxiv.org/abs/2206.04227v3), revised 15 Mar 2023.

- **§III.A and Figure 4:** fixed analytic proxy covariance in the pseudo-`χ²` statistic; Patchy mocks provide the rank null. Result: **2.9σ** joint CMASS.
- **§III.B and Figure 5:** analytic-covariance eigenvectors define the compression, and the compressed covariance is estimated from Patchy. At 50 modes: **1.3σ N, 1.7σ S, 1.9σ joint**; the joint value rises to about **3.9σ at 100 modes**.
- **Figure 3** shows the true/mock covariance amplitude is approximately twice the idealized model for most modes.

This compares analysis/covariance roles, but not independent mock suites, and it does not substitute multiple raw covariances under a single unchanged significance statistic.

### Krolewski, May, Smith & Hopkins 2024 rebuttal: one mock suite throughout

**A. Krolewski, S. May, K. Smith & H. Hopkins, “No evidence for parity violation in BOSS.”**  
*JCAP* **08** (2024) 044. DOI: [10.1088/1475-7516/2024/08/044](https://doi.org/10.1088/1475-7516/2024/08/044). arXiv: [2407.03397v1](https://arxiv.org/abs/2407.03397v1), submitted 3 Jul 2024.

- **§1.2** is unambiguous: **“Following [1,2], we have used the MultiDark-PATCHY BOSS mock catalogs … throughout this paper.”**
- **Figure 1** reproduces the approximately 7σ original statistic using an analytic covariance as the quadratic metric and Patchy to calibrate the null.
- Their new cross/null statistics give a parity signal from **0 to 2.5σ**, with data–mock mismatch around 6σ; **§4.4 / Appendix E** reports null-test failures of **5.6σ (CMASS-NGC) and 6.8σ (CMASSLOWZTOT-SGC)**.
- **Appendix D, Figures 10–11** studies analytic-covariance conditioning, not replacement by a second covariance suite.

This is a different-statistic rebuttal, not a multi-covariance comparison. The paper itself cites the Philcox–Ereza mock-suite result in **§1.1**, saying a different mock set shifted significance by about 2σ.

### Cabass, Ivanov & Philcox 2023: model fitting, not multi-covariance significance

**G. Cabass, M. M. Ivanov & O. H. E. Philcox, “Colliding Ghosts: Constraining Inflation with the Parity-Odd Galaxy Four-Point Function.”**  
*Phys. Rev. D* **107**, 023523 (2023). DOI: [10.1103/PhysRevD.107.023523](https://doi.org/10.1103/PhysRevD.107.023523). arXiv: [2210.16320v3](https://arxiv.org/abs/2210.16320v3), revised 15 Mar 2023.

- **§III.A** fixes `N_eig = 100` from the theoretical covariance eigenbasis, with the analytic covariance’s effective volume, number density and power-spectrum amplitude calibrated to Patchy.
- The likelihood covariance of the compressed vector is estimated from all **2,048 Patchy** mocks.
- An Nseries mean vector is used as a validation/systematics test, not as an alternative covariance.
- **Table I** reports all 18 inflation-template amplitudes below 2σ.

No same-vector significance comparison across multiple covariance matrices/mock suites is present.

### Cahn, Slepian & Hou 2023 framework paper

**R. N. Cahn, Z. Slepian & J. Hou, “A Test for Cosmological Parity Violation Using the 3D Distribution of Galaxies.”**  
*Phys. Rev. Lett.* **130**, 201002 (2023). DOI: [10.1103/PhysRevLett.130.201002](https://doi.org/10.1103/PhysRevLett.130.201002). arXiv: [2110.12004v1](https://arxiv.org/abs/2110.12004v1).

This establishes the parity-odd 4PCF test and analytic-covariance formalism; it does not analyze the measured BOSS parity-odd vector under competing covariance constructions.

### Adari & Slosar 2024: a genuine covariance cross-check, but a different observable and survey tracer

**P. Adari & A. Slosar, “Searching for parity violation in SDSS DR16 Lyman-α forest data.”**  
*Phys. Rev. D* **110**, 103534 (2024). DOI: [10.1103/PhysRevD.110.103534](https://doi.org/10.1103/PhysRevD.110.103534). arXiv: [2405.04660v2](https://arxiv.org/abs/2405.04660v2), revised 21 Nov 2024.

This is not the BOSS galaxy 4PCF vector, but it contains the closest cross-dataset covariance precedent:

- **§III.B / Figures 2–3:** compares data-derived/jackknife error estimates to **5,000 LyaCoLoRe** simulations.
- **§III.C / Figure 4:** mock principal components plus patch bootstrap covariance.
- **Appendix A / Figures 6–7 / Table 1:** recomputes the same Lyman-α data tests using covariance from data (`cov_data`) and simulations (`cov_sim`). Table 1 gives `(cov_data, cov_sim)`: original-estimator `Δχ² = (0.20, 0.20)`, hybrid `Δχ² = (1.02, 1.05)`, and normalized `χ² = (1.19, 1.18)`.
- Their main null p-values are **21.2%** (original) and **6.4%** (hybrid).

This demonstrates the general multi-covariance design, but it cannot be cited as an existing comparison of the BOSS galaxy parity-odd 4PCF measurement.

---

## Related items that do not duplicate the BOSS 4PCF comparison

- Taylor, Craigie & Ting, *Phys. Rev. D* **109**, 083518 (2024), DOI [10.1103/PhysRevD.109.083518](https://doi.org/10.1103/PhysRevD.109.083518), arXiv [2312.09287v1](https://arxiv.org/abs/2312.09287v1), and Craigie et al., *Phys. Rev. D* **112**, 023503 (2025), DOI [10.1103/1knk-j9j9](https://doi.org/10.1103/1knk-j9j9), arXiv [2405.13083v1](https://arxiv.org/abs/2405.13083v1): unsupervised parity methods demonstrated on toy/mock fields, not a reanalysis of the measured BOSS 4PCF vector.
- Gao et al., **arXiv:2604.06021v1** (7 Apr 2026), “Testing parity with composite-field spectra of BOSS and DESI luminous red galaxies”: explicitly estimates BOSS covariances from both Patchy and Uchuu, but for new low-dimensional **kurto-spectrum** vectors, not the Hou/Philcox 4PCF vector. The arXiv record says “Prepared for submission to JCAP” and lists no journal DOI as of this check.

## Scope answer in one sentence

**Published literature already contains (a) an exact same-BOSS-vector, two-mock-suite significance comparison and (b) a same-restricted-vector analytic-versus-sample covariance comparison; it does not appear to contain one controlled, full-uncompressed-vector table that simultaneously substitutes raw analytic, Patchy-sample, and GLAM-Uchuu-sample covariances under a single identical statistic/projection.**
