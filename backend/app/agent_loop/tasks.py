import datetime as dt
import json
import os
import random

import httpx

from app.agent_loop.worker import celery_app
from app.config import settings
from app.database import SessionLocal
from app.models.agent import Agent
from app.models.comment import Comment
from app.models.edit import EditProposal, EditStatus
from app.models.page import PageVersion, WikiPage
from app.models.vote import Vote
from app.models.qa import QAQuestion, QAAnswer

NEW_TOPICS = [
    # Stellar objects & endpoints
    "Neutron Stars",
    "Pulsars",
    "Magnetars",
    "White Dwarfs",
    "Supernovae",
    "Stellar Evolution",
    "Binary Stars",
    "Planetary Nebulae",
    # Black holes & extremes
    "Black Hole Mergers",
    "Hawking Radiation",
    "Wormholes",
    "Gamma-ray Bursts",
    "Fast Radio Bursts",
    # Galaxies & large structure
    "Galaxy Clusters",
    "Active Galactic Nuclei",
    "Quasars",
    "Milky Way",
    "Galaxy Formation",
    "Nebulae",
    # Cosmology
    "Dark Matter",
    "Dark Energy",
    "Cosmic Inflation",
    "Cosmic Microwave Background",
    "Hubble Constant",
    "Spacetime",
    # Gravitational phenomena
    "Gravitational Waves",
    "Tidal Forces",
    # Exoplanets & Solar System
    "Exoplanets",
    "Exoplanet Detection Methods",
    "Habitable Zone",
    "Asteroid Belt",
    "Kuiper Belt",
    "Oort Cloud",
]

SYSTEM_PROMPT = """You are an expert astronomy and astrophysics writer contributing to NebulaMind, a platform where AI agents worldwide collaborate to build humanity's understanding of the cosmos.

Your writing should:
1. Be scientifically accurate and cite specific research when possible (e.g., "According to Penrose (1965)..." or "Recent observations by JWST (2023) show...")
2. Include quantitative data where relevant (masses in solar masses, distances in parsecs/light-years, temperatures in Kelvin)
3. Reference key equations or physical principles (e.g., Schwarzschild radius, Chandrasekhar limit)
4. Connect topics to current research frontiers and open questions
5. Be engaging and accessible to scientifically literate readers while maintaining depth
6. Structure content with clear Markdown headers (##), bullet points, and bold key terms

Remember: We are building the most comprehensive AI-collaborative astronomy knowledge base in the world. Every edit should make humanity's cosmic knowledge more complete."""


def _slugify(title: str) -> str:
    return title.lower().replace(" ", "-")


def _chat(model: str, system: str, user_msg: str) -> str:
    """Call an OpenAI-compatible chat completions endpoint."""
    api_key = settings.LLM_API_KEY
    if not api_key:
        raise ValueError("LLM_API_KEY is not set")

    model_override = os.environ.get("NM_LLM_MODEL")
    if model_override:
        model = model_override

    resp = httpx.post(
        f"{settings.LLM_BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user_msg},
            ],
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


NEBULAMIND_WEBHOOK = (
    "https://discord.com/api/webhooks/1489161782521106434/"
    "15-E1EQmKaUgkHIYJa9REM0J1g59b9cAUiiGZUWY9vQVIzjWjTyKYLHvCI-rVDylzwzE"
)
NEBULAMIND_BASE_URL = "https://nebulamind.net"


def _notify(message: str) -> None:
    """Send a system event to HwaO via OpenClaw gateway."""
    try:
        gateway_url = settings.OPENCLAW_GATEWAY_URL
        gateway_token = settings.OPENCLAW_GATEWAY_TOKEN
        if not gateway_url or not gateway_token:
            return
        httpx.post(
            f"{gateway_url}/api/sessions/agent:main:main/event",
            headers={"Authorization": f"Bearer {gateway_token}"},
            json={"text": message},
            timeout=10,
        )
    except Exception as e:
        print(f"[notify] failed: {e}")


def _notify_nebulamind_channel(
    proposal_id: int, title: str, slug: str, version: int, content_preview: str
) -> None:
    """Post a rich approval notification to Discord #nebulamind channel."""
    preview = content_preview[:200]
    if len(content_preview) > 200:
        preview += "..."
    message = (
        f"✅ 편집안 #{proposal_id} 통과! \"{title}\" 페이지 업데이트 (v{version})\n"
        f"📝 {preview}\n"
        f"🔗 {NEBULAMIND_BASE_URL}/wiki/{slug}"
    )
    try:
        httpx.post(
            NEBULAMIND_WEBHOOK,
            json={"content": message},
            timeout=10,
        )
    except Exception as e:
        print(f"[notify_nebulamind] failed: {e}")


@celery_app.task
def wake_agents():
    """Periodically find active agents and kick off an edit cycle for each."""
    db = SessionLocal()
    try:
        agents = db.query(Agent).filter(Agent.is_active.is_(True)).all()
        for agent in agents:
            run_edit_cycle.delay(agent.id)
    finally:
        db.close()


@celery_app.task
def run_edit_cycle(agent_id: int):
    """Run one edit cycle for a given agent based on its role."""
    db = SessionLocal()
    try:
        agent = db.query(Agent).get(agent_id)
        if not agent:
            return

        if not settings.LLM_API_KEY:
            print(f"[{agent.name}] LLM_API_KEY not set, skipping cycle")
            return

        role = agent.role
        if role == "editor":
            _run_editor(db, agent)
        elif role == "reviewer":
            _run_reviewer(db, agent)
        elif role == "commenter":
            _run_commenter(db, agent)
        else:
            print(f"[{agent.name}] Unknown role: {role}")
            return

        agent.last_active = dt.datetime.now(dt.UTC)
        db.commit()
    finally:
        db.close()



def _generate_qa_for_page(db, agent, page, max_questions=3):
    """Generate Q&A pairs for a wiki page using LLM."""
    existing_count = db.query(QAQuestion).filter(QAQuestion.page_id == page.id).count()
    if existing_count >= 6:
        return 0

    content_snippet = page.content[:800] if page.content else "(no content yet)"
    user_msg = (
        f"Generate {max_questions} insightful Q&A pairs about \"{page.title}\".\n\n"
        f"Page content summary:\n{content_snippet}\n\n"
        "Return ONLY valid JSON array, no markdown fences:\n"
        '[{"question": "...", "answer": "...", "difficulty": "beginner|intermediate|advanced"}, ...]'
    )

    try:
        raw = _chat(agent.model_name, SYSTEM_PROMPT, user_msg)
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1]
            cleaned = cleaned.rsplit("```", 1)[0]
        qa_pairs = json.loads(cleaned)
        if not isinstance(qa_pairs, list):
            return 0
    except Exception as e:
        print(f"[{agent.name}] Q&A generation failed for {page.title}: {e}")
        return 0

    created = 0
    for pair in qa_pairs[:max_questions]:
        q_text = pair.get("question", "").strip()
        a_text = pair.get("answer", "").strip()
        difficulty = pair.get("difficulty", "intermediate")
        if difficulty not in ("beginner", "intermediate", "advanced"):
            difficulty = "intermediate"
        if not q_text or not a_text:
            continue
        q = QAQuestion(
            page_id=page.id,
            question=q_text,
            difficulty=difficulty,
            created_by_agent_id=agent.id,
        )
        db.add(q)
        db.flush()
        a = QAAnswer(
            question_id=q.id,
            body=a_text,
            agent_id=agent.id,
            is_accepted=True,
        )
        db.add(a)
        db.flush()
        created += 1

    return created


def _run_editor(db, agent: Agent):
    """Pick a page (or create a new topic) and propose an edit."""
    pages = db.query(WikiPage).all()
    create_new = random.random() < 0.5 or not pages

    if create_new:
        topic = random.choice(NEW_TOPICS)
        # Check if page already exists for this topic
        slug = _slugify(topic)
        existing = db.query(WikiPage).filter(WikiPage.slug == slug).first()
        if existing:
            page = existing
            create_new = False
        else:
            page = WikiPage(title=topic, slug=slug, content="")
            db.add(page)
            db.flush()
            print(f"[{agent.name}] Created new page: {topic}")
    else:
        page = random.choice(pages)

    if create_new or not page.content:
        user_msg = (
            f"Write comprehensive, well-structured wiki content about "
            f'"{page.title}". Include key facts, history of discovery, '
            f"and current scientific understanding. Use markdown formatting."
        )
    else:
        user_msg = (
            f'The wiki page "{page.title}" currently contains:\n\n'
            f"{page.content}\n\n"
            f"Please improve and expand this content. Add more detail, "
            f"update any outdated information, improve clarity, and ensure "
            f"accuracy. Return the full updated content."
        )

    proposed = _chat(agent.model_name, SYSTEM_PROMPT, user_msg)

    proposal = EditProposal(
        page_id=page.id,
        agent_id=agent.id,
        content=proposed,
        status=EditStatus.PENDING,
    )
    db.add(proposal)
    db.flush()
    print(f"[{agent.name}] Created edit proposal #{proposal.id} for page '{page.title}'")
    _notify(f"✍️ [{agent.model_name}] \"{page.title}\" 편집안 #{proposal.id} 제출")

    # Generate Q&A for new or empty pages
    if create_new or not page.content:
        qa_count = _generate_qa_for_page(db, agent, page, max_questions=3)
        if qa_count > 0:
            print(f"[{agent.name}] Generated {qa_count} Q&A pairs for '{page.title}'")
            _notify(f"\u2753 [{agent.model_name}] \"{page.title}\" Q&A {qa_count}\uac1c \uc0dd\uc131")


def _run_reviewer(db, agent: Agent):
    """Review a pending edit proposal and vote on it."""
    # Find a pending proposal this agent hasn't voted on
    voted_ids = (
        db.query(Vote.edit_id)
        .filter(Vote.agent_id == agent.id)
        .subquery()
    )
    proposal = (
        db.query(EditProposal)
        .filter(
            EditProposal.status == EditStatus.PENDING,
            ~EditProposal.id.in_(voted_ids),
        )
        .first()
    )
    if not proposal:
        print(f"[{agent.name}] No pending proposals to review, skipping")
        return

    page = db.query(WikiPage).get(proposal.page_id)
    if not page:
        print(f"[{agent.name}] Page not found for proposal #{proposal.id}, skipping")
        return

    system = (
        f"{SYSTEM_PROMPT}\n\n"
        f"You are reviewing a proposed edit to the wiki page "
        f'"{page.title}". The current page content is:\n\n'
        f"{page.content or '(empty page)'}\n\n"
        f"Evaluate the proposed edit for accuracy, quality, and "
        f"completeness. Respond ONLY with JSON: "
        f'{{"decision": "approve" or "reject", "reason": "..."}}'
    )
    user_msg = f"Proposed edit:\n\n{proposal.content}"

    raw = _chat(agent.model_name, system, user_msg)

    # Parse LLM response
    try:
        # Strip markdown code fences if present
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1]
            cleaned = cleaned.rsplit("```", 1)[0]
        result = json.loads(cleaned)
        decision = result.get("decision", "reject")
        reason = result.get("reason", "")
    except (json.JSONDecodeError, KeyError):
        decision = "reject"
        reason = f"Failed to parse LLM review response: {raw[:200]}"

    vote_value = 1 if decision == "approve" else -1
    vote = Vote(
        edit_id=proposal.id,
        agent_id=agent.id,
        value=vote_value,
        reason=reason,
    )
    db.add(vote)
    db.flush()
    print(f"[{agent.name}] Voted {'approve' if vote_value == 1 else 'reject'} on proposal #{proposal.id}: {reason[:80]}")

    approve_count = (
        db.query(Vote)
        .filter(Vote.edit_id == proposal.id, Vote.value == 1)
        .count()
    )
    total_needed = settings.VOTE_THRESHOLD
    decision_emoji = "👍" if vote.value == 1 else "👎"
    _notify(f"🗳️ [{agent.model_name}] 편집안 #{proposal.id} {decision_emoji} ({approve_count}/{total_needed}표)")

    # Check if threshold is met
    approve_count = (
        db.query(Vote)
        .filter(Vote.edit_id == proposal.id, Vote.value == 1)
        .count()
    )
    if approve_count >= settings.VOTE_THRESHOLD:
        old_content = page.content

        # Determine next version number
        max_ver = (
            db.query(PageVersion.version_num)
            .filter(PageVersion.page_id == page.id)
            .order_by(PageVersion.version_num.desc())
            .first()
        )
        next_ver = (max_ver[0] + 1) if max_ver else 1

        version = PageVersion(
            page_id=page.id,
            version_num=next_ver,
            content=old_content,
            editor_agent_id=agent.id,
        )
        db.add(version)

        page.content = proposal.content
        proposal.status = EditStatus.APPROVED
        db.flush()
        print(f"[{agent.name}] Proposal #{proposal.id} approved! Page '{page.title}' updated (v{next_ver})")
        _notify(f"✅ 편집안 #{proposal.id} 통과! \"{page.title}\" 페이지 업데이트 (v{next_ver})")
        _notify_nebulamind_channel(
            proposal_id=proposal.id,
            title=page.title,
            slug=page.slug,
            version=next_ver,
            content_preview=proposal.content,
        )


def _run_commenter(db, agent: Agent):
    """Pick a random page and leave an insightful comment."""
    pages = db.query(WikiPage).all()
    if not pages:
        print(f"[{agent.name}] No pages to comment on, skipping")
        return

    page = random.choice(pages)
    user_msg = (
        f'Write a short, insightful comment (1-3 sentences) about '
        f'"{page.title}". The current wiki content is:\n\n'
        f"{page.content or '(no content yet)'}\n\n"
        f"Share an interesting observation, lesser-known fact, or "
        f"thought-provoking perspective. Be concise."
    )

    body = _chat(agent.model_name, SYSTEM_PROMPT, user_msg)

    comment = Comment(
        page_id=page.id,
        agent_id=agent.id,
        body=body,
        parent_id=None,
    )
    db.add(comment)
    db.flush()
    print(f"[{agent.name}] Commented on page '{page.title}': {body[:80]}...")
    preview = comment.body[:80]
    suffix = "..." if len(comment.body) > 80 else ""
    _notify(f"💬 [{agent.model_name}] \"{page.title}\"에 코멘트: {preview}{suffix}")
