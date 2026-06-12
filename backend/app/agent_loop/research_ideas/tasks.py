"""Celery tasks for Research Ideas pipeline.

v1.0 skeleton — triggers the Rakon → (AstroSage) → Atom chain.
Full pipeline implementation is gated behind Redis flags (design §6.5):
  research_ideas:enabled  — master gate (default 0)
  research_ideas:polish_enabled — AstroSage polish pass (default 0)
"""
import json
import logging
import datetime

from celery import shared_task

from app.config import settings
from app.services.llm_utils import strip_think_blocks

log = logging.getLogger(__name__)

ALLOWED_COMBOS = {
    "JWST+DESI", "JWST+Euclid", "JWST+ALMA", "JWST+HSC", "JWST+LSST", "JWST+VLA",
    "DESI+Euclid", "DESI+HSC", "DESI+ALMA", "DESI+LSST",
    "ALMA+Euclid", "ALMA+HSC", "ALMA+LSST", "ALMA+VLA",
    "Euclid+HSC", "Euclid+LSST",
    "HSC+LSST", "LSST+VLA",
}

NOVELTY_FLOOR = 0.40
FEASIBILITY_FLOOR = 0.30
DEDUP_COSINE_THRESHOLD = 0.75


@shared_task(name="app.agent_loop.research_ideas.tasks.regenerate_research_ideas", bind=True)
def regenerate_research_ideas(self, slug: str):
    """
    Main entry point for per-page research idea generation.
    Steps: context build → Rakon skeleton → (AstroSage polish) → Atom scoring → persist.
    """
    from app.database import SessionLocal
    from app.config import settings

    db = SessionLocal()
    run_id = None
    try:
        run_id = _create_run(db, slug)
        if run_id is None:
            log.error("regenerate_research_ideas: page '%s' not found", slug)
            return {"error": "page_not_found"}

        context = _build_context(db, slug)
        if not context:
            _finish_run(db, run_id, error="context_build_failed")
            return {"error": "context_build_failed"}

        skeletons = _call_rakon(context)
        if not skeletons:
            _finish_run(db, run_id, error="rakon_no_output")
            return {"error": "rakon_no_output", "run_id": run_id}

        log.info("Rakon returned %d skeletons for '%s'", len(skeletons), slug)

        # v1.0: AstroSage polish off by default (§6.5); enabled by Redis flag
        polish_enabled = _redis_flag("research_ideas:polish_enabled")
        if polish_enabled:
            skeletons = _astrosage_polish_batch(skeletons, context)

        # Atom scoring + dedup
        scored = _atom_score_and_dedup(skeletons, context)

        # Persist
        ideas_inserted = _persist_ideas(db, context["page_id"], scored, run_id)

        _finish_run(db, run_id, ideas_inserted=ideas_inserted)
        _discord_notify(slug, ideas_inserted, len(skeletons))

        return {"slug": slug, "run_id": run_id, "inserted": ideas_inserted, "generated": len(skeletons)}

    except Exception as exc:
        log.exception("regenerate_research_ideas failed for '%s': %s", slug, exc)
        if run_id:
            _finish_run(db, run_id, error=str(exc)[:200])
        raise
    finally:
        db.close()


def _redis_flag(key: str) -> bool:
    try:
        import redis as redis_lib
        from app.config import settings
        r = redis_lib.from_url(settings.REDIS_URL)
        return r.get(key) == b"1"
    except Exception:
        return False


def _create_run(db, slug: str) -> int | None:
    from sqlalchemy import text
    page_row = db.execute(text("SELECT id FROM wiki_pages WHERE slug = :s"), {"s": slug}).fetchone()
    if page_row is None:
        return None
    result = db.execute(text(
        "INSERT INTO autowiki_runs (page_id, started_at, kind, model_proposer, decision)"
        " VALUES (:pid, now(), 'research_ideas', 'rakon→atom-7b', 'pending')"
        " RETURNING id"
    ), {"pid": page_row.id})
    db.commit()
    return result.fetchone()[0]


def _finish_run(db, run_id: int, ideas_inserted: int = 0, error: str | None = None):
    from sqlalchemy import text
    decision = "error" if error else "commit"
    db.execute(text(
        "UPDATE autowiki_runs SET finished_at = now(), decision = :d, error_text = :e WHERE id = :id"
    ), {"d": decision, "e": error, "id": run_id})
    db.commit()


def _build_context(db, slug: str) -> dict | None:
    from sqlalchemy import text
    page = db.execute(text(
        "SELECT id, title, slug, hero_tagline FROM wiki_pages WHERE slug = :s"
    ), {"s": slug}).fetchone()
    if page is None:
        return None

    claims = db.execute(text(
        "SELECT id, section, text, trust_level, claim_type FROM claims"
        " WHERE page_id = :pid ORDER BY trust_score DESC NULLS LAST LIMIT 20"
    ), {"pid": page.id}).fetchall()

    debates = db.execute(text(
        "SELECT id, text, debate_topic FROM claims WHERE page_id = :pid AND claim_type = 'debate'"
    ), {"pid": page.id}).fetchall()

    papers = db.execute(text(
        "SELECT arxiv_id, title, abstract_summary, submitted FROM arxiv_papers"
        " WHERE related_pages::text LIKE :slug_pattern"
        " AND submitted >= :cutoff ORDER BY submitted DESC LIMIT 30"
    ), {"slug_pattern": f'%{slug}%', "cutoff": (datetime.date.today() - datetime.timedelta(days=365)).isoformat()}).fetchall()

    existing = db.execute(text(
        "SELECT id, survey_combo, question FROM research_ideas"
        " WHERE page_id = :pid AND status IN ('active', 'saved') LIMIT 20"
    ), {"pid": page.id}).fetchall()

    return {
        "page_id": page.id,
        "title": page.title,
        "slug": page.slug,
        "hero_tagline": page.hero_tagline or "",
        "claims": [{"id": c.id, "text": c.text, "type": c.claim_type, "trust": c.trust_level} for c in claims],
        "debates": [{"id": d.id, "text": d.text, "topic": d.debate_topic} for d in debates],
        "papers": [{"id": p.arxiv_id, "title": p.title, "summary": p.abstract_summary, "date": str(p.submitted)} for p in papers],
        "existing_ideas": [{"id": e.id, "combo": e.survey_combo, "question": e.question} for e in existing],
    }


def _format_block(items: list, key: str, max_len: int = 20) -> str:
    return "\n".join(f"[{i.get('id', i)}] {i.get(key, '')}" for i in items[:max_len])


def _call_rakon(context: dict) -> list:
    from app.agent_loop.research_ideas.prompts import RAKON_SKELETON_PROMPT
    from app.config import settings
    import httpx

    claims_block = _format_block(context["claims"], "text")
    debates_block = _format_block(context["debates"], "text")
    arxiv_block = _format_block(context["papers"], "title")
    existing_block = _format_block(context["existing_ideas"], "question")
    survey_coverage = _compute_survey_coverage(context["claims"])

    prompt = RAKON_SKELETON_PROMPT.format(
        title=context["title"],
        slug=context["slug"],
        hero_tagline=context["hero_tagline"],
        claims_block=claims_block,
        debates_block=debates_block,
        arxiv_block=arxiv_block,
        survey_coverage_block=survey_coverage,
        existing_ideas_block=existing_block,
    )

    try:
        resp = httpx.post(
            f"{settings.RAKON_BASE_URL}/api/generate",
            json={"model": settings.RAKON_MODEL, "prompt": prompt, "stream": False,
                  "options": {"temperature": 0.4, "num_predict": 8192}},
            timeout=300,
        )
        resp.raise_for_status()
        raw = strip_think_blocks(resp.json().get("response", ""))
        # Extract JSON
        import re
        json_match = re.search(r"\{[\s\S]*\}", raw)
        if not json_match:
            log.warning("Rakon response contains no JSON block")
            return []
        data = json.loads(json_match.group())
        skeletons = data.get("skeletons", [])
        # Validate combos
        return [s for s in skeletons if s.get("combo") in ALLOWED_COMBOS]
    except httpx.ReadTimeout:
        log.error("Rakon timeout after 300s for page '%s'", context["slug"])
        return []
    except Exception as exc:
        log.error("Rakon call failed: %s", exc)
        return []


def _compute_survey_coverage(claims: list) -> str:
    SURVEY_KEYWORDS = ["JWST", "DESI", "ALMA", "Euclid", "HSC", "LSST", "VLA", "Planck", "Gaia", "eROSITA"]
    counts: dict = {s: 0 for s in SURVEY_KEYWORDS}
    for c in claims:
        txt = c.get("text", "").upper()
        for s in SURVEY_KEYWORDS:
            if s.upper() in txt:
                counts[s] += 1
    return " ; ".join(f"{s}: {n} claims" for s, n in counts.items() if n > 0)


def _astrosage_polish_batch(skeletons: list, context: dict) -> list:
    """Polish each skeleton through AstroSage-70B in batches of 4."""
    from app.agent_loop.research_ideas.prompts import ASTROSAGE_POLISH_PROMPT
    from app.config import settings
    import httpx

    polished = []
    claims_5 = _format_block(context["claims"][:5], "text")
    batch_size = 4

    for i in range(0, len(skeletons), batch_size):
        batch = skeletons[i:i + batch_size]
        for skel in batch:
            prompt = ASTROSAGE_POLISH_PROMPT.format(
                combo=skel["combo"],
                question=skel["question"],
                why_now_skeleton=skel.get("why_now_skeleton", ""),
                approach_skeleton=skel.get("approach_skeleton", ""),
                title=context["title"],
                hero_tagline=context["hero_tagline"],
                claims_block_5=claims_5,
            )
            try:
                resp = httpx.post(
                    f"{settings.OLLAMA_BASE_URL}/api/generate",
                    json={"model": settings.ASTRO_SYNTH_MODEL, "prompt": prompt, "stream": False,
                          "options": {"temperature": 0.3, "num_predict": 2048}, "keep_alive": "1h"},
                    timeout=120,
                )
                resp.raise_for_status()
                import re
                raw = resp.json().get("response", "")
                json_match = re.search(r"\{[\s\S]*\}", raw)
                if not json_match:
                    polished.append(skel)
                    continue
                result = json.loads(json_match.group())
                if result.get("plausible") == "no":
                    log.info("AstroSage rejected combo=%s: %s", skel["combo"], result.get("rejection_reason"))
                    continue
                skel.update({
                    "question": result.get("question", skel["question"]),
                    "why_now": result.get("why_now", skel.get("why_now_skeleton", "")),
                    "approach": result.get("approach", skel.get("approach_skeleton", "")),
                    "systematics": result.get("systematics", []),
                })
                polished.append(skel)
            except Exception as exc:
                log.warning("AstroSage polish failed for %s: %s — keeping skeleton", skel["combo"], exc)
                polished.append(skel)
    return polished


def _atom_score_and_dedup(skeletons: list, context: dict) -> list:
    """Score each skeleton with Atom-7B and dedup against existing ideas."""
    from app.agent_loop.research_ideas.prompts import ATOM_SCORING_PROMPT
    from app.config import settings
    import httpx
    import re

    existing_short = "\n".join(
        f"[{e['id']}] {e['combo']}: {e['question'][:100]}"
        for e in context["existing_ideas"]
    )

    scored = []
    for skel in skeletons:
        n_claims = len(skel.get("anchors", {}).get("claim_ids", []))
        n_debates = len(skel.get("anchors", {}).get("debate_ids", []))
        n_papers = len(skel.get("anchors", {}).get("arxiv_ids", []))
        prompt = ATOM_SCORING_PROMPT.format(
            combo=skel["combo"],
            question=skel["question"],
            why_now=skel.get("why_now", skel.get("why_now_skeleton", "")),
            approach=skel.get("approach", skel.get("approach_skeleton", "")),
            n_claims=n_claims,
            n_debates=n_debates,
            n_papers=n_papers,
            existing_ideas_short=existing_short,
        )
        try:
            resp = httpx.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json={"model": settings.ASTRO_SCORER_MODEL, "prompt": prompt, "stream": False,
                      "options": {"temperature": 0.1, "num_predict": 512}, "keep_alive": "1h"},
                timeout=60,
            )
            resp.raise_for_status()
            raw = resp.json().get("response", "")
            json_match = re.search(r"\{[\s\S]*\}", raw)
            if not json_match:
                skel["novelty"] = 0.5
                skel["feasibility"] = 0.5
            else:
                result = json.loads(json_match.group())
                skel["novelty"] = float(result.get("novelty", 0.5))
                skel["feasibility"] = float(result.get("feasibility", 0.5))
                if result.get("duplicates_existing_idea_id"):
                    log.info("Atom flagged %s as dup of idea %s — skipping", skel["combo"], result["duplicates_existing_idea_id"])
                    continue
        except Exception as exc:
            log.warning("Atom scoring failed for %s: %s — using defaults", skel["combo"], exc)
            skel["novelty"] = 0.5
            skel["feasibility"] = 0.5

        if skel["novelty"] < NOVELTY_FLOOR or skel["feasibility"] < FEASIBILITY_FLOOR:
            log.info("Dropped %s (novelty=%.2f feasibility=%.2f)", skel["combo"], skel["novelty"], skel["feasibility"])
            continue

        scored.append(skel)

    return scored


def _persist_ideas(db, page_id: int, ideas: list, run_id: int) -> int:
    from sqlalchemy import text
    inserted = 0
    for skel in ideas:
        why_now = skel.get("why_now", skel.get("why_now_skeleton", ""))
        approach = skel.get("approach", skel.get("approach_skeleton", ""))
        result = db.execute(text("""
            INSERT INTO research_ideas
                (page_id, survey_combo, question, why_now, approach,
                 systematics_json, novelty, feasibility, status,
                 model_chain, generated_by_run_id, seeded)
            VALUES (:pid, :combo, :q, :wn, :ap, :sys, :nov, :feas,
                    'active', :chain, :run_id, FALSE)
            RETURNING id
        """), {
            "pid": page_id,
            "combo": skel["combo"],
            "q": skel["question"],
            "wn": why_now,
            "ap": approach,
            "sys": json.dumps(skel.get("systematics", [])),
            "nov": round(skel["novelty"], 2),
            "feas": round(skel["feasibility"], 2),
            "chain": "rakon→atom-7b",
            "run_id": run_id,
        })
        idea_id = result.fetchone()[0]
        inserted += 1

        # Insert anchors
        anchors = skel.get("anchors", {})
        for claim_id in anchors.get("claim_ids", []):
            try:
                db.execute(text(
                    "INSERT INTO research_idea_anchors (idea_id, kind, ref_id) VALUES (:iid, 'claim', :rid)"
                ), {"iid": idea_id, "rid": str(claim_id)})
            except Exception:
                pass
        for arxiv_id in anchors.get("arxiv_ids", []):
            try:
                db.execute(text(
                    "INSERT INTO research_idea_anchors (idea_id, kind, ref_id) VALUES (:iid, 'arxiv', :rid)"
                ), {"iid": idea_id, "rid": str(arxiv_id)})
            except Exception:
                pass

        # Wire research_idea_surveys
        tokens = [t.strip() for t in skel["combo"].split("+")]
        for token in tokens:
            survey_row = db.execute(text(
                "SELECT id FROM surveys WHERE UPPER(name) = UPPER(:t) OR UPPER(slug) = UPPER(:t)"
            ), {"t": token}).fetchone()
            if survey_row:
                try:
                    db.execute(text(
                        "INSERT INTO research_idea_surveys (idea_id, survey_id) VALUES (:iid, :sid) ON CONFLICT DO NOTHING"
                    ), {"iid": idea_id, "sid": survey_row.id})
                except Exception:
                    pass

    # Supersede old active ideas not re-emitted in this run
    db.execute(text("""
        UPDATE research_ideas
        SET status = 'superseded', updated_at = now()
        WHERE page_id = :pid
          AND status = 'active'
          AND seeded = FALSE
          AND generated_by_run_id != :run_id
    """), {"pid": page_id, "run_id": run_id})

    db.commit()
    return inserted


def _discord_notify(slug: str, inserted: int, generated: int):
    from app.config import settings
    import httpx
    if not getattr(settings, "DISCORD_WEBHOOK_URL", None):
        return
    survival = f"{inserted}/{generated}" if generated else "0/0"
    msg = f"🔬 Research Ideas: regenerated **{slug}** — {survival} ideas survived (inserted {inserted})"
    try:
        httpx.post(settings.DISCORD_WEBHOOK_URL, json={"content": msg}, timeout=10)
    except Exception:
        pass


@shared_task(name="app.agent_loop.research_ideas.tasks.regenerate_top_pages")
def regenerate_top_pages():
    """Nightly batch: regenerate ideas for top flagship pages by debate+paper activity."""
    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    try:
        pages = db.execute(text("""
            SELECT wp.slug
            FROM wiki_pages wp
            LEFT JOIN (
                SELECT page_id, count(*) as debate_count
                FROM claims WHERE claim_type = 'debate'
                GROUP BY page_id
            ) d ON d.page_id = wp.id
            ORDER BY COALESCE(d.debate_count, 0) DESC
            LIMIT 1
        """)).fetchall()
        for page in pages:
            regenerate_research_ideas.delay(page.slug)
    finally:
        db.close()
