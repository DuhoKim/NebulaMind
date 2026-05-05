#!/usr/bin/env python3
"""
Backfill Wikipedia bibliography mining for all pages with wikipedia_title set.

ADS quota: 5000/day. 42 pages × ~40 ADS calls = ~1680 calls — fits one day.
Pacing: WIKIPEDIA_BIBLIO_PAGES_PER_HOUR pages/hour (default 5).
At 5/hr: 42 pages ≈ 9 hours total.

Usage:
  .venv/bin/python3 scripts/backfill_wikipedia_biblio.py           # dry-run
  .venv/bin/python3 scripts/backfill_wikipedia_biblio.py --apply   # actual
  .venv/bin/python3 scripts/backfill_wikipedia_biblio.py --apply --pages 3  # test 3 pages
"""
import sys, os, argparse, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from app.database import SessionLocal
from app.config import settings
from app.models.page import WikiPage
from app.services.wikipedia_client import wp_external_links
from app.services.paper_search import extract_arxiv_id, extract_doi, is_arxiv, is_doi


def dry_run_page(db, page):
    """Fetch external links and count staging candidates. No DB writes, no ADS calls."""
    refs = wp_external_links(page.wikipedia_title)
    arxiv_ids = [extract_arxiv_id(r) for r in refs if is_arxiv(r)]
    arxiv_ids = [a for a in arxiv_ids if a]
    doi_ids = [extract_doi(r) for r in refs if is_doi(r) and not is_arxiv(r)]
    doi_ids = [d for d in doi_ids if d]
    return len(arxiv_ids), len(doi_ids)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", default=False)
    parser.add_argument("--pages", type=int, default=None, help="Limit to N pages")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        pages = db.query(WikiPage).filter(WikiPage.wikipedia_title.isnot(None)).all()
        if args.pages:
            pages = pages[:args.pages]
        total = len(pages)

        pace_seconds = max(1, 3600 // settings.WIKIPEDIA_BIBLIO_PAGES_PER_HOUR)
        est_minutes = total * pace_seconds // 60
        mode = "APPLYING" if args.apply else "DRY RUN"
        print(f"{'='*60}")
        print(f"WIKIPEDIA BIBLIO BACKFILL — {mode}")
        print(f"{'='*60}")
        print(f"Pages to process: {total}")
        print(f"Pacing: {settings.WIKIPEDIA_BIBLIO_PAGES_PER_HOUR}/hour = {pace_seconds}s between pages")
        print(f"Estimated time: ~{est_minutes} minutes")
        if not args.apply:
            print("(DRY RUN — no ADS calls, no evidence inserted)")
        print()

        total_arxiv = 0
        total_doi = 0

        for i, page in enumerate(pages, 1):
            arxiv_count, doi_count = dry_run_page(db, page)
            total_arxiv += arxiv_count
            total_doi += doi_count
            print(f"  [{i:2}/{total}] {page.slug}: {arxiv_count} arXiv, {doi_count} DOI links")

            if args.apply:
                # Import here to avoid circular import at module level
                from app.agent_loop.tasks import mine_wikipedia_bibliography
                mine_wikipedia_bibliography(page.id)

                # Progress every 5 pages
                if i % 5 == 0:
                    evidence_count = db.execute(text(
                        "SELECT COUNT(*) FROM evidence WHERE source_channel='wikipedia_biblio'"
                    )).scalar()
                    print(f"\n  📊 Progress: {i}/{total} pages done; {evidence_count} evidence rows inserted so far\n")

                if i < total:
                    time.sleep(pace_seconds)

        print(f"\n{'='*60}")
        print(f"SUMMARY")
        print(f"  Pages processed: {total}")
        print(f"  Total arXiv links found: {total_arxiv}")
        print(f"  Total DOI links found:   {total_doi}")
        if args.apply:
            final_count = db.execute(text(
                "SELECT COUNT(*) FROM evidence WHERE source_channel='wikipedia_biblio'"
            )).scalar()
            print(f"  Evidence rows inserted: {final_count}")
        else:
            print(f"  Run with --apply to execute")

    finally:
        db.close()


if __name__ == "__main__":
    main()
