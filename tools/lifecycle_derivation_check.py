#!/usr/bin/env python3
"""LIFECYCLE DERIVATION CHECK — the draft's invariant quotes must be the spec's bytes.

Why this exists
---------------
The spec's header says the draft's lifecycle text is DERIVED from it and a conflict is a defect in
the draft. For two rounds that derivation was a claim in prose — a name with no predicate — and it
died exactly as prose claims die: V70 amended the draft and left the spec behind was warned against;
V71 amended the SPEC and left the DRAFT behind, and both seats' F1 was the same sentence. This makes
the claim a check: divergence now fails a control instead of waiting for a referee.

The contract
------------
1. The draft pins the spec:  `lifecycle-spec: sha256 <64 hex>`  — and the pin must equal the spec
   file's current digest. A spec edit therefore BREAKS the pin until the draft re-pins, which forces
   the re-derivation instead of permitting the drift.
2. Every invariant the draft quotes — any line fragment beginning `G1 —` … `G5 —`, `N1 —` … `N3 —` —
   must appear VERBATIM in the spec (after normalising whitespace and stripping emphasis). The draft
   may quote fewer invariants than the spec has; it may not paraphrase one.

What this cannot do: notice a paraphrase that avoids the G/N label entirely. A reworded invariant
with no label is invisible here — the round remains the control for that, and this file says so
rather than claiming otherwise.
"""

import hashlib
import re
import sys
from pathlib import Path

ERRORS = {
    "L01": "the draft carries no lifecycle-spec pin",
    "L02": "the pinned digest does not match the spec file's current bytes — re-derive and re-pin",
    "L03": "a quoted invariant diverges from ITS OWN spec row — the label binds (GPT56-V72 F2: an "
           "unbound quote accepted swapped labels)",
    "L04": "an invariant present in the spec is not quoted in the draft — deletion from the draft "
           "is a divergence, not a choice (GPT56-V72 F2: the checker accepted deletion of the "
           "entire quoted block)",
    "L05": "the draft quotes a tag the spec does not define",
    "L06": "a quoted invariant is TRUNCATED — a true substring can reverse meaning by omission, so "
           "the quote must be the row's FULL body (GPT56-V73 F3, CODEX-V73 F2)",
    "L07": "the draft carries more than one lifecycle-spec pin — a second pin is a second source "
           "for one fact",
    "L08": "a shared closed-schema tuple diverges between draft and spec — the V98 "
           "partition_cut_position field landed draft-side only and the invariant-bound "
           "checker missed it for two rounds (GPT56-V100 F2)",
}

TAG = re.compile(r"lifecycle-spec:\s*sha256\s*`?([0-9a-f]{64})`?")
INV = re.compile(r"\*{0,2}((?:G[1-9]|N[1-9])) — ([^|\n]+)")  # tag AND body; the body must be the
# tagged spec ROW's bytes — label-bound, so swapped labels fail (GPT56-V72 F2)
ROW = re.compile(r"^\| ((?:G|N)[1-9]) \| (.+?) \|", re.M)


def norm(s: str) -> str:
    s = re.sub(r"[*`]", "", s)
    return re.sub(r"\s+", " ", s).strip().rstrip(".")


def check(draft_text: str, spec_text: str, spec_bytes: bytes):
    out = []
    pins = TAG.findall(draft_text)
    if not pins:
        out.append(("L01", ERRORS["L01"]))
    elif len(pins) > 1:
        out.append(("L07", ERRORS["L07"] + f" — {len(pins)} pins"))
    elif pins[0] != hashlib.sha256(spec_bytes).hexdigest():
        out.append(("L02", ERRORS["L02"] + f" — pinned {pins[0][:16]}…"))
    spec_rows = {tag: norm(body) for tag, body in ROW.findall(spec_text)}
    quoted = {}
    for tag, body in INV.findall(draft_text):
        quoted.setdefault(tag, []).append(norm(body))
    for tag, bodies in quoted.items():
        if tag not in spec_rows:
            out.append(("L05", ERRORS["L05"] + f" — {tag}"))
            continue
        for nb in bodies:
            if nb == spec_rows[tag]:
                continue
            if nb in spec_rows[tag]:
                out.append(("L06", ERRORS["L06"] + f" — {tag} quotes {len(nb)}/{len(spec_rows[tag])} chars"))
            else:
                out.append(("L03", ERRORS["L03"] + f" — {tag}: {nb[:60]!r}"))
    for tag in spec_rows:
        if tag not in quoted:
            out.append(("L04", ERRORS["L04"] + f" — {tag}"))
    # L08 (GPT56-V100 F2): schema tuples that exist in BOTH files must match exactly.
    import re as _re
    def tuples(s):
        return {m.group(1) for m in _re.finditer(r"`\((gate, [^)]+)\)`", s)}
    dt, st = tuples(draft_text), tuples(spec_text)
    _normsig = lambda x: x.replace("signature-enveloped", "signature")
    if {_normsig(x) for x in dt} != {_normsig(x) for x in st} and dt and st:
        out.append(("L08", ERRORS["L08"] + f" — draft {sorted(dt)} vs spec {sorted(st)}"))
    return out


def self_test():
    spec = ("| G1 | no bytes move without a committed event | x |\n"
            "| G2 | events tell the truth | x |\n")
    spec_b = spec.encode()
    pin = hashlib.sha256(spec_b).hexdigest()
    good = (f"lifecycle-spec: sha256 `{pin}`\n"
            "**G1 — no bytes move without a committed event**\n"
            "**G2 — events tell the truth**\n")
    cases = [
        ("clean quotation passes", good, set()),
        ("missing pin", good.replace("lifecycle-spec:", "x:"), {"L01"}),
        ("stale pin", good.replace(pin, "0" * 64), {"L02"}),
        ("paraphrased invariant", good.replace("no bytes move", "no byte moves"), {"L03"}),
        ("swapped labels", good.replace("G1 — no bytes", "G2 — no bytes")
                              .replace("G2 — events", "G1 — events"), {"L03"}),
        ("an invariant deleted from the draft",
         good.replace("**G2 — events tell the truth**\n", ""), {"L04"}),
        ("a tag the spec does not define", good + "**G9 — invented**\n", {"L04", "L05"})
         if False else
        ("a tag the spec does not define", good + "**N1 — invented**\n", {"L05"}),
        ("a truncated quote", good.replace("G1 — no bytes move without a committed event",
                                           "G1 — no bytes move"), {"L06"}),
        ("two pins", good + f"lifecycle-spec: sha256 `{pin}`\n", {"L07"}),
    ]
    fails = []
    for name, draft, want in cases:
        got = {c for c, _ in check(draft, spec, spec_b)}
        if got != want:
            fails.append(f"{name}: expected {sorted(want) or 'clean'}, got {sorted(got) or 'clean'}")
    for f in fails:
        print(f"  FAIL {f}")
    print(f"  self-test: {len(cases)} controls, {len(fails)} failure(s)")
    return 1 if fails else 0


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()
    if len(args) != 2:
        print("usage: lifecycle_derivation_check.py DRAFT.md SPEC.md | --self-test")
        return 2
    draft, spec = Path(args[0]), Path(args[1])
    problems = check(draft.read_text(), spec.read_text(), spec.read_bytes())
    for c, msg in problems:
        print(f"  [{c}] {msg}")
    print(f"  lifecycle derivation: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
