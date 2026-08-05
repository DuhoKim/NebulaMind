#!/usr/bin/env python3
"""nm_workflow_advance.py — advance a lane's WORKFLOW_CHECKLIST from artifacts on disk.

Duho, 2026-08-06, on learning the merged paper workflow was a spec and a record format rather
than an executing pipeline: "start with the auto-advancing checklists".

The rule this tool exists to enforce: **a stage advances only on evidence, and the evidence is
recorded**. That is the same discipline the lanes themselves run on — no lane types a result, so
no checklist claims a stage without naming the artifact that proves it. A stage with no detector
stays untouched and is reported as undetectable rather than quietly assumed done.

Each stage may carry an `evidence` block:

    "evidence": {
      "files":    ["SPIN_PARITY_CONTRACT_V1.md"],        # all must exist
      "frozen":   ["SPIN_PARITY_CONTRACT_V1.md"],        # all must exist AND be read-only (444)
      "glob":     "KUN_*GATE*.md",                       # at least one match must exist
      "contains": {"file": "T1_FUNNEL.json", "pattern": "\"status\":\\s*\"DONE\""},
      "verdict":  {"glob": "*GATE*.md", "pattern": "PASS|APPROVED"},
      "blocked_if": {"glob": "*GATE*.md", "pattern": "FAIL|REJECTED"}
    }

Every present key must pass. `blocked_if` wins over everything: a stage whose gate said FAIL is
reported `blocked`, never `done`.

Safety properties, deliberate:
  - Never downgrades a human-set state silently. A disagreement is reported and, without
    --apply-downgrades, left as the human set it.
  - Never invents a stage, never reorders, never edits `done_means`.
  - --dry-run (default) prints what would change and writes nothing.

Usage:
  nm_workflow_advance.py                 # survey every lane, dry run
  nm_workflow_advance.py --apply         # write the advances
  nm_workflow_advance.py --lane <dir>    # one lane
"""
import argparse, glob as globmod, json, os, re, stat, sys

ROOT = "/Users/duhokim/NebulaMind/NebulaMind"
HANDOFFS = os.path.join(ROOT, ".hermes", "handoffs")
CHECKLIST = "WORKFLOW_CHECKLIST.json"
# Terminal human judgments: a seat decided something the disk cannot express. Never overwritten.
TERMINAL_HUMAN = {"skipped", "done_with_blocker", "blocked"}
# Progress ordering. The tool may move a stage FORWARD on evidence, never backward: disk evidence
# cannot distinguish "not started" from "a seat is working on it right now", so demoting
# running -> pending would destroy information the tool cannot regenerate. Advancing
# running -> done on a recorded verdict is a different thing, and is allowed.
RANK = {"pending": 0, "running": 1, "in_progress": 1, "done": 2, "blocked": 3}


def find_lanes(lane=None):
    if lane:
        p = lane if os.path.isabs(lane) else os.path.join(HANDOFFS, lane)
        return [p] if os.path.exists(os.path.join(p, CHECKLIST)) else []
    return sorted(os.path.dirname(p) for p in
                  globmod.glob(os.path.join(HANDOFFS, "**", CHECKLIST), recursive=True))


def _read(path, cap=400_000):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read(cap)
    except OSError:
        return ""


def evaluate(lane, ev):
    """Return (verdict, [evidence strings], [reasons unmet]). verdict in done|blocked|pending."""
    seen, unmet = [], []

    for name in ev.get("files", []):
        p = os.path.join(lane, name)
        if os.path.exists(p):
            seen.append(f"exists {name} ({os.path.getsize(p)}B)")
        else:
            unmet.append(f"missing {name}")

    for name in ev.get("frozen", []):
        p = os.path.join(lane, name)
        if not os.path.exists(p):
            unmet.append(f"missing {name}"); continue
        mode = stat.S_IMODE(os.stat(p).st_mode)
        if mode & 0o222:                      # any write bit set => not frozen
            unmet.append(f"{name} not frozen (mode {oct(mode)})")
        else:
            seen.append(f"frozen {name} (mode {oct(mode)})")

    g = ev.get("glob")
    if g:
        hits = globmod.glob(os.path.join(lane, g))
        if hits:
            seen.append(f"glob {g} -> {os.path.basename(hits[0])}")
        else:
            unmet.append(f"no match for {g}")

    c = ev.get("contains")
    if c:
        body = _read(os.path.join(lane, c["file"]))
        if body and re.search(c["pattern"], body):
            seen.append(f"{c['file']} matches /{c['pattern'][:40]}/")
        else:
            unmet.append(f"{c['file']} lacks /{c['pattern'][:40]}/")

    # blocked_if is checked before verdict: an explicit FAIL outranks any other evidence
    b = ev.get("blocked_if")
    if b:
        for p in globmod.glob(os.path.join(lane, b["glob"])):
            m = re.search(b["pattern"], _read(p))
            if m:
                return "blocked", seen + [f"{os.path.basename(p)} says {m.group(0)}"], []

    v = ev.get("verdict")
    if v:
        hit = None
        for p in globmod.glob(os.path.join(lane, v["glob"])):
            m = re.search(v["pattern"], _read(p))
            if m:
                hit = f"{os.path.basename(p)} says {m.group(0)}"; break
        if hit:
            seen.append(hit)
        else:
            unmet.append(f"no {v['glob']} carrying /{v['pattern'][:30]}/")

    return ("done" if not unmet else "pending"), seen, unmet


def run(lane, apply_changes, apply_downgrades):
    path = os.path.join(lane, CHECKLIST)
    data = json.load(open(path))
    name = os.path.basename(lane)
    changes, conflicts, undetectable = [], [], 0

    for st in data.get("stages", []):
        ev = st.get("evidence")
        if not ev:
            undetectable += 1
            continue
        verdict, seen, unmet = evaluate(lane, ev)
        cur = st.get("state") or "pending"
        if verdict == cur:
            st["evidence_seen"] = seen
            continue
        # a terminal human judgment is never silently overwritten
        if cur in TERMINAL_HUMAN and not apply_downgrades:
            conflicts.append(f"    ! {st['stage']}: disk says {verdict}, human set {cur} — kept")
            continue
        # forward on evidence, never backward
        if RANK.get(verdict, 0) < RANK.get(cur, 0) and not apply_downgrades:
            why = unmet[0] if unmet else "evidence absent"
            conflicts.append(f"    ! {st['stage']}: {cur} -> {verdict} is a regression ({why}) — kept")
            continue
        changes.append((st, cur, verdict, seen))

    print(f"\n{name}")
    if not changes and not conflicts:
        print(f"    no change ({undetectable} stages have no detector)")
    for st, cur, new, seen in changes:
        print(f"    {cur:18s} -> {new:8s}  {st['stage']}")
        for s in seen[:3]:
            print(f"        via {s}")
    for c in conflicts:
        print(c)
    if undetectable and (changes or conflicts):
        print(f"    ({undetectable} stages have no detector and were not touched)")

    if apply_changes and changes:
        for st, cur, new, seen in changes:
            st["state"] = new
            st["evidence_seen"] = seen
            st["advanced_by"] = "nm_workflow_advance"
        json.dump(data, open(path, "w"), indent=1, ensure_ascii=False)
        print(f"    written: {len(changes)} stage(s)")
    return len(changes), len(conflicts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane")
    ap.add_argument("--apply", action="store_true", help="write changes (default is dry run)")
    ap.add_argument("--apply-downgrades", action="store_true",
                    help="also overwrite human-set states and done->pending regressions")
    a = ap.parse_args()

    lanes = find_lanes(a.lane)
    if not lanes:
        print("no lanes with a checklist found"); return 1
    tot_c = tot_x = 0
    for lane in lanes:
        c, x = run(lane, a.apply, a.apply_downgrades)
        tot_c += c; tot_x += x
    print(f"\n{len(lanes)} lane(s): {tot_c} advance(s), {tot_x} conflict(s)"
          + ("" if a.apply else "  [dry run — rerun with --apply to write]"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
