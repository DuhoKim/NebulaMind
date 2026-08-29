#!/usr/bin/env python3
"""REFUSAL VOCABULARY CHECK — the access log's ELEVEN codes, and the guard the catch-all needs.

WHAT CHANGED, AND IT IS AN INVERSION — read this before trusting a green result
------------------------------------------------------------------------------
This module previously enforced a CLOSED eight-code set with NO catch-all, and its central control
(R02/R05) demanded that the draft pin a **derivation fingerprint** over §6.1's gate-bearing columns.
That fingerprint existed to detect the invalidation of a **closure argument**.

**On 2026-08-29 at 22:18 the principal ruled that non-closure is established and took the catch-all,
formally reversing the no-catch-all decision of 19:52.** Two independent closure derivations had been
written and both were broken within an hour of being written — the first missed the availability class
entirely; the second rested on *"permitted is binary and evaluated before the attempt"*, which is false
in two directions (a permission check can die before deciding; a write's conformance cannot be judged
before its payload is read).

**So the fingerprint control is INVERTED here, deliberately and loudly:** pinning a
`refusal-vocabulary-derivation` fingerprint is now a FAILURE (R02), because there is no closure claim
for it to protect, and **a control that reports health about a claim nobody makes is worse than no
control.** A reader who remembers the old behaviour would otherwise read a silent inversion as a bug.

What this checks
----------------
    R01  the draft pins a vocabulary that is not the ruled eleven-code set
    R02  the draft pins a derivation fingerprint, or claims the set is closed
    R03  the draft does not state the principle (request/authorisation state, never the object)
    R04  the draft does not forbid free text in the refusal-reason field
    R05  the draft does not state the CATCH-ALL GUARD

**What a lint can establish, stated because three revisions phrase-matched here:** every check in
this file verifies that the DRAFT'S TEXT states a mechanism. None verifies the mechanism exists —
that is the job of the referenced build items and their gate rounds. A green result here says the
words are present and consistent, nothing more.

**R05 is the load-bearing one now.** A catch-all whose count is never reviewed becomes the vocabulary;
the ruling attached the guard for exactly that reason, and the guard is the only thing standing between
`REFUSED-UNCLASSIFIED` and a free-text field with one legal value.

`row_fingerprint()` is retained for diagnosis and **gates nothing**. It is the corrected version — it
includes the `may touch` column, whose omission let both seats rewrite Row B's surface to unrestricted
access without moving the digest (GPT56-V56 F1, CODEX-V56 F1).
"""

import hashlib
import re
import sys
from pathlib import Path

AUTHORISATION = (
    "REFUSED-ROW-NOT-AUTHORISED",
    "REFUSED-OUTSIDE-STATED-SURFACE",
    "REFUSED-PRECONDITION-UNVERIFIED",
    "REFUSED-PHASE-NOT-REACHED",
    "REFUSED-LOCK-OR-CEREMONY-STATE",
)
AVAILABILITY = (
    "REFUSED-OBJECT-ABSENT",
    "REFUSED-OBJECT-UNREADABLE",
    "REFUSED-OBJECT-INCOMPLETE",
    "REFUSED-INTEGRITY-MISMATCH",
)
CONFORMANCE = ("REFUSED-SCHEMA-NONCONFORMING",)
CATCH_ALL = ("REFUSED-UNCLASSIFIED",)
CODES = AUTHORISATION + AVAILABILITY + CONFORMANCE + CATCH_ALL

# Codes from the superseded eight-code set that must NOT reappear. Both were removed for a reason and
# both would pass a naive "is it a REFUSED-* token" check.
RETIRED = {
    "REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET": "describes the OBJECT; deleted, not reworded",
    "REFUSED-LOCK-NOT-OPEN": "merged into REFUSED-LOCK-OR-CEREMONY-STATE",
    "REFUSED-CEREMONY-CONSUMED": "merged into REFUSED-LOCK-OR-CEREMONY-STATE",
}

ERRORS = {
    "R01": "the draft pins a refusal vocabulary that is not the ruled eleven-code set",
    "R02": "the draft pins a derivation fingerprint or claims closure — non-closure was ruled "
           "established on 2026-08-29, so there is no closure claim for a control to protect",
    "R03": "the draft does not state the principle the vocabulary rests on (request/authorisation "
           "state, never the object)",
    "R04": "the draft does not forbid free text in the refusal-reason field",
    "R05": "the draft does not state the CATCH-ALL GUARD — that every REFUSED-UNCLASSIFIED emission "
           "is a defect to be enumerated, never a routine outcome",
    "R06": "the catch-all enumeration is anchored at FREEZE, which precedes every refusal and "
           "therefore cannot police any of them",
    "R07": "the catch-all guard has no BLOCKING INVARIANT — an obligation to review with no "
           "executable consequence is a promise, and the seats read it as one",
    "R08": "the guard names no VERIFIER that recomputes the emissions from the log, or consults it "
           "only once — an obligation complete at one gate does not cover events appended after it",
    "R09": "explanation alone can discharge a RECURRING catch-all class, which is the catch-all "
           "becoming the vocabulary by the route the guard exists to block, while passing it",
}

ROW_RE = re.compile(r"^\|\s*([A-Z][0-9]?)\s*\|")


def row_fingerprint(text: str) -> str:
    """Digest §6.1's gate-bearing columns. RETAINED FOR DIAGNOSIS; GATES NOTHING."""
    parts = []
    for line in text.splitlines():
        if not ROW_RE.match(line):
            continue
        cols = [c.strip() for c in line.split("|")]
        # row id, MAY TOUCH (the stated surface), when (phase), authorized-by, what voids the run.
        keep = [cols[1]] + [cols[i] if len(cols) > i else "" for i in (3, 4, 5, 7)]
        parts.append("\x1f".join(re.sub(r"[*`]", "", k) for k in keep))
    return hashlib.sha256("\x1e".join(parts).encode()).hexdigest()


def check(text: str):
    out = []

    def fail(code, extra=""):
        out.append((code, ERRORS[code] + (f" — {extra}" if extra else "")))

    pinned = set(re.findall(r"`(REFUSED-[A-Z-]+)`", text))
    if pinned and pinned != set(CODES):
        missing, extra = sorted(set(CODES) - pinned), sorted(pinned - set(CODES))
        revived = [c for c in extra if c in RETIRED]
        note = f"missing {missing}, extra {extra}"
        if revived:
            note += f"; RETIRED CODE REVIVED: {[(c, RETIRED[c]) for c in revived]}"
        fail("R01", note)
    elif not pinned:
        fail("R01", "no REFUSED-* codes found")

    if re.search(r"refusal-vocabulary-derivation:\s*`[0-9a-f]{64}`", text):
        fail("R02", "a 64-hex fingerprint is pinned")
    else:
        # SCOPED to the vocabulary. An unscoped search for "closed set" fired on
        # invariance_outcome's HELD/FAILED/NOT-EVALUATED token set in a different section - a control
        # reporting a closure claim that was never made, which is the same wrong-scope defect this
        # lane keeps finding. A closure claim must mention the vocabulary ON THE SAME LINE.
        for line in text.splitlines():
            if re.search(r"closed\s+(set|vocabulary)", line, re.I) and \
               re.search(r"REFUSED-|refusal[- ]reason|refusal vocabulary", line, re.I):
                fail("R02", f"a closure claim about the vocabulary: {line.strip()[:70]!r}")
                break

    if not re.search(r"never describe the\s+\*{0,2}OBJECT|never the\s+\*{0,2}OBJECT|"
                     r"may\s+\*{0,2}never\*{0,2}\s+describe the\s+\*{0,2}object", text, re.I):
        fail("R03")
    if not re.search(r"no free text", text, re.I):
        fail("R04")
    # The guard is checked as a MECHANISM, not as a phrase. V64 stated the obligation and both seats
    # found it unenforceable: a freeze-time review cannot police run-time emissions, and an
    # obligation with no consequence is a promise. Phrase-matching the guard was the finding.
    if not (re.search(r"enumerat(ed|ion)", text, re.I) and re.search(r"REFUSED-UNCLASSIFIED", text)):
        fail("R05")
    else:
        anchored_at_freeze = re.search(r"REFUSED-UNCLASSIFIED[^.]{0,200}?enumerated at freeze|"
                                       r"enumerated at freeze[^.]{0,200}?REFUSED-UNCLASSIFIED",
                                       text, re.I | re.S)
        if anchored_at_freeze:
            fail("R06", "the enumeration is tied to freeze")
        if not re.search(r"MAY NOT BE ISSUED while any `?REFUSED-UNCLASSIFIED", text, re.I):
            fail("R07", "no artifact is blocked by an unenumerated emission")
        # R08 and R09 exist because V66 stated a continuous obligation and named nothing that checks
        # it, and because a class that recurs can be explained every run and stay formally enumerated
        # forever. Matching the words "BS-L" was the defect; these match the MECHANISM.
        verifier = re.search(r"enumeration verifier", text, re.I)
        entry = re.search(r"enumeration entry", text, re.I) and re.search(r"chain_position", text)
        twice = re.search(r"consulted (twice|at both)", text, re.I) or (
            re.search(r"at the opening of the lock", text, re.I) and
            re.search(r"at \*{0,2}`?BS-L`? issuance", text, re.I))
        if not (verifier and twice and entry):
            fail("R08", "verifier named: %s; second consultation: %s; entry object with a join: %s"
                 % (bool(verifier), bool(twice), bool(entry)))
        if not re.search(r"recur", text, re.I):
            fail("R09", "no rule for a recurring catch-all class")
        elif not re.search(r"class_key", text):
            fail("R09", "recurrence has no computed equivalence key - a class you may name is a "
                        "class you may rename")
    return out


# ---------------------------------------------------------------------------
# Controls. Each asserts its OWN code — "something refused" is not detection.
# ---------------------------------------------------------------------------

def _fixture(codes=CODES, principle=True, freetext=True, guard=True, fingerprint=False,
             closed=False):
    txt = "| B | Store mediator | conduit | Any | BS-2k | log | unlogged refusal |\n"
    if principle:
        txt += "The reason may describe the request and the authorisation state, never the OBJECT.\n"
    if freetext:
        txt += "The field carries exactly one code: no free text.\n"
    if guard == "freeze":
        txt += ("Every emission of REFUSED-UNCLASSIFIED is a defect to be enumerated at freeze.\n"
                "BS-L MAY NOT BE ISSUED while any REFUSED-UNCLASSIFIED event is unenumerated.\n")
    elif guard == "noblock":
        txt += ("Every emission of REFUSED-UNCLASSIFIED is a defect to be enumerated at the lock "
                "checkpoint, never a routine outcome.\n")
    elif guard in ("noverifier", "once", "norecur", "noentry", "nokey", True):
        txt += ("Every emission of REFUSED-UNCLASSIFIED is a defect to be enumerated at the lock "
                "checkpoint, never a routine outcome.\n"
                "BS-L MAY NOT BE ISSUED while any REFUSED-UNCLASSIFIED event is unenumerated.\n")
        if guard != "noverifier":
            txt += "The enumeration verifier recomputes the emissions from the chain.\n"
        if guard not in ("noentry", "noverifier"):
            txt += "Each enumeration entry joins by chain_position and event_digest.\n"
        if guard != "once" and guard != "noverifier":
            txt += "It is consulted twice: at BS-L issuance and at the opening of the lock.\n"
        if guard != "norecur":
            txt += "If the same class recurs, explanation stops discharging it.\n"
        if guard not in ("nokey", "norecur"):
            txt += "Two emissions share a class iff their class_key values are equal.\n"
    txt += "".join(f"- `{c}`\n" for c in codes)
    if fingerprint:
        txt += f"refusal-vocabulary-derivation: `{'a' * 64}`\n"
    if closed:
        txt += "The closed set of REFUSED- codes is pinned above.\n"
    return txt


CONTROLS = (
    ("a twelfth code is pinned", lambda: _fixture(CODES + ("REFUSED-OTHER",)), "R01"),
    ("the catch-all is dropped", lambda: _fixture(CODES[:-1]), "R01"),
    ("a retired code is revived", lambda: _fixture(CODES + ("REFUSED-LOCK-NOT-OPEN",)), "R01"),
    ("a derivation fingerprint is pinned", lambda: _fixture(fingerprint=True), "R02"),
    ("the set is called closed", lambda: _fixture(closed=True), "R02"),
    ("the principle is absent", lambda: _fixture(principle=False), "R03"),
    ("free text is not forbidden", lambda: _fixture(freetext=False), "R04"),
    ("the catch-all guard is absent", lambda: _fixture(guard=False), "R05"),
    ("the enumeration is anchored at freeze", lambda: _fixture(guard="freeze"), "R06"),
    ("the guard has no blocking invariant", lambda: _fixture(guard="noblock"), "R07"),
    ("the guard names no enumeration verifier", lambda: _fixture(guard="noverifier"), "R08"),
    ("the verifier is consulted only once", lambda: _fixture(guard="once"), "R08"),
    ("recurrence can be explained away", lambda: _fixture(guard="norecur"), "R09"),
    ("the verifier has no entry object", lambda: _fixture(guard="noentry"), "R08"),
    ("recurrence has no computed key", lambda: _fixture(guard="nokey"), "R09"),
)

# A control that asserts a code does NOT fire. Without this, scoping R02 could be narrowed to nothing
# and every positive control would still pass - the shape that let a fingerprint miss the surface
# column for four drafts.
NEGATIVE_CONTROLS = (
    ("an unrelated closed set does not fire R02",
     lambda: _fixture() + "invariance_outcome takes one token from the closed set HELD/FAILED.\n",
     "R02"),
)


def self_test() -> int:
    fails = []
    codes = {c for c, _ in check(_fixture())}
    if codes:
        fails.append(f"clean fixture refused: {sorted(codes)}")
    for name, build, want in CONTROLS:
        got = {c for c, _ in check(build())}
        if want not in got:
            fails.append(f"{name}: expected {want}, got {sorted(got) or 'nothing'}")
    for name, build, must_not in NEGATIVE_CONTROLS:
        got = {c for c, _ in check(build())}
        if must_not in got:
            fails.append(f"{name}: {must_not} fired and must not have")
    for f in fails:
        print(f"  FAIL {f}")
    unexercised = set(ERRORS) - {w for _, _, w in CONTROLS}
    print(f"  self-test: {len(CONTROLS) + len(NEGATIVE_CONTROLS) + 1} controls "
          f"({len(NEGATIVE_CONTROLS)} negative), {len(fails)} failure(s)"
          + (f"; UNEXERCISED {sorted(unexercised)}" if unexercised else "; every code controlled"))
    return 1 if fails else 0


def main() -> int:
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()
    if "--fingerprint" in args and len(args) > 1:
        print(row_fingerprint(Path(args[0]).read_text()))
        return 0
    if not args:
        print("usage: refusal_vocabulary_check.py DRAFT.md | --self-test | DRAFT.md --fingerprint")
        return 2
    problems = check(Path(args[0]).read_text())
    for code, msg in problems:
        print(f"  [{code}] {msg}")
    print(f"  refusal vocabulary: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
