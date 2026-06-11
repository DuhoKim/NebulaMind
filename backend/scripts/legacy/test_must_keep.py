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
    SELECT c.id, c.trust_level
    FROM claim_section_assignments a
    JOIN claims c ON c.id = a.claim_id
    WHERE a.page_id = 57 AND a.assignment_status = 'active'
""")).fetchall()

must_keep = {r.id for r in owned_res if r.trust_level in ('accepted', 'consensus')}
missing = must_keep - set(int(x) for x in markers)

print(f"Total must-keep: {len(must_keep)}")
print(f"Missing must-keep: {len(missing)}")
db.close()
