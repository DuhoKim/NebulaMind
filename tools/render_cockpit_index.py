#!/usr/bin/env python3
"""Generate the cockpit index from what is actually on disk.

Hand-written index pages rot: the one this replaces was six weeks old with all six
links broken. This reads the directory instead, so a page that disappears drops off
the index and a page that goes stale says so on its own card.
"""
import html, os, re, subprocess, sys
from datetime import datetime, timezone

COCKPIT = "/Users/duhokim/HermesOps/cockpit"

# Curation: what a surface IS cannot be read off disk. Everything else is derived.
GROUPS = [
    ("Live", "Regenerated from data. Trust these.", [
        ("ge-autopilot.html",        "Galaxy-evolution + surveys autopilot — provider usage, lanes, septet matrix"),
        ("spin-parity-status.html",  "Longo spin-parity study — gates, route, what is waiting on whom"),
        ("bhu-lane2-status.html",    "Black-hole-universe lane 2 — the chain fails by its own forgotten test"),
    ]),
    ("Current", "Static, but recent and still meaningful.", [
        ("methods-note-mittal-singal-v4.html",   "Methods note — Mittal–Singal Quaia dipole"),
        ("methods-note-mittal-singal-text.html", "The same note as exact source text"),
        ("bhu-video.html",                       "BHU closing record, 12 Aug — superseded by lane 2 below"),
        ("pipeline-board.html",                  "AI-scientist pipeline board"),
    ]),
    ("Stale", "Left in place, but old enough to mislead. Read the date before believing anything here.", [
        ("live-steering-cockpit.html",   "Queue helper QA — renderer is now a .bak file, nothing regenerates this"),
        ("mobile.html",                  "Batch B3 row decisions"),
        ("baseline-galaxy-current.html", "Locked with the macOS uchg flag — deliberately immutable"),
        ("baseline-roadmap.html",        "Locked with the macOS uchg flag — byte-identical to the two above"),
        ("galaxy-evolution-readonly-scope-reset-latest.html", "July scope reset"),
        ("galaxy-canonical-quartet-design.html",              "Quartet design note"),
        ("paper-prose-distillation-board.html",               "Prose distillation board"),
        ("overnight-paper-distillation-report-20260702.html",  "Overnight distillation report"),
        ("copy-execution-phrase.html",   "Execution-phrase helper"),
    ]),
]

def age(path):
    mt = datetime.fromtimestamp(os.path.getmtime(path), tz=timezone.utc)
    days = (datetime.now(timezone.utc) - mt).days
    return mt, days

def band(days):
    if days <= 1:  return "fresh"
    if days <= 7:  return "recent"
    if days <= 30: return "aging"
    return "old"

rows, missing = [], []
for title, blurb, items in GROUPS:
    out = []
    for name, desc in items:
        p = os.path.join(COCKPIT, name)
        if not os.path.exists(p):
            missing.append(name); continue
        mt, days = age(p)
        out.append((name, desc, mt, days, band(days), os.path.getsize(p)))
    rows.append((title, blurb, out))

# Anything on disk we did not curate — surfaced rather than silently omitted.
curated = {n for _,_,items in GROUPS for n,_ in items} | {"index.html"}
uncurated = sorted(f for f in os.listdir(COCKPIT)
                   if f.endswith(".html") and f not in curated)

now = datetime.now().strftime("%d %b %Y, %H:%M KST")
P = []
P.append("<!doctype html><meta charset=utf-8><title>NebulaMind cockpit</title>")
P.append('<meta name=viewport content="width=device-width,initial-scale=1">')
P.append("""<style>
:root{color-scheme:dark light}*{box-sizing:border-box}
body{font:16px/1.6 -apple-system,BlinkMacSystemFont,system-ui,sans-serif;max-width:54rem;margin:0 auto;padding:2rem 1.1rem 4rem;background:#0f1115;color:#dfe3ea}
h1{font-size:1.5rem;margin:.2em 0 .1em;color:#fff}
.sub{color:#8b93a1;font-size:.9rem;margin-bottom:2rem}
h2{font-size:1rem;margin:2.4em 0 .3em;padding-top:.8em;border-top:1px solid #232833;color:#9db8e8;letter-spacing:.02em}
.blurb{color:#8b93a1;font-size:.85rem;margin:0 0 1em}
a.card{display:flex;gap:1em;align-items:baseline;text-decoration:none;background:#141922;border:1px solid #232833;border-radius:9px;padding:.85em 1em;margin:.5em 0;transition:border-color .15s}
a.card:hover{border-color:#3a4658}
.nm{color:#fff;font-weight:500;flex:1}
.ds{color:#8b93a1;font-size:.85rem;display:block;margin-top:.2em;font-weight:400}
.ag{font-size:.78rem;white-space:nowrap;font-variant-numeric:tabular-nums}
.fresh{color:#8ee6b8}.recent{color:#c9d97a}.aging{color:#e8b87a}.old{color:#ff9e8a}
.note{color:#78818f;font-size:.82rem;margin:1.4em 0 0}
code{background:#1b212b;padding:.1em .35em;border-radius:4px;font-size:.85em}
</style>""")
P.append("<body>")
P.append("<h1>NebulaMind cockpit</h1>")
P.append(f'<div class=sub>Generated from what is on disk · {now}</div>')

for title, blurb, items in rows:
    if not items: continue
    P.append(f"<h2>{title}</h2>")
    P.append(f'<p class=blurb>{html.escape(blurb)}</p>')
    for name, desc, mt, days, bd, size in items:
        agestr = "today" if days == 0 else ("1 day" if days == 1 else f"{days} days")
        P.append(
            f'<a class=card href="{name}">'
            f'<span class=nm>{html.escape(name)}<span class=ds>{html.escape(desc)}</span></span>'
            f'<span class="ag {bd}">{agestr}</span></a>'
        )

if uncurated:
    P.append("<h2>Uncurated</h2>")
    P.append('<p class=blurb>On disk but not classified above. Listed rather than hidden — decide or retire.</p>')
    for f in uncurated:
        mt, days = age(os.path.join(COCKPIT, f))
        P.append(f'<a class=card href="{f}"><span class=nm>{html.escape(f)}</span>'
                 f'<span class="ag {band(days)}">{days} days</span></a>')

if missing:
    P.append("<h2>Missing</h2>")
    P.append('<p class=blurb>Curated but not on disk. This is the failure the previous index had — '
             'all six of its links pointed at paths that no longer existed.</p>')
    for m in missing:
        P.append(f'<div class=card style="opacity:.6"><span class=nm>{html.escape(m)}</span>'
                 f'<span class="ag old">missing</span></div>')

P.append('<p class=note>Retired pages are under <code>archive/retired-20260817/</code> with a manifest '
         'recording pre-move hashes. Nothing was deleted.</p>')
P.append('<p class=note>Regenerate: <code>python3 mkindex.py</code>. This page is derived, so a surface that '
         'vanishes drops off it and a surface that goes stale says so — rather than the index quietly '
         'lying, which is what the last one did for six weeks.</p>')
P.append("</body>")

out = "\n".join(P)
open(os.path.join(COCKPIT, "index.html"), "w").write(out)
print(f"  wrote index.html — {len(out)} chars")
print(f"  curated {sum(len(i) for _,_,i in rows)} · uncurated {len(uncurated)} · missing {len(missing)}")
