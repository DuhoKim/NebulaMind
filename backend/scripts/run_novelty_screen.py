#!/usr/bin/env python3
"""Run the research-idea novelty coverage screen backfill."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal
from app.utils.novelty_screen import persist_screen_result, run_calibration, screen_idea, unscreened_query
from sqlalchemy import text


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("run_novelty_screen")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--limit", type=int, default=0, help="Optional max ideas after calibration")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    processed = 0
    with SessionLocal() as db:
        calibration = run_calibration(db)
        log.info("CALIBRATION_RESULT %s", json.dumps(calibration, sort_keys=True))
        if not calibration["passed"]:
            log.error("Calibration failed; aborting unscreened backfill")
            return 2

        while True:
            remaining = args.limit - processed if args.limit else args.batch_size
            if remaining <= 0:
                break
            batch_size = min(args.batch_size, remaining)
            query, params = unscreened_query(batch_size)
            rows = db.execute(text(query), params).fetchall()
            if not rows:
                break

            for row in rows:
                result = screen_idea(row, db)
                log.info("idea %s => %s papers=%s", row.id, result.coverage_status, result.papers_checked)
                if not args.dry_run:
                    persist_screen_result(db, result)
                    db.commit()
                processed += 1
                if args.limit and processed >= args.limit:
                    break

    log.info("NOVELTY_SCREEN_COMPLETE processed=%s", processed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
