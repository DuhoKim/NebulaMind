#!/usr/bin/env python3
"""Seed CCM seminal claim mappings from backend/data/seminal_claims.yaml."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml
from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal  # noqa: E402
from app.models.claim import Claim  # noqa: E402
from app.models.page import WikiPage  # noqa: E402
from app.models.seminal import SeminalClaimMap  # noqa: E402
from app.services.paper_search import PaperSearchError, ads_search  # noqa: E402


DEFAULT_SEED_PATH = BACKEND_ROOT / "data" / "seminal_claims.yaml"


class SeedError(RuntimeError):
    pass


def load_seed(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise SeedError(f"Seed file not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or []
    if not isinstance(data, list):
        raise SeedError("Seed YAML must be a list of mappings.")
    for idx, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise SeedError(f"Entry {idx} must be a mapping.")
        for key in ("label", "bibcode", "match_claims"):
            if not item.get(key):
                raise SeedError(f"Entry {idx} missing required key: {key}")
        if not isinstance(item["match_claims"], list):
            raise SeedError(f"Entry {idx} match_claims must be a list.")
    return data


def resolve_claim_ids(db: Session, match: dict[str, Any], *, allow_ambiguous: bool = False) -> list[int]:
    if "claim_id" in match:
        claim = db.get(Claim, int(match["claim_id"]))
        if not claim:
            raise SeedError(f"claim_id={match['claim_id']} was not found.")
        return [claim.id]

    page_slug = match.get("page_slug")
    text_contains = match.get("text_contains")
    if not page_slug or not text_contains:
        raise SeedError("Each match must include claim_id or both page_slug and text_contains.")

    stmt = (
        select(Claim.id)
        .join(WikiPage, Claim.page_id == WikiPage.id)
        .where(WikiPage.slug == page_slug)
        .where(Claim.text.ilike(f"%{text_contains}%"))
        .order_by(Claim.id)
    )
    claim_ids = list(db.scalars(stmt))
    if not claim_ids:
        raise SeedError(f"No claim matched page_slug={page_slug!r}, text_contains={text_contains!r}.")
    if len(claim_ids) > 1 and not allow_ambiguous:
        raise SeedError(
            f"Ambiguous match page_slug={page_slug!r}, text_contains={text_contains!r}: "
            f"{claim_ids}. Add claim_id or pass --allow-ambiguous."
        )
    return claim_ids


def validate_bibcode(bibcode: str) -> None:
    try:
        records = ads_search(f'bibcode:"{bibcode}"', rows=1, sort="date desc", fq=None)
    except PaperSearchError as exc:
        raise SeedError(f"ADS validation failed for {bibcode}: {exc}") from exc
    if not records or records[0].bibcode != bibcode:
        raise SeedError(f"ADS validation did not find exact bibcode: {bibcode}")


def build_rows(
    db: Session,
    seed_entries: list[dict[str, Any]],
    *,
    added_by: str,
    allow_ambiguous: bool,
    validate_ads: bool,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[tuple[int, str]] = set()
    for entry in seed_entries:
        bibcode = str(entry["bibcode"]).strip()
        if validate_ads:
            validate_bibcode(bibcode)

        keyphrases = entry.get("keyphrases")
        topic_keyphrases = json.dumps(keyphrases, ensure_ascii=True) if keyphrases is not None else None
        for match in entry["match_claims"]:
            for claim_id in resolve_claim_ids(db, match, allow_ambiguous=allow_ambiguous):
                key = (claim_id, bibcode)
                if key in seen:
                    continue
                seen.add(key)
                rows.append(
                    {
                        "claim_id": claim_id,
                        "canonical_bibcode": bibcode,
                        "canonical_label": str(entry["label"]).strip(),
                        "canonical_doi": entry.get("doi"),
                        "canonical_arxiv_id": entry.get("arxiv_id"),
                        "topic_keyphrases": topic_keyphrases,
                        "enabled": bool(entry.get("enabled", True)),
                        "added_by": entry.get("added_by") or added_by,
                        "notes": entry.get("notes"),
                    }
                )
    return rows


def upsert_rows(db: Session, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    stmt = pg_insert(SeminalClaimMap).values(rows)
    update_cols = {
        "canonical_label": stmt.excluded.canonical_label,
        "canonical_doi": stmt.excluded.canonical_doi,
        "canonical_arxiv_id": stmt.excluded.canonical_arxiv_id,
        "topic_keyphrases": stmt.excluded.topic_keyphrases,
        "enabled": stmt.excluded.enabled,
        "added_by": stmt.excluded.added_by,
        "notes": stmt.excluded.notes,
        "updated_at": func.now(),
    }
    db.execute(
        stmt.on_conflict_do_update(
            constraint="uq_seminal_claim_map_claim_bibcode",
            set_=update_cols,
        )
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Seed CCM seminal_claim_map from YAML.")
    parser.add_argument("--seed-file", type=Path, default=DEFAULT_SEED_PATH)
    parser.add_argument("--dry-run", action="store_true", help="Resolve and print rows without writing.")
    parser.add_argument("--validate-ads", action="store_true", help="Require each bibcode to resolve in ADS.")
    parser.add_argument("--allow-ambiguous", action="store_true", help="Allow one matcher to map to multiple claims.")
    parser.add_argument("--added-by", default="kun_audit")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    entries = load_seed(args.seed_file)
    db = SessionLocal()
    try:
        rows = build_rows(
            db,
            entries,
            added_by=args.added_by,
            allow_ambiguous=args.allow_ambiguous,
            validate_ads=args.validate_ads,
        )
        print(json.dumps(rows, indent=2, sort_keys=True))
        if args.dry_run:
            print(f"Dry run: resolved {len(rows)} seminal mapping row(s).")
            return
        upsert_rows(db, rows)
        db.commit()
        print(f"Seeded {len(rows)} seminal mapping row(s).")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
