"""Generate pilot_audit.html for the marker embed pipeline.

Usage:
    .venv/bin/python scripts/marker_audit_report.py --page-slug galaxy-evolution [--output pilot_audit.html]

Reads the most recent claim_marker_runs row for the page and produces an HTML
table with: claim_id, claim_text, trust_level, chosen_span (highlighted in
context), Buddle confidence, Atom-7B agreement, and the page version that
was written.
"""
import argparse
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Marker Embed Audit — {page_slug}</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 1200px; margin: 2em auto; padding: 0 1em; }}
h1 {{ font-size: 1.4em; }}
.summary {{ background: #f5f5f5; padding: 1em; border-radius: 4px; margin-bottom: 1.5em; }}
table {{ width: 100%; border-collapse: collapse; font-size: 0.88em; }}
th {{ background: #222; color: #fff; padding: 6px 10px; text-align: left; }}
td {{ padding: 6px 10px; border-bottom: 1px solid #ddd; vertical-align: top; }}
tr:hover td {{ background: #fafafa; }}
.span-highlight {{ background: #ffe066; padding: 1px 0; }}
.trust-accepted {{ color: #1a7a1a; font-weight: bold; }}
.trust-consensus-candidates {{ color: #0055cc; font-weight: bold; }}
.trust-debated {{ color: #cc7700; font-weight: bold; }}
.trust-challenged {{ color: #cc1a1a; font-weight: bold; }}
.conf-high {{ color: #1a7a1a; }}
.conf-mid {{ color: #cc7700; }}
.conf-low {{ color: #cc1a1a; }}
</style>
</head>
<body>
<h1>Marker Embed Pilot Audit — {page_slug}</h1>
<div class="summary">
  <strong>Run ID:</strong> {run_id} &nbsp;|&nbsp;
  <strong>Page Version:</strong> {page_version} &nbsp;|&nbsp;
  <strong>Status:</strong> {status} &nbsp;|&nbsp;
  <strong>Coverage:</strong> {coverage_pct:.1%} ({matched_claims}/{total_claims}) &nbsp;|&nbsp;
  <strong>Mean confidence:</strong> {mean_confidence:.3f} &nbsp;|&nbsp;
  <strong>Judge agreement:</strong> {judge_agreement_pct:.1%}
</div>
<table>
<thead>
<tr>
  <th>#</th><th>Claim ID</th><th>Trust</th><th>Claim text</th>
  <th>Section</th><th>Span (in context)</th>
</tr>
</thead>
<tbody>
{rows}
</tbody>
</table>
</body>
</html>
"""

_ROW_TEMPLATE = """\
<tr>
  <td>{idx}</td>
  <td>{claim_id}</td>
  <td class="trust-{trust_class}">{trust_level}</td>
  <td>{claim_text}</td>
  <td>{section}</td>
  <td>{span_context}</td>
</tr>"""


def _trust_class(trust_level: str) -> str:
    return trust_level.lower().replace(" ", "-").replace("_", "-")


def _highlight_span(sentence: str, span: str) -> str:
    if not span or span not in sentence:
        return html.escape(sentence)
    idx = sentence.index(span)
    before = html.escape(sentence[:idx])
    middle = html.escape(span)
    after = html.escape(sentence[idx + len(span):])
    return f'{before}<span class="span-highlight">{middle}</span>{after}'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-slug", default="galaxy-evolution")
    parser.add_argument("--output", default="pilot_audit.html")
    args = parser.parse_args()

    from app.database import SessionLocal
    from sqlalchemy import text

    db = SessionLocal()
    try:
        page_row = db.execute(
            text("SELECT id FROM wiki_pages WHERE slug = :slug"),
            {"slug": args.page_slug},
        ).fetchone()
        if not page_row:
            print(f"Page not found: {args.page_slug}")
            sys.exit(1)
        page_id = page_row[0]

        run_row = db.execute(
            text("""
                SELECT id, page_version, source_version, total_claims, matched_claims,
                       mean_confidence, judge_agreement_pct, coverage_pct, status
                FROM claim_marker_runs
                WHERE page_id = :pid
                ORDER BY run_started_at DESC LIMIT 1
            """),
            {"pid": page_id},
        ).fetchone()
        if not run_row:
            print("No claim_marker_runs found for this page.")
            sys.exit(1)

        run_id, page_version, _, total_claims, matched_claims, mean_conf, judge_pct, cov_pct, status = run_row

        # Get the page version content to extract injected spans
        pv_content = None
        if page_version:
            pv_row = db.execute(
                text("SELECT content FROM page_versions WHERE page_id=:pid AND version_num=:v"),
                {"pid": page_id, "v": page_version},
            ).fetchone()
            if pv_row:
                pv_content = pv_row[0]

        # Load claims
        claims = db.execute(
            text("SELECT id, text, trust_level, section FROM claims WHERE page_id=:pid ORDER BY section, order_idx"),
            {"pid": page_id},
        ).fetchall()

        # Extract injected spans from content
        span_map: dict[int, str] = {}
        if pv_content:
            for m in re.finditer(r"<!--claim:(\d+)-->(.*?)<!--/claim:\1-->", pv_content, re.DOTALL):
                cid = int(m.group(1))
                span_map[cid] = m.group(2)

        rows_html = ""
        for idx, (claim_id, claim_text, trust_level, section) in enumerate(claims, 1):
            span = span_map.get(claim_id, "")
            if span:
                # Find context: 80 chars around the span in pv_content
                span_pos = pv_content.find(span) if pv_content else -1
                if span_pos >= 0:
                    ctx_start = max(0, span_pos - 80)
                    ctx_end = min(len(pv_content), span_pos + len(span) + 80)
                    context_raw = pv_content[ctx_start:ctx_end]
                    # Strip markers for display
                    context_clean = re.sub(r"<!--/?claim:\d+-->", "", context_raw)
                    span_context = _highlight_span(context_clean, span)
                else:
                    span_context = f'<span class="span-highlight">{html.escape(span)}</span>'
            else:
                span_context = "<em>no marker</em>"

            rows_html += _ROW_TEMPLATE.format(
                idx=idx,
                claim_id=claim_id,
                trust_class=_trust_class(trust_level or ""),
                trust_level=html.escape(trust_level or ""),
                claim_text=html.escape(claim_text or ""),
                section=html.escape(section or ""),
                span_context=span_context,
            )

        report = _HTML_TEMPLATE.format(
            page_slug=html.escape(args.page_slug),
            run_id=run_id,
            page_version=page_version or "—",
            status=html.escape(status or ""),
            coverage_pct=cov_pct or 0.0,
            matched_claims=matched_claims or 0,
            total_claims=total_claims or 0,
            mean_confidence=mean_conf or 0.0,
            judge_agreement_pct=judge_pct or 0.0,
            rows=rows_html,
        )

        with open(args.output, "w") as f:
            f.write(report)
        print(f"Wrote {args.output} ({len(report):,} bytes)")

    finally:
        db.close()


if __name__ == "__main__":
    main()
