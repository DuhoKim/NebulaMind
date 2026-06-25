#!/usr/bin/env python3
"""Read-only tripwire for Evidence rows from frozen/autowiki channels."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from sqlalchemy import text

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal  # noqa: E402


WATCH_PATTERNS = (
    "arxiv_wiki_feed_%",
    "page57_broad_coverage_mine_%",
    "autowiki%",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--since-minutes", type=int, default=30)
    args = parser.parse_args()
    with SessionLocal() as db:
        rows = db.execute(
            text(
                """
                SELECT id, claim_id, arxiv_id, source_channel, created_at
                FROM evidence
                WHERE created_at >= now() - (:since_minutes * interval '1 minute')
                  AND (
                    source_channel LIKE :p0
                    OR source_channel LIKE :p1
                    OR source_channel LIKE :p2
                  )
                ORDER BY created_at DESC, id DESC
                LIMIT 50
                """
            ),
            {
                "since_minutes": args.since_minutes,
                "p0": WATCH_PATTERNS[0],
                "p1": WATCH_PATTERNS[1],
                "p2": WATCH_PATTERNS[2],
            },
        ).mappings().all()
    if rows:
        print(
            "SYSTEM_EVENT EVIDENCE_CHANNEL_TRIPWIRE_ALERT "
            + json.dumps(
                {
                    "since_minutes": args.since_minutes,
                    "count": len(rows),
                    "rows": [
                        {
                            "id": row["id"],
                            "claim_id": row["claim_id"],
                            "arxiv_id": row["arxiv_id"],
                            "source_channel": row["source_channel"],
                            "created_at": row["created_at"].isoformat(),
                        }
                        for row in rows
                    ],
                    "db_write": False,
                },
                sort_keys=True,
            )
        )
        return 2
    print(
        "SYSTEM_EVENT EVIDENCE_CHANNEL_TRIPWIRE_OK "
        + json.dumps({"since_minutes": args.since_minutes, "count": 0, "db_write": False})
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
