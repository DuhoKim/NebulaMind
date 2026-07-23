#!/usr/bin/env python3
"""Append a real human interaction to a paper's revision history.

The Lab's per-paper "revision log" (Draft board) is human-interaction only: it
records the researcher's own directions on a draft — what was said and what it
changed — and nothing else. Machine referee / analysis detail stays behind the
"referee" link. A draft with no human input reads as empty, honestly.

USE THIS whenever the researcher's words cause a draft to change: append the real
direction, in their actual words. NEVER invent a step, never attribute a machine
catch to the human. Papers with no human interaction keep an empty record.

  nm_paper_history.py append --file PATH_TO_<slug>_history.json \
      --said "the researcher's words" \
      --changed "what changed in the draft as a result" \
      [--verdict DIRECTION|REVISE|FRAMING] [--by "lead researcher"] [--topic "..."]

The history.json is served statically (a deploy asset), so an append shows up on
the live board immediately — no rebuild. Creates the file if absent.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path


def do_append(a) -> int:
    p = Path(a.file)
    if p.exists():
        doc = json.loads(p.read_text())
    else:
        doc = {"model": "n/a (human-directed)", "lineage": {"topicSource": None, "topic": a.topic},
               "humanFeedback": {"captured": False}, "revisions": []}
    doc.setdefault("humanFeedback", {})["captured"] = True
    if a.topic:
        doc.setdefault("lineage", {})["topic"] = a.topic
    doc.setdefault("revisions", []).append({
        "feedbackSource": "human",
        "feedbackBy": a.by,
        "feedbackKind": {"verdict": a.verdict, "categories": []},
        "feedbackText": a.said,
        "changed": {"summary": a.changed},
    })
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(doc, indent=2) + "\n")
    n = len(doc["revisions"])
    print(f"appended human direction #{n} to {p.name}: {a.said[:60]!r} -> {a.changed[:60]!r}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Append a real human direction to a paper's revision history.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    ap_a = sub.add_parser("append", help="append one human direction")
    ap_a.add_argument("--file", required=True, help="path to <slug>_history.json (a deploy asset)")
    ap_a.add_argument("--said", required=True, help="the researcher's actual words (verbatim / close to it)")
    ap_a.add_argument("--changed", required=True, help="what changed in the draft as a result")
    ap_a.add_argument("--verdict", default="DIRECTION", help="short tag: DIRECTION | REVISE | FRAMING")
    ap_a.add_argument("--by", default="lead researcher", help="who (kept generic unless asked)")
    ap_a.add_argument("--topic", default=None, help="optional topic label for the lineage line")
    a = ap.parse_args()
    if a.cmd == "append":
        return do_append(a)
    return 1


if __name__ == "__main__":
    sys.exit(main())
