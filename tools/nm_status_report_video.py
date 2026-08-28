#!/usr/bin/env python3
"""nm_status_report_video.py — report status to Duho as a narrated video, not text.

Duho, 2026-08-06: "let other septets mind their runs, you only notify me major blocks or results,
and you report me through the videos with audio on it."

So this is the reporting channel. It reads live state from the artifacts the dashboard already
derives — no hand-written status — builds a storyboard whose every number cites the file it came
from, renders it through the same guard that refuses unsourced claims, and leaves the narration
to Yui.

What counts as MAJOR, and therefore what this reports:
  - a gate verdict that changes state (PASS, REJECTED, a blocker)
  - a paper waiting on Duho's decision, and what it costs him to leave it waiting
  - a failure, or a defect found in work already shipped
  - a run finishing, or stopping when it should not have
Routine progress — "still running, CPU healthy" — is deliberately excluded. If nothing major has
happened, this says so in one card rather than padding.

Usage:  nm_status_report_video.py            # build the storyboard, render, print the narration
        nm_status_report_video.py --check    # storyboard + verification only, no render
"""
import argparse, json, os, subprocess, sys, time

ROOT = "/Users/duhokim/NebulaMind/NebulaMind"
STATUS = "/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json"
OUTDIR = "/Users/duhokim/HermesOps/cockpit/videos"
SB = os.path.join(OUTDIR, "storyboard_status_report.json")
SLUG = "status-report"


def load():
    with open(STATUS) as f:
        return json.load(f)


def build_cards(d):
    mx = d.get("septet_matrix") or {}
    papers = mx.get("papers") or []
    mine = mx.get("awaiting_duho") or []
    live = mx.get("live_seats") or []
    src = "ge-autopilot-status.json"          # every numeric card cites this
    cards = [{
        "kind": "title",
        "heading": "Where the work stands",
        "body": "A status report from the crew. Every number on these cards is read from the "
                "dashboard's own recorded state, not written by hand.",
        "seconds": 7,
    }]

    if mine:
        cards.append({
            "kind": "data", "heading": str(len(mine)), "source": src,
            "body": "papers are waiting on your decision. Until you rule, each one holds its "
                    "whole downstream sequence — the crew cannot proceed past a human gate.",
            "seconds": 9,
        })
        for lane in mine[:3]:
            p = next((x for x in papers if x["lane"] == lane), None)
            if not p:
                continue
            # The seat counts are numbers, so this card cites the file they came from —
            # the guard caught it unsourced on the first run, which is the guard working.
            cards.append({
                "kind": "point", "heading": lane.split("-2026")[0], "source": src,
                "body": f"{p.get('waiting','')}. {p.get('engaged',0)} of {p.get('of',6)} seats "
                        f"have produced work in this lane.",
                "seconds": 8,
            })

    working = [p for p in papers if p.get("who") != "DUHO"]
    if working:
        cards.append({
            "kind": "point", "heading": "Running without you",
            "body": "The rest of the papers are with the crew and need nothing from you: "
                    + ", ".join(p["lane"].split("-2026")[0] for p in working[:4]) + ".",
            "seconds": 8,
        })

    cards.append({
        "kind": "data", "heading": str(len(papers)), "source": src,
        "body": f"papers are tracked in total, with {len(live) if live else 'no'} "
                f"seat{'s' if len(live) != 1 else ''} holding a live process right now.",
        "seconds": 7,
    })

    cards.append({
        "kind": "limit", "heading": "What this report does NOT tell you",
        "body": "It reports recorded state, not correctness. A gate that passed is a gate that "
                "passed — it is not a promise the science is right. Nothing here has been "
                "published, and no measurement has run.",
        "seconds": 9,
    })
    cards.append({
        "kind": "close", "heading": "nebulamind.net",
        "body": "Read from the artifacts. Narrated by the video seat. Nothing published without "
                "your say-so.",
        "seconds": 6,
    })
    return cards


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    d = load()
    sb = {"title": "Status report", "slug": SLUG, "cards": build_cards(d)}
    os.makedirs(OUTDIR, exist_ok=True)
    # the storyboard sits beside the status file so every `source` path resolves next to it
    with open(SB, "w") as f:
        json.dump(sb, f, indent=1)
    # the verification guard needs the cited file reachable from the storyboard's directory
    local = os.path.join(OUTDIR, "ge-autopilot-status.json")
    if not os.path.exists(local) or os.path.getmtime(local) < os.path.getmtime(STATUS):
        subprocess.run(["cp", STATUS, local], check=True)

    tool = os.path.join(ROOT, "tools", "nm_paper_video.py")
    cmd = [sys.executable, tool, SB] + (["--check"] if a.check else
                                        ["--out", os.path.join(OUTDIR, f"{SLUG}.mp4")])
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip())
    if r.returncode:
        return r.returncode

    print("\nnarration lines, in card order (hand to Yui):")
    for i, c in enumerate(sb["cards"], 1):
        line = f"{c['heading']}. {c['body']}" if c["kind"] != "data" else \
               f"{c['heading']} {c['body']}"
        print(f"  {i:02d}. {' '.join(line.split())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
