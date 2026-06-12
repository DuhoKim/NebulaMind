#!/usr/bin/env python3
"""Repair arXiv feed dates and refusal summaries that affect public surfaces."""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
import sys

from sqlalchemy import text

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal
from app.services.arxiv_quality import looks_like_llm_refusal, normalize_submitted_date


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    today = dt.date.today().isoformat()
    future_fixed = 0
    future_unfixable = 0
    refusals_purged = 0

    with SessionLocal() as db:
        future_rows = db.execute(
            text(
                """
                SELECT id, arxiv_id, submitted
                FROM arxiv_papers
                WHERE submitted > :today
                ORDER BY submitted DESC, arxiv_id
                """
            ),
            {"today": today},
        ).fetchall()
        for row in future_rows:
            repaired = normalize_submitted_date(row.submitted, row.arxiv_id)
            if not repaired:
                future_unfixable += 1
                print(f"unfixable_future_date arxiv_id={row.arxiv_id} submitted={row.submitted}")
                continue
            future_fixed += 1
            print(f"fix_future_date arxiv_id={row.arxiv_id} {row.submitted} -> {repaired}")
            if not args.dry_run:
                db.execute(
                    text("UPDATE arxiv_papers SET submitted = :submitted WHERE id = :id"),
                    {"id": row.id, "submitted": repaired},
                )

        summary_rows = db.execute(
            text(
                """
                SELECT id, arxiv_id, abstract, abstract_summary
                FROM arxiv_papers
                WHERE abstract_summary IS NOT NULL
                  AND abstract_summary <> ''
                ORDER BY id
                """
            )
        ).fetchall()
        for row in summary_rows:
            if not looks_like_llm_refusal(row.abstract_summary):
                continue
            fallback = (row.abstract or "")[:300]
            refusals_purged += 1
            print(f"purge_refusal_summary arxiv_id={row.arxiv_id}")
            if not args.dry_run:
                db.execute(
                    text("UPDATE arxiv_papers SET abstract_summary = :summary WHERE id = :id"),
                    {"id": row.id, "summary": fallback},
                )

        if args.dry_run:
            db.rollback()
        else:
            db.commit()

    print(
        "ARXIV_FRONTPAGE_REPAIR_COMPLETE "
        f"future_fixed={future_fixed} future_unfixable={future_unfixable} "
        f"refusals_purged={refusals_purged} dry_run={args.dry_run}"
    )
    return 0 if future_unfixable == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
