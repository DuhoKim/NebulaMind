import time
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.page import WikiPage

router = APIRouter(prefix="/api/wiki", tags=["wiki"])

CATEGORIES = [
    {"id": "stars",        "label": "Stars",        "emoji": "⭐"},
    {"id": "black-holes",  "label": "Black Holes",  "emoji": "🕳️"},
    {"id": "galaxies",     "label": "Galaxies",     "emoji": "🌌"},
    {"id": "cosmology",    "label": "Cosmology",    "emoji": "🌠"},
    {"id": "high-energy",  "label": "High Energy",  "emoji": "⚡"},
    {"id": "solar-system", "label": "Solar System", "emoji": "🪐"},
    {"id": "methods",      "label": "Methods",      "emoji": "🔬"},
]

_CACHE: dict = {"at": 0.0, "data": None}
_CACHE_TTL = 60.0


def _summarize(content: str | None, summary: str | None, max_len: int = 120) -> str:
    text = (summary or content or "").strip()
    # Strip leading markdown heading if present
    if text.startswith("#"):
        lines = text.splitlines()
        text = "\n".join(l for l in lines if not l.lstrip().startswith("#")).strip()
    text = " ".join(text.split())
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "…"


@router.get("/directory")
def directory(db: Session = Depends(get_db)):
    now = time.time()
    if _CACHE["data"] is not None and (now - _CACHE["at"]) < _CACHE_TTL:
        return _CACHE["data"]

    pages = db.query(WikiPage).order_by(WikiPage.title.asc()).all()
    by_cat: dict[str, list[dict]] = {c["id"]: [] for c in CATEGORIES}
    for p in pages:
        cat = (p.category or "").strip()
        if cat in by_cat:
            by_cat[cat].append({
                "title": p.title,
                "slug": p.slug,
                "summary": _summarize(p.content, p.summary),
            })

    result = {
        "categories": [
            {**c, "topics": by_cat[c["id"]]}
            for c in CATEGORIES
        ]
    }
    _CACHE["at"] = now
    _CACHE["data"] = result
    return result
