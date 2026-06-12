#!/usr/bin/env python3
"""
Nutty hero fact generation for 3 pages missing hero_facts.
Model: gpt-oss:20b via Ollama
"""
import json
import logging
import re
import sys
import httpx
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.models.page import WikiPage
from app.services.llm_utils import strip_think_blocks

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

DB_URL = "postgresql://nebula:nebula@localhost:5432/nebulamind"
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "gpt-oss:20b"
TARGET_PAGES = [
    {"id": 8,  "slug": "black-hole-mergers"},
    {"id": 41, "slug": "gravitational-lensing"},
    {"id": 11, "slug": "exoplanets"},
]

SYSTEM = "You are an astronomy knowledge engineer."
PROMPT_TPL = (
    "Given this wiki page content, generate 3 hero facts — quantitative, specific, sourced findings "
    "that would impress a professional astronomer. Return JSON array only:\n"
    '[{{"label": "...", "value": "...", "unit": "...", "kind": "range", '
    '"source": {{"tier": "authoritative", "arxiv_id": "...", "year": 2024}}}}]\n'
    "Use real arXiv IDs or leave arxiv_id as null. Do not hallucinate.\n\n"
    "Page content:\n{content}"
)

_decoder = json.JSONDecoder()

def extract_json(raw: str):
    text = re.sub(r"```(?:json)?\s*", "", raw, flags=re.IGNORECASE).strip()
    text = strip_think_blocks(text)
    try:
        return json.loads(text)
    except Exception:
        pass
    for opener in "[{":
        for i, ch in enumerate(text):
            if ch != opener:
                continue
            try:
                obj, _ = _decoder.raw_decode(text, i)
                return obj
            except json.JSONDecodeError:
                continue
    return None

def call_nutty(content: str) -> list:
    prompt = PROMPT_TPL.format(content=content[:3000])
    resp = httpx.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.4,
        },
        timeout=120,
    )
    resp.raise_for_status()
    raw = resp.json()["choices"][0]["message"]["content"].strip()
    log.info("Raw response (first 400): %s", raw[:400])
    parsed = extract_json(raw)
    if isinstance(parsed, dict):
        parsed = parsed.get("facts") or parsed.get("hero_facts") or list(parsed.values())[0] if parsed else []
    if not isinstance(parsed, list):
        log.warning("Could not parse JSON list from response")
        return []
    return [f for f in parsed if isinstance(f, dict) and f.get("label") and f.get("value")][:3]

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

with Session() as db:
    for target in TARGET_PAGES:
        page = db.get(WikiPage, target["id"])
        if page is None:
            log.warning("Page id=%d not found in DB", target["id"])
            continue
        if page.hero_facts:
            log.info("Page %s already has hero_facts — skipping", target["slug"])
            continue
        log.info("Generating hero facts for %s (id=%d)", target["slug"], target["id"])
        try:
            facts = call_nutty(page.content)
        except Exception as exc:
            log.error("Nutty call failed for %s: %s", target["slug"], exc)
            continue
        if not facts:
            log.warning("No facts returned for %s", target["slug"])
            continue
        page.hero_facts = json.dumps(facts)
        db.commit()
        log.info("Saved %d hero facts for %s: %s", len(facts), target["slug"],
                 [f.get("label") for f in facts])

log.info("nutty_hero_facts done")
