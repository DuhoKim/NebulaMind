#!/usr/bin/env python3
"""Unattended overnight study loop for the NebulaMind Lab runner.

Runs a queue of study specs through the worker's process(), triages each against
the publishability bar, and writes a STATUS ledger for dawn review. Safety
envelope (Lana's lane):
  - Sandboxed: writes ONLY to its own run dir (--dir); LAB_RUNS_DIR is pinned there.
  - No publish / DB write / deploy / git / paid credits. Local Ollama + ADS
    grounding only (inherited from the worker). Nothing is landed on the board —
    that stays a separate, human-gated step.
  - Honors a STOP sentinel file (checked before each run) and a runtime/run budget.
  - Every attempt is logged (STATUS.jsonl + STATUS.md), successes AND shelves.

Default queue: a reionization f_esc photon-budget redshift sweep (z=7..10) that
extends the z~6 result into the JWST high-z regime where the "crisis" is claimed.
Override with --queue <json-list-of-specs> to run anything else.
"""
import os, sys, json, time, argparse
from pathlib import Path


def triage(rec):
    """Fable's bar: done + grounded + referee ACCEPT/MINOR + (f_esc) non-circular."""
    res = rec.get("result") or {}
    st = rec.get("status")
    grounded = bool(rec.get("lit_grounded"))
    verdict = (res.get("review_verdict") or "").upper()
    fesc = res.get("fesc") or {}
    noncirc = fesc.get("noncircular_robust")
    ok = (st == "done") and grounded and verdict in ("ACCEPT", "MINOR")
    if fesc:
        ok = ok and bool(noncirc)
    label = "REVIEW" if ok else ("SHELVE" if st and st.startswith(("done", "gated")) else "FAILED")
    return {"status": st, "grounded": grounded, "verdict": verdict or None,
            "noncircular": noncirc, "triage": label, "headline": (res.get("summary") or "")[:200]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="sandbox run dir (all output stays here)")
    ap.add_argument("--queue", default="", help="optional JSON file: a list of run specs")
    ap.add_argument("--max-runs", type=int, default=20)
    ap.add_argument("--max-minutes", type=float, default=360.0)
    a = ap.parse_args()

    rundir = Path(a.dir).resolve()
    rundir.mkdir(parents=True, exist_ok=True)
    os.environ["LAB_RUNS_DIR"] = str(rundir)                 # pin worker output to the sandbox
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import lab_runner_worker as W                            # noqa: E402  (after LAB_RUNS_DIR is set)

    if a.queue and Path(a.queue).exists():
        specs = json.loads(Path(a.queue).read_text())
    else:
        specs = [{"topic": "reionization-photon-budget", "topic_source": "overnight-loop",
                  "data_sources": ["jwst"], "method": "ionizing-photon-budget", "z0": z,
                  "outputs": ["aastex-draft", "dr-review-loop"], "force": True}
                 for z in (7, 8, 9, 10)]

    stop = rundir / "STOP"
    status_md = rundir / "STATUS.md"
    status_jsonl = rundir / "STATUS.jsonl"
    ledger = []
    t0 = time.time()

    def write_status(state):
        n_rev = sum(1 for e in ledger if e["triage"] == "REVIEW")
        n_shv = sum(1 for e in ledger if e["triage"] == "SHELVE")
        n_fai = sum(1 for e in ledger if e["triage"] == "FAILED")
        L = [f"# Overnight loop — {state}", "",
             f"run dir: `{rundir}`", f"elapsed: {(time.time()-t0)/60:.1f} min | "
             f"runs: {len(ledger)}/{len(specs)} | REVIEW: {n_rev} | SHELVE: {n_shv} | FAILED: {n_fai}", "",
             "| # | id | study | grounded | verdict | triage | headline |",
             "|---|----|-------|----------|---------|--------|----------|"]
        for i, e in enumerate(ledger, 1):
            L.append(f"| {i} | {e['id']} | {e['study']} | {'yes' if e['grounded'] else 'no'} | "
                     f"{e.get('verdict') or '-'} | **{e['triage']}** | {e['headline'][:80].replace('|','/')} |")
        L += ["", f"Emergency stop: `touch {stop}` (halts before the next run).",
              "Nothing landed on the board — REVIEW items await your sign-off."]
        status_md.write_text("\n".join(L))

    write_status("STARTED")
    for i, spec in enumerate(specs):
        if stop.exists() or len(ledger) >= a.max_runs or (time.time()-t0)/60 >= a.max_minutes:
            break
        rid = f"ovl{int(t0) % 100000}{i:02d}"
        rec = {"id": rid, "spec": spec, "status": "queued",
               "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "log": ["queued by overnight loop"], "artifacts": [], "result": None}
        (rundir / f"{rid}.json").write_text(json.dumps(rec, indent=2))
        try:
            W.process(rec)
        except Exception as e:                               # never let one bad run kill the loop
            rec["status"] = "failed"; rec.setdefault("result", {})["error"] = str(e)[:200]
            (rundir / f"{rid}.json").write_text(json.dumps(rec, indent=2))
        rec = json.loads((rundir / f"{rid}.json").read_text())
        entry = {"id": rid, "study": f"{spec.get('method')} z={spec.get('z0', '-')}", **triage(rec)}
        ledger.append(entry)
        with open(status_jsonl, "a") as f:
            f.write(json.dumps(entry) + "\n")
        write_status("RUNNING")

    final = "STOPPED" if stop.exists() else "DONE"
    write_status(final)
    n_rev = sum(1 for e in ledger if e["triage"] == "REVIEW")
    print(f"overnight loop {final}: {len(ledger)} runs, {n_rev} for review. STATUS -> {status_md}")


if __name__ == "__main__":
    main()
