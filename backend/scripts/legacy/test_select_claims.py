import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Claim
from scripts.targeted_ads_miner import SECTION_CLASS_MAP

db = SessionLocal()
query = db.query(Claim).filter(Claim.page_id == 57)
print("Step 1 (page_id=57):", query.count())

query2 = query.filter(Claim.trust_level.in_(["unverified", "debated"]))
print("Step 2 (trust_level filter):", query2.count())

claims = query2.all()
mapped_count = 0
for c in claims:
    mapped = SECTION_CLASS_MAP.get(c.section or "")
    if mapped:
        mapped_count += 1
print("Step 3 (section map filter):", mapped_count)

# Let's print the first 10 unverified claims and their sections
for c in claims[:10]:
    print(f"ID: {c.id} | Section: '{c.section}' | Mapped: {SECTION_CLASS_MAP.get(c.section or '')}")

db.close()
