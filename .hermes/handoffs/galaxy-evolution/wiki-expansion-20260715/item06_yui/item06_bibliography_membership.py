#!/usr/bin/env python3
"""Reconcile item-06 raw source rows against the pinned review bibliography.

This is a deterministic local-only custody tool. It does not call network services.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any


ROW_RE = re.compile(r"^\[(REV06-P\d{3})\]\t(.+)$", re.MULTILINE)
ROW_FIELDS_RE = re.compile(
    r"^(.*?) \((\d{4}), ([^)]+)\) \| title=(.*?) \| "
    r"DOI:([^;]+); arXiv:([^;]+); ADS:([^ |]+) \| "
    r"role=([^ |]+) \| review_locator=([^|]+) \| (.*)$"
)
YEAR_RE = re.compile(r"\b(?:19|20)\d{2}[a-z]?\b")
PAGE_RE = re.compile(r"^=== PDF PAGE \d+ ===$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", ascii_value.lower())


def parse_raw_rows(raw_text: str) -> dict[str, dict[str, Any]]:
    harvest_start = raw_text.index("6. Primary-Citation Harvest")
    harvest_end = raw_text.index("7. DO_NOT_USE_UNVERIFIED", harvest_start)
    harvest = raw_text[harvest_start:harvest_end]
    rows: dict[str, dict[str, Any]] = {}
    for key, row_text in ROW_RE.findall(harvest):
        match = ROW_FIELDS_RE.match(row_text)
        if match is None:
            raise ValueError(f"Malformed physical source row: {key}")
        rows[key] = {
            "author": match[1],
            "year": int(match[2]),
            "journal": match[3],
            "title": match[4],
            "doi": match[5],
            "arxiv": match[6],
            "ads": match[7],
            "role": match[8],
            "review_locator": match[9].strip(),
            "boundary": match[10],
        }
    return rows


def parse_bibliography_entries(bibliography_text: str) -> list[str]:
    entries: list[str] = []
    for raw_line in bibliography_text.splitlines():
        line = raw_line.strip()
        if (
            not line
            or line == "Literature Cited"
            or PAGE_RE.match(line)
            or line.isdigit()
        ):
            continue
        starts_entry = bool(YEAR_RE.search(line)) and line[0].isupper()
        if starts_entry:
            entries.append(line)
        elif entries:
            entries[-1] += " " + line
    return entries


def ads_volume_page(bibcode: str) -> tuple[str, str, str]:
    if len(bibcode) != 19:
        raise ValueError(f"Unexpected ADS bibcode length: {bibcode}")
    volume = bibcode[9:13].replace(".", "")
    qualifier = bibcode[13].replace(".", "")
    page = bibcode[14:18].replace(".", "")
    if volume.isdigit():
        volume = str(int(volume))
    if page.isdigit():
        page = str(int(page))
    return volume, qualifier, page


def candidate_entries(
    row: dict[str, Any], bibliography_entries: list[str]
) -> list[str]:
    surname = normalize(row["author"].split(",", 1)[0])
    year = str(row["year"])
    return [
        entry
        for entry in bibliography_entries
        if normalize(entry).startswith(surname)
        and re.search(rf"\b{re.escape(year)}[a-z]?\b", entry)
    ]


def exact_entries(row: dict[str, Any], candidates: list[str]) -> list[str]:
    volume, qualifier, page = ads_volume_page(row["ads"])
    exact: list[str] = []
    for entry in candidates:
        # The review's compact reference style often omits ADS qualifiers such as
        # ``L`` (ApJ Letters) and ``A`` (A&A article number) before the page.
        page_prefix = f"(?:{re.escape(qualifier)})?" if qualifier else ""
        volume_page_match = bool(
            volume
            and page
            and re.search(
                rf"\b{re.escape(volume)}\s*:\s*{page_prefix}{re.escape(page)}\b",
                entry,
            )
        )
        arxiv_match = row["arxiv"].lower() != "none" and row["arxiv"] in entry
        if volume_page_match or arxiv_match:
            exact.append(entry)
    return exact


def build_report(raw_path: Path, bibliography_path: Path) -> dict[str, Any]:
    raw_text = raw_path.read_text(encoding="utf-8")
    bibliography_text = bibliography_path.read_text(encoding="utf-8")
    rows = parse_raw_rows(raw_text)
    bibliography_entries = parse_bibliography_entries(bibliography_text)

    results: list[dict[str, Any]] = []
    for key, row in rows.items():
        candidates = candidate_entries(row, bibliography_entries)
        exact = exact_entries(row, candidates)
        if len(exact) == 1:
            status = "EXACT_BIBLIOGRAPHY_MEMBER"
        elif len(exact) > 1:
            status = "AMBIGUOUS_EXACT_MATCH"
        elif candidates:
            status = "SURNAME_YEAR_PRESENT_BUT_COMPOSITE_MISMATCH"
        else:
            status = "NOT_FOUND_IN_REVIEW_BIBLIOGRAPHY"
        volume, qualifier, page = ads_volume_page(row["ads"])
        results.append(
            {
                "key": key,
                "status": status,
                "raw_identity": {
                    "author": row["author"],
                    "year": row["year"],
                    "journal": row["journal"],
                    "title": row["title"],
                    "doi": row["doi"],
                    "arxiv": row["arxiv"],
                    "ads": row["ads"],
                    "ads_volume": volume,
                    "ads_qualifier": qualifier,
                    "ads_page": page,
                    "role": row["role"],
                },
                "exact_bibliography_entries": exact,
                "surname_year_candidates": candidates,
            }
        )

    statuses = sorted({result["status"] for result in results})
    return {
        "schema_version": 1,
        "status": "DETERMINISTIC_BIBLIOGRAPHY_MEMBERSHIP_SCAN",
        "inputs": {
            "raw_packet": str(raw_path),
            "raw_packet_sha256": sha256(raw_path),
            "bibliography": str(bibliography_path),
            "bibliography_sha256": sha256(bibliography_path),
        },
        "bibliography_logical_entry_count": len(bibliography_entries),
        "physical_source_row_count": len(rows),
        "status_counts": {
            status: sum(result["status"] == status for result in results)
            for status in statuses
        },
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--bibliography", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = build_report(args.raw, args.bibliography)
    encoded = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
