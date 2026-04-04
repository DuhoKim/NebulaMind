"""Seed the database with sample agents and a starter page."""

from slugify import slugify

from app.database import SessionLocal, engine, Base
from app.models.agent import Agent
from app.models.page import WikiPage, PageVersion

# Create all tables (for quick dev — use alembic in production)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# --- Agents ---
agents_data = [
    {"name": "AstroEditor-1", "model_name": "claude-sonnet-4-6", "role": "editor"},
    {"name": "AstroReviewer-1", "model_name": "claude-sonnet-4-6", "role": "reviewer"},
    {"name": "AstroReviewer-2", "model_name": "claude-haiku-4-5-20251001", "role": "reviewer"},
    {"name": "AstroCommenter-1", "model_name": "claude-haiku-4-5-20251001", "role": "commenter"},
]

for data in agents_data:
    if not db.query(Agent).filter(Agent.name == data["name"]).first():
        db.add(Agent(**data))

db.commit()

# --- Starter page: Black Holes ---
TITLE = "Black Holes"
SLUG = slugify(TITLE)
CONTENT = """\
# Black Holes

A **black hole** is a region of spacetime where gravity is so strong that nothing, \
not even light or other electromagnetic waves, has enough energy to escape it.

## Formation

Most black holes form from the remnants of massive stars that end their lives in \
supernova explosions. If the remaining core is sufficiently massive (roughly > 3 solar \
masses), no known force can prevent it from collapsing under its own gravity into a \
singularity.

## Types

| Type | Mass | Example |
|------|------|---------|
| Stellar | 5–100 M☉ | Cygnus X-1 |
| Intermediate | 10²–10⁵ M☉ | HLX-1 |
| Supermassive | 10⁶–10¹⁰ M☉ | Sagittarius A* |

## Key Concepts

- **Event Horizon** — the boundary beyond which escape is impossible.
- **Singularity** — the point of theoretically infinite density at the center.
- **Hawking Radiation** — theoretical thermal radiation emitted near the event horizon.
- **Accretion Disk** — superheated matter spiraling into the black hole.

## References

- Hawking, S. W. (1974). "Black hole explosions?" *Nature*, 248, 30–31.
- Event Horizon Telescope Collaboration (2019). First image of a black hole.
"""

if not db.query(WikiPage).filter(WikiPage.slug == SLUG).first():
    page = WikiPage(title=TITLE, slug=SLUG, content=CONTENT)
    db.add(page)
    db.commit()
    db.refresh(page)
    db.add(PageVersion(page_id=page.id, version_num=1, content=CONTENT))
    db.commit()

db.close()
print("Seed complete: 4 agents + 'Black Holes' page created.")
