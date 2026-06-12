#!/usr/bin/env python3
"""Celery task/script that scans for and attempts to relink unmatched citation sentinels."""

from __future__ import annotations
import re
import sys
from datetime import datetime

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")

from app.database import SessionLocal
from app.models.page import WikiPage, PageVersion
from scripts.align_citations import find_evidence, CitationMatch, _first_author_last, upsert_link

UNMATCHED_SENTINEL_RE = re.compile(r"<!--cite-unmatched:(?P<key>[^>]+?)-->")

def relink_unmatched_citations() -> dict:
    db = SessionLocal()
    pages = db.query(WikiPage).all()
    total_scanned = 0
    total_relinked = 0
    
    print(f"Scanning {len(pages)} pages for unmatched citation sentinels...")
    
    for page in pages:
        content = page.content or ""
        matches = list(UNMATCHED_SENTINEL_RE.finditer(content))
        if not matches:
            continue
            
        new_content = content
        page_relinked = 0
        # Replace from right-to-left to preserve indexes
        for m in sorted(matches, key=lambda x: x.start(), reverse=True):
            total_scanned += 1
            key = m.group("key").strip()
            
            # Deconstruct the author_year_key into first_author and year
            parts = key.rsplit(" ", 1)
            if len(parts) != 2 or not parts[1].isdigit():
                continue
            authors, year_str = parts[0], parts[1]
            year = int(year_str)
            first_author = _first_author_last(authors)
            
            # Construct a dummy CitationMatch
            dummy = CitationMatch(
                start=m.start(),
                end=m.end(),
                raw=m.group(0),
                author_year_key=key,
                first_author=first_author,
                year=year
            )
            
            evidence_id, method, confidence = find_evidence(db, dummy)
            if evidence_id:
                # We have a match! Relink!
                marker = f"<!--cite:{evidence_id}-->"
                new_content = new_content[:m.start()] + marker + new_content[m.end():]
                upsert_link(db, page.id, evidence_id, key, method, confidence)
                page_relinked += 1
                total_relinked += 1
                print(f"  [Relinked] page={page.slug} key='{key}' -> evidence_id={evidence_id}")
                
        if page_relinked > 0:
            last_pv = (
                db.query(PageVersion)
                .filter(PageVersion.page_id == page.id)
                .order_by(PageVersion.version_num.desc())
                .first()
            )
            next_vnum = (last_pv.version_num + 1) if last_pv else 1
            pv = PageVersion(
                page_id=page.id,
                version_num=next_vnum,
                content=new_content,
                source_note=f"relink_unmatched:relinked_{page_relinked}"
            )
            db.add(pv)
            page.content = new_content
            db.flush()
            
    db.commit()
    print(f"Relink run completed. Scanned {total_scanned} sentinels, relinked {total_relinked}.")
    return {"scanned": total_scanned, "relinked": total_relinked}

if __name__ == "__main__":
    relink_unmatched_citations()
