import json
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
RAW = AREA / "area_review_02_madau_dickinson_2014_DR_RAW_PACKET.md"
REGISTRY = AREA / "area_review_02_madau_dickinson_2014_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_02_madau_dickinson_2014_DR_PACKET.md"
registry = json.loads(REGISTRY.read_text())

body = """# Review Base 02 canonical advisory packet — Madau & Dickinson 2014

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
"""

primary = [row["source"] for row in registry["rows"] if row["source"]["source_class"] == "primary"]
supporting = [row["source"] for row in registry["rows"] if row["source"]["source_class"] != "primary"]
for s in primary:
    body += f"\n[{s['key']}] {s['authors']} ({s['year']}, {s['journal']}) | title={s['title']} | DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']} | role={s['role']} | review_locator={s['review_locator']} | {s['boundary']}"
body += "\n\n### Supporting cited reviews/proceeding — not counted as primary\n"
for s in supporting:
    body += f"\n[{s['key']}] {s['authors']} ({s['year']}, {s['journal']}) | title={s['title']} | DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']} | role={s['role']} | review_locator={s['review_locator']} | {s['boundary']}"

body += "\n\n## 7. DO_NOT_USE_UNVERIFIED\n\n"
for row in registry["rows"]:
    raw = row.get("raw_identity")
    if raw and row.get("corrected_from_raw"):
        s = row["source"]
        body += f"UNCITED_NOT_USABLE | raw {s['key']} tuple title={raw['title']}; DOI:{raw['doi']}; arXiv:{raw['arxiv']}; ADS:{raw['ads_bibcode']} | cross-wired, uncited, or nonexistent composite identity | usable replacement is exact cited tuple title={s['title']}; DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']}\n"
concepts = [
    "UNCITED_NOT_USABLE | one survey alone supplies a complete cosmic SFR density | overbroad claim | multi-tracer coverage, limits, dust, and cosmic variance remain",
    "UNCITED_NOT_USABLE | dust corrections are redshift-independent | overbroad claim | attenuation depends on population, geometry, and calibration",
    "UNCITED_NOT_USABLE | the IMF is observationally fixed across cosmic time | unsupported extrapolation | the review adopts an IMF for conversion and closure",
    "UNCITED_NOT_USABLE | stellar-mass-density agreement proves exact closure | overbroad claim | a model-dependent residual offset remains",
    "UNCITED_NOT_USABLE | the review-fit peak is selection- and model-free | overbroad claim | heterogeneous tracers and the analytic form set the result",
    "UNCITED_NOT_USABLE | bright detected z>6 galaxies alone close reionization | unsupported closure | faint-end, escape fraction, and recombination assumptions dominate",
    "UNCITED_NOT_USABLE | post-2014/JWST source anchors captured by web search | outside date and not review-cited | excluded from all usable rows",
    "UNCITED_NOT_USABLE | AGN-centered accretion or feedback source | outside non-AGN core scope | not promoted in this packet",
]
body += "\n".join(concepts) + "\n"

body += "\n## 8. Review and source identity ledger\n\n"
body += "[REV02] | Madau & Dickinson (2014, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev-astro-081811-125615; arXiv:1403.0007; ADS:2014ARA&A..52..415M | role=review | 2014 bounded cosmic-SFH synthesis\n"
for row in registry["rows"]:
    s = row["source"]
    body += f"[{s['key']}] | {s['authors']} ({s['year']}, {s['journal']}) | DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']} | role={s['role']} | {s['boundary']}\n"
body += "\nREVIEW_BASE_02_DR_COMPLETE_REFERENCE_ONLY\n"
OUT.write_text(body)
print(json.dumps({"canonical_packet": str(OUT), "chars": len(body), "lines": len(body.splitlines()), "primary": len(primary), "supporting": len(supporting)}, sort_keys=True))
