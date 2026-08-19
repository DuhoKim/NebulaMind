#!/usr/bin/env python3
"""Render a private tailnet-only HTML dashboard for the Galaxy Evolution autopilot.

Source:  .hermes/handoffs/galaxy-evolution/mastermind/autopilot-status.json
Output:  /Users/duhokim/HermesOps/cockpit/ge-autopilot.html
         /Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json

This script is intentionally static/report-only. It does not dispatch prompts,
approve permissions, publish live wiki pages, edit the public NebulaMind cockpit,
touch DB/API, deploy, restart services, run git, or contact cloud APIs.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import time
from pathlib import Path
from typing import Any, Dict, List

MARKER = "GE_AUTOPILOT_PRIVATE_DASHBOARD_V1"
REPO = Path(os.environ.get("NEBULAMIND_REPO", "/Users/duhokim/NebulaMind/NebulaMind"))
SOURCE_STATUS = Path(os.environ.get(
    "GE_AUTOPILOT_SOURCE_STATUS",
    str(REPO / ".hermes/handoffs/galaxy-evolution/mastermind/autopilot-status.json"),
))
WEB_ROOT = Path(os.environ.get("GE_AUTOPILOT_WEB_ROOT", "/Users/duhokim/HermesOps/cockpit"))
HTML_PATH = WEB_ROOT / "ge-autopilot.html"
JSON_PATH = WEB_ROOT / "ge-autopilot-status.json"
LATEST_URL_PATH = WEB_ROOT / "latest-ge-autopilot-url.txt"
URL = os.environ.get("GE_AUTOPILOT_URL", "https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html")
STATUS_URL = "ge-autopilot-status.json"

# Superseded by render_ge_autopilot_dashboard_v2.py (the live renderer). Groups remapped
# 2026-08-05 with v2 so the two files cannot disagree if this one is ever run again; the
# paper-to-wiki method lanes and their mesh-ge-m{1,2,3}-* sessions are retired.
GROUP_ORDER = ["Directors", "Review", "Lanes", "Other"]
SAFETY_GATES = [
    "DB/SQL writes",
    "/api/pages, page_versions, live wiki publish",
    "deploy/restart/service mutation",
    "git commit/push/merge/rebase/reset",
    "public NebulaMind cockpit/Baseline replacement",
    "cloud/GCP/API/billing/OAuth/token/secrets/.env",
    "browser automation or cron",
    "direct method wiki-page.html overwrite",
]


def now_utc() -> str:
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def parse_ts(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return dt.datetime.fromisoformat(value)
    except Exception:
        return None


def age_seconds(ts: str | None) -> int | None:
    parsed = parse_ts(ts)
    if not parsed:
        return None
    return max(0, int((dt.datetime.now(dt.timezone.utc) - parsed).total_seconds()))


def age_label(seconds: int | None) -> str:
    if seconds is None:
        return "unknown"
    if seconds < 60:
        return f"{seconds}s"
    if seconds < 3600:
        return f"{seconds // 60}m {seconds % 60}s"
    return f"{seconds // 3600}h {(seconds % 3600) // 60}m"


def load_source() -> Dict[str, Any]:
    if not SOURCE_STATUS.exists():
        return {
            "ts": now_utc(),
            "repo": str(REPO),
            "phase": "phase1-bounded-controller",
            "targets": [],
            "panes": [],
            "blockers": [{"role": "dashboard", "reason": f"source status not found: {SOURCE_STATUS}", "safe_to_approve": False}],
            "hard_gates_closed": SAFETY_GATES,
            "status_path": str(SOURCE_STATUS),
        }
    return json.loads(SOURCE_STATUS.read_text())


def group_for(pane: Dict[str, Any]) -> str:
    role = str(pane.get("role") or "")
    target = str(pane.get("target") or "")
    if target.startswith("ge-mastermind") or role in {"Hwao-director", "Tori-director", "Goru-director-live-view"}:
        return "Directors"
    if "m1" in target or role.endswith("-m1"):
        return "Review"
    if "m2" in target or role.endswith("-m2"):
        return "Lanes"
    if "m3" in target or role.endswith("-m3"):
        return "Other"
    return "Other"


def pane_status(pane: Dict[str, Any]) -> str:
    cls = pane.get("classification") or {}
    if pane.get("dead"):
        return "dead"
    if cls.get("permission_prompt") and not cls.get("safe_to_approve"):
        return "review"
    if cls.get("permission_prompt") and cls.get("safe_to_approve"):
        return "safe-prompt"
    if pane.get("in_mode"):
        return "copy-mode"
    if pane.get("active"):
        return "active"
    return "idle"


def compact_tail(tail: str | None, limit: int = 160) -> str:
    if not tail:
        return ""
    lines = [line.strip() for line in str(tail).splitlines() if line.strip()]
    if not lines:
        return ""
    text = " · ".join(lines[-2:])
    if len(text) > limit:
        return text[: limit - 1] + "…"
    return text


def compact_status(source: Dict[str, Any]) -> Dict[str, Any]:
    groups: Dict[str, List[Dict[str, Any]]] = {name: [] for name in GROUP_ORDER}
    counts = {
        "targets_ok": 0,
        "targets_total": len(source.get("targets", [])),
        "panes": 0,
        "active": 0,
        "idle": 0,
        "dead": 0,
        "copy_mode": 0,
        "safe_prompts": 0,
        "review_prompts": 0,
        "blockers": len(source.get("blockers", [])),
    }

    for target in source.get("targets", []):
        if target.get("exists"):
            counts["targets_ok"] += 1

    for pane in source.get("panes", []):
        cls = pane.get("classification") or {}
        status = pane_status(pane)
        if status == "active":
            counts["active"] += 1
        elif status == "idle":
            counts["idle"] += 1
        elif status == "dead":
            counts["dead"] += 1
        elif status == "copy-mode":
            counts["copy_mode"] += 1
        elif status == "safe-prompt":
            counts["safe_prompts"] += 1
        elif status == "review":
            counts["review_prompts"] += 1
        counts["panes"] += 1
        item = {
            "pane_id": pane.get("pane_id"),
            "role": pane.get("role") or "unknown",
            "command": pane.get("current_command") or "",
            "status": status,
            "active": bool(pane.get("active")),
            "dead": bool(pane.get("dead")),
            "copy_mode": bool(pane.get("in_mode")),
            "target": pane.get("target") or "",
            "size": pane.get("size") or "",
            "permission_prompt": bool(cls.get("permission_prompt")),
            "safe_to_approve": bool(cls.get("safe_to_approve")),
            "reason": cls.get("reason") or "",
            "tail_excerpt": compact_tail(pane.get("tail")),
        }
        groups.setdefault(group_for(pane), []).append(item)

    source_ts = source.get("ts")
    age = age_seconds(source_ts)
    health = "healthy"
    health_text = "RUNNING CLEAN"
    if counts["dead"] or counts["review_prompts"]:
        health = "needs-review"
        health_text = f"NEEDS YOU · {counts['dead'] + counts['review_prompts']}"
    elif counts["blockers"] or counts["safe_prompts"] or counts["copy_mode"]:
        health = "watching"
        health_text = "WATCHING SAFE PROMPTS"
    if age is not None and age > 90:
        health = "stale"
        health_text = "STALE · monitor may be paused"

    return {
        "marker": MARKER,
        "generated_at": now_utc(),
        "source_ts": source_ts,
        "source_age_seconds": age,
        "source_age_label": age_label(age),
        "health": health,
        "health_text": health_text,
        "phase": source.get("phase") or "phase1-bounded-controller",
        "repo": source.get("repo") or str(REPO),
        "url": URL,
        "tailnet_only": True,
        "browser_executes_actions": False,
        "counts": counts,
        "targets": source.get("targets", []),
        "groups": groups,
        "blockers": source.get("blockers", []),
        "hard_gates_closed": source.get("hard_gates_closed") or SAFETY_GATES,
        "source_status_path": str(SOURCE_STATUS),
        "web_status_path": str(JSON_PATH),
    }


def e(value: Any) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def render_html() -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>Galaxy Evolution Autopilot Dashboard</title>
  <style>
    :root {{
      --bg:#050914; --bg2:#071525; --panel:#0d1d32; --panel2:#112946; --line:#244263;
      --text:#edf5ff; --muted:#91a9c8; --soft:#c7d9f1; --green:#3ee28f; --yellow:#ffd166;
      --red:#ff6b7a; --blue:#7dccff; --violet:#c6a6ff; --shadow:0 22px 70px rgba(0,0,0,.35);
    }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,sans-serif; color:var(--text); background:
      radial-gradient(circle at 12% 0%, rgba(67,139,255,.34), transparent 34%),
      radial-gradient(circle at 88% 8%, rgba(62,226,143,.16), transparent 28%),
      linear-gradient(180deg,#071525,#050914 58%,#040712); min-height:100vh; }}
    header {{ padding:28px clamp(16px,4vw,46px) 18px; border-bottom:1px solid rgba(125,204,255,.18); position:sticky; top:0; z-index:3; backdrop-filter:blur(18px); background:rgba(5,9,20,.78); }}
    h1 {{ margin:0; font-size:clamp(28px,4vw,52px); letter-spacing:-.055em; line-height:.98; }}
    h2 {{ margin:0 0 12px; font-size:19px; }}
    h3 {{ margin:0; font-size:14px; color:var(--muted); text-transform:uppercase; letter-spacing:.1em; }}
    p {{ color:var(--muted); line-height:1.55; }}
    a {{ color:#a7dcff; }} code {{ color:#bce6ff; }}
    main {{ padding:22px clamp(16px,4vw,46px) 54px; }}
    .hero {{ display:grid; grid-template-columns:minmax(0,1.4fr) minmax(280px,.6fr); gap:18px; align-items:stretch; }}
    .panel,.metric,.lane,.gate,.flowbox {{ border:1px solid rgba(125,204,255,.20); background:linear-gradient(180deg,rgba(17,41,70,.88),rgba(9,23,41,.92)); border-radius:22px; box-shadow:var(--shadow); }}
    .panel {{ padding:20px; }}
    .subtitle {{ margin:10px 0 0; max-width:980px; color:var(--soft); }}
    .topline {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:16px; }}
    .pill {{ display:inline-flex; align-items:center; gap:8px; border:1px solid var(--line); background:rgba(8,20,35,.72); border-radius:999px; padding:8px 11px; color:var(--soft); font-size:13px; }}
    .dot {{ width:10px; height:10px; border-radius:50%; background:var(--blue); box-shadow:0 0 18px currentColor; }}
    .healthy .dot {{ background:var(--green); }} .watching .dot,.stale .dot {{ background:var(--yellow); }} .needs-review .dot {{ background:var(--red); }}
    .metrics {{ display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:12px; margin:18px 0; }}
    .metric {{ padding:16px; min-height:106px; }} .metric b {{ display:block; font-size:34px; letter-spacing:-.04em; }} .metric span {{ color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:.1em; }}
    .flow {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; margin-top:14px; }}
    .flowbox {{ padding:13px; min-height:96px; position:relative; overflow:hidden; }} .flowbox strong {{ display:block; font-size:17px; }} .flowbox small {{ color:var(--muted); }}
    .flowbox::after {{ content:""; position:absolute; right:-20px; bottom:-26px; width:90px; height:90px; border-radius:50%; background:rgba(125,204,255,.11); }}
    .board {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:16px; margin-top:18px; }}
    .directors-band {{ margin-top:18px; border-color:rgba(125,204,255,.36); }}
    .directors-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; }}
    .methods-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px; margin-top:18px; }}
    .other-grid {{ margin-top:18px; }}
    .lane-group {{ min-width:0; }}
    .lane {{ padding:14px; margin:10px 0; box-shadow:none; background:rgba(8,20,35,.64); }}
    .lane-head {{ display:flex; justify-content:space-between; gap:10px; align-items:baseline; }}
    .lane-role {{ font-weight:750; word-break:break-word; }} .pane-id {{ color:#bce6ff; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
    .meta {{ color:var(--muted); font-size:12px; line-height:1.45; margin-top:7px; word-break:break-word; }}
    .chips {{ display:flex; flex-wrap:wrap; gap:6px; margin-top:10px; }}
    .chip {{ font-size:11px; border-radius:999px; padding:5px 8px; border:1px solid var(--line); color:var(--muted); background:#0b1a2d; }}
    .chip.active {{ background:var(--blue); color:#04101c; border-color:var(--blue); }} .chip.healthy {{ background:var(--green); color:#04120b; border-color:var(--green); }}
    .chip.review,.chip.stale {{ background:var(--yellow); color:#160f00; border-color:var(--yellow); }} .chip.dead {{ background:var(--red); color:white; border-color:var(--red); }}
    .tail {{ margin-top:9px; color:#b8c9df; font-size:11px; opacity:.86; border-left:2px solid rgba(125,204,255,.24); padding-left:8px; }}
    .wide {{ display:grid; grid-template-columns:1.2fr .8fr; gap:16px; margin-top:18px; }}
    .gate-list {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px; }} .gate {{ padding:10px 12px; box-shadow:none; color:var(--soft); font-size:13px; }}
    .gates-strip {{ margin:0 0 18px; }} .gates-strip .gate-list {{ grid-template-columns:repeat(4,minmax(0,1fr)); }} .lock {{ color:var(--green); font-weight:900; }}
    textarea {{ width:100%; min-height:62px; border-radius:14px; border:1px solid var(--line); background:#071525; color:var(--text); padding:12px; resize:vertical; }}
    .empty {{ color:var(--muted); border:1px dashed var(--line); border-radius:14px; padding:14px; }}
    footer {{ color:var(--muted); padding:10px clamp(16px,4vw,46px) 36px; }}
    @media (max-width:1180px) {{ .metrics {{ grid-template-columns:repeat(3,minmax(0,1fr)); }} .board,.flow,.directors-grid,.methods-grid,.gates-strip .gate-list {{ grid-template-columns:repeat(2,minmax(0,1fr)); }} .hero,.wide {{ grid-template-columns:1fr; }} }}
    @media (max-width:720px) {{ header {{ position:static; }} .metrics,.board,.flow,.gate-list,.directors-grid,.methods-grid,.gates-strip .gate-list {{ grid-template-columns:1fr; }} }}
  </style>
</head>
<body>
  <header>
    <h1>Galaxy Evolution Autopilot</h1>
    <p class="subtitle">PRIVATE TAILNET MIRROR · READ-ONLY · this page takes no actions. Private Mac Studio → MacBook cockpit for Phase 1 bounded autonomy.</p>
    <div class="topline">
      <span id="health-pill" class="pill"><span class="dot"></span><span id="health-text">Loading…</span></span>
      <span class="pill"><span class="dot"></span><span id="updated-text">Waiting for JSON</span></span>
      <span class="pill"><span class="dot"></span><span>{MARKER}</span></span>
    </div>
  </header>
  <main>
    <section class="panel gates-strip">
      <h2>Hard gates closed</h2>
      <p>Hard gates closed — no DB · no live wiki/publish · no deploy · no git · no cockpit/global · no cloud/billing/OAuth · no browser · no cron.</p>
      <div id="gates-top" class="gate-list"></div>
    </section>
    <section class="hero">
      <div class="panel">
        <h2>What you should check first</h2>
        <div class="flow">
          <div class="flowbox"><strong>1. Health</strong><small>Healthy, watching, stale, or needs review.</small></div>
          <div class="flowbox"><strong>2. Blockers</strong><small>Permission prompts that need action.</small></div>
          <div class="flowbox"><strong>3. Method lanes</strong><small>M1/M2/M3 pane states at a glance.</small></div>
          <div class="flowbox"><strong>4. Safety gates</strong><small>What the controller still cannot do.</small></div>
        </div>
      </div>
      <div class="panel">
        <h2>Open from MacBook</h2>
        <textarea id="urlbox" readonly>{e(URL)}</textarea>
        <p class="small">Select the URL above to copy, or open <a href="{e(URL)}">the private tailnet link</a>. Requires Tailscale login on the MacBook. This is not open public internet. The browser does not execute actions.</p>
      </div>
    </section>
    <section class="metrics" id="metrics"></section>
    <section class="panel directors-band">
      <h2>Directors</h2>
      <p>Hwao sets direction; Tori verifies and relays; Goru provides mechanical crosschecks.</p>
      <div id="directors" class="directors-grid"></div>
    </section>
    <section class="methods-grid" id="methods"></section>
    <section class="other-grid" id="other"></section>
    <section class="wide">
      <div class="panel">
        <h2>Current blockers / prompts</h2>
        <div id="blockers" class="empty">Loading…</div>
      </div>
      <div class="panel">
        <h2>Safety gates closed</h2>
        <div id="gates" class="gate-list"></div>
      </div>
    </section>
  </main>
  <footer>
    Source: <code>{e(str(SOURCE_STATUS))}</code><br>
    Rendered JSON: <code>{e(str(JSON_PATH))}</code>. Auto-refreshes every 5 seconds.
  </footer>
<script>
const STATUS_URL = {json.dumps(STATUS_URL)};
const GROUP_ORDER = {json.dumps(GROUP_ORDER)};
function esc(s) {{ return String(s ?? '').replace(/[&<>"']/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c])); }}
function metric(label, value) {{ return `<div class="metric"><b>${{esc(value)}}</b><span>${{esc(label)}}</span></div>`; }}
function chip(text, cls='') {{ return `<span class="chip ${{cls}}">${{esc(text)}}</span>`; }}
function paneFlags(p) {{
  const out = [];
  if (p.status === 'dead') out.push(chip('dead','dead'));
  if (p.status === 'review') out.push(chip('review prompt','review'));
  if (p.status === 'safe-prompt') out.push(chip('safe prompt','healthy'));
  if (p.status === 'copy-mode') out.push(chip('copy-mode','review'));
  if (p.active) out.push(chip('active','active'));
  if (!out.length) out.push(chip('observed'));
  return out.join('');
}}
function paneCard(p) {{
  return `<div class="lane"><div class="lane-head"><span class="lane-role">${{esc(p.role)}}</span><span class="pane-id">${{esc(p.pane_id)}}</span></div><div class="meta">${{esc(p.command)}} · ${{esc(p.size)}}<br>${{esc(p.reason || p.target || '')}}</div><div class="chips">${{paneFlags(p)}}</div>${{p.tail_excerpt ? `<div class="tail">${{esc(p.tail_excerpt)}}</div>` : ''}}</div>`;
}}
function groupCard(name, panes) {{
  return `<section class="panel lane-group"><h3>${{esc(name)}}</h3><h2>${{panes.length}} panes</h2>${{panes.length ? panes.map(paneCard).join('') : '<div class="empty">No panes seen</div>'}}</section>`;
}}
function blockerCard(b) {{
  return `<div class="lane"><div class="lane-head"><span class="lane-role">${{esc(b.role || 'unknown')}}</span><span class="pane-id">${{esc(b.pane_id || '')}}</span></div><div class="meta">safe=${{esc(b.safe_to_approve)}} · ${{esc(b.reason || '')}}</div></div>`;
}}
async function load() {{
  try {{
    const res = await fetch(`${{STATUS_URL}}?t=${{Date.now()}}`, {{cache:'no-store'}});
    if (!res.ok) throw new Error(`HTTP ${{res.status}}`);
    const d = await res.json();
    const c = d.counts || {{}};
    const pill = document.getElementById('health-pill');
    pill.className = `pill ${{d.health || 'healthy'}}`;
    document.getElementById('health-text').textContent = d.health_text || d.health || 'unknown';
    document.getElementById('updated-text').textContent = `Updated ${{d.source_ts || d.generated_at || 'unknown'}} · age ${{d.source_age_label || 'unknown'}}`;
    document.getElementById('metrics').innerHTML = [
      metric('Targets OK', `${{c.targets_ok ?? 0}}/${{c.targets_total ?? 0}}`),
      metric('Panes', c.panes ?? 0),
      metric('Active', c.active ?? 0),
      metric('Blockers', c.blockers ?? 0),
      metric('Safe prompts', c.safe_prompts ?? 0),
      metric('Review prompts', c.review_prompts ?? 0),
    ].join('');
    const groups = d.groups || {{}};
    document.getElementById('directors').innerHTML = (groups['Directors'] || []).length ? (groups['Directors'] || []).map(paneCard).join('') : '<div class="empty">No director panes seen</div>';
    document.getElementById('methods').innerHTML = ['Review','Lanes'].map(g => groupCard(g, groups[g] || [])).join('');
    const other = groups['Other'] || [];
    document.getElementById('other').innerHTML = other.length ? groupCard('Standalone / helpers', other) : '';
    const blockers = d.blockers || [];
    document.getElementById('blockers').className = blockers.length ? '' : 'empty';
    document.getElementById('blockers').innerHTML = blockers.length ? blockers.map(blockerCard).join('') : 'No current blockers or permission prompts.';
    const gateHtml = (d.hard_gates_closed || []).map(x => `<div class="gate"><span class="lock">🔒</span> ${{esc(x)}}</div>`).join('');
    document.getElementById('gates').innerHTML = gateHtml;
    document.getElementById('gates-top').innerHTML = gateHtml;
  }} catch (err) {{
    const pill = document.getElementById('health-pill');
    pill.className = 'pill needs-review';
    document.getElementById('health-text').textContent = `Dashboard data unavailable: ${{err.message}}`;
  }}
}}
load(); setInterval(load, 5000);
</script>
</body>
</html>
"""


def write_outputs(compact: Dict[str, Any]) -> None:
    WEB_ROOT.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(compact, indent=2, sort_keys=True) + "\n")
    HTML_PATH.write_text(render_html())
    LATEST_URL_PATH.write_text(URL + "\n")


def render_once() -> Dict[str, Any]:
    source = load_source()
    compact = compact_status(source)
    write_outputs(compact)
    return compact


def main() -> int:
    parser = argparse.ArgumentParser(description="Render private Galaxy Evolution autopilot dashboard")
    parser.add_argument("--watch", action="store_true", help="refresh continuously")
    parser.add_argument("--interval", type=float, default=20.0)
    parser.add_argument("--json", action="store_true", help="print compact JSON after one render")
    args = parser.parse_args()
    if args.watch:
        while True:
            compact = render_once()
            print(json.dumps({"ts": compact["generated_at"], "health": compact["health"], "blockers": compact["counts"]["blockers"], "url": URL}), flush=True)
            time.sleep(args.interval)
    compact = render_once()
    if args.json:
        print(json.dumps(compact, indent=2, sort_keys=True))
    else:
        print(f"rendered {HTML_PATH}")
        print(f"rendered {JSON_PATH}")
        print(URL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
