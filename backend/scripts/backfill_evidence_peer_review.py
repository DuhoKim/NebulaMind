#!/usr/bin/env python3
"""Resolve Evidence arXiv IDs to refereed ADS records.

Read-only by default. Use --commit to fill DOI/journal_ref and mark
peer_reviewed=true when ADS returns a refereed record for the arXiv ID.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.config import settings
from app.database import SessionLocal
from app.models.agent import Agent  # noqa: F401 - ensure Evidence FK target is registered
from app.models.claim import Claim, Evidence
from app.services.paper_search import PaperSearchError, ads_search


def _resolve_refereed_arxiv(arxiv_id: str):
    clean = arxiv_id.replace("arXiv:", "").strip()
    clean = re.sub(r"v\d+$", "", clean)
    try:
        records = ads_search(
            f'identifier:"{clean}" AND property:refereed',
            rows=1,
            sort="date desc",
            fq="database:astronomy",
        )
    except PaperSearchError as exc:
        print(f"[peer_review] ADS failed arxiv={clean}: {exc}")
        return None
    return records[0] if records else None


def _candidate_query(db, args):
    query = db.query(Evidence).join(Claim, Claim.id == Evidence.claim_id)
    if args.evidence_id:
        query = query.filter(Evidence.id.in_(args.evidence_id))
    if args.claim_id:
        query = query.filter(Evidence.claim_id.in_(args.claim_id))
    if args.page_id is not None:
        query = query.filter(Claim.page_id == args.page_id)
    if not args.include_resolved:
        query = query.filter(
            (Evidence.peer_reviewed.is_(False))
            | (Evidence.doi.is_(None))
            | (Evidence.journal_ref.is_(None))
        )
    query = query.filter(Evidence.arxiv_id.isnot(None))
    query = query.order_by(Evidence.id)
    if args.limit:
        query = query.limit(args.limit)
    return query


def run(args) -> dict:
    if not settings.ADS_API_KEY:
        raise SystemExit("ADS_API_KEY is not configured")

    totals = {"checked": 0, "resolved": 0, "updated": 0, "unresolved": 0}
    db = SessionLocal()
    try:
        rows = list(_candidate_query(db, args).all())
        print(json.dumps({"candidates": len(rows), "commit": args.commit}, indent=2))
        for ev in rows:
            totals["checked"] += 1
            rec = _resolve_refereed_arxiv(ev.arxiv_id or "")
            if not rec:
                totals["unresolved"] += 1
                print(f"evidence {ev.id}: arxiv={ev.arxiv_id} unresolved")
                continue

            totals["resolved"] += 1
            new_doi = ev.doi or rec.doi
            new_journal_ref = ev.journal_ref or rec.venue
            should_update = (ev.doi != new_doi) or (ev.journal_ref != new_journal_ref) or not ev.peer_reviewed
            print(
                "evidence {id}: arxiv={arxiv} refereed doi={doi} journal_ref={journal} update={update}".format(
                    id=ev.id,
                    arxiv=ev.arxiv_id,
                    doi=new_doi or "",
                    journal=new_journal_ref or "",
                    update=should_update,
                )
            )
            if args.commit and should_update:
                ev.doi = new_doi
                ev.journal_ref = new_journal_ref
                ev.peer_reviewed = True
                if rec.bibcode and not ev.ads_bibcode:
                    ev.ads_bibcode = rec.bibcode
                totals["updated"] += 1

        if args.commit:
            db.commit()
        else:
            db.rollback()
        print(json.dumps(totals, indent=2))
        return totals
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill Evidence DOI/journal_ref/peer_reviewed from ADS")
    parser.add_argument("--page-id", type=int, default=None)
    parser.add_argument("--claim-id", action="append", type=int, default=[])
    parser.add_argument("--evidence-id", action="append", type=int, default=[])
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--include-resolved", action="store_true")
    parser.add_argument("--commit", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
