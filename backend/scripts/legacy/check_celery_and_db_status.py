import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Evidence
from app.models.arxiv import ArxivPaper
from app.models.page import WikiPage
from datetime import datetime, timedelta
import re

db = SessionLocal()
p = db.query(WikiPage).get(57)
markers = re.findall(r"<!--claim:([\d,\s]+)\s*-->", p.content) if p else []
all_ids = []
for m in markers:
    for val in m.split(","):
        val = val.strip()
        if val:
            all_ids.append(int(val))

cutoff = datetime.utcnow() - timedelta(hours=6)
new_papers = db.query(ArxivPaper).filter(ArxivPaper.created_at >= cutoff).count()
new_evidence = db.query(Evidence).filter(Evidence.verified_at >= cutoff).count()

print("--- SYSTEM STATE UPDATE (17:15 KST) ---")
print(f"Page 57 Current Markers on Live Page: {len(markers)}")
print(f"Page 57 Current Unique Claim IDs: {len(set(all_ids))}")
print(f"New Papers Ingested (Last 6 hours): {new_papers}")
print(f"New Evidence Rows Created (Last 6 hours): {new_evidence}")

# Check any actual new evidence rows details
if new_evidence > 0:
    rows = db.query(Evidence).filter(Evidence.verified_at >= cutoff).all()
    print("\n--- NEW LIVE EVIDENCE DETECTED ---")
    for r in rows:
        print(f"- Claim ID: {r.claim_id} | Paper: {r.arxiv_id} | Title: {r.title[:70]} | Stance: {r.stance}")

db.close()
