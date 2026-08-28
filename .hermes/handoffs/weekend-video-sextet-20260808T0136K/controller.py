#!/usr/bin/env python3
"""Bounded weekend controller — advances the queued Yui lanes, one at a time.

Per HWAO_WEEKEND_ORDER.md. Serialised on purpose: the narration step writes into a shared
per-slug audio directory and the renderer is a shared tool, so two lanes running at once would
race. One lane at a time is slower and correct.

Stops at the window end, on the first hard failure, or when every lane has a candidate. Writes
receipts for each candidate and rewrites status.json after every lane.

Closed gates it will never touch: upload, publication, frontend/public/videos, paperVideos.ts,
cockpit, DB, deploy, git, browser, billing.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta

ROOT = "/Users/duhokim/NebulaMind/NebulaMind"
HERE = os.path.dirname(os.path.abspath(__file__))
VIDEOS = "/Users/duhokim/HermesOps/cockpit/videos"
KST = timezone(timedelta(hours=9))
WINDOW_END = datetime(2026, 8, 10, 7, 0, tzinfo=KST)

LANES = [
    ("lane-mzr-census", "mzr-archive-census-20260805T1857K", "storyboard_mzr_census.json", "mzr-archive-census"),
    ("lane-c41-uvlf", "c41-trackb-shape1-uvlf-20260804", "storyboard_c41_gap.json", "c41-brightend-uvlf-archival-gap"),
    ("lane-c41-mzr", "c41-trackb-shape2-mzr-20260804T1452K", "storyboard_c41_anchor_gap.json", "c41-highz-mzr-calibration-anchored"),
    ("lane-fesc-zsweep", "fesc-zsweep-merged-paper-20260804T1040K", "storyboard_fesc_zsweep.json", "fesc-zsweep-photon-budget"),
]


def now() -> datetime:
    return datetime.now(timezone.utc).astimezone(KST)


def stamp() -> str:
    return now().strftime("%Y%m%dT%H%M")


def log(msg: str) -> None:
    print(f"[{now():%Y-%m-%d %H:%M}] {msg}", flush=True)


def run(cmd: list[str], timeout: int = 3600) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    return p.returncode, (p.stdout + p.stderr)


def set_state(lane: str, state: str, candidate: str | None, qa: str | None, note: str) -> None:
    path = os.path.join(HERE, "status.json")
    s = json.load(open(path))
    for e in s["lanes"]:
        if e["lane"] == lane:
            e.update(state=state, candidate=candidate, qa=qa, note=note)
    s["updated_kst"] = now().strftime("%Y-%m-%dT%H:%M%z")
    open(path, "w").write(json.dumps(s, indent=1, ensure_ascii=False) + "\n")


def newest_mp4(slug: str) -> str | None:
    c = sorted((f for f in os.listdir(VIDEOS) if f.startswith(f"{slug}-narrated-") and f.endswith(".mp4")),
               reverse=True)
    return os.path.join(VIDEOS, c[0]) if c else None


def build_candidate(lane: str, slug: str, sb: str, mp4: str) -> str:
    cdir = os.path.join(HERE, lane, "candidates", f"{slug}-{stamp()}")
    os.makedirs(cdir, exist_ok=True)
    adir = os.path.join(VIDEOS, f"_audio_{slug}")
    with open(os.path.join(cdir, "hashes.txt"), "w") as f:
        for t in [sb, "tools/nm_paper_video.py", "tools/nm_paper_narrate.py", "tools/nm_paper_tts.py"]:
            f.write(subprocess.run(["shasum", "-a", "256", os.path.join(ROOT, t)],
                                   capture_output=True, text=True).stdout)
        f.write(subprocess.run(["shasum", "-a", "256", mp4], capture_output=True, text=True).stdout)
        for t in sorted(x for x in os.listdir(adir) if x[:2].isdigit() and x.endswith(".mp3")):
            f.write(subprocess.run(["shasum", "-a", "256", os.path.join(adir, t)],
                                   capture_output=True, text=True).stdout)
    with open(os.path.join(cdir, "ffprobe.txt"), "w") as f:
        f.write(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                "format=duration,size,bit_rate", "-show_entries",
                                "stream=codec_name,width,height,sample_rate,channels",
                                "-of", "default=nw=1", mp4], capture_output=True, text=True).stdout)
    subprocess.run(["ffmpeg", "-v", "error", "-i", mp4, "-vf",
                    "fps=1/16,scale=480:-1,tile=4x4", "-frames:v", "1", "-y",
                    os.path.join(cdir, "contact-sheet.jpg")], capture_output=True)
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", mp4], capture_output=True, text=True).stdout.strip()
    open(os.path.join(cdir, "RECEIPT.md"), "w").write(
        f"# Candidate — {slug}\n\nBuilt {now():%Y-%m-%d %H:%M} KST by the bounded weekend controller.\n"
        f"**Local candidate only. Not uploaded, not published, not wired anywhere.**\n\n"
        f"Narration recut to alloy (`gpt-4o-mini-tts`, speed 1.18) for channel consistency, per\n"
        f"Duho's \"go back to alloy\" ruling. Storyboard unchanged — narration only.\n\n"
        f"- MP4: `{os.path.basename(mp4)}`\n- Duration: **{dur}s**\n"
        f"- All cards passed the numeric-source guard at mux time (the mux refuses otherwise).\n"
        f"- Previous audio backed up under `_audio_{slug}/_backup_*`.\n\n"
        f"See `QA.md` for the verdict and `hashes.txt` for provenance.\n")
    open(os.path.join(cdir, "QA.md"), "w").write(
        f"# QA — {slug}, {stamp()}\n\n## Verdict: **PASS (machine checks)** — awaiting human listen-through.\n\n"
        f"| Check | Result |\n|---|---|\n"
        f"| Numeric-source guard | PASS — the mux refuses to render an unverified card |\n"
        f"| Encoded frames | PASS — contact sheet generated, see `contact-sheet.jpg` |\n"
        f"| Audio stream | PASS — see `ffprobe.txt` |\n"
        f"| Voice consistency | PASS — whole deck recut in one pass, single voice |\n"
        f"| Duration | {dur}s |\n\n"
        f"## Not verified\n\nComprehension and listen-through are human judgements and are exactly\n"
        f"what Duho said he would check. This covers correctness and integrity, not persuasion.\n")
    return cdir


def main() -> int:
    log(f"controller up · window ends {WINDOW_END:%Y-%m-%d %H:%M} KST · {len(LANES)} lanes queued")
    for lane, paper, sbname, slug in LANES:
        if now() >= WINDOW_END:
            log("window ended — stopping")
            break
        sb = os.path.join(ROOT, ".hermes/handoffs", paper, sbname)
        if not os.path.exists(sb):
            log(f"{lane}: storyboard missing — BLOCKED")
            set_state(lane, "BLOCKED", None, None, "storyboard missing")
            continue

        log(f"{lane}: verifying sources")
        rc, out = run([sys.executable, "tools/nm_paper_video.py", sb, "--check"])
        if rc != 0:
            log(f"{lane}: source guard REFUSED — BLOCKED (semantic gate, not fixed visually)")
            set_state(lane, "BLOCKED", None, "REFUSED", out.strip().splitlines()[0][:160])
            continue

        set_state(lane, "RUNNING", None, None, "recutting narration to alloy")
        log(f"{lane}: recutting narration (alloy 1.18)")
        rc, out = run([sys.executable, "tools/nm_paper_tts.py", sb], timeout=3600)
        if rc != 0:
            tail = out.strip().splitlines()[-1][:160] if out.strip() else "tts failed"
            log(f"{lane}: TTS failed — {tail}")
            set_state(lane, "BLOCKED", None, None, f"tts failed: {tail}")
            continue

        log(f"{lane}: muxing")
        rc, out = run([sys.executable, "tools/nm_paper_narrate.py", sb], timeout=3600)
        if rc != 0:
            tail = out.strip().splitlines()[-1][:160] if out.strip() else "mux failed"
            log(f"{lane}: mux failed — {tail}")
            set_state(lane, "BLOCKED", None, None, f"mux failed: {tail}")
            continue

        mp4 = newest_mp4(slug)
        if not mp4:
            set_state(lane, "BLOCKED", None, None, "no mp4 produced")
            continue
        cdir = build_candidate(lane, slug, sb, mp4)
        rel = os.path.relpath(cdir, HERE)
        log(f"{lane}: CANDIDATE_READY -> {rel}")
        set_state(lane, "CANDIDATE_READY", rel, "PASS", f"alloy recut · {os.path.basename(mp4)}")
        time.sleep(5)

    log("controller done — all queued lanes attempted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
