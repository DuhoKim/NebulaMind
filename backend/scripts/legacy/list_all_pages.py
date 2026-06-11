import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.page import WikiPage

db = SessionLocal()
pages = db.query(WikiPage).all()
print("--- ALL PAGES IN DB ---")
for p in pages:
    print(f"ID: {p.id} | Slug: {p.slug} | Title: {p.title}")
db.close()
