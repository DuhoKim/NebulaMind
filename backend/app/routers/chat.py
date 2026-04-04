import httpx
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.page import WikiPage
from app.config import settings

router = APIRouter(prefix="/api/chat", tags=["chat"])


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    question: str
    history: list[ChatMessage] = []


class ReferencePage(BaseModel):
    title: str
    slug: str


class ChatResponse(BaseModel):
    answer: str
    references: list[ReferencePage]


def _search_pages(question: str, pages: list[WikiPage], top_k: int = 3) -> list[WikiPage]:
    words = [w.lower() for w in question.split() if len(w) > 2]
    scored: list[tuple[WikiPage, int]] = []
    for p in pages:
        text = (p.title + " " + p.content).lower()
        score = sum(text.count(w) for w in words)
        if score > 0:
            scored.append((p, score))
    scored.sort(key=lambda x: x[1], reverse=True)
    return [p for p, _ in scored[:top_k]]


@router.post("/ask", response_model=ChatResponse)
async def ask(body: ChatRequest, db: Session = Depends(get_db)):
    pages = db.query(WikiPage).all()
    relevant = _search_pages(body.question, pages)

    context_parts = []
    for p in relevant:
        snippet = p.content[:500] if p.content else ""
        context_parts.append(f"## {p.title}\n{snippet}")
    context = "\n\n".join(context_parts)

    system_prompt = (
        "You are NebulaMind, an astronomy knowledge assistant. "
        "Answer questions using the provided wiki context. "
        "Be concise and accurate. If you don't know, say so.\n\n"
        f"--- Wiki Context ---\n{context}\n--- End Context ---"
    )

    messages = [{"role": "system", "content": system_prompt}]
    for msg in body.history:
        messages.append({"role": msg.role, "content": msg.content})
    messages.append({"role": "user", "content": body.question})

    if not settings.LLM_API_KEY:
        return ChatResponse(
            answer="LLM API key not configured. Please set NM_LLM_API_KEY.",
            references=[ReferencePage(title=p.title, slug=p.slug) for p in relevant],
        )

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(
                f"{settings.LLM_BASE_URL}/chat/completions",
                headers={"Authorization": f"Bearer {settings.LLM_API_KEY}"},
                json={
                    "model": settings.LLM_MODEL or "gpt-4o-mini",
                    "messages": messages,
                    "max_tokens": 1024,
                },
            )
            resp.raise_for_status()
            data = resp.json()
            answer = data["choices"][0]["message"]["content"]
    except Exception as e:
        answer = f"Error calling LLM: {e}"

    return ChatResponse(
        answer=answer,
        references=[ReferencePage(title=p.title, slug=p.slug) for p in relevant],
    )
