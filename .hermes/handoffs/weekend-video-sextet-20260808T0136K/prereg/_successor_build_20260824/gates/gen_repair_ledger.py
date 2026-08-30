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
    ("V102", "GPT56"): {
        1: ("REPAIRED", "V103 ceremony: pinned build item, acquisition path, check-not-read"),
        2: ("REPAIRED", "V103 T2: DRAIN-OPEN chain state, draining epochs lawful"),
        3: ("REPAIRED", "V103 T1: admission closes at drain-start"),
        4: ("REPAIRED", "V103: new-chain sentence killed, rule is 3c's, T-quotes label-bound"),
        5: ("REPAIRED", "V103 kinds v2: real site enumeration, seeded control + deletion probe"),
        6: ("REPAIRED", "V103 T3 + (ii-f): schemas, registry, kinds, clock pass"),
        7: ("REPAIRED", "V103 ledger v2: block contracts checked, limit stated on its face"),
    },
    ("V102", "CODEX"): {
        1: ("REPAIRED", "V103: draft re-derived from 3c, opposite semantics dead"),
        2: ("REPAIRED", "V103 T2: durable drain intent = the drain-start record"),
        3: ("REPAIRED", "V103 T3 + (ii-f) + registry + clock pass"),
        4: ("REPAIRED", "V103: honest pin (REQUIRED-DOES-NOT-EXIST), acquisition + check contract"),
        5: ("REPAIRED", "V103 kinds v2: registry digest-ref rows are the site enumerator"),
        6: ("REPAIRED", "V103 ledger v2: rounds from directory, contracts, self-test"),
        7: ("REPAIRED", "V103 R08 requires BS-V, deletion control added"),
        8: ("REPAIRED", "V103 bool bytes 0x00/0x01 only"),
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

def parse_block(path_or_text, is_text=False):
    t = path_or_text if is_text else Path(path_or_text).read_text()
    m = re.search(r"<!-- FINDINGS-BLOCK v1 -->(.*?)<!-- END FINDINGS-BLOCK -->", t, re.S)
    if not m:
        return None, "no block"
    body = m.group(1)
    nums = [int(n) for n in re.findall(r"^F(\d+) \|", body, re.M)]
    cm = re.search(r"^COUNT:\s*(\d+)", body, re.M)
    # v2 (CODEX-V102 F6, GPT56-V102 F7): the block CONTRACT is checked, not just numbers -
    # COUNT must equal the F-lines and numbering must be contiguous from 1, else the report
    # itself is the problem and no disposition math is trustworthy over it.
    if not cm or int(cm.group(1)) != len(nums):
        return None, f"COUNT contract broken ({cm and cm.group(1)} vs {len(nums)} lines)"
    if nums != list(range(1, len(nums) + 1)):
        return None, f"non-contiguous findings {nums}"
    return nums, None

def discover_rounds():
    """Rounds come from the DIRECTORY, not the disposition table (CODEX-V102 F6: a table that
    discovers its own coverage cannot notice a round it forgot). Coverage floor: V100, where
    the ledger begins; earlier rounds predate it and are named as out of scope."""
    seen = set()
    for p in HERE.glob("V*_WHOLE_REVIEW_*.md"):
        m = re.match(r"(V\d+)_WHOLE_REVIEW_(GPT56|CODEX)\.md$", p.name)
        if m and int(m.group(1)[1:]) >= 100:
            seen.add(m.group(1))
    return sorted(seen, key=lambda v: int(v[1:]))

def self_test():
    """Standing rule: seeded positive + deletion probe."""
    fails = []
    blk = ("<!-- FINDINGS-BLOCK v1 -->\nSEAT: X\nVERSION: V1\nVERDICT: NOT CLEAR\n"
           "COUNT: 2\nF1 | H | R | a | b\nF2 | H | R | a | b\n<!-- END FINDINGS-BLOCK -->")
    nums, err = parse_block(blk, is_text=True)
    if nums != [1, 2]:
        fails.append(f"well-formed block misparsed: {nums} {err}")
    # SEEDED: a finding with no disposition must be fatal at the accounting layer
    disp = {1: ("REPAIRED", "x")}
    undisposed = [n for n in (nums or []) if n not in disp]
    if undisposed != [2]:
        fails.append(f"seeded undisposed finding not caught: {undisposed}")
    # CONTRACT: COUNT mismatch must refuse the block
    bad = blk.replace("COUNT: 2", "COUNT: 5")
    nums2, err2 = parse_block(bad, is_text=True)
    if nums2 is not None or not err2:
        fails.append("COUNT-broken block accepted")
    # DELETION PROBE: dropping the contiguity rule would accept F1/F3 - assert it refuses
    gap = blk.replace("F2 |", "F3 |")
    nums3, err3 = parse_block(gap, is_text=True)
    if nums3 is not None:
        fails.append("non-contiguous block accepted")
    for f in fails:
        print(f"  FAIL {f}")
    print(f"  self-test: 4 controls, {len(fails)} failure(s)")
    return 1 if fails else 0

def main():
    if "--self-test" in sys.argv:
        return self_test()
    argv = [a for a in sys.argv[1:] if a != "--check"]
    rounds = discover_rounds()
    out = ["# REPAIR LEDGER — findings in, dispositions out\n"]
    problems = 0
    for rnd in rounds:
        for seat in ("GPT56", "CODEX"):
            path = HERE / f"{rnd}_WHOLE_REVIEW_{seat}.md"
            nums, err = parse_block(path) if path.exists() else (None, "missing report")
            if nums is None:
                out.append(f"- {rnd}/{seat}: BLOCK REFUSED — {err}"); problems += 1; continue
            disp = DISPOSITIONS.get((rnd, seat), {})
            for n in nums:
                d = disp.get(n)
                if d is None:
                    out.append(f"- **{rnd}/{seat} F{n}: UNDISPOSED — the V101 failure shape**")
                    problems += 1
                else:
                    out.append(f"- {rnd}/{seat} F{n}: {d[0]} — {d[1]}")
    out.append("\n**LIMIT, on the ledger's own face (GPT56-V102 F7): this instrument checks disposition PRESENCE and block CONTRACTS, never repair ADEQUACY - whether a disposition's cited repair actually answers the finding is the referee round's to judge, and always was. Coverage floor V100; earlier rounds predate the ledger.**")
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
