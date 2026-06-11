import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from sqlalchemy import text

db = SessionLocal()
print("\n--- LATEST 10 Edit Proposals for Page 57 ---")
edits = db.execute(text("""
    SELECT id, page_id, agent_id, status, created_at, summary
    FROM edit_proposals
    WHERE page_id = 57
    ORDER BY created_at DESC
    LIMIT 10
""")).fetchall()

for e in edits:
    print(f"ID: {e[0]} | Page ID: {e[1]} | Agent ID: {e[2]} | Status: {e[3]} | Created At: {e[4]} | Summary: {e[5]}")

db.close()
