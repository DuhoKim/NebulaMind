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
from datetime import datetime, timezone, timedelta

VIDEOS = "/Users/duhokim/HermesOps/cockpit/videos"
VOICE = "en-US-AndrewMultilingualNeural"   # Duho picked this over alloy on a blind A/B, 2026-08-07
RATE = "+25%"                              # see docstring — pacing-critical, not cosmetic


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
    ap.add_argument("--voice", default=VOICE)
    ap.add_argument("--rate", default=RATE)
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

    try:
        import edge_tts
    except ImportError:
        print("edge_tts not installed (pip install edge-tts)", file=sys.stderr)
        return 2

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

    async def run() -> float:
        total = 0.0
        for i, c in enumerate(cards, 1):
            if only and i not in only:
                continue
            out = os.path.join(adir, f"{i:02d}.mp3")
            await edge_tts.Communicate(script_for(c), a.voice, rate=a.rate).save(out)
            d = duration(out)
            total += d
            flag = "" if d <= c.get("seconds", 0) else f"  (over hold by {d - c.get('seconds', 0):.1f}s — card will stretch)"
            print(f"  {i:02d}  {d:6.2f}s  {c.get('heading', '')[:44]}{flag}")
        return total

    total = asyncio.run(run())
    print(f"{slug}: {total:.1f}s of narration written to {adir}")
    print("next: nm_paper_narrate.py <storyboard.json>   (renders through the numeric-source guard)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
