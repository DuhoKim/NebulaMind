"""Shared helpers for local and hosted LLM responses."""
from __future__ import annotations

import re

# Match <think>...</think> or <thinking>...</thinking>, case-insensitive.
_THINK_BLOCK_RE = re.compile(
    r"<think(?:ing)?>.*?</think(?:ing)?>",
    re.DOTALL | re.IGNORECASE,
)

# Match an unclosed <think> or <thinking> block running to EOF.
_UNCLOSED_THINK_RE = re.compile(
    r"<think(?:ing)?>.*\Z",
    re.DOTALL | re.IGNORECASE,
)

# Match a single outer Markdown code fence, including ```json.
_JSON_FENCE_RE = re.compile(
    r"^\s*```(?:json)?\s*(.*?)\s*```\s*\Z",
    re.DOTALL | re.IGNORECASE,
)


def strip_think_blocks(text: str | None) -> str:
    """Remove reasoning traces emitted by DeepSeek/Qwen-style thinking models."""
    if not text:
        return ""
    cleaned = _THINK_BLOCK_RE.sub("", text)
    cleaned = _UNCLOSED_THINK_RE.sub("", cleaned)
    return cleaned.strip()


def clean_llm_response(text: str | None) -> str:
    """Strip reasoning traces and unwrap one outer JSON Markdown fence."""
    cleaned = strip_think_blocks(text)
    match = _JSON_FENCE_RE.match(cleaned)
    if match:
        cleaned = match.group(1).strip()
    return cleaned
