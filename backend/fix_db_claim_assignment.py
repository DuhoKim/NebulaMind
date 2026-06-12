import sys
from app.database import SessionLocal
from sqlalchemy import text

db = SessionLocal()
try:
    db.execute(text("""
    CREATE TABLE claim_section_assignments (
      id SERIAL PRIMARY KEY,
      claim_id INTEGER NOT NULL REFERENCES claims(id) ON DELETE CASCADE,
      page_id INTEGER NOT NULL REFERENCES wiki_pages(id) ON DELETE CASCADE,
      owner_section TEXT NOT NULL,
      owner_section_key TEXT NOT NULL,
      assignment_status TEXT NOT NULL DEFAULT 'active',
      assignment_method TEXT NOT NULL,
      confidence FLOAT NOT NULL DEFAULT 1.0,
      evidence JSONB,
      last_seen_marker_version INTEGER,
      last_seen_marker_section TEXT,
      last_seen_marker_span TEXT,
      missing_since TIMESTAMP,
      created_at TIMESTAMP DEFAULT NOW(),
      updated_at TIMESTAMP DEFAULT NOW(),
      UNIQUE (claim_id)
    );
    """))
    db.execute(text("""
    CREATE INDEX ix_claim_section_assignments_page_section
      ON claim_section_assignments(page_id, owner_section_key);
    """))
    db.commit()
    print("Table created")
except Exception as e:
    db.rollback()
    print(f"Error or already exists: {e}")
db.close()
