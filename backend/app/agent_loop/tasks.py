import asyncio
import datetime as dt
import json
import os
import random
import re
import time
from pathlib import Path


def _normalize_authors(authors_raw, cap: int = 5) -> str | None:
    """Normalize authors to a JSON array of individual name strings, capped at `cap`."""
    if not authors_raw:
        return None
    try:
        if isinstance(authors_raw, list):
            names = authors_raw
        elif authors_raw.startswith("["):
            names = json.loads(authors_raw)
        else:
            names = [authors_raw]
        # If stored as single comma-sep string, split it
        if len(names) == 1 and "," in names[0]:
            names = [n.strip() for n in names[0].split(",") if n.strip()]
        return json.dumps([n for n in names if n][:cap])
    except Exception:
        return authors_raw[:200] if authors_raw else None

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
from app.services.llm_utils import strip_think_blocks
from app.utils.model_guard import guard_batch_model
from app.utils.premium_dispatch import dispatch_premium, log_llm_call, log_llm_spend
from app.agent_loop.autowiki.citation_context import build_evidence_map, emit_citation_scrub_required

# ---------------------------------------------------------------------------
# Model keep-alive helpers
# ---------------------------------------------------------------------------

def _keep_alive_ollama(base_url: str, model: str, keep_alive: str = "24h") -> None:
    """Ping Ollama to keep a model loaded in memory with a capped context."""
    try:
        httpx.post(
            f"{base_url.rstrip('/').rstrip('/v1')}/api/chat",
            json={
                "model": model,
                "keep_alive": keep_alive,
                "stream": False,
                "messages": [{"role": "user", "content": "ping"}],
                "options": {"num_ctx": 8192, "num_predict": 1},
            },
            timeout=10,
        )
    except Exception:
        pass


@celery_app.task(name="app.agent_loop.tasks.warm_models")
def warm_models():
    """Keep key models loaded in Ollama memory. Runs every 20 minutes.
    Resident set: Vera, Mima, Nutty, Pico. Buddle/Blanc load on demand.
    """
    _keep_alive_ollama(settings.RAKON_BASE_URL, settings.RAKON_MODEL, "24h")  # Rakon
    _keep_alive_ollama(settings.BUDDLE_BASE_URL, settings.BUDDLE_MODEL, "2h")  # Buddle
    # Studio resident set — ~212GB safe budget
    for model in [settings.ASTRO_SYNTH_MODEL, settings.OLLAMA_STUDIO_HEAVY_MODEL, settings.OLLAMA_STUDIO_FAST_MODEL, settings.ASTRO_SCORER_MODEL]:
        _keep_alive_ollama("http://localhost:11434", model, "30m")
    print("[warm_models] keep-alive pings sent")


# ---------------------------------------------------------------------------
# Wiki Schema loader
# ---------------------------------------------------------------------------

def load_wiki_schema() -> str:
    """Load wiki_schema.md from project root. Returns empty string if missing."""
    schema_path = Path(__file__).parents[3] / "wiki_schema.md"
    if schema_path.exists():
        return schema_path.read_text(encoding="utf-8")
    return ""

# ---------------------------------------------------------------------------
# Trust Phase 2: Stance Jury + Adversarial Pass
# ---------------------------------------------------------------------------
try:
    from app.services.prompt_registry import PromptRegistry
    STANCE_JURY_SYSTEM = PromptRegistry().render("stance", {}, policy="permissive_v1")
except Exception as e:
    STANCE_JURY_SYSTEM = """You are an astronomy peer reviewer judging whether a cited paper actually supports a wiki claim.

Read the claim and the paper's abstract carefully. Apply scientific judgment:
- A paper "supports" a claim if its findings are consistent with and reinforce the claim.
- A paper "challenges" a claim if it presents contradicting evidence or finds the claim falsified.
- A paper is "off-topic" if its abstract doesn't address the claim's subject matter.

Be skeptical. If the abstract doesn't clearly engage with the claim, vote 0.

Respond with ONLY a JSON object:
{"stance_correct": true|false, "vote": 1|-1|0, "reason": "<one sentence, max 200 chars>"}"""

STANCE_JURY_MODELS = [
    {"base_url": "https://generativelanguage.googleapis.com/v1beta/openai", "api_key": settings.GEMINI_API_KEY, "model": "gemini-2.5-flash", "label": "gemini-2.5-flash", "max_tokens": 8192},
    {"base_url": settings.LLM_BASE_URL, "api_key": settings.LLM_API_KEY, "model": "openai/gpt-oss-20b", "label": "openai/gpt-oss-20b", "max_tokens": 512},
    {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.STANCE_JURY_FAST_MODEL, "label": settings.STANCE_JURY_FAST_MODEL, "max_tokens": 512, "no_think": True},
    {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.OLLAMA_STUDIO_FAST_MODEL, "label": settings.OLLAMA_STUDIO_FAST_MODEL, "max_tokens": 512, "no_think": True},
    {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": "vanta-research/atom-astronomy-7b", "label": "vanta-research/atom-astronomy-7b"},
    {
        "provider": "mlx_outlines",
        "api_key": "local",
        "model": "mlx-community/Qwen3.6-35B-A3B-NVFP4",
        "label": "MimaOutlines",
        "max_tokens": 128,
        "timeout": 45,
        "overall_timeout": 90,
    },
]
STANCE_JURY_MODELS = [m for m in STANCE_JURY_MODELS if m["api_key"]]

JURY_AGENT_LABELS = {
    "gemini-2.5-flash":  "JuryGeminiFlash",
    "qwen3.6:35b-a3b-nvfp4":       "JuryQwen36",
    "gpt-oss:20b": "JuryGptOss20",
    "llama3.3:70b":       "JuryLlama",
    "deepseek-r1:671b":    "JuryDeepseek671",
    "openai/gpt-oss-20b":  "JuryGroq",
    "groq-llama3.3":      "JuryGroq",
    "cerebras-llama3.1":  "JuryCerebras",
    "vanta-research/atom-astronomy-7b": "JuryAtom",
    "MimaOutlines": "JuryMimaOutlines",
}

STANCE_JURY_INFLIGHT_PREFIX = "stance_jury:inflight:"
_MLX_OUTLINES_CACHE: dict[str, tuple[object, object]] = {}


def _stance_jury_inflight_ttl(countdown: int = 0) -> int:
    base_ttl = max(
        settings.STANCE_JURY_INFLIGHT_TTL_SECONDS,
        settings.STANCE_JURY_TIMEOUT_SECONDS
        + settings.STANCE_JURY_RETRY_BACKOFF_SECONDS
        + 300,
    )
    return int(max(60, countdown + base_ttl))


def _claim_stance_jury_inflight(evidence_id: int, countdown: int = 0) -> bool:
    """Reserve an evidence id before delayed jury enqueue so producers cannot overlap."""
    try:
        import redis as _redis_lib
        r = _redis_lib.from_url(settings.REDIS_URL, decode_responses=True)
        return bool(
            r.set(
                f"{STANCE_JURY_INFLIGHT_PREFIX}{evidence_id}",
                "1",
                nx=True,
                ex=_stance_jury_inflight_ttl(countdown),
            )
        )
    except Exception as e:
        print(f"[stance_jury] inflight claim failed for ev #{evidence_id}: {e}")
        return False


def _release_stance_jury_inflight(evidence_id: int) -> None:
    try:
        import redis as _redis_lib
        _redis_lib.from_url(settings.REDIS_URL, decode_responses=True).delete(
            f"{STANCE_JURY_INFLIGHT_PREFIX}{evidence_id}"
        )
    except Exception:
        pass


def _parse_stance_jury_id_csv(raw: str | None) -> set[int]:
    ids: set[int] = set()
    for token in (raw or "").split(","):
        token = token.strip()
        if not token:
            continue
        try:
            ids.add(int(token))
        except ValueError:
            print(f"[stance_jury] ignoring invalid held id token: {token!r}")
    return ids


def _stance_jury_held_page_ids() -> set[int]:
    return _parse_stance_jury_id_csv(settings.STANCE_JURY_HELD_PAGE_IDS)


def _stance_jury_held_claim_ids() -> set[int]:
    return _parse_stance_jury_id_csv(settings.STANCE_JURY_HELD_CLAIM_IDS)


def _stance_jury_held_evidence_ids() -> set[int]:
    return _parse_stance_jury_id_csv(settings.STANCE_JURY_HELD_EVIDENCE_IDS)


def _stance_jury_is_held(ev=None, claim=None, evidence_id: int | None = None,
                         claim_id: int | None = None, page_id: int | None = None) -> bool:
    ev_id = evidence_id if evidence_id is not None else getattr(ev, "id", None)
    cl_id = claim_id if claim_id is not None else getattr(ev, "claim_id", None)
    cl_id = cl_id if cl_id is not None else getattr(claim, "id", None)
    pg_id = page_id if page_id is not None else getattr(claim, "page_id", None)
    return (
        (ev_id is not None and ev_id in _stance_jury_held_evidence_ids())
        or (cl_id is not None and cl_id in _stance_jury_held_claim_ids())
        or (pg_id is not None and pg_id in _stance_jury_held_page_ids())
    )


def _apply_stance_jury_held_filters(query, Evidence, Claim):
    held_evidence_ids = _stance_jury_held_evidence_ids()
    held_claim_ids = _stance_jury_held_claim_ids()
    held_page_ids = _stance_jury_held_page_ids()
    if held_evidence_ids:
        query = query.filter(~Evidence.id.in_(held_evidence_ids))
    if held_claim_ids:
        query = query.filter(~Claim.id.in_(held_claim_ids))
    if held_page_ids:
        query = query.filter(~Claim.page_id.in_(held_page_ids))
    return query


def _enqueue_stance_jury_task(task, evidence_id: int, countdown: int) -> bool:
    if not _claim_stance_jury_inflight(evidence_id, countdown=countdown):
        return False
    try:
        task.apply_async(args=[evidence_id], countdown=countdown)
        return True
    except Exception:
        _release_stance_jury_inflight(evidence_id)
        raise

ADVERSARIAL_QUERY_SYSTEM = """You translate scientific claims into ADS search queries that find DISAGREEING or CONTRADICTING papers.

Given a wiki claim, generate one ADS query to find papers that present contradicting evidence or show the claim is superseded.
Use astronomy terminology. Prefer recent papers (post-2018).

Return ONLY: {"query": "..."}
Do NOT invent specific arXiv IDs."""

_CHAL_CUES = (
    "contradict", "refute", "inconsistent", "rules out", "ruled out",
    "in tension", "not supported", "argue against", "reject",
    "problem with", "fail", "cannot explain", "challenge",
    "tension with", "disagree", "questioned", "calls into question",
)

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
    groq_model = os.environ.get("NM_LLM_MODEL", "openai/gpt-oss-120b")
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

    # 4. Fallback: Ollama (local, free)
    ollama_url = settings.OLLAMA_BASE_URL
    if ollama_url:
        chain.append({
            "base_url": ollama_url,
            "api_key": "ollama",
            "model": settings.OLLAMA_MODEL or "llama3.3:70b",
            "label": "ollama",
        })

    return chain


def _build_provider_chain_for_role(role: str = None):
    """Build provider chain with Ollama as primary provider.
    
    Ollama(local) → Groq → Cerebras → SambaNova
    Role → Ollama model mapping (from .env).
    """
    # 역할별 Ollama 모델 결정
    role_model_map = {
        "writer":          settings.OLLAMA_WRITER or settings.OLLAMA_MODEL,
        "editor":          settings.OLLAMA_EDITOR or settings.OLLAMA_MODEL,
        "reviewer":        settings.OLLAMA_REVIEWER or settings.OLLAMA_MODEL,
        "commenter":       settings.OLLAMA_COMMENTER or settings.OLLAMA_MODEL,
        "evidence_linker": settings.OLLAMA_ARXIV or settings.OLLAMA_MODEL,
        "arxivbot":        settings.OLLAMA_ARXIV or settings.OLLAMA_MODEL,
    }
    ollama_model = role_model_map.get(role, settings.OLLAMA_MODEL) if role else settings.OLLAMA_MODEL

    chain = []

    # 1. Ollama (로컬, 무제한) — 1순위
    if settings.OLLAMA_BASE_URL and ollama_model:
        chain.append({
            "base_url": settings.OLLAMA_BASE_URL,
            "api_key": "ollama",
            "model": ollama_model,
            "label": "ollama",
        })

    # 2. Groq — fallback
    if settings.LLM_API_KEY:
        chain.append({
            "base_url": settings.LLM_BASE_URL,
            "api_key": settings.LLM_API_KEY,
            "model": os.environ.get("NM_LLM_MODEL", "openai/gpt-oss-120b"),
            "label": "groq",
        })

    # 3. Cerebras — fallback
    if settings.CEREBRAS_API_KEY:
        chain.append({
            "base_url": "https://api.cerebras.ai/v1",
            "api_key": settings.CEREBRAS_API_KEY,
            "model": settings.CEREBRAS_MODEL or "llama3.1-8b",
            "label": "cerebras",
        })

    # 4. SambaNova — fallback
    if settings.SAMBANOVA_API_KEY:
        chain.append({
            "base_url": "https://api.sambanova.ai/v1",
            "api_key": settings.SAMBANOVA_API_KEY,
            "model": settings.SAMBANOVA_MODEL or "Meta-Llama-3.3-70B-Instruct",
            "label": "sambanova",
        })

    # 5. Mac Pro Ollama (Rakon 671b — heavy analysis)
    macpro_url = settings.RAKON_BASE_URL or settings.OLLAMA_MACPRO_BASE_URL
    if macpro_url:
        chain.append({
            "base_url": macpro_url.rstrip("/") if macpro_url.rstrip("/").endswith("/v1") else f"{macpro_url.rstrip('/')}/v1",
            "api_key": "ollama",
            "model": settings.OLLAMA_MACPRO_MODEL or settings.BUDDLE_MODEL,
            "label": "ollama-macpro",
        })

    return chain

def _ms(t0: float) -> int:
    return int((time.monotonic() - t0) * 1000)


def _call_provider(provider: dict, system: str, user_msg: str) -> str:
    """Single call to one provider (no retry — caller handles that)."""
    est_tokens = max(1, (len(system) + len(user_msg)) // 4)
    job_name = f"tasks.chat.{provider.get('label', provider['model'])}"
    dispatch_premium(job_name, provider["model"], est_tokens)
    started = time.monotonic()
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
    latency_ms = _ms(started)
    if resp.status_code < 400:
        usage = {}
        try:
            usage = resp.json().get("usage") or {}
        except Exception:
            pass
        log_llm_spend(
            job_name,
            provider["model"],
            prompt_tokens=usage.get("prompt_tokens"),
            completion_tokens=usage.get("completion_tokens"),
            estimated_tokens=est_tokens,
            metadata={"latency_ms": latency_ms},
        )
    else:
        log_llm_call(
            job_name,
            provider["model"],
            model_name=provider["model"],
            success=False,
            latency_ms=latency_ms,
            prompt_tokens=est_tokens,
            error=f"HTTP {resp.status_code}: {resp.text[:500]}",
        )
    return resp  # caller inspects status


def _chat(model: str, system: str, user_msg: str, max_retries: int = 3, role: str = None) -> str:
    """Call LLM with provider fallback chain + per-provider retry.

    Strategy:
    1. Try each provider in order (Groq → Cerebras → SambaNova → Ollama).
    2. Per provider: retry up to max_retries on short 429s and timeouts.
    3. If a provider hits daily limit (retry-after > _CHAT_MAX_WAIT),
       immediately fall through to the next provider.
    4. If all providers exhausted, raise.
    """
    chain = _build_provider_chain_for_role(role)
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


# ---------------------------------------------------------------------------
# Parallel multi-model chat (Reviewer Phase 1 — voting)
# ---------------------------------------------------------------------------

def _call_mlx_outlines_stance_model(model: dict, system: str, user_msg: str) -> str:
    from typing import Literal

    import outlines
    from mlx_lm import load
    from pydantic import BaseModel, Field

    class StanceJuryVote(BaseModel):
        stance_correct: bool
        vote: Literal[-1, 0, 1]
        reason: str = Field(max_length=200)

    model_id = model["model"]
    if model_id not in _MLX_OUTLINES_CACHE:
        _MLX_OUTLINES_CACHE[model_id] = load(model_id)

    mlx_model, tokenizer = _MLX_OUTLINES_CACHE[model_id]
    wrapped = outlines.from_mlxlm(mlx_model, tokenizer)
    generator = outlines.Generator(wrapped, StanceJuryVote)
    prompt = (
        f"{system}\n\n"
        "Return ONLY JSON matching this schema: "
        '{"stance_correct": true|false, "vote": 1|-1|0, "reason": "<one sentence>"}'
        f"\n\n{user_msg}"
    )
    result = generator(prompt, max_tokens=model.get("max_tokens", 128))
    if hasattr(result, "model_dump_json"):
        return result.model_dump_json()
    parsed = StanceJuryVote.model_validate_json(str(result))
    return parsed.model_dump_json()


async def _call_one_async(client: httpx.AsyncClient, model: dict, system: str, user_msg: str, timeout: int) -> dict | None:
    """Call a single model asynchronously. Returns dict on success, None on failure."""
    started = time.monotonic()
    try:
        est_tokens = max(1, (len(system) + len(user_msg)) // 4)
        job_name = f"tasks.chat_parallel.{model.get('label', model['model'])}"

        if model.get("provider") == "mlx_outlines":
            content = await asyncio.wait_for(
                asyncio.to_thread(_call_mlx_outlines_stance_model, model, system, user_msg),
                timeout=model.get("timeout", timeout),
            )
            log_llm_call(
                job_name,
                model["label"],
                model_name=model["model"],
                success=bool(content),
                latency_ms=_ms(started),
                prompt_tokens=est_tokens,
                completion_tokens=len(content) // 4 if content else 0,
                error=None if content else "empty content",
            )
            return {"model": model["model"], "label": model["label"], "response": content}

        if settings.INFERENCE_SCHEDULER_ENABLED:
            from app.services.inference_scheduler import InferenceScheduler
            scheduler = InferenceScheduler()
            dispatch_premium(job_name, model["model"], est_tokens)
            content = await scheduler.execute(model, user_msg, timeout, system_prompt=system)
            if content is None:
                return None
            log_llm_spend(
                job_name,
                model["model"],
                prompt_tokens=None,
                completion_tokens=None,
                estimated_tokens=est_tokens,
                metadata={"latency_ms": _ms(started), "error": None if content else "empty content"},
                status="executed" if content else "empty",
            )
            return {"model": model["model"], "label": model["label"], "response": content}

        system_msg = system
        user_content = user_msg
        if model.get("no_think"):
            system_msg = f"{system_msg}\n\nDo not think step by step. Return only the requested JSON."
            user_content = f"/no_think\n{user_content}"

        payload: dict = {
            "model": model["model"],
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_content},
            ],
        }
        if model.get("no_think"):
            payload["thinking"] = False
            payload["reasoning_effort"] = "none"
        if model.get("api_key") == "ollama":
            payload["options"] = {"num_ctx": 8192}
        if "max_tokens" in model:
            payload["max_tokens"] = model["max_tokens"]
        dispatch_premium(job_name, model["model"], est_tokens)
        resp = await client.post(
            f"{model['base_url']}/chat/completions",
            headers={"Authorization": f"Bearer {model['api_key']}"},
            json=payload,
            timeout=timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        usage = data.get("usage") or {}
        log_llm_spend(
            job_name,
            model["model"],
            prompt_tokens=usage.get("prompt_tokens"),
            completion_tokens=usage.get("completion_tokens"),
            estimated_tokens=est_tokens,
            metadata={"latency_ms": _ms(started)},
        )
        content = data["choices"][0]["message"]["content"]
        if not content:
            log_llm_call(
                job_name,
                model["label"],
                model_name=model["model"],
                success=False,
                latency_ms=_ms(started),
                prompt_tokens=usage.get("prompt_tokens") or est_tokens,
                completion_tokens=usage.get("completion_tokens"),
                error="empty content",
            )
        return {"model": model["model"], "label": model["label"], "response": content}
    except Exception as e:
        try:
            log_llm_call(
                f"tasks.chat_parallel.{model.get('label', model.get('model', '?'))}",
                model.get("label", model.get("model", "?")),
                model_name=model.get("model"),
                success=False,
                latency_ms=_ms(started),
                error=str(e),
            )
        except Exception:
            pass
        print(f"[_chat_parallel][{model.get('label', '?')}] failed: {e}")
        return None


def _chat_parallel(models: list[dict], system: str, user_msg: str, timeout: int = 60) -> list[dict]:
    """Call multiple models in parallel. Returns successful responses if >= 2 succeed.

    Each model call has its own `timeout` (default 60s).
    The whole gather is bounded by an overall 90s timeout.
    Returns [] if 1 or fewer models succeeded.
    """
    async def _runner() -> list[dict]:
        async with httpx.AsyncClient() as client:
            tasks = [_call_one_async(client, m, system, user_msg, timeout) for m in models]
            try:
                overall_timeout = max(90, *[int(m.get("overall_timeout", timeout + 30)) for m in models])
                results = await asyncio.wait_for(
                    asyncio.gather(*tasks, return_exceptions=False),
                    timeout=overall_timeout,
                )
            except asyncio.TimeoutError:
                print("[_chat_parallel] overall timeout exceeded")
                return []
            return [r for r in results if r is not None]

    try:
        successes = asyncio.run(_runner())
    except Exception as e:
        print(f"[_chat_parallel] runner crashed: {e}")
        return []

    if len(successes) < 2:
        print(f"[_chat_parallel] only {len(successes)} model(s) succeeded — need >=2; returning []")
        return []
    print(f"[_chat_parallel] {len(successes)}/{len(models)} models succeeded: {[s['label'] for s in successes]}")
    return successes


NEBULAMIND_WEBHOOK = (
    "https://discord.com/api/webhooks/1489161782521106434/"
    "15-E1EQmKaUgkHIYJa9REM0J1g59b9cAUiiGZUWY9vQVIzjWjTyKYLHvCI-rVDylzwzE"
)
NEBULAMIND_BASE_URL = "https://nebulamind.net"


def _strip_md(text: str) -> str:
    """Strip markdown code fences from LLM output."""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0]
    return cleaned.strip()


def _notify(message: str) -> None:
    """Log agent activity. Discord notifications go via _notify_nebulamind_channel for approvals only."""
    print(f"[activity] {message}")


def _notify_nebulamind_channel(
    proposal_id: int, title: str, slug: str, version: int, content_preview: str
) -> None:
    """Post a rich approval notification to Discord #nebulamind channel. Currently disabled (too noisy)."""
    return  # disabled by Papa 2026-05-04
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


# ---------------------------------------------------------------------------
# Trust Phase 2: helper functions
# ---------------------------------------------------------------------------

def _parse_jury_json(text: str) -> dict | None:
    cleaned = strip_think_blocks(text)
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0]
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start < 0 or end < 0:
        return None
    try:
        return json.loads(cleaned[start:end+1])
    except Exception:
        return None


def _jury_retry(self, exc: Exception):
    """Retry stance jury calls without marking evidence as processed."""
    backoff = max(30, settings.STANCE_JURY_RETRY_BACKOFF_SECONDS)
    countdown = min(backoff * (2 ** getattr(self.request, "retries", 0)), 3600)
    raise self.retry(exc=exc, countdown=countdown)


def _agent_id_for_model(db, label: str, role: str = "jury") -> int | None:
    from app.models.agent import Agent as _Agent
    name = JURY_AGENT_LABELS.get(label, f"Jury-{label}")
    a = db.query(_Agent).filter(_Agent.name == name).first()
    if not a:
        a = _Agent(name=name, role=role, model_name=label, specialty="jury")
        db.add(a)
        db.flush()
    return a.id


def _abstract_looks_adversarial(abstract: str) -> bool:
    a = abstract.lower()
    return any(c in a for c in _CHAL_CUES)


def _adversarial_candidates(db):
    from app.models.claim import Claim as _Claim
    import datetime as _dt
    cutoff_age = _dt.datetime.utcnow() - _dt.timedelta(days=settings.ADVERSARIAL_CLAIM_MIN_AGE_DAYS)
    cutoff_probed = _dt.datetime.utcnow() - _dt.timedelta(days=settings.ADVERSARIAL_REPROBE_INTERVAL_DAYS)
    from sqlalchemy import or_
    return (
        db.query(_Claim)
        .filter(_Claim.trust_level == "accepted")
        .filter(_Claim.created_at < cutoff_age)
        .filter(or_(
            _Claim.last_adversarial_probe_at.is_(None),
            _Claim.last_adversarial_probe_at < cutoff_probed,
        ))
        .order_by(_Claim.last_adversarial_probe_at.asc().nulls_first())
        .limit(settings.ADVERSARIAL_PASS_BATCH_SIZE)
        .all()
    )


def _get_or_create_agent(db, name: str, role: str, model_name: str, specialty: str = None):
    from app.models.agent import Agent as _Agent
    a = db.query(_Agent).filter(_Agent.name == name).first()
    if not a:
        a = _Agent(name=name, role=role, model_name=model_name, specialty=specialty)
        db.add(a)
        db.flush()
    return a


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
            _run_evidence_linker_v2(db, agent)
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
        raw = _chat(agent.model_name, system_prompt, user_msg, role="editor")
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


_SYNTHESIS_MODEL = {
    "base_url": "http://localhost:11434/v1",
    "api_key": "ollama",
    "model": settings.ADVERSARIAL_QUERY_MODEL,
    "label": settings.ADVERSARIAL_QUERY_MODEL,
}

_SYNTHESIS_SYSTEM_PROMPT = (
    "You are a synthesis editor. Merge these 3 astronomy wiki drafts into "
    "one superior version, taking the best elements from each."
)


def _synthesize(drafts: list[dict], page_title: str) -> str:
    """Merge multiple wiki drafts into a single superior version via Tera.

    drafts: list of {"label": str, "response": str} from _chat_parallel.
    Falls back to the longest response if synthesis fails.
    """
    if not drafts:
        return ""

    longest = max(drafts, key=lambda d: len(d.get("response", "")))["response"]

    if len(drafts) == 1:
        return longest

    sections = []
    for i, d in enumerate(drafts, 1):
        sections.append(f"### Draft {i} ({d['label']})\n\n{d['response']}")
    user_msg = (
        f'Topic: "{page_title}"\n\n'
        f"Merge the following {len(drafts)} drafts into one superior wiki article. "
        f"Preserve the required section structure (## Overview, ## Discovery & History, "
        f"## Physical Properties, ## Current Research, ## Open Questions). Do NOT include a ## References section. "
        f"Take the strongest content from each draft, resolve contradictions, and produce "
        f"a single cohesive article. Return ONLY the merged article in markdown — no preamble.\n\n"
        + "\n\n".join(sections)
    )

    try:
        async def _runner() -> "str | None":
            async with httpx.AsyncClient() as client:
                result = await _call_one_async(
                    client, _SYNTHESIS_MODEL, _SYNTHESIS_SYSTEM_PROMPT, user_msg, timeout=120
                )
                return result["response"] if result else None

        merged = asyncio.run(_runner())
        if merged and merged.strip():
            print(f"[_synthesize] merged {len(drafts)} drafts via {_SYNTHESIS_MODEL['label']}")
            return merged
    except Exception as e:
        print(f"[_synthesize] synthesis failed: {e}")

    print(f"[_synthesize] falling back to longest draft ({len(longest)} chars)")
    return longest


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
            f"## Current Research, ## Open Questions. Do NOT include a ## References section. "
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

    # Phase 3: parallel writer (3 models) + synthesis via qwen3.6:27b-nvfp4
    parallel_models = [
        {"base_url": "http://localhost:11434/v1", "api_key": "ollama", "model": "llama3.3:70b",    "label": "llama3.3:70b"},
        {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.OLLAMA_STUDIO_HEAVY_MODEL, "label": settings.OLLAMA_STUDIO_HEAVY_MODEL},
        {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.OLLAMA_STUDIO_FAST_MODEL, "label": settings.OLLAMA_STUDIO_FAST_MODEL},
    ]
    if settings.GEMINI_API_KEY:
        parallel_models.append({"base_url": "https://generativelanguage.googleapis.com/v1beta/openai", "api_key": settings.GEMINI_API_KEY, "model": "gemini-2.5-flash", "label": "gemini-2.5-flash", "max_tokens": 8192})

    parallel_results = _chat_parallel(parallel_models, system_prompt, user_msg, timeout=60)

    if parallel_results:
        proposed = _synthesize(parallel_results, page.title)
    else:
        # Fallback: single _chat() path
        print(f"[{agent.name}] parallel writing unavailable, falling back to single _chat()")
        proposed = _chat(agent.model_name, system_prompt, user_msg, role="reviewer")

    # Throttle gate: skip if page already has pending proposals or agent hit daily limit
    allowed, reason = can_propose_edit(db, page.id, agent.id)
    if not allowed:
        print(f"[{agent.name}] Edit throttled for '{page.title}': {reason}")
        return

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

    # Phase 1: parallel multi-model voting (4 Ollama models)
    parallel_models = [
        {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.OLLAMA_STUDIO_FAST_MODEL, "label": settings.OLLAMA_STUDIO_FAST_MODEL},
        {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.OLLAMA_STUDIO_HEAVY_MODEL, "label": settings.OLLAMA_STUDIO_HEAVY_MODEL},
    ]
    if settings.GEMINI_API_KEY:
        parallel_models.append({"base_url": "https://generativelanguage.googleapis.com/v1beta/openai", "api_key": settings.GEMINI_API_KEY, "model": "gemini-2.5-flash", "label": "gemini-2.5-flash", "max_tokens": 8192})

    parallel_results = _chat_parallel(parallel_models, system, user_msg, timeout=90)

    def _parse_decision(raw_text: str) -> tuple[str, str]:
        try:
            cleaned = raw_text.strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.split("\n", 1)[1]
                cleaned = cleaned.rsplit("```", 1)[0]
            result = json.loads(cleaned)
            return result.get("decision", "reject"), result.get("reason", "")
        except (json.JSONDecodeError, KeyError):
            return "reject", f"Failed to parse LLM review response: {raw_text[:200]}"

    last_vote = None
    if parallel_results:
        for r in parallel_results:
            decision, reason = _parse_decision(r["response"])
            vote_value = 1 if decision == "approve" else -1
            v = Vote(
                edit_id=proposal.id,
                agent_id=agent.id,
                value=vote_value,
                reason=reason,
                model_name=r["label"],
            )
            db.add(v)
            db.flush()
            last_vote = v
            print(f"[{agent.name}][{r['label']}] Voted {'approve' if vote_value == 1 else 'reject'} on proposal #{proposal.id}: {reason[:80]}")
    else:
        # Fallback: single-model path
        print(f"[{agent.name}] parallel voting unavailable, falling back to single _chat()")
        raw = _chat(agent.model_name, system, user_msg, role="reviewer")
        decision, reason = _parse_decision(raw)
        vote_value = 1 if decision == "approve" else -1
        last_vote = Vote(
            edit_id=proposal.id,
            agent_id=agent.id,
            value=vote_value,
            reason=reason,
            model_name=agent.model_name or "",
        )
        db.add(last_vote)
        db.flush()
        print(f"[{agent.name}] Voted {'approve' if vote_value == 1 else 'reject'} on proposal #{proposal.id}: {reason[:80]}")

    from app.levels import get_vote_weight

    pos_votes = db.query(Vote).filter(Vote.edit_id == proposal.id, Vote.value == 1).all()
    weighted_sum = sum(get_vote_weight(v.agent_id, db) for v in pos_votes)
    total_needed = settings.VOTE_THRESHOLD
    decision_emoji = "👍" if last_vote and last_vote.value == 1 else "👎"
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
    """Pick a random page and leave an insightful comment.

    Phase 2: parallel multi-model commenting — each successful model produces
    a separate Comment record (not merged), tagged with model_name.
    Falls back to single _chat() path if parallel fails.
    """
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

    parallel_models = [
        {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.ADVERSARIAL_QUERY_MODEL, "label": settings.ADVERSARIAL_QUERY_MODEL},
        {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.OLLAMA_STUDIO_FAST_MODEL, "label": settings.OLLAMA_STUDIO_FAST_MODEL},
        {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.OLLAMA_STUDIO_HEAVY_MODEL, "label": settings.OLLAMA_STUDIO_HEAVY_MODEL},
    ]
    if settings.GEMINI_API_KEY:
        parallel_models.append({"base_url": "https://generativelanguage.googleapis.com/v1beta/openai", "api_key": settings.GEMINI_API_KEY, "model": "gemini-2.5-flash", "label": "gemini-2.5-flash", "max_tokens": 8192})

    parallel_results = _chat_parallel(parallel_models, system_prompt, user_msg, timeout=60)

    if parallel_results:
        for r in parallel_results:
            body = r["response"]
            comment = Comment(
                page_id=page.id,
                agent_id=agent.id,
                body=body,
                parent_id=None,
                model_name=r["label"],
            )
            db.add(comment)
            db.flush()
            preview = body[:80]
            suffix = "..." if len(body) > 80 else ""
            print(f"[{agent.name}][{r['label']}] Commented on page '{page.title}': {preview}{suffix}")
            _notify(f"💬 [{r['label']}] \"{page.title}\"에 코멘트: {preview}{suffix}")
    else:
        # Fallback: single-model path
        print(f"[{agent.name}] parallel commenting unavailable, falling back to single _chat()")
        body = _chat(agent.model_name, system_prompt, user_msg, role="commenter")
        comment = Comment(
            page_id=page.id,
            agent_id=agent.id,
            body=body,
            parent_id=None,
            model_name=agent.model_name or "",
        )
        db.add(comment)
        db.flush()
        print(f"[{agent.name}] Commented on page '{page.title}': {body[:80]}...")
        preview = comment.body[:80]
        suffix = "..." if len(comment.body) > 80 else ""
        _notify(f"💬 [{agent.model_name}] \"{page.title}\"에 코멘트: {preview}{suffix}")


def _run_evidence_linker_v1(db, agent: Agent):
    """Legacy evidence linker (single-model, LLM-guessed arXiv IDs). Keep for rollback."""
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
    raw = _chat(agent.model_name, SYSTEM_PROMPT, prompt, role="evidence_linker")

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

    from app.services.paper_search import verify_arxiv_id
    added = 0
    skipped = 0
    for p in papers[:2]:
        if not isinstance(p, dict) or not p.get("title"):
            continue
        arxiv_id = p.get("arxiv_id")
        # Phase 1 quality gate: hallucinated papers (no arxiv_id, or arxiv_id
        # the world doesn't recognize) are dropped instead of polluting the wiki.
        if not arxiv_id:
            skipped += 1
            continue
        v = verify_arxiv_id(arxiv_id, claim.text)
        if not v["verified"]:
            skipped += 1
            continue
        ev = Evidence(
            claim_id=claim.id,
            arxiv_id=arxiv_id,
            title=v["title"] or p.get("title", ""),
            authors=_normalize_authors(p.get("authors")),
            year=v["year"] or p.get("year"),
            summary=p.get("summary"),
            stance=p.get("stance", "supports"),
            added_by_agent_id=agent.id,
            url=f"https://arxiv.org/abs/{arxiv_id}",
            quality=v["quality"],
            arxiv_verified=True,
        )
        db.add(ev)
        added += 1

    if added:
        db.flush()
        from app.routers.claims import recalculate_trust_v2
        new_trust, _ = recalculate_trust_v2(claim.id, db, trigger="arxiv_verification")
        print(f"[{agent.name}] Linked {added} verified paper(s) to claim #{claim.id} "
              f"(trust: {new_trust}, skipped: {skipped})")
        _notify(f"🔗 [{agent.model_name}] 클레임 #{claim.id}에 근거 {added}개 연결 → {new_trust}")
    elif skipped:
        print(f"[{agent.name}] claim #{claim.id}: dropped {skipped} unverifiable paper(s)")


# ---------------------------------------------------------------------------
# Evidence Linker v2 (Phase 1) — real sources only
# ---------------------------------------------------------------------------

def can_propose_edit(db, page_id: int, agent_id: int) -> tuple[bool, str]:
    """Throttle gate: max 1 edit/page/agent/day, skip if page has pending proposals."""
    import datetime as _dt
    if settings.ARXIV_SKIP_PAGE_IF_PENDING_PROPOSALS:
        n_pending = db.query(EditProposal).filter(
            EditProposal.page_id == page_id,
            EditProposal.status == EditStatus.PENDING,
        ).count()
        if n_pending >= 1:
            return False, f"page has {n_pending} PENDING proposals"
    cutoff = _dt.datetime.utcnow() - _dt.timedelta(hours=24)
    n_today = db.query(EditProposal).filter(
        EditProposal.page_id == page_id,
        EditProposal.agent_id == agent_id,
        EditProposal.created_at > cutoff,
    ).count()
    if n_today >= settings.ARXIV_MAX_PAGE_EDITS_PER_PAGE_PER_DAY:
        return False, f"agent already proposed {n_today} edits on this page today"
    return True, "ok"


def schedule_stance_jury(claim_id: int) -> None:
    """Phase 2: enqueue stance jury for any unjudged evidence on this claim."""
    from app.models.claim import Claim as _Claim, Evidence as _Evidence
    db = SessionLocal()
    try:
        claim = db.query(_Claim).get(claim_id)
        if _stance_jury_is_held(claim=claim, claim_id=claim_id):
            print(f"[schedule_stance_jury] held skip for claim #{claim_id}")
            return
        pending = db.query(_Evidence).filter(
            _Evidence.claim_id == claim_id,
            _Evidence.stance_jury_run_at.is_(None),
            _Evidence.abstract.isnot(None),
        ).all()
        enqueued = 0
        for ev in pending:
            if _stance_jury_is_held(ev=ev, claim=claim):
                continue
            if _enqueue_stance_jury_task(run_stance_jury_for_evidence, ev.id, countdown=5):
                enqueued += 1
        if enqueued:
            print(f"[schedule_stance_jury] enqueued {enqueued} jury runs for claim #{claim_id}")
    finally:
        db.close()


def _maybe_create_jury_task(db, evidence_id: int, claim_id: int, page_id) -> None:
    """Create a JuryTask row when new evidence is inserted. Idempotent."""
    from app.models.jury import JuryTask as _JuryTask
    import datetime as _dt
    if db.query(_JuryTask).filter_by(evidence_id=evidence_id).first():
        return
    page_cat = None
    if page_id:
        from app.models.page import WikiPage as _WikiPage
        p = db.query(_WikiPage).get(page_id)
        page_cat = p.category if p else None
    db.add(_JuryTask(
        evidence_id=evidence_id,
        claim_id=claim_id,
        category=page_cat,
        votes_target=settings.OAC_JURY_VOTES_TARGET,
        expires_at=_dt.datetime.utcnow() + _dt.timedelta(days=settings.OAC_JURY_TASK_EXPIRY_DAYS),
    ))


def _check_arxiv_journal_ref(arxiv_id: str) -> str | None:
    """Fetch journal_ref from arXiv API for a single paper. Returns None on error or absence."""
    import urllib.request
    import urllib.error
    import xml.etree.ElementTree as ET
    try:
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}&max_results=1"
        req = urllib.request.Request(url, headers={"User-Agent": "NebulaMind/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            root = ET.fromstring(resp.read())
        ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
        for entry in root.findall("atom:entry", ns):
            jr = entry.find("arxiv:journal_ref", ns)
            if jr is not None and jr.text:
                return jr.text.strip()
    except Exception:
        pass
    return None


def _run_evidence_linker_v2(db, agent: Agent, target_claim=None, inserts_per_run=2):
    """Phase 1 evidence linker: real sources only, no hallucinated papers."""
    import json as _json
    from datetime import datetime, timedelta
    from app.models.claim import Claim, Evidence
    from app.services.intro_fetch import fetch_intro, select_excerpt
    from app.services.paper_search import _claim_keywords, search_papers, verify_for_claim
    from sqlalchemy import func as sqlfunc

    # ---- Pick a target claim ----
    if target_claim is None:
        cooloff = datetime.utcnow() - timedelta(days=settings.EVIDENCE_RETRY_COOLOFF_DAYS)
        subq = db.query(Evidence.claim_id).subquery()
        claim = (
            db.query(Claim)
            .filter(
                Claim.trust_level == "unverified",
                ~Claim.id.in_(subq),
                (Claim.evidence_search_attempted_at.is_(None)) |
                (Claim.evidence_search_attempted_at < cooloff),
            )
            .order_by(sqlfunc.random())
            .first()
        )
        if not claim:
            print(f"[{agent.name if agent else 'system'}] no unverified claims due for evidence search")
            return
    else:
        claim = target_claim

    page = db.query(WikiPage).get(claim.page_id)
    topic = page.title if page else "astronomy"

    # ---- Step 1: 4-model parallel query generation ----
    sys_prompt = (
        "You translate scientific claims into 1-2 ADS-style search queries. "
        "Return ONLY a JSON array of strings. No prose. "
        "Use astronomy terminology, key physical quantities, and proper nouns. "
        "Do NOT invent specific arXiv IDs."
    )
    user_msg = (
        f'Topic: "{topic}"\nClaim: "{claim.text}"\n\n'
        f'Generate 1-2 search queries optimized for ADS that would find papers '
        f'either supporting or challenging this claim.'
    )

    from app.services.llm_routing.routing import get_models as _get_models
    parallel_models = _get_models("query_gen")
    proposals = _chat_parallel(parallel_models, sys_prompt, user_msg, timeout=60)

    queries: list[str] = []
    for p in (proposals or []):
        try:
            cleaned = p["response"].strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0]
            arr = _json.loads(cleaned)
            for q in (arr if isinstance(arr, list) else [arr]):
                if isinstance(q, str) and 5 < len(q) < 250:
                    queries.append(q)
        except Exception:
            continue
    if not queries:
        queries = [f'"{topic}" {claim.text[:80]}']
    keyphrase_tokens = []
    claim_kw = _claim_keywords(claim.text)
    for token in re.findall(r"[A-Za-z][A-Za-z\-]+", claim.text.lower()):
        if token in claim_kw and token not in keyphrase_tokens:
            keyphrase_tokens.append(token)
        if len(keyphrase_tokens) >= 5:
            break
    if keyphrase_tokens:
        queries.append(f'full:"{" ".join(keyphrase_tokens)}"')
    queries = list(dict.fromkeys(queries))[:6]

    # ---- Step 2: deterministic paper search ----
    all_records = []
    for q in queries:
        try:
            all_records.extend(search_papers(q, rows=4))
        except Exception as e:
            print(f"[{agent.name}] search failed for '{q[:40]}': {e}")

    seen: set[str] = set()
    unique = []
    for r in all_records:
        key = r.arxiv_id or r.doi or r.title.lower().strip()
        if key and key not in seen:
            seen.add(key)
            unique.append(r)

    # ---- Step 3: verification + quality scoring ----
    verified = []
    intro_fetches = [0]

    def _intro_provider(arxiv_id: str, text: str) -> str | None:
        if intro_fetches[0] >= max(0, settings.INTRO_FETCH_PER_LINKER_RUN):
            return None
        intro_fetches[0] += 1
        intro_text = fetch_intro(arxiv_id, db)
        return select_excerpt(intro_text, text, cap=1200)

    for rec in unique[:12]:
        v = verify_for_claim(
            rec,
            claim.text,
            s2_cross_check=bool(rec.doi),
            intro_provider=_intro_provider,
        )
        if v:
            verified.append(v)
    verified.sort(key=lambda x: x.quality, reverse=True)

    # ---- Step 4: persist top-N (peer-reviewed papers only) ----
    from datetime import datetime as _dt
    top = verified[:inserts_per_run]
    added = 0
    rejected = 0
    ev_list = []
    for v in top:
        ed = v.record.to_evidence_dict()
        # Peer-review gate: accept only if DOI, ADS bibcode, or arXiv journal_ref present.
        # Pure preprints (arXiv only, no DOI, no bibcode, no journal_ref) are rejected.
        journal_ref = None
        is_peer_reviewed = bool(ed.get("doi") or ed.get("ads_bibcode"))
        if not is_peer_reviewed and ed.get("arxiv_id"):
            journal_ref = _check_arxiv_journal_ref(ed["arxiv_id"])
            is_peer_reviewed = bool(journal_ref)
        if not is_peer_reviewed:
            print(f"[{agent.name}] rejected pure preprint: {ed.get('arxiv_id') or ed.get('title', '')[:60]}")
            rejected += 1
            continue
        ev = Evidence(
            claim_id=claim.id,
            arxiv_id=ed["arxiv_id"],
            doi=ed["doi"],
            url=ed["url"],
            title=ed["title"],
            authors=ed["authors"],
            year=ed["year"],
            summary=None,
            stance=v.stance_hint or "supports",
            added_by_agent_id=agent.id if agent else None,
            quality=v.quality,
            abstract=ed["abstract"],
            intro_excerpt=v.intro_excerpt,
            intro_fetch_attempted_at=_dt.utcnow() if v.intro_excerpt else None,
            ads_bibcode=ed["ads_bibcode"],
            s2_paper_id=ed["s2_paper_id"],
            verified_at=_dt.utcnow(),
            arxiv_verified=bool(ed["arxiv_id"]),
            journal_ref=journal_ref,
            peer_reviewed=True,
        )
        db.add(ev)
        ev_list.append(ev)
        added += 1
    if rejected:
        print(f"[{agent.name if agent else 'system'}] rejected {rejected} pure preprint(s) for claim #{claim.id}")

    claim.evidence_search_attempted_at = _dt.utcnow()

    if added:
        db.flush()
        for _ev in ev_list:
            _maybe_create_jury_task(db, _ev.id, claim.id, claim.page_id)
        from app.routers.claims import recalculate_trust_v2
        new_trust, ts = recalculate_trust_v2(
            claim.id, db, trigger="evidence_linker_v2",
            actor_agent_id=agent.id if agent else None,
        )
        schedule_stance_jury(claim.id)
        print(f"[{agent.name if agent else 'system'}] linked {added} verified paper(s) to claim #{claim.id} "
              f"→ {new_trust} (TS={ts:+.2f})")
        _notify(
            f"🔗 [{(agent.model_name if agent else 'system')}] claim #{claim.id} +{added} verified → {new_trust}"
        )
    else:
        print(f"[{agent.name if agent else 'system'}] claim #{claim.id}: no verifiable papers from {len(unique)} candidates")
        _notify(f"🔍 [{(agent.model_name if agent else 'system')}] claim #{claim.id}: 0/{len(unique)} candidates passed verification")


# ---------------------------------------------------------------------------
# P1 Pipeline Redesign: drain_evidence_for_page
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.drain_evidence_for_page")
def drain_evidence_for_page(page_id: int):
    """
    Celery beat task to run the ADS/S2 evidence search directly for unverified
    established claims with <2 evidence.
    """
    from datetime import datetime, timedelta
    from app.models.claim import Claim, Evidence
    from sqlalchemy import func as sqlfunc

    db = SessionLocal()
    try:
        cooloff = datetime.utcnow() - timedelta(days=settings.EVIDENCE_RETRY_COOLOFF_DAYS)

        # Count evidence per claim to find those with < 2
        evidence_counts = (
            db.query(Evidence.claim_id, sqlfunc.count(Evidence.id).label("c"))
            .group_by(Evidence.claim_id)
            .subquery()
        )

        claims = (
            db.query(Claim)
            .outerjoin(evidence_counts, Claim.id == evidence_counts.c.claim_id)
            .filter(
                Claim.page_id == page_id,
                Claim.trust_level == "unverified",
                Claim.claim_type == "established",
                (evidence_counts.c.c == None) | (evidence_counts.c.c < 2),
                (Claim.evidence_search_attempted_at.is_(None)) |
                (Claim.evidence_search_attempted_at < cooloff),
            )
            .order_by(sqlfunc.random())
            .limit(5)
            .all()
        )

        if not claims:
            print(f"[system] drain_evidence_for_page({page_id}): No unverified claims due for search.")
            return

        for claim in claims:
            print(f"[system] drain_evidence_for_page: Running search for claim_id={claim.id}")
            # we run it for each found claim, overriding inserts_per_run to 3-4
            _run_evidence_linker_v2(db, agent=None, target_claim=claim, inserts_per_run=4)

    except Exception as e:
        print(f"[system] drain_evidence_for_page failed: {e}")
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Intro augmentation: backfill intro excerpts
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.backfill_intro_excerpts")
def backfill_intro_excerpts(batch_size: int | None = None):
    """Backfill intro excerpts for arXiv evidence with missing/terse abstracts."""
    import datetime as _dt
    from app.models.claim import Claim, Evidence
    from app.services.intro_fetch import fetch_intro, select_excerpt
    from sqlalchemy import func as sqlfunc, or_

    db = SessionLocal()
    processed = 0
    fetched = 0
    excerpted = 0
    errors = 0
    try:
        limit = max(1, int(batch_size or settings.INTRO_BACKFILL_BATCH))
        candidates = (
            db.query(Evidence, Claim)
            .join(Claim, Claim.id == Evidence.claim_id)
            .filter(Evidence.arxiv_id.isnot(None))
            .filter(Evidence.intro_excerpt.is_(None))
            .filter(or_(
                Evidence.abstract.is_(None),
                sqlfunc.length(Evidence.abstract) < 100,
                Evidence.stance_jury_run_at.is_(None),
            ))
            .order_by(Evidence.created_at)
            .limit(limit)
            .all()
        )
        for ev, claim in candidates:
            processed += 1
            ev.intro_fetch_attempted_at = _dt.datetime.utcnow()
            try:
                intro = fetch_intro(ev.arxiv_id, db) if ev.arxiv_id else None
                if intro:
                    fetched += 1
                    excerpt = select_excerpt(intro, claim.text, cap=1200)
                    if excerpt:
                        ev.intro_excerpt = excerpt
                        excerpted += 1
                db.commit()
            except Exception as exc:
                errors += 1
                db.rollback()
                print(f"[backfill_intro_excerpts] evidence #{ev.id} failed: {exc}")
            time.sleep(0.5)
        result = {
            "processed": processed,
            "intro_fetch_success": fetched,
            "excerpted": excerpted,
            "errors": errors,
        }
        print(f"[backfill_intro_excerpts] {result}")
        return result
    finally:
        db.close()


# ---------------------------------------------------------------------------
# P1 Pipeline Redesign: sync_verbatim_markers_nightly
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.sync_verbatim_markers_nightly")
def sync_verbatim_markers_nightly(page_id: int):
    """
    Nightly beat task to run sync_verbatim_claim_markers.py and check coverage.
    """
    import subprocess
    import json

    db = SessionLocal()
    try:
        cmd = [
            ".venv/bin/python",
            "scripts/sync_verbatim_claim_markers.py",
            "--commit",
            "--page", str(page_id)
        ]
        print(f"[system] Running nightly verbatim sync for page {page_id}...")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd="/Users/duhokim/NebulaMind/NebulaMind/backend")
        print(result.stdout)
        if result.stderr:
            print(result.stderr)

        # Coverage Map / Watchdog (Phase 4)
        from sqlalchemy import text
        from app.models.page import WikiPage
        page = db.execute(text("SELECT id, slug, content FROM wiki_pages WHERE id = :pid"), {"pid": page_id}).fetchone()
        if page and page.content:
            import re
            # Count visible asserted markers
            markers = {
                int(token.strip())
                for group in re.findall(r"<!--claim:([\d,\s]+)-->", page.content)
                for token in group.split(",")
                if token.strip()
            }
            visible_count = len(markers)
            
            # Count active assigned claims
            owned_res = db.execute(text("""
                SELECT c.id, c.trust_level 
                FROM claim_section_assignments a
                JOIN claims c ON c.id = a.claim_id
                WHERE a.page_id = :pid AND a.assignment_status = 'active'
            """), {"pid": page_id}).fetchall()
            
            active_claims = {r.id for r in owned_res}
            must_keep_claims = {r.id for r in owned_res if r.trust_level in ('accepted', 'consensus')}
            
            # --- Coverage v2 (2026-06-04): scope denominator to MUST-KEEP claims. ---
            # Rationale: accepted/consensus claims are the high-trust facts that
            # belong in article prose. Debated/unverified/structured-only claims are
            # correctly NOT inline (rendered via /claims API). The old denominator
            # (all active assignments) counted 462/478 structured-only nodes on p57,
            # making <50% unsatisfiable by construction. See Watchdog_Denominator_Fix_v1.md.
            must_keep_missing = must_keep_claims - markers
            mk_total = len(must_keep_claims)
            # Informational structural ratio (kept for the log, NOT for alerting):
            structural_ratio = visible_count / len(active_claims) if active_claims else 1.0
            # The alerting metric: fraction of must-keep claims present in prose.
            mk_coverage = (len(must_keep_claims & markers) / mk_total) if mk_total else 1.0

            print(
                f"[system] Watchdog for {page.slug}: must-keep coverage {mk_coverage:.1%} "
                f"({mk_total - len(must_keep_missing)}/{mk_total}); "
                f"structural {structural_ratio:.1%} ({visible_count}/{len(active_claims)}, info-only)"
            )
            
            from app.agent_loop.tasks import _notify
            # Only must-keep claims drive alerts now. Severity reflects a CONTENT gap,
            # not a "collapse": route to regen, do not cry catastrophe.
            if mk_total == 0:
                pass  # no high-trust claims yet — nothing to assert in prose
            elif mk_coverage < 0.50 or len(must_keep_missing) >= 10:
                msg = (
                    f"⚠️ [WARN] Page {page_id} must-keep prose coverage low: "
                    f"{mk_coverage:.1%}; {len(must_keep_missing)} high-trust claims not in prose. "
                    f"Content regeneration recommended."
                )
                print(msg)
                _notify(msg)
                from app.agent_loop.marker_embed.tasks import claim_marker_embed_page, marker_reembed_enabled
                if marker_reembed_enabled():
                    claim_marker_embed_page.delay(page_id)
                else:
                    print("[system] marker overlay repair suppressed: marker_embed:enabled is off")
            elif must_keep_missing:
                # A few missing: log + repair, but no notify (sub-alert noise floor).
                print(
                    f"📉 [info] Page {page_id} must-keep coverage {mk_coverage:.1%}, "
                    f"{len(must_keep_missing)} missing. Triggering repair pass."
                )
                from app.agent_loop.marker_embed.tasks import claim_marker_embed_page, marker_reembed_enabled
                if marker_reembed_enabled():
                    claim_marker_embed_page.delay(page_id)
                else:
                    print("[system] marker overlay repair suppressed: marker_embed:enabled is off")

    except Exception as e:
        print(f"[system] sync_verbatim_markers_nightly failed: {e}")
    finally:
        db.close()

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
# Wikipedia Summary Refresh
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.refresh_wikipedia_summaries")
def refresh_wikipedia_summaries():
    """Daily refresh of wiki_pages.wiki_summary for all Wikipedia-mapped pages.
    Scheduled: UTC 03:00 = KST 12:00.
    """
    import datetime as _dt
    from app.models.page import WikiPage
    from app.services.wikipedia_client import wp_summary, log_external
    from app.config import settings

    db = SessionLocal()
    try:
        cutoff = _dt.datetime.utcnow() - _dt.timedelta(days=settings.WIKIPEDIA_SUMMARY_REFRESH_DAYS)
        from sqlalchemy import or_
        pages = db.query(WikiPage).filter(
            WikiPage.wikipedia_title.isnot(None),
            or_(
                WikiPage.wiki_summary_fetched_at.is_(None),
                WikiPage.wiki_summary_fetched_at < cutoff
            )
        ).limit(settings.WIKIPEDIA_SUMMARY_MAX_PER_DAY).all()

        refreshed = 0
        failed = 0
        for page in pages:
            try:
                summary = wp_summary(page.wikipedia_title)
            except Exception as e:
                log_external(db, source="wikipedia",
                             external_id=page.wikipedia_title or "unknown",
                             page_id=page.id, decision="fetch_failed",
                             notes=str(e)[:200])
                failed += 1
                continue
            if not summary:
                log_external(db, source="wikipedia",
                             external_id=page.wikipedia_title or "unknown",
                             page_id=page.id, decision="fetch_failed",
                             notes="wp_summary returned None")
                failed += 1
                continue
            page.wiki_summary = summary.first_sentences(max_n=2)
            page.wiki_summary_url = summary.canonical_url
            page.wiki_summary_revision = summary.revision[:40]
            page.wiki_summary_license = summary.license
            page.wiki_summary_fetched_at = _dt.datetime.utcnow()
            log_external(db, source="wikipedia",
                         external_id=summary.revision[:100],
                         page_id=page.id, decision="summary_refreshed")
            refreshed += 1
            import time as _time
            _time.sleep(0.5)  # polite rate limiting

        db.commit()
        msg = f"📖 Wikipedia summaries: {refreshed} refreshed, {failed} failed"
        print(f"[refresh_wikipedia_summaries] {msg}")
        _notify(msg)
    except Exception as e:
        db.rollback()
        print(f"[refresh_wikipedia_summaries] Error: {e}")
        raise
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Wikipedia Bibliography Miner (PR-7)
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.mine_wikipedia_bibliography",
                 bind=True, max_retries=3)
def mine_wikipedia_bibliography(self, page_id: int):
    """Mine Wikipedia external links → ADS lookup → Evidence insertion."""
    import datetime as _dt
    from app.models.page import WikiPage
    from app.models.claim import Claim, Evidence
    from app.models.external import WikipediaReference
    from app.services.wikipedia_client import wp_external_links, log_external
    from app.services.paper_search import (
        ads_lookup_arxiv, ads_lookup_doi, extract_arxiv_id, extract_doi,
        is_arxiv, is_doi, verify_for_claim
    )
    from app.routers.claims import recalculate_trust_v2

    db = SessionLocal()
    try:
        page = db.query(WikiPage).get(page_id)
        if not page or not page.wikipedia_title:
            return

        # Skip if mined recently
        if page.wiki_biblio_mined_at:
            age_days = (_dt.datetime.utcnow() - page.wiki_biblio_mined_at).days
            if age_days < 30:
                print(f"[mine_wikipedia_bibliography] page #{page_id} mined {age_days}d ago, skipping")
                return

        wikibot = db.query(Agent).filter(Agent.name == "ArxivBot").first()
        if not wikibot:
            print("[mine_wikipedia_bibliography] ArxivBot not found, skipping")
            return

        # 1. Fetch external links
        refs = wp_external_links(page.wikipedia_title)
        arxiv_ids = list(dict.fromkeys(
            extract_arxiv_id(r) for r in refs if is_arxiv(r)
        ))
        arxiv_ids = [a for a in arxiv_ids if a]  # filter None
        doi_ids = list(dict.fromkeys(
            extract_doi(r) for r in refs if is_doi(r) and not is_arxiv(r)
        ))
        doi_ids = [d for d in doi_ids if d]  # filter None

        print(f"[mine_wikipedia_bibliography] page #{page_id} '{page.title}': "
              f"{len(arxiv_ids)} arXiv, {len(doi_ids)} DOI links found")

        # 2. Stage arXiv refs
        for arxiv_id in arxiv_ids[:settings.WIKIPEDIA_BIBLIO_ARXIV_CAP]:
            exists = db.query(WikipediaReference).filter_by(
                page_id=page_id, arxiv_id=arxiv_id
            ).first()
            if not exists:
                db.add(WikipediaReference(
                    page_id=page_id,
                    wikipedia_title=page.wikipedia_title,
                    source_url=f"https://arxiv.org/abs/{arxiv_id}",
                    arxiv_id=arxiv_id,
                    processed=False,
                ))

        # 3. Stage DOI refs
        for doi in doi_ids[:settings.WIKIPEDIA_BIBLIO_DOI_CAP]:
            exists = db.query(WikipediaReference).filter_by(
                page_id=page_id, doi=doi
            ).first()
            if not exists:
                db.add(WikipediaReference(
                    page_id=page_id,
                    wikipedia_title=page.wikipedia_title,
                    source_url=f"https://doi.org/{doi}",
                    doi=doi,
                    processed=False,
                ))
        db.flush()

        # 4. Process unprocessed staged refs
        claims = db.query(Claim).filter(Claim.page_id == page_id).all()
        pending_refs = db.query(WikipediaReference).filter_by(
            page_id=page_id, processed=False
        ).all()

        inserted_total = 0
        for ref in pending_refs:
            try:
                record = (
                    ads_lookup_arxiv(ref.arxiv_id) if ref.arxiv_id
                    else ads_lookup_doi(ref.doi)
                )
            except Exception as e:
                print(f"[mine_wikipedia_bibliography] ADS lookup failed: {e}")
                ref.processed = True
                ref.process_result = "ads_miss"
                ref.last_attempted_at = _dt.datetime.utcnow()
                continue

            if not record:
                ref.processed = True
                ref.process_result = "ads_miss"
                ref.last_attempted_at = _dt.datetime.utcnow()
                log_external(db, source="wikipedia",
                             external_id=(ref.arxiv_id or ref.doi or "unknown")[:100],
                             page_id=page_id, decision="ads_miss")
                continue

            any_inserted = False
            for claim in claims:
                try:
                    verified = verify_for_claim(record, claim.text)
                except Exception:
                    continue

                if not verified or verified.quality < settings.EVIDENCE_MIN_QUALITY_FOR_ACCEPTED:
                    continue

                # Idempotent check
                existing = db.query(Evidence).filter_by(
                    claim_id=claim.id,
                    arxiv_id=record.arxiv_id,
                ).first() if record.arxiv_id else None
                if existing:
                    continue

                ev = Evidence(
                    claim_id=claim.id,
                    arxiv_id=record.arxiv_id,
                    doi=record.doi,
                    title=record.title,
                    year=record.year,
                    abstract=record.abstract,
                    ads_bibcode=record.bibcode,
                    stance=verified.stance_hint or "supports",
                    quality=verified.quality,
                    added_by_agent_id=wikibot.id,
                    verified_at=_dt.datetime.utcnow(),
                    source_channel="wikipedia_biblio",
                )
                db.add(ev)
                db.flush()
                _maybe_create_jury_task(db, ev.id, claim.id, page_id)

                try:
                    recalculate_trust_v2(claim.id, db,
                                        trigger="wikipedia_biblio_mine",
                                        actor_agent_id=wikibot.id)
                except Exception as e:
                    print(f"[mine_wikipedia_bibliography] trust recalc failed: {e}")

                log_external(db, source="wikipedia",
                             external_id=(record.arxiv_id or record.doi or "")[:100],
                             page_id=page_id, claim_id=claim.id,
                             evidence_id=ev.id, decision="evidence_inserted",
                             quality=verified.quality)
                any_inserted = True
                inserted_total += 1

            ref.processed = True
            ref.process_result = "evidence_inserted" if any_inserted else "no_claim_match"
            ref.last_attempted_at = _dt.datetime.utcnow()

        page.wiki_biblio_mined_at = _dt.datetime.utcnow()
        db.commit()
        print(f"[mine_wikipedia_bibliography] page #{page_id} done: "
              f"{inserted_total} evidence inserted from {len(pending_refs)} refs")

    except Exception as exc:
        db.rollback()
        print(f"[mine_wikipedia_bibliography] Error page #{page_id}: {exc}")
        raise self.retry(exc=exc, countdown=300)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Phase E: New-Topic Clustering → NewPageProposal
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.triage_new_page_proposals")
def triage_new_page_proposals():
    """D1 triage pass: expire stale low-similarity proposals, enforce queue cap."""
    from app.services.proposal_triage import run_triage

    db = SessionLocal()
    try:
        result = run_triage(db)
        print(f"[triage_new_page_proposals] {result}")
        return result
    except Exception as e:
        db.rollback()
        print(f"[triage_new_page_proposals] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.cluster_new_topic_candidates")
def cluster_new_topic_candidates():
    """Cluster new-topic arxiv papers → NewPageProposal rows → Discord batch notify."""
    import datetime as _dt
    import math
    from collections import defaultdict
    from app.models.arxiv import ArxivPaper
    from app.models.external import NewPageProposal
    from app.services.arxiv_classifier import _tokenize, _tfidf_vector, _cosine
    from slugify import slugify

    db = SessionLocal()
    try:
        cutoff = _dt.datetime.utcnow() - _dt.timedelta(days=settings.ARXIV_NEW_TOPIC_LOOKBACK_DAYS)
        papers = db.query(ArxivPaper).filter(
            ArxivPaper.match_type == "new_topic_candidate",
            ArxivPaper.submitted >= cutoff.strftime("%Y-%m-%d"),
        ).all()

        if not papers:
            print("[cluster_new_topic_candidates] No new_topic_candidate papers in window")
            return

        print(f"[cluster_new_topic_candidates] {len(papers)} candidate papers in last {settings.ARXIV_NEW_TOPIC_LOOKBACK_DAYS}d")

        # Build TF-IDF vectors for all candidate papers
        def paper_text(p):
            return f"{p.title} {(p.abstract or '')[:800]}"

        # Build a simple IDF over this local corpus
        all_tokens = [_tokenize(paper_text(p)) for p in papers]
        df: defaultdict = defaultdict(int)
        for tokens in all_tokens:
            for t in set(tokens):
                df[t] += 1
        N = len(papers) or 1
        idf = {t: math.log((N + 1) / (c + 1)) + 1.0 for t, c in df.items()}

        # Compute per-paper TF-IDF vectors
        vecs = [_tfidf_vector(tokens, idf) for tokens in all_tokens]

        # Greedy clustering by centroid similarity
        clusters: list[list[int]] = []   # each cluster = list of paper indices
        centroids: list[dict] = []

        for i, vec in enumerate(vecs):
            best_cluster = -1
            best_sim = settings.ARXIV_NEW_TOPIC_CENTROID_THRESHOLD
            for j, centroid in enumerate(centroids):
                sim = _cosine(vec, centroid)
                if sim > best_sim:
                    best_sim = sim
                    best_cluster = j

            if best_cluster >= 0:
                clusters[best_cluster].append(i)
                # Update centroid: average of all paper vectors in cluster
                cluster_vecs = [vecs[idx] for idx in clusters[best_cluster]]
                all_keys = set().union(*cluster_vecs)
                centroids[best_cluster] = {
                    k: sum(v.get(k, 0.0) for v in cluster_vecs) / len(cluster_vecs)
                    for k in all_keys
                }
            else:
                clusters.append([i])
                centroids.append(dict(vec))

        # Filter clusters by minimum size
        big_clusters = [(c, centroids[j]) for j, c in enumerate(clusters)
                        if len(c) >= settings.ARXIV_NEW_TOPIC_MIN_CLUSTER_SIZE]

        print(f"[cluster_new_topic_candidates] {len(big_clusters)} clusters >= {settings.ARXIV_NEW_TOPIC_MIN_CLUSTER_SIZE} papers")

        created = 0
        for cluster_indices, centroid in big_clusters:
            cluster_papers_obj = [papers[i] for i in cluster_indices]
            arxiv_ids = [p.arxiv_id for p in cluster_papers_obj]

            # Pick the cluster's "best title": the paper title most similar to centroid
            best_title = max(
                cluster_papers_obj,
                key=lambda p: _cosine(vecs[papers.index(p)], centroid)
            ).title

            # Clean title for slug
            suggested_title = best_title[:100]
            suggested_slug = slugify(suggested_title)[:120]

            if not suggested_slug:
                continue

            # D1 dedupe gate: exact proposal slug + exact/fuzzy wiki page slug
            from app.services.proposal_triage import is_duplicate_slug
            dup_reason = is_duplicate_slug(db, suggested_slug)
            if dup_reason:
                print(f"[cluster_new_topic_candidates] dedupe skip '{suggested_slug}': {dup_reason}")
                continue

            # Compute avg centroid similarity of cluster members
            avg_sim = sum(
                _cosine(vecs[papers.index(p)], centroid)
                for p in cluster_papers_obj
            ) / len(cluster_papers_obj)

            import json as _json
            proposal = NewPageProposal(
                suggested_slug=suggested_slug,
                suggested_title=suggested_title,
                cluster_papers=_json.dumps(arxiv_ids),
                centroid_similarity=avg_sim,
                status="pending",
            )
            db.add(proposal)
            created += 1
            print(f"[cluster_new_topic_candidates] New proposal: '{suggested_title}' ({len(arxiv_ids)} papers, sim={avg_sim:.3f})")

        if created:
            db.flush()

        # Batch-notify Discord when ≥3 proposals accumulate OR after 24h
        _maybe_notify_new_proposals(db)

        db.commit()
        print(f"[cluster_new_topic_candidates] Done: {created} new proposals created")
        _notify(f"🌌 Topic clustering: {created} new page proposals created from {len(papers)} candidates")

    except Exception as e:
        db.rollback()
        print(f"[cluster_new_topic_candidates] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.normalize_hero_facts")
def normalize_hero_facts():
    """Tier-cascade for hero_facts: A (KNOWN_CONSTANTS) → B (claim matcher) → suppress."""
    import json as _json
    import datetime as _dt
    from app.services.hero_facts import (
        FORBIDDEN_VAGUE, find_known_constant,
        try_authoritative_source, try_claim_grounded_source,
        _should_suppress_tier_c,
    )
    from app.models.page import WikiPage as _WikiPage

    db = SessionLocal()
    try:
        pages = db.query(_WikiPage).filter(_WikiPage.hero_facts.isnot(None)).all()
        n_pages_changed = n_promoted_a = n_promoted_b = n_kept_c = n_dropped = 0

        for page in pages:
            try:
                facts = _json.loads(page.hero_facts)
            except Exception:
                continue
            if not isinstance(facts, list):
                continue

            new_facts = []
            changed = False

            for f in facts:
                if not isinstance(f, dict):
                    continue
                src = f.get("source") or {}

                # 1. Already authoritatively sourced → leave alone
                if src.get("tier") in ("authoritative", "claim"):
                    new_facts.append(f)
                    continue

                # 2. Vague-language path: try KNOWN_CONSTANTS, else suppress
                value_str = str(f.get("value", "")).lower().strip()
                vague = (
                    value_str in FORBIDDEN_VAGUE
                    or any(w in value_str.split() for w in FORBIDDEN_VAGUE)
                )
                if vague:
                    rep = find_known_constant(f.get("label", ""), f.get("unit"))
                    if rep:
                        rep["label"] = f.get("label", rep.get("label", ""))
                        new_facts.append(rep)
                        n_promoted_a += 1
                    else:
                        n_dropped += 1
                    changed = True
                    continue

                # 3. Tier C path: try A → B → suppress/keep
                a_source = try_authoritative_source(f)
                if a_source:
                    f = dict(f)
                    f["source"] = a_source
                    new_facts.append(f)
                    n_promoted_a += 1
                    changed = True
                    continue

                b_source = try_claim_grounded_source(f, page.id, db)
                if b_source:
                    f = dict(f)
                    f["source"] = b_source
                    new_facts.append(f)
                    n_promoted_b += 1
                    changed = True
                    continue

                # 4. Suppress per rules
                if _should_suppress_tier_c(f):
                    n_dropped += 1
                    changed = True
                    continue

                # 5. Explicitly mark remaining as Tier C (was implicit before)
                f = dict(f)
                f["source"] = {
                    "tier": "ai_estimate",
                    "attribution": "AI estimate (no peer-reviewed source linked)",
                    "cited_at": _dt.datetime.utcnow().isoformat(),
                }
                new_facts.append(f)
                n_kept_c += 1
                changed = True

            if changed:
                page.hero_facts = _json.dumps(new_facts, ensure_ascii=False)
                n_pages_changed += 1

        db.commit()
        msg = (
            f"📊 Hero facts normalized: {n_pages_changed} pages changed, "
            f"+{n_promoted_a} → Tier A, +{n_promoted_b} → Tier B, "
            f"{n_kept_c} kept Tier C, {n_dropped} suppressed"
        )
        print(msg)
        _notify(msg)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Evidence Highlights
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.refresh_evidence_highlights")
def refresh_evidence_highlights(page_id: int | None = None):
    """Regenerate the EVIDENCE_HIGHLIGHTS block on one or all pages. No LLM — pure templating."""
    import json as _json
    from app.models.page import WikiPage as _WikiPage
    from app.models.claim import Claim as _Claim, Evidence as _Evidence

    db = SessionLocal()
    try:
        if page_id:
            pages = [db.query(_WikiPage).get(page_id)]
        else:
            pages = db.query(_WikiPage).filter(_WikiPage.content != "").all()

        updated = 0
        for page in pages:
            if not page or not page.content:
                continue

            # Get top 5 evidence by quality DESC, year DESC for this page
            top_ev = (
                db.query(_Evidence)
                .join(_Claim, _Evidence.claim_id == _Claim.id)
                .filter(
                    _Claim.page_id == page.id,
                    _Evidence.quality >= 0.40,
                    _Evidence.arxiv_id.isnot(None),
                    _Evidence.title.isnot(None),
                )
                .order_by(_Evidence.quality.desc(), _Evidence.year.desc())
                .limit(5)
                .all()
            )
            if not top_ev:
                continue

            # Count trust levels for this page
            from sqlalchemy import func as _func
            trust_counts = dict(
                db.query(_Claim.trust_level, _func.count(_Claim.id))
                .filter(_Claim.page_id == page.id)
                .group_by(_Claim.trust_level)
                .all()
            )
            n_evidence = (
                db.query(_func.count(_Evidence.id))
                .join(_Claim, _Evidence.claim_id == _Claim.id)
                .filter(_Claim.page_id == page.id)
                .scalar() or 0
            )
            n_consensus = trust_counts.get("consensus", 0)
            n_accepted = trust_counts.get("accepted", 0)
            n_debated = trust_counts.get("debated", 0)

            # Build bullet list
            bullets = []
            for ev in top_ev:
                authors = ""
                if ev.authors:
                    try:
                        au_list = _json.loads(ev.authors) if ev.authors.startswith("[") else [ev.authors]
                        # Handle legacy single-string comma-sep entries
                        if len(au_list) == 1 and "," in au_list[0]:
                            au_list = [n.strip() for n in au_list[0].split(",") if n.strip()]
                        first_au = au_list[0].split(" ")[-1] if au_list else ""
                        authors = f"{first_au} et al." if len(au_list) > 1 else first_au
                    except Exception:
                        authors = str(ev.authors)[:30]
                year_str = f" ({ev.year})" if ev.year else ""
                arxiv_link = f"https://arxiv.org/abs/{ev.arxiv_id}"
                stance_emoji = "✅" if ev.stance == "supports" else "⚠️" if ev.stance == "challenges" else "➖"
                summary_snippet = (ev.summary or "")[:120].rstrip()
                bullets.append(
                    f"- {stance_emoji} **{authors}{year_str}** — [{ev.title[:80]}]({arxiv_link})"
                    + (f". *{summary_snippet}*" if summary_snippet else "")
                )

            block = (
                "\n<!-- EVIDENCE_HIGHLIGHTS_START -->\n"
                "## Evidence Highlights\n\n"
                f"This page is supported by **{n_evidence} cited papers**, including:\n\n"
                + "\n".join(bullets)
                + f"\n\n<small>*{n_consensus} consensus · {n_accepted} accepted · {n_debated} debated claims*</small>\n"
                "<!-- EVIDENCE_HIGHLIGHTS_END -->"
            )

            # Strip old block if present
            content = page.content
            if "<!-- EVIDENCE_HIGHLIGHTS_START -->" in content:
                start_idx = content.find("<!-- EVIDENCE_HIGHLIGHTS_START -->")
                end_idx = content.find("<!-- EVIDENCE_HIGHLIGHTS_END -->")
                if end_idx > 0:
                    content = content[:start_idx].rstrip() + content[end_idx + len("<!-- EVIDENCE_HIGHLIGHTS_END -->"):]

            page.content = content.rstrip() + block
            updated += 1

        db.commit()
        print(f"[refresh_evidence_highlights] Updated {updated} pages")
        if updated > 5:
            _notify(f"📚 Evidence highlights refreshed on {updated} pages")
    except Exception as e:
        db.rollback()
        print(f"[refresh_evidence_highlights] Error: {e}")
        raise
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Trust Phase 2: Celery tasks
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.run_stance_jury_for_evidence",
                 bind=True, max_retries=2, default_retry_delay=300)
def run_stance_jury_for_evidence(self, evidence_id: int):
    """4-model parallel jury reads (claim, abstract) and votes per evidence."""
    import datetime as _dt
    from app.models.claim import Claim, Evidence, EvidenceVote
    from app.routers.claims import recalculate_trust_v2

    db = SessionLocal()
    try:
        ev = db.query(Evidence).get(evidence_id)
        if not ev or ev.stance_jury_run_at is not None:
            _release_stance_jury_inflight(evidence_id)
            return  # idempotent
        if _stance_jury_is_held(ev=ev, evidence_id=evidence_id):
            print(f"[stance_jury] held skip for evidence #{evidence_id}")
            _release_stance_jury_inflight(evidence_id)
            return
        abstract_text = ev.abstract or ""
        intro_excerpt = ev.intro_excerpt or ""
        if (
            len(abstract_text) < settings.STANCE_JURY_MIN_ABSTRACT_CHARS
            and len(intro_excerpt) < settings.INTRO_EXCERPT_MIN_CHARS
        ):
            ev.stance_jury_run_at = _dt.datetime.utcnow()
            db.commit()
            _release_stance_jury_inflight(evidence_id)
            return

        claim = db.query(Claim).get(ev.claim_id)
        if not claim:
            _release_stance_jury_inflight(evidence_id)
            return
        if _stance_jury_is_held(ev=ev, claim=claim):
            print(f"[stance_jury] held skip for evidence #{evidence_id} claim #{claim.id}")
            _release_stance_jury_inflight(evidence_id)
            return

        user_msg = (
            f'Claim from the wiki:\n"{claim.text}"\n\n'
            f'Cited paper:\n"{ev.title}" '
            f'({"arXiv:" + ev.arxiv_id if ev.arxiv_id else "DOI:" + (ev.doi or "")}, '
            f'{ev.year or "n.d."})\n\n'
            f'Abstract:\n{abstract_text[:2000]}\n\n'
            f'Introduction excerpt:\n{intro_excerpt[:1200]}\n\n'
            f'Asserted stance: {ev.stance}\n\n'
            f'Respond ONLY with JSON: {{"stance_correct": true|false, "vote": 1|-1|0, "reason": "<one sentence>"}}'
        )

        results = _chat_parallel(STANCE_JURY_MODELS, STANCE_JURY_SYSTEM, user_msg,
                                  timeout=settings.STANCE_JURY_TIMEOUT_SECONDS)

        if not results:
            raise RuntimeError(f"no stance jury model responses for evidence #{evidence_id}")

        wrong_stance_count = 0
        parsed_count = 0
        votes_added = 0
        jurors_data = []
        for r in results:
            parsed = _parse_jury_json(r["response"])
            if not parsed:
                continue
            parsed_count += 1
            if not parsed.get("stance_correct", True):
                wrong_stance_count += 1
            value = max(-1, min(1, int(parsed.get("vote", 0))))
            agent_id = _agent_id_for_model(db, r["label"])
            jurors_data.append({
                "agent_id": agent_id,
                "vote": value,
                "confidence_str": "MEDIUM",
                "reason": (parsed.get("reason") or "")[:500],
                "model_name": r["label"]
            })
            if value == 0:
                continue
            db.add(EvidenceVote(
                evidence_id=ev.id, value=value,
                agent_id=agent_id, voter_type="jury",
                weight=1.0,
                reason=(parsed.get("reason") or "")[:500],
            ))
            votes_added += 1

        if parsed_count == 0:
            raise RuntimeError(f"stance jury returned no parseable votes for evidence #{evidence_id}")

        # Stance gate: 3+ of 4 say wrong → flip (one-time only)
        if wrong_stance_count >= settings.STANCE_JURY_FLIP_THRESHOLD:
            old_stance = ev.stance
            ev.stance = "challenges" if ev.stance == "supports" else "supports"
            print(f"[stance_jury] ev #{evidence_id}: STANCE FLIPPED {old_stance}→{ev.stance}")
            _notify(f"⚠️ Stance flipped on ev #{evidence_id} (claim #{ev.claim_id})")

        ev.stance_jury_run_at = _dt.datetime.utcnow()
        db.flush()

        try:
            from app.services.jury_shadow import execute_shadow_validation
            execute_shadow_validation(
                db=db,
                evidence_id=ev.id,
                claim_id=claim.id,
                claim_text=claim.text,
                evidence_title=ev.title,
                legacy_stance=ev.stance,
                legacy_quality=ev.quality,
                jurors_data=jurors_data
            )
        except Exception as shadow_err:
            print(f"[stance_jury] shadow validation failed: {shadow_err}")

        old_trust = claim.trust_level

        # Recompute trust
        result = recalculate_trust_v2(ev.claim_id, db,
                                       trigger="stance_jury", actor_agent_id=None)
        new_trust = result[0] if isinstance(result, tuple) else result
        db.commit()
        _release_stance_jury_inflight(evidence_id)
        print(f"[stance_jury] ev #{evidence_id}: {votes_added} votes, "
              f"claim #{ev.claim_id} → {new_trust}")

        # Notify on trust level promotions
        if new_trust == "consensus":
            _notify(f"🟢 Claim #{ev.claim_id} → consensus: \"{claim.text[:80]}…\"")
        elif new_trust == "challenged":
            _notify(f"🔴 Claim #{ev.claim_id} → challenged: \"{claim.text[:80]}…\"")

        # §16 demotion trigger: if claim just became debated/challenged, seed ideas for it
        if new_trust in ("debated", "challenged") and old_trust not in ("debated", "challenged"):
            try:
                import redis as _redis_lib
                from app.config import settings as _s
                _phase3 = _redis_lib.from_url(_s.REDIS_URL, decode_responses=True).get(
                    "research_ideas:phase3_enabled"
                ) == "1"
            except Exception:
                _phase3 = False
            if _phase3:
                try:
                    from app.agent_loop.research_ideas.auto_improvement import seed_debated_claim_ideas
                    seed_debated_claim_ideas.delay(page_id=claim.page_id, target_per_claim=3)
                except Exception:
                    pass

    except Exception as e:
        db.rollback()
        print(f"[stance_jury] ev #{evidence_id} error: {e}")
        _jury_retry(self, e)
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.drain_stance_jury_backlog")
def drain_stance_jury_backlog():
    """Hourly: pace unjudged evidence into stance jury tasks."""
    import datetime as _dt
    from app.models.claim import Claim, Evidence, EvidenceVote
    from sqlalchemy import func as sqlfunc, case, or_

    if not settings.STANCE_JURY_ENABLED:
        return

    db = SessionLocal()
    try:
        cutoff = _dt.datetime.utcnow() - _dt.timedelta(hours=1)
        recent_jury = db.query(sqlfunc.count(EvidenceVote.id)).filter(
            EvidenceVote.created_at > cutoff,
            EvidenceVote.voter_type == "jury",
        ).scalar() or 0
        hourly_cap = min(settings.STANCE_JURY_MAX_PER_HOUR, settings.STANCE_JURY_MAX_ENQUEUE_PER_HOUR)
        budget = max(0, hourly_cap - (recent_jury // 4))
        if budget == 0:
            print("[stance_jury] hourly budget exhausted, skipping")
            return

        candidates_query = (
            db.query(Evidence)
            .join(Claim, Claim.id == Evidence.claim_id)
            .filter(Evidence.stance_jury_run_at.is_(None))
            .filter(or_(
                sqlfunc.length(Evidence.abstract) >= settings.STANCE_JURY_MIN_ABSTRACT_CHARS,
                sqlfunc.length(Evidence.intro_excerpt) >= settings.INTRO_EXCERPT_MIN_CHARS,
            ))
        )
        candidates = (
            _apply_stance_jury_held_filters(candidates_query, Evidence, Claim)
            .order_by(
                case((Claim.trust_level == "accepted", 0), else_=1),
                Evidence.created_at,
            )
            .limit(budget)
            .all()
        )

        spacing = max(1, settings.STANCE_JURY_ENQUEUE_SPACING_SECONDS)
        enqueued = 0
        skipped_inflight = 0
        for idx, ev in enumerate(candidates):
            countdown = 2 + idx * spacing
            if _enqueue_stance_jury_task(run_stance_jury_for_evidence, ev.id, countdown=countdown):
                enqueued += 1
            else:
                skipped_inflight += 1

        print(f"[stance_jury] enqueued {enqueued} jury runs (budget={budget}, skipped_inflight={skipped_inflight})")
        if enqueued >= 10:
            _notify(f"🧑\u200d⚖️ [Phase 2] {enqueued} evidence queued for jury this hour")
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.settle_evidence_and_update_rep")
def settle_evidence_and_update_rep():
    """Hourly at :15 — settle voted evidence and update agent reputations."""
    import datetime as _dt
    from app.models.claim import Evidence, EvidenceVote
    from app.models.agent import Agent as _Agent
    from app.models.jury import ReputationLog

    if not settings.OAC_ENABLED:
        return

    db = SessionLocal()
    try:
        cutoff = _dt.datetime.utcnow() - _dt.timedelta(hours=settings.OAC_JURY_SETTLEMENT_HOURS)
        candidates = (
            db.query(Evidence)
            .filter(Evidence.stance_jury_run_at < cutoff)
            .filter(Evidence.consensus_settled_at.is_(None))
            .filter(Evidence.consensus_vote.is_(None))
            .limit(200)
            .all()
        )

        settled = 0
        rep_changes = 0
        for ev in candidates:
            votes = db.query(EvidenceVote).filter(EvidenceVote.evidence_id == ev.id).all()
            if len(votes) < settings.OAC_JURY_SETTLEMENT_MIN_VOTES:
                continue
            weighted = sum(v.value * (v.weight or 1.0) for v in votes)
            if weighted == 0:
                continue  # tied, come back later
            consensus_vote = 1 if weighted > 0 else -1
            ev.consensus_vote = consensus_vote
            ev.consensus_settled_at = _dt.datetime.utcnow()
            settled += 1

            for v in votes:
                if v.agent_id is None or v.value == 0:
                    continue
                agent = db.query(_Agent).get(v.agent_id)
                if not agent or getattr(agent, "status", "active") != "active":
                    continue
                agreed = (v.value == consensus_vote)
                delta = settings.OAC_REPUTATION_AGREE_DELTA if agreed else settings.OAC_REPUTATION_DISAGREE_DELTA
                old_rep = getattr(agent, "reputation", 0.5)
                new_rep = max(settings.OAC_REPUTATION_FLOOR,
                              min(settings.OAC_REPUTATION_CEILING, old_rep + delta))
                # Cap new agents
                total_votes = getattr(agent, "total_jury_votes", 0)
                if total_votes < settings.OAC_NEW_AGENT_GRACE_VOTES:
                    new_rep = min(new_rep, settings.OAC_NEW_AGENT_REPUTATION_CAP)
                agent.reputation = new_rep
                agent.reputation_updated_at = _dt.datetime.utcnow()
                agent.total_jury_votes = total_votes + 1
                if agreed:
                    agent.agreed_jury_votes = getattr(agent, "agreed_jury_votes", 0) + 1
                agent.accuracy = agent.agreed_jury_votes / max(1, agent.total_jury_votes)

                # Auto-infer topic affinity after 50 votes (OAC spec §6)
                if agent.total_jury_votes == 50 and not agent.topic_affinity:
                    try:
                        from app.models.claim import Claim, Evidence, EvidenceVote
                        from app.models.page import WikiPage as _WikiPage
                        from collections import Counter as _Counter
                        # Get categories of evidence this agent voted positively on
                        cat_votes = db.query(_WikiPage.category).join(
                            Claim, Claim.page_id == _WikiPage.id
                        ).join(Evidence, Evidence.claim_id == Claim.id).join(
                            EvidenceVote, EvidenceVote.evidence_id == Evidence.id
                        ).filter(
                            EvidenceVote.agent_id == agent.id,
                            EvidenceVote.value > 0,
                            _WikiPage.category.isnot(None),
                        ).all()
                        counts = _Counter(r[0] for r in cat_votes if r[0])
                        if counts:
                            top_cats = [c for c, _ in counts.most_common(3)]
                            agent.topic_affinity = ",".join(top_cats)
                            _notify(f"🎯 Agent {agent.name} affinity auto-set: {agent.topic_affinity}")
                    except Exception:
                        pass
                db.add(ReputationLog(
                    agent_id=agent.id,
                    delta=delta,
                    old_value=old_rep,
                    new_value=new_rep,
                    old_reputation=old_rep,
                    new_reputation=new_rep,
                    reason="vote_agreed_consensus" if agreed else "vote_disagreed_consensus",
                    ref_id=ev.id,
                    ref_type="evidence",
                ))
                rep_changes += 1

                # Auto-mute check
                if (agent.reputation <= settings.OAC_MUTE_THRESHOLD
                        and agent.total_jury_votes >= settings.OAC_MUTE_MIN_VOTES):
                    agent.status = "muted"
                    _notify(f"⚠️ Agent {agent.name} auto-muted (rep={agent.reputation:.2f})")

        # E1/E2 auto-escalation check after settling
        if settled and settings.OAC_ENABLED:
            from app.services.council import evaluate_escalation_triggers, open_escalation
            from app.models.council import Escalation
            ev_settled_ids = [ev.id for ev in candidates if ev.consensus_settled_at is not None]
            for ev_id in ev_settled_ids:
                ev = db.query(Evidence).filter(Evidence.id == ev_id).first()
                if not ev:
                    continue
                all_votes = db.query(EvidenceVote).filter(EvidenceVote.evidence_id == ev_id).all()
                trigger = evaluate_escalation_triggers(db, ev_id, all_votes)
                if trigger:
                    # Check for existing open escalation
                    existing = db.query(Escalation).filter(
                        Escalation.source_kind == "evidence_vote",
                        Escalation.source_id == ev_id,
                        Escalation.status == "open",
                    ).first()
                    if not existing:
                        esc = open_escalation(db, "evidence_vote", ev_id, trigger,
                            trigger_detail=f"Auto-triggered after jury settlement (ev #{ev_id})")
                        print(f"[settle_rep] Auto-escalation #{esc.id} opened (trigger={trigger}, ev={ev_id})")

        db.commit()
        if settled:
            print(f"[settle_rep] Settled {settled} evidence, {rep_changes} rep changes")
    except Exception as e:
        db.rollback()
        print(f"[settle_rep] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.dispatch_jury_webhooks")
def dispatch_jury_webhooks():
    """Hourly: push open jury tasks to agents with endpoint_url registered."""
    import datetime as _dt
    import hashlib as _hashlib
    import hmac as _hmac
    from app.models.agent import Agent as _Agent
    from app.models.jury import JuryTask, JuryAssignment
    from app.models.claim import Claim, Evidence

    if not settings.OAC_ENABLED:
        return

    db = SessionLocal()
    try:
        # Get agents with healthy/unknown webhooks that are active
        webhook_agents = db.query(_Agent).filter(
            _Agent.endpoint_url.isnot(None),
            _Agent.status == "active",
            _Agent.endpoint_health != "error",
        ).all()

        if not webhook_agents:
            return

        # Get open tasks
        open_tasks = db.query(JuryTask).filter(
            JuryTask.status == "open"
        ).order_by(JuryTask.created_at).limit(settings.OAC_JURY_WEBHOOK_BATCH_SIZE).all()

        delivered = 0
        for agent in webhook_agents:
            cats = [c.strip() for c in (agent.topic_affinity or "").split(",") if c.strip()]
            for task in open_tasks:
                # Skip if already assigned
                if db.query(JuryAssignment).filter_by(task_id=task.id, agent_id=agent.id).first():
                    continue
                # Affinity filter
                if cats and task.category and task.category not in cats:
                    continue

                ev = db.query(Evidence).get(task.evidence_id)
                claim = db.query(Claim).get(task.claim_id)
                if not ev or not claim:
                    continue

                payload = {
                    "task_id": task.id,
                    "claim": claim.text,
                    "evidence": {
                        "title": ev.title,
                        "abstract": ev.abstract,
                        "year": ev.year,
                        "arxiv_id": ev.arxiv_id,
                        "url": ev.url,
                        "asserted_stance": ev.stance,
                    },
                    "vote_url": f"{settings.OPENCLAW_GATEWAY_URL or 'https://nebulamind.net'}/api/jury/tasks/{task.id}/vote",
                }

                sig = ""
                if agent.endpoint_secret_hash:
                    sig = _hmac.new(agent.endpoint_secret_hash.encode(),
                                    json.dumps(payload, sort_keys=True).encode(),
                                    _hashlib.sha256).hexdigest()

                try:
                    import httpx as _httpx
                    r = _httpx.post(
                        agent.endpoint_url,
                        json=payload,
                        headers={"X-NebulaMind-Signature": sig, "X-NebulaMind-Task-Id": str(task.id)},
                        timeout=settings.OAC_JURY_WEBHOOK_TIMEOUT_SECONDS,
                    )
                    agent.endpoint_health = "healthy" if r.status_code < 300 else f"http_{r.status_code}"
                except Exception as we:
                    agent.endpoint_health = "error"
                    print(f"[dispatch_webhooks] {agent.name} failed: {we}")

                agent.endpoint_last_check_at = _dt.datetime.utcnow()
                db.add(JuryAssignment(task_id=task.id, agent_id=agent.id, delivery_method="webhook"))
                delivered += 1

        db.commit()
        if delivered:
            print(f"[dispatch_webhooks] Delivered {delivered} tasks to webhook agents")
    except Exception as e:
        db.rollback()
        print(f"[dispatch_webhooks] Error: {e}")
    finally:
        db.close()


# ── Wiki Renovation Phase 2 Pipeline ────────────────────────────────────────

@celery_app.task(name="app.agent_loop.tasks.diagnose_page")
def diagnose_page(page_id: int):
    """Stage 1: Compute health score → create RenovationPlan."""
    import json as _json
    import datetime as _dt
    from app.models.page import WikiPage, RenovationPlan
    from app.services.page_health import compute_health_score

    db = SessionLocal()
    try:
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page or page.do_not_renovate:
            return
        # Check no active plan
        existing = db.query(RenovationPlan).filter(
            RenovationPlan.page_id == page_id,
            RenovationPlan.status.in_(["queued", "gathering", "synthesizing", "proposed"])
        ).first()
        if existing:
            return

        h = compute_health_score(page, db)
        page.health_score = h["score"]
        page.health_updated_at = _dt.datetime.utcnow()

        plan = RenovationPlan(
            page_id=page_id,
            health_score=h["score"],
            components=_json.dumps(h["components"]),
            weakest_dimensions=",".join(h.get("weakest_dimensions", [])),
            missing_subtopics=_json.dumps(h.get("missing_subtopics", [])),
            status="queued",
        )
        db.add(plan)
        db.flush()
        plan_id = plan.id
        db.commit()

        _notify(f"🔍 Renovation diagnosed: {page.slug} (score={h['score']:.1f} {h['emoji']} {h['band']})")
        # Kick off Stage 2
        gather_renovation_evidence.delay(plan_id)
    except Exception as e:
        db.rollback()
        print(f"[diagnose_page] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.gather_renovation_evidence",
                 bind=True, max_retries=2, default_retry_delay=300)
def gather_renovation_evidence(self, plan_id: int):
    """Stage 2: Gather arXiv evidence for missing subtopics."""
    import json as _json
    import datetime as _dt
    from app.models.page import WikiPage, RenovationPlan
    from app.services.subtopic_maps import get_required_subtopics
    from app.services.paper_search import search_papers

    db = SessionLocal()
    try:
        plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
        if not plan or plan.status not in ("queued",):
            return
        plan.status = "gathering"
        plan.started_at = _dt.datetime.utcnow()
        db.commit()

        page = db.query(WikiPage).filter(WikiPage.id == plan.page_id).first()
        missing = _json.loads(plan.missing_subtopics or "[]")
        subtopic_kw = get_required_subtopics(page.slug)

        papers = []
        seen_ids = set()

        # Freshness: fetch 2024+ papers on main topic
        try:
            fresh = search_papers(f"{page.title} 2024 2025", rows=5, prefer_recent=True)
            for p in fresh:
                if p.arxiv_id and p.arxiv_id not in seen_ids:
                    papers.append({"arxiv_id": p.arxiv_id, "title": p.title,
                                   "year": p.year, "abstract": (p.abstract or "")[:400],
                                   "source": "freshness"})
                    seen_ids.add(p.arxiv_id)
        except Exception:
            pass

        # Missing subtopics: fetch relevant papers
        for subtopic_id in missing[:4]:  # max 4 subtopics
            aliases = subtopic_kw.get(subtopic_id, [subtopic_id.replace("_", " ")])
            query = f"{page.title} {aliases[0]}"
            try:
                results = search_papers(query, rows=5, prefer_recent=True)
                for p in results:
                    if p.arxiv_id and p.arxiv_id not in seen_ids and len(papers) < 30:
                        papers.append({"arxiv_id": p.arxiv_id, "title": p.title,
                                       "year": p.year, "abstract": (p.abstract or "")[:400],
                                       "source": subtopic_id})
                        seen_ids.add(p.arxiv_id)
            except Exception:
                pass

        # Store gathered evidence in plan notes
        plan.notes = _json.dumps({"papers": papers})
        plan.status = "synthesizing" if papers else "queued"
        db.commit()

        if papers:
            synthesize_renovation.delay(plan_id)
            _notify(f"📚 Renovation gathered: {page.slug} — {len(papers)} papers")
        else:
            _notify(f"⚠️ Renovation: no papers found for {page.slug}")
    except Exception as e:
        db.rollback()
        plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
        if plan:
            plan.status = "queued"
            db.commit()
        raise self.retry(exc=e)
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.synthesize_renovation",
                 bind=True, max_retries=1, default_retry_delay=600)
def synthesize_renovation(self, plan_id: int):
    """Stage 3: Parallel multi-model synthesis → propose rewrite."""
    import json as _json
    import datetime as _dt
    import re as _re
    from app.models.page import WikiPage, RenovationPlan
    from app.services.subtopic_maps import get_required_subtopics

    db = SessionLocal()
    try:
        plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
        if not plan or plan.status != "synthesizing":
            return

        page = db.query(WikiPage).filter(WikiPage.id == plan.page_id).first()
        try:
            from app.agent_loop.autowiki.tasks import align_citations_page
            align_citations_page.delay(page.id)
        except Exception:
            pass
        notes = _json.loads(plan.notes or "{}")
        papers = notes.get("papers", [])
        missing = _json.loads(plan.missing_subtopics or "[]")
        subtopic_kw = get_required_subtopics(page.slug)

        if not papers:
            plan.status = "queued"
            db.commit()
            return

        # Format evidence for prompt
        evidence_text = "\n".join(
            f"- [{p.get('arxiv_id','?')}] {p.get('title','?')} ({p.get('year','n.d.')}): {p.get('abstract','')}"
            for p in papers[:20]
        )

        missing_with_kw = {sid: subtopic_kw.get(sid, [sid]) for sid in missing[:4]}
        missing_text = "\n".join(f"- {sid}: {', '.join(v[:3])}" for sid, v in missing_with_kw.items())

        # Find weakest section name
        section_to_rewrite = "Current Research"  # default
        components = _json.loads(plan.components) if isinstance(plan.components, str) else (plan.components or {})
        weakest = plan.weakest_dimensions.split(",") if plan.weakest_dimensions else []
        if "freshness" in weakest or "depth" in weakest:
            section_to_rewrite = "Current Research"

        # Extract current section
        content = page.content or ""
        section_match = _re.search(
            rf'(## {section_to_rewrite}.*?)(?=\n## |\Z)', content, _re.DOTALL
        )
        current_section = section_match.group(1)[:2000] if section_match else f"## {section_to_rewrite}\n(empty)"

        evidence_map = build_evidence_map(db, page.id, max_rows=80)

        SYNTH_SYSTEM = f"""You are renovating the NebulaMind wiki page "{page.title}".
Goal: rewrite the {section_to_rewrite} section to be genuinely representative.

CONSTRAINTS:
- Each new claim should be backed by a paper in the evidence map when possible.
- DO NOT write author-year parenthetical citations. Use only <!--cite:EVIDENCE_ID--> markers from the EVIDENCE MAP.
- If no evidence ID is available for an assertion, write it without a citation marker.
- Missing subtopics listed are suggestions — only include if applicable to {page.title}.
  For subtopics not relevant to this specific page, write "NOT_APPLICABLE".
- Preserve any existing accepted/consensus claims in the section.
- You MUST PRESERVE any existing HTML claim markers (e.g. <!--claim:123-->) from the current section.
- You MUST weave HTML claim markers inline immediately after asserting any of the provided key claims (e.g. <!--claim:xxx-->).
- Do NOT invent papers, evidence IDs, or unsourced claims.
- Output ONLY the rewritten section starting with ## {section_to_rewrite}
- 6-10 distinct claim sentences with dynamic citation markers where evidence IDs are available."""

        from app.models.claim import Claim as ClaimModel
        page_claims = db.query(ClaimModel).filter(ClaimModel.page_id == page.id).order_by(ClaimModel.created_at.desc()).limit(200).all()
        claims_text = "\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in page_claims)

        user_msg = f"""Available evidence (arXiv, last 3 years):
{evidence_text}

{evidence_map}

Key claims on this page:
{claims_text}

Missing subtopics to address (if applicable):
{missing_text}

Current section (preserve strong existing content):
{current_section}

Rewrite ## {section_to_rewrite} with these papers."""

        # Renovation synthesis — use routing table (Rakon leads)
        from app.services.llm_routing.routing import get_models
        parallel_models = get_models("renovation_synth")

        results = _chat_parallel(parallel_models, SYNTH_SYSTEM, user_msg, timeout=120)

        if not results or len(results) < 2:
            # Fallback: single model
            try:
                fallback = _chat(settings.ADVERSARIAL_QUERY_MODEL, SYNTH_SYSTEM, user_msg, role="renovator")
                results = [{"label": f"{settings.ADVERSARIAL_QUERY_MODEL}_fallback", "response": fallback}]
            except Exception:
                plan.status = "queued"
                db.commit()
                return

        # Synthesize: pick best/merged response
        if len(results) == 1:
            final_section = results[0]["response"]
        else:
            MERGE_SYSTEM = f"""You are merging {len(results)} draft rewrites of ## {section_to_rewrite} for the {page.title} wiki page.

Rules:
1. Include claims that ≥2 agents proposed (consensus)
2. Include uniquely strong cited claims from single agents
3. Prefer claims with <!--cite:N--> markers from the EVIDENCE MAP; do not invent IDs
4. Keep 6-10 total claim sentences
5. Output ONLY the merged section starting with ## {section_to_rewrite}"""

            drafts = "\n\n".join(
                f"=== Draft {i+1} ({r['label']}) ===\n{r['response']}"
                for i, r in enumerate(results)
            )
            merge_msg = f"Evidence pool:\n{evidence_text}\n\nDrafts to merge:\n{drafts}"

            try:
                final_section = _chat(settings.ADVERSARIAL_QUERY_MODEL, MERGE_SYSTEM, merge_msg, role="renovator")
            except Exception:
                final_section = results[0]["response"]  # best single result

        # Validate: must start with section header
        if not final_section.strip().startswith(f"## {section_to_rewrite}"):
            final_section = f"## {section_to_rewrite}\n\n{final_section.strip()}"

        # Store synthesized section
        notes["synthesized_section"] = final_section
        notes["section_name"] = section_to_rewrite
        plan.notes = _json.dumps(notes)
        db.commit()

        verify_renovation.delay(plan_id)
    except Exception as e:
        db.rollback()
        plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
        if plan:
            plan.status = "queued"
            db.commit()
        raise self.retry(exc=e)
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.verify_renovation",
                 bind=True, max_retries=1, default_retry_delay=120)
def verify_renovation(self, plan_id: int):
    """Stage 3.5: QA check synthesized section before committing as proposal."""
    import json as _json
    import datetime as _dt
    from app.models.page import WikiPage, RenovationPlan
    from app.services.llm_routing.routing import get_models, _gemini

    db = SessionLocal()
    try:
        plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
        if not plan or plan.status != "synthesizing":
            return

        page = db.query(WikiPage).filter(WikiPage.id == plan.page_id).first()
        notes = _json.loads(plan.notes or "{}")
        synthesized_section = notes.get("synthesized_section", "")
        section_name = notes.get("section_name", "Current Research")

        if not synthesized_section:
            plan.status = "queued"
            db.commit()
            return

        QA_SYSTEM = """You are a QA reviewer for an astronomy wiki. You verify renovated wiki sections.

Check the section and reply with exactly one line:
PASS if ALL of the following are true:
- Contains at least 2 inline citations, either dynamic <!--cite:N--> markers or legacy [arXiv:XXXX] markers during rollout
- Starts with the correct markdown section header (## ...)
- Makes specific scientific claims (not vague/generic statements)
- Content is relevant astronomy/astrophysics (not off-topic)

FAIL:<reason> if any check fails. Keep reason under 20 words."""

        QA_USER = f"""Wiki page: {page.title}
Section name: {section_name}

Section content:
{synthesized_section[:3000]}

Is this section PASS or FAIL?"""

        verdict = "PASS"
        try:
            gemini_cfg = _gemini()
            if gemini_cfg:
                result = _chat_parallel([gemini_cfg], QA_SYSTEM, QA_USER, timeout=45)
                if result:
                    verdict = result[0]["response"].strip().upper()
            else:
                # Fallback: structural check only
                has_header = synthesized_section.strip().startswith(f"## {section_name}")
                import re as _re
                citation_count = len(_re.findall(r"\[arXiv:|<!--cite:\d+(?:,\d+)*-->", synthesized_section, _re.IGNORECASE))
                verdict = "PASS" if (has_header and citation_count >= 2) else f"FAIL:structural check — header={has_header} citations={citation_count}"
        except Exception as qa_err:
            print(f"[verify_renovation] QA error (defaulting PASS): {qa_err}")
            verdict = "PASS"

        if verdict.startswith("PASS"):
            notes["verify_passed"] = True
            plan.notes = _json.dumps(notes)
            db.commit()
            commit_renovation_proposal.delay(plan_id)
            print(f"[verify_renovation] Plan #{plan_id} ({page.slug}): PASSED QA")
        else:
            reason = verdict.replace("FAIL:", "").strip() if "FAIL:" in verdict else verdict
            notes["verify_failed"] = reason
            plan.notes = _json.dumps(notes)
            plan.status = "queued"
            db.commit()
            _notify(f"❌ Renovation QA failed: {page.slug} — {reason[:80]}")
            print(f"[verify_renovation] Plan #{plan_id} ({page.slug}): FAILED — {reason}")
    except Exception as e:
        db.rollback()
        plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
        if plan:
            plan.status = "queued"
            db.commit()
        raise self.retry(exc=e)
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.commit_renovation_proposal")
def commit_renovation_proposal(plan_id: int):
    """Stage 4: Submit synthesized rewrite as EditProposal."""
    import json as _json
    import datetime as _dt
    import re as _re
    from app.models.page import WikiPage, RenovationPlan
    from app.models.edit import EditProposal, EditStatus
    from app.models.agent import Agent

    db = SessionLocal()
    try:
        plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
        if not plan:
            return
        page = db.query(WikiPage).filter(WikiPage.id == plan.page_id).first()
        notes = _json.loads(plan.notes or "{}")
        synthesized_section = notes.get("synthesized_section", "")
        section_name = notes.get("section_name", "Current Research")

        if not synthesized_section:
            plan.status = "queued"
            db.commit()
            return

        # Throttle gate
        arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()
        if not arxivbot:
            return
        allowed, reason = can_propose_edit(db, page.id, arxivbot.id)
        if not allowed:
            plan.status = "queued"
            plan.notes = str(_json.loads(plan.notes or "{}") | {"throttle_reason": reason})
            db.commit()
            _notify(f"⏸ Renovation throttled for {page.slug}: {reason}")
            return

        # Replace section in full content
        content = page.content or ""
        pattern = rf'(## {_re.escape(section_name)}.*?)(?=\n## |\Z)'
        if _re.search(pattern, content, _re.DOTALL):
            new_content = _re.sub(pattern, synthesized_section, content, flags=_re.DOTALL)
        else:
            # Section doesn't exist — append
            new_content = content.rstrip() + "\n\n" + synthesized_section

        from app.services.content_canonicalizer import canonicalize
        new_content = canonicalize(new_content, page_id=page.id, db=db).new_content

        proposal = EditProposal(
            page_id=page.id,
            agent_id=arxivbot.id,
            content=new_content,
            status=EditStatus.PENDING,
        )
        db.add(proposal)
        db.flush()

        plan.status = "proposed"
        plan.completed_at = _dt.datetime.utcnow()
        plan.edit_proposal_id = proposal.id
        page.last_renovated_at = _dt.datetime.utcnow()
        db.commit()

        _notify(f"✏️ Renovation proposed: {page.slug} (plan #{plan_id}, proposal #{proposal.id}, score={plan.health_score:.1f})")
    except Exception as e:
        db.rollback()
        print(f"[commit_renovation] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.queue_next_renovation")
def queue_next_renovation():
    """Daily: pick worst-scoring pages and kick off renovation."""
    from app.models.page import WikiPage, RenovationPlan
    from sqlalchemy import text as _text

    db = SessionLocal()
    try:
        candidates = db.execute(_text("""
            SELECT p.id, p.slug, COALESCE(p.health_score, 0) AS score
            FROM wiki_pages p
            WHERE p.do_not_renovate = false
              AND p.category IS NOT NULL
              AND NOT EXISTS (
                SELECT 1 FROM renovation_plans rp
                WHERE rp.page_id = p.id
                  AND rp.status IN ('queued','gathering','synthesizing','proposed')
              )
              AND (
                p.last_renovated_at IS NULL
                OR p.last_renovated_at < NOW() - (COALESCE(p.renovation_interval_days, 14) || ' days')::interval
              )
            ORDER BY score ASC NULLS FIRST
            LIMIT 2
        """)).fetchall()

        for row in candidates:
            diagnose_page.delay(row.id)
            _notify(f"🔧 Renovation queued: {row.slug} (score={row.score:.1f})")
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.rescue_stale_renovation_plans")
def rescue_stale_renovation_plans():
    """Daily: retry renovation plans stuck in queued/proposed with gathered papers but no edit proposal."""
    import json as _json
    import ast as _ast
    import datetime as _dt
    from app.models.page import WikiPage, RenovationPlan

    db = SessionLocal()
    rescued = 0
    try:
        # Find plans that have papers but are stuck (up to 3 per run to avoid overload)
        stuck = db.query(RenovationPlan).filter(
            RenovationPlan.status.in_(["queued", "proposed"]),
            RenovationPlan.edit_proposal_id.is_(None),
            RenovationPlan.notes.isnot(None),
        ).order_by(RenovationPlan.health_score.asc()).limit(3).all()

        for plan in stuck:
            try:
                notes_str = plan.notes or ""
                if not notes_str or "papers" not in notes_str:
                    continue

                # Parse notes — try JSON first, then Python dict literal (legacy format)
                notes = None
                if notes_str.startswith('{"') or notes_str == "{}":
                    try:
                        notes = _json.loads(notes_str)
                    except Exception:
                        pass
                if notes is None:
                    try:
                        notes = _ast.literal_eval(notes_str)
                        # Convert to canonical JSON format
                        plan.notes = _json.dumps(notes)
                        db.commit()
                        print(f"[rescue] Plan #{plan.id}: converted Python-dict notes to JSON")
                    except Exception as parse_err:
                        print(f"[rescue] Plan #{plan.id}: can't parse notes — {parse_err}")
                        continue

                papers = notes.get("papers", [])
                if not papers:
                    continue

                # Has synthesized_section but still not committed → go to verify
                if notes.get("synthesized_section"):
                    plan.status = "synthesizing"
                    db.commit()
                    verify_renovation.delay(plan.id)
                    rescued += 1
                    print(f"[rescue] Plan #{plan.id} (page={plan.page_id}): has synth → queued verify")
                else:
                    # Has papers but no synthesis → re-trigger synthesis
                    plan.status = "synthesizing"
                    db.commit()
                    synthesize_renovation.delay(plan.id)
                    rescued += 1
                    print(f"[rescue] Plan #{plan.id} (page={plan.page_id}): has papers → queued synthesize")

            except Exception as inner_e:
                print(f"[rescue] Plan #{plan.id}: error — {inner_e}")
                continue

        if rescued:
            _notify(f"🔄 Rescued {rescued} stale renovation plan(s)")
        else:
            print("[rescue] No stale renovation plans to rescue")
    except Exception as e:
        db.rollback()
        print(f"[rescue_stale_renovation_plans] Error: {e}")
    finally:
        db.close()


# ── End Wiki Renovation Phase 2 Pipeline ─────────────────────────────────────


@celery_app.task(name="app.agent_loop.tasks.normalize_did_you_know")
def normalize_did_you_know():
    """Tier-cascade for did_you_know — retired: DYK UI removed, column no longer in schema."""
    return {"skipped": "dyk_column_removed"}

    import json as _json
    import datetime as _dt
    from app.services.hero_facts import validate_dyk, try_claim_grounded_source
    from app.models.page import WikiPage as _WikiPage

    db = SessionLocal()
    try:
        pages = db.query(_WikiPage).filter(_WikiPage.hero_facts.isnot(None)).all()
        n_pages_changed = n_promoted_b = n_kept_c = n_dropped = 0

        for page in pages:
            try:
                items = _json.loads(page.did_you_know)
            except Exception:
                continue
            if not isinstance(items, list):
                continue

            new_items = []
            changed = False

            for item in items:
                if isinstance(item, str):
                    item = {"text": item, "source": None}
                elif not isinstance(item, dict):
                    continue

                text = item.get("text", "")
                src = item.get("source") or {}

                # Already sourced with authoritative — leave alone
                if src.get("tier") == "authoritative":
                    new_items.append(item)
                    continue
                # claim already matched — leave alone too
                if src.get("tier") == "claim":
                    new_items.append(item)
                    continue

                # 1. Validate (suppress vague language)
                ok, reason = validate_dyk(text)
                if not ok:
                    n_dropped += 1
                    changed = True
                    continue

                # 2. Try Tier B: claim grounding via TF-IDF
                pseudo_fact = {"label": text, "value": "", "unit": ""}
                b_source = try_claim_grounded_source(pseudo_fact, page.id, db)
                if b_source:
                    item = dict(item)
                    item["source"] = b_source
                    new_items.append(item)
                    n_promoted_b += 1
                    changed = True
                    continue

                # 3. Fallback: explicit Tier C
                item = dict(item)
                item["source"] = {
                    "tier": "ai_estimate",
                    "attribution": "AI estimate (no peer-reviewed source linked)",
                    "cited_at": _dt.datetime.utcnow().isoformat(),
                }
                new_items.append(item)
                n_kept_c += 1
                changed = True

            if changed:
                page.did_you_know = _json.dumps(new_items, ensure_ascii=False)
                n_pages_changed += 1

        db.commit()
        msg = (
            f"📊 DYK normalized: {n_pages_changed} pages changed, "
            f"+{n_promoted_b} → Tier B, {n_kept_c} kept Tier C, {n_dropped} suppressed"
        )
        print(msg)
        _notify(msg)
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.sweep_human_overrides")
def sweep_human_overrides():
    """Daily: expire 30-day-old overrides + notify when 3+ new evidence rows landed."""
    import datetime as _dt
    from app.models.claim import Claim, Evidence, TrustAuditLog
    from sqlalchemy import func as sqlfunc

    db = SessionLocal()
    try:
        now = _dt.datetime.utcnow()
        cutoff = now - _dt.timedelta(days=30)

        overridden = db.query(Claim).filter(
            Claim.human_trust_override.isnot(None),
            Claim.human_override_at.isnot(None),
        ).all()

        expired = 0
        reminded = 0
        for claim in overridden:
            # 1. Expire old overrides
            if claim.human_override_at < cutoff:
                old_override = claim.human_trust_override
                claim.human_trust_override = None
                claim.human_override_locked = False
                claim.human_override_at = None
                claim.human_override_reason = None
                # Recompute trust now
                from app.routers.claims import recalculate_trust_v2
                new_level, ts = recalculate_trust_v2(claim.id, db, trigger="override_expired")
                expired += 1
                print(f"[override_sweep] Claim #{claim.id}: {old_override} override expired → {new_level}")
                _notify(f"⏳ Override expired on claim #{claim.id}: {old_override} → {new_level}")
                continue

            # 2. Notify if 3+ new evidence rows since override
            new_ev = db.query(sqlfunc.count(Evidence.id)).filter(
                Evidence.claim_id == claim.id,
                Evidence.created_at > claim.human_override_at,
            ).scalar() or 0

            if new_ev >= 3:
                reminded += 1
                print(f"[override_sweep] Claim #{claim.id}: {new_ev} new evidence rows since override")
                _notify(
                    f"📌 Override reminder: claim #{claim.id} has {new_ev} new evidence rows "
                    f"since the {claim.human_trust_override!r} override was set. "
                    f"Consider reviewing at /wiki/{db.query(__import__('app.models.page', fromlist=['WikiPage']).WikiPage if True else None).filter_by(id=claim.page_id).first().slug if True else claim.page_id}"
                )

        db.commit()
        if expired or reminded:
            print(f"[override_sweep] {expired} expired, {reminded} reminders sent")
    except Exception as e:
        db.rollback()
        print(f"[override_sweep] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.sweep_stale_escalations")
def sweep_stale_escalations():
    """Daily: expire escalations past their deadline."""
    import datetime as _dt
    from app.models.council import Escalation

    db = SessionLocal()
    try:
        now = _dt.datetime.utcnow()
        stale = db.query(Escalation).filter(
            Escalation.status.in_(["open", "in_review"]),
            Escalation.expires_at < now,
        ).all()

        expired = 0
        for esc in stale:
            esc.status = "resolved"
            esc.resolution = "expired"
            esc.resolved_at = now
            esc.notes = (esc.notes or "") + f"\nExpired after insufficient quorum ({esc.votes_received}/{esc.votes_target} votes)."
            expired += 1

        db.commit()
        if expired:
            print(f"[sweep_escalations] Expired {expired} stale escalations")
            _notify(f"⏳ {expired} escalation(s) expired (insufficient quorum)")
    except Exception as e:
        db.rollback()
        print(f"[sweep_escalations] Error: {e}")
        raise
    finally:
        db.close()




@celery_app.task(name="app.agent_loop.tasks.sweep_council_tiers")
def sweep_council_tiers():
    """Hourly: escalate contested Stage 2 decisions to Stage 3; safety-net E1/E2 jury patterns."""
    import datetime as _dt
    from app.models.council import Escalation, EscalationVote
    from app.models.claim import EvidenceVote
    from app.services.council import open_escalation, evaluate_escalation_triggers
    from app.config import settings

    db = SessionLocal()
    try:
        now = _dt.datetime.utcnow()
        promoted = 0
        auto_opened = 0

        # 1. Promote contested Stage 2 "overturned" to Stage 3 (S1 trigger)
        window = now - _dt.timedelta(hours=48)
        stage2_overturned = db.query(Escalation).filter(
            Escalation.current_stage == 2,
            Escalation.status == "resolved",
            Escalation.resolution == "overturned",
            Escalation.resolved_at >= window,
        ).all()

        for esc in stage2_overturned:
            # Check if Stage 3 already exists for this source
            existing_s3 = db.query(Escalation).filter(
                Escalation.source_kind == esc.source_kind,
                Escalation.source_id == esc.source_id,
                Escalation.current_stage == 3,
                Escalation.status.in_(["open", "resolved"]),
            ).first()
            if existing_s3:
                continue

            # Compute vote margin
            votes = db.query(EscalationVote).filter(
                EscalationVote.escalation_id == esc.id,
                EscalationVote.voter_tier == 2,
            ).all()
            w_overturn = sum(v.weight for v in votes if v.action in ("overturn", "revoke"))
            w_uphold = sum(v.weight for v in votes if v.action in ("uphold", "ratify"))
            total = w_overturn + w_uphold
            margin = abs(w_overturn - w_uphold) / total if total > 0 else 1.0

            # Only auto-escalate if margin < 30% (contested)
            if margin < 0.30:
                s3 = open_escalation(
                    db,
                    esc.source_kind,
                    esc.source_id,
                    "S1",
                    trigger_detail=f"Contested Stage 2 overturn (margin={margin:.1%}, esc #{esc.id})",
                    stage=3,
                )
                promoted += 1
                print(f"[sweep_council_tiers] Promoted esc #{esc.id} → Stage 3 (#{s3.id})")

        # 2. Safety-net: find evidence rows settled in the last 2h with no escalation.
        # Current schema records settlement on Evidence.consensus_settled_at;
        # votes are attached rows without their own settlement flag.
        ev_window = now - _dt.timedelta(hours=2)
        try:
            from app.models.claim import Evidence, EvidenceVote
            recent_ev_ids = (
                db.query(Evidence.id)
                .filter(Evidence.consensus_settled_at >= ev_window)
                .all()
            )
            for (ev_id,) in recent_ev_ids:
                # Skip if escalation already exists
                existing = db.query(Escalation).filter(
                    Escalation.source_kind == "evidence_vote",
                    Escalation.source_id == ev_id,
                    Escalation.status == "open",
                ).first()
                if existing:
                    continue

                votes = db.query(EvidenceVote).filter(
                    EvidenceVote.evidence_id == ev_id
                ).all()
                trigger = evaluate_escalation_triggers(db, ev_id, votes)
                if trigger:
                    open_escalation(db, "evidence_vote", ev_id, trigger)
                    auto_opened += 1
                    print(f"[sweep_council_tiers] Auto-escalated evidence #{ev_id} ({trigger})")
        except Exception as e_inner:
            print(f"[sweep_council_tiers] Safety-net scan skipped: {e_inner}")

        db.commit()
        if promoted or auto_opened:
            _notify(
                f"🏛️ Council sweep: {promoted} Stage 2→3 promotion(s), "
                f"{auto_opened} auto-escalation(s)"
            )
        else:
            print("[sweep_council_tiers] Nothing to escalate")
    except Exception as e:
        db.rollback()
        print(f"[sweep_council_tiers] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.update_agent_behavior_scores")
def update_agent_behavior_scores():
    """Daily: compute behavior scores for all active agents. Write-only, no enforcement."""
    from app.services.agent_behavior import upsert_behavior_score
    from app.models.agent import Agent
    db = SessionLocal()
    try:
        agents = db.query(Agent).filter(Agent.status == "active").all()
        flagged = []
        for agent in agents:
            result = upsert_behavior_score(agent.id, db)
            if result["flags"]:
                flagged.append((agent.name, result["flags"], result["score"]))
        db.commit()
        if flagged:
            msg = "🚨 Agent behavior flags:\n" + "\n".join(
                f"  • {name}: {', '.join(flags)} (score={score:.3f})"
                for name, flags, score in flagged
            )
            _notify(msg)
        print(f"[behavior] Scored {len(agents)} agents, {len(flagged)} flagged")
    except Exception as e:
        db.rollback()
        print(f"[behavior] Error: {e}")
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.check_api_key_expiry")
def check_api_key_expiry():
    """Daily: alert agents whose API key expires within 30 days."""
    import datetime as _dt
    from sqlalchemy import text as _text
    db = SessionLocal()
    try:
        soon = _dt.datetime.utcnow() + _dt.timedelta(days=30)
        expiring = db.execute(_text("""
            SELECT id, name, api_key_expires_at FROM agents
            WHERE api_key_expires_at BETWEEN now() AND :soon
              AND status = 'active'
        """), {"soon": soon}).fetchall()
        if expiring:
            lines = "\n".join(f"  • {r.name} (expires {r.api_key_expires_at.date()})" for r in expiring)
            _notify(f"🔑 API keys expiring soon:\n{lines}")
        print(f"[key_expiry] {len(expiring)} keys expiring within 30 days")
    except Exception as e:
        print(f"[key_expiry] Error: {e}")
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.gdpr_subscriber_purge")
def gdpr_subscriber_purge():
    """Weekly: anonymize subscriber PII 90 days after unsubscribe."""
    import datetime as _dt
    from sqlalchemy import text as _text
    db = SessionLocal()
    try:
        cutoff = _dt.datetime.utcnow() - _dt.timedelta(days=90)
        result = db.execute(_text("""
            UPDATE subscribers
            SET email = concat('anon_', id, '@deleted.invalid'),
                anonymized_at = now()
            WHERE unsubscribed_at < :cutoff
              AND anonymized_at IS NULL
              AND is_active = false
        """), {"cutoff": cutoff})
        db.commit()
        print(f"[gdpr] Anonymized {result.rowcount} subscriber(s)")
    except Exception as e:
        db.rollback()
        print(f"[gdpr] Error: {e}")
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.source_facts_for_page")
def source_facts_for_page(page_id: int):
    """One-pass fact sourcing for all hero_facts and did_you_know on one page."""
    import json as _json
    import datetime as _dt
    from app.models.page import WikiPage, FactSource
    from app.models.claim import Claim
    from app.services.hero_facts import (
        validate_hero_fact, validate_dyk,
        try_authoritative_source, try_claim_grounded_source, stamp_ai_estimate,
    )

    db = SessionLocal()
    try:
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page:
            return

        # — Hero facts —
        hero = []
        try:
            hero = _json.loads(page.hero_facts) if page.hero_facts else []
        except Exception:
            pass

        new_hero = []
        for idx, fact in enumerate(hero):
            if not isinstance(fact, dict):
                continue
            ok, reason = validate_hero_fact(fact)
            if not ok:
                # Suppressed — log but don't render
                db.add(FactSource(
                    page_id=page_id, fact_kind="hero", fact_index=idx,
                    source_tier="ai_estimate", flagged=True, reason=reason,
                    attribution=f"Suppressed: {reason}",
                ))
                continue
            source = (
                try_authoritative_source(fact)
                or try_claim_grounded_source(fact, page_id, db)
                or stamp_ai_estimate(fact.get("label", ""), "No source found")
            )
            fact = dict(fact)
            fact["source"] = source
            new_hero.append(fact)
            db.add(FactSource(
                page_id=page_id, fact_kind="hero", fact_index=idx,
                source_tier=source.get("tier", "ai_estimate"),
                authority=source.get("authority"),
                reference_url=source.get("reference_url"),
                reference_title=source.get("reference_title"),
                retrieval_year=source.get("retrieval_year"),
                claim_id=source.get("claim_id"),
                trust_level_snapshot=source.get("trust_level"),
                evidence_count_snapshot=source.get("evidence_count"),
                representative_arxiv_id=source.get("representative_arxiv_id"),
                generator=source.get("generator"),
                flagged=source.get("flagged", False),
                reason=source.get("reason"),
                attribution=source.get("attribution", ""),
                cited_at=_dt.datetime.utcnow(),
            ))

        if new_hero:
            page.hero_facts = _json.dumps(new_hero, ensure_ascii=False)

        db.commit()
        print(f"[source_facts] page #{page_id}: {len(new_hero)} hero sourced (dyk retired)")
        _notify(f"📐 Fact sourcing: page #{page_id} done ({len(new_hero)} hero)")
    except Exception as e:
        db.rollback()
        print(f"[source_facts] error page #{page_id}: {e}")
        raise
    finally:
        db.close()


# ============================================================
# Fact Sourcing v1 — LLM-assisted hero fact and DYK upgrading
# ============================================================

_FACT_DRAFT_SYSTEM = """You are a precision astronomy fact extractor for NebulaMind wiki.
Given a page topic and content excerpt, return 3–5 hero facts with SPECIFIC numeric values.

Return ONLY a JSON array — no explanation, no markdown fences:
[
  {"label": "...", "value": "...", "unit": "...", "kind": "scalar"},
  ...
]

Rules:
- Values MUST be specific numbers (e.g. 1.4, 1e51, 2.7255, 30000-52000).
- FORBIDDEN in value: millions, billions, trillions, thousands, hundreds, many, few, several.
- kind = "scalar" for single values; kind = "range" with value_min / value_max for ranges.
- Labels ≤ 4 words. Units are real physical units or empty string.
- Prefer values backed by Planck 2018, NIST CODATA, IAU, NASA, or peer-reviewed papers.
- NO discovery years unless the page is specifically about that event.
- NO person names as values."""

_DYK_DRAFT_SYSTEM = """You are an astronomy writer for NebulaMind wiki's "Did You Know?" section.
Given a page topic and content excerpt, write 3 concise surprising facts.

Return ONLY a JSON array of strings — no objects, no markdown, no explanation:
["fact one", "fact two", "fact three"]

Rules:
- Each fact: 1 sentence, 40–120 characters.
- MUST contain a specific number. FORBIDDEN: millions, billions, trillions, thousands, hundreds, many, few.
- Surprising or counter-intuitive. Start each with a different word."""

_FACT_DRAFT_MODELS = [
    {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.OLLAMA_STUDIO_HEAVY_MODEL, "label": settings.OLLAMA_STUDIO_HEAVY_MODEL},
    {"base_url": settings.OLLAMA_STUDIO_BASE_URL, "api_key": "ollama", "model": settings.OLLAMA_STUDIO_FAST_MODEL, "label": settings.OLLAMA_STUDIO_FAST_MODEL},
    {"base_url": "http://localhost:11434/v1", "api_key": "ollama", "model": "llama3.3:70b", "label": "llama3.3:70b"},
]


def _call_local_llm_for_facts(system: str, user: str, timeout: int = 300) -> str:
    """Call local Ollama models in priority order until one succeeds."""
    import json as _j
    import urllib.request as _req

    for m in _FACT_DRAFT_MODELS:
        try:
            model = guard_batch_model(m["model"], "tasks.fact_draft")
            est_tokens = max(1, (len(system) + len(user)) // 4)
            payload = _j.dumps({
                "model": model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user",   "content": user},
                ],
                "stream": False,
                "options": {"num_predict": 1024, "num_ctx": 4096},
            }).encode()
            dispatch_premium("tasks.fact_draft", model, est_tokens)
            req = _req.Request(
                f"{m['base_url']}/chat/completions",
                data=payload,
                headers={"Content-Type": "application/json"},
            )
            with _req.urlopen(req, timeout=timeout) as r:
                resp = _j.loads(r.read())
            usage = resp.get("usage") or {}
            log_llm_spend(
                "tasks.fact_draft",
                model,
                prompt_tokens=usage.get("prompt_tokens"),
                completion_tokens=usage.get("completion_tokens"),
                estimated_tokens=est_tokens,
            )
            content = resp["choices"][0]["message"]["content"]
            content = strip_think_blocks(content)
            print(f"[fact_draft] served by {m['label']}")
            return content
        except Exception as e:
            print(f"[fact_draft] {m['label']} failed: {e}")
    raise RuntimeError("All local LLM models failed for fact drafting")


def _parse_fact_json(raw: str) -> list:
    """Extract first JSON array from raw LLM output."""
    import json as _j
    import re as _re

    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    m = _re.search(r"\[.*\]", cleaned, _re.DOTALL)
    if m:
        return _j.loads(m.group())
    return _j.loads(cleaned)


@celery_app.task(name="app.agent_loop.tasks.draft_hero_facts_for_page", bind=True, max_retries=2)
def draft_hero_facts_for_page(self, page_id: int):
    """Use local LLM to draft improved hero facts for Tier-C / unsourced slots.

    Keeps existing Tier-A and Tier-B facts untouched. Uses local Ollama to
    generate replacements for Tier-C facts, validates them, applies 3-tier
    sourcing, and writes back to the page.
    """
    import json as _json
    import datetime as _dt
    from app.models.page import WikiPage, FactSource
    from app.services.hero_facts import (
        validate_hero_fact, _should_suppress_tier_c,
        try_authoritative_source, try_claim_grounded_source, stamp_ai_estimate,
    )

    db = SessionLocal()
    try:
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page:
            return f"page {page_id} not found"

        current = []
        try:
            current = _json.loads(page.hero_facts) if page.hero_facts else []
        except Exception:
            pass

        keep_facts = []
        needs_draft = []
        for f in current:
            if not isinstance(f, dict):
                continue
            tier = f.get("source", {}).get("tier", "")
            if tier in ("authoritative", "claim"):
                keep_facts.append(f)
            else:
                needs_draft.append(f)

        if not needs_draft and len(current) >= 3:
            return f"page {page_id}: all {len(current)} facts already A/B-tier, skip"

        content_excerpt = (page.content or "")[:1500]
        user_msg = (
            f"Page topic: {page.title or page.slug}\n\n"
            f"Content excerpt:\n{content_excerpt}\n\n"
            f"Weak/missing facts to replace (generate specific numeric alternatives):\n"
            + _json.dumps(needs_draft or [{"note": "generate fresh facts"}], ensure_ascii=False)
        )

        try:
            raw = _call_local_llm_for_facts(_FACT_DRAFT_SYSTEM, user_msg)
            candidates = _parse_fact_json(raw)
        except Exception as e:
            print(f"[draft_hero] page {page_id} LLM failed: {e}")
            return f"page {page_id}: LLM failed — {e}"

        new_facts = list(keep_facts)
        n_added = 0
        for fact in candidates[:5]:
            if not isinstance(fact, dict):
                continue
            if "kind" not in fact:
                fact["kind"] = "scalar"
            ok, reason = validate_hero_fact(fact)
            if not ok:
                print(f"[draft_hero] page {page_id} rejected: {reason}")
                continue
            if _should_suppress_tier_c(fact):
                continue
            source = (
                try_authoritative_source(fact)
                or try_claim_grounded_source(fact, page_id, db)
                or stamp_ai_estimate(fact.get("label", ""), "LLM draft — no authoritative source found")
            )
            fact["source"] = source
            new_facts.append(fact)
            n_added += 1
            db.add(FactSource(
                page_id=page_id,
                fact_kind="hero",
                fact_index=len(new_facts) - 1,
                source_tier=source.get("tier", "ai_estimate"),
                authority=source.get("authority"),
                reference_url=source.get("reference_url"),
                reference_title=source.get("reference_title"),
                retrieval_year=source.get("retrieval_year"),
                claim_id=source.get("claim_id"),
                trust_level_snapshot=source.get("trust_level"),
                evidence_count_snapshot=source.get("evidence_count"),
                representative_arxiv_id=source.get("representative_arxiv_id"),
                generator="fact_sourcing_v1",
                flagged=source.get("flagged", False),
                reason=source.get("reason"),
                attribution=source.get("attribution", ""),
                cited_at=_dt.datetime.utcnow(),
            ))

        if new_facts:
            page.hero_facts = _json.dumps(new_facts, ensure_ascii=False)

        db.commit()
        msg = (
            f"page {page_id} ({page.slug}): "
            f"kept {len(keep_facts)} A/B, added {n_added} new "
            f"(A={sum(1 for f in new_facts if f.get('source',{}).get('tier')=='authoritative')} "
            f"B={sum(1 for f in new_facts if f.get('source',{}).get('tier')=='claim')} "
            f"C={sum(1 for f in new_facts if f.get('source',{}).get('tier')=='ai_estimate')})"
        )
        print(f"[draft_hero] {msg}")
        return msg
    except Exception as e:
        db.rollback()
        print(f"[draft_hero] page {page_id} error: {e}")
        raise self.retry(exc=e, countdown=60)
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.draft_dyk_for_page", bind=True, max_retries=2)
def draft_dyk_for_page(self, page_id: int):
    """DYK drafting — retired: DYK UI removed, column no longer in schema."""
    return {"skipped": "dyk_column_removed"}

    import json as _json
    import datetime as _dt
    from app.models.page import WikiPage, FactSource
    from app.services.hero_facts import (
        validate_dyk, try_claim_grounded_source, stamp_ai_estimate,
    )

    db = SessionLocal()
    try:
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page:
            return f"page {page_id} not found"

        current = []
        try:
            for item in _json.loads(page.did_you_know or "[]"):
                if isinstance(item, str):
                    current.append({"text": item})
                elif isinstance(item, dict):
                    current.append(item)
        except Exception:
            pass

        keep_items = []
        needs_draft = []
        for item in current:
            tier = item.get("source", {}).get("tier", "")
            if tier == "claim":
                keep_items.append(item)
            else:
                needs_draft.append(item)

        if not needs_draft and len(current) >= 3:
            return f"page {page_id}: all {len(current)} DYK already B-tier, skip"

        content_excerpt = (page.content or "")[:1200]
        user_msg = (
            f"Page topic: {page.title or page.slug}\n\n"
            f"Content excerpt:\n{content_excerpt}\n\n"
            f"Generate 3 surprising Did You Know facts about this topic."
        )

        try:
            raw = _call_local_llm_for_facts(_DYK_DRAFT_SYSTEM, user_msg)
            candidates = _parse_fact_json(raw)
        except Exception as e:
            print(f"[draft_dyk] page {page_id} LLM failed: {e}")
            return f"page {page_id}: LLM failed — {e}"

        new_items = list(keep_items)
        n_added = 0
        for text in candidates[:5]:
            if not isinstance(text, str):
                if isinstance(text, dict):
                    text = text.get("text", text.get("fact", ""))
                if not isinstance(text, str):
                    continue
            ok, reason = validate_dyk(text)
            if not ok:
                print(f"[draft_dyk] page {page_id} rejected: {reason}")
                continue
            source = (
                try_claim_grounded_source(
                    {"label": text, "value": "", "unit": ""}, page_id, db
                )
                or stamp_ai_estimate(text[:50], "LLM draft — no matching claim")
            )
            new_items.append({"text": text, "source": source})
            n_added += 1
            db.add(FactSource(
                page_id=page_id,
                fact_kind="did_you_know",
                fact_index=len(new_items) - 1,
                source_tier=source.get("tier", "ai_estimate"),
                claim_id=source.get("claim_id"),
                trust_level_snapshot=source.get("trust_level"),
                evidence_count_snapshot=source.get("evidence_count"),
                representative_arxiv_id=source.get("representative_arxiv_id"),
                generator="fact_sourcing_v1",
                flagged=source.get("flagged", False),
                reason=source.get("reason"),
                attribution=source.get("attribution", ""),
                cited_at=_dt.datetime.utcnow(),
            ))

        if new_items:
            page.did_you_know = _json.dumps(new_items, ensure_ascii=False)

        db.commit()
        msg = (
            f"page {page_id} ({page.slug}): "
            f"kept {len(keep_items)} B-tier DYK, added {n_added} new"
        )
        print(f"[draft_dyk] {msg}")
        return msg
    except Exception as e:
        db.rollback()
        print(f"[draft_dyk] page {page_id} error: {e}")
        raise self.retry(exc=e, countdown=60)
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.run_fact_sourcing_v1")
def run_fact_sourcing_v1():
    """Batch coordinator: dispatch per-page LLM fact drafting for all pages
    with Tier-C or unsourced hero_facts / did_you_know items.

    Hero facts: keeps A/B-tier, uses local LLM to replace C-tier.
    DYK: keeps claim-grounded items, uses local LLM to replace C-tier.
    """
    import json as _json
    from app.models.page import WikiPage

    db = SessionLocal()
    try:
        pages = db.query(WikiPage).filter(WikiPage.hero_facts.isnot(None)).all()

        hero_queue = []
        dyk_queue = []

        for page in pages:
            # Hero: any non-A/B fact → queue
            try:
                facts = _json.loads(page.hero_facts or "[]")
                if any(
                    isinstance(f, dict)
                    and f.get("source", {}).get("tier", "") not in ("authoritative", "claim")
                    for f in facts
                ):
                    hero_queue.append(page.id)
            except Exception:
                hero_queue.append(page.id)

        print(f"[fact_sourcing_v1] queuing {len(hero_queue)} hero pages (dyk retired)")

        for page_id in hero_queue:
            draft_hero_facts_for_page.delay(page_id)

        msg = f"Fact Sourcing v1: queued {len(hero_queue)} hero pages"
        _notify(f"🧪 {msg}")
        return msg
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.run_temporal_decay")
def run_temporal_decay():
    """Daily: apply temporal decay to claims with stale evidence.
    
    Claims whose most recent supporting evidence is older than FRESHNESS_FLOOR_YEARS
    get a small trust_score penalty. This prevents confident-looking claims from
    staying 'accepted' indefinitely when supporting literature hasn't been updated.
    Scheduled: UTC 05:00 = KST 14:00.
    """
    import datetime as _dt
    from app.models.claim import Claim, Evidence
    from app.models.jury import ReputationLog
    from sqlalchemy import func as sqlfunc

    db = SessionLocal()
    try:
        now = _dt.datetime.utcnow()
        cutoff_year = now.year - settings.FRESHNESS_FLOOR_YEARS
        decay_per_year = 0.02  # lose 0.02 per year beyond the floor
        max_daily_decay = 0.005  # never decay more than 0.005/day

        # Claims with evidence where the newest supporting paper is older than floor
        stale_claims = (
            db.query(Claim)
            .filter(Claim.trust_level.in_(["accepted", "consensus"]))
            .filter(Claim.trust_score.isnot(None))
            .filter(
                # Has evidence, but newest supporting evidence is old
                db.query(sqlfunc.max(Evidence.year))
                .filter(Evidence.claim_id == Claim.id)
                .filter(Evidence.stance == "supports")
                .correlate(Claim)
                .as_scalar() < cutoff_year
            )
            .limit(200)
            .all()
        )

        decayed = 0
        demoted = 0
        for claim in stale_claims:
            # Find most recent evidence year
            max_year = (
                db.query(sqlfunc.max(Evidence.year))
                .filter(Evidence.claim_id == claim.id, Evidence.stance == "supports")
                .scalar() or 1990
            )
            years_stale = max(0, cutoff_year - max_year)
            decay = min(max_daily_decay, decay_per_year * years_stale / 365.0)
            if decay <= 0:
                continue

            old_score = claim.trust_score or 0.0
            new_score = max(-1.0, old_score - decay)
            claim.trust_score = new_score
            claim.trust_score_updated_at = now

            # Check if trust level should drop
            old_level = claim.trust_level
            if new_score < settings.TRUST_ACCEPTED_MIN and old_level == "consensus":
                claim.trust_level = "accepted"
                demoted += 1
                print(f"[temporal_decay] Claim #{claim.id}: consensus→accepted (stale {years_stale}y)")
            elif new_score < settings.TRUST_ACCEPTED_MIN * 0.7 and old_level == "accepted":
                claim.trust_level = "unverified"
                demoted += 1
                print(f"[temporal_decay] Claim #{claim.id}: accepted→unverified (stale {years_stale}y)")

            decayed += 1

        db.commit()
        if decayed > 0:
            msg = f"⏳ Temporal decay: {decayed} stale claims decayed, {demoted} demoted"
            print(f"[temporal_decay] {msg}")
            _notify(msg)
        else:
            print("[temporal_decay] No stale claims found")
    except Exception as e:
        db.rollback()
        print(f"[temporal_decay] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.run_adversarial_pass")
def run_adversarial_pass():
    """Daily: probe accepted claims for contradicting papers."""
    import datetime as _dt
    from app.models.claim import Claim, Evidence
    from app.services.paper_search import search_papers, verify_for_claim

    if not settings.ADVERSARIAL_PASS_ENABLED:
        return

    db = SessionLocal()
    try:
        candidates = _adversarial_candidates(db)
        if not candidates:
            print("[adversarial] no candidates")
            return

        adv_bot = _get_or_create_agent(db, "AdversaryBot",
                                        role="external_source",
                                        model_name=settings.ADVERSARIAL_QUERY_MODEL,
                                        specialty="curation")

        challenges_added = 0
        for claim in candidates:
            try:
                raw = _chat(settings.ADVERSARIAL_QUERY_MODEL,
                            ADVERSARIAL_QUERY_SYSTEM,
                            f'Claim: "{claim.text}"\n\nGenerate ONE adversarial ADS query.',
                            role="adversarial")
                parsed = _parse_jury_json(raw)
                query = (parsed or {}).get("query", "").strip() if parsed else ""
                if not (5 < len(query) < 250):
                    claim.last_adversarial_probe_at = _dt.datetime.utcnow()
                    continue
            except Exception as e:
                print(f"[adversarial] query gen failed claim #{claim.id}: {e}")
                claim.last_adversarial_probe_at = _dt.datetime.utcnow()
                continue

            try:
                records = search_papers(query, rows=5, prefer_recent=True)
            except Exception as e:
                print(f"[adversarial] search failed claim #{claim.id}: {e}")
                claim.last_adversarial_probe_at = _dt.datetime.utcnow()
                continue

            inserted = 0
            for rec in records[:settings.ADVERSARIAL_MAX_INSERTS_PER_CLAIM]:
                if not rec.arxiv_id:
                    continue
                if db.query(Evidence).filter_by(claim_id=claim.id, arxiv_id=rec.arxiv_id).first():
                    continue
                try:
                    verified = verify_for_claim(rec, claim.text)
                except Exception:
                    continue
                if not verified or verified.quality < settings.EVIDENCE_MIN_QUALITY_FOR_ACCEPTED:
                    continue
                if not _abstract_looks_adversarial(rec.abstract or ""):
                    continue

                ev = Evidence(
                    claim_id=claim.id,
                    arxiv_id=rec.arxiv_id, doi=rec.doi,
                    title=rec.title, year=rec.year, abstract=rec.abstract,
                    ads_bibcode=rec.bibcode,
                    url=f"https://arxiv.org/abs/{rec.arxiv_id}" if rec.arxiv_id else None,
                    stance="challenges",
                    quality=verified.quality,
                    added_by_agent_id=adv_bot.id,
                    verified_at=_dt.datetime.utcnow(),
                    source_channel="adversarial_pass",
                )
                db.add(ev)
                db.flush()
                _maybe_create_jury_task(db, ev.id, claim.id, claim.page_id)
                challenges_added += 1
                inserted += 1
                _enqueue_stance_jury_task(run_stance_jury_for_evidence, ev.id, countdown=10)

            claim.last_adversarial_probe_at = _dt.datetime.utcnow()
            import time as _time; _time.sleep(1)

        db.commit()
        print(f"[adversarial] +{challenges_added} challenges on {len(candidates)} claims")
        if challenges_added:
            _notify(f"🔥 Adversarial pass: +{challenges_added} challenge candidate(s) on {len(candidates)} claims")
    except Exception as e:
        db.rollback()
        print(f"[adversarial] error: {e}")
        raise
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Trust Phase 2: Fast single-model jury drain
# ---------------------------------------------------------------------------

@celery_app.task(name="app.agent_loop.tasks.run_stance_jury_single",
                 bind=True, max_retries=3, default_retry_delay=300)
def run_stance_jury_single(self, evidence_id: int, model: str | None = None):
    """Fast single-model jury for bulk processing."""
    import datetime as _dt
    import urllib.request as _urlreq
    from app.models.claim import Claim, Evidence, EvidenceVote
    # batch guard — prevents accidentally routing expensive preview/pro models into high-volume loops.
    # drain_jury_fast_pass enqueues this task per evidence row; a premium model override would
    # multiply cost across the entire jury backlog.
    from app.utils.model_guard import guard_batch_model

    model = model or settings.STANCE_JURY_FAST_MODEL
    model = guard_batch_model(model, "tasks.run_stance_jury_single")
    db = SessionLocal()
    try:
        ev = db.query(Evidence).filter(Evidence.id == evidence_id).first()
        if not ev or ev.stance_jury_run_at is not None:
            _release_stance_jury_inflight(evidence_id)
            return
        if _stance_jury_is_held(ev=ev, evidence_id=evidence_id):
            print(f"[jury_single] held skip for evidence #{evidence_id}")
            _release_stance_jury_inflight(evidence_id)
            return
        abstract_text = ev.abstract or ""
        intro_excerpt = ev.intro_excerpt or ""
        if len(abstract_text) < 100 and len(intro_excerpt) < settings.INTRO_EXCERPT_MIN_CHARS:
            ev.stance_jury_run_at = _dt.datetime.utcnow()
            db.commit()
            _release_stance_jury_inflight(evidence_id)
            return

        claim = db.query(Claim).filter(Claim.id == ev.claim_id).first()
        if not claim:
            _release_stance_jury_inflight(evidence_id)
            return
        if _stance_jury_is_held(ev=ev, claim=claim):
            print(f"[jury_single] held skip for evidence #{evidence_id} claim #{claim.id}")
            _release_stance_jury_inflight(evidence_id)
            return

        user_msg = (
            f'Claim: "{claim.text[:300]}"\n\n'
            f'Paper: "{ev.title[:150]}" ({ev.year or "n.d."})\n'
            f'Abstract: {abstract_text[:600]}\n'
            f'Introduction excerpt: {intro_excerpt[:800]}\n'
            f'Asserted stance: {ev.stance}\n\n'
            f'Respond ONLY with JSON: {{"vote": 1|-1|0, "reason": "one sentence"}}'
        )
        payload = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": STANCE_JURY_SYSTEM},
                {"role": "user", "content": user_msg},
            ],
            "stream": False,
            "temperature": 0.1,
        }).encode()

        try:
            dispatch_premium(
                "tasks.run_stance_jury_single",
                model,
                max(1, (len(STANCE_JURY_SYSTEM) + len(user_msg)) // 4),
            )
            req = _urlreq.Request(
                "http://localhost:11434/v1/chat/completions",
                data=payload,
                headers={"Content-Type": "application/json"},
            )
            with _urlreq.urlopen(req, timeout=45) as resp:
                data = json.loads(resp.read())
                usage = data.get("usage") or {}
                log_llm_spend(
                    "tasks.run_stance_jury_single",
                    model,
                    prompt_tokens=usage.get("prompt_tokens"),
                    completion_tokens=usage.get("completion_tokens"),
                    estimated_tokens=max(1, (len(STANCE_JURY_SYSTEM) + len(user_msg)) // 4),
                )
                content = data["choices"][0]["message"]["content"]
                content = strip_think_blocks(content)
                parsed = _parse_jury_json(content)
        except Exception as e:
            print(f"[jury_single] ev #{evidence_id}: model call failed: {e}")
            raise

        if not parsed:
            raise RuntimeError(f"jury_single returned no parseable vote for evidence #{evidence_id}")

        value = max(-1, min(1, int(parsed.get("vote", 0))))
        if value != 0:
            agent_id = _agent_id_for_model(db, model)
            db.add(EvidenceVote(
                evidence_id=ev.id,
                value=value,
                agent_id=agent_id,
                voter_type="jury",
                weight=1.0,
                reason=(parsed.get("reason") or "")[:500],
            ))

        # Stance flip if clearly wrong
        if not parsed.get("stance_correct", True):
            if ev.stance == "supports":
                ev.stance = "challenges"
            elif ev.stance == "challenges":
                ev.stance = "supports"

        ev.stance_jury_run_at = _dt.datetime.utcnow()
        db.flush()

        from app.routers.claims import recalculate_trust_v2
        result = recalculate_trust_v2(ev.claim_id, db, trigger="jury_single")
        new_trust = result[0] if isinstance(result, tuple) else result
        db.commit()
        _release_stance_jury_inflight(evidence_id)

        if new_trust == "consensus":
            _notify(f"🟢 Claim #{ev.claim_id} → consensus (jury_single)")
        elif new_trust == "challenged":
            _notify(f"🔴 Claim #{ev.claim_id} → challenged (jury_single)")

    except Exception as e:
        db.rollback()
        print(f"[jury_single] ev #{evidence_id} error: {e}")
        _jury_retry(self, e)
    finally:
        db.close()


@celery_app.task(name="app.agent_loop.tasks.drain_jury_fast_pass")
def drain_jury_fast_pass():
    """Every 30 min: send jury tasks to fast single-model path for evidence with <3 votes."""
    import datetime as _dt
    from app.models.claim import Claim, Evidence, EvidenceVote
    from sqlalchemy import func as sqlfunc, or_

    if not settings.STANCE_JURY_ENABLED:
        return

    db = SessionLocal()
    try:
        budget = max(0, settings.STANCE_JURY_FAST_MAX_ENQUEUE_PER_PASS)
        if budget == 0:
            print("[drain_jury_fast] fast-pass budget is 0, skipping")
            return

        # Priority 1: evidence with 0 votes on accepted/consensus claims
        zero_vote_accepted_query = (
            db.query(Evidence)
            .join(Claim, Claim.id == Evidence.claim_id)
            .outerjoin(EvidenceVote, EvidenceVote.evidence_id == Evidence.id)
            .filter(Evidence.stance_jury_run_at.is_(None))
            .filter(or_(
                sqlfunc.length(Evidence.abstract) >= 100,
                sqlfunc.length(Evidence.intro_excerpt) >= settings.INTRO_EXCERPT_MIN_CHARS,
            ))
            .filter(Claim.trust_level.in_(["accepted", "consensus"]))
        )
        zero_vote_accepted = (
            _apply_stance_jury_held_filters(zero_vote_accepted_query, Evidence, Claim)
            .group_by(Evidence.id)
            .having(sqlfunc.count(EvidenceVote.id) == 0)
            .order_by(Evidence.quality.desc())
            .limit(budget)
            .all()
        )

        enqueued = 0
        skipped_inflight = 0
        spacing = max(1, settings.STANCE_JURY_ENQUEUE_SPACING_SECONDS)
        for ev in zero_vote_accepted:
            countdown = enqueued * spacing
            if _enqueue_stance_jury_task(run_stance_jury_single, ev.id, countdown=countdown):
                enqueued += 1
            else:
                skipped_inflight += 1

        if enqueued < budget:
            # Priority 2: evidence with 1-2 votes (needs 3 for full confidence)
            low_vote_retry_cutoff = _dt.datetime.utcnow() - _dt.timedelta(
                seconds=max(0, settings.STANCE_JURY_LOW_VOTE_RETRY_MIN_AGE_SECONDS)
            )
            vote_count = (
                db.query(sqlfunc.count(EvidenceVote.id))
                .filter(EvidenceVote.evidence_id == Evidence.id)
                .correlate(Evidence)
                .as_scalar()
            )
            low_vote_query = (
                db.query(Evidence)
                .join(Claim, Claim.id == Evidence.claim_id)
                .filter(Evidence.stance_jury_run_at.isnot(None))  # already run but low votes
                .filter(Evidence.stance_jury_run_at < low_vote_retry_cutoff)
                .filter(or_(
                    sqlfunc.length(Evidence.abstract) >= 100,
                    sqlfunc.length(Evidence.intro_excerpt) >= settings.INTRO_EXCERPT_MIN_CHARS,
                ))
                .filter(Claim.trust_level.in_(["accepted", "debated"]))
                .filter(vote_count > 0)
                .filter(vote_count < 3)
            )
            low_vote = (
                _apply_stance_jury_held_filters(low_vote_query, Evidence, Claim)
                .order_by(Evidence.quality.desc())
                .limit(budget - enqueued)
                .all()
            )
            low_vote_claims: list[tuple[int, int]] = []
            for ev in low_vote:
                countdown = (enqueued + len(low_vote_claims)) * spacing
                if _claim_stance_jury_inflight(ev.id, countdown=countdown):
                    # Reset so single jury can run again
                    ev.stance_jury_run_at = None
                    low_vote_claims.append((ev.id, countdown))
                else:
                    skipped_inflight += 1
            if low_vote_claims:
                db.commit()
            for ev_id, countdown in low_vote_claims:
                try:
                    run_stance_jury_single.apply_async(args=[ev_id], countdown=countdown)
                except Exception:
                    _release_stance_jury_inflight(ev_id)
                    raise
                enqueued += 1

        print(f"[drain_jury_fast] enqueued {enqueued} fast jury runs (skipped_inflight={skipped_inflight})")
        if enqueued >= 50:
            _notify(f"⚡ Fast jury drain: {enqueued} evidence queued")
    finally:
        db.close()


def _maybe_notify_new_proposals(db) -> None:
    """Batch-notify Discord when >=3 proposals accumulate OR 24h since first."""
    import datetime as _dt
    from datetime import timedelta
    from app.models.external import NewPageProposal

    pending = db.query(NewPageProposal).filter(
        NewPageProposal.status == "pending",
        NewPageProposal.notified_at.is_(None)
    ).order_by(NewPageProposal.created_at).all()

    if not pending:
        return

    oldest_age = _dt.datetime.utcnow() - pending[0].created_at
    should_notify = (
        len(pending) >= settings.NEW_PAGE_PROPOSAL_NOTIFY_BATCH_SIZE
        or oldest_age >= timedelta(hours=settings.NEW_PAGE_PROPOSAL_NOTIFY_FLUSH_HOURS)
    )
    if not should_notify:
        return

    import json as _json
    lines = [f"🌌 **{len(pending)} new topics** ready for review:"]
    for p in pending[:10]:
        lines.append(f"• {p.suggested_title} ({len(_json.loads(p.cluster_papers))} papers)")
    msg = "\n".join(lines)
    _notify(msg)

    now = _dt.datetime.utcnow()
    for p in pending:
        p.notified_at = now


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

        from app.services.arxiv_classifier import refresh_page_vectors
        refresh_page_vectors(db)

        total_new = 0
        for cat in ARXIV_CATEGORIES:
            try:
                papers = _parse_arxiv_rss(cat, limit=20)
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

                try:
                    # LLM summary
                    try:
                        user_msg = (
                            f"Summarize this astronomy paper in 2-3 sentences for a general science audience.\n\n"
                            f"Title: {p['title']}\n\nAbstract: {p['abstract'][:800]}"
                        )
                        summary = _chat(arxivbot.model_name, ARXIV_SUMMARY_SYSTEM, user_msg, role="arxivbot")
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
                    print(f"[fetch_arxiv_daily] Saved: {p['title'][:60]}")

                    # === arXiv integration v2 (Phase B) ===
                    if settings.ARXIV_INTEGRATION_ENABLED:
                        try:
                            from app.services.arxiv_classifier import classify_match_type
                            from app.services.arxiv_ingest import (
                                handle_claim_evidence, handle_page_extension, handle_new_topic
                            )
                            import datetime as _dt
                            match_type, meta = classify_match_type(paper, db)
                            paper.match_type = match_type
                            paper.processed_at = _dt.datetime.utcnow()
                            if match_type == "claim_evidence":
                                handle_claim_evidence(paper, meta, db, arxivbot)
                            elif match_type == "page_extension":
                                handle_page_extension(paper, meta, db, arxivbot)
                            elif match_type == "new_topic_candidate":
                                handle_new_topic(paper, meta, db, arxivbot)
                            print(f"[fetch_arxiv_daily] classified: {match_type} ({paper.arxiv_id})")
                        except Exception as _integ_err:
                            print(f"[fetch_arxiv_daily] integration error: {_integ_err}")
                    else:
                        # Legacy: propose wiki edit if related pages found
                        if related:
                            for slug in related[:1]:
                                wiki_page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
                                if not wiki_page or not wiki_page.content:
                                    continue
                                try:
                                    edit_msg = (
                                        f"Update the wiki page."
                                    )
                                    updated = _chat(arxivbot.model_name, SYSTEM_PROMPT, edit_msg, role="arxivbot")
                                    allowed, reason = can_propose_edit(db, wiki_page.id, arxivbot.id)
                                    if allowed:
                                        proposal = EditProposal(page_id=wiki_page.id, agent_id=arxivbot.id, content=updated, status=EditStatus.PENDING)
                                        db.add(proposal)
                                        paper.wiki_edit_proposed = True
                                    else:
                                        print(f"[fetch_arxiv_daily] Edit throttled for {slug}: {reason}")
                                except Exception as e:
                                    print(f"[fetch_arxiv_daily] Wiki edit failed for {slug}: {e}")

                    db.commit()
                    total_new += 1
                except Exception as _paper_err:
                    db.rollback()
                    print(f"[fetch_arxiv_daily] paper failed ({p.get('arxiv_id', '?')}): {_paper_err}")

                time.sleep(2)

        print(f"[fetch_arxiv_daily] Done. {total_new} new papers saved.")
        _notify(f"📡 arXiv 수집 완료: {total_new}개 새 논문")
    except Exception as e:
        print(f"[fetch_arxiv_daily] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task
def retry_unprocessed_arxiv_papers():
    """Re-classify ArxivPaper rows that were saved but never processed (match_type IS NULL)."""
    import datetime as _dt
    from app.models.arxiv import ArxivPaper

    db = SessionLocal()
    try:
        cutoff = _dt.datetime.utcnow() - _dt.timedelta(hours=1)
        papers = db.query(ArxivPaper).filter(
            ArxivPaper.match_type.is_(None),
            ArxivPaper.processed_at.is_(None),
            ArxivPaper.created_at < cutoff,
        ).all()

        if not papers:
            print("[retry_unprocessed] nothing to retry")
            return

        print(f"[retry_unprocessed] {len(papers)} papers to retry")
        arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()

        from app.services.arxiv_classifier import classify_match_type, refresh_page_vectors
        from app.services.arxiv_ingest import (
            handle_claim_evidence, handle_page_extension, handle_new_topic
        )
        refresh_page_vectors(db)

        for paper in papers:
            try:
                match_type, meta = classify_match_type(paper, db)
                paper.match_type = match_type
                paper.processed_at = _dt.datetime.utcnow()
                if match_type == "claim_evidence":
                    handle_claim_evidence(paper, meta, db, arxivbot)
                elif match_type == "page_extension":
                    handle_page_extension(paper, meta, db, arxivbot)
                elif match_type == "new_topic_candidate":
                    handle_new_topic(paper, meta, db, arxivbot)
                db.commit()
                print(f"[retry_unprocessed] {paper.arxiv_id} → {match_type}")
            except Exception as _err:
                db.rollback()
                print(f"[retry_unprocessed] failed {paper.arxiv_id}: {_err}")
    except Exception as e:
        print(f"[retry_unprocessed] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task
def process_pending_verify_retries():
    """Retry claim_evidence papers that were rejected due to ADS indexing lag.

    Runs daily at UTC 08:00. Finds ArxivPaper rows with verify_retry_at <= now
    (set 48h after initial verify_rejected_ads_lag) and re-attempts the ADS
    lookup + evidence insertion. Clears verify_retry_at after each attempt
    regardless of outcome so papers are retried at most once.
    """
    import datetime as _dt
    from app.models.arxiv import ArxivPaper

    db = SessionLocal()
    try:
        now = _dt.datetime.utcnow()
        papers = db.query(ArxivPaper).filter(
            ArxivPaper.verify_retry_at <= now,
            ArxivPaper.match_type == "claim_evidence",
        ).all()

        if not papers:
            print("[verify_retry] nothing due")
            return

        print(f"[verify_retry] {len(papers)} papers due for ADS-lag retry")
        arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()

        from app.services.arxiv_classifier import classify_match_type
        from app.services.arxiv_ingest import handle_claim_evidence
        from app.models.external import ExternalSourceLog

        for paper in papers:
            # Clear retry flag before attempt so it isn't picked up again even
            # if this worker crashes mid-flight.
            paper.verify_retry_at = None
            db.flush()

            # Re-fetch match meta from a fresh classify or reconstruct from log
            try:
                match_type, meta = classify_match_type(paper, db)
                if match_type != "claim_evidence":
                    # Page/claim vectors changed; re-route naturally
                    paper.match_type = match_type
                    db.commit()
                    print(f"[verify_retry] {paper.arxiv_id} reclassified → {match_type}")
                    continue

                handle_claim_evidence(paper, meta, db, arxivbot)
                db.commit()
                print(f"[verify_retry] {paper.arxiv_id} → retried")
            except Exception as _err:
                db.rollback()
                # Re-clear retry flag after rollback
                try:
                    paper.verify_retry_at = None
                    db.commit()
                except Exception:
                    pass
                print(f"[verify_retry] failed {paper.arxiv_id}: {_err}")
    except Exception as e:
        print(f"[verify_retry] Error: {e}")
        raise
    finally:
        db.close()


@celery_app.task
def send_arxiv_daily_summary():
    """Post a daily arXiv ingest summary to Discord #general."""
    import datetime as _dt
    import json as _json
    import os
    import subprocess
    from app.models.external import ExternalSourceLog, NewPageProposal
    from app.models.arxiv import ArxivPaper

    db = SessionLocal()
    try:
        today_start = _dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)

        rows = db.query(ExternalSourceLog).filter(
            ExternalSourceLog.source == "arxiv",
            ExternalSourceLog.created_at >= today_start,
        ).all()

        decision_counts: dict[str, int] = {}
        for row in rows:
            decision_counts[row.decision] = decision_counts.get(row.decision, 0) + 1

        paper_count = db.query(ArxivPaper).filter(
            ArxivPaper.created_at >= today_start,
        ).count()

        evidence = decision_counts.get("evidence_inserted", 0)
        page_edits = decision_counts.get("page_extension_proposed", 0)
        new_topics = decision_counts.get("new_topic_staged", 0)
        skipped = sum(
            v for k, v in decision_counts.items()
            if k.startswith("skipped") or k in ("verify_rejected", "verify_failed")
        )

        pending_proposals = db.query(NewPageProposal).filter(
            NewPageProposal.status == "pending",
        ).count()

        lines = [
            f"📡 **arXiv ingest {today_start.strftime('%Y-%m-%d')}:**",
            f"  • {paper_count} new papers",
            f"  • {evidence} evidence inserted",
            f"  • {page_edits} page edits proposed",
            f"  • {new_topics} new topic candidates staged",
            f"  • {skipped} skipped/rejected",
        ]
        if pending_proposals > 0:
            lines.append(f"  • {pending_proposals} pending proposals in queue")

        message = "\n".join(lines)

        webhook_url = os.getenv("DISCORD_NEBULAMIND_WEBHOOK", "")
        if webhook_url:
            subprocess.run(
                ["curl", "-s", "-X", "POST", webhook_url,
                 "-H", "Content-Type: application/json",
                 "-d", _json.dumps({"content": message})],
                timeout=5, capture_output=True,
            )
        print(f"[arxiv_daily_summary] posted: {paper_count} papers, {evidence} evidence")
    except Exception as e:
        print(f"[arxiv_daily_summary] Error: {e}")
        raise
    finally:
        db.close()
