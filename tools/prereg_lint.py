#!/usr/bin/env python3
"""PREREG LINT — the consistency checks a 650-line promise cannot enforce on itself.

WHY THIS EXISTS
---------------
Blanc, 2026-08-27: "three times yesterday your own change broke your own probe because the test
still pointed at the old shape. The same risk applies to a document — a repair in §5 that leaves
§7 asserting the old behaviour is the identical failure in prose."

That is exactly what happened. V12 renamed the lock receipt and left §7 calling BS-V the lock.
V12 created BS-2a as a class-P prerequisite and filed it under Class E. V14 renumbered a list
into 1,2,3,4,6,7,5. Every one was found by a referee, spending a review round on bookkeeping
that a script can check in a second.

None of these checks judge the science or the promise. They check that the document agrees with
itself, which is the part I keep getting wrong while attending to the part I do not.

    python3 tools/prereg_lint.py <draft.md> [--gates DIR]

Exit 0 clean, 1 if any check fails.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

SLOT = re.compile(r"\bBS-[0-9]+[a-z]?\b|\bBS-[A-Z]\b")


def slot_rows(text):
    """Slot identifiers that have a row in the §7 table, and the class each sits under."""
    rows, cls = {}, None
    for line in text.splitlines():
        if re.match(r"\*\*Class [PE]", line.strip()):
            cls = "P" if "Class P" in line else "E"
        m = re.match(r"\|\s*(BS-[0-9]+[a-z]?|BS-[A-Z])\b", line.strip())
        if m:
            rows[m.group(1)] = cls
    return rows


def check_slots_exist(text, rows, out):
    """Every slot named in prose must have a row in §7 — the V12 BS-2a failure."""
    referenced = {s for s in SLOT.findall(text)}
    missing = sorted(referenced - set(rows))
    if missing:
        out.append(("slots-referenced-but-not-in-table",
                    f"named in prose with no §7 row: {', '.join(missing)}"))


def check_class_agreement(text, rows, out):
    """A slot the prose calls a class-P prerequisite must not sit in Class E."""
    for slot, cls in rows.items():
        claim = re.search(rf"{re.escape(slot)}[^.\n]{{0,120}}class-P", text)
        if claim and cls == "E":
            out.append(("slot-class-disagreement",
                        f"{slot} is called a class-P prerequisite in prose and sits in Class E"))


def check_lock_identity(text, out):
    """After the BS-L split, nothing may still call BS-V the lock — the V12 cycle."""
    # Line-by-line, because a sentence-fragment regex cannot tell whether it began inside a
    # blockquote. Blockquotes are the document's record of its own corrections: they quote the
    # wrong sentence deliberately, so they are history rather than live text.
    for line in text.splitlines():
        if line.lstrip().startswith(">"):
            continue
        for m in re.finditer(r"[^.\n]*BS-V[^.\n]*", line):
            frag = m.group(0)
            if re.search(r"\block\b", frag) and "not the lock" not in frag and "BS-L" not in frag:
                out.append(("lock-identity",
                            f"BS-V described with the lock: …{frag.strip()[:110]}…"))


def check_list_numbering(text, out):
    """Ordered lists must run 1..n in document order — the V14 1,2,3,4,6,7,5."""
    runs, current = [], []
    for line in text.splitlines():
        m = re.match(r"^(\d+)\.\s+\*\*", line)
        if m:
            current.append(int(m.group(1)))
        elif current:
            runs.append(current)
            current = []
    if current:
        runs.append(current)
    for run in runs:
        if len(run) > 2 and run != list(range(run[0], run[0] + len(run))):
            out.append(("list-numbering", f"ordered list runs {run}"))
        dupes = [n for n, c in Counter(run).items() if c > 1]
        if dupes:
            out.append(("list-numbering", f"list repeats item number(s) {dupes}"))


def check_repair_citations(text, gates, out):
    """A 'V## CORRECTION (SEAT-Vn Fk)' claim must cite a finding that exists on disk.

    The document's most dangerous sentence is one announcing a repair, because a reader stops
    checking there. V12's blockquote claimed the unanimous round-1 blinding finding repaired
    while half of it stood.
    """
    if not gates or not gates.is_dir():
        out.append(("repair-citations", "gates directory not readable; citations unchecked"))
        return
    corpus = "\n".join(p.read_text(errors="ignore") for p in gates.glob("PREREG_TEXT*.md"))
    if not corpus:
        return
    for m in re.finditer(r"\((?:KIMI|GPT56|CODEX)[^)]{0,80}\)", text):
        cite = m.group(0)
        for seat, ver, fid in re.findall(r"(KIMI|GPT56|CODEX)-V(\d+)\s*(F?\d+)", cite):
            if f"PREREG_TEXT_V{ver}_{seat}.md" not in [p.name for p in gates.glob("*.md")]:
                out.append(("repair-citations",
                            f"cites {seat}-V{ver} {fid} but no PREREG_TEXT_V{ver}_{seat}.md exists"))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("draft")
    ap.add_argument("--gates", default="")
    args = ap.parse_args()
    text = Path(args.draft).read_text()
    gates = Path(args.gates) if args.gates else Path(args.draft).parent / "gates"

    rows = slot_rows(text)
    out = []
    check_slots_exist(text, rows, out)
    check_class_agreement(text, rows, out)
    check_lock_identity(text, out)
    check_list_numbering(text, out)
    check_repair_citations(text, gates, out)

    print(f"prereg lint — {Path(args.draft).name}")
    print(f"  §7 slot rows found: {len(rows)} "
          f"({sum(1 for c in rows.values() if c == 'P')} class P, "
          f"{sum(1 for c in rows.values() if c == 'E')} class E)")
    if not out:
        print("  no inconsistencies found")
        return 0
    for kind, msg in out:
        print(f"  [{kind}] {msg}")
    print(f"  {len(out)} finding(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
