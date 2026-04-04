from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.page import WikiPage
from app.models.graph import PageRelation

router = APIRouter(prefix="/api/graph", tags=["graph"])

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


class NodeOut(BaseModel):
    id: int
    title: str
    slug: str
    category: str


class EdgeOut(BaseModel):
    source: int
    target: int
    type: str
    weight: float


class GraphOut(BaseModel):
    nodes: list[NodeOut]
    edges: list[EdgeOut]


@router.get("", response_model=GraphOut)
def get_graph(db: Session = Depends(get_db)):
    pages = db.query(WikiPage).all()
    nodes = [
        NodeOut(id=p.id, title=p.title, slug=p.slug, category=_classify(p.title, p.content))
        for p in pages
    ]

    relations = db.query(PageRelation).all()
    edges = [
        EdgeOut(source=r.source_page_id, target=r.target_page_id, type=r.relation_type, weight=r.weight)
        for r in relations
    ]

    return GraphOut(nodes=nodes, edges=edges)


@router.post("/auto-generate")
def auto_generate(db: Session = Depends(get_db)):
    pages = db.query(WikiPage).all()

    # Clear existing auto-generated relations
    db.query(PageRelation).delete()
    db.commit()

    page_cats: dict[int, str] = {}
    page_words: dict[int, set[str]] = {}
    for p in pages:
        page_cats[p.id] = _classify(p.title, p.content)
        text = (p.title + " " + p.content).lower()
        page_words[p.id] = set(w for w in text.split() if len(w) > 3)

    created = 0
    for i, p1 in enumerate(pages):
        for p2 in pages[i + 1 :]:
            weight = 0.0

            # Same category bonus
            if page_cats[p1.id] == page_cats[p2.id]:
                weight += 0.6

            # Title mention bonus
            if p2.title.lower() in (p1.content or "").lower():
                weight += 0.8
            if p1.title.lower() in (p2.content or "").lower():
                weight += 0.8

            # Common keywords bonus
            common = page_words[p1.id] & page_words[p2.id]
            weight += min(len(common) * 0.02, 0.4)

            if weight >= 0.5:
                rel = PageRelation(
                    source_page_id=p1.id,
                    target_page_id=p2.id,
                    relation_type="related",
                    weight=min(weight, 1.0),
                )
                db.add(rel)
                created += 1

    db.commit()
    return {"created": created}
