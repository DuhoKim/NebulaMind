import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Evidence
from app.models.arxiv import ArxivPaper
from app.models.page import PageVersion
from datetime import datetime, timedelta

db = SessionLocal()
cutoff = datetime.utcnow() - timedelta(hours=1)

new_papers = db.query(ArxivPaper).filter(ArxivPaper.created_at >= cutoff).all()
new_evidence = db.query(Evidence).filter(Evidence.verified_at >= cutoff).all()
new_versions = db.query(PageVersion).filter(PageVersion.created_at >= cutoff).all()

print("--- PIPELINE RUN STATISTICS (LAST 1 HOUR) ---")
print(f"Total Papers Ingested from ADS: {len(new_papers)}")
print(f"Total New Evidence Rows Created: {len(new_evidence)}")
print(f"Total New Page Versions Created: {len(new_versions)}")

if len(new_evidence) > 0:
    print("\n--- NEW EVIDENCE COMMITTED ---")
    for ev in new_evidence:
        print(f"- Evidence ID: {ev.id} | Claim ID: {ev.claim_id} | Paper: {ev.arxiv_id} | Title: {ev.title[:70]} | Stance: {ev.stance}")

if len(new_papers) > 0:
    related = [p for p in new_papers if p.match_type and p.match_type != "unrelated"]
    print(f"\n--- RELATED PAPERS CLASSIFIED ({len(related)}) ---")
    for r in related:
        print(f"- {r.arxiv_id} | Match: {r.match_type} | Title: {r.title[:70]}")

db.close()
