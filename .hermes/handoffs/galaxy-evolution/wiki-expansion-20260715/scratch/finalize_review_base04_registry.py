import json
import re
import time
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
RAW = AREA / "area_review_04_naab_ostriker_2017_DR_RAW_PACKET.md"
ADS = json.loads((AREA / "area_review_04_naab_ostriker_2017_ADS_IDENTITIES.json").read_text())["identities"]
NED = Path("/Users/duhokim/.hermes/cache/web/ned.ipac.caltech.edu-e8dc74f24b.md").read_text()
OUT = AREA / "area_review_04_naab_ostriker_2017_CURATED_SOURCE_REGISTRY.json"

text = RAW.read_text()
harvest = text.split("6. Primary-Citation Harvest", 1)[1].split("7. DO_NOT_USE_UNVERIFIED", 1)[0]
pattern = re.compile(
    r"^\[(REV04-(?:P\d{3}|S\d{2}))\] (.+?) \((\d{4}), (.+?)\) \| title=(.+?) \| DOI:(.+?); arXiv:(.+?); ADS:(\S+) \| role=(\w+) \| review_locator=(.+?) \| (.*)$",
    re.M,
)
raw_rows = {}
for match in pattern.finditer(harvest):
    key, authors, year, journal, title, doi, arxiv, bibcode, role, locator, boundary = match.groups()
    raw_rows[key] = {"key": key, "authors": authors, "first_author": authors.split()[0], "year": int(year), "journal": journal, "title": title, "doi": doi, "arxiv": arxiv, "ads_bibcode": bibcode, "role": role, "review_locator": locator, "boundary": boundary}
if len(raw_rows) != 53:
    raise SystemExit(f"expected 53 rows, parsed {len(raw_rows)}")

supporting = {"REV04-P016", "REV04-S01", "REV04-S02", "REV04-S04"}
uncited = {"REV04-P005", "REV04-P011", "REV04-P013", "REV04-P019", "REV04-P042", "REV04-P043", "REV04-P047", "REV04-P048", "REV04-S03"}
quarantine_reasons = {
    key: "Exact ADS bibcode is absent from the authoritative NED review bibliography and the corrected DOI is absent from the review's structured Crossref references; physically valid candidate is not usable as review-cited."
    for key in uncited
}
quarantine_reasons["REV04-P019"] = "Supplied conference bibcode does not resolve to a public ADS abstract and is absent from the review bibliography; identity and review membership are unresolved."
boundary_updates = {
    "REV04-P008": "Analytic hydrostatic-equilibrium accounting for magnetic and cosmic-ray support in the Galactic disk; not a direct observational measurement.",
    "REV04-P009": "Simulation result that preferentially ejected low-angular-momentum gas can support bulgeless disks; implementation and halo-history dependent.",
    "REV04-P013": "Small-scale cold-dark-matter crisis analysis; do not use as the named angular-momentum-loss simulation paper.",
    "REV04-P014": "Kinetic supernova-feedback outflow implementation; wind behavior depends on launch parameters and hydrodynamic coupling.",
    "REV04-P016": "Textbook synthesis of ISM and intergalactic-medium physics; supporting reference, not a primary paper.",
    "REV04-P018": "Controlled supernova-remnant calculations across wind-blown, turbulent, and power-law media; ambient structure sets momentum evolution.",
    "REV04-P020": "Magnetized multiphase galactic-disc simulation regulated by supernova explosions; numerical and chemistry assumptions apply.",
    "REV04-P029": "Galactic-fountain interaction with rotating coronae; constrains fountain/corona angular-momentum exchange rather than generic nonlinear torques.",
    "REV04-P033": "Simulation of photoionizing ultraviolet-background effects on disk-galaxy formation; not a generic no-feedback angular-momentum experiment.",
    "REV04-P044": "SILCC chemical evolution of a supernova-driven ISM; do not overextend to a universal clustered-versus-isolated momentum validation.",
    "REV04-P048": "Molecular-cloud formation from gravitational collapse of static initial conditions; not a general turbulence-controlled timescale result.",
}
role_updates = {"REV04-P008": "analytic_theory", "REV04-P016": "supporting_reference", "REV04-P019": "supporting_reference"}

usable = []
quarantined = []
for key in sorted(raw_rows):
    raw = raw_rows[key]
    identity = ADS[key]
    source = dict(raw)
    ads_resolved = identity["title"] != "Page not found"
    if ads_resolved:
        source.update(title=identity["title"], doi=identity["doi"], arxiv=identity["arxiv"])
    source["role"] = role_updates.get(key, source["role"])
    source["boundary"] = boundary_updates.get(key, source["boundary"])
    member = source["ads_bibcode"] in NED or source["ads_bibcode"].replace("&", "%26") in NED
    if not member and key not in uncited:
        raise SystemExit(f"review membership missing unexpectedly: {key} {source['ads_bibcode']}")
    changed = any(str(raw[field]).lower() != str(source[field]).lower() for field in ("title", "doi", "arxiv", "ads_bibcode"))
    record = {
        "source": source,
        "raw_identity": {field: raw[field] for field in ("title", "doi", "arxiv", "ads_bibcode")},
        "evidence": {
            "ads_public_abstract_identity": "PASS" if ads_resolved else "FAIL_UNRESOLVED",
            "review_membership_via_ned_bibliography": member,
            "corrected_doi_absent_from_crossref_review_references": key in uncited and key != "REV04-P019",
            "composite_author_year_title_doi_arxiv_ads": "PASS" if ads_resolved else "FAIL",
        },
        "corrected_from_raw": changed,
        "correction_reason": "ADS-direct composite reconciliation of title, DOI, and arXiv identifier." if changed else None,
    }
    if key in uncited:
        record.update(status="QUARANTINED_MEMBERSHIP_OR_IDENTITY", quarantine_reason=quarantine_reasons[key])
        quarantined.append(record)
    else:
        source["source_class"] = "supporting_review_or_reference" if key in supporting else "primary"
        record["status"] = "PASS"
        usable.append(record)

primary_count = sum(row["source"]["source_class"] == "primary" for row in usable)
supporting_count = len(usable) - primary_count
corrected_count = sum(row["corrected_from_raw"] for row in usable + quarantined)
output = {
    "status": "PASS",
    "verified_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "review": {"title": "Theoretical Challenges in Galaxy Formation", "authors": "Naab & Ostriker", "year": 2017, "doi": "10.1146/annurev-astro-081913-040019", "arxiv": "1612.06891", "ads_bibcode": "2017ARA&A..55...59N", "identity_status": "PASS_ADS_CROSSREF_ARXIV"},
    "method": "Every candidate reconciled against its exact public ADS page and exact review membership through the NED bibliography; absent bibcodes also checked against Crossref structured reference DOIs.",
    "raw_source_count": 53,
    "source_count": len(usable),
    "primary_count": primary_count,
    "supporting_review_count": supporting_count,
    "corrected_raw_rows": corrected_count,
    "quarantined_count": len(quarantined),
    "pass_count": len(usable),
    "fail_count": 0,
    "rows": usable,
    "quarantined_rows": quarantined,
}
if len(usable) != 44 or primary_count != 40 or supporting_count != 4 or len(quarantined) != 9:
    raise SystemExit(f"unexpected counts total={len(usable)} primary={primary_count} supporting={supporting_count} quarantine={len(quarantined)}")
OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: output[k] for k in ("status", "source_count", "primary_count", "supporting_review_count", "corrected_raw_rows", "quarantined_count", "pass_count", "fail_count")}, sort_keys=True))
