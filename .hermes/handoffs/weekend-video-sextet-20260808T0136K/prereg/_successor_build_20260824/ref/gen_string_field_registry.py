#!/usr/bin/env python3
"""STRING-FIELD REGISTRY — enumerated from the schema blocks, because the universal sentence died.

V72 asserted: every string field in every non-chi artifact is closed-vocab or bounded - "no third
kind". The corpus already contained counterexamples (CODEX-V72 F2: slot-receipt schemas constrain
names, not value domains; GPT56-V72 F3: explanation_ref itself was unbounded). A universal sentence
written in one sitting is the anywhere/never defect; the fix is the VOID-registry fix - ENUMERATE.

This generator extracts every field token from the draft's declared schema blocks, so it cannot
silently omit a field the way a keyword filter omitted Row F. Classification is human and lives in
CONSTRAINTS below; a field the extractor finds with no row is FORBIDDEN-BY-DEFAULT and this exits
nonzero, which blocks the battery rather than shipping an omission. (And the first version of
this extractor proved the point against itself: its token pattern [a-z_]+ silently dropped every
field containing a digit - all seven sha256 fields - which is Row F's keyword omission, committed
by the tool built to prevent it. The stale-row report is what caught it.)
"""
import re
import sys
from pathlib import Path

B = Path(__file__).resolve().parent.parent
DRAFTS = sorted(B.glob("PREREG_SUCCESSOR_DRAFT_V*.md"),
                key=lambda p: int(re.search(r"_V(\d+)_", p.name).group(1)))
DRAFT = DRAFTS[-1]

# (field, constraint, declared-where, note). Constraints: closed-vocab | bounded-encoding | digest-ref
CONSTRAINTS = {
    # BS-3g slot receipt (§11)
    "mask_sha256": ("digest-ref", "§11 BS-3g", "must equal BS-2f's pinned mask_digest"),
    "calibration_sha256": ("digest-ref", "§11 BS-3g", ""),
    "perturbation_manifest_sha256": ("digest-ref", "§11 BS-3g", ""),
    "kernel_sha256": ("digest-ref", "§11 BS-3g", ""),
    "estimator_sha256": ("digest-ref", "§11 BS-3g", ""),
    "verifier_sha256": ("digest-ref", "§11 BS-3g", ""),
    "counterfactual_path_sha256": ("digest-ref", "§11 BS-3g", "plus in-process v9 assert"),
    "mapping_id": ("closed-vocab", "§11 BS-3g", "sole member MAPPING-NOT-PREREGISTERED until ruled"),
    "gamma_hat": ("bounded-encoding", "§11 BS-3g", "finite IEEE-754 double, decimal"),
    "sigma_gamma": ("bounded-encoding", "§11 BS-3g", "finite IEEE-754 double, decimal"),
    "gamma_bound": ("bounded-encoding", "§11 BS-3g", "recomputed |gamma_hat|+k*sigma, never accepted"),
    "invariance_outcome": ("closed-vocab", "§11 BS-3g", "HELD | FAILED"),
    "n_perturbations": ("bounded-encoding", "§11 BS-3g", "decimal int [1,10^6]"),
    "n_draws": ("bounded-encoding", "§11 BS-3g", "decimal int [1,10^6]; frozen value UNSET"),
    "draw_generator_id": ("closed-vocab", "§11 BS-3g", "set currently EMPTY - blocker"),
    "draw_master_seed": ("bounded-encoding", "§11 BS-3g", "decimal int [0,2^64-1]; frozen UNSET"),
    "draw_verdict_digest": ("digest-ref", "§11 BS-3g", "row-major serialization stated"),
    "baseline_verdict": ("closed-vocab", "§11 BS-3g", "HELD | FAILED | PER-DRAW; informational"),
    "delta_gamma_max": ("bounded-encoding", "§11 BS-3g", "finite positive double = frozen class-P"),
    # access-log event (§6.1 (ii))
    "timestamp": ("bounded-encoding", "§6.1 event schema", ""),
    "actor": ("closed-vocab", "§6.1 event schema", "row identifiers"),
    "table row": ("closed-vocab", "§6.1 event schema", ""),
    "operation": ("closed-vocab", "§6.1 event schema", "BS-2k closed operation set"),
    "object identity": ("bounded-encoding", "§6.1 event schema", "brickid/objid keys"),
    "success/refusal": ("closed-vocab", "§6.1 event schema", ""),
    "refusal reason": ("closed-vocab", "§6.1 event schema", "the eleven codes"),
    "running chain digest": ("digest-ref", "§6.1 event schema", ""),
    # enumeration entry (§6.1)
    "chain_position": ("bounded-encoding", "§6.1 entry", "index into the chain"),
    "event_digest": ("digest-ref", "§6.1 entry", ""),
    "class_key": ("closed-vocab", "§6.1 entry", "(row, operation), both closed"),
    "disposition": ("closed-vocab", "§6.1 entry", "NAMED-AS-DEFECT | EXPLAINED"),
    "rederivation_digest": ("digest-ref", "§6.1 entry", "revision must contain the class_key"),
    "explanation_ref": ("digest-ref", "§6.1 entry", "sha256 of the canonical explanation body"),
    # explanation artifact (§6.1)
    "cause": ("closed-vocab", "§6.1 explanation", "five-member set"),
    # acceptance-evidence projection (§6.1 (v))
    "parent_attempt_present": ("closed-vocab", "§6.1 projection", "predicate bit"),
    "byte_integrity_pass": ("closed-vocab", "§6.1 projection", "predicate bit"),
    "canonical_shape_pass": ("closed-vocab", "§6.1 projection", "predicate bit"),
}

def extract(text):
    fields = set()
    m = re.search(r"exactly these \w+ fields[^:]*:\*\*\n(.+?)\.\n  \*\*", text, re.S)
    if m:
        fields |= set(re.findall(r"`([a-z0-9_]+)`", m.group(1)))
    m = re.search(r"access log under its BS-2k event schema \(([^)]+)\)", text)
    if m:
        fields |= {f.strip() for f in re.sub(r"—.*", "", m.group(1)).split(",")}
    m = re.search(r"ENUMERATION ENTRY\*\* is an authenticated record with exactly these fields: (.+?)· the enumerator", text, re.S)
    if m:
        fields |= set(re.findall(r"`([a-z0-9_]+)`", m.group(0)))
    if re.search(r"`cause` token from the declared set", text):
        fields.add("cause")
    fields |= set(re.findall(r"`(parent_attempt_present|byte_integrity_pass|canonical_shape_pass)`", text))
    return {f for f in fields if f and not f.isdigit()}

def main():
    text = DRAFT.read_text()
    found = extract(text)
    rows, missing = [], []
    for f in sorted(found):
        if f in CONSTRAINTS:
            c, w, note = CONSTRAINTS[f]
            rows.append(f"| `{f}` | {c} | {w} | {note} |")
        else:
            missing.append(f)
            rows.append(f"| `{f}` | **FORBIDDEN-BY-DEFAULT — no registry row** | ? | classify or remove |")
    stale = sorted(set(CONSTRAINTS) - found)
    out = ["# STRING-FIELD REGISTRY — every string-bearing field in every non-χ artifact\n",
           f"**Generated from `{DRAFT.name}`'s schema blocks by `ref/gen_string_field_registry.py`; "
           "the extraction is mechanical so the enumeration cannot silently omit a declared field, "
           "and the CLASSIFICATION is human, exactly as the raise-site ledger splits the same "
           "labour.** A field with no row is **forbidden by default** and the generator exits "
           "nonzero. Constraints: `closed-vocab` (a declared member set) · `bounded-encoding` "
           "(digest/decimal-in-range) · `digest-ref` (sha256 of a canonical body).\n",
           "**The honest limit:** bounded numerics still carry bits; the registry bounds capacity "
           "and cannot zero it. What it removes is free prose.\n",
           "| field | constraint | declared | note |", "|---|---|---|---|"] + rows
    if stale:
        out.append(f"\n**Classified but not found in the draft (stale rows, check the extractor):** "
                   f"{', '.join(f'`{s}`' for s in stale)}")
    (B / "ref/STRING_FIELD_REGISTRY.md").write_text("\n".join(out) + "\n")
    print(f"fields found {len(found)}  classified {len(found)-len(missing)}  "
          f"FORBIDDEN-BY-DEFAULT {len(missing)}  stale {len(stale)}")
    if missing:
        print("UNCLASSIFIED:", missing)
    return 1 if missing else 0

if __name__ == "__main__":
    sys.exit(main())
