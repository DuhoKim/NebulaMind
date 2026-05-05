#!/usr/bin/env python3
"""
Normalize wiki page heading levels.
Pages that use ### as primary headings (no ## present) → promote ### → ##, #### → ###
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.page import WikiPage

def count_heading(content, prefix):
    return content.count('\n' + prefix + ' ') + (1 if content.startswith(prefix + ' ') else 0)

def promote_headings(content: str) -> str:
    """Promote ### → ## and #### → ### throughout content."""
    # Replace #### first (to avoid double-promoting), then ###
    content = re.sub(r'^#### ', '### ', content, flags=re.MULTILINE)
    content = re.sub(r'^### ', '## ', content, flags=re.MULTILINE)
    return content

def main():
    db = SessionLocal()
    try:
        pages = db.query(WikiPage).all()
        fixed = 0
        skipped = 0

        for page in pages:
            if not page.content:
                continue

            h2 = count_heading(page.content, '##')
            h3 = count_heading(page.content, '###')
            h4 = count_heading(page.content, '####')

            # Only fix pages where h3 is the dominant/only top-level heading
            # Case 1: No h2 at all, but has h3 → h3 is the top-level (promote all)
            # Case 2: h3 >> h2 by a large margin (h3 is being used as primary)
            if h3 == 0:
                skipped += 1
                continue

            if h2 == 0:
                # No h2 at all — h3 is the primary heading, promote everything
                new_content = promote_headings(page.content)
                action = "promoted (no h2)"
            elif h3 > h2:
                # More h3 than h2 — h3 is being misused as primary section headings
                new_content = promote_headings(page.content)
                action = f"promoted (h3={h3} > h2={h2})"
            else:
                # h3 <= h2 — h3 is likely legitimate sub-headings, skip
                skipped += 1
                continue

            page.content = new_content
            new_h2 = count_heading(new_content, '##')
            new_h3 = count_heading(new_content, '###')
            print(f"  FIXED [{action}]: {page.slug}")
            print(f"    Before: h2={h2}, h3={h3}, h4={h4}")
            print(f"    After:  h2={new_h2}, h3={new_h3}")
            fixed += 1

        db.commit()
        print(f"\nDone: {fixed} pages fixed, {skipped} skipped")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()
