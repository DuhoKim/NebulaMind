#!/usr/bin/env python3
"""Run Citation Context Mining over enabled seminal_claim_map rows."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.agent_loop.citation_context.miner import DEFAULT_MIN_YEAR, run_ccm_cycle  # noqa: E402
from app.database import SessionLocal  # noqa: E402


def _csv_ints(raw: str | None) -> list[int] | None:
    if not raw:
        return None
    return [int(part.strip()) for part in raw.split(",") if part.strip()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the CCM citation context miner.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Classify and report without database writes.")
    mode.add_argument("--commit", action="store_true", help="Insert SUPPORTIVE evidence and recalculate trust.")
    parser.add_argument("--map-ids", help="Comma-separated seminal_claim_map IDs.")
    parser.add_argument("--claim-ids", help="Comma-separated claim IDs.")
    parser.add_argument("--min-year", type=int, default=DEFAULT_MIN_YEAR)
    parser.add_argument("--max-maps", type=int, default=16)
    parser.add_argument("--ads-rows", type=int, default=200)
    parser.add_argument("--max-candidates-per-map", type=int, default=20)
    parser.add_argument("--max-evidence-per-claim", type=int, default=6)
    parser.add_argument("--arxiv-intro-cap", type=int, default=5)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    db = SessionLocal()
    try:
        report = run_ccm_cycle(
            db,
            dry_run=args.dry_run,
            map_ids=_csv_ints(args.map_ids),
            claim_ids=_csv_ints(args.claim_ids),
            min_year=args.min_year,
            max_maps=args.max_maps,
            ads_rows=args.ads_rows,
            max_candidates_per_map=args.max_candidates_per_map,
            max_evidence_per_claim=args.max_evidence_per_claim,
            arxiv_intro_cap=args.arxiv_intro_cap,
        )
        print(
            "CCM report: "
            f"maps={report.maps_seen} ads_citers={report.ads_citers_seen} "
            f"contexts={report.contexts_fetched} supportive={report.supportive} "
            f"rejected={report.rejected} held={report.held} inserted={report.inserted}"
        )
        for decision in report.decisions:
            ctx = decision.context
            verdict = decision.verdict
            print(
                f"{decision.action.upper()} claim={ctx.claim_id} seminal={ctx.seminal_bibcode} "
                f"citer={ctx.citing_bibcode or ctx.citing_arxiv_id or ctx.citing_doi} "
                f"source={ctx.context_source} hits={ctx.keyphrase_hits} "
                f"label={verdict.label} confidence={verdict.confidence}"
            )
            print(f"  {ctx.context_sentence[:260]}")
        for claim_id, (level, score) in sorted(report.recalculated.items()):
            print(f"RECALCULATED claim={claim_id} trust_level={level} trust_score={score:.3f}")
        if report.errors:
            print("Errors:")
            for error in report.errors:
                print(f"  {error}")
        return 0 if not report.errors else 1
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
