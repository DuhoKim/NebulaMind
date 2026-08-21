#!/usr/bin/env python3
"""Verify that gate-state claims spoken in audio were TRUE when spoken.

The companion to a numeric disclosure sweep. A number is sensitive if its artifact
has not passed its gate; a phrase is sensitive if the gate state it asserts did not
hold at the moment it was spoken. Same join, different column.

    "Phase 2 is closed: 4 gates, 4 passes"  spoken 2026-08-20 18:48
      -> did four PASS_ tokens exist on disk at 18:48 that day?

EVIDENCE, in order of strength:
  1. git first-appearance (`--diff-filter=A`) — survives history rewrites of content,
     though not of history itself;
  2. filesystem mtime — WEAK, and flagged as such. A git checkout rewrites mtimes: on
     this repo many gate files share an 08-20 23:36 stamp from a history cleanup, which
     is not when they were written. Never trust mtime alone to date a gate.

A claim we cannot date is reported UNVERIFIABLE, never TRUE. Silence is not a pass.

KNOWN LIMIT, stated because a detector's blind spot belongs beside its findings:
this counts PASS tokens lane-wide, so it answers "did at least N passes exist when
this was spoken?" — necessary, not sufficient. It would catch a reading claiming
four passes before any gate had run. It would NOT catch a reading claiming the
wrong four. Scoping a claim to the specific gates it means needs a phase key the
transcripts do not carry; until they do, a TRUE here means "not impossible", not
"verified". Do not read it as more than that.
"""
from __future__ import annotations
import re, subprocess, sys, pathlib, datetime as dt

LANE = pathlib.Path(__file__).resolve().parent
AUDIO = pathlib.Path("/Users/duhokim/HermesOps/reports/status-audio")
KST = dt.timezone(dt.timedelta(hours=9))
VERDICT = re.compile(r"^(PASS|HOLD)_[A-Z0-9_]+", re.I)
CLAIM = re.compile(r"(\d+)\s+gates?,\s*(\d+)\s+passe?s?", re.I)


def git_first_seen(p: pathlib.Path):
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%aI", "--", str(p)],
            cwd=str(p.parent), capture_output=True, text=True, timeout=20).stdout.strip()
        if out:
            return dt.datetime.fromisoformat(out.splitlines()[-1]), "git"
    except Exception:
        pass
    return None, None


def gates():
    """Every file whose FIRST LINE is a verdict token — the lane's own convention."""
    out = []
    for p in sorted(LANE.rglob("*.md")):
        try:
            first = p.open(errors="replace").readline().strip()
        except OSError:
            continue
        m = VERDICT.match(first)
        if not m:
            continue
        when, how = git_first_seen(p)
        if when is None:
            when, how = dt.datetime.fromtimestamp(p.stat().st_mtime, KST), "mtime(WEAK)"
        out.append({"path": p.relative_to(LANE).as_posix(), "token": first.split()[0],
                    "passing": first.upper().startswith("PASS"), "when": when, "how": how})
    return out


def readings():
    for p in sorted(AUDIO.glob("*tori-report.txt")):
        m = re.match(r"(\d{8})T(\d{6})", p.name)
        if not m:
            continue
        when = dt.datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S").replace(tzinfo=KST)
        yield p, when, p.read_text(errors="replace")


def main():
    g = gates()
    weak = sum(1 for x in g if x["how"].startswith("mtime"))
    print(f"  {len(g)} gate files found; dated by git: {len(g)-weak}, by weak mtime: {weak}\n")
    rows, checked = [], 0
    for p, when, text in readings():
        for m in CLAIM.finditer(text):
            checked += 1
            claimed_gates, claimed_passes = int(m.group(1)), int(m.group(2))
            existed = [x for x in g if x["when"] <= when]
            passes = [x for x in existed if x["passing"]]
            any_weak = any(x["how"].startswith("mtime") for x in existed)
            if any_weak:
                v = "UNVERIFIABLE"
            elif len(passes) >= claimed_passes:
                v = "TRUE(weak)"   # lane-wide count; see KNOWN LIMIT in the docstring
            else:
                v = "FALSE"
            rows.append((p.name[:24], when.strftime("%m-%d %H:%M"),
                         f"{claimed_gates} gates/{claimed_passes} passes", len(passes), v))
    print(f"  {'reading':26}{'spoken':14}{'claim':22}{'PASS on disk':14}verdict")
    for r in rows:
        print(f"  {r[0]:26}{r[1]:14}{r[2]:22}{r[3]:<14}{r[4]}")
    print(f"\n  {checked} gate-state claim(s) checked")
    print("  TRUE(weak) = at least that many passes existed lane-wide; not scoped to the")
    print("  specific gates the claim means. See KNOWN LIMIT in the docstring.")
    bad = [r for r in rows if r[4] == "FALSE"]
    if bad:
        print(f"  FALSE CLAIMS: {len(bad)} — a reading asserted a gate state that did not hold")
        return 1
    unv = [r for r in rows if r[4] == "UNVERIFIABLE"]
    if unv:
        print(f"  {len(unv)} UNVERIFIABLE — gate dates rest on mtimes a checkout may have rewritten.")
        print("  Not a pass. Commit the gate files to date them by git and re-run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
