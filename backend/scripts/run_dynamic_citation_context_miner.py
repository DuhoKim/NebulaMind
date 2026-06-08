#!/usr/bin/env python3
"""Run Dynamic Citation Context Mining for one newly ingested paper."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.agent_loop.citation_context.dynamic_miner import (  # noqa: E402
    DCCM_MAX_CLAIMS_PER_SEED,
    DCCM_MAX_EVIDENCE_PER_CLAIM_LIFETIME,
    process_dynamic_paper,
    resolve_new_record,
)
from app.database import SessionLocal  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run DCCM for one newly ingested paper.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Classify and report without database writes.")
    mode.add_argument("--commit", action="store_true", help="Insert SUPPORTIVE evidence and recalculate trust.")
    parser.add_argument("--evidence-id", type=int, help="Existing evidence row for the new paper.")
    parser.add_argument("--bibcode", help="ADS bibcode for the new paper.")
    parser.add_argument("--doi", help="DOI for the new paper.")
    parser.add_argument("--arxiv-id", help="arXiv ID for the new paper.")
    parser.add_argument("--title", help="Title for manual/new-paper fallback.")
    parser.add_argument("--abstract", help="Abstract for manual/new-paper fallback.")
    parser.add_argument("--year", type=int, help="Publication year for manual/new-paper fallback.")
    parser.add_argument("--max-claims-per-seed", type=int, default=DCCM_MAX_CLAIMS_PER_SEED)
    parser.add_argument("--lifetime-cap", type=int, default=DCCM_MAX_EVIDENCE_PER_CLAIM_LIFETIME)
    parser.add_argument("--arxiv-intro-cap", type=int, default=5)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    db = SessionLocal()
    try:
        record = resolve_new_record(
            db,
            evidence_id=args.evidence_id,
            bibcode=args.bibcode,
            doi=args.doi,
            arxiv_id=args.arxiv_id,
            title=args.title,
            abstract=args.abstract,
            year=args.year,
        )
        report = process_dynamic_paper(
            db,
            record,
            dry_run=args.dry_run,
            max_claims_per_seed=args.max_claims_per_seed,
            lifetime_cap=args.lifetime_cap,
            arxiv_intro_cap=args.arxiv_intro_cap,
        )
        print(
            "DCCM report: "
            f"seeds={report.seed_count} references={report.references_seen} "
            f"intersections={report.intersections} contexts={report.contexts_fetched} "
            f"supportive={report.supportive} rejected={report.rejected} held={report.held} "
            f"inserted={report.inserted} capped={report.capped} "
            f"primary_floor_blocked={report.primary_floor_blocked}"
        )
        for decision in report.decisions:
            hit = decision.hit
            print(
                f"{decision.action.upper()} claim={hit.seed.claim_id} seed_ev={hit.seed.evidence_id} "
                f"seed={hit.seed.seed_bibcode or hit.seed.seed_doi} "
                f"new={hit.new_record.bibcode or hit.new_record.arxiv_id or hit.new_record.doi} "
                f"source={hit.context_source} relevance={hit.relevance_hits} "
                f"label={decision.verdict_label} confidence={decision.confidence} quality={decision.quality}"
            )
            print(f"  {hit.context_sentence[:260]}")
        for claim_id, (level, score) in sorted(report.recalculated.items()):
            print(f"RECALCULATED claim={claim_id} trust_level={level} trust_score={score:.3f}")
        return 0 if not report.errors else 1
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
