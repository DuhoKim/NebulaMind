#!/usr/bin/env python3
"""
Mima evidence link pass on bottom pages (qwen3.6:35b-a3b-nvfp4).
Finds claims with < 3 evidence items, suggests arXiv papers.
"""
import json
import logging
import re
import sys
import httpx
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.models.claim import Claim, Evidence
from app.services.llm_utils import strip_think_blocks

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

DB_URL = "postgresql://nebula:nebula@localhost:5432/nebulamind"
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "qwen3.6:35b-a3b-nvfp4"
TARGET_PAGES = [
    {"id": 40, "slug": "accretion-disks"},
    {"id": 50, "slug": "planetary-formation"},
    {"id": 37, "slug": "interstellar-medium"},
]
MAX_CLAIMS_PER_PAGE = 20

PROMPT_TPL = (
    "Given this astronomy claim: '{claim_text}' — suggest 1-2 real arXiv paper IDs "
    "(format: YYMM.NNNNN) that directly support this. Return JSON only: "
    '[{{"arxiv_id": "...", "stance": "supports"}}]. '
    "Only suggest papers you are confident exist. No hallucination."
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

def call_mima(claim_text: str) -> list:
    prompt = PROMPT_TPL.format(claim_text=claim_text[:400])
    resp = httpx.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
        },
        timeout=90,
    )
    resp.raise_for_status()
    raw = resp.json()["choices"][0]["message"]["content"].strip()
    parsed = extract_json(raw)
    if isinstance(parsed, dict):
        parsed = [parsed]
    if not isinstance(parsed, list):
        return []
    valid = []
    for item in parsed:
        if not isinstance(item, dict):
            continue
        arxiv_id = item.get("arxiv_id", "").strip()
        # Validate format: YYMM.NNNNN or YYMM.NNNNNN
        if re.match(r"^\d{4}\.\d{4,6}$", arxiv_id):
            valid.append({"arxiv_id": arxiv_id, "stance": item.get("stance", "supports")})
    return valid[:2]

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

with Session() as db:
    for target in TARGET_PAGES:
        log.info("Processing page %s (id=%d)", target["slug"], target["id"])

        # Get claims for this page with evidence count
        claims = (
            db.query(Claim)
            .filter(Claim.page_id == target["id"])
            .order_by(Claim.id)
            .limit(MAX_CLAIMS_PER_PAGE)
            .all()
        )
        log.info("  Found %d claims", len(claims))

        for claim in claims:
            # Count existing evidence
            ev_count = (
                db.query(func.count(Evidence.id))
                .filter(Evidence.claim_id == claim.id)
                .scalar()
            )
            if ev_count >= 3:
                continue

            log.info("  Claim %d (ev=%d): %s", claim.id, ev_count, claim.text[:80])
            try:
                suggestions = call_mima(claim.text)
            except Exception as exc:
                log.warning("  Mima call failed for claim %d: %s", claim.id, exc)
                continue

            for sug in suggestions:
                arxiv_id = sug["arxiv_id"]
                # Skip if already exists for this claim
                exists = (
                    db.query(Evidence)
                    .filter(Evidence.claim_id == claim.id, Evidence.arxiv_id == arxiv_id)
                    .first()
                )
                if exists:
                    log.info("  arXiv %s already linked to claim %d — skip", arxiv_id, claim.id)
                    continue

                ev = Evidence(
                    claim_id=claim.id,
                    arxiv_id=arxiv_id,
                    title=f"arXiv:{arxiv_id}",
                    stance=sug.get("stance", "supports"),
                    quality=0.5,
                    source_channel="mima-link",
                )
                db.add(ev)
                db.commit()
                log.info("  Added evidence arXiv:%s → claim %d", arxiv_id, claim.id)

log.info("mima_evidence_link done")
