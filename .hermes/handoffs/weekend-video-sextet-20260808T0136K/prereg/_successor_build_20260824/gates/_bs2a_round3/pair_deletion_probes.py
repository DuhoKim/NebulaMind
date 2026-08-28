#!/usr/bin/env python3
"""Round-3 PAIR deletion probes, streaming progress. See single-code deletion_probes.py
for methodology notes (filters refusal codes post-hoc from the real verify_receipt output;
equivalent to deleting the refuse() call since nothing branches on `bad`'s contents besides
the E01/E02 structural early return, which is unaffected by filtering later codes)."""
import sys, json, itertools, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "ref"))
import bs2a_quality_gate as G

ACQ = Path(__file__).resolve().parent.parent.parent / "acquire"
ev0, rec0 = G.authenticated_fixture(ACQ)

def fresh():
    return [dict(e) for e in ev0], json.loads(json.dumps(rec0))

def make_filtered_verify(delete_codes):
    def filtered(receipt, evidence):
        bad = G.verify_receipt(receipt, evidence)
        return [b for b in bad if not any(b.startswith(f"[{c}]") for c in delete_codes)]
    return filtered

def run_self_test_with(verify_fn):
    ev, rec = fresh()
    base = verify_fn(rec, ev)
    results = {"baseline": (not base, set())}
    for name, mutate, expect in G.CONTROLS:
        ev2, rec2 = fresh()
        rec2, ev2 = mutate(rec2, ev2)
        got = G.codes_of(verify_fn(rec2, ev2))
        results[name] = (got == expect, got)
    return results

codes_sorted = sorted(G.CODES)
pairs = list(itertools.combinations(codes_sorted, 2))
t0 = time.time()
silent = []
for idx, (a, b) in enumerate(pairs):
    vf = make_filtered_verify({a, b})
    results = run_self_test_with(vf)
    mismatches = {name: got for name, (ok, got) in results.items() if not ok}
    caught = len(mismatches) > 0
    if not caught:
        silent.append((a, b))
        print(f"[{idx+1}/{len(pairs)}] delete {a}+{b}: SILENT-DEFECT", flush=True)
    if (idx + 1) % 25 == 0:
        elapsed = time.time() - t0
        print(f"[{idx+1}/{len(pairs)}] progress, {elapsed:.1f}s elapsed", flush=True)

print(f"DONE. {len(pairs)} pairs tested in {time.time()-t0:.1f}s.", flush=True)
print(f"Pair-deletion silent (undetected) pairs: {silent if silent else 'NONE'}", flush=True)
