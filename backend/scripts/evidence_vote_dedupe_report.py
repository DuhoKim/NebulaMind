#!/usr/bin/env python3
"""Read-only duplicate report for future evidence_votes uniqueness migration.

Reports duplicate non-null (evidence_id, agent_id) pairs and proposes retaining
the newest row per pair by (created_at, id). This script does not delete or
update rows.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from collections import defaultdict

from sqlalchemy import text

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal


VOTE_ROWS_SQL = text("""
SELECT id, evidence_id, agent_id, created_at
FROM evidence_votes
WHERE agent_id IS NOT NULL
""")


def _newest_sort_key(row: dict) -> tuple[bool, dt.datetime, int]:
    created_at = row["created_at"]
    return (
        created_at is not None,
        created_at or dt.datetime.min,
        int(row["id"]),
    )


def build_dedupe_report(db, *, limit: int = 50) -> dict:
    grouped: dict[tuple[int, int], list[dict]] = defaultdict(list)
    for row in db.execute(VOTE_ROWS_SQL).mappings():
        grouped[(row["evidence_id"], row["agent_id"])].append(dict(row))

    duplicate_rows = []
    duplicate_pairs = 0
    extra_rows = 0
    for (evidence_id, agent_id), rows in grouped.items():
        if len(rows) <= 1:
            continue
        duplicate_pairs += 1
        extra_rows += len(rows) - 1
        ordered = sorted(rows, key=_newest_sort_key, reverse=True)
        duplicate_rows.append({
            "evidence_id": evidence_id,
            "agent_id": agent_id,
            "keep_id": ordered[0]["id"],
            "row_count": len(rows),
            "extra_rows": len(rows) - 1,
            "vote_ids": [row["id"] for row in ordered],
        })

    duplicate_rows.sort(key=lambda row: (-row["extra_rows"], row["evidence_id"], row["agent_id"]))
    return {
        "duplicate_pairs": duplicate_pairs,
        "extra_rows": extra_rows,
        "retention_policy": "keep newest row per (evidence_id, agent_id) by created_at DESC NULLS LAST, id DESC",
        "destructive_action": False,
        "sample": duplicate_rows[:max(1, limit)],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=50, help="Maximum duplicate pairs to print")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        payload = build_dedupe_report(db, limit=args.limit)
    finally:
        db.close()
    if args.json:
        print(json.dumps(payload, default=str, indent=2, sort_keys=True))
        return 0

    print(f"duplicate_pairs={payload['duplicate_pairs']} extra_rows={payload['extra_rows']}")
    print(f"retention_policy={payload['retention_policy']}")
    for row in payload["sample"]:
        print(
            "evidence_id={evidence_id} agent_id={agent_id} keep_id={keep_id} "
            "row_count={row_count} extra_rows={extra_rows} vote_ids={vote_ids}".format(**row)
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
