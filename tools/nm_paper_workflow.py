#!/usr/bin/env python3
"""nm_paper_workflow.py — instantiate a paper lane from PAPER_WORKFLOW_V1.

Duho, 2026-08-05: "build a workflow for each paper ... leveraging subscription models in max and
use Kimi model oversee from time to time, and report the results in a YouTube video."

This creates the lane skeleton and the stage checklist with seats already assigned, so a paper
starts with its gates named instead of inventing an order per lane. It runs nothing and reviews
nothing — it lays out the track.

    python3 tools/nm_paper_workflow.py new "<question>" --slug <slug>
    python3 tools/nm_paper_workflow.py status <lane-dir>
"""
import argparse, json, os, subprocess, sys, time

ROOT = "/Users/duhokim/NebulaMind/NebulaMind"
HANDOFFS = os.path.join(ROOT, ".hermes/handoffs")
SPEC = ".hermes/workflows/PAPER_WORKFLOW_V2.md"

# seat, kimi-gated?, what "done" means — the checklist is the contract with ourselves
STAGES = [
    # v2: designed by the crew (design-inputs/{GORU,TORI,YUI,LANA}_WORKFLOW_INPUT.md), not by Hwao alone
    ("0 global map",         "Goru",  False, "archive holdings AND corpus for this question held in ONE context (Goru: capacity is for unbroken context, not clerical bulk)"),
    ("1 framing",            "Goru→Lana", False, "what is contested, what would settle it"),
    ("1b prediction freeze", "Lana",  False, "what the literature predicts, receipted verbatim spans, sha-pinned BEFORE any data; scarcity recorded honestly"),
    ("1.5 evidence freeze",  "Yui",   False, "which figures/claims carry the story; source identity and rights; co-designed with video NOW, not after landing"),
    ("2 contract freeze",    "Lana/Hwao", True, "frame/cuts/statistic/honest-outcomes frozen, sha256 + chmod 444 BEFORE any science row"),
    ("2b amendment path",    "Lana",  None,  "ONLY if invoked: pre-result amendment, pre-result property itself receipted, gated by the author of the amended clause"),
    ("3 eligibility",        "Hwao",  False, "two-channel enumeration; per-table verdicts with verbatim receipts; quote-verification by script, not by a frontier model"),
    ("4 reviewed script",    "Hwao",  True,  "the only artifact allowed to produce numbers (demotable ONLY where stage 6 enforces funnel conservation by a non-author seat)"),
    ("5 execute + funnel",   "Hwao",  False, "counts and terminal states; every zero diagnosed with direct evidence"),
    ("5.5 data sanity",      "Goru",  False, "does the output make physical sense; automated diff vs expected bounds (Goru: static review cannot see live data shape)"),
    ("5b measurement",       "Hwao",  False, "the contracted statistic + uncertainty decomposition + forecast-vs-realized + sensitivity + negative controls. NO prose (Tori: v1 had no stage computing the result)"),
    ("6 receipts",           "Tori",  False, "totals re-added from raw artifacts; FUNNEL CONSERVATION: every input row reaches exactly one terminal state and they re-add to the input count"),
    ("7 draft",              "Lana",  False, "prose from receipted artifacts only; provenance block with hashes"),
    ("7b contradiction",     "Lana",  False, "enumerate what this contradicts and engage it"),
    ("8 referee",            "-",     True,  "overclaim hunt + claim-to-artifact binding; established / overstated / understated"),
    ("9 video",              "Yui",   False, "9A story → 9B evidence graphics → 9C audio gate → 9D paper-naive comprehension gate → 9E render → 9F upload (UNLISTED; the current uploader defaults to PUBLIC and must be replaced)"),
    ("10 landing",           "Duho",  False, "human gate"),
]

def new(question, slug):
    stamp = time.strftime("%Y%m%dT%H%M") + "K"
    lane = os.path.join(HANDOFFS, f"{slug}-{stamp}")
    os.makedirs(lane, exist_ok=True)
    checklist = {
        "workflow": "PAPER_WORKFLOW_V2", "spec": SPEC, "slug": slug,
        "question": question, "opened": time.strftime("%Y-%m-%d %H:%M KST"),
        "kimi_budget": {"planned_calls": sum(1 for s in STAGES if s[2] is True),
                        "note": "GATES not calls (Tori): a gate finding a defect spawns patch/micro-review/rerun cycles. Shape-1 spent 9 calls on one lane. Budget $10-15 per hard paper; re-gates are expected, never a reason to skip review."},
        "stages": [{"stage": n, "seat": s, "kimi_gate": k, "done_means": d, "state": "pending"}
                   for n, s, k, d in STAGES],
        "human_gates": ["Lab landing", "publication", "YouTube public", "new fetch channel", "new engine seat"],
    }
    json.dump(checklist, open(os.path.join(lane, "WORKFLOW_CHECKLIST.json"), "w"), indent=1)
    hist = os.path.join(lane, f"{slug}_history.json")
    subprocess.run([f"{ROOT}/backend/.venv/bin/python", f"{ROOT}/tools/nm_paper_history.py", "append",
                    "--file", hist, "--said", question,
                    "--changed", f"Lane opened under PAPER_WORKFLOW_V1: {len(STAGES)} stages, "
                                 f"{checklist['kimi_budget']['planned_calls']} Kimi gates (contract, script, referee).",
                    "--verdict", "DIRECTION", "--by", "Duho"], capture_output=True)
    print(f"lane: {lane}")
    for s in checklist["stages"]:
        print(f"  [{'K' if s['kimi_gate'] else ' '}] {s['stage']:22s} {s['seat']:6s} {s['done_means'][:70]}")
    print(f"\nKimi gates: {checklist['kimi_budget']['planned_calls']}  (~${1.42*checklist['kimi_budget']['planned_calls']:.2f} at measured rate)")

def status(lane):
    c = json.load(open(os.path.join(lane, "WORKFLOW_CHECKLIST.json")))
    done = sum(1 for s in c["stages"] if s["state"] == "done")
    print(f"{c['slug']}: {done}/{len(c['stages'])} stages · question: {c['question'][:70]}")
    for s in c["stages"]:
        mark = {"done": "x", "pending": " ", "blocked": "!"}.get(s["state"], "?")
        print(f"  [{mark}]{'K' if s['kimi_gate'] else ' '} {s['stage']:22s} {s['seat']:6s} {s['state']}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new"); n.add_argument("question"); n.add_argument("--slug", required=True)
    st = sub.add_parser("status"); st.add_argument("lane")
    a = ap.parse_args()
    new(a.question, a.slug) if a.cmd == "new" else status(a.lane)
