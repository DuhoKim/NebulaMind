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
    R03  the draft does not state the REBUILT principle (storage state allowed, content-derived forbidden, chi-blind-schedule dependency stated)
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
    "R03": "the draft does not state the REBUILT principle (storage state may be described; "
           "anything content-derived never; safe only under a precommitted chi-blind read schedule)",
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

    # GPT56-V70 F4: backtick-only extraction let a bare "REFUSED-EVADE." evade R01 entirely, and the
    # retired-mention convention (write it unformatted so it is not counted) was the evasion's twin.
    # Members are now parsed independently of Markdown decoration; a non-member token is legal ONLY
    # on a line that also carries a retirement word.
    # CODEX-V72 F6: "REFUSED-ZOMBIE is not deleted" contained the word "deleted" and was exempted -
    # a negated retirement is an ACTIVATION. The retirement word must not be negated just before it.
    RETIREMENT = re.compile(r"(?<!not )(?<!never )(deleted|merged|retired|superseded|GONE|does not survive)", re.I)
    # The activation list is FINITE AND KNOWN INCOMPLETE (CODEX-V77 F4 evaded it with "now
    # mandatory" - added - and the next phrasing will evade it too). The guard catches named shapes;
    # prose semantics beyond them are the referee round's job, which is this lint's stated limit,
    # not a gap it pretends to close.
    ACTIVATION = re.compile(r"reinstat|restored|reactivat|is active|in force|hereby|applies again|"
                            r"governs|mandatory|shall apply|takes effect|is live|will be|will apply|becomes|to be used|remains operative|expected to apply|should control|continues to|required|authoritative|controls |will be used", re.I)
    pinned, illegal = set(), []
    for line in text.splitlines():
        # GPT56-V73 F4 / CODEX-V73 F6: one retirement word exempted every token ON THE LINE, so
        # "REFUSED-OLD was deleted; REFUSED-NEW is in force." activated NEW under OLD's retirement.
        # The exemption is now per-SENTENCE-FRAGMENT: a token is exempt only if a retirement word
        # shares its fragment (split on . ; :). Em-dash is NOT a splitter - this corpus uses it for
        # asides inside one sentence, and splitting on it orphaned a legitimate retired mention from
        # its own "was deleted" two asides later.
        for frag in re.split(r"[.;:]", line):
            toks = [tk.rstrip("-") for tk in re.findall(r"(?<![A-Z0-9-])REFUSED-[A-Z][A-Z-]+(?![a-z0-9_])", frag)]
            nonmembers = [tk for tk in toks for _ in [0] if tk not in CODES]
            for tok in toks:
                if tok in CODES:
                    pinned.add(tok)
                    # GPT56-V77 F9: an active-code TOMBSTONE ("REFUSED-<member> is deleted") makes
                    # prose diverge from the operative set while the checker stayed green - a member
                    # in a retiring fragment is a divergence, not an exemption.
                    if RETIREMENT.search(frag):
                        illegal.append(tok + " (member inside a retiring fragment)")
                # CODEX-V74 F3: a retiring fragment may retire AT MOST ONE token. GPT56-V75 F4:
                # the exemption applies ONLY to tokens in the KNOWN retired set. And GPT56-V76 F4 /
                # CODEX-V76 F3: a retired token REACTIVATED in the same fragment as its historical
                # retirement word ("was deleted but is hereby reinstated") rode the exemption -
                # an activation word anywhere in the fragment defeats it.
                elif (tok not in RETIRED or not RETIREMENT.search(frag)
                      or ACTIVATION.search(line[line.find(tok):line.find(tok) + len(tok) + 160])
                      or len(nonmembers) > 1):
                    # activation is scanned in a 160-char window AFTER the token: "was retired; it
                    # is now mandatory" rode a pronoun across the fragment boundary (CODEX-V77 F4),
                    # while whole-line and next-fragment scans both false-fired on "governs" three
                    # sentences later in a legitimate retired mention. Proximity is the repair for
                    # both directions; the window size is a stated heuristic, and wording that
                    # activates beyond it is the round's to catch, per this file's limit statement
                    illegal.append(tok)
    if illegal:
        fail("R01", f"non-member REFUSED-* token(s) outside a retirement line: {sorted(set(illegal))}")
    if pinned and pinned != set(CODES):
        fail("R01", f"missing {sorted(set(CODES) - pinned)}")
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

    # REBUILT (principal ruling 2026-08-30 10:46). The old body required the PRE-ruling sentence
    # ("never the OBJECT") and stayed green off a dead draft tail until the V88 supersession sweep
    # killed the tail and this control surfaced as the eighth stale site — a control encoding the
    # old regime is part of the regime. Three prongs, each required, failure names the missing one.
    _prongs = (
        ("storage-state permission", r"storage\s+state"),
        ("content-derived ban", r"never\s+carr(?:y|ies)\s+anything\s+content-derived"),
        ("chi-blind-schedule dependency", r"precommitted\s+and\s+(?:χ|chi)-blind"),
    )
    _missing = [n for n, p in _prongs if not re.search(p, text, re.I)]
    if _missing:
        fail("R03", f"missing prong(s): {', '.join(_missing)}")
    else:
        # a later contradiction must not coexist with the phrase that makes R03 pass (GPT56-V70 F4)
        # - under the rebuilt principle the contradiction is an affirmative CONTENT-DERIVED allowance
        for line in text.splitlines():
            if re.search(r"may (?:carry|describe|encode)[^.]*content-derived|may describe the object(?!['’]s storage)", line, re.I) and \
               not re.search(r"\bnever\b|\bnot\b|forbid|refuses", line, re.I):
                fail("R03", f"affirmative contradiction: {line.strip()[:60]!r}")
                break
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
        gates5 = re.search(r"BS-7f", text) and re.search(r"disclosure", text, re.I) and \
                 re.search(r"fresh", text, re.I)
        # CODEX-V82 F6: these checks were polarity-blind - "the verifier is NOT consulted" passed
        # because the words appeared. A negated mechanism line now fails the mechanism.
        # Negated-FORM patterns, not word proximity: two proximity attempts false-fired on "not"
        # belonging to neighbouring clauses ("does not discharge", "label is not in the key"). What
        # R08 must catch is the mechanism VERB negated - "is not consulted", "never runs", "no
        # longer recomputes" - so those forms are matched directly (CODEX-V82 F6).
        m_neg = re.search(
            r"(?:enumeration verifier|fresh pass)[^.;\n]{0,50}\b(?:is|are|was|were|will be)\s+"
            r"(?:not|never|no longer)\b"
            r"|\bnot\s+consulted\b|\bnever\s+consulted\b|\bno longer\s+(?:consulted|runs?|recomputes?)\b",
            text, re.I)
        if m_neg:
            fail("R08", f"a mechanism verb is NEGATED: {m_neg.group(0)[:60]!r}")
        if not (verifier and twice and entry and gates5):
            fail("R08", "verifier: %s; second consultation: %s; entry object: %s; post-opening "
                 "gates: %s" % (bool(verifier), bool(twice), bool(entry), bool(gates5)))
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
        txt += ("The reason may describe the request, the authorisation state, and the object's "
                "STORAGE STATE; it may never carry anything CONTENT-DERIVED, and storage-state "
                "codes are safe only because the read schedule is precommitted and chi-blind.\n")
    if freetext:
        txt += "The field carries exactly one code: no free text.\n"
    if guard == "freeze":
        txt += ("Every emission of REFUSED-UNCLASSIFIED is a defect to be enumerated at freeze.\n"
                "BS-L MAY NOT BE ISSUED while any REFUSED-UNCLASSIFIED event is unenumerated.\n")
    elif guard == "noblock":
        txt += ("Every emission of REFUSED-UNCLASSIFIED is a defect to be enumerated at the lock "
                "checkpoint, never a routine outcome.\n")
    elif guard in ("noverifier", "once", "norecur", "noentry", "nokey", "nogates", True):
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
        if guard != "nogates":
            txt += "Fresh passes run at BS-7f, BS-V and disclosure.\n"
    txt += "".join(f"- `{c}`\n" for c in codes)
    if fingerprint:
        txt += f"refusal-vocabulary-derivation: `{'a' * 64}`\n"
    if closed:
        txt += "The closed set of REFUSED- codes is pinned above.\n"
    return txt


CONTROLS = (
    ("a twelfth code is pinned", lambda: _fixture(CODES + ("REFUSED-OTHER",)), "R01"),
    ("the catch-all is dropped everywhere", lambda: _fixture(CODES[:-1], guard=False), "R01"),
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
    ("a bare twelfth member evades the backtick parse",
     lambda: _fixture() + "Active refusal member: REFUSED-EVADE.\n", "R01"),
    ("a later contradiction coexists with the principle",
     lambda: _fixture() + "A refusal reason may carry content-derived values.\n", "R03"),
    ("a blanket object-permission contradicts the rebuilt principle",
     lambda: _fixture() + "A refusal reason may describe the object.\n", "R03"),
    ("it-controls reactivation is caught",
     lambda: _fixture() + "REFUSED-CEREMONY-CONSUMED was retired; it controls requests at P7.\n", "R01"),
    ("the post-opening gates are unnamed", lambda: _fixture(guard="nogates"), "R08"),
    ("a negated mechanism fails the mechanism",
     lambda: _fixture() + "The enumeration verifier is not consulted at BS-L issuance.\n", "R08"),
    ("a negated retirement activates a token",
     lambda: _fixture() + "REFUSED-ZOMBIE is not deleted and remains in force.\n", "R01"),
    ("one retirement word does not exempt a second token on the line",
     lambda: _fixture() + "REFUSED-OLD was deleted; REFUSED-NEW is in force.\n", "R01"),
    ("an em-dash pair cannot share one retirement",
     lambda: _fixture() + "REFUSED-OLD was deleted — REFUSED-NEW is in force.\n", "R01"),
    ("a novel token cannot buy legality from the word deleted",
     lambda: _fixture() + "REFUSED-NOVEL was deleted long ago.\n", "R01"),
    ("a retired token cannot be reactivated beside its retirement",
     lambda: _fixture() + "REFUSED-LOCK-NOT-OPEN was deleted but is hereby reinstated.\n", "R01"),
    ("now-mandatory evades the old activation list",
     lambda: _fixture() + "REFUSED-CEREMONY-CONSUMED was retired; it is now mandatory.\n", "R01"),
    ("an active-code tombstone is a divergence",
     lambda: _fixture() + "REFUSED-PHASE-NOT-REACHED is deleted.\n", "R01"),
    ("future-tense reactivation is caught",
     lambda: _fixture() + "REFUSED-LOCK-NOT-OPEN was retired; it will be used at P7.\n", "R01"),
    ("remains-operative reactivation is caught",
     lambda: _fixture() + "REFUSED-CEREMONY-CONSUMED was superseded yet remains operative.\n", "R01"),
    ("required-authoritative reactivation is caught",
     lambda: _fixture() + "REFUSED-LOCK-NOT-OPEN was merged, and it is required at P6.\n", "R01"),
    ("a suffixed non-member is not a member",
     lambda: _fixture() + "Emit REFUSED-OBJECT-ABSENTLY here.\n", "R01"),
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
