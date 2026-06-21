"""auto_improvement.py — Auto Research Improvement Celery tasks (design §2, §3.6, §6)

Jobs implemented here:
  J1  process_lightweight_event  — per-event Nutty generation + refresh (≤8/hr, debounce 1h/page)
  J3  rakon_weekly_promotion_pass — Sunday 03:00 KST; Buddle fallback if Rakon down (Papa Q5)
  J11 coverage_detection_pass    — Tuesday 02:00 KST; TF-IDF pre-filter + Atom-7B
"""
import json
import logging
import datetime
import re

import httpx

from celery import shared_task
from app.config import settings
from app.services.llm_utils import strip_think_blocks
from app.utils.model_guard import guard_batch_model
from app.utils.premium_dispatch import dispatch_premium, log_llm_spend

log = logging.getLogger(__name__)

# ── Model endpoints ────────────────────────────────────────────────────────────
OLLAMA_LOCAL  = settings.OLLAMA_STUDIO_BASE_URL
OLLAMA_MACPRO = settings.OLLAMA_MACPRO_BASE_URL or f"{settings.RAKON_BASE_URL.rstrip('/')}/v1"
OLLAMA_BUDDLE = settings.BUDDLE_BASE_URL.rstrip("/")
if not OLLAMA_BUDDLE.endswith("/v1"):
    OLLAMA_BUDDLE = f"{OLLAMA_BUDDLE}/v1"

MODEL_NUTTY      = settings.OLLAMA_STUDIO_FAST_MODEL          # J1 generate + refresh
MODEL_ATOM       = "vanta-research/atom-astronomy-7b:latest"  # J2, J11 scoring
MODEL_RAKON      = settings.RAKON_MODEL          # J3 primary, 8h timeout
MODEL_BUDDLE     = settings.BUDDLE_MODEL         # J3 fallback / B-lane
MODEL_MIMA       = settings.OLLAMA_STUDIO_HEAVY_MODEL  # M-lane diversity drafter
MODEL_TERA       = settings.ADVERSARIAL_QUERY_MODEL  # T-lane 128k coverage + audit
MODEL_TAKJI      = settings.ADVERSARIAL_SKEPTIC_MODEL  # K-lane methodology gate
MODEL_ASTROSAGE  = "astrosage-70b:latest"      # J4 polish

NUTTY_RATE_LIMIT_PER_HOUR = 8          # Papa Q6
NUTTY_DRAFT_CAP_PER_PAGE  = 5          # §2.2 skip if page has ≥5 drafts
COVERAGE_CONFIDENCE_FLOOR = 0.70       # §3.6 auto-retire floor

RAKON_WEEKLY_TOP_PAGES    = 10         # §2.4
COVERAGE_LOOKBACK_DAYS    = 180        # §3.6
COVERAGE_TFIDF_FLOOR      = 0.55       # §3.6 pre-filter

_RAW_COMBOS = {
    ("JWST", "DESI"), ("JWST", "Euclid"), ("JWST", "ALMA"), ("JWST", "HSC"),
    ("JWST", "LSST"), ("JWST", "VLA"),
    ("DESI", "Euclid"), ("DESI", "HSC"), ("DESI", "ALMA"), ("DESI", "LSST"),
    ("ALMA", "Euclid"), ("ALMA", "HSC"), ("ALMA", "LSST"), ("ALMA", "VLA"),
    ("Euclid", "HSC"), ("Euclid", "LSST"), ("HSC", "LSST"), ("LSST", "VLA"),
}
ALLOWED_COMBOS = {f"{a}+{b}" for a, b in _RAW_COMBOS} | {f"{b}+{a}" for a, b in _RAW_COMBOS}

NOVELTY_FLOOR     = 0.40
FEASIBILITY_FLOOR = 0.30
DEDUP_COSINE_THRESHOLD = 0.75


# ── Redis helpers ──────────────────────────────────────────────────────────────

def _redis():
    import redis as redis_lib
    from app.config import settings
    return redis_lib.from_url(settings.REDIS_URL, decode_responses=True)


def _redis_flag(key: str) -> bool:
    try:
        return _redis().get(key) == "1"
    except Exception:
        return False


def _provenance_enforce_enabled() -> bool:
    mode = (getattr(settings, "AUTOWIKI_PROVENANCE_GATE_MODE", "shadow") or "shadow").strip().lower()
    return mode == "enforce"


def _nutty_rate_check_and_increment() -> bool:
    """Return True if the call is allowed (increments counter). False if over limit."""
    try:
        r = _redis()
        key = "nutty:rate:hourly"
        count = r.incr(key)
        if count == 1:
            r.expire(key, 3600)
        return count <= NUTTY_RATE_LIMIT_PER_HOUR
    except Exception:
        return True  # fail open to avoid blocking on Redis error


def _page_debounce_check(page_id: int, window_seconds: int = 3600) -> bool:
    """Return True if we should proceed (sets debounce key). False if debounced."""
    try:
        r = _redis()
        key = f"research_ideas:debounce:{page_id}"
        result = r.set(key, "1", ex=window_seconds, nx=True)
        return result is True
    except Exception:
        return True


# ── LLM call helpers ───────────────────────────────────────────────────────────

def _ollama_chat(base_url: str, model: str, prompt: str, temperature: float = 0.5, timeout: int = 120) -> str | None:
    try:
        model = guard_batch_model(model, "research_ideas.auto_improvement._ollama_chat")
        est_tokens = max(1, len(prompt) // 4)
        dispatch_premium("research_ideas.ollama_chat", model, est_tokens)
        resp = httpx.post(
            f"{base_url.rstrip('/')}/chat/completions",
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": temperature,
                "stream": False,
            },
            timeout=timeout,
            headers={"Authorization": "Bearer ollama"},
        )
        resp.raise_for_status()
        data = resp.json()
        usage = data.get("usage") or {}
        log_llm_spend(
            "research_ideas.ollama_chat",
            model,
            prompt_tokens=usage.get("prompt_tokens"),
            completion_tokens=usage.get("completion_tokens"),
            estimated_tokens=est_tokens,
        )
        return data["choices"][0]["message"]["content"]
    except Exception as exc:
        log.warning("_ollama_chat %s/%s failed: %s", base_url, model, exc)
        return None


def _parse_json_block(text: str) -> dict | list | None:
    """Extract first JSON object/array from text, tolerating markdown fences."""
    if not text:
        return None
    text = re.sub(r"```(?:json)?\s*", "", text)
    text = re.sub(r"```", "", text)
    text = strip_think_blocks(text)
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        m = re.search(r"\{[\s\S]*\}", text)
        if m:
            try:
                return json.loads(m.group())
            except Exception:
                pass
        m = re.search(r"\[[\s\S]*\]", text)
        if m:
            try:
                return json.loads(m.group())
            except Exception:
                pass
    return None


def _tfidf_cosine(a: str, b: str) -> float:
    """Minimal TF-IDF cosine similarity without heavy deps."""
    import math
    def tokenize(s):
        return re.findall(r"[a-z0-9]+", s.lower())
    def tf(tokens):
        d = {}
        for t in tokens:
            d[t] = d.get(t, 0) + 1
        total = len(tokens) or 1
        return {t: c / total for t, c in d.items()}
    ta, tb = tokenize(a), tokenize(b)
    tfa, tfb = tf(ta), tf(tb)
    vocab = set(tfa) | set(tfb)
    if not vocab:
        return 0.0
    dot = sum(tfa.get(t, 0) * tfb.get(t, 0) for t in vocab)
    na  = math.sqrt(sum(v**2 for v in tfa.values()))
    nb  = math.sqrt(sum(v**2 for v in tfb.values()))
    if na * nb == 0:
        return 0.0
    return dot / (na * nb)


# ── Discord helper ─────────────────────────────────────────────────────────────

def _discord(msg: str) -> None:
    try:
        from app.config import settings
        url = settings.NM_DISCORD_WEBHOOK_URL if hasattr(settings, "NM_DISCORD_WEBHOOK_URL") else settings.DISCORD_WEBHOOK_URL
        if not url:
            return
        httpx.post(url, json={"content": msg[:2000]}, timeout=8)
    except Exception as exc:
        log.debug("Discord notify failed: %s", exc)


# ── Context builder ────────────────────────────────────────────────────────────

def _build_page_context(db, page_id: int, full: bool = False, max_arxiv: int = 15) -> dict | None:
    """Build page context dict for LLM prompts.
    full=True: include page.content, all claims (no LIMIT), and up to max_arxiv papers (default 30).
    """
    from sqlalchemy import text
    page = db.execute(
        text("SELECT id, slug, title, hero_tagline, content FROM wiki_pages WHERE id = :pid"),
        {"pid": page_id},
    ).fetchone()
    if not page:
        return None

    claim_limit = "" if full else " LIMIT 10"
    claims = db.execute(text(
        "SELECT id, text, trust_level FROM claims WHERE page_id = :pid"
        " ORDER BY CASE trust_level WHEN 'consensus' THEN 1 WHEN 'accepted' THEN 2"
        f" WHEN 'debated' THEN 3 ELSE 4 END{claim_limit}"
    ), {"pid": page_id}).fetchall()

    debates = db.execute(text(
        "SELECT id, text, trust_level FROM claims WHERE page_id = :pid AND trust_level = 'debated'"
    ), {"pid": page_id}).fetchall()

    cutoff_str = (datetime.datetime.utcnow() - datetime.timedelta(days=90)).strftime("%Y-%m-%d")
    arxiv = db.execute(text(
        f"SELECT arxiv_id, title, abstract FROM arxiv_papers"
        f" WHERE related_pages::jsonb ? :slug"
        f" AND submitted >= :cut"
        f" ORDER BY submitted DESC LIMIT {max_arxiv}"
    ), {"slug": page.slug, "cut": cutoff_str}).fetchall()

    existing_ideas = db.execute(text(
        "SELECT id, survey_combo, question, why_now, approach, status"
        " FROM research_ideas WHERE page_id = :pid AND status IN ('draft','active','saved')"
    ), {"pid": page_id}).fetchall()

    idea_anchors = {}
    if existing_ideas:
        ids = tuple(r.id for r in existing_ideas)
        if ids:
            placeholders = ",".join(str(i) for i in ids)
            anchor_rows = db.execute(text(
                f"SELECT idea_id, kind, ref_id FROM research_idea_anchors WHERE idea_id IN ({placeholders})"
            )).fetchall()
            for a in anchor_rows:
                idea_anchors.setdefault(a.idea_id, []).append({"kind": a.kind, "ref_id": str(a.ref_id)})

    return {
        "page_id":    page.id,
        "slug":       page.slug,
        "title":      page.title,
        "tagline":    page.hero_tagline or "",
        "content":    page.content or "",
        "claims":     [{"id": c.id, "text": c.text, "trust": c.trust_level} for c in claims],
        "debates":    [{"id": c.id, "text": c.text} for c in debates],
        "arxiv":      [{"arxiv_id": a.arxiv_id, "title": a.title, "abstract": (a.abstract or "")[:400]} for a in arxiv],
        "ideas":      [{"id": r.id, "combo": r.survey_combo, "question": r.question,
                        "why_now": r.why_now, "approach": r.approach, "status": r.status,
                        "anchors": idea_anchors.get(r.id, [])} for r in existing_ideas],
    }


# ── J1: per-event lightweight pipeline ─────────────────────────────────────────

NUTTY_GENERATE_PROMPT = """\
You are an astronomy research strategist generating SHORT-FORM research ideas.

WIKI PAGE
---------
Title: {title}
Slug: {slug}
Tagline: {tagline}

TRIGGER
-------
{trigger_kind} just fired. Context:
{trigger_context}

TOP CLAIMS (by trust):
{claims_block}

ACTIVE DEBATES:
{debates_block}

RECENT LITERATURE (last 90d):
{arxiv_block}

EXISTING IDEAS ON THIS PAGE (do NOT duplicate):
{existing_ideas_block}

ALLOWED SURVEY COMBOS (use exactly two):
JWST+DESI, JWST+Euclid, JWST+ALMA, JWST+HSC, JWST+LSST, JWST+VLA,
DESI+Euclid, DESI+HSC, DESI+ALMA, DESI+LSST,
ALMA+Euclid, ALMA+HSC, ALMA+LSST, ALMA+VLA,
Euclid+HSC, Euclid+LSST, HSC+LSST, LSST+VLA

OUTPUT — strict JSON, NO prose. Generate 3 candidate ideas (or fewer if quality dictates):
{{
  "skeletons": [
    {{
      "combo": "JWST+DESI",
      "question": "<1-sentence research question, falsifiable>",
      "why_now": "<1-2 sentences anchored to the trigger>",
      "approach": "<2-3 sentences: data, cuts, measurement, expected N>",
      "anchors": {{
        "claim_ids": [],
        "debate_ids": [],
        "arxiv_ids": []
      }}
    }}
  ]
}}

CONSTRAINTS:
- Each question MUST be answerable only by combining the two named surveys.
- Each question MUST reference at least 1 claim_id OR 1 debate_id.
- No vague verbs ("understand", "explore"); use "measure", "constrain", "test whether", "rule out".
- Quality over quota — emit 1 good idea rather than 3 weak ones.
"""

NUTTY_REFRESH_PROMPT = """\
You are updating an existing research idea in response to new evidence.

EXISTING IDEA (preserve question unless scope materially expands)
-----------------------------------------------------------------
Question:  {question}
Why now:   {why_now}
Approach:  {approach}
Anchors:   {anchors_summary}

WIKI PAGE: {title} — {tagline}

NEW EVIDENCE
------------
Kind:      {trigger_kind}
Reference: {trigger_ref_summary}

TASK:
1. Decide: STRENGTHENS, COMPLICATES, or TANGENTIAL.
2. If STRENGTHENS or COMPLICATES, rewrite why_now (2-3 sentences) citing the new evidence.
3. If STRENGTHENS, optionally update approach only if data availability changes.
4. Only edit question if scope materially expands. Default: keep verbatim.
5. If TANGENTIAL, return {{"action": "skip"}}.

OUTPUT JSON:
{{
  "action": "refresh" | "skip",
  "verdict": "strengthens" | "complicates" | "tangential",
  "question": "<usually unchanged>",
  "why_now": "<rewritten>",
  "approach": "<rewritten or unchanged>",
  "rationale": "<one sentence for the audit log>"
}}
"""

ATOM_SCORE_PROMPT = """\
You are scoring an astronomy research idea for novelty and feasibility.

IDEA
----
Survey combo: {combo}
Question: {question}
Why now: {why_now}
Approach: {approach}

EXISTING IDEAS ON THIS PAGE (for dedup check):
{existing_block}

Respond with ONLY valid JSON:
{{
  "novelty": <0.0-1.0; 0 = already done, 1 = completely unexplored>,
  "feasibility": <0.0-1.0; 0 = impossible today, 1 = trivially doable>,
  "dedup_cosine_estimate": <0.0-1.0; estimated similarity to most-similar existing idea>
}}
"""


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.process_lightweight_event", bind=True, max_retries=2)
def process_lightweight_event(self, page_id: int, trigger: str, cause_id: str | None = None):
    """J1 — per-event Nutty pipeline: refresh existing drafts, then generate new candidates."""
    if _provenance_enforce_enabled():
        return {
            "skipped": "provenance_enforce_suppressed_research_ideas_lightweight",
            "page_id": page_id,
        }
    log.warning("[J1] ENTRY page_id=%d trigger=%s cause_id=%s retry=%d", page_id, trigger, cause_id, self.request.retries)
    if not _nutty_rate_check_and_increment():
        log.info("[J1] rate limit hit (>%d/hr), skipping page_id=%d trigger=%s", NUTTY_RATE_LIMIT_PER_HOUR, page_id, trigger)
        return {"skipped": "rate_limited"}

    if not _page_debounce_check(page_id, window_seconds=3600):
        log.info("[J1] debounced page_id=%d trigger=%s", page_id, trigger)
        return {"skipped": "debounced"}

    from app.database import SessionLocal
    from sqlalchemy import text

    db = SessionLocal()
    try:
        ctx = _build_page_context(db, page_id)
        if not ctx:
            log.warning("[J1] page_id=%d not found", page_id)
            return {"error": "page_not_found"}

        drafts_count = sum(1 for i in ctx["ideas"] if i["status"] == "draft")

        # ── REFRESH PATH ──────────────────────────────────────────────────────
        refreshed = 0
        trigger_ref_summary = _build_trigger_ref_summary(db, trigger, cause_id)

        for idea in ctx["ideas"]:
            if _anchors_overlap(idea["anchors"], trigger, cause_id):
                result = _run_nutty_refresh(idea, ctx, trigger, trigger_ref_summary)
                if result and result.get("action") == "refresh":
                    _apply_idea_refresh(db, idea["id"], result, trigger, cause_id)
                    refreshed += 1

        # ── GENERATE PATH ─────────────────────────────────────────────────────
        generated = 0
        if drafts_count < NUTTY_DRAFT_CAP_PER_PAGE:
            skeletons = _run_nutty_generate(ctx, trigger, trigger_ref_summary)
            for skel in (skeletons or []):
                if not _validate_skeleton(skel):
                    continue
                score = _atom_score(skel, ctx["ideas"])
                if score is None:
                    continue
                if score["novelty"] < NOVELTY_FLOOR or score["feasibility"] < FEASIBILITY_FLOOR:
                    continue
                if score.get("dedup_cosine_estimate", 0) >= DEDUP_COSINE_THRESHOLD:
                    continue
                _persist_draft(db, page_id, skel, score, trigger, cause_id)
                generated += 1

        _log_autowiki_run(db, page_id, "research_ideas_lightweight",
                          refreshed_count=refreshed, generated_count=generated)
        db.commit()
        log.info("[J1] page_id=%d trigger=%s refreshed=%d generated=%d", page_id, trigger, refreshed, generated)
        return {"page_id": page_id, "trigger": trigger, "refreshed": refreshed, "generated": generated}

    except Exception as exc:
        db.rollback()
        log.error("[J1] FAILED page_id=%d retry=%d/2: %s", page_id, self.request.retries, exc)
        raise self.retry(exc=exc, countdown=300)
    finally:
        db.close()


def _build_trigger_ref_summary(db, trigger: str, cause_id: str | None) -> str:
    if not cause_id:
        return f"trigger={trigger}"
    try:
        from sqlalchemy import text
        if trigger == "claim_inserted":
            row = db.execute(text("SELECT text FROM claims WHERE id = :id"), {"id": int(cause_id)}).fetchone()
            return f"New claim: {row.text[:300]}" if row else f"claim_id={cause_id}"
        if trigger == "new_arxiv":
            row = db.execute(text("SELECT title, abstract FROM arxiv_papers WHERE arxiv_id = :id"), {"id": cause_id}).fetchone()
            return f"arXiv {cause_id}: {row.title}" if row else f"arxiv_id={cause_id}"
    except Exception:
        pass
    return f"trigger={trigger}, ref={cause_id}"


def _anchors_overlap(anchors: list, trigger: str, cause_id: str | None) -> bool:
    if not cause_id or not anchors:
        return False
    for a in anchors:
        if trigger in ("claim_inserted", "evidence_linked") and a["kind"] == "claim" and str(a["ref_id"]) == str(cause_id):
            return True
        if trigger == "new_arxiv" and a["kind"] == "arxiv" and a["ref_id"] == cause_id:
            return True
    return False


def _run_nutty_refresh(idea: dict, ctx: dict, trigger: str, trigger_ref_summary: str) -> dict | None:
    try:
        anchors_summary = f"{len(idea['anchors'])} anchors"
        prompt = NUTTY_REFRESH_PROMPT.format(
            question=idea["question"],
            why_now=idea["why_now"],
            approach=idea["approach"],
            anchors_summary=anchors_summary,
            title=ctx["title"],
            tagline=ctx["tagline"],
            trigger_kind=trigger,
            trigger_ref_summary=trigger_ref_summary[:500],
        )
        raw = _ollama_chat(OLLAMA_LOCAL, MODEL_NUTTY, prompt, temperature=0.3, timeout=120)
        if not raw:
            log.warning("[J1] Nutty refresh returned empty for idea=%d trigger=%s", idea.get("id"), trigger)
            return None
        return _parse_json_block(raw)
    except Exception as exc:
        log.warning("[J1] Nutty refresh failed for idea=%d trigger=%s: %s", idea.get("id"), trigger, exc)
        return None


def _apply_idea_refresh(db, idea_id: int, result: dict, trigger: str, cause_id: str | None):
    from sqlalchemy import text
    old = db.execute(text("SELECT question, why_now, approach FROM research_ideas WHERE id = :id"), {"id": idea_id}).fetchone()
    if not old:
        return
    db.execute(text("""
        INSERT INTO research_idea_refresh_log
          (idea_id, trigger_kind, trigger_ref_id, model_chain,
           old_question, old_why_now, old_approach,
           new_question, new_why_now, new_approach)
        VALUES (:iid, :tk, :tref, :mc, :oq, :ow, :oa, :nq, :nw, :na)
    """), {
        "iid":  idea_id,
        "tk":   trigger,
        "tref": cause_id,
        "mc":   "nutty",
        "oq":   old.question,
        "ow":   old.why_now,
        "oa":   old.approach,
        "nq":   result.get("question") or old.question,
        "nw":   result.get("why_now") or old.why_now,
        "na":   result.get("approach") or old.approach,
    })
    db.execute(text("""
        UPDATE research_ideas
        SET question         = :q,
            why_now          = :w,
            approach         = :a,
            last_refreshed_at = NOW(),
            refresh_count    = COALESCE(refresh_count, 0) + 1,
            updated_at       = NOW()
        WHERE id = :id
    """), {
        "q":  result.get("question") or old.question,
        "w":  result.get("why_now") or old.why_now,
        "a":  result.get("approach") or old.approach,
        "id": idea_id,
    })


def _run_nutty_generate(ctx: dict, trigger: str, trigger_ref_summary: str) -> list:
    try:
        claims_block = "\n".join(f"[{c['id']}] ({c['trust']}) {c['text'][:200]}" for c in ctx["claims"])
        debates_block = "\n".join(f"[{d['id']}] {d['text'][:200]}" for d in ctx["debates"]) or "(none)"
        arxiv_block = "\n".join(f"[{a['arxiv_id']}] {a['title']}: {a['abstract'][:300]}" for a in ctx["arxiv"]) or "(none)"
        existing_block = "\n".join(f"- [{i['combo']}] {i['question'][:150]}" for i in ctx["ideas"]) or "(none)"

        prompt = NUTTY_GENERATE_PROMPT.format(
            title=ctx["title"],
            slug=ctx["slug"],
            tagline=ctx["tagline"],
            trigger_kind=trigger,
            trigger_context=trigger_ref_summary[:600],
            claims_block=claims_block[:1500],
            debates_block=debates_block[:800],
            arxiv_block=arxiv_block[:1500],
            existing_ideas_block=existing_block[:800],
        )
        raw = _ollama_chat(OLLAMA_LOCAL, MODEL_NUTTY, prompt, temperature=0.5, timeout=120)
        if not raw:
            log.warning("[J1] Nutty generate returned empty page=%d trigger=%s", ctx.get("page_id"), trigger)
            return []
        parsed = _parse_json_block(raw)
        if isinstance(parsed, dict):
            return parsed.get("skeletons", [])
        return []
    except Exception as exc:
        log.warning("[J1] Nutty generate failed page=%d trigger=%s: %s", ctx.get("page_id"), trigger, exc)
        return []


def _validate_skeleton(skel: dict) -> bool:
    if not isinstance(skel, dict):
        return False
    if skel.get("combo") not in ALLOWED_COMBOS:
        return False
    from app.config import settings
    if settings.RESEARCH_IDEAS_COMBO_WHITELIST:
        whitelist = {x.strip() for x in settings.RESEARCH_IDEAS_COMBO_WHITELIST.split(",") if x.strip()}
        if skel.get("combo") not in whitelist:
            return False
    for field in ("question", "why_now", "approach"):
        if not skel.get(field):
            return False
    anchors = skel.get("anchors", {})
    if not (anchors.get("claim_ids") or anchors.get("debate_ids")):
        return False
    return True


def _atom_score(skel: dict, existing_ideas: list) -> dict | None:
    existing_block = "\n".join(f"- {i['question'][:150]}" for i in existing_ideas) or "(none)"
    prompt = ATOM_SCORE_PROMPT.format(
        combo=skel.get("combo", ""),
        question=skel.get("question", ""),
        why_now=skel.get("why_now", ""),
        approach=skel.get("approach", ""),
        existing_block=existing_block[:1000],
    )
    raw = _ollama_chat(OLLAMA_LOCAL, MODEL_ATOM, prompt, temperature=0.1, timeout=60)
    if not raw:
        return None
    result = _parse_json_block(raw)
    if not isinstance(result, dict):
        return None
    return result


def _persist_draft(db, page_id: int, skel: dict, score: dict, trigger: str, cause_id: str | None):
    from sqlalchemy import text
    row = db.execute(text("""
        INSERT INTO research_ideas
          (page_id, survey_combo, question, why_now, approach,
           novelty, feasibility, status, model_chain, seeded)
        VALUES (:pid, :combo, :q, :w, :a, :n, :f, 'draft', 'nutty→atom-7b', FALSE)
        RETURNING id
    """), {
        "pid":   page_id,
        "combo": skel["combo"],
        "q":     skel["question"],
        "w":     skel["why_now"],
        "a":     skel["approach"],
        "n":     min(max(float(score.get("novelty", 0.5)), 0), 1),
        "f":     min(max(float(score.get("feasibility", 0.5)), 0), 1),
    }).fetchone()
    if not row:
        return
    idea_id = row.id

    # insert anchors — normalize ref values; Nutty occasionally returns
    # nested lists like [[1494]] which str() encodes as "[1494]", breaking
    # the ::int cast in _compute_idea_signals.
    def _norm_ref(v) -> str:
        if isinstance(v, (list, tuple)):
            v = v[0] if v else ""
        return str(v)

    anchors = skel.get("anchors", {})
    for cid in (anchors.get("claim_ids") or []):
        nested = db.begin_nested()
        try:
            db.execute(text(
                "INSERT INTO research_idea_anchors (idea_id, kind, ref_id) VALUES (:iid, 'claim', :ref)"
                " ON CONFLICT DO NOTHING"
            ), {"iid": idea_id, "ref": _norm_ref(cid)})
            nested.commit()
        except Exception:
            nested.rollback()
    for did in (anchors.get("debate_ids") or []):
        nested = db.begin_nested()
        try:
            db.execute(text(
                "INSERT INTO research_idea_anchors (idea_id, kind, ref_id) VALUES (:iid, 'debate', :ref)"
                " ON CONFLICT DO NOTHING"
            ), {"iid": idea_id, "ref": _norm_ref(did)})
            nested.commit()
        except Exception:
            nested.rollback()
    for aid in (anchors.get("arxiv_ids") or []):
        nested = db.begin_nested()
        try:
            db.execute(text(
                "INSERT INTO research_idea_anchors (idea_id, kind, ref_id) VALUES (:iid, 'arxiv', :ref)"
                " ON CONFLICT DO NOTHING"
            ), {"iid": idea_id, "ref": _norm_ref(aid)})
            nested.commit()
        except Exception:
            nested.rollback()

    # wire survey join
    for token in [t.strip() for t in skel["combo"].split("+")]:
        survey_row = db.execute(
            text("SELECT id FROM surveys WHERE UPPER(name) = UPPER(:t) OR UPPER(slug) = UPPER(:t)"),
            {"t": token},
        ).fetchone()
        if survey_row:
            nested = db.begin_nested()
            try:
                db.execute(text(
                    "INSERT INTO research_idea_surveys (idea_id, survey_id) VALUES (:iid, :sid)"
                    " ON CONFLICT DO NOTHING"
                ), {"iid": idea_id, "sid": survey_row.id})
                nested.commit()
            except Exception:
                nested.rollback()
        else:
            _log_orphan(db, token, idea_id)


def _log_orphan(db, token: str, idea_id: int):
    from sqlalchemy import text
    nested = db.begin_nested()
    try:
        db.execute(text("""
            INSERT INTO surveys_orphans (raw_token, idea_id, occurrence_count)
            VALUES (:tok, :iid, 1)
            ON CONFLICT (raw_token) DO UPDATE
            SET occurrence_count = surveys_orphans.occurrence_count + 1,
                last_seen_at = NOW(),
                idea_id = EXCLUDED.idea_id
        """), {"tok": token, "iid": idea_id})
        # ping Discord if threshold crossed
        row = db.execute(text(
            "SELECT occurrence_count FROM surveys_orphans WHERE raw_token = :tok"
        ), {"tok": token}).fetchone()
        if row and row.occurrence_count == 3:
            _discord(f"⚠️ 3 ideas referenced unknown survey `{token}` — consider adding it to the directory.")
        nested.commit()
    except Exception as exc:
        nested.rollback()
        log.debug("_log_orphan failed: %s", exc)


def _log_autowiki_run(db, page_id: int, kind: str, **metrics):
    from sqlalchemy import text
    try:
        extra = json.dumps(metrics)
        nested = db.begin_nested()
        try:
            db.execute(text("""
                INSERT INTO autowiki_runs (page_id, started_at, finished_at, proposal_type, model_proposer, decision, idea_signals_json)
                VALUES (:pid, NOW(), NOW(), :kind, 'nutty→atom-7b', 'completed', :extra)
            """), {"pid": page_id, "kind": kind, "extra": extra})
            nested.commit()
        except Exception as exc:
            nested.rollback()
            log.debug("_log_autowiki_run failed: %s", exc)
    except Exception as exc:
        log.debug("_log_autowiki_run savepoint failed: %s", exc)


# ── J3: Rakon weekly promotion pass ───────────────────────────────────────────

RAKON_PROMOTION_PROMPT = """\
You are a senior astronomy research strategist curating a research-idea pool for a wiki page.

WIKI PAGE: {title}
Tagline: {tagline}

EXISTING DRAFT IDEAS (your job: decide which to promote, not generate new ones unless the pool is empty):
{drafts_block}

ACTIVE IDEAS ALREADY PROMOTED (for dedup — do not re-emit these):
{active_block}

TOP CLAIMS:
{claims_block}

RECENT LITERATURE (last 90 days):
{arxiv_block}

TASK: Emit up to 12 high-quality candidates. For each, decide:
- If it closely matches an existing draft (same question axis), emit it with "draft_match_id": <idea_id>.
  This promotes the draft to active. Rakon's candidate is dropped; the matched draft is promoted.
- If it's a genuinely new idea not in the draft pool, emit it without draft_match_id.

OUTPUT JSON:
{{
  "candidates": [
    {{
      "combo": "JWST+DESI",
      "question": "<1-sentence, falsifiable>",
      "why_now": "<1-2 sentences>",
      "approach": "<2-3 sentences>",
      "anchors": {{"claim_ids": [], "debate_ids": [], "arxiv_ids": []}},
      "draft_match_id": <int or null>
    }}
  ]
}}
"""


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.rakon_weekly_promotion_pass", bind=True, max_retries=0)
def rakon_weekly_promotion_pass(self):
    """J3 — Sunday 03:00 KST weekly heavy pass. Rakon primary; Buddle fallback (Papa Q5)."""
    from app.database import SessionLocal
    from app.config import settings
    from sqlalchemy import text

    db = SessionLocal()
    promoted = 0
    inserted = 0
    model_used = None

    try:
        # Select top-10 pages by draft_count + debate_count + recent_arxiv
        pages = db.execute(text("""
            SELECT wp.id, wp.slug, wp.title, wp.hero_tagline,
                   COUNT(DISTINCT ri.id) FILTER (WHERE ri.status='draft') AS draft_count,
                   COUNT(DISTINCT c.id)  FILTER (WHERE c.trust_level='debated') AS debate_count
            FROM wiki_pages wp
            LEFT JOIN research_ideas ri ON ri.page_id = wp.id
            LEFT JOIN claims c ON c.page_id = wp.id
            GROUP BY wp.id, wp.slug, wp.title, wp.hero_tagline
            ORDER BY draft_count + debate_count DESC
            LIMIT :n
        """), {"n": RAKON_WEEKLY_TOP_PAGES}).fetchall()

        if not pages:
            log.info("[J3] no pages to process")
            return {"promoted": 0, "inserted": 0}

        # Determine model: try Rakon, fall back to Buddle
        rakon_alive = _check_ollama_alive(OLLAMA_MACPRO, MODEL_RAKON)
        if rakon_alive:
            skeleton_base_url = OLLAMA_MACPRO
            skeleton_model    = MODEL_RAKON
            model_chain       = "rakon→astrosage-70b→atom-7b"
            fallback_reason   = None
            model_used        = "rakon"
        else:
            log.warning("[J3] Rakon unreachable — falling back to Buddle (Papa Q5)")
            skeleton_base_url = OLLAMA_BUDDLE
            skeleton_model    = MODEL_BUDDLE
            model_chain       = "buddle→astrosage-70b→atom-7b"
            fallback_reason   = "rakon_unavailable"
            model_used        = "buddle"
            _discord("⚠️ J3: Rakon unavailable — Sunday pass falling back to Buddle on Mac Studio.")

        promoted_by_label = "rakon_weekly" if model_used == "rakon" else "buddle_weekly"

        for page in pages:
            ctx = _build_page_context(db, page.id)
            if not ctx:
                continue

            drafts   = [i for i in ctx["ideas"] if i["status"] == "draft"]
            active   = [i for i in ctx["ideas"] if i["status"] in ("active", "saved")]
            claims   = ctx["claims"]
            arxiv    = ctx["arxiv"]

            drafts_block  = "\n".join(f"[id={d['id']}] [{d['combo']}] {d['question'][:200]}" for d in drafts) or "(none)"
            active_block  = "\n".join(f"[{a['combo']}] {a['question'][:200]}" for a in active) or "(none)"
            claims_block  = "\n".join(f"[{c['id']}] ({c['trust']}) {c['text'][:200]}" for c in claims) or "(none)"
            arxiv_block   = "\n".join(f"[{a['arxiv_id']}] {a['title']}: {a['abstract'][:300]}" for a in arxiv) or "(none)"

            prompt = RAKON_PROMOTION_PROMPT.format(
                title=page.title,
                tagline=page.hero_tagline or "",
                drafts_block=drafts_block[:3000],
                active_block=active_block[:1500],
                claims_block=claims_block[:1500],
                arxiv_block=arxiv_block[:1500],
            )

            _j3_timeout = 28800 if skeleton_model == MODEL_RAKON else 1800
            raw = _ollama_chat(skeleton_base_url, skeleton_model, prompt, temperature=0.4, timeout=_j3_timeout)
            if not raw:
                log.warning("[J3] skeleton call returned nothing for page %s", page.slug)
                continue

            parsed = _parse_json_block(raw)
            candidates = (parsed or {}).get("candidates", []) if isinstance(parsed, dict) else []

            for cand in candidates:
                draft_match_id = cand.get("draft_match_id")
                if draft_match_id:
                    # promote the matched draft
                    db.execute(text("""
                        UPDATE research_ideas
                        SET status       = 'active',
                            promoted_at  = NOW(),
                            promoted_by  = :pby,
                            model_chain  = :mc,
                            updated_at   = NOW()
                        WHERE id = :id AND status = 'draft'
                    """), {"id": draft_match_id, "pby": promoted_by_label, "mc": model_chain})
                    promoted += 1
                else:
                    # new idea from Rakon — validate + score before inserting as active
                    if not _validate_skeleton(cand):
                        continue
                    score = _atom_score(cand, ctx["ideas"])
                    if score is None:
                        continue
                    if score["novelty"] < NOVELTY_FLOOR or score["feasibility"] < FEASIBILITY_FLOOR:
                        continue
                    _persist_active_idea(db, page.id, cand, score, promoted_by_label, model_chain)
                    inserted += 1

        _log_autowiki_run(db, 0, "research_ideas_weekly",
                          promoted_count=promoted, inserted_count=inserted,
                          model_used=model_used, fallback_reason=fallback_reason)
        db.commit()

        _discord(f"✅ J3 weekly pass complete — promoted={promoted} new_active={inserted} model={model_used}")
        return {"promoted": promoted, "inserted": inserted, "model_used": model_used}

    except Exception as exc:
        db.rollback()
        log.exception("[J3] rakon_weekly_promotion_pass failed: %s", exc)
        raise
    finally:
        db.close()


def _check_ollama_alive(base_url: str, model: str) -> bool:
    try:
        r = httpx.get(f"{base_url.rstrip('/v1').rstrip('/')}/api/ps", timeout=10)
        if r.status_code != 200:
            return False
        loaded = {m.get("name") or m.get("model") for m in r.json().get("models", [])}
        # also try a tiny ping
        if model not in loaded:
            # attempt keep-alive to load
            httpx.post(
                f"{base_url.rstrip('/v1').rstrip('/')}/api/generate",
                json={"model": model, "keep_alive": "1m", "prompt": "ping", "options": {"num_predict": 1}},
                timeout=30,
            )
        return True
    except Exception:
        return False


def _rakon_prewarm(max_wait: int = 1800) -> bool:
    """Block until Rakon (671b) is loaded in Ollama, up to max_wait seconds.

    On cold start the 404GB model can take 10-20 minutes to load.  The 30s
    ping in _check_ollama_alive is not enough; this function sends a 1-token
    generation request with a long timeout so we actually wait for it.
    """
    base = OLLAMA_MACPRO.rstrip("/v1").rstrip("/")
    try:
        r = httpx.get(f"{base}/api/ps", timeout=10)
        if r.status_code == 200:
            loaded = {m.get("name") or m.get("model") for m in r.json().get("models", [])}
            if MODEL_RAKON in loaded:
                return True
    except Exception:
        return False

    log.info("[rakon_prewarm] Rakon not loaded — warming up (max_wait=%ds)", max_wait)
    try:
        httpx.post(
            f"{base}/api/generate",
            json={"model": MODEL_RAKON, "keep_alive": "4h", "prompt": "ping", "options": {"num_predict": 1}},
            timeout=max_wait,
        )
    except Exception as exc:
        log.warning("[rakon_prewarm] warm-up failed: %s", exc)
        return False

    # Confirm it's now in the loaded set
    try:
        r = httpx.get(f"{base}/api/ps", timeout=10)
        if r.status_code == 200:
            loaded = {m.get("name") or m.get("model") for m in r.json().get("models", [])}
            return MODEL_RAKON in loaded
    except Exception:
        pass
    return False


def _persist_active_idea(db, page_id: int, skel: dict, score: dict, promoted_by: str, model_chain: str):
    from sqlalchemy import text
    row = db.execute(text("""
        INSERT INTO research_ideas
          (page_id, survey_combo, question, why_now, approach,
           novelty, feasibility, status, model_chain, seeded, promoted_at, promoted_by)
        VALUES (:pid, :combo, :q, :w, :a, :n, :f, 'active', :mc, FALSE, NOW(), :pby)
        RETURNING id
    """), {
        "pid":   page_id,
        "combo": skel["combo"],
        "q":     skel["question"],
        "w":     skel["why_now"],
        "a":     skel["approach"],
        "n":     min(max(float(score.get("novelty", 0.5)), 0), 1),
        "f":     min(max(float(score.get("feasibility", 0.5)), 0), 1),
        "mc":    model_chain,
        "pby":   promoted_by,
    }).fetchone()
    if not row:
        return
    idea_id = row.id
    anchors = skel.get("anchors", {})
    for cid in (anchors.get("claim_ids") or []):
        try:
            db.execute(text(
                "INSERT INTO research_idea_anchors (idea_id, kind, ref_id) VALUES (:iid, 'claim', :ref)"
                " ON CONFLICT DO NOTHING"
            ), {"iid": idea_id, "ref": str(cid)})
        except Exception:
            pass


# ── J11: weekly coverage detection ─────────────────────────────────────────────

ATOM_COVERAGE_PROMPT = """\
You are determining whether an astronomy paper directly addresses a posed research question.

RESEARCH QUESTION
-----------------
{question}

CONTEXT
-------
Why posed: {why_now}
Proposed approach: {approach}
Survey combo: {combo}

CANDIDATE PAPER
---------------
Title:     {paper_title}
Abstract:  {paper_abstract}
arXiv ID:  {arxiv_id}

CLASSIFY (be conservative — false positives retire a still-valuable idea):

answers_question:
  "fully"   — paper measures the exact quantity proposed, on the same data combination, concludes the question
  "partial" — related measurement but doesn't close the question
  "no"      — same topic but doesn't address THIS question

confidence: 0.0-1.0

OUTPUT JSON:
{{
  "answers_question": "fully" | "partial" | "no",
  "confidence": <float>,
  "one_line_rationale": "<plain text>"
}}
"""


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.coverage_detection_pass", bind=True, max_retries=0)
def coverage_detection_pass(self):
    """J11 — Tuesday 02:00 KST: TF-IDF pre-filter + Atom-7B coverage classifier."""
    from app.database import SessionLocal
    from sqlalchemy import text

    db = SessionLocal()
    scheduled = 0
    dropped   = 0

    try:
        ideas = db.execute(text("""
            SELECT ri.id, ri.survey_combo, ri.question, ri.why_now, ri.approach, ri.page_id
            FROM research_ideas ri
            WHERE ri.status IN ('draft', 'active', 'saved')
              AND ri.covered_by_arxiv_id IS NULL
        """)).fetchall()

        cutoff_str = (datetime.datetime.utcnow() - datetime.timedelta(days=COVERAGE_LOOKBACK_DAYS)).strftime("%Y-%m-%d")

        for idea in ideas:
            survey_names = [t.strip() for t in idea.survey_combo.split("+")]

            # scope arxiv papers to this idea's page + survey mentions
            papers = db.execute(text("""
                SELECT ap.arxiv_id, ap.title, ap.abstract
                FROM arxiv_papers ap
                WHERE ap.related_pages::jsonb ? (SELECT slug FROM wiki_pages WHERE id = :pid)
                  AND ap.submitted >= :cut
            """), {"pid": idea.page_id, "cut": cutoff_str}).fetchall()

            idea_text = f"{idea.question} {idea.why_now} {idea.approach}"

            for paper in papers:
                if not paper.abstract:
                    continue
                # TF-IDF pre-filter
                paper_text = f"{paper.title} {paper.abstract}"
                cosine = _tfidf_cosine(idea_text, paper_text)
                if cosine < COVERAGE_TFIDF_FLOOR:
                    continue

                prompt = ATOM_COVERAGE_PROMPT.format(
                    question=idea.question,
                    why_now=idea.why_now,
                    approach=idea.approach,
                    combo=idea.survey_combo,
                    paper_title=paper.title or "",
                    paper_abstract=(paper.abstract or "")[:800],
                    arxiv_id=paper.arxiv_id,
                )
                raw = _ollama_chat(OLLAMA_LOCAL, MODEL_ATOM, prompt, temperature=0.1, timeout=60)
                result = _parse_json_block(raw) if raw else None
                if not isinstance(result, dict):
                    continue

                answers = result.get("answers_question", "no")
                confidence = float(result.get("confidence", 0))
                rationale  = result.get("one_line_rationale", "")

                if answers == "fully" and confidence >= COVERAGE_CONFIDENCE_FLOOR:
                    retire_after = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
                    try:
                        db.execute(text("""
                            INSERT INTO research_idea_coverage_candidates
                              (idea_id, arxiv_id, answers_kind, confidence, rationale, status, retire_after)
                            VALUES (:iid, :aid, :ak, :conf, :rat, 'pending', :ra)
                            ON CONFLICT (idea_id, arxiv_id) DO NOTHING
                        """), {
                            "iid":  idea.id,
                            "aid":  paper.arxiv_id,
                            "ak":   "fully",
                            "conf": confidence,
                            "rat":  rationale[:500],
                            "ra":   retire_after,
                        })
                        scheduled += 1
                        _discord(
                            f"📖 Atom-7B: idea #{idea.id} may be covered by arXiv:{paper.arxiv_id} "
                            f"(confidence={confidence:.2f}). Auto-retires in 24h. Reply `!keep {idea.id}` to override."
                        )
                    except Exception:
                        pass

                elif answers in ("fully", "partial") and confidence >= 0.50:
                    try:
                        db.execute(text("""
                            INSERT INTO research_idea_coverage_candidates
                              (idea_id, arxiv_id, answers_kind, confidence, rationale, status)
                            VALUES (:iid, :aid, :ak, :conf, :rat, 'pending')
                            ON CONFLICT (idea_id, arxiv_id) DO NOTHING
                        """), {
                            "iid":  idea.id,
                            "aid":  paper.arxiv_id,
                            "ak":   answers,
                            "conf": confidence,
                            "rat":  rationale[:500],
                        })
                    except Exception:
                        pass
                else:
                    dropped += 1

        # Tick: apply any grace-period retirements that have elapsed
        _apply_elapsed_retirements(db)

        _log_autowiki_run(db, 0, "research_ideas_coverage",
                          scheduled_retirements=scheduled, dropped=dropped)
        db.commit()
        log.info("[J11] coverage_detection_pass scheduled=%d dropped=%d", scheduled, dropped)
        return {"scheduled": scheduled, "dropped": dropped}

    except Exception as exc:
        db.rollback()
        log.exception("[J11] coverage_detection_pass failed: %s", exc)
        raise
    finally:
        db.close()


def _apply_elapsed_retirements(db):
    from sqlalchemy import text
    now = datetime.datetime.utcnow()
    pending = db.execute(text("""
        SELECT id, idea_id, arxiv_id, confidence
        FROM research_idea_coverage_candidates
        WHERE status = 'pending' AND retire_after IS NOT NULL AND retire_after <= :now
    """), {"now": now}).fetchall()

    for row in pending:
        db.execute(text("""
            UPDATE research_ideas
            SET status              = 'covered',
                covered_by_arxiv_id = :aid,
                covered_at          = NOW(),
                covered_confidence  = :conf,
                updated_at          = NOW()
            WHERE id = :iid AND status NOT IN ('covered', 'rejected', 'superseded')
        """), {"iid": row.idea_id, "aid": row.arxiv_id, "conf": row.confidence})
        db.execute(text("""
            UPDATE research_idea_coverage_candidates
            SET status = 'retired', reviewed_at = NOW(), reviewed_by = 'auto_cron'
            WHERE id = :id
        """), {"id": row.id})
        log.info("[J11] retired idea_id=%d covered_by=%s", row.idea_id, row.arxiv_id)


# ── J2: Rakon daily idea drafting pass ────────────────────────────────────────

RAKON_DRAFT_PROMPT = """
You are a senior astronomy research strategist generating new research ideas for a wiki page.

WIKI PAGE: {title}
Tagline: {tagline}

TOP CLAIMS (prioritise debated/uncertain claims):
{claims_block}

RECENT LITERATURE (last 90 days):
{arxiv_block}

EXISTING IDEAS (do NOT duplicate — use these for context only):
{existing_block}

ALLOWED SURVEY COMBOS (pick exactly two):
JWST+DESI, JWST+Euclid, JWST+ALMA, JWST+HSC, JWST+LSST, JWST+VLA,
DESI+Euclid, DESI+HSC, DESI+ALMA, DESI+LSST,
ALMA+Euclid, ALMA+HSC, ALMA+LSST, ALMA+VLA,
Euclid+HSC, Euclid+LSST, HSC+LSST, LSST+VLA

Generate up to 5 high-quality DRAFT research ideas not already in the existing pool.
Focus on: debated claims, gaps in the existing idea pool, and recent arXiv findings.

OUTPUT — strict JSON:
{{
  "drafts": [
    {{
      "combo": "JWST+DESI",
      "question": "<1-sentence, falsifiable>",
      "why_now": "<1-2 sentences anchored to claims or recent arXiv>",
      "approach": "<2-3 sentences: data, cuts, measurement, expected N>",
      "anchors": {{"claim_ids": [], "debate_ids": [], "arxiv_ids": []}}
    }}
  ]
}}

CONSTRAINTS:
- Question MUST be answerable only by combining the two named surveys.
- At least 1 claim_id or debate_id per idea.
- No vague verbs; use measure/constrain/test whether/rule out.
- Quality over quota — 2 great ideas beat 5 weak ones.
"""


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.rakon_daily_idea_draft", bind=True, max_retries=0)
def rakon_daily_idea_draft(self):
    """J2 — Daily 02:00 KST Rakon idea drafting pass. Generates new draft ideas (Rakon primary, Buddle fallback).
    Distinct from J3 (promotion/curation) — J2 purely drafts; J3 curates weekly."""
    from app.database import SessionLocal
    from app.config import settings
    from sqlalchemy import text

    db = SessionLocal()
    drafted = 0
    model_used = None

    try:
        # Top pages by debate count + recent activity
        pages = db.execute(text("""
            SELECT wp.id, wp.slug, wp.title, wp.hero_tagline,
                   COUNT(DISTINCT c.id) FILTER (WHERE c.trust_level='debated') AS debate_count
            FROM wiki_pages wp
            LEFT JOIN claims c ON c.page_id = wp.id
            GROUP BY wp.id, wp.slug, wp.title, wp.hero_tagline
            ORDER BY debate_count DESC
            LIMIT 5
        """)).fetchall()

        if not pages:
            return {"drafted": 0}

        rakon_alive = _check_ollama_alive(OLLAMA_MACPRO, MODEL_RAKON)
        if rakon_alive:
            base_url    = OLLAMA_MACPRO
            model       = MODEL_RAKON
            model_chain = "rakon→astrosage-70b→atom-7b"
            model_used  = "rakon"
        else:
            log.warning("[J2] Rakon unavailable — falling back to Buddle")
            base_url    = OLLAMA_BUDDLE
            model       = MODEL_BUDDLE
            model_chain = "buddle→astrosage-70b→atom-7b"
            model_used  = "buddle"
            _discord("⚠️ J2 daily draft: Rakon unavailable, using Buddle fallback.")

        for page in pages:
            ctx = _build_page_context(db, page.id)
            if not ctx:
                continue

            existing    = ctx["ideas"]
            claims      = ctx["claims"]
            arxiv       = ctx["arxiv"]
            debates     = ctx["debates"]

            claims_block   = "\n".join(f"[{c['id']}] ({c['trust']}) {c['text'][:200]}" for c in claims) or "(none)"
            arxiv_block    = "\n".join(f"[{a['arxiv_id']}] {a['title']}: {a['abstract'][:300]}" for a in arxiv) or "(none)"
            existing_block = "\n".join(f"[{e['combo']}] {e['question'][:200]}" for e in existing) or "(none)"

            prompt = RAKON_DRAFT_PROMPT.format(
                title=page.title,
                tagline=page.hero_tagline or "",
                claims_block=claims_block[:2000],
                arxiv_block=arxiv_block[:2000],
                existing_block=existing_block[:2000],
            )

            _j2_timeout = 28800 if model == MODEL_RAKON else 1800
            raw = _ollama_chat(base_url, model, prompt, temperature=0.5, timeout=_j2_timeout)
            if not raw:
                log.warning("[J2] no output from %s for page %s", model, page.slug)
                continue

            parsed = _parse_json_block(raw)
            drafts = (parsed or {}).get("drafts", []) if isinstance(parsed, dict) else []

            for draft in drafts:
                if not _validate_skeleton(draft):
                    continue
                score = _atom_score(draft, existing)
                if score is None or score.get("dedup_cosine_estimate", 0) >= DEDUP_COSINE_THRESHOLD:
                    continue
                if score.get("novelty", 0) < NOVELTY_FLOOR:
                    continue
                _persist_draft(db, page.id, draft, score, "rakon_daily_draft", None)
                drafted += 1

        db.commit()
        _discord(f"✏️ J2 daily draft complete — {drafted} new drafts added · model={model_used}")
        log.info("[J2] rakon_daily_idea_draft complete drafted=%d model=%s", drafted, model_used)
        return {"drafted": drafted, "model_used": model_used}

    except Exception as exc:
        db.rollback()
        log.exception("[J2] rakon_daily_idea_draft failed: %s", exc)
        raise
    finally:
        db.close()


# ═══════════════════════════════════════════════════════════════════════════════
# §9 v2 — 8-model throughput additions
# ═══════════════════════════════════════════════════════════════════════════════

# ── Rakon mutex (Mac Pro is single-tenant) ─────────────────────────────────────

_RAKON_LOCK_KEY = "rakon:lock"

def _rakon_lock_acquire(ttl_seconds: int) -> bool:
    """SETNX acquire rakon:lock. Returns True if acquired."""
    try:
        r = _redis()
        return bool(r.set(_RAKON_LOCK_KEY, "1", nx=True, ex=ttl_seconds))
    except Exception:
        return True  # fail open — don't block on Redis error

def _rakon_lock_release() -> None:
    try:
        _redis().delete(_RAKON_LOCK_KEY)
    except Exception:
        pass

def _rakon_lock_held() -> bool:
    try:
        return bool(_redis().get(_RAKON_LOCK_KEY))
    except Exception:
        return False


# ── Page picker ────────────────────────────────────────────────────────────────

def _pick_next_priority_page() -> int | None:
    """Return page_id to work on. Respects wiki_improvement:priority_page_id pin."""
    try:
        pinned = _redis().get("wiki_improvement:priority_page_id")
        if pinned:
            return int(pinned)
    except Exception:
        pass
    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    try:
        row = db.execute(text("""
            SELECT wp.id
            FROM wiki_pages wp
            LEFT JOIN research_ideas ri ON ri.page_id = wp.id AND ri.status = 'draft'
            LEFT JOIN claims c ON c.page_id = wp.id AND c.trust_level = 'debated'
            GROUP BY wp.id
            ORDER BY COUNT(DISTINCT ri.id) ASC, COUNT(DISTINCT c.id) DESC
            LIMIT 1
        """)).fetchone()
        return row.id if row else None
    except Exception:
        return None
    finally:
        db.close()


# ── Prompt constants ───────────────────────────────────────────────────────────

MIMA_DRAFT_PROMPT = """\
You are a research strategist generating DIVERSE research ideas for the {title} wiki page.
Diversity framing: avoid duplicating question axes already in the pool — prioritise unexplored angles
across redshift, mass-function, merger-rate, feedback, morphology, and chemical-enrichment regimes.

WIKI PAGE: {title}
Tagline: {tagline}

TOP CLAIMS:
{claims_block}

RECENT LITERATURE (last 90d):
{arxiv_block}

EXISTING IDEAS (avoid duplicates):
{existing_block}

ALLOWED SURVEY COMBOS (pick exactly two):
JWST+DESI, JWST+Euclid, JWST+ALMA, JWST+HSC, JWST+LSST, JWST+VLA,
DESI+Euclid, DESI+HSC, DESI+ALMA, DESI+LSST,
ALMA+Euclid, ALMA+HSC, ALMA+LSST, ALMA+VLA,
Euclid+HSC, Euclid+LSST, HSC+LSST, LSST+VLA

Generate up to 5 high-quality DRAFT ideas. Prioritise diversity over volume.

OUTPUT JSON:
{{"drafts": [{{"combo": "X+Y", "question": "...", "why_now": "...", "approach": "...",
  "anchors": {{"claim_ids": [], "debate_ids": [], "arxiv_ids": []}}}}]}}
"""

TERA_GAP_PROMPT = """\
You are a coverage analyst with a 128k-token context window reviewing the {title} wiki page.
Your task: identify research gaps and structural issues using the FULL page content and claim list.

WIKI PAGE: {title}

FULL PAGE CONTENT (Markdown):
{page_content}

ALL CLAIMS ({claim_count} total):
{claims_block}

RECENT LITERATURE (up to 30 abstracts):
{arxiv_block}

OUTPUT strict JSON:
{{
  "missing_subtopics": ["<subtopic not covered by any section>", ...],
  "split_merge_suggestions": ["<e.g. split §3 into quenching+feedback>", ...],
  "orphan_section_flags": ["<section title with no claims or evidence>", ...],
  "confidence": <0.0-1.0>
}}
"""

TAKJI_VERIFY_PROMPT = """\
You are a methodology gate for astronomy research ideas.
Check whether this idea has sound methodology, realistic datasets, and consistent systematics.

IDEA
----
Survey combo: {combo}
Question: {question}
Why now: {why_now}
Approach: {approach}

PAGE CLAIMS CONTEXT:
{claims_block}

Respond with ONLY valid JSON:
{{
  "verdict": "pass" | "soft_fail" | "hard_fail",
  "rationale": "<one sentence; cite the specific flaw for fail cases>"
}}

hard_fail: idea is methodologically impossible, uses non-existent data, or is logically incoherent.
soft_fail: idea has weaknesses but is salvageable with minor revisions.
pass: methodology is sound.
"""

ASTROSAGE_POLISH_PROMPT = """\
You are an astronomy science communicator. Rewrite the three text fields of a research idea
to Wikipedia-grade prose — precise, jargon-explained, no buzzwords, quantitative where possible.

PAGE: {page_title}

ORIGINAL IDEA
-------------
Question:  {question}
Why now:   {why_now}
Approach:  {approach}

OUTPUT strict JSON (preserve meaning, improve prose only):
{{"question": "...", "why_now": "...", "approach": "..."}}
"""

ASTROSAGE_ADVERSARIAL_PROMPT = """\
You are stress-testing astronomy claims by finding published falsifying evidence.

PAGE CLAIM (status=accepted):
[{claim_id}] {claim_text}

Search your knowledge of arXiv papers published in the last 12 months.
Find UP TO 2 papers that directly contradict, challenge, or significantly complicate this claim.
Only include papers with arxiv_id you are confident exist.

OUTPUT strict JSON:
{{
  "falsifying_papers": [
    {{"arxiv_id": "...", "title": "...", "abstract": "...<200 chars>",
      "stance": "contradicts", "year": 2024}}
  ]
}}
If no strong falsifying evidence exists, return {{"falsifying_papers": []}}.
"""

HERO_REFRESH_PROMPT = """\
You are updating a wiki page hero section based on recent accepted claims.

PAGE: {title}
Current tagline: {tagline}

RECENTLY ACCEPTED CLAIMS (last 7 days):
{new_claims_block}

ALL ACCEPTED CLAIMS (for context):
{all_claims_block}

OUTPUT strict JSON:
{{
  "hero_tagline": "<1-sentence punchy summary of the field's current state>",
  "hero_facts": [
    "<fact 1, cite claim or instrument>",
    "<fact 2>",
    "<fact 3>"
  ]
}}
"""

NUTTY_TRUST_PROMPT = """\
Given the following evidence for/against a claim, assign a trust level.

CLAIM: {claim_text}

SUPPORTING EVIDENCE ({support_count} items):
{support_block}

CONTRADICTING EVIDENCE ({contra_count} items):
{contra_block}

Choose ONE trust level: consensus | accepted | debated | contested | retracted

Output ONLY the trust level string, nothing else.
"""


# ── Judge-step helpers ──────────────────────────────────────────────────────────

def _takji_verify(draft: dict, claims: list, arxiv: list) -> dict:
    """Returns {'verdict': 'pass'|'soft_fail'|'hard_fail', 'rationale': str}."""
    claims_block = "\n".join(f"[{c['id']}] {c['text'][:200]}" for c in claims[:8]) or "(none)"
    prompt = TAKJI_VERIFY_PROMPT.format(
        combo=draft.get("combo", ""),
        question=draft.get("question", ""),
        why_now=draft.get("why_now", ""),
        approach=draft.get("approach", ""),
        claims_block=claims_block,
    )
    raw = _ollama_chat(OLLAMA_LOCAL, MODEL_TAKJI, prompt, temperature=0.1, timeout=120)
    if not raw:
        return {"verdict": "pass", "rationale": "takji_timeout_fail_open"}
    result = _parse_json_block(raw)
    if not isinstance(result, dict):
        return {"verdict": "pass", "rationale": "takji_parse_fail_open"}
    return result


def _astrosage_polish(draft: dict, page_title: str) -> dict:
    """Returns {'question', 'why_now', 'approach'} with Wikipedia-grade prose."""
    polish_enabled = True
    try:
        polish_enabled = _redis().get("idea_judge:astrosage_polish_enabled") != "0"
    except Exception:
        pass
    if not polish_enabled:
        return {k: draft.get(k, "") for k in ("question", "why_now", "approach")}

    prompt = ASTROSAGE_POLISH_PROMPT.format(
        page_title=page_title,
        question=draft.get("question", ""),
        why_now=draft.get("why_now", ""),
        approach=draft.get("approach", ""),
    )
    raw = _ollama_chat(OLLAMA_LOCAL, MODEL_ASTROSAGE, prompt, temperature=0.3, timeout=180)
    if not raw:
        return {k: draft.get(k, "") for k in ("question", "why_now", "approach")}
    result = _parse_json_block(raw)
    if not isinstance(result, dict):
        return {k: draft.get(k, "") for k in ("question", "why_now", "approach")}
    return {
        "question": result.get("question") or draft.get("question", ""),
        "why_now":  result.get("why_now")  or draft.get("why_now", ""),
        "approach": result.get("approach") or draft.get("approach", ""),
    }


# ── §9 v2 Producer tasks ────────────────────────────────────────────────────────

@shared_task(name="app.agent_loop.research_ideas.auto_improvement.rakon_draft_async", bind=True, max_retries=0)
def rakon_draft_async(self, page_id: int | None = None):
    """R-lane: Rakon (671b) per-page idea drafting with rakon:lock mutex (TTL 8h)."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    if _provenance_enforce_enabled():
        return {
            "skip": "provenance_enforce_suppressed_research_idea_draft",
            "page_id": page_id,
        }

    if not _rakon_lock_acquire(28800):
        log.info("[rakon_draft_async] rakon:lock held, skipping page %d", page_id)
        return {"skip": "rakon_lock_held"}

    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    drafted = 0
    try:
        rakon_alive = _rakon_prewarm()  # blocks up to 1800s on cold-load
        model = MODEL_RAKON if rakon_alive else MODEL_BUDDLE
        base_url = OLLAMA_MACPRO if model == MODEL_RAKON else OLLAMA_BUDDLE
        model_chain = f"{model}→atom-7b"

        ctx = _build_page_context(db, page_id)
        if not ctx:
            return {"error": "page_not_found"}

        claims_block   = "\n".join(f"[{c['id']}] ({c['trust']}) {c['text'][:200]}" for c in ctx["claims"]) or "(none)"
        arxiv_block    = "\n".join(f"[{a['arxiv_id']}] {a['title']}: {a['abstract'][:300]}" for a in ctx["arxiv"]) or "(none)"
        existing_block = "\n".join(f"[{e['combo']}] {e['question'][:200]}" for e in ctx["ideas"]) or "(none)"

        prompt = RAKON_DRAFT_PROMPT.format(
            title=ctx["title"], tagline=ctx["tagline"],
            claims_block=claims_block[:2000], arxiv_block=arxiv_block[:2000],
            existing_block=existing_block[:2000],
        )

        _timeout = 28800 if model == MODEL_RAKON else 1800
        raw = _ollama_chat(base_url, model, prompt, temperature=0.5, timeout=_timeout)
        parsed = _parse_json_block(raw) if raw else None
        drafts = (parsed or {}).get("drafts", []) if isinstance(parsed, dict) else []

        for draft in drafts:
            if not _validate_skeleton(draft):
                continue
            score = _atom_score(draft, ctx["ideas"])
            if score is None or score.get("dedup_cosine_estimate", 0) >= DEDUP_COSINE_THRESHOLD:
                continue
            if score.get("novelty", 0) < NOVELTY_FLOOR:
                continue
            _persist_draft(db, page_id, draft, score, "rakon_async", None)
            drafted += 1

        db.commit()
        log.info("[rakon_draft_async] page=%d drafted=%d model=%s", page_id, drafted, model)
        return {"page_id": page_id, "drafted": drafted, "model": model}
    except Exception as exc:
        db.rollback()
        log.exception("[rakon_draft_async] failed: %s", exc)
        raise
    finally:
        _rakon_lock_release()
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.mima_draft_async", bind=True, max_retries=0)
def mima_draft_async(self, page_id: int | None = None):
    """M-lane: Mima (qwen3.6:35b-a3b-nvfp4) diversity drafter with mima:lock mutex (TTL 2h)."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    if _provenance_enforce_enabled():
        return {
            "skip": "provenance_enforce_suppressed_research_idea_draft",
            "page_id": page_id,
        }

    try:
        r = _redis()
        if not r.set("mima:lock", "1", nx=True, ex=7200):
            return {"skip": "mima_lock_held"}
    except Exception:
        r = None

    from app.database import SessionLocal
    db = SessionLocal()
    drafted = 0
    try:
        ctx = _build_page_context(db, page_id)
        if not ctx:
            return {"error": "page_not_found"}

        claims_block   = "\n".join(f"[{c['id']}] ({c['trust']}) {c['text'][:200]}" for c in ctx["claims"]) or "(none)"
        arxiv_block    = "\n".join(f"[{a['arxiv_id']}] {a['title']}: {a['abstract'][:300]}" for a in ctx["arxiv"]) or "(none)"
        existing_block = "\n".join(f"[{e['combo']}] {e['question'][:200]}" for e in ctx["ideas"]) or "(none)"

        prompt = MIMA_DRAFT_PROMPT.format(
            title=ctx["title"], tagline=ctx["tagline"],
            claims_block=claims_block[:2000], arxiv_block=arxiv_block[:2000],
            existing_block=existing_block[:2000],
        )

        raw = _ollama_chat(OLLAMA_LOCAL, MODEL_MIMA, prompt, temperature=0.6, timeout=1800)
        parsed = _parse_json_block(raw) if raw else None
        drafts = (parsed or {}).get("drafts", []) if isinstance(parsed, dict) else []

        for draft in drafts:
            if not _validate_skeleton(draft):
                continue
            score = _atom_score(draft, ctx["ideas"])
            if score is None or score.get("dedup_cosine_estimate", 0) >= DEDUP_COSINE_THRESHOLD:
                continue
            if score.get("novelty", 0) < NOVELTY_FLOOR:
                continue
            _persist_draft(db, page_id, draft, score, "mima_async", None)
            drafted += 1

        db.commit()
        log.info("[mima_draft_async] page=%d drafted=%d", page_id, drafted)
        return {"page_id": page_id, "drafted": drafted}
    except Exception as exc:
        db.rollback()
        log.exception("[mima_draft_async] failed: %s", exc)
        raise
    finally:
        try:
            if r:
                r.delete("mima:lock")
        except Exception:
            pass
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.tera_draft_async", bind=True, max_retries=0)
def tera_draft_async(self, page_id: int | None = None):
    """T-lane: Tera (qwen3.6:27b-nvfp4) full-context gap drafter with tera:lock mutex (TTL 1h)."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    if _provenance_enforce_enabled():
        return {
            "skip": "provenance_enforce_suppressed_research_idea_draft",
            "page_id": page_id,
        }

    try:
        r = _redis()
        if not r.set("tera:lock", "1", nx=True, ex=3600):
            return {"skip": "tera_lock_held"}
    except Exception:
        r = None

    from app.database import SessionLocal
    db = SessionLocal()
    drafted = 0
    try:
        ctx = _build_page_context(db, page_id, full=True, max_arxiv=30)
        if not ctx:
            return {"error": "page_not_found"}

        claims_block = "\n".join(f"[{c['id']}] ({c['trust']}) {c['text'][:300]}" for c in ctx["claims"]) or "(none)"
        arxiv_block  = "\n".join(f"[{a['arxiv_id']}] {a['title']}: {a['abstract'][:400]}" for a in ctx["arxiv"]) or "(none)"

        prompt = TERA_GAP_PROMPT.format(
            title=ctx["title"],
            page_content=ctx["content"][:80000],
            claim_count=len(ctx["claims"]),
            claims_block=claims_block[:8000],
            arxiv_block=arxiv_block[:8000],
        )

        raw = _ollama_chat(OLLAMA_LOCAL, MODEL_TERA, prompt, temperature=0.3, timeout=1800)
        parsed = _parse_json_block(raw) if raw else None
        if not isinstance(parsed, dict):
            return {"page_id": page_id, "drafted": 0}

        # Write CoverageReport row from the gap analysis
        from sqlalchemy import text
        missing = parsed.get("missing_subtopics", [])
        splits  = parsed.get("split_merge_suggestions", [])
        orphans = parsed.get("orphan_section_flags", [])
        try:
            db.execute(text("""
                INSERT INTO coverage_reports
                  (page_id, generated_at, generator_model, missing_subtopics_jsonb,
                   split_merge_suggestions_jsonb, orphan_section_flags_jsonb)
                VALUES (:pid, NOW(), :model, :ms, :sm, :os)
            """), {
                "pid": page_id, "model": MODEL_TERA,
                "ms": json.dumps(missing), "sm": json.dumps(splits), "os": json.dumps(orphans),
            })
        except Exception as e:
            log.debug("tera_draft_async: CoverageReport write failed: %s", e)

        db.commit()
        log.info("[tera_draft_async] page=%d missing=%d splits=%d", page_id, len(missing), len(splits))
        return {"page_id": page_id, "drafted": drafted,
                "missing_subtopics": len(missing), "orphan_flags": len(orphans)}
    except Exception as exc:
        db.rollback()
        log.exception("[tera_draft_async] failed: %s", exc)
        raise
    finally:
        try:
            if r:
                r.delete("tera:lock")
        except Exception:
            pass
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.buddle_draft_async", bind=True, max_retries=0)
def buddle_draft_async(self, page_id: int | None = None):
    """B-lane: Buddle drafter on Mac Studio local Ollama."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    if _provenance_enforce_enabled():
        return {
            "skip": "provenance_enforce_suppressed_research_idea_draft",
            "page_id": page_id,
        }

    try:
        r = _redis()
        if not r.set("buddle:lock", "1", nx=True, ex=7200):
            return {"skip": "buddle_lock_held"}
    except Exception:
        r = None

    from app.database import SessionLocal
    db = SessionLocal()
    drafted = 0
    try:
        ctx = _build_page_context(db, page_id)
        if not ctx:
            return {"error": "page_not_found"}

        claims_block   = "\n".join(f"[{c['id']}] ({c['trust']}) {c['text'][:200]}" for c in ctx["claims"]) or "(none)"
        arxiv_block    = "\n".join(f"[{a['arxiv_id']}] {a['title']}: {a['abstract'][:300]}" for a in ctx["arxiv"]) or "(none)"
        existing_block = "\n".join(f"[{e['combo']}] {e['question'][:200]}" for e in ctx["ideas"]) or "(none)"

        prompt = RAKON_DRAFT_PROMPT.format(
            title=ctx["title"], tagline=ctx["tagline"],
            claims_block=claims_block[:2000], arxiv_block=arxiv_block[:2000],
            existing_block=existing_block[:2000],
        )

        raw = _ollama_chat(OLLAMA_BUDDLE, MODEL_BUDDLE, prompt, temperature=0.5, timeout=900)
        parsed = _parse_json_block(raw) if raw else None
        drafts = (parsed or {}).get("drafts", []) if isinstance(parsed, dict) else []

        for draft in drafts:
            if not _validate_skeleton(draft):
                continue
            score = _atom_score(draft, ctx["ideas"])
            if score is None or score.get("dedup_cosine_estimate", 0) >= DEDUP_COSINE_THRESHOLD:
                continue
            if score.get("novelty", 0) < NOVELTY_FLOOR:
                continue
            _persist_draft(db, page_id, draft, score, "buddle_async", None)
            drafted += 1

        db.commit()
        log.info("[buddle_draft_async] page=%d drafted=%d", page_id, drafted)
        return {"page_id": page_id, "drafted": drafted}
    except Exception as exc:
        db.rollback()
        log.exception("[buddle_draft_async] failed: %s", exc)
        raise
    finally:
        try:
            if r:
                r.delete("buddle:lock")
        except Exception:
            pass
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.rakon_adversarial_probe", bind=True, max_retries=0)
def rakon_adversarial_probe(self, page_id: int | None = None):
    """R3: Rakon finds published falsifying evidence for accepted claims. rakon:lock TTL 8h."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    provenance_mode = (
        getattr(settings, "AUTOWIKI_PROVENANCE_GATE_MODE", "shadow") or "shadow"
    ).strip().lower()
    if provenance_mode == "enforce":
        return {
            "skip": "provenance_enforce_suppressed_direct_adversarial_evidence_insert",
            "page_id": page_id,
        }

    if not _rakon_lock_acquire(28800):
        return {"skip": "rakon_lock_held"}

    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    probed = 0
    inserted = 0
    try:
        claims = db.execute(text("""
            SELECT id, text FROM claims
            WHERE page_id = :pid AND trust_level = 'accepted'
            ORDER BY created_at ASC LIMIT 3
        """), {"pid": page_id}).fetchall()

        rakon_alive = _rakon_prewarm()  # blocks up to 1800s on cold-load
        model = MODEL_RAKON if rakon_alive else MODEL_BUDDLE
        base_url = OLLAMA_MACPRO if model == MODEL_RAKON else OLLAMA_BUDDLE
        _timeout = 28800 if model == MODEL_RAKON else 1800

        for claim in claims:
            probed += 1
            prompt = ASTROSAGE_ADVERSARIAL_PROMPT.format(
                claim_id=claim.id, claim_text=claim.text[:500],
            )
            raw = _ollama_chat(base_url, model, prompt, temperature=0.2, timeout=_timeout)
            parsed = _parse_json_block(raw) if raw else None
            papers = (parsed or {}).get("falsifying_papers", []) if isinstance(parsed, dict) else []

            for paper in papers[:2]:
                if not paper.get("arxiv_id"):
                    continue
                try:
                    db.execute(text("""
                        INSERT INTO evidence
                          (claim_id, arxiv_id, title, year, abstract, stance, quality, source_channel)
                        VALUES (:cid, :aid, :title, :year, :abstract, 'contradicts', 0.40, 'adversarial_probe')
                        ON CONFLICT DO NOTHING
                    """), {
                        "cid":     claim.id,
                        "aid":     paper.get("arxiv_id"),
                        "title":   paper.get("title", "")[:300],
                        "year":    paper.get("year"),
                        "abstract": (paper.get("abstract") or "")[:500],
                    })
                    inserted += 1
                except Exception as e:
                    log.debug("[rakon_adversarial_probe] evidence insert failed: %s", e)

        db.commit()
        log.info("[rakon_adversarial_probe] page=%d probed=%d inserted=%d", page_id, probed, inserted)
        return {"page_id": page_id, "probed": probed, "inserted": inserted}
    except Exception as exc:
        db.rollback()
        log.exception("[rakon_adversarial_probe] failed: %s", exc)
        raise
    finally:
        _rakon_lock_release()
        db.close()


# ── §9 v2 Judge task ───────────────────────────────────────────────────────────

JUDGE_POOL_PROMOTE_N = 5  # idea_judge:promote_per_tick default

@shared_task(name="app.agent_loop.research_ideas.auto_improvement.judge_idea_pool", bind=True, max_retries=0)
def judge_idea_pool(self):
    """JI: three-stage judge (Atom score → Takji verify → AstroSage polish). Promotes top-N drafts."""
    if _provenance_enforce_enabled():
        return {"skip": "provenance_enforce_suppressed_idea_judge_pool"}

    from app.database import SessionLocal
    from sqlalchemy import text

    page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}

    promote_n = JUDGE_POOL_PROMOTE_N
    try:
        promote_n = int(_redis().get("idea_judge:promote_per_tick") or promote_n)
    except Exception:
        pass

    db = SessionLocal()
    promoted = 0
    retired_atom = 0
    retired_takji = 0
    rakon_spawned_page_id = None

    try:
        ctx = _build_page_context(db, page_id)
        if not ctx:
            return {"error": "page_not_found"}

        drafts = [i for i in ctx["ideas"] if i["status"] == "draft"]
        if not drafts:
            return {"page_id": page_id, "promoted": 0, "note": "no_drafts"}

        # Stage 1: Atom score — filter out low novelty/feasibility
        scored = []
        for draft in drafts:
            score = _atom_score(draft, ctx["ideas"])
            if score is None:
                continue
            if score.get("novelty", 0) < NOVELTY_FLOOR or score.get("feasibility", 0) < FEASIBILITY_FLOOR:
                retired_atom += 1
                db.execute(text(
                    "UPDATE research_ideas SET status='rejected', updated_at=NOW() WHERE id=:id AND status='draft'"
                ), {"id": draft["id"]})
                continue
            if score.get("dedup_cosine_estimate", 0) >= DEDUP_COSINE_THRESHOLD:
                retired_atom += 1
                db.execute(text(
                    "UPDATE research_ideas SET status='rejected', updated_at=NOW() WHERE id=:id AND status='draft'"
                ), {"id": draft["id"]})
                continue
            scored.append((draft, score))

        # Stage 2: Takji verify — hard_fail drafts rejected
        verified = []
        for draft, score in scored:
            verdict = _takji_verify(draft, ctx["claims"], ctx["arxiv"])
            if verdict.get("verdict") == "hard_fail":
                retired_takji += 1
                db.execute(text(
                    "UPDATE research_ideas SET status='rejected', updated_at=NOW() WHERE id=:id AND status='draft'"
                ), {"id": draft["id"]})
                continue
            verified.append((draft, score, verdict))

        # Stage 3: AstroSage polish — rewrite the top-N by combined score
        verified.sort(key=lambda x: -(x[1].get("novelty", 0) + x[1].get("feasibility", 0)))
        polished_candidates = []
        for draft, score, verdict in verified[:promote_n]:
            polished = _astrosage_polish(draft, ctx["title"])
            polished_candidates.append((draft, score, verdict, polished))

        # opus_judge_pool stage removed 2026-06-13 (audit D2): 0% success against the
        # premium whitelist; opus-judge-tick already covers Opus judging.

        for draft, score, verdict, polished in polished_candidates:
            model_chain = "nutty→atom-7b→takji→astrosage"
            db.execute(text("""
                UPDATE research_ideas
                SET status      = 'active',
                    promoted_at = NOW(),
                    promoted_by = 'judge_pool_ji',
                    question    = :q,
                    why_now     = :w,
                    approach    = :a,
                    model_chain = :mc,
                    updated_at  = NOW()
                WHERE id = :id AND status = 'draft'
            """), {
                "id": draft["id"],
                "q":  polished["question"],
                "w":  polished["why_now"],
                "a":  polished["approach"],
                "mc": model_chain,
            })
            promoted += 1

        # Opportunistic: spawn Rakon draft if lock is free and pool is thin
        if not _rakon_lock_held() and len(drafts) < 3:
            rakon_draft_async.delay(page_id)
            rakon_spawned_page_id = page_id

        _log_autowiki_run(db, page_id, "idea_judge_pool",
                          pool_size=len(drafts), retired_atom=retired_atom,
                          retired_takji=retired_takji, promoted=promoted,
                          rakon_spawned_page_id=rakon_spawned_page_id)
        db.commit()
        log.info("[judge_idea_pool] page=%d promoted=%d retired_atom=%d retired_takji=%d",
                 page_id, promoted, retired_atom, retired_takji)
        return {
            "page_id": page_id, "promoted": promoted,
            "retired_atom": retired_atom, "retired_takji": retired_takji,
            "rakon_spawned_page_id": rakon_spawned_page_id,
        }
    except Exception as exc:
        db.rollback()
        log.exception("[judge_idea_pool] failed: %s", exc)
        raise
    finally:
        db.close()


# ── §9 v2 Work tasks ───────────────────────────────────────────────────────────

@shared_task(name="app.agent_loop.research_ideas.auto_improvement.buddle_evidence_pair", bind=True, max_retries=0)
def buddle_evidence_pair(self, page_id: int | None = None):
    """B3: Buddle finds supporting evidence for claims with <2 evidence links (arxiv last 90d)."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    provenance_mode = (
        getattr(settings, "AUTOWIKI_PROVENANCE_GATE_MODE", "shadow") or "shadow"
    ).strip().lower()
    if provenance_mode == "enforce":
        return {
            "skip": "provenance_enforce_suppressed_direct_evidence_insert",
            "page_id": page_id,
        }

    if _rakon_lock_held():
        return {"skip": "rakon_lock_held"}

    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    inserted = 0
    try:
        thin_claims = db.execute(text("""
            SELECT c.id, c.text
            FROM claims c
            LEFT JOIN evidence ev ON ev.claim_id = c.id
            WHERE c.page_id = :pid
            GROUP BY c.id, c.text
            HAVING COUNT(ev.id) < 2
            ORDER BY COUNT(ev.id) ASC LIMIT 3
        """), {"pid": page_id}).fetchall()

        if not thin_claims:
            return {"page_id": page_id, "inserted": 0, "note": "no_thin_claims"}

        cutoff_str = (datetime.datetime.utcnow() - datetime.timedelta(days=90)).strftime("%Y-%m-%d")
        recent_arxiv = db.execute(text("""
            SELECT ap.arxiv_id, ap.title, ap.abstract
            FROM arxiv_papers ap
            WHERE ap.related_pages::jsonb ? (SELECT slug FROM wiki_pages WHERE id = :pid)
              AND ap.submitted >= :cut
            ORDER BY ap.submitted DESC LIMIT 20
        """), {"pid": page_id, "cut": cutoff_str}).fetchall()

        arxiv_block = "\n".join(
            f"[{a.arxiv_id}] {a.title}: {(a.abstract or '')[:300]}" for a in recent_arxiv
        ) or "(none)"

        for claim in thin_claims:
            prompt = (
                f"CLAIM [{claim.id}]: {claim.text[:400]}\n\n"
                f"RECENT ARXIV (last 90d):\n{arxiv_block[:3000]}\n\n"
                "Find UP TO 2 arxiv papers from the list above that SUPPORT this claim. "
                "Return JSON: {\"papers\": [{\"arxiv_id\": \"...\", \"title\": \"...\", "
                "\"stance\": \"supports\", \"abstract\": \"...<200 chars>\", \"year\": 2024}]}"
            )
            raw = _ollama_chat(OLLAMA_BUDDLE, MODEL_BUDDLE, prompt, temperature=0.2, timeout=900)
            parsed = _parse_json_block(raw) if raw else None
            papers = (parsed or {}).get("papers", []) if isinstance(parsed, dict) else []

            for paper in papers[:2]:
                if not paper.get("arxiv_id"):
                    continue
                try:
                    db.execute(text("""
                        INSERT INTO evidence
                          (claim_id, arxiv_id, title, year, abstract, stance, quality, source_channel)
                        VALUES (:cid, :aid, :title, :year, :abstract, 'supports', 0.50, 'buddle_evidence_pair')
                        ON CONFLICT DO NOTHING
                    """), {
                        "cid":     claim.id,
                        "aid":     paper.get("arxiv_id"),
                        "title":   paper.get("title", "")[:300],
                        "year":    paper.get("year"),
                        "abstract": (paper.get("abstract") or "")[:500],
                    })
                    inserted += 1
                except Exception as e:
                    log.debug("[buddle_evidence_pair] insert failed: %s", e)

        db.commit()
        log.info("[buddle_evidence_pair] page=%d inserted=%d", page_id, inserted)
        return {"page_id": page_id, "inserted": inserted}
    except Exception as exc:
        db.rollback()
        log.exception("[buddle_evidence_pair] failed: %s", exc)
        raise
    finally:
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.opus_hero_refresh", bind=True, max_retries=0)
def opus_hero_refresh(self, page_id: int | None = None):
    """A3-v3: Opus (claude-opus-4-8) regenerates hero_tagline + hero_facts from recent accepted claims."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    provenance_mode = (
        getattr(settings, "AUTOWIKI_PROVENANCE_GATE_MODE", "shadow") or "shadow"
    ).strip().lower()
    if provenance_mode == "enforce":
        return {
            "skip": "provenance_enforce_suppressed_direct_hero_refresh",
            "page_id": page_id,
        }

    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    try:
        page = db.execute(
            text("SELECT id, title, hero_tagline FROM wiki_pages WHERE id = :pid"),
            {"pid": page_id},
        ).fetchone()
        if not page:
            return {"error": "page_not_found"}

        cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=7)
        new_claims = db.execute(text("""
            SELECT id, text FROM claims
            WHERE page_id = :pid AND trust_level IN ('accepted','consensus') AND created_at >= :cut
            ORDER BY created_at DESC LIMIT 10
        """), {"pid": page_id, "cut": cutoff}).fetchall()

        all_claims = db.execute(text("""
            SELECT id, text FROM claims
            WHERE page_id = :pid AND trust_level IN ('accepted','consensus')
            ORDER BY created_at DESC LIMIT 20
        """), {"pid": page_id}).fetchall()

        if not new_claims:
            return {"page_id": page_id, "skipped": "no_new_claims"}

        new_claims_block = "\n".join(f"[{c.id}] {c.text[:300]}" for c in new_claims)
        all_claims_block = "\n".join(f"[{c.id}] {c.text[:200]}" for c in all_claims) or "(none)"

        prompt = HERO_REFRESH_PROMPT.format(
            title=page.title, tagline=page.hero_tagline or "",
            new_claims_block=new_claims_block[:3000],
            all_claims_block=all_claims_block[:2000],
        )

        try:
            import anthropic
            client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
            est_tokens = {"input": max(1, len(prompt) // 4), "output": 512}
            dispatch_premium("research_ideas.opus_hero_refresh", "claude-opus-4-8", est_tokens)
            response = client.messages.create(
                model="claude-opus-4-8",
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}],
            )
            usage = getattr(response, "usage", None)
            log_llm_spend(
                "research_ideas.opus_hero_refresh",
                "claude-opus-4-8",
                prompt_tokens=getattr(usage, "input_tokens", None),
                completion_tokens=getattr(usage, "output_tokens", None),
                estimated_tokens=est_tokens["input"],
            )
            raw = response.content[0].text
        except Exception as exc:
            log.warning("[opus_hero_refresh] Opus API failed: %s", exc)
            return {"page_id": page_id, "error": str(exc)}

        parsed = _parse_json_block(raw) if raw else None
        if not isinstance(parsed, dict):
            return {"page_id": page_id, "error": "parse_failed"}

        new_tagline = parsed.get("hero_tagline", "").strip()
        new_facts   = parsed.get("hero_facts", [])
        if not new_tagline or not new_facts:
            return {"page_id": page_id, "error": "empty_response"}

        db.execute(text("""
            UPDATE wiki_pages
            SET hero_tagline = :tl, hero_facts = :hf, updated_at = NOW()
            WHERE id = :pid
        """), {
            "pid": page_id,
            "tl":  new_tagline[:300],
            "hf":  json.dumps(new_facts[:3]),
        })
        db.commit()
        log.info("[opus_hero_refresh] page=%d tagline refreshed", page_id)
        return {"page_id": page_id, "new_tagline": new_tagline[:100]}
    except Exception as exc:
        db.rollback()
        log.exception("[opus_hero_refresh] failed: %s", exc)
        raise
    finally:
        db.close()


# backward-compat alias so existing beat entries don't break during rollout
astrosage_hero_refresh = opus_hero_refresh


RAKON_SYNTHESIS_PROMPT = """\
You are an expert astronomy wiki editor. Rewrite the following wiki section with maximum scientific depth and rigor.

PAGE: {title}

CURRENT SECTION:
{current_section}

ACCEPTED CLAIMS (for context):
{claims_block}

RECENT LITERATURE (last 90d):
{arxiv_block}

REQUIREMENTS:
- Keep the ## header unchanged; rewrite everything below it
- Minimum 400 words below the header
- At least 3 quantitative facts (numbers, redshifts, masses, percentages, timescales)
- Every major claim cited inline as (Author et al. YYYY) or [arXiv:YYYY.NNNNN]
- Surface active debates explicitly with named positions
- No filler phrases: 'plays a crucial role', 'complex and dynamic', 'remains to be seen'

Return the rewritten section in markdown only (no JSON wrapper, no preamble).
"""


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.rakon_synthesis_pass", bind=True, max_retries=0)
def rakon_synthesis_pass(self, page_id: int | None = None):
    """R4-v3: Rakon (671b) directly authors a section rewrite proposal — delta_q tracked."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}

    provenance_mode = (
        getattr(settings, "AUTOWIKI_PROVENANCE_GATE_MODE", "shadow") or "shadow"
    ).strip().lower()
    if provenance_mode == "enforce":
        log.info(
            "[rakon_synthesis_pass] skipped page=%s: provenance enforce suppresses direct section_rewrite",
            page_id,
        )
        return {
            "skip": "provenance_enforce_suppressed_direct_section_rewrite",
            "page_id": page_id,
        }

    if not _rakon_lock_acquire(28800):
        return {"skip": "rakon_lock_held"}

    import re
    from app.database import SessionLocal
    from sqlalchemy import text
    from app.models.autowiki import AutowikiRun

    started_at = datetime.datetime.utcnow()
    db = SessionLocal()
    try:
        page = db.execute(
            text("SELECT id, slug, title, content FROM wiki_pages WHERE id = :pid"),
            {"pid": page_id},
        ).fetchone()
        if not page:
            return {"error": "page_not_found"}

        claims = db.execute(text(
            "SELECT text, trust_level FROM claims WHERE page_id = :pid"
            " ORDER BY CASE trust_level WHEN 'consensus' THEN 1 WHEN 'accepted' THEN 2 ELSE 3 END LIMIT 15"
        ), {"pid": page_id}).fetchall()
        claims_block = "\n".join(f"[{c.trust_level}] {c.text[:150]}" for c in claims) or "(none)"

        cutoff_str = (datetime.datetime.utcnow() - datetime.timedelta(days=90)).strftime("%Y-%m-%d")
        arxiv_rows = db.execute(text(
            "SELECT arxiv_id, title, abstract FROM arxiv_papers"
            " WHERE related_pages::jsonb ? :slug AND submitted >= :cut"
            " ORDER BY submitted DESC LIMIT 8"
        ), {"slug": page.slug, "cut": cutoff_str}).fetchall()
        arxiv_block = "\n".join(
            f"[{a.arxiv_id}] {a.title}: {(a.abstract or '')[:200]}" for a in arxiv_rows
        ) or "(none)"

        # Pick section (round-robin over ## headers)
        sections = re.findall(r"^## (.+)$", page.content, re.MULTILINE)
        if not sections:
            return {"skip": "no_sections"}
        rewrite_count = db.execute(text(
            "SELECT COUNT(*) FROM autowiki_runs WHERE page_id = :pid AND proposal_type = 'section_rewrite'"
        ), {"pid": page_id}).scalar() or 0
        section_header = sections[rewrite_count % len(sections)]

        # Extract current section text
        section_lines: list[str] = []
        in_section = False
        for line in page.content.split("\n"):
            if line.startswith("## ") and section_header in line:
                in_section = True
            elif line.startswith("## ") and in_section:
                break
            if in_section:
                section_lines.append(line)
        current_section = "\n".join(section_lines[:60])

        # Pre-warm Rakon (blocks up to 1800s on cold-load)
        rakon_alive = _rakon_prewarm()
        model = MODEL_RAKON if rakon_alive else MODEL_BUDDLE
        base_url = OLLAMA_MACPRO if model == MODEL_RAKON else OLLAMA_BUDDLE
        _timeout = 28800 if model == MODEL_RAKON else 1800

        prompt = RAKON_SYNTHESIS_PROMPT.format(
            title=page.title,
            current_section=current_section[:2000],
            claims_block=claims_block[:2000],
            arxiv_block=arxiv_block[:1500],
        )
        raw = _ollama_chat(base_url, model, prompt, temperature=0.5, timeout=_timeout)

        if not raw or len(raw) < 200:
            run = AutowikiRun(
                page_id=page_id, started_at=started_at, finished_at=datetime.datetime.utcnow(),
                proposal_type="section_rewrite", model_proposer=model,
                decision="gate_reject", reject_reason="rakon output too short or empty",
            )
            db.add(run)
            db.commit()
            return {"skip": "empty_output", "model": model}

        # Rebuild page content with the new section replacing the old one
        new_section_text = raw.strip()
        if not new_section_text.startswith("## "):
            new_section_text = f"## {section_header}\n\n{new_section_text}"

        new_parts: list[str] = []
        in_sec = False
        replaced = False
        for line in page.content.split("\n"):
            if line.startswith("## ") and section_header in line and not replaced:
                in_sec = True
                new_parts.append(new_section_text)
                replaced = True
            elif line.startswith("## ") and in_sec:
                in_sec = False
                new_parts.append(line)
            elif not in_sec:
                new_parts.append(line)
        new_content = "\n".join(new_parts)

        if not replaced:
            return {"skip": "section_not_found"}

        # Commit gate: body must be substantive. Do NOT compute delta_q via Python
        # dims — those metrics are inconsistent with the LLM judge in autowiki_tick.
        # Leave q0/q1/delta_q as None; autowiki_tick will score the committed content.
        section_body = new_section_text.split("\n", 1)[-1] if "\n" in new_section_text else ""
        if len(section_body.strip()) < 200:
            run = AutowikiRun(
                page_id=page_id, started_at=started_at, finished_at=datetime.datetime.utcnow(),
                proposal_type="section_rewrite", model_proposer=model,
                decision="gate_reject", reject_reason="section body < 200 chars after header",
            )
            db.add(run)
            db.commit()
            return {"skip": "body_too_short", "model": model}

        db.execute(text(
            "UPDATE wiki_pages SET content = :c, updated_at = NOW() WHERE id = :pid"
        ), {"c": new_content, "pid": page_id})

        run = AutowikiRun(
            page_id=page_id, started_at=started_at, finished_at=datetime.datetime.utcnow(),
            proposal_type="section_rewrite", model_proposer=model,
            decision="commit",
            judge_rationale=f"rakon_synthesis section='{section_header}' body_len={len(section_body)}",
            judge_prompt_version="rakon_synthesis_v1",
        )
        db.add(run)
        db.commit()
        log.info("[rakon_synthesis_pass] page=%d section='%s' body_len=%d decision=commit model=%s",
                 page_id, section_header, len(section_body), model)
        return {"page_id": page_id, "section": section_header, "decision": "commit", "model": model}
    except Exception as exc:
        db.rollback()
        log.exception("[rakon_synthesis_pass] failed: %s", exc)
        raise
    finally:
        _rakon_lock_release()
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.buddle_claim_propose", bind=True, max_retries=0)
def buddle_claim_propose(self, page_id: int | None = None):
    """B4-v3: Buddle proposes new claims from orphan high-value research idea signals."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    provenance_mode = (
        getattr(settings, "AUTOWIKI_PROVENANCE_GATE_MODE", "shadow") or "shadow"
    ).strip().lower()
    if provenance_mode == "enforce":
        return {
            "skip": "provenance_enforce_suppressed_direct_claim_insert",
            "page_id": page_id,
        }

    from app.database import SessionLocal
    from sqlalchemy import text
    from app.models.autowiki import AutowikiRun

    started_at = datetime.datetime.utcnow()
    db = SessionLocal()
    inserted = 0
    try:
        # Orphan ideas: high-value drafts/actives with no claim anchor on this page
        orphan_ideas = db.execute(text("""
            SELECT ri.id, ri.question, ri.why_now, ri.approach, ri.survey_combo
            FROM research_ideas ri
            WHERE ri.page_id = :pid
              AND ri.status IN ('draft', 'active')
              AND ri.novelty >= 0.6
              AND NOT EXISTS (
                  SELECT 1 FROM research_idea_anchors a
                  WHERE a.idea_id = ri.id AND a.kind = 'claim'
              )
            ORDER BY ri.novelty DESC LIMIT 3
        """), {"pid": page_id}).fetchall()

        if not orphan_ideas:
            return {"page_id": page_id, "inserted": 0, "note": "no_orphan_ideas"}

        page = db.execute(
            text("SELECT id, slug, title FROM wiki_pages WHERE id = :pid"), {"pid": page_id}
        ).fetchone()
        if not page:
            return {"error": "page_not_found"}

        for idea in orphan_ideas:
            prompt = (
                f"PAGE: {page.title}\n\n"
                f"RESEARCH IDEA:\n"
                f"Question: {idea.question}\n"
                f"Why now: {idea.why_now}\n"
                f"Approach: {idea.approach}\n\n"
                "Draft a single authoritative claim statement (1-2 sentences) that this research idea "
                "implies or builds upon. The claim should be a scientific assertion about the current "
                "state of knowledge, suitable for an astronomy research wiki.\n\n"
                'Return JSON: {"claim_text": "...", "rationale": "..."}'
            )
            raw = _ollama_chat(OLLAMA_BUDDLE, MODEL_BUDDLE, prompt, temperature=0.3, timeout=900)
            parsed = _parse_json_block(raw) if raw else None
            if not isinstance(parsed, dict):
                continue
            claim_text = parsed.get("claim_text", "").strip()
            if not claim_text or len(claim_text) < 20:
                continue

            db.execute(text("""
                INSERT INTO claims
                  (page_id, text, trust_level, claim_type, section, order_idx, created_at, updated_at)
                VALUES (:pid, :txt, 'debated', 'subtopic', 'Open Questions and Active Debates',
                        COALESCE((SELECT MAX(order_idx) FROM claims WHERE page_id = :pid), 0) + 1,
                        NOW(), NOW())
                ON CONFLICT DO NOTHING
            """), {"pid": page_id, "txt": claim_text[:500]})
            inserted += 1

        run = AutowikiRun(
            page_id=page_id, started_at=started_at, finished_at=datetime.datetime.utcnow(),
            proposal_type="claim_insert_subtopic", model_proposer=MODEL_BUDDLE,
            decision="commit" if inserted > 0 else "gate_reject",
            judge_rationale=f"buddle_claim_propose inserted={inserted} from {len(orphan_ideas)} orphan ideas",
        )
        db.add(run)
        db.commit()
        log.info("[buddle_claim_propose] page=%d inserted=%d", page_id, inserted)
        return {"page_id": page_id, "inserted": inserted}
    except Exception as exc:
        db.rollback()
        log.exception("[buddle_claim_propose] failed: %s", exc)
        raise
    finally:
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.mima_cross_page_synthesis", bind=True, max_retries=0)
def mima_cross_page_synthesis(self, page_id: int | None = None):
    """M4: Mima computes cross-page claim similarity; emits ClaimMigrationProposal when similarity > 0.7."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    if _provenance_enforce_enabled():
        return {
            "skip": "provenance_enforce_suppressed_claim_migration_proposals",
            "page_id": page_id,
        }

    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    proposals = 0
    try:
        src_claims = db.execute(text(
            "SELECT id, text FROM claims WHERE page_id = :pid AND trust_level IN ('accepted','consensus')"
        ), {"pid": page_id}).fetchall()

        if not src_claims:
            return {"page_id": page_id, "proposals": 0}

        # Pick top-5 other pages by claim count
        other_pages = db.execute(text("""
            SELECT wp.id, wp.title, array_agg(c.text ORDER BY c.created_at DESC) FILTER (WHERE c.id IS NOT NULL) AS claim_texts
            FROM wiki_pages wp
            LEFT JOIN claims c ON c.page_id = wp.id AND c.trust_level IN ('accepted','consensus')
            WHERE wp.id != :pid
            GROUP BY wp.id, wp.title
            ORDER BY COUNT(c.id) DESC LIMIT 5
        """), {"pid": page_id}).fetchall()

        for other in other_pages:
            if not other.claim_texts:
                continue
            other_text = " ".join(t for t in other.claim_texts if t)[:3000]

            for src in src_claims:
                sim = _tfidf_cosine(src.text, other_text)
                if sim < 0.7:
                    continue
                # Emit ClaimMigrationProposal
                try:
                    db.execute(text("""
                        INSERT INTO claim_migration_proposals
                          (claim_id, target_page_id, rationale, proposer_model, status, created_at)
                        VALUES (:cid, :tpid, :rat, :model, 'pending', NOW())
                        ON CONFLICT DO NOTHING
                    """), {
                        "cid":   src.id,
                        "tpid":  other.id,
                        "rat":   f"TF-IDF cosine={sim:.2f} vs page '{other.title}'",
                        "model": MODEL_MIMA,
                    })
                    proposals += 1
                except Exception as e:
                    log.debug("[mima_cross_page_synthesis] insert failed: %s", e)

        db.commit()
        log.info("[mima_cross_page_synthesis] page=%d proposals=%d", page_id, proposals)
        return {"page_id": page_id, "proposals": proposals}
    except Exception as exc:
        db.rollback()
        log.exception("[mima_cross_page_synthesis] failed: %s", exc)
        raise
    finally:
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.tera_coverage_audit", bind=True, max_retries=0)
def tera_coverage_audit(self, page_id: int | None = None):
    """T2: Tera 128k full-page coverage audit → CoverageReport."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    if _provenance_enforce_enabled():
        return {
            "skip": "provenance_enforce_suppressed_coverage_audit",
            "page_id": page_id,
        }

    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    try:
        ctx = _build_page_context(db, page_id, full=True, max_arxiv=30)
        if not ctx:
            return {"error": "page_not_found"}

        claims_block = "\n".join(f"[{c['id']}] ({c['trust']}) {c['text'][:300]}" for c in ctx["claims"]) or "(none)"
        arxiv_block  = "\n".join(f"[{a['arxiv_id']}] {a['title']}: {a['abstract'][:400]}" for a in ctx["arxiv"]) or "(none)"

        prompt = TERA_GAP_PROMPT.format(
            title=ctx["title"],
            page_content=ctx["content"][:80000],
            claim_count=len(ctx["claims"]),
            claims_block=claims_block[:8000],
            arxiv_block=arxiv_block[:8000],
        )
        raw = _ollama_chat(OLLAMA_LOCAL, MODEL_TERA, prompt, temperature=0.2, timeout=1800)
        parsed = _parse_json_block(raw) if raw else None
        if not isinstance(parsed, dict):
            return {"page_id": page_id, "error": "parse_failed"}

        db.execute(text("""
            INSERT INTO coverage_reports
              (page_id, generated_at, generator_model, missing_subtopics_jsonb,
               split_merge_suggestions_jsonb, orphan_section_flags_jsonb)
            VALUES (:pid, NOW(), :model, :ms, :sm, :os)
        """), {
            "pid": page_id, "model": MODEL_TERA,
            "ms": json.dumps(parsed.get("missing_subtopics", [])),
            "sm": json.dumps(parsed.get("split_merge_suggestions", [])),
            "os": json.dumps(parsed.get("orphan_section_flags", [])),
        })
        db.commit()
        log.info("[tera_coverage_audit] page=%d saved", page_id)
        return {"page_id": page_id, "missing": len(parsed.get("missing_subtopics", []))}
    except Exception as exc:
        db.rollback()
        log.exception("[tera_coverage_audit] failed: %s", exc)
        raise
    finally:
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.tera_evidence_audit", bind=True, max_retries=0)
def tera_evidence_audit(self, page_id: int | None = None):
    """T3: Tera verifies claim-evidence relationships for stale evidence (>30 days, no audit)."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    if _provenance_enforce_enabled():
        return {
            "skip": "provenance_enforce_suppressed_evidence_mismatch_audit",
            "page_id": page_id,
        }

    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    mismatches = 0
    try:
        cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=30)
        evidence_rows = db.execute(text("""
            SELECT ev.id, ev.claim_id, ev.arxiv_id, ev.title, ev.abstract, ev.stance,
                   c.text AS claim_text
            FROM evidence ev
            JOIN claims c ON c.id = ev.claim_id
            WHERE c.page_id = :pid
              AND ev.created_at < :cut
              AND NOT EXISTS (
                SELECT 1 FROM evidence_mismatches em WHERE em.evidence_link_id = ev.id
              )
            ORDER BY ev.created_at ASC LIMIT 20
        """), {"pid": page_id, "cut": cutoff}).fetchall()

        for ev in evidence_rows:
            prompt = (
                f"CLAIM: {ev.claim_text[:400]}\n\n"
                f"EVIDENCE (stance={ev.stance}): {ev.title}\n{(ev.abstract or '')[:600]}\n\n"
                "Does this evidence actually SUPPORT the claim with the stated stance? "
                "Output JSON: {\"match\": true|false, \"reason\": \"<one sentence>\"}"
            )
            raw = _ollama_chat(OLLAMA_LOCAL, MODEL_TERA, prompt, temperature=0.1, timeout=120)
            parsed = _parse_json_block(raw) if raw else None
            if not isinstance(parsed, dict):
                continue
            if not parsed.get("match", True):
                try:
                    db.execute(text("""
                        INSERT INTO evidence_mismatches
                          (evidence_link_id, mismatch_reason, detected_by_model, detected_at)
                        VALUES (:eid, :reason, :model, NOW())
                        ON CONFLICT DO NOTHING
                    """), {
                        "eid":    ev.id,
                        "reason": parsed.get("reason", "")[:500],
                        "model":  MODEL_TERA,
                    })
                    mismatches += 1
                except Exception as e:
                    log.debug("[tera_evidence_audit] insert failed: %s", e)

        db.commit()
        log.info("[tera_evidence_audit] page=%d mismatches=%d", page_id, mismatches)
        return {"page_id": page_id, "audited": len(evidence_rows), "mismatches": mismatches}
    except Exception as exc:
        db.rollback()
        log.exception("[tera_evidence_audit] failed: %s", exc)
        raise
    finally:
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.nutty_trust_recompute", bind=True, max_retries=0)
def nutty_trust_recompute(self):
    """N5: For each EvidenceLink created in last 70 min, recompute parent Claim.trust_level."""
    if _provenance_enforce_enabled():
        return {"skip": "provenance_enforce_suppressed_trust_recompute"}

    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    updated = 0
    try:
        cutoff = datetime.datetime.utcnow() - datetime.timedelta(minutes=70)
        recent_ev = db.execute(text("""
            SELECT DISTINCT ev.claim_id
            FROM evidence ev
            WHERE ev.created_at >= :cut
        """), {"cut": cutoff}).fetchall()

        for row in recent_ev:
            cid = row.claim_id
            claim = db.execute(
                text("SELECT id, text FROM claims WHERE id = :id"), {"id": cid}
            ).fetchone()
            if not claim:
                continue

            supports = db.execute(text("""
                SELECT title, abstract FROM evidence WHERE claim_id = :cid AND stance = 'supports'
                LIMIT 5
            """), {"cid": cid}).fetchall()
            contras = db.execute(text("""
                SELECT title, abstract FROM evidence WHERE claim_id = :cid AND stance = 'contradicts'
                LIMIT 5
            """), {"cid": cid}).fetchall()

            support_block = "\n".join(f"- {e.title}: {(e.abstract or '')[:200]}" for e in supports) or "(none)"
            contra_block  = "\n".join(f"- {e.title}: {(e.abstract or '')[:200]}" for e in contras) or "(none)"

            prompt = NUTTY_TRUST_PROMPT.format(
                claim_text=claim.text[:400],
                support_count=len(supports), support_block=support_block,
                contra_count=len(contras), contra_block=contra_block,
            )
            raw = _ollama_chat(OLLAMA_LOCAL, MODEL_NUTTY, prompt, temperature=0.1, timeout=90)
            if not raw:
                continue

            raw_stripped = strip_think_blocks(raw).lower()
            valid_levels = {"consensus", "accepted", "debated", "contested", "retracted"}
            new_trust = next((lvl for lvl in valid_levels if lvl in raw_stripped), None)
            if new_trust:
                db.execute(text(
                    "UPDATE claims SET trust_level = :tl, updated_at = NOW() WHERE id = :id"
                ), {"tl": new_trust, "id": cid})
                updated += 1

        db.commit()
        log.info("[nutty_trust_recompute] updated=%d", updated)
        return {"updated": updated}
    except Exception as exc:
        db.rollback()
        log.exception("[nutty_trust_recompute] failed: %s", exc)
        raise
    finally:
        db.close()


@shared_task(name="app.agent_loop.research_ideas.auto_improvement.takji_schema_validate", bind=True, max_retries=0)
def takji_schema_validate(self, page_id: int | None = None):
    """K3: Takji sweeps JSONB columns for schema violations and emits SchemaViolation rows."""
    if page_id is None:
        page_id = _pick_next_priority_page()
    if page_id is None:
        return {"skip": "no_page"}
    if _provenance_enforce_enabled():
        return {
            "skip": "provenance_enforce_suppressed_schema_validate",
            "page_id": page_id,
        }

    from app.database import SessionLocal
    from sqlalchemy import text
    db = SessionLocal()
    fixed = 0
    violations = 0

    # Expected keys per JSONB column
    IDEA_REQUIRED = {"novelty", "feasibility"}
    EVIDENCE_META_DEFAULTS: dict = {}

    try:
        # Sweep research_ideas.systematics_json
        ideas = db.execute(text(
            "SELECT id, systematics_json FROM research_ideas WHERE page_id = :pid"
        ), {"pid": page_id}).fetchall()

        for idea in ideas:
            sj = idea.systematics_json
            if sj is None:
                continue
            if isinstance(sj, str):
                try:
                    sj = json.loads(sj)
                except Exception:
                    try:
                        db.execute(text("""
                            INSERT INTO schema_violations
                              (table_name, row_id, violation_kind, auto_fixed, flagged_for_hwao, created_at)
                            VALUES ('research_ideas', :rid, 'systematics_json_invalid_json', FALSE, TRUE, NOW())
                            ON CONFLICT DO NOTHING
                        """), {"rid": idea.id})
                        violations += 1
                    except Exception:
                        pass
                    continue

        # Sweep autowiki_runs.idea_signals_json for required keys
        runs = db.execute(text("""
            SELECT id, idea_signals_json FROM autowiki_runs
            WHERE page_id = :pid AND idea_signals_json IS NOT NULL
            ORDER BY id DESC LIMIT 50
        """), {"pid": page_id}).fetchall()

        for run in runs:
            sig = run.idea_signals_json
            if not isinstance(sig, dict):
                continue
            missing_keys = {"claim_boosts", "orphan_count"} - set(sig.keys())
            if missing_keys:
                try:
                    # Auto-fix: set defaults
                    fixed_sig = dict(sig)
                    if "claim_boosts" not in fixed_sig:
                        fixed_sig["claim_boosts"] = {}
                    if "orphan_count" not in fixed_sig:
                        fixed_sig["orphan_count"] = 0
                    db.execute(text(
                        "UPDATE autowiki_runs SET idea_signals_json = :sig WHERE id = :id"
                    ), {"sig": json.dumps(fixed_sig), "id": run.id})
                    fixed += 1
                except Exception as e:
                    log.debug("[takji_schema_validate] auto-fix failed: %s", e)

        # Emit SchemaViolation for idea_signals that have non-dict claim_boosts
        for run in runs:
            sig = run.idea_signals_json
            if isinstance(sig, dict) and not isinstance(sig.get("claim_boosts"), dict):
                try:
                    db.execute(text("""
                        INSERT INTO schema_violations
                          (table_name, row_id, violation_kind, auto_fixed, flagged_for_hwao, created_at)
                        VALUES ('autowiki_runs', :rid, 'idea_signals_json.claim_boosts_not_dict', FALSE, FALSE, NOW())
                        ON CONFLICT DO NOTHING
                    """), {"rid": run.id})
                    violations += 1
                except Exception:
                    pass

        db.commit()
        log.info("[takji_schema_validate] page=%d fixed=%d violations=%d", page_id, fixed, violations)
        return {"page_id": page_id, "fixed": fixed, "violations": violations}
    except Exception as exc:
        db.rollback()
        log.exception("[takji_schema_validate] failed: %s", exc)
        raise
    finally:
        db.close()


# ── Debated-claim idea seeder ──────────────────────────────────────────────────

RAKON_LOCK_KEY = "rakon:lock"
RAKON_LOCK_TTL = 14400  # 4h

DEBATED_CLAIM_SEEDER_PROMPT = """\
You are an astronomy research strategist. A specific claim on the Wikipedia-style page \
"{page_title}" is currently {trust_level}. Generate {n_ideas} testable research \
questions that would help resolve this specific disagreement.

THE CONTESTED CLAIM
-------------------
{claim_text}

EVIDENCE ALREADY ON FILE FOR THIS CLAIM
---------------------------------------
{evidence_block}

RECENT RELEVANT LITERATURE (last 12 mo)
---------------------------------------
{arxiv_block}

EXISTING IDEAS ALREADY ANCHORED TO THIS CLAIM (avoid duplicating)
-----------------------------------------------------------------
{existing_anchored_block}

REQUIREMENTS
------------
For each idea:
- question: a 1-2 sentence research question that would discriminate between the
            disputed positions. Must reference the specific claim.
- why_now: 1 sentence on what makes this answerable in 2024-2026.
- approach: 1-2 sentences naming the concrete dataset, survey, simulation suite,
            or experimental technique. Must be a REAL named dataset/instrument.
- combo: two real astronomy survey names joined with '+' (e.g. "JWST+ALMA").
- systematics_json: {{}}
- novelty: do NOT propose ideas covered by the existing anchored ideas above.
- anchors: {{"claim_ids": [{claim_id}], "debate_ids": [], "arxiv_ids": []}}

Return JSON: {{"drafts": [{{"question": "...", "why_now": "...", "approach": "...",
                          "combo": "...", "systematics_json": {{}},
                          "anchors": {{"claim_ids": [{claim_id}], "debate_ids": [], "arxiv_ids": []}}
                          }}]}}
"""


def _acquire_rakon_lock() -> bool:
    """Attempt to acquire the rakon mutex. Returns True if acquired."""
    try:
        r = _redis()
        return r.set(RAKON_LOCK_KEY, "debated_claim_seed", ex=RAKON_LOCK_TTL, nx=True) is True
    except Exception:
        return False


def _release_rakon_lock() -> None:
    try:
        _redis().delete(RAKON_LOCK_KEY)
    except Exception:
        pass


def _generate_ideas_for_claim(claim_id: int, claim_text: str, trust_level: str,
                               page_title: str, evidence_block: str, arxiv_block: str,
                               existing_anchored_block: str, n_ideas: int = 3) -> list:
    """Call Rakon→Buddle→Mima fallback chain; return list of skeleton dicts."""
    prompt = DEBATED_CLAIM_SEEDER_PROMPT.format(
        page_title=page_title,
        trust_level=trust_level,
        n_ideas=n_ideas,
        claim_text=claim_text[:600],
        evidence_block=evidence_block[:800],
        arxiv_block=arxiv_block[:1200],
        existing_anchored_block=existing_anchored_block[:600],
        claim_id=claim_id,
    )

    # Try Rakon (deepseek-r1:671b on Mac Pro) first
    rakon_alive = _check_ollama_alive(OLLAMA_MACPRO, MODEL_RAKON)
    if rakon_alive:
        raw = _ollama_chat(OLLAMA_MACPRO, MODEL_RAKON, prompt, temperature=0.5, timeout=28800)
        if raw:
            parsed = _parse_json_block(raw)
            drafts = (parsed or {}).get("drafts", []) if isinstance(parsed, dict) else []
            if drafts:
                log.info("[seed_claim] claim=%d model=rakon got %d drafts", claim_id, len(drafts))
                return drafts

    # Buddle fallback on Mac Studio
    buddle_alive = _check_ollama_alive(OLLAMA_BUDDLE, MODEL_BUDDLE)
    if buddle_alive:
        raw = _ollama_chat(OLLAMA_BUDDLE, MODEL_BUDDLE, prompt, temperature=0.5, timeout=1800)
        if raw:
            parsed = _parse_json_block(raw)
            drafts = (parsed or {}).get("drafts", []) if isinstance(parsed, dict) else []
            if drafts:
                log.info("[seed_claim] claim=%d model=buddle got %d drafts", claim_id, len(drafts))
                return drafts

    # Mima fallback (qwen3.6:35b-a3b-nvfp4 on Mac Studio)
    raw = _ollama_chat(OLLAMA_LOCAL, MODEL_MIMA, prompt, temperature=0.5, timeout=1800)
    if raw:
        parsed = _parse_json_block(raw)
        drafts = (parsed or {}).get("drafts", []) if isinstance(parsed, dict) else []
        if drafts:
            log.info("[seed_claim] claim=%d model=mima got %d drafts", claim_id, len(drafts))
            return drafts

    log.warning("[seed_claim] claim=%d all models failed", claim_id)
    return []


@shared_task(
    name="app.agent_loop.research_ideas.auto_improvement.seed_debated_claim_ideas",
    bind=True, max_retries=0,
)
def seed_debated_claim_ideas(self, page_id: int, target_per_claim: int = 3):
    """Seed research ideas anchored to debated/challenged claims with < target_per_claim active ideas."""
    if _provenance_enforce_enabled():
        return {
            "skipped": "provenance_enforce_suppressed_debated_claim_seed",
            "page_id": page_id,
        }

    from app.database import SessionLocal
    from sqlalchemy import text

    if not _acquire_rakon_lock():
        log.info("[seed_claim] rakon:lock held — skipping tick page_id=%d", page_id)
        return {"skipped": "rakon_locked"}

    db = SessionLocal()
    claims_visited = 0
    ideas_generated = 0
    per_claim_counts: dict = {}

    try:
        page_row = db.execute(
            text("SELECT title FROM wiki_pages WHERE id = :pid"), {"pid": page_id}
        ).fetchone()
        if not page_row:
            return {"error": "page_not_found"}
        page_title = page_row.title

        # Build candidate list: debated/challenged claims with < target_per_claim active ideas
        candidates = db.execute(text("""
            SELECT c.id, c.text, c.trust_level, COUNT(ri.id) AS idea_count
            FROM claims c
            LEFT JOIN research_ideas ri
              ON ri.claim_id = c.id AND ri.status IN ('active', 'draft', 'saved')
            WHERE c.page_id = :page_id
              AND c.trust_level IN ('debated', 'challenged')
            GROUP BY c.id, c.text, c.trust_level
            HAVING COUNT(ri.id) < :target
            ORDER BY c.trust_level DESC, COUNT(ri.id) ASC, c.id ASC
            LIMIT 5
        """), {"page_id": page_id, "target": target_per_claim}).fetchall()

        if not candidates:
            log.info("[seed_claim] no candidates for page_id=%d (gap already closed)", page_id)
            _log_autowiki_run(db, page_id, "debated_claim_seed",
                              claims_visited=0, ideas_generated=0, per_claim_counts={})
            db.commit()
            return {"claims_visited": 0, "ideas_generated": 0}

        for claim in candidates:
            claims_visited += 1
            claim_id = claim.id

            # Fetch supporting/contradicting evidence for this claim
            ev_rows = db.execute(text("""
                SELECT e.title, e.abstract, e.stance
                FROM evidence e
                WHERE e.claim_id = :cid AND e.abstract IS NOT NULL
                ORDER BY e.created_at DESC LIMIT 5
            """), {"cid": claim_id}).fetchall()
            evidence_block = "\n".join(
                f"[{e.stance}] {e.title}: {(e.abstract or '')[:200]}" for e in ev_rows
            ) or "(no evidence on file)"

            # Fetch recent arxiv papers (GA category preferred)
            arxiv_rows = db.execute(text("""
                SELECT arxiv_id, title, abstract
                FROM arxiv_papers
                WHERE category LIKE '%astro-ph%'
                ORDER BY submitted DESC LIMIT 5
            """)).fetchall()
            arxiv_block = "\n".join(
                f"[{a.arxiv_id}] {a.title}: {(a.abstract or '')[:250]}" for a in arxiv_rows
            ) or "(none)"

            # Fetch existing ideas already anchored to this claim (for dedup)
            anchored_rows = db.execute(text("""
                SELECT ri.question
                FROM research_ideas ri
                WHERE ri.claim_id = :cid OR EXISTS (
                    SELECT 1 FROM research_idea_anchors a
                    WHERE a.idea_id = ri.id AND a.kind = 'claim' AND a.ref_id = :cid_str
                )
            """), {"cid": claim_id, "cid_str": str(claim_id)}).fetchall()
            existing_anchored_block = "\n".join(
                f"- {r.question[:150]}" for r in anchored_rows
            ) or "(none)"

            # Generate ideas
            drafts = _generate_ideas_for_claim(
                claim_id=claim_id,
                claim_text=claim.text,
                trust_level=claim.trust_level,
                page_title=page_title,
                evidence_block=evidence_block,
                arxiv_block=arxiv_block,
                existing_anchored_block=existing_anchored_block,
                n_ideas=target_per_claim - claim.idea_count,
            )

            committed_this_claim = 0
            for skel in drafts:
                # Normalize skeleton to match _validate_skeleton / _persist_draft expectations
                if not isinstance(skel, dict):
                    continue
                # combo may be missing if model didn't follow schema — default to JWST+ALMA
                if not skel.get("combo"):
                    skel["combo"] = "JWST+ALMA"
                if not _validate_skeleton(skel):
                    continue

                # Build existing ideas list for atom scoring
                existing_ideas = [{"question": r.question, "combo": "", "why_now": "", "approach": ""}
                                   for r in anchored_rows]
                score = _atom_score(skel, existing_ideas)
                if score is None:
                    log.warning("[seed_claim] atom score failed for claim=%d, persisting without score", claim_id)
                    score = {"novelty": 0.5, "feasibility": 0.5}

                if score.get("novelty", 0) < NOVELTY_FLOOR:
                    continue
                if score.get("dedup_cosine_estimate", 0) >= DEDUP_COSINE_THRESHOLD:
                    continue

                # Ensure claim anchors are present in skel
                if not skel.get("anchors"):
                    skel["anchors"] = {}
                if claim_id not in (skel["anchors"].get("claim_ids") or []):
                    skel["anchors"].setdefault("claim_ids", []).append(claim_id)

                # Persist draft (uses existing _persist_draft which writes anchor rows)
                _persist_draft(db, page_id, skel, score, "debated_claim_seed", str(claim_id))

                # Belt-and-suspenders: also set claim_id direct FK
                nested = db.begin_nested()
                try:
                    last_id = db.execute(text(
                        "SELECT id FROM research_ideas WHERE page_id=:pid ORDER BY id DESC LIMIT 1"
                    ), {"pid": page_id}).fetchone()
                    if last_id:
                        db.execute(text(
                            "UPDATE research_ideas SET claim_id=:cid WHERE id=:iid AND claim_id IS NULL"
                        ), {"cid": claim_id, "iid": last_id.id})
                    nested.commit()
                except Exception:
                    nested.rollback()

                committed_this_claim += 1
                ideas_generated += 1

            per_claim_counts[str(claim_id)] = committed_this_claim
            log.info("[seed_claim] page=%d claim=%d trust=%s ideas_committed=%d",
                     page_id, claim_id, claim.trust_level, committed_this_claim)

        _log_autowiki_run(db, page_id, "debated_claim_seed",
                          claims_visited=claims_visited,
                          ideas_generated=ideas_generated,
                          per_claim_counts=per_claim_counts)
        db.commit()
        log.info("[seed_claim] DONE page=%d claims=%d ideas=%d", page_id, claims_visited, ideas_generated)
        return {"claims_visited": claims_visited, "ideas_generated": ideas_generated,
                "per_claim_counts": per_claim_counts}

    except Exception as exc:
        db.rollback()
        log.exception("[seed_claim] failed page_id=%d: %s", page_id, exc)
        raise
    finally:
        _release_rakon_lock()
        db.close()


# ── Karpathy v2: gap-detection research idea generator ────────────────────────

_KV2_LOCK_TTL = 7200  # 2h — matches rakon:lock pattern

_KV2_GAP_TYPES = {"gap", "tension", "bridge", "frontier", "synergy"}

_KV2_OBSERVABLE_KEYWORDS = {
    "stellar mass", "sfr", "ssfr", "sérsic index", "sersic index",
    "velocity dispersion", "[oii] flux", "hα flux", "ha flux",
    "fir luminosity", "hi mass", "x-ray luminosity", "agn luminosity",
    "quenching fraction", "metallicity", "dust obscuration",
}

_KV2_SYSTEM_PROMPT = """\
You are an expert astrophysics research strategist. Your role is to read the \
current knowledge state of a NebulaMind wiki page and identify high-value research \
ideas by detecting what is missing, contested, or needs bridging.

You will receive:
1. A structured JSON object representing the full page state (sections, claims with \
trust scores, and existing research ideas).
2. A list of active surveys available for observational follow-up.

Your task: identify and output up to 15 research ideas, each addressing a specific \
knowledge gap. Classify each idea by gap_type: gap | tension | bridge | frontier | synergy.

RULES:
- Every idea MUST anchor to exactly one claim (anchor_claim_id) from the page state.
- Every idea MUST specify at least one survey instrument from the active surveys list.
- Every idea MUST include a redshift range.
- Every idea MUST name at least one physical observable (e.g., stellar mass, SFR, \
Sérsic index, [OII] flux).
- Do NOT repeat any idea already present in existing_ideas (check semantically, not just lexically).
- Prioritize ideas where claim trust_score < 0.7 or pro_count/con_count ratio < 3 (contested claims).
- For gap and frontier types, prioritize sections with the fewest claims relative to their body length.
- For tension type, explicitly identify the two conflicting claims by ID.
- For bridge type, identify the two sections being connected.
- For synergy type, name at least two distinct survey datasets and explain the observational leverage.

OUTPUT FORMAT: Return a JSON array only. No prose before or after.

Each element must have these fields:
question, why_now, approach, survey_combo, anchor_claim_id, secondary_claim_ids,
gap_type, conflicting_claim_ids, bridge_section_pair, redshift_range,
physical_observable, novelty, feasibility
"""

_KV2_ASTROSAGE_PROMPT = """\
You are an astrophysicist reviewing a research idea draft. Polish the listed prose \
fields for scientific accuracy and fluency. Fix any incorrect survey specifications, \
units, or physically implausible claims.

EDITABLE FIELDS (you may rewrite these):
  - question
  - why_now
  - approach

READ-ONLY FIELDS (return EXACTLY as given):
  - anchor_claim_id, secondary_claim_ids, gap_type, conflicting_claim_ids,
    bridge_section_pair, survey_combo, redshift_range, physical_observable,
    novelty, feasibility

If you detect an unsalvageable physics error, set question to "" and add
"reject_reason": "<one-line explanation>".

IDEA (JSON): {idea_json}

Return the same JSON structure with polished editable-field text only.
"""

_KV2_ATOM_PROMPT = """\
Score this astrophysics research idea on two axes:
- novelty (0-1): how new is the specific combination of survey + observable + redshift range?
- feasibility (0-1): can this be executed with currently available data and standard methods?

Consider the existing evidence corpus (provided as titles).

Return JSON: {{"novelty": float, "feasibility": float, "flag": "ok" or "too_similar" or "infeasible"}}

IDEA:
question: {question}
survey_combo: {survey_combo}
redshift_range: {redshift_range}
physical_observable: {physical_observable}

EXISTING EVIDENCE TITLES (for novelty context):
{evidence_titles}
"""


def _kv2_acquire_rakon_lock() -> bool:
    try:
        r = _redis()
        return r.set("rakon:lock", "karpathy_v2", ex=_KV2_LOCK_TTL, nx=True) is True
    except Exception:
        return False


def _kv2_release_rakon_lock() -> None:
    try:
        _redis().delete("rakon:lock")
    except Exception:
        pass


def _wait_until_cleared(key: str, timeout_sec: int = 300) -> bool:
    """Poll Redis key until gone or timeout. Returns True if cleared."""
    import time
    deadline = time.monotonic() + timeout_sec
    while time.monotonic() < deadline:
        try:
            if not _redis().exists(key):
                return True
        except Exception:
            return True  # fail open on Redis error
        time.sleep(10)
    return False


def _split_sections(content: str) -> list[dict]:
    """Split markdown content into sections by ## headings. Returns [{heading, body}]."""
    import re
    parts = re.split(r"(?m)^#{1,3}\s+(.+)$", content)
    # parts alternates: [pre-header text, heading1, body1, heading2, body2, ...]
    sections = []
    if parts[0].strip():
        sections.append({"heading": "Introduction", "body": parts[0].strip()})
    for i in range(1, len(parts) - 1, 2):
        heading = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ""
        if heading:
            sections.append({"heading": heading, "body": body})
    return sections or [{"heading": "Content", "body": content}]


def _truncate_to_words(text: str, max_words: int = 350) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + " …"


def _get_or_build_section_digest(r, page_id: int, idx: int, body: str) -> str:
    import hashlib
    section_hash = hashlib.md5(body.encode()).hexdigest()[:12]
    cache_key = f"digest:section:{page_id}:{idx}:{section_hash}"
    cached = r.get(cache_key)
    if cached:
        return cached
    digest = _truncate_to_words(body, max_words=350)
    r.setex(cache_key, 7 * 86400, digest)
    return digest


def _build_page_context_v2(db, r, page_id: int, page_slug: str) -> dict | None:
    from sqlalchemy import text

    # Sections from page content
    page_row = db.execute(
        text("SELECT content FROM wiki_pages WHERE id = :pid"), {"pid": page_id}
    ).fetchone()
    if not page_row:
        return None
    raw_sections = _split_sections(page_row.content or "")

    sections = []
    for idx, sec in enumerate(raw_sections):
        digest = _get_or_build_section_digest(r, page_id, idx, sec["body"])
        sections.append({"heading": sec["heading"], "body_digest": digest})

    # Claims with trust data
    claims = db.execute(text("""
        SELECT c.id, c.text, c.trust_score, c.trust_level,
               COUNT(e.id) FILTER (WHERE e.stance = 'pro') AS pro_count,
               COUNT(e.id) FILTER (WHERE e.stance = 'con') AS con_count,
               COUNT(e.id) AS evidence_count
        FROM claims c
        LEFT JOIN evidence e ON e.claim_id = c.id
        WHERE c.page_id = :pid
        GROUP BY c.id, c.text, c.trust_score, c.trust_level
        ORDER BY c.trust_score ASC NULLS LAST
        LIMIT 60
    """), {"pid": page_id}).fetchall()

    # Existing ideas
    existing = db.execute(text("""
        SELECT id, question, gap_type, claim_id
        FROM research_ideas
        WHERE page_id = :pid AND status IN ('active', 'draft', 'saved')
        ORDER BY created_at DESC LIMIT 60
    """), {"pid": page_id}).fetchall()

    # Top 20 usable surveys by quality_score (active or operational)
    surveys = db.execute(text("""
        SELECT s.name, sd.redshift_range, sd.data_type, sd.sample_size
        FROM surveys s
        JOIN survey_datasets sd ON sd.survey_id = s.id
        WHERE s.status IN ('active', 'operational')
        ORDER BY s.quality_score DESC NULLS LAST
        LIMIT 20
    """)).fetchall()

    # Evidence titles for novelty context (Atom scoring)
    evidence_titles = db.execute(text("""
        SELECT ap.title
        FROM arxiv_papers ap
        WHERE ap.related_pages::text LIKE :slug_pattern
        ORDER BY ap.submitted DESC LIMIT 30
    """), {"slug_pattern": f"%{page_slug}%"}).fetchall()

    return {
        "page_id": page_id,
        "sections": [
            {"heading": s["heading"], "body_markdown": s["body_digest"]}
            for s in sections
        ],
        "claims": [
            {
                "id": c.id,
                "text": c.text,
                "trust_score": float(c.trust_score or 0.5),
                "evidence_count": c.evidence_count or 0,
                "pro_count": c.pro_count or 0,
                "con_count": c.con_count or 0,
            }
            for c in claims
        ],
        "existing_ideas": [
            {"id": e.id, "question": e.question, "gap_type": e.gap_type, "anchor_claim_id": e.claim_id}
            for e in existing
        ],
        "surveys": [
            {"name": s.name, "redshift_range": s.redshift_range, "data_type": s.data_type}
            for s in surveys
        ],
        "evidence_titles": [t.title for t in evidence_titles],
    }


def _rakon_gap_detect(context: dict) -> tuple[list, str]:
    """Call Rakon → Buddle → Mima for gap detection. Returns (candidates, model_chain_tag)."""
    page_json = json.dumps({
        "sections": context["sections"],
        "claims": context["claims"],
        "existing_ideas": context["existing_ideas"],
    }, ensure_ascii=False)

    surveys_block = "\n".join(
        f"- {s['name']} ({s.get('data_type', '')}, z={s.get('redshift_range', 'unknown')})"
        for s in context["surveys"]
    )

    prompt = (
        _KV2_SYSTEM_PROMPT
        + "\n\nPAGE STATE (JSON):\n" + page_json
        + "\n\nACTIVE SURVEYS (use these names exactly):\n" + surveys_block
        + "\n\nReturn a JSON array of up to 15 ideas."
    )

    def _parse_candidates(raw: str | None) -> list:
        if not raw:
            return []
        parsed = _parse_json_block(raw)
        if isinstance(parsed, list):
            return [c for c in parsed if isinstance(c, dict) and c.get("question")]
        return []

    # Rakon primary
    if _check_ollama_alive(OLLAMA_MACPRO, MODEL_RAKON):
        raw = _ollama_chat(OLLAMA_MACPRO, MODEL_RAKON, prompt, temperature=0.7, timeout=1800)
        candidates = _parse_candidates(raw)
        if candidates:
            log.info("[ideas_v2] rakon returned %d candidates", len(candidates))
            return candidates, "karpathy_v2"

    # Buddle fallback
    if _check_ollama_alive(OLLAMA_BUDDLE, MODEL_BUDDLE):
        raw = _ollama_chat(OLLAMA_BUDDLE, MODEL_BUDDLE, prompt, temperature=0.7, timeout=1200)
        candidates = _parse_candidates(raw)
        if candidates:
            log.info("[ideas_v2] buddle fallback returned %d candidates", len(candidates))
            return candidates[:10], "karpathy_v2_buddle"

    # Mima last resort
    raw = _ollama_chat(OLLAMA_LOCAL, MODEL_MIMA, prompt, temperature=0.7, timeout=1200)
    candidates = _parse_candidates(raw)
    if candidates:
        log.info("[ideas_v2] mima fallback returned %d candidates", len(candidates))
        return candidates[:8], "karpathy_v2_mima"

    log.warning("[ideas_v2] all models failed gap detection")
    return [], "karpathy_v2_failed"


def _astrosage_polish_v2(candidates: list) -> list:
    """Polish each candidate's prose fields via AstroSage-70B in batches of 5."""
    polished = []
    batch_size = 5
    for i in range(0, len(candidates), batch_size):
        for candidate in candidates[i:i + batch_size]:
            prompt = _KV2_ASTROSAGE_PROMPT.format(idea_json=json.dumps(candidate, ensure_ascii=False))
            raw = _ollama_chat(OLLAMA_LOCAL, MODEL_ASTROSAGE, prompt, temperature=0.3, timeout=120)
            if not raw:
                polished.append(candidate)
                continue
            result = _parse_json_block(raw)
            if not isinstance(result, dict):
                polished.append(candidate)
                continue
            # Read-only fields are preserved; only overwrite editable fields
            for field in ("question", "why_now", "approach"):
                if result.get(field):
                    candidate[field] = result[field]
            if result.get("reject_reason"):
                candidate["question"] = ""
                candidate["_reject_reason"] = result["reject_reason"]
            polished.append(candidate)
    return polished


def _atom_score_v2(candidates: list) -> list:
    """Score each candidate with Atom-7B. Defaults to 0.5/0.5 on failure."""
    evidence_titles = ""  # evidence context not available here; passed in full flow
    scored = []
    for c in candidates:
        prompt = _KV2_ATOM_PROMPT.format(
            question=c.get("question", "")[:200],
            survey_combo=c.get("survey_combo", ""),
            redshift_range=c.get("redshift_range", ""),
            physical_observable=c.get("physical_observable", ""),
            evidence_titles=evidence_titles[:800],
        )
        raw = _ollama_chat(OLLAMA_LOCAL, MODEL_ATOM, prompt, temperature=0.1, timeout=60)
        if raw:
            result = _parse_json_block(raw)
            if isinstance(result, dict):
                c["novelty"] = min(max(float(result.get("novelty", 0.5)), 0.0), 1.0)
                c["feasibility"] = min(max(float(result.get("feasibility", 0.5)), 0.0), 1.0)
                c["_atom_flag"] = result.get("flag", "ok")
                scored.append(c)
                continue
        log.warning("[ideas_v2] atom score failed for idea '%s...', using defaults", c.get("question", "")[:40])
        c["novelty"] = c.get("novelty") or 0.5
        c["feasibility"] = c.get("feasibility") or 0.5
        c["_atom_flag"] = "ok"
        scored.append(c)
    return scored


def _nutty_dedup_v2(db, candidates: list, page_id: int) -> list:
    """Dedup candidates against existing page ideas using Nutty embeddings (cosine sim > 0.85 → drop).
    Falls back to TF-IDF cosine similarity when Nutty embedding endpoint is unavailable.
    """
    from sqlalchemy import text
    existing_texts = db.execute(text(
        "SELECT question, approach FROM research_ideas"
        " WHERE page_id = :pid AND status IN ('active', 'draft', 'saved')"
    ), {"pid": page_id}).fetchall()
    existing_combined = [f"{r.question} {r.approach}" for r in existing_texts]

    if not existing_combined:
        return candidates

    # Try Nutty embedding endpoint
    def _nutty_embed(text_input: str) -> list | None:
        try:
            resp = httpx.post(
                f"{OLLAMA_LOCAL.rstrip('/v1')}/api/embeddings",
                json={"model": MODEL_NUTTY, "prompt": text_input},
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json().get("embedding")
        except Exception:
            return None

    def _cosine(a: list, b: list) -> float:
        import math
        dot = sum(x * y for x, y in zip(a, b))
        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(y * y for y in b))
        return dot / (na * nb) if na * nb > 0 else 0.0

    surviving = []
    for c in candidates:
        candidate_text = f"{c.get('question', '')} {c.get('approach', '')}"
        emb_c = _nutty_embed(candidate_text)

        if emb_c:
            max_sim = 0.0
            for ex_text in existing_combined:
                emb_e = _nutty_embed(ex_text)
                if emb_e:
                    max_sim = max(max_sim, _cosine(emb_c, emb_e))
        else:
            # TF-IDF fallback
            max_sim = max((_tfidf_cosine(candidate_text, ex) for ex in existing_combined), default=0.0)

        if max_sim < 0.85:
            surviving.append(c)
        else:
            log.info("[ideas_v2] dedup dropped '%s...' (sim=%.3f)", c.get("question", "")[:60], max_sim)

    return surviving


def _parse_redshift_range(rr: str) -> tuple[float, float] | None:
    """Return (lo, hi) float tuple if redshift_range parses; None otherwise."""
    import re
    if not rr:
        return None
    rr = rr.lower().replace("z", "").replace("=", "").strip()
    m = re.search(r"([0-9.]+)\s*[-–—]\s*([0-9.]+)", rr)
    if m:
        return float(m.group(1)), float(m.group(2))
    m = re.search(r">?\s*([0-9.]+)", rr)
    if m:
        return float(m.group(1)), 20.0
    return None


def _quality_gate(candidates: list) -> tuple[list, list]:
    """Conjunctive quality check. Returns (passing, rejected)."""
    from app.constants.observables import OBSERVABLE_KEYWORDS
    passing, rejected = [], []
    for c in candidates:
        reject_reason = None

        survey_combo = (c.get("survey_combo") or "").strip()
        if not survey_combo:
            reject_reason = "missing_survey_combo"

        if not reject_reason:
            observable = (c.get("physical_observable") or "").lower()
            if not any(kw in observable for kw in _KV2_OBSERVABLE_KEYWORDS | OBSERVABLE_KEYWORDS):
                reject_reason = "unrecognized_observable"

        if not reject_reason:
            if _parse_redshift_range(c.get("redshift_range", "")) is None:
                reject_reason = "unparseable_redshift"

        if reject_reason:
            c["_reject_reason"] = reject_reason
            rejected.append(c)
        else:
            passing.append(c)
    return passing, rejected


def _rank_and_cap(db, candidates: list, cap: int = 10) -> list:
    """Rank by 0.4*novelty + 0.4*feasibility + 0.2*(1 - anchor_trust), return top cap."""
    from sqlalchemy import text

    def _anchor_trust(c: dict) -> float:
        anchor_id = c.get("anchor_claim_id")
        if not anchor_id:
            return 0.5
        try:
            row = db.execute(
                text("SELECT trust_score FROM claims WHERE id = :cid"), {"cid": int(anchor_id)}
            ).fetchone()
            return float(row.trust_score or 0.5) if row else 0.5
        except Exception:
            return 0.5

    ranked = sorted(
        candidates,
        key=lambda c: (
            0.4 * float(c.get("novelty", 0.5))
            + 0.4 * float(c.get("feasibility", 0.5))
            + 0.2 * (1.0 - _anchor_trust(c))
        ),
        reverse=True,
    )
    return ranked[:cap]


def _persist_ideas_v2(db, page_id: int, ideas: list, run_id: int | None, model_chain: str) -> int:
    from sqlalchemy import text
    inserted = 0
    for idea in ideas:
        try:
            anchor_claim_id = idea.get("anchor_claim_id")
            if anchor_claim_id:
                try:
                    anchor_claim_id = int(anchor_claim_id)
                except (TypeError, ValueError):
                    anchor_claim_id = None

            secondary_ids = idea.get("secondary_claim_ids") or []
            conflicting = idea.get("conflicting_claim_ids")
            bridge_pair = idea.get("bridge_section_pair")

            # Normalize arrays
            if isinstance(conflicting, list) and conflicting:
                conflicting = [int(x) for x in conflicting if x]
            else:
                conflicting = None
            if isinstance(bridge_pair, list) and bridge_pair:
                bridge_pair = [str(x) for x in bridge_pair]
            else:
                bridge_pair = None

            nested = db.begin_nested()
            try:
                result = db.execute(text("""
                    INSERT INTO research_ideas
                      (page_id, survey_combo, question, why_now, approach,
                       novelty, feasibility, status, model_chain,
                       generated_by_run_id, seeded, claim_id,
                       gap_type, conflicting_claim_ids, bridge_section_pair)
                    VALUES
                      (:pid, :combo, :q, :wn, :ap,
                       :nov, :feas, 'active', :chain,
                       :run_id, FALSE, :claim_id,
                       :gap_type,
                       :conflicting::integer[],
                       :bridge::text[])
                    RETURNING id
                """), {
                    "pid":        page_id,
                    "combo":      (idea.get("survey_combo") or "")[:40],
                    "q":          idea.get("question") or "",
                    "wn":         idea.get("why_now") or "",
                    "ap":         idea.get("approach") or "",
                    "nov":        round(min(max(float(idea.get("novelty") or 0.5), 0), 1), 2),
                    "feas":       round(min(max(float(idea.get("feasibility") or 0.5), 0), 1), 2),
                    "chain":      model_chain,
                    "run_id":     run_id,
                    "claim_id":   anchor_claim_id,
                    "gap_type":   idea.get("gap_type") if idea.get("gap_type") in _KV2_GAP_TYPES else None,
                    "conflicting": "{%s}" % ",".join(str(x) for x in conflicting) if conflicting else None,
                    "bridge":     "{%s}" % ",".join(f'"{x}"' for x in bridge_pair) if bridge_pair else None,
                })
                idea_id = result.fetchone()[0]

                # Anchor rows for secondary claim IDs
                for cid in (secondary_ids or []):
                    try:
                        db.execute(text(
                            "INSERT INTO research_idea_anchors (idea_id, kind, ref_id)"
                            " VALUES (:iid, 'claim', :ref) ON CONFLICT DO NOTHING"
                        ), {"iid": idea_id, "ref": str(int(cid))})
                    except Exception:
                        pass

                nested.commit()
                inserted += 1
            except Exception as exc:
                nested.rollback()
                log.warning("[ideas_v2] persist failed for idea '%s...': %s",
                            (idea.get("question") or "")[:60], exc)
        except Exception as exc:
            log.warning("[ideas_v2] outer persist error: %s", exc)

    db.commit()
    return inserted


@shared_task(
    name="app.agent_loop.research_ideas.auto_improvement.generate_research_ideas_v2",
    bind=True,
    max_retries=0,
)
def generate_research_ideas_v2(self, page_slug: str):
    """Karpathy-style gap-detection research idea generator.
    Reads full page state (sections, claims, existing ideas) and identifies
    what is missing, contested, or needs bridging across five gap types.
    Lock: shared rakon:lock (value=karpathy_v2), TTL 2h.
    """
    if _provenance_enforce_enabled():
        return {
            "skipped": "provenance_enforce_suppressed_karpathy_v2",
            "page_slug": page_slug,
        }

    from app.database import SessionLocal
    from sqlalchemy import text

    r = _redis()
    db = SessionLocal()

    try:
        # 1. Load page
        page = db.execute(
            text("SELECT id, slug, updated_at FROM wiki_pages WHERE slug = :s"),
            {"s": page_slug},
        ).fetchone()
        if not page:
            log.error("[ideas_v2] page '%s' not found", page_slug)
            return {"error": "page_not_found"}

        # 2. Idempotency guard — time-based (20h TTL).
        # Do NOT gate on page.updated_at: pages with do_not_renovate=true are
        # never touched by the renovation pipeline, so updated_at never advances
        # and a page-change guard would permanently block v2 after the first run.
        run_key = f"research_ideas:karpathy_run_at:{page.id}"
        last_run_iso = r.get(run_key)
        if last_run_iso:
            try:
                import datetime
                last_dt = datetime.datetime.fromisoformat(last_run_iso)
                elapsed_h = (datetime.datetime.utcnow() - last_dt).total_seconds() / 3600
                if elapsed_h < 20:
                    log.info("[ideas_v2] %s ran %.1fh ago, skipping.", page_slug, elapsed_h)
                    return {"skipped": "ran_recently"}
            except Exception:
                pass

        # 3. Cross-loop AstroSage priority: surveys > karpathy_v2
        # surveys writes the lock as "surveys:{slug}" (e.g. "surveys:desi")
        astrosage_holder = r.get("astrosage:in_use")
        if astrosage_holder and astrosage_holder.startswith("surveys"):
            cleared = _wait_until_cleared("astrosage:in_use", timeout_sec=300)
            if not cleared:
                log.info("[ideas_v2] surveys hold astrosage; deferring to tomorrow.")
                return {"skipped": "astrosage_held_by_surveys"}

        # 4. Acquire shared rakon:lock
        if not _kv2_acquire_rakon_lock():
            holder = r.get("rakon:lock") or "unknown"
            log.info("[ideas_v2] rakon:lock held by '%s'; skipping tick.", holder)
            return {"skipped": "rakon_locked"}

        try:
            # 5. Build page context
            context = _build_page_context_v2(db, r, page.id, page_slug)
            if not context:
                log.error("[ideas_v2] failed to build context for %s", page_slug)
                return {"error": "context_build_failed"}

            # 6. Gap detection: Rakon → Buddle → Mima
            candidates, model_chain_tag = _rakon_gap_detect(context)
            if not candidates:
                log.info("[ideas_v2] no candidates produced for %s", page_slug)
                _log_autowiki_run(db, page.id, "karpathy_v2",
                                  decision="no_commit", error="all_models_failed",
                                  chain=model_chain_tag)
                db.commit()
                return {"inserted": 0, "reason": "all_models_failed"}

            # Cache raw output for postmortem debugging (24h)
            try:
                r.setex(
                    f"research_ideas:karpathy_candidates:{page.id}",
                    86400,
                    json.dumps(candidates[:20], ensure_ascii=False),
                )
            except Exception:
                pass

            # 7. AstroSage prose polish + physics audit
            candidates = _astrosage_polish_v2(candidates)
            candidates = [c for c in candidates if c.get("question")]

            if not candidates:
                log.info("[ideas_v2] all candidates rejected by AstroSage for %s", page_slug)
                _log_autowiki_run(db, page.id, "karpathy_v2",
                                  decision="no_commit", error="all_astrosage_rejected",
                                  chain=model_chain_tag)
                db.commit()
                return {"inserted": 0, "reason": "all_astrosage_rejected"}

            # 8. Atom-7B novelty/feasibility scoring
            candidates = _atom_score_v2(candidates)
            candidates = [c for c in candidates if c.get("_atom_flag") != "too_similar"]

            # 9. Nutty dedup vs existing page ideas
            candidates = _nutty_dedup_v2(db, candidates, page.id)

            # 10. Quality gate (conjunctive: survey + observable + redshift)
            passing, rejected = _quality_gate(candidates)
            for rej in rejected:
                log.info("[ideas_v2] quality gate rejected '%s...': %s",
                         (rej.get("question") or "")[:60], rej.get("_reject_reason", ""))

            if not passing:
                log.info("[ideas_v2] no ideas passed quality gate for %s", page_slug)
                _log_autowiki_run(db, page.id, "karpathy_v2",
                                  decision="no_commit", error="no_survivors_quality_gate",
                                  chain=model_chain_tag)
                db.commit()
                return {"inserted": 0, "reason": "no_survivors_quality_gate"}

            # 11. Volume cap: top 10
            if len(passing) > 10:
                passing = _rank_and_cap(db, passing, cap=10)

            # 12. Persist
            run_id_row = db.execute(text("""
                INSERT INTO autowiki_runs (page_id, started_at, kind, model_proposer, decision)
                VALUES (:pid, NOW(), 'karpathy_v2', :chain, 'pending')
                RETURNING id
            """), {"pid": page.id, "chain": model_chain_tag}).fetchone()
            run_id = run_id_row[0] if run_id_row else None
            db.commit()

            inserted = _persist_ideas_v2(db, page.id, passing, run_id, model_chain_tag)

            if run_id:
                db.execute(text(
                    "UPDATE autowiki_runs SET finished_at = NOW(), decision = 'commit' WHERE id = :id"
                ), {"id": run_id})
                db.commit()

            # 13. Mark idempotency key
            import datetime
            r.set(run_key, datetime.datetime.utcnow().isoformat())

            log.info("[ideas_v2] saved %d ideas for %s (chain=%s)", inserted, page_slug, model_chain_tag)
            _discord(f"🔭 Karpathy v2: **{page_slug}** — {inserted} gap-detection ideas saved "
                     f"({len(candidates)} survived gates, chain={model_chain_tag})")

            return {
                "page_slug": page_slug,
                "inserted": inserted,
                "candidates_raw": len(candidates),
                "model_chain": model_chain_tag,
            }

        finally:
            _kv2_release_rakon_lock()

    except Exception as exc:
        log.exception("[ideas_v2] unexpected error for %s: %s", page_slug, exc)
        try:
            _kv2_release_rakon_lock()
        except Exception:
            pass
        raise
    finally:
        db.close()
