#!/usr/bin/env python3
"""
Dry-run classifier over all ArxivPapers in the DB.

Usage:
    .venv/bin/python3 scripts/classify_arxiv_dry_run.py

Checks:
  1. Connects to DB
  2. Builds TF-IDF corpus from wiki pages
  3. Classifies every ArxivPaper
  4. Prints match_type distribution
  5. Asserts no paper produces an exception
  6. Runs twice to verify idempotency
"""
import sys
import os

# Allow running from the backend/ directory without installing the package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from collections import Counter

from app.database import SessionLocal
from app.models.arxiv import ArxivPaper
from app.services.arxiv_classifier import classify_match_type, refresh_page_vectors


def run_once(db) -> dict[str, int]:
    refresh_page_vectors(db)
    papers = db.query(ArxivPaper).all()
    print(f"  Papers found: {len(papers)}")

    dist: Counter = Counter()
    errors = 0
    for paper in papers:
        try:
            match_type, _meta = classify_match_type(paper, db)
            dist[match_type] += 1
        except Exception as exc:
            errors += 1
            print(f"  ERROR on arxiv_id={paper.arxiv_id}: {exc}", file=sys.stderr)

    assert errors == 0, f"{errors} papers raised exceptions!"
    return dict(dist)


def main():
    db = SessionLocal()
    try:
        print("=== Run 1 ===")
        dist1 = run_once(db)
        for k, v in sorted(dist1.items()):
            print(f"  {k}: {v}")

        print("\n=== Run 2 (idempotency check) ===")
        dist2 = run_once(db)
        for k, v in sorted(dist2.items()):
            print(f"  {k}: {v}")

        assert dist1 == dist2, f"Idempotency FAILED:\n  run1={dist1}\n  run2={dist2}"
        print("\n✅ Idempotency OK — both runs produced identical distributions.")

        total = sum(dist1.values())
        print(f"\n=== Distribution Summary (total={total}) ===")
        for match_type in ("claim_evidence", "page_extension", "new_topic_candidate", "unrelated"):
            count = dist1.get(match_type, 0)
            pct = 100.0 * count / total if total else 0
            print(f"  {match_type:<25} {count:>5}  ({pct:5.1f}%)")

    finally:
        db.close()


if __name__ == "__main__":
    main()
