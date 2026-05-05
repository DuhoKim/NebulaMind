#!/usr/bin/env python3
"""Run fact sourcing on all wiki pages."""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage
from app.agent_loop.tasks import source_facts_for_page


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", default=False)
    parser.add_argument("--page-id", type=int, default=None)
    args = parser.parse_args()

    db = SessionLocal()
    try:
        if args.page_id:
            pages = [db.query(WikiPage).filter(WikiPage.id == args.page_id).first()]
        else:
            pages = db.query(WikiPage).filter(WikiPage.hero_facts.isnot(None)).all()

        print(f"Sourcing {len(pages)} pages...")
        for p in pages:
            if not p:
                continue
            print(f"  Page #{p.id} {p.slug}...", end="", flush=True)
            if args.apply:
                source_facts_for_page(p.id)
                print(" done")
            else:
                print(" [dry-run]")

        if not args.apply:
            print("Dry run done. Run with --apply to write.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
