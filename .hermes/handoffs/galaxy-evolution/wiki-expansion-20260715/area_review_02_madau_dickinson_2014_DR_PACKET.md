# Review Base 02 canonical advisory packet — Madau & Dickinson 2014

status: READY_FOR_HWAO_REVIEW
advisory_only: true
wiki_write_performed_by_tori: false
canonical_source_base_not_live_wiki_prose: true
raw_packet_sha256: ef029656480cfc3867cfef85999be5a9a812bd6b48907df141cead8d98d7a36f
source_registry_status: PASS
usable_sources: 44
primary_sources: 40
supporting_reviews_or_proceeding: 4

## 1. Review identity and scope map

[REV02] Madau, Piero & Dickinson, Mark (2014, Annual Review of Astronomy and Astrophysics) | title=Cosmic Star-Formation History | DOI:10.1146/annurev-astro-081811-125615; arXiv:1403.0007; ADS:2014ARA&A..52..415M | role=review_synthesis | trust_score=0.98 | boundary=2014 review-level synthesis; retain tracer, IMF, dust, luminosity-limit, redshift, cosmology, and model assumptions.

- Cosmic SFR density: supports a bounded multi-tracer synthesis and analytic fit; it does not make any one survey complete.
- UV and IR luminosity functions: support tracer-specific measurements after explicit integration, dust, and faint-end assumptions; observed luminosity density is not identical to total SFR density.
- Stellar-mass density: supports comparison with the time integral of prior star formation; agreement is approximate and model-dependent rather than exact closure.
- IMF and stellar populations: support explicit conversion and recycling conventions; the review does not establish a universal IMF observationally.
- Chemical evolution: supports IMF- and yield-dependent metal accounting; closed-box curves are models rather than direct global metallicity observations.
- Reionization: supports photon-budget constraints; escape fraction, IGM clumping, and the unobserved faint end remain decisive unknowns.
- AGN-centered mechanics, post-2014 surveys, and JWST-era revisions are outside this packet's usable boundary.

## 2. Established findings

[REV02-E01]
- role: established
- epistemic_type: review_synthesis
- atomic finding: A multi-survey UV+IR synthesis rises from the present to a broad maximum near z~2 and declines toward higher redshift; the review's analytic fit peaks near z~1.9 and gives an approximately 3.9 Gyr late-time e-folding decline.
- scope/boundary: Salpeter-normalized review fit to heterogeneous luminosity-density measurements; peak position and normalization depend on fit form, dust corrections, integration limits, and cosmology.
- review basis: Abstract; Section 5.1; Equation 15; Figure 9.
- confidence note: High for the broad rise-and-fall shape, lower for an exact peak redshift.
- source keys: [REV02], [REV02-P003], [REV02-P005], [REV02-P015], [REV02-P042]
- trust_score: 0.94

[REV02-E02]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Under the review's adopted history and recycling assumptions, roughly half of today's stellar mass had formed by z~1.3 and roughly one quarter formed above z~2.
- scope/boundary: Integrated cosmic history, not a direct count of formation times for individual galaxies; systematic errors in stellar masses, dust, IMF, and mass return propagate into the fractions.
- review basis: Abstract; Sections 5.1 and 5.3; Figures 9 and 11.
- confidence note: Moderate; treat the fractions as synthesis landmarks, not exact closure constraints.
- source keys: [REV02], [REV02-P018], [REV02-P019], [REV02-P044]
- trust_score: 0.88

[REV02-E03]
- role: established
- epistemic_type: review_synthesis
- atomic finding: The review infers that less than about one percent of present-day stellar mass formed during z>6.
- scope/boundary: Depends on extrapolated high-redshift UV luminosity functions and assumed dust and IMF; it is not a direct complete census of ultra-faint galaxies.
- review basis: Abstract; Section 6.
- confidence note: Moderate.
- source keys: [REV02], [REV02-P010], [REV02-P011], [REV02-P012]
- trust_score: 0.84

[REV02-E04]
- role: established
- epistemic_type: review_synthesis
- atomic finding: The observed stellar-mass-density history is broadly consistent with the integral of preceding SFR density after stellar mass return is included, but a residual offset remains.
- scope/boundary: Consistency depends on common IMF, stellar-population synthesis, dust, star-formation histories, and recycling assumptions.
- review basis: Section 5.3; Figure 11.
- confidence note: High for broad consistency; moderate for normalization.
- source keys: [REV02], [REV02-P018], [REV02-P021], [REV02-P022], [REV02-P024], [REV02-P044]
- trust_score: 0.91

[REV02-E05]
- role: established
- epistemic_type: calibration
- atomic finding: Rest-frame FUV luminosity around 1500 Å traces recent formation of massive stars before dust correction for a specified IMF and star-formation history.
- scope/boundary: Continuous-star-formation calibrations fail for sufficiently bursty or very young systems; dust correction is separate.
- review basis: Sections 3.1 and 4.1.
- confidence note: High within calibration assumptions.
- source keys: [REV02], [REV02-P001], [REV02-P002], [REV02-P041]
- trust_score: 0.96

[REV02-E06]
- role: established
- epistemic_type: observation
- atomic finding: Infrared measurements show that dust-obscured activity is a major, and near cosmic noon dominant, component of the total star-formation budget.
- scope/boundary: Population-integrated 8-1000 micron luminosity functions and extrapolations; confusion, template conversion, and UV/IR overlap matter.
- review basis: Sections 4.2 and 5.1; Figure 9; Table 1.
- confidence note: High for a large obscured contribution, lower for an exact fraction at every redshift.
- source keys: [REV02], [REV02-P013], [REV02-P014], [REV02-P015], [REV02-P016], [REV02-P017], [REV02-P030]
- trust_score: 0.94

[REV02-E07]
- role: established
- epistemic_type: observation
- atomic finding: High-redshift rest-frame UV luminosity functions have steep faint-end slopes, near alpha~-2 around z~7 in the cited HST samples.
- scope/boundary: Dropout-selected fields with strong completeness, size, cosmic-variance, and functional-form dependence; extrapolation below detection is not observed.
- review basis: Section 5.1; Table 1.
- confidence note: Moderate to high for a steep observed slope, moderate for its exact value.
- source keys: [REV02], [REV02-P010], [REV02-P011], [REV02-P012]
- trust_score: 0.90

[REV02-E08]
- role: established
- epistemic_type: calibration
- atomic finding: Salpeter- and Chabrier-like IMFs imply materially different SFR normalizations, stellar mass return fractions, and metal yields.
- scope/boundary: Model-dependent integrated IMFs and instantaneous recycling; this does not prove either IMF universal.
- review basis: Section 2; Equations 6-8.
- confidence note: High as a conversion dependency.
- source keys: [REV02], [REV02-P031], [REV02-P032], [REV02-P033], [REV02-P035]
- trust_score: 0.95

[REV02-E09]
- role: established
- epistemic_type: observation
- atomic finding: Core-collapse supernova rates provide an independent massive-star check on SFR histories, while the cited data also show a normalization shortfall relative to simple predictions.
- scope/boundary: Progenitor-mass limits, dust-hidden events, failed supernovae, survey control times, and small samples remain important.
- review basis: Section 5.2; Figure 10.
- confidence note: High for tracer relevance; moderate for the size and origin of the discrepancy.
- source keys: [REV02], [REV02-P025], [REV02-P026]
- trust_score: 0.91

[REV02-E10]
- role: established
- epistemic_type: measurement
- atomic finding: Rest-frame optical and near-IR surveys are essential for estimating accumulated stellar mass and its redshift evolution.
- scope/boundary: Mass-to-light ratios depend on age, metallicity, dust, star-formation history, IMF, and TP-AGB treatment; near-IR light is not a model-free mass measurement.
- review basis: Sections 3.2 and 5.3; Table 2.
- confidence note: High for method necessity, moderate for absolute masses.
- source keys: [REV02], [REV02-P018], [REV02-P019], [REV02-P022], [REV02-P024], [REV02-P044]
- trust_score: 0.92

[REV02-E11]
- role: established
- epistemic_type: theory
- atomic finding: Integrating star formation with an IMF-dependent yield links the cosmic SF history to a predicted metal-production history.
- scope/boundary: Yield tables, stellar rotation/binarity, black-hole mass cuts, gas flows, and closed-box assumptions limit interpretation.
- review basis: Sections 2, 5.5, and 5.6.
- confidence note: High for the accounting identity, moderate for absolute yields.
- source keys: [REV02], [REV02-P033], [REV02-P035], [REV02-P039], [REV02-P040]
- trust_score: 0.88

[REV02-E12]
- role: established
- epistemic_type: theory
- atomic finding: Galaxy-driven reionization is a photon-budget problem coupling high-z UV luminosity density to ionizing production efficiency, escape fraction, and IGM recombination.
- scope/boundary: Detected bright galaxies alone do not close the budget without assumptions about faint galaxies and escape; quasar mechanics are not promoted here.
- review basis: Section 5.8.
- confidence note: High for the accounting framework, low-to-moderate for closure parameters.
- source keys: [REV02], [REV02-P011], [REV02-P037], [REV02-P038], [REV02-P043]
- trust_score: 0.91

## 3. Open debates and tensions

[REV02-D01] | role=debate | topic=High-z decline versus incompleteness | positions=The observed drop toward z>6 may be largely physical versus substantially amplified by galaxies below HST detection and selection limits. | unresolved=The faint-end turnover, completeness, sizes, and cosmic variance were not directly measured. | boundary=Dropout UV luminosity functions, not a complete bolometric census. | source keys=[REV02], [REV02-P010], [REV02-P011], [REV02-P012], [REV02-P028] | trust_score=0.90
[REV02-D02] | role=debate | topic=Dust correction at high redshift | positions=Apply locally calibrated UV-slope attenuation relations versus allow different dust geometry, composition, and star-formation history. | unresolved=Representative far-IR constraints for ordinary z>4 galaxies were inadequate in 2014. | boundary=UV-selected galaxies; IRX-beta is an empirical calibration, not a universal law. | source keys=[REV02], [REV02-P009], [REV02-P041] | trust_score=0.89
[REV02-D03] | role=debate | topic=UV+IR combination | positions=Add unobscured UV and obscured IR components versus infer totals with joint SED/energy-balance models. | unresolved=Matched, mass-complete UV-to-far-IR samples were limited, and templates/overlap can bias totals. | boundary=Population totals around cosmic noon. | source keys=[REV02], [REV02-P015], [REV02-P016], [REV02-P017], [REV02-P030] | trust_score=0.88
[REV02-D04] | role=debate | topic=SFRD integral versus stellar-mass density | positions=Residual offset comes mainly from dust/SPS/selection systematics versus IMF or recycling changes. | unresolved=Photometric mass inference has linked age-metallicity-dust-SFH degeneracies. | boundary=Common IMF and cosmology required. | source keys=[REV02], [REV02-P018], [REV02-P021], [REV02-P022], [REV02-P024], [REV02-P044] | trust_score=0.92
[REV02-D05] | role=debate | topic=IMF universality | positions=Use a universal Salpeter/Chabrier-like IMF for cross-epoch comparison versus allow environment- or metallicity-dependent forms. | unresolved=Unresolved high-z stellar populations do not directly measure the low-mass IMF. | boundary=All light-to-SFR, light-to-mass, return, and yield conversions. | source keys=[REV02], [REV02-P031], [REV02-P032], [REV02-P035] | trust_score=0.85
[REV02-D06] | role=debate | topic=Ionizing escape fraction | positions=Galaxy-driven reionization needs substantial escape versus lower-redshift direct limits suggesting small typical values. | unresolved=The neutral high-z IGM prevents direct z>6 Lyman-continuum measurement. | boundary=Population-averaged escape may differ from individual galaxies and redshifts. | source keys=[REV02], [REV02-P037], [REV02-P043] | trust_score=0.86
[REV02-D07] | role=debate | topic=Reionization photon sufficiency | positions=Numerous undetected faint galaxies close the budget versus different emissivity, escape, or recombination assumptions leaving a deficit. | unresolved=Faint cutoff and IGM clumping were poorly constrained. | boundary=Model budget, not direct proof of the dominant source population. | source keys=[REV02], [REV02-P011], [REV02-P037], [REV02-P038], [REV02-P043] | trust_score=0.89
[REV02-D08] | role=debate | topic=Faint-end extrapolation | positions=A physical turnover occurs at relatively bright faint magnitudes versus continuation to much lower luminosity. | unresolved=HST did not reach the putative turnover; alpha near/below -2 makes integrals sensitive to the imposed limit. | boundary=Schechter extrapolation below observations. | source keys=[REV02], [REV02-P010], [REV02-P011], [REV02-P012] | trust_score=0.91

## 4. Key measurements and calibrations

[REV02-N01] | role=measurement | metric=Review analytic CSFH fit | value=psi(z)=0.015(1+z)^2.7/[1+((1+z)/2.9)^5.6] Msun yr^-1 Mpc^-3 | method=UV+IR compilation on the review's Salpeter scale | caveat=Fit and integration conventions; not a direct datum | source keys=[REV02], [REV02-P003], [REV02-P005], [REV02-P015] | trust_score=0.92
[REV02-N02] | role=measurement | metric=Broad SFRD maximum | value=z~1.9 with roughly 3.9 Gyr late-time e-folding in the review fit | method=analytic fit to heterogeneous luminosity-density points | caveat=peak redshift uncertain by fit form and tracer systematics | source keys=[REV02], [REV02-P003], [REV02-P015], [REV02-P042] | trust_score=0.89
[REV02-N03] | role=calibration | metric=FUV-to-SFR factor | value=K_FUV~1.15e-28 Msun yr^-1/(erg s^-1 Hz^-1) | method=1500 Å, continuous >=100 Myr, Salpeter 0.1-100 Msun | caveat=dust and bursty histories separate | source keys=[REV02], [REV02-P001], [REV02-P002] | trust_score=0.94
[REV02-N04] | role=measurement | metric=z~7 UV-LF faint-end slope | value=alpha~-2.01 +/- 0.21 in the review synthesis | method=HUDF/GOODS dropout selection and completeness modeling | caveat=sample, size, lensing, and functional-form assumptions | source keys=[REV02], [REV02-P010], [REV02-P011] | trust_score=0.88
[REV02-N05] | role=measurement | metric=Local stellar-mass density scale | value=order 2e8 Msun Mpc^-3 on the review's adopted scale | method=near-IR/optical luminosity functions plus SPS mass-to-light ratios | caveat=IMF and SPS dependent | source keys=[REV02], [REV02-P021], [REV02-P044] | trust_score=0.88
[REV02-N06] | role=calibration | metric=Stellar mass return fraction | value=R~0.27 Salpeter; R~0.41 Chabrier | method=IMF-integrated instantaneous recycling | caveat=stellar tracks and age dependence | source keys=[REV02], [REV02-P031], [REV02-P032] | trust_score=0.93
[REV02-N07] | role=calibration | metric=Core-collapse supernova efficiency | value=k_CC~0.0068 Msun^-1 for an 8-40 Msun Salpeter progenitor interval | method=IMF integral | caveat=progenitor limits, failed SNe, dust, and binaries | source keys=[REV02], [REV02-P025], [REV02-P026] | trust_score=0.88
[REV02-N08] | role=calibration | metric=Net metal yield examples | value=y~0.016 Salpeter; y~0.032 Chabrier in the review's adopted calculations | method=IMF-integrated stellar-yield tables | caveat=rotation, binaries, metallicity, and black-hole cutoff | source keys=[REV02], [REV02-P033], [REV02-P035] | trust_score=0.82

## 5. What remained unknown in 2014

[REV02-U01] | role=future | gap=Physical faint-end turnover of the high-z UV luminosity function | importance=prevents divergent extrapolation and controls reionization emissivity | needed=deeper imaging/lensing and completeness-calibrated luminosity functions | source keys=[REV02], [REV02-P010], [REV02-P011], [REV02-P012]
[REV02-U02] | role=future | gap=Population-averaged ionizing escape fraction at z>6 | importance=directly scales the galaxy photon budget | needed=indirect high-z diagnostics plus calibrated lower-z analogs and radiative-transfer models | source keys=[REV02], [REV02-P037], [REV02-P043]
[REV02-U03] | role=future | gap=Dust-obscured contribution at z>4 | importance=UV-only SFRD could miss dusty systems | needed=deep, representative submillimeter measurements with matched UV selection | source keys=[REV02], [REV02-P009], [REV02-P015], [REV02-P041]
[REV02-U04] | role=future | gap=IMF in metal-poor and primordial populations | importance=changes every SFR, mass-return, yield, and ionizing conversion | needed=population-sensitive spectroscopy and transient constraints | source keys=[REV02], [REV02-P031], [REV02-P032], [REV02-P035]
[REV02-U05] | role=future | gap=Origin of residual SFRD-integral/SMD mismatch | importance=tests dust, SPS, recycling, and IMF assumptions | needed=mass-complete samples, improved SPS, and independent dynamical constraints | source keys=[REV02], [REV02-P018], [REV02-P022], [REV02-P024], [REV02-P044]
[REV02-U06] | role=future | gap=Exact timing and width of the broad cosmic-SFR maximum | importance=benchmark for baryon-conversion histories | needed=uniform multiwavelength, mass-complete 1<z<3 surveys and harmonized calibrations | source keys=[REV02], [REV02-P015], [REV02-P016], [REV02-P019], [REV02-P030]

## 6. Primary-citation harvest

The 40 rows below are primary observational, calibration, or theory papers directly cited by Madau & Dickinson 2014. Four additional cited reviews/proceedings are retained separately for orientation and are not counted toward the 40-primary minimum.

[REV02-P002] Madau, P. et al. (1996, Monthly Notices of the Royal Astronomical Society) | title=High-redshift galaxies in the Hubble Deep Field: colour selection and star formation history to z~4 | DOI:10.1093/mnras/283.4.1388; arXiv:astro-ph/9607172; ADS:1996MNRAS.283.1388M | role=measurement | review_locator=Section 1 | Pioneer application of the Lyman-break dropout technique to estimate early SFRD from the HDF.
[REV02-P003] Lilly, S. J. et al. (1996, Astrophysical Journal) | title=The Canada-France Redshift Survey: The Luminosity Density and Star Formation History of the Universe to Z approximately 1 | DOI:10.1086/309975; arXiv:astro-ph/9601050; ADS:1996ApJ...460L...1L | role=measurement | review_locator=Section 1 | Early foundational measurement of the intermediate-redshift cosmic star-formation history tracking the decline to the present.
[REV02-P004] Wyder, T. K. et al. (2005, Astrophysical Journal Letters) | title=The Ultraviolet Galaxy Luminosity Function in the Local Universe from GALEX Data | DOI:10.1086/424735; arXiv:astro-ph/0411364; ADS:2005ApJ...619L..15W | role=measurement | review_locator=Table 1 | Provides the definitive local (z~0.1) FUV luminosity function anchoring the low-redshift end of the SFRD fit.
[REV02-P005] Schiminovich, D. et al. (2005, Astrophysical Journal Letters) | title=The GALEX-VVDS Measurement of the Evolution of the Far-Ultraviolet Luminosity Density and the Cosmic Star Formation Rate | DOI:10.1086/427077; arXiv:astro-ph/0411424; ADS:2005ApJ...619L..47S | role=measurement | review_locator=Table 1 | Extends the GALEX FUV luminosity density measurements out to z < 1.
[REV02-P006] Cucciati, O. et al. (2012, Astronomy and Astrophysics) | title=The star formation rate density and dust attenuation evolution over 12 Gyr with the VVDS surveys | DOI:10.1051/0004-6361/201118010; arXiv:1109.1005; ADS:2012A&A...539A..31C | role=measurement | review_locator=Table 1 | Provides FUV luminosity densities and dust attenuation trends across intermediate redshifts (0.1 < z < 4).
[REV02-P007] Dahlen, T. et al. (2007, Astrophysical Journal) | title=Evolution of the Luminosity Function, Star Formation Rate, Morphology, and Size of Star-forming Galaxies Selected at Rest-Frame 1500 and 2800 Å | DOI:10.1086/508854; arXiv:astro-ph/0609016; ADS:2007ApJ...654..172D | role=measurement | review_locator=Table 1 | Anchors the FUV luminosity density across the "cosmic noon" epoch (z~1-3).
[REV02-P008] Reddy, N. A. & Steidel, C. C. (2009, Astrophysical Journal) | title=A Steep Faint-End Slope of the UV Luminosity Function at z ~ 2-3: Implications for the Global Stellar Mass Density and Star Formation in Low-Mass Halos | DOI:10.1088/0004-637X/692/1/778; arXiv:0810.2788; ADS:2009ApJ...692..778R | role=measurement | review_locator=Table 1 | Constrains the faint-end slope and dust corrections of the UV LF at the peak SFRD epoch.
[REV02-P009] Calzetti, D. et al. (2000, Astrophysical Journal) | title=The Dust Content and Opacity of Actively Star-forming Galaxies | DOI:10.1086/308692; arXiv:astro-ph/9911459; ADS:2000ApJ...533..682C | role=calibration | review_locator=Section 4.1 | Establishes the foundational empirical dust attenuation curve and the IRX-beta relationship used to correct UV luminosities.
[REV02-P010] Bouwens, R. J. et al. (2011, Astrophysical Journal) | title=Ultraviolet Luminosity Functions from 132 z ~ 7 and z ~ 8 Lyman-break Galaxies in the Ultra-deep HUDF09 and Wide-area Early Release Science WFC3/IR Observations | DOI:10.1088/0004-637X/737/2/90; arXiv:1006.4360; ADS:2011ApJ...737...90B | role=measurement | review_locator=Section 5.1 | Provides critical high-z UV LF parameters demonstrating the steepening of the faint-end slope at z~7.
[REV02-P011] Bouwens, R. J. et al. (2012, Astrophysical Journal Letters) | title=Lower-luminosity Galaxies Could Reionize the Universe: Very Steep Faint-end Slopes to the UV Luminosity Functions at z >= 5-8 from the HUDF09 WFC3/IR Observations | DOI:10.1088/2041-8205/752/1/L5; arXiv:1105.2038; ADS:2012ApJ...752L...5B | role=debate | review_locator=Table 1 | Defines the debate around divergent faint-end slopes and their necessity for supplying the reionization photon budget.
[REV02-P012] Schenker, M. A. et al. (2013, Astrophysical Journal) | title=The UV Luminosity Function of Star-forming Galaxies via Dropout Selection at Redshifts z ~ 7 and 8 from the 2012 Ultra Deep Field Campaign | DOI:10.1088/0004-637X/768/2/196; arXiv:1212.4819; ADS:2013ApJ...768..196S | role=measurement | review_locator=Table 1 | Extends robust UV LF measurements to z~8, anchoring the sharp decline of the high-redshift SFRD.
[REV02-P013] Sanders, D. B. et al. (2003, Astronomical Journal) | title=The IRAS Revised Bright Galaxy Sample | DOI:10.1086/376841; arXiv:astro-ph/0306263; ADS:2003AJ....126.1607S | role=measurement | review_locator=Table 1 | Baseline local calibration of the far-infrared luminosity function tracking dust-obscured star formation at z~0.
[REV02-P014] Takeuchi, T. T. et al. (2003, Astrophysical Journal Letters) | title=The Luminosity Function of IRAS Point Source Catalog Redshift Survey Galaxies | DOI:10.1086/375181; arXiv:astro-ph/0303181; ADS:2003ApJ...587L..89T | role=measurement | review_locator=Table 1 / local IR luminosity density | Local IRAS PSCz luminosity-function anchor; do not use as a high-redshift evolution measurement.
[REV02-P015] Gruppioni, C. et al. (2013, Monthly Notices of the Royal Astronomical Society) | title=The Herschel PEP/HerMES luminosity function - I. Probing the evolution of PACS selected Galaxies to z ≃ 4 | DOI:10.1093/mnras/stt308; arXiv:1302.5209; ADS:2013MNRAS.432...23G | role=measurement | review_locator=Table 1 | Key Herschel measurement mapping the extreme rise and dominance of dust-obscured star formation at z~2.
[REV02-P016] Magnelli, B. et al. (2011, Astronomy and Astrophysics) | title=Evolution of the dusty infrared luminosity function from z = 0 to z = 2.3 using observations from Spitzer | DOI:10.1051/0004-6361/200913941; arXiv:1101.2467; ADS:2011A&A...528A..35M | role=measurement | review_locator=Table 1 | Spitzer-based constraints on the intermediate-redshift evolution of the obscured SFRD.
[REV02-P017] Magnelli, B. et al. (2013, Astronomy and Astrophysics) | title=The deepest Herschel-PACS far-infrared survey: number counts and infrared luminosity functions from combined PEP/GOODS-H observations | DOI:10.1051/0004-6361/201321371; arXiv:1303.4436; ADS:2013A&A...553A.132M | role=measurement | review_locator=Table 1 | Deep far-IR measurements confirming that obscured star formation accounts for the vast majority of the SFRD peak.
[REV02-P018] Dickinson, M. et al. (2003, Astrophysical Journal) | title=The Evolution of the Global Stellar Mass Density at 0<z<3 | DOI:10.1086/368111; arXiv:astro-ph/0212242; ADS:2003ApJ...587...25D | role=measurement | review_locator=Section 1 | Foundational near-infrared survey linking the rest-frame optical light of evolved stars to cosmic stellar mass buildup.
[REV02-P019] Muzzin, A. et al. (2013, Astrophysical Journal) | title=The Evolution of the Stellar Mass Functions of Star-forming and Quiescent Galaxies to z = 4 from the COSMOS/UltraVISTA Survey | DOI:10.1088/0004-637X/777/1/18; arXiv:1303.4409; ADS:2013ApJ...777...18M | role=measurement | review_locator=Table 2 | Provides critical high-redshift (z~4) constraints on the assembly of the cosmic stellar mass density.
[REV02-P021] Cole, S. et al. (2001, Monthly Notices of the Royal Astronomical Society) | title=The 2dF galaxy redshift survey: near-infrared galaxy luminosity functions | DOI:10.1046/j.1365-8711.2001.04591.x; arXiv:astro-ph/0012429; ADS:2001MNRAS.326..255C | role=measurement | review_locator=Section 5.3 | Establishes the local z=0 stellar mass density benchmark used to test the integral of the SFRD.
[REV02-P022] Conroy, C. et al. (2009, Astrophysical Journal) | title=The Propagation of Uncertainties in Stellar Population Synthesis Modeling. I. The Relevance of Uncertain Aspects of Stellar Evolution and the Initial Mass Function to the Derived Physical Properties of Galaxies | DOI:10.1088/0004-637X/699/1/486; arXiv:0809.4261; ADS:2009ApJ...699..486C | role=caveat | review_locator=Section 3.2 | Highlights severe systematic uncertainties in stellar mass and SFR conversions due to TP-AGB stars and IMF choices.
[REV02-P023] Steidel, C. C. et al. (1999, Astrophysical Journal) | title=Lyman-Break Galaxies at z>~4 and the Evolution of the Ultraviolet Luminosity Density at High Redshift | DOI:10.1086/307363; arXiv:astro-ph/9811399; ADS:1999ApJ...519....1S | role=measurement | review_locator=Section 1 | Classical definition of the Lyman-break selection technique enabling the first reliable z>3 cosmic censuses.
[REV02-P024] Maraston, C. (2005, Monthly Notices of the Royal Astronomical Society) | title=Evolutionary population synthesis: models, analysis of the ingredients and application to high-z galaxies | DOI:10.1111/j.1365-2966.2005.09270.x; arXiv:astro-ph/0410207; ADS:2005MNRAS.362..799M | role=caveat | review_locator=Section 3.2 | Demonstrates how the treatment of Thermally Pulsing AGB stars drastically alters derived stellar masses and ages.
[REV02-P025] Dahlen, T. et al. (2004, Astrophysical Journal) | title=High-Redshift Supernova Rates | DOI:10.1086/422899; arXiv:astro-ph/0406547; ADS:2004ApJ...613..189D | role=measurement | review_locator=Section 5.2 | Measures core-collapse supernova rates tracking the decline of massive star formation over cosmic time.
[REV02-P026] Horiuchi, S. et al. (2011, Astrophysical Journal) | title=The Cosmic Core-collapse Supernova Rate Does Not Match the Massive-star Formation Rate | DOI:10.1088/0004-637X/738/2/154; arXiv:1102.1977; ADS:2011ApJ...738..154H | role=debate | review_locator=Section 5.2 | Introduces the discrepancy between the observed CC SN rate and the predicted rate derived from the integrated SFRD.
[REV02-P027] Finkelstein, S. L. et al. (2013, Nature) | title=A galaxy rapidly forming stars 700 million years after the Big Bang at redshift 7.51 | DOI:10.1038/nature12657; arXiv:1310.6031; ADS:2013Natur.502..524F | role=measurement | review_locator=Section 1 | Confirmation of extreme, bursty star-formation well into the reionization epoch, pushing empirical boundaries.
[REV02-P028] Coe, D. et al. (2013, Astrophysical Journal) | title=CLASH: Three Strongly Lensed Images of a Candidate z ≈ 11 Galaxy | DOI:10.1088/0004-637X/762/1/32; arXiv:1211.3663; ADS:2013ApJ...762...32C | role=future | review_locator=Section 1 | Represents the extreme observational frontier for UV photometric dropouts awaiting spectroscopic confirmation.
[REV02-P029] Franx, M. et al. (2003, Astrophysical Journal Letters) | title=A Significant Population of Red, Near-Infrared-selected High-Redshift Galaxies | DOI:10.1086/375155; arXiv:astro-ph/0303163; ADS:2003ApJ...587L..79F | role=measurement | review_locator=Section 1 | Identifies heavily dust-obscured, passive galaxies at high redshift missed by standard rest-frame UV dropout selections.
[REV02-P030] Daddi, E. et al. (2005, Astrophysical Journal Letters) | title=The Population of BzK-selected ULIRGs at z ~ 2 | DOI:10.1086/496918; arXiv:astro-ph/0507504; ADS:2005ApJ...631L..13D | role=measurement | review_locator=Section 1 / obscured populations at cosmic noon | Massive BzK-selected star-forming galaxies at z~2; not a census of all galaxies or a passive-galaxy paper.
[REV02-P031] Chabrier, G. (2003, Publications of the Astronomical Society of the Pacific) | title=Galactic Stellar and Substellar Initial Mass Function | DOI:10.1086/376392; arXiv:astro-ph/0304382; ADS:2003PASP..115..763C | role=calibration | review_locator=Section 2 | Defines the modern standard log-normal IMF, significantly shifting predicted stellar mass return fractions compared to Salpeter.
[REV02-P032] Salpeter, E. E. (1955, Astrophysical Journal) | title=The Luminosity Function and Stellar Evolution. | DOI:10.1086/145971; arXiv:none; ADS:1955ApJ...121..161S | role=calibration | review_locator=Section 2 | The historic baseline power-law IMF used to calibrate the primary analytical SFRD fit and SN rates.
[REV02-P033] Maeder, A. (1992, Astronomy and Astrophysics) | title=Stellar yields as a function of initial metallicity and mass limit for black hole formation | DOI:none; arXiv:none; ADS:1992A&A...264..105M | role=theory | review_locator=Section 2 | Provides the foundational stellar nucleosynthetic yields necessary for calculating the metal enrichment tracking the SFRD.
[REV02-P035] Chieffi, A. & Limongi, M. (2004, Astrophysical Journal) | title=Explosive Yields of Massive Stars from Z = 0 to Z = Zsolar | DOI:10.1086/392523; arXiv:astro-ph/0402625; ADS:2004ApJ...608..405C | role=theory | review_locator=Section 2 | Calculates the metallic yield returned to the IGM via supernovae as a function of the underlying SFR.
[REV02-P037] Robertson, B. E. et al. (2013, Astrophysical Journal) | title=New Constraints on Cosmic Reionization from the 2012 Hubble Ultra Deep Field Campaign | DOI:10.1088/0004-637X/768/1/71; arXiv:1301.1228; ADS:2013ApJ...768...71R | role=theory | review_locator=Section 5.8 | Models the translation of the observed z>6 UV LF into the ionizing photon budget required to maintain cosmic reionization.
[REV02-P038] Haardt, F. & Madau, P. (2012, Astrophysical Journal) | title=Radiative Transfer in a Clumpy Universe. IV. New Synthesis Models of the Cosmic UV/X-Ray Background | DOI:10.1088/0004-637X/746/2/125; arXiv:1105.2039; ADS:2012ApJ...746..125H | role=theory | review_locator=Section 5.8 | Calculates hydrogen recombination timescales and the required IGM clumping factors to balance the reionization photon budget.
[REV02-P039] Pei, Y. C. & Fall, S. M. (1995, Astrophysical Journal) | title=Cosmic Chemical Evolution | DOI:10.1086/176466; arXiv:none; ADS:1995ApJ...454...69P | role=theory | review_locator=Section 5.1 | Early theoretical framework linking the observable cosmological mass density of HI to the overall comoving star formation.
[REV02-P040] Lanzetta, K. M. et al. (1995, Astrophysical Journal) | title=The IUE Survey for Damped Lyman-alpha and Lyman-Limit Absorption Systems: Evolution of the Gaseous Content of the Universe | DOI:10.1086/175286; arXiv:none; ADS:1995ApJ...440..435L | role=measurement | review_locator=Section 5.5 / neutral-gas and chemical-evolution accounting | Damped-Lyman-alpha neutral-gas evolution and closed-box interpretation; not a direct cosmic SFR-density measurement.
[REV02-P041] Meurer, G. R. et al. (1999, Astrophysical Journal) | title=Dust Absorption and the Ultraviolet Luminosity Density at z ~ 3 as Calibrated by Local Starburst Galaxies | DOI:10.1086/307523; arXiv:astro-ph/9903054; ADS:1999ApJ...521...64M | role=calibration | review_locator=Section 4.1 / UV attenuation | Local-starburst IRX-beta calibration applied to z~3 UV samples; applicability to other populations is not universal.
[REV02-P042] Madau, P. et al. (1998, Astrophysical Journal) | title=The Star Formation History of Field Galaxies | DOI:10.1086/305523; arXiv:astro-ph/9708220; ADS:1998ApJ...498..106M | role=measurement | review_locator=Section 1 / historical cosmic-SFH synthesis | Early integrated-light CSFH inference to z~4 under then-current cosmology, IMF, and dust assumptions.
[REV02-P043] Madau, P. et al. (1999, Astrophysical Journal) | title=Radiative Transfer in a Clumpy Universe. III. The Nature of Cosmological Ionizing Sources | DOI:10.1086/306975; arXiv:astro-ph/9809058; ADS:1999ApJ...514..648M | role=theory | review_locator=Section 5.8 / reionization photon accounting | Ionizing-source and clumpy-IGM budget model; conclusions depend on emissivity, escape fraction, and recombination assumptions.
[REV02-P044] Li, C. & White, S. D. M. (2009, Monthly Notices of the Royal Astronomical Society) | title=The distribution of stellar mass in the low-redshift Universe | DOI:10.1111/j.1365-2966.2009.15268.x; arXiv:0901.0706; ADS:2009MNRAS.398.2177L | role=measurement | review_locator=Section 5.3 / local stellar-mass-density benchmark | Low-redshift SDSS stellar-mass distribution under a standard IMF; not a high-redshift mass-function measurement.

### Supporting cited reviews/proceeding — not counted as primary

[REV02-P001] Kennicutt, R. C. (1998, Annual Review of Astronomy and Astrophysics) | title=Star Formation in Galaxies Along the Hubble Sequence | DOI:10.1146/annurev.astro.36.1.189; arXiv:astro-ph/9807187; ADS:1998ARA&A..36..189K | role=calibration | review_locator=Section 3.1 | Standardizes the foundational conversion between rest-frame UV luminosity and instantaneous star-formation rate.
[REV02-P020] Hopkins, A. M. & Beacom, J. F. (2006, Astrophysical Journal) | title=On the Normalization of the Cosmic Star Formation History | DOI:10.1086/506610; arXiv:astro-ph/0601463; ADS:2006ApJ...651..142H | role=review | review_locator=Section 1 | Predecessor compilation of the cosmic SFRD highlighting cross-calibration issues between independent measurements.
[REV02-P034] Asplund, M. et al. (2009, Annual Review of Astronomy and Astrophysics) | title=The Chemical Composition of the Sun | DOI:10.1146/annurev.astro.46.060407.145222; arXiv:0909.0948; ADS:2009ARA&A..47..481A | role=calibration | review_locator=Section 2 | Updates the solar metallicity boundary, generating tensions with older models calculating cosmic enrichment.
[REV02-P036] Kewley, L. J. & Kobulnicky, H. A. (2007, Astrophysics and Space Science Proceedings) | title=The Metallicity History of Disk Galaxies | DOI:10.1007/978-1-4020-5573-7\_75; arXiv:none; ADS:2007iuse.book..435K | role=measurement | review_locator=Section 3.1 | Empirically traces the redshift evolution of global metallicity, modifying the conversion factors between UV light and SFR.

## 7. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | raw REV02-P003 tuple title=The Canada-France Redshift Survey. XI. The Cosmic Star Formation History from the Expected Evolution of the Galaxy Luminosity Function; DOI:10.1086/177272; arXiv:astro-ph/9601050; ADS:1996ApJ...460L...1L | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Canada-France Redshift Survey: The Luminosity Density and Star Formation History of the Universe to Z approximately 1; DOI:10.1086/309975; arXiv:astro-ph/9601050; ADS:1996ApJ...460L...1L
UNCITED_NOT_USABLE | raw REV02-P004 tuple title=The Ultraviolet Galaxy Luminosity Function in the Local Universe from GALEX Data; DOI:10.1086/427359; arXiv:astro-ph/0411600; ADS:2005ApJ...619L..15W | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Ultraviolet Galaxy Luminosity Function in the Local Universe from GALEX Data; DOI:10.1086/424735; arXiv:astro-ph/0411364; ADS:2005ApJ...619L..15W
UNCITED_NOT_USABLE | raw REV02-P005 tuple title=The GALEX-VVDS Measurement of the Evolution of the Far-Ultraviolet Luminosity Density and the Cosmic Star Formation Rate; DOI:10.1086/427376; arXiv:astro-ph/0411602; ADS:2005ApJ...619L..47S | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The GALEX-VVDS Measurement of the Evolution of the Far-Ultraviolet Luminosity Density and the Cosmic Star Formation Rate; DOI:10.1086/427077; arXiv:astro-ph/0411424; ADS:2005ApJ...619L..47S
UNCITED_NOT_USABLE | raw REV02-P007 tuple title=The Rest-Frame Ultraviolet Luminosity Function of Galaxies at Redshifts z~1-3; DOI:10.1086/508854; arXiv:astro-ph/0608442; ADS:2007ApJ...654..172D | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=Evolution of the Luminosity Function, Star Formation Rate, Morphology, and Size of Star-forming Galaxies Selected at Rest-Frame 1500 and 2800 Å; DOI:10.1086/508854; arXiv:astro-ph/0609016; ADS:2007ApJ...654..172D
UNCITED_NOT_USABLE | raw REV02-P008 tuple title=A Steep Faint-End Slope of the UV Luminosity Function at z ~ 2-3: Implications for the Global Star Formation Rate and Energy Density; DOI:10.1088/0004-637X/692/1/778; arXiv:0810.2788; ADS:2009ApJ...692..778R | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=A Steep Faint-End Slope of the UV Luminosity Function at z ~ 2-3: Implications for the Global Stellar Mass Density and Star Formation in Low-Mass Halos; DOI:10.1088/0004-637X/692/1/778; arXiv:0810.2788; ADS:2009ApJ...692..778R
UNCITED_NOT_USABLE | raw REV02-P010 tuple title=Ultraviolet Luminosity Functions from 132 z ~ 7 and z ~ 8 Early-epoch Galaxies in the HUDF09 and Oesch+2010 Fields; DOI:10.1088/0004-637X/737/2/90; arXiv:1006.4360; ADS:2011ApJ...737...90B | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=Ultraviolet Luminosity Functions from 132 z ~ 7 and z ~ 8 Lyman-break Galaxies in the Ultra-deep HUDF09 and Wide-area Early Release Science WFC3/IR Observations; DOI:10.1088/0004-637X/737/2/90; arXiv:1006.4360; ADS:2011ApJ...737...90B
UNCITED_NOT_USABLE | raw REV02-P011 tuple title=Lower-luminosity Galaxies Could Reionize the Universe: Very Steep Faint-end Slopes to the UV Luminosity Functions at z >= 5-8; DOI:10.1088/2041-8205/752/1/L5; arXiv:1105.2038; ADS:2012ApJ...752L...5B | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=Lower-luminosity Galaxies Could Reionize the Universe: Very Steep Faint-end Slopes to the UV Luminosity Functions at z >= 5-8 from the HUDF09 WFC3/IR Observations; DOI:10.1088/2041-8205/752/1/L5; arXiv:1105.2038; ADS:2012ApJ...752L...5B
UNCITED_NOT_USABLE | raw REV02-P014 tuple title=The Luminosity Function of Galaxies in the Local Universe; DOI:none; arXiv:astro-ph/0212061; ADS:2003PASJ...55..381T | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Luminosity Function of IRAS Point Source Catalog Redshift Survey Galaxies; DOI:10.1086/375181; arXiv:astro-ph/0303181; ADS:2003ApJ...587L..89T
UNCITED_NOT_USABLE | raw REV02-P015 tuple title=The Herschel PEP/HerMES luminosity function - I. Probing the evolution of PACS selected Galaxies to z ~ 4; DOI:10.1093/mnras/stt308; arXiv:1302.5209; ADS:2013MNRAS.432...23G | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Herschel PEP/HerMES luminosity function - I. Probing the evolution of PACS selected Galaxies to z ≃ 4; DOI:10.1093/mnras/stt308; arXiv:1302.5209; ADS:2013MNRAS.432...23G
UNCITED_NOT_USABLE | raw REV02-P016 tuple title=Evolution of the dusty infrared luminosity function from z = 0 to z = 2.3 using observations from Spitzer; DOI:10.1051/0004-6361/201016146; arXiv:1101.2467; ADS:2011A&A...528A..35M | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=Evolution of the dusty infrared luminosity function from z = 0 to z = 2.3 using observations from Spitzer; DOI:10.1051/0004-6361/200913941; arXiv:1101.2467; ADS:2011A&A...528A..35M
UNCITED_NOT_USABLE | raw REV02-P018 tuple title=The Evolution of the Global Stellar Mass Density at 0 < z < 3; DOI:10.1086/374329; arXiv:astro-ph/0302445; ADS:2003ApJ...587...25D | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Evolution of the Global Stellar Mass Density at 0<z<3; DOI:10.1086/368111; arXiv:astro-ph/0212242; ADS:2003ApJ...587...25D
UNCITED_NOT_USABLE | raw REV02-P022 tuple title=The Propagation of Uncertainties in Stellar Population Synthesis Modeling. I. The Relevance of Uncertain Aspects of Stellar Evolution and the Initial Mass Function to the Derived Physical Properties of Galaxies; DOI:10.1088/0004-637X/699/1/486; arXiv:0810.0577; ADS:2009ApJ...699..486C | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Propagation of Uncertainties in Stellar Population Synthesis Modeling. I. The Relevance of Uncertain Aspects of Stellar Evolution and the Initial Mass Function to the Derived Physical Properties of Galaxies; DOI:10.1088/0004-637X/699/1/486; arXiv:0809.4261; ADS:2009ApJ...699..486C
UNCITED_NOT_USABLE | raw REV02-P023 tuple title=Lyman-Break Galaxies at z~4 and the Evolution of the Ultraviolet Luminosity Density at High Redshift; DOI:10.1086/307363; arXiv:astro-ph/9811399; ADS:1999ApJ...519....1S | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=Lyman-Break Galaxies at z>~4 and the Evolution of the Ultraviolet Luminosity Density at High Redshift; DOI:10.1086/307363; arXiv:astro-ph/9811399; ADS:1999ApJ...519....1S
UNCITED_NOT_USABLE | raw REV02-P024 tuple title=Evolutionary synthesis of stellar populations: a mock grid for extra-galactic studies; DOI:10.1111/j.1365-2966.2005.09270.x; arXiv:astro-ph/0410207; ADS:2005MNRAS.362..799M | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=Evolutionary population synthesis: models, analysis of the ingredients and application to high-z galaxies; DOI:10.1111/j.1365-2966.2005.09270.x; arXiv:astro-ph/0410207; ADS:2005MNRAS.362..799M
UNCITED_NOT_USABLE | raw REV02-P025 tuple title=High-Redshift Supernova Rates; DOI:10.1086/422402; arXiv:astro-ph/0406547; ADS:2004ApJ...613..189D | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=High-Redshift Supernova Rates; DOI:10.1086/422899; arXiv:astro-ph/0406547; ADS:2004ApJ...613..189D
UNCITED_NOT_USABLE | raw REV02-P026 tuple title=The Cosmic Core-collapse Supernova Rate does not match the Star Formation Rate; DOI:10.1088/0004-637X/738/2/154; arXiv:1102.1977; ADS:2011ApJ...738..154H | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Cosmic Core-collapse Supernova Rate Does Not Match the Massive-star Formation Rate; DOI:10.1088/0004-637X/738/2/154; arXiv:1102.1977; ADS:2011ApJ...738..154H
UNCITED_NOT_USABLE | raw REV02-P028 tuple title=CLASH: Three Strongly Lensed Images of a Candidate z ~ 11 Galaxy; DOI:10.1088/0004-637X/762/1/32; arXiv:1211.3663; ADS:2013ApJ...762...32C | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=CLASH: Three Strongly Lensed Images of a Candidate z ≈ 11 Galaxy; DOI:10.1088/0004-637X/762/1/32; arXiv:1211.3663; ADS:2013ApJ...762...32C
UNCITED_NOT_USABLE | raw REV02-P029 tuple title=A Significant Population of Red, Near-Infrared-selected High-Redshift Galaxies; DOI:10.1086/375253; arXiv:astro-ph/0302343; ADS:2003ApJ...587L..79F | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=A Significant Population of Red, Near-Infrared-selected High-Redshift Galaxies; DOI:10.1086/375155; arXiv:astro-ph/0303163; ADS:2003ApJ...587L..79F
UNCITED_NOT_USABLE | raw REV02-P030 tuple title=Passively Evolving Early-Type Galaxies at 1.4 < z < 2.5 in the Hubble Ultra Deep Field; DOI:10.1086/430349; arXiv:astro-ph/0503102; ADS:2005ApJ...626..680D | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Population of BzK-selected ULIRGs at z ~ 2; DOI:10.1086/496918; arXiv:astro-ph/0507504; ADS:2005ApJ...631L..13D
UNCITED_NOT_USABLE | raw REV02-P032 tuple title=The Luminosity Function and Stellar Evolution; DOI:10.1086/145971; arXiv:none; ADS:1955ApJ...121..161S | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Luminosity Function and Stellar Evolution.; DOI:10.1086/145971; arXiv:none; ADS:1955ApJ...121..161S
UNCITED_NOT_USABLE | raw REV02-P033 tuple title=Stellar yields as a function of mass and metallicity; DOI:none; arXiv:none; ADS:1992A&A...264..105M | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=Stellar yields as a function of initial metallicity and mass limit for black hole formation; DOI:none; arXiv:none; ADS:1992A&A...264..105M
UNCITED_NOT_USABLE | raw REV02-P035 tuple title=Explosive Yields of Massive Stars from Z = 0 to Z = Z_sun; DOI:10.1086/382801; arXiv:astro-ph/0311311; ADS:2004ApJ...608..405C | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=Explosive Yields of Massive Stars from Z = 0 to Z = Zsolar; DOI:10.1086/392523; arXiv:astro-ph/0402625; ADS:2004ApJ...608..405C
UNCITED_NOT_USABLE | raw REV02-P036 tuple title=Metallicity of Star-Forming Galaxies; DOI:10.1007/978-1-4020-5696-9_24; arXiv:astro-ph/0702283; ADS:2007iuse.book..435K | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The Metallicity History of Disk Galaxies; DOI:10.1007/978-1-4020-5573-7\_75; arXiv:none; ADS:2007iuse.book..435K
UNCITED_NOT_USABLE | raw REV02-P039 tuple title=Cosmic Chemical Evolution; DOI:10.1086/176503; arXiv:astro-ph/9508107; ADS:1995ApJ...454...69P | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=Cosmic Chemical Evolution; DOI:10.1086/176466; arXiv:none; ADS:1995ApJ...454...69P
UNCITED_NOT_USABLE | raw REV02-P040 tuple title=The Star Formation History of the Universe; DOI:10.1086/309765; arXiv:astro-ph/9502073; ADS:1995ApJ...453L..17L | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title=The IUE Survey for Damped Lyman-alpha and Lyman-Limit Absorption Systems: Evolution of the Gaseous Content of the Universe; DOI:10.1086/175286; arXiv:none; ADS:1995ApJ...440..435L
UNCITED_NOT_USABLE | one survey alone supplies a complete cosmic SFR density | overbroad claim | multi-tracer coverage, limits, dust, and cosmic variance remain
UNCITED_NOT_USABLE | dust corrections are redshift-independent | overbroad claim | attenuation depends on population, geometry, and calibration
UNCITED_NOT_USABLE | the IMF is observationally fixed across cosmic time | unsupported extrapolation | the review adopts an IMF for conversion and closure
UNCITED_NOT_USABLE | stellar-mass-density agreement proves exact closure | overbroad claim | a model-dependent residual offset remains
UNCITED_NOT_USABLE | the review-fit peak is selection- and model-free | overbroad claim | heterogeneous tracers and the analytic form set the result
UNCITED_NOT_USABLE | bright detected z>6 galaxies alone close reionization | unsupported closure | faint-end, escape fraction, and recombination assumptions dominate
UNCITED_NOT_USABLE | post-2014/JWST source anchors captured by web search | outside date and not review-cited | excluded from all usable rows
UNCITED_NOT_USABLE | AGN-centered accretion or feedback source | outside non-AGN core scope | not promoted in this packet

## 8. Review and source identity ledger

[REV02] | Madau & Dickinson (2014, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev-astro-081811-125615; arXiv:1403.0007; ADS:2014ARA&A..52..415M | role=review | 2014 bounded cosmic-SFH synthesis
[REV02-P001] | Kennicutt, R. C. (1998, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev.astro.36.1.189; arXiv:astro-ph/9807187; ADS:1998ARA&A..36..189K | role=calibration | Standardizes the foundational conversion between rest-frame UV luminosity and instantaneous star-formation rate.
[REV02-P002] | Madau, P. et al. (1996, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/283.4.1388; arXiv:astro-ph/9607172; ADS:1996MNRAS.283.1388M | role=measurement | Pioneer application of the Lyman-break dropout technique to estimate early SFRD from the HDF.
[REV02-P003] | Lilly, S. J. et al. (1996, Astrophysical Journal) | DOI:10.1086/309975; arXiv:astro-ph/9601050; ADS:1996ApJ...460L...1L | role=measurement | Early foundational measurement of the intermediate-redshift cosmic star-formation history tracking the decline to the present.
[REV02-P004] | Wyder, T. K. et al. (2005, Astrophysical Journal Letters) | DOI:10.1086/424735; arXiv:astro-ph/0411364; ADS:2005ApJ...619L..15W | role=measurement | Provides the definitive local (z~0.1) FUV luminosity function anchoring the low-redshift end of the SFRD fit.
[REV02-P005] | Schiminovich, D. et al. (2005, Astrophysical Journal Letters) | DOI:10.1086/427077; arXiv:astro-ph/0411424; ADS:2005ApJ...619L..47S | role=measurement | Extends the GALEX FUV luminosity density measurements out to z < 1.
[REV02-P006] | Cucciati, O. et al. (2012, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201118010; arXiv:1109.1005; ADS:2012A&A...539A..31C | role=measurement | Provides FUV luminosity densities and dust attenuation trends across intermediate redshifts (0.1 < z < 4).
[REV02-P007] | Dahlen, T. et al. (2007, Astrophysical Journal) | DOI:10.1086/508854; arXiv:astro-ph/0609016; ADS:2007ApJ...654..172D | role=measurement | Anchors the FUV luminosity density across the "cosmic noon" epoch (z~1-3).
[REV02-P008] | Reddy, N. A. & Steidel, C. C. (2009, Astrophysical Journal) | DOI:10.1088/0004-637X/692/1/778; arXiv:0810.2788; ADS:2009ApJ...692..778R | role=measurement | Constrains the faint-end slope and dust corrections of the UV LF at the peak SFRD epoch.
[REV02-P009] | Calzetti, D. et al. (2000, Astrophysical Journal) | DOI:10.1086/308692; arXiv:astro-ph/9911459; ADS:2000ApJ...533..682C | role=calibration | Establishes the foundational empirical dust attenuation curve and the IRX-beta relationship used to correct UV luminosities.
[REV02-P010] | Bouwens, R. J. et al. (2011, Astrophysical Journal) | DOI:10.1088/0004-637X/737/2/90; arXiv:1006.4360; ADS:2011ApJ...737...90B | role=measurement | Provides critical high-z UV LF parameters demonstrating the steepening of the faint-end slope at z~7.
[REV02-P011] | Bouwens, R. J. et al. (2012, Astrophysical Journal Letters) | DOI:10.1088/2041-8205/752/1/L5; arXiv:1105.2038; ADS:2012ApJ...752L...5B | role=debate | Defines the debate around divergent faint-end slopes and their necessity for supplying the reionization photon budget.
[REV02-P012] | Schenker, M. A. et al. (2013, Astrophysical Journal) | DOI:10.1088/0004-637X/768/2/196; arXiv:1212.4819; ADS:2013ApJ...768..196S | role=measurement | Extends robust UV LF measurements to z~8, anchoring the sharp decline of the high-redshift SFRD.
[REV02-P013] | Sanders, D. B. et al. (2003, Astronomical Journal) | DOI:10.1086/376841; arXiv:astro-ph/0306263; ADS:2003AJ....126.1607S | role=measurement | Baseline local calibration of the far-infrared luminosity function tracking dust-obscured star formation at z~0.
[REV02-P014] | Takeuchi, T. T. et al. (2003, Astrophysical Journal Letters) | DOI:10.1086/375181; arXiv:astro-ph/0303181; ADS:2003ApJ...587L..89T | role=measurement | Local IRAS PSCz luminosity-function anchor; do not use as a high-redshift evolution measurement.
[REV02-P015] | Gruppioni, C. et al. (2013, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stt308; arXiv:1302.5209; ADS:2013MNRAS.432...23G | role=measurement | Key Herschel measurement mapping the extreme rise and dominance of dust-obscured star formation at z~2.
[REV02-P016] | Magnelli, B. et al. (2011, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/200913941; arXiv:1101.2467; ADS:2011A&A...528A..35M | role=measurement | Spitzer-based constraints on the intermediate-redshift evolution of the obscured SFRD.
[REV02-P017] | Magnelli, B. et al. (2013, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201321371; arXiv:1303.4436; ADS:2013A&A...553A.132M | role=measurement | Deep far-IR measurements confirming that obscured star formation accounts for the vast majority of the SFRD peak.
[REV02-P018] | Dickinson, M. et al. (2003, Astrophysical Journal) | DOI:10.1086/368111; arXiv:astro-ph/0212242; ADS:2003ApJ...587...25D | role=measurement | Foundational near-infrared survey linking the rest-frame optical light of evolved stars to cosmic stellar mass buildup.
[REV02-P019] | Muzzin, A. et al. (2013, Astrophysical Journal) | DOI:10.1088/0004-637X/777/1/18; arXiv:1303.4409; ADS:2013ApJ...777...18M | role=measurement | Provides critical high-redshift (z~4) constraints on the assembly of the cosmic stellar mass density.
[REV02-P020] | Hopkins, A. M. & Beacom, J. F. (2006, Astrophysical Journal) | DOI:10.1086/506610; arXiv:astro-ph/0601463; ADS:2006ApJ...651..142H | role=review | Predecessor compilation of the cosmic SFRD highlighting cross-calibration issues between independent measurements.
[REV02-P021] | Cole, S. et al. (2001, Monthly Notices of the Royal Astronomical Society) | DOI:10.1046/j.1365-8711.2001.04591.x; arXiv:astro-ph/0012429; ADS:2001MNRAS.326..255C | role=measurement | Establishes the local z=0 stellar mass density benchmark used to test the integral of the SFRD.
[REV02-P022] | Conroy, C. et al. (2009, Astrophysical Journal) | DOI:10.1088/0004-637X/699/1/486; arXiv:0809.4261; ADS:2009ApJ...699..486C | role=caveat | Highlights severe systematic uncertainties in stellar mass and SFR conversions due to TP-AGB stars and IMF choices.
[REV02-P023] | Steidel, C. C. et al. (1999, Astrophysical Journal) | DOI:10.1086/307363; arXiv:astro-ph/9811399; ADS:1999ApJ...519....1S | role=measurement | Classical definition of the Lyman-break selection technique enabling the first reliable z>3 cosmic censuses.
[REV02-P024] | Maraston, C. (2005, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2005.09270.x; arXiv:astro-ph/0410207; ADS:2005MNRAS.362..799M | role=caveat | Demonstrates how the treatment of Thermally Pulsing AGB stars drastically alters derived stellar masses and ages.
[REV02-P025] | Dahlen, T. et al. (2004, Astrophysical Journal) | DOI:10.1086/422899; arXiv:astro-ph/0406547; ADS:2004ApJ...613..189D | role=measurement | Measures core-collapse supernova rates tracking the decline of massive star formation over cosmic time.
[REV02-P026] | Horiuchi, S. et al. (2011, Astrophysical Journal) | DOI:10.1088/0004-637X/738/2/154; arXiv:1102.1977; ADS:2011ApJ...738..154H | role=debate | Introduces the discrepancy between the observed CC SN rate and the predicted rate derived from the integrated SFRD.
[REV02-P027] | Finkelstein, S. L. et al. (2013, Nature) | DOI:10.1038/nature12657; arXiv:1310.6031; ADS:2013Natur.502..524F | role=measurement | Confirmation of extreme, bursty star-formation well into the reionization epoch, pushing empirical boundaries.
[REV02-P028] | Coe, D. et al. (2013, Astrophysical Journal) | DOI:10.1088/0004-637X/762/1/32; arXiv:1211.3663; ADS:2013ApJ...762...32C | role=future | Represents the extreme observational frontier for UV photometric dropouts awaiting spectroscopic confirmation.
[REV02-P029] | Franx, M. et al. (2003, Astrophysical Journal Letters) | DOI:10.1086/375155; arXiv:astro-ph/0303163; ADS:2003ApJ...587L..79F | role=measurement | Identifies heavily dust-obscured, passive galaxies at high redshift missed by standard rest-frame UV dropout selections.
[REV02-P030] | Daddi, E. et al. (2005, Astrophysical Journal Letters) | DOI:10.1086/496918; arXiv:astro-ph/0507504; ADS:2005ApJ...631L..13D | role=measurement | Massive BzK-selected star-forming galaxies at z~2; not a census of all galaxies or a passive-galaxy paper.
[REV02-P031] | Chabrier, G. (2003, Publications of the Astronomical Society of the Pacific) | DOI:10.1086/376392; arXiv:astro-ph/0304382; ADS:2003PASP..115..763C | role=calibration | Defines the modern standard log-normal IMF, significantly shifting predicted stellar mass return fractions compared to Salpeter.
[REV02-P032] | Salpeter, E. E. (1955, Astrophysical Journal) | DOI:10.1086/145971; arXiv:none; ADS:1955ApJ...121..161S | role=calibration | The historic baseline power-law IMF used to calibrate the primary analytical SFRD fit and SN rates.
[REV02-P033] | Maeder, A. (1992, Astronomy and Astrophysics) | DOI:none; arXiv:none; ADS:1992A&A...264..105M | role=theory | Provides the foundational stellar nucleosynthetic yields necessary for calculating the metal enrichment tracking the SFRD.
[REV02-P034] | Asplund, M. et al. (2009, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev.astro.46.060407.145222; arXiv:0909.0948; ADS:2009ARA&A..47..481A | role=calibration | Updates the solar metallicity boundary, generating tensions with older models calculating cosmic enrichment.
[REV02-P035] | Chieffi, A. & Limongi, M. (2004, Astrophysical Journal) | DOI:10.1086/392523; arXiv:astro-ph/0402625; ADS:2004ApJ...608..405C | role=theory | Calculates the metallic yield returned to the IGM via supernovae as a function of the underlying SFR.
[REV02-P036] | Kewley, L. J. & Kobulnicky, H. A. (2007, Astrophysics and Space Science Proceedings) | DOI:10.1007/978-1-4020-5573-7\_75; arXiv:none; ADS:2007iuse.book..435K | role=measurement | Empirically traces the redshift evolution of global metallicity, modifying the conversion factors between UV light and SFR.
[REV02-P037] | Robertson, B. E. et al. (2013, Astrophysical Journal) | DOI:10.1088/0004-637X/768/1/71; arXiv:1301.1228; ADS:2013ApJ...768...71R | role=theory | Models the translation of the observed z>6 UV LF into the ionizing photon budget required to maintain cosmic reionization.
[REV02-P038] | Haardt, F. & Madau, P. (2012, Astrophysical Journal) | DOI:10.1088/0004-637X/746/2/125; arXiv:1105.2039; ADS:2012ApJ...746..125H | role=theory | Calculates hydrogen recombination timescales and the required IGM clumping factors to balance the reionization photon budget.
[REV02-P039] | Pei, Y. C. & Fall, S. M. (1995, Astrophysical Journal) | DOI:10.1086/176466; arXiv:none; ADS:1995ApJ...454...69P | role=theory | Early theoretical framework linking the observable cosmological mass density of HI to the overall comoving star formation.
[REV02-P040] | Lanzetta, K. M. et al. (1995, Astrophysical Journal) | DOI:10.1086/175286; arXiv:none; ADS:1995ApJ...440..435L | role=measurement | Damped-Lyman-alpha neutral-gas evolution and closed-box interpretation; not a direct cosmic SFR-density measurement.
[REV02-P041] | Meurer, G. R. et al. (1999, Astrophysical Journal) | DOI:10.1086/307523; arXiv:astro-ph/9903054; ADS:1999ApJ...521...64M | role=calibration | Local-starburst IRX-beta calibration applied to z~3 UV samples; applicability to other populations is not universal.
[REV02-P042] | Madau, P. et al. (1998, Astrophysical Journal) | DOI:10.1086/305523; arXiv:astro-ph/9708220; ADS:1998ApJ...498..106M | role=measurement | Early integrated-light CSFH inference to z~4 under then-current cosmology, IMF, and dust assumptions.
[REV02-P043] | Madau, P. et al. (1999, Astrophysical Journal) | DOI:10.1086/306975; arXiv:astro-ph/9809058; ADS:1999ApJ...514..648M | role=theory | Ionizing-source and clumpy-IGM budget model; conclusions depend on emissivity, escape fraction, and recombination assumptions.
[REV02-P044] | Li, C. & White, S. D. M. (2009, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2009.15268.x; arXiv:0901.0706; ADS:2009MNRAS.398.2177L | role=measurement | Low-redshift SDSS stellar-mass distribution under a standard IMF; not a high-redshift mass-function measurement.

REVIEW_BASE_02_DR_COMPLETE_REFERENCE_ONLY
