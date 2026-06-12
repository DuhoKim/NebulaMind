from __future__ import annotations
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

from scripts.align_citations import (
    tokenize_paren_citations,
    find_evidence,
    upsert_link,
    replace_citations,
    strip_hallucinated_cites,
    insert_claim_citation_markers,
    ResolvedCitation
)

def normalize_citations(db: Session, page_id: int, content: str) -> tuple[str, int]:
    matches = tokenize_paren_citations(content)
    resolved = []
    for match in matches:
        evidence_id, method, confidence = find_evidence(db, match)
        resolved.append(ResolvedCitation(match, evidence_id, method, confidence))
        if evidence_id:
            upsert_link(db, page_id, evidence_id, match.author_year_key, method, confidence)
    
    new_content = replace_citations(content, resolved)
    new_content, _ = strip_hallucinated_cites(db, page_id, new_content)
    new_content = insert_claim_citation_markers(db, page_id, new_content)
    new_content, _ = strip_hallucinated_cites(db, page_id, new_content)
    
    return new_content, len(resolved)
