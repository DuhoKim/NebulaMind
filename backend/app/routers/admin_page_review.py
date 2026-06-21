import hmac
import os

from fastapi import APIRouter, Depends, Header, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.page_review_candidate_registry import build_page_review_candidate_response


router = APIRouter(prefix="/api/admin/page-review", tags=["admin-page-review"])


def _validate_page_review_token(
    header_token: str | None,
    query_token: str | None,
) -> tuple[str, str | None]:
    expected = os.getenv("PAGE_REVIEW_TOKEN")
    if not expected:
        return "unauthenticated_local_preview", None

    supplied = header_token or query_token
    if not supplied:
        raise HTTPException(401, "Page review token required")
    if not hmac.compare_digest(supplied, expected):
        raise HTTPException(403, "Invalid page review token")
    return "token_validated", "header" if header_token else "query"


@router.get("/page/{page_id}/candidates/{candidate_id}")
def get_page_review_candidate(
    page_id: int,
    candidate_id: str,
    db: Session = Depends(get_db),
    page_review_token: str | None = Header(default=None, alias="X-Page-Review-Token"),
    review_token: str | None = Query(default=None),
):
    access_mode, token_transport = _validate_page_review_token(page_review_token, review_token)
    response = build_page_review_candidate_response(page_id, candidate_id, db)
    if response is None:
        raise HTTPException(404, "Review candidate not registered")
    access_control = response.setdefault("access_control", {})
    access_control["current_mode"] = access_mode
    access_control["token_transport"] = token_transport
    return response
