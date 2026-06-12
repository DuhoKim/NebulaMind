"""Admin endpoint: /admin/marker-audit?page_id=N

Serves the pilot_audit.html for a given page, generated on-demand from the
most recent claim_marker_runs row and the corresponding page_versions content.
"""
import html
import re

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter(prefix="/admin", tags=["admin"])

_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Marker Audit — page {page_id}</title>
<style>
body{{font-family:system-ui,sans-serif;max-width:1200px;margin:2em auto;padding:0 1em;}}
h1{{font-size:1.3em;}}
.summary{{background:#f5f5f5;padding:1em;border-radius:4px;margin-bottom:1.5em;font-size:.9em;}}
table{{width:100%;border-collapse:collapse;font-size:.85em;}}
th{{background:#222;color:#fff;padding:6px 10px;text-align:left;}}
td{{padding:6px 10px;border-bottom:1px solid #ddd;vertical-align:top;max-width:320px;word-break:break-word;}}
tr:hover td{{background:#fafafa;}}
.hl{{background:#ffe066;}}
.accepted{{color:#1a7a1a;font-weight:bold;}}
.debated{{color:#cc7700;font-weight:bold;}}
.challenged{{color:#cc1a1a;font-weight:bold;}}
.consensus-candidates{{color:#0055cc;font-weight:bold;}}
</style>
</head>
<body>
<h1>Marker Embed Audit — page_id={page_id}</h1>
<div class="summary">{summary}</div>
<table>
<thead><tr>
  <th>#</th><th>Claim ID</th><th>Trust</th><th>Section</th>
  <th>Claim text</th><th>Injected span (in context)</th>
</tr></thead>
<tbody>{rows}</tbody>
</table>
</body>
</html>
"""

_ROW = (
    "<tr><td>{i}</td><td>{cid}</td>"
    "<td class='{tc}'>{tl}</td><td>{sec}</td>"
    "<td>{ct}</td><td>{span_ctx}</td></tr>"
)


def _tc(trust: str) -> str:
    return (trust or "").lower().replace(" ", "-").replace("_", "-")


def _highlight(context: str, span: str) -> str:
    if not span or span not in context:
        return html.escape(context)
    idx = context.index(span)
    return (
        html.escape(context[:idx])
        + f'<span class="hl">{html.escape(span)}</span>'
        + html.escape(context[idx + len(span) :])
    )


@router.get("/marker-audit", response_class=HTMLResponse)
def marker_audit(page_id: int, db: Session = Depends(get_db)):
    from sqlalchemy import text

    run = db.execute(
        text("""
            SELECT id, page_version, total_claims, matched_claims,
                   mean_confidence, judge_agreement_pct, coverage_pct, status, notes
            FROM claim_marker_runs
            WHERE page_id = :pid
            ORDER BY run_started_at DESC LIMIT 1
        """),
        {"pid": page_id},
    ).fetchone()

    if not run:
        raise HTTPException(404, "No marker_embed runs found for this page")

    run_id, pv_num, total, matched, mean_conf, judge_pct, cov_pct, status, notes = run

    summary = (
        f"<b>Run:</b> {run_id} &nbsp;|&nbsp; "
        f"<b>PV:</b> {pv_num} &nbsp;|&nbsp; "
        f"<b>Status:</b> {html.escape(status or '')} &nbsp;|&nbsp; "
        f"<b>Coverage:</b> {(cov_pct or 0):.1%} ({matched}/{total}) &nbsp;|&nbsp; "
        f"<b>Mean conf:</b> {(mean_conf or 0):.3f} &nbsp;|&nbsp; "
        f"<b>Judge agree:</b> {(judge_pct or 0):.1%}"
    )
    if notes:
        summary += f"<br><b>Notes:</b> {html.escape(notes)}"

    pv_content = ""
    if pv_num:
        pv_row = db.execute(
            text("SELECT content FROM page_versions WHERE page_id=:pid AND version_num=:v"),
            {"pid": page_id, "v": pv_num},
        ).fetchone()
        if pv_row:
            pv_content = pv_row[0]

    # Build span map from injected content
    span_map: dict[int, str] = {}
    if pv_content:
        for m in re.finditer(r"<!--claim:(\d+)-->(.*?)<!--/claim:\1-->", pv_content, re.DOTALL):
            span_map[int(m.group(1))] = m.group(2)

    claims = db.execute(
        text(
            "SELECT id, text, trust_level, section FROM claims "
            "WHERE page_id=:pid ORDER BY section, order_idx"
        ),
        {"pid": page_id},
    ).fetchall()

    rows_html = ""
    for i, (cid, ctext, trust, sec) in enumerate(claims, 1):
        span = span_map.get(cid, "")
        if span and pv_content:
            pos = pv_content.find(span)
            if pos >= 0:
                raw = pv_content[max(0, pos - 80) : pos + len(span) + 80]
                clean = re.sub(r"<!--/?claim:\d+-->", "", raw)
                span_ctx = _highlight(clean, span)
            else:
                span_ctx = f'<span class="hl">{html.escape(span)}</span>'
        else:
            span_ctx = "<em>no marker</em>"

        rows_html += _ROW.format(
            i=i,
            cid=cid,
            tc=_tc(trust or ""),
            tl=html.escape(trust or ""),
            sec=html.escape(sec or ""),
            ct=html.escape(ctext or ""),
            span_ctx=span_ctx,
        )

    return _HTML.format(page_id=page_id, summary=summary, rows=rows_html)
