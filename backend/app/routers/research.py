"""
arXiv Research Frontier router.
Fetches latest papers from arXiv and matches them to NebulaMind wiki pages.
"""
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Optional

import httpx
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.page import WikiPage

router = APIRouter(prefix="/api/research", tags=["research"])

ARXIV_BASE = "http://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom"}

VALID_CATEGORIES = {
    "astro-ph",
    "astro-ph.GA",
    "astro-ph.HE",
    "astro-ph.CO",
    "astro-ph.SR",
    "astro-ph.EP",
    "astro-ph.IM",
}


class ArxivPaper(BaseModel):
    arxiv_id: str
    title: str
    authors: list[str]
    abstract_summary: str
    submitted: str
    related_pages: list[str]
    url: str


def _parse_date(date_str: str) -> str:
    """Parse arXiv date string to YYYY-MM-DD."""
    try:
        return datetime.fromisoformat(date_str.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except Exception:
        return date_str[:10] if len(date_str) >= 10 else date_str


def _match_pages(title: str, abstract: str, pages: list[WikiPage]) -> list[str]:
    """Return slugs of wiki pages whose titles appear in the paper title or abstract."""
    combined = (title + " " + abstract).lower()
    matched = []
    for page in pages:
        # Match on multi-word title (at least 3 chars) or slug keywords
        page_title_lower = page.title.lower()
        if len(page_title_lower) >= 3 and page_title_lower in combined:
            matched.append(page.slug)
    return matched


@router.get("/arxiv", response_model=list[ArxivPaper])
def get_arxiv_papers(
    category: str = Query(default="astro-ph", description="arXiv category (e.g. astro-ph, astro-ph.GA)"),
    limit: int = Query(default=10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    """
    Fetch latest papers from arXiv for the given astronomy category,
    and match them to NebulaMind wiki pages by keyword.
    """
    # Sanitize category
    if category not in VALID_CATEGORIES:
        category = "astro-ph"

    url = (
        f"{ARXIV_BASE}?search_query=cat:{category}"
        f"&sortBy=submittedDate&sortOrder=descending&max_results={limit}"
    )

    try:
        resp = httpx.get(url, timeout=15)
        resp.raise_for_status()
        xml_text = resp.text
    except Exception as exc:
        return []  # graceful degradation

    # Parse XML
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []

    # Load all wiki pages for matching
    wiki_pages = db.query(WikiPage).all()

    papers = []
    for entry in root.findall("atom:entry", NS):
        # arxiv ID
        id_el = entry.find("atom:id", NS)
        if id_el is None or id_el.text is None:
            continue
        raw_id = id_el.text.strip()
        arxiv_id = raw_id.split("/abs/")[-1] if "/abs/" in raw_id else raw_id

        title_el = entry.find("atom:title", NS)
        title = (title_el.text or "").strip().replace("\n", " ") if title_el is not None else ""

        summary_el = entry.find("atom:summary", NS)
        abstract = (summary_el.text or "").strip().replace("\n", " ") if summary_el is not None else ""
        abstract_summary = abstract[:200] + ("..." if len(abstract) > 200 else "")

        published_el = entry.find("atom:published", NS)
        submitted = _parse_date(published_el.text.strip()) if published_el is not None and published_el.text else ""

        authors = []
        for author_el in entry.findall("atom:author", NS):
            name_el = author_el.find("atom:name", NS)
            if name_el is not None and name_el.text:
                authors.append(name_el.text.strip())

        related_pages = _match_pages(title, abstract, wiki_pages)

        papers.append(ArxivPaper(
            arxiv_id=arxiv_id,
            title=title,
            authors=authors,
            abstract_summary=abstract_summary,
            submitted=submitted,
            related_pages=related_pages,
            url=f"https://arxiv.org/abs/{arxiv_id}",
        ))

    return papers
