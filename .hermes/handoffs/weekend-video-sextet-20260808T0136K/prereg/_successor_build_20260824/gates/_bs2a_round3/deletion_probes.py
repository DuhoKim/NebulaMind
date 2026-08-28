#!/usr/bin/env python3
"""Round-3 deletion probe battery. Does NOT edit the reviewed module. Instead:
  - imports the real module, uses its real verify_receipt/CONTROLS/CODES
  - simulates "deleting" a refusal code by filtering it out of the returned bad list
    post-hoc (equivalent for self-test purposes: nothing downstream in verify_receipt
    branches on `bad`'s contents except the E01/E02 early return, which is keyed off
    missing/extra, not bad, so filtering afterwards has identical observable effect to
    deleting the refuse() call at the source)
  - re-runs the FULL self-test control loop (using the module's own hardcoded CONTROLS
    expected sets, unmodified) against the filtered verifier
  - reports whether the deletion is CAUGHT (>=1 control mismatches) or SILENT (all
    controls still match their hardcoded expected sets despite the code being gone)

Tests every single code deletion, then every pair.
"""
import sys, json, itertools
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
    """Mirrors self_test()'s control loop exactly, using verify_fn instead of
    G.verify_receipt, and the module's own real CONTROLS/expected sets."""
    ev, rec = fresh()
    base = verify_fn(rec, ev)
    results = {"baseline": (not base, set())}
    for name, mutate, expect in G.CONTROLS:
        ev2, rec2 = fresh()
        rec2, ev2 = mutate(rec2, ev2)
        got = G.codes_of(verify_fn(rec2, ev2))
        results[name] = (got == expect, got)
    return results

def summarize(delete_codes, results):
    mismatches = {name: got for name, (ok, got) in results.items() if not ok}
    caught = len(mismatches) > 0
    return caught, mismatches

print("=== SINGLE-CODE DELETION PROBES ===")
single_silent = []
for code in sorted(G.CODES):
    vf = make_filtered_verify({code})
    results = run_self_test_with(vf)
    caught, mismatches = summarize({code}, results)
    status = "CAUGHT" if caught else "SILENT-DEFECT"
    print(f"  delete {code}: {status}" + (f"  mismatches={list(mismatches.keys())}" if caught else ""))
    if not caught:
        single_silent.append(code)

print()
print(f"Single-deletion silent (undetected) codes: {single_silent if single_silent else 'NONE'}")

print()
print("=== PAIR DELETION PROBES (all C(24,2)=276 pairs) ===")
pair_silent = []
codes_sorted = sorted(G.CODES)
for a, b in itertools.combinations(codes_sorted, 2):
    vf = make_filtered_verify({a, b})
    results = run_self_test_with(vf)
    caught, mismatches = summarize({a, b}, results)
    if not caught:
        pair_silent.append((a, b))

print(f"Pair-deletion silent (undetected) pairs: {pair_silent if pair_silent else 'NONE'}")
print()
print("=== DONE ===")
