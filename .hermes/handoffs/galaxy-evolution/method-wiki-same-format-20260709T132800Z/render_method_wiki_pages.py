#!/usr/bin/env python3
"""Render Galaxy Evolution method wiki pages in NebulaMind wiki format.

Scope: static method artifacts only. This does not touch DB/page_versions, trust,
backend/runtime, deploy, or git.
"""
from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
ROOT = REPO / "frontend/public/agent-reports/wiki-method-results/galaxy-evolution"
RECEIPT = REPO / ".hermes/handoffs/galaxy-evolution/method-wiki-same-format-20260709T132800Z"
MARKER = "NEBULAMIND_METHOD_WIKI_SAME_FORMAT_CARD_RETAINED_20260709T132800Z"

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
    # Explicit Method 1 trust states from the existing page.
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
    marker: str
    source_note: str
    evidence_note: str
    links: List[tuple[str, str, str]]
    body_attrs: Dict[str, str]
    after_mode: str = "keep_after_article"

SPECS = [
    MethodSpec(
        slug="packet-gated-paper-to-wiki-reconciliation",
        num="1",
        short="PGR",
        title="Packet-gated paper-to-wiki reconciliation",
        eyebrow="Method 1 · packet-gated paper-to-wiki reconciliation",
        lead=(
            "Independent Method 1 result rendered as a NebulaMind Galaxy Evolution wiki-format article. "
            "The method card remains on top; the wiki article below follows the current title, blockquote, "
            "section skeleton, sparse claim-chip, and no-hero-facts format."
        ),
        verdict="A5 verdict: PASS",
        badges=["static method artifact · not product wiki/page_versions", "30 provenance chips", "9 wiki sections", "0 inline citations", "zero NO-GO chips"],
        draft="pgr-same-format-draft-20260707T005045Z.md",
        marker="GALAXY_EVOLUTION_METHOD1_ULTRA_FORMAT_ROLE_SPLIT_20260707",
        source_note="Rendered deterministically from pgr-same-format-draft-20260707T005045Z.md; trust/evidence audit cards are preserved below the article.",
        evidence_note="Method 1 keeps existing provenance chips and watch-layer trust states while preserving the NebulaMind wiki article skeleton.",
        links=[
            ("Workspace", "index.html", "Directory overview and role table."),
            ("Same-format draft", "pgr-same-format-draft-20260707T005045Z.md", "Markdown source rendered below."),
            ("Quintet set", "quintet.html", "Hwao, Lana, Goru, Kun, Tori roles."),
        ],
        body_attrs={
            "data-marker": "GALAXY_EVOLUTION_METHOD1_ULTRA_FORMAT_ROLE_SPLIT_20260707",
            "data-verdict": "HWAO_PGR_METHOD_VERDICT_20260707T040523Z",
            "data-method": "method1-packet-gated-paper-to-wiki-reconciliation",
            "data-safety": "NO_ACTIVE_EXECUTION_PHRASE",
            "data-product-published": "false",
        },
    ),
    MethodSpec(
        slug="source-first-paper-adjudication",
        num="2",
        short="SFA",
        title="Source-first paper adjudication",
        eyebrow="Method 2 · source-first paper adjudication",
        lead=(
            "Independent Method 2 result rendered as a NebulaMind Galaxy Evolution wiki-format article. "
            "The source-first method card remains on top, followed by the same wiki title, blockquote, "
            "section order, claim markers, citation markers, and reader-facing article structure used by NebulaMind."
        ),
        verdict="Hwao-m2 verdict: PASS",
        badges=["static method artifact · not product wiki/page_versions", "claims 2942–2947", "22 accepted/limited", "2 excluded", "12 rejected"],
        draft="galaxy-evolution-same-format-draft.md",
        marker="HWAO_M2_SAME_FORMAT_CONVERSION_V2_20260707T043503Z",
        source_note="Rendered from galaxy-evolution-same-format-draft.md; accepted, accepted-limited, excluded, and rejected source-position audit cards are preserved below the article.",
        evidence_note="Method 2 cites only accepted or accepted-limited source positions inside the article and keeps rejected rows outside support.",
        links=[
            ("Workspace", "index.html", "Directory overview and role table."),
            ("Same-format draft", "galaxy-evolution-same-format-draft.md", "Ratified Markdown source rendered below."),
            ("P1 source ledger", "p1-source-position-ledger.html", "36 rows · 24 accepted/limited · 12 rejected."),
            ("Quintet set", "quintet.html", "Hwao, Lana, Goru, Kun, Tori roles."),
        ],
        body_attrs={
            "data-marker": "HWAO_M2_SAME_FORMAT_CONVERSION_V2_20260707T043503Z",
            "data-method": "method2-source-first-paper-adjudication",
            "data-verdict": "PASS",
            "data-safety": "NO_ACTIVE_EXECUTION_PHRASE",
            "data-product-published": "false",
        },
    ),
    MethodSpec(
        slug="debate-map-to-wiki-rebuild",
        num="3",
        short="DMW",
        title="Debate-map-to-wiki rebuild",
        eyebrow="Method 3 · debate-map-to-wiki rebuild",
        lead=(
            "Independent Method 3 result rendered as a NebulaMind Galaxy Evolution wiki-format article. "
            "The original method/meta card is retained on top; the article below follows the current wiki title, "
            "opening claim-chip blockquote, H2 skeleton, and no-hero-facts contract."
        ),
        verdict="P2 same-format narrative draft",
        badges=["static method artifact · not product wiki/page_versions", "17 P1.5 sentence roles", "9 wiki sections", "claim/citation binding deferred to P3", "no hero_facts"],
        draft="m3-p2-same-format-draft-20260707T050500Z.md",
        marker="GALAXY_EVOLUTION_METHOD3_P15_PATCH_EXTENSION_20260707T005702Z",
        source_note="Rendered from m3-p2-same-format-draft-20260707T050500Z.md; P3 claim-chip and citation binding remain a separate gate.",
        evidence_note="Method 3 foregrounds the debate map as cautious prose; it deliberately does not promote unbound claim/citation chips into the article.",
        links=[
            ("Workspace", "index.html", "Directory overview and role table."),
            ("Same-format draft", "m3-p2-same-format-draft-20260707T050500Z.md", "P2 Markdown source rendered below."),
            ("P1 sentence plan", "p1-debate-map-sentence-plan.md", "Debate-map sentence plan source."),
            ("Quintet set", "quintet.html", "Hwao, Lana, Goru, Kun, Tori roles."),
        ],
        body_attrs={
            "data-marker": "GALAXY_EVOLUTION_METHOD3_P15_PATCH_EXTENSION_20260707T005702Z",
            "data-method": "method3-debate-map-to-wiki-rebuild",
            "data-verdict": "P2_SAME_FORMAT_NARRATIVE_DRAFT",
            "data-safety": "NO_ACTIVE_EXECUTION_PHRASE",
            "data-product-published": "false",
        },
        after_mode="footer_note",
    ),
]

CSS = r"""
:root{color-scheme:dark;--bg:#0f172a;--panel:#111827;--panel2:#1e293b;--fg:#f8fafc;--muted:#94a3b8;--dim:#64748b;--line:#334155;--accent:#6366f1;--sky:#38bdf8;--green:#22c55e;--amber:#f59e0b;--red:#ef4444;--purple:#a78bfa}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}a{color:#93c5fd;text-decoration:none}a:hover{text-decoration:underline}main{max-width:64rem;margin:0 auto;padding:28px 18px 72px}.method-card{margin:0 0 1rem;padding:1.1rem;border:1px solid rgba(129,140,248,.45);border-radius:14px;background:linear-gradient(135deg,rgba(15,23,42,.98),rgba(30,41,59,.86));box-shadow:0 16px 36px rgba(2,6,23,.28)}.method-card .eyebrow{margin:0 0 .35rem;color:#a5b4fc;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.12em}.method-card h2{margin:.1rem 0 .45rem;color:var(--fg);font-size:clamp(1.25rem,4vw,2rem);line-height:1.15;font-weight:700;border:0;padding:0}.lead{margin:0 0 .8rem;color:#cbd5e1;font-size:.9rem;line-height:1.58}.status-row{display:flex;flex-wrap:wrap;gap:.35rem;margin:.35rem 0 .85rem}.status,.pill{display:inline-block;border-radius:999px;padding:.18rem .55rem;font-size:.72rem;font-weight:700;border:1px solid rgba(148,163,184,.38);color:#cbd5e1;background:rgba(15,23,42,.72)}.status{border-color:rgba(34,197,94,.48);color:#86efac;background:rgba(34,197,94,.10)}.method-links{display:grid;grid-template-columns:repeat(auto-fit,minmax(12rem,1fr));gap:.55rem;margin-top:.8rem}.method-links a{display:block;padding:.68rem .78rem;border-radius:12px;border:1px solid rgba(148,163,184,.35);background:rgba(15,23,42,.86);color:var(--fg)}.method-links b{display:block;font-size:.82rem}.method-links span{display:block;margin-top:.22rem;color:var(--muted);font-size:.72rem;line-height:1.42}.source-note{margin:.75rem 0 0;color:var(--dim);font-size:.78rem}.wiki-shell{display:grid;grid-template-columns:minmax(0,56rem) 240px;gap:2rem;align-items:start}.wiki-main{min-width:0}.wiki-topbar{display:flex;align-items:center;gap:.5rem;margin:0 0 1.5rem;font-size:.875rem;flex-wrap:wrap}.health{font-size:.72rem;font-weight:600;padding:.15rem .5rem;border-radius:99px;background:rgba(59,130,246,.15);color:#3b82f6}.small-link{font-size:.75rem;color:var(--dim);padding:.25rem .5rem;border:1px solid var(--line);border-radius:4px}.small-link.first{margin-left:auto}.flight-deck{margin:0 0 1rem;padding:1rem;border:1px solid var(--line);border-radius:8px;background:rgba(30,41,59,.72)}.flight-deck h3{margin:0 0 .35rem;color:var(--fg);font-size:.85rem;text-transform:uppercase;letter-spacing:.08em}.flight-deck p{margin:.25rem 0;color:var(--muted);font-size:.82rem;line-height:1.5}.toolbar{display:flex;gap:.5rem;margin:0 0 1rem;align-items:center;flex-wrap:wrap}.tool-chip{font-size:.75rem;padding:.25rem .75rem;border-radius:4px;border:1px solid var(--line);color:var(--muted)}.tool-chip.active{border-color:var(--accent);background:var(--accent);color:#fff}.tool-note{font-size:.78rem;color:var(--dim);margin:0}.legend{display:flex;gap:.5rem;font-size:.75rem;color:var(--dim);margin:.25rem 0 1.1rem;flex-wrap:wrap}.legend span{padding-left:5px;border-left:2px solid var(--line)}.legend .consensus{border-color:var(--green)}.legend .accepted{border-color:#3b82f6}.legend .debated{border-color:var(--amber)}.legend .challenged{border-color:var(--red)}article.wiki{line-height:1.7;color:var(--muted)}article.wiki h1{font-size:1.5rem;font-weight:600;margin:2rem 0 1rem;color:var(--fg)}article.wiki h2{font-size:1.25rem;font-weight:600;margin:1.5rem 0 .75rem;border-bottom:1px solid var(--line);padding-bottom:.5rem;color:var(--fg)}article.wiki p{margin:0 0 1rem;color:var(--muted)}article.wiki blockquote{border-left:3px solid var(--accent);padding-left:1rem;margin:1rem 0;color:var(--muted);font-style:italic}.claim{border-radius:5px;padding:.05em .15em;box-shadow:inset 0 -2px 0 rgba(59,130,246,.45);background:rgba(59,130,246,.10);color:#cbd5e1}.claim .cid{font-size:.63rem;font-weight:800;margin-left:.24rem;padding:.04rem .26rem;border-radius:6px;white-space:nowrap;background:rgba(59,130,246,.22);color:#bfdbfe}.claim.trust-debated{background:rgba(245,158,11,.12);box-shadow:inset 0 -2px 0 rgba(245,158,11,.52)}.claim.trust-debated .cid{background:rgba(245,158,11,.24);color:#fde68a}.claim.trust-unverified{background:rgba(100,116,139,.18);box-shadow:inset 0 -2px 0 rgba(100,116,139,.55)}.claim.trust-unverified .cid{background:rgba(100,116,139,.32);color:#e2e8f0}.claim.trust-reported{background:rgba(56,189,248,.12);box-shadow:inset 0 -2px 0 rgba(56,189,248,.52)}.claim.trust-reported .cid{background:rgba(56,189,248,.24);color:#bae6fd}.cite-badges{white-space:normal}.cite-badge{display:inline-block;margin-left:.22rem;margin-bottom:.1rem;border-radius:999px;border:1px solid rgba(129,140,248,.45);padding:.05rem .36rem;color:#c4b5fd;background:rgba(129,140,248,.12);font-size:.72rem;font-weight:700}.math{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono",monospace;color:#a7f3d0}.toc{position:sticky;top:1rem;border-left:1px solid var(--line);padding-left:1rem;color:var(--dim);font-size:.78rem}.toc h3{margin:0 0 .55rem;color:var(--fg);font-size:.72rem;text-transform:uppercase;letter-spacing:.08em}.toc a{display:block;color:var(--dim);margin:.35rem 0;line-height:1.35}.audit-section,section.panel,section.card,footer.method-footer{margin-top:2rem;border:1px solid var(--line);border-radius:8px;background:rgba(30,41,59,.74);padding:1rem;color:var(--muted)}section.panel h2,section.card h2,footer.method-footer h2{margin:0 0 .55rem;color:var(--fg);font-size:1.05rem;border:0;padding:0}.panel.reject,.card.reject{border-color:rgba(239,68,68,.42);background:rgba(127,29,29,.18)}.panel.safety,.card.safety{border-color:rgba(34,197,94,.38);background:rgba(20,83,45,.18)}table{width:100%;border-collapse:collapse;margin-top:.7rem;font-size:.82rem}th,td{border-bottom:1px solid var(--line);padding:.48rem .55rem;text-align:left;vertical-align:top}th{color:#93c5fd;text-transform:uppercase;letter-spacing:.04em;font-size:.72rem}code{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono",monospace;color:#a7f3d0}.muted{color:var(--muted);font-size:.82rem}.badge{display:inline-block;padding:.12rem .45rem;border-radius:999px;font-size:.68rem;font-weight:800}.b-debated{background:rgba(245,158,11,.24);color:#fde68a}.b-unverified{background:rgba(100,116,139,.28);color:#e2e8f0}.b-reported{background:rgba(56,189,248,.24);color:#bae6fd}.b-baseline{background:rgba(59,130,246,.18);color:#bfdbfe}.b-nogo{background:rgba(239,68,68,.24);color:#fecaca}@media(max-width:860px){.wiki-shell{display:block}.toc{position:static;margin-top:1.5rem;border-left:0;border-top:1px solid var(--line);padding:1rem 0 0}.small-link.first{margin-left:0}main{padding-top:18px}}
""".strip()

CLAIM_RE = re.compile(r"<!--\s*claim:([\d,\s]+)\s*-->(.*?)<!--\s*/claim:\1\s*-->", re.S)
CITE_RE = re.compile(r"<!--\s*cite:([\d,\s]+)\s*-->")
MATH_RE = re.compile(r"\$(.+?)\$")


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def inline_basic(text: str) -> str:
    """Escape text and render only simple math spans."""
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
        badges = "".join(f'<span class="cite-badge">📄 e:{esc(i)}</span>' for i in ids)
        html_value = f'<span class="cite-badges" data-cite-ids="{esc(",".join(ids))}">{badges}</span>'
        token = f"@@TOKEN{len(tokens)}@@"
        tokens[token] = html_value
        return token

    text = CLAIM_RE.sub(claim_repl, text)
    text = CITE_RE.sub(cite_repl, text)
    out = inline_basic(text)
    for token, value in tokens.items():
        out = out.replace(esc(token), value)
    # Small markdown leftovers used in source notes.
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
        if line.startswith(">"):
            flush_para()
            quote = line.lstrip("> ").strip()
            html_parts.append(f"<blockquote><p>{convert_inline(quote)}</p></blockquote>")
            continue
        para.append(line)
    flush_para()
    return "\n".join(html_parts), headings


def extract_after_article(existing_html: str, spec: MethodSpec) -> str:
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
    after = re.sub(r"</main>\s*</body>\s*</html>\s*$", "", after, flags=re.S | re.I).strip()
    # Drop stale body/main closers if present.
    after = re.sub(r"</body>\s*</html>\s*$", "", after, flags=re.S | re.I).strip()
    # Retain audit cards below the article; they are method evidence/safety cards, not the top method card.
    return after


def render_toc(headings: Iterable[str]) -> str:
    links = "\n".join(f'<a href="#{slugify(h)}">{esc(h)}</a>' for h in headings)
    return f'<aside class="toc" aria-label="Table of contents"><h3>On this page</h3>{links}</aside>'


def attrs_html(attrs: Dict[str, str]) -> str:
    merged = dict(attrs)
    merged["data-wiki-format"] = "nebulamind-v1709-same-format"
    merged["data-method-card-retained"] = "true"
    merged["data-same-format-marker"] = MARKER
    return " ".join(f'{k}="{html.escape(v, quote=True)}"' for k, v in merged.items())


def render_method_card(spec: MethodSpec) -> str:
    badges = "\n".join(f'<span class="pill">{esc(b)}</span>' for b in spec.badges)
    links = []
    for label, href, note in spec.links:
        links.append(
            f'<a href="/agent-reports/wiki-method-results/galaxy-evolution/{spec.slug}/{html.escape(href, quote=True)}">'
            f'<b>{esc(label)}</b><span>{esc(note)}</span></a>'
        )
    return f"""
<section class="method-card" aria-label="Method card">
  <p class="eyebrow">{esc(spec.eyebrow)}</p>
  <h2>Galaxy Evolution — {esc(spec.title)}</h2>
  <p class="lead">{esc(spec.lead)}</p>
  <div class="status-row"><span class="status">{esc(spec.verdict)}</span>{badges}</div>
  <div class="method-links">{''.join(links)}</div>
  <p class="source-note">{esc(spec.source_note)}</p>
</section>
""".strip()


def render_page(spec: MethodSpec, article_html: str, headings: list[str], after_article: str) -> str:
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
    <div class="wiki-topbar" aria-label="NebulaMind wiki controls">
      <span class="health">🔵 74.6/100</span>
      <a class="small-link first" href="/wiki/galaxy-evolution/history">📜 History</a>
      <a class="small-link" href="/wiki/galaxy-evolution/sources">📚 Sources</a>
    </div>
    <section class="flight-deck" aria-label="Paper-to-claim flight deck">
      <h3>Paper-to-claim flight deck</h3>
      <p><strong>Which papers drive visible claims</strong></p>
      <p>{esc(spec.evidence_note)}</p>
      <p>Static method artifact only. Claim-scoped paper links remain compatible with the NebulaMind source/history surfaces and are not a product-wiki publish.</p>
    </section>
    <div class="toolbar" aria-label="NebulaMind wiki view controls">
      <span class="tool-chip active">Reader view</span>
      <span class="tool-chip">Evidence view compatible</span>
      <span class="tool-chip">Show highlights compatible</span>
      <span class="tool-chip">Citation chips compatible</span>
      <p class="tool-note">Highlighted claims are linked to method evidence where the method has bound them.</p>
    </div>
    <div class="legend" aria-label="Trust legend"><span class="consensus">Consensus</span><span class="accepted">Accepted</span><span class="debated">Debated</span><span class="challenged">Challenged</span></div>
    <article class="wiki" data-nebulamind-wiki-article="galaxy-evolution" data-markdown-source="{esc(spec.draft)}">
{article_html}
    </article>
{after_article}
  </div>
  {render_toc(headings)}
</div>
</main>
</body>
</html>
"""


def main() -> None:
    RECEIPT.mkdir(parents=True, exist_ok=True)
    backup_dir = RECEIPT / "working-backup-before-render"
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
        md = md_path.read_text(encoding="utf-8")
        article_html, headings = render_markdown(md)
        after_article = extract_after_article(original, spec)
        page = render_page(spec, article_html, headings, after_article)
        html_path.write_text(page, encoding="utf-8")
        outputs.append({
            "slug": spec.slug,
            "path": str(html_path),
            "bytes": len(page.encode("utf-8")),
            "h2_count": len(headings),
            "claim_count": page.count('data-claim-id="'),
            "cite_count": page.count('data-cite-ids="'),
            "method_card_retained": 'class="method-card"' in page and page.find('class="method-card"') < page.find('<article class="wiki"'),
            "marker": MARKER,
        })
    receipt = RECEIPT / "RENDER_RECEIPT.md"
    lines = [
        f"# Method wiki same-format render receipt",
        "",
        f"- marker: `{MARKER}`",
        f"- rendered_utc: `{datetime.now(timezone.utc).isoformat()}`",
        "- scope: static method `wiki-page.html` artifacts only",
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
        lines.append(f"- `{item['slug']}`: {item['bytes']} B, {item['h2_count']} H2, {item['claim_count']} claim spans, {item['cite_count']} cite spans, method card before article = {item['method_card_retained']}")
    lines.append("")
    lines.append(f"Working backups: `{backup_dir}`")
    receipt.write_text("\n".join(lines) + "\n", encoding="utf-8")
    for item in outputs:
        print(f"{item['slug']} bytes={item['bytes']} h2={item['h2_count']} claims={item['claim_count']} cites={item['cite_count']} card_before_article={item['method_card_retained']}")
    print(f"receipt={receipt}")

if __name__ == "__main__":
    main()
