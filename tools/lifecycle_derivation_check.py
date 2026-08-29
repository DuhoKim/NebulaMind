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
    "L03": "a quoted invariant diverges from the spec's text",
}

TAG = re.compile(r"lifecycle-spec:\s*sha256\s*`?([0-9a-f]{64})`?")
INV = re.compile(r"\*{0,2}(?:G[1-5]|N[1-3]) — ([^|\n]+)")  # the BODY after the tag must be spec bytes;
# the tag+dash form is the draft's quotation marker, while the spec keeps tag and body in table cells


def norm(s: str) -> str:
    s = re.sub(r"[*`]", "", s)
    return re.sub(r"\s+", " ", s).strip().rstrip(".")


def check(draft_text: str, spec_text: str, spec_bytes: bytes):
    out = []
    m = TAG.search(draft_text)
    if not m:
        out.append(("L01", ERRORS["L01"]))
    elif m.group(1) != hashlib.sha256(spec_bytes).hexdigest():
        out.append(("L02", ERRORS["L02"] + f" — pinned {m.group(1)[:16]}…"))
    spec_norm = norm(spec_text)
    for frag in INV.findall(draft_text):
        n = norm(frag)
        # a quote may be a truncation of the spec line, but its full extent must be spec bytes
        if n not in spec_norm:
            out.append(("L03", ERRORS["L03"] + f" — {n[:70]!r}"))
    return out


def self_test():
    spec = "| G1 — NO UNLOGGED TOUCH: no bytes move without a committed event | x |\n"
    spec_b = spec.encode()
    pin = hashlib.sha256(spec_b).hexdigest()
    good = f"lifecycle-spec: sha256 `{pin}`\nquote: **G1 — NO UNLOGGED TOUCH: no bytes move without a committed event**\n"
    cases = [
        ("clean quotation passes", good, set()),
        ("missing pin", good.replace("lifecycle-spec:", "x:"), {"L01"}),
        ("stale pin", good.replace(pin, "0" * 64), {"L02"}),
        ("paraphrased invariant", good.replace("no bytes move", "no byte moves"), {"L03"}),
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
