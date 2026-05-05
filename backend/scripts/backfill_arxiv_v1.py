"""
Backfill arXiv papers through the Phase B integration pipeline.

Usage:
    python -m backend.scripts.backfill_arxiv_v1            # dry-run (default)
    python -m backend.scripts.backfill_arxiv_v1 --apply
    python -m backend.scripts.backfill_arxiv_v1 --apply --batch-size 50

Streams all ArxivPaper rows in batches, classifies each via arxiv_classifier,
and calls the appropriate ingest handler. Idempotent — re-running won't
double-insert because all handlers check ExternalSourceLog.

Expected post-apply:
  ~100-150 new evidence rows (source_channel='arxiv_ingest')
  ~150-200 external_source_log rows
  ~10 claims promoted unverified → accepted
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from datetime import datetime

# Ensure backend package is importable
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.config import settings


def run(apply: bool, batch_size: int) -> None:
    db = SessionLocal()
    try:
        from app.models.arxiv import ArxivPaper
        from app.models.agent import Agent
        from app.services.arxiv_classifier import classify_match_type, refresh_page_vectors
        from app.services.arxiv_ingest import (
            handle_claim_evidence, handle_page_extension, handle_new_topic
        )

        # Find ArxivBot agent
        arxivbot = db.query(Agent).filter(Agent.name.ilike("%arxiv%")).first()
        if not arxivbot:
            arxivbot = db.query(Agent).first()
        print(f"[backfill_arxiv] agent: {arxivbot.name if arxivbot else 'None'}")

        # Pre-warm TF-IDF corpus
        print("[backfill_arxiv] building TF-IDF corpus...")
        refresh_page_vectors(db)

        total = db.query(ArxivPaper).count()
        print(f"[backfill_arxiv] {'DRY RUN' if not apply else 'APPLY'} — {total} papers, batch_size={batch_size}")
        if not apply:
            print("[backfill_arxiv] use --apply to actually write changes")

        counts = Counter()
        evidence_inserted = 0
        offset = 0

        while True:
            papers = db.query(ArxivPaper).order_by(ArxivPaper.id).offset(offset).limit(batch_size).all()
            if not papers:
                break

            for paper in papers:
                try:
                    match_type, meta = classify_match_type(paper, db)
                    counts[match_type] += 1

                    if apply:
                        if match_type == "claim_evidence":
                            handle_claim_evidence(paper, meta, db, arxivbot)
                            evidence_inserted += 1
                        elif match_type == "page_extension":
                            handle_page_extension(paper, meta, db, arxivbot)
                        elif match_type == "new_topic_candidate":
                            handle_new_topic(paper, meta, db, arxivbot)
                        # mark as processed
                        paper.match_type = match_type
                        paper.processed_at = datetime.utcnow()
                    else:
                        # dry-run: just show what would happen
                        if match_type != "unrelated":
                            best_page = meta.get("best_page_id", "?")
                            best_score = meta.get("best_page_score", 0)
                            print(f"  [{match_type}] {paper.arxiv_id} | page={best_page} score={best_score:.3f} | {paper.title[:60]}")

                except Exception as e:
                    counts["error"] += 1
                    print(f"[backfill_arxiv] error on {paper.arxiv_id}: {e}")

            if apply:
                db.flush()
                processed = offset + len(papers)
                print(f"[backfill_arxiv] batch {offset}–{processed}/{total} | "
                      f"evidence_inserted={evidence_inserted} | {dict(counts)}")

            offset += batch_size
            if apply:
                time.sleep(0.5)  # be gentle on the DB

        if apply:
            db.commit()

        # Final report
        print("\n[backfill_arxiv] === Summary ===")
        for k, v in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"  {k:25s}: {v}")
        print(f"  {'evidence_inserted':25s}: {evidence_inserted}")

        if apply:
            # Validation queries
            from sqlalchemy import text
            log_rows = db.execute(text(
                "SELECT decision, COUNT(*) as n FROM external_source_log "
                "WHERE source='arxiv' GROUP BY decision ORDER BY n DESC"
            )).fetchall()
            print("\n[backfill_arxiv] external_source_log:")
            for row in log_rows:
                print(f"  {row[0]:30s}: {row[1]}")

            trust_rows = db.execute(text(
                "SELECT trust_level, COUNT(*) as n FROM claims GROUP BY trust_level ORDER BY n DESC"
            )).fetchall()
            print("\n[backfill_arxiv] claim trust distribution:")
            for row in trust_rows:
                print(f"  {row[0]:20s}: {row[1]}")

    except Exception as e:
        db.rollback()
        print(f"[backfill_arxiv] fatal error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backfill arXiv integration pipeline")
    parser.add_argument("--apply", action="store_true", help="Actually write changes (default: dry-run)")
    parser.add_argument("--batch-size", type=int, default=50, help="Papers per batch (default: 50)")
    args = parser.parse_args()
    run(apply=args.apply, batch_size=args.batch_size)
