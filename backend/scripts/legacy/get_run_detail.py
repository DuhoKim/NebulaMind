import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from sqlalchemy import text
import json

db = SessionLocal()
res = db.execute(text("SELECT * FROM claim_marker_runs WHERE id = 519")).fetchone()
columns = db.execute(text("SELECT column_name FROM information_schema.columns WHERE table_name='claim_marker_runs'")).fetchall()
col_names = [c[0] for c in columns]

print("--- DETAIL FOR RUN 519 ---")
for col, val in zip(col_names, res):
    print(f"{col}: {val}")
db.close()
