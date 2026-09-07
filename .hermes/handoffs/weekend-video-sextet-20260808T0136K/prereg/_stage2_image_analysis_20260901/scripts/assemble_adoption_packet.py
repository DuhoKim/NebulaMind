#!/usr/bin/env python3
"""Assemble the adoption packet Codex presents to Duho — DETERMINISTIC, no AI worker (Trio efficiency policy).
It reports what exists and what does not; it decides nothing, adopts nothing, and refuses to describe an
unreviewed or unfinished package as ready. Run from the lane root."""
import hashlib, json, os, sys, datetime
def sha(p):
    try: return hashlib.sha256(open(p,'rb').read()).hexdigest()
    except OSError: return None
CORE = [("candidate", "AGREEMENT_RUN_AMENDMENT_A1_20260907.md"),
        ("decision sheet", "AGREEMENT_RUN_DECISION_SHEET_FOR_DUHO_20260907.md"),
        ("implementation delta", "A1_IMPLEMENTATION_DELTA_20260907.md"),
        ("input manifest (CORE)", "_optionA_dev/agreement_run/INPUT_MANIFEST_A1_CORE.json"),
        ("runtime pins (CORE)", "_optionA_dev/agreement_run/RUNTIME_PINS_A1_CORE.json"),
        ("selection code", "_optionA_dev/agreement_run/select_sample.py"),
        ("run path", "_optionA_dev/agreement_run/run_path.py"),
        ("MEDIUM producer", "_optionA_dev/agreement_run/medium_perturbation.py"),
        ("eligible ids", "_optionA_dev/agreement_run/inputs/eligible_ids_20260907.txt"),
        ("failed-set ids", "_optionA_dev/agreement_run/inputs/failed_set_ids_20260907.txt")]
REVIEWS = [("review 1 (REFUSED)", "AGY_A1_REVIEW_20260907.md"),
           ("review 2 (changed bytes)", "AGY_A1_REVIEW2_20260907.md"),
           ("review 3 (final delta)", "AGY_A1_REVIEW3_20260907.md")]
def verdict(p):
    try:
        for line in open(p, encoding="utf-8"):
            if line.startswith("VERDICT"): return line.strip()
    except OSError: return None
    return None
out = ["# ADOPTION PACKET — assembled deterministically, " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M KST"),
       "Assembled by `scripts/assemble_adoption_packet.py`. It states what exists; it adopts nothing and asserts no review result it cannot read.", "", "## The bytes", "| item | path | sha256 |", "|---|---|---|"]
missing = []
for label, p in CORE:
    d = sha(p)
    if d is None: missing.append(p)
    out.append(f"| {label} | `{p}` | `{d or 'ABSENT'}` |")
out += ["", "## The independent review chain", "| pass | file | verdict |", "|---|---|---|"]
pending = []
for label, p in REVIEWS:
    v = verdict(p)
    if v is None: pending.append(p)
    out.append(f"| {label} | `{p}` | {v or '**not yet filed in the lane**'} |")
core_mf = "_optionA_dev/agreement_run/INPUT_MANIFEST_A1_CORE.json"
ready = None
try: ready = json.load(open(core_mf)).get("ready_for_input_freeze")
except Exception: pass
out += ["", "## Status, stated narrowly",
        f"- `ready_for_input_freeze` = **{ready}** — this means ONLY that the input-stage files are ready to freeze. It is not adoption, not permission to start a run, and not the existence of later-stage evidence.",
        "- Nothing is adopted. Duho has made no decision. No seed, round, anchor, selection, draw or holdout has occurred.",
        "- Approval medium: plain-language approval in Duho's dialogue with Codex, bound to the exact presented version (his recorded decision, `CODEX_DUHO_CONVERSATION_APPROVAL_RECORD_20260906.md`). He recites no digest."]
blockers = []
if missing: blockers.append(f"{len(missing)} packet file(s) absent: {', '.join(missing)}")
if pending: blockers.append(f"{len(pending)} review report(s) not yet filed in the lane: {', '.join(pending)}")
if ready is not True: blockers.append("input readiness is not TRUE")
out += ["", "## Is this presentable to Duho?"]
out += ["**NO — " + "; ".join(blockers) + ".**"] if blockers else ["**The packet is assembled and complete as listed.** Presentation remains Codex's step; assembly is not adoption."]
print("\n".join(out))
sys.exit(2 if blockers else 0)
