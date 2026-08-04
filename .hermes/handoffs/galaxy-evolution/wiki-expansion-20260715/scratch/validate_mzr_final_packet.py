import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PACKET = AREA / "area1_mass_metallicity_DR_PACKET.md"
RAW = AREA / "area1_mass_metallicity_DR_RAW_PACKET.md"
REGISTRY = AREA / "area1_mass_metallicity_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area1_mass_metallicity_DR_PACKET_VALIDATION.json"
META = AREA / "area1_mass_metallicity_DR_PACKET.final.metadata.json"

sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
text = PACKET.read_text()
registry = json.loads(REGISTRY.read_text())
expected = {(source["doi"].lower(), source["arxiv"], source["bibcode"]) for source in registry["sources"]}
usable = text[: text.index("## 5. DO_NOT_USE_UNVERIFIED")]
found = re.findall(r"DOI:([^;\s]+); arXiv:([^;\s]+); ADS:([^\s|]+) \| role=", usable)
unknown = [triple for triple in found if (triple[0].lower(), triple[1], triple[2]) not in expected]
checks = {
    "raw_archive_hash_preserved": sha(RAW) == "2f2c4d46bf0583058069d3eb04489f0fb46891cfc719f3c58eaaad34b0094112",
    "registry_pass": registry.get("status") == "PASS" and registry.get("pass_count") == 19 and registry.get("fail_count") == 0,
    "all_usable_citation_tuples_in_registry": bool(found) and not unknown,
    "usable_citation_count_at_least_30": len(found) >= 30,
    "verified_source_ledger_has_19_entries": len(re.findall(r"(?m)^\d+\. .+ DOI `", text[text.index("## 6. Verified source identity ledger"):])) == 19,
    "established_finding_count": len(re.findall(r"(?m)^### MZR-E\d{2}", text)) == 8,
    "debate_count": len(re.findall(r"(?m)^### MZR-D\d{2}", text)) == 7,
    "measurement_count": len(re.findall(r"(?m)^### MZR-N\d{2}", text)) == 7,
    "unknown_count": len(re.findall(r"(?m)^### MZR-U\d{2}", text)) == 5,
    "do_not_use_count_at_least_15": text.count("UNCITED_NOT_USABLE") >= 15,
    "trust_scores_present": text.count("trust:") >= 20,
    "gas_stellar_resolved_boundary_present": "gas-phase metallicity, stellar metallicity, global/fiber measurements, and spatially resolved measurements are not interchangeable" in text,
    "advisory_only": "advisory_only: true" in text and "wiki_write_performed_by_tori: false" in text,
    "terminal_marker": text.rstrip().endswith("MZR_DR_PACKET_COMPLETE_REFERENCE_ONLY"),
}
status = "PASS" if all(checks.values()) else "HOLD"
validation = {
    "status": status,
    "checked_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    "checks": checks,
    "usable_citation_occurrences": len(found),
    "unknown_usable_citation_tuples": unknown,
    "packet_sha256": sha(PACKET),
    "raw_packet_sha256": sha(RAW),
    "registry_sha256": sha(REGISTRY),
}
OUT.write_text(json.dumps(validation, indent=2, sort_keys=True) + "\n")
metadata = {
    "status": "READY_FOR_HWAO_REVIEW" if status == "PASS" else "HOLD",
    "advisory_only": True,
    "wiki_write_performed_by_tori": False,
    "deep_research_conversation_id": "17659460ae83f48a",
    "raw_packet_path": str(RAW),
    "raw_packet_sha256": sha(RAW),
    "final_packet_path": str(PACKET),
    "final_packet_sha256": sha(PACKET),
    "curated_registry_path": str(REGISTRY),
    "curated_registry_sha256": sha(REGISTRY),
    "curated_registry_status": registry.get("status"),
    "curated_source_count": registry.get("source_count"),
    "validation_path": str(OUT),
    "validation_sha256": sha(OUT),
    "validation_status": status,
}
META.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
print(json.dumps(validation, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 2)
