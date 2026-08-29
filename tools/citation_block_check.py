#!/usr/bin/env python3
"""CITATION BLOCK CHECK — verify a repair citation against a report's DECLARED findings.

Why this module exists, and why it is not another parser
--------------------------------------------------------
Three adversarial rounds killed the previous citation check, and all three died the same way. It
enumerated a report's findings with a regex and then concluded a cited finding was *absent*. That is
using a pattern to establish a negative, which is unsound by construction: when the pattern misses a
grammar, absence is manufactured. It ended up reporting `FABRICATED` against citations that were
real, which is strictly worse than not checking, and it was quarantined rather than repaired a
fourth time.

The principal's ruling (2026-08-29, "fix it so checker actually read it") is option C: stop trying to
recover an unencoded judgement, and encode it at the source. Which numbered items in a report are
*findings* is a judgement its author makes; `FINDINGS-BLOCK v1` makes the author write it down. This
module reads that block and nothing else. It does not parse prose, and it never infers a finding from
a heading.

The four outcomes, and why there are four
-----------------------------------------
    VERIFIED       the report declares a well-formed block and the cited number is in it
    FABRICATED     the report declares a well-formed block and the cited number is NOT in it
    UNVERIFIABLE   a block exists but is malformed or internally inconsistent
    NO_BLOCK       the report predates FINDINGS-BLOCK v1 (the ~30 historical reports)

Only FABRICATED may be reported as a document defect. UNVERIFIABLE and NO_BLOCK are reported as
what they are — the checker declining to decide. NO_BLOCK is deliberately separate from
UNVERIFIABLE: the historical corpus is a known, bounded set awaiting a disposition from the
principal, not a parse failure. Collapsing them would hide that a decision is pending.
"""

import re
import sys
from pathlib import Path

CODES = {
    "C01": "the block declares COUNT that disagrees with the number of F lines",
    "C02": "the block's finding numbers are not contiguous from 1",
    "C03": "the block declares a SEAT or VERSION that contradicts the citation being checked",
    "C04": "an F line does not carry all five fields",
    "C05": "more than one FINDINGS-BLOCK appears in a single report",
}

OPEN = "<!-- FINDINGS-BLOCK v1 -->"
CLOSE = "<!-- END FINDINGS-BLOCK -->"

_F_LINE = re.compile(r"^F(\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|(.*)$")
_HDR = re.compile(r"^(SEAT|VERSION|VERDICT|COUNT)\s*:\s*(.+?)\s*$")


class Block:
    def __init__(self, seat, version, verdict, count, findings):
        self.seat, self.version, self.verdict = seat, version, verdict
        self.count, self.findings = count, findings


def parse_block(text):
    """Return (Block, None) or (None, reason). Never raises on hostile input.

    A malformed block is a REFUSAL, not an empty finding set. Returning an empty set for a block the
    parser could not read is precisely how the previous check manufactured absence.
    """
    opens = text.count(OPEN)
    if opens == 0:
        return None, "NO_BLOCK"
    if opens > 1:
        return None, "C05: more than one FINDINGS-BLOCK in the report"
    start = text.index(OPEN) + len(OPEN)
    if CLOSE not in text[start:]:
        return None, "unterminated FINDINGS-BLOCK"
    body = text[start:start + text[start:].index(CLOSE)]

    hdr, findings = {}, []
    for raw in body.split("\n"):
        line = raw.strip()
        if not line:
            continue
        m = _HDR.match(line)
        if m:
            hdr[m.group(1)] = m.group(2)
            continue
        f = _F_LINE.match(line)
        if f:
            fields = [f.group(i).strip() for i in range(2, 6)]
            if not all(fields):
                return None, f"C04: F{f.group(1)} does not carry all five fields"
            findings.append(int(f.group(1)))
            continue
        return None, f"unrecognised line in block: {line[:60]!r}"

    for k in ("SEAT", "VERSION", "VERDICT", "COUNT"):
        if k not in hdr:
            return None, f"block is missing {k}"
    try:
        count = int(hdr["COUNT"])
    except ValueError:
        return None, f"COUNT is not an integer: {hdr['COUNT']!r}"

    if count != len(findings):
        return None, f"C01: COUNT says {count} but {len(findings)} F line(s) are present"
    if findings != list(range(1, len(findings) + 1)):
        return None, f"C02: finding numbers {findings} are not contiguous from 1"

    return Block(hdr["SEAT"], hdr["VERSION"], hdr["VERDICT"], count, findings), None


def classify(seat, version, number, report_text):
    """Classify one citation against one report. Returns (outcome, detail)."""
    block, why = parse_block(report_text)
    if block is None:
        if why == "NO_BLOCK":
            return "NO_BLOCK", "report predates FINDINGS-BLOCK v1"
        return "UNVERIFIABLE", why
    if block.seat != seat or block.version != version:
        return "UNVERIFIABLE", (f"C03: block declares {block.seat}/{block.version}, "
                               f"citation is {seat}/{version}")
    if number in block.findings:
        return "VERIFIED", f"F{number} is declared among {block.count} finding(s)"
    return "FABRICATED", (f"F{number} is not declared; the block declares "
                          f"{block.findings or 'no findings'}")


# ---------------------------------------------------------------------------
# Controls. Each asserts an EXACT outcome, not that "something fired".
# ---------------------------------------------------------------------------

def _blk(seat="GPT56", version="V38", verdict="NOT CLEAR", count=2, lines=None):
    body = [OPEN, f"SEAT: {seat}", f"VERSION: {version}", f"VERDICT: {verdict}", f"COUNT: {count}"]
    body += lines if lines is not None else [
        "F1 | HIGH | REPAIR-REQUIRED | §7 line 700 | the slot does not block what it claims",
        "F2 | MEDIUM | ADVISORY | §2.7 line 388 | wording is ambiguous",
    ]
    body.append(CLOSE)
    return "prose above\n" + "\n".join(body) + "\nprose below\n"


CONTROLS = (
    ("cited finding is declared", ("GPT56", "V38", 1, _blk()), "VERIFIED"),
    ("second cited finding is declared", ("GPT56", "V38", 2, _blk()), "VERIFIED"),
    ("cited finding is absent from a good block", ("GPT56", "V38", 3, _blk()), "FABRICATED"),
    ("absent from an empty but valid block",
     ("GPT56", "V38", 1, _blk(count=0, lines=[])), "FABRICATED"),
    ("legacy report with no block", ("GPT56", "V11", 3, "# old report\n### 3. finding\n"), "NO_BLOCK"),
    ("COUNT disagrees with F lines", ("GPT56", "V38", 1, _blk(count=5)), "UNVERIFIABLE"),
    ("numbering is not contiguous",
     ("GPT56", "V38", 1, _blk(count=2, lines=[
         "F1 | HIGH | REPAIR-REQUIRED | §7 | a",
         "F3 | LOW | ADVISORY | §2 | b"])), "UNVERIFIABLE"),
    ("F line missing a field",
     ("GPT56", "V38", 1, _blk(count=1, lines=["F1 | HIGH | REPAIR-REQUIRED |  | a"])), "UNVERIFIABLE"),
    ("block is for a different seat", ("CODEX", "V38", 1, _blk()), "UNVERIFIABLE"),
    ("block is for a different version", ("GPT56", "V37", 1, _blk()), "UNVERIFIABLE"),
    ("two blocks in one report", ("GPT56", "V38", 1, _blk() + _blk()), "UNVERIFIABLE"),
    ("unterminated block", ("GPT56", "V38", 1, "x\n" + OPEN + "\nSEAT: GPT56\n"), "UNVERIFIABLE"),
)


def run_controls():
    fails = []
    for name, (seat, ver, num, text), expect in CONTROLS:
        got, detail = classify(seat, ver, num, text)
        if got != expect:
            fails.append(f"{name}: expected {expect}, got {got} ({detail})")
    return fails


def self_test():
    fails = run_controls()
    for f in fails:
        print(f"  FAIL {f}")
    print(f"  self-test: {len(CONTROLS)} controls, {len(fails)} failure(s)")

    # Every outcome must be asserted by at least one control. An outcome no control pins can be
    # deleted without turning the battery red - which is exactly how the previous check shipped a
    # canary that could not detect deletion of its own positive branch.
    pinned = {e for _, _, e in CONTROLS}
    missing = {"VERIFIED", "FABRICATED", "UNVERIFIABLE", "NO_BLOCK"} - pinned
    if missing:
        print(f"  UNPINNED OUTCOME(S): {sorted(missing)} — a control battery that cannot detect "
              f"their deletion proves nothing")
        return 1
    print(f"  all four outcomes pinned by at least one control: {sorted(pinned)}")
    return 1 if fails else 0


def deletion_probe():
    """Strictly probe that removing each outcome breaks the battery.

    A crash does NOT count as detection. Only a named control changing verdict counts.
    """
    global classify
    original = classify
    ALL = ("VERIFIED", "FABRICATED", "UNVERIFIABLE", "NO_BLOCK")
    probed, undetected = 0, []
    for outcome in ALL:
        # A deleted branch stops producing its outcome and yields some OTHER one. My first version
        # of this probe redirected every outcome to VERIFIED, which made the VERIFIED case a no-op
        # and reported the battery as unable to detect its own positive branch. That was the probe
        # being vacuous, not the checker being uncontrolled - and it is the identical defect that
        # sank the previous citation check, reproduced here in the tool built to replace it.
        # Redirect to a DIFFERENT outcome so every branch is genuinely exercised.
        substitute = next(o for o in ALL if o != outcome)

        def broken(seat, version, number, text, _o=outcome, _s=substitute):
            got, detail = original(seat, version, number, text)
            return (_s, detail) if got == _o else (got, detail)
        classify = broken
        try:
            fails = run_controls()
        except Exception as e:  # a crash is not detection
            fails = []
            print(f"  {outcome}: probe CRASHED ({type(e).__name__}) — not counted as detection")
        finally:
            classify = original
        probed += 1
        if fails:
            print(f"  OK   deleting {outcome} turns the battery red ({len(fails)} control(s))")
        else:
            undetected.append(outcome)
            print(f"  FAIL deleting {outcome} leaves the battery GREEN")
    print(f"  deletion probe: {probed} outcome(s), {len(undetected)} undetected")
    return 1 if undetected else 0


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()
    if "--deletion-probe" in args:
        return deletion_probe()
    if len(args) == 4:
        seat, version, number, path = args[0], args[1], int(args[2]), Path(args[3])
        outcome, detail = classify(seat, version, number, path.read_text(errors="ignore"))
        print(f"{outcome}: {detail}")
        return 0 if outcome == "VERIFIED" else 1
    print(__doc__.strip().split("\n")[0])
    print("usage: citation_block_check.py SEAT VERSION NUMBER REPORT.md")
    print("       citation_block_check.py --self-test | --deletion-probe")
    return 2


if __name__ == "__main__":
    sys.exit(main())
