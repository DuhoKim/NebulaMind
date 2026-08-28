#!/usr/bin/env python3
"""Build a deterministic pass-4 A3.8 unblock-contract coverage scan."""

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
OUT = Path(__file__).with_name("pass4_unblock_contract_scan.json")
T4_NAME = "T4_PAIRED_FLIP.json"
T4_SHA256 = "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873"
A38_NAME_PATTERN = re.compile(r"A3\.8", re.IGNORECASE)
A38_SHA256 = "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0"


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def file_format(raw: bytes) -> str:
    if raw.startswith(b"\x1f\x8b"):
        return "gzip"
    if raw.startswith(b"%PDF-"):
        return "pdf"
    return "other-binary"


def marker_row(path: Path, text: str, t4_mtime_ns: int) -> dict[str, object]:
    return {
        "path": path.relative_to(SOURCE).as_posix(),
        "sha256": sha256_bytes(path.read_bytes()),
        "bytes": path.stat().st_size,
        "mtime_ns": path.stat().st_mtime_ns,
        "mtime_utc": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
        "post_t4_by_mtime": path.stat().st_mtime_ns > t4_mtime_ns,
        "markers": {
            "t4_exact_filename": T4_NAME in text,
            "t4_exact_sha256": T4_SHA256 in text,
            "a3_8_name": bool(A38_NAME_PATTERN.search(text)),
            "a3_8_exact_sha256": A38_SHA256 in text,
            "first_opened_ledger": bool(
                re.search(r"first[- ]opened\s+ledger", text, re.IGNORECASE)
            ),
            "independent_verdict_review": bool(
                re.search(r"independent\s+verdict\s+review", text, re.IGNORECASE)
            ),
            "independent_branch": bool(
                re.search(r"independent\s+branch", text, re.IGNORECASE)
            ),
            "review_incomplete": "REVIEW_INCOMPLETE" in text,
            "verbatim_requirement": bool(
                re.search(r"\bverbatim\b", text, re.IGNORECASE)
            ),
            "review_or_verdict_language": bool(
                re.search(r"\b(?:review|verdict)\b", text, re.IGNORECASE)
            ),
            "independent_language": bool(
                re.search(r"\bindependent\b", text, re.IGNORECASE)
            ),
        },
    }


def main() -> None:
    t4 = SOURCE / T4_NAME
    t4_mtime_ns = t4.stat().st_mtime_ns
    regular_files = sorted(
        path for path in SOURCE.rglob("*") if path.is_file() and not path.is_symlink()
    )
    text_rows = []
    binary_rows = []
    for path in regular_files:
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            binary_rows.append(
                {
                    "path": path.relative_to(SOURCE).as_posix(),
                    "sha256": sha256_bytes(raw),
                    "bytes": len(raw),
                    "format": file_format(raw),
                    "mtime_ns": path.stat().st_mtime_ns,
                    "mtime_utc": datetime.fromtimestamp(
                        path.stat().st_mtime, timezone.utc
                    ).isoformat(),
                    "post_t4_by_mtime": path.stat().st_mtime_ns > t4_mtime_ns,
                }
            )
            continue
        text_rows.append(marker_row(path, text, t4_mtime_ns))

    post_t4_text = [row for row in text_rows if row["post_t4_by_mtime"]]
    t4_identifying = [
        row
        for row in post_t4_text
        if row["markers"]["t4_exact_filename"]
        or row["markers"]["t4_exact_sha256"]
    ]
    exact_hash_pair = [
        row
        for row in post_t4_text
        if row["markers"]["t4_exact_sha256"]
        and row["markers"]["a3_8_exact_sha256"]
    ]
    complete_marker_candidates = [
        row
        for row in post_t4_text
        if row["markers"]["t4_exact_sha256"]
        and row["markers"]["a3_8_exact_sha256"]
        and row["markers"]["first_opened_ledger"]
        and row["markers"]["independent_language"]
        and row["markers"]["review_or_verdict_language"]
    ]
    output = {
        "status": "DETERMINISTIC_A3_8_UNBLOCK_CONTRACT_SCAN",
        "scope": str(SOURCE),
        "t4_path": str(t4),
        "t4_sha256": T4_SHA256,
        "t4_mtime_ns": t4_mtime_ns,
        "a3_8_sha256": A38_SHA256,
        "regular_file_count": len(regular_files),
        "utf8_decodable_count": len(text_rows),
        "non_utf8_count": len(binary_rows),
        "post_t4_utf8_count": len(post_t4_text),
        "post_t4_non_utf8_count": sum(row["post_t4_by_mtime"] for row in binary_rows),
        "non_utf8_files": binary_rows,
        "all_non_utf8_files_predate_t4": all(
            not row["post_t4_by_mtime"] for row in binary_rows
        ),
        "post_t4_t4_identifier_count": len(t4_identifying),
        "post_t4_t4_identifier_rows": t4_identifying,
        "post_t4_exact_t4_and_a3_8_hash_pair_count": len(exact_hash_pair),
        "post_t4_exact_t4_and_a3_8_hash_pair_paths": [
            row["path"] for row in exact_hash_pair
        ],
        "post_t4_complete_minimum_marker_candidate_count": len(
            complete_marker_candidates
        ),
        "post_t4_complete_minimum_marker_candidate_paths": [
            row["path"] for row in complete_marker_candidates
        ],
        "post_t4_utf8_rows": post_t4_text,
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(
        "PASS "
        f"files={len(regular_files)} post_t4_utf8={len(post_t4_text)} "
        f"post_t4_binary={output['post_t4_non_utf8_count']} "
        f"t4_identifiers={len(t4_identifying)} exact_hash_pairs={len(exact_hash_pair)} "
        f"complete_candidates={len(complete_marker_candidates)}"
    )


if __name__ == "__main__":
    main()
