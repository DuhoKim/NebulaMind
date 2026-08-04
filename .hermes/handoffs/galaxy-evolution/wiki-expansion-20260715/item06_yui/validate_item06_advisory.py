#!/usr/bin/env python3
"""Deterministically validate and receipt the Yui item-06 advisory packet."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EXPECTED_CLAIM_COUNTS = {
    "REV06-E": 11,
    "REV06-D": 7,
    "REV06-N": 6,
    "REV06-U": 3,
}

EXCLUDED_CLAIMS = {
    "REV06-E07",
    "REV06-D05",
    "REV06-N05",
    "REV06-N06",
    "REV06-U02",
    "REV06-U04",
    "REV06-U06",
}

POLLUTED_ANCHOR_TOKENS = (
    "api.adsabs.harvard.edu",
    "ui.adsabs.harvard.edu/search",
    "api.semanticscholar.org/graph/v1/paper/search",
    "source anchor:",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(condition: bool, name: str, checks: list[dict[str, Any]], detail: Any = None) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--bibliography-receipt", type=Path, required=True)
    parser.add_argument("--membership", type=Path, required=True)
    parser.add_argument("--identity", type=Path, required=True)
    parser.add_argument("--classification", type=Path, required=True)
    parser.add_argument("--canonical", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
    bibliography = json.loads(args.bibliography_receipt.read_text(encoding="utf-8"))
    membership = json.loads(args.membership.read_text(encoding="utf-8"))
    identity = json.loads(args.identity.read_text(encoding="utf-8"))
    classification = json.loads(args.classification.read_text(encoding="utf-8"))
    canonical = args.canonical.read_text(encoding="utf-8")
    checks: list[dict[str, Any]] = []

    check(
        sha256(args.raw) == inventory["custody"]["raw_packet_sha256"],
        "raw_packet_hash_matches_inventory",
        checks,
    )
    authoritative_dir = args.bibliography_receipt.parent / "authoritative"
    authoritative_pdf = authoritative_dir / "arxiv_2003.06245_source"
    bibliography_extract = authoritative_dir / "arxiv_2003.06245_literature_cited.txt"
    check(
        bibliography["source"]["pdf_sha256"] == sha256(authoritative_pdf),
        "authoritative_pdf_hash_matches_receipt",
        checks,
    )
    check(
        bibliography["extraction"]["literature_cited_sha256"]
        == sha256(bibliography_extract),
        "bibliography_extract_hash_matches_receipt",
        checks,
    )
    check(
        membership["physical_source_row_count"] == 45,
        "membership_source_count_45",
        checks,
        membership["physical_source_row_count"],
    )
    membership_counts = membership["status_counts"]
    check(
        membership_counts == {
            "EXACT_BIBLIOGRAPHY_MEMBER": 35,
            "NOT_FOUND_IN_REVIEW_BIBLIOGRAPHY": 8,
            "SURNAME_YEAR_PRESENT_BUT_COMPOSITE_MISMATCH": 2,
        },
        "membership_disposition_counts",
        checks,
        membership_counts,
    )
    identity_counts = identity["disposition_counts"]
    check(
        identity_counts == {
            "QUARANTINE_NOT_EXACT_REVIEW_BIBLIOGRAPHY_MEMBER": 10,
            "USABLE_COMPOSITE_VERIFIED": 35,
        },
        "identity_disposition_counts",
        checks,
        identity_counts,
    )

    results = identity["results"]
    usable = [result for result in results if result["disposition"] == "USABLE_COMPOSITE_VERIFIED"]
    quarantined = [result for result in results if result["disposition"].startswith("QUARANTINE")]
    usable_keys = {result["key"] for result in usable}
    quarantined_keys = {result["key"] for result in quarantined}
    check(len(usable) == 35, "usable_source_count_35", checks, len(usable))
    check(len(quarantined) == 10, "quarantined_source_count_10", checks, len(quarantined))
    check(
        all(all(result["checks"].values()) for result in usable),
        "all_usable_composite_checks_pass",
        checks,
    )
    check(
        all(result["raw_identity"]["year"] <= 2020 for result in usable),
        "no_post_2020_usable_source",
        checks,
    )
    for field in ("canonical_doi", "canonical_arxiv"):
        values = [result[field] for result in usable]
        check(
            all(values) and len(values) == len(set(values)),
            f"{field}_present_and_unique",
            checks,
        )
    ads_values = [result["raw_identity"]["ads"] for result in usable]
    check(
        len(ads_values) == len(set(ads_values)),
        "ads_identifiers_unique",
        checks,
    )

    classifications = classification["entries"]
    check(
        set(classifications) == {result["key"] for result in results},
        "classification_key_set_complete",
        checks,
    )
    role_counts: dict[str, int] = {}
    for value in classifications.values():
        role = value["canonical_role"]
        role_counts[role] = role_counts.get(role, 0) + 1
    check(
        role_counts == {
            "primary_empirical": 24,
            "primary_model": 7,
            "primary_simulation": 2,
            "supporting_review": 2,
            "quarantined_contamination": 10,
        },
        "role_counts",
        checks,
        role_counts,
    )
    check(
        all(classifications[key]["topic_scope"] for key in usable_keys),
        "every_usable_source_has_topic_scope",
        checks,
    )

    claim_region = canonical.split("## Canonical source ledger", 1)[0]
    claim_counts: dict[str, int] = {}
    claim_keys: list[str] = []
    for prefix, expected in EXPECTED_CLAIM_COUNTS.items():
        keys = re.findall(rf"^- \[({prefix}\d{{2}})\]", claim_region, re.MULTILINE)
        claim_counts[prefix] = len(keys)
        claim_keys.extend(keys)
        check(
            len(keys) == expected,
            f"claim_count_{prefix}",
            checks,
            len(keys),
        )
    check(
        len(claim_keys) == 27 and len(set(claim_keys)) == 27,
        "retained_claim_keys_unique_27",
        checks,
    )
    check(
        not (set(claim_keys) & EXCLUDED_CLAIMS),
        "excluded_claim_keys_absent_from_claim_sections",
        checks,
    )
    claim_source_keys = set(re.findall(r"\[(REV06-P\d{3})\]", claim_region))
    check(
        not (claim_source_keys & quarantined_keys),
        "no_quarantined_source_cited_by_retained_claim",
        checks,
        sorted(claim_source_keys & quarantined_keys),
    )
    check(
        claim_source_keys <= usable_keys,
        "all_claim_sources_resolve_to_usable_ledger",
        checks,
        sorted(claim_source_keys - usable_keys),
    )

    primary_region = canonical.split("### Primary empirical/model/simulation sources", 1)[1].split("### Supporting reviews", 1)[0]
    supporting_region = canonical.split("### Supporting reviews", 1)[1].split("## Quarantine ledger", 1)[0]
    quarantine_region = canonical.split("## Quarantine ledger", 1)[1].split("### Quarantined claim keys", 1)[0]
    primary_rows = re.findall(r"^- \[(REV06-P\d{3})\]", primary_region, re.MULTILINE)
    supporting_rows = re.findall(r"^- \[(REV06-P\d{3})\]", supporting_region, re.MULTILINE)
    quarantine_rows = re.findall(r"^- \[(REV06-P\d{3})\]", quarantine_region, re.MULTILINE)
    check(len(primary_rows) == 33, "canonical_primary_rows_33", checks, len(primary_rows))
    check(len(supporting_rows) == 2, "canonical_supporting_review_rows_2", checks, len(supporting_rows))
    check(len(quarantine_rows) == 10, "canonical_quarantine_rows_10", checks, len(quarantine_rows))
    check(
        set(primary_rows + supporting_rows) == usable_keys,
        "canonical_usable_ledger_key_set_exact",
        checks,
    )
    check(
        set(quarantine_rows) == quarantined_keys,
        "canonical_quarantine_key_set_exact",
        checks,
    )
    check(
        not any(token.lower() in canonical.lower() for token in POLLUTED_ANCHOR_TOKENS),
        "polluted_raw_anchor_tokens_absent",
        checks,
    )
    required_safety = (
        "Browser/account action: none.",
        "Live wiki/DB/trust mutation: none.",
        "Deploy/restart: none.",
        "Git write/publication: none.",
        "Hwao/DESI crew interruption after redirect: none.",
    )
    check(
        all(statement in canonical for statement in required_safety),
        "safety_receipt_complete",
        checks,
    )

    failed = [item for item in checks if not item["passed"]]
    receipt = {
        "schema_version": 1,
        "status": "PASS" if not failed else "FAIL",
        "validated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "counts": {
            "checks": len(checks),
            "failed": len(failed),
            "usable_sources": len(usable),
            "primary_sources": len(primary_rows),
            "supporting_reviews": len(supporting_rows),
            "quarantined_sources": len(quarantine_rows),
            "retained_claims": len(claim_keys),
            "claim_prefixes": claim_counts,
        },
        "artifact_sha256": {
            "raw": sha256(args.raw),
            "inventory": sha256(args.inventory),
            "bibliography_receipt": sha256(args.bibliography_receipt),
            "membership": sha256(args.membership),
            "identity": sha256(args.identity),
            "classification": sha256(args.classification),
            "canonical": sha256(args.canonical),
        },
        "checks": checks,
        "failed_checks": failed,
        "safety": {
            "network_operations_performed_by_validator": 0,
            "browser_or_account_action": False,
            "live_wiki_db_trust_write": False,
            "deploy_restart": False,
            "git_write": False,
            "publication": False,
            "other_agents_or_hwao_interrupted": False,
        },
    }
    args.output.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    if failed:
        for item in failed:
            print(f"FAIL {item['name']}: {item.get('detail')}")
        return 1
    print(
        "PASS",
        f"checks={len(checks)}",
        "usable=35",
        "primary=33",
        "supporting_reviews=2",
        "quarantine=10",
        "claims=27",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
