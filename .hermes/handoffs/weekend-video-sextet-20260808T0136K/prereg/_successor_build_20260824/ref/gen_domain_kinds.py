#!/usr/bin/env python3
"""DOMAIN KINDS — the NMPR1 tag set as generator output, never a hand count.

Blanc's order after V101 (GPT56-V101 F2, CODEX-V101 F3): every hand-written exhaustive claim in
this corpus has failed; the kind set is therefore EMITTED — declared kinds crosschecked against
the corpus's own digest-preimage mentions, strangers fatal both ways, count as output, --check
as the diff control. Frozen v9's envelope preimages are excluded BY NAME with the reason.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent

DECLARED = {
    # kind -> the record-definition probe phrase that must exist in the corpus; the pair IS the
    # declaration, so a kind with no living definition site is DECLARED-ONLY and fatal, and a
    # definition site whose kind is missing here surfaces as a stranger when tagged bodies land.
    "entry": "ENUMERATION ENTRY",
    "explanation": "explanation body",
    "passrec": "GATE PASS RECORD",
    "termrec": "terminated-verdict record",
    "haltrec": "EXHAUSTION HALT RECEIPT",
    "bindmap-entry": "CONTINUATION MAP ENTRY",
    "lockcp": "lock checkpoint",
    "sealed-entry-set": "sealed_entry_set_digest",
    "sealed-bindmap": "sealed_bindmap_digest",
    "opening-auth": "opening authorization",
    "lock-body": "canonical lock digest",
    "freeze-body": "freeze-signature body",
    "wire-frame": "framed unit",
    "verdict-record": "verdict record",
    "terminal-review": "TERMINAL-REVIEW BODY",
}
FROZEN_EXCLUDED = [
    ("ref/successor_ref_v9.py:219-224", "receipt envelope body/envelope digests - frozen; "
     "kind-separated by the envelope's own slot/schema fields"),
    ("ref/successor_ref_v9.py access-log running digest", "the chain digest itself - frozen "
     "discipline predating the tag rule; separated by position, not kind"),
]

def main():
    argv = [a for a in sys.argv[1:] if a != "--check"]
    if len(argv) != 1:
        print("usage: gen_domain_kinds.py DRAFT.md [--check]")
        return 2
    texts = [Path(argv[0]).read_text(), (BASE / "LIFECYCLE_GUARANTEE_SPEC.md").read_text(),
             (HERE / "gen_string_field_registry.py").read_text()]
    corpus = "\n".join(texts)
    literal = set(re.findall(r"NMPR1:([a-z][a-z-]+)", corpus)) - {"kind"}  # template excluded
    declared = set(DECLARED)
    strangers = sorted(literal - declared)
    unmentioned = sorted(k for k, probe in DECLARED.items() if probe not in corpus)
    out = ["# DOMAIN KINDS — generated, count is OUTPUT\n",
           f"**{len(declared)} kinds at this revision** (a number this file emits and no prose "
           "may restate):\n"]
    out += [f"- `{k}`" for k in sorted(declared)]
    out.append("\n**Frozen exclusions, by name (GPT56-V101 F2):**")
    out += [f"- {site} — {why}" for site, why in FROZEN_EXCLUDED]
    if strangers:
        out.append(f"\n**STRANGERS (mentioned, undeclared): {strangers} — FATAL**")
    if unmentioned:
        out.append(f"\n**DECLARED-ONLY (no corpus mention): {unmentioned} — FATAL**")
    content = "\n".join(out) + "\n"
    target = HERE / "DOMAIN_KINDS.md"
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text() == content and not strangers and not unmentioned
        print("domain kinds --check:", "byte-equal, no strangers" if ok else "DRIFTED or strangers")
        return 0 if ok else 1
    target.write_text(content)
    print(f"domain kinds: {len(declared)} declared, {len(strangers)} stranger(s), "
          f"{len(unmentioned)} unmentioned")
    return 1 if (strangers or unmentioned) else 0

if __name__ == "__main__":
    sys.exit(main())
