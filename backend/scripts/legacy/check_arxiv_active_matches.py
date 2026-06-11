import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.arxiv import ArxivPaper
from datetime import datetime, timedelta

db = SessionLocal()
recent_cutoff = datetime.utcnow() - timedelta(minutes=10)
matches = db.query(ArxivPaper).filter(
    ArxivPaper.created_at >= recent_cutoff,
    ArxivPaper.match_type.is_not(None),
    ArxivPaper.match_type != "unrelated"
).all()

print("--- RECENT RELATED PAPERS ---")
print(f"Total related papers found: {len(matches)}")
for m in matches:
    print(f"- {m.arxiv_id} | Title: {m.title[:80]} | Match Type: {m.match_type}")
db.close()
