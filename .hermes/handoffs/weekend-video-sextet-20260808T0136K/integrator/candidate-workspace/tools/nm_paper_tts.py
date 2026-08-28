#!/usr/bin/env python3
"""nm_paper_tts.py — cut a paper video's narration tracks with edge-tts.

Why this exists: the managed Nous/OpenAI TTS route that produced the original `alloy` tracks needs
an active Nous subscription, and that account is on a free tier with $0.00 usable (and the Tool
Gateway separately disabled). Duho, 2026-08-08: "use edge-tts for the videos this weekend."
edge-tts needs no key and no subscription.

Two parameters are NOT free choices and are defaulted here so nobody has to rediscover them:

1. **rate `+25%`.** edge-tts at its default rate reads 20-28% slower than the alloy tracks it
   replaces — 19.7 s vs 15.59 s on the same script. `nm_paper_narrate.py` holds each card for the
   length of its audio (the storyboard's `seconds` is a floor, not the duration), so the default
   rate silently stretches a 15-card cut by about a minute. At +25% the same script lands within
   0.03 s of the original. Change this and the pacing drifts.

2. **script = heading + body.** Verified by transcribing existing tracks, not assumed. Narration
   reads the card heading first, then the body — so ANY heading edit forces that card's recut.

Output is mono MP3 24 kHz ~48 kb/s, which matches the previous tracks, so the muxer needs no
change. An existing track set is moved aside into a timestamped backup before anything is written;
this never overwrites in place.

Usage:
  nm_paper_tts.py <storyboard.json> [--dry-run] [--only 2,3,14] [--voice V] [--rate R]
Then mux with: nm_paper_narrate.py <storyboard.json>
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta

VIDEOS = "/Users/duhokim/HermesOps/cockpit/videos"
HERMES_PY = "/Users/duhokim/.hermes/hermes-agent/venv/bin/python"

# TWO ENGINES, and the default is the one that keeps the channel consistent.
#
# `nous` — OpenAI `gpt-4o-mini-tts`, voice `alloy`, through the managed Nous gateway. This is what
# the channel's other videos use, so it is the default whenever the account can pay for it.
# Requires Nous credits; returns 403 SUBSCRIPTION_REQUIRED when the balance is dry.
#
# `edge` — edge-tts, no key and no subscription. The fallback that kept video moving on 2026-08-07
# while Nous was at $0.00. Cannot reproduce `alloy`, so switching engines means recutting the WHOLE
# deck, never a few cards, or the voice changes partway through the video.
ENGINE = "nous"
NOUS_MODEL, NOUS_VOICE = "gpt-4o-mini-tts", "alloy"
# CALIBRATED, not a guess. gpt-4o-mini-tts at speed 1.0 reads ~18.5s where the channel's shipped
# alloy track for the identical script is 15.59s — the original set was cut faster than default.
# Measured 2026-08-08 on that script: 1.0->18.46s, 1.15->15.10s, 1.19->16.03s, 1.25->14.66s.
# TTS timing varies ~+/-0.5s run to run, so 1.18 is the centre of the bracket that reproduces the
# channel's pacing rather than an exact-match constant. Drop this to 1.0 and every video grows ~19%.
NOUS_SPEED = 1.18
EDGE_VOICE = "en-US-AndrewMultilingualNeural"   # Duho's pick on a blind A/B, 2026-08-07
EDGE_RATE = "+25%"                              # pacing-critical, not cosmetic — see below


def script_for(card: dict) -> str:
    """Heading, then body — the convention the existing tracks were cut with."""
    h = (card.get("heading") or "").strip()
    b = (card.get("body") or "").strip()
    if h and h[-1] not in ".!?":
        h += "."
    return f"{h} {b}".strip()


def duration(path: str) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def kst_stamp() -> str:
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=9))).strftime("%Y%m%dT%H%M")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("storyboard")
    ap.add_argument("--engine", choices=("nous", "edge"), default=ENGINE)
    ap.add_argument("--voice", help="default: alloy (nous) / Andrew (edge)")
    ap.add_argument("--rate", default=EDGE_RATE, help="edge only; ignored for nous")
    ap.add_argument("--speed", type=float, default=NOUS_SPEED, help="nous only; ignored for edge")
    ap.add_argument("--only", help="1-indexed card numbers to cut, e.g. 2,3,14 (default: all)")
    ap.add_argument("--dry-run", action="store_true", help="print the scripts, synthesise nothing")
    a = ap.parse_args()

    sb = json.load(open(a.storyboard))
    slug, cards = sb["slug"], sb["cards"]
    only = {int(x) for x in a.only.split(",")} if a.only else None
    adir = os.path.join(VIDEOS, f"_audio_{slug}")

    if a.dry_run:
        print(f"{slug}: {len(cards)} cards · voice={a.voice} · rate={a.rate}")
        for i, c in enumerate(cards, 1):
            if only and i not in only:
                continue
            s = script_for(c)
            print(f"  {i:02d}  hold={c.get('seconds', '?')}s  {len(s.split())} words")
            print(f"      {s[:150]}{'…' if len(s) > 150 else ''}")
        return 0

    synth = None
    if a.engine == "nous":
        voice = a.voice or NOUS_VOICE
        # The gateway resolver lives in the Hermes tree and needs Python 3.10+ syntax, while this
        # repo runs on system 3.9 — importing it in-process dies on `str | object`. Shelling out to
        # the Hermes venv keeps the credential inside that process; no token is ever read here.
        if not os.path.exists(HERMES_PY):
            print(f"hermes venv python not found at {HERMES_PY}; "
                  f"re-run with --engine edge for the no-key fallback", file=sys.stderr)
            return 2

        def synth(text: str, out: str) -> None:
            code = (
                "import sys,json,urllib.request\n"
                "sys.path.insert(0,'/Users/duhokim/.hermes/hermes-agent')\n"
                "from tools.managed_tool_gateway import resolve_managed_tool_gateway\n"
                "g=resolve_managed_tool_gateway('openai-audio')\n"
                "text=json.load(sys.stdin)['text']\n"
                f"body=json.dumps({{'model':{NOUS_MODEL!r},'voice':{voice!r},'input':text,'speed':{a.speed!r}}}).encode()\n"
                "r=urllib.request.Request(g.gateway_origin.rstrip('/')+'/v1/audio/speech',"
                "data=body,method='POST')\n"
                "r.add_header('Authorization','Bearer '+g.nous_user_token)\n"
                "r.add_header('Content-Type','application/json')\n"
                f"open({out!r},'wb').write(urllib.request.urlopen(r,timeout=120).read())\n"
            )
            p = subprocess.run([HERMES_PY, "-c", code], input=json.dumps({"text": text}),
                               text=True, capture_output=True)
            if p.returncode != 0:
                raise RuntimeError(f"nous tts failed: {p.stderr.strip()[-300:]}")
    else:
        voice = a.voice or EDGE_VOICE
        try:
            import edge_tts
        except ImportError:
            print("edge_tts not installed (pip install edge-tts)", file=sys.stderr)
            return 2

        def synth(text: str, out: str) -> None:
            asyncio.run(edge_tts.Communicate(text, voice, rate=a.rate).save(out))

    os.makedirs(adir, exist_ok=True)
    # Never overwrite a working track set in place: a bad run would otherwise destroy the only
    # copy of narration that took a subscription to produce.
    # Back up exactly the tracks this run would overwrite — including under --only, where a
    # targeted recut is otherwise the easiest way to lose a good take with no copy anywhere.
    will_write = {f"{i:02d}.mp3" for i in range(1, len(cards) + 1) if not only or i in only}
    existing = sorted(f for f in os.listdir(adir)
                      if f[:2].isdigit() and f.endswith(".mp3") and f in will_write)
    if existing:
        bdir = os.path.join(adir, f"_backup_{kst_stamp()}")
        os.makedirs(bdir, exist_ok=True)
        for f in existing:
            shutil.copy2(os.path.join(adir, f), os.path.join(bdir, f))
        print(f"backed up {len(existing)} track(s) about to be replaced -> {os.path.basename(bdir)}")

    def synth_checked(text: str, out: str) -> None:
        """Synthesise, then PROVE the file is audio before accepting it.

        The gateway can return 200 with an empty body: on 2026-08-08 that wrote a 0-byte 08.mp3
        for the c41-uvlf lane, which the muxer only surfaced much later as an opaque
        "Invalid data found when processing input". A silent empty write is worse than a loud
        failure, so validate here and retry once."""
        for attempt in (1, 2):
            if os.path.exists(out):
                os.remove(out)
            synth(text, out)
            if os.path.exists(out) and os.path.getsize(out) > 0 and duration(out) > 0:
                return
            if attempt == 1:
                print(f"      empty/invalid audio, retrying once", file=sys.stderr)
                time.sleep(2)
        raise RuntimeError(f"{os.path.basename(out)}: engine returned no usable audio after 2 tries")

    total = 0.0
    print(f"{slug}: engine={a.engine} voice={voice}" + (f" rate={a.rate}" if a.engine == "edge" else f" speed={a.speed}"))
    for i, c in enumerate(cards, 1):
        if only and i not in only:
            continue
        out = os.path.join(adir, f"{i:02d}.mp3")
        synth_checked(script_for(c), out)
        d = duration(out)
        total += d
        over = d - c.get("seconds", 0)
        flag = "" if over <= 0 else f"  (over hold by {over:.1f}s — card will stretch)"
        print(f"  {i:02d}  {d:6.2f}s  {c.get('heading', '')[:44]}{flag}")
    print(f"{slug}: {total:.1f}s of narration written to {adir}")
    print("next: nm_paper_narrate.py <storyboard.json>   (renders through the numeric-source guard)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
