#!/usr/bin/env python3
"""PREREG COUNTS — emit §7's slot counts from the table instead of asserting them in prose.

WHY THIS EXISTS
---------------
Blanc, 2026-08-28, with the evidence:

    §7 stated class-E count, per draft:  V18=8  V19=8  V20=8  V21=8  V22=7  V23=8

    That invariant was closed at V18 by admitting the eighth row. It held for four drafts, broke at
    V22, and V23 repaired it again. A closed thing reopened.

It reopened because a human types the number and a table holds the truth. Every row insertion is a
chance for them to part, and the §7 count parted three separate ways in one night: V16 undercounted
class E, V21 undercounted class P after the VOID row arrived, and V22 undercounted class E because
I misread my own linter and instructed the change.

A linter that *verifies* a typed number still leaves the number typed. This writes it.

    python3 tools/prereg_counts.py <draft.md>            # report what the sentence should say
    python3 tools/prereg_counts.py <draft.md> --write    # rewrite it to match the table

Idempotent: running it twice changes nothing the second time. Exit 0 if already correct or
successfully written, 1 if the count sentence could not be located.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prereg_lint import count_rows, slot_rows  # noqa: E402

_NUM_WORD = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
    9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
}

# The two count claims §7 makes about itself. Group 1 is the number to replace.
CLAIMS = [
    ("P", re.compile(r"(?<=of )([a-z]+|\d+)(?= class-P slots)", re.I), lambda n: _NUM_WORD.get(n, str(n))),
    ("E", re.compile(r"(?<=are )([a-z]+|\d+)(?= class-E slots)", re.I), lambda n: str(n)),
]


def filled_slots(text):
    """Slots the §7 table marks as filled — reported, never rewritten.

    The count of filled slots is a claim about receipts existing on disk, not about the table's
    shape. This tool will not invent it; it only reports what the prose says so a human can see it
    beside the computed totals.
    """
    m = re.search(r"class-P slots (?:is|are) filled \(([^)]*)\)", text)
    return m.group(1) if m else None


_CITES_VERSION = re.compile(r"\bV\d+\s+lines?\b")


def rewrite(text):
    """Return (new_text, changes). Each change is (class, was, now).

    Operates per block and SKIPS blocks that cite another version by number. The fold record quotes
    V15's stale "One of twelve class-P slots" on purpose; rewriting it would edit the document's
    account of its own history into a lie — the same class of damage this tool exists to prevent.

    The first version of this function had that bug. It is the fourth time in one night that a check
    of mine has treated a quotation as an assertion, so the exclusion lives here explicitly rather
    than being assumed.

    Blockquotes are NOT excluded: §7 states its live count inside one.
    """
    actual = count_rows(text)
    changes, out_blocks = [], []
    # Split on blank lines, preserving them, so reassembly is byte-exact.
    parts = re.split(r"(\n\s*\n)", text)
    for part in parts:
        if _CITES_VERSION.search(part):
            out_blocks.append(part)
            continue
        new = part
        for cls, pat, fmt in CLAIMS:
            want = fmt(actual[cls])
            for m in list(pat.finditer(new)):
                if m.group(1).lower() != want.lower():
                    changes.append((cls, m.group(1), want))
            new = pat.sub(want, new)
        out_blocks.append(new)
    return "".join(out_blocks), changes


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("draft")
    ap.add_argument("--write", action="store_true", help="rewrite the sentence in place")
    args = ap.parse_args()

    path = Path(args.draft)
    text = path.read_text()
    actual = count_rows(text)
    ids = slot_rows(text)

    print(f"prereg counts — {path.name}")
    print(f"  computed from the table: {actual['P']} class P, {actual['E']} class E "
          f"({len(ids)} rows carry a BS- identifier)")
    filled = filled_slots(text)
    if filled:
        print(f"  prose says filled: {filled}  (not computed — a claim about receipts, not rows)")

    new, changes = rewrite(text)
    if not re.search(r"class-[PE] slots", text):
        print("  ERROR: no §7 count sentence found; nothing to emit into")
        return 1
    if not changes:
        print("  prose already matches the table")
        return 0
    for cls, was, now in changes:
        print(f"  class-{cls}: prose said {was}, table has {now}")
    if args.write:
        path.write_text(new)
        print(f"  WRITTEN — {len(changes)} claim(s) replaced from the table")
    else:
        print("  (run with --write to emit these into the document)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
