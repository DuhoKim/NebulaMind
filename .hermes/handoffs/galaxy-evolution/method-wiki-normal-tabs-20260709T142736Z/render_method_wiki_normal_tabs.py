#!/usr/bin/env python3
"""Render Galaxy Evolution method wiki pages with normal NebulaMind wiki tabs.

Scope: static method artifacts only. This does not touch product DB/page_versions,
trust recompute, backend/API runtime, deploy, git, cron, billing, or external submission.
"""
from __future__ import annotations

import html
import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
ROOT = REPO / "frontend/public/agent-reports/wiki-method-results/galaxy-evolution"
RECEIPT = REPO / ".hermes/handoffs/galaxy-evolution/method-wiki-normal-tabs-20260709T142736Z"
MARKER = "NEBULAMIND_METHOD_WIKI_NORMAL_TABS_NO_TOP_CLUTTER_20260709T142736Z"

H2_SKELETON = [
    "Overview: Galaxy Evolution as a Regulated Baryon Cycle",
    "Dark Matter Halos & Structure Formation",
    "Gas Supply, Star Formation & Feedback",
    "AGN Feedback & Quenching",
    "Environment, Morphology & Structural Growth",
    "Chemical Enrichment & Cosmic Timing",
    "High-Redshift & Reionization Frontier",
    "Observational Evidence & Surveys",
    "Synthesis & Open Tensions",
]

TRUST_BY_CLAIM = {
    "2931": "debated",
    "2929": "unverified",
    "2946": "reported",
}

@dataclass(frozen=True)
class MethodSpec:
    slug: str
    num: str
    short: str
    title: str
    eyebrow: str
    lead: str
    verdict: str
    badges: List[str]
    draft: str
    body_attrs: Dict[str, str]
    source_note: str
    after_mode: str = "keep_below_article"

SPECS = [
    MethodSpec(
        slug="packet-gated-paper-to-wiki-reconciliation",
        num="1",
        short="PGR",
        title="Packet-gated paper-to-wiki reconciliation",
        eyebrow="Method 1 · packet-gated paper-to-wiki reconciliation",
        lead="Method 1 result for the Galaxy Evolution page. The method identifier stays here; the article below follows the normal NebulaMind wiki layout and controls.",
        verdict="A5 verdict: PASS",
        badges=["static method artifact", "not product wiki/page_versions", "NO ACTIVE EXECUTION PHRASE"],
        draft="pgr-same-format-draft-20260707T005045Z.md",
        body_attrs={
            "data-marker": "GALAXY_EVOLUTION_METHOD1_ULTRA_FORMAT_ROLE_SPLIT_20260707",
            "data-verdict": "HWAO_PGR_METHOD_VERDICT_20260707T040523Z",
            "data-method": "method1-packet-gated-paper-to-wiki-reconciliation",
            "data-safety": "NO_ACTIVE_EXECUTION_PHRASE",
            "data-product-published": "false",
        },
        source_note="Source draft: pgr-same-format-draft-20260707T005045Z.md. Method provenance and safety notes are below the article, not above it.",
    ),
    MethodSpec(
        slug="source-first-paper-adjudication",
        num="2",
        short="SFA",
        title="Source-first paper adjudication",
        eyebrow="Method 2 · source-first paper adjudication",
        lead="Method 2 result for the Galaxy Evolution page. The method identifier stays here; the article below keeps the normal NebulaMind wiki tabs and reader flow.",
        verdict="Hwao-m2 verdict: PASS",
        badges=["static method artifact", "not product wiki/page_versions", "NO ACTIVE EXECUTION PHRASE"],
        draft="galaxy-evolution-same-format-draft.md",
        body_attrs={
            "data-marker": "HWAO_M2_SAME_FORMAT_CONVERSION_V2_20260707T043503Z",
            "data-method": "method2-source-first-paper-adjudication",
            "data-verdict": "PASS",
            "data-safety": "NO_ACTIVE_EXECUTION_PHRASE",
            "data-product-published": "false",
        },
        source_note="Source draft: galaxy-evolution-same-format-draft.md. Accepted/rejected source-position details remain below the article only.",
    ),
    MethodSpec(
        slug="debate-map-to-wiki-rebuild",
        num="3",
        short="DMW",
        title="Debate-map-to-wiki rebuild",
        eyebrow="Method 3 · debate-map-to-wiki rebuild",
        lead="Method 3 result for the Galaxy Evolution page. The method identifier stays here; the article below reads as a normal NebulaMind wiki page, not a dashboard.",
        verdict="P2 same-format narrative draft",
        badges=["static method artifact", "not product wiki/page_versions", "NO ACTIVE EXECUTION PHRASE"],
        draft="m3-p2-same-format-draft-20260707T050500Z.md",
        body_attrs={
            "data-marker": "GALAXY_EVOLUTION_METHOD3_P15_PATCH_EXTENSION_20260707T005702Z",
            "data-method": "method3-debate-map-to-wiki-rebuild",
            "data-verdict": "P2_SAME_FORMAT_NARRATIVE_DRAFT",
            "data-safety": "NO_ACTIVE_EXECUTION_PHRASE",
            "data-product-published": "false",
        },
        source_note="Source draft: m3-p2-same-format-draft-20260707T050500Z.md. Claim/citation binding remains a separate gate.",
        after_mode="footer_note",
    ),
]

CSS = r"""
:root{color-scheme:dark;--bg:#0f172a;--panel:#111827;--panel2:#1e293b;--fg:#f8fafc;--muted:#94a3b8;--dim:#64748b;--line:#334155;--accent:#6366f1;--green:#22c55e;--blue:#3b82f6;--amber:#f59e0b;--red:#ef4444}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}a{color:#93c5fd;text-decoration:none}a:hover{text-decoration:underline}main{max-width:64rem;margin:0 auto;padding:28px 18px 72px}.method-card{margin:0 0 1rem;padding:.95rem 1rem;border:1px solid rgba(129,140,248,.45);border-radius:14px;background:linear-gradient(135deg,rgba(15,23,42,.98),rgba(30,41,59,.82));box-shadow:0 12px 28px rgba(2,6,23,.24)}.method-card .eyebrow{margin:0 0 .28rem;color:#a5b4fc;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.12em}.method-card h2{margin:.1rem 0 .35rem;color:var(--fg);font-size:clamp(1.08rem,3vw,1.55rem);line-height:1.18;font-weight:700;border:0;padding:0}.lead{margin:0 0 .55rem;color:#cbd5e1;font-size:.86rem;line-height:1.55}.status-row{display:flex;flex-wrap:wrap;gap:.35rem;margin:.25rem 0 .55rem}.status,.pill{display:inline-block;border-radius:999px;padding:.16rem .52rem;font-size:.7rem;font-weight:750;border:1px solid rgba(148,163,184,.34);color:#cbd5e1;background:rgba(15,23,42,.72)}.status{border-color:rgba(34,197,94,.48);color:#86efac;background:rgba(34,197,94,.10)}.source-note{margin:.45rem 0 0;color:var(--dim);font-size:.75rem}.wiki-shell{display:grid;grid-template-columns:minmax(0,56rem) 240px;gap:2rem;align-items:start}.wiki-main{min-width:0}.wiki-topbar{display:flex;align-items:center;gap:.5rem;margin:0 0 1.5rem;font-size:.875rem;flex-wrap:wrap}.health{font-size:.72rem;font-weight:600;padding:.15rem .5rem;border-radius:99px;background:rgba(59,130,246,.15);color:#3b82f6}.small-link{font-size:.75rem;color:#64748b;border:1px solid #334155;border-radius:4px;padding:.25rem .5rem}.small-link.first{margin-left:auto}.wiki-controls{display:flex;gap:.5rem;margin:0 0 1rem;align-items:center;flex-wrap:wrap}.tab{display:inline-block;font-size:.75rem;padding:.25rem .75rem;border-radius:4px;border:1px solid #334155;color:#94a3b8;background:transparent}.tab.active{border-color:#6366f1;background:#6366f1;color:#fff}.tab.citations{border-color:#818cf8}.tool-note{font-size:.78rem;color:#64748b;margin:0}.legend{display:flex;gap:.5rem;font-size:.75rem;color:#64748b;margin:0 0 1rem;flex-wrap:wrap}.legend span{padding-left:4px}.legend .consensus{border-left:2px solid #22c55e}.legend .accepted{border-left:2px solid #3b82f6}.legend .debated{border-left:2px solid #f59e0b}.legend .challenged{border-left:2px solid #ef4444}.wiki{line-height:1.7;color:#94a3b8}.wiki h1{font-size:1.5rem;font-weight:600;margin:2rem 0 1rem;color:#f8fafc}.wiki h2,.method-audit-details h2,.method-footer h2{font-size:1.25rem;font-weight:600;margin:1.5rem 0 .75rem;border-bottom:1px solid #334155;padding-bottom:.5rem;color:#f8fafc}.wiki h3{font-size:1.1rem;font-weight:500;margin:1rem 0 .5rem;color:#f8fafc}.wiki p{margin:0 0 1rem}.wiki blockquote{border-left:3px solid #6366f1;padding-left:1rem;font-style:italic;color:#94a3b8;margin:1rem 0}.math{font-family:"Times New Roman",serif;color:#cbd5e1}.claim{border-bottom:1px solid rgba(59,130,246,.55);color:#cbd5e1}.trust-debated{border-bottom-color:#f59e0b}.trust-unverified{border-bottom-color:#64748b}.trust-reported{border-bottom-color:#a78bfa}.cid,.cite-badge{font-size:.68em;color:#818cf8;margin-left:2px}.cite-badge{vertical-align:super}.method-audit-details,.method-footer{margin-top:2rem;border-top:1px solid #334155;padding-top:1rem;color:#94a3b8}.method-audit-details summary{cursor:pointer;color:#f8fafc;font-weight:750;font-size:.9rem;margin-bottom:.75rem}.panel{margin:1rem 0;padding:1rem;border:1px solid rgba(51,65,85,.9);border-radius:10px;background:rgba(15,23,42,.62)}.reject{border-left:3px solid #ef4444}.safety{border-left:3px solid #22c55e}.muted{color:#94a3b8}.badge{display:inline-block;border-radius:999px;padding:.1rem .45rem;font-size:.68rem;font-weight:700;border:1px solid #334155}.b-debated{color:#fbbf24}.b-unverified{color:#94a3b8}.b-reported{color:#c4b5fd}table{width:100%;border-collapse:collapse;margin:.75rem 0;font-size:.82rem}th,td{border:1px solid #334155;padding:.45rem;text-align:left;vertical-align:top}th{color:#f8fafc;background:rgba(30,41,59,.8)}code{background:#334155;padding:2px 6px;border-radius:4px;font-size:.875rem}.toc{position:sticky;top:1rem;border:1px solid #334155;border-radius:10px;background:#111827;padding:1rem}.toc h3{margin:0 0 .75rem;font-size:.78rem;text-transform:uppercase;letter-spacing:.08em;color:#94a3b8}.toc a{display:block;color:#94a3b8;font-size:.78rem;line-height:1.35;margin:.45rem 0}.toc a:hover{color:#f8fafc}.strike{text-decoration:line-through;text-decoration-color:#ef4444}@media(max-width:900px){.wiki-shell{display:block}.small-link.first{margin-left:0}.toc{position:static;margin-top:1.5rem}.method-card{padding:.85rem}.wiki-topbar{gap:.4rem}}
""".strip()

CLAIM_RE = re.compile(r"<!--\s*claim:([\d,\s]+)\s*-->(.*?)<!--\s*/claim:\1\s*-->", re.S)
CITE_RE = re.compile(r"<!--\s*cite:([\d,\s]+)\s*-->")
MATH_RE = re.compile(r"\$(.+?)\$")


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def inline_basic(text: str) -> str:
    parts = []
    pos = 0
    for m in MATH_RE.finditer(text):
        parts.append(esc(text[pos:m.start()]))
        parts.append(f'<span class="math">{esc(m.group(1))}</span>')
        pos = m.end()
    parts.append(esc(text[pos:]))
    return "".join(parts)


def claim_class(ids: str) -> tuple[str, str]:
    first = ids.split(",")[0].strip()
    trust = TRUST_BY_CLAIM.get(first, "accepted")
    return f"claim trust-{trust}", trust


def convert_inline(text: str) -> str:
    tokens: Dict[str, str] = {}

    def claim_repl(m: re.Match[str]) -> str:
        ids = ",".join(part.strip() for part in m.group(1).split(",") if part.strip())
        body = m.group(2)
        cls, trust = claim_class(ids)
        first = ids.split(",")[0]
        label = f"claim {ids}"
        if trust not in {"accepted", "baseline"}:
            label += f" · {trust}"
        html_value = (
            f'<span class="{cls}" data-claim-id="{esc(ids)}" id="claim-{esc(first)}">'
            f'{inline_basic(body)}<sup class="cid">{esc(label)}</sup></span>'
        )
        token = f"@@TOKEN{len(tokens)}@@"
        tokens[token] = html_value
        return token

    def cite_repl(m: re.Match[str]) -> str:
        ids = [part.strip() for part in m.group(1).split(",") if part.strip()]
        badges = "".join(f'<span class="cite-badge">📄</span>' for _ in ids)
        html_value = f'<span class="cite-badges" data-cite-ids="{esc(",".join(ids))}">{badges}</span>'
        token = f"@@TOKEN{len(tokens)}@@"
        tokens[token] = html_value
        return token

    text = CLAIM_RE.sub(claim_repl, text)
    text = CITE_RE.sub(cite_repl, text)
    out = inline_basic(text)
    for token, value in tokens.items():
        out = out.replace(esc(token), value)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    return out


def slugify(text: str) -> str:
    return re.sub(r"(^-|-$)", "", re.sub(r"[^a-z0-9]+", "-", text.lower()))


def render_markdown(md: str) -> tuple[str, list[str]]:
    html_parts: list[str] = []
    headings: list[str] = []
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if para:
            joined = " ".join(line.strip() for line in para).strip()
            html_parts.append(f"<p>{convert_inline(joined)}</p>")
            para = []

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            continue
        if line.startswith("# "):
            flush_para()
            title = line[2:].strip()
            html_parts.append(f'<h1 id="{slugify(title)}">{esc(title)}</h1>')
            continue
        if line.startswith("## "):
            flush_para()
            title = line[3:].strip()
            headings.append(title)
            html_parts.append(f'<h2 id="{slugify(title)}">{esc(title)}</h2>')
            continue
        if line.startswith("### "):
            flush_para()
            title = line[4:].strip()
            html_parts.append(f'<h3 id="{slugify(title)}">{esc(title)}</h3>')
            continue
        if line.startswith(">"):
            flush_para()
            quote = line.lstrip("> ").strip()
            html_parts.append(f"<blockquote><p>{convert_inline(quote)}</p></blockquote>")
            continue
        para.append(line)
    flush_para()
    return "\n".join(html_parts), headings


def extract_below_article(existing_html: str, spec: MethodSpec) -> str:
    if spec.after_mode == "footer_note":
        return (
            '<footer class="method-footer">\n'
            '  <h2>Method &amp; safety state</h2>\n'
            '  <p>Method 3 · debate-map-to-wiki rebuild · Galaxy Evolution · P2 same-format narrative draft. Source of record: '
            '<code>m3-p2-same-format-draft-20260707T050500Z.md</code>. Provenance and format-conformance record: '
            '<code>LANA_M3_P2_WIKI_PAGE_AUTHOR_20260707T050500Z.md</code>.</p>\n'
            '  <p><code>NO ACTIVE EXECUTION PHRASE</code> — static method-local evaluation artifact only. No live-wiki publish, no DB/page_versions, no trust recompute, no deploy, no git.</p>\n'
            '</footer>'
        )
    if "</article>" not in existing_html:
        return ""
    after = existing_html.split("</article>", 1)[1]
    if '<aside class="toc"' in after:
        after = after.split('<aside class="toc"', 1)[0]
    after = re.sub(r"\s*</div>\s*$", "", after, flags=re.S).strip()
    if not after:
        return ""
    return (
        '<details class="method-audit-details">\n'
        '  <summary>Method provenance and safety notes</summary>\n'
        f'{after}\n'
        '</details>'
    )


def render_toc(headings: Iterable[str]) -> str:
    links = "\n".join(f'<a href="#{slugify(h)}">{esc(h)}</a>' for h in headings)
    return f'<aside class="toc" aria-label="Table of contents"><h3>On this page</h3>{links}</aside>'


def attrs_html(attrs: Dict[str, str]) -> str:
    merged = dict(attrs)
    merged["data-wiki-format"] = "normal-nebulamind-tabs"
    merged["data-method-card-retained"] = "true"
    merged["data-no-top-dashboard-clutter"] = "true"
    merged["data-normal-tabs-marker"] = MARKER
    return " ".join(f'{k}="{html.escape(v, quote=True)}"' for k, v in merged.items())


def render_method_card(spec: MethodSpec) -> str:
    badges = "\n".join(f'<span class="pill">{esc(b)}</span>' for b in spec.badges)
    return f"""
<section class="method-card" aria-label="Method identifier">
  <p class="eyebrow">{esc(spec.eyebrow)}</p>
  <h2>Galaxy Evolution — {esc(spec.title)}</h2>
  <p class="lead">{esc(spec.lead)}</p>
  <div class="status-row"><span class="status">{esc(spec.verdict)}</span>{badges}</div>
  <p class="source-note">{esc(spec.source_note)}</p>
</section>
""".strip()


def render_normal_wiki_controls() -> str:
    return """
    <div class="wiki-topbar" aria-label="NebulaMind wiki header controls">
      <span class="health">🔵 74.6/100</span>
      <a class="small-link first" href="/wiki/galaxy-evolution/history">📜 History</a>
      <a class="small-link" href="/wiki/galaxy-evolution/sources">📚 Sources</a>
    </div>
    <div class="wiki-controls" aria-label="NebulaMind wiki view controls">
      <span class="tab active">Raw Text</span>
      <span class="tab">Colors On</span>
      <span class="tab citations">Hide Citations</span>
      <span class="tab">Show Ideas</span>
      <p class="tool-note">Each sentence is sourced from a published paper. Click the citation icon to see sources.</p>
    </div>
    <div class="legend" aria-label="Trust legend"><span class="consensus">Consensus</span><span class="accepted">Accepted</span><span class="debated">Debated</span><span class="challenged">Challenged</span></div>
""".rstrip()


def render_page(spec: MethodSpec, article_html: str, headings: list[str], below_article: str) -> str:
    head_list = set(headings)
    missing = [h for h in H2_SKELETON if h not in head_list]
    if missing:
        raise SystemExit(f"{spec.slug}: missing NebulaMind H2 skeleton entries: {missing}")
    extra = [h for h in headings if h not in H2_SKELETON]
    if extra:
        raise SystemExit(f"{spec.slug}: unexpected H2 entries: {extra}")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Galaxy Evolution — Method {esc(spec.num)} {esc(spec.title)} · NebulaMind wiki-format artifact</title>
<style>{CSS}</style>
</head>
<body {attrs_html(spec.body_attrs)}>
<main>
{render_method_card(spec)}
<div class="wiki-shell">
  <div class="wiki-main">
{render_normal_wiki_controls()}
    <article class="wiki" data-nebulamind-wiki-article="galaxy-evolution" data-markdown-source="{esc(spec.draft)}">
{article_html}
    </article>
{below_article}
  </div>
  {render_toc(headings)}
</div>
</main>
</body>
</html>
"""


def main() -> None:
    RECEIPT.mkdir(parents=True, exist_ok=True)
    backup_dir = RECEIPT / "working-backup-before-normal-tabs-render"
    backup_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    for spec in SPECS:
        mdir = ROOT / spec.slug
        html_path = mdir / "wiki-page.html"
        md_path = mdir / spec.draft
        if not html_path.exists():
            raise SystemExit(f"missing existing html: {html_path}")
        if not md_path.exists():
            raise SystemExit(f"missing markdown source: {md_path}")
        original = html_path.read_text(encoding="utf-8")
        shutil.copy2(html_path, backup_dir / f"{spec.slug}__wiki-page.html")
        article_html, headings = render_markdown(md_path.read_text(encoding="utf-8"))
        below_article = extract_below_article(original, spec)
        page = render_page(spec, article_html, headings, below_article)
        html_path.write_text(page, encoding="utf-8")
        top_before_article = page.split('<article class="wiki"', 1)[0]
        outputs.append({
            "slug": spec.slug,
            "path": str(html_path),
            "bytes": len(page.encode("utf-8")),
            "h2_count": len(headings),
            "claim_count": page.count('data-claim-id="'),
            "cite_count": page.count('data-cite-ids="'),
            "marker": MARKER,
            "method_card_before_article": page.find('class="method-card"') < page.find('<article class="wiki"'),
            "normal_tabs_present": all(t in page for t in ["Raw Text", "Colors On", "Hide Citations", "Show Ideas"]),
            "top_clutter_absent": all(t not in top_before_article for t in ["Three paper-to-wiki result lanes", "Paper-to-claim flight deck", "Workspace", "Same-format draft", "Quintet", "snapshot", "Snapshot", "deck", "Deck", "atlas", "Atlas"]),
        })
    receipt_md = RECEIPT / "RENDER_RECEIPT.md"
    receipt_json = RECEIPT / "RENDER_RECEIPT.json"
    receipt_json.write_text(json.dumps({"marker": MARKER, "rendered_utc": datetime.now(timezone.utc).isoformat(), "outputs": outputs}, indent=2), encoding="utf-8")
    lines = [
        "# Method wiki normal-tabs render receipt",
        "",
        f"- marker: `{MARKER}`",
        f"- rendered_utc: `{datetime.now(timezone.utc).isoformat()}`",
        "- scope: static method `wiki-page.html` artifacts only",
        "- removed from above article: method-link card grid, paper-to-claim flight deck, snapshot/deck/atlas dashboard furniture",
        "- retained above article: one compact method identifier card plus normal NebulaMind wiki tabs/controls",
        "- product DB/page_versions writes: 0",
        "- live wiki publish: 0",
        "- backend/API restart: 0",
        "- trust recompute: 0",
        "- deploy: 0",
        "- git commit/push/merge: 0",
        "- active execution phrase: `NO ACTIVE EXECUTION PHRASE`",
        "",
        "## Outputs",
    ]
    for item in outputs:
        lines.append(
            f"- `{item['slug']}`: {item['bytes']} B, {item['h2_count']} H2, "
            f"{item['claim_count']} claim spans, {item['cite_count']} cite spans, "
            f"method card before article = {item['method_card_before_article']}, "
            f"normal tabs present = {item['normal_tabs_present']}, "
            f"top clutter absent = {item['top_clutter_absent']}"
        )
    lines.append("")
    lines.append(f"Working backups: `{backup_dir}`")
    receipt_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    for item in outputs:
        print(f"{item['slug']} bytes={item['bytes']} h2={item['h2_count']} claims={item['claim_count']} cites={item['cite_count']} tabs={item['normal_tabs_present']} top_clutter_absent={item['top_clutter_absent']}")
    print(f"receipt={receipt_md}")

if __name__ == "__main__":
    main()
