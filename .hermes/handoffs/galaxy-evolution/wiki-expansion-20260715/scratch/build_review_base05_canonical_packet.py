import json
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
REGISTRY = AREA / "area_review_05_maiolino_mannucci_2019_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_05_maiolino_mannucci_2019_DR_PACKET.md"
reg = json.loads(REGISTRY.read_text())
sources = {r["key"]: r for r in reg["usable_sources"]}

claims = [
("## 1. Review Identity and Scope Map", [
("REV05-R00", "review_identity", "review_synthesis", "Maiolino & Mannucci (2019), *De re metallica: the cosmic chemical evolution of galaxies*, is verified as DOI 10.1007/s00159-018-0112-2, arXiv 1811.09642, ADS 2019A&ARv..27....3M.", "Review-wide synthesis through 2019; non-AGN chemical evolution; post-2019/JWST work excluded.", ["REV05-R00"]),
("REV05-S01", "scope", "review_synthesis", "The source base covers metal production, gas-phase and stellar abundance diagnostics, MZR/FMR relations, abundance ratios, spatial gradients, metal budgets, and bounded models.", "Gas, stars, neutral gas, CGM, and ICM remain distinct phases; calibration, IMF, aperture, and redshift boundaries are mandatory.", ["REV05-R00"]),
]),
("## 2. Established Findings", [
("REV05-E01", "scaling_relation", "observation", "The local gas-phase mass-metallicity relation rises with stellar mass and flattens above a calibration-dependent turnover.", "SDSS star-forming fibers near z≈0.1; oxygen scale and stellar-mass IMF must be fixed.", ["REV05-P001","REV05-P008"]),
("REV05-E02", "secondary_relation", "observation", "At fixed stellar mass, several local analyses find lower gas-phase metallicity at higher SFR, but its amplitude depends on selection and analysis choices.", "Local star-forming samples; same abundance calibration, aperture correction, and SFR estimator required.", ["REV05-P003","REV05-P041","REV05-P042"]),
("REV05-E03", "abundance_ratio", "review_synthesis", "Nitrogen exhibits primary-like behavior at low O/H and an increasing secondary contribution at higher O/H, with delayed intermediate-mass-star enrichment affecting N/O.", "H II-region gas abundances; yields, time delays, and direct-versus-strong-line scale remain coupled.", ["REV05-P020","REV05-P021"]),
("REV05-E04", "regulator_framework", "analytic_theory", "Gas-regulator models express metallicity as a balance among inflow, star formation, recycling, yields, and outflow rather than as a closed-box clock.", "Quasi-equilibrium and mixing assumptions are model premises, not universal observations.", ["REV05-P011","REV05-P012","REV05-P013"]),
("REV05-E05", "spatial_distribution", "observation", "Most local non-interacting star-forming disks show negative gas-phase radial abundance gradients when radii and calibrations are normalized consistently.", "H II-region/IFU gas-phase oxygen; sample cuts, DIG, bars, and radial normalization matter.", ["REV05-P018","REV05-P019"]),
("REV05-E06", "diagnostic_baseline", "calibration", "Strong-line metallicity calibrations disagree substantially in absolute O/H, although internally consistent transformations can recover relative trends.", "H II-region gas phase only; direct, empirical, and photoionization-model scales are not interchangeable.", ["REV05-P002","REV05-P004","REV05-P015","REV05-P030","REV05-P031"]),
("REV05-E07", "metal_budget", "observation", "A large fraction of metals synthesized by galaxies is not in their stars and cold ISM, and metal-bearing circumgalactic gas is therefore a required budget component.", "Ionization corrections and unobserved hot phases dominate the CGM inventory uncertainty.", ["REV05-P007","REV05-P009","REV05-P010"]),
("REV05-E08", "redshift_evolution", "observation", "Gas-phase MZR measurements at z≈2–3.5 generally lie below local relations when compared on a controlled abundance scale.", "Pre-JWST rest-optical samples; line selection, excitation, aperture, and calibration evolution limit absolute comparison.", ["REV05-P027","REV05-P028","REV05-P029"]),
("REV05-E09", "chemical_clock", "observation", "Enhanced stellar [alpha/Fe] in rapidly formed early-type populations is consistent with short formation times relative to delayed Type Ia iron enrichment.", "Integrated stellar populations; stellar libraries, response functions, IMF, and star-formation-history assumptions apply.", ["REV05-P023"]),
("REV05-E10", "gradient_perturbation", "observation", "Interactions and rapid inflow can flatten or invert gas-phase abundance gradients relative to isolated disks.", "Merger stage, beam smearing, spatial sampling, and abundance calibration must be controlled.", ["REV05-P034","REV05-P036"]),
("REV05-E11", "effective_yield", "review_synthesis", "Low-mass systems have lower effective yields than simple closed-box expectations, consistent with inflow and/or preferential metal loss.", "Effective yield is inferred from gas fraction and gas-phase abundance; it does not uniquely identify one mechanism.", ["REV05-P032","REV05-P033","REV05-P051"]),
("REV05-E12", "cross_tracer_check", "observation", "Direct-method nebular abundances can agree more closely with young-star abundances than some model-based strong-line scales in resolved nearby systems.", "Young stars and co-spatial H II regions; this does not make gas and stellar metallicities generally interchangeable.", ["REV05-P014","REV05-P044","REV05-P045"]),
]),
("## 3. Open Debates and Tensions", [
("REV05-D01", "abundance_scale", "calibration", "Electron-temperature, recombination-line, and photoionization-model methods do not share one settled absolute abundance scale.", "Temperature fluctuations, depletion, geometry, atomic data, and model priors remain entangled.", ["REV05-P002","REV05-P004","REV05-P015","REV05-P030","REV05-P031"]),
("REV05-D02", "nitrogen_origin", "review_synthesis", "The relative massive-star and intermediate-mass-star contributions to primary nitrogen remain yield- and timescale-dependent.", "N/O cannot be mapped to one age or metallicity without a chemical-evolution model.", ["REV05-P020","REV05-P021","REV05-P022"]),
("REV05-D03", "fmr_reality", "observation", "The existence, strength, and redshift invariance of a universal M-Z-SFR surface remained disputed in 2019.", "Selection, aperture, S/N cuts, calibration, and correlated errors can create or suppress residual trends.", ["REV05-P003","REV05-P005","REV05-P041","REV05-P042","REV05-P050"]),
("REV05-D04", "mzr_driver", "review_synthesis", "The MZR alone cannot separate mass-dependent outflow, inflow dilution, star-formation efficiency, recycling, and enriched reaccretion.", "Several regulator and simulation parameter combinations reproduce similar scaling relations.", ["REV05-P008","REV05-P011","REV05-P012","REV05-P033","REV05-P048"]),
("REV05-D05", "gradient_evolution", "observation", "The frequency of genuinely flat or inverted high-redshift gradients remained uncertain because beam smearing and selection can mimic them.", "Compare matched tracers and resolution; local normalized slopes are not a universal high-z baseline.", ["REV05-P006","REV05-P018","REV05-P019","REV05-P034","REV05-P036","REV05-P049"]),
("REV05-D06", "yield_imf_delay", "review_synthesis", "Yield tables, IMF shape, stellar rotation/binarity, and enrichment delays remain degenerate in abundance-ratio fits.", "An apparent yield change need not imply an IMF change.", ["REV05-P020","REV05-P023","REV05-P032","REV05-P037"]),
("REV05-D07", "highz_diagnostics", "observation", "Harder ionizing spectra, density, ionization parameter, and N/O evolution complicate use of local strong-line calibrations at z≈2–3.", "BPT offsets bound diagnostic transfer; they are not an AGN-demographic result here.", ["REV05-P024","REV05-P025","REV05-P026","REV05-P027"]),
("REV05-D08", "missing_metals", "observation", "The location and ionization state of the remaining galactic and cosmic metal budget were unresolved in 2019.", "Cool-CGM inventories exclude poorly constrained hot and diffuse phases.", ["REV05-P007","REV05-P009","REV05-P010"]),
]),
("## 4. Key Measurements, Model Benchmarks, and Calibrations", [
("REV05-N01", "solar_reference", "calibration", "A commonly adopted solar oxygen abundance is 12+log(O/H)=8.69.", "Solar photospheric reference from a supporting synthesis; changing the solar scale shifts normalized metallicities.", ["REV05-P043"]),
("REV05-N02", "mzr_turnover", "observation", "The SDSS gas-phase MZR steepens below and flattens above a characteristic stellar mass of order 10^10.5 solar masses.", "Local fiber sample and adopted stellar masses/strong-line model scale.", ["REV05-P001","REV05-P008"]),
("REV05-N03", "calibration_offset", "calibration", "Published strong-line methods can differ by up to roughly 0.7 dex in inferred 12+log(O/H) for the same galaxy sample.", "Maximum method-to-method systematic, not measurement scatter within one scale.", ["REV05-P015"]),
("REV05-N04", "fmr_scatter", "observation", "The original local FMR parameterization reported residual metallicity scatter near 0.05 dex.", "SDSS selection and that paper's calibration/parameterization; later analyses question universality.", ["REV05-P003","REV05-P042"]),
("REV05-N05", "nitrogen_plateau", "observation", "Low-metallicity systems show an approximate primary-nitrogen plateau near log(N/O)≈-1.5, with substantial object and method scatter.", "Ionized-gas measurements; ionization corrections and delayed enrichment apply.", ["REV05-P020","REV05-P021"]),
("REV05-N06", "gradient_scale", "observation", "CALIFA disks yielded a characteristic normalized oxygen-abundance slope of order -0.1 dex per effective radius.", "Non-interacting local disks on the adopted calibration and radial fit range.", ["REV05-P018"]),
("REV05-N07", "highz_mzr_offset", "observation", "Pre-JWST z≈3–3.5 samples reported gas-phase metallicities lower than local galaxies by several tenths of a dex at fixed stellar mass.", "Not an absolute universal offset: calibrations, excitation, and sample selection dominate cross-redshift comparison.", ["REV05-P028","REV05-P029"]),
("REV05-N08", "retained_metal_fraction", "observation", "Nearby-galaxy accounting placed only a minority—of order one quarter—of produced metals in stars, the ISM, and dust, with additional metals inferred in the CGM.", "Inventory depends on assumed yields, IMF, ionization corrections, and poorly observed hot gas.", ["REV05-P007","REV05-P009"]),
]),
("## 5. What Remained Unknown in 2019", [
("REV05-U01", "absolute_oxygen_scale", "review_synthesis", "The absolute nebular oxygen scale remained uncertain.", "Joint auroral, recombination-line, IR, and stellar-abundance measurements in matched regions were needed.", ["REV05-P004","REV05-P015","REV05-P045"]),
("REV05-U02", "fmr_evolution", "review_synthesis", "Whether one FMR is invariant over cosmic time remained unknown.", "Calibration-matched, representative samples with controlled apertures and gas measurements were needed.", ["REV05-P003","REV05-P042","REV05-P050"]),
("REV05-U03", "highz_ionization", "review_synthesis", "The physical mixture producing the high-redshift nebular diagnostic offset was unresolved.", "Stellar UV, rest-optical, density, and direct-temperature constraints in the same galaxies were needed.", ["REV05-P024","REV05-P025","REV05-P026"]),
("REV05-U04", "depletion", "review_synthesis", "Environment-specific dust depletion corrections for individual elements were insufficiently known.", "Co-spatial volatile and refractory-element measurements across phases were needed.", ["REV05-P007","REV05-P043"]),
("REV05-U05", "positive_gradients", "review_synthesis", "The prevalence and lifetime of genuine positive high-redshift metallicity gradients were uncertain.", "Higher-resolution lensing/IFU data and forward beam-smearing models were needed.", ["REV05-P006","REV05-P036","REV05-P049"]),
("REV05-U06", "hot_metal_budget", "review_synthesis", "The amount of metals in hot and ultra-diffuse circumgalactic/intergalactic phases remained poorly constrained.", "Sensitive X-ray and UV ion inventories with multiphase ionization models were needed.", ["REV05-P007","REV05-P009","REV05-P010"]),
]),
]

lines = ["# Review Base 05 canonical advisory packet — Maiolino & Mannucci 2019", "", "status: READY_FOR_HWAO_REVIEW", "advisory_only: true", "canonical_packet_released: true", "wiki_write_performed_by_tori: false", "raw_packet_sha256: `d68f2e08e22261cc70195f5ee6654c2fa2270f463642e3b25600e646392e5fd4`", "independent_identifier_verification: `PASS`", ""]
for heading, entries in claims:
    lines += [heading, ""]
    for cid, role, epistemic, finding, boundary, refs in entries:
        lines += [f"### [{cid}]", f"role: {role}", f"epistemic_type: {epistemic}", f"finding: {finding}", f"boundary: {boundary}", "confidence: high for bounded review synthesis; preserve stated systematics", "source_keys: " + ", ".join(f"[{x}]" for x in refs), ""]

lines += ["## 6. Primary-Citation Harvest", ""]
for row in reg["usable_sources"]:
    if row["source_class"] != "primary": continue
    lines.append(f"[{row['key']}] {row['authors']} ({row['year']}, {row['journal']}) | title={row['title']} | DOI:{row['doi'] or 'none'}; arXiv:{row['arxiv'] or 'none'}; ADS:{row['ads_bibcode']} | role={row['role']} | review_locator={row['review_locator']} | {row['boundary']}")
lines += ["", "### Supporting reviews/syntheses (not counted as primary)", ""]
for row in reg["usable_sources"]:
    if row["source_class"] != "supporting": continue
    lines.append(f"[{row['key']}] {row['authors']} ({row['year']}, {row['journal']}) | title={row['title']} | DOI:{row['doi'] or 'none'}; arXiv:{row['arxiv'] or 'none'}; ADS:{row['ads_bibcode']} | role={row['role']} | review_locator={row['review_locator']} | {row['boundary']}")

lines += ["", "## 7. DO_NOT_USE_UNVERIFIED", ""]
for c in reg["corrected_sources"]:
    lines.append(f"UNCITED_NOT_USABLE | raw tuple for [{c['key']}] | corrected fields: {', '.join(c['fields'])} | raw cross-wired tuple is superseded by curated ADS identity")
for row in reg["quarantined_sources"]:
    lines.append(f"UNCITED_NOT_USABLE | [{row['key']}] {row['authors']} ({row['year']}) | ADS:{row['ads_bibcode']} | {row['quarantine_reason']}")
for text in [
    "all metallicity calibrations share one absolute abundance scale",
    "gas-phase, stellar, neutral-gas, CGM, and ICM metallicities are directly interchangeable",
    "the FMR is universal and redshift-invariant",
    "one radial gradient measures all chemical phases",
    "matching the MZR validates one unique feedback model",
    "post-2019, JWST, or machine-learning browsing results belong to this 2019 review harvest",
]: lines.append(f"UNCITED_NOT_USABLE | {text} | prohibited overclaim or temporal violation")

lines += ["", "## 8. Review and Source Identity Ledger", "", "[REV05-R00] Maiolino & Mannucci (2019, Astronomy and Astrophysics Review) | DOI:10.1007/s00159-018-0112-2; arXiv:1811.09642; ADS:2019A&ARv..27....3M | role=review_synthesis | 2019 review boundary", ""]
for row in reg["usable_sources"]:
    lines.append(f"[{row['key']}] {row['authors']} ({row['year']}, {row['journal']}) | DOI:{row['doi'] or 'none'}; arXiv:{row['arxiv'] or 'none'}; ADS:{row['ads_bibcode']} | role={row['role']} | {row['boundary']}")
lines += ["", "REVIEW_BASE_05_DR_COMPLETE_REFERENCE_ONLY", ""]
OUT.write_text("\n".join(lines))
print(json.dumps({"path": str(OUT), "primary": reg["primary_source_count"], "supporting": reg["supporting_source_count"], "claims": sum(len(x[1]) for x in claims)}, sort_keys=True))
