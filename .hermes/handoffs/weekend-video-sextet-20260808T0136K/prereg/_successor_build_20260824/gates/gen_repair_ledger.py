#!/usr/bin/env python3
"""REPAIR LEDGER — findings in, dispositions out, diffable (Blanc's order after V101's
process flag: V101 repaired from the relay digest, never enumerated the raw blocks, and its
brief claimed "all answered" — three V100 findings came back unaddressed).

Every finding of round N must carry a disposition for the N+1 build: REPAIRED (with the citing
text expected in the draft/map), DEFERRED (with the reason), or DISPUTED (with the argument).
An undisposed finding exits nonzero. Dispositions are DECLARED here per round — appending them
is the build's first act after reading the RAW blocks, and the brief quotes this ledger instead
of asserting completeness.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (round, seat) -> {finding_number: ("REPAIRED"|"DEFERRED"|"DISPUTED", note)}
DISPOSITIONS = {
    ("V100", "GPT56"): {
        1: ("REPAIRED", "V101 recomputed-head ceremony; V102 rooted launcher/env"),
        2: ("REPAIRED", "V101 schema sync + L08"),
        3: ("REPAIRED", "V101 BS-SI build item"),
        4: ("REPAIRED", "V101 grammar; V102 valued bounds + ndarray contract"),
        5: ("REPAIRED", "V102 count-prefix/duplicates/cut-binding - MISSED by V101, owned"),
    },
    ("V100", "CODEX"): {
        1: ("REPAIRED", "V101 recomputed-head; V102 rooted ceremony"),
        2: ("REPAIRED", "V101 receipt-time stop; V102 termination checkpoint + opening check"),
        3: ("REPAIRED", "V102 key-uniqueness scoped as-of-anchors - MISSED by V101, owned"),
        4: ("REPAIRED", "V102 count-prefix + duplicate refusal - MISSED by V101, owned"),
        5: ("REPAIRED", "V101 grammar; V102 valued bounds"),
        6: ("REPAIRED", "V101 backticked membership; V102 comment stripping - half-missed, owned"),
        7: ("REPAIRED", "V101 trace row inserted"),
    },
    ("V101", "GPT56"): {
        1: ("REPAIRED", "V102 rooted ceremony: printed verifier digest, principal launcher, review body"),
        2: ("REPAIRED", "V102 generated kind set + frozen-v9 exclusions by name"),
        3: ("REPAIRED", "V102 termination checkpoint - drain, append, chain-state refusal"),
        4: ("REPAIRED", "V102 decimal alternation closed per branch"),
        5: ("REPAIRED", "V102 bounds valued as productions"),
        6: ("REPAIRED", "V102 L08 generalized, keyed by first field, control added"),
    },
    ("V101", "CODEX"): {
        1: ("REPAIRED", "V102 rooted ceremony"),
        2: ("REPAIRED", "V102 termination checkpoint drains then appends - atomic by single writer"),
        3: ("REPAIRED", "V102 generated kind set; live untagged preimages enumerated or excluded"),
        4: ("REPAIRED", "V102 count-prefix decimal-ASCII+newline, duplicates refused, cut bound"),
        5: ("REPAIRED", "V102 key-uniqueness scoped as-of-anchors"),
        6: ("REPAIRED", "V102 valued bounds + closed ndarray encoding"),
        7: ("REPAIRED", "V102 L08 generalized + self-test control"),
        8: ("REPAIRED", "V102 comment stripping for membership"),
    },
}

def parse_block(path):
    t = Path(path).read_text()
    m = re.search(r"<!-- FINDINGS-BLOCK v1 -->(.*?)<!-- END FINDINGS-BLOCK -->", t, re.S)
    if not m:
        return None
    return re.findall(r"^F(\d+) \|", m.group(1), re.M)

def main():
    argv = [a for a in sys.argv[1:] if a != "--check"]
    rounds = sorted({r for r, _ in DISPOSITIONS})
    out = ["# REPAIR LEDGER — findings in, dispositions out\n"]
    problems = 0
    for rnd in rounds:
        for seat in ("GPT56", "CODEX"):
            path = HERE / f"{rnd}_WHOLE_REVIEW_{seat}.md"
            nums = parse_block(path) if path.exists() else None
            if nums is None:
                out.append(f"- {rnd}/{seat}: NO BLOCK — cannot audit"); problems += 1; continue
            disp = DISPOSITIONS.get((rnd, seat), {})
            for n in nums:
                d = disp.get(int(n))
                if d is None:
                    out.append(f"- **{rnd}/{seat} F{n}: UNDISPOSED — the V101 failure shape**")
                    problems += 1
                else:
                    out.append(f"- {rnd}/{seat} F{n}: {d[0]} — {d[1]}")
    content = "\n".join(out) + f"\n\n**{problems} undisposed.**\n"
    target = HERE / "REPAIR_LEDGER.md"
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text() == content and problems == 0
        print("repair ledger --check:", "complete and byte-equal" if ok else "UNDISPOSED or drifted")
        return 0 if ok else 1
    target.write_text(content)
    print(f"repair ledger: {problems} undisposed")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
