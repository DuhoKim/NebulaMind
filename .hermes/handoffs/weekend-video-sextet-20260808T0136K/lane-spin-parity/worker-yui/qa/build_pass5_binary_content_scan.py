#!/usr/bin/env python3
"""Decode and marker-scan all six non-UTF-8 source files for pass 5."""

from __future__ import annotations

import gzip
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

SOURCE = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "spin-parity-census-20260805T1922K"
)
OUT = Path(__file__).with_name("pass5_binary_content_scan.json")
T4_NAME = "T4_PAIRED_FLIP.json"
T4_SHA256 = "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873"
A38_SHA256 = "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0"


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def marker_counts(text: str) -> dict[str, int]:
    return {
        "t4_exact_filename": text.count(T4_NAME),
        "t4_exact_sha256": text.count(T4_SHA256),
        "a3_8_name": len(re.findall(r"A3\.8", text, re.IGNORECASE)),
        "a3_8_exact_sha256": text.count(A38_SHA256),
        "first_opened_ledger": len(
            re.findall(r"first[- ]opened\s+ledger", text, re.IGNORECASE)
        ),
        "independent_verdict_review": len(
            re.findall(r"independent\s+verdict\s+review", text, re.IGNORECASE)
        ),
    }


def decode_binary(path: Path, raw: bytes) -> tuple[str, bytes, str]:
    if raw.startswith(b"\x1f\x8b"):
        payload = gzip.decompress(raw)
        return "gzip", payload, payload.decode("utf-8", errors="replace")
    if raw.startswith(b"%PDF-"):
        result = subprocess.run(
            ["pdftotext", str(path), "-"],
            check=True,
            text=False,
            capture_output=True,
        )
        payload = result.stdout
        return "pdf", payload, payload.decode("utf-8", errors="replace")
    raise SystemExit(f"unexpected binary format: {path}")


def main() -> None:
    rows: list[dict[str, Any]] = []
    regular = sorted(
        path for path in SOURCE.rglob("*") if path.is_file() and not path.is_symlink()
    )
    for path in regular:
        raw = path.read_bytes()
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError:
            file_format, decoded, text = decode_binary(path, raw)
            rows.append(
                {
                    "path": path.relative_to(SOURCE).as_posix(),
                    "format": file_format,
                    "source_bytes": len(raw),
                    "source_sha256": sha256_bytes(raw),
                    "decoded_bytes": len(decoded),
                    "decoded_sha256": sha256_bytes(decoded),
                    "replacement_character_count": text.count("\ufffd"),
                    "markers": marker_counts(text),
                }
            )
    exact_hash_pair_rows = [
        row
        for row in rows
        if row["markers"]["t4_exact_sha256"]
        and row["markers"]["a3_8_exact_sha256"]
    ]
    any_identity_rows = [
        row
        for row in rows
        if row["markers"]["t4_exact_filename"]
        or row["markers"]["t4_exact_sha256"]
        or row["markers"]["a3_8_name"]
        or row["markers"]["a3_8_exact_sha256"]
    ]
    output = {
        "status": "DETERMINISTIC_NON_UTF8_CONTENT_MARKER_SCAN",
        "scope": str(SOURCE),
        "regular_file_count": len(regular),
        "non_utf8_file_count": len(rows),
        "gzip_file_count": sum(row["format"] == "gzip" for row in rows),
        "pdf_file_count": sum(row["format"] == "pdf" for row in rows),
        "decoder": {
            "gzip": "Python gzip.decompress",
            "pdf": subprocess.run(
                ["pdftotext", "-v"], check=True, text=True, capture_output=True
            ).stderr.splitlines()[0],
        },
        "raw_content_not_reproduced": True,
        "files": rows,
        "files_with_any_t4_or_a3_8_identity_marker": len(any_identity_rows),
        "identity_marker_paths": [row["path"] for row in any_identity_rows],
        "files_with_exact_t4_and_a3_8_hash_pair": len(exact_hash_pair_rows),
        "exact_hash_pair_paths": [row["path"] for row in exact_hash_pair_rows],
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(
        f"PASS files={len(rows)} gzip={output['gzip_file_count']} "
        f"pdf={output['pdf_file_count']} identity_markers="
        f"{output['files_with_any_t4_or_a3_8_identity_marker']} "
        f"exact_hash_pairs={output['files_with_exact_t4_and_a3_8_hash_pair']}"
    )


if __name__ == "__main__":
    main()
