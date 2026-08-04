import json
import re
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
RAW = AREA / "area_review_01_kennicutt_evans_2012_DR_RAW_PACKET.md"
REGISTRY = AREA / "area_review_01_kennicutt_evans_2012_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_01_kennicutt_evans_2012_DR_PACKET.md"

registry = json.loads(REGISTRY.read_text())
assert registry["status"] == "PASS" and registry["pass_count"] == 43 and registry["fail_count"] == 0

body = """# Review Base 01 verified source packet — Kennicutt & Evans 2012

status: READY_FOR_HWAO_REVIEW
advisory_only: true
canonical_packet_released: true
wiki_write_performed_by_tori: false
conversation_deleted: false

Review: Robert C. Kennicutt Jr. & Neal J. Evans II (2012), *Star Formation in the Milky Way and Nearby Galaxies*, ARA&A 50, 531-608.
Verified review identity: DOI `10.1146/annurev-astro-081811-125610`; arXiv `1204.3552`; ADS `2012ARA&A..50..531K`.
Raw-custody packet: `area_review_01_kennicutt_evans_2012_DR_RAW_PACKET.md`
Composite registry: `area_review_01_kennicutt_evans_2012_CURATED_SOURCE_REGISTRY.json`
Verification status: PASS — 43/43 physical primary rows; 25 raw composite rows corrected; 20 phantom source keys quarantined.
Method: authoritative review bibliography membership via Crossref structured references and the NED review reference page; exact source identity via public ADS abstract route/title, Crossref DOI record, and arXiv export metadata. Hwao's ADS API verifier and jury remain the live-wiki gate.

## 1. Review identity and scope map

[REV01-S01] SFR indicators and calibrations | Supports review-era FUV/NUV, recombination-line, IR, radio, X-ray, and hybrid calibrations with explicit IMF, star-formation-history, metallicity, dust, cirrus, leakage, and stochastic-sampling boundaries. Does not support treating one conversion as universal.

[REV01-S02] Gas inventories and mass tracers | Supports bounded use of HI, CO-derived H2, dust extinction/emission, gamma rays, and dense-gas tracers. Does not support conflating HI, H2, total gas, CO-bright gas, CO-dark gas, or dense gas.

[REV01-S03] Milky Way clouds and nearby galaxies | Connects YSO-counting and cloud-scale measurements to resolved and global galaxy relations. Spatial scales, apertures, tracers, and averaging must remain explicit.

[REV01-S04] Star-formation laws | Supports integrated total-gas, resolved molecular, low-density/HI-dominated, and dense-gas relations as distinct empirical regimes. It does not establish one scale-free universal power law.

[REV01-S05] Efficiencies and timescales | Supports instantaneous depletion-time and efficiency ratios under stated assumptions. It does not make depletion time a guaranteed future exhaustion clock.

[REV01-S06] Theory interface | Reviews gravity, turbulence, chemistry, free-fall scaling, and feedback interpretations. Models demonstrate mechanisms or reproduce relations; they do not by themselves establish observational prevalence.

[REV01-S07] Temporal boundary | The packet represents the review's 2012 status. Post-2012 ALMA/JWST results, later IMF claims, and subsequent calibrations require separate source packets and must not be back-projected into this review.

## 2. Established findings

[REV01-E01]
role: established
epistemic_type: observation
finding: Disk-averaged total-gas measurements spanning normal spirals and starbursts yield a super-linear global Schmidt relation, with the foundational combined fit near index 1.4.
scope/boundary: Integrated HI+H2 surface density and integrated SFR indicators; the fitted slope depends on sample mixing, aperture, regression, and CO-to-H2 conversion. It is not the resolved molecular-only law.
review_basis: Section 6.1 and Figure 11.
trust_score: 0.96
sources: [REV01, REV01-P001, REV01-P003]

[REV01-E02]
role: established
epistemic_type: observation
finding: Integrated infrared luminosity correlates approximately linearly with HCN(1-0) luminosity across galaxies, and the relation extends toward massive Milky Way clumps.
scope/boundary: HCN luminosity is a dense-gas proxy whose excitation, abundance, optical depth, and conversion to mass can vary. Linearity does not prove a universal dense-gas SFE or one causal unit of star formation.
review_basis: Section 6.1.
trust_score: 0.89
sources: [REV01, REV01-P005, REV01-P006]

[REV01-E03]
role: established
epistemic_type: observation
finding: In nearby normal disks at roughly sub-kiloparsec to kiloparsec resolution, SFR surface density correlates more closely with CO-traced molecular gas than with HI surface density.
scope/boundary: Main optical disks in THINGS/HERACLES-related samples; standard CO conversion and UV+IR SFR tracers. Correlation does not prove that H2 chemistry is causally required for collapse.
review_basis: Section 6.3 and Figure 12.
trust_score: 0.94
sources: [REV01, REV01-P007, REV01-P008]

[REV01-E04]
role: established
epistemic_type: observation
finding: Nearby resolved samples commonly show HI surface-density saturation near roughly 9-10 solar masses per square parsec and much lower star-formation efficiency in HI-dominated outer disks.
scope/boundary: Empirical local-sample scale, not a hard universal ceiling; metallicity, shielding, opacity, inclination, and resolution matter.
review_basis: Sections 6.3 and 7.1.
trust_score: 0.90
sources: [REV01, REV01-P007, REV01-P011, REV01-P043]

[REV01-E05]
role: established
epistemic_type: calibration
finding: The review updates commonly used SFR conversions to a Kroupa IMF and modern population synthesis, producing lower inferred SFRs than older Salpeter-IMF calibrations for the same luminosity.
scope/boundary: Continuous-SFR assumptions and tracer-specific response times; metallicity, dust, leakage, cirrus, and IMF sampling remain systematic limits.
review_basis: Section 3.8 and Table 1.
trust_score: 0.95
sources: [REV01, REV01-P015, REV01-P016, REV01-P017, REV01-P018]

[REV01-E06]
role: established
epistemic_type: observation
finding: Nearby molecular clouds form stars inefficiently when their recent YSO-counted SFR is compared with total cloud mass, free-fall time, and crossing time.
scope/boundary: Local Spitzer cloud samples and approximately two-million-year YSO census windows. Cloud selection, lifetime, dense-gas definition, and SFR timescale prevent direct substitution into galaxy-integrated relations.
review_basis: Sections 4.3-4.4.
trust_score: 0.91
sources: [REV01, REV01-P012, REV01-P014]

[REV01-E07]
role: established
epistemic_type: observation
finding: Within nearby clouds, recent star formation is concentrated toward high-extinction, high-column-density material, and total SFR correlates more closely with mass above a dense threshold than with total cloud mass.
scope/boundary: Extinction-selected local clouds; threshold values depend on dust conversion, geometry, completeness, and YSO timescale. This is not proof of a universal sharp physical threshold.
review_basis: Sections 4.4 and 7.1.3.
trust_score: 0.88
sources: [REV01, REV01-P012, REV01-P013]

[REV01-E08]
role: established
epistemic_type: calibration
finding: CO-to-H2 conversion is environment-dependent because CO chemistry, excitation, optical depth, cloud structure, metallicity, radiation field, temperature, and dynamics vary.
scope/boundary: Diffuse gas, normal disks, low-metallicity systems, dense centers, and starbursts cannot be represented safely by one unqualified conversion factor.
review_basis: Section 2.4.
trust_score: 0.94
sources: [REV01, REV01-P028, REV01-P030, REV01-P034, REV01-P035, REV01-P036, REV01-P037, REV01-P038, REV01-P039]

[REV01-E09]
role: established
epistemic_type: observation
finding: Gamma-ray and dust analyses reveal gas not adequately traced by standard HI and CO maps, including CO-faint molecular envelopes.
scope/boundary: Local Milky Way regions and tracer-model assumptions. The evidence does not justify assigning one universal dark-gas fraction or treating all excess material as H2.
review_basis: Section 2.4.
trust_score: 0.87
sources: [REV01, REV01-P020]

[REV01-E10]
role: established
epistemic_type: calibration
finding: Conversions between extinction or reddening and gas column depend on dust properties and metallicity and differ between the Milky Way, LMC, and SMC.
scope/boundary: Diffuse sightlines and adopted extinction curves; dense-cloud grain evolution and emission opacity require separate calibration.
review_basis: Section 2.3.
trust_score: 0.92
sources: [REV01, REV01-P025, REV01-P026]

[REV01-E11]
role: established
epistemic_type: observation
finding: Star-formation relations depend on spatial averaging; resolved measurements expose environmental and evolutionary scatter hidden by whole-galaxy averages.
scope/boundary: Nearby-galaxy integral-field, CO, HI, UV, and IR mapping. The exact breakdown scale was not fixed in 2012.
review_basis: Sections 6.2-6.3.
trust_score: 0.86
sources: [REV01, REV01-P007, REV01-P008, REV01-P041, REV01-P042]

[REV01-E12]
role: established
epistemic_type: review_synthesis
finding: The review organizes galaxy-scale star formation into low-density HI-dominated, normal molecular-disk, and high-density starburst regimes with differing empirical efficiencies and dominant systematics.
scope/boundary: A useful 2012 synthesis, not three immutable physical classes or exact universal surface-density boundaries.
review_basis: Section 7.1 and Table 3.
trust_score: 0.87
sources: [REV01, REV01-P003, REV01-P011, REV01-P040]

## 3. Open debates and tensions

[REV01-D01]
role: debate
debate_topic: Discrete disk/starburst sequences versus a continuous star-formation law.
competing_positions: High-redshift disks and starbursts were presented as offset sequences; continuous environmental changes in CO conversion and dynamical state can reduce apparent bimodality.
why_unresolved_2012: Gas masses, excitation, conversion factors, geometry, and targeted selection covaried.
boundary: Integrated high-redshift and local samples, not resolved cloud physics.
trust_score: 0.84
sources: [REV01, REV01-P009, REV01-P010, REV01-P038]

[REV01-D02]
role: debate
debate_topic: Long-lived supported molecular clouds versus rapidly evolving turbulent clouds.
competing_positions: Slow star formation can reflect support/regulation over many dynamical times; turbulent assembly and disruption can make clouds transient while ensemble depletion times remain long.
why_unresolved_2012: Gas assembly lacks a direct clock, YSO ages sample only the stellar phase, and simulations depend on feedback, magnetic fields, and cloud definitions.
boundary: Milky Way cloud demographics and models; not galaxy-integrated depletion time.
trust_score: 0.76
sources: [REV01, REV01-P014, REV01-P036, REV01-P040]

[REV01-D03]
role: debate
debate_topic: Chemical shielding transition versus gravitational/dynamical threshold in outer disks.
competing_positions: Low SFE may follow failure to form shielded molecular gas, or large-scale disk stability and low midplane pressure may inhibit collapse.
why_unresolved_2012: Column density, metallicity, stellar density, pressure, and galactocentric radius covary.
boundary: Local outer disks, low-surface-brightness systems, and model interpretations.
trust_score: 0.79
sources: [REV01, REV01-P011, REV01-P040, REV01-P043]

[REV01-D04]
role: debate
debate_topic: Which tracer provides the least biased molecular-gas mass.
competing_positions: CO luminosity is practical and empirically calibrated; dust, gamma rays, isotopologues, and chemistry models expose CO-faint gas and environment-dependent conversion.
why_unresolved_2012: Every alternative inherits dust, cosmic-ray, abundance, excitation, geometry, or radiative-transfer assumptions.
boundary: Separate diffuse Milky Way gas, dense cores, nearby galaxies, low metallicity, and starbursts.
trust_score: 0.90
sources: [REV01, REV01-P020, REV01-P024, REV01-P025, REV01-P028, REV01-P030, REV01-P034, REV01-P035, REV01-P036, REV01-P037, REV01-P038, REV01-P039]

[REV01-D05]
role: debate
debate_topic: Constant versus environment-dependent efficiency per free-fall time.
competing_positions: Unified models use a low approximately constant efficiency per free-fall time; cloud and galaxy measurements can imply changes with density, tracer, or regime.
why_unresolved_2012: Volume density, geometry, cloud boundaries, dense-gas conversion, and SFR averaging timescale are uncertain.
boundary: Do not compare local dense clumps directly with disk-averaged surface densities without a scale model.
trust_score: 0.77
sources: [REV01, REV01-P012, REV01-P014, REV01-P040]

[REV01-D06]
role: debate
debate_topic: Whether the IR-HCN relation reflects a universal dense-gas SFE.
competing_positions: Approximate linearity can indicate proportional star formation per dense-gas proxy; it can also arise from tracer excitation, selection, abundance, or changing dense-gas fraction.
why_unresolved_2012: HCN was faint outside bright clumps and galaxy centers, and dense-gas mass conversion was poorly constrained.
boundary: Integrated galaxies and massive Milky Way clumps; not all molecular gas.
trust_score: 0.79
sources: [REV01, REV01-P005, REV01-P006, REV01-P012, REV01-P027]

[REV01-D07]
role: debate
debate_topic: A single global power law versus scale- and phase-dependent relations.
competing_positions: Whole-galaxy total-gas data give a compact super-linear law; resolved molecular data are closer to linear and low-density HI-dominated regions fall below simple extrapolations.
why_unresolved_2012: Gas phase, spatial scale, diffuse emission, selection, regression, and conversion factor differ across studies.
boundary: Keep integrated total gas, resolved H2, and outer-disk HI distinct.
trust_score: 0.93
sources: [REV01, REV01-P003, REV01-P007, REV01-P008, REV01-P011, REV01-P041, REV01-P042, REV01-P043]

[REV01-D08]
role: debate
debate_topic: Whether H2 is causally necessary for star formation or mainly co-locates with shielded cold gas.
competing_positions: Observed SFR-H2 correlation motivates a precursor interpretation; chemistry/turbulence models allow molecule formation and gravitational collapse to share environmental causes.
why_unresolved_2012: The decisive tests require low-metallicity regimes where molecular-formation and dynamical times separate, with reliable CO-dark gas accounting.
boundary: Correlation does not determine causal direction.
trust_score: 0.74
sources: [REV01, REV01-P008, REV01-P036, REV01-P039, REV01-P040]

## 4. Key measurements and calibrations

[REV01-N01]
role: measurement
metric: Review Table 1 Kroupa-IMF SFR constants.
value: log Cx values include FUV 43.35, NUV 43.17, H-alpha 41.27, TIR 43.41, 24-micron 42.69, 70-micron 43.23, 1.4-GHz 28.20, and 2-10-keV 39.77 in the review's stated luminosity units.
boundary: Tracer response times and continuous-SFR assumptions differ; dust, metallicity, cirrus, leakage, binaries, and IMF sampling matter.
trust_score: 0.94
sources: [REV01, REV01-P015, REV01-P016, REV01-P017, REV01-P018, REV01-P019]

[REV01-N02]
role: measurement
metric: Global total-gas Schmidt exponent.
value: Approximately N=1.4 in the foundational combined normal-disk plus starburst fit.
boundary: Disk averages, total gas, legacy SFR scale, and adopted CO conversion; not a resolved H2-only exponent.
trust_score: 0.96
sources: [REV01, REV01-P003]

[REV01-N03]
role: measurement
metric: Nearby-disk molecular depletion time.
value: Roughly 1-2 Gyr under standard CO-to-H2 and UV+IR calibrations.
boundary: Sub-kiloparsec/kiloparsec normal-disk averages; conversion factor, centers, starbursts, and low metallicity differ; not a future exhaustion clock.
trust_score: 0.91
sources: [REV01, REV01-P007, REV01-P008]

[REV01-N04]
role: measurement
metric: Nearby-cloud recent depletion time.
value: Approximately 82 Myr for the c2d cloud sample, compared in the review with mean free-fall time about 1.4 Myr and crossing time about 5.5 Myr.
boundary: YSO-counted recent SFR, selected local clouds, and review definitions; not directly comparable to galaxy-wide CO depletion time.
trust_score: 0.88
sources: [REV01, REV01-P014]

[REV01-N05]
role: measurement
metric: Characteristic resolved HI saturation scale.
value: Approximately 9-10 solar masses per square parsec in the cited nearby samples.
boundary: Empirical characteristic scale, not a strict universal maximum.
trust_score: 0.89
sources: [REV01, REV01-P007, REV01-P011]

[REV01-N06]
role: measurement
metric: Integrated dense-gas relation.
value: IR luminosity versus HCN(1-0) luminosity is approximately linear over the cited galaxy/clump range.
boundary: HCN luminosity is not an environment-invariant dense-gas mass; the result does not establish universal dense-gas SFE.
trust_score: 0.87
sources: [REV01, REV01-P005, REV01-P006]

[REV01-N07]
role: measurement
metric: Standard Milky-Way CO-to-H2 factor used by the review.
value: X_CO approximately 2.3e20 H2 molecules per square centimeter per K km s^-1.
boundary: Review-era standard with order-unity cloud-scale uncertainty and strong environmental failure modes.
trust_score: 0.89
sources: [REV01, REV01-P028, REV01-P030, REV01-P037, REV01-P038]

[REV01-N08]
role: measurement
metric: Diffuse Milky-Way gas-to-reddening ratio.
value: N(HI)+2N(H2) approximately 5.8e21 cm^-2 E(B-V)^-1.
boundary: Diffuse solar-neighborhood sightlines and standard extinction; dense clouds and low-metallicity systems differ.
trust_score: 0.94
sources: [REV01, REV01-P025]

## 5. What remained unknown in 2012

[REV01-U01]
role: future
gap: The scale and physical cause of star-formation-law decorrelation below kiloparsec averaging.
needed: Matched cloud-scale gas, young-star, and feedback mapping with temporal modeling.
trust_score: 0.84
sources: [REV01, REV01-P007, REV01-P041, REV01-P042]

[REV01-U02]
role: future
gap: The amount and environmental distribution of CO-dark gas and the calibration of CO-independent mass tracers.
needed: Joint gamma-ray, dust, [CII], isotopologue, and metallicity constraints.
trust_score: 0.85
sources: [REV01, REV01-P020, REV01-P035, REV01-P038]

[REV01-U03]
role: future
gap: Whether high-redshift disks and starbursts truly occupy separate star-formation sequences.
needed: Resolved multi-transition gas imaging, dynamical masses, and continuous conversion-factor calibration.
trust_score: 0.78
sources: [REV01, REV01-P009, REV01-P010, REV01-P038]

[REV01-U04]
role: future
gap: Molecular-cloud assembly, lifetime, fragmentation, and disruption chronology.
needed: Cloud population time-ordering, magnetic/turbulent structure, dense-core mapping, and feedback-coupled simulations.
trust_score: 0.78
sources: [REV01, REV01-P014, REV01-P027, REV01-P036, REV01-P040]

[REV01-U05]
role: future
gap: Star formation and gas-mass calibration in very low-metallicity and HI-dominated systems.
needed: CO-dark-gas accounting plus dust, [CII], HI, young-star, and chemistry measurements across metallicity.
trust_score: 0.81
sources: [REV01, REV01-P039, REV01-P043]

[REV01-U06]
role: future
gap: Separating true low-SFR thresholds from tracer response time and stochastic high-mass-star sampling.
needed: Probabilistic population synthesis and matched UV, recombination-line, IR, and resolved stellar-population data.
trust_score: 0.80
sources: [REV01, REV01-P015, REV01-P016, REV01-P017, REV01-P018, REV01-P043]

## 6. Primary-citation harvest

"""

harvest = []
ledger = []
for row in registry["rows"]:
    source = row["source"]
    harvest.append(
        f"[{source['key']}] {source['authors']} ({source['year']}, {source['journal']}) | title={source['title']} | "
        f"DOI:{source['doi']}; arXiv:{source['arxiv']}; ADS:{source['bibcode']} | role={source['role']} | "
        f"review_locator={source['review_locator']} | {source['boundary']}"
    )
    ledger.append(
        f"{source['key']} | {source['authors']} ({source['year']}, {source['journal']}) | "
        f"DOI:{source['doi']}; arXiv:{source['arxiv']}; ADS:{source['bibcode']} | role={source['role']} | {source['boundary']}"
    )

raw_result = RAW.read_text().split("## Deep Research review-base result\n\n", 1)[1].split("\n\n## Captured external source anchors", 1)[0]
raw_rows = {}
pattern = re.compile(r"^\[(REV01-P\d{3})\] (.+?) \((\d{4}), ([^)]+)\) \| title=(.+?) \| DOI:([^;]+); arXiv:([^;]+); ADS:(\S+) \| role=(\S+) \| review_locator=(.+?) \| (.+)$", re.M)
for match in pattern.finditer(raw_result):
    key, authors, year, journal, title, doi, arxiv, bibcode, role, locator, boundary = match.groups()
    raw_rows[key] = {"title": title, "doi": doi.strip(), "arxiv": arxiv.strip(), "bibcode": bibcode}

quarantine = []
for row in registry["rows"]:
    source = row["source"]
    raw = raw_rows[source["key"]]
    changed = [field for field in ("title", "doi", "arxiv") if raw[field] != source[field]]
    if changed:
        quarantine.append(
            f"UNCITED_NOT_USABLE | raw {source['key']} tuple: title={raw['title']}; DOI={raw['doi']}; arXiv={raw['arxiv']}; ADS={raw['bibcode']} | "
            f"cross-wired fields={','.join(changed)} | use only corrected canonical row with DOI={source['doi']}; arXiv={source['arxiv']}; ADS={source['bibcode']}"
        )
for key in registry["phantom_source_keys_quarantined"]:
    quarantine.append(f"UNCITED_NOT_USABLE | {key} | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented")
quarantine.extend([
    "UNCITED_NOT_USABLE | Post-2012 ALMA, JWST, or later-review result | outside Kennicutt & Evans 2012 citation boundary | place in its own later source packet",
    "UNCITED_NOT_USABLE | Depletion time is a guaranteed exhaustion clock | overbroad interpretation | inflow, outflow, recycling, phase conversion, and changing SFR break the claim",
    "UNCITED_NOT_USABLE | HI, H2, total gas, CO-bright gas, CO-dark gas, and dense gas are interchangeable | phase/tracer conflation | keep separate quantities and calibrations",
    "UNCITED_NOT_USABLE | IR-HCN linearity proves universal dense-gas SFE | tracer-to-mass and selection overclaim | retain excitation, abundance, opacity, and environment caveats",
    "UNCITED_NOT_USABLE | HI has a strict universal 10 solar-mass-per-square-parsec ceiling | hard-threshold overclaim | retain empirical local-sample boundary",
    "UNCITED_NOT_USABLE | H2-SFR correlation proves molecular chemistry is causally necessary for collapse | correlation-to-causation error | retain shielded-cold-gas alternative",
    "UNCITED_NOT_USABLE | One SFR calibration is independent of IMF, metallicity, history, dust, leakage, or stochastic sampling | calibration overclaim | use tracer-specific review assumptions",
    "UNCITED_NOT_USABLE | A model mechanism establishes observational prevalence | epistemic-type error | label theory and require observations separately",
    "UNCITED_NOT_USABLE | Raw external source-anchor list | contaminated search custody containing post-2012 and unrelated links | never use as the canonical source base",
])

final = body + "\n".join(harvest) + "\n\n## 7. DO_NOT_USE_UNVERIFIED\n\n" + "\n".join(quarantine) + "\n\n## 8. Review and source identity ledger\n\n"
final += "REV01 | Kennicutt & Evans (2012, ARA&A) | DOI:10.1146/annurev-astro-081811-125610; arXiv:1204.3552; ADS:2012ARA&A..50..531K | role=review | Authoritative 2012 synthesis; later literature requires separate packets.\n"
final += "\n".join(ledger) + "\n\nREVIEW_BASE_01_VERIFIED_READY_REFERENCE_ONLY\n"
OUT.write_text(final)
print(json.dumps({"status": "READY_FOR_HWAO_REVIEW", "sources": len(harvest), "corrected_raw_rows": len([line for line in quarantine if "cross-wired fields=" in line]), "phantom_keys": len(registry["phantom_source_keys_quarantined"]), "packet": str(OUT)}))
