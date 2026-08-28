#!/usr/bin/env python3
"""PREREG TRACE — generate §10's revision trace from the diffs, instead of writing prose about it.

WHY THIS EXISTS
---------------
Blanc, 2026-08-28:

    gpt56 records the V16→V17 row as ACCURATE in V20, ACCURATE in V21, then NOT ACCURATE in V22.
    Nobody edited that row. Later edits made a previously true statement false.

    §10 grows one trace row per round — six by V22 — each a fresh assertion about history that a
    later edit can invalidate. The document is generating self-description obligations faster than
    it closes them.

That is the describe-versus-compute law applied to a document's account of itself. Twenty-one gates
established that self-describing prose always falls and self-computing checks never did.

THE DESIGN DECISION THAT MATTERS
--------------------------------
This emits **what changed**, never **what the change accomplished**.

"Repaired the Class E count from 7 to 8" is a characterisation. It was true when written, and became
false when a later round revealed the table had held 8 all along — the sentence did not change, the
world around it did. A characterisation carries an implicit claim about correctness, and correctness
is exactly what later evidence revises.

"§7: 1 line changed; class-E count 7 → 8" is an observation. It cannot go stale, because it says only
what the bytes did. Whether that was a repair or a regression is a finding, and findings live in the
referee reports where they can be superseded without rewriting history.

So: sections touched, line counts, digest chain, and any §7 count transitions — all computed. Intent
is referenced by finding ID only, never restated.

    python3 tools/prereg_trace.py <dir>                    # emit the trace table
    python3 tools/prereg_trace.py <dir> --check <draft>    # compare against the draft's §10

Exit 0 clean, 1 if --check finds the written trace disagrees with the computed one.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prereg_lint import count_rows  # noqa: E402

DRAFT = re.compile(r"PREREG_SUCCESSOR_DRAFT_V(\d+)_(\d+)\.md$")
HEADING = re.compile(r"^#{2,3}\s+(§[\d.]+|[A-Za-z].*)")


def drafts(d: Path):
    """Every draft in the directory, ordered by version number."""
    found = []
    for p in sorted(d.glob("PREREG_SUCCESSOR_DRAFT_V*.md")):
        m = DRAFT.search(p.name)
        if m:
            found.append((int(m.group(1)), p))
    return [p for _, p in sorted(found)]


def sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def section_of(lines, idx):
    """The nearest §-heading at or above line idx — which section a changed line sits in."""
    for i in range(idx, -1, -1):
        m = HEADING.match(lines[i])
        if m:
            t = m.group(1)
            return t.split()[0] if t.startswith("§") else t[:28]
    return "(preamble)"


def changed_sections(a_text, b_text):
    """Map section -> (added, removed), computed from a real line diff."""
    a, b = a_text.splitlines(), b_text.splitlines()
    stats = {}
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        for j in range(j1, j2):
            s = section_of(b, j)
            stats.setdefault(s, [0, 0])[0] += 1
        for i in range(i1, i2):
            s = section_of(a, i)
            stats.setdefault(s, [0, 0])[1] += 1
    return stats


def count_transition(a_text, b_text):
    """§7 class counts before and after — the invariant that reopened at V22."""
    a, b = count_rows(a_text), count_rows(b_text)
    bits = []
    for cls in ("P", "E"):
        if a[cls] != b[cls]:
            bits.append(f"class-{cls} rows {a[cls]} → {b[cls]}")
    return "; ".join(bits) or "no row-count change"


def build(d: Path):
    ds = drafts(d)
    rows = []
    for prev, cur in zip(ds, ds[1:]):
        pt, ct = prev.read_text(), cur.read_text()
        stats = changed_sections(pt, ct)
        # NO SILENT CAP. The first version showed the six largest and dropped the rest without
        # saying so, and CODEX found it: "sections changed silently truncates". A table that omits
        # what it omits reads as complete. Emit every changed section; if that is long, it is long.
        ordered = sorted(stats.items(), key=lambda kv: -sum(kv[1]))
        touched = ", ".join(f"{s} (+{a}/−{r})" for s, (a, r) in ordered)
        rows.append({
            "from": DRAFT.search(prev.name).group(1),
            "to": DRAFT.search(cur.name).group(1),
            "from_sha": sha(prev)[:16],
            "to_sha": sha(cur)[:16],
            "touched": touched or "(no textual change)",
            "counts": count_transition(pt, ct),
        })
    return rows


def load_findings(d: Path):
    """Human-supplied finding IDs per transition, from FINDINGS_MAP.md in the gates directory.

    Format, one per line:   V22→V23: CODEX-V22-1, GPT56-V22-3

    This half is NOT generated, and the distinction is the whole design. Blanc, 2026-08-28,
    correcting the advice that produced the first version:

        The COUNTS are a pure function of the table and should be computed. The TRACE is not. It is
        part mechanical — which bytes changed — and part semantic — which finding a change answers.
        Your prereg_trace.py says so itself: it deliberately does not characterise whether a change
        was a repair, because that is a finding. The semantic half does not survive being computed.

    Generating the whole table dropped the finding→change map §6.3 mandates, and both referee seats
    faulted it independently. So: the tool computes the bytes and *enforces* that a human has
    attached a finding to every substantive change. Enforcing the obligation mechanically was the
    actual point; discharging it mechanically was the error.
    """
    p = d / "gates" / "FINDINGS_MAP.md"
    if not p.exists():
        p = d / "FINDINGS_MAP.md"
    fm = {}
    if p.exists():
        for line in p.read_text().splitlines():
            m = re.match(r"\s*V(\d+)\s*(?:→|->)\s*V(\d+)\s*:\s*(.+?)\s*$", line)
            if m:
                fm[(m.group(1), m.group(2))] = m.group(3).strip()
    return fm


def render(rows, findings=None):
    findings = findings or {}
    out = ["| transition | predecessor sha256 (16) | result sha256 (16) | sections changed (+added/−removed) | §7 row counts | findings answered |",
           "|---|---|---|---|---|---|"]
    for r in rows:
        fid = findings.get((r["from"], r["to"]), "**— none cited —**")
        out.append(f"| V{r['from']} → V{r['to']} | `{r['from_sha']}` | `{r['to_sha']}` | "
                   f"{r['touched']} | {r['counts']} | {fid} |")
    out.append("")
    out.append("*Byte-level columns generated by `tools/prereg_trace.py` — digests by sha256, "
               "sections and line counts by diff, row counts by parsing the §7 table. The "
               "**findings answered** column is human-supplied from `gates/FINDINGS_MAP.md` and is "
               "NOT generated: which finding a change answers is a judgement, and the tool refuses "
               "to make it. The tool does enforce it — a transition that changes a normative section "
               "while citing no finding is a failure, which is how §6.3's finding→change obligation "
               "is checked rather than asserted.*")
    out.append("")
    out.append("*A draft cannot describe the transition that created it: the row for V(n−1) → V(n) "
               "would change V(n)'s bytes and therefore its own digest. Each draft's table covers "
               "transitions up to its predecessor; the transition that produced it appears in the "
               "next draft. This is a property of self-reference, not an omission.*")
    return "\n".join(out)



def trace_table(text):
    """Just the §10 transition-table rows — not the whole document.

    GPT56-V27-3: the presence test searched the entire document, so §6.3's prose sentence "The
    V24→V25 mapping must..." satisfied it and masked a missing table row. The endpoint test ORed
    both digests across the whole document, and V24's digest already appears as the *result* of the
    preceding row. Two rows were absent; the checker reported one.

    A check that passes for the wrong reason is worse than one that fails, because it certifies.
    """
    rows, inside = [], False
    for line in text.splitlines():
        st = line.strip()
        if st.startswith("## ") and "§10" in st:
            inside = True
            continue
        if inside and st.startswith("## ") and "§10" not in st:
            break
        if inside and st.startswith("|") and re.search(r"V\d+\s*(?:→|->)\s*V\d+", st):
            rows.append(st)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dir")
    ap.add_argument("--check", help="draft whose written §10 trace should agree with the computed one")
    args = ap.parse_args()

    d = Path(args.dir)
    rows = build(d)
    if not rows:
        print("no consecutive draft pairs found")
        return 1

    findings = load_findings(d)

    if not args.check:
        print(render(rows, findings))
        return 0

    text = Path(args.check).read_text()
    bad = 0
    print(f"prereg trace check — {Path(args.check).name}")
    table = trace_table(text)
    subj = DRAFT.search(Path(args.check).name)
    subj_v = int(subj.group(1)) if subj else None
    for r in rows:
        if int(r["to"]) <= 15 or (subj_v is not None and int(r["to"]) >= subj_v):
            continue
        # A written row may say anything; what it must not do is contradict a computed digest.
        pat = re.compile(rf"V{r['from']}\s*(?:→|->|to)\s*V{r['to']}\b")
        row = next((t for t in table if pat.search(t)), None)
        if row is None:
            print(f"  MISSING: no §10 table row for V{r['from']} → V{r['to']}")
            bad += 1
            continue
        # The RESULT digest, in THAT row — not either endpoint anywhere in the document.
        if r["to_sha"][:12] not in row:
            print(f"  UNPINNED: V{r['from']} → V{r['to']} row does not carry its result digest")
            bad += 1

    # §6.3's obligation, enforced rather than asserted: a transition that touched a normative
    # section must name the finding it answers. Sections whose whole purpose is bookkeeping are
    # exempt — §10 is the trace itself, and the preamble carries banners.
    BOOKKEEPING = {"§10", "(preamble)"}
    # COVERAGE CONTRACT, encoded here rather than asserted in prose (GPT56-V26-4):
    #   * in-band  — the draft's own table covers transitions up to its PREDECESSOR only. A draft
    #                cannot describe the transition that created it; that row would change its bytes
    #                and therefore its own digest.
    #   * sidecar  — the current transition is mapped in gates/FINDINGS_MAP.md, outside the draft.
    #   * historic — V1→V15 predate this lane's referee record and are exempt by rule, not by
    #                silence. Naming the exemption is the difference between a gap and an omission.
    HISTORIC_EXEMPT_BEFORE = 15
    subject_ver = None
    m = DRAFT.search(Path(args.check).name)
    if m:
        subject_ver = int(m.group(1))
    for r in rows:
        if int(r["to"]) <= HISTORIC_EXEMPT_BEFORE:
            continue                      # exempt by stated rule
        if subject_ver is not None and int(r["to"]) >= subject_ver:
            # In-band coverage stops at the predecessor — but the sidecar OWNS this transition, so
            # it must still be checked there. The first version skipped it entirely, which meant the
            # one row that most needs verifying was the one guaranteed never to be examined: a guard
            # that cannot fire, reporting clean. Both seats caught it (GPT56-V27-1 CRITICAL,
            # CODEX-V27-1). Same shape as the blockquote exemption that silently voided the count
            # check earlier today.
            if (r["from"], r["to"]) not in findings:
                print(f"  SIDECAR MISSING: V{r['from']} → V{r['to']} is the current transition and "
                      f"is not mapped in gates/FINDINGS_MAP.md")
                bad += 1
            continue
        normative = [s_ for s_ in re.findall(r"(§[\d.]+|\(preamble\))", r["touched"])
                     if s_ not in BOOKKEEPING]
        if normative and (r["from"], r["to"]) not in findings:
            print(f"  NO FINDING CITED: V{r['from']} → V{r['to']} changed {', '.join(normative[:4])} "
                  f"but gates/FINDINGS_MAP.md names no finding")
            bad += 1
    print(f"  {len(rows)} computed transition(s); {bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
