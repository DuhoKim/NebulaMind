from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.page import WikiPage
from app.agent_loop.tasks import _chat

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
def ask(body: ChatRequest, db: Session = Depends(get_db)):
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

    # Build history text (last 4 messages)
    history_text = ""
    for msg in body.history[-4:]:
        history_text += f"\n{msg.role.upper()}: {msg.content}"

    full_user_msg = (
        f"{history_text}\nUSER: {body.question}" if history_text else body.question
    )

    try:
        answer = _chat("llama3.1-8b", system_prompt, full_user_msg)
    except Exception as e:
        answer = f"Sorry, I couldn't process your question right now. Error: {str(e)[:100]}"

    return ChatResponse(
        answer=answer,
        references=[ReferencePage(title=p.title, slug=p.slug) for p in relevant],
    )
