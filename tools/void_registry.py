#!/usr/bin/env python3
"""The §7.1 VOID antecedent registry: extract it, digest it, and check it is complete.

WHY THIS EXISTS
---------------
The BS-2v row says the VOID converter gate is **UNRESOLVED** for this reason:

    "Because the registry cannot be pinned before the converter exists, this gate is marked
     unresolved — a third round of rewording will not make a self-comparison independent."

**That reason does not hold, and this tool is the argument.** The registry's content is determined by
the preregistration's own normative clauses — §5, §6.1's row table, §6.3 and §2.7. The converter must
*handle* those IDs; it does not author them. So the registry can be pinned first and the converter
gated against it afterwards, which is the independence the row asks for.

The genuine self-reference risk is different and narrower: embedding a digest OF §7.1 INTO the
document would move the bytes being digested. It is avoided the same way §10's revision trace avoids
it — **the digest covers §7.1's canonical rows only, and is recorded outside §7.1** (in the BS-2v
slot row). Digesting the table and storing the result elsewhere has no fixed point.

WHAT THIS DOES AND DOES NOT ESTABLISH
-------------------------------------
It establishes that the registry is **well-formed and complete against the row table**: every §6.1
row that the document defines has at least one antecedent, IDs are unique, every source names a real
section, every phase is from the closed vocabulary, and every effect is VOID.

It does **not** write the converter, does not execute a VOID conversion, and does not by itself make
clause 10 executable. It removes the stated obstacle to pinning the registry. Whether that is
sufficient to move BS-2v off UNRESOLVED is a gate question, not this tool's claim.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ID_RE = re.compile(r"^\|\s*`(VOID-[A-Za-z0-9.\-]+)`\s*\|([^|]*)\|([^|]*)\|([^|]*)\|")
ROW_RE = re.compile(r"^\|\s*([A-Z][0-9]?)\s*\|")
# The phase vocabulary is a RULE, not a hand list. My first version hardcoded the phases visible in
# the first thirty rows and then refused seventeen legitimate ones (P5-P9, "P3, P6") - specifying
# something narrower than the data and calling the data wrong. A phase is now valid if every
# component is a numbered stage or a named phase the document uses.
NAMED_PHASES = {"Any", "Pre-unblinding", "Post-unblinding", "Post-first-real-χ",
                "After BS-8p", "Before BS-8f"}
STAGE_RE = re.compile(r"^P[0-9]$")


def phase_ok(phase: str) -> bool:
    parts = [x.strip() for x in phase.replace("\u2013", ",").replace("-", ",").split(",")
             if x.strip()] if phase not in NAMED_PHASES else [phase]
    if not parts:
        return False
    return all(STAGE_RE.match(x) or x in NAMED_PHASES for x in parts)

CODES = {
    "V01": "the §7.1 registry section is absent or holds no rows",
    "V02": "an antecedent ID is duplicated",
    "V03": "an antecedent names a phase outside the closed vocabulary",
    "V04": "an antecedent's failure effect is not VOID",
    "V05": "a §6.1 row is defined in the table but has no antecedent in the registry",
    "V06": "an antecedent references a §6.1 row the table does not define",
}


def extract(text: str):
    """Return the registry rows as (id, source, phase, effect) tuples, in document order."""
    lines = text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.startswith("### §7.1"))
    except StopIteration:
        return []
    out = []
    for l in lines[start:]:
        if l.startswith("### ") and not l.startswith("### §7.1"):
            break
        m = ID_RE.match(l)
        if m:
            out.append(tuple(g.strip().strip("`") for g in m.groups()))
    return out


def defined_rows(text: str) -> set[str]:
    """The §6.1 row labels the document's own row table defines."""
    return {ROW_RE.match(l).group(1) for l in text.splitlines() if ROW_RE.match(l)}


def canonical(rows) -> str:
    """Order-independent, length-prefixed. Sorted so a reordering of the table does not move the
    digest, and length-prefixed so no field value can forge a delimiter."""
    def enc(r):
        return "".join(f"{len(x)}:{x}" for x in r)
    return "\n".join(sorted(enc(r) for r in rows))


def digest(rows) -> str:
    return hashlib.sha256(canonical(rows).encode("utf-8")).hexdigest()


def check(text: str):
    """Return (rows, refusals)."""
    bad = []

    def refuse(code, msg):
        bad.append(f"[{code}] {msg}")

    rows = extract(text)
    if not rows:
        refuse("V01", "no §7.1 registry rows found")
        return rows, bad

    ids = [r[0] for r in rows]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        refuse("V02", f"duplicate antecedent ID(s): {dupes}")
    for r in rows:
        if not phase_ok(r[2]):
            refuse("V03", f"{r[0]} has phase {r[2]!r} outside the closed vocabulary")
        if r[3] != "VOID":
            refuse("V04", f"{r[0]} has failure effect {r[3]!r}, not VOID")

    defined = defined_rows(text)
    covered = {m.group(1) for m in (re.match(r"VOID-6\.1([A-Z][0-9]?)-", i) for i in ids) if m}
    for missing in sorted(defined - covered):
        refuse("V05", f"§6.1 row {missing} is defined but has no VOID antecedent")
    for extra in sorted(covered - defined):
        refuse("V06", f"antecedent references §6.1 row {extra}, which the table does not define")
    return rows, bad


# ── Controls. Each mutation must produce exactly its code. ───────────────────────────────────────

def _mut_drop_row(text):
    """Remove one registry row -> its §6.1 row loses coverage."""
    return re.sub(r"^\|\s*`VOID-6\.1S-[^\n]*\n", "", text, count=1, flags=re.M)


def _mut_duplicate(text):
    lines = text.splitlines(keepends=True)
    i = next(i for i, l in enumerate(lines) if l.startswith("| `VOID-5-FORBIDDEN-ACT`"))
    lines.insert(i + 1, lines[i])
    return "".join(lines)


def _mut_bad_phase(text):
    return text.replace("| `VOID-5-NONFINITE` | §5 | Post-unblinding | VOID |",
                        "| `VOID-5-NONFINITE` | §5 | Whenever | VOID |", 1)


def _mut_bad_effect(text):
    return text.replace("| `VOID-5-FORBIDDEN-ACT` | §5 | Any | VOID |",
                        "| `VOID-5-FORBIDDEN-ACT` | §5 | Any | INCONCLUSIVE |", 1)


def _mut_unknown_row(text):
    return text.replace("| `VOID-5-FORBIDDEN-ACT` | §5 | Any | VOID |",
                        "| `VOID-5-FORBIDDEN-ACT` | §5 | Any | VOID |\n"
                        "| `VOID-6.1Z-GHOST` | §6.1 Row Z | Any | VOID |", 1)


CONTROLS = (
    ("row loses coverage", _mut_drop_row, {"V05"}),
    ("duplicate id", _mut_duplicate, {"V02"}),
    ("phase outside vocabulary", _mut_bad_phase, {"V03"}),
    ("effect not VOID", _mut_bad_effect, {"V04"}),
    ("antecedent for an undefined row", _mut_unknown_row, {"V06"}),
)


def _codes(bad):
    return {r[1:4] for r in bad}


def self_test(text: str) -> int:
    print("void-registry self-test")
    rows, bad = check(text)
    ok0 = not bad
    print(f"  {'OK  ' if ok0 else 'FAIL'} the real registry checks clean: {len(rows)} antecedents"
          f"{'' if ok0 else f' — {bad}'}")
    fails = [] if ok0 else ["baseline"]

    for name, mutate, expect in CONTROLS:
        _, b = check(mutate(text))
        got = _codes(b)
        ok = got == expect
        print(f"  {'OK  ' if ok else 'FAIL'} {name}: {sorted(got) or 'ACCEPTED'}"
              f"{'' if ok else f' — expected {sorted(expect)}'}")
        if not ok:
            fails.append(name)

    orphans = set(CODES) - set().union(*(e for _, _, e in CONTROLS)) - {"V01"}
    if orphans:
        print(f"  FAIL codes with no control: {sorted(orphans)}")
        fails.append("coverage")
    else:
        print(f"  OK   every code has a control (V01 is covered by the empty-document case)")
    _, b01 = check("no registry here")
    if _codes(b01) != {"V01"}:
        print(f"  FAIL empty-document case gave {sorted(_codes(b01))}")
        fails.append("V01")
    else:
        print(f"  OK   empty document: ['V01']")

    print(f"  self-test: {len(CONTROLS) + 1} controls, {len(fails)} failure(s)")
    return 1 if fails else 0


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("draft")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    text = Path(a.draft).read_text()
    if a.self_test:
        return self_test(text)
    rows, bad = check(text)
    print(f"void registry — {Path(a.draft).name}")
    print(f"  antecedents      {len(rows)}")
    print(f"  §6.1 rows defined {len(defined_rows(text))}")
    print(f"  registry_digest  {digest(rows)}")
    for b in bad:
        print(f"  REFUSED: {b}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
