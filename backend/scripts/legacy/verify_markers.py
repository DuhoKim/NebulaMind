from app.database import SessionLocal
from app.models.page import WikiPage
import re

db = SessionLocal()
page = db.query(WikiPage).get(57)
print(page.content[:2000])
db.close()
