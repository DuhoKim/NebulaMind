import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PACKET = AREA / "area_review_04_naab_ostriker_2017_DR_PACKET.md"
RAW = AREA / "area_review_04_naab_ostriker_2017_DR_RAW_PACKET.md"
REGISTRY = AREA / "area_review_04_naab_ostriker_2017_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_04_naab_ostriker_2017_VALIDATION.json"
text = PACKET.read_text()
raw_sha = hashlib.sha256(RAW.read_bytes()).hexdigest()
packet_sha = hashlib.sha256(PACKET.read_bytes()).hexdigest()
reg = json.loads(REGISTRY.read_text())
usable = {row["source"]["key"] for row in reg["rows"]}
quarantined = {row["source"]["key"] for row in reg["quarantined_rows"]}
claim_region = text.split("## 2. Established findings", 1)[1].split("## 6. Primary-citation harvest", 1)[0]
harvest_region = text.split("## 6. Primary-citation harvest", 1)[1].split("## 7. DO_NOT_USE_UNVERIFIED", 1)[0]
primary_region, supporting_region = harvest_region.split("### Supporting cited reviews or references", 1)
ledger_region = text.split("## 8. Review and source identity ledger", 1)[1]
usable_region = harvest_region + ledger_region
refs = set(re.findall(r"\[(REV04-(?:P\d{3}|S\d{2}))\]", claim_region))
primary_keys = set(re.findall(r"^\[(REV04-P\d{3})\]", primary_region, re.M))
supporting_keys = set(re.findall(r"^\[(REV04-(?:P\d{3}|S\d{2}))\]", supporting_region, re.M))
ledger_keys = set(re.findall(r"^\[(REV04-(?:P\d{3}|S\d{2}))\] \|", ledger_region, re.M))
wrong_in_usable = []
for row in reg["rows"] + reg["quarantined_rows"]:
    if not row.get("corrected_from_raw"):
        continue
    old = row["raw_identity"]
    final = row["source"]
    tokens = {"title": f"title={old['title']} |", "doi": f"DOI:{old['doi']};", "arxiv": f"arXiv:{old['arxiv']};", "ads_bibcode": f"ADS:{old['ads_bibcode']}"}
    final_tokens = {"title": f"title={final['title']} |", "doi": f"DOI:{final['doi']};", "arxiv": f"arXiv:{final['arxiv']};", "ads_bibcode": f"ADS:{final['ads_bibcode']}"}
    for field, token in tokens.items():
        if old[field] != "none" and token != final_tokens[field] and token in usable_region:
            wrong_in_usable.append(f"{final['key']}:{field}:{old[field]}")
checks = {
    "raw_hash_preserved": raw_sha == "69860881137f7c919f2bc9be32f149eace280672df093870ff63abb8f54e9af0",
    "registry_pass": reg["status"] == "PASS" and reg["pass_count"] == 44 and reg["fail_count"] == 0,
    "counts_registry": reg["primary_count"] == 40 and reg["supporting_review_count"] == 4 and reg["quarantined_count"] == 9,
    "review_identity": all(x in text for x in ("10.1146/annurev-astro-081913-040019", "1612.06891", "2017ARA&A..55...59N")),
    "established_12": len(re.findall(r"^\[REV04-E\d{2}\]$", text, re.M)) == 12,
    "debates_8": len(re.findall(r"^\[REV04-D\d{2}\]", text, re.M)) == 8,
    "measurements_8": len(re.findall(r"^\[REV04-N\d{2}\]", text, re.M)) == 8,
    "unknowns_6": len(re.findall(r"^\[REV04-U\d{2}\]", text, re.M)) == 6,
    "primary_harvest_40": len(primary_keys) == 40,
    "supporting_4": len(supporting_keys) == 4,
    "harvest_exact_registry": primary_keys | supporting_keys == usable,
    "ledger_44": ledger_keys == usable,
    "claim_refs_resolve": refs <= usable,
    "quarantined_absent_claims": not (refs & quarantined),
    "quarantined_absent_usable_ledger": not any(f"[{key}]" in usable_region for key in quarantined),
    "wrong_raw_identifiers_absent_usable": not wrong_in_usable,
    "dnu_minimum": text.count("UNCITED_NOT_USABLE") >= 45,
    "year_boundary": max(row["source"]["year"] for row in reg["rows"]) <= 2017,
    "terminal_marker_once_and_last": text.count("REVIEW_BASE_04_DR_COMPLETE_REFERENCE_ONLY") == 1 and text.rstrip().endswith("REVIEW_BASE_04_DR_COMPLETE_REFERENCE_ONLY"),
    "advisory_only": "advisory_only: true" in text and "wiki_write_performed_by_tori: false" in text,
}
failed = [name for name, ok in checks.items() if not ok]
result = {"status": "PASS" if not failed else "FAIL", "validated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"), "packet": str(PACKET), "packet_sha256": packet_sha, "raw_packet_sha256": raw_sha, "checks": checks, "failed_checks": failed, "wrong_in_usable": wrong_in_usable, "claim_source_keys": sorted(refs), "usable_source_count": len(usable), "quarantined_source_count": len(quarantined)}
OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": result["status"], "failed_checks": failed, "packet_sha256": packet_sha}, sort_keys=True))
raise SystemExit(0 if not failed else 2)
