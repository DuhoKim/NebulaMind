#!/usr/bin/env python3
"""Build a deterministic recursive inventory for the pass-3 blocker absence proof."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "spin-parity-census-20260805T1922K"
)
OUT = Path(__file__).with_name("pass3_source_inventory.json")
T4_NAME = "T4_PAIRED_FLIP.json"
T4_SHA256 = "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873"
A38_SHA256 = "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    t4 = SOURCE / T4_NAME
    t4_mtime_ns = t4.stat().st_mtime_ns
    symlinks = sorted(
        path.relative_to(SOURCE).as_posix()
        for path in SOURCE.rglob("*")
        if path.is_symlink()
    )
    rows = []
    for path in sorted(
        path for path in SOURCE.rglob("*") if path.is_file() and not path.is_symlink()
    ):
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
            utf8_decodable = True
        except UnicodeDecodeError:
            text = ""
            utf8_decodable = False
        exact_t4_mentions = text.count(T4_NAME)
        t4_sha_mentions = text.count(T4_SHA256)
        a3_8_mentions = len(re.findall(r"A3\.8", text, re.IGNORECASE))
        a3_8_sha_mentions = text.count(A38_SHA256)
        independent_mentions = len(re.findall(r"\bindependent\b", text, re.IGNORECASE))
        review_or_verdict_mentions = len(
            re.findall(r"\b(?:review|verdict)\b", text, re.IGNORECASE)
        )
        post_t4 = path.stat().st_mtime_ns > t4_mtime_ns
        rows.append(
            {
                "path": path.relative_to(SOURCE).as_posix(),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
                "mtime_ns": path.stat().st_mtime_ns,
                "mtime_utc": datetime.fromtimestamp(
                    path.stat().st_mtime, timezone.utc
                ).isoformat(),
                "utf8_decodable": utf8_decodable,
                "filename_contains_verdict_casefold": "verdict" in path.name.casefold(),
                "predates_t4": path.stat().st_mtime_ns < t4_mtime_ns,
                "post_t4": post_t4,
                "exact_t4_name_mentions": exact_t4_mentions,
                "t4_sha256_mentions": t4_sha_mentions,
                "a3_8_mentions": a3_8_mentions,
                "a3_8_sha256_mentions": a3_8_sha_mentions,
                "independent_mentions": independent_mentions,
                "review_or_verdict_mentions": review_or_verdict_mentions,
                "post_t4_candidate_review_record": bool(
                    post_t4
                    and (exact_t4_mentions or t4_sha_mentions)
                    and (a3_8_mentions or a3_8_sha_mentions)
                    and independent_mentions
                    and review_or_verdict_mentions
                ),
            }
        )

    verdict_rows = [row for row in rows if row["filename_contains_verdict_casefold"]]
    post_t4_t4_rows = [
        row
        for row in rows
        if row["post_t4"]
        and (row["exact_t4_name_mentions"] or row["t4_sha256_mentions"])
    ]
    candidate_rows = [row for row in rows if row["post_t4_candidate_review_record"]]
    rows_sha = hashlib.sha256(
        json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    receipt = {
        "status": "DETERMINISTIC_RECURSIVE_SOURCE_INVENTORY",
        "scope": str(SOURCE),
        "t4_path": str(t4),
        "t4_sha256": sha256(t4),
        "t4_mtime_ns": t4_mtime_ns,
        "regular_file_count": len(rows),
        "utf8_decodable_count": sum(row["utf8_decodable"] for row in rows),
        "non_utf8_count": sum(not row["utf8_decodable"] for row in rows),
        "symlink_count": len(symlinks),
        "symlinks_skipped": symlinks,
        "casefold_verdict_filename_count": len(verdict_rows),
        "casefold_verdict_filename_paths": [row["path"] for row in verdict_rows],
        "all_verdict_filename_files_predate_t4": all(
            row["predates_t4"] for row in verdict_rows
        ),
        "post_t4_utf8_files_identifying_t4_by_name_or_hash_count": len(post_t4_t4_rows),
        "post_t4_utf8_files_identifying_t4_by_name_or_hash": [
            {
                "path": row["path"],
                "sha256": row["sha256"],
                "t4_name_mentions": row["exact_t4_name_mentions"],
                "t4_sha256_mentions": row["t4_sha256_mentions"],
                "a3_8_mentions": row["a3_8_mentions"],
                "a3_8_sha256_mentions": row["a3_8_sha256_mentions"],
            }
            for row in post_t4_t4_rows
        ],
        "post_t4_candidate_review_record_count": len(candidate_rows),
        "post_t4_candidate_review_records": [row["path"] for row in candidate_rows],
        "inventory_rows_sha256": rows_sha,
        "rows": rows,
    }
    OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(
        "PASS "
        f"files={len(rows)} utf8={receipt['utf8_decodable_count']} "
        f"verdict_names={len(verdict_rows)} t4_mentions={len(post_t4_t4_rows)} "
        f"candidate_records={len(candidate_rows)} rows_sha={rows_sha}"
    )


if __name__ == "__main__":
    main()
