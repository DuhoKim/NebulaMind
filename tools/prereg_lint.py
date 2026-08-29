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

sys.path.insert(0, str(Path(__file__).resolve().parent))
import citation_block_check as cbc

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


ADVISORY_CATEGORIES = {"repair-citation-legacy"}


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


# OPTION C, 2026-08-29. The principal ruled: "fix it so checker actually read it." The old check
# enumerated a report's findings with a regex and then concluded a cited finding was ABSENT - using
# a pattern to establish a negative, which is unsound by construction. It called CODEX-V4 F9
# fabricated because `_reports_for` demanded "REVIEW" in the filename and judged the citation
# against an unrelated report.
#
# Two things changed. Reports now DECLARE their findings in FINDINGS-BLOCK v1, so the judgement is
# encoded by its author instead of recovered by guessing. And reports are indexed BY THE BLOCKS THEY
# DECLARE rather than by filename pattern - which removes the original defect at its root, since no
# filename convention has to be guessed at all.
#
# Three categories, and only two of them block:
#   repair-citation-fabricated  - a well-formed block exists and does not declare the cited finding
#   repair-citation-malformed   - a report carries a block that does not parse; the format is
#                                 mandatory in the dispatch brief, so this is a real defect
#   repair-citation-legacy      - ADVISORY. No block for that seat/version: the ~30 historical
#                                 reports predate the format. The principal has NOT ruled on that
#                                 corpus, so this must not fail anything.
def _block_index(gates):
    """Map (SEAT, VERSION) -> declared finding numbers, by reading blocks, not filenames."""
    idx, malformed = {}, []
    for f in sorted(gates.glob("*.md")):
        body = f.read_text(errors="ignore")
        # The marker must sit at COLUMN 0. A dispatch brief carries the block TEMPLATE as an
        # indented code sample, and scanning for the marker anywhere indexed those templates and
        # reported them as malformed reports. Briefs are not reports. This is a structural test,
        # not a filename pattern - guessing filenames is precisely what made the previous check
        # call a real citation fabricated.
        if not any(line == cbc.OPEN for line in body.split("\n")):
            continue
        blk, why = cbc.parse_block(body)
        if blk is None:
            malformed.append((f.name, why))
        else:
            idx[(blk.seat, blk.version)] = set(blk.findings)
    return idx, malformed


def check_repair_citations(text, gates, out):
    """Verify every `SEAT-Vn k` repair citation against that report's DECLARED findings."""
    if not gates or not gates.is_dir():
        out.append(("repair-citation-legacy",
                    "ADVISORY: gates directory not readable; citations unchecked"))
        return
    idx, malformed = _block_index(gates)
    for name, why in malformed:
        out.append(("repair-citation-malformed",
                    f"{name} carries a FINDINGS-BLOCK that does not parse: {why}"))
    # Compound citations must be EXPANDED, not skipped. The document writes
    # "KIMI/GPT56-V11 F4" to attribute one finding to two seats, and the plain
    # SEAT-Vn-Fk pattern only ever saw the LAST seat - so a wrong first seat was
    # invisible. Hand-verification found exactly that: KIMI-V11 F4 is a §6.1
    # access finding, not the Stage-P one, and this check could not see it.
    # A citation the checker cannot parse must never be silently dropped.
    cites = []
    for m in re.finditer(r"\b((?:(?:GPT56|CODEX|KIMI)/)+)?(GPT56|CODEX|KIMI)[- ]V(\d+)[- ]F?(\d+)\b",
                         text):
        seats = [s for s in (m.group(1) or "").split("/") if s] + [m.group(2)]
        for s in seats:
            cites.append((s, "V" + m.group(3), int(m.group(4))))
    for seat, ver, k in cites:
        declared = idx.get((seat, ver))
        if declared is None:
            out.append(("repair-citation-legacy",
                        f"ADVISORY: {seat}-{ver} F{k} - no FINDINGS-BLOCK for that seat/version "
                        f"(pre-format report); citation neither verified nor disproved"))
        elif k not in declared:
            out.append(("repair-citation-fabricated",
                        f"{seat}-{ver} F{k} is cited but that report declares "
                        f"{sorted(declared) or 'no findings'}"))


def _reports_for(gates, seat, ver):
    """Reports for exactly this seat and version. The version needs a NUMERIC BOUNDARY: a plain
    `f"V{ver}" in name` let a citation to V1 be satisfied by V11_... files."""
    out = []
    for p in gates.glob("*.md"):
        n = p.name
        if seat not in n or not re.search(rf"V{ver}(?!\d)", n):
            continue
        if "REVIEW" in n.upper() or n == f"PREREG_TEXT_V{ver}_{seat}.md":
            out.append(p)
    return out


_GRAMMARS = (
    ("F",       re.compile(r"^#+\s*F(\d+)\b", re.M)),
    ("Finding", re.compile(r"^#+\s*Finding\s+(\d+)\b", re.M | re.I)),
    ("bare",    re.compile(r"^#+\s*(\d+)\.", re.M)),
    ("list",    re.compile(r"^\s{0,3}(\d+)\.\s+\*\*", re.M)),
)


def declared_findings(body: str):
    """Return ('recognised'|'unverifiable', numbers).

    Recognised requires EXACTLY ONE grammar inside the findings section, numbering contiguous from
    1. A mixed-grammar report, or one with holes, is UNVERIFIABLE - because there "not declared"
    cannot be told apart from "not parsed", and asserting either would be manufacturing a result.
    """
    m = re.search(r"^#+\s*.*finding.*$", body, re.M | re.I)
    if not m:
        return "unverifiable", set()
    region = body[m.end():]
    hits = {}
    for name, rx in _GRAMMARS:
        nums = {int(g) for g in rx.findall(region)}
        if nums:
            hits[name] = nums
    if len(hits) != 1:
        return "unverifiable", set()
    nums = next(iter(hits.values()))
    if sorted(nums) != list(range(1, max(nums) + 1)):
        return "unverifiable", nums
    return "recognised", nums


def citation_outcome(gates, seat, ver, k):
    """VERIFIED / FABRICATED / UNVERIFIABLE / NO-REPORT. Three real outcomes, not a binary."""
    hits = _reports_for(gates, seat, ver)
    if not hits:
        return "NO-REPORT", set()
    best = ("unverifiable", set())
    for h in hits:
        outcome, nums = declared_findings(h.read_text(errors="ignore"))
        if outcome == "recognised":
            if k in nums:
                return "VERIFIED", nums
            best = ("recognised", nums)
    if best[0] == "recognised":
        return "FABRICATED", best[1]
    return "UNVERIFIABLE", set()


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


def _mut_citation_fabricated(text):
    """Cite a number a WELL-PARSED report does not declare. This is the control the old canary
    lacked: it exercised only report-absence, so deleting the membership test left it green."""
    return text + "\n\nV99 CORRECTION (GPT56-V11 F97): fabricated.\n"


def _mut_citation_unverifiable(text):
    """Cite into a report whose grammar is not recognisable. Must report UNVERIFIABLE - not clean,
    and not a document defect. Absence-by-parse-miss is not absence."""
    return text + "\n\nV99 CORRECTION (CODEX-V21 F4): unparseable grammar.\n"


def _mut_repair_citations(text):
    """Cite a finding a REAL block does not declare. GPT56's V38 block declares exactly F1."""
    return text + "\n\nV99 CORRECTION (GPT56-V38 9): repaired per that finding.\n"


def _mut_compound_citation(text):
    """A compound citation's FIRST seat must be checked, not just the last."""
    return text + "\n\nV99 CORRECTION (GPT56/CODEX-V38 9): repaired per that finding.\n"


def _mut_indented_block_ignored(text):
    """An indented block (a brief's template) must not be indexed as a report."""
    return text + "\n\nV99 CORRECTION (GPT56-V38 9): repaired per that finding.\n"


def _mut_citation_legacy(text):
    """Cite a pre-format report: advisory, never a failure."""
    return text + "\n\nV99 CORRECTION (CODEX-V11 9): repaired per that finding.\n"


CONTROLS = [
    ("check_repair_citations", _mut_repair_citations, "repair-citation-fabricated"),
    ("citation legacy is advisory", _mut_citation_legacy, "repair-citation-legacy"),
    ("compound citation expanded", _mut_compound_citation, "repair-citation-fabricated"),
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
    covered = {c[0] for c in CONTROLS}
    return [c for c in CHECKS_RUN if c not in covered]


def run_controls(text, gates):
    """Return a list of check names that FAILED to fire on their own negative control."""
    vacuous = []
    for ctrl in CONTROLS:
        name, mutate, category = ctrl[0], ctrl[1], ctrl[2]
        want = ctrl[3] if len(ctrl) > 3 else None
        broken = mutate(text)
        rows = slot_rows(broken)
        out = []
        check_slots_exist(broken, rows, out)
        check_class_agreement(broken, rows, out)
        check_prose_counts(broken, rows, out)
        check_lock_identity(broken, out)
        check_list_numbering(broken, out)
        check_repair_citations(broken, gates, out)
        # The OUTCOME, not merely the category. Asserting "a repair-citations message appeared" let
        # a neutered parser pass both citation controls at once, because UNVERIFIABLE and
        # FABRICATED share a category. That is the same defect the controls exist to catch.
        if not any(k == category and (want is None or want in m) for k, m in out):
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
    for ctrl in CONTROLS:
        name, mutate, category = ctrl[0], ctrl[1], ctrl[2]
        want = ctrl[3] if len(ctrl) > 3 else None
        broken = mutate(text)
        rows = slot_rows(broken)
        out = []
        check_slots_exist(broken, rows, out)
        check_class_agreement(broken, rows, out)
        check_prose_counts(broken, rows, out)
        check_lock_identity(broken, out)
        check_list_numbering(broken, out)
        check_repair_citations(broken, gates, out)
        fired = any(k == category and (want is None or want in m) for k, m in out)
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
    # Lifecycle derivation (GPT56-V72 F1: the predicate existed and was not wired into this battery,
    # so a stale pin left the advertised battery green - an unwired check is an unstated spec, one
    # level up). Blocking. Runs only when the spec exists beside the draft.
    spec = Path(args.draft).parent / "LIFECYCLE_GUARANTEE_SPEC.md"
    if not spec.exists():
        # GPT56-V73 F3 / CODEX-V73 F5: a silent skip on the missing companion is the unwired-check
        # defect re-entering through the file system - the battery must go red, not quiet.
        out.append(("lifecycle-derivation-L00",
                    "LIFECYCLE_GUARANTEE_SPEC.md is MISSING beside the draft - the derivation "
                    "cannot be checked, and unchecked is not passed"))
    # The refusal-checker digest quoted in the draft has gone stale three times, each time because
    # a later edit to the checker in the same build cycle postdated the hand-update. The rule
    # "compute it last" survives only as a mechanism (GPT56-V74 F4, CODEX-V74 F5): recompute and
    # compare, blocking on mismatch.
    import hashlib as _hl, re as _re
    _ck = Path(__file__).resolve().parent / "refusal_vocabulary_check.py"
    if _ck.exists():
        _live = _hl.sha256(_ck.read_bytes()).hexdigest()[:16]
        _m = _re.search(r"`([0-9a-f]{16})…` is the sha256 of `tools/refusal_vocabulary_check\.py`", text)
        if _m and _m.group(1) != _live:
            out.append(("checker-digest-stale",
                        f"the draft claims refusal-checker digest {_m.group(1)}… but the live file "
                        f"is {_live}… — the compute-it-last rule, mechanised after three manual "
                        f"violations"))
    if spec.exists():
        try:
            from lifecycle_derivation_check import check as _lc_check
        except ImportError:
            import sys as _s
            _s.path.insert(0, str(Path(__file__).resolve().parent))
            from lifecycle_derivation_check import check as _lc_check
        for code, msg in _lc_check(text, spec.read_text(), spec.read_bytes()):
            out.append((f"lifecycle-derivation-{code}", msg))
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
    blocking = [k for k, _ in out if k not in ADVISORY_CATEGORIES]
    print(f"  {len(out)} finding(s), {len(blocking)} blocking "
          f"({len(out) - len(blocking)} advisory)")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
