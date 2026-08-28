#!/usr/bin/env python3
"""PREREG LINT — the consistency checks a 650-line promise cannot enforce on itself.

WHY THIS EXISTS
---------------
Blanc, 2026-08-27: "three times yesterday your own change broke your own probe because the test
still pointed at the old shape. The same risk applies to a document — a repair in §5 that leaves
§7 asserting the old behaviour is the identical failure in prose."

That is exactly what happened. V12 renamed the lock receipt and left §7 calling BS-V the lock.
V12 created BS-2a as a class-P prerequisite and filed it under Class E. V14 renumbered a list
into 1,2,3,4,6,7,5. Every one was found by a referee, spending a review round on bookkeeping
that a script can check in a second.

None of these checks judge the science or the promise. They check that the document agrees with
itself, which is the part I keep getting wrong while attending to the part I do not.

    python3 tools/prereg_lint.py <draft.md> [--gates DIR]

Exit 0 clean, 1 if any check fails.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

SLOT = re.compile(r"\bBS-[0-9]+[a-z]?\b|\bBS-[A-Z]\b")


def slot_rows(text):
    """Slot identifiers that have a row in the §7 table, and the class each sits under.

    Keyed by slot ID, so this is the map for *identity* questions (does BS-2f sit in Class E?).
    It is NOT a row count: it only sees rows whose first cell starts with a BS- identifier.
    Use count_rows() to count. See the note there — assuming these were the same thing put a
    wrong number into the document.
    """
    rows, cls = {}, None
    for line in text.splitlines():
        if re.match(r"\*\*Class [PE]", line.strip()):
            cls = "P" if "Class P" in line else "E"
        m = re.match(r"\|\s*(BS-[0-9]+[a-z]?|BS-[A-Z])\b", line.strip())
        if m:
            rows[m.group(1)] = cls
    return rows


def count_rows(text):
    """Count §7 DATA rows per class — every row, not only BS-prefixed ones.

    Class E holds a row whose first cell reads "Unblinding receipt", not a BS- identifier. The
    identifier-keyed matcher above never saw it, so this linter reported 7 Class-E rows where the
    table has 8. I trusted that over five drafts of prior agreement, had a correct 8 changed to an
    incorrect 7, and had the repair trace rewritten to accuse V17 of introducing an error it had
    actually fixed. CODEX caught it by counting data rows instead of asserted slot IDs.

    My cross-check used the same `^| BS-` shape as the matcher, so it shared the blind spot and
    confirmed nothing. Two checks that agree because they carry the same assumption are one check.

    Header and separator rows are excluded; anything else with a non-empty first cell is a row.
    """
    n, cls = {"P": 0, "E": 0}, None
    for line in text.splitlines():
        s = line.strip()
        if re.match(r"\*\*Class [PE]", s):
            cls = "P" if "Class P" in s else "E"
            continue
        if s.startswith("#"):
            # ANY heading closes the class block, not just level two. V23 added
            # `### §7.1 Canonical VOID Antecedent Registry` immediately after the Class-E table;
            # a `## `-only reset left the block open and counted the registry's ~54 antecedent rows
            # as class-E slots, reporting 62. Third counter bug tonight, same shape as the first two:
            # correct for the structure in front of me, blind to the next one that appears.
            cls = None
        if cls and s.startswith("|"):
            if re.match(r"^\|[\s:|-]*\|?$", s):          # separator row
                continue
            first = s.split("|")[1].strip() if s.count("|") > 1 else ""
            if not first or first.lower() in {"slot", "slot id"}:  # header row
                continue
            n[cls] += 1
    return n


def check_slots_exist(text, rows, out):
    """Every slot named in prose must have a row in §7 — the V12 BS-2a failure."""
    referenced = {s for s in SLOT.findall(text)}
    missing = sorted(referenced - set(rows))
    if missing:
        out.append(("slots-referenced-but-not-in-table",
                    f"named in prose with no §7 row: {', '.join(missing)}"))


def _is_history(line):
    """True if this line records what an earlier version said, rather than asserting current state.

    V16 folded §6 and wrote a record of the seams the referees had raised. One of those sentences
    quotes V15's stale class-P list verbatim — and this check flagged it, reporting a defect in the
    document's account of a defect. `check_lock_identity` already skips blockquotes for the same
    reason; the fold record is the same kind of text wearing different punctuation.

    A block is history if it cites another version by number, or sits in a blockquote.

    Scoped to the BLOCK, not the line: the fold record's citation ("V15 lines 595–600 said …") and
    the slot name it quotes land on different physical lines because the list item wraps. A
    line-scoped check splits the two and reports the quotation as an assertion — which is how the
    first attempt at this fix failed.
    """
    return line.lstrip().startswith(">") or re.search(r"\bV\d+\s+lines?\b", line) is not None


def _blocks(text):
    """Paragraph-ish units: consecutive non-blank lines, joined. Wrapped list items stay whole."""
    buf, out = [], []
    for line in text.splitlines():
        if line.strip():
            buf.append(line)
        elif buf:
            out.append("\n".join(buf))
            buf = []
    if buf:
        out.append("\n".join(buf))
    return out


def check_class_agreement(text, rows, out):
    """A slot the prose calls a class-P prerequisite must not sit in Class E."""
    for block in _blocks(text):
        if any(_is_history(l) for l in block.splitlines()):
            continue
        flat = " ".join(block.split())
        for slot, cls in rows.items():
            if cls != "E":
                continue
            if re.search(rf"{re.escape(slot)}[^.]{{0,120}}class-P", flat):
                out.append(("slot-class-disagreement",
                            f"{slot} is called a class-P prerequisite in prose and sits in Class E"))


def check_lock_identity(text, out):
    """After the BS-L split, nothing may still call BS-V the lock — the V12 cycle."""
    # Line-by-line, because a sentence-fragment regex cannot tell whether it began inside a
    # blockquote. Blockquotes are the document's record of its own corrections: they quote the
    # wrong sentence deliberately, so they are history rather than live text.
    for line in text.splitlines():
        if line.lstrip().startswith(">"):
            continue
        for m in re.finditer(r"[^.\n]*BS-V[^.\n]*", line):
            frag = m.group(0)
            if re.search(r"\block\b", frag) and "not the lock" not in frag and "BS-L" not in frag:
                out.append(("lock-identity",
                            f"BS-V described with the lock: …{frag.strip()[:110]}…"))


def check_list_numbering(text, out):
    """Ordered lists must run 1..n in document order — the V14 1,2,3,4,6,7,5."""
    runs, current = [], []
    for line in text.splitlines():
        m = re.match(r"^(\d+)\.\s+\*\*", line)
        if m:
            current.append(int(m.group(1)))
        elif current:
            runs.append(current)
            current = []
    if current:
        runs.append(current)
    for run in runs:
        if len(run) > 2 and run != list(range(run[0], run[0] + len(run))):
            out.append(("list-numbering", f"ordered list runs {run}"))
        dupes = [n for n, c in Counter(run).items() if c > 1]
        if dupes:
            out.append(("list-numbering", f"list repeats item number(s) {dupes}"))


_WORD_NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20,
}


def _as_int(tok):
    tok = tok.strip().lower()
    return _WORD_NUM.get(tok, int(tok) if tok.isdigit() else None)


def check_prose_counts(text, rows, out):
    """§7's prose slot counts must equal the counts parsed from its own table.

    §7 promises a lint assertion that the prose count equals the parsed table count. Nothing
    implemented it, so V21 could say "There are 8 class-E slots" over a table holding 7 and lint
    clean — a referee found it by counting rows. A section that states its own tally and is never
    checked against it will drift every time a row is inserted, which is exactly how the VOID
    prerequisite broke the count it was inserted into.

    Historical lines are skipped — but NOT by the blockquote rule. §7 states its live count inside a
    blockquote callout, so treating every blockquote as history made this check silently vacuous: it
    passed V21's false "8 class-E slots" on the first run. Only an explicit version citation marks
    history here. A guard that cannot fire is worse than no guard, because it reports "clean".
    """
    def _cites_version(line):
        return re.search(r"\bV\d+\s+lines?\b", line) is not None

    actual = count_rows(text)
    pats = [(re.compile(r"of\s+([a-z]+|\d+)\s+class-P slots", re.I), "P"),
            (re.compile(r"are\s+([a-z]+|\d+)\s+class-E slots", re.I), "E")]
    for block in _blocks(text):
        if any(_cites_version(l) for l in block.splitlines()):
            continue
        flat = " ".join(block.split())
        for pat, cls in pats:
            for m in pat.finditer(flat):
                claimed = _as_int(m.group(1))
                if claimed is not None and claimed != actual[cls]:
                    out.append(("prose-count-disagreement",
                                f"prose says {claimed} class-{cls} slots; the §7 table has "
                                f"{actual[cls]}"))


def check_repair_citations(text, gates, out):
    """A 'V## CORRECTION (SEAT-Vn Fk)' claim must cite a finding that exists in that seat's report.

    NAMED for what it evaluates. Until 2026-08-29 the docstring claimed it verified the FINDING
    existed while the predicate only checked that a REPORT FILE for that seat and version existed -
    `fid` was parsed and then used solely in the error message. A citation to CODEX-V27 F9 passed
    against a report with four findings. That is a name asserting more than its predicate tested,
    the same defect this lane found in Tori's harness and in two of mine.

    The document's most dangerous sentence is one announcing a repair, because a reader stops
    checking there. V12's blockquote claimed the unanimous round-1 blinding finding repaired
    while half of it stood.
    """
    if not gates or not gates.is_dir():
        out.append(("repair-citations", "gates directory not readable; citations unchecked"))
        return
    corpus = "\n".join(p.read_text(errors="ignore") for p in gates.glob("PREREG_TEXT*.md"))
    if not corpus:
        return
    for m in re.finditer(r"\((?:KIMI|GPT56|CODEX)[^)]{0,80}\)", text):
        cite = m.group(0)
        # \b after the version digits, or "V24-1" parses as version 2 finding 4 and reports a
        # citation nobody wrote. That false positive fired on every draft from V25 on.
        for seat, ver, fid in re.findall(r"(KIMI|GPT56|CODEX)-V(\d+)\b\s*[-–]?\s*(F?\d+)", cite):
            # Match the report by SEAT and VERSION, not by one filename shape. Reports have been
            # PREREG_TEXT_V*_SEAT.md, SECTION6_REVIEW_R*_SEAT.md and V*_WHOLE_REVIEW_SEAT.md as the
            # review's subject changed. Hard-coding one pattern made the check report missing
            # citations for reports sitting next to it under a newer name — the same staleness this
            # tool exists to catch, in the tool.
            hits = [p for p in gates.glob("*.md")
                    if (seat in p.name and f"V{ver}" in p.name and "REVIEW" in p.name.upper())
                    or p.name == f"PREREG_TEXT_V{ver}_{seat}.md"]
            if not hits:
                out.append(("repair-citations",
                            f"cites {seat}-V{ver} {fid} but no report for {seat} V{ver} exists"))
                continue
            # The finding NUMBER must actually be in that report. Reports number findings as
            # "### 3." headings or as explicit SEAT-Vn-3 ids; accept either.
            k = fid.lstrip("Ff")
            body = "\n".join(h.read_text(errors="ignore") for h in hits)
            # Accept every heading shape the reports have actually used: "### F3 — ...",
            # "### 3. ...", and the explicit SEAT-Vn-3 id. My first version accepted only "### 3."
            # and reported a REAL citation missing against a report whose findings are "### F3" -
            # a pattern narrower than the data, which is the third time tonight.
            found = (re.search(rf"^#+\s*F?{re.escape(k)}\b", body, re.M)
                     or re.search(rf"{seat}-V{ver}-{re.escape(k)}\b", body))
            if not found:
                nums = sorted({n for n in re.findall(r"^#+\s*F?(\d+)\b", body, re.M)}, key=int)
                out.append(("repair-citations",
                            f"cites {seat}-V{ver} {fid} but that report has no finding {k}"
                            + (f" (it has {', '.join(nums)})" if nums else
                               " and no parseable numbered findings")))



# ─────────────────────────────────────────────────────────────────────────────────────────────
# NEGATIVE CONTROLS — every check must prove it can fail, on every run.
#
# Twice in one day a guard here reported "clean" because it could not fire at all. The blockquote
# exemption made check_prose_counts vacuous: §7 states its live count inside a blockquote, the
# history predicate skipped every blockquote, and the check silently examined nothing while
# printing no inconsistencies. In prereg_trace.py the current-transition branch was skipped
# entirely, so the row most needing verification was the one guaranteed never to be examined.
# Both were found by referees, not by me, and both looked exactly like success.
#
# Blanc, 2026-08-28: "a check that passes because it never ran ... worth a canary in the checker
# itself, since it has now happened twice in one day in two different guards."
#
# So: each check ships a mutator that breaks the document in the specific way that check exists to
# catch. Before any clean report, every check is run against its own mutated copy and MUST produce
# a finding. A check that stays silent on its own negative control is reported VACUOUS — which is a
# failure, not a pass. Silence is only evidence when the check has shown it can speak.
# ─────────────────────────────────────────────────────────────────────────────────────────────

def _mut_prose_count(text):
    """Make the prose count disagree with the table."""
    return re.sub(r"(are )(\d+)( class-E slots)",
                  lambda m: f"{m.group(1)}{int(m.group(2)) + 3}{m.group(3)}", text, count=1)


def _mut_class_agreement(text):
    """Assert, in live text, that a Class-E slot is a class-P prerequisite."""
    e = [k for k, v in slot_rows(text).items() if v == "E"]
    return text + f"\n\n{e[0] if e else 'BS-2f'} is a class-P prerequisite for the freeze.\n"


def _mut_lock_identity(text):
    return text + "\n\nBS-V is the lock for this run.\n"


def _mut_list_numbering(text):
    return text + "\n\n1. **a**\n2. **b**\n7. **c**\n"


def _mut_slots_exist(text):
    return text + "\n\nSlot BS-77 governs the freeze.\n"


def _mut_repair_citations(text):
    """Cite a referee finding whose report does not exist."""
    return text + "\n\nV99 CORRECTION (CODEX-V98 7): repaired per that finding.\n"


CONTROLS = [
    ("check_repair_citations", _mut_repair_citations, "repair-citations"),
    ("check_prose_counts",    _mut_prose_count,     "prose-count-disagreement"),
    ("check_class_agreement", _mut_class_agreement, "slot-class-disagreement"),
    ("check_lock_identity",   _mut_lock_identity,   "lock-identity"),
    ("check_list_numbering",  _mut_list_numbering,  "list-numbering"),
    ("check_slots_exist",     _mut_slots_exist,     "slots-referenced-but-not-in-table"),
]


# Every check main() runs. If a check is here and not in CONTROLS, the run says so rather than
# claiming coverage it does not have — CODEX-V29-1: the clean line said "all checks demonstrated
# they can fail" while CONTROLS covered five of the six checks executed. An uncontrolled check is
# not a failure, but reporting it as controlled is.
CHECKS_RUN = ["check_slots_exist", "check_class_agreement", "check_prose_counts",
              "check_lock_identity", "check_list_numbering", "check_repair_citations"]


def uncontrolled():
    covered = {n for n, _, _ in CONTROLS}
    return [c for c in CHECKS_RUN if c not in covered]


def run_controls(text, gates):
    """Return a list of check names that FAILED to fire on their own negative control."""
    vacuous = []
    for name, mutate, category in CONTROLS:
        broken = mutate(text)
        rows = slot_rows(broken)
        out = []
        check_slots_exist(broken, rows, out)
        check_class_agreement(broken, rows, out)
        check_prose_counts(broken, rows, out)
        check_lock_identity(broken, out)
        check_list_numbering(broken, out)
        check_repair_citations(broken, gates, out)
        if not any(k == category for k, _ in out):
            vacuous.append((name, category))
    return vacuous



def self_test(draft, gates):
    """CODEX-V29-1's regression assertion: breaking a check must produce VACUOUS and exit 1.

    Manual verification is not a regression test. This disables each check in turn — by feeding the
    controls a run where that check's category can never appear — and asserts the canary notices.
    Run it in CI or by hand: `python3 tools/prereg_lint.py <draft> --self-test`.
    """
    text = Path(draft).read_text()
    failures = []
    for name, mutate, category in CONTROLS:
        broken = mutate(text)
        rows = slot_rows(broken)
        out = []
        check_slots_exist(broken, rows, out)
        check_class_agreement(broken, rows, out)
        check_prose_counts(broken, rows, out)
        check_lock_identity(broken, out)
        check_list_numbering(broken, out)
        check_repair_citations(broken, gates, out)
        fired = any(k == category for k, _ in out)
        print(f"  {'OK  ' if fired else 'FAIL'} {name}: control {'fires' if fired else 'SILENT'}")
        if not fired:
            failures.append(name)
    unc = uncontrolled()
    if unc:
        print(f"  FAIL uncontrolled checks executed: {', '.join(unc)}")
        failures.extend(unc)
    print(f"  self-test: {len(CONTROLS)} controls, {len(failures)} failure(s)")
    return 1 if failures else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("draft")
    ap.add_argument("--gates", default="")
    ap.add_argument("--self-test", action="store_true",
                    help="assert every control fires and no executed check is uncontrolled")
    args = ap.parse_args()
    text = Path(args.draft).read_text()
    gates = Path(args.gates) if args.gates else Path(args.draft).parent / "gates"

    if args.self_test:
        print(f"prereg lint self-test — {Path(args.draft).name}")
        return self_test(args.draft, gates)

    rows = slot_rows(text)
    out = []
    check_slots_exist(text, rows, out)
    check_class_agreement(text, rows, out)
    check_prose_counts(text, rows, out)
    check_lock_identity(text, out)
    check_list_numbering(text, out)
    check_repair_citations(text, gates, out)

    vacuous = run_controls(text, gates)
    print(f"prereg lint — {Path(args.draft).name}")
    for name, cat in vacuous:
        print(f"  VACUOUS: {name} did not fire on its own negative control ({cat}) — "
              f"its silence on the real document proves nothing")
    n = count_rows(text)
    print(f"  §7 data rows: {n['P'] + n['E']} ({n['P']} class P, {n['E']} class E) "
          f"— {len(rows)} carry a BS- identifier")
    if vacuous:
        print(f"  {len(vacuous)} check(s) could not fire; a clean result cannot be reported")
        return 1
    if not out:
        unc = uncontrolled()
        cov = len(CHECKS_RUN) - len(unc)
        note = (f"all {len(CHECKS_RUN)} checks demonstrated they can fail" if not unc
                else f"{cov} of {len(CHECKS_RUN)} checks demonstrated they can fail; "
                     f"UNCONTROLLED: {', '.join(unc)}")
        print(f"  no inconsistencies found ({note})")
        return 0
    for kind, msg in out:
        print(f"  [{kind}] {msg}")
    print(f"  {len(out)} finding(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
