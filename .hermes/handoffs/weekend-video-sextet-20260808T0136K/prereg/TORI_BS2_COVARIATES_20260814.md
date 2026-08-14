# TORI BS-2 COVARIATE PRODUCTS — 2026-08-14

**Slot:** BS-2 — named products, coverage, photo-z, and deblend decision  
**Verdict:** **PASS — 9 OF 10 CORE COVARIATES SURVIVE**  
**Tuning:** none; products and transformations were fixed before the aggregate counts completed.  
**Publication/acceptance:** none.

## Controlling freeze

- Task brief SHA-256: `6431f9cf56fc4732162059e08a97b944a48d2b8ad79dd560d1747342b0c9e190`
- Frozen preregistration SHA-256: `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590`
- Kun re-gate SHA-256: `e5bc40fc4368d813649534dd50dd9fe686b6200c244e7ffe4a457602ba483a66`
- Core rule: at least 8 of the 10 CB-1 covariates must have a named product and cover at least 95% of the accepted sample.
- Conditional public photo-z is declared separately as the possible eleventh covariate.
- Deblend quality is a separate declared decision; it is not counted as one of the ten.

## Coverage proof

The frozen eligible parent has 832,393 rows and the scientific gate requires `N_accepted >= 100,000`. Therefore a product is guaranteed to cover at least 95% of **every** qualifying accepted subset if no more than 5,000 eligible parents lack it:

`worst_case_accepted_coverage = 1 - min(parent_missing, 100000) / 100000`.

This is an absolute-count lower bound. It does not extrapolate from sky area, density, or the observed parent fraction.

## Exact ten-product matrix

| # | Frozen covariate | Exact product/version and transform | Parent available | Parent missing | Worst-case accepted coverage | Decision | Basis |
|---:|---|---|---:|---:|---:|---|---|
| 1 | `imaging_depth` | DESI Legacy DR10 South `survey-bricks-dr10-south.fits.gz` pinned SHA-256 `93c0f928306bf4755ee2397b5817734cf82974d2f9b429eff28a25a867528843`; field `PSFDEPTH_R` | 831,159 | 1,234 | 98.766000% | **SURVIVES** | aggregate per-brick product coverage [3] |
| 2 | `seeing_psf` | same pinned DR10 South brick-summary product; field `PSFSIZE_R` | 831,173 | 1,220 | 98.780000% | **SURVIVES** | aggregate per-brick product coverage [3] |
| 3 | `galactic_extinction` | DESI Legacy DR10.1 South sweeps / `ls_dr10.tractor_s`; `EBV` from SFD98 | 832,393 | 0 | 100.000000% | **SURVIVES** | direct aggregate validity [3] |
| 4 | `stellar_density` | Gaia DR3 `gaiadr3.gaia_source`; `PHOT_G_MEAN_MAG < 19`; counts on the frozen `Nside=128`, RING, ICRS grid; zero is a defined observed-source count | 832,393 | 0 | 100.000000% | **SURVIVES** | structural total coverage [6][7][8][9][12] |
| 5 | `crowding` | DESI Legacy DR10.1 South sweeps / `ls_dr10.tractor_s`; `RA`,`DEC`; neighbour count within 30 arcsec | 832,393 | 0 | 100.000000% | **SURVIVES** | structural for every accepted object because the same bound coordinate is required to request its cutout [3] |
| 6 | `angular_size` | DESI Legacy DR10.1 South sweeps / `ls_dr10.tractor_s`; `SHAPE_R` in arcsec | 832,393 | 0 | 100.000000% | **SURVIVES** | direct aggregate validity [3] |
| 7 | `axis_ratio` | DESI Legacy DR10.1 South sweeps / `ls_dr10.tractor_s`; `SHAPE_E1`,`SHAPE_E2`; freeze `e=sqrt(e1^2+e2^2)`, `b/a=(1-e)/(1+e)` | 832,393 | 0 | 100.000000% | **SURVIVES** | direct aggregate validity [3] |
| 8 | `colour_g_minus_r` | DESI Legacy DR10.1 South sweeps / `ls_dr10.tractor_s`; dereddened `g-r=-2.5 log10[(FLUX_G/MW_TRANSMISSION_G)/(FLUX_R/MW_TRANSMISSION_R)]` | 832,391 | 2 | 99.998000% | **SURVIVES** | direct aggregate validity [3] |
| 9 | `magnitude_r` | DESI Legacy DR10.1 South sweeps / `ls_dr10.tractor_s`; dereddened `r=22.5-2.5 log10(FLUX_R/MW_TRANSMISSION_R)` | 832,393 | 0 | 100.000000% | **SURVIVES** | direct aggregate validity [3] |
| 10 | `arm_contrast` | no product: frozen BS-3 appendix defines only antisymmetric `chi_net`; no `s(x)`, `u(x)`, arm-contrast, or mirror-invariant output | 0 | 832,393 | 0.000000% | **DROP** | machine-audited dropout |

**Survivors:** `9/10`; required `>= 8/10`.  
**Only core dropout:** arm contrast. Its product is absent; `chi_net` was not renamed or averaged after the fact.

## Photo-z decision

**INCLUDE as the conditional eleventh covariate.** The exact product is the DESI Legacy DR10.1 South `10.1-photo-z` sweeps / Data Lab `ls_dr10.photo_z`, field `Z_PHOT_MEDIAN`. The public files documentation says these photo-z sweeps are row-by-row matched to the DR10.1 sweeps and uses `-99` for rows outside its supported input conditions [3]. The frozen Cut-6 predicates already require `0 <= Z_PHOT_MEDIAN < 0.15`; the aggregate census found 832,393/832,393 available, so the worst-case accepted coverage is 100%. This optional covariate is **not** counted among the core ten. The PRLS citation and additional acknowledgement remain required [1].

## Deblend/flag decision

- The frozen selection remains exactly `MASKBITS=0`. This excludes every named `MASKBITS` condition, including `BAILOUT` bit 10 and `SUB_BLOB` bit 16 [5].
- `MASKBITS` and `FITBITS` fields are present for 832,393/832,393 eligible parents.
- **No additional FITBITS exclusion is introduced.** The DR10 documentation describes `FITBITS` as peculiarities of how a source was fit, not as a calibrated deblend-quality scalar [5]. Selecting a post-count subset of those bits would alter the frozen parent without a preregistered interpretation.
- The separate deblend-quality covariate is therefore **DROPPED AND PUBLISHED AS A DROPOUT**. The existing `MASKBITS=0` selection mask remains binding.

## Gaia terms for the stellar-density input

The frozen input is Gaia DR3 `gaia_source`, whose data model says it contains every observed Gaia source in that release and defines `phot_g_mean_mag` [6]; standard public TAP access is available [7]. Gaia data are under CC BY-NC 3.0 IGO [8][12], and the Gaia DR3 acknowledgement is required [9]. This receipt establishes product availability and total grid-domain coverage only; it does not claim astrophysical completeness in crowded regions.

## Aggregate census and independent verification

- Partitions: 67/67 complete
- Rows returned across the wire: 67 aggregate rows, one per fixed BRICKID range
- Eligible-parent population: 832,393, exact match to frozen Cut-6
- Colour-valid: 832,391; missing: 2
- Extinction, angular size, axis ratio, magnitude, flag fields, photo-z: 832,393 each
- Imaging-depth valid: 831,159; missing: 1,234; worst-case accepted coverage 98.766000%
- Seeing valid: 831,173; missing: 1,220; worst-case accepted coverage 98.780000%
- Service-pressure receipts: 0
- Lost-job receipts: 0
- Submission entry point: closed after completion; re-entry refused with the submission count unchanged at 67

The independent verifier rescanned all 67 query hashes, result hashes, one-row schemas, and boundary fields; independently resummed every count; and matched the orchestrator exactly.

## Custody

- Direct coverage: `_tori_parent_row_count_evidence/bs2_covariate_coverage_20260814/FINAL_COVERAGE.json` — SHA-256 `999c89cb56f0da9df1eabb267dcd4825eb587e5d65e5c3c5e1a221c33b538722`
- Brick-product coverage: `_tori_parent_row_count_evidence/bs2_covariate_coverage_20260814/BRICK_PRODUCT_COVERAGE.json` — SHA-256 `4b16ab0a3ef7e0973a755e8b9cfb200064b3a9cde0359b6e324eb1cbc7afed97`
- Arm-contrast product audit: `_tori_parent_row_count_evidence/bs2_covariate_coverage_20260814/ARM_CONTRAST_PRODUCT_AUDIT.json` — SHA-256 `a31b9b982b90ae06de9745e994e5b609c0243b4ebbd2a6adb6c2be6e1d14cf0f`
- Independent final verification: `_tori_parent_row_count_evidence/bs2_covariate_coverage_20260814/FINAL_BS2_VERIFICATION.json` — SHA-256 `fd0f8b2728a6ca0c8a00efe7eb0b4f76e7598c9b87814abc86a2b8c5441f442a`
- Query manifest SHA-256: `5e3303969e91886c328208acdb81cca54ab3036fe277974fce14575cb6f1a809`
- Ordinary aggregate guard SHA-256: `228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51`
- Primary-source pin register: `_tmp_bs1247_source_pins.json` — SHA-256 `fdaa064aa1eab2c03881c1f6bdc16ca574399b3ffe46b8ead72120cc80cf1906`

## Boundary receipt

- Object/sample rows exported: 0
- Positions exported: 0
- Images requested: 0
- Morphology or chirality labels computed: 0
- Sky statistics computed: 0
- Database writes: 0
- Publication, acceptance, cockpit update, commit, push, or merge: none

## Limits retained

This receipt proves preregistration product existence and coverage. It does not compute the covariate maps, match real accepted galaxies, inspect images, or run the Longo estimator. Later authorized production must still apply the frozen complete-case rule and publish the arm-contrast/deblend dropouts without replacement.

## Sources

[1] https://www.legacysurvey.org/acknowledgment
[3] https://www.legacysurvey.org/dr10/files
[5] https://www.legacysurvey.org/dr10/bitmasks
[6] https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html
[7] https://www.cosmos.esa.int/web/gaia-users/archive/programmatic-access
[8] https://www.cosmos.esa.int/web/gaia-users/license
[9] https://gea.esac.esa.int/archive/documentation/GDR3/Miscellaneous/sec_credit_and_citation_instructions
[12] https://www.cosmos.esa.int/web/esdc/terms-and-conditions
