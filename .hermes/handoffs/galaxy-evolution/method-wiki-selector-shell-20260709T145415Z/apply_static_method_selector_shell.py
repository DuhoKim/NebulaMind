#!/usr/bin/env python3
"""Make static Galaxy Evolution method wiki pages use a shared selector shell.

Intent from user correction:
- the method result selector remains at the top;
- the normal NebulaMind wiki tabs/controls remain;
- only the wiki article/content below changes per method;
- no snapshot/deck/atlas audit cards above the article.

Scope: static method `wiki-page.html` artifacts only. This does not touch product DB,
page_versions, trust recompute, backend/API runtime, deploy, git, cron, billing, or
external submission.
"""
from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
ROOT = REPO / "frontend/public/agent-reports/wiki-method-results/galaxy-evolution"
RECEIPT_DIR = REPO / ".hermes/handoffs/galaxy-evolution/method-wiki-selector-shell-20260709T145415Z"
MARKER = "NEBULAMIND_METHOD_WIKI_SELECTOR_TABS_STATIC_SHELL_20260709T145415Z"
SLUGS = [
    "packet-gated-paper-to-wiki-reconciliation",
    "source-first-paper-adjudication",
    "debate-map-to-wiki-rebuild",
]

SELECTOR_HTML = """<section class="method-selector" aria-label="Galaxy Evolution method result selector" data-testid="galaxy-method-result-selector">
  <div class="selector-head">
    <div>
      <p class="selector-eyebrow">Method result selector</p>
      <h2>Choose one of the three Galaxy Evolution wiki methods</h2>
    </div>
    <span class="selector-count">3 pages</span>
  </div>
  <div class="selector-links">
    <a data-testid="galaxy-method-result-link" href="/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html"><span>1 · Packet-gated reconciliation</span><small>Open the assembled wiki page from the packet-gated method.</small></a>
    <a data-testid="galaxy-method-result-link" href="/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html"><span>2 · Source-first adjudication</span><small>Open the assembled wiki page from the source-first method.</small></a>
    <a data-testid="galaxy-method-result-link" href="/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html"><span>3 · Debate-map rebuild</span><small>Open the assembled wiki page from the debate-map rebuild method.</small></a>
  </div>
</section>"""

SELECTOR_CSS = """.method-selector{margin:0 0 1rem;padding:.9rem;border:1px solid rgba(129,140,248,.45);border-radius:12px;background:linear-gradient(135deg,rgba(15,23,42,.96),rgba(30,41,59,.88));box-shadow:0 10px 24px rgba(2,6,23,.20)}.selector-head{display:flex;align-items:flex-start;justify-content:space-between;gap:.75rem;margin-bottom:.65rem}.selector-eyebrow{margin:0 0 .18rem;color:#a5b4fc;font-size:.66rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}.selector-head h2{margin:0;color:#f8fafc;font-size:1rem;line-height:1.25;font-weight:750;border:0;padding:0}.selector-count{flex-shrink:0;color:#c4b5fd;border:1px solid rgba(129,140,248,.45);border-radius:999px;padding:.16rem .48rem;font-size:.66rem;font-weight:800}.selector-links{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.55rem}.selector-links a{display:block;min-height:100%;border:1px solid rgba(148,163,184,.28);border-radius:10px;padding:.62rem .7rem;background:rgba(15,23,42,.72);color:#bfdbfe;text-decoration:none}.selector-links a:hover{border-color:rgba(147,197,253,.55);text-decoration:none}.selector-links span{display:block;color:#f8fafc;font-size:.78rem;font-weight:800;margin-bottom:.18rem}.selector-links small{display:block;color:#94a3b8;font-size:.7rem;line-height:1.38}@media(max-width:900px){.selector-head{display:block}.selector-count{display:inline-block;margin-top:.45rem}.selector-links{grid-template-columns:1fr}}"""

METHOD_CARD_RE = re.compile(r'<section class="method-card" aria-label="Method identifier">[\s\S]*?</section>\s*')


def transform(text: str) -> str:
    if SELECTOR_HTML in text:
        out = text
    else:
        out, count = METHOD_CARD_RE.subn(SELECTOR_HTML + "\n", text, count=1)
        if count != 1:
            raise RuntimeError("expected exactly one top method-card section")
    if ".method-selector{" not in out:
        out = out.replace("</style>", SELECTOR_CSS + "\n</style>", 1)
    if MARKER not in out:
        out = out.replace("data-no-top-dashboard-clutter=\"true\"", f"data-no-top-dashboard-clutter=\"true\" data-method-result-selector-retained=\"true\" data-static-shell-marker=\"{MARKER}\"", 1)
    # This field was accurate for the previous correction, but now the retained top
    # shell is the method selector rather than per-method identifier card.
    out = out.replace('data-method-card-retained="true" ', '')
    return out


def inspect_page(slug: str, text: str) -> dict:
    top = text.split('<article class="wiki"', 1)[0]
    return {
        "slug": slug,
        "bytes": len(text.encode("utf-8")),
        "marker": MARKER in text,
        "selector_present": 'data-testid="galaxy-method-result-selector"' in text,
        "selector_link_count": text.count('data-testid="galaxy-method-result-link"'),
        "selector_before_tabs": text.find('data-testid="galaxy-method-result-selector"') < text.find("Raw Text"),
        "tabs_present": all(term in text for term in ["Raw Text", "Colors On", "Hide Citations", "Show Ideas"]),
        "article_present": '<article class="wiki"' in text,
        "article_h1": '<h1 id="galaxy-evolution">Galaxy Evolution</h1>' in text,
        "method_card_absent": 'class="method-card"' not in top,
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
        "no_active_execution_phrase": "NO ACTIVE EXECUTION PHRASE" in text,
        "approve_execute_absent": "APPROVE EXECUTE" not in text,
        "approve_apply_absent": "APPROVE APPLY" not in text,
    }


def main() -> None:
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    backup_dir = RECEIPT_DIR / "working-backup-before-selector-shell"
    backup_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for slug in SLUGS:
        path = ROOT / slug / "wiki-page.html"
        if not path.exists():
            raise SystemExit(f"missing {path}")
        original = path.read_text(encoding="utf-8")
        shutil.copy2(path, backup_dir / f"{slug}__wiki-page.html")
        updated = transform(original)
        row = inspect_page(slug, updated)
        required_bool_keys = [
            "marker",
            "selector_present",
            "selector_before_tabs",
            "tabs_present",
            "article_present",
            "article_h1",
            "method_card_absent",
            "top_clutter_absent",
            "no_active_execution_phrase",
            "approve_execute_absent",
            "approve_apply_absent",
        ]
        failures = [key for key in required_bool_keys if not row[key]]
        if row["selector_link_count"] != 3:
            failures.append("selector_link_count != 3")
        if failures:
            raise SystemExit(f"{slug}: validation failed: {failures}")
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
    (RECEIPT_DIR / "SELECTOR_SHELL_RENDER_RECEIPT.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    lines = [
        "# Static method wiki selector-shell render receipt",
        "",
        f"- marker: `{MARKER}`",
        f"- updated_utc: `{receipt['updated_utc']}`",
        "- result: the shared method result selector and normal top tabs remain; only article/content varies by method.",
        "- removed from top shell: per-method identifier card and snapshot/deck/atlas/workspace/quintet clutter.",
        "- scope: static method `wiki-page.html` artifacts only.",
        "- safety: DB/page_versions/live product wiki publish/backend restart/trust recompute/deploy/git all 0.",
        "",
        "## Outputs",
    ]
    for row in rows:
        lines.append(
            f"- `{row['slug']}`: selector={row['selector_present']}, links={row['selector_link_count']}, "
            f"tabs={row['tabs_present']}, article_h1={row['article_h1']}, top_clutter_absent={row['top_clutter_absent']}"
        )
    lines.append("")
    lines.append(f"Working backups: `{backup_dir}`")
    (RECEIPT_DIR / "SELECTOR_SHELL_RENDER_RECEIPT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))

if __name__ == "__main__":
    main()
