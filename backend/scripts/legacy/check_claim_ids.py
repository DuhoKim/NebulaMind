import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Claim
from sqlalchemy import text

db = SessionLocal()
ids_to_check = [1713, 1719, 1741, 1955, 1967, 1976, 1977]
print("--- CLAIMS IN DB ---")
for cid in ids_to_check:
    c = db.query(Claim).get(cid)
    if c:
        print(f"ID: {c.id} | Page ID: {c.page_id} | Section: {c.section} | Rewrite Status: {getattr(c, 'rewrite_status', None)} | Text: {c.text[:80]}")
    else:
        print(f"ID: {cid} | NOT FOUND")
db.close()
