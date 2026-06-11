from __future__ import annotations

from sqlalchemy import text


CITATION_RULES = """Citation rules:
- DO NOT write inline citations in (Author et al. Year) format.
- Evidence is linked via <!--cite:EVIDENCE_ID--> markers.
- When prose asserts a claim backed by a specific paper, insert <!--cite:EVIDENCE_ID--> immediately after the assertion.
- Use only evidence IDs provided in the EVIDENCE MAP below.
- If no evidence ID is available for an assertion, write it without a citation marker.
- DO NOT invent author names, years, or evidence IDs."""


def build_evidence_map(db, page_id: int, max_rows: int = 80, section: str | None = None) -> str:
    section_filter = ""
    params: dict[str, object] = {"pid": page_id, "n": max_rows}
    if section:
        section_filter = "AND (c.section = :section OR c.section ILIKE :section_like)"
        params["section"] = section
        params["section_like"] = f"%{section}%"

    rows = db.execute(
        text(
            f"""
            SELECT DISTINCT ON (pcl.evidence_id)
                pcl.evidence_id,
                pcl.author_year_key,
                e.title,
                COALESCE(e.quality, 0.0) AS quality
            FROM page_citation_links pcl
            JOIN evidence e ON e.id = pcl.evidence_id
            LEFT JOIN claims c ON c.id = e.claim_id
            WHERE pcl.page_id = :pid
            {section_filter}
            ORDER BY pcl.evidence_id, COALESCE(e.quality, 0.0) DESC
            LIMIT :n
            """
        ),
        params,
    ).fetchall()
    if not rows:
        return ""
    lines = [
        f"  {row.evidence_id} -> {row.author_year_key}: {(row.title or '')[:100]}"
        for row in rows
    ]
    return "EVIDENCE MAP (use these IDs in <!--cite:N--> markers):\n" + "\n".join(lines)


def emit_citation_scrub_required(page_id: int) -> None:
    try:
        from app.agent_loop.autowiki.tasks import align_citations_page

        align_citations_page.delay(page_id)
    except Exception:
        pass
