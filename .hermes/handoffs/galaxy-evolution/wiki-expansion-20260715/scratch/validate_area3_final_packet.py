import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PACKET = AREA / "area3_gas_depletion_DR_PACKET.md"
RAW = AREA / "area3_gas_depletion_DR_RAW_PACKET.md"
REGISTRY = AREA / "area3_gas_depletion_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area3_gas_depletion_DR_PACKET_VALIDATION.json"
EXPECTED_RAW_SHA = "17addc6dd3d13850ceef6b844d1264f5cc3167bbccc86ffd11fae963a5501fed"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


text = PACKET.read_text()
registry = json.loads(REGISTRY.read_text())
usable = text.split("## 5. DO_NOT_USE_UNVERIFIED", 1)[0]
ledger = text.split("## 6. Source identity ledger", 1)[1]
source_keys = {row["source"]["key"] for row in registry["rows"]}
referenced = set(re.findall(r"sources: \[([^\]]+)\]", usable))
referenced = {key.strip() for group in referenced for key in group.split(",")}
claim_ids = re.findall(r"\[(GAS-[EDNU]\d{2})\]", usable)
source_rows = re.findall(r"(?m)^.+ \(\d{4}, [^)]+\) \| DOI:[^;]+; arXiv:[^;]+; ADS:\S+ \| role=\S+ \| .+$", ledger)
checks = {
    "raw_sha256_matches": sha(RAW) == EXPECTED_RAW_SHA,
    "registry_status_pass": registry.get("status") == "PASS",
    "registry_source_count_25": registry.get("source_count") == 25,
    "registry_fail_count_zero": registry.get("fail_count") == 0,
    "established_count_12": len(re.findall(r"\[GAS-E\d{2}\]", usable)) == 12,
    "debate_count_7": len(re.findall(r"\[GAS-D\d{2}\]", usable)) == 7,
    "measurement_count_7": len(re.findall(r"\[GAS-N\d{2}\]", usable)) == 7,
    "unknown_count_5": len(re.findall(r"\[GAS-U\d{2}\]", usable)) == 5,
    "do_not_use_count_at_least_20": len(re.findall(r"(?m)^\d+\. UNCITED_NOT_USABLE", text)) >= 20,
    "claim_ids_unique": len(claim_ids) == len(set(claim_ids)),
    "every_claim_has_trust_score": len(re.findall(r"^trust_score:", usable, re.M)) == 31,
    "all_claim_sources_in_registry": referenced <= source_keys,
    "all_registry_sources_used": source_keys <= referenced,
    "source_ledger_rows_25": len(source_rows) == 25,
    "terminal_marker": text.rstrip().endswith("GAS_DR_PACKET_VERIFIED_READY"),
    "no_live_mutation": "wiki_write_performed_by_tori: false" in text and "conversation_deleted: false" in text,
    "no_agn_usable_claim": not re.search(r"\bAGN\b|active galactic", usable, re.I),
    "no_future_2026_usable_claim": "2026" not in usable,
}
for row in registry["rows"]:
    source = row["source"]
    checks[f"ledger_identity_{source['key']}"] = all(value in ledger for value in (source["doi"], source["arxiv"], source["bibcode"]))
wrong = [
    "10.3847/1538-4357/abb82d", "2009.10748", "1301.7436", "10.1093/mnrasl/slz185", "1912.01015",
    "10.1111/j.1365-2966.2011.18678.x", "1103.1644", "1004.1673", "1111.5173", "0909.1325",
    "10.1111/j.1365-2966.2009.16175.x", "1511.02529", "1101.4984",
]
checks["wrong_identifiers_absent_from_usable_and_ledger"] = not any(value in usable or value in ledger for value in wrong)
status = "PASS" if all(checks.values()) else "HOLD"
out = {
    "status": status,
    "validated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    "packet_sha256": sha(PACKET),
    "raw_packet_sha256": sha(RAW),
    "registry_sha256": sha(REGISTRY),
    "counts": {
        "established": 12,
        "debates": 7,
        "measurements": 7,
        "unknowns": 5,
        "do_not_use": len(re.findall(r"(?m)^\d+\. UNCITED_NOT_USABLE", text)),
        "verified_sources": registry.get("pass_count"),
    },
    "checks": checks,
    "failures": [key for key, value in checks.items() if not value],
}
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": status, "counts": out["counts"], "failures": out["failures"]}, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 2)
