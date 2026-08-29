#!/usr/bin/env python3
"""REFUSAL VOCABULARY CHECK — the access log's closed refusal set, and the derivation it rests on.

The principal ruled option A on 2026-08-29: eight codes, closed, **no catch-all**. That ruling has no
escape hatch, and the only thing that makes it safe is a derivation claim:

    the vocabulary is closed BECAUSE §6.1's row table is closed
    (Row B is the only path to sealed bytes; Row R's default is forbidden)

**A derivation stated in prose is a claim. This makes it a check.** The lane has spent two days on
exactly the shape where a document asserts something a reader cannot verify, so the closure argument
gets a control rather than a paragraph.

What this cannot do, stated plainly
-----------------------------------
It cannot *generate* eight codes from prose — the mapping from a row table to refusal categories is a
reading, not a parse. What it can do, and what actually matters, is **detect that the basis changed**:
it fingerprints the gate-bearing structure of §6.1 (the rows, their phases, their authorising
preconditions and their void columns) and fails when that fingerprint moves away from the one pinned
beside the vocabulary.

That is the honest form of the guarantee. When it fails it does not say "here are the new codes"; it
says **the derivation must be redone and the set re-pinned, not extended by hand** — which is the
instruction the ruling attaches.

Measured behaviour of the fingerprint, 2026-08-29, before anything relied on it
------------------------------------------------------------------------------
A control that fires on noise stops being read — that is how the void_registry self-test sat red for
four drafts while its output was quoted. So the stability claim was tested rather than assumed:

    stable when a whole new section is appended            yes
    stable when prose inside a row description is edited   yes
    moves when a gate-bearing column changes (row id)      yes
    identical across V52, V53 and V54                      yes  <- three real drafts, §6.1 untouched

The last line is the one that matters: across three consecutive drafts that changed §5, §7.1, §11 and
the preamble, the fingerprint did not move once. It is sensitive to the thing the derivation depends
on and deaf to everything else.
"""

import hashlib
import re
import sys
from pathlib import Path

CODES = (
    "REFUSED-ROW-NOT-AUTHORISED",
    "REFUSED-OUTSIDE-STATED-SURFACE",
    "REFUSED-PRECONDITION-UNVERIFIED",
    "REFUSED-PHASE-NOT-REACHED",
    "REFUSED-LOCK-NOT-OPEN",
    "REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET",
    "REFUSED-SCHEMA-NONCONFORMING",
    "REFUSED-CEREMONY-CONSUMED",
)

ERRORS = {
    "R01": "the draft pins a refusal vocabulary that is not the ruled eight-code set",
    "R02": "§6.1's gate-bearing structure no longer matches the fingerprint pinned with the set — "
           "the derivation must be redone and the set re-pinned, never extended by hand",
    "R03": "the draft does not state the principle the closure rests on (request/authorisation "
           "state, never the object)",
    "R04": "the draft does not forbid free text in the refusal-reason field",
    "R05": "the draft pins no derivation fingerprint at all",
}

ROW_RE = re.compile(r"^\|\s*([A-Z][0-9]?)\s*\|")


def row_fingerprint(text: str) -> str:
    """Digest the gate-bearing columns of §6.1 — the structure the derivation actually depends on.

    Deliberately NOT the whole row: prose edits inside a row's description must not trip this, or the
    control becomes noise and gets ignored, which is how a check stops being read.
    """
    parts = []
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        cols = [c.strip() for c in line.split("|")]
        # row id, MAY TOUCH (the stated surface), when (phase), authorized-by, what voids the run.
        #
        # cols[3] — the surface — was omitted when this shipped, and both seats broke it in one
        # round (GPT56-V56 F1, CODEX-V56 F1): rewriting Row B's surface to unrestricted access left
        # the fingerprint unchanged. The derivation claims the vocabulary is closed BECAUSE the
        # surfaces are closed, so a fingerprint blind to the surface cannot check that claim at all.
        # I excluded it reaching for insensitivity to prose edits and excluded the load-bearing
        # column instead.
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
        fail("R01", f"missing {missing}, extra {extra}")
    elif not pinned:
        fail("R01", "no REFUSED-* codes found")

    m = re.search(r"refusal-vocabulary-derivation:\s*`([0-9a-f]{64})`", text)
    if not m:
        fail("R05")
    elif m.group(1) != row_fingerprint(text):
        fail("R02", f"pinned {m.group(1)[:16]}…, computed {row_fingerprint(text)[:16]}…")

    if not re.search(r"never describe the\s+\*{0,2}OBJECT|never the\s+\*{0,2}OBJECT", text, re.I):
        fail("R03")
    if not re.search(r"no free text", text, re.I):
        fail("R04")
    return out


# ---------------------------------------------------------------------------
# Controls. Each asserts its OWN code — "something refused" is not detection.
# ---------------------------------------------------------------------------

def _fixture(codes=CODES, principle=True, freetext=True, fp=None, rows=True):
    body = []
    if rows:
        body += ["| B | Store mediator | conduit | Any | BS-2k | log | unlogged refusal |",
                 "| R | Every other process | nothing | Pre-unblinding | — | — | any access |"]
    txt = "\n".join(body) + "\n"
    txt += "The reason may describe the request and the authorisation state, never the OBJECT.\n" if principle else ""
    txt += "The field carries exactly one code: no free text.\n" if freetext else ""
    txt += "".join(f"- `{c}`\n" for c in codes)
    txt += f"refusal-vocabulary-derivation: `{fp if fp else row_fingerprint(txt)}`\n"
    return txt


CONTROLS = (
    ("a ninth code is pinned", lambda: _fixture(CODES + ("REFUSED-OTHER",)), "R01"),
    ("a code is dropped", lambda: _fixture(CODES[:-1]), "R01"),
    ("the row table changed under the pin", lambda: _fixture(fp="0" * 64), "R02"),
    ("the principle is absent", lambda: _fixture(principle=False), "R03"),
    ("free text is not forbidden", lambda: _fixture(freetext=False), "R04"),
)


def self_test() -> int:
    fails = []
    good = _fixture()
    codes = {c for c, _ in check(good)}
    if codes:
        fails.append(f"clean fixture refused: {sorted(codes)}")
    for name, build, want in CONTROLS:
        got = {c for c, _ in check(build())}
        if want not in got:
            fails.append(f"{name}: expected {want}, got {sorted(got) or 'nothing'}")
    # R05 must be reachable, or a document with no fingerprint would pass silently
    if "R05" not in {c for c, _ in check(_fixture().replace("refusal-vocabulary-derivation:", "x:"))}:
        fails.append("R05: a missing fingerprint was not detected")
    for f in fails:
        print(f"  FAIL {f}")
    unexercised = set(ERRORS) - {w for _, _, w in CONTROLS} - {"R05"}
    print(f"  self-test: {len(CONTROLS) + 2} controls, {len(fails)} failure(s)"
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
    text = Path(args[0]).read_text()
    problems = check(text)
    for code, msg in problems:
        print(f"  [{code}] {msg}")
    print(f"  refusal vocabulary: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
