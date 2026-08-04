import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PACKET = AREA / "area_review_05_maiolino_mannucci_2019_DR_PACKET.md"
REGISTRY = AREA / "area_review_05_maiolino_mannucci_2019_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_05_maiolino_mannucci_2019_VALIDATION.json"
text = PACKET.read_text()
reg = json.loads(REGISTRY.read_text())
checks = {}
for prefix, expected in (("E", 12), ("D", 8), ("N", 8), ("U", 6)):
    ids = set(re.findall(rf"\[REV05-{prefix}\d{{2}}\]", text))
    checks[f"{prefix}_count"] = {"pass": len(ids) == expected, "actual": len(ids), "expected": expected}
usable = {r["key"] for r in reg["usable_sources"]}
quarantine = {r["key"] for r in reg["quarantined_sources"]}
claim_part = text.split("## 6. Primary-Citation Harvest", 1)[0]
claim_refs = set(re.findall(r"\[(REV05-P\d{3})\]", claim_part))
checks["claim_refs_resolve"] = {"pass": claim_refs <= usable, "unresolved": sorted(claim_refs - usable)}
harvest = text.split("## 6. Primary-Citation Harvest", 1)[1].split("## 7. DO_NOT_USE_UNVERIFIED", 1)[0]
primary = set(re.findall(r"^\[(REV05-P\d{3})\].+role=(?!supporting)", harvest.split("### Supporting",1)[0], re.M))
support = set(re.findall(r"^\[(REV05-P\d{3})\]", harvest.split("### Supporting reviews/syntheses",1)[1], re.M))
checks["primary_harvest"] = {"pass": len(primary) == 45, "actual": len(primary), "expected": 45}
checks["supporting_harvest"] = {"pass": len(support) == 2, "actual": len(support), "expected": 2}
ledger = text.split("## 8. Review and Source Identity Ledger", 1)[1]
ledger_keys = set(re.findall(r"^\[(REV05-P\d{3})\]", ledger, re.M))
checks["ledger_complete"] = {"pass": ledger_keys == usable, "missing": sorted(usable-ledger_keys), "extra": sorted(ledger_keys-usable)}
checks["quarantine_absent_from_usable"] = {"pass": not (quarantine & (primary | support | ledger_keys)), "bad": sorted(quarantine & (primary | support | ledger_keys))}
checks["review_identity"] = {"pass": all(x in text for x in ("10.1007/s00159-018-0112-2", "1811.09642", "2019A&ARv..27....3M"))}
checks["raw_hash"] = {"pass": "d68f2e08e22261cc70195f5ee6654c2fa2270f463642e3b25600e646392e5fd4" in text}
checks["terminal_marker"] = {"pass": text.rstrip().endswith("REVIEW_BASE_05_DR_COMPLETE_REFERENCE_ONLY")}
checks["dnu_count"] = {"pass": text.count("UNCITED_NOT_USABLE |") >= 56, "actual": text.count("UNCITED_NOT_USABLE |"), "minimum": 56}
checks["temporal_cutoff"] = {"pass": max(r["year"] for r in reg["usable_sources"]) <= 2019, "maximum_year": max(r["year"] for r in reg["usable_sources"])}
checks["registry_counts"] = {"pass": (reg["usable_source_count"], reg["primary_source_count"], reg["supporting_source_count"], reg["quarantined_source_count"]) == (47,45,2,4)}
checks["raw_tuple_corrections"] = {"pass": reg["corrected_source_count"] == 46, "actual": reg["corrected_source_count"]}
checks["safety"] = {"pass": "advisory_only: true" in text and "wiki_write_performed_by_tori: false" in text}
failed = [k for k,v in checks.items() if not v["pass"]]
payload = {"status": "PASS" if not failed else "FAIL", "validated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00","Z"), "packet_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest(), "failed_checks": failed, "checks": checks}
OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"status":payload["status"],"packet_sha256":payload["packet_sha256"],"failed_checks":failed},sort_keys=True))
raise SystemExit(0 if not failed else 1)
