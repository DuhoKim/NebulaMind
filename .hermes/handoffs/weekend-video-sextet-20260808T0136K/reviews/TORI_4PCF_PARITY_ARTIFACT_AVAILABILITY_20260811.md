# TORI — 4PCF parity artifact-availability checks

**Receipt:** `TORI_4PCF_PARITY_ARTIFACT_AVAILABILITY_20260811`  
**Checked:** 2026-08-11  
**Scope:** custody and prior-art facts only. No scientific rerun, no large-product download, no design freeze, no publication, and no assessment of whether a new study is worth doing.

## Decisive result

| Check | Fact result |
|---|---|
| **A — Are public products sufficient for a no-new-measurement rerun?** | **PARTIAL / NOT COMPLETE.** Philcox's 10-bin BOSS vectors, 2,048-mock computed Patchy 4PCFs, analysis notebook, and analytic covariances are public. Krolewski et al.'s archival release supplies 10- and 18-bin BOSS measurements, computed Patchy-mock 4PCFs, analytic covariances, and code. The original Hou/Slepian CADENZA vectors are not deposited by that paper, although Krolewski later independently remeasures the 18-bin case. Most importantly, Philcox & Ereza point to the 1.6-TB GLAM-Uchuu **galaxy catalogues** and public `encore`; I found no cited release of their 2,000 already-computed GLAM 4PCFs or GLAM sample covariance. Reconstructing that published covariance branch therefore reintroduces catalogue-level 4PCF measurement. [1][2][3][4][6][7][11] |
| **B — Is the multiple-covariance comparison already published?** | **YES for the broad study; PARTIAL for a stricter three-way table.** Philcox & Ereza hold the 1,288-element BOSS CMASS measurement and cuts fixed and compare Patchy with GLAM-Uchuu. Their peer-reviewed Table 1 gives **2.9σ versus 1.0σ** for combined CMASS, and their compressed empirical-`T²` comparison gives **1.9σ versus 0.5σ**. Hou et al. separately compare compressed sample, direct Patchy sample, and fitted analytic covariances on a restricted common vector. I found no one-table peer-reviewed substitution of raw analytic, Patchy-sample, and GLAM-sample covariances on the identical full 1,288-element vector under one fixed statistic/projection. [1][4] |
| **C — Is the measured data vector itself disputed?** | **The excess is independently reproduced, but not byte-identically.** Krolewski et al. explicitly reproduce the approximately 7σ and 3σ original-style results and say they reproduce the “essential features.” Their rebuttal targets data–mock covariance/8PCF mismatch and the interpretation of the original χ² statistic. Exact entries and χ² move under documented bin endpoints, sample definitions, random catalogues, BOSS weights, and estimator inputs, so “everyone used exactly the same vector” is not defensible. Philcox & Ereza similarly keep/recompute the BOSS result while changing the mock/noise distribution. [3][4] |

**Custody consequence:** the proposed complete “all published covariance constructions, released products only, no new measurement” packet is not presently closed under public artifacts because the published GLAM branch is catalogue-level, not computed-4PCF-level [4][11]. Separately, the central same-BOSS-vector Patchy-versus-GLAM significance comparison is already in a peer-reviewed paper [4]. These are availability and prior-art findings, not a scientific-value verdict.

---

## 1. Paper identity and scope

### Claim measurements

1. J. Hou, Z. Slepian & R. N. Cahn, “Measurement of parity-odd modes in the large-scale 4-point correlation function of Sloan Digital Sky Survey BOSS DR12 CMASS and LOWZ galaxies,” *MNRAS* **522**, 5701–5739 (2023), DOI [`10.1093/mnras/stad1062`](https://doi.org/10.1093/mnras/stad1062), arXiv [`2206.03625v2`](https://arxiv.org/abs/2206.03625v2). [1]
2. O. H. E. Philcox, “Probing parity violation with the four-point correlation function of BOSS galaxies,” *Phys. Rev. D* **106**, 063501 (2022), DOI [`10.1103/PhysRevD.106.063501`](https://doi.org/10.1103/PhysRevD.106.063501), arXiv [`2206.04227v3`](https://arxiv.org/abs/2206.04227v3). [2]

### Direct BOSS reanalyses

3. A. Krolewski, S. May, K. Smith & H. Hopkins, “No evidence for parity violation in BOSS,” *JCAP* **08** (2024) 044, DOI [`10.1088/1475-7516/2024/08/044`](https://doi.org/10.1088/1475-7516/2024/08/044), arXiv [`2407.03397v1`](https://arxiv.org/abs/2407.03397v1). [3]
4. O. H. E. Philcox & J. Ereza, “Could sample variance be responsible for the parity-violating signal seen in the Baryon Oscillation Spectroscopic Survey?”, *Phil. Trans. R. Soc. A* **383**, 20240034 (2025), DOI [`10.1098/rsta.2024.0034`](https://doi.org/10.1098/rsta.2024.0034), arXiv [`2401.09523v1`](https://arxiv.org/abs/2401.09523v1) [4]. The peer-reviewed journal version is numerically different from the sole arXiv version and is the authority for the values quoted here [4].

### Related papers that do not add another BOSS-galaxy 4PCF covariance branch

- Cabass, Ivanov & Philcox fit inflation templates to the Philcox BOSS vector with Patchy-calibrated compression/covariance; it is not an independent mock-suite comparison [14].
- Adari & Slosar compare data- and simulation-derived covariances for the distinct SDSS DR16 Lyman-α observable, not the BOSS galaxy parity-odd 4PCF vector [13].
- The requested “Ivanov and collaborators” item is therefore claim-side model interpretation, not another direct BOSS measurement rebuttal [14].

---

## 2. Check A — exact public-product custody

### A1. Philcox measured BOSS vectors: public numerical files

Philcox's paper says:

> “This includes the measurements of the 4PCF in observational data and Patchy mocks, as well as the relevant covariance matrices” [2].

The cited repository is [`oliverphilcox/Parity-Odd-4PCF`](https://github.com/oliverphilcox/Parity-Odd-4PCF) [5]. At inspected tree SHA `04606edd621c7e34dd34895fef546c1980b4f275`, the numerical files include [5][6]:

| Product | Exact path/link | Size |
|---|---|---:|
| CMASS NGC measured 4PCF | [`data/boss_cmassN.zeta_4pcf.txt`](https://raw.githubusercontent.com/oliverphilcox/Parity-Odd-4PCF/main/data/boss_cmassN.zeta_4pcf.txt) | 208,573 B |
| CMASS SGC measured 4PCF | [`data/boss_cmassS.zeta_4pcf.txt`](https://raw.githubusercontent.com/oliverphilcox/Parity-Odd-4PCF/main/data/boss_cmassS.zeta_4pcf.txt) | 208,663 B |
| NGC disconnected term | `data/boss_cmassN.zeta_discon_4pcf.txt` | 130,330 B |
| SGC disconnected term | `data/boss_cmassS.zeta_discon_4pcf.txt` | 130,603 B |
| NGC fitted Gaussian covariance | `data/gaussian_cov_patchy_ngc.cov` | 47,874,880 B |
| SGC fitted Gaussian covariance | `data/gaussian_cov_patchy_sgc.cov` | 47,175,444 B |

The raw 4PCF headers identify `Order: 5`, `Bins: 10`, minimum radius `20`, maximum radius `160`, the row/column ordering, and the convention that odd modes store `-i*zeta` [5]. The analysis notebook applies the angular/radial cuts and `ravel()` ordering, yielding 23 odd multiplets × 56 radial triples = **1,288 elements** with multiplet-major/radial-fastest flattening [5]. Compression is defined in the notebook as projection onto inverse-covariance eigenvectors; a separate canonical compressed vector is not deposited [5].

### A2. Philcox computed mock 4PCFs: public, not catalogues

The repository README links two external computed-product files: [6]

| Product | Exact public link | Live response size |
|---|---|---:|
| 2,048 Patchy NGC/SGC computed 4PCFs | [`all_patchy2048_fourpcf.npz`](https://www.dropbox.com/s/594iol702s7gk86/all_patchy2048_fourpcf.npz?dl=1) | **707,798,836 B** |
| 2,048 Nseries/Patchy computed 4PCFs | [`all_nseries-patchy2048_fourpcf.npz`](https://www.dropbox.com/s/r5ezfez15ou93ws/all_nseries-patchy2048_fourpcf.npz?dl=1) | **353,903,968 B** |

Range-only header inspection found `fourpcfN.npy` and `fourpcfS.npy` with shape `(2048,111,120)`, disconnected arrays, and explicit `ells`, `radii`, and `bins` ordering arrays [6]. These are per-mock computed 4PCFs, not mock-galaxy catalogues [6]. The notebook constructs the empirical covariance with `np.cov`; there is no separately named Patchy sample-covariance file [6].

### A3. Original Hou/Slepian release: input catalogues, not derived vectors

Hou et al. state:

> “The GPU-accelerated code CADENZA used to compute the NPCFs is available from the corresponding author upon reasonable request.” [1]

> “The datasets underlying this article are publicly available in the SDSS repository at https://data.sdss.org/sas/dr12/boss/lss/. This includes the BOSS data and MultiDark-Patchy mocks used to measure the 4PCF and covariance matrices.” [1]

The cited SDSS location contains BOSS galaxy/random catalogues and MultiDark-Patchy galaxy/random catalogue tarballs [1]. It does not list a derived `zeta_4pcf`, `.cov`, `.npz`, or equivalent Hou/CADENZA numerical vector product [1]. No author repository or numerical journal supplement for the original measured Hou vectors was located [1]. A later Slepian-led paper calls CADENZA “a proprietary GPU code” [1].

This original release is therefore catalogue-level [1]. It cannot by itself support a no-new-measurement replay of the Hou pipeline [1].

### A4. Krolewski archival release: public 10/18-bin vectors, mocks, covariances, and code

Krolewski et al. say:

> “All data and code needed to reproduce the results in the paper is available at https://zenodo.org/doi/10.5281/zenodo.12537417.” [3]

The versioned record is [`10.5281/zenodo.12537418`](https://doi.org/10.5281/zenodo.12537418), concept DOI `10.5281/zenodo.12537417`, created 2024-06-25, with record license **CC-BY-4.0** [7]. The single file `Parity-Odd-4PCF-regions.zip` is exactly **10,622,877,459 B**, with record checksum MD5 `f9e90ff88074a4d28a6a13e5d7101e4f`; the record's versions endpoint reports one version [7].

The archive preview contains 873 entries [7]. Representative deposited products are [7][8]:

| Archive member | Size |
|---|---:|
| `cov/18bins-160Mpc-cmass-ngc-bessel_improved.jld2.cov` | 4,288,129,689 B |
| `cov/18bins-160Mpc-cmass-sgc-bessel_improved.jld2.cov` | 4,288,129,689 B |
| `out/18_bins/patchy_mocks_DR12CMASS.tar.bz2` | 444,559,361 B |
| `out/18_bins/patchy_mocks.tar.bz2` | 265,717,392 B |
| `out/10_bins/patchy_mocks.tar.bz2` | 149,492,365 B |
| `out/18_bins/boss_cmass_CMASS.tar.bz2` | 24,820,015 B |
| `out/18_bins/boss_cmass.tar.bz2` | 886,514 B |
| `out/10_bins/boss_cmass.tar.bz2` | 3,835,694 B |
| `out/18_bins/chi2_files/*.txt`, `out/10_bins/chi2_files/*.txt` | present |

The deposited README says, “We provide the 4PCF outputs, covariance matrices and code to reproduce all analysis,” and, “Parity-odd four point functions for the data and mocks are in `out`” [8]. It labels `patchy_mocks_DR12CMASS` as all 2,048 CMASS mocks and `patchy_mocks` as the first 500 CMASSLOWZTOT mocks [8].

This is a computed-4PCF release, not only a mock-catalogue release [7][8]. The two large covariance files are analytic covariance outputs; the empirical mock distributions/covariances are reconstructed from the released mock 4PCFs [7][8].

### A5. GLAM-Uchuu branch: catalogue-level only in the published custody chain

Philcox & Ereza state that the 4PCFs are obtained with `encore`, use **2,000 GLAM-Uchuu mocks**, and link the GLAM-Uchuu galaxy catalogues through the Skies & Universes site [4]. Their paper does not cite a DOI, archive, or file containing the 2,000 already-computed GLAM 4PCFs or a GLAM sample covariance [4].

The linked GLAM-Uchuu site labels its files as **galaxy catalogues** and gives the GLAM BOSS/eBOSS data-set size as about **1.6 TB** [11]. The **2,000-mock** count comes from Philcox & Ereza's journal paper, not from the current catalogue page [4]. The site also warns of known catalogue-construction problems for some listed products [11].

No author-linked computed `zeta_4pcf`/NPZ/tar product or GLAM covariance artifact was located in the paper's data-accessibility chain, the cited site, Zenodo targeted records, or author repositories [4][11]. This is a scoped absence finding: the published public path ends at mock galaxy catalogues plus the estimator code [4][11]. Reproducing this covariance/noise branch therefore requires running `encore` over catalogue products [4][11].

### A6. Code and licensing

| Code/data custody item | Public status | Licence fact |
|---|---|---|
| [`oliverphilcox/encore`](https://github.com/oliverphilcox/encore) | Public CPU isotropic NPCF estimator; v1.0 is cited by Philcox. [2][10] | Current master contains MIT; the `v1.0` tag tree itself lacks `LICENSE`. Zenodo record [`13952879`](https://zenodo.org/records/13952879), `oliverphilcox/encore-v1.0.zip`, is 13,844,174 B with MD5 `7496e4d487c835d91af03c7fca3483ad` and record licence CC-BY-4.0. [9][10] |
| CADENZA | Available on request in Hou; later described as proprietary, with no public source repository located. [1] | No public reuse licence. |
| [`oliverphilcox/Parity-Odd-4PCF`](https://github.com/oliverphilcox/Parity-Odd-4PCF) | Analysis notebooks, measured BOSS vectors, fitted covariances; external computed-mock links. [5][6] | No `LICENSE`/`COPYING`, no GitHub-detected licence, no release/tag licence; Dropbox products expose no separate licence. [5][6] |
| [`akrolewski/Parity-Odd-4PCF-regions`](https://github.com/akrolewski/Parity-Odd-4PCF-regions) | GitHub is mainly code; the numerical custody copy is Zenodo. [7][8] | GitHub tree has no separate licence; Zenodo deposit is CC-BY-4.0. [7] |
| [`Socob/Analytic4PC`](https://gitlab.com/Socob/Analytic4PC) | Public Julia analytic parity-odd 4PCF covariance code, used for the Hou/Philcox analyses. [12] | No repository licence field/file located. [12] |
| [`Moctobers/npcf_cov`](https://github.com/Moctobers/npcf_cov) | Public Python analytic 4PCF covariance code; not a measurement estimator. | No repository licence file/API licence located. |

### Check-A sufficiency matrix

| Required ingredient | Philcox 10-bin | Hou original 18-bin | Krolewski reproduction | Philcox–Ereza GLAM branch |
|---|---:|---:|---:|---:|
| Numerical BOSS 4PCF | **Yes** [2][5] | **No author deposit located** [1] | **Yes** [7][8] | Recomputed/held BOSS result described; no separate new deposit [4] |
| Per-mock computed 4PCFs | **Yes, Patchy/Nseries** [6] | **No; SDSS catalogues only** [1] | **Yes, Patchy** [7][8] | **No cited computed GLAM product located** [4][11] |
| Analytic covariance artifact | **Yes** [5] | Not deposited by original paper | **Yes** [7] | Common fiducial metric described, but no new release [4] |
| Analysis/statistic code | **Yes** [5][6] | CADENZA on request/proprietary [1] | **Yes** [7][8] | Method public through `encore`; final GLAM outputs absent [4][10] |
| Ordering/binning/convention sufficient | **Yes** [2][5] | Paper-level description, but no public original vector | **Yes** [3][7][8] | Paper specifies shared 10-bin vector/cuts [4] |
| Explicit reusable licence | **No for analysis/data repo** [5] | **No public code/data product** [1] | **Yes for Zenodo deposit: CC-BY-4.0** [7] | Catalogue-use licence not identified on cited page; no computed-product licence [11] |

---

## 3. Check B — exact prior-art finding

### B1. The central same-input, two-mock-suite comparison is published

Philcox & Ereza use the same 10-bin BOSS CMASS parity-odd measurement: 23 angular multiplets × 56 radial triples = **1,288 elements per sky region** [4]. They use 2,042 usable MultiDark-Patchy mocks and 2,000 GLAM-Uchuu mocks in the peer-reviewed journal analysis [4].

For the fixed rank statistic, the paper holds the BOSS value and fiducial analytic metric fixed and changes the empirical null distribution [4]. Figure 2 states [4]:

> “Using the GLAM-Uchuu catalogues, we find no evidence for parity-violation in BOSS, but a strong preference when the 4PCF noise distribution is modelled with the MultiDark-Patchy suite.” [4]

Peer-reviewed Table 1 reports: [4]

| BOSS subset | GLAM-Uchuu | MultiDark-Patchy |
|---|---:|---:|
| CMASS-N | 1.0σ | 2.5σ |
| CMASS-S | 0.9σ | 2.2σ |
| **CMASS N+S combined** | **1.0σ** | **2.9σ** |

The same paper also compares suite-specific sample covariances after an identical 250-mode projection: 800 mocks from each suite estimate the projected covariance, and remaining mocks form empirical nulls [4]. Its combined CMASS empirical-`T²` result is **0.5σ with GLAM-Uchuu versus 1.9σ with MultiDark-Patchy** [4].

**Version guard:** do not quote the sole arXiv-v1 abstract's 1.4σ combined CMASS+LOWZ value as the published result [4]. The journal paper restricts its final comparison to CMASS and reports 1.0σ versus 2.9σ [4].

### B2. Analytic-versus-sample covariance precedent is also published, but restricted

Hou et al. §5.1.5/Figure 14 reduce the dimension to 10 radial bins and low `ell_max`, then place three treatments in columns: compressed sample covariance, direct Patchy mock covariance, and fitted analytic covariance [1]. The caption says [1]:

> “There is overall good agreement in detection significance between the purely mock-based covariance (central column) and the analytic covariance (right column).” [1]

Their full 18,760-element vector cannot be inverted with the available direct sample covariance, and this comparison uses Patchy only [1].

### B3. Exact boundary of the redundancy finding

- **Already published:** same BOSS 1,288-element measurement/cuts under Patchy versus GLAM nulls, plus a fixed-projection comparison of their sample covariances [4].
- **Already published separately:** analytic versus Patchy sample covariance on a restricted common BOSS vector [1].
- **Not located as one peer-reviewed table:** raw analytic, Patchy-sample, and GLAM-sample covariances substituted on the identical full 1,288-element vector under one unchanged statistic/projection [1][4].

---

## 4. Check C — what follow-ups reproduce and what they dispute

### C1. Philcox & Ereza

They recompute the 10-bin BOSS measurement with `encore`, retain “the BOSS result shown as a vertical red line,” and replace the mock distribution [4]. The same BOSS statistic is 99.6%/2.9σ against Patchy but 69.5%/1.0σ against GLAM-Uchuu [4].

This directly reproduces/accepts the Philcox-style measured excess and disputes the noise distribution [4]. It does **not** directly rerun Hou's complete 18-bin vector; the paper says that extension would be interesting to investigate with GLAM [4].

### C2. Krolewski et al.

Krolewski et al. say:

> “In this section we will define the χ² statistic, and reproduce the ∼7σ and ∼3σ results from [1, 2].” [3]

Their reproduction obtains 2.8σ/1.9σ for the 10-bin NGC/SGC cases and 7.3σ/6.9σ for the 18-bin NGC/SGC cases [3]. They conclude [3]:

> “Summarizing, we agree nearly perfectly with the 10-bin results from [2], and agree qualitatively with the 18-bin results from [1].” [3]

> “we are confident that we have reproduced the essential features of the analysis.” [3]

They then use cross/null statistics to split parity signal from data–mock mismatch, explicitly assuming the per-patch odd-4PCF estimator “is still unbiased” [3]. Their null tests fail while the parity-sensitive cross statistic is consistent with zero; their conclusion is that the original χ² contains a covariance/8PCF mismatch term [3].

The exact 18-bin vectors/statistics are not byte-identical: Krolewski uses `[20,160] h^-1 Mpc` rather than Hou's `[20,164] h^-1 Mpc`, and documents sensitivity to sample selection, randoms, redshift-failure weights, and fibre-collision weights [3]. Those changes move exact χ² values, but the paper does not conclude that an estimator/window error erased the odd vector [3].

### C3. Safe and unsafe custody wording

**Safe:** “Follow-up work independently reproduced the BOSS parity-odd 4PCF excess, but found that its nominal parity-violation significance was not robust to the mock covariance/noise distribution and test statistic.” [3][4]

**Unsafe:** “Every paper used a byte-identical vector,” “the vector is completely uncontested,” or “the rebuttals showed the original 4PCF measurement was fabricated.” [3][4]

---

## 5. What is still unavailable or not closed

1. No public original Hou/CADENZA measured-vector/covariance deposit was located; the paper points to input catalogues and offers CADENZA only on request [1].
2. No cited release of the 2,000 computed GLAM-Uchuu 4PCFs or their sample covariance was located; the public link is to approximately 1.6 TB of galaxy catalogues [4][11].
3. The Philcox analysis/data repository and Dropbox files lack an explicit reuse licence; the Krolewski Zenodo deposit has CC-BY-4.0 [5][6][7].
4. There is no single frozen manifest binding analytic, Patchy, and GLAM covariance products to one identical vector/statistic/projection [1][4].
5. A complete all-published-construction replay from released **derived products only** is therefore not available [4][11]. The missing GLAM computed layer is exactly the catalogue-to-4PCF compute boundary [4][11].

## 6. Custody-only conclusion

- `CHECK_A = PARTIAL_PRODUCTS; COMPLETE_NO_MEASUREMENT_REPLAY_BLOCKED_BY_MISSING_COMPUTED_GLAM_4PCFS`
- `CHECK_B = BROAD_COMPARISON_ALREADY_PUBLISHED; STRICT_FULL_VECTOR_THREE_WAY_TABLE_NOT_LOCATED`
- `CHECK_C = EXCESS_RECOMPUTED_AND_QUALITATIVELY_REPRODUCED; EXACT_VECTOR_NOT_BYTE_IDENTICAL; DISPUTE_IS_COVARIANCE_NULL_MODEL_AND_STATISTIC`

No design was frozen and no scientific products were executed or downloaded in full.

---

## Sources

[1] Hou, Slepian & Cahn, arXiv:2206.03625v2 and MNRAS DOI 10.1093/mnras/stad1062: https://arxiv.org/abs/2206.03625

[2] Philcox, arXiv:2206.04227v3 and Phys. Rev. D DOI 10.1103/PhysRevD.106.063501: https://arxiv.org/abs/2206.04227

[3] Krolewski, May, Smith & Hopkins, JCAP 08 (2024) 044, DOI 10.1088/1475-7516/2024/08/044: https://doi.org/10.1088/1475-7516/2024/08/044

[4] Philcox & Ereza, peer-reviewed PMC full text, DOI 10.1098/rsta.2024.0034: https://pmc.ncbi.nlm.nih.gov/articles/PMC12169525

[5] Philcox parity-odd 4PCF analysis/data repository: https://github.com/oliverphilcox/Parity-Odd-4PCF

[6] Philcox repository README with computed-mock product links: https://raw.githubusercontent.com/oliverphilcox/Parity-Odd-4PCF/main/README.md

[7] Krolewski et al. Zenodo version record/API, DOI 10.5281/zenodo.12537418: https://zenodo.org/api/records/12537418

[8] Krolewski analysis/release README: https://raw.githubusercontent.com/akrolewski/Parity-Odd-4PCF-regions/main/README.md

[9] `encore` v1.0 Zenodo record/API, DOI 10.5281/zenodo.13952879: https://zenodo.org/api/records/13952879

[10] `encore` v1.0 README: https://raw.githubusercontent.com/oliverphilcox/encore/v1.0/README.md

[11] GLAM-Uchuu public galaxy-catalogue page: https://skiesanduniverses.org/Simulations/Uchuu/GalaxyCatalogues

[12] `Socob/Analytic4PC` README: https://gitlab.com/api/v4/projects/Socob%2Fanalytic4pc/repository/files/README.md/raw?ref=master

[13] Adari & Slosar, SDSS DR16 Lyman-α parity analysis: https://arxiv.org/abs/2405.04660

[14] Cabass, Ivanov & Philcox, inflation-template interpretation: https://arxiv.org/abs/2210.16320
