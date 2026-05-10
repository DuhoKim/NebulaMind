"""
LLM Routing v1 — Model-role assignment for NebulaMind agent tasks.

Tiers:
  T1  Mac Studio fast   — Nutty (deepseek-r1:14b), Takji (phi4:14b)
  T2  Mac Studio heavy  — Blanc (llama3.3:70b), Mima (qwen3:30b), Tera (gemma3:27b)
  T3  Mac Pro 32b       — Buddle (deepseek-r1:32b)
  T4  Mac Pro 671b      — Rakon (deepseek-r1:671b) — galaxy-evolution priority
  T5  Cloud free        — Gemini-2.0-flash, Cerebras, SambaNova, Groq
"""
from __future__ import annotations

from app.config import settings

_STUDIO = "http://localhost:11434/v1"
_PRO    = "http://192.188.0.4:11434/v1"

def _ollama(host: str, model: str, label: str | None = None, timeout: int = 120) -> dict:
    return {"base_url": host, "api_key": "ollama", "model": model,
            "label": label or model, "timeout": timeout}

def _gemini(label: str = "gemini-2.0-flash") -> dict | None:
    if not settings.GEMINI_API_KEY:
        return None
    return {"base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
            "api_key": settings.GEMINI_API_KEY, "model": "gemini-2.0-flash",
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
        _ollama(_STUDIO, "llama3.3:70b",    "blanc"),
        _ollama(_STUDIO, "qwen3:30b",        "mima"),
        _ollama(_PRO,    "deepseek-r1:32b",  "buddle", timeout=180),
        _gemini(),
        _sambanova(),
    ]),

    # Reviewer: critical evaluation of proposals
    "reviewer": _compact([
        _ollama(_STUDIO, "deepseek-r1:14b",  "nutty"),
        _ollama(_STUDIO, "qwen3:30b",        "mima"),
        _ollama(_PRO,    "deepseek-r1:32b",  "buddle", timeout=180),
        _gemini(),
    ]),

    # Commenter: discussion comments
    "commenter": _compact([
        _ollama(_STUDIO, "gemma3:27b",       "tera"),
        _ollama(_STUDIO, "phi4:14b",         "takji"),
        _ollama(_STUDIO, "deepseek-r1:14b",  "nutty"),
        _gemini(),
    ]),

    # Synthesis: multi-draft merge (heavy reasoning)
    "synthesis": _compact([
        _ollama(_PRO,    "deepseek-r1:32b",  "buddle",  timeout=240),
        _ollama(_STUDIO, "llama3.3:70b",     "blanc"),
        _ollama(_STUDIO, "qwen3:30b",        "mima"),
        _gemini(),
    ]),

    # Renovation synthesis: Studio local preferred; Rakon reserved for galaxy-evolution
    "renovation_synth": _compact([
        _ollama(_STUDIO, "qwen3:30b",        "mima"),
        _ollama(_STUDIO, "gemma3:27b",       "tera"),
        _ollama(_STUDIO, "deepseek-r1:14b",  "nutty"),
        _ollama(_PRO,    "deepseek-r1:32b",  "buddle",  timeout=240),
        _gemini(),
    ]),

    # Jury fast: evidence stance voting (speed matters)
    "jury_fast": _compact([
        _ollama(_STUDIO, "llama3.3:70b",     "blanc"),
        _cerebras("cerebras-fast"),
        _sambanova(),
    ]),

    # Adversarial: challenging existing claims (deep reasoning)
    "adversarial": _compact([
        _ollama(_PRO,    "deepseek-r1:671b", "rakon",   timeout=300),
        _ollama(_PRO,    "deepseek-r1:32b",  "buddle",  timeout=240),
        _ollama(_STUDIO, "deepseek-r1:14b",  "nutty"),
    ]),

    # Evidence linker: Nutty/Takji for cheap inference, Cerebras fallback
    "evidence_linker": _compact([
        _ollama(_STUDIO, "deepseek-r1:14b",  "nutty"),
        _ollama(_STUDIO, "phi4:14b",         "takji"),
        _cerebras("cerebras-fast"),
        _gemini(),
    ]),

    # ArXiv bot: paper summarization (Cerebras primary for speed)
    "arxivbot": _compact([
        _cerebras("cerebras-fast"),
        _ollama(_STUDIO, "llama3.3:70b",     "blanc"),
        _gemini(),
    ]),

    # Council adjudication: high-stakes decisions (Rakon)
    "council": _compact([
        _ollama(_PRO,    "deepseek-r1:671b", "rakon",   timeout=300),
        _ollama(_PRO,    "deepseek-r1:32b",  "buddle",  timeout=240),
        _ollama(_STUDIO, "qwen3:30b",        "mima"),
    ]),

    # Query generation: search query formulation
    "query_gen": _compact([
        _ollama(_STUDIO, "qwen3:30b",        "mima"),
        _ollama(_STUDIO, "gemma3:27b",       "tera"),
        _ollama(_STUDIO, "deepseek-r1:14b",  "nutty"),
        _ollama(_STUDIO, "llama3.3:70b",     "blanc"),
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
