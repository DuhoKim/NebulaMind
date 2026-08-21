#!/usr/bin/env python3
"""nm_paper_run_dashboard.py — per-paper autonomous-run status, derived from artifacts.

Duho, 2026-08-06, after the overnight run: "make a dashboard for the auto run for each paper?"

The question this exists to answer is the one the overnight cron could not: **for each paper,
what is blocking it, and is that blocker actually queued?** The cron was written as a reactive
loop — check for verdicts, apply edits, resubmit — so it could only advance work already in
flight. Amendment A2 had six edits applied at 23:14 and was never resubmitted; it was the hard
precondition for an entire measurement sequence and it sat unqueued for eleven hours, invisible,
because nothing ever asked what the critical path needed. A BLOCKED lane with nothing running is
the state this dashboard is built to make impossible to miss.

Everything is read from artifacts on disk. Nothing is hand-maintained, so the dashboard cannot
drift from reality the way a status file does — if it is wrong, the artifacts are wrong.

Signals, per lane:
  - gate rounds and the LATEST verdict per gate family (KUN_*/MIRU_* files, verdict lines)
  - frozen artifacts (read-only + a recorded sha) vs still-mutable drafts
  - fail-closed state of any reviewed script (unfilled pins)
  - stage progress from WORKFLOW_CHECKLIST.json where one exists
  - whether a reviewer seat is CURRENTLY running for that lane
  - the derived state: RUNNING / AT GATE / BLOCKED-NOT-QUEUED / AWAITING HUMAN / IDLE

Usage:  nm_paper_run_dashboard.py            # text to stdout
        nm_paper_run_dashboard.py --html OUT # write a standalone page
"""
import argparse, glob, json, os, re, subprocess, time

ROOT = "/Users/duhokim/NebulaMind/NebulaMind"
HANDOFFS = os.path.join(ROOT, ".hermes", "handoffs")
STUDIES = os.path.join(ROOT, "frontend", "public", "studies")
VIDEOS = os.path.join(ROOT, "frontend", "public", "videos")

VERDICT = re.compile(
    r"^(?:.*\b)?((?:[A-Z0-9 _-]*)?(?:GATE|VERDICT|CONFIRMATION|RE-GATE)[A-Z0-9 _-]*)\s*:\s*"
    r"(PASS_WITH_EDITS|PASS|FAIL|APPROVED_WITH_EDITS|APPROVED|REJECTED|"
    r"FREEZE APPROVED|MINOR|ESTABLISHED|UNEVALUABLE)\b", re.M)
OPEN_VERDICTS = {"PASS_WITH_EDITS", "APPROVED_WITH_EDITS", "REJECTED", "FAIL"}


def sh(cmd):
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return ""


def seats_running():
    """Which lanes have a reviewer seat live right now (cwd of the hermes process)."""
    out, lanes = sh("pgrep -f 'kimi-k3 -Q'"), set()
    for pid in [p for p in out.split() if p.strip().isdigit()]:
        cwd = sh(f"lsof -a -p {pid} -d cwd -Fn 2>/dev/null | grep '^n'")
        for lane in cwd.strip().splitlines():
            lanes.add(os.path.basename(lane.lstrip("n")))
    return lanes


def gate_files(lane):
    return sorted(glob.glob(os.path.join(lane, "KUN_*.md")) +
                  glob.glob(os.path.join(lane, "MIRU_*.md")), key=os.path.getmtime)


def latest_verdicts(lane):
    """Latest verdict per family, newest file wins. Returns [(family, verdict, file, mtime)]."""
    seen = {}
    for f in gate_files(lane):
        try:
            body = open(f, "r", encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for fam, v in VERDICT.findall(body):
            fam = re.sub(r"\s+", " ", fam).strip()
            # collapse round numbering so RE-GATE 4 and RE-GATE 7 are one family
            key = re.sub(r"\b\d+\b", "", fam).strip() or fam
            if key in ("VERDICT UP FRONT", "VERDICT"):
                key = "GATE"          # report preamble, not a distinct gate family
            seen[key] = (v, os.path.basename(f), os.path.getmtime(f))
    return [(k, *v) for k, v in sorted(seen.items(), key=lambda kv: -kv[1][2])]


def frozen_artifacts(lane):
    frozen, mutable = [], []
    for f in glob.glob(os.path.join(lane, "*CONTRACT*.md")) + glob.glob(os.path.join(lane, "AMENDMENT_*.md")):
        (frozen if not (os.stat(f).st_mode & 0o222) else mutable).append(os.path.basename(f))
    return sorted(frozen), sorted(mutable)


def script_state(lane):
    """Reviewed scripts and whether their chain is fail-closed (unfilled pins)."""
    out = []
    for f in glob.glob(os.path.join(lane, "t*.py")):
        try:
            s = open(f, "r", encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        if "PINS" not in s and "verify_chain" not in s:
            continue
        # Count placeholder VALUES only. A bare "<FILL" substring also matches the guard code
        # that COMPARES against the placeholder (`pin.startswith("<FILL")`), which inflated the
        # count from 4 to 9 on first run — the dashboard reporting its own logic as state.
        n = len(re.findall(r':\s*"<FILL[^"]*"', s))
        out.append({"file": os.path.basename(f), "unfilled_pins": n,
                    "state": (f"fail-closed ({n} placeholder pin{'s' if n != 1 else ''} unfilled)"
                              if n else "chain satisfiable — every pin filled")})
    return out


# Quintet role table (.hermes/workflows/QUINTET_PAPER_RUN_V1.md). A lane running with a seat
# empty is a ROLE_TABLE_BLOCKER: the overnight run staffed only Kun, and every mechanical-count
# defect it produced belonged to an unstaffed seat.
# Naming reform 2026-08-19: helper seats go by engine (claude-seat, agy, kimi,
# gpt1/gpt2); persona names are retired for NEW records, but every pre-reform
# lane's artifacts are still named KUN_*/GORU_*/TORI_* — so staffing matches the
# legacy tokens as aliases while DISPLAYING engine names.
SEATS = {"Hwao": "coordinates", "claude-seat": "science pressure", "agy": "mechanical counts",
         "kimi": "reproducibility", "gpt2": "relay/receipts"}
SEAT_ALIASES = {"claude-seat": ("LANA",), "agy": ("GORU",), "kimi": ("KUN", "MIRU"),
                "gpt2": ("TORI",), "gpt1": ("YUI",)}


def staffing(lane):
    """Which seats have actually produced an artifact in this lane (engine or legacy names)."""
    names = " ".join(os.path.basename(f) for f in glob.glob(os.path.join(lane, "*"))).upper()
    def hit(seat):
        return any(tok in names for tok in (seat.upper(),) + SEAT_ALIASES.get(seat, ()))
    staffed = {s for s in SEATS if hit(s)}
    return sorted(staffed), sorted(set(SEATS) - staffed - {"Hwao"})


def checklist(lane):
    p = os.path.join(lane, "WORKFLOW_CHECKLIST.json")
    if not os.path.exists(p):
        return None
    try:
        d = json.load(open(p))
    except (OSError, ValueError):
        return None
    st = d.get("stages", [])
    return {"done": sum(1 for s in st if s.get("state") == "done"), "total": len(st),
            "blocked": [s["stage"] for s in st if s.get("state") in ("blocked", "done_with_blocker")]}


def derive_state(lane_name, verdicts, running, scripts):
    """The load-bearing column: is this lane moving, waiting on a human, or stuck unqueued?"""
    if lane_name in running:
        return "RUNNING", "a reviewer seat is live for this lane"
    # State follows the NEWEST gate file only. Verdicts are listed newest-first, and an older
    # superseded report must not drive state: on first run the spin lane read BLOCKED off a
    # PASS_WITH_EDITS preamble in a report that a later PASS had already superseded.
    if not verdicts:
        return "IDLE", "no gate activity recorded"
    newest_mtime = verdicts[0][3]
    current = [(f, v) for f, v, _, m in verdicts if m == newest_mtime]
    open_v = [(f, v) for f, v in current if v in OPEN_VERDICTS]
    if open_v:
        fam, v = open_v[0]
        return ("BLOCKED — NOT QUEUED",
                f"newest gate says {fam}: {v} — edits owed, nothing running. This is the state "
                f"that cost eleven hours on 2026-08-06.")
    if verdicts:
        if any(s["unfilled_pins"] for s in scripts):
            return "AWAITING HUMAN", "all gates clear; the chain stays fail-closed pending a decision"
        return "AWAITING HUMAN", "all gates clear"
    return "IDLE", "no gate activity recorded"


# Engine → seat. A seat is "live" when its engine has a process running. Kept in ONE dashboard
# with paper status deliberately: the 2026-08-06 failure was a blocked paper and an idle seat
# sitting in different places with nobody joining them. Split the views and that blind spot
# comes back.
# Seat identification is by FULL COMMAND LINE, not engine name. Two traps this closes, both
# found live on 2026-08-06:
#   - Kun and Tori share the `hermes chat` binary; matching the binary reported an interactive
#     Kimi session as "Tori running".
#   - An interactive `agy` session from the previous day reported as "Goru running" with 231
#     minutes of CPU, when no Goru work had been dispatched.
# A seat counts as WORKING only if its process carries a one-shot prompt flag (-q / -p). An
# interactive session on the same engine is a human at a console, not a staffed seat — reported
# separately rather than counted, because "seat busy" when it is idle is the exact false
# confidence the A2 failure ran on.
SEAT_MATCH = [
    ("kimi",        lambda c: "kimi-k3" in c and "-Q" in c),
    ("gpt2",        lambda c: "hermes chat" in c and "kimi" not in c),
    ("claude-seat", lambda c: "claude" in c and "--dangerously-skip" in c),
    ("agy",         lambda c: c.strip().startswith("agy") or " agy " in c),
]

# Seat identity really lives in the tmux SESSION NAME, not the command line. Tori and Yui both run
# `hermes chat`, so the command-line matcher above cannot tell them apart and silently labels every
# Yui process "Tori" — and Yui has no entry at all. Session names are how the crew is actually
# addressed (dispatches are send-keys to a named session), so they are the honest key.
SEAT_SESSION = [
    ("gpt1",        ("gpt1", "yui-")),
    ("gpt2",        ("gpt2", "tori-")),
    ("claude-seat", ("cseat", "claude-seat", "lana-")),
    ("agy",         ("agy", "goru-")),
    ("kimi",        ("kimi", "kun-")),
    ("Hwao",        ("hwao-",)),
]
TMUX = "/opt/homebrew/bin/tmux"


def _tmux_seats():
    """Seats with a live tmux session, and which of them are busy right now.

    Busy is decided by ANIMATION, not keywords: a pane identical across two captures a second
    apart is idle, and anything rendering a spinner, timer or streaming output changes. Keyword
    detection is unreliable across these UIs — agy prints a static "Working" string and a static
    braille glyph, which reads as permanently busy.
    """
    live, busy = {}, set()
    try:
        out = sh(f"{TMUX} list-sessions -F '#{{session_name}}'")
    except Exception:
        return live, busy
    for name in [s.strip() for s in out.splitlines() if s.strip()]:
        seat = next((s for s, pre in SEAT_SESSION if any(name.startswith(p) for p in pre)), None)
        if not seat:
            continue
        live.setdefault(seat, []).append(name)
        try:
            qname = shlex.quote(name)  # session names reach a shell=True command
            a = sh(f"{TMUX} capture-pane -p -t {qname}")
            time.sleep(1)
            b = sh(f"{TMUX} capture-pane -p -t {qname}")
            if a != b:
                busy.add(seat)
        except Exception:
            pass
    return live, busy


def _dispatched(cmd):
    """A one-shot job carries a prompt flag; an interactive session does not."""
    return (" -q " in cmd or " -p " in cmd or cmd.rstrip().endswith(" -q")
            or cmd.rstrip().endswith(" -p") or " -Q -q" in cmd)


def crew_live():
    """Seats working on dispatched jobs, and interactive sessions reported apart from them."""
    working, interactive = [], []
    tmux_live, tmux_busy = _tmux_seats()
    out = sh("ps -eo pid,etime,time,command")
    for line in out.splitlines()[1:]:
        parts = line.split(None, 3)
        if len(parts) < 4:
            continue
        pid, el, cpu, cmd = parts
        if not any(k in cmd for k in ("hermes chat", "claude", "agy", "kimi-k3")):
            continue
        if "pgrep" in cmd or "nm_paper_run_dashboard" in cmd:
            continue
        seat = next((s for s, m in SEAT_MATCH if m(cmd)), None)
        if not seat:
            continue
        rec = {"seat": seat, "pid": pid, "elapsed": el, "cpu": cpu}
        (working if _dispatched(cmd) else interactive).append(rec)

    # A seat driven by send-keys into a persistent pane carries no -q/-p flag, so the flag test
    # alone reported live_seats == [] while five seats were working. That is worse than no
    # dashboard: it says "nobody is on it" about a crew that is mid-task. Sessions that are
    # actually rendering output are counted as working.
    seen = {r["seat"] for r in working}
    for seat, names in tmux_live.items():
        if seat in seen or seat not in tmux_busy:
            continue
        working.append({"seat": seat, "pid": "-", "elapsed": "-", "cpu": "-",
                        "via": "tmux:" + ",".join(names)})
    for seat, names in tmux_live.items():
        if seat in {r["seat"] for r in working} or seat in {r["seat"] for r in interactive}:
            continue
        interactive.append({"seat": seat, "pid": "-", "elapsed": "-", "cpu": "-",
                            "via": "tmux:" + ",".join(names), "idle": True})
    return working, interactive


def collect():
    rows, running = [], seats_running()
    for lane in sorted(glob.glob(os.path.join(HANDOFFS, "*"))):
        if not os.path.isdir(lane):
            continue
        # A lane carrying RETIRED.md has been ruled on by Duho and must stop
        # asking for a decision (2026-08-21). Nothing is deleted; the lane and
        # its artifacts stay on disk, they simply leave the board.
        if os.path.exists(os.path.join(lane, "RETIRED.md")):
            continue
        v = latest_verdicts(lane)
        if not v:
            continue
        name = os.path.basename(lane)
        scripts = script_state(lane)
        state, why = derive_state(name, v, running, scripts)
        # HOLD.md: paused by Duho, reversible — unlike RETIRED.md the lane stays
        # visible, it just stops asking anyone for anything (2026-08-21).
        if os.path.exists(os.path.join(lane, "HOLD.md")):
            state, why = "HELD", "on hold by Duho until he says otherwise"
        frozen, mutable = frozen_artifacts(lane)
        rows.append({"lane": name, "verdicts": v, "rounds": len(gate_files(lane)),
                     "frozen": frozen, "mutable": mutable, "scripts": scripts,
                     "checklist": checklist(lane), "state": state, "why": why,
                     "staffed": staffing(lane)[0], "unstaffed": staffing(lane)[1],
                     "last": max(m for *_, m in v)})
    rows.sort(key=lambda r: (r["state"] != "BLOCKED — NOT QUEUED", -r["last"]))
    return rows


def shelf():
    out = []
    for pdf in sorted(glob.glob(os.path.join(STUDIES, "*.pdf"))):
        slug = os.path.basename(pdf)[:-4]
        out.append({"slug": slug,
                    "history": os.path.exists(os.path.join(STUDIES, f"{slug}_history.json")),
                    "referee": os.path.exists(os.path.join(STUDIES, f"{slug}_review_loop.md")),
                    "video": os.path.exists(os.path.join(VIDEOS, f"{slug}.mp4"))})
    return out


def as_text(rows, papers, crew, interactive):
    L = [f"NebulaMind — autonomous run status   {time.strftime('%Y-%m-%d %H:%M %Z')}", ""]
    seats = {s for s, _ in SEAT_MATCH}
    idle = sorted(seats - {c["seat"] for c in crew})
    L.append("CREW — seats working on a dispatched job")
    if crew:
        for c in crew:
            L.append(f"    {c['seat']:6s} WORKING  {c['elapsed']:>9s} elapsed, {c['cpu']:>9s} cpu")
    else:
        L.append("    no seat is working a dispatched job")
    L.append(f"    idle: {', '.join(idle) if idle else 'none'}"
             + ("   <-- idle seats beside a blocked lane is the A2 failure" if idle else ""))
    if interactive:
        L.append("    (interactive sessions, NOT staffed work: "
                 + ", ".join(f"{c['seat']} pid {c['pid']} {c['elapsed']}" for c in interactive) + ")")
    L.append("")
    for r in rows:
        L.append(f"[{r['state']}]  {r['lane']}")
        L.append(f"    {r['why']}")
        for fam, v, f, _ in r["verdicts"][:4]:
            L.append(f"    · {fam}: {v}   ({f})")
        if r["frozen"]:
            L.append(f"    frozen: {', '.join(r['frozen'])}")
        if r["mutable"]:
            L.append(f"    mutable: {', '.join(r['mutable'])}")
        for s in r["scripts"]:
            L.append(f"    script {s['file']}: {s['state']}")
        if r["unstaffed"]:
            L.append(f"    ROLE_TABLE_BLOCKER — unstaffed: {', '.join(r['unstaffed'])}"
                     f"   (staffed: {', '.join(r['staffed']) or 'none'})")
        c = r["checklist"]
        if c:
            L.append(f"    stages: {c['done']}/{c['total']} done"
                     + (f"; blocked: {', '.join(c['blocked'])}" if c["blocked"] else ""))
        L.append("")
    L.append("Shelf — provenance and video per study:")
    for p in papers:
        miss = [k for k in ("history", "referee") if not p[k]]
        flag = f"   MISSING: {', '.join(miss)}" if miss else ""
        L.append(f"    {'video' if p['video'] else '  —  '}  {p['slug']}{flag}")
    return "\n".join(L)


def as_html(rows, papers):
    css = """body{background:#0b0f1a;color:#e9eef7;font:15px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;margin:0;padding:32px}
h1{font-size:22px;margin:0 0 4px}.sub{color:#8b98ae;font-size:13px;margin-bottom:28px}
.lane{border:1px solid #1e2637;border-radius:10px;padding:16px 18px;margin-bottom:14px;background:#0e1420}
.lane.blocked{border-color:#a8622f;background:#160f0b}.lane.running{border-color:#2f6fa8}
.st{display:inline-block;font-size:11px;letter-spacing:.06em;padding:3px 9px;border-radius:20px;
background:#1e2637;color:#a9b6cc;margin-right:10px;vertical-align:2px}
.st.blocked{background:#a8622f;color:#fff}.st.running{background:#2f6fa8;color:#fff}
.nm{font-weight:600}.why{color:#8b98ae;font-size:13px;margin:8px 0 12px}
.v{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;color:#a9b6cc}
.v b{color:#e9eef7;font-weight:600}.meta{color:#6b7789;font-size:12px}
table{border-collapse:collapse;width:100%;margin-top:8px}td{padding:4px 10px 4px 0;font-size:13px;color:#a9b6cc}
.miss{color:#d69a66}.ok{color:#7fb27f}
@media (prefers-color-scheme: light){body{background:#fff;color:#111}.lane{background:#fafbfc;border-color:#dde3ec}
.lane.blocked{background:#fdf6f0}.why,.v{color:#5a6779}.v b{color:#111}}"""
    h = [f"<style>{css}</style>", "<h1>NebulaMind — autonomous run status</h1>",
         f"<div class=sub>derived from artifacts on disk · {time.strftime('%Y-%m-%d %H:%M %Z')} · "
         "a lane reading BLOCKED — NOT QUEUED has edits owed and nothing running</div>"]
    for r in rows:
        cls = "blocked" if r["state"].startswith("BLOCKED") else ("running" if r["state"] == "RUNNING" else "")
        h.append(f"<div class='lane {cls}'><span class='st {cls}'>{r['state']}</span>"
                 f"<span class=nm>{r['lane']}</span><div class=why>{r['why']}</div><div class=v>")
        for fam, v, f, _ in r["verdicts"][:4]:
            h.append(f"{fam}: <b>{v}</b> &nbsp;<span style='opacity:.6'>{f}</span><br>")
        if r["frozen"]:
            h.append(f"frozen: <b>{', '.join(r['frozen'])}</b><br>")
        for s in r["scripts"]:
            h.append(f"{s['file']}: <b>{s['state']}</b><br>")
        c = r["checklist"]
        if c:
            h.append(f"stages: <b>{c['done']}/{c['total']}</b><br>")
        h.append("</div></div>")
    h.append("<h1 style='font-size:17px;margin-top:30px'>Shelf</h1><table>")
    for p in papers:
        miss = [k for k in ("history", "referee") if not p[k]]
        h.append(f"<tr><td>{'🎬' if p['video'] else ''}</td><td>{p['slug']}</td>"
                 f"<td class='{'miss' if miss else 'ok'}'>"
                 f"{('missing ' + ', '.join(miss)) if miss else 'provenance complete'}</td></tr>")
    h.append("</table>")
    return "\n".join(h)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", help="write a standalone HTML page here")
    a = ap.parse_args()
    rows, papers = collect(), shelf()
    crew, interactive = crew_live()
    print(as_text(rows, papers, crew, interactive))
    if a.html:
        open(a.html, "w").write(as_html(rows, papers))
        print(f"\nhtml -> {a.html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
