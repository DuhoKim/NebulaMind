"""Astronomical Surveys Directory router."""
import json
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text, func
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter(prefix="/api/surveys", tags=["surveys"])


def _survey_row_to_dict(row, linked_count: int = 0) -> dict:
    return {
        "slug": row.slug,
        "name": row.name,
        "full_name": row.full_name,
        "description": row.description,
        "emoji": row.emoji,
        "logo_url": getattr(row, "logo_url", None),
        "logo_bg": getattr(row, "logo_bg", None),
        "wavelength_range": row.wavelength_range,
        "wavelength_band": row.wavelength_band,
        "sky_coverage_deg2": float(row.sky_coverage_deg2) if row.sky_coverage_deg2 is not None else None,
        "sky_coverage_note": row.sky_coverage_note,
        "redshift_range": row.redshift_range,
        "instruments": row.instruments_json if isinstance(row.instruments_json, list) else json.loads(row.instruments_json or "[]"),
        "current_data_release": row.current_data_release,
        "data_volume": row.data_volume,
        "primary_science_goals": row.primary_science_goals,
        "flagship_programs": row.flagship_programs_json if isinstance(row.flagship_programs_json, list) else json.loads(row.flagship_programs_json or "[]"),
        "operator": row.operator,
        "status": row.status,
        "archive_url": row.archive_url,
        "mission_url": row.mission_url,
        "linked_research_ideas_count": linked_count,
        "updated_at": row.updated_at.isoformat() if row.updated_at else None,
        "wavelength_center_um": float(row.wavelength_center_um) if row.wavelength_center_um is not None else None,
        "z_max": float(row.z_max) if row.z_max is not None else None,
        "dr_year": int(row.dr_year) if row.dr_year is not None else None,
        "data_volume_tb": float(row.data_volume_tb) if row.data_volume_tb is not None else None,
        "limiting_magnitude": float(row.limiting_magnitude) if row.limiting_magnitude is not None else None,
        "num_sources_count": int(row.num_sources_count) if row.num_sources_count is not None else None,
    }


def _idea_counts_by_survey_id(db: Session) -> dict:
    """Return a mapping of survey_id → idea count, safe if the join table doesn't exist."""
    try:
        rows = db.execute(text(
            "SELECT survey_id, count(*) as cnt FROM research_idea_surveys GROUP BY survey_id"
        )).fetchall()
        return {r.survey_id: r.cnt for r in rows}
    except Exception:
        return {}


def _release_row_to_dict(row) -> dict:
    return {
        "label": row.label,
        "release_date": row.release_date.isoformat() if row.release_date else None,
        "release_year": int(row.release_year) if row.release_year is not None else None,
        "summary": row.summary,
        "n_objects": int(row.n_objects) if row.n_objects is not None else None,
        "sky_coverage_deg2": float(row.sky_coverage_deg2) if row.sky_coverage_deg2 is not None else None,
        "data_volume_tb": float(row.data_volume_tb) if row.data_volume_tb is not None else None,
        "doi": row.doi,
        "bibcode": row.bibcode,
        "url": row.url,
        "status": row.status,
    }


def _catalog_field_row_to_dict(row) -> dict:
    return {
        "name": row.name,
        "dtype": row.dtype,
        "unit": row.unit,
        "ucd": row.ucd,
        "description": row.description,
        "example": row.example,
        "is_key": bool(row.is_key),
        "source_url": row.source_url,
    }


def _dataset_row_to_dict(row, catalog_fields: list[dict] | None = None) -> dict:
    return {
        "slug": row.slug,
        "name": row.name,
        "full_name": row.full_name,
        "description": row.description,
        "data_type": row.data_type,
        "release_label": row.release_label,
        "release_year": int(row.release_year) if row.release_year is not None else None,
        "sample_size": int(row.sample_size) if row.sample_size is not None else None,
        "doi": row.doi,
        "bibcode": row.bibcode,
        "registry": row.registry,
        "license": row.license,
        "primary_url": row.primary_url,
        "archive_url": row.archive_url,
        "url_verified_ok": row.url_verified_ok,
        "catalog_fields": catalog_fields or [],
    }


def _facility_profile_row_to_dict(row) -> dict:
    return {
        "slug": row.slug,
        "short_name": row.short_name,
        "full_name": row.full_name,
        "relation_type": row.relation_type,
        "is_primary": bool(row.is_primary),
        "event_count": int(row.event_count or 0),
        "upcoming_count": int(row.upcoming_count or 0),
    }


def _get_survey_identity(slug: str, db: Session):
    survey_row = db.execute(
        text("SELECT id, slug, name FROM surveys WHERE slug = :slug"), {"slug": slug}
    ).fetchone()
    if survey_row is None:
        raise HTTPException(status_code=404, detail=f"Survey '{slug}' not found")
    return survey_row


def _get_survey_facility_profiles(survey_id: int, db: Session) -> list[dict]:
    try:
        rows = db.execute(text("""
            SELECT fp.slug, fp.short_name, fp.full_name,
                   sfl.relation_type, sfl.is_primary,
                   (
                     SELECT count(*)
                     FROM facility_news_items fni
                     WHERE fni.facility_id = fp.id
                   ) AS event_count,
                   (
                     SELECT count(*)
                     FROM facility_news_items fni
                     WHERE fni.facility_id = fp.id
                       AND fni.occurs_at >= NOW()
                   ) AS upcoming_count
            FROM survey_facility_links sfl
            JOIN facility_profiles fp ON fp.id = sfl.facility_profile_id
            WHERE sfl.survey_id = :sid
            ORDER BY sfl.is_primary DESC, fp.short_name ASC NULLS LAST, fp.slug ASC
        """), {"sid": survey_id}).fetchall()
    except Exception:
        return []
    return [_facility_profile_row_to_dict(row) for row in rows]


def _get_survey_releases(survey_id: int, db: Session) -> list[dict]:
    try:
        rows = db.execute(text("""
            SELECT label, release_date, release_year, summary, n_objects,
                   sky_coverage_deg2, data_volume_tb, doi, bibcode, url, status
            FROM survey_data_releases
            WHERE survey_id = :sid
            ORDER BY release_year DESC NULLS LAST,
                     release_date DESC NULLS LAST,
                     id DESC
        """), {"sid": survey_id}).fetchall()
    except Exception:
        return []
    return [_release_row_to_dict(r) for r in rows]


def _get_survey_datasets_count(survey_id: int, db: Session) -> int:
    try:
        return int(db.execute(
            text("SELECT count(*) FROM survey_datasets WHERE survey_id = :sid"),
            {"sid": survey_id},
        ).scalar() or 0)
    except Exception:
        return 0


@router.get("")
def list_surveys(
    wavelength_band: str | None = Query(default=None),
    status: str | None = Query(default=None),
    sort: str = Query(default="name"),
    q: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    base = "SELECT s.*, s.id as survey_id FROM surveys s WHERE 1=1"
    params: dict = {}
    if wavelength_band:
        base += " AND s.wavelength_band = :band"
        params["band"] = wavelength_band
    if status:
        base += " AND s.status = :status"
        params["status"] = status
    if q:
        base += (
            " AND (UPPER(s.name) LIKE UPPER(:q) OR UPPER(s.full_name) LIKE UPPER(:q)"
            " OR UPPER(s.description) LIKE UPPER(:q) OR UPPER(s.primary_science_goals) LIKE UPPER(:q))"
        )
        params["q"] = f"%{q}%"

    order_clause = {
        "name": "s.name ASC",
        "-sky_coverage_deg2": "s.sky_coverage_deg2 DESC NULLS LAST",
        "-updated_at": "s.updated_at DESC",
    }.get(sort, "s.name ASC")
    base += f" ORDER BY {order_clause}"

    rows = db.execute(text(base), params).fetchall()
    counts = _idea_counts_by_survey_id(db)
    id_to_row = {}
    for r in rows:
        id_to_row[r.id] = r

    result = []
    for r in rows:
        d = _survey_row_to_dict(r, counts.get(r.id, 0))
        result.append(d)

    return {"count": len(result), "surveys": result}


@router.get("/{slug}")
def get_survey(slug: str, db: Session = Depends(get_db)):
    row = db.execute(
        text("SELECT * FROM surveys WHERE slug = :slug"), {"slug": slug}
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Survey '{slug}' not found")

    counts = _idea_counts_by_survey_id(db)
    detail = _survey_row_to_dict(row, counts.get(row.id, 0))

    # Related wiki pages via survey_wiki_pages
    try:
        page_rows = db.execute(text(
            "SELECT wp.slug, wp.title FROM survey_wiki_pages swp"
            " JOIN wiki_pages wp ON wp.id = swp.page_id"
            " WHERE swp.survey_id = :sid ORDER BY wp.title"
        ), {"sid": row.id}).fetchall()
        detail["related_wiki_page_slugs"] = [p.slug for p in page_rows]
    except Exception:
        detail["related_wiki_page_slugs"] = []

    detail["data_releases"] = _get_survey_releases(row.id, db)
    detail["datasets_count"] = _get_survey_datasets_count(row.id, db)
    detail["facility_profiles"] = _get_survey_facility_profiles(row.id, db)

    return detail


@router.get("/{slug}/events")
def get_survey_events(
    slug: str,
    past_days: int = Query(default=180, ge=0, le=180),
    upcoming_days: int = Query(default=730, ge=0, le=730),
    limit: int = Query(default=8, ge=1, le=50),
    db: Session = Depends(get_db),
):
    survey_row = _get_survey_identity(slug, db)
    since = datetime.utcnow() - timedelta(days=past_days)
    until = datetime.utcnow() + timedelta(days=upcoming_days)

    linked = db.execute(text("""
        SELECT count(*)
        FROM survey_facility_links
        WHERE survey_id = :sid
    """), {"sid": survey_row.id}).scalar() or 0
    if not linked:
        return {
            "survey": {"slug": survey_row.slug, "name": survey_row.name},
            "count": 0,
            "events": [],
        }

    params = {"sid": survey_row.id, "since": since, "until": until}
    count = int(db.execute(text("""
        SELECT count(*)
        FROM survey_facility_links sfl
        JOIN facility_profiles fp ON fp.id = sfl.facility_profile_id
        JOIN facility_news_items fni ON fni.facility_id = fp.id
        WHERE sfl.survey_id = :sid
          AND (fni.occurs_at BETWEEN :since AND :until OR fni.occurs_at IS NULL)
    """), params).scalar() or 0)

    rows = db.execute(text("""
        SELECT fni.id, fni.slug, fni.title, fni.kind, fni.track, fni.summary,
               fni.occurs_at, fni.occurs_at_confidence, fni.occurrence_status,
               fni.source_url, fni.data_portal_urls, fni.featured, fni.credibility_score,
               fni.created_at,
               fp.slug AS facility_slug,
               COALESCE(fp.short_name, fp.full_name, fp.slug) AS facility_name,
               fp.homepage_url AS facility_url
        FROM survey_facility_links sfl
        JOIN facility_profiles fp ON fp.id = sfl.facility_profile_id
        JOIN facility_news_items fni ON fni.facility_id = fp.id
        WHERE sfl.survey_id = :sid
          AND (fni.occurs_at BETWEEN :since AND :until OR fni.occurs_at IS NULL)
        ORDER BY
          CASE WHEN fni.occurs_at >= NOW() THEN 0 ELSE 1 END,
          fni.featured DESC,
          CASE WHEN fni.occurs_at >= NOW() THEN fni.occurs_at END ASC NULLS LAST,
          CASE WHEN fni.occurs_at < NOW() THEN fni.occurs_at END DESC NULLS LAST,
          fni.created_at DESC
        LIMIT :limit
    """), {**params, "limit": limit}).fetchall()

    return {
        "survey": {"slug": survey_row.slug, "name": survey_row.name},
        "count": count,
        "events": [dict(row._mapping) for row in rows],
    }


@router.get("/{slug}/releases")
def get_survey_releases(slug: str, db: Session = Depends(get_db)):
    survey_row = _get_survey_identity(slug, db)
    releases = _get_survey_releases(survey_row.id, db)
    return {
        "survey": {"slug": survey_row.slug, "name": survey_row.name},
        "count": len(releases),
        "releases": releases,
    }


@router.get("/{slug}/datasets")
def get_survey_datasets(slug: str, db: Session = Depends(get_db)):
    survey_row = _get_survey_identity(slug, db)

    try:
        dataset_rows = db.execute(text("""
            SELECT id, slug, name, full_name, description, data_type,
                   release_label, release_year, sample_size, doi, bibcode,
                   registry, license, primary_url, archive_url, url_verified_ok
            FROM survey_datasets
            WHERE survey_id = :sid
            ORDER BY release_year DESC NULLS LAST, name ASC
        """), {"sid": survey_row.id}).fetchall()
    except Exception:
        dataset_rows = []

    dataset_ids = [r.id for r in dataset_rows]
    fields_by_dataset: dict[int, list[dict]] = {dataset_id: [] for dataset_id in dataset_ids}

    if dataset_ids:
        try:
            field_rows = db.execute(text("""
                SELECT dataset_id, name, dtype, unit, ucd, description,
                       example, is_key, source_url
                FROM survey_catalog_fields
                WHERE dataset_id = ANY(:dataset_ids)
                ORDER BY dataset_id, is_key DESC, sort_order ASC, name ASC
            """), {"dataset_ids": dataset_ids}).fetchall()
            for row in field_rows:
                fields_by_dataset.setdefault(row.dataset_id, []).append(_catalog_field_row_to_dict(row))
        except Exception:
            pass

    datasets = [
        _dataset_row_to_dict(row, fields_by_dataset.get(row.id, []))
        for row in dataset_rows
    ]

    return {
        "survey": {"slug": survey_row.slug, "name": survey_row.name},
        "count": len(datasets),
        "datasets": datasets,
    }


@router.get("/{slug}/ideas")
def get_survey_ideas(
    slug: str,
    include_stale: bool = Query(default=False),
    db: Session = Depends(get_db),
):
    survey_row = db.execute(
        text("SELECT id, name FROM surveys WHERE slug = :slug"), {"slug": slug}
    ).fetchone()
    if survey_row is None:
        raise HTTPException(status_code=404, detail=f"Survey '{slug}' not found")

    status_clause = "" if include_stale else "AND ri.status NOT IN ('stale', 'rejected')"
    try:
        rows = db.execute(text(f"""
            SELECT ri.id, ri.survey_combo, ri.question, ri.novelty, ri.feasibility,
                   ri.saved_by_papa, ri.status, wp.slug as page_slug, wp.title as page_title
            FROM research_ideas ri
            JOIN research_idea_surveys ris ON ris.idea_id = ri.id
            JOIN wiki_pages wp ON wp.id = ri.page_id
            WHERE ris.survey_id = :sid {status_clause}
            ORDER BY ri.novelty DESC, ri.id DESC
        """), {"sid": survey_row.id}).fetchall()
    except Exception:
        rows = []

    ideas = [
        {
            "id": r.id,
            "page_slug": r.page_slug,
            "page_title": r.page_title,
            "survey_combo": r.survey_combo,
            "question": r.question,
            "novelty": float(r.novelty),
            "feasibility": float(r.feasibility),
            "saved_by_papa": r.saved_by_papa,
            "status": r.status,
        }
        for r in rows
    ]
    return {"survey": {"slug": slug, "name": survey_row.name}, "count": len(ideas), "ideas": ideas}


@router.get("/{slug}/pages")
def get_survey_pages(slug: str, db: Session = Depends(get_db)):
    survey_row = db.execute(
        text("SELECT id, name FROM surveys WHERE slug = :slug"), {"slug": slug}
    ).fetchone()
    if survey_row is None:
        raise HTTPException(status_code=404, detail=f"Survey '{slug}' not found")

    try:
        rows = db.execute(text(
            "SELECT wp.slug, wp.title, wp.is_featured FROM survey_wiki_pages swp"
            " JOIN wiki_pages wp ON wp.id = swp.page_id"
            " WHERE swp.survey_id = :sid ORDER BY wp.title"
        ), {"sid": survey_row.id}).fetchall()
    except Exception:
        rows = []

    return {
        "survey": {"slug": slug, "name": survey_row.name},
        "pages": [{"slug": r.slug, "title": r.title, "is_featured": getattr(r, "is_featured", False)} for r in rows],
    }

@router.get("/{slug}/quality")
def get_survey_quality(slug: str, db: Session = Depends(get_db)):
    row = db.execute(
        text("SELECT * FROM surveys WHERE slug = :slug"), {"slug": slug}
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Survey '{slug}' not found")

    survey = dict(row._mapping)

    try:
        from app.services.survey_health import compute_survey_health, compute_quality
        aok = survey.get("url_archive_ok", True)
        mok = survey.get("url_mission_ok", True)
        health = compute_survey_health(survey, url_archive_ok=aok, url_mission_ok=mok)
        quality = compute_quality(survey, utility_score=None,
                                  url_archive_ok=aok, url_mission_ok=mok)

        components = {
            "field_completeness":       health.components.field_completeness,
            "description_richness":     health.components.description_richness,
            "science_goals_specificity": health.components.science_goals_specificity,
            "url_validity":             health.components.url_validity,
            "dr_freshness":             health.components.dr_freshness,
            "instruments_count":        health.components.instruments_count,
            "programs_count":           health.components.programs_count,
        }
    except Exception as exc:
        import logging
        logging.getLogger(__name__).warning("quality compute failed for %s: %s", slug, exc)
        quality = survey.get("quality_score")
        components = {}

    return {
        "slug": slug,
        "name": survey.get("name"),
        "quality_score": quality,
        "quality_updated_at": survey.get("quality_updated_at"),
        "url_archive_ok": survey.get("url_archive_ok"),
        "url_mission_ok": survey.get("url_mission_ok"),
        "url_checked_at": survey.get("url_checked_at"),
        "components": components,
    }
