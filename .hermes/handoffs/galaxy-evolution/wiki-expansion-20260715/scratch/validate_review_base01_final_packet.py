import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PACKET = AREA / "area_review_01_kennicutt_evans_2012_DR_PACKET.md"
RAW = AREA / "area_review_01_kennicutt_evans_2012_DR_RAW_PACKET.md"
REGISTRY = AREA / "area_review_01_kennicutt_evans_2012_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_01_kennicutt_evans_2012_DR_PACKET_VALIDATION.json"
EXPECTED_RAW_SHA = "8a778bc16d31b928866c9df397fcb57515d7841406ed1c760322a16e185df568"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


text = PACKET.read_text()
registry = json.loads(REGISTRY.read_text())
claims = text.split("## 6. Primary-citation harvest", 1)[0]
harvest = text.split("## 6. Primary-citation harvest", 1)[1].split("## 7. DO_NOT_USE_UNVERIFIED", 1)[0]
dnu = text.split("## 7. DO_NOT_USE_UNVERIFIED", 1)[1].split("## 8. Review and source identity ledger", 1)[0]
ledger = text.split("## 8. Review and source identity ledger", 1)[1]
source_keys = {row["source"]["key"] for row in registry["rows"]}
claim_refs = set()
for group in re.findall(r"sources: \[([^\]]+)\]", claims):
    claim_refs.update(key.strip() for key in group.split(","))
harvest_keys = set(re.findall(r"(?m)^\[(REV01-P\d{3})\]", harvest))
ledger_keys = set(re.findall(r"(?m)^(REV01-P\d{3}) \|", ledger))
claim_ids = re.findall(r"\[(REV01-[EDNU]\d{2})\]", claims)
checks = {
    "raw_sha256_matches": sha(RAW) == EXPECTED_RAW_SHA,
    "registry_status_pass": registry.get("status") == "PASS",
    "registry_rows_43": registry.get("pass_count") == 43 and registry.get("fail_count") == 0,
    "corrected_raw_rows_25": registry.get("corrected_raw_composite_rows") == 25,
    "phantom_keys_20": len(registry.get("phantom_source_keys_quarantined", [])) == 20,
    "established_count_12": len(re.findall(r"\[REV01-E\d{2}\]", claims)) == 12,
    "debate_count_8": len(re.findall(r"\[REV01-D\d{2}\]", claims)) == 8,
    "measurement_count_8": len(re.findall(r"\[REV01-N\d{2}\]", claims)) == 8,
    "unknown_count_6": len(re.findall(r"\[REV01-U\d{2}\]", claims)) == 6,
    "claim_ids_unique": len(claim_ids) == len(set(claim_ids)),
    "all_claims_have_trust": len(re.findall(r"(?m)^trust_score:", claims)) == 34,
    "all_claim_refs_resolve": claim_refs <= source_keys | {"REV01"},
    "harvest_has_exact_43": harvest_keys == source_keys,
    "ledger_has_exact_43": ledger_keys == source_keys,
    "no_post_2012_harvest": all(row["source"]["year"] <= 2012 for row in registry["rows"]),
    "dnu_correction_rows_25": len(re.findall(r"cross-wired fields=", dnu)) == 25,
    "dnu_phantom_rows_20": len(re.findall(r"phantom source key", dnu)) == 20,
    "terminal_marker": text.rstrip().endswith("REVIEW_BASE_01_VERIFIED_READY_REFERENCE_ONLY"),
    "review_identity": all(value in text for value in ("10.1146/annurev-astro-081811-125610", "1204.3552", "2012ARA&A..50..531K")),
    "advisory_no_mutation": "wiki_write_performed_by_tori: false" in text and "conversation_deleted: false" in text,
}
for row in registry["rows"]:
    source = row["source"]
    checks[f"identity_harvest_{source['key']}"] = all(value in harvest for value in (source["title"], source["doi"], source["arxiv"], source["bibcode"]))
    checks[f"identity_ledger_{source['key']}"] = all(value in ledger for value in (source["doi"], source["arxiv"], source["bibcode"]))
raw_result = RAW.read_text().split("## Deep Research review-base result\n\n", 1)[1].split("\n\n## Captured external source anchors", 1)[0]
pattern = re.compile(r"^\[(REV01-P\d{3})\] (.+?) \((\d{4}), ([^)]+)\) \| title=(.+?) \| DOI:([^;]+); arXiv:([^;]+); ADS:(\S+) \| role=(\S+) \| review_locator=(.+?) \| (.+)$", re.M)
raw_rows = {match.group(1): {"title": match.group(5), "doi": match.group(6).strip(), "arxiv": match.group(7).strip()} for match in pattern.finditer(raw_result)}
canonical_by_key = {row["source"]["key"]: row["source"] for row in registry["rows"]}
wrong_values = []
for key, raw in raw_rows.items():
    canonical = canonical_by_key[key]
    wrong_values.extend(raw[field] for field in ("title", "doi", "arxiv") if raw[field] != canonical[field] and raw[field].lower() not in {"none", "n/a", ""})
checks["raw_wrong_values_absent_from_usable_and_ledger"] = not any(value in claims or value in harvest or value in ledger for value in wrong_values)
status = "PASS" if all(checks.values()) else "HOLD"
out = {
    "status": status,
    "validated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    "packet_sha256": sha(PACKET),
    "raw_packet_sha256": sha(RAW),
    "registry_sha256": sha(REGISTRY),
    "counts": {
        "established": 12,
        "debates": 8,
        "measurements": 8,
        "unknowns": 6,
        "verified_primary_sources": 43,
        "corrected_raw_composites": 25,
        "phantom_keys_quarantined": 20,
        "do_not_use_rows": len(re.findall(r"(?m)^UNCITED_NOT_USABLE", dnu)),
    },
    "checks": checks,
    "failures": [key for key, value in checks.items() if not value],
}
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": status, "counts": out["counts"], "failures": out["failures"]}, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 2)
