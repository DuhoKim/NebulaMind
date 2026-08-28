#!/usr/bin/env python3
"""Bounded autonomous sustainer — Duho away, Hwao coordinating.

Keeps the sextet moving without a human in the loop, and stops rather than improvising:
 - retries a queued dispatch only when a seat's composer is IDLE (never pastes into a busy pane;
   that is the hazard already fixed once in the earlier sustainer)
 - watches for the next candidate MP4 and records it
 - never writes outside this handoff root, never touches cockpit/videos, never uses git
"""
import json, os, subprocess, time
from datetime import datetime, timezone, timedelta

H = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K"
KST = timezone(timedelta(hours=9))
END = datetime(2026, 8, 10, 7, 0, tzinfo=KST)
TMUX = "/opt/homebrew/bin/tmux"
LOG = os.path.join(H, "autonomous_sustainer.log")

QUEUED = {"tori-overhaul": (
    "CONTAINMENT RECHECK (queued retry). All four staged files were moved INTACT out of "
    "cockpit/videos/_weekend-canaries into reviews/tori-overhaul-evidence/hwao-gate-containment-"
    "20260808T1405/; nothing deleted; violating directory gone; authoritative hash 40804f86 "
    "unchanged; my duplicate server on 8098 retired so your 8765 is the single exposure path. "
    "Read reviews/HWAO_GATE_BREACH_CONTAINMENT.md, independently recheck served/shared roots, "
    "hashes and reachability, then append a containment verdict to TORI_OVERHAUL.md preserving "
    "the original HOLD as incident history: PASS, PASS WITH INCIDENT, or still HOLD, and why.")}

def now(): return datetime.now(timezone.utc).astimezone(KST)
def log(m):
    line = f"[{now():%H:%M}] {m}"
    print(line, flush=True)
    open(LOG, "a").write(line + "\n")

def busy(s):
    r = subprocess.run([TMUX, "capture-pane", "-p", "-t", s], capture_output=True, text=True)
    if r.returncode != 0: return None          # session gone
    t = r.stdout
    return any(k in t for k in ("esc to interrupt", "ruminating", "Cogitat", "Booping", "msg=interrupt"))

def send(s, msg):
    subprocess.run([TMUX, "send-keys", "-t", s, "-l", msg], capture_output=True)
    time.sleep(2)
    subprocess.run([TMUX, "send-keys", "-t", s, "Enter"], capture_output=True)

def candidates():
    d = os.path.join(H, "integrator", "canaries")
    out = []
    for n in sorted(os.listdir(d)):
        p = os.path.join(d, n)
        if os.path.isdir(p):
            for f in os.listdir(p):
                if f.endswith(".mp4"): out.append(os.path.join(p, f))
    return out

def main():
    log(f"autonomous sustainer up · window ends {END:%m-%d %H:%M} KST")
    seen = set(candidates())
    log(f"baseline candidates: {len(seen)}")
    while now() < END:
        for s, msg in list(QUEUED.items()):
            b = busy(s)
            if b is None:
                log(f"{s}: session gone — dropping queued dispatch"); QUEUED.pop(s); continue
            if not b:
                send(s, msg); log(f"{s}: queued dispatch delivered"); QUEUED.pop(s)
        cur = set(candidates())
        for new in sorted(cur - seen):
            sz = os.path.getsize(new)
            time.sleep(20)
            if os.path.getsize(new) == sz:
                sha = subprocess.run(["shasum","-a","256",new],capture_output=True,text=True).stdout.split()[0]
                log(f"NEW CANDIDATE STABLE: {os.path.basename(new)} bytes={sz} sha256={sha[:16]}…")
        seen = cur
        time.sleep(90)
    log("window reached — sustainer stopping")

main()
