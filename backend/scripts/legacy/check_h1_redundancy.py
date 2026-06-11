import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.page import WikiPage

db = SessionLocal()
pages = db.query(WikiPage).all()
print("--- H1 REDUNDANCY CHECK ---")
count = 0
for p in pages:
    lines = [l.strip() for l in p.content.split("\n") if l.strip()]
    if lines and lines[0].startswith("# "):
        print(f"ID: {p.id} | Slug: {p.slug} | First Line: {lines[0]}")
        count += 1
print(f"Total pages starting with H1: {count} / {len(pages)}")
db.close()
