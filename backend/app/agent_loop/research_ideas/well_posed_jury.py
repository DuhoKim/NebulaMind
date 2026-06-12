import json
import logging
from datetime import datetime

from celery import shared_task
from sqlalchemy import text

from app.config import settings
from app.database import SessionLocal

logger = logging.getLogger(__name__)
BUDDLE_BASE_URL = settings.BUDDLE_BASE_URL.rstrip("/")


@shared_task(name="well_posed_jury.run")
def run_well_posed_jury():
    db = SessionLocal()
    try:
        _run(db)
    finally:
        db.close()


def _run(db):
    ideas = db.execute(text("""
        SELECT id, question, why_now, approach
        FROM research_ideas
        WHERE well_posed_score IS NULL
          AND status IN (active, covered)
        ORDER BY created_at DESC
        LIMIT 50
    """)).fetchall()

    logger.info(f"Well-posed jury: scoring {len(ideas)} ideas")

    for idea in ideas:
        score, rationale = _score_idea(idea)
        db.execute(text("""
            UPDATE research_ideas
            SET well_posed_score = :score, well_posed_updated_at = NOW(), updated_at = NOW()
            WHERE id = :id
        """), {"score": score, "id": idea.id})
        db.commit()
        logger.debug(f"Idea {idea.id}: well_posed={score:.2f} — {rationale}")

    logger.info("Well-posed jury: done")


def _score_idea(idea) -> tuple[float, str]:
    import httpx
    from app.services.prompt_registry import PromptRegistry

    variables = {
        "question": idea.question,
        "why_now": idea.why_now[:500] if idea.why_now else "",
        "approach": idea.approach[:500] if idea.approach else "",
    }

    try:
        prompt = PromptRegistry().render("well_posed", variables)
    except Exception as e:
        prompt = f"""You are evaluating whether a research idea is well-posed.

A well-posed idea has:
1. A clear, falsifiable question (not "explore" or "understand")
2. A specific measurement with pass/fail criteria a graduate student could write
3. Named datasets and methods

Score 0.0-1.0:
- 0.9-1.0: fully falsifiable, specific measurement, clear success criterion
- 0.6-0.8: mostly specific, minor ambiguity
- 0.3-0.5: partially specified
- 0.0-0.2: vague exploration, no testable prediction

Research Idea:
QUESTION: {variables['question']}
WHY NOW: {variables['why_now']}
APPROACH: {variables['approach']}

Respond with JSON only: {{"well_posed": 0.XX, "rationale": "one sentence"}}"""

    try:
        with httpx.Client(timeout=120) as client:
            resp = client.post(f"{BUDDLE_BASE_URL}/api/generate", json={
                "model": settings.BUDDLE_MODEL,
                "prompt": prompt,
                "stream": False,
                "format": "json",
            })
            data = resp.json()
            result = json.loads(data.get("response", "{}"))
            score = float(result.get("well_posed", 0.5))
            score = max(0.0, min(1.0, score))
            rationale = result.get("rationale", "")
            return score, rationale
    except Exception as e:
        logger.warning(f"Well-posed jury error for idea {idea.id}: {e}")
        return 0.5, "jury_error"
