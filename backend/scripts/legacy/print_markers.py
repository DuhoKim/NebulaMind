import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.page import PageVersion
import re

db = SessionLocal()
v = db.query(PageVersion).filter(PageVersion.page_id == 57, PageVersion.version_num == 1472).first()
if v:
    markers = re.findall(r"<!--claim:(\d+)\s*-->", v.content)
    print("Unique markers:", sorted(list(set([int(m) for m in markers]))))
    print("Total marker instances:", len(markers))
else:
    print("Version not found")
db.close()
