import json
import re
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
RAW = AREA / "area_review_07_peroux_howk_2020_DR_RAW_PACKET.md"
IDENTITIES = AREA / "scratch/review_base07_ads_identities.json"
OUT = AREA / "area_review_07_peroux_howk_2020_CURATED_SOURCE_REGISTRY.json"

SUPPORTING = {"P006", "P020", "P028", "P040"}
QUARANTINE = {
    "P003": "UNCITED_NOT_USABLE: composite identity resolves in ADS, but Anderson & Sunyaev 2016 is absent from the review bibliography",
    "P005": "UNCITED_NOT_USABLE: composite identity resolves after correction, but Asano et al. 2013 is absent from the review bibliography",
    "P039": "UNCITED_NOT_USABLE: Macquart et al. 2020 is absent from the authors' 2020 draft bibliography",
}
ROLE_MAP = {"observation": "measurement", "analytic_theory": "analytic_theory", "hydrodynamic_simulation": "hydrodynamic_simulation", "semi_analytic_model": "semi_analytic_model", "calibration": "calibration", "review_synthesis": "supporting_review"}

ADDITIONS = [
    {
        "key": "P042", "authors": "Planck Collaboration, Ade PAR, Aghanim N, et al.", "year": 2016,
        "journal": "Astronomy & Astrophysics", "title": "Planck 2015 results. XIII. Cosmological parameters",
        "doi": "10.1051/0004-6361/201525830", "arxiv": "1502.01589", "ads_bibcode": "2016A&A...594A..13P",
        "role": "measurement", "review_locator": "Context and cosmic baryon density",
        "boundary": "CMB-anisotropy cosmological parameter inference; supplies the total baryon-density normalization rather than a collapsed-phase census.",
    },
    {
        "key": "P043", "authors": "Driver SP, Andrews SK, da Cunha E, et al.", "year": 2018,
        "journal": "Monthly Notices of the Royal Astronomical Society", "title": "GAMA/G10-COSMOS/3D-HST: the 0 < z < 5 cosmic star formation history, stellar-mass, and dust-mass densities",
        "doi": "10.1093/mnras/stx2728", "arxiv": "1710.06628", "ads_bibcode": "2018MNRAS.475.2891D",
        "role": "measurement", "review_locator": "Condensed baryon, stellar-metal, and dust censuses",
        "boundary": "SED-model-dependent stellar, star-formation, and dust mass densities over 0 < z < 5 under a consistent IMF and energy-balance model.",
    },
    {
        "key": "P044", "authors": "Noterdaeme P, Laursen P, Petitjean P, et al.", "year": 2012,
        "journal": "Astronomy & Astrophysics", "title": "Discovery of a compact gas-rich damped Lyman-alpha galaxy at z = 2.2: evidence of a starburst-driven outflow",
        "doi": "10.1051/0004-6361/201118691", "arxiv": "1202.0280", "ads_bibcode": "2012A&A...540A..63N",
        "role": "measurement", "review_locator": "Neutral gas and absorber-selected galaxies",
        "boundary": "A single extremely high-column-density DLA counterpart at z = 2.207; not a population-wide neutral-gas census.",
    },
    {
        "key": "P045", "authors": "Peroux C, McMahon RG, Storrie-Lombardi LJ, Irwin MJ", "year": 2003,
        "journal": "Monthly Notices of the Royal Astronomical Society", "title": "The evolution of Omega_HI and the epoch of formation of damped Lyman alpha absorbers",
        "doi": "10.1111/j.1365-2966.2003.07129.x", "arxiv": "astro-ph/0107045", "ads_bibcode": "2003MNRAS.346.1103P",
        "role": "measurement", "review_locator": "Neutral-gas mass density and column-density distribution",
        "boundary": "DLA and Lyman-limit absorber column-density statistics; conclusions depend on absorber thresholds and extrapolation of f(N,z).",
    },
    {
        "key": "P046", "authors": "Decarli R, Walter F, Gonzalez-Lopez J, et al.", "year": 2019,
        "journal": "The Astrophysical Journal", "title": "The ALMA Spectroscopic Survey in the HUDF: CO Luminosity Functions and the Molecular Gas Content of Galaxies through Cosmic History",
        "doi": "10.3847/1538-4357/ab30fe", "arxiv": "1903.09164", "ads_bibcode": "2019ApJ...882..138D",
        "role": "measurement", "review_locator": "Cosmic molecular-gas density",
        "boundary": "Blind CO line survey in the HUDF; molecular masses depend on excitation corrections and the adopted CO-to-H2 conversion factor.",
    },
    {
        "key": "P047", "authors": "Wotta CB, Lehner N, Howk JC, et al.", "year": 2019,
        "journal": "The Astrophysical Journal", "title": "The COS CGM Compendium. II. Metallicities of the Partial and Lyman Limit Systems at z <= 1",
        "doi": "10.3847/1538-4357/aafb74", "arxiv": "1811.10654", "ads_bibcode": "2019ApJ...872...81W",
        "role": "measurement", "review_locator": "Ionized CGM metallicity distribution",
        "boundary": "HI-selected pLLSs and LLSs at z <= 1; metallicities depend on photoionization modeling and the ionizing radiation field.",
    },
]

def norm(value):
    if value is None or str(value).strip().lower() == "none":
        return None
    return str(value).strip()

def eq(a, b):
    aa, bb = norm(a), norm(b)
    if aa is None or bb is None:
        return aa is None and bb is None
    return re.sub(r"\s+", " ", aa).casefold() == re.sub(r"\s+", " ", bb).casefold()

data = json.loads(IDENTITIES.read_text())["sources"]
sources = []
for row in data:
    key = row["key"]
    ads = row["ads_direct"]
    title = norm(ads.get("title")) or norm(row["title_raw"])
    doi = norm(ads.get("doi"))
    arxiv = norm(ads.get("arxiv"))
    bibcode = norm(ads.get("bibcode")) or norm(row["ads_raw"])
    role = "supporting_review" if key in SUPPORTING else ROLE_MAP[row["role_raw"]]
    corrections = []
    for field, raw, canonical in (
        ("title", row["title_raw"], title), ("doi", row["doi_raw"], doi),
        ("arxiv", row["arxiv_raw"], arxiv), ("ads_bibcode", row["ads_raw"], bibcode),
    ):
        if not eq(raw, canonical):
            corrections.append({"field": field, "raw": norm(raw), "canonical": canonical})
    if row["role_raw"] != role:
        corrections.append({"field": "role", "raw": row["role_raw"], "canonical": role})
    status = "QUARANTINED" if key in QUARANTINE else "PASS"
    sources.append({
        "key": f"REV07-{key}", "authors": row["authors_raw"], "year": row["year"],
        "journal": ads.get("publication") or row["journal_raw"], "title": title,
        "doi": doi, "arxiv": arxiv, "ads_bibcode": bibcode, "role": role,
        "review_locator": row["review_locator_raw"], "boundary": row["boundary_raw"],
        "source_status": status,
        "identity_verification": {
            "status": "PASS_ADS_DIRECT" if status == "PASS" else "QUARANTINED_UNCITED",
            "ads_url": ads["url"], "ads_direct_status": ads["status"],
            "review_membership": "PASS_AR5IV_AUTHOR_YEAR_JOURNAL_PAGE" if status == "PASS" else "FAIL_NOT_IN_AR5IV_REVIEW_BIBLIOGRAPHY",
        },
        "raw_tuple_corrected": bool(corrections), "corrections": corrections,
        "quarantine_reason": QUARANTINE.get(key),
    })

for row in ADDITIONS:
    sources.append({
        "key": f"REV07-{row['key']}", "authors": row["authors"], "year": row["year"],
        "journal": row["journal"], "title": row["title"], "doi": row["doi"],
        "arxiv": row["arxiv"], "ads_bibcode": row["ads_bibcode"], "role": row["role"],
        "review_locator": row["review_locator"], "boundary": row["boundary"], "source_status": "PASS",
        "identity_verification": {
            "status": "PASS_ADS_DIRECT",
            "ads_url": f"https://ui.adsabs.harvard.edu/abs/{row['ads_bibcode']}/abstract",
            "ads_direct_status": "PASS",
            "review_membership": "PASS_AR5IV_EXACT_REFERENCE_BLOCK",
        },
        "raw_tuple_corrected": False, "corrections": [], "quarantine_reason": None,
        "added_during_curated_reconciliation": True,
    })

usable = [s for s in sources if s["source_status"] == "PASS"]
primaries = [s for s in usable if s["role"] != "supporting_review"]
supporting = [s for s in usable if s["role"] == "supporting_review"]
quarantined = [s for s in sources if s["source_status"] != "PASS"]
assert len(sources) == 47
assert len(primaries) == 40
assert len(supporting) == 4
assert len(quarantined) == 3
assert len({s["key"] for s in sources}) == 47
assert all(s["year"] <= 2020 for s in usable)
assert all(s["ads_bibcode"] for s in usable)
assert all(s["identity_verification"]["review_membership"].startswith("PASS") for s in usable)

registry = {
    "status": "PASS_COMPOSITE_IDS_AND_REVIEW_MEMBERSHIP",
    "mission_id": "GALAXY_REVIEW_BASE_DR_20260715", "queue_item": 7,
    "review": {
        "key": "REV07-R00", "authors": "Peroux C & Howk JC", "year": 2020,
        "title": "The Cosmic Baryon and Metal Cycles", "journal": "Annual Review of Astronomy and Astrophysics",
        "doi": "10.1146/annurev-astro-021820-120014", "arxiv": "2011.01935",
        "ads_bibcode": "2020ARA&A..58..363P", "identity_status": "PASS_ADS_CROSSREF_ARXIV",
    },
    "review_bibliography_basis": {
        "source": "https://ar5iv.labs.arxiv.org/html/2011.01935",
        "status": "PASS_COMPLETE_REVIEW_TEXT_AND_REFERENCE_LIST_WEB_ONLY",
        "local_raw_source_extraction_used": False,
    },
    "counts": {
        "raw_harvest_rows": 41, "added_verified_primary_rows": 6, "total_registry_rows": len(sources),
        "usable_primary_sources": len(primaries), "usable_supporting_reviews": len(supporting),
        "quarantined_sources": len(quarantined),
        "corrected_raw_rows": sum(1 for s in sources if s["raw_tuple_corrected"]),
    },
    "sources": sources,
}
OUT.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(registry["counts"], sort_keys=True))
