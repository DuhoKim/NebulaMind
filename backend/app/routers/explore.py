from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.models.page import WikiPage
from app.models.edit import EditProposal

router = APIRouter(prefix="/api/explore", tags=["explore"])

CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "blackhole": ["black hole", "blackhole", "event horizon", "singularity"],
    "stellar": ["star", "stellar", "neutron", "supernova", "pulsar", "dwarf"],
    "galaxy": ["galaxy", "galaxies", "milky way", "andromeda", "spiral"],
    "cosmology": ["dark", "cosmic", "hubble", "big bang", "universe", "redshift", "inflation"],
    "solarsystem": ["planet", "asteroid", "kuiper", "comet", "moon", "orbit", "solar system", "mars", "jupiter"],
}


def _classify(title: str, content: str) -> str:
    text = (title + " " + content).lower()
    scores: dict[str, int] = {}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        scores[cat] = sum(text.count(kw) for kw in keywords)
    best = max(scores, key=scores.get)  # type: ignore[arg-type]
    return best if scores[best] > 0 else "general"


class CardOut(BaseModel):
    id: int
    title: str
    slug: str
    summary: str
    category: str
    edit_count: int


@router.get("/cards", response_model=list[CardOut])
def list_cards(
    category: Optional[str] = Query(None),
    sort: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    pages = db.query(WikiPage).all()

    cards: list[dict] = []
    for p in pages:
        cat = _classify(p.title, p.content)
        if category and cat != category:
            continue
        edit_count = db.query(func.count(EditProposal.id)).filter(EditProposal.page_id == p.id).scalar() or 0
        cards.append(
            {
                "id": p.id,
                "title": p.title,
                "slug": p.slug,
                "summary": p.content[:150] if p.content else "",
                "category": cat,
                "edit_count": edit_count,
            }
        )

    if sort == "edits":
        cards.sort(key=lambda c: c["edit_count"], reverse=True)
    else:
        cards.sort(key=lambda c: c["title"])

    return cards
