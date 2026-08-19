#!/usr/bin/env python3
"""Independent local verifier for the M1+M3+M4+M5 execution package."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from fractions import Fraction

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent.parent
EXPECTED_BINDING = "1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b"
EXPECTED_MANIFEST = "ff75636cf8fe14f14bcd35721491cbdf225d31d706325c114ecba4e91cf0dde2"
EXPECTED_HARVEST_RECEIPTS = "d3ffc2c2a05d710f247ca253cb7b645b75acc83991042e6e1897e03be06e14ef"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def verify() -> dict:
    binding = PREREG / "TORI_ROUTE_BINDING_SUCCESSOR_20260817.md"
    manifest = HERE.parent / "candidate_image_manifest.jsonl"
    require(digest(binding) == EXPECTED_BINDING, "binding hash")
    require((binding.stat().st_mode & 0o777) == 0o444, "binding mode")
    require(digest(manifest) == EXPECTED_MANIFEST, "manifest hash")

    harvest = PREREG / "_tori_harvest_20260817/receipts.jsonl"
    completion = json.loads((PREREG / "_tori_harvest_20260817/HARVEST_COMPLETE.json").read_text())
    require(digest(harvest) == EXPECTED_HARVEST_RECEIPTS, "harvest receipt hash")
    count = covered = ok = 0
    urls: set[str] = set()
    with harvest.open() as f:
        for line in f:
            row = json.loads(line)
            count += 1
            covered += row.get("image_r_listed") is True
            ok += row.get("outcome") == "OK_CONFIRMED"
            urls.add(row["url"])
    require((count, covered, ok, len(urls)) == (60308, 60308, 60308, 60308), "coverage census")
    require(completion["completed"] == completion["total"] == 60308, "completion record")

    cross = json.loads((PREREG / "_tmp_crosscheck_receipts/intersection_result.json").read_text())
    require(cross["replaced_total"] == 598, "replaced total")
    require(cross["replaced_in_ws"] == cross["late"] == 397, "replacement/late equality")
    require(cross["hazard"] == [] and cross["anomaly"] == [], "hazard/anomaly empty")
    require(cross["control_nonreplaced"] == 59911 and cross["control_late_violations"] == 0, "control clean")
    require((PREREG / "CROSSCHECK_VERDICT_20260819.md").read_text().splitlines()[0] == "CROSSCHECK_PASS", "crosscheck first line")
    require((PREREG / "KUN_CC_GATE_20260819.md").read_text().splitlines()[0] == "PASS_CROSSCHECK_GATE", "gate first line")

    custody_path = PREREG / "_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/STATIC_PRODUCT_CUSTODY.json"
    sidecar_path = PREREG / "_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/static/survey-bricks-dr10-south.fits.gz"
    custody = json.loads(custody_path.read_text())
    local_hash = digest(sidecar_path)
    require(custody["source_url"].endswith("/survey-bricks-dr10-south.fits.gz"), "sidecar source URL")
    require(custody["content_length_bytes"] == custody["download_bytes"] == sidecar_path.stat().st_size, "sidecar size")
    require(custody["download_sha256"] == local_hash, "sidecar local SHA")
    require(custody["published_checksum_line"].split()[0] == local_hash, "sidecar published SHA")

    plan = json.loads((HERE / "size_sample_plan.json").read_text())
    receipts = [json.loads(line) for line in (HERE / "receipts.jsonl").read_text().splitlines()]
    summary = json.loads((HERE / "SIZE_SAMPLE_SUMMARY.json").read_text())
    require(plan["sample_count"] == len(plan["requests"]) == 1024, "sample plan count")
    require(len(receipts) == 1024, "receipt count")
    require(len({r["url"] for r in receipts}) == 1024, "sample URL uniqueness")
    require(len(set(r["aaa"] for r in receipts)) == 360, "all AAA strata represented")
    for i, receipt in enumerate(receipts):
        require(receipt["sample_index"] == i and receipt["url"] == plan["requests"][i]["url"], f"plan binding {i}")
        require(receipt["method"] == "HEAD" and receipt["body_bytes"] == 0, f"HEAD/body {i}")
        if i:
            require(receipt["request_start_epoch"] - receipts[i - 1]["request_start_epoch"] >= 1.0, f"pacing {i}")
    non_200 = sum(r["status"] != 200 for r in receipts)
    require(non_200 <= math.floor(1024 * 0.01), "non-200 threshold")
    sizes = [r["content-length"] for r in receipts if r["status"] == 200 and isinstance(r["content-length"], int)]
    require(bool(sizes), "valid size observations")
    mean = Fraction(sum(sizes), len(sizes))
    raw = mean * 60308 * Fraction(5, 4)
    ceiling = (raw.numerator + raw.denominator - 1) // raw.denominator
    require(summary["approved_byte_ceiling"] == ceiling, "ceiling arithmetic")
    require(summary["body_bytes_transferred"] == 0, "summary zero body")
    require(summary["receipts_sha256"] == digest(HERE / "receipts.jsonl"), "summary receipt pin")

    return {
        "status": "PASS",
        "coverage": {"required": count, "receipted": count, "absent": count - covered, "contradictions": count - len(urls)},
        "digest_currency": {"identified": 598, "in_ws": 397, "late": 397, "hazard": 0, "anomaly": 0, "control_clean": 59911},
        "sidecar_sha256": local_hash,
        "sample": {"requests": len(receipts), "http_200": len(receipts) - non_200, "non_200": non_200, "body_bytes": 0, "approved_byte_ceiling": ceiling},
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
