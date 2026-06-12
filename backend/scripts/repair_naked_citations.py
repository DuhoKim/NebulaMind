#!/usr/bin/env python3
"""Automatically detect naked year-less 'Author et al.' mentions and backfill their years based on page evidence."""

import sys
import re
from sqlalchemy import text

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")

from app.database import SessionLocal
from app.models.page import WikiPage
from scripts.align_citations import align_page


def repair_naked_citations(page_id: int) -> None:
    with SessionLocal() as db:
        page = db.get(WikiPage, page_id)
        if not page:
            print(f"Page {page_id} not found.")
            return

        content = page.content or ""
        
        # 1. Retrieve all known evidence for this page to build an author-year mapping
        rows = db.execute(
            text(
                """
                SELECT DISTINCT e.id, e.authors, e.year
                FROM page_citation_links pcl
                JOIN evidence e ON e.id = pcl.evidence_id
                WHERE pcl.page_id = :pid AND e.year IS NOT NULL
                """
            ),
            {"pid": page_id}
        ).fetchall()
        
        print("Fetched rows count:", len(rows))
        author_map = {}
        for row in rows:
            ev_id, authors, year = row
            if not authors:
                continue
            
            clean_authors = authors.strip("[]\"'")
            first = re.split(r"\s*,\s*|\s+;\s*|\s+and\s+", clean_authors, flags=re.I)[0].strip()
            clean_first = re.sub(r"\bet\s+al\.?\b|\bCollaboration\b", "", first, flags=re.I).strip(" ,.")
            last_name = clean_first.split()[-1] if clean_first.split() else clean_first
            
            if last_name:
                # Remove diacritics / clean up last name to be safe
                last_name_clean = last_name.lower()
                if last_name_clean not in author_map:
                    author_map[last_name_clean] = []
                author_map[last_name_clean].append((year, ev_id))

        print("Page evidence author map clean keys count:", len(author_map))

        # 2. Find naked author mentions: 'Author et al.'
        # We want to match cases NOT followed by a year, e.g. '(2023)' or '2023' or '<!--cite:'
        pattern = re.compile(
            r"\b(?P<authors>[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’.\-]+\s+et\s+al\.?)"
            r"(?!\s*\(?(?:19|20)\d{2}\)?)"  # Not followed by year (with optional parens)
            r"(?!\s*<!--cite:)"            # Not followed by cite marker
        )

        def repl(match: re.Match) -> str:
            raw_author = match.group("authors")
            clean = re.sub(r"\bet\s+al\.?\b", "", raw_author, flags=re.I).strip(" ,.")
            last = clean.split()[-1] if clean.split() else clean
            last_clean = last.lower()
            
            # See if we have a unique year in our author map
            candidates = author_map.get(last_clean, [])
            if len(candidates) == 1:
                year, ev_id = candidates[0]
                print(f"Repairing naked mention: '{raw_author}' -> '{raw_author} ({year})'")
                return f"{raw_author} ({year})"
            elif len(candidates) > 1:
                # If multiple years, default to the latest or don't guess to be safe
                year = max(c[0] for c in candidates)
                print(f"Repairing naked mention (multiple options, picking latest): '{raw_author}' -> '{raw_author} ({year})'")
                return f"{raw_author} ({year})"
            
            return raw_author

        new_content = pattern.sub(repl, content)
        
        if new_content != content:
            page.content = new_content
            db.commit()
            print("Successfully updated page with repaired naked citations. Triggering align_page...")
            
            # Run the alignment script to compile parentheticals into dynamic cite markers
            report = align_page(db, page, dry_run=False, bootstrap=False)
            db.commit()
            print("Alignment report:", report)
        else:
            print("No naked citations were repaired.")


if __name__ == "__main__":
    repair_naked_citations(57)
