import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from sqlalchemy import text
from app.models.page import WikiPage

db = SessionLocal()
page = db.query(WikiPage).get(57)

import re
markers = set(re.findall(r"<!--claim:(\d+)\s*-->", page.content))
visible_count = len(markers)

owned_res = db.execute(text("""
    SELECT c.id
    FROM claim_section_assignments a
    JOIN claims c ON c.id = a.claim_id
    WHERE a.page_id = 57 AND a.assignment_status = 'active'
""")).fetchall()

total = len(owned_res)
ratio = visible_count / total if total else 0.0

print(f"{visible_count}/{total} ({ratio:.1%})")
db.close()
