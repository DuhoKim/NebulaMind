import hashlib
import json
import re
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PACKET = AREA / "area2_chemical_evolution_DR_PACKET.md"
RAW = AREA / "area2_chemical_evolution_DR_RAW_PACKET.md"
REGISTRY = AREA / "area2_chemical_evolution_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area2_chemical_evolution_DR_PACKET_VALIDATION.json"
EXPECTED_RAW_SHA = "5a877ee469067716f7c11bc8e3bc6ad1a25e7c5cf41ca6527713490c6bb7313e"

text = PACKET.read_text()
registry = json.loads(REGISTRY.read_text())
registry_keys = {row["source"]["key"] for row in registry["rows"] if row["status"] == "PASS"}
ids = {
    prefix: re.findall(rf"\[(CHEM-{prefix}\d{{2}})\]", text)
    for prefix in ("E", "D", "N", "U")
}
source_refs = set()
for match in re.finditer(r"^sources:\s*\[([^\]]+)\]", text, re.M):
    source_refs.update(key.strip() for key in match.group(1).split(","))
ledger = text.split("## 6. Source identity ledger", 1)[1].split("CHEM_DR_PACKET_COMPLETE_REFERENCE_ONLY", 1)[0]
ledger_rows = [line for line in ledger.splitlines() if " | DOI:" in line or " | arXiv:" in line]
checks = {
    "status_ready": "status: READY_FOR_HWAO_REVIEW" in text,
    "advisory_only": "advisory_only: true" in text and "wiki_write_performed_by_tori: false" in text,
    "distinct_from_area1": "distinct_from_area1_mzr: true" in text,
    "established_count_at_least_10": len(set(ids["E"])) >= 10,
    "debate_count_at_least_7": len(set(ids["D"])) >= 7,
    "number_count_at_least_6": len(set(ids["N"])) >= 6,
    "unknown_count_at_least_5": len(set(ids["U"])) >= 5,
    "all_ids_unique": all(len(values) == len(set(values)) for values in ids.values()),
    "role_markers_present": text.count("role: established") >= 10 and text.count("role: debate") >= 7 and text.count("role: measurement") >= 6 and text.count("role: future") >= 5,
    "trust_scores_present": text.count("trust_score:") >= 25,
    "dnu_present": "## 5. DO_NOT_USE_UNVERIFIED" in text and text.count("UNCITED_NOT_USABLE") >= 12,
    "terminal_marker": "CHEM_DR_PACKET_COMPLETE_REFERENCE_ONLY" in text,
    "registry_pass": registry.get("status") == "PASS" and registry.get("pass_count") == 29 and registry.get("fail_count") == 0,
    "all_claim_source_keys_verified": source_refs <= registry_keys,
    "no_orphan_registry_key_typo": not (source_refs - registry_keys),
    "ledger_row_count_29": len(ledger_rows) == 29,
    "ledger_ads_count_29": ledger.count("ADS:") == 29,
    "raw_preserved": hashlib.sha256(RAW.read_bytes()).hexdigest() == EXPECTED_RAW_SHA,
    "no_live_write_claim": "No DB, wiki, trust-score, claim/evidence, deploy, git, publish" in text,
    "no_unbounded_raw_superlatives_in_usable_sections": all(
        phrase not in text.split("## 5. DO_NOT_USE_UNVERIFIED", 1)[0]
        for phrase in ("universally necessitating", "strictly correspond", "unequivocally", "definitive nucleosynthetic sources")
    ),
}
result = {
    "status": "PASS" if all(checks.values()) else "HOLD",
    "checks": checks,
    "counts": {prefix: len(set(values)) for prefix, values in ids.items()},
    "source_reference_count": len(source_refs),
    "registry_key_count": len(registry_keys),
    "unverified_source_keys": sorted(source_refs - registry_keys),
    "ledger_row_count": len(ledger_rows),
    "packet_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest(),
    "raw_sha256": hashlib.sha256(RAW.read_bytes()).hexdigest(),
}
OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
raise SystemExit(0 if result["status"] == "PASS" else 2)
