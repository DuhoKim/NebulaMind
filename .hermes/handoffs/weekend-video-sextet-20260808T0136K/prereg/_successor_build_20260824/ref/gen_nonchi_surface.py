#!/usr/bin/env python3
"""gen_nonchi_surface - the exhaustive non-chi surface as a GENERATED registry.

GPT56-V111 F2 was the FOURTH instance of the same integration lag: a new record kind
built into the machinery while absent from the draft's exhaustive non-chi schema list,
making it chi-bearing by the list's own default rule. The coordinator's directive
(2026-08-30): stop maintaining the exhaustive lists by hand - generate them from a
record-kind registry and fail the battery on any kind not integrated.

Three checks, all deletion-probed:
  1. CLOSURE - every schema-set prefix in gen_string_field_registry that carries a
     `.kind` field must have a SURFACE row here. A future record kind entering the
     string-field registry (which L09 forces) without a SURFACE row is refused, so a
     new kind cannot exist unintegrated.
  2. ADMISSION - every SURFACE row's admission probe must occur in its declared home
     (draft or spec). A kind whose schema exists in the registry but is admitted
     nowhere is the exact V111 defect.
  3. FIELD ECHO (restate=True rows only) - every bare field name of the row's schema
     set must appear within the admission paragraph, so an admitted-by-name schema
     whose exact tuple drifted from the registry (GPT56-V111 F3's five-field export)
     goes red. Quote-bound rows (the T-tuples, single-surface rule GPT56-V105 F3)
     set restate=False.
"""
import re, sys, hashlib, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _load_registry_module():
    spec = importlib.util.spec_from_file_location(
        "gen_string_field_registry", HERE / "gen_string_field_registry.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

# kind-prefix -> (schema set name, home: DRAFT|SPEC|BOTH, admission probe, restate)
SURFACE = [
    ("arrival",  "ARRIVAL*", "DRAFT",
     "(ii-b) **the ARRIVAL event under its own authenticated closed schema", False),
    ("ckclock",  "CKCLOCK",  "DRAFT",
     "(ii-c) **the CHECKPOINT CLOCK RECORD under its closed schema", True),
    ("succexp",  "SUCCEXP",  "DRAFT",
     "AND the SUCCESSOR EXPORT `(kind, sealed_enumeration_digest, "
     "continuation_segment_digest, terminal_head, freeze_signature_digest, "
     "flagged_keys)`", True),
    ("haltrec",  "HALTREC",  "DRAFT",
     "the EXHAUSTION HALT RECEIPT `(kind, chain_head, freeze_signature_digest, "
     "first_opening_digest)`", True),
    ("termrec",  "TERMREC",  "DRAFT",
     "the UNNAMEABLE-CLASS terminated-verdict record `(kind, class_key, gate, "
     "chain_head, freeze_signature_digest, first_opening_digest)`", True),
    ("passrec",  "PASSREC",  "DRAFT",
     "(ii-e) **the GATE PASS RECORD `(gate,", True),
    ("drainst",  "DRAINST",  "DRAFT",
     "(ii-f) **the DRAIN-START record, the TERMINAL CHECKPOINT and the RECEIPT-NOTE", False),
    ("termcp",   "TERMCP",   "DRAFT",
     "(ii-f) **the DRAIN-START record, the TERMINAL CHECKPOINT and the RECEIPT-NOTE", False),
    ("rnote",    "RNOTE",    "DRAFT",
     "(ii-f) **the DRAIN-START record, the TERMINAL CHECKPOINT and the RECEIPT-NOTE", False),
    ("bindmap",  "BINDMAP",  "DRAFT",
     "**(iv-c) the binding→key map", True),
    ("dlm_entry",   "ENTRIES", "DRAFT", "(iv-b) the enumeration entries", False),
    ("roots_entry", "ENTRIES", "DRAFT", "(iv-b) the enumeration entries", False),
    # V112: the four kinds GPT56-V111 F2 found unadmitted, plus attempt-close
    ("vread",    "VERIF", "DRAFT",
     "(ii-g) **the VERIFICATION-READ record `(kind, request_key, touch_position, "
     "boot_epoch, monotonic_reading)`", True),
    ("vbound",   "VERIF", "DRAFT",
     "the VERIFICATION-BOUNDARY record `(kind, gate, boot_epoch, monotonic_reading)`",
     True),
    ("attstart", "VERIF", "DRAFT",
     "the ATTEMPT-START record `(kind, member_position, boot_epoch, "
     "monotonic_reading)`", True),
    ("attclose", "VERIF", "DRAFT",
     "the ATTEMPT-CLOSE record `(kind, member_position, close_class, boot_epoch, "
     "monotonic_reading)`", True),
    ("vclose",   "VERIF", "DRAFT",
     "the VERIFICATION-CLOSE record `(kind, gate, boundary_position, close_class, "
     "boot_epoch, monotonic_reading)`", True),
    ("roster",   "ROSTER", "DRAFT",
     "the REVIEWER ROSTER — closed schema `(kind, roster_entries)`", True),
    ("revrec",   "REVREC", "DRAFT",
     "the SIGNED REVIEW RECORD `(kind, reviewer_identity, review_timestamp, "
     "review_disposition, evidence_ref, reviewed_chain_position, "
     "reviewed_event_digest, reviewed_class_key, first_opening_digest)`", True),
    # post-run surface: the ceremony body is admitted at the spec's trust paragraph
    ("revbody",  "REVBODY", "SPEC", "CANONICAL TERMINAL-REVIEW BODY", True),
]
_ROWMAP = {p: (s, h, pr, rs) for p, s, h, pr, rs in SURFACE}

def _fields_by_prefix(mod):
    out = {}
    for name in dir(mod):
        if not re.fullmatch(r"[A-Z][A-Z0-9_]*", name):
            continue
        val = getattr(mod, name)
        if isinstance(val, (set, frozenset)):
            for f in val:
                if isinstance(f, str) and "." in f:
                    out.setdefault(f.split(".")[0], set()).add(f.split(".", 1)[1])
    return out

def check(draft_text, spec_text):
    problems = []
    mod = _load_registry_module()
    by_prefix = _fields_by_prefix(mod)
    # 1. CLOSURE
    for prefix, fields in sorted(by_prefix.items()):
        if "kind" in fields and prefix not in _ROWMAP:
            problems.append(
                f"CLOSURE: registry prefix '{prefix}' carries a .kind field but has no "
                f"SURFACE row - a record kind exists unintegrated (the V111-F2 class)")
    for prefix in _ROWMAP:
        if prefix not in by_prefix:
            problems.append(
                f"CLOSURE: SURFACE row '{prefix}' has no schema set in the string-field "
                f"registry - a surface row admitting nothing")
    # 2 + 3. ADMISSION and FIELD ECHO
    for prefix, (setname, home, probe, restate) in _ROWMAP.items():
        text = draft_text if home == "DRAFT" else spec_text if home == "SPEC" \
            else draft_text + spec_text
        n = text.count(probe)
        if n == 0:
            problems.append(
                f"ADMISSION: kind '{prefix}' ({setname}) has no admission - probe "
                f"{probe[:60]!r} absent from the {home} (GPT56-V111 F2)")
            continue
        # NEGATION TRIPWIRE (GPT56-V112 F4: 'HISTORICAL ONLY' appended after a live probe
        # passed) - a finite named-shape list, NOT a semantic guarantee; rewording is the
        # round's to catch, and this comment says so (the vocab checker's precedent).
        tail = text[text.index(probe):text.index(probe) + len(probe) + 400]
        for neg in ("no longer admits", "HISTORICAL ONLY", "schema retired",
                    "does not admit", "admission withdrawn"):
            if neg in tail:
                problems.append(
                    f"ADMISSION-NEGATED: kind '{prefix}' probe is followed by "
                    f"{neg!r} - a live probe under a dead admission (GPT56-V112 F4)")
        if restate and prefix in by_prefix:
            i = text.index(probe)
            para = text[i:i + 3000]
            for f in sorted(by_prefix[prefix]):
                # the registry's own norm map treats space and underscore as one
                # (the (iv-c) tuple writes 'decision chain_position'); mirror it
                forms = {f, f.replace("_", " "), f.replace("_", " ", 1)}
                if not any(re.search(r"\b" + re.escape(v) + r"\b", para)
                           for v in forms):
                    problems.append(
                        f"FIELD-ECHO: kind '{prefix}' admission at {probe[:40]!r} does "
                        f"not carry field '{f}' - the admitted tuple drifted from the "
                        f"registry schema (the V111-F3 class)")
    return problems

def emit(draft_path, spec_path):
    draft_text = Path(draft_path).read_text()
    spec_text = Path(spec_path).read_text()
    problems = check(draft_text, spec_text)
    mod = _load_registry_module()
    by_prefix = _fields_by_prefix(mod)
    lines = ["# NON-χ SURFACE REGISTRY — generated by ref/gen_nonchi_surface.py",
             f"# source draft: {Path(draft_path).name}",
             "# One row per record kind. CLOSURE: every .kind-bearing registry prefix",
             "# must appear here; ADMISSION: the probe must exist in its home;",
             "# FIELD ECHO (restate rows): admitted tuple carries every schema field.",
             "",
             "| kind prefix | schema set | fields | home | restate |",
             "|---|---|---|---|---|"]
    for prefix, setname, home, probe, restate in SURFACE:
        fl = " ".join(sorted(by_prefix.get(prefix, set())))
        lines.append(f"| {prefix} | {setname} | {fl} | {home} | "
                     f"{'yes' if restate else 'quote-bound/no'} |")
    lines.append("")
    lines.append(f"rows: {len(SURFACE)} · problems at generation: {len(problems)}")
    return "\n".join(lines) + "\n", problems

def selftest():
    """Seeded controls - each must FAIL on its seeded defect."""
    mod = _load_registry_module()
    by_prefix = _fields_by_prefix(mod)
    ok_draft = "".join(
        f"\n{pr} filler {' '.join(sorted(by_prefix.get(p, set())))}\n"
        for p, s, h, pr, rs in SURFACE if h == "DRAFT")
    ok_spec = "".join(
        f"\n{pr} filler {' '.join(sorted(by_prefix.get(p, set())))}\n"
        for p, s, h, pr, rs in SURFACE if h == "SPEC")
    fails = []
    # control 1: clean fixture is green
    if check(ok_draft, ok_spec):
        fails.append("clean fixture not green: " + str(check(ok_draft, ok_spec)[:2]))
    # control 2: deleted admission goes red
    broken = ok_draft.replace("(ii-g) **the VERIFICATION-READ record", "GONE", 1)
    if not any("ADMISSION: kind 'vread'" in p for p in check(broken, ok_spec)):
        fails.append("deleted vread admission not caught")
    # control 3: tuple drift goes red - full-tuple probes make drift an admission miss
    drifted = ok_draft.replace("flagged_keys)`", "flag_gone)`", 1)
    if not any("kind 'succexp'" in p for p in check(drifted, ok_spec)):
        fails.append("succexp tuple drift not caught")
    # control 5 (CODEX-V112 F3): vbound tuple drift - the V112 blind spot, now a probe miss
    vdrift = ok_draft.replace(
        "the VERIFICATION-BOUNDARY record `(kind, gate, boot_epoch, monotonic_reading)`",
        "the VERIFICATION-BOUNDARY record `(kind, timestamp)`", 1)
    if not any("kind 'vbound'" in p for p in check(vdrift, ok_spec)):
        fails.append("vbound tuple drift not caught")
    # control 6 (GPT56-V112 F4): a live probe under a negated admission goes red
    negd = ok_draft.replace(
        "the ATTEMPT-START record `(kind, member_position, boot_epoch, "
        "monotonic_reading)`",
        "the ATTEMPT-START record `(kind, member_position, boot_epoch, "
        "monotonic_reading)` HISTORICAL ONLY; this paragraph no longer admits these records",
        1)
    if not any("ADMISSION-NEGATED" in p for p in check(negd, ok_spec)):
        fails.append("negated admission not caught")
    # control 4: closure - an unregistered kind-bearing prefix goes red
    saved = _ROWMAP.pop("rnote")
    try:
        if not any("CLOSURE: registry prefix 'rnote'" in p for p in check(ok_draft, ok_spec)):
            fails.append("closure deletion not caught")
    finally:
        _ROWMAP["rnote"] = saved
    return fails

if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--selftest":
        f = selftest()
        for x in f:
            print("SELFTEST FAIL:", x)
        print(f"selftest: {6 - len(f)}/6 controls fired correctly")
        sys.exit(1 if f else 0)
    draft, spec = args[0], args[1]
    body, problems = emit(draft, spec)
    if "--check" in args:
        want = (HERE / "NONCHI_SURFACE.md").read_text()
        same = want == body
        print(f"--check: {'byte-equal' if same else 'STALE'}; problems: {len(problems)}")
        for p in problems:
            print("  ", p)
        sys.exit(0 if same and not problems else 1)
    (HERE / "NONCHI_SURFACE.md").write_text(body)
    print(f"NONCHI_SURFACE.md written; problems: {len(problems)}")
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)
