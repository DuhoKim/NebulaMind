import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.arxiv import ArxivPaper
from datetime import datetime, timedelta

db = SessionLocal()
total = db.query(ArxivPaper).count()
recent_cutoff = datetime.utcnow() - timedelta(minutes=10)
recent = db.query(ArxivPaper).filter(ArxivPaper.created_at >= recent_cutoff).count()

print("--- ARXIV PAPERS IN DB ---")
print(f"Total Papers in DB: {total}")
print(f"New Papers Ingested in Last 10 Mins: {recent}")

# Print recent 5 papers if any
if recent > 0:
    rows = db.query(ArxivPaper).filter(ArxivPaper.created_at >= recent_cutoff).limit(5).all()
    for r in rows:
        print(f"- {r.arxiv_id} | Created: {r.created_at} | Title: {r.title[:80]} | Match Type: {r.match_type}")

db.close()
