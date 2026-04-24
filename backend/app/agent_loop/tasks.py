import datetime as dt
import json
import os
import random
import re
import time
from pathlib import Path

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

# ---------------------------------------------------------------------------
# Wiki Schema loader
# ---------------------------------------------------------------------------

def load_wiki_schema() -> str:
    """Load wiki_schema.md from project root. Returns empty string if missing."""
    schema_path = Path(__file__).parents[3] / "wiki_schema.md"
    if schema_path.exists():
        return schema_path.read_text(encoding="utf-8")
    return ""

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

# Core identity prompt — structural rules are loaded from wiki_schema.md
SYSTEM_PROMPT = """You are an expert astronomy and astrophysics writer contributing to NebulaMind, a platform where AI agents worldwide collaborate to build humanity's understanding of the cosmos.

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
    """Build a specialty-aware system prompt for the given agent.
    
    Loads wiki_schema.md dynamically — changes to the schema file propagate
    to all agents on the next edit cycle without redeploying.
    """
    specialty = agent.specialty or "general"
    model_name = agent.model_name

    # Load schema (structural rules, categories, cross-link rules)
    schema = load_wiki_schema()
    # Strip Coverage Map section — agents don't need the raw map, only the rules
    if "## Coverage Map" in schema:
        schema = schema[:schema.index("## Coverage Map")].rstrip()

    base = SYSTEM_PROMPT.replace("{specialty}", specialty).replace("{model_name}", model_name)

    if schema:
        base = base + "\n\n" + schema

    if specialty in SPECIALTY_EMPHASIS:
        base += f"\n\n## Your Specialty Focus ({specialty})\n{SPECIALTY_EMPHASIS[specialty]}"

    return base


def _slugify(title: str) -> str:
    return title.lower().replace(" ", "-")


# ---------------------------------------------------------------------------
# Coverage Map (Phase 5)
# ---------------------------------------------------------------------------

def compute_coverage(db) -> dict:
    """Compare DB wiki pages with NEW_TOPICS. Returns coverage stats."""
    existing_slugs = {p.slug for p in db.query(WikiPage).all()}
    existing_titles = {p.title.lower() for p in db.query(WikiPage).all()}

    covered = []
    not_covered = []
    for topic in NEW_TOPICS:
        slug = _slugify(topic)
        if slug in existing_slugs or topic.lower() in existing_titles:
            covered.append(topic)
        else:
            not_covered.append(topic)

    total = len(NEW_TOPICS)
    pct = round(len(covered) / total * 100, 1) if total else 0
    return {
        "covered": covered,
        "not_covered": not_covered,
        "total": total,
        "coverage_pct": pct,
        "existing_page_count": len(existing_slugs),
    }


def update_coverage_map_in_schema(db) -> dict:
    """Recalculate coverage and update the Coverage Map section in wiki_schema.md."""
    schema_path = Path(__file__).parents[3] / "wiki_schema.md"
    if not schema_path.exists():
        print("[coverage] wiki_schema.md not found, skipping update")
        return {}

    stats = compute_coverage(db)
    covered = stats["covered"]
    not_covered = stats["not_covered"]
    pct = stats["coverage_pct"]
    now = dt.datetime.now(dt.UTC).strftime("%Y-%m-%d %H:%M UTC")

    covered_lines = "\n".join(f"  ✅ {t}" for t in sorted(covered)) or "  (none yet)"
    not_covered_lines = "\n".join(f"  ⏳ {t}" for t in not_covered) or "  (all topics covered!)"

    new_map = f"""## Coverage Map

> Auto-updated daily by the `update_coverage_map` Celery task.
> Last updated: {now}

### Topic Coverage Status

```
COVERED ({len(covered)} topics):
{covered_lines}

NOT YET COVERED ({len(not_covered)} topics — priority queue):
{not_covered_lines}

Coverage: {len(covered)} / {stats['total']} predefined topics ({pct}%)
Total wiki pages in DB: {stats['existing_page_count']}
```

### Expansion Priority

Topics are selected for new page creation in this priority order:
1. Topics in `NOT YET COVERED` list (highest priority)
2. arXiv-trending topics not yet in DB
3. Weakest existing pages (empty or short content)
4. Random page improvement
"""

    # Replace Coverage Map section in existing schema file
    schema_text = schema_path.read_text(encoding="utf-8")
    if "## Coverage Map" in schema_text:
        # Replace from ## Coverage Map to end of file
        schema_text = schema_text[:schema_text.index("## Coverage Map")] + new_map
    else:
        schema_text = schema_text.rstrip() + "\n\n" + new_map

    schema_path.write_text(schema_text, encoding="utf-8")
    print(f"[coverage] Updated wiki_schema.md — {len(covered)}/{stats['total']} covered ({pct}%)")
    return stats


def _select_uncovered_topic(db) -> "str | None":
    """Return a NEW_TOPICS entry not yet in DB. Returns None if all covered."""
    existing_slugs = {p.slug for p in db.query(WikiPage).all()}
    existing_titles = {p.title.lower() for p in db.query(WikiPage).all()}
    uncovered = [
        t for t in NEW_TOPICS
        if _slugify(t) not in existing_slugs and t.lower() not in existing_titles
    ]
    if uncovered:
        return random.choice(uncovered)
    return None


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

@celery_app.task
def drain_pending_reviews():
    """Run reviewers on pending proposals until queue is drained. Cost: $0 (free LLMs only)."""
    db = SessionLocal()
    try:
        pending_count = db.query(EditProposal).filter(EditProposal.status == EditStatus.PENDING).count()
        if pending_count == 0:
            return
        print(f"[drain] {pending_count} pending proposals — waking reviewers")
        reviewers = db.query(Agent).filter(
            Agent.is_active.is_(True),
            Agent.role == "reviewer"
        ).all()
        for agent in reviewers:
            run_edit_cycle.delay(agent.id)
    finally:
        db.close()

@celery_app.task(name='app.agent_loop.tasks.wake_agents')
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
        elif role == "evidence_linker":
            _run_evidence_linker(db, agent)
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


def _pick_weak_page(db) -> "WikiPage | None":
    """Pick the page most in need of improvement.
    Priority: 1) empty content, 2) short content (<500 chars), 3) oldest updated.
    """
    from sqlalchemy import func

    # 1. Empty pages first
    empty = db.query(WikiPage).filter(
        (WikiPage.content == None) | (WikiPage.content == "")
    ).first()
    if empty:
        return empty

    # 2. Short pages (< 500 chars)
    all_pages = db.query(WikiPage).all()
    short_pages = [p for p in all_pages if p.content and len(p.content) < 500]
    if short_pages:
        return random.choice(short_pages)

    # 3. Page with fewest approved edits
    edit_counts = (
        db.query(EditProposal.page_id, func.count(EditProposal.id).label("cnt"))
        .filter(EditProposal.status == EditStatus.APPROVED)
        .group_by(EditProposal.page_id)
        .all()
    )
    edit_map = {row.page_id: row.cnt for row in edit_counts}
    if all_pages:
        return min(all_pages, key=lambda p: edit_map.get(p.id, 0))

    return None


def _discover_new_topic(db) -> "str | None":
    """Find a new topic from arXiv papers not yet covered in the wiki."""
    from app.models.arxiv import ArxivPaper
    import re

    # Get existing slugs
    existing_slugs = {p.slug for p in db.query(WikiPage).all()}

    # Scan recent arXiv titles for candidate topics
    papers = db.query(ArxivPaper).order_by(ArxivPaper.id.desc()).limit(100).all()
    candidate_freq: dict[str, int] = {}
    topic_patterns = [
        r'\b(magnetar[s]?)\b',
        r'\b(fast radio burst[s]?)\b',
        r'\b(neutron star[s]?)\b',
        r'\b(black hole[s]?)\b',
        r'\b(gravitational wave[s]?)\b',
        r'\b(dark matter)\b',
        r'\b(dark energy)\b',
        r'\b(exoplanet[s]?)\b',
        r'\b(galaxy cluster[s]?)\b',
        r'\b(cosmic inflation)\b',
        r'\b(stellar evolution)\b',
        r'\b(supernova[e]?)\b',
        r'\b(pulsar[s]?)\b',
        r'\b(quasar[s]?)\b',
        r'\b(gamma.ray burst[s]?)\b',
        r'\b(active galactic nuclei?)\b',
        r'\b(interstellar medium)\b',
        r'\b(planetary formation)\b',
        r'\b(stellar nursery|stellar nurseries)\b',
        r'\b(cosmic web)\b',
        r'\b(reionization)\b',
        r'\b(baryon acoustic oscillation[s]?)\b',
        r'\b(gravitational lensing)\b',
        r'\b(accretion dis[ck])\b',
        r'\b(red giant[s]?)\b',
    ]
    title_to_canonical = {
        'magnetar': 'Magnetars', 'magnetars': 'Magnetars',
        'fast radio burst': 'Fast Radio Bursts', 'fast radio bursts': 'Fast Radio Bursts',
        'neutron star': 'Neutron Stars', 'neutron stars': 'Neutron Stars',
        'black hole': 'Black Holes', 'black holes': 'Black Holes',
        'gravitational wave': 'Gravitational Waves', 'gravitational waves': 'Gravitational Waves',
        'dark matter': 'Dark Matter', 'dark energy': 'Dark Energy',
        'exoplanet': 'Exoplanets', 'exoplanets': 'Exoplanets',
        'galaxy cluster': 'Galaxy Clusters', 'galaxy clusters': 'Galaxy Clusters',
        'cosmic inflation': 'Cosmic Inflation',
        'stellar evolution': 'Stellar Evolution',
        'supernova': 'Supernovae', 'supernovae': 'Supernovae',
        'pulsar': 'Pulsars', 'pulsars': 'Pulsars',
        'quasar': 'Quasars', 'quasars': 'Quasars',
        'gamma-ray burst': 'Gamma-ray Bursts', 'gamma-ray bursts': 'Gamma-ray Bursts',
        'gamma ray burst': 'Gamma-ray Bursts', 'gamma ray bursts': 'Gamma-ray Bursts',
        'active galactic nucleus': 'Active Galactic Nuclei', 'active galactic nuclei': 'Active Galactic Nuclei',
        'interstellar medium': 'Interstellar Medium',
        'planetary formation': 'Planetary Formation',
        'stellar nursery': 'Stellar Nurseries', 'stellar nurseries': 'Stellar Nurseries',
        'cosmic web': 'Cosmic Web',
        'reionization': 'Reionization',
        'baryon acoustic oscillation': 'Baryon Acoustic Oscillations',
        'baryon acoustic oscillations': 'Baryon Acoustic Oscillations',
        'gravitational lensing': 'Gravitational Lensing',
        'accretion disk': 'Accretion Disks', 'accretion disc': 'Accretion Disks',
        'red giant': 'Red Giants', 'red giants': 'Red Giants',
    }

    for paper in papers:
        text = (paper.title + " " + (paper.abstract or "")).lower()
        for pattern in topic_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                key = match.group(1).lower()
                canonical = title_to_canonical.get(key)
                if canonical:
                    slug = _slugify(canonical)
                    if slug not in existing_slugs:
                        candidate_freq[canonical] = candidate_freq.get(canonical, 0) + 1

    if candidate_freq:
        # Return the most frequently mentioned new topic
        return max(candidate_freq, key=lambda k: candidate_freq[k])
    return None


def _run_editor(db, agent: Agent):
    """Pick a page (or create a new topic) and propose an edit.

    Strategy (priority order):
    1. 20% chance: discover a new topic from arXiv trends
    2. 40% chance: pick the weakest existing page (empty/short/least-edited)
    3. 40% chance: random page
    """
    pages = db.query(WikiPage).all()
    create_new = False
    page = None
    rand = random.random()

    if rand < 0.20:
        # Try to discover a new topic from arXiv
        new_topic = _discover_new_topic(db)
        if new_topic:
            slug = _slugify(new_topic)
            existing = db.query(WikiPage).filter(WikiPage.slug == slug).first()
            if existing:
                page = existing
            else:
                page = WikiPage(title=new_topic, slug=slug, content="")
                db.add(page)
                db.flush()
                create_new = True
                print(f"[{agent.name}] arXiv-discovered new topic: {new_topic}")

    if page is None and rand < 0.60:
        # Pick weakest page
        page = _pick_weak_page(db)
        if page and not page.content:
            create_new = True

    if page is None:
        # Try uncovered topics from NEW_TOPICS first
        uncovered_topic = _select_uncovered_topic(db)
        if uncovered_topic:
            slug = _slugify(uncovered_topic)
            existing = db.query(WikiPage).filter(WikiPage.slug == slug).first()
            if existing:
                page = existing
            else:
                page = WikiPage(title=uncovered_topic, slug=slug, content="")
                db.add(page)
                db.flush()
                create_new = True
                print(f"[{agent.name}] Created uncovered topic page: {uncovered_topic}")
        elif pages:
            # All predefined topics covered — improve existing pages
            page = random.choice(pages)
        else:
            # Absolute last resort
            topic = random.choice(NEW_TOPICS)
            slug = _slugify(topic)
            existing = db.query(WikiPage).filter(WikiPage.slug == slug).first()
            if existing:
                page = existing
            else:
                page = WikiPage(title=topic, slug=slug, content="")
                db.add(page)
                db.flush()
                create_new = True
                print(f"[{agent.name}] Created new page: {topic}")

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
            EditProposal.agent_id != agent.id,  # 자기 글 리뷰 금지
        )
        .first()
    )
    if not proposal:
        print(f"[{agent.name}] No pending proposals to review, skipping")
        return

    # 같은 모델끼리 리뷰 금지
    proposer = db.query(Agent).get(proposal.agent_id)
    if proposer and proposer.model_name == agent.model_name:
        print(f"[{agent.name}] Skipping proposal #{proposal.id} — same model ({agent.model_name})")
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

    from app.levels import get_vote_weight

    pos_votes = db.query(Vote).filter(Vote.edit_id == proposal.id, Vote.value == 1).all()
    weighted_sum = sum(get_vote_weight(v.agent_id, db) for v in pos_votes)
    total_needed = settings.VOTE_THRESHOLD
    decision_emoji = "👍" if vote.value == 1 else "👎"
    specialty_tag = f" [{agent.specialty}]" if agent.specialty else ""
    _notify(f"🗳️ [{agent.model_name}{specialty_tag}] 편집안 #{proposal.id} {decision_emoji} ({weighted_sum:.1f}/{total_needed}가중치)")

    # Check if threshold is met (weighted)
    if weighted_sum >= settings.VOTE_THRESHOLD:
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


def _run_evidence_linker(db, agent: Agent):
    """Find unverified claims without evidence and auto-link papers via LLM."""
    import json as _json
    from app.models.claim import Claim, Evidence
    from sqlalchemy import func as sqlfunc

    # Pick an unverified claim with no evidence
    subq = db.query(Evidence.claim_id).subquery()
    claim = (
        db.query(Claim)
        .filter(
            Claim.trust_level == "unverified",
            ~Claim.id.in_(subq),
        )
        .order_by(sqlfunc.random())
        .first()
    )
    if not claim:
        print(f"[{agent.name}] No unverified claims without evidence, skipping")
        return

    page = db.query(WikiPage).get(claim.page_id)
    topic = page.title if page else "astronomy"

    prompt = (
        f'Scientific claim from the "{topic}" wiki page:\n'
        f'"{claim.text}"\n\n'
        f"Find 1-2 real published papers that support or challenge this claim. "
        f'Respond ONLY with JSON array: '
        f'[{{"title":"...","authors":"...","year":2020,"arxiv_id":"2301.12345 or null","stance":"supports|challenges|neutral","summary":"How this paper relates to the claim"}}]'
    )
    raw = _chat(agent.model_name, SYSTEM_PROMPT, prompt)

    try:
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0]
        papers = _json.loads(cleaned)
        if not isinstance(papers, list):
            papers = [papers]
    except Exception as exc:
        print(f"[{agent.name}] Failed to parse evidence response: {exc}")
        return

    added = 0
    for p in papers[:2]:
        if not isinstance(p, dict) or not p.get("title"):
            continue
        ev = Evidence(
            claim_id=claim.id,
            arxiv_id=p.get("arxiv_id"),
            title=p.get("title", ""),
            authors=p.get("authors"),
            year=p.get("year"),
            summary=p.get("summary"),
            stance=p.get("stance", "supports"),
            added_by_agent_id=agent.id,
            url=f"https://arxiv.org/abs/{p['arxiv_id']}" if p.get("arxiv_id") else p.get("url"),
        )
        db.add(ev)
        added += 1

    if added:
        db.flush()
        from app.routers.claims import recalculate_trust
        new_trust = recalculate_trust(claim.id, db)
        claim.trust_level = new_trust
        print(f"[{agent.name}] Linked {added} paper(s) to claim #{claim.id} (trust: {new_trust})")
        _notify(f"🔗 [{agent.model_name}] 클레임 #{claim.id}에 근거 {added}개 연결 → {new_trust}")


# ---------------------------------------------------------------------------
# Coverage Map Celery Task (Phase 5)
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.update_coverage_map")
def update_coverage_map():
    """Recompute coverage and update wiki_schema.md Coverage Map section (daily)."""
    db = SessionLocal()
    try:
        stats = update_coverage_map_in_schema(db)
        if stats:
            _notify(
                f"🗺️ Coverage Map updated: "
                f"{len(stats['covered'])}/{stats['total']} topics covered "
                f"({stats['coverage_pct']}%) | "
                f"{stats['existing_page_count']} total wiki pages"
            )
    except Exception as e:
        print(f"[update_coverage_map] Error: {e}")
        raise
    finally:
        db.close()


# ---------------------------------------------------------------------------
# arXiv Research Frontier
# ---------------------------------------------------------------------------
import feedparser

ARXIV_CATEGORIES = ["astro-ph.GA", "astro-ph.CO", "astro-ph.HE", "astro-ph.SR"]

ARXIV_WIKI_KEYWORDS = {
    "black hole": ["black-holes", "black-hole-mergers"],
    "dark matter": ["dark-matter"],
    "dark energy": ["dark-energy"],
    "hubble": ["hubble-constant"],
    "gravitational wave": ["gravitational-waves"],
    "galaxy": ["galaxy-formation", "galaxy-clusters"],
    "exoplanet": ["exoplanets"],
    "neutron star": ["neutron-stars"],
    "supernova": ["supernovae"],
    "pulsar": ["pulsars"],
    "cosmic inflation": ["cosmic-inflation"],
    "fast radio burst": ["fast-radio-bursts"],
    "quasar": ["quasars"],
    "active galactic": ["active-galactic-nuclei"],
}

ARXIV_SUMMARY_SYSTEM = (
    "You are a science communicator summarizing astronomy papers for a knowledge base. "
    "Be concise and accurate."
)


def _match_wiki_pages(title: str, abstract: str) -> list[str]:
    text = (title + " " + abstract).lower()
    matched = set()
    for keyword, slugs in ARXIV_WIKI_KEYWORDS.items():
        if keyword in text:
            matched.update(slugs)
    return list(matched)[:3]  # max 3


def _parse_arxiv_rss(category: str, limit: int = 10) -> list[dict]:
    url = f"https://rss.arxiv.org/rss/{category}"
    feed = feedparser.parse(url)
    papers = []
    for entry in feed.entries[:limit]:
        arxiv_id = entry.get("id", "").split("/abs/")[-1].replace("v1", "").strip()
        title = entry.get("title", "").replace("\n", " ").strip()
        abstract = entry.get("summary", "").replace("\n", " ").strip()

        authors = []
        if hasattr(entry, "authors"):
            authors = [a.get("name", "") for a in entry.authors]
        elif hasattr(entry, "author"):
            authors = [entry.author]

        submitted = ""
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            t = entry.published_parsed
            submitted = f"{t.tm_year}-{t.tm_mon:02d}-{t.tm_mday:02d}"

        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "abstract": abstract,
            "authors": json.dumps(authors[:5]),
            "submitted": submitted,
            "url": entry.get("link", f"https://arxiv.org/abs/{arxiv_id}"),
            "category": category,
        })
    return papers


@celery_app.task
def fetch_arxiv_daily():
    """Fetch latest arXiv papers, summarize with LLM, store in DB."""
    from app.models.arxiv import ArxivPaper

    db = SessionLocal()
    try:
        arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()
        if not arxivbot:
            print("[fetch_arxiv_daily] ArxivBot not found, skipping")
            return

        total_new = 0
        for cat in ARXIV_CATEGORIES:
            try:
                papers = _parse_arxiv_rss(cat, limit=8)
            except Exception as e:
                print(f"[fetch_arxiv_daily] RSS parse failed for {cat}: {e}")
                continue

            for p in papers:
                if not p["arxiv_id"]:
                    continue

                # dedup
                exists = db.query(ArxivPaper).filter(ArxivPaper.arxiv_id == p["arxiv_id"]).first()
                if exists:
                    continue

                # LLM summary
                try:
                    user_msg = (
                        f"Summarize this astronomy paper in 2-3 sentences for a general science audience.\n\n"
                        f"Title: {p['title']}\n\nAbstract: {p['abstract'][:800]}"
                    )
                    summary = _chat(arxivbot.model_name, ARXIV_SUMMARY_SYSTEM, user_msg)
                    summary = summary.strip()[:500]
                except Exception as e:
                    print(f"[fetch_arxiv_daily] LLM summary failed: {e}")
                    summary = p["abstract"][:300]

                # wiki matching
                related = _match_wiki_pages(p["title"], p["abstract"])

                # save
                paper = ArxivPaper(
                    arxiv_id=p["arxiv_id"],
                    title=p["title"],
                    authors=p["authors"],
                    abstract=p["abstract"],
                    abstract_summary=summary,
                    category=p["category"],
                    submitted=p["submitted"],
                    url=p["url"],
                    related_pages=json.dumps(related),
                    wiki_edit_proposed=False,
                )
                db.add(paper)
                db.flush()
                total_new += 1
                print(f"[fetch_arxiv_daily] Saved: {p['title'][:60]}")

                # propose wiki edit if related pages found
                if related:
                    for slug in related[:1]:  # max 1 edit per paper
                        wiki_page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
                        if not wiki_page or not wiki_page.content:
                            continue
                        try:
                            edit_msg = (
                                f"Update the '## Current Research' section of the '{wiki_page.title}' wiki page "
                                f"to include this recent finding. Keep all existing content and naturally integrate:\n\n"
                                f"Paper: {p['title']}\nAuthors: {json.loads(p['authors'])[:3]}\n"
                                f"Summary: {summary}\nSource: {p['url']}\n\n"
                                f"Current page content:\n{wiki_page.content[:2000]}"
                            )
                            updated = _chat(arxivbot.model_name, SYSTEM_PROMPT, edit_msg)
                            proposal = EditProposal(
                                page_id=wiki_page.id,
                                agent_id=arxivbot.id,
                                content=updated,
                                status=EditStatus.PENDING,
                            )
                            db.add(proposal)
                            paper.wiki_edit_proposed = True
                            print(f"[fetch_arxiv_daily] Proposed wiki edit for: {slug}")
                        except Exception as e:
                            print(f"[fetch_arxiv_daily] Wiki edit failed for {slug}: {e}")

                time.sleep(2)

        db.commit()
        print(f"[fetch_arxiv_daily] Done. {total_new} new papers saved.")
        _notify(f"📡 arXiv 수집 완료: {total_new}개 새 논문")
    except Exception as e:
        db.rollback()
        print(f"[fetch_arxiv_daily] Error: {e}")
        raise
    finally:
        db.close()
