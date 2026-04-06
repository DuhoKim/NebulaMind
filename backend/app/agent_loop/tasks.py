import datetime as dt
import json
import os
import random
import time

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

## Required Article Structure

Every wiki article MUST follow this Wikipedia-style section structure:

```
## Overview
Brief introduction and significance of the topic.

## Discovery & History
Historical context, key discoveries, and scientists involved.

## Physical Properties
Quantitative data, measurements, key equations, and observable characteristics.

## Current Research
Recent findings, ongoing studies, and state-of-the-art understanding.

## Open Questions
Unresolved mysteries, active debates, and future research directions.

## References
Key papers, missions, and sources (e.g., "Penrose, R. (1965). Gravitational Collapse and Space-Time Singularities.")
```

## Writing Standards

1. **Scientific accuracy**: Cite specific research (e.g., "According to Penrose (1965)..." or "Recent JWST observations (2023) show...")
2. **Quantitative data**: Include masses in solar masses (M☉), distances in parsecs/light-years, temperatures in Kelvin
3. **Key equations**: Reference physical principles (Schwarzschild radius, Chandrasekhar limit, etc.)
4. **Research frontiers**: Connect to open questions and current investigations
5. **Accessibility**: Engaging for scientifically literate readers while maintaining depth
6. **Attribution**: Always begin your article with a brief note identifying your perspective, e.g.: *[Written from a {specialty} astronomy perspective by {model_name}]*

## Specialty-Based Emphasis

Your writing emphasis depends on your astronomical specialty:
- **observational**: Prioritize telescope data, observational techniques, instrument specifications, and empirical measurements
- **theoretical**: Emphasize mathematical frameworks, physical laws, theoretical models, and predictive power
- **computational**: Focus on simulation results, numerical methods, computational models, and data analysis pipelines
- **cosmology**: Connect topics to large-scale structure, cosmic evolution, and the universe's origin and fate
- **stellar**: Emphasize stellar physics, stellar populations, stellar evolution, and the role of stars in galactic ecology
- **galactic**: Focus on galactic dynamics, structure, formation, and the Milky Way's place in the cosmos

Remember: We are building the most comprehensive AI-collaborative astronomy knowledge base in the world. Every edit should make humanity's cosmic knowledge more complete."""


SPECIALTY_EMPHASIS = {
    "observational": (
        "Focus on observational data, telescope instruments, detection methods, "
        "and empirical measurements. Reference specific observatories and surveys."
    ),
    "theoretical": (
        "Emphasize theoretical frameworks, mathematical models, key equations, "
        "and the predictive power of physical laws."
    ),
    "computational": (
        "Highlight simulation results, numerical methods, computational models, "
        "and data analysis pipelines and their implications."
    ),
    "cosmology": (
        "Connect the topic to large-scale cosmic structure, the universe's evolution, "
        "and its origin and ultimate fate."
    ),
    "stellar": (
        "Emphasize stellar physics, stellar populations, stellar evolution stages, "
        "and how stars shape the galactic ecosystem."
    ),
    "galactic": (
        "Focus on galactic dynamics, structure, formation history, and the Milky Way's "
        "place within the larger cosmic context."
    ),
}


def _build_system_prompt(agent: Agent) -> str:
    """Build a specialty-aware system prompt for the given agent."""
    specialty = agent.specialty or "general"
    model_name = agent.model_name

    base = SYSTEM_PROMPT.replace("{specialty}", specialty).replace("{model_name}", model_name)

    if specialty in SPECIALTY_EMPHASIS:
        base += f"\n\n## Your Specialty Focus ({specialty})\n{SPECIALTY_EMPHASIS[specialty]}"

    return base


def _slugify(title: str) -> str:
    return title.lower().replace(" ", "-")


_CHAT_MAX_WAIT = 30  # seconds — cap retry-after so threads don't block for minutes

# ---------------------------------------------------------------------------
# LLM provider fallback chain
# Each entry: (base_url, api_key_env, model_name_or_env, label)
# Tried in order; if a provider returns 429 with retry-after > _CHAT_MAX_WAIT
# (daily limit), we skip to the next provider instead of blocking.
# ---------------------------------------------------------------------------
def _build_provider_chain():
    """Build the ordered list of LLM providers from env vars."""
    chain = []

    # 1. Primary: Groq (from settings / env)
    groq_key = settings.LLM_API_KEY
    groq_url = settings.LLM_BASE_URL
    groq_model = os.environ.get("NM_LLM_MODEL", "llama-3.3-70b-versatile")
    if groq_key:
        chain.append({
            "base_url": groq_url,
            "api_key": groq_key,
            "model": groq_model,
            "label": "groq",
        })

    # 2. Fallback: Cerebras
    cerebras_key = settings.CEREBRAS_API_KEY
    if cerebras_key:
        chain.append({
            "base_url": "https://api.cerebras.ai/v1",
            "api_key": cerebras_key,
            "model": settings.CEREBRAS_MODEL or "llama3.1-8b",
            "label": "cerebras",
        })

    # 3. Fallback: SambaNova
    samba_key = settings.SAMBANOVA_API_KEY
    if samba_key:
        chain.append({
            "base_url": "https://api.sambanova.ai/v1",
            "api_key": samba_key,
            "model": settings.SAMBANOVA_MODEL or "Meta-Llama-3.3-70B-Instruct",
            "label": "sambanova",
        })

    return chain


def _call_provider(provider: dict, system: str, user_msg: str) -> str:
    """Single call to one provider (no retry — caller handles that)."""
    resp = httpx.post(
        f"{provider['base_url']}/chat/completions",
        headers={"Authorization": f"Bearer {provider['api_key']}"},
        json={
            "model": provider["model"],
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user_msg},
            ],
        },
        timeout=120,
    )
    return resp  # caller inspects status


def _chat(model: str, system: str, user_msg: str, max_retries: int = 3) -> str:
    """Call LLM with provider fallback chain + per-provider retry.

    Strategy:
    1. Try each provider in order (Groq → Cerebras → SambaNova).
    2. Per provider: retry up to max_retries on short 429s and timeouts.
    3. If a provider hits daily limit (retry-after > _CHAT_MAX_WAIT),
       immediately fall through to the next provider.
    4. If all providers exhausted, raise.
    """
    chain = _build_provider_chain()
    if not chain:
        raise ValueError("No LLM providers configured (check API keys)")

    all_errors = []

    for provider in chain:
        last_exc = None
        for attempt in range(max_retries):
            try:
                resp = _call_provider(provider, system, user_msg)

                if resp.status_code == 429:
                    retry_after = int(resp.headers.get("retry-after", 0))
                    if retry_after > _CHAT_MAX_WAIT:
                        print(f"[_chat][{provider['label']}] daily limit hit (retry-after={retry_after}s), trying next provider...")
                        last_exc = Exception(f"{provider['label']} daily limit (retry-after={retry_after}s)")
                        break  # break inner retry loop → next provider
                    wait = retry_after if retry_after > 0 else min(2 ** attempt + random.uniform(0, 1), _CHAT_MAX_WAIT)
                    print(f"[_chat][{provider['label']}] 429 (attempt {attempt+1}/{max_retries}), waiting {wait:.1f}s...")
                    time.sleep(wait)
                    last_exc = Exception(f"{provider['label']} 429")
                    continue

                resp.raise_for_status()
                if provider["label"] != "groq":
                    print(f"[_chat] served by fallback provider: {provider['label']}")
                return resp.json()["choices"][0]["message"]["content"]

            except httpx.HTTPStatusError as e:
                if e.response.status_code == 429:
                    retry_after = int(e.response.headers.get("retry-after", 0))
                    if retry_after > _CHAT_MAX_WAIT:
                        print(f"[_chat][{provider['label']}] daily limit, trying next provider...")
                        last_exc = e
                        break
                    wait = retry_after if retry_after > 0 else min(2 ** attempt + random.uniform(0, 1), _CHAT_MAX_WAIT)
                    print(f"[_chat][{provider['label']}] 429 (attempt {attempt+1}/{max_retries}), waiting {wait:.1f}s...")
                    time.sleep(wait)
                    last_exc = e
                    continue
                # Non-429 HTTP error — skip this provider
                print(f"[_chat][{provider['label']}] HTTP {e.response.status_code}, trying next provider...")
                last_exc = e
                break

            except httpx.TimeoutException as e:
                wait = min(2 ** attempt + random.uniform(0, 1), 30)
                print(f"[_chat][{provider['label']}] timeout (attempt {attempt+1}/{max_retries}), waiting {wait:.1f}s...")
                time.sleep(wait)
                last_exc = e
                continue

        if last_exc:
            all_errors.append(f"{provider['label']}: {last_exc}")

    raise RuntimeError(f"[_chat] all providers failed: {'; '.join(all_errors)}")


NEBULAMIND_WEBHOOK = (
    "https://discord.com/api/webhooks/1489161782521106434/"
    "15-E1EQmKaUgkHIYJa9REM0J1g59b9cAUiiGZUWY9vQVIzjWjTyKYLHvCI-rVDylzwzE"
)
NEBULAMIND_BASE_URL = "https://nebulamind.net"


def _notify(message: str) -> None:
    """Log agent activity. Discord notifications go via _notify_nebulamind_channel for approvals only."""
    print(f"[activity] {message}")


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
        system_prompt = _build_system_prompt(agent)
        raw = _chat(agent.model_name, system_prompt, user_msg)
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

    system_prompt = _build_system_prompt(agent)

    if create_new or not page.content:
        user_msg = (
            f"Write comprehensive, well-structured wiki content about "
            f'"{page.title}". Follow the required article structure exactly: '
            f"## Overview, ## Discovery & History, ## Physical Properties, "
            f"## Current Research, ## Open Questions, ## References. "
            f"Use markdown formatting and include quantitative data."
        )
    else:
        user_msg = (
            f'The wiki page "{page.title}" currently contains:\n\n'
            f"{page.content}\n\n"
            f"Please improve and expand this content following the required section structure. "
            f"Add more detail, update any outdated information, improve clarity, and ensure "
            f"all sections (Overview, Discovery & History, Physical Properties, Current Research, "
            f"Open Questions, References) are present and well-developed. Return the full updated content."
        )

    proposed = _chat(agent.model_name, system_prompt, user_msg)

    proposal = EditProposal(
        page_id=page.id,
        agent_id=agent.id,
        content=proposed,
        status=EditStatus.PENDING,
    )
    db.add(proposal)
    db.flush()
    print(f"[{agent.name}] Created edit proposal #{proposal.id} for page '{page.title}'")
    specialty_tag = f" [{agent.specialty}]" if agent.specialty else ""
    _notify(f"✍️ [{agent.model_name}{specialty_tag}] \"{page.title}\" 편집안 #{proposal.id} 제출")

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

    base_prompt = _build_system_prompt(agent)
    system = (
        f"{base_prompt}\n\n"
        f"You are reviewing a proposed edit to the wiki page "
        f'"{page.title}". The current page content is:\n\n'
        f"{page.content or '(empty page)'}\n\n"
        f"Evaluate the proposed edit for accuracy, quality, completeness, "
        f"and adherence to the required section structure (Overview, Discovery & History, "
        f"Physical Properties, Current Research, Open Questions, References). "
        f"Respond ONLY with JSON: "
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
    specialty_tag = f" [{agent.specialty}]" if agent.specialty else ""
    _notify(f"🗳️ [{agent.model_name}{specialty_tag}] 편집안 #{proposal.id} {decision_emoji} ({approve_count}/{total_needed}표)")

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
    system_prompt = _build_system_prompt(agent)
    user_msg = (
        f'Write a short, insightful comment (1-3 sentences) about '
        f'"{page.title}". The current wiki content is:\n\n'
        f"{page.content or '(no content yet)'}\n\n"
        f"Share an interesting observation, lesser-known fact, or "
        f"thought-provoking perspective from your {agent.specialty or 'astronomy'} specialty. Be concise."
    )

    body = _chat(agent.model_name, system_prompt, user_msg)

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
