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
REVIEWS = [("review 9 (A1 bytes)", "AGY_A1_REVIEW9_20260907.md"), ("review 8 (decision sheet)", "AGY_A1_REVIEW8_20260907.md"), ("review 7", "AGY_A1_REVIEW7_20260907.md"),("review 6 (final)", "AGY_A1_REVIEW6_20260907.md"), ("review 5", "AGY_A1_REVIEW5_20260907.md"), ("review 4 (repair)", "AGY_A1_REVIEW4_20260907.md"),("review 1 (REFUSED)", "AGY_A1_REVIEW_20260907.md"),
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
# --- THE CHECK THIS ASSEMBLER WAS MISSING (found 2026-09-07 17:50 by the owner):
# it verified that review files EXIST, never that the latest verdict is POSITIVE or that the reviewed
# bytes are the CURRENT bytes. It called a package presentable whose last A1 review said NOT-SOUND
# against a digest two revisions old. Same defect class as every other one this lane found today:
# a check over a list that never asks whether the list covers what it claims to cover.
def access_sha(p):
    try:
        import re as _re
        m = _re.search(r"ACCESS_SHA=([0-9a-f]{64})", open(p, encoding="utf-8").read())
        return m.group(1) if m else None
    except OSError: return None
# EXACT TOKEN MATCH, never substring: "FINAL-NOT-SOUND" must never satisfy a rule written for "FINAL-SOUND".
# (The first version of this list also simply omitted FINAL-SOUND, so a positive review read as unreviewed.)
POSITIVE = {"REVIEWABLE-AND-SOUND", "DELTA-SOUND", "REPAIR-SOUND", "FINAL-SOUND", "SHEET-SOUND", "CANDIDATE-SOUND"}
def verdict_token(v):
    return (v or "").split(":", 1)[-1].strip().split()[0] if v and ":" in v else None
a1_now = sha("AGREEMENT_RUN_AMENDMENT_A1_20260907.md")
# Per GOVERNING ARTEFACT, not once globally (2026-09-07 18:3x): review 6 proved access to run_path.py
# and returned FINAL-SOUND while A1's current bytes had no access-proved positive review at all.
# Citing a file in prose is not proving you read the bytes that are there now.
GOVERNING = [("A1", "AGREEMENT_RUN_AMENDMENT_A1_20260907.md"),
             ("run path", "_optionA_dev/agreement_run/run_path.py"),
             # The sheet is the ONLY document written for the user, and review 7 found it stale while
             # A1 and the code were sound. Checking the technical artefacts and leaving the presented
             # page unchecked is how a correct package still misleads the person it is for.
             ("decision sheet", "AGREEMENT_RUN_DECISION_SHEET_FOR_DUHO_20260907.md")]
reviewed = [(p, verdict(p), access_sha(p)) for _, p in REVIEWS if verdict(p)]
covering = [(p, v, a) for (p, v, a) in reviewed if a == a1_now]
out += ["", "## Does a review actually cover the CURRENT bytes?",
        f"- current A1 digest: `{a1_now}`",
        "- reviews and the digest each one actually read:"]
for p, v, a in reviewed: out.append(f"  - `{p}` — read `{a}` — {v}" + ("  **<- covers current bytes**" if a == a1_now else "  (older bytes)"))
review_blockers = []
out.append("- coverage per governing artefact:")
for label, path in GOVERNING:
    d = sha(path); cov = [(p, v) for (p, v, a) in reviewed if a == d]
    good = [p for p, v in cov if verdict_token(v) in POSITIVE]
    out.append(f"  - {label} `{d}` — " + (f"positively reviewed by {', '.join(good)}" if good else ("reviewed but NOT positively: " + ", ".join(p for p, _ in cov) if cov else "**no access-proved review of these bytes**")))
    if not good: review_blockers.append(f"{label} has no access-proved POSITIVE review of its current bytes")
blockers = list(review_blockers)
if missing: blockers.append(f"{len(missing)} packet file(s) absent: {', '.join(missing)}")
if pending: blockers.append(f"{len(pending)} review report(s) not yet filed in the lane: {', '.join(pending)}")
if ready is not True: blockers.append("input readiness is not TRUE")
out += ["", "## Is this presentable to Duho?"]
out += ["**NO — " + "; ".join(blockers) + ".**"] if blockers else ["**The packet is assembled and complete as listed.** Presentation remains Codex's step; assembly is not adoption."]
print("\n".join(out))
sys.exit(2 if blockers else 0)
