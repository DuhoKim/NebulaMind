#!/usr/bin/env python3
"""Seed CCM seminal claim mappings from data/seminal_claims.yaml.

The YAML binds directly to claim_id, but every row also carries a text_guard.
The guard is matched against claim text after stripping embedded claim markers,
so autowiki marker insertion does not look like claim drift.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal  # noqa: E402
from app.models.claim import Claim  # noqa: E402
from app.models.seminal import SeminalClaimMap  # noqa: E402


DEFAULT_SEED_PATH = BACKEND_ROOT / "data" / "seminal_claims.yaml"
MARKER_RE = re.compile(r"<!--.*?-->", re.DOTALL)
SPACE_RE = re.compile(r"\s+")


class SeedError(RuntimeError):
    pass


@dataclass(frozen=True)
class ResolvedMapping:
    row: dict[str, Any]
    text_guard: str
    claim_preview: str


@dataclass(frozen=True)
class MappingFailure:
    index: int
    claim_id: int | None
    label: str
    bibcode: str
    reason: str


def strip_claim_markers(text: str) -> str:
    """Remove embedded HTML claim/citation markers and normalize whitespace."""
    return SPACE_RE.sub(" ", MARKER_RE.sub(" ", text)).strip()


def _contains_guard(claim_text: str, text_guard: str) -> bool:
    return strip_claim_markers(text_guard) in strip_claim_markers(claim_text)


def load_seed(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if not path.exists():
        raise SeedError(f"Seed file not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise SeedError("Seed YAML must be a mapping with meta and mappings keys.")
    meta = data.get("meta") or {}
    mappings = data.get("mappings")
    if not isinstance(meta, dict):
        raise SeedError("Seed YAML meta must be a mapping.")
    if not isinstance(mappings, list):
        raise SeedError("Seed YAML mappings must be a list.")
    return meta, mappings


def _validate_entry(entry: dict[str, Any], index: int) -> None:
    required = ("claim_id", "text_guard", "label", "bibcode", "keyphrases")
    for key in required:
        if entry.get(key) in (None, ""):
            raise SeedError(f"Mapping {index} missing required key: {key}")
    if not isinstance(entry["keyphrases"], list):
        raise SeedError(f"Mapping {index} keyphrases must be a list.")


def resolve_mappings(
    db: Session,
    meta: dict[str, Any],
    mappings: list[dict[str, Any]],
    *,
    added_by: str,
) -> tuple[list[ResolvedMapping], list[MappingFailure]]:
    resolved: list[ResolvedMapping] = []
    failures: list[MappingFailure] = []
    seen: set[tuple[int, str]] = set()
    expected_page_id = meta.get("page_id")
    expected_section = meta.get("section")

    for index, entry in enumerate(mappings, start=1):
        _validate_entry(entry, index)
        claim_id = int(entry["claim_id"])
        bibcode = str(entry["bibcode"]).strip()
        label = str(entry["label"]).strip()
        text_guard = str(entry["text_guard"]).strip()

        claim = db.get(Claim, claim_id)
        if not claim:
            failures.append(MappingFailure(index, claim_id, label, bibcode, "claim_id not found"))
            continue
        if expected_page_id is not None and claim.page_id != int(expected_page_id):
            failures.append(
                MappingFailure(index, claim_id, label, bibcode, f"page_id {claim.page_id} != {expected_page_id}")
            )
            continue
        if expected_section and claim.section != expected_section:
            failures.append(
                MappingFailure(index, claim_id, label, bibcode, f"section {claim.section!r} != {expected_section!r}")
            )
            continue
        if not _contains_guard(claim.text, text_guard):
            failures.append(MappingFailure(index, claim_id, label, bibcode, "text_guard not found after marker stripping"))
            continue

        key = (claim_id, bibcode)
        if key in seen:
            failures.append(MappingFailure(index, claim_id, label, bibcode, "duplicate claim_id/bibcode in seed file"))
            continue
        seen.add(key)

        resolved.append(
            ResolvedMapping(
                row={
                    "claim_id": claim_id,
                    "canonical_bibcode": bibcode,
                    "canonical_label": label,
                    "canonical_doi": entry.get("doi"),
                    "canonical_arxiv_id": entry.get("arxiv_id"),
                    "topic_keyphrases": json.dumps(entry["keyphrases"], ensure_ascii=True),
                    "enabled": bool(entry.get("enabled", True)),
                    "added_by": entry.get("added_by") or added_by,
                    "notes": entry.get("notes"),
                },
                text_guard=text_guard,
                claim_preview=strip_claim_markers(claim.text)[:180],
            )
        )

    return resolved, failures


def upsert_rows(db: Session, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    stmt = pg_insert(SeminalClaimMap).values(rows)
    db.execute(
        stmt.on_conflict_do_update(
            constraint="uq_seminal_claim_map_claim_bibcode",
            set_={
                "canonical_label": stmt.excluded.canonical_label,
                "canonical_doi": stmt.excluded.canonical_doi,
                "canonical_arxiv_id": stmt.excluded.canonical_arxiv_id,
                "topic_keyphrases": stmt.excluded.topic_keyphrases,
                "enabled": stmt.excluded.enabled,
                "added_by": stmt.excluded.added_by,
                "notes": stmt.excluded.notes,
                "updated_at": func.now(),
            },
        )
    )


def print_report(resolved: list[ResolvedMapping], failures: list[MappingFailure]) -> None:
    print(f"Resolved mappings: {len(resolved)}")
    for item in resolved:
        row = item.row
        print(
            f"  OK claim_id={row['claim_id']} bibcode={row['canonical_bibcode']} "
            f"label={row['canonical_label']!r}"
        )
    if failures:
        print(f"Failures: {len(failures)}")
        for failure in failures:
            print(
                f"  FAIL #{failure.index} claim_id={failure.claim_id} "
                f"bibcode={failure.bibcode} label={failure.label!r}: {failure.reason}"
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Seed CCM seminal_claim_map from authoritative YAML.")
    parser.add_argument("--seed-file", type=Path, default=DEFAULT_SEED_PATH)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Validate and report without writing.")
    mode.add_argument("--commit", action="store_true", help="Validate and upsert rows.")
    parser.add_argument("--added-by", default="kun_audit")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    meta, mappings = load_seed(args.seed_file)
    db = SessionLocal()
    try:
        resolved, failures = resolve_mappings(db, meta, mappings, added_by=args.added_by)
        print_report(resolved, failures)
        if failures:
            db.rollback()
            return 1
        if args.dry_run:
            print("Dry run only; no database writes performed.")
            return 0
        upsert_rows(db, [item.row for item in resolved])
        db.commit()
        print(f"Committed {len(resolved)} seminal_claim_map row(s).")
        return 0
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
