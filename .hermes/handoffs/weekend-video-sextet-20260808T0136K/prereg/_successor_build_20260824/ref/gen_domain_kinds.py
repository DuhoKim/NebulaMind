#!/usr/bin/env python3
"""DOMAIN KINDS — kinds bound to REAL preimage sites, under the lane's standing rule.

STANDING RULE (the coordinator, after V102's hollow-generator finding — CODEX-V102 F5,
GPT56-V102 F5: the first version passed 15 kinds off probe phrases and enumerated nothing):
no generator's output is citable until it passes a SEEDED POSITIVE CONTROL and a DELETION
PROBE. Both live in --self-test here and run in the battery.

What this enumerates: every digest-ref field row of ref/STRING_FIELD_REGISTRY.md is a
digest-preimage SITE. Each site must be covered exactly one way:
  TAGGED   — its preimage is a canonical body with an NMPR1 kind (the PREIMAGE_OF map)
  FROZEN   — a frozen-v9 discipline that cannot take a tag, excluded BY NAME with a reason
  RAW      — a digest over raw file/artifact bytes, not a canonical body: no tag applies,
             separation comes from usage context, and the row SAYS so
An unmapped site is FATAL. Kinds must also keep a live definition site (probe phrase), and
declared-only or stranger kinds are fatal — the two-way check the first version had, kept.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent

DECLARED = {
    "entry": "ENUMERATION ENTRY", "explanation": "explanation body",
    "passrec": "GATE PASS RECORD", "termrec": "terminated-verdict record",
    "haltrec": "EXHAUSTION HALT RECEIPT", "bindmap-entry": "CONTINUATION MAP ENTRY",
    "lockcp": "lock checkpoint", "sealed-entry-set": "sealed_entry_set_digest",
    "sealed-bindmap": "sealed_bindmap_digest", "opening-auth": "opening authorization",
    "lock-body": "canonical lock digest", "freeze-body": "freeze-signature body",
    "wire-frame": "framed unit", "verdict-record": "verdict record",
    "terminal-review": "TERMINAL-REVIEW BODY", "drain-start": "DRAIN-START record",
    "terminal-checkpoint": "TERMINAL CHECKPOINT",
}
# field-name regex -> coverage. Order matters; first match wins.
PREIMAGE_OF = [
    (r"^entry\.event_digest$", ("FROZEN", "chain running digest at a position")),
    (r"^(bindmap|termrec|haltrec|passrec)\.(decision_event_digest|chain_head_digest)$",
     ("FROZEN", "chain running digest values")),
    (r"^passrec\.(head_digest)$", ("FROZEN", "chain running digest at the head")),
    (r"^passrec\.predecessor_record_digest$", ("TAGGED", "passrec")),
    (r"^passrec\.verifier_digest$", ("RAW", "verifier file bytes")),
    (r"^(drainst|termcp)\.receipt_digest$", ("TAGGED", "termrec")),
    (r"^termcp\.chain_head_digest$", ("FROZEN", "chain running digest")),
    (r"^(termrec|haltrec)\.freeze_signature_digest$", ("TAGGED", "freeze-body")),
    (r"^(termrec|haltrec)\.first_opening_digest$", ("FROZEN",
     "the opening record digest - clock-family, chain-side")),
    (r"^lockcp\.chain_head_digest$", ("FROZEN", "chain running digest")),
    (r"^lockcp\.sealed_entry_set_digest$", ("TAGGED", "sealed-entry-set")),
    (r"^lockcp\.sealed_bindmap_digest$", ("TAGGED", "sealed-bindmap")),
    (r"^openauth\.bsl_digest$", ("TAGGED", "lock-body")),
    (r"^lockbody\..*digest.*$", ("MIXED", "clause 3(b) constituent digests - slot receipts "
     "(RAW envelope discipline, frozen v9) and checkpoint (TAGGED lockcp)")),
    (r"^lockbody\.freeze_signature$", ("TAGGED", "freeze-body")),
    (r".*_sha256$", ("RAW", "raw file/artifact bytes - code pins, weights, fixtures")),
    (r".*mask_digest$", ("RAW", "the sealed mask artifact bytes (frozen envelope discipline)")),
    (r".*(payload|anchor|config|manifest|perm_payload)_digest$", ("RAW", "artifact bytes")),
    (r"^event\.running_chain_digest$|^arrival\.running_chain_digest$",
     ("FROZEN", "the chain digest itself")),
    (r"^nonslot\..*$", ("RAW", "non-slot artifact bytes or pending schemas, per their rows")),
    (r"^canonical\..*$", ("RAW", "canonical artifact bytes per their rows")),
    (r"^dlm_entry\.digest$|^roots_entry\.digest$", ("RAW", "loaded-object file bytes")),
    (r"^bs7p_env\.(dependency_roots|dynamic_load_manifest)$",
     ("RAW", "manifest document bytes (roots/DLM files)")),
    (r"^envelope\.environment$", ("FROZEN", "environment record under the frozen v9 envelope")),
    (r"^freezebody\.code_digest$", ("RAW", "pinned code bytes")),
    (r"^lockbody\..*$", ("MIXED", "clause 3(b) constituents - slot receipts and artifacts "
     "under the frozen envelope discipline (RAW/FROZEN per constituent); the checkpoint "
     "constituent is TAGGED lockcp; signer identity is roster data, not a preimage")),
    (r"^openauth\.(ceremony_id|signer_identity)$", ("RAW",
     "opaque one-use identifier / roster-bound identity - identifiers, not canonical-body "
     "preimages")),
    (r"^param\.lease_id_digest$", ("RAW", "lease identifier bytes")),
    (r"^draw_verdict_digest$", ("RAW", "the row-major verdict-matrix serialization - its own "
     "stated section-11 rule, single-use, pre-tag, no cross-kind partner")),
    (r"^event_digest$", ("FROZEN", "chain running digest (entry join field)")),
    (r"^explanation_ref$", ("TAGGED", "explanation")),
    (r"^rederivation_digest$", ("RAW", "vocabulary revision text bytes")),
    (r".*_digest$", (None, None)),   # any other *_digest falls through -> UNMAPPED, fatal
]

def enumerate_sites(registry_text):
    sites = []
    for m in re.finditer(r"^\| `([a-z0-9_.-]+)` \| digest-ref \|", registry_text, re.M):
        sites.append(m.group(1))
    return sites

def cover(site):
    for pat, val in PREIMAGE_OF:
        if re.match(pat, site):
            return val
    return (None, None)

def run(registry_text, corpus):
    sites = enumerate_sites(registry_text)
    rows, unmapped = [], []
    for s in sites:
        cat, detail = cover(s)
        if cat is None:
            unmapped.append(s)
        else:
            rows.append((s, cat, detail))
    declared = set(DECLARED)
    literal = set(re.findall(r"NMPR1:([a-z][a-z-]+)", corpus)) - {"kind"}
    strangers = sorted(literal - declared)
    unment = sorted(k for k, probe in DECLARED.items() if probe not in corpus)
    tagged_kinds = {d for _, c, d in rows if c == "TAGGED"}
    orphan_kinds = sorted(k for k in tagged_kinds if k not in declared)
    return sites, rows, unmapped, strangers, unment, orphan_kinds

def self_test():
    fails = []
    # SEEDED POSITIVE: a planted unknown digest-ref site MUST surface as unmapped
    seeded = "| `wombat.mystery_digest` | digest-ref | x | y |\n"
    _, _, unmapped, *_ = run(seeded, "")
    if unmapped != ["wombat.mystery_digest"]:
        fails.append(f"seeded site not caught: {unmapped}")
    # DELETION PROBE: dropping a mapping entry must turn a real site unmapped
    global PREIMAGE_OF
    keep = PREIMAGE_OF
    PREIMAGE_OF = [p for p in PREIMAGE_OF if "sealed_entry_set" not in p[0]]
    try:
        _, _, unmapped2, *_ = run("| `lockcp.sealed_entry_set_digest` | digest-ref | x | y |\n", "")
    finally:
        PREIMAGE_OF = keep
    if "lockcp.sealed_entry_set_digest" not in unmapped2:
        fails.append("deletion probe: removed mapping stayed green")
    # a mapped site must NOT surface
    _, rows3, unmapped3, *_ = run("| `passrec.predecessor_record_digest` | digest-ref | x |\n", "")
    if unmapped3 or not rows3:
        fails.append(f"mapped site misfired: {unmapped3} {rows3}")
    for f in fails:
        print(f"  FAIL {f}")
    print(f"  self-test: 3 controls, {len(fails)} failure(s)")
    return 1 if fails else 0

def main():
    if "--self-test" in sys.argv:
        return self_test()
    argv = [a for a in sys.argv[1:] if a != "--check"]
    if len(argv) != 1:
        print("usage: gen_domain_kinds.py DRAFT.md [--check|--self-test]")
        return 2
    registry_text = (HERE / "STRING_FIELD_REGISTRY.md").read_text()
    corpus = "\n".join([Path(argv[0]).read_text(),
                        (BASE / "LIFECYCLE_GUARANTEE_SPEC.md").read_text(),
                        (HERE / "gen_string_field_registry.py").read_text()])
    sites, rows, unmapped, strangers, unment, orphans = run(registry_text, corpus)
    out = ["# DOMAIN KINDS — kinds bound to enumerated preimage sites\n",
           f"**{len(DECLARED)} kinds; {len(sites)} digest-preimage sites enumerated from the "
           "registry's digest-ref rows; every site covered TAGGED/FROZEN/RAW or the build "
           "fails.** Controls: seeded positive + deletion probe in --self-test (the standing "
           "rule after V102's hollow first version).\n",
           "## Kinds"]
    out += [f"- `{k}`" for k in sorted(DECLARED)]
    out.append("\n## Sites")
    out += [f"- `{s}` — {c}: {d}" for s, c, d in rows]
    for name, bad in (("UNMAPPED SITES", unmapped), ("STRANGER KINDS", strangers),
                      ("DECLARED-ONLY KINDS", unment), ("ORPHAN TAGGED KINDS", orphans)):
        if bad:
            out.append(f"\n**{name}: {bad} — FATAL**")
    content = "\n".join(out) + "\n"
    target = HERE / "DOMAIN_KINDS.md"
    fatal = bool(unmapped or strangers or unment or orphans)
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text() == content and not fatal
        print("domain kinds --check:", "byte-equal, all sites covered" if ok else "DRIFT or FATAL")
        return 0 if ok else 1
    target.write_text(content)
    print(f"domain kinds: {len(DECLARED)} kinds, {len(sites)} sites, "
          f"{len(unmapped)} unmapped, {len(strangers)} strangers, {len(unment)} declared-only")
    return 1 if fatal else 0

if __name__ == "__main__":
    sys.exit(main())
