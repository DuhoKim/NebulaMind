import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Claim

db = SessionLocal()
res = db.query(Claim.trust_level).filter(Claim.page_id == 57).distinct().all()
print("Distinct trust_levels in DB for Page 57:")
for r in res:
    print(f"- '{r[0]}'")
db.close()
