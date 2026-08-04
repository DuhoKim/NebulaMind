import json
import re
import time
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
RAW = AREA / "area_review_05_maiolino_mannucci_2019_DR_RAW_PACKET.md"
ADS_CACHE = AREA / "scratch/review_base05_ads_identities.json"
OUT = AREA / "area_review_05_maiolino_mannucci_2019_CURATED_SOURCE_REGISTRY.json"
raw = RAW.read_text()
ads_rows = {r["key"]: r for r in json.loads(ADS_CACHE.read_text())["sources"]}

# Recover detailed titles and review locators from the raw harvest blocks.
details = {}
section = raw.split("Primary-Citation Harvest", 1)[1].split("DO_NOT_USE_UNVERIFIED", 1)[0]
for m in re.finditer(r"\[REV05-(P\d{3})\]\t(?P<body>.*?)(?=\n\[REV05-P\d{3}\]\t|\Z)", section, re.S):
    key, body = m.group(1), m.group("body")
    title_m = re.search(r"title=(.+?)\n", body)
    row_m = re.search(r"\n\t(measurement|analytic_theory|hydrodynamic_simulation|semi_analytic_model|calibration)\t([^\t\n]+)\t([^\n]+)", body)
    if not title_m or not row_m:
        raise RuntimeError(f"Could not parse detailed raw harvest row {key}")
    details[key] = {"title_raw": title_m.group(1).strip(), "review_locator_raw": row_m.group(2).strip(), "boundary_raw": row_m.group(3).strip()}

if len(ads_rows) != 51 or len(details) != 51:
    raise RuntimeError(f"Expected 51 rows; ADS={len(ads_rows)}, details={len(details)}")

QUARANTINE = {
    "P035": "Exact Kewley et al. 2010 ApJ 721 L48 bibcode/DOI is absent from the review's structured ar5iv bibliography.",
    "P038": "Exact Pagel et al. 1979 MNRAS 189, 95 bibcode/DOI is absent from the review's structured ar5iv bibliography.",
    "P046": "Kennicutt 1998 is a supporting review, not a primary paper, and its exact bibcode/DOI is absent from the review bibliography.",
    "P047": "Exact Bigiel et al. 2008 AJ 136, 2846 bibcode/DOI is absent from the review's structured ar5iv bibliography.",
}
SUPPORTING = {"P037", "P043"}
ROLE_OVERRIDE = {"P013": "analytic_theory", "P037": "supporting_review", "P043": "supporting_review", "P051": "measurement"}
BOUNDARY_OVERRIDE = {
    "P013": "Analytic equilibrium model for stellar, gas, and metal evolution; not a hydrodynamic simulation.",
    "P037": "Foundational broad chemical-evolution synthesis; supporting review, not primary evidence.",
    "P043": "Solar-abundance synthesis that anchors zero points; supporting review, not primary evidence.",
    "P051": "Observed luminosity-metallicity relation and effective-yield limits in nearby spirals and irregulars.",
}

def norm(v):
    if v is None or str(v).lower() == "none":
        return None
    return str(v).strip().replace("arXiv:", "")

usable, quarantined, corrected = [], [], []
for key in sorted(ads_rows):
    source = ads_rows[key]
    direct = source["ads_direct"]
    if direct["status"] != "PASS":
        raise RuntimeError(f"ADS direct identity failed for {key}")
    doi = norm(direct["doi"])
    arxiv = norm(direct["arxiv"])
    if key == "P037":
        # ADS now links a 2022 retrospective upload of this 1980 paper. Preserve
        # the pre-2019 review-era identifier boundary rather than presenting it
        # as a contemporaneous preprint.
        arxiv = None
    title = (direct["title"] or details[key]["title_raw"]).replace("\\[", "[").replace("\\]", "]")
    corrected_fields = []
    if norm(source["doi_raw"]) != doi:
        corrected_fields.append("doi")
    if norm(source["arxiv_raw"]) != arxiv:
        corrected_fields.append("arxiv")
    if details[key]["title_raw"].casefold() != title.casefold():
        corrected_fields.append("title")
    if key in ROLE_OVERRIDE and source["role_raw"] != ROLE_OVERRIDE[key]:
        corrected_fields.append("role")
    row = {
        "key": f"REV05-{key}",
        "authors": source["authors_raw"],
        "year": source["year"],
        "journal": direct["publication"] or source["journal_raw"],
        "title": title,
        "doi": doi,
        "arxiv": arxiv,
        "ads_bibcode": direct["bibcode"],
        "role": ROLE_OVERRIDE.get(key, source["role_raw"]),
        "review_locator": details[key]["review_locator_raw"],
        "boundary": BOUNDARY_OVERRIDE.get(key, details[key]["boundary_raw"]),
        "review_membership": key not in QUARANTINE,
        "review_membership_evidence": "Exact ADS bibcode or DOI in structured ar5iv bibliography for arXiv:1811.09642." if key not in QUARANTINE else "Exact ADS bibcode and DOI absent from structured ar5iv bibliography for arXiv:1811.09642.",
        "ads_public_identity_status": "PASS",
        "identifier_reconciliation": "PASS" if key not in QUARANTINE else "IDENTITY_PASS_MEMBERSHIP_FAIL",
        "corrected_from_raw": bool(corrected_fields),
        "corrected_fields": corrected_fields,
        "source_class": "supporting" if key in SUPPORTING else "primary",
        "ads_public_url": direct["url"],
    }
    if corrected_fields:
        corrected.append({"key": row["key"], "fields": corrected_fields})
    if key in QUARANTINE:
        row["status"] = "QUARANTINED_UNCITED_NOT_USABLE"
        row["quarantine_reason"] = QUARANTINE[key]
        quarantined.append(row)
    else:
        row["status"] = "PASS"
        usable.append(row)

primary_count = sum(r["source_class"] == "primary" for r in usable)
supporting_count = sum(r["source_class"] == "supporting" for r in usable)
if (len(usable), primary_count, supporting_count, len(quarantined)) != (47, 45, 2, 4):
    raise RuntimeError((len(usable), primary_count, supporting_count, len(quarantined)))

payload = {
    "review": "Maiolino & Mannucci 2019 — De re metallica: the cosmic chemical evolution of galaxies",
    "review_identity": {"doi": "10.1007/s00159-018-0112-2", "arxiv": "1811.09642", "ads_bibcode": "2019A&ARv..27....3M", "status": "PASS_ADS_CROSSREF_ARXIV"},
    "review_membership_source": "Structured ar5iv rendering and bibliography for arXiv:1811.09642, checked by exact ADS bibcode or DOI.",
    "generated_unix": time.time(),
    "raw_packet_sha256": "d68f2e08e22261cc70195f5ee6654c2fa2270f463642e3b25600e646392e5fd4",
    "temporal_cutoff_year": 2019,
    "usable_source_count": len(usable),
    "primary_source_count": primary_count,
    "supporting_source_count": supporting_count,
    "quarantined_source_count": len(quarantined),
    "corrected_source_count": len(corrected),
    "corrected_sources": corrected,
    "usable_sources": usable,
    "quarantined_sources": quarantined,
}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({k: payload[k] for k in ("usable_source_count", "primary_source_count", "supporting_source_count", "quarantined_source_count", "corrected_source_count")}, sort_keys=True))
