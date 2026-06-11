import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Claim, Evidence

db = SessionLocal()
claims = db.query(Claim).filter(Claim.page_id == 57).all()
unverified = []
for c in claims:
    ev_count = db.query(Evidence).filter(Evidence.claim_id == c.id).count()
    if ev_count == 0:
        unverified.append(c)

print("--- UNVERIFIED CLAIMS AUDIT ---")
print(f"Total Claims on Page 57: {len(claims)}")
print(f"Unverified (0 papers linked): {len(unverified)} / {len(claims)} ({len(unverified)/len(claims)*100:.1f}%)")

# Print first 5 unverified claims as examples
print("\n--- SAMPLE UNVERIFIED CLAIMS ---")
for c in unverified[:5]:
    print(f"- ID: {c.id} | Text: {c.text[:120]}")
db.close()
