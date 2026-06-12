"""
NebulaMind Rate Limiting — Redis-backed, API-key-aware.

Limits (all configurable via env vars):
  NM_RATE_VOTES_PER_KEY    = 200/minute  (per API key)
  NM_RATE_EDITS_PER_KEY    = 30/minute   (per API key)
  NM_RATE_REGISTER_PER_IP  = 5/hour      (per IP)
  NM_RATE_ANON_READ        = 60/minute   (anonymous per IP)
  NM_RATE_ADMIN_PER_IP     = 10/minute   (admin endpoints per IP, except /admin/llm)
"""
from __future__ import annotations

import os
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

# ── Key function ──────────────────────────────────────────────────────────────

def rate_key_or_ip(request: Request) -> str:
    """Use X-API-Key if present, else Cloudflare real IP, else remote addr."""
    api_key = request.headers.get("x-api-key") or request.headers.get("X-Api-Key")
    if api_key:
        return f"key:{api_key[:16]}"  # prefix to namespace, truncate for safety
    cf_ip = request.headers.get("cf-connecting-ip")
    if cf_ip:
        return f"ip:{cf_ip}"
    return f"ip:{get_remote_address(request)}"


def rate_ip_only(request: Request) -> str:
    """Always key by IP (for register + admin endpoints)."""
    cf_ip = request.headers.get("cf-connecting-ip")
    if cf_ip:
        return f"ip:{cf_ip}"
    return f"ip:{get_remote_address(request)}"


# ── Redis storage URI ─────────────────────────────────────────────────────────

_REDIS_URL = os.environ.get("NM_REDIS_URL", "redis://localhost:6379/1")

# ── Limiter instances ─────────────────────────────────────────────────────────

# Primary limiter — keyed by API key or IP, Redis-backed
limiter = Limiter(
    key_func=rate_key_or_ip,
    storage_uri=_REDIS_URL,
    default_limits=[],
)

# IP-only limiter for registration + admin
ip_limiter = Limiter(
    key_func=rate_ip_only,
    storage_uri=_REDIS_URL,
    default_limits=[],
)

# ── Limit strings (read from env, with defaults) ──────────────────────────────

VOTES_LIMIT    = os.environ.get("NM_RATE_VOTES_PER_KEY",   "200/minute")
EDITS_LIMIT    = os.environ.get("NM_RATE_EDITS_PER_KEY",   "30/minute")
REGISTER_LIMIT = os.environ.get("NM_RATE_REGISTER_PER_IP", "5/hour")
ANON_LIMIT     = os.environ.get("NM_RATE_ANON_READ",       "60/minute")
ADMIN_LIMIT    = os.environ.get("NM_RATE_ADMIN_PER_IP",    "10/minute")
GENERAL_LIMIT  = os.environ.get("NM_RATE_GENERAL",         "120/minute")
