import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PACKET = AREA / "area_review_02_madau_dickinson_2014_DR_PACKET.md"
RAW = AREA / "area_review_02_madau_dickinson_2014_DR_RAW_PACKET.md"
REGISTRY = AREA / "area_review_02_madau_dickinson_2014_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_02_madau_dickinson_2014_VALIDATION.json"
text = PACKET.read_text()
raw = RAW.read_bytes()
registry = json.loads(REGISTRY.read_text())
checks = {}
checks["raw_sha256_preserved"] = hashlib.sha256(raw).hexdigest() == "ef029656480cfc3867cfef85999be5a9a812bd6b48907df141cead8d98d7a36f"
checks["registry_pass"] = registry["status"] == "PASS" and registry["source_count"] == 44 and registry["primary_count"] == 40 and registry["supporting_review_or_proceeding_count"] == 4 and registry["fail_count"] == 0
for i in range(1, 9):
    checks[f"section_{i}_present"] = f"## {i}." in text
checks["established_count"] = len(re.findall(r"^\[REV02-E\d{2}\]", text, re.M)) == 12
checks["debate_count"] = len(re.findall(r"^\[REV02-D\d{2}\]", text, re.M)) == 8
checks["measurement_count"] = len(re.findall(r"^\[REV02-N\d{2}\]", text, re.M)) == 8
checks["unknown_count"] = len(re.findall(r"^\[REV02-U\d{2}\]", text, re.M)) == 6
section6 = text.split("## 6. Primary-citation harvest", 1)[1].split("## 7. DO_NOT_USE_UNVERIFIED", 1)[0]
primary_part, supporting_part = section6.split("### Supporting cited reviews/proceeding", 1)
checks["primary_harvest_count"] = len(re.findall(r"^\[REV02-P\d{3}\]", primary_part, re.M)) == 40
checks["supporting_count"] = len(re.findall(r"^\[REV02-P\d{3}\]", supporting_part, re.M)) == 4
section7 = text.split("## 7. DO_NOT_USE_UNVERIFIED", 1)[1].split("## 8. Review and source identity ledger", 1)[0]
checks["dnu_present_and_complete"] = len(re.findall(r"^UNCITED_NOT_USABLE", section7, re.M)) == registry["corrected_raw_rows"] + 8
section8 = text.split("## 8. Review and source identity ledger", 1)[1]
checks["ledger_count"] = len(re.findall(r"^\[REV02-P\d{3}\]", section8, re.M)) == 44
keys = {row["source"]["key"] for row in registry["rows"]}
claim_refs = set(re.findall(r"\[(REV02-P\d{3})\]", text.split("## 6. Primary-citation harvest", 1)[0]))
checks["all_claim_refs_resolve"] = claim_refs <= keys
source_part = section6 + section8
identity_missing = []
for row in registry["rows"]:
    s = row["source"]
    for field in ("title", "doi", "arxiv", "ads_bibcode"):
        if str(s[field]) not in source_part:
            identity_missing.append(f"{s['key']}:{field}")
checks["all_registry_identities_rendered"] = not identity_missing
checks["all_sources_within_2014"] = all(row["source"]["year"] <= 2014 for row in registry["rows"])
wrong_in_usable = []
for row in registry["rows"]:
    raw_id = row.get("raw_identity")
    if not raw_id or not row.get("corrected_from_raw"):
        continue
    final = row["source"]
    for field in ("title", "doi", "arxiv", "ads_bibcode"):
        old = str(raw_id[field])
        token = {
            "title": f"title={old} |",
            "doi": f"DOI:{old};",
            "arxiv": f"arXiv:{old};",
            "ads_bibcode": f"ADS:{old}",
        }[field]
        if old.lower() != str(final[field]).lower() and old.lower() != "none" and token in source_part:
            wrong_in_usable.append(f"{final['key']}:{field}:{old}")
checks["crosswired_raw_values_quarantined"] = not wrong_in_usable
checks["review_identity_complete"] = all(value in text for value in ("10.1146/annurev-astro-081811-125615", "1403.0007", "2014ARA&A..52..415M"))
checks["terminal_marker_exact"] = text.rstrip().endswith("REVIEW_BASE_02_DR_COMPLETE_REFERENCE_ONLY")
checks["advisory_boundary"] = all(value in text for value in ("advisory_only: true", "wiki_write_performed_by_tori: false", "canonical_source_base_not_live_wiki_prose: true"))
checks["no_external_anchor_dump"] = "## Captured external source anchors" not in text
failed = [key for key, value in checks.items() if not value]
result = {
    "status": "PASS" if not failed else "FAIL",
    "validated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    "packet": str(PACKET),
    "packet_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest(),
    "raw_packet_sha256": hashlib.sha256(raw).hexdigest(),
    "registry_sha256": hashlib.sha256(REGISTRY.read_bytes()).hexdigest(),
    "counts": {"established": 12, "debates": 8, "measurements": 8, "unknowns": 6, "primary_sources": 40, "supporting_sources": 4, "usable_sources": 44},
    "identity_missing": identity_missing,
    "wrong_in_usable": wrong_in_usable,
    "checks": checks,
    "failed_checks": failed,
}
OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": result["status"], "failed_checks": failed, "packet_sha256": result["packet_sha256"]}, sort_keys=True))
raise SystemExit(0 if not failed else 2)
