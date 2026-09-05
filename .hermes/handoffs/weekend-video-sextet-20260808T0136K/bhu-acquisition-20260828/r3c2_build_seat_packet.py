#!/usr/bin/env python3
"""Build the R3-C2 SEAT packet from the master preregistration, mechanically.

Blanc 2026-09-04 22:02 item 2; kimi V4 finding 6; codex V4 finding 5.

The seat packet must contain only what a seat needs to DO the reproduction. The master
preregistration also contains the study's rationale, its gate history and the reason the blind
exists -- all of which disclose the pattern the seat is supposed to be blind to.

Redaction happens HERE, in a script, not by hand-editing a copy, so that
  (a) it is reproducible and auditable, and
  (b) the master document is never altered to serve the blind. In particular the HELD clause of
      the master is left byte-for-byte alone; only the seat's copy loses the example inside it.

Exit 0 = packet built and every assertion passed. Exit 1 = FAIL, packet NOT written.
"""
import re, sys, hashlib, pathlib

MASTER = pathlib.Path("R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md")
# Permanent, committed home. NOT a _tmp_ path: a clause cites this file by hash, and a cited
# artefact that lives in scratch is not part of the record (Blanc 2026-09-04 23:32, item 1).
OUT    = pathlib.Path("r3c2_seat_packet/R3C2_SEAT_PACKET.md")

# Whole sections dropped: rationale, post-tally handling, out-of-scope, gate/version history.
DROP_SECTIONS = ["0.", "7.", "8.", "10."]

# Inline spans marked in the master with <!--SEAT-REDACT-->...<!--/SEAT-REDACT--> are stripped.
# Marking them in the master (rather than listing sentences here) keeps the split visible to a reader
# of the master and keeps this script from silently under-redacting when the wording changes.
REDACT_OPEN, REDACT_CLOSE = "<!--SEAT-REDACT-->", "<!--/SEAT-REDACT-->"

# Every control must reach the seat WITH its instruction, not just its pass-code, and every outcome
# class it may file must be readable. Each entry is checked for literal presence in the built packet.
REQUIRED = [
    "C0_REACHABILITY", "C1_DENOMINATOR_PRINTED", "C2_INPUT_LEDGER", "C3_NO_SUBSTITUTION",
    "C4 — what the seat must do", "C4_PATTERN_BLIND",
    "C5_HARNESS_PINNED", "C5B_NO_CROSS_LANE", "C6_AUDIT_SAMPLE",
    "REPRO_EXACT", "REPRO_FAILED", "REPRO_BLOCKED", "REPRO_NOT_EVALUABLE",
    "REPRO_INPUT_ABSENT", "REPRO_NO_DERIVATION_STATED",
    "origin_evidence", "root_origins", "derived_from", "rests_on",
    "Print every path you\n  open",
]

FORBIDDEN = [
    "shape/magnitude", "pattern record", "the pattern", "ΛCDM", "LCDM",
    "what this census exists to detect", "gate finding", "gate findings", "PREREG_UNSOUND",
    "Blanc", "entry 59", "929.25", "hypothesis", "Duho", "R3C_MAGNITUDE", "circular",
    # V11 (Duho 14:31: strip consequence, not just content) — custody chain, engines, sibling study, consequence words
    "Tori", "codex", "kimi", "Kimi", "agy", "R3D", "R3A", "R3B",
    "expectation", "expects", "refute", "consequential", "invisible", "favourable", "unfavourable", "stake", "prior", "tempting", "warn",
    "pattern-blind", "removed **deliberately",
]

def split_sections(text):
    """Return [(heading_or_None, body)] preserving order; heading is like '0.' for '## 0. ...'."""
    parts, cur, curhead = [], [], None
    for line in text.splitlines(keepends=True):
        m = re.match(r"^## (\d+)\.", line)
        if m:
            parts.append((curhead, "".join(cur))); cur, curhead = [line], m.group(1) + "."
        else:
            cur.append(line)
    parts.append((curhead, "".join(cur)))
    return parts

def main():
    text = MASTER.read_text(encoding="utf-8")
    master_sha = hashlib.sha256(text.encode()).hexdigest()

    kept = []
    for head, body in split_sections(text):
        if head is None:
            continue                      # front matter (title + provenance block) is replaced
        if head in DROP_SECTIONS:
            continue
        kept.append((head, body))

    header = (
        "# R3-C2 seat packet — reproduction census: what to do\n\n"
        "**You are one of two independent seats. Work only from this file, the seat brief, and the pinned\n"
        "sources in this directory. Do not open any other path; print every path you open.**\n\n"
        "This packet is the complete instruction set for your task, extracted mechanically by\n"
        "`r3c2_build_seat_packet.py`. Apply the rules below exactly as written.\n\n"
        f"Built from master sha256 `{master_sha}` by `r3c2_build_seat_packet.py`.\n\n"
    )
    out = header + "".join(b for _, b in kept)

    n_spans = 0
    while REDACT_OPEN in out:
        a = out.index(REDACT_OPEN)
        b = out.find(REDACT_CLOSE, a)
        if b < 0:
            print("FAIL: unclosed <!--SEAT-REDACT--> in master; packet NOT written.")
            return 1
        out = out[:a] + out[b + len(REDACT_CLOSE):]
        n_spans += 1
    if REDACT_CLOSE in out:
        print("FAIL: stray <!--/SEAT-REDACT--> without an opener; packet NOT written.")
        return 1

    # Hard assertion 2: everything a seat NEEDS must SURVIVE. The forbidden list checks what must be
    # absent; without this, a redaction span that swallows an instruction leaves a control code with
    # nothing to do -- which is exactly what happened to C4, whose packet entry was reduced to the bare
    # line "C4_PATTERN_BLIND=PASS" while the master read correctly. A control a seat cannot read is a
    # control it can only assert.
    missing = [r for r in REQUIRED if r not in out]
    if missing:
        print("FAIL: required seat-facing content did not survive redaction:")
        for m in missing:
            print(f"  missing: {m!r}")
        print("Packet NOT written.")
        return 1

    # Hard assertion: nothing on the forbidden list may survive anywhere in the packet.
    bad = []
    for line_no, line in enumerate(out.splitlines(), 1):
        for f in FORBIDDEN:
            if f.lower() in line.lower():
                bad.append((line_no, f, line.strip()[:90]))
    if bad:
        print("FAIL: C4_PACKET_REDACTED=FAIL — forbidden content survived redaction:")
        for n, f, l in bad:
            print(f"  line {n}: {f!r} in: {l}")
        print("Packet NOT written.")
        return 1

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(out, encoding="utf-8")
    print(f"C4_PACKET_REDACTED=PASS")
    print(f"master        sha256 {master_sha}")
    print(f"seat packet   sha256 {hashlib.sha256(out.encode()).hexdigest()}")
    print(f"sections kept {[h for h,_ in kept]}   dropped {DROP_SECTIONS}   inline spans redacted {n_spans}")
    print(f"written       {OUT}  ({len(out)} bytes, master {len(text)} bytes)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
