# Public-documentation provenance gate: Pantheon+ / Pantheon+SH0ES and Cosmicflows-4

Grades describe whether the checked primary public documentation supplies the named provenance item. `UNDOCUMENTED` includes an explicitly named missing product or unresolved public-release identity. No category remains `NOT-YET-CHECKED`.

## Primary-source ledger

### Pantheon+ / Pantheon+SH0ES

- **P0 — GitHub release page:** https://github.com/PantheonPlusSH0ES/DataRelease/releases
- **P1 — commit-pinned release root (`c447f0fea703fcd0fff57de5000947b5ca81286b`):** https://github.com/PantheonPlusSH0ES/DataRelease/blob/c447f0fea703fcd0fff57de5000947b5ca81286b/README.md
- **P2 — commit-pinned distance/covariance dictionary:** https://github.com/PantheonPlusSH0ES/DataRelease/blob/c447f0fea703fcd0fff57de5000947b5ca81286b/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/README
- **P3 — Scolnic et al., full data/light-curve release:** https://arxiv.org/abs/2112.03863 ; DOI https://doi.org/10.3847/1538-4357/ac8b7a
- **P4 — Brout et al., cosmological constraints/distances/covariance:** https://arxiv.org/abs/2202.04077 ; DOI https://doi.org/10.3847/1538-4357/ac8e04
- **P5 — Carr et al., coordinates/redshifts/peculiar velocities:** https://arxiv.org/abs/2112.01471 ; DOI https://doi.org/10.1017/pasa.2022.41
- **P6 — Brout et al., SuperCal-Fragilistic calibration:** https://arxiv.org/abs/2112.03864 ; DOI https://doi.org/10.3847/1538-4357/ac8bcc
- **P7 — Riess et al., SH0ES selection/calibration:** https://arxiv.org/abs/2112.04510 ; DOI https://doi.org/10.3847/2041-8213/ac5c5b

### Cosmicflows-4

- **C1 — Tully et al., Cosmicflows-4:** https://arxiv.org/abs/2209.11238 ; DOI https://doi.org/10.3847/1538-4357/ac94d8
- **C2 — CDS/VizieR catalog J/ApJ/944/94 ReadMe:** https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/ReadMe
- **C3 — Extragalactic Distance Database release notice:** https://edd.ifa.hawaii.edu/

## Gate results — Pantheon+ / Pantheon+SH0ES

| Gate item | Grade | Verbatim public evidence / result |
|---|---|---|
| Release identity | **UNDOCUMENTED** | P1: “Data for Pantheon+ is in `Pantheon+_Data`” and “Data for SH0ES is in `SH0ES_Data`.” P0: “There aren’t any releases here.” The repository exposes no release/tag; the evidence above is therefore commit-pinned rather than release-versioned. |
| Row selection | **DOCUMENTED** | P3: “Here we present 1701 light curves of 1550 unique, spectroscopically confirmed Type Ia supernovae”. P4: “after quality cuts are applied (Table 2 of S22), this results in 1701 SN light curves of 1550 unique SNe Ia usable for cosmological constraints.” P7: “Our calibrator sample contains 42 SNe Ia in the 37 Cepheid hosts … and 277 SNe Ia in the Hubble flow, all the objects at 0.0233 < z < 0.15 from the Pantheon+ sample which pass the same quality cuts and are in late-type hosts like the Cepheid calibrators.” P2: “USED_IN_SH0ES_HF - 1 if used in SH0ES 2021 Hubble Flow dataset. 0 if not included.” |
| Coordinates / frame | **DOCUMENTED** | P5 table headers define SN RA, SN Dec, Host RA, and Host Dec in “deg (J2000)”. P2 identifies “RA - Right Ascension”, “DEC - Declination”, “HOST_RA - Host Galaxy RA”, and “HOST_DEC - Host Galaxy DEC”. |
| Redshift fields; heliocentric/CMB conventions | **DOCUMENTED** | P2: “zHD - Hubble Diagram Redshift (with CMB and VPEC corrections)”; “zCMB - CMB Corrected Redshift”; “zHEL - Heliocentric Redshift.” P4: “heliocentric redshifts are required in the SALT2 light-curve fits” and “The peculiar-velocity corrected CMB-frame redshift … is required to compare the inferred distance to a distance predicted by a cosmological model.” |
| Corrected magnitude / distance modulus | **DOCUMENTED** | P2: “m_b_corr - Tripp1998 corrected/standardized m_b magnitude.” P2: “MU_SH0ES - Tripp1998 corrected/standardized distance modulus where fiducial SNIa magnitude (M) has been determined from SH0ES 2021 Cepheid host distances.” P4: “the distance modulus is defined as μ=mB + αx1 − βc − M − δbias + δhost.” |
| Calibration provenance | **DOCUMENTED** | P4: “The outputs of Fragilistic are a best-fit calibration solution for each of the 105 passbands and a joint 105×105 covariance matrix … from using a single common stellar catalog to tie all surveys together (PS1).” P6: “We utilize the large and uniform sky coverage of the public Pan-STARRS stellar photometry catalog to cross-calibrate against tertiary standards released by individual SN Ia surveys.” |
| Selection/bias correction | **DOCUMENTED** | P4: “δbias is a correction term … to account for selection biases that is determined from simulations”. P2 defines `biasCor_m_b`, `biasCorErr_m_b`, `biasCor_m_b_COVSCALE`, and `biasCor_m_b_COVADD`. P4: “These biases are corrected in the δbias term”. |
| Angular completeness / sky-selection function | **UNDOCUMENTED** | No machine-readable angular completeness mask, sky-dependent targeting/confirmation efficiency, or directional bias-correction product is named in P1–P7. P4 names survey simulation inputs as “Cadence,” “DETEFF,” and “SPECEFF,” but not a released angular selection function. |
| Duplicate policy | **DOCUMENTED** | P3: “we do not choose between specific versions of the SNe and instead propagate each fit from each survey, and then include a covariance term between the duplicate SNe in our final covariance matrix used for cosmology.” P4: “each row of the matrix corresponds to an SN light curve” and off-diagonal covariance is included “between entries corresponding to light curves of the same SN … observed by two different surveys.” |
| Covariance semantics | **DOCUMENTED** | P2: “The format of the covariance (.cov) file is NxN lines … (N=1701).” P2: “The STATONLY matrix has only elements that correspond to the statistical distance uncertainties”; “The STAT+SYS matrix also includes all the covariance between SNe (and also Cepheid host covariance) due to systematic uncertainties.” P2 warns: “DO NOT FIT COSMOLOGICAL PARAMETERS WITH THESE UNCERTAINTIES. YOU MUST USE THE FULL COVARIANCE.” |
| Peculiar-velocity / bulk-flow corrections | **DOCUMENTED** | P4: “The baseline corrections are based on 2M++ … with global parameters found in Said et al. (2020) and combined with group velocities estimated from Tully (2015) group assignments.” P4 also documents the 2M++ iLOS and 2MRS alternatives and states: “The two approaches added in quadrature result in an effective σψ²=1.0.” P2 publishes `VPEC`, `VPECERR`, and a VPEC systematic covariance grouping. |

## Gate results — Cosmicflows-4

**Material distinction:** C1 describes a galaxy/group distance compendium using eight distance methodologies, not a Pantheon+ SN-light-curve release: “Eight methodologies are employed”.

| Gate item | Grade | Verbatim public evidence / result |
|---|---|---|
| Release identity | **UNDOCUMENTED** | C3: “The initial release of tables associated with Cosmicflows-4 in August, 2022, were flawed. NOT TO BE USED!” and “The corrected tables were made available online with the publication of the article”. Public counts conflict: C1 abstract says “55,877 galaxies gathered into 38,065 groups”; C1 table description says “38,057 groups”; C3 says “38057 groups”; C2 lists `table3.dat` and `table4.dat` with **38053** records. No revision identifier/checksum reconciles these public counts. |
| Row selection / row-level lineage | **UNDOCUMENTED** | C1 supplies method-specific selections and final tables, but no unified row-level inclusion/exclusion-reason or source-measurement lineage manifest for the merged eight-method compendium is named in C1–C3. C1: “The line entries … provide information on 55,877 individual galaxies”; method distances are supplied “where available”. |
| Coordinates / frame | **DOCUMENTED** | C2: `RAdeg` — “Right Ascension, decimal degree (J2000)” and `DEdeg` — “Declination, decimal degree (J2000)”; it also defines Galactic `GLON/GLAT` and supergalactic `SGL/SGB`. |
| Redshift fields; heliocentric/CMB conventions | **DOCUMENTED** | The release provides velocities rather than dimensionless redshift fields. C2 defines `Vh` as group velocity “relative to the Sun”, `Vls` as group velocity “relative to Local Sheet”, and `V3k` as group velocity “relative to cosmic background”. |
| Corrected magnitude / distance modulus | **DOCUMENTED** | C2 defines `DMav` as “Group, weighted average distance modulus” and `Dist` as the corresponding luminosity distance; it also defines method-specific moduli (`DMsnIa`, `DMtf`, `DMfp`, `DMsbf`, `DMsnII`, `DMtrgb`, `DMceph`, `DMmas`). C1: “Individual distance moduli and uncertainties are given, where available, for each of the methodologies”. |
| Calibration provenance | **DOCUMENTED** | C1: the weighted average is “all on the absolute scaling established by the combined TRGB, CPLR, and MASER calibrators.” C1: “our cumulative sample of zero-point calibrators will consist of 489 galaxies with TRGB distance estimates … 76 galaxies with CPLR distances … and six maser distances”. |
| Selection/bias correction | **DOCUMENTED** | For 6dFGSv, C1: “we correct for this problem by modifying the magnitude limit used in the Malmquist bias correction/normalization of each galaxy's PDF.” C1: “The distance moduli accepted into Cosmicflows-4 incorporate both the revised bias corrections and the morphological corrections”. For SDSS FP, C1 says the PDF normalization “encodes the selection bias”. |
| Angular completeness / sky-selection function | **UNDOCUMENTED** | C1 documents uneven footprints—e.g. “Undersampling in the celestial south accounts for the underrepresentation of events at supergalactic longitudes 180°–270°”—but C1–C3 name no merged machine-readable angular completeness/selection mask or per-method sky selection-function product. |
| Duplicate / overlap policy | **DOCUMENTED** | C1: “There are considerable overlaps between these and the earlier contributions”. For catalog merging, C1: “The best offset parameters minimize the total deviation of adjusted object distance moduli (groups and individual galaxies) from the weighted distance modulus averages offered by all samples together.” C1 says the 15 SN-Ia samples “are merged in a manner analogous” to this MCMC procedure. Group construction priority is also specified: Kourkchi et al. (2017), Tully (2015), then Tempel et al. (2017). |
| Covariance semantics | **DOCUMENTED** | C1: “We assume that all measured object distances are independent with Gaussian uncertainties.” C2 provides per-row distance-modulus uncertainties, but no inter-object covariance matrix. |
| Peculiar-velocity / bulk-flow corrections | **DOCUMENTED** | C2 defines `Vpds` as “Peculiar velocity, Equation 9, Davis & Scrimgeour (2014)” and `Vpwf` as “Peculiar velocity, Equation 10, Watkins & Feldman (2015).” C1 gives `Vpec^ds = (f Vcmb − H0 d)/(1 + H0 d/c)` and `Vpec^wf = [f Vcmb/(1+f Vcmb/c)] log(f Vcmb/H0 d)`, with a ramp ending at `Vls=3000 km/s`. For 6dFGSv, C1 says the revised magnitude limit is used “while also substantially reducing the difference between the adjusted and measured bulk flows.” |

## Missing directional-systematics products named by the gate

### Pantheon+ / Pantheon+SH0ES

1. Machine-readable angular completeness / targeting / spectroscopic-confirmation selection mask by survey.
2. Sky-position-dependent bias-correction surfaces or directional selection-efficiency realizations.
3. Directional photometric-calibration residual map / focal-plane-to-sky zeropoint product; the public calibration product is passband-level covariance.
4. Peculiar-velocity reconstruction posterior/ensemble or sky-space covariance beyond the released aggregate VPEC systematic covariance grouping.
5. Per-row coordinate-source lineage and RA/DEC uncertainty product.
6. Explicit duplicate-group identifier/crossmatch manifest linking the 1701 light-curve rows to the 1550 unique SNe.

### Cosmicflows-4

1. Reconciled corrected-release manifest with immutable revision, checksums, and one authoritative group-row count.
2. Unified per-row source-measurement lineage and inclusion/exclusion-reason manifest across all eight methodologies.
3. Machine-readable angular completeness / sky-selection mask for each constituent methodology and for the merged compendium.
4. Sky-dependent residual-bias map or released anisotropy/null simulation ensemble for the merged catalog.
5. Inter-object covariance matrix, shared calibration-zero-point covariance, or posterior samples for the merged distance moduli.
6. Peculiar-velocity / bulk-flow covariance or full flow-field posterior ensemble for the released group velocities.
7. Group-membership probability/ambiguity product for direction-dependent grouping uncertainty.

## Grade inventory

- **Pantheon+ / Pantheon+SH0ES:** DOCUMENTED — row selection, coordinates/frame, redshift conventions, corrected magnitudes/distance modulus, calibration provenance, selection/bias correction, duplicate policy, covariance semantics, peculiar-velocity/bulk-flow corrections. UNDOCUMENTED — immutable release identity; angular completeness/sky-selection product.
- **Cosmicflows-4:** DOCUMENTED — coordinates/frame, velocity-frame conventions, distance modulus, calibration provenance, selection/bias correction, duplicate/overlap policy, covariance independence semantics, peculiar-velocity/bulk-flow corrections. UNDOCUMENTED — reconciled immutable release identity; unified row-level selection/lineage; angular completeness/sky-selection product.
- **NOT-YET-CHECKED:** none.
