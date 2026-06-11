import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.page import WikiPage
import re

db = SessionLocal()
p = db.query(WikiPage).get(57)
if p:
    markers = re.findall(r"<!--claim:(\d+)\s*-->", p.content)
    print("WikiPage 57 Current Content:")
    print("Unique markers:", sorted(list(set([int(m) for m in markers]))))
    print("Total marker instances:", len(markers))
else:
    print("WikiPage not found")
db.close()
