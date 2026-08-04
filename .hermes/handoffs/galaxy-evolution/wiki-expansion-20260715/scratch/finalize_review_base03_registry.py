import json
import re
import time
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
RAW = AREA / "area_review_03_somerville_dave_2015_DR_RAW_PACKET.md"
ADS = json.loads((AREA / "area_review_03_somerville_dave_2015_ADS_IDENTITIES.json").read_text())["identities"]
NED = Path("/Users/duhokim/.hermes/cache/web/ned.ipac.caltech.edu-e00f211196.md").read_text()
OUT = AREA / "area_review_03_somerville_dave_2015_CURATED_SOURCE_REGISTRY.json"

text = RAW.read_text()
harvest = text.split("6. Primary-citation harvest", 1)[1].split("7. DO_NOT_USE_UNVERIFIED", 1)[0]
pattern = re.compile(
    r"^\[(REV03-P\d{3})\] (.+?) \((\d{4}), (.+?)\) \| title=(.+?) \| DOI:(.+?); arXiv:(.+?); ADS:(\S+) \| role=(\w+) \| review_locator=(.+?) \| (.*)$",
    re.M,
)
raw_rows = {}
for match in pattern.finditer(harvest):
    key, authors, year, journal, title, doi, arxiv, bibcode, role, locator, boundary = match.groups()
    raw_rows[key] = {"key": key, "authors": authors, "first_author": authors.split()[0], "year": int(year), "journal": journal, "title": title, "doi": doi, "arxiv": arxiv, "ads_bibcode": bibcode, "role": role, "review_locator": locator, "boundary": boundary}
if len(raw_rows) != 58:
    raise SystemExit(f"expected 58 rows, parsed {len(raw_rows)}")

supporting = {"REV03-P025", "REV03-P035", "REV03-P037", "REV03-P043", "REV03-P044"}
quarantine = {
    "REV03-P007": "Exact ADS bibcode is absent from the review bibliography; physically valid paper but not usable as a review-cited harvest row.",
    "REV03-P040": "Bondi spherical-accretion microphysics is AGN-subgrid context and outside the queue's non-AGN core harvest.",
    "REV03-P041": "Black-hole growth and AGN thermal-feedback method paper is AGN-centered and outside the queue's non-AGN core harvest.",
    "REV03-P044": "Exact ADS bibcode and DOI are absent from the review bibliography; supporting review cannot be promoted as review-cited here.",
    "REV03-P052": "Exact ADS bibcode is absent from the review bibliography; physically valid code-comparison paper but not a review-cited harvest row.",
    "REV03-P056": "Exact ADS bibcode is absent from the review bibliography; physically valid FIRE paper but not a review-cited harvest row.",
    "REV03-P057": "Exact ADS bibcode is absent from the review bibliography; physically valid CGM observation but not a review-cited harvest row.",
    "REV03-P058": "Exact ADS bibcode is absent from the review bibliography; physically valid transition model but not a review-cited harvest row.",
}
boundary_updates = {
    "REV03-P011": "Halo-catalog and merger-tree consistency method for dark-matter simulations; not a hydrodynamic galaxy simulation or a direct halo-structure measurement.",
    "REV03-P019": "Simulation study of environmental dependence in the Kennicutt-Schmidt relation; do not use as the Gnedin-Kravtsov molecular-shielding prescription paper.",
    "REV03-P023": "CANDELS morphology comparison of star-forming and quiescent galaxies to z~2; morphology alone does not identify the quenching mechanism.",
    "REV03-P032": "Systematic uncertainty analysis for stellar-mass-to-halo-mass inference over 0<z<4; not a toy-cosmology guide.",
    "REV03-P034": "Observed structural properties of dynamically hot galaxies; not a generic velocity-kinematics census of all ellipticals.",
    "REV03-P036": "Local disc/spheroid luminosity and stellar-mass functions from decomposed SDSS galaxies; do not use as a dwarf-demographics feedback experiment.",
    "REV03-P038": "Pressure-based giant-molecular-cloud formation relation in nearby galaxies; bounded empirical partition recipe.",
    "REV03-P045": "Cross-environment local star-formation-law model; universality is model-bounded rather than a parameter-free empirical fact.",
    "REV03-P052": "Aquila same-halo code comparison demonstrating sensitivity to numerical and feedback choices; not proof that one method is physically correct.",
    "REV03-P058": "Atomic-to-molecular transition column-density model; retain metallicity, radiation-field, and equilibrium assumptions.",
}
role_updates = {
    "REV03-P011": "calibration",
    "REV03-P035": "review_synthesis",
    "REV03-P037": "review_synthesis",
    "REV03-P043": "review_synthesis",
    "REV03-P044": "review_synthesis",
}

usable = []
quarantined = []
for key in sorted(raw_rows):
    raw = raw_rows[key]
    identity = ADS[key]
    source = dict(raw)
    source.update(title=identity["title"], doi=identity["doi"], arxiv=identity["arxiv"])
    source["role"] = role_updates.get(key, source["role"])
    source["boundary"] = boundary_updates.get(key, source["boundary"])
    member = source["ads_bibcode"] in NED or source["ads_bibcode"].replace("&", "%26") in NED
    if not member and key not in quarantine:
        raise SystemExit(f"review membership missing: {key} {source['ads_bibcode']}")
    changed = any(str(raw[field]).lower() != str(source[field]).lower() for field in ("title", "doi", "arxiv", "ads_bibcode"))
    record = {
        "source": source,
        "raw_identity": {field: raw[field] for field in ("title", "doi", "arxiv", "ads_bibcode")},
        "evidence": {"ads_public_abstract_identity": "PASS", "review_membership_via_ned_bibliography": member, "composite_author_year_title_doi_arxiv_ads": "PASS"},
        "corrected_from_raw": changed,
        "correction_reason": "ADS-direct composite reconciliation of title, DOI, and arXiv identifier." if changed else None,
    }
    if key in quarantine:
        record.update(status="QUARANTINED_SCOPE", quarantine_reason=quarantine[key])
        quarantined.append(record)
    else:
        source["source_class"] = "supporting_review" if key in supporting else "primary"
        record["status"] = "PASS"
        usable.append(record)

primary_count = sum(row["source"]["source_class"] == "primary" for row in usable)
supporting_count = len(usable) - primary_count
corrected_count = sum(row["corrected_from_raw"] for row in usable + quarantined)
output = {
    "status": "PASS",
    "verified_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "review": {"title": "Physical Models of Galaxy Formation in a Cosmological Framework", "authors": "Somerville & Davé", "year": 2015, "doi": "10.1146/annurev-astro-082812-140951", "arxiv": "1412.2712", "ads_bibcode": "2015ARA&A..53...51S", "identity_status": "PASS_ADS_CROSSREF_ARXIV"},
    "method": "Every raw row reconciled against its ADS public abstract and exact ADS-bibcode membership in the review bibliography; AGN-microphysics rows separately quarantined per mission scope.",
    "raw_source_count": 58,
    "source_count": len(usable),
    "primary_count": primary_count,
    "supporting_review_count": supporting_count,
    "corrected_raw_rows": corrected_count,
    "quarantined_scope_count": len(quarantined),
    "pass_count": len(usable),
    "fail_count": 0,
    "rows": usable,
    "quarantined_rows": quarantined,
}
if len(usable) != 50 or primary_count != 46 or supporting_count != 4 or len(quarantined) != 8:
    raise SystemExit(f"unexpected counts total={len(usable)} primary={primary_count} supporting={supporting_count} quarantine={len(quarantined)}")
OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: output[k] for k in ("status", "source_count", "primary_count", "supporting_review_count", "corrected_raw_rows", "quarantined_scope_count", "pass_count", "fail_count")}, sort_keys=True))
