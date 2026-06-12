"""Admin endpoints for survey update proposals and auto-apply log (§3.2, §3.5b, §7.2)."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter(prefix="/api/admin/surveys", tags=["admin-surveys"])


@router.get("/proposals")
def list_proposals(
    status: str = "pending",
    db: Session = Depends(get_db),
):
    rows = db.execute(text("""
        SELECT p.*, s.name as survey_name, s.slug as survey_slug
        FROM survey_update_proposals p
        JOIN surveys s ON s.id = p.survey_id
        WHERE p.status = :status
        ORDER BY p.created_at DESC
    """), {"status": status}).fetchall()
    return {
        "count": len(rows),
        "proposals": [_proposal_to_dict(r) for r in rows],
    }


@router.post("/proposals/{proposal_id}/approve")
def approve_proposal(proposal_id: int, db: Session = Depends(get_db)):
    """Apply a HIGH-tier survey update proposal (Papa one-click approve, §3.2, §7.1)."""
    row = db.execute(
        text("SELECT * FROM survey_update_proposals WHERE id = :id"), {"id": proposal_id}
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Proposal {proposal_id} not found")
    if row.status != "pending":
        raise HTTPException(status_code=409, detail=f"Proposal is already '{row.status}'")

    # Apply the field update
    allowed_fields = {
        "current_data_release", "status", "sky_coverage_deg2", "flagship_programs_json",
        "instruments_json", "wavelength_range", "wavelength_band", "redshift_range",
        "archive_url", "mission_url", "data_volume", "description",
    }
    if row.field not in allowed_fields:
        raise HTTPException(status_code=400, detail=f"Field '{row.field}' not updatable via this endpoint")

    db.execute(
        text(f"UPDATE surveys SET {row.field} = :val, updated_at = NOW() WHERE id = :sid"),
        {"val": row.proposed_value, "sid": row.survey_id},
    )
    db.execute(
        text("""
            UPDATE survey_update_proposals
            SET status = 'approved', reviewed_at = NOW(), reviewed_by = 'papa'
            WHERE id = :id
        """),
        {"id": proposal_id},
    )
    db.commit()

    # Discord notification
    try:
        import httpx
        from app.config import settings
        url = getattr(settings, "NM_DISCORD_WEBHOOK_URL", None) or settings.DISCORD_WEBHOOK_URL
        survey_name = db.execute(
            text("SELECT name FROM surveys WHERE id = :sid"), {"sid": row.survey_id}
        ).fetchone()
        name = survey_name.name if survey_name else f"survey_id={row.survey_id}"
        msg = (f"✅ Survey proposal #{proposal_id} approved — "
               f"`{name}` `{row.field}`: `{(row.current_value or 'none')[:60]}` → `{row.proposed_value[:60]}`")
        if url:
            httpx.post(url, json={"content": msg}, timeout=8)
    except Exception:
        pass

    return {
        "proposal_id": proposal_id,
        "status": "approved",
        "survey_id": row.survey_id,
        "field": row.field,
        "applied_value": row.proposed_value,
    }


@router.post("/proposals/{proposal_id}/reject")
def reject_proposal(proposal_id: int, db: Session = Depends(get_db)):
    row = db.execute(
        text("SELECT id, status FROM survey_update_proposals WHERE id = :id"), {"id": proposal_id}
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Proposal {proposal_id} not found")
    if row.status != "pending":
        raise HTTPException(status_code=409, detail=f"Proposal is already '{row.status}'")
    db.execute(
        text("UPDATE survey_update_proposals SET status='rejected', reviewed_at=NOW(), reviewed_by='papa' WHERE id=:id"),
        {"id": proposal_id},
    )
    db.commit()
    return {"proposal_id": proposal_id, "status": "rejected"}


@router.get("/autoapply-log")
def list_autoapply_log(limit: int = 50, db: Session = Depends(get_db)):
    rows = db.execute(text("""
        SELECT l.*, s.name as survey_name, s.slug as survey_slug
        FROM survey_autoapply_log l
        JOIN surveys s ON s.id = l.survey_id
        ORDER BY l.applied_at DESC
        LIMIT :n
    """), {"n": limit}).fetchall()
    return {
        "count": len(rows),
        "entries": [
            {
                "id":           r.id,
                "survey_name":  r.survey_name,
                "survey_slug":  r.survey_slug,
                "field":        r.field,
                "old_value":    r.old_value,
                "new_value":    r.new_value,
                "source_kind":  r.source_kind,
                "source_url":   r.source_url,
                "confidence":   float(r.confidence) if r.confidence is not None else None,
                "applied_at":   r.applied_at.isoformat() if r.applied_at else None,
                "reverted_at":  r.reverted_at.isoformat() if r.reverted_at else None,
            }
            for r in rows
        ],
    }


def _proposal_to_dict(r) -> dict:
    return {
        "id":             r.id,
        "survey_name":    r.survey_name,
        "survey_slug":    r.survey_slug,
        "field":          r.field,
        "current_value":  r.current_value,
        "proposed_value": r.proposed_value,
        "source_kind":    r.source_kind,
        "source_url":     r.source_url,
        "source_excerpt": r.source_excerpt,
        "confidence":     float(r.confidence) if r.confidence is not None else None,
        "status":         r.status,
        "created_at":     r.created_at.isoformat() if r.created_at else None,
        "reviewed_at":    r.reviewed_at.isoformat() if r.reviewed_at else None,
    }
