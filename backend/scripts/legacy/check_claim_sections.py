import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Claim

db = SessionLocal()
sections = db.query(Claim.section).filter(Claim.page_id == 57).distinct().all()
print("Distinct sections in DB for Page 57:")
for s in sections:
    print(f"- '{s[0]}'")
db.close()
