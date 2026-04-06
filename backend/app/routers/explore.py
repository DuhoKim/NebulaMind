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

CATEGORY_EMOJI: dict[str, str] = {
    "blackhole": "🕳️",
    "stellar": "⭐",
    "galaxy": "🌌",
    "cosmology": "🔭",
    "solarsystem": "🪐",
    "general": "📖",
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
    difficulty: Optional[str]
    thumbnail_emoji: Optional[str]
    edit_count: int
    is_featured: bool


@router.get("/cards", response_model=list[CardOut])
def list_cards(
    category: Optional[str] = Query(None),
    difficulty: Optional[str] = Query(None),
    sort: Optional[str] = Query(None),
    featured: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(WikiPage)
    if featured and featured.lower() == "true":
        query = query.filter(WikiPage.is_featured == True)
    pages = query.all()

    cards: list[dict] = []
    for p in pages:
        # DB에 category가 있으면 사용, 없으면 키워드 매칭 fallback
        cat = p.category if p.category else _classify(p.title, p.content)
        if category and cat != category:
            continue
        # difficulty 필터
        if difficulty and p.difficulty != difficulty:
            continue
        edit_count = db.query(func.count(EditProposal.id)).filter(EditProposal.page_id == p.id).scalar() or 0
        # summary: DB에 있으면 사용, 없으면 content[:150]
        summary = p.summary if p.summary else (p.content[:150] if p.content else "")
        # thumbnail_emoji: DB에 있으면 사용, 없으면 카테고리 기본값
        emoji = p.thumbnail_emoji if p.thumbnail_emoji else CATEGORY_EMOJI.get(cat, "📖")
        cards.append(
            {
                "id": p.id,
                "title": p.title,
                "slug": p.slug,
                "summary": summary,
                "category": cat,
                "difficulty": p.difficulty,
                "thumbnail_emoji": emoji,
                "edit_count": edit_count,
                "is_featured": p.is_featured,
            }
        )

    if sort == "edits":
        cards.sort(key=lambda c: c["edit_count"], reverse=True)
    else:
        cards.sort(key=lambda c: c["title"])

    return cards
