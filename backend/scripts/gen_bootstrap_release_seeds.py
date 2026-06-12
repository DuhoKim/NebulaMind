"""One-shot: emit bootstrap survey_data_releases seed JSON for every survey.

Reads the live surveys table (read-only) and writes backend/seeds/survey_releases/{slug}.json
with one mechanically-derived row per survey (design doc survey_detail_page_v1.md §3.2-3).
Hand-curated T1/T3 files are written afterwards and overwrite these.
"""
import json
import re
from pathlib import Path

import psycopg2

OUT = Path(__file__).resolve().parent.parent / "seeds" / "survey_releases"
OUT.mkdir(parents=True, exist_ok=True)

conn = psycopg2.connect("postgresql://nebula:nebula@localhost:5432/nebulamind")
cur = conn.cursor()
cur.execute(
    "SELECT slug, current_data_release, dr_year, num_sources_count, archive_url, status"
    " FROM surveys ORDER BY slug"
)

LABEL_RE = re.compile(
    r"\b(DR\d+(?:\.\d+)?|PDR\d+|PR\d+(?:\s*/\s*NPIPE)?|GR\d+(?:/\d+)?|EDR|Q\d+|HDR\d+|"
    r"4FGL-DR\d+|4XMM-DR\d+|2RXS|AllWISE|eRASS\d+|DP\d+(?:\.\d+)?|IPL-\d+)\b"
)

count = 0
for slug, cdr, dr_year, n_src, archive_url, sstatus in cur.fetchall():
    cdr = cdr or ""
    m = LABEL_RE.search(cdr)
    label = m.group(1) if m else (cdr.split(" (")[0].split(";")[0].strip()[:60] or "Current")
    planned = bool(re.search(r"no data|not yet|expected|planned|under construction", cdr, re.I))
    status = "planned" if planned else ("final" if sstatus == "retired" else "released")
    row = {
        "label": label,
        "release_date": None,
        "release_year": dr_year,
        "summary": cdr or "No release information recorded.",
        "n_objects": int(n_src) if (n_src and not planned) else None,
        "sky_coverage_deg2": None,
        "data_volume_tb": None,
        "doi": None,
        "bibcode": None,
        "url": archive_url,
        "status": status,
    }
    path = OUT / f"{slug}.json"
    path.write_text(json.dumps({"survey_slug": slug, "releases": [row]}, indent=2) + "\n")
    count += 1

print(f"wrote {count} bootstrap files to {OUT}")
