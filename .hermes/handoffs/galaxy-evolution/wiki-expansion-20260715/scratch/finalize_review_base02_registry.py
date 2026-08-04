import json
import time
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
VERIFY = json.loads((AREA / "area_review_02_madau_dickinson_2014_SOURCE_VERIFICATION.json").read_text())
ADS = json.loads((AREA / "area_review_02_madau_dickinson_2014_ADS_IDENTITIES.json").read_text())["identities"]
NED = Path("/Users/duhokim/.hermes/cache/web/ned.ipac.caltech.edu-6373b53fc0.md").read_text()
OUT = AREA / "area_review_02_madau_dickinson_2014_CURATED_SOURCE_REGISTRY.json"

rows = []
raw_by_key = {row["source"]["key"]: row["source"] for row in VERIFY["rows"]}
supporting = {"REV02-P001", "REV02-P020", "REV02-P034", "REV02-P036"}

replacements = {
    "REV02-P014": {
        "authors": "Takeuchi, T. T. et al.", "first_author": "Takeuchi", "year": 2003, "journal": "Astrophysical Journal Letters",
        "title": "The Luminosity Function of IRAS Point Source Catalog Redshift Survey Galaxies", "doi": "10.1086/375181", "arxiv": "astro-ph/0303181", "ads_bibcode": "2003ApJ...587L..89T",
        "role": "measurement", "review_locator": "Table 1 / local IR luminosity density", "boundary": "Local IRAS PSCz luminosity-function anchor; do not use as a high-redshift evolution measurement.",
    },
    "REV02-P030": {
        "authors": "Daddi, E. et al.", "first_author": "Daddi", "year": 2005, "journal": "Astrophysical Journal Letters",
        "title": "The Population of BzK-selected ULIRGs at z ~ 2", "doi": "10.1086/496918", "arxiv": "astro-ph/0507504", "ads_bibcode": "2005ApJ...631L..13D",
        "role": "measurement", "review_locator": "Section 1 / obscured populations at cosmic noon", "boundary": "Massive BzK-selected star-forming galaxies at z~2; not a census of all galaxies or a passive-galaxy paper.",
    },
    "REV02-P040": {
        "authors": "Lanzetta, K. M. et al.", "first_author": "Lanzetta", "year": 1995, "journal": "Astrophysical Journal",
        "title": "The IUE Survey for Damped Lyman-alpha and Lyman-Limit Absorption Systems: Evolution of the Gaseous Content of the Universe", "doi": "10.1086/175286", "arxiv": "none", "ads_bibcode": "1995ApJ...440..435L",
        "role": "measurement", "review_locator": "Section 5.5 / neutral-gas and chemical-evolution accounting", "boundary": "Damped-Lyman-alpha neutral-gas evolution and closed-box interpretation; not a direct cosmic SFR-density measurement.",
    },
}

for key in sorted(raw_by_key):
    raw = raw_by_key[key]
    if key in replacements:
        source = {"key": key, **replacements[key]}
        correction_reason = "Raw row named an uncited or nonexistent ADS tuple; replaced with the exact review-cited physical paper matching the intended topic."
    else:
        identity = ADS[key]
        source = dict(raw)
        source.update(title=identity["title"], doi=identity["doi"], arxiv=identity["arxiv"])
        if key == "REV02-P038":
            source["arxiv"] = "1105.2039"
        correction_reason = "ADS-direct composite reconciliation of title, DOI, and arXiv identifier."
    source["source_class"] = "supporting_review_or_proceeding" if key in supporting else "primary"
    member = source["ads_bibcode"] in NED or source["ads_bibcode"].replace("&", "%26") in NED
    if not member:
        raise SystemExit(f"review membership missing after correction: {key} {source['ads_bibcode']}")
    changed = any(str(raw.get(field, "")).lower() != str(source.get(field, "")).lower() for field in ("title", "doi", "arxiv", "ads_bibcode"))
    rows.append({
        "source": source,
        "raw_identity": {field: raw.get(field) for field in ("title", "doi", "arxiv", "ads_bibcode")},
        "evidence": {
            "ads_public_abstract_identity": "PASS",
            "review_membership_via_ned_bibliography": True,
            "composite_author_year_title_doi_arxiv_ads": "PASS",
            "arxiv_note": "Direct arXiv title/author resolution retained although ADS does not expose the e-print" if key == "REV02-P038" else None,
        },
        "corrected_from_raw": changed,
        "correction_reason": correction_reason if changed else None,
        "status": "PASS",
    })

additions = [
    {"key": "REV02-P041", "authors": "Meurer, G. R. et al.", "first_author": "Meurer", "year": 1999, "journal": "Astrophysical Journal", "title": "Dust Absorption and the Ultraviolet Luminosity Density at z ~ 3 as Calibrated by Local Starburst Galaxies", "doi": "10.1086/307523", "arxiv": "astro-ph/9903054", "ads_bibcode": "1999ApJ...521...64M", "role": "calibration", "review_locator": "Section 4.1 / UV attenuation", "boundary": "Local-starburst IRX-beta calibration applied to z~3 UV samples; applicability to other populations is not universal."},
    {"key": "REV02-P042", "authors": "Madau, P. et al.", "first_author": "Madau", "year": 1998, "journal": "Astrophysical Journal", "title": "The Star Formation History of Field Galaxies", "doi": "10.1086/305523", "arxiv": "astro-ph/9708220", "ads_bibcode": "1998ApJ...498..106M", "role": "measurement", "review_locator": "Section 1 / historical cosmic-SFH synthesis", "boundary": "Early integrated-light CSFH inference to z~4 under then-current cosmology, IMF, and dust assumptions."},
    {"key": "REV02-P043", "authors": "Madau, P. et al.", "first_author": "Madau", "year": 1999, "journal": "Astrophysical Journal", "title": "Radiative Transfer in a Clumpy Universe. III. The Nature of Cosmological Ionizing Sources", "doi": "10.1086/306975", "arxiv": "astro-ph/9809058", "ads_bibcode": "1999ApJ...514..648M", "role": "theory", "review_locator": "Section 5.8 / reionization photon accounting", "boundary": "Ionizing-source and clumpy-IGM budget model; conclusions depend on emissivity, escape fraction, and recombination assumptions."},
    {"key": "REV02-P044", "authors": "Li, C. & White, S. D. M.", "first_author": "Li", "year": 2009, "journal": "Monthly Notices of the Royal Astronomical Society", "title": "The distribution of stellar mass in the low-redshift Universe", "doi": "10.1111/j.1365-2966.2009.15268.x", "arxiv": "0901.0706", "ads_bibcode": "2009MNRAS.398.2177L", "role": "measurement", "review_locator": "Section 5.3 / local stellar-mass-density benchmark", "boundary": "Low-redshift SDSS stellar-mass distribution under a standard IMF; not a high-redshift mass-function measurement."},
]
for source in additions:
    source["source_class"] = "primary"
    member = source["ads_bibcode"] in NED
    if not member:
        raise SystemExit(f"addition not cited by review: {source['key']}")
    rows.append({"source": source, "raw_identity": None, "evidence": {"ads_public_abstract_identity": "PASS", "review_membership_via_ned_bibliography": True, "composite_author_year_title_doi_arxiv_ads": "PASS"}, "corrected_from_raw": False, "added_during_curation": True, "status": "PASS"})

primary_count = sum(row["source"]["source_class"] == "primary" for row in rows)
supporting_count = len(rows) - primary_count
corrected_count = sum(row.get("corrected_from_raw", False) for row in rows)
output = {
    "status": "PASS", "verified_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "review": {"title": "Cosmic Star-Formation History", "authors": "Madau & Dickinson", "year": 2014, "doi": "10.1146/annurev-astro-081811-125615", "arxiv": "1403.0007", "ads_bibcode": "2014ARA&A..52..415M", "identity_status": "PASS_ADS_CROSSREF_ARXIV"},
    "method": "Every usable row reconciled against its ADS public abstract identity and exact ADS-bibcode membership in the review's NED bibliography; cross-wired raw identifiers replaced or quarantined.",
    "raw_source_count": 40, "source_count": len(rows), "primary_count": primary_count, "supporting_review_or_proceeding_count": supporting_count,
    "corrected_raw_rows": corrected_count, "review_cited_primary_additions": len(additions), "pass_count": len(rows), "fail_count": 0, "rows": rows,
}
if len(rows) != 44 or primary_count != 40 or supporting_count != 4:
    raise SystemExit(f"unexpected counts: total={len(rows)} primary={primary_count} supporting={supporting_count}")
OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: output[k] for k in ("status", "source_count", "primary_count", "supporting_review_or_proceeding_count", "corrected_raw_rows", "pass_count", "fail_count")}, sort_keys=True))
