"""Research Ideas router — per-page AI-generated survey-anchored research questions."""
import json
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter(prefix="/api/research/ideas", tags=["research-ideas"])


def _idea_to_dict(row, anchors: list | None = None) -> dict:
    verification_notes = getattr(row, "factual_verification_notes", None)
    if isinstance(verification_notes, str):
        try:
            verification_notes = json.loads(verification_notes)
        except Exception:
            verification_notes = {"raw": verification_notes}
    coverage_status = getattr(row, "coverage_status", None)
    derived_verified = coverage_status in ("screened_pass", "partial")
    closest_prior_work = getattr(row, "closest_prior_work", None)
    if isinstance(closest_prior_work, str):
        try:
            closest_prior_work = json.loads(closest_prior_work)
        except Exception:
            closest_prior_work = []
    papers_checked = None
    if isinstance(verification_notes, dict):
        papers_checked = verification_notes.get("papers_checked")
    return {
        "id": row.id,
        "page_id": row.page_id,
        "survey_combo": row.survey_combo,
        "question": row.question,
        "why_now": row.why_now,
        "approach": row.approach,
        "systematics": row.systematics_json if isinstance(row.systematics_json, list) else (
            json.loads(row.systematics_json) if row.systematics_json else []
        ),
        "novelty": float(row.novelty),
        "feasibility": float(row.feasibility),
        "status": row.status,
        "model_chain": row.model_chain,
        "saved_by_papa": row.saved_by_papa,
        "seeded": row.seeded,
        "anchors": anchors,
        "created_at": row.created_at.isoformat() if row.created_at else None,
        "updated_at": row.updated_at.isoformat() if row.updated_at else None,
        "last_seen_at": row.last_seen_at.isoformat() if row.last_seen_at else None,
        # auto-improvement lifecycle fields
        "promoted_at":        row.promoted_at.isoformat() if getattr(row, "promoted_at", None) else None,
        "promoted_by":        getattr(row, "promoted_by", None),
        "last_refreshed_at":  row.last_refreshed_at.isoformat() if getattr(row, "last_refreshed_at", None) else None,
        "refresh_count":      getattr(row, "refresh_count", 0) or 0,
        "covered_by_arxiv_id": getattr(row, "covered_by_arxiv_id", None),
        "covered_at":          row.covered_at.isoformat() if getattr(row, "covered_at", None) else None,
        "covered_confidence":  float(row.covered_confidence) if getattr(row, "covered_confidence", None) is not None else None,
        "gap_type":            getattr(row, "gap_type", None),
        "gap_type_source":     getattr(row, "gap_type_source", None),
        "factual_verified":    derived_verified,
        "factual_verified_at": row.factual_verified_at.isoformat() if getattr(row, "factual_verified_at", None) else None,
        "factual_verification_notes": verification_notes or {},
        "coverage_status":     coverage_status,
        "closest_prior_work":  closest_prior_work or [],
        "coverage_checked_at": row.coverage_checked_at.isoformat() if getattr(row, "coverage_checked_at", None) else None,
        "papers_checked":      papers_checked,
        "display_badge":       "unverified" if coverage_status in (None, "inconclusive") else None,
    }


def _screening_filter(include_covered: bool = False) -> str:
    if include_covered:
        return "1=1"
    return "(ri.coverage_status IS NULL OR ri.coverage_status IN ('screened_pass', 'partial', 'inconclusive'))"


def _screened_fail_filter() -> str:
    return "ri.coverage_status IN ('covered', 'failed_entity')"


def _resolve_survey_slugs(db: Session, combo: str) -> dict[str, str]:
    """Return {token: slug} mapping for each survey in a combo string, or {} if table absent."""
    try:
        tokens = [t.strip() for t in combo.split("+")]
        result = {}
        for token in tokens:
            row = db.execute(
                text("SELECT slug FROM surveys WHERE UPPER(name) = UPPER(:t) OR UPPER(slug) = UPPER(:t)"),
                {"t": token},
            ).fetchone()
            if row:
                result[token] = row.slug
        return result
    except Exception:
        return {}


@router.get("/{slug}")
def list_ideas(
    slug: str,
    combo: str | None = Query(default=None),
    status_filter: str | None = Query(default=None, alias="status"),
    sort: str = Query(default="novelty"),
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=20, ge=1, le=200),
    db: Session = Depends(get_db),
):
    page_row = db.execute(
        text("SELECT id FROM wiki_pages WHERE slug = :slug"), {"slug": slug}
    ).fetchone()
    if page_row is None:
        raise HTTPException(status_code=404, detail=f"Wiki page '{slug}' not found")

    conditions = "ri.page_id = :pid AND ri.status NOT IN ('superseded', 'rejected')"
    params: dict = {"pid": page_row.id}

    if combo:
        conditions += " AND ri.survey_combo = :combo"
        params["combo"] = combo
    if status_filter:
        conditions += " AND ri.status = :sf"
        params["sf"] = status_filter
    else:
        conditions += " AND ri.status NOT IN ('stale', 'covered')"
    conditions += f" AND {_screening_filter(include_covered=False)}"

    order_map = {
        "novelty": "ri.novelty DESC",
        "feasibility": "ri.feasibility DESC",
        "recency": "ri.created_at DESC",
        "saved": "ri.saved_by_papa DESC, ri.novelty DESC",
    }
    order_clause = order_map.get(sort, "ri.novelty DESC")

    offset = (page - 1) * per_page
    params["limit"] = per_page
    params["offset"] = offset

    rows = db.execute(text(f"""
        SELECT ri.*
        FROM research_ideas ri
        WHERE {conditions}
        ORDER BY {order_clause}
        LIMIT :limit OFFSET :offset
    """), params).fetchall()

    total_row = db.execute(
        text(f"SELECT count(*) FROM research_ideas ri WHERE {conditions}"),
        {k: v for k, v in params.items() if k not in ("limit", "offset")},
    ).fetchone()
    total = total_row[0] if total_row else 0

    ideas = []
    for r in rows:
        d = _idea_to_dict(r)
        d["survey_slugs"] = _resolve_survey_slugs(db, r.survey_combo)
        ideas.append(d)

    last_run = db.execute(text(
        "SELECT finished_at, model_proposer FROM autowiki_runs"
        " WHERE page_id = :pid AND proposal_type = 'research_ideas'"
        " ORDER BY finished_at DESC LIMIT 1"
    ), {"pid": page_row.id}).fetchone()

    return {
        "page_slug": slug,
        "total": total,
        "page": page,
        "per_page": per_page,
        "ideas": ideas,
        "last_refreshed_at": last_run.finished_at.isoformat() if last_run and last_run.finished_at else None,
        "last_model_chain": last_run.model_proposer if last_run else None,
    }


@router.get("/by-id/{idea_id}")
def get_idea(idea_id: int, db: Session = Depends(get_db)):
    row = db.execute(
        text("SELECT * FROM research_ideas WHERE id = :id"), {"id": idea_id}
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Idea {idea_id} not found")

    anchor_rows = db.execute(
        text("SELECT kind, ref_id FROM research_idea_anchors WHERE idea_id = :id ORDER BY kind"), {"id": idea_id}
    ).fetchall()
    anchors = [{"kind": a.kind, "ref_id": a.ref_id} for a in anchor_rows]

    d = _idea_to_dict(row, anchors=anchors)
    d["survey_slugs"] = _resolve_survey_slugs(db, row.survey_combo)
    return d


@router.post("/{slug}/regenerate", status_code=202)
def regenerate_ideas(slug: str, db: Session = Depends(get_db)):
    """Trigger the Rakon pipeline for a wiki page. Admin-intended; no hard auth in v1 (rate-limited via Redis)."""
    import time
    from app.config import settings

    page_row = db.execute(
        text("SELECT id FROM wiki_pages WHERE slug = :slug"), {"slug": slug}
    ).fetchone()
    if page_row is None:
        raise HTTPException(status_code=404, detail=f"Wiki page '{slug}' not found")

    # Rate-limit: reject if a run completed <6h ago
    recent = db.execute(text(
        "SELECT finished_at FROM autowiki_runs"
        " WHERE page_id = :pid AND proposal_type = 'research_ideas' AND finished_at IS NOT NULL"
        " ORDER BY finished_at DESC LIMIT 1"
    ), {"pid": page_row.id}).fetchone()
    if recent and recent.finished_at:
        import datetime
        age = datetime.datetime.utcnow() - recent.finished_at.replace(tzinfo=None)
        if age.total_seconds() < 6 * 3600:
            raise HTTPException(
                status_code=429,
                detail=f"Last run was {int(age.total_seconds() / 60)} minutes ago. Minimum interval is 6 hours.",
            )

    from app.agent_loop.research_ideas.tasks import regenerate_research_ideas
    task = regenerate_research_ideas.delay(slug)
    return {"status": "accepted", "task_id": task.id, "page_slug": slug}


@router.post("/{idea_id}/save")
def save_idea(idea_id: int, db: Session = Depends(get_db)):
    row = db.execute(
        text("SELECT id FROM research_ideas WHERE id = :id"), {"id": idea_id}
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Idea {idea_id} not found")

    db.execute(
        text("UPDATE research_ideas SET saved_by_papa = TRUE, updated_at = now() WHERE id = :id"),
        {"id": idea_id},
    )
    db.execute(
        text("DELETE FROM research_idea_votes WHERE idea_id = :iid AND user_id IS NULL AND axis = 'overall'"),
        {"iid": idea_id},
    )
    db.execute(
        text("INSERT INTO research_idea_votes (idea_id, user_id, value, axis) VALUES (:iid, NULL, 1, 'overall')"),
        {"iid": idea_id},
    )
    db.commit()
    return {"id": idea_id, "saved_by_papa": True}


@router.post("/{idea_id}/mark-stale")
def mark_stale(idea_id: int, db: Session = Depends(get_db)):
    row = db.execute(
        text("SELECT id FROM research_ideas WHERE id = :id"), {"id": idea_id}
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Idea {idea_id} not found")

    db.execute(
        text("UPDATE research_ideas SET status = 'stale', updated_at = now() WHERE id = :id"),
        {"id": idea_id},
    )
    db.commit()
    return {"id": idea_id, "status": "stale"}


@router.post("/{idea_id}/vote")
def vote_idea(idea_id: int, value: int = Query(..., ge=-1, le=1), db: Session = Depends(get_db)):
    row = db.execute(
        text("SELECT id FROM research_ideas WHERE id = :id"), {"id": idea_id}
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Idea {idea_id} not found")

    db.execute(
        text("DELETE FROM research_idea_votes WHERE idea_id = :iid AND user_id IS NULL AND axis = 'overall'"),
        {"iid": idea_id},
    )
    db.execute(
        text("INSERT INTO research_idea_votes (idea_id, user_id, value, axis) VALUES (:iid, NULL, :val, 'overall')"),
        {"iid": idea_id, "val": value},
    )
    db.commit()
    return {"id": idea_id, "voted": value}


@router.get("/{slug}/stats")
def idea_stats(slug: str, db: Session = Depends(get_db)):
    page_row = db.execute(
        text("SELECT id FROM wiki_pages WHERE slug = :slug"), {"slug": slug}
    ).fetchone()
    if page_row is None:
        raise HTTPException(status_code=404, detail=f"Wiki page '{slug}' not found")

    combo_counts = db.execute(text(
        "SELECT survey_combo, count(*) as cnt FROM research_ideas"
        " WHERE page_id = :pid AND status = 'active'"
        " GROUP BY survey_combo ORDER BY cnt DESC"
    ), {"pid": page_row.id}).fetchall()

    last_run = db.execute(text(
        "SELECT finished_at, model_proposer FROM autowiki_runs"
        " WHERE page_id = :pid AND proposal_type = 'research_ideas'"
        " ORDER BY finished_at DESC LIMIT 1"
    ), {"pid": page_row.id}).fetchone()

    total = db.execute(
        text("SELECT count(*) FROM research_ideas WHERE page_id = :pid AND status != 'rejected'"),
        {"pid": page_row.id},
    ).fetchone()[0]

    return {
        "page_slug": slug,
        "total_ideas": total,
        "by_combo": [{"combo": r.survey_combo, "count": r.cnt} for r in combo_counts],
        "last_run_at": last_run.finished_at.isoformat() if last_run and last_run.finished_at else None,
        "last_model_chain": last_run.model_proposer if last_run else None,
    }


@router.get("/{slug}/covered")
def list_covered_ideas(
    slug: str,
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=20, ge=1, le=200),
    db: Session = Depends(get_db),
):
    """Retrospective: research questions the literature has answered (§2.1, §3.6)."""
    page_row = db.execute(
        text("SELECT id FROM wiki_pages WHERE slug = :slug"), {"slug": slug}
    ).fetchone()
    if page_row is None:
        raise HTTPException(status_code=404, detail=f"Wiki page '{slug}' not found")

    offset = (page - 1) * per_page
    rows = db.execute(text("""
        SELECT ri.*
        FROM research_ideas ri
        WHERE ri.page_id = :pid AND ri.status = 'covered'
        ORDER BY ri.covered_at DESC NULLS LAST
        LIMIT :limit OFFSET :offset
    """), {"pid": page_row.id, "limit": per_page, "offset": offset}).fetchall()

    total = db.execute(
        text("SELECT count(*) FROM research_ideas WHERE page_id = :pid AND status = 'covered'"),
        {"pid": page_row.id},
    ).fetchone()[0]

    ideas = []
    for r in rows:
        d = _idea_to_dict(r)
        d["survey_slugs"] = _resolve_survey_slugs(db, r.survey_combo)
        ideas.append(d)

    return {"page_slug": slug, "total": total, "page": page, "per_page": per_page, "ideas": ideas}


# ── Phase 3 router ──────────────────────────────────────────────────────────
p3_router = APIRouter(prefix="/api", tags=["research-ideas-v3"])


def _dataset_to_dict(row) -> dict:
    return {
        "slug": row.slug,
        "name": row.name,
        "full_name": row.full_name,
        "data_type": row.data_type,
        "release_year": row.release_year,
        "release_label": row.release_label,
        "redshift_range": row.redshift_range,
        "sky_coverage_deg2": float(row.sky_coverage_deg2) if row.sky_coverage_deg2 else None,
        "sample_size": row.sample_size,
        "primary_url": row.primary_url,
        "registry": row.registry,
        "license": row.license,
        "status": row.status,
        "verified": row.url_verified_ok,
        "verified_at": row.url_verified_at.isoformat() if row.url_verified_at else None,
        "description": row.description,
    }


def _idea_to_dict_v3(row, db: Session) -> dict:
    base = _idea_to_dict(row)
    base["claim_id"] = getattr(row, "claim_id", None)
    base["well_posed_score"] = float(row.well_posed_score) if getattr(row, "well_posed_score", None) is not None else None
    base["datasets_verified"] = getattr(row, "datasets_verified", False)

    # datasets
    ds_rows = db.execute(text("""
        SELECT sd.slug, sd.name, sd.url_verified_ok as verified, rid.role
        FROM research_idea_datasets rid
        JOIN survey_datasets sd ON sd.id = rid.dataset_id
        WHERE rid.idea_id = :iid
        ORDER BY rid.role, sd.slug
    """), {"iid": row.id}).fetchall()
    primary_ds = [{"slug": r.slug, "name": r.name, "verified": r.verified} for r in ds_rows if r.role == "primary"]
    support_ds = [{"slug": r.slug, "name": r.name, "verified": r.verified} for r in ds_rows if r.role != "primary"]
    all_verified = bool(primary_ds) and all(d["verified"] for d in primary_ds)
    base["datasets"] = {"primary": primary_ds, "support": support_ds, "all_verified": all_verified}

    # anchors
    anchor_rows = db.execute(text("""
        SELECT kind, ref_id FROM research_idea_anchors WHERE idea_id = :iid ORDER BY kind
    """), {"iid": row.id}).fetchall()
    def _parse_ref_id(ref_id: str) -> int:
        """Handle ref_id stored as plain int string '1495' or JSON array '[1495]'."""
        import json as _json
        s = str(ref_id).strip()
        if s.startswith('['):
            parsed = _json.loads(s)
            return int(parsed[0]) if parsed else 0
        return int(s)
    claim_anchors = [{"id": _parse_ref_id(a.ref_id), "ref_id": a.ref_id} for a in anchor_rows if a.kind == "claim"]
    arxiv_anchors = [a.ref_id for a in anchor_rows if a.kind == "arxiv"]
    base["anchors"] = {"claims": claim_anchors, "debates": [], "arxiv": arxiv_anchors}

    claim_ids = sorted({c["id"] for c in claim_anchors if c["id"]} | ({int(row.claim_id)} if getattr(row, "claim_id", None) else set()))
    if claim_ids:
        claim_rows = db.execute(text("""
            SELECT id, text, trust_level
            FROM claims
            WHERE id = ANY(:claim_ids)
            ORDER BY id
        """), {"claim_ids": claim_ids}).fetchall()
        base["anchor_claims"] = [
            {"id": c.id, "text": c.text, "trust_level": c.trust_level}
            for c in claim_rows
        ]
        ev_rows = db.execute(text("""
            SELECT id, claim_id, arxiv_id, title, year, stance, evidence_status, arxiv_verified
            FROM evidence
            WHERE claim_id = ANY(:claim_ids)
            ORDER BY claim_id, quality DESC NULLS LAST, id
            LIMIT 12
        """), {"claim_ids": claim_ids}).fetchall()
        base["supporting_evidence"] = [
            {
                "id": ev.id,
                "claim_id": ev.claim_id,
                "arxiv_id": ev.arxiv_id,
                "title": ev.title,
                "year": ev.year,
                "stance": ev.stance,
                "evidence_status": ev.evidence_status,
                "arxiv_verified": ev.arxiv_verified,
            }
            for ev in ev_rows
        ]
    else:
        base["anchor_claims"] = []
        base["supporting_evidence"] = []

    # votes by axis
    vote_rows = db.execute(text("""
        SELECT axis, COUNT(*) as n, AVG(value) as mean_val
        FROM research_idea_votes
        WHERE idea_id = :iid
        GROUP BY axis
    """), {"iid": row.id}).fetchall()
    votes = {}
    for v in vote_rows:
        axis = v.axis or "overall"
        votes[axis] = {"mean": float(v.mean_val) if v.mean_val is not None else None, "n": v.n}
    if "overall" not in votes:
        votes["overall"] = {"saved_by_papa": row.saved_by_papa, "user_count": 0}
    else:
        votes["overall"]["saved_by_papa"] = row.saved_by_papa

    base["scores"] = {
        "well_posed": float(row.well_posed_score) if getattr(row, "well_posed_score", None) is not None else None,
        "feasibility": float(row.feasibility),
        "novelty": float(row.novelty),
    }
    base["votes"] = votes
    return base


@p3_router.get("/pages/{slug}/ideas")
def list_ideas_p3(
    slug: str,
    combo: str | None = Query(default=None),
    min_well_posed: float | None = Query(default=None),
    verified_only: bool = Query(default=False),
    include_covered: bool = Query(default=False),
    sort: str = Query(default="novelty"),
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=20, ge=1, le=200),
    db: Session = Depends(get_db),
):
    page_row = db.execute(text("SELECT id FROM wiki_pages WHERE slug = :slug"), {"slug": slug}).fetchone()
    if page_row is None:
        raise HTTPException(404, f"Wiki page {slug} not found")

    conditions = "ri.page_id = :pid AND ri.status NOT IN ('superseded', 'rejected', 'stale')"
    if not include_covered:
        conditions += " AND ri.status != 'covered'"
        conditions += f" AND {_screening_filter(include_covered=False)}"
    params: dict = {"pid": page_row.id}

    if combo:
        conditions += " AND ri.survey_combo = :combo"
        params["combo"] = combo
    if verified_only:
        conditions += " AND ri.datasets_verified = TRUE"
    if min_well_posed is not None:
        conditions += " AND ri.well_posed_score >= :mwp"
        params["mwp"] = min_well_posed

    order_map = {"novelty": "ri.novelty DESC", "feasibility": "ri.feasibility DESC",
                 "recency": "ri.created_at DESC", "saved": "ri.saved_by_papa DESC, ri.novelty DESC"}
    order_clause = order_map.get(sort, "ri.novelty DESC")
    offset = (page - 1) * per_page
    params.update({"limit": per_page, "offset": offset})

    rows = db.execute(text(f"SELECT ri.* FROM research_ideas ri WHERE {conditions} ORDER BY {order_clause} LIMIT :limit OFFSET :offset"), params).fetchall()
    total = db.execute(text(f"SELECT count(*) FROM research_ideas ri WHERE {conditions}"), {k: v for k, v in params.items() if k not in ("limit", "offset")}).scalar()

    ideas = [_idea_to_dict_v3(r, db) for r in rows]
    return {"page_slug": slug, "total": total, "page": page, "per_page": per_page, "ideas": ideas, "count": len(ideas)}


@p3_router.get("/pages/{slug}/ideas/screened-fail")
def list_screened_fail_ideas(
    slug: str,
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    page_row = db.execute(text("SELECT id FROM wiki_pages WHERE slug = :slug"), {"slug": slug}).fetchone()
    if page_row is None:
        raise HTTPException(404, f"Wiki page {slug} not found")

    offset = (page - 1) * per_page
    conditions = f"ri.page_id = :pid AND {_screened_fail_filter()}"
    params = {"pid": page_row.id, "limit": per_page, "offset": offset}
    rows = db.execute(
        text(f"SELECT ri.* FROM research_ideas ri WHERE {conditions} ORDER BY ri.coverage_checked_at DESC NULLS LAST, ri.id LIMIT :limit OFFSET :offset"),
        params,
    ).fetchall()
    total = db.execute(
        text(f"SELECT count(*) FROM research_ideas ri WHERE {conditions}"),
        {"pid": page_row.id},
    ).scalar()
    return {"page_slug": slug, "total": total, "page": page, "per_page": per_page, "ideas": [_idea_to_dict_v3(r, db) for r in rows]}


@p3_router.get("/pages/{slug}/claims/{claim_id}/ideas")
def list_claim_ideas(slug: str, claim_id: int, db: Session = Depends(get_db)):
    page_row = db.execute(text("SELECT id FROM wiki_pages WHERE slug = :slug"), {"slug": slug}).fetchone()
    if page_row is None:
        raise HTTPException(404, f"Wiki page {slug} not found")

    rows = db.execute(text("""
        SELECT ri.* FROM research_ideas ri
        WHERE ri.page_id = :pid
          AND ri.status NOT IN ('superseded', 'rejected', 'stale')
          AND (ri.coverage_status IS NULL OR ri.coverage_status IN ('screened_pass', 'partial', 'inconclusive'))
          AND (ri.claim_id = :cid
               OR ri.id IN (
                   SELECT idea_id FROM research_idea_anchors
                   WHERE kind = 'claim' AND ref_id = :cid_str
               ))
        ORDER BY ri.saved_by_papa DESC, ri.novelty DESC
        LIMIT 10
    """), {"pid": page_row.id, "cid": claim_id, "cid_str": str(claim_id)}).fetchall()

    return {"claim_id": claim_id, "ideas": [_idea_to_dict_v3(r, db) for r in rows], "count": len(rows)}


@p3_router.get("/ideas/{idea_id}")
def get_idea_v3(idea_id: int, db: Session = Depends(get_db)):
    row = db.execute(text("SELECT * FROM research_ideas WHERE id = :id"), {"id": idea_id}).fetchone()
    if row is None:
        raise HTTPException(404, f"Idea {idea_id} not found")
    return _idea_to_dict_v3(row, db)


@p3_router.post("/ideas", status_code=201)
def create_idea(body: dict, db: Session = Depends(get_db)):
    required = {"page_id", "survey_combo", "question", "why_now", "approach"}
    missing = required - set(body.keys())
    if missing:
        raise HTTPException(400, f"Missing fields: {missing}")

    claim_id = body.get("claim_id")
    datasets_primary = body.get("datasets_primary", [])
    datasets_support = body.get("datasets_support", [])

    result = db.execute(text("""
        INSERT INTO research_ideas
          (page_id, survey_combo, question, why_now, approach, systematics_json,
           novelty, feasibility, status, model_chain, seeded, claim_id)
        VALUES
          (:page_id, :combo, :question, :why_now, :approach, :sys,
           :nov, :feas, active, papa-manual, TRUE, :claim_id)
        RETURNING id
    """), {
        "page_id": body["page_id"],
        "combo": body["survey_combo"],
        "question": body["question"],
        "why_now": body["why_now"],
        "approach": body["approach"],
        "sys": json.dumps(body.get("systematics", [])),
        "nov": body.get("novelty", 0.5),
        "feas": body.get("feasibility", 0.5),
        "claim_id": claim_id,
    })
    idea_id = result.fetchone().id

    for ds_slug in datasets_primary:
        ds_row = db.execute(text("SELECT id FROM survey_datasets WHERE slug = :s"), {"s": ds_slug}).fetchone()
        if ds_row:
            db.execute(text("INSERT INTO research_idea_datasets (idea_id, dataset_id, role) VALUES (:iid, :did, 'primary') ON CONFLICT DO NOTHING"), {"iid": idea_id, "did": ds_row.id})
    for ds_slug in datasets_support:
        ds_row = db.execute(text("SELECT id FROM survey_datasets WHERE slug = :s"), {"s": ds_slug}).fetchone()
        if ds_row:
            db.execute(text("INSERT INTO research_idea_datasets (idea_id, dataset_id, role) VALUES (:iid, :did, 'support') ON CONFLICT DO NOTHING"), {"iid": idea_id, "did": ds_row.id})

    if claim_id:
        db.execute(text("INSERT INTO research_idea_anchors (idea_id, kind, ref_id) VALUES (:iid, 'claim', :cid) ON CONFLICT DO NOTHING"), {"iid": idea_id, "cid": str(claim_id)})

    db.commit()
    row = db.execute(text("SELECT * FROM research_ideas WHERE id = :id"), {"id": idea_id}).fetchone()
    return _idea_to_dict_v3(row, db)


@p3_router.put("/ideas/{idea_id}/vote")
def vote_idea_v3(
    idea_id: int,
    body: dict,
    db: Session = Depends(get_db),
):
    row = db.execute(text("SELECT id FROM research_ideas WHERE id = :id"), {"id": idea_id}).fetchone()
    if row is None:
        raise HTTPException(404, f"Idea {idea_id} not found")

    axis = body.get("axis", "overall")
    value = body.get("value", 1)
    if axis not in ("overall", "well_posed", "feasible", "novel"):
        raise HTTPException(400, f"Invalid axis: {axis}")
    if value not in (-1, 0, 1):
        raise HTTPException(400, f"Invalid value: {value}")

    db.execute(text(
        "DELETE FROM research_idea_votes WHERE idea_id = :iid AND user_id IS NULL AND axis = :axis"
    ), {"iid": idea_id, "axis": axis})
    db.execute(text(
        "INSERT INTO research_idea_votes (idea_id, user_id, value, axis) VALUES (:iid, NULL, :val, :axis)"
    ), {"iid": idea_id, "val": value, "axis": axis})

    if axis == "overall" and value == 1:
        db.execute(text("UPDATE research_ideas SET saved_by_papa = TRUE, updated_at = NOW() WHERE id = :id"), {"id": idea_id})

    db.commit()
    return {"id": idea_id, "axis": axis, "voted": value}


@p3_router.get("/datasets")
def list_datasets(
    survey_id: int | None = Query(default=None),
    data_type: str | None = Query(default=None),
    verified: bool | None = Query(default=None),
    db: Session = Depends(get_db),
):
    conditions = "1=1"
    params: dict = {}
    if survey_id:
        conditions += " AND survey_id = :sid"
        params["sid"] = survey_id
    if data_type:
        conditions += " AND data_type = :dt"
        params["dt"] = data_type
    if verified is not None:
        conditions += " AND url_verified_ok = :v"
        params["v"] = verified

    rows = db.execute(text(f"SELECT * FROM survey_datasets WHERE {conditions} ORDER BY name"), params).fetchall()
    return {"datasets": [_dataset_to_dict(r) for r in rows], "count": len(rows)}


@p3_router.get("/datasets/{dataset_slug}")
def get_dataset(dataset_slug: str, db: Session = Depends(get_db)):
    row = db.execute(text("SELECT * FROM survey_datasets WHERE slug = :s"), {"s": dataset_slug}).fetchone()
    if row is None:
        raise HTTPException(404, f"Dataset {dataset_slug} not found")
    return _dataset_to_dict(row)
