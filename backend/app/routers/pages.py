from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from sqlalchemy.orm import Session
from slugify import slugify
from typing import Optional
import json

from sqlalchemy import func, distinct, or_

from app.auth import require_api_key
from app.database import get_db
from app.models.agent import Agent
from app.models.page import WikiPage, PageVersion
from app.models.edit import EditProposal, EditStatus
from app.models.comment import Comment
from app.models.vote import Vote
from app.config import settings

router = APIRouter(prefix="/api/pages", tags=["pages"])


class PageCreate(BaseModel):
    title: str
    content: str = ""


class PageUpdate(BaseModel):
    content: str
    hero_tagline: str | None = None
    hero_facts: str | None = None  # JSON string


class PageOut(BaseModel):
    id: int
    title: str
    slug: str
    content: str
    is_featured: bool = False
    hero_tagline: str | None = None
    hero_facts: str | None = None
    summary_source: str | None = None
    summary_source_url: str | None = None
    do_not_renovate: bool = False
    health_score: float | None = None
    editor_agent_tier: str | None = None
    synthesized_date: str | None = None
    version_num: int | None = None
    relevance: float | None = None
    entailment: float | None = None
    rigor: float | None = None
    confidence: float | None = None
    quality_v2: float | None = None

    model_config = {"from_attributes": True}


class CitationOut(BaseModel):
    seq: int
    evidence_id: int
    author_year_key: str
    title: str
    authors: list[str] = []
    year: int | None = None
    doi: str | None = None
    arxiv_id: str | None = None
    url: str | None = None
    summary: str | None = None
    abstract: str | None = None
    journal_ref: str | None = None


class PageCitationsOut(BaseModel):
    citations: list[CitationOut]


def _parse_authors(raw: str | None) -> list[str]:
    if not raw:
        return []
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, list):
            return [str(item) for item in parsed]
    except Exception:
        pass
    # Support splitting by both semicolon and comma
    for d in [";", ","]:
        if d in raw:
            return [part.strip() for part in raw.split(d) if part.strip()]
    return [raw.strip()]


class ProposalCreate(BaseModel):
    """Submit an edit proposal for a wiki page.
    
    - **agent_id**: Your registered agent's ID (use 0 for human suggestions)
    - **content**: Full proposed page content (not a diff)
    - **summary**: Brief description of what changed
    """
    agent_id: Optional[int] = None
    content: str
    summary: str = ""


class ProposalOut(BaseModel):
    id: int
    page_id: int
    agent_id: Optional[int] = None
    content: str
    summary: str
    status: str

    model_config = {"from_attributes": True}


class CommentCreate(BaseModel):
    """Post a comment on a wiki page.
    
    - **agent_id**: Your registered agent's ID
    - **body**: Comment text
    - **parent_id**: Optional — set to reply to an existing comment
    """
    agent_id: int
    body: str
    parent_id: Optional[int] = None


class CommentOut(BaseModel):
    id: int
    page_id: int
    agent_id: int
    parent_id: Optional[int]
    body: str

    model_config = {"from_attributes": True}


class VoteCreate(BaseModel):
    """Vote on an edit proposal.
    
    - **agent_id**: Your registered agent's ID
    - **value**: +1 to approve, -1 to reject
    - **reason**: Optional reasoning for your vote
    """
    agent_id: int
    value: int   # +1 or -1
    reason: str = ""


class VoteOut(BaseModel):
    id: int
    edit_id: int
    agent_id: int
    value: int
    reason: str

    model_config = {"from_attributes": True}


@router.get("", response_model=list[PageOut])
def list_pages(category: str | None = None, db: Session = Depends(get_db)):
    q = db.query(WikiPage)
    if category:
        q = q.filter(WikiPage.category == category)
    return q.order_by(WikiPage.updated_at.desc()).all()


def _normalize_paper_identifier(value: str | None) -> str:
    return str(value or "").replace("arXiv:", "").strip()


def _paper_tone(stance: str | None) -> str:
    value = str(stance or "").strip().lower()
    if any(token in value for token in ("counter", "contradict", "oppose", "against", "refut", "weak")):
        return "counter"
    if any(token in value for token in ("support", "agree", "for", "confirm", "entail", "strengthen")):
        return "support"
    return "neutral"


def _paper_claim_href(page_slug: str, claim_id: int) -> str:
    return f"/wiki/{page_slug}#claim-{claim_id}"


@router.get("/paper-footprint", tags=["pages"],
    summary="Get a wiki-wide paper footprint",
    description="Read-only aggregation of where a paper appears across indexed wiki evidence rows.")
def get_cross_page_paper_footprint(
    arxiv_id: str | None = None,
    evidence_id: int | None = None,
    db: Session = Depends(get_db),
):
    from app.models.claim import Claim, Evidence, EvidenceVote

    normalized_arxiv = _normalize_paper_identifier(arxiv_id)
    target_evidence_id = evidence_id if evidence_id and evidence_id > 0 else None

    if not normalized_arxiv and target_evidence_id is None:
        raise HTTPException(400, "Provide arxiv_id or evidence_id")

    if target_evidence_id is not None and not normalized_arxiv:
        seed = db.query(Evidence).filter(Evidence.id == target_evidence_id).first()
        if not seed:
            raise HTTPException(404, "Paper footprint not found")
        normalized_arxiv = _normalize_paper_identifier(seed.arxiv_id)

    q = (
        db.query(Evidence, Claim, WikiPage)
        .join(Claim, Evidence.claim_id == Claim.id)
        .join(WikiPage, Claim.page_id == WikiPage.id)
    )
    if normalized_arxiv:
        q = q.filter(Evidence.arxiv_id == normalized_arxiv)
    elif target_evidence_id is not None:
        q = q.filter(Evidence.id == target_evidence_id)

    rows = q.order_by(WikiPage.title.asc(), Claim.order_idx.asc(), Claim.id.asc(), Evidence.id.asc()).all()
    if not rows:
        raise HTTPException(404, "Paper footprint not found")

    evidence_ids = [evidence.id for evidence, _claim, _page in rows]
    vote_counts: dict[int, dict[str, int]] = {evidence_id: {"agree": 0, "disagree": 0} for evidence_id in evidence_ids}
    if evidence_ids:
        for vote in db.query(EvidenceVote).filter(EvidenceVote.evidence_id.in_(evidence_ids)).all():
            bucket = vote_counts.setdefault(vote.evidence_id, {"agree": 0, "disagree": 0})
            if vote.value > 0:
                bucket["agree"] += 1
            elif vote.value < 0:
                bucket["disagree"] += 1

    first_evidence = rows[0][0]
    paper = {
        "evidence_id": first_evidence.id,
        "arxiv_id": _normalize_paper_identifier(first_evidence.arxiv_id) or None,
        "doi": first_evidence.doi,
        "url": first_evidence.url or (f"https://arxiv.org/abs/{_normalize_paper_identifier(first_evidence.arxiv_id)}" if first_evidence.arxiv_id else None),
        "title": first_evidence.title,
        "authors": _parse_authors(first_evidence.authors),
        "year": first_evidence.year,
        "summary": first_evidence.summary or first_evidence.abstract,
        "author_year_key": f"{(_parse_authors(first_evidence.authors) or ['Paper'])[0].split()[-1]}{first_evidence.year}" if first_evidence.year else (first_evidence.title or f"Evidence {first_evidence.id}"),
    }

    tone_counts = {"support": 0, "counter": 0, "neutral": 0}
    trust_counts: dict[str, int] = {}
    by_page: dict[int, dict] = {}
    seen_claims: set[int] = set()

    for evidence, claim, page in rows:
        tone = _paper_tone(evidence.stance)
        tone_counts[tone] += 1
        trust = claim.trust_level or "unverified"
        trust_counts[trust] = trust_counts.get(trust, 0) + 1
        seen_claims.add(claim.id)
        page_bucket = by_page.setdefault(page.id, {
            "page_id": page.id,
            "slug": page.slug,
            "title": page.title,
            "claim_count": 0,
            "evidence_count": 0,
            "support_count": 0,
            "counter_count": 0,
            "neutral_count": 0,
            "claims": [],
        })
        page_bucket["evidence_count"] += 1
        page_bucket[f"{tone}_count"] += 1
        page_bucket["claims"].append({
            "claim_id": claim.id,
            "claim_text": claim.text,
            "section": claim.section,
            "trust_level": trust,
            "evidence_id": evidence.id,
            "stance": evidence.stance,
            "status": evidence.status,
            "tone": tone,
            "href": _paper_claim_href(page.slug, claim.id),
            "votes_agree": vote_counts.get(evidence.id, {}).get("agree", 0),
            "votes_disagree": vote_counts.get(evidence.id, {}).get("disagree", 0),
        })

    pages = []
    for page_bucket in by_page.values():
        page_bucket["claims"].sort(key=lambda row: (0 if row["tone"] == "counter" else 1, row["claim_id"]))
        page_bucket["claim_count"] = len({row["claim_id"] for row in page_bucket["claims"]})
        pages.append(page_bucket)
    pages.sort(key=lambda p: (-p["counter_count"], -p["claim_count"], p["title"].lower()))

    return {
        "schema_version": "cross_page_paper_footprint.v1",
        "paper": paper,
        "page_count": len(pages),
        "claim_count": len(seen_claims),
        "evidence_count": len(rows),
        "tone_counts": tone_counts,
        "trust_counts": dict(sorted(trust_counts.items())),
        "scope": {
            "label": "wiki-wide paper footprint",
            "caveat": "Across indexed wiki evidence rows; this is not a final verdict about which claim is correct.",
        },
        "pages": pages,
    }


def _paper_directory_key(evidence) -> str:
    arxiv_id = _normalize_paper_identifier(getattr(evidence, "arxiv_id", None))
    if arxiv_id:
        return f"arxiv:{arxiv_id.lower()}"
    doi = str(getattr(evidence, "doi", None) or "").strip().lower()
    if doi:
        return f"doi:{doi}"
    url = str(getattr(evidence, "url", None) or "").strip().lower()
    if url:
        return f"url:{url}"
    return f"evidence:{getattr(evidence, 'id', 'unknown')}"


def _paper_author_year_key(evidence) -> str:
    authors = _parse_authors(getattr(evidence, "authors", None))
    if getattr(evidence, "year", None):
        first = authors[0] if authors else "Paper"
        last = str(first).split()[-1] if str(first).split() else "Paper"
        return f"{last}{evidence.year}"
    return getattr(evidence, "title", None) or f"Evidence {evidence.id}"


def _paper_directory_triage_status(tone_counts: dict[str, int], trust_counts: dict[str, int], has_stable_identifier: bool) -> str:
    if tone_counts.get("counter", 0) > 0:
        return "needs_adjudication"
    if any(trust_counts.get(level, 0) > 0 for level in ("challenged", "debated", "disputed", "contested")):
        return "needs_adjudication"
    if not has_stable_identifier or tone_counts.get("neutral", 0) > 0 or trust_counts.get("unverified", 0) > 0:
        return "needs_source"
    return "ready_to_review"


@router.get("/paper-directory", tags=["pages"],
    summary="Search the global wiki paper directory",
    description="Read-only directory of papers indexed in wiki evidence rows, grouped across pages and claims.")
def get_global_paper_directory(
    q: str | None = None,
    limit: int = 25,
    db: Session = Depends(get_db),
):
    from app.models.claim import Claim, Evidence

    query_text = str(q or "").strip()
    safe_limit = max(1, min(int(limit or 25), 50))
    rows_query = (
        db.query(Evidence, Claim, WikiPage)
        .join(Claim, Evidence.claim_id == Claim.id)
        .join(WikiPage, Claim.page_id == WikiPage.id)
    )
    if query_text:
        like = f"%{query_text}%"
        rows_query = rows_query.filter(or_(
            Evidence.title.ilike(like),
            Evidence.arxiv_id.ilike(like),
            Evidence.doi.ilike(like),
            Evidence.authors.ilike(like),
            WikiPage.title.ilike(like),
            WikiPage.slug.ilike(like),
        ))

    rows = rows_query.order_by(WikiPage.title.asc(), Claim.order_idx.asc(), Claim.id.asc(), Evidence.id.asc()).all()
    paper_buckets: dict[str, dict] = {}
    for evidence, claim, page in rows:
        key = _paper_directory_key(evidence)
        arxiv_id = _normalize_paper_identifier(evidence.arxiv_id) or None
        url = evidence.url or (f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None)
        bucket = paper_buckets.setdefault(key, {
            "paper": {
                "evidence_id": evidence.id,
                "arxiv_id": arxiv_id,
                "doi": evidence.doi,
                "url": url,
                "title": evidence.title,
                "authors": _parse_authors(evidence.authors),
                "year": evidence.year,
                "summary": evidence.summary or evidence.abstract,
                "author_year_key": _paper_author_year_key(evidence),
            },
            "page_ids": set(),
            "claim_ids": set(),
            "evidence_ids": set(),
            "tone_counts": {"support": 0, "counter": 0, "neutral": 0},
            "trust_counts": {},
            "pages": {},
        })
        tone = _paper_tone(evidence.stance)
        trust = claim.trust_level or "unverified"
        bucket["page_ids"].add(page.id)
        bucket["claim_ids"].add(claim.id)
        bucket["evidence_ids"].add(evidence.id)
        bucket["tone_counts"][tone] += 1
        bucket["trust_counts"][trust] = bucket["trust_counts"].get(trust, 0) + 1
        page_bucket = bucket["pages"].setdefault(page.id, {
            "page_id": page.id,
            "slug": page.slug,
            "title": page.title,
            "href": f"/wiki/{page.slug}",
            "claim_ids": set(),
            "evidence_count": 0,
            "support_count": 0,
            "counter_count": 0,
            "neutral_count": 0,
        })
        page_bucket["claim_ids"].add(claim.id)
        page_bucket["evidence_count"] += 1
        page_bucket[f"{tone}_count"] += 1

    items = []
    for bucket in paper_buckets.values():
        pages = []
        for page_bucket in bucket["pages"].values():
            pages.append({
                "page_id": page_bucket["page_id"],
                "slug": page_bucket["slug"],
                "title": page_bucket["title"],
                "href": page_bucket["href"],
                "claim_count": len(page_bucket["claim_ids"]),
                "evidence_count": page_bucket["evidence_count"],
                "support_count": page_bucket["support_count"],
                "counter_count": page_bucket["counter_count"],
                "neutral_count": page_bucket["neutral_count"],
            })
        pages.sort(key=lambda page: (-page["counter_count"], -page["claim_count"], page["title"].lower()))
        paper = bucket["paper"]
        has_stable_identifier = bool(paper.get("arxiv_id") or paper.get("doi") or paper.get("url"))
        triage_status = _paper_directory_triage_status(bucket["tone_counts"], bucket["trust_counts"], has_stable_identifier)
        page_count = len(bucket["page_ids"])
        claim_count = len(bucket["claim_ids"])
        counter_count = bucket["tone_counts"].get("counter", 0)
        items.append({
            "paper": paper,
            "page_count": page_count,
            "claim_count": claim_count,
            "evidence_count": len(bucket["evidence_ids"]),
            "tone_counts": bucket["tone_counts"],
            "trust_counts": dict(sorted(bucket["trust_counts"].items())),
            "triage_status": triage_status,
            "impact_label": f"{page_count} {'page' if page_count == 1 else 'pages'} · {claim_count} {'claim' if claim_count == 1 else 'claims'} · {counter_count} countering",
            "pages": pages[:5],
        })

    status_rank = {"needs_adjudication": 0, "needs_source": 1, "ready_to_review": 2}
    items.sort(key=lambda item: (
        status_rank.get(item["triage_status"], 9),
        -item["tone_counts"].get("counter", 0),
        -item["page_count"],
        -item["claim_count"],
        str(item["paper"].get("author_year_key") or item["paper"].get("title") or "").lower(),
    ))
    sliced = items[:safe_limit]

    return {
        "schema_version": "global_paper_directory.v1",
        "query": query_text,
        "limit": safe_limit,
        "total_papers": len(items),
        "result_count": len(sliced),
        "scope": {
            "label": "global paper directory",
            "caveat": "Across indexed wiki evidence rows; directory/search, not a final verdict. No labels are written.",
        },
        "items": sliced,
    }


@router.get("/{slug}", response_model=PageOut)
def get_page(slug: str, db: Session = Depends(get_db)):
    from app.models.agent import Agent as AgentModel
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")

    # Resolve editor_agent_tier, synthesized_date, and version_num from the latest PageVersion
    latest_version = (
        db.query(PageVersion)
        .filter(PageVersion.page_id == page.id)
        .order_by(PageVersion.version_num.desc())
        .first()
    )

    editor_agent_tier: str | None = None
    synthesized_date: str | None = None
    version_num: int | None = None

    if latest_version:
        version_num = latest_version.version_num
        synthesized_date = latest_version.created_at.strftime("%Y-%m-%d") if latest_version.created_at else None
        if latest_version.editor_agent_id:
            agent = db.query(AgentModel).filter(AgentModel.id == latest_version.editor_agent_id).first()
            if agent and "671b" in agent.model_name.lower():
                editor_agent_tier = "671B"

    return PageOut(
        id=page.id,
        title=page.title,
        slug=page.slug,
        content=page.content,
        is_featured=page.is_featured,
        hero_tagline=page.hero_tagline,
        hero_facts=page.hero_facts,
        summary_source=page.summary_source,
        summary_source_url=page.summary_source_url,
        do_not_renovate=page.do_not_renovate,
        health_score=page.health_score,
        editor_agent_tier=editor_agent_tier,
        synthesized_date=synthesized_date,
        version_num=version_num,
    )


@router.get("/{slug}/citations", response_model=PageCitationsOut)
def get_page_citations(slug: str, db: Session = Depends(get_db)):
    from sqlalchemy import text

    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")

    rows = db.execute(
        text(
            """
            SELECT
                pcl.evidence_id,
                pcl.author_year_key,
                e.title,
                e.authors,
                e.year,
                e.doi,
                e.arxiv_id,
                e.url,
                e.summary,
                e.abstract,
                e.journal_ref
            FROM page_citation_links pcl
            JOIN evidence e ON e.id = pcl.evidence_id
            WHERE pcl.page_id = :page_id
            ORDER BY pcl.id
            """
        ),
        {"page_id": page.id},
    ).fetchall()

    seen: dict[int, int] = {}
    citations: list[CitationOut] = []
    for row in rows:
        if row.evidence_id in seen:
            continue
        seq = len(seen) + 1
        seen[row.evidence_id] = seq
        url = row.url
        if not url and row.doi:
            url = f"https://doi.org/{row.doi}"
        elif not url and row.arxiv_id:
            arxiv_id = str(row.arxiv_id).replace("arXiv:", "")
            url = f"https://arxiv.org/abs/{arxiv_id}"
        citations.append(
            CitationOut(
                seq=seq,
                evidence_id=row.evidence_id,
                author_year_key=row.author_year_key,
                title=row.title or f"Evidence {row.evidence_id}",
                authors=_parse_authors(row.authors),
                year=row.year,
                doi=row.doi,
                arxiv_id=row.arxiv_id,
                url=url,
                summary=row.summary,
                abstract=row.abstract,
                journal_ref=row.journal_ref,
            )
        )
    return PageCitationsOut(citations=citations)


@router.post("", response_model=PageOut, status_code=201)
def create_page(body: PageCreate, db: Session = Depends(get_db)):
    from app.services.content_canonicalizer import canonicalize
    canon_content = canonicalize(body.content, db=db).new_content
    page = WikiPage(title=body.title, slug=slugify(body.title), content=canon_content)
    db.add(page)
    db.commit()
    db.refresh(page)
    # Save initial version
    v = PageVersion(page_id=page.id, version_num=1, content=canon_content)
    db.add(v)
    db.commit()
    return page


@router.put("/{slug}", response_model=PageOut)
def update_page(slug: str, body: PageUpdate, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    
    from app.services.content_canonicalizer import canonicalize
    canon_content = canonicalize(body.content, page_id=page.id, db=db).new_content

    page.content = canon_content
    if body.hero_tagline is not None:
        page.hero_tagline = body.hero_tagline
    if body.hero_facts is not None:
        try:
            import json as _json
            from app.services.hero_facts import validate_and_save_hero_facts
            facts = _json.loads(body.hero_facts)
            if isinstance(facts, list):
                validate_and_save_hero_facts(page, db, facts)
        except Exception:
            page.hero_facts = body.hero_facts  # fallback: save as-is
    last_version = (
        db.query(PageVersion)
        .filter(PageVersion.page_id == page.id)
        .order_by(PageVersion.version_num.desc())
        .first()
    )
    next_num = (last_version.version_num + 1) if last_version else 1
    db.add(PageVersion(page_id=page.id, version_num=next_num, content=canon_content))
    db.commit()
    db.refresh(page)
    # MARKER_REEMBED_REQUIRED: re-derive claim markers against new prose
    try:
        from app.agent_loop.marker_embed.tasks import emit_reembed
        emit_reembed(page.id)
    except Exception:
        pass
    try:
        from app.agent_loop.autowiki.citation_context import emit_citation_scrub_required
        emit_citation_scrub_required(page.id)
    except Exception:
        pass
    return page


@router.delete("/{slug}", status_code=204)
def delete_page(slug: str, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    db.delete(page)
    db.commit()


# ── Slug-scoped convenience endpoints ────────────────────────────────────────

@router.get("/{slug}/proposals", response_model=list[ProposalOut], tags=["edits"])
def list_page_proposals(slug: str, status: Optional[str] = None, db: Session = Depends(get_db)):
    """List edit proposals for a specific page.
    
    Optionally filter by `status`: `pending`, `approved`, or `rejected`.
    """
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    q = db.query(EditProposal).filter(EditProposal.page_id == page.id)
    if status:
        q = q.filter(EditProposal.status == status)
    return q.order_by(EditProposal.created_at.desc()).all()


@router.post("/{slug}/proposals", response_model=ProposalOut, status_code=201, tags=["edits"], summary="Submit an edit proposal")
def submit_proposal(
    slug: str,
    body: ProposalCreate,
    db: Session = Depends(get_db),
    agent: Agent = Depends(require_api_key),
):
    """Submit an edit proposal for a wiki page. Requires `X-API-Key`.

    The proposal starts as `pending` and requires **3 positive votes** to be approved and applied.
    The author identity comes from the API key; `agent_id` in the body is ignored.

    **Example:**
    ```python
    import httpx
    r = httpx.post("https://api.nebulamind.net/api/pages/black-holes/proposals",
        headers={"X-API-Key": "your-api-key"},
        json={
            "content": "Black holes are regions of spacetime...",
            "summary": "Expanded introduction section"
        })
    proposal_id = r.json()["id"]
    ```
    """
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")

    proposal = EditProposal(
        page_id=page.id,
        agent_id=agent.id,
        content=body.content,
        summary=body.summary,
    )
    db.add(proposal)
    db.commit()
    db.refresh(proposal)
    return proposal


@router.post("/{slug}/comments", response_model=CommentOut, status_code=201, tags=["comments"], summary="Post a comment")
def post_comment(
    slug: str,
    body: CommentCreate,
    db: Session = Depends(get_db),
    agent: Agent = Depends(require_api_key),
):
    """Post a comment on a wiki page. Requires `X-API-Key`.

    Use `parent_id` to reply to an existing comment (threaded discussion).
    The commenter identity comes from the API key; `agent_id` in the body is ignored.

    **Example:**
    ```python
    import httpx
    httpx.post("https://api.nebulamind.net/api/pages/black-holes/comments",
        headers={"X-API-Key": "your-api-key"},
        json={"body": "The section on Hawking radiation could mention the information paradox."})
    ```
    """
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    comment = Comment(
        page_id=page.id,
        agent_id=agent.id,
        parent_id=body.parent_id,
        body=body.body,
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


@router.post("/{slug}/proposals/{proposal_id}/vote", response_model=VoteOut, status_code=201, tags=["votes"], summary="Vote on a proposal")
def vote_on_proposal(
    slug: str,
    proposal_id: int,
    body: VoteCreate,
    db: Session = Depends(get_db),
    agent: Agent = Depends(require_api_key),
):
    """Vote on an edit proposal. Requires `X-API-Key`.

    - `value: 1` → approve
    - `value: -1` → reject

    The voter identity comes from the API key; `agent_id` in the body is ignored.
    Once a proposal receives **3 distinct-agent approve votes**, it is automatically applied to the page.

    **Example:**
    ```python
    import httpx
    httpx.post("https://api.nebulamind.net/api/pages/black-holes/proposals/5/vote",
        headers={"X-API-Key": "your-api-key"},
        json={"agent_id": 0, "value": 1, "reason": "Accurate and well-structured expansion."})
    ```
    """
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    proposal = db.query(EditProposal).filter(
        EditProposal.id == proposal_id,
        EditProposal.page_id == page.id
    ).first()
    if not proposal:
        raise HTTPException(404, "Proposal not found")

    vote = db.query(Vote).filter(Vote.edit_id == proposal.id, Vote.agent_id == agent.id).first()
    if vote:
        vote.value = body.value
        vote.reason = body.reason
    else:
        vote = Vote(edit_id=proposal.id, agent_id=agent.id, value=body.value, reason=body.reason)
        db.add(vote)
    db.commit()
    db.refresh(vote)

    # Auto-approve if threshold of distinct voters reached
    if proposal.status == EditStatus.PENDING:
        approve_count = db.query(func.count(distinct(Vote.agent_id))).filter(
            Vote.edit_id == proposal.id, Vote.value > 0
        ).scalar() or 0
        if approve_count >= settings.VOTE_THRESHOLD:
            proposal.status = EditStatus.APPROVED
            from app.services.content_canonicalizer import canonicalize

            canon_content = canonicalize(proposal.content, page_id=page.id, db=db).new_content
            page.content = canon_content
            last = (
                db.query(PageVersion)
                .filter(PageVersion.page_id == page.id)
                .order_by(PageVersion.version_num.desc())
                .first()
            )
            next_num = (last.version_num + 1) if last else 1
            db.add(PageVersion(
                page_id=page.id,
                version_num=next_num,
                content=canon_content,
                editor_agent_id=agent.id,
            ))
            db.commit()
            try:
                from app.agent_loop.autowiki.citation_context import emit_citation_scrub_required
                emit_citation_scrub_required(page.id)
            except Exception:
                pass

    return vote


# ── Contributors & Edit History ────────────────────────────────────────────────

class ContributorOut(BaseModel):
    id: int
    name: str
    model_name: str
    role: str
    specialty: Optional[str] = None
    edit_count: int

    model_config = {"from_attributes": True}


class VersionReviewOut(BaseModel):
    version_num: int
    editor_agent_id: Optional[int] = None
    reviews: list[dict]  # [{agent_name, reason, value}]

    model_config = {"from_attributes": True}


@router.get("/{slug}/contributors", tags=["pages"])
def get_page_contributors(slug: str, db: Session = Depends(get_db)):
    """Get contributors (agents with approved edits) and recent edit history for a page."""
    from app.models.agent import Agent as AgentModel

    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")

    # Approved proposals for this page
    approved = (
        db.query(EditProposal)
        .filter(EditProposal.page_id == page.id, EditProposal.status == EditStatus.APPROVED)
        .all()
    )

    # Build contributor list
    contrib_map: dict[int, dict] = {}
    for proposal in approved:
        aid = proposal.agent_id
        if aid not in contrib_map:
            agent = db.query(AgentModel).get(aid)
            if agent:
                contrib_map[aid] = {
                    "id": agent.id,
                    "name": agent.name,
                    "model_name": agent.model_name,
                    "role": agent.role,
                    "specialty": agent.specialty,
                    "edit_count": 0,
                }
        if aid in contrib_map:
            contrib_map[aid]["edit_count"] += 1

    contributors = sorted(contrib_map.values(), key=lambda x: x["edit_count"], reverse=True)

    # Recent 5 versions with reviewer opinions
    versions = (
        db.query(PageVersion)
        .filter(PageVersion.page_id == page.id)
        .order_by(PageVersion.version_num.desc())
        .limit(5)
        .all()
    )

    # For each version, find the approved proposal at that point and its votes
    history = []
    for v in versions:
        reviews = []
        # Approved proposals near this version — match by position heuristically
        # We use approved proposals ordered by created_at, matching to version_num
        ap_for_ver = (
            db.query(EditProposal)
            .filter(EditProposal.page_id == page.id, EditProposal.status == EditStatus.APPROVED)
            .order_by(EditProposal.created_at.asc())
            .offset(max(0, v.version_num - 2))
            .limit(1)
            .first()
        )
        if ap_for_ver:
            votes = db.query(Vote).filter(Vote.edit_id == ap_for_ver.id).all()
            for vote in votes:
                reviewer = db.query(AgentModel).get(vote.agent_id)
                reviews.append({
                    "agent_name": reviewer.name if reviewer else f"Agent#{vote.agent_id}",
                    "specialty": reviewer.specialty if reviewer else None,
                    "value": vote.value,
                    "reason": vote.reason,
                })
        history.append({
            "version_num": v.version_num,
            "editor_agent_id": v.editor_agent_id,
            "reviews": reviews,
        })

    return {
        "contributors": contributors,
        "edit_history": history,
    }


@router.get("/{slug}/fact-sources", tags=["pages"],
    summary="Get fact source records for a page",
    description="Returns all FactSource rows for hero_facts on this page.")
def get_fact_sources(slug: str, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    from app.models.page import FactSource
    sources = db.query(FactSource).filter(FactSource.page_id == page.id).all()
    return [
        {
            "id": s.id,
            "fact_kind": s.fact_kind,
            "fact_index": s.fact_index,
            "source_tier": s.source_tier,
            "authority": s.authority,
            "reference_url": s.reference_url,
            "reference_title": s.reference_title,
            "retrieval_year": s.retrieval_year,
            "claim_id": s.claim_id,
            "trust_level_snapshot": s.trust_level_snapshot,
            "evidence_count_snapshot": s.evidence_count_snapshot,
            "representative_arxiv_id": s.representative_arxiv_id,
            "attribution": s.attribution,
            "flagged": s.flagged,
            "reason": s.reason,
        }
        for s in sources
    ]


@router.get("/{slug}/health",
    summary="Get page health score",
    description="Computes and returns the 6-dimension health score for a wiki page. Public read.")
def get_page_health(slug: str, db: Session = Depends(get_db)):
    import datetime as _dt
    from app.services.page_health import compute_health_score
    from app.models.page import WikiPage as _WikiPage
    page = db.query(_WikiPage).filter(_WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    if page.do_not_renovate:
        return {"score": None, "band": "Frozen", "emoji": "🔒", "note": "do_not_renovate=true"}
    result = compute_health_score(page, db)
    # Cache in wiki_pages
    page.health_score = result["score"]
    page.health_updated_at = _dt.datetime.utcnow()
    db.commit()
    return result


@router.post("/admin/renovation/queue/{slug}",
    summary="Manually queue a page for renovation")
def queue_renovation_manual(
    slug: str,
    x_admin_key: str = Header(...),
    db: Session = Depends(get_db),
):
    import os
    import secrets as _sec
    if not _sec.compare_digest(x_admin_key, os.environ.get("NM_ADMIN_KEY", "")):
        raise HTTPException(401, "Invalid admin key")
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    if page.do_not_renovate:
        raise HTTPException(409, "Page has do_not_renovate=true")
    from app.agent_loop.tasks import diagnose_page
    diagnose_page.delay(page.id)
    return {"queued": slug, "page_id": page.id}


@router.get("/{slug}/research-ideas",
    summary="Get research ideas for a wiki page",
    description="Returns AI-generated survey-anchored research ideas for the given wiki page slug.")
def get_page_research_ideas(
    slug: str,
    combo: str | None = None,
    sort: str = "novelty",
    page: int = 1,
    per_page: int = 20,
    db: Session = Depends(get_db),
):
    from sqlalchemy import text as _text
    import json as _json

    page_row = db.execute(_text("SELECT id FROM wiki_pages WHERE slug = :s"), {"s": slug}).fetchone()
    if page_row is None:
        raise HTTPException(404, f"Wiki page '{slug}' not found")

    conditions = (
        "ri.page_id = :pid AND ri.status NOT IN ('superseded', 'rejected', 'stale') "
        "AND (ri.coverage_status IS NULL OR ri.coverage_status IN ('screened_pass', 'partial', 'inconclusive'))"
    )
    params: dict = {"pid": page_row.id}

    if combo:
        conditions += " AND ri.survey_combo = :combo"
        params["combo"] = combo

    order_map = {
        "novelty": "ri.novelty DESC",
        "feasibility": "ri.feasibility DESC",
        "newest": "ri.created_at DESC",
    }
    order_clause = order_map.get(sort, "ri.novelty DESC")

    offset = (page - 1) * per_page

    try:
        total_row = db.execute(_text(
            f"SELECT count(*) FROM research_ideas ri WHERE {conditions}"
        ), params).scalar()
        rows = db.execute(_text(f"""
            SELECT ri.id, ri.survey_combo, ri.question, ri.why_now, ri.approach,
                   ri.systematics_json, ri.novelty, ri.feasibility, ri.status,
                   ri.model_chain, ri.saved_by_papa, ri.seeded,
                   ri.created_at, ri.updated_at, ri.last_seen_at,
                   ri.claim_id, ri.coverage_status, ri.closest_prior_work,
                   ri.coverage_checked_at, ri.factual_verification_notes
            FROM research_ideas ri
            WHERE {conditions}
            ORDER BY {order_clause}
            LIMIT :lim OFFSET :off
        """), {**params, "lim": per_page, "off": offset}).fetchall()
    except Exception:
        return {"page_slug": slug, "total": 0, "page": page, "per_page": per_page, "ideas": []}

    def _resolve_slugs(combo_str: str) -> dict:
        try:
            tokens = [t.strip() for t in combo_str.split("+")]
            result = {}
            for token in tokens:
                row = db.execute(
                    _text("SELECT slug FROM surveys WHERE UPPER(name)=UPPER(:t) OR UPPER(slug)=UPPER(:t)"),
                    {"t": token},
                ).fetchone()
                if row:
                    result[token] = row.slug
            return result
        except Exception:
            return {}

    ideas = []
    for r in rows:
        systematics = r.systematics_json if isinstance(r.systematics_json, list) else (
            _json.loads(r.systematics_json) if r.systematics_json else []
        )
        ideas.append({
            "id": r.id,
            "survey_combo": r.survey_combo,
            "question": r.question,
            "why_now": r.why_now,
            "approach": r.approach,
            "systematics": systematics,
            "novelty": float(r.novelty),
            "feasibility": float(r.feasibility),
            "status": r.status,
            "claim_id": getattr(r, "claim_id", None),
            "coverage_status": getattr(r, "coverage_status", None),
            "closest_prior_work": r.closest_prior_work if isinstance(getattr(r, "closest_prior_work", None), list) else (
                _json.loads(r.closest_prior_work) if getattr(r, "closest_prior_work", None) else []
            ),
            "coverage_checked_at": r.coverage_checked_at.isoformat() if getattr(r, "coverage_checked_at", None) else None,
            "display_badge": "unverified" if getattr(r, "coverage_status", None) in (None, "inconclusive") else None,
            "papers_checked": (r.factual_verification_notes or {}).get("papers_checked") if isinstance(getattr(r, "factual_verification_notes", None), dict) else None,
            "model_chain": r.model_chain,
            "saved_by_papa": r.saved_by_papa,
            "seeded": r.seeded,
            "survey_slugs": _resolve_slugs(r.survey_combo),
            "created_at": r.created_at.isoformat() if r.created_at else None,
            "updated_at": r.updated_at.isoformat() if r.updated_at else None,
            "last_seen_at": r.last_seen_at.isoformat() if r.last_seen_at else None,
        })

    return {
        "page_slug": slug,
        "total": total_row or 0,
        "page": page,
        "per_page": per_page,
        "ideas": ideas,
    }
