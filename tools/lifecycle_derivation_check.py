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
    "L08": "one schema, divergent occurrences — same field/constraint content in a "
           "different order, across or within files (strike three's rebuild: the four seeded "
           "controls are the spec, this sentence is the summary)",
    "L09": "a schema tuple carries a field the registry does not know — a rename's "
           "fingerprint (GPT56-V104 F2: a one-file rename left the intersection and passed)",
}

TAG = re.compile(r"lifecycle-spec:\s*sha256\s*`?([0-9a-f]{64})`?")
INV = re.compile(r"\*{0,2}((?:G[1-9]|N[1-9]|T[1-9])) — ([^|\n]+)")  # tag AND body; the body must be the
# tagged spec ROW's bytes — label-bound, so swapped labels fail (GPT56-V72 F2)
ROW = re.compile(r"^\| ((?:G|N|T)[1-9]) \| (.+?) \|", re.M)


def norm(s: str) -> str:
    s = re.sub(r"[*`]", "", s)
    return re.sub(r"\s+", " ", s).strip().rstrip(".")


def check(draft_text: str, spec_text: str, spec_bytes: bytes, spec_path=None,
          cmap=None, cmap_draft=None, cmap_spec=None):
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
    # L08 v4 — strike three's rebuild (GPT56-V104 F2, CODEX-V104 F3; the coordinator:
    # CONTROLS BEFORE CODE — four seeded controls were run against v3 and their colors
    # recorded before this body existed: rename BLIND, type-change BLIND, reorder caught,
    # collapsed-duplicate red-for-the-wrong-reason. The controls are the spec):
    #   identity = digest over the ORDERED canonical serialization of (field, constraint)
    #   pairs, computed at EVERY occurrence in both files; constraints come from the string
    #   registry (single-sourced live; injectable for controls).
    #   L09: an unregistered field in any tuple — the rename fingerprint.
    #   L08: within one loose group (same sorted field-name set, same constraints), ordered
    #   forms differ — a reorder or a drifted occurrence, across or within files.
    #   Distinct schemas sharing a field-name set but differing in constraints are DISTINCT
    #   and unflagged — the v3 collapse is gone.
    import hashlib as _hl
    import re as _re
    import unicodedata as _ud
    _normsig = lambda x: x.replace("signature-enveloped", "signature")
    if cmap is None:
        cmap = {}
        try:
            reg = (spec_path.parent / "ref" / "STRING_FIELD_REGISTRY.md").read_text()
            for m in _re.finditer(r"^\| `([a-z0-9_.-]+)` \| ([a-zA-Z-]+) \|", reg, _re.M):
                cmap[m.group(1).split(".")[-1]] = m.group(2)
        except Exception:
            pass
    def occs(s, mp):
        found = []
        # 3+ char fields: `(i, j)` is matrix notation, not a schema (live-run catch)
        for m in _re.finditer(r"`\(([a-z_]{3,}(?:,\s+[a-z_][a-z_ ]{2,})+)\)`", s):
            fields = [_ud.normalize("NFC", f.strip()) for f in _normsig(m.group(1)).split(",")]
            pairs = [(f, mp.get(f, mp.get(f.replace(" ", "_"), "UNREGISTERED"))) for f in fields]
            strict = _hl.sha256(("\n".join(f"{a}|{b}" for a, b in pairs)).encode()).hexdigest()
            loose = tuple(sorted(a for a, b in pairs))
            found.append((fields, pairs, strict, loose, m.group(1)))
        return found
    NOT_SCHEMAS = {("brickid", "objid")}   # data-column join keys quoted in prose, not
    # record schemas; listed rather than heuristically sized (live-run catch)
    all_occ = [o for o in occs(draft_text, cmap_draft or cmap)
               + occs(spec_text, cmap_spec or cmap)
               if tuple(o[0]) not in NOT_SCHEMAS]
    groups = {}
    for fields, pairs, strict, loose, raw in all_occ:
        unreg = [a for a, b in pairs if b == "UNREGISTERED"]
        if unreg and cmap:
            out.append(("L09", ERRORS["L09"] + f" — {unreg} in `({raw})`"))
        groups.setdefault(loose, set()).add(strict)
    for loose, stricts in groups.items():
        if len(stricts) > 1:
            # one field-NAME set, divergent (order|constraint) forms: a reorder, a type change,
            # or two schemas colliding on a name set — the last is the stated residual (no live
            # pair collides today; if one appears, this flag forces an explicit rename, which
            # is the hygiene the register wants anyway) and the round adjudicates.
            out.append(("L08", ERRORS["L08"] + f" — field set {list(loose)}"))
    return out


def self_test():
    spec = ("| G1 | no bytes move without a committed event | x |\n"
            "| G2 | events tell the truth | x |\n"
            "`(kind, chain_head)`\n")
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
        ("SEEDED reorder (one schema, two orders)",
         good + "`(chain_head, kind)`\n", {"L08"}),
        ("SEEDED rename (unregistered field)",
         good.replace("**G2 — events tell the truth**\n", "")
         + "**G2 — events tell the truth**\n`(kind, chain_hed)`\n", {"L09"}),
    ]
    fails = []
    for name, draft, want in cases:
        got = {c for c, _ in check(draft, spec, spec_b,
                                   cmap={'kind': 'x', 'chain_head': 'x'})}
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
    problems = check(draft.read_text(), spec.read_text(), spec.read_bytes(),
                     spec_path=spec)
    for c, msg in problems:
        print(f"  [{c}] {msg}")
    print(f"  lifecycle derivation: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
