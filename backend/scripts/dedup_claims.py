#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).resolve()
BACKEND = HERE.parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from sqlalchemy import text
from app.database import SessionLocal

def run_dedup(page_id: int = 57, commit: bool = False):
    db = SessionLocal()
    try:
        claims = db.execute(
            text("SELECT id, text, trust_level FROM claims WHERE page_id=:pid ORDER BY id"),
            {"pid": page_id}
        ).fetchall()

        # Simple prefix-based dedup: check first 40 chars
        prefix_groups = defaultdict(list)
        for cid, txt, tlevel in claims:
            # Clean up the text a bit to avoid whitespace/punctuation differences
            import re
            cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', txt).lower()
            tokens = cleaned.split()
            # Use first 15 words or 80 chars
            prefix = " ".join(tokens[:15])
            if len(prefix) > 40:
                prefix = prefix[:60]
            prefix_groups[prefix].append((cid, txt))

        merged = 0
        groups_found = 0
        for prefix, members in prefix_groups.items():
            if len(members) > 1:
                groups_found += 1
                primary_id = members[0][0]
                for cid, txt in members[1:]:
                    print(f"Duplicate found: {cid} -> {primary_id}")
                    print(f"  Primary: {members[0][1][:80]}...")
                    print(f"  Dup:     {txt[:80]}...")
                    merged += 1
                    if commit:
                        # Soft delete / hide the duplicate by setting rewrite_status = 'parent_replaced'
                        # Additive only, no trust data changes. 'parent_replaced' hides it from the UI.
                        db.execute(
                            text("UPDATE claims SET rewrite_status='parent_replaced' WHERE id=:cid"),
                            {"cid": cid}
                        )

        if commit:
            db.commit()
            print(f"Committed: Merged {merged} claims across {groups_found} groups.")
        else:
            print(f"Dry run: Found {merged} duplicates across {groups_found} groups.")

    finally:
        db.close()

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    p.add_argument("--page", type=int, default=57)
    args = p.parse_args()
    run_dedup(page_id=args.page, commit=args.commit)
