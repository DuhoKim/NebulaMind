import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from sqlalchemy import text

db = SessionLocal()
res = db.execute(text("""
    SELECT 
        c.trust_level,
        a.assignment_status,
        count(*) as c
    FROM claim_section_assignments a
    JOIN claims c ON c.id = a.claim_id
    WHERE a.page_id = 57
    GROUP BY c.trust_level, a.assignment_status
""")).fetchall()

for r in res:
    print(f"{r.trust_level} / {r.assignment_status}: {r.c}")

db.close()
