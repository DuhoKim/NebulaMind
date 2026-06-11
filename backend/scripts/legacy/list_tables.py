import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from sqlalchemy import text

db = SessionLocal()
res = db.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")).fetchall()
print("Tables in public schema:")
for r in res:
    print("- ", r[0])
db.close()
