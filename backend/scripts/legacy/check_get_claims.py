import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Claim
from app.routers.claims import visible_claim_filter
from sqlalchemy import or_

db = SessionLocal()
claims = (
    db.query(Claim)
    .filter(Claim.page_id == 57)
    .filter(visible_claim_filter())
    .all()
)

claim_ids = [c.id for c in claims]
print("Total visible claims in query:", len(claim_ids))
print("Is 1713 in query result?", 1713 in claim_ids)
print("Is 1955 in query result?", 1955 in claim_ids)

# Let's check why they might be excluded
c1713 = db.query(Claim).get(1713)
print("Claim 1713 page_id:", c1713.page_id)
print("Claim 1713 rewrite_status:", getattr(c1713, 'rewrite_status', None))

db.close()
