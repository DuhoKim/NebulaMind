"""Grounded Chat API — Phase 2 (non-streaming + SSE streaming)."""
import json
import re
import urllib.request
from typing import Optional

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth import optional_api_key
from app.models.agent import Agent
from app.services.chat_retrieve import retrieve_grounding, GroundedClaim, ASTRO_KEYWORDS
from app.services.chat_intent import classify_intent
from app.config import settings

router = APIRouter(prefix="/api/chat", tags=["chat"])

TRUST_EMOJI = {
    "consensus": "🟢",
    "accepted": "⚪",
    "debated": "🟠",
    "challenged": "🔴",
    "unverified": "❓",
}

SYNTHESIS_SYSTEM = """You are NebulaMind, an astronomy chat assistant grounded in peer-reviewed sources.

RULES:
- Answer ONLY using the supplied numbered claims. Cite inline as [N] after each fact.
- Include the trust level in citations: [1, accepted] or [2, consensus] etc.
- If claims don't fully cover the question, say so honestly.
- Never invent facts. Only use what's in the supplied claims.
- Concise answers: 3-6 sentences for definitions, 6-10 for explanations.
- If claims show debate/disagreement, present BOTH sides fairly.
- End with a "Sources:" section listing each cited claim with its paper info.

ABSTENTION: If you cannot answer from the supplied claims, respond with exactly:
ABSTAIN: <one sentence on what's missing>
"""

REFUSE_RESPONSE = {
    "answer": (
        "I focus exclusively on astronomy and astrophysics. "
        "For other topics, I'm not the right assistant. "
        "Ask me about black holes, galaxies, dark matter, neutron stars, or any other astronomy topic!"
    ),
    "grounding_strength": "n/a",
    "citations": [],
    "suggested_pages": [],
    "abstain": False,
    "register_cta": False,
}

ABSTAIN_TEMPLATE = (
    "The NebulaMind council hasn't built strong consensus on this specific question yet.\n\n"
    "{hint}\n\n"
    "You can help! Register your AI agent at nebulamind.net/council to propose evidence "
    "and vote on existing claims. The first agent to add a quality-vetted paper on this topic "
    "helps unlock the answer."
)


def _rate_limit_check(request: Request) -> bool:
    """Returns True if request is allowed, False if rate-limited."""
    try:
        import redis as _redis_lib
        rc = _redis_lib.from_url(settings.REDIS_URL, decode_responses=True)
        ip = request.headers.get("X-Forwarded-For", "").split(",")[0].strip() or (
            request.client.host if request.client else "unknown"
        )
        key = f"nm:chat:anon:{ip}"
        count = int(rc.get(key) or 0)
        if count >= 30:  # 30/hour per IP
            return False
        pipe = rc.pipeline()
        pipe.incr(key)
        pipe.expire(key, 3600)
        pipe.execute()
        return True
    except Exception:
        return True  # Redis unavailable → allow


def _call_ollama(model: str, system: str, user: str) -> str:
    """Single Ollama call for synthesis."""
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(
        "http://localhost:11434/v1/chat/completions",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=90) as r:
        content = json.loads(r.read())["choices"][0]["message"]["content"]
        return re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()


def _build_prompt(question: str, grounded: list[GroundedClaim], history: list) -> str:
    history_text = "\n".join(
        f"{m.get('role', 'user').upper()}: {m.get('content', '')}"
        for m in (history or [])[-4:]
    )

    claims_block = ""
    for i, gc in enumerate(grounded, 1):
        ev_lines = "\n".join(
            f"  - {e.title[:80]} ({e.year or 'n.d.'}) "
            f"{'arXiv:' + e.arxiv_id if e.arxiv_id else ('DOI:' + e.doi if e.doi else 'no citation')}"
            for e in gc.evidence[:2]
        )
        badge = TRUST_EMOJI.get(gc.trust_level, "❓")
        claims_block += (
            f"[{i}] {badge} trust={gc.trust_level}, page={gc.page_title}\n"
            f"  Claim: {gc.claim_text}\n"
            f"  Evidence:\n{ev_lines}\n\n"
        )

    return (
        (f"Prior conversation:\n{history_text}\n\n" if history_text else "")
        + f"Question: {question}\n\n"
        + f"Available grounded claims:\n{claims_block}"
        + "Answer using ONLY these claims. Cite inline as [N, trust_level]."
    )


def _parse_response(raw: str, grounded: list[GroundedClaim]) -> dict:
    if raw.startswith("ABSTAIN:"):
        return {
            "answer": ABSTAIN_TEMPLATE.format(hint=raw[8:].strip()),
            "abstain": True,
            "citations": {},
            "grounding_strength": "low",
            "register_cta": True,
        }

    # Extract citations [N, badge]
    citations = {}
    for m in re.finditer(r"\[(\d+),?\s*(consensus|accepted|debated|challenged)?\]", raw):
        n = int(m.group(1))
        if 1 <= n <= len(grounded):
            gc = grounded[n - 1]
            citations[str(n)] = {
                "claim_id": gc.claim_id,
                "claim_text": gc.claim_text[:150],
                "trust_level": gc.trust_level,
                "page_slug": gc.page_slug,
                "page_title": gc.page_title,
                "evidence": [
                    {
                        "title": e.title[:80],
                        "arxiv_id": e.arxiv_id,
                        "doi": e.doi,
                        "year": e.year,
                        "quality": e.quality,
                        "n_jury_votes": e.n_jury_votes,
                    }
                    for e in gc.evidence[:2]
                ],
            }

    n_consensus = sum(
        1 for c in grounded
        if c.trust_level == "consensus" and str(grounded.index(c) + 1) in citations
    )
    n_total = len(citations)
    if n_total == 0:
        strength = "low"
    elif n_consensus >= 1:
        strength = "high"
    else:
        strength = "medium"

    return {
        "answer": raw,
        "abstain": False,
        "citations": citations,
        "grounding_strength": strength,
        "register_cta": strength in ("low", "medium"),
    }


class ChatRequest(BaseModel):
    question: str
    history: list = []


class ChatMessage(BaseModel):
    role: str
    content: str


class ReferencePage(BaseModel):
    title: str
    slug: str


@router.post("/ask")
def ask(
    body: ChatRequest,
    request: Request,
    db: Session = Depends(get_db),
    agent: Optional[Agent] = Depends(optional_api_key),
):
    # Anonymous rate limit: 30/hour/IP
    if not agent and not _rate_limit_check(request):
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit: 30 chats/hour for anonymous users. Register an agent for unlimited access."},
            headers={"Retry-After": "3600"},
        )

    # Intent classification
    intent = classify_intent(body.question)
    if intent.mode == "refuse":
        return JSONResponse(REFUSE_RESPONSE)

    # Claim-level retrieval
    grounded = retrieve_grounding(body.question, db, top_k=8)

    # Low grounding → abstain
    if not grounded or all(g.relevance < 0.10 for g in grounded):
        suggested = list({(g.page_slug, g.page_title) for g in grounded[:3]}) if grounded else []
        return JSONResponse({
            "answer": ABSTAIN_TEMPLATE.format(
                hint=f"Your question about '{body.question[:60]}' hasn't been deeply covered by our council yet."
            ),
            "grounding_strength": "low",
            "citations": {},
            "suggested_pages": [{"slug": s, "title": t} for s, t in suggested],
            "abstain": True,
            "register_cta": True,
        })

    # Synthesize
    prompt = _build_prompt(body.question, grounded, body.history)
    try:
        raw = _call_ollama("gemma3:27b", SYNTHESIS_SYSTEM, prompt)
    except Exception:
        # Fallback to larger model
        try:
            raw = _call_ollama("llama3.3:70b", SYNTHESIS_SYSTEM, prompt)
        except Exception:
            raw = (
                "Sorry, synthesis is temporarily unavailable. Here are relevant claims:\n\n"
                + "\n".join(f"• {g.claim_text[:100]}" for g in grounded[:3])
            )

    result = _parse_response(raw, grounded)
    result["suggested_pages"] = [
        {"slug": g.page_slug, "title": g.page_title}
        for g in grounded[:3]
        if g.page_slug
    ]

    return JSONResponse(result)


# Keep backward compat — legacy GET endpoint
@router.get("/ask")
def ask_get(q: str, db: Session = Depends(get_db)):
    return ask(ChatRequest(question=q), request=None, db=db, agent=None)


@router.get("/stream")
async def stream_ask(
    q: str,
    request: Request,
    db: Session = Depends(get_db),
    agent: Optional[Agent] = Depends(optional_api_key),
):
    """Streaming SSE version of /ask. Returns chunks then a final JSON event."""
    # Rate limit (same as POST)
    if not agent and not _rate_limit_check(request):
        async def rate_limit_gen():
            yield f"data: {json.dumps({'error': 'Rate limit exceeded', 'retry_after': 3600})}\n\n"
            yield "data: [DONE]\n\n"
        return StreamingResponse(rate_limit_gen(), media_type="text/event-stream")

    intent = classify_intent(q)
    if intent.mode == "refuse":
        async def refuse_gen():
            yield f"data: {json.dumps({'chunk': REFUSE_RESPONSE['answer']})}\n\n"
            yield f"data: {json.dumps({'final': REFUSE_RESPONSE})}\n\n"
            yield "data: [DONE]\n\n"
        return StreamingResponse(refuse_gen(), media_type="text/event-stream")

    grounded = retrieve_grounding(q, db, top_k=8)

    if not grounded or all(g.relevance < 0.10 for g in grounded):
        abstain_msg = ABSTAIN_TEMPLATE.format(
            hint=f"Your question about '{q[:60]}' hasn't been deeply covered by our council yet."
        )
        async def abstain_gen():
            yield f"data: {json.dumps({'chunk': abstain_msg})}\n\n"
            yield f"data: {json.dumps({'final': {'answer': abstain_msg, 'grounding_strength': 'low', 'citations': {}, 'abstain': True, 'register_cta': True}})}\n\n"
            yield "data: [DONE]\n\n"
        return StreamingResponse(abstain_gen(), media_type="text/event-stream")

    prompt = _build_prompt(q, grounded, [])

    async def stream_gen():
        payload = json.dumps({
            "model": "gemma3:27b",
            "messages": [
                {"role": "system", "content": SYNTHESIS_SYSTEM},
                {"role": "user", "content": prompt},
            ],
            "stream": True,
            "temperature": 0.2,
        }).encode()

        chunks = []
        try:
            import urllib.request as _urlreq
            req = _urlreq.Request(
                "http://localhost:11434/v1/chat/completions",
                data=payload,
                headers={"Content-Type": "application/json"},
            )
            with _urlreq.urlopen(req, timeout=120) as resp:
                for line in resp:
                    line = line.decode("utf-8").strip()
                    if not line.startswith("data:"):
                        continue
                    data_str = line[5:].strip()
                    if data_str == "[DONE]":
                        break
                    try:
                        data = json.loads(data_str)
                        delta = data.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        if delta:
                            chunks.append(delta)
                            yield f"data: {json.dumps({'chunk': delta})}\n\n"
                    except Exception:
                        continue
        except Exception:
            # Fallback: non-streaming call
            try:
                raw = _call_ollama("gemma3:27b", SYNTHESIS_SYSTEM, prompt)
            except Exception:
                raw = "\n".join(f"• {g.claim_text[:100]}" for g in grounded[:3])
            yield f"data: {json.dumps({'chunk': raw})}\n\n"
            chunks = [raw]

        # Final structured event
        full_text = "".join(chunks)
        result = _parse_response(full_text, grounded)
        result["suggested_pages"] = [
            {"slug": g.page_slug, "title": g.page_title}
            for g in grounded[:3] if g.page_slug
        ]
        yield f"data: {json.dumps({'final': result})}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        stream_gen(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


class ChatFeedbackRequest(BaseModel):
    question: str
    answer: str
    grounding_strength: str
    cited_claim_ids: list[int]
    page_slug: str | None = None
    agent_api_key: str | None = None


@router.post("/propose-edit")
def propose_edit_from_chat(
    body: ChatFeedbackRequest,
    db: Session = Depends(get_db),
):
    """Promote a high-quality grounded chat answer as a wiki edit proposal.
    
    Only accepts high-grounding answers. Creates an EditProposal on the
    most-cited page, attributed to the calling agent or a generic ChatBot.
    """
    from app.models.page import WikiPage
    from app.models.claim import Claim
    from app.models.edit import EditProposal
    from app.models.agent import Agent

    if body.grounding_strength not in ("high",):
        return JSONResponse(
            status_code=400,
            content={"error": "Only high-grounding answers can be promoted to wiki edits."}
        )

    if not body.answer or len(body.answer) < 50:
        return JSONResponse(status_code=400, content={"error": "Answer too short."})

    # Find the page to edit
    page = None
    if body.page_slug:
        page = db.query(WikiPage).filter(WikiPage.slug == body.page_slug).first()

    if not page and body.cited_claim_ids:
        # Use the page of the first cited claim
        claim = db.query(Claim).get(body.cited_claim_ids[0])
        if claim:
            page = db.query(WikiPage).get(claim.page_id)

    if not page:
        return JSONResponse(status_code=404, content={"error": "Could not identify target page."})

    # Find or create ChatBot agent
    agent = None
    if body.agent_api_key:
        agent = db.query(Agent).filter(Agent.api_key == body.agent_api_key).first()
    if not agent:
        agent = db.query(Agent).filter(Agent.name == "ChatBot").first()
    if not agent:
        agent = db.query(Agent).filter(Agent.name.ilike("%chat%")).first()
    if not agent:
        agent = db.query(Agent).first()

    # Format the edit content
    content = (
        f"**Q: {body.question}**\n\n"
        f"{body.answer}\n\n"
        f"*Promoted from NebulaMind Chat — grounding: {body.grounding_strength}*"
    )

    proposal = EditProposal(
        page_id=page.id,
        agent_id=agent.id if agent else None,
        content=content,
        summary=f"Chat answer promoted to wiki: {body.question[:80]}",
    )
    db.add(proposal)
    db.commit()

    return {
        "status": "proposed",
        "proposal_page": page.title,
        "proposal_slug": page.slug,
        "message": f"Your answer has been proposed as an edit to '{page.title}'. It will be reviewed by the council.",
    }
