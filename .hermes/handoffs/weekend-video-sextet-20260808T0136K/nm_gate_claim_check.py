#!/usr/bin/env python3
"""Verify that gate-state claims spoken in audio were TRUE when spoken.

The companion to a numeric disclosure sweep. A number is sensitive if its artifact
has not passed its gate; a phrase is sensitive if the gate state it asserts did not
hold at the moment it was spoken. Same join, different column.

    "Phase 2 is closed: 4 gates, 4 passes"  spoken 2026-08-20 18:48
      -> did four PASS_ tokens exist on disk at 18:48 that day?

WHAT THE DATE MEANS, because getting this wrong makes the tool accuse rather than
report: git first-appearance and mtime are both UPPER bounds — they say the gate
existed BY then, never that it did not exist EARLIER. A gate written on the 19th
and committed on the 21st looks two days young. So a claim whose gates we can only
date after the reading is UNVERIFIABLE, not FALSE. FALSE is reserved for a claim
that exceeds the gates that exist AT ALL, which is the only form we can prove.

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
# Widened 2026-08-21 after measuring the first pattern: it matched 3 of 128 gate
# mentions across the corpus, so a near-empty result was evidence about the regex
# rather than about the audio. Two stages now — match broadly, then CLASSIFY,
# because most gate language is not a claim about a gate's state.
# Allow qualifiers between the two halves: "5 gates SINCE MIDNIGHT, 5 passes" is a
# countable claim and the first version scored it as merely asserted.
CLAIM = re.compile(r"(\d+)\s+gates?\b[^.,]{0,30},?\s*(\d+)\s+passe?s?", re.I)   # countable
GATEISH = re.compile(r"[^.!?]{0,90}\b(?:re-?gates?|gates?|gating|gated)\b[^.!?]{0,90}", re.I)
# A gate's state is ASSERTED (checkable) ...
ASSERTS = re.compile(r"\b(?:passed|passes|held|holds|cleared|is in|came back|returned|"
                     r"went through|survived|failed|reopened|closed)\b", re.I)
# ... unless the sentence is a plan, a condition, or a requirement (not checkable).
HYPOTHETICAL = re.compile(r"\b(?:if|would|should|will|must|need|needs|needed|require[sd]?|"
                          r"add|adding|propose|proposed|plan|before any|until|whether|ask(?:ed)?)\b", re.I)


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


def readings(pattern="*.txt"):
    """Every transcript we can DATE. Two naming families exist: a leading
    YYYYMMDDTHHMMSS stamp (172 files) and an older trailing YYYYMMDDTHHMM (45).
    Undateable files are skipped and COUNTED — an unchecked reading must never
    disappear into a clean total."""
    skipped = []
    for p in sorted(AUDIO.glob(pattern)):
        if p.name.endswith((".deck.json", ".times.json")):
            continue
        m = (re.match(r"(\d{8})T(\d{6})", p.name)
             or re.search(r"(\d{8})T(\d{4})(?!\d)", p.name))
        if not m:
            skipped.append(p.name)
            continue
        stamp = m.group(1) + m.group(2).ljust(6, "0")
        when = dt.datetime.strptime(stamp, "%Y%m%d%H%M%S").replace(tzinfo=KST)
        yield p, when, p.read_text(errors="replace")
    if skipped:
        print(f"  NOTE: {len(skipped)} transcript(s) carry no parseable stamp and were NOT checked:")
        for n in skipped[:6]:
            print(f"     {n}")
        if len(skipped) > 6:
            print(f"     ... and {len(skipped)-6} more")
        print()


def gate_scope(stem: str):
    """The claim's own declaration of which gates it means, if the speaker left one."""
    f = AUDIO / f"{stem}.gates.json"
    if not f.exists():
        return None
    try:
        import json
        return json.loads(f.read_text())
    except Exception:
        return None


def main():
    g = gates()
    weak = sum(1 for x in g if x["how"].startswith("mtime"))
    print(f"  {len(g)} gate files found; dated by git: {len(g)-weak}, by weak mtime: {weak}\n")
    rows, checked = [], 0
    kinds = {"countable": 0, "asserted": 0, "hypothetical": 0, "mention-only": 0}
    asserted_rows = []
    for p, when, text in readings():
        for seg in GATEISH.findall(text):
            if CLAIM.search(seg):
                kinds["countable"] += 1
            elif HYPOTHETICAL.search(seg):
                kinds["hypothetical"] += 1        # a plan or a condition, not a claim
            elif ASSERTS.search(seg):
                kinds["asserted"] += 1            # claims a state, but names no count
                asserted_rows.append((p.name[:34], when.strftime("%m-%d %H:%M"),
                                      re.sub(r"\s+", " ", seg).strip()[:74]))
            else:
                kinds["mention-only"] += 1
        for m in CLAIM.finditer(text):
            checked += 1
            claimed_gates, claimed_passes = int(m.group(1)), int(m.group(2))
            scope = gate_scope(p.name.rsplit(".", 1)[0])
            if scope:
                # SCOPED: resolve against the specific gates the claim names, and require
                # each to have existed when spoken. This is the strong form.
                named = {x["file"] for x in scope["gates"]}
                have = [x for x in g if x["path"] in named]
                undated = [x for x in have if x["how"].startswith("mtime")]
                in_time = [x for x in have if x["when"] <= when and x["passing"]]
                passing_now = [x for x in have if x["passing"]]
                if len(have) != len(named):
                    v = "UNVERIFIABLE"          # a named gate is not discoverable
                elif len(passing_now) < claimed_passes:
                    v = "FALSE"                 # provable: the passes do not exist even now
                elif undated or len(in_time) < claimed_passes:
                    # the gates exist and pass, but our earliest evidence of them postdates
                    # the reading — an upper bound cannot rule the claim out
                    v = "UNVERIFIABLE"
                else:
                    v = "TRUE(reconstructed)" if scope.get("reconstructed") else "TRUE"
                passes = passing_now
            else:
                existed = [x for x in g if x["when"] <= when]
                passes = [x for x in existed if x["passing"]]
                any_weak = any(x["how"].startswith("mtime") for x in existed)
                if any_weak:
                    v = "UNVERIFIABLE"
                elif len(passes) >= claimed_passes:
                    v = "TRUE(weak)"   # lane-wide count; see KNOWN LIMIT in the docstring
                else:
                    v = "FALSE"
            rows.append((p.name[:34], when.strftime("%m-%d %H:%M"),
                         f"{claimed_gates} gates/{claimed_passes} passes", len(passes), v))
    print(f"  {'reading':36}{'spoken':14}{'claim':22}{'PASS':7}verdict")
    for r in rows:
        print(f"  {r[0]:36}{r[1]:14}{r[2]:22}{r[3]:<7}{r[4]}")
    print(f"\n  {checked} COUNTABLE claim(s) checked above")
    print(f"  classification of all {sum(kinds.values())} gate mentions: {kinds}")
    if asserted_rows:
        print(f"\n  {len(asserted_rows)} ASSERTED-but-uncountable claim(s) — a state is claimed,")
        print("  no number is given, so this check cannot verify them. Listed, not passed:")
        for r in asserted_rows[:12]:
            print(f"    {r[0]:36}{r[1]:14}{r[2]}")
        if len(asserted_rows) > 12:
            print(f"    ... and {len(asserted_rows)-12} more")
    print("  FALSE = provable only: the claimed passes do not exist even now.")
    print("  UNVERIFIABLE = our earliest evidence of the gate postdates the reading. Dates are")
    print("  UPPER bounds, so this cannot rule the claim out — and must not be read as doubt.")
    print("  TRUE = the gates the claim NAMES existed and passed when it was spoken.")
    print("  TRUE(reconstructed) = same, but the naming sidecar was written after the audio,")
    print("  so it records what the claim referred to, not what was declared at the time.")
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
