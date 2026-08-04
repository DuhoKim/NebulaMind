import hashlib
import json
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
RAW = AREA / "area_review_07_peroux_howk_2020_DR_RAW_PACKET.md"
REG = AREA / "area_review_07_peroux_howk_2020_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_07_peroux_howk_2020_DR_PACKET.md"
registry = json.loads(REG.read_text())
usable = [s for s in registry["sources"] if s["source_status"] == "PASS"]
primary = [s for s in usable if s["role"] != "supporting_review"]
supporting = [s for s in usable if s["role"] == "supporting_review"]
quarantined = [s for s in registry["sources"] if s["source_status"] != "PASS"]
assert (len(primary), len(supporting), len(quarantined)) == (40, 4, 3)

def table(headers, rows):
    def esc(v): return str(v).replace("|", "\\|").replace("\n", " ")
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    out += ["| " + " | ".join(esc(v) for v in row) + " |" for row in rows]
    return "\n".join(out)

established = [
("REV07-E01", "observation", "The comoving neutral-atomic-gas density shows only modest evolution from z about 5 to the present.", "HI traced by 21-cm emission at low z and high-column-density quasar absorbers at high z; helium and cosmology normalization must be explicit.", "High for the review-level trend; absorber thresholds and high-column tail remain systematic limits.", "[REV07-R00] [REV07-P017] [REV07-P045]"),
("REV07-E02", "observation", "The cosmic molecular-gas density rises toward cosmic noon and declines afterward in a pattern similar to the cosmic star-formation-rate density.", "CO-line surveys and derived H2 masses; excitation and CO-to-H2 conversion assumptions apply.", "Moderate; blind survey volumes and conversion factors dominate uncertainty.", "[REV07-R00] [REV07-P009] [REV07-P046]"),
("REV07-E03", "review_synthesis", "The volume-averaged molecular depletion time is approximately constant across the redshift interval then measured.", "Ratio of cosmic H2 mass density to cosmic SFR density; not a claim that every galaxy or ISM phase has one efficiency.", "Moderate; both numerator and denominator are model-dependent censuses.", "[REV07-R00] [REV07-P009] [REV07-P046]"),
("REV07-E04", "review_synthesis", "The low-redshift fall in cosmic star formation is consistent with reduced molecular-gas supply as net cosmological accretion and halo growth slow.", "Population-averaged interpretation linking halo growth, gas supply, and star formation; not a direct measurement of every inflow.", "Moderate; supported by models and selected kinematic probes.", "[REV07-R00] [REV07-P022] [REV07-P023]"),
("REV07-E05", "observation", "At z greater than about 2.5, the inferred metal mass in cold gas can account for nearly all metals expected from the integrated star-formation history.", "Cold T < 10^4 K gas, chiefly absorber-selected; expected metals depend on IMF, yields, ionization, depletion, and SFR history.", "Moderate; apparent closure is conditional on those corrections.", "[REV07-R00] [REV07-P010] [REV07-P011]"),
("REV07-E06", "review_synthesis", "At z below about 1, stars are the largest identified contributor to the observed cosmic metal inventory.", "Stellar-mass density converted to metal mass using population and metallicity assumptions; not total baryon dominance.", "Moderate; systematic errors exceed formal survey errors.", "[REV07-R00] [REV07-P043]"),
("REV07-E07", "review_synthesis", "The combined 2020 census showed little evidence for a severe global missing-metals problem.", "Aggregate stars, cold gas, dust-rich populations, and ionized reservoirs; does not mean every phase or spatial distribution is measured.", "Moderate; yield and hot-phase uncertainties permit residual imbalance.", "[REV07-R00] [REV07-P024] [REV07-P025] [REV07-P026]"),
("REV07-E08", "observation", "Dust-to-gas ratio in neutral absorbers decreases with decreasing metallicity.", "Absorber-selected neutral gas; depletion, extinction selection, and abundance scale matter.", "Moderate to high within measured samples.", "[REV07-R00] [REV07-P002] [REV07-P015]"),
("REV07-E09", "observation", "Dust-to-metals ratio is not universal and also decreases toward low metallicity.", "Neutral-gas depletion and extinction in selected sightlines; do not extrapolate unchanged to hot CGM/IGM phases.", "Moderate; grain composition and depletion modeling contribute uncertainty.", "[REV07-R00] [REV07-P002] [REV07-P015]"),
("REV07-E10", "review_synthesis", "More than 90 percent of cosmic baryons remain gaseous rather than locked in stars at the present epoch.", "Global baryon normalization versus stellar and condensed-matter censuses; gas spans ISM, CGM, intracluster, and IGM phases.", "High for gas-versus-stars; lower for detailed phase partition.", "[REV07-R00] [REV07-P042] [REV07-P043]"),
("REV07-E11", "observation", "Big-Bang-nucleosynthesis and CMB-anisotropy estimates give concordant total baryon-density normalizations.", "Primordial deuterium plus BBN physics compared with CMB cosmology; this fixes total Omega_b, not where baryons reside later.", "High under the adopted cosmological model.", "[REV07-R00] [REV07-P041] [REV07-P042]"),
("REV07-E12", "observation", "Independent absorption- and emission-based estimates of cosmic dust density are broadly consistent over their common redshift range.", "Dust mass functions and SED models versus absorber reddening/depletion; opacity and temperature assumptions differ.", "Moderate; agreement is at census scale, not object-by-object.", "[REV07-R00] [REV07-P012] [REV07-P043]"),
]
debates = [
("REV07-D01", "Metal-census closure", "Near closure after adding known reservoirs versus residual metals in poorly measured warm-hot phases.", "Yield/IMF normalization and ionized-phase corrections remain uncertain.", "[REV07-R00] [REV07-P024] [REV07-P025] [REV07-P026]"),
("REV07-D02", "HI evolution and absorber selection", "Weak Omega_HI evolution versus possible bias from absorber thresholds, high-column rarity, and dust-obscured sightlines.", "Compare optical absorption, radio selection, and low-z 21-cm measurements under one cosmology.", "[REV07-R00] [REV07-P017] [REV07-P045]"),
("REV07-D03", "Molecular-gas census", "Observed CO luminosity functions versus uncertain excitation corrections and metallicity-dependent CO-to-H2 conversion.", "Blind survey volume, line identification, and conversion-factor priors dominate.", "[REV07-R00] [REV07-P020] [REV07-P046]"),
("REV07-D04", "Dust obscuration bias", "Optical quasar samples may miss dusty high-column absorbers, but the magnitude of the missing population was unresolved.", "Background-source selection and sightline geometry; not all dusty galaxies are DLAs.", "[REV07-R00] [REV07-P002] [REV07-P021]"),
("REV07-D05", "Metal yield and IMF systematics", "Different IMFs, solar abundance scales, and nucleosynthetic yields shift the expected metal denominator.", "Calibration uncertainty, not a direct discrepancy in one observed reservoir.", "[REV07-R00] [REV07-P006] [REV07-P031]"),
("REV07-D06", "Ionization corrections in CGM/LLS gas", "Observed ions do not uniquely determine total hydrogen or metal mass under an uncertain radiation field.", "Photoionization model, density, multiphase structure, and UV background.", "[REV07-R00] [REV07-P034] [REV07-P038] [REV07-P047]"),
("REV07-D07", "Dust-to-metals evolution", "Stellar dust production versus ISM grain growth and destruction can reproduce different low-metallicity behavior.", "Model timescales and phase exchange; absorber depletion does not directly measure every dust reservoir.", "[REV07-R00] [REV07-P004] [REV07-P013]"),
("REV07-D08", "Observed versus simulated phase partition", "Simulations can match some totals while assigning baryons or metals to different temperatures, ionization states, or halo radii.", "Resolution, feedback, ionization post-processing, and tracer selection.", "[REV07-R00] [REV07-P018] [REV07-P035] [REV07-P038]"),
]
measurements = [
("REV07-N01", "Omega_b approximately 0.0455", "dimensionless density parameter", "Review's adopted cosmology; total cosmic baryons from CMB and BBN.", "Calibrated cosmological normalization, not a collapsed-baryon fraction.", "[REV07-R00] [REV07-P041] [REV07-P042]"),
("REV07-N02", ">90 percent", "fraction of total baryon mass", "Present-day baryons in gaseous rather than stellar form.", "Review synthesis; detailed gas-phase partition remains less certain.", "[REV07-R00] [REV07-P042] [REV07-P043]"),
("REV07-N03", "Omega_HI changes only modestly from z about 5 to 0", "dimensionless density parameter", "Neutral gas from absorber and 21-cm censuses, homogenized to one cosmology and including helium where stated.", "Observed trend; high-column and selection corrections apply.", "[REV07-R00] [REV07-P017] [REV07-P045]"),
("REV07-N04", "t_dep,cosmic = rho_H2 / rho_SFR; approximately constant", "time", "Volume-averaged molecular-gas depletion time over the sampled redshift range.", "Derived from two cosmic densities; not a universal galaxy-by-galaxy constant.", "[REV07-R00] [REV07-P009] [REV07-P046]"),
("REV07-N05", "approximately 100 percent at z > 2.5", "fraction of expected produced metal mass", "Metals inferred in cold T < 10^4 K gas compared with integrated stellar production.", "Yield-, IMF-, ionization-, and depletion-dependent review synthesis.", "[REV07-R00] [REV07-P010] [REV07-P011]"),
("REV07-N06", "<15 percent", "fraction of cosmic metal budget", "Estimated maximum contribution of submillimeter galaxies in the historical missing-metals accounting.", "Population abundance and metal-mass assumptions apply.", "[REV07-R00] [REV07-P025]"),
("REV07-N07", "N(HI) = integral n_HI ds", "atoms cm^-2", "Neutral-hydrogen column density along a sightline.", "Definition; conversion to cosmic density requires path-length and selection accounting.", "[REV07-R00]"),
("REV07-N08", "log10 N(HI) >= 20.3 for the classical DLA census quoted", "N(HI) in atoms cm^-2", "High-column absorber threshold; lower-column systems can contribute non-negligible neutral mass, especially at high z.", "Operational tracer boundary, not a physical phase discontinuity.", "[REV07-R00] [REV07-P045]"),
]
unknowns = [
("REV07-U01", "Direct separation of CGM inflow, outflow, and recycling rates.", "Needed to test whether declining net supply drives late-time star-formation decline.", "Spatially resolved multiphase kinematics and matched galaxy-halo sightlines.", "[REV07-R00] [REV07-P022] [REV07-P023]"),
("REV07-U02", "Metal and baryon mass in million-degree warm-hot gas.", "This weakly detected phase controls detailed census closure and feedback energetics.", "Higher-sensitivity X-ray/UV absorption and emission with ionization modeling.", "[REV07-R00] [REV07-P007] [REV07-P033]"),
("REV07-U03", "Molecular-gas density at z > 5.", "Constrains the fuel available near the onset of normal galaxy assembly.", "Blind deep line/continuum surveys with explicit excitation and conversion uncertainties.", "[REV07-R00] [REV07-P028] [REV07-P046]"),
("REV07-U04", "Frequency of heavily dust-obscured, metal-rich DLAs missing from optical samples.", "Could bias neutral-gas and metal-density estimates.", "Radio/mm-selected background sources and controlled optical-versus-radio samples.", "[REV07-R00] [REV07-P002] [REV07-P021]"),
("REV07-U05", "Dust growth, destruction, and survival rates at low metallicity and early times.", "Controls dust-to-metals evolution and molecular-gas formation.", "Resolved grain diagnostics plus chemical-evolution models tested across metallicity.", "[REV07-R00] [REV07-P004] [REV07-P013]"),
("REV07-U06", "Universality of the IMF and nucleosynthetic yields in extreme environments.", "Changes the expected metal production used in every closure calculation.", "Independent abundance patterns, stellar constraints, and yield-model comparisons.", "[REV07-R00] [REV07-P006] [REV07-P031]"),
]

lines = [
"# Review Base 07 — Péroux & Howk (2020): The Cosmic Baryon and Metal Cycles",
"", "Status: READY_FOR_HWAO_REVIEW — advisory source base only; no live wiki/database/trust/deployment/publication/git mutation.",
"", f"Raw custody SHA-256: `{hashlib.sha256(RAW.read_bytes()).hexdigest()}`", "",
"## 1. Review Identity and Scope Map", "",
table(["Field", "Value"], [
("Review key", "[REV07-R00]"), ("Authors", "Céline Péroux and J. Christopher Howk"), ("Year / journal", "2020, Annual Review of Astronomy and Astrophysics 58, 363-406"),
("DOI", "10.1146/annurev-astro-021820-120014"), ("arXiv", "2011.01935"), ("ADS", "2020ARA&A..58..363P"),
("Authorized scope", "Cosmic baryon, atomic/molecular gas, metal, dust, CGM/IGM, and collapsed-matter censuses through the review's 2020 boundary."),
("Explicit exclusions", "Post-2020 work, AGN-only physics, uncited candidates, phase-collapsing claims, and claims that census-scale agreement uniquely validates a model."),
]), "",
"## 2. Established Findings", "", table(["ID", "Epistemic type", "Bounded finding", "Boundary", "Confidence note", "Sources"], established), "",
"## 3. Open Debates and Tensions", "", table(["ID", "Topic", "Competing positions", "Why unresolved / boundary", "Sources"], debates), "",
"## 4. Key Measurements, Model Benchmarks, and Calibrations", "", table(["ID", "Value / equation", "Units", "Context", "Status / caveat", "Sources"], measurements), "",
"## 5. What Remained Unknown in 2020", "", table(["ID", "Gap", "Why it matters", "Needed test", "Sources"], unknowns), "",
"## 6. Primary-Citation Harvest", "",
]
for s in primary:
    lines.append(f"[{s['key']}] {s['authors']} ({s['year']}, {s['journal']}) | title={s['title']} | DOI:{s['doi'] or 'none'}; arXiv:{s['arxiv'] or 'none'}; ADS:{s['ads_bibcode']} | role={s['role']} | review_locator={s['review_locator']} | {s['boundary']} | source_status=PASS_COMPOSITE_ID_AND_REVIEW_MEMBERSHIP")
lines += ["", "### Supporting reviews", ""]
for s in supporting:
    lines.append(f"[{s['key']}] {s['authors']} ({s['year']}, {s['journal']}) | title={s['title']} | DOI:{s['doi'] or 'none'}; arXiv:{s['arxiv'] or 'none'}; ADS:{s['ads_bibcode']} | role=supporting_review | review_locator={s['review_locator']} | {s['boundary']} | source_status=PASS_COMPOSITE_ID_AND_REVIEW_MEMBERSHIP")
lines += ["", "## 7. DO_NOT_USE_UNVERIFIED", ""]
for s in quarantined:
    lines.append(f"UNCITED_NOT_USABLE | [{s['key']}] {s['authors']} ({s['year']}) — {s['title']} | DOI:{s['doi'] or 'none'}; arXiv:{s['arxiv'] or 'none'}; ADS:{s['ads_bibcode'] or 'none'} | {s['quarantine_reason']}")
lines += [
"UNCITED_NOT_USABLE | Macquart et al. 2020 FRB baryon-census result and Omega_b h70 = 0.051 (+0.021/-0.025) | supplied in raw prose as [REV07-P039] | absent from the authors' arXiv review bibliography; do not use as review-derived evidence.",
"UNCITED_NOT_USABLE | post-2020/JWST/ML browsing results | none | outside the review's temporal and citation boundary.",
"UNCITED_NOT_USABLE | claims that all baryons are directly detected, every reservoir is known, or all metals occupy one phase | none | overbroad phase-collapsing interpretation.",
"UNCITED_NOT_USABLE | claims that one absorber class measures all gas or that matching one global density validates one unique baryon-cycle model | none | tracer/model overreach.",
"", "## 8. Review and Source Identity Ledger", "",
"[REV07-R00] Peroux C & Howk JC (2020, Annual Review of Astronomy and Astrophysics) | title=The Cosmic Baryon and Metal Cycles | DOI:10.1146/annurev-astro-021820-120014; arXiv:2011.01935; ADS:2020ARA&A..58..363P | role=review_synthesis | source_status=PASS_ADS_CROSSREF_ARXIV", "",
]
for s in usable:
    lines.append(f"[{s['key']}] {s['authors']} ({s['year']}, {s['journal']}) | title={s['title']} | DOI:{s['doi'] or 'none'}; arXiv:{s['arxiv'] or 'none'}; ADS:{s['ads_bibcode']} | role={s['role']} | boundary={s['boundary']} | source_status=PASS_COMPOSITE_ID_AND_REVIEW_MEMBERSHIP")
lines += ["", "REVIEW_BASE_07_DR_COMPLETE_REFERENCE_ONLY", ""]
OUT.write_text("\n".join(lines))
print(json.dumps({"packet": str(OUT), "primary": len(primary), "supporting": len(supporting), "quarantined": len(quarantined), "sha256": hashlib.sha256(OUT.read_bytes()).hexdigest()}, sort_keys=True))
