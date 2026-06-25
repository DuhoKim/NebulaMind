"""
LLM Routing v3 — canonical platoon nicknames from docs/platoon_overhaul_v2.md §4.

Tiers:
  T1  Mac Studio fast   — Nutty (gpt-oss:20b)
  T2  Mac Studio heavy  — Mima (qwen3.6:35b-a3b-nvfp4)
  T3  Mac Studio heavy  — Buddle (gpt-oss:120b)
  T4  Mac Pro 671b      — Rakon (deepseek-r1:671b) — galaxy-evolution priority
  T5  Cloud free        — Gemini-2.0-flash, Cerebras, SambaNova, Groq

Other canonical residents: Vera (astrosage-70b), Blanc (llama3.3:70b),
Pico (vanta-research/atom-astronomy-7b).
"""
from __future__ import annotations

from app.config import BATCH_SAFE_DEFAULT_MODEL, settings

def _v1_url(url: str) -> str:
    base = (url or "").rstrip("/")
    if not base:
        return ""
    return base if base.endswith("/v1") else f"{base}/v1"


_STUDIO = _v1_url(settings.OLLAMA_STUDIO_BASE_URL or settings.OLLAMA_BASE_URL)
_PRO = _v1_url(settings.RAKON_BASE_URL or settings.OLLAMA_MACPRO_BASE_URL)
_BUDDLE_HOST = _v1_url(settings.BUDDLE_BASE_URL or settings.OLLAMA_STUDIO_BASE_URL or settings.OLLAMA_BASE_URL)
_NUTTY = settings.OLLAMA_STUDIO_FAST_MODEL
_MIMA = settings.OLLAMA_STUDIO_HEAVY_MODEL
_TERA = settings.ADVERSARIAL_QUERY_MODEL
_BUDDLE = settings.BUDDLE_MODEL or settings.OLLAMA_MACPRO_FAST_MODEL or settings.OLLAMA_MACPRO_MODEL
_RAKON = settings.RAKON_MODEL or settings.OLLAMA_MACPRO_HEAVY_MODEL

def _ollama(host: str, model: str, label: str | None = None, timeout: int = 120) -> dict:
    return {"base_url": host, "api_key": "ollama", "model": model,
            "label": label or model, "timeout": timeout}

def _gemini(label: str = BATCH_SAFE_DEFAULT_MODEL) -> dict | None:
    if not settings.GEMINI_API_KEY:
        return None
    model = BATCH_SAFE_DEFAULT_MODEL or "gemini-2.5-flash"
    return {"base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
            "api_key": settings.GEMINI_API_KEY, "model": model,
            "label": label, "timeout": 60}

def _cerebras(label: str = "cerebras") -> dict | None:
    if not settings.CEREBRAS_API_KEY:
        return None
    return {"base_url": "https://api.cerebras.ai/v1",
            "api_key": settings.CEREBRAS_API_KEY, "model": "llama3.1-8b",
            "label": label, "timeout": 30}

def _sambanova(label: str = "sambanova") -> dict | None:
    if not settings.SAMBANOVA_API_KEY:
        return None
    return {"base_url": "https://api.sambanova.ai/v1",
            "api_key": settings.SAMBANOVA_API_KEY,
            "model": settings.SAMBANOVA_MODEL or "Meta-Llama-3.3-70B-Instruct",
            "label": label, "timeout": 60}

def _compact(lst: list) -> list:
    """Remove None entries."""
    return [m for m in lst if m is not None]


# ---------------------------------------------------------------------------
# ROUTING — 11 task roles → ordered model list (parallel)
# ---------------------------------------------------------------------------

ROUTING: dict[str, list[dict]] = {

    # Writer: best quality content generation
    "writer": _compact([
        _ollama(_STUDIO, _MIMA,              "mima"),
        _ollama(_BUDDLE_HOST, _BUDDLE,       "buddle", timeout=180),
        _gemini(),
        _sambanova(),
    ]),

    # Reviewer: critical evaluation of proposals
    "reviewer": _compact([
        _ollama(_STUDIO, _NUTTY,             "nutty"),
        _ollama(_STUDIO, _MIMA,              "mima"),
        _ollama(_BUDDLE_HOST, _BUDDLE,       "buddle", timeout=180),
        _gemini(),
    ]),

    # Commenter: discussion comments
    "commenter": _compact([
        _ollama(_STUDIO, _MIMA,              "mima"),
        _ollama(_STUDIO, _NUTTY,             "nutty"),
        _gemini(),
    ]),

    # Synthesis: multi-draft merge (heavy reasoning)
    "synthesis": _compact([
        _ollama(_BUDDLE_HOST, _BUDDLE,       "buddle", timeout=240),
        _ollama(_STUDIO, _MIMA,              "mima"),
        _gemini(),
    ]),

    # Renovation synthesis: Studio local preferred; Rakon reserved for galaxy-evolution
    "renovation_synth": _compact([
        _ollama(_STUDIO, _MIMA,              "mima"),
        _ollama(_STUDIO, _NUTTY,             "nutty"),
        _ollama(_BUDDLE_HOST, _BUDDLE,       "buddle", timeout=240),
        _gemini(),
    ]),

    # Jury fast: evidence stance voting (speed matters)
    "jury_fast": _compact([
        _ollama(_STUDIO, _NUTTY,             "nutty"),
        _cerebras("cerebras-fast"),
        _sambanova(),
    ]),

    # Adversarial: challenging existing claims (deep reasoning)
    "adversarial": _compact([
        _ollama(_PRO,    _RAKON,             "rakon",   timeout=300),
        _ollama(_BUDDLE_HOST, _BUDDLE,       "buddle", timeout=240),
        _ollama(_STUDIO, _NUTTY,             "nutty"),
    ]),

    # Evidence linker: Nutty for inference, Cerebras fallback
    "evidence_linker": _compact([
        _ollama(_STUDIO, _NUTTY,             "nutty"),
        _cerebras("cerebras-fast"),
        _gemini(),
    ]),

    # ArXiv bot: paper summarization (Cerebras primary for speed)
    "arxivbot": _compact([
        _cerebras("cerebras-fast"),
        _gemini(),
    ]),

    # Council adjudication: high-stakes decisions (Rakon)
    "council": _compact([
        _ollama(_PRO,    _RAKON,             "rakon",   timeout=300),
        _ollama(_BUDDLE_HOST, _BUDDLE,       "buddle", timeout=240),
        _ollama(_STUDIO, _MIMA,              "mima"),
    ]),

    # Query generation: search query formulation
    "query_gen": _compact([
        _ollama(_STUDIO, _TERA,              "tera"),
        _ollama(_STUDIO, _NUTTY,             "nutty"),
        _gemini(),
    ]),
}


def get_models(role: str) -> list[dict]:
    """Return model list for a given task role. Falls back to 'writer' if unknown."""
    return ROUTING.get(role, ROUTING["writer"])


def get_primary(role: str) -> dict | None:
    """Return the primary (first) model for a role."""
    models = get_models(role)
    return models[0] if models else None
