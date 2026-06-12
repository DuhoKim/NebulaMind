#!/usr/bin/env python3
"""
Verify 311 unverified arXiv Evidence rows.
Uses arXiv Atom API — returns title, abstract, year, journal_ref in one call.
Rate limit: 1 req/sec (arXiv ToS).
"""
import logging
import re
import sys
import time
import xml.etree.ElementTree as ET
from urllib.request import Request, urlopen
from urllib.error import HTTPError

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.claim import Evidence

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

DB_URL = "postgresql://nebula:nebula@localhost:5432/nebulamind"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom",
           "arxiv": "http://arxiv.org/schemas/atom"}
BATCH_COMMIT = 20
MAX_ROWS = 300

def fetch_arxiv_atom(arxiv_id: str) -> dict | None:
    """Returns {title, abstract, year, journal_ref} or None if 404/error."""
    clean = arxiv_id.replace("arXiv:", "").strip()
    url = f"http://export.arxiv.org/api/query?id_list={clean}&max_results=1"
    try:
        req = Request(url, headers={"User-Agent": "NebulaMind/1.0 (arxiv-verify)"})
        with urlopen(req, timeout=15) as resp:
            xml_bytes = resp.read()
    except Exception as exc:
        log.warning("Network error for %s: %s", arxiv_id, exc)
        return None

    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return None

    entries = root.findall("atom:entry", ATOM_NS)
    if not entries:
        return None

    entry = entries[0]
    # arXiv returns a "no-match" entry if ID is wrong
    title_el = entry.find("atom:title", ATOM_NS)
    if title_el is None:
        return None
    title = (title_el.text or "").strip()
    if not title or "Error" in title:
        return None

    summary_el = entry.find("atom:summary", ATOM_NS)
    abstract = (summary_el.text or "").strip() if summary_el is not None else ""

    published_el = entry.find("atom:published", ATOM_NS)
    year = None
    if published_el is not None and published_el.text:
        m = re.match(r"(\d{4})", published_el.text.strip())
        if m:
            year = int(m.group(1))

    journal_el = entry.find("arxiv:journal_ref", ATOM_NS)
    journal_ref = (journal_el.text or "").strip() if journal_el is not None else None

    return {
        "title": title,
        "abstract": abstract,
        "year": year,
        "journal_ref": journal_ref or None,
    }

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

with Session() as db:
    rows = (
        db.query(Evidence)
        .filter(Evidence.arxiv_verified == False, Evidence.arxiv_id.isnot(None))
        .order_by(Evidence.id)
        .limit(MAX_ROWS)
        .all()
    )
    log.info("Found %d unverified Evidence rows to process", len(rows))

    verified_ok = 0
    verified_bad = 0

    for i, ev in enumerate(rows):
        meta = fetch_arxiv_atom(ev.arxiv_id)
        if meta:
            ev.arxiv_verified = True
            if not ev.abstract:
                ev.abstract = meta["abstract"]
            if not ev.year:
                ev.year = meta["year"]
            if not ev.title or ev.title == f"arXiv:{ev.arxiv_id}":
                ev.title = meta["title"]
            if meta["journal_ref"]:
                ev.journal_ref = meta["journal_ref"]
                ev.peer_reviewed = True
            verified_ok += 1
            log.info("[%d/%d] OK  %s — %s (%s)", i+1, len(rows), ev.arxiv_id,
                     meta["title"][:60], meta["year"])
        else:
            ev.arxiv_verified = False
            ev.quality = 0.1
            verified_bad += 1
            log.warning("[%d/%d] BAD %s — not found or network error", i+1, len(rows), ev.arxiv_id)

        if (i + 1) % BATCH_COMMIT == 0:
            db.commit()
            log.info("Committed batch at row %d", i+1)

        time.sleep(1.0)  # arXiv ToS: 1 req/sec

    db.commit()
    log.info("Done. verified_ok=%d verified_bad=%d", verified_ok, verified_bad)
