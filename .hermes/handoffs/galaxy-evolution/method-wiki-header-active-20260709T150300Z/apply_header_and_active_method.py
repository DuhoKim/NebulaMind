#!/usr/bin/env python3
"""Restore NebulaMind top header and current-method focus on static method pages.

User intent:
- the top main NebulaMind header should not disappear on method wiki pages;
- the method result selector and wiki tabs remain;
- on a method-specific wiki page, that method's selector box is visually focused/current;
- only the wiki article/content differs per method.

Scope: static method `wiki-page.html` artifacts only. No product DB/page_versions,
trust recompute, backend/API runtime, deploy, git, cron, billing, or external submission.
"""
from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
ROOT = REPO / "frontend/public/agent-reports/wiki-method-results/galaxy-evolution"
RECEIPT_DIR = REPO / ".hermes/handoffs/galaxy-evolution/method-wiki-header-active-20260709T150300Z"
MARKER = "NEBULAMIND_METHOD_WIKI_HEADER_ACTIVE_SELECTOR_20260709T150300Z"
PREVIOUS_SELECTOR_MARKER = "NEBULAMIND_METHOD_WIKI_SELECTOR_TABS_STATIC_SHELL_20260709T145415Z"

@dataclass(frozen=True)
class MethodLink:
    slug: str
    label: str
    description: str

METHODS = [
    MethodLink(
        slug="packet-gated-paper-to-wiki-reconciliation",
        label="1 · Packet-gated reconciliation",
        description="Open the assembled wiki page from the packet-gated method.",
    ),
    MethodLink(
        slug="source-first-paper-adjudication",
        label="2 · Source-first adjudication",
        description="Open the assembled wiki page from the source-first method.",
    ),
    MethodLink(
        slug="debate-map-to-wiki-rebuild",
        label="3 · Debate-map rebuild",
        description="Open the assembled wiki page from the debate-map rebuild method.",
    ),
]

HEADER_HTML = """<header class="site-header" role="banner" data-testid="nebulamind-main-header">
  <div class="site-header-inner">
    <a class="brand" href="/">NebulaMind</a>
    <nav class="site-nav" aria-label="Main navigation">
      <a href="/wiki">Wiki</a>
      <a href="/surveys">Surveys</a>
      <a href="/ideas">Research Topics</a>
      <a href="/news">News</a>
      <a href="/council">Council</a>
      <a href="/agents">Agents</a>
      <a href="/explore/chat">More</a>
      <a class="join-link" href="/join">Join</a>
    </nav>
  </div>
</header>"""

HEADER_CSS = """.site-header{position:sticky;top:0;z-index:40;border-bottom:1px solid #334155;background:#0f172a}.site-header-inner{max-width:1024px;margin:0 auto;padding:1rem 1.5rem;display:flex;align-items:center;justify-content:space-between;gap:1.5rem}.brand{color:#f8fafc;text-decoration:none;font-weight:600;font-size:1.1rem;letter-spacing:-.025em}.brand:hover{text-decoration:none}.site-nav{display:flex;gap:1.5rem;align-items:center;font-size:.875rem}.site-nav a{color:#94a3b8;text-decoration:none;white-space:nowrap}.site-nav a:hover{color:#f8fafc;text-decoration:none}.site-nav .join-link{padding:6px 14px;background:#6366f1;color:#f8fafc;border-radius:4px;font-weight:600;font-size:.85rem}.site-nav .join-link:hover{background:#4f46e5;color:#f8fafc}@media(max-width:900px){.site-header-inner{align-items:flex-start;display:block}.brand{display:inline-block;margin-bottom:.6rem}.site-nav{display:flex;flex-wrap:wrap;gap:.7rem 1rem}.site-nav a{font-size:.82rem}.site-nav .join-link{padding:4px 10px}}"""

ACTIVE_SELECTOR_CSS = """.selector-links a.is-current{border-color:rgba(129,140,248,.95);background:linear-gradient(135deg,rgba(79,70,229,.34),rgba(30,41,59,.92));box-shadow:0 0 0 2px rgba(129,140,248,.2),0 14px 30px rgba(79,70,229,.18);outline:2px solid rgba(199,210,254,.55);outline-offset:2px}.selector-links a.is-current span{color:#fff}.selector-links a.is-current small{color:#dbeafe}.current-badge{display:inline-flex;margin-top:.45rem;border-radius:999px;border:1px solid rgba(199,210,254,.55);background:rgba(99,102,241,.22);color:#e0e7ff;padding:.12rem .45rem;font-size:.64rem;font-weight:800;letter-spacing:.02em;text-transform:uppercase}"""

HEADER_RE = re.compile(r'<header class="site-header"[\s\S]*?</header>\s*')
SELECTOR_RE = re.compile(r'<section class="method-selector" aria-label="Galaxy Evolution method result selector" data-testid="galaxy-method-result-selector">[\s\S]*?</section>')


def build_selector(current_slug: str) -> str:
    items = []
    for item in METHODS:
        href = f"/agent-reports/wiki-method-results/galaxy-evolution/{item.slug}/wiki-page.html"
        current = item.slug == current_slug
        attrs = [
            'data-testid="galaxy-method-result-link"',
            f'href="{href}"',
        ]
        if current:
            attrs.extend([
                'class="is-current"',
                'aria-current="page"',
                'data-current-method="true"',
            ])
        badge = '<strong class="current-badge">Current method</strong>' if current else ""
        items.append(
            f"    <a {' '.join(attrs)}><span>{item.label}</span><small>{item.description}</small>{badge}</a>"
        )
    return """<section class="method-selector" aria-label="Galaxy Evolution method result selector" data-testid="galaxy-method-result-selector">
  <div class="selector-head">
    <div>
      <p class="selector-eyebrow">Method result selector</p>
      <h2>Choose one of the three Galaxy Evolution wiki methods</h2>
    </div>
    <span class="selector-count">3 pages</span>
  </div>
  <div class="selector-links">
%s
  </div>
</section>""" % "\n".join(items)


def ensure_css(text: str, css: str, marker: str) -> str:
    if marker in text:
        return text
    return text.replace("</style>", css + f"\n/* {marker} */\n</style>", 1)


def transform(slug: str, text: str) -> str:
    if '<main>' not in text:
        raise RuntimeError("missing <main>")
    out = HEADER_RE.sub("", text)
    out = out.replace("<main>", HEADER_HTML + "\n<main>", 1)
    out, selector_count = SELECTOR_RE.subn(build_selector(slug), out, count=1)
    if selector_count != 1:
        raise RuntimeError(f"expected exactly one selector section, saw {selector_count}")
    out = ensure_css(out, HEADER_CSS, "NEBULAMIND_METHOD_STATIC_HEADER_CSS")
    out = ensure_css(out, ACTIVE_SELECTOR_CSS, "NEBULAMIND_METHOD_ACTIVE_SELECTOR_CSS")
    if MARKER not in out:
        out = out.replace(
            "data-method-result-selector-retained=\"true\"",
            f"data-method-result-selector-retained=\"true\" data-main-header-retained=\"true\" data-current-method-highlighted=\"true\" data-header-active-marker=\"{MARKER}\"",
            1,
        )
    return out


def inspect_page(slug: str, text: str) -> dict:
    top = text.split('<article class="wiki"', 1)[0]
    current_href = f"/agent-reports/wiki-method-results/galaxy-evolution/{slug}/wiki-page.html"
    current_anchor_pattern = re.compile(
        r'<a(?=[^>]*data-testid="galaxy-method-result-link")(?=[^>]*href="' + re.escape(current_href) + r'")(?=[^>]*aria-current="page")(?=[^>]*data-current-method="true")',
        re.S,
    )
    non_current_bad = re.findall(
        r'<a(?=[^>]*data-testid="galaxy-method-result-link")(?=[^>]*aria-current="page")',
        text,
        re.S,
    )
    return {
        "slug": slug,
        "bytes": len(text.encode("utf-8")),
        "marker": MARKER in text,
        "previous_selector_marker": PREVIOUS_SELECTOR_MARKER in text,
        "main_header_present": 'data-testid="nebulamind-main-header"' in text,
        "brand_present": ">NebulaMind</a>" in text,
        "main_nav_links_present": all(term in text for term in ["/wiki", "/surveys", "Research Topics", "/news", "/council", "/agents", "/join"]),
        "selector_present": 'data-testid="galaxy-method-result-selector"' in text,
        "selector_link_count": text.count('data-testid="galaxy-method-result-link"'),
        "current_anchor_present": bool(current_anchor_pattern.search(text)),
        "only_one_current_anchor": len(non_current_bad) == 1,
        "current_badge_present": text.count("Current method") == 1,
        "current_before_tabs": text.find('data-current-method="true"') < text.find("Raw Text"),
        "tabs_present": all(term in text for term in ["Raw Text", "Colors On", "Hide Citations", "Show Ideas"]),
        "article_present": '<article class="wiki"' in text,
        "article_h1": '<h1 id="galaxy-evolution">Galaxy Evolution</h1>' in text,
        "top_clutter_absent": all(term not in top for term in [
            "Page trust snapshot",
            "Paper-to-claim flight deck",
            "Page-level contradiction atlas",
            "Snapshot",
            "snapshot",
            "deck",
            "Deck",
            "atlas",
            "Atlas",
            "Workspace",
            "Same-format draft",
            "Quintet",
        ]),
        "no_scripts": "<script" not in text.lower(),
        "no_forms": "<form" not in text.lower(),
        "no_active_execution_phrase": "NO ACTIVE EXECUTION PHRASE" in text,
        "approve_execute_absent": "APPROVE EXECUTE" not in text,
        "approve_apply_absent": "APPROVE APPLY" not in text,
    }


def main() -> None:
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    backup_dir = RECEIPT_DIR / "working-backup-before-header-active"
    backup_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for item in METHODS:
        path = ROOT / item.slug / "wiki-page.html"
        if not path.exists():
            raise SystemExit(f"missing {path}")
        original = path.read_text(encoding="utf-8")
        shutil.copy2(path, backup_dir / f"{item.slug}__wiki-page.html")
        updated = transform(item.slug, original)
        row = inspect_page(item.slug, updated)
        required = [
            "marker",
            "previous_selector_marker",
            "main_header_present",
            "brand_present",
            "main_nav_links_present",
            "selector_present",
            "current_anchor_present",
            "only_one_current_anchor",
            "current_badge_present",
            "current_before_tabs",
            "tabs_present",
            "article_present",
            "article_h1",
            "top_clutter_absent",
            "no_scripts",
            "no_forms",
            "no_active_execution_phrase",
            "approve_execute_absent",
            "approve_apply_absent",
        ]
        failures = [key for key in required if not row[key]]
        if row["selector_link_count"] != 3:
            failures.append("selector_link_count != 3")
        if failures:
            raise SystemExit(f"{item.slug}: validation failed: {failures}")
        path.write_text(updated, encoding="utf-8")
        rows.append(row)
    receipt = {
        "marker": MARKER,
        "updated_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "static method wiki-page.html artifacts only",
        "backup_dir": str(backup_dir),
        "rows": rows,
        "safety": {
            "db_page_versions_writes": 0,
            "live_product_wiki_publish": 0,
            "backend_api_restart": 0,
            "trust_recompute": 0,
            "deploy": 0,
            "git_commit_push_merge": 0,
        },
    }
    (RECEIPT_DIR / "HEADER_ACTIVE_RENDER_RECEIPT.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    lines = [
        "# Static method wiki header + active selector render receipt",
        "",
        f"- marker: `{MARKER}`",
        f"- updated_utc: `{receipt['updated_utc']}`",
        "- result: restored top NebulaMind main header on static method pages and highlighted the current method card in the selector.",
        "- selector and wiki tabs remain; only article/content varies per method.",
        "- scope: static method `wiki-page.html` artifacts only.",
        "- safety: DB/page_versions/live product wiki publish/backend restart/trust recompute/deploy/git all 0.",
        "",
        "## Outputs",
    ]
    for row in rows:
        lines.append(
            f"- `{row['slug']}`: header={row['main_header_present']}, selector_links={row['selector_link_count']}, "
            f"current_anchor={row['current_anchor_present']}, tabs={row['tabs_present']}, top_clutter_absent={row['top_clutter_absent']}"
        )
    lines.append("")
    lines.append(f"Working backups: `{backup_dir}`")
    (RECEIPT_DIR / "HEADER_ACTIVE_RENDER_RECEIPT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))

if __name__ == "__main__":
    main()
