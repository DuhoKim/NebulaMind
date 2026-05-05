#!/usr/bin/env python3
"""Fill summary + summary_source fields from wiki_summary for all mapped pages."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage

def first_sentence(text: str) -> str:
    if not text: return ""
    abbrevs = {"e.g.", "i.e.", "cf.", "et al.", "vs.", "Dr.", "Prof."}
    out = ""
    for chunk in text.split(". "):
        out = (out + ". " + chunk).strip(". ").strip()
        if len(out) >= 40 and not any(out.endswith(a.rstrip(".")) for a in abbrevs):
            return out + "."
    return (out + ".") if out else text[:200]

def main():
    db = SessionLocal()
    pages = db.query(WikiPage).filter(WikiPage.wiki_summary.isnot(None)).all()
    updated = 0
    for p in pages:
        if p.summary_source == "wikipedia" and p.summary:
            continue  # already done
        new_sum = first_sentence(p.wiki_summary)[:300]
        p.summary = new_sum
        p.summary_source = "wikipedia"
        p.summary_source_url = p.wiki_summary_url
        print(f"  {p.slug}: {new_sum[:70]}...")
        updated += 1
    db.commit()
    print(f"\nUpdated {updated} pages.")
    db.close()

if __name__ == "__main__":
    main()
