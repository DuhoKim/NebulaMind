#!/usr/bin/env python3
"""Completion-day verification. Run when the transfer reports accepted >= total.

VERIFICATION ONLY. This deliberately stops before the one-shot strata computation:
whether strata are EVER computed is Duho's open decision (the decline memo is unsigned,
and the footprint power finding makes the hand-check's value his call, not a default).
Running this script commits nothing and reads no chi value.
"""
import json, subprocess, sys

ok = True
def check(name, got, want):
    global ok
    good = (got == want)
    ok &= good
    print(f"{'PASS' if good else 'FAIL'}  {name}: {got}{'' if good else f'  (wanted {want})'}")

# 1. transfer complete, nothing quarantined.
# WORKING_SET is the frozen prereg working set. The heartbeat carries a `total` key today,
# but a live process's status file is not a schema contract (Blanc, 2026-08-22) — this
# script depends on nothing the heartbeat is not guaranteed to hold, and any absent key
# is a clear FAIL, never a traceback.
WORKING_SET = 60308
h = json.load(open("/Users/duhokim/NebulaMindData/dr10_south_image_r/heartbeat.json"))
accepted = h.get("accepted")
check("heartbeat carries `accepted`", accepted is not None, True)
check("bricks accepted", accepted, WORKING_SET)
if h.get("total") not in (None, WORKING_SET):
    check("heartbeat total agrees with frozen working set", h.get("total"), WORKING_SET)
import os
q = "/Users/duhokim/NebulaMindData/dr10_south_image_r/quarantine"
check("quarantine empty", len(os.listdir(q)) if os.path.isdir(q) else 0, 0)

# 2. every accepted receipt matches the producer's digest list (task 26 final run)
r = subprocess.run([sys.executable, __file__.rsplit("/",1)[0] + "/crosscheck.py"],
                   capture_output=True, text=True)
print(r.stdout.strip())
check("producer cross-check exit", r.returncode, 0)

# 3. every parent object resolved by the cutter (receipt count vs parent count)
d = "/Users/duhokim/NebulaMindData/cutouts_dr10_south/receipts"
n = sum(1 for _ in os.scandir(d)) if os.path.isdir(d) else 0
check("cutter receipts (resolved objects)", n >= 208407, True)
print(f"      (exact count {n:,}; tensors may be fewer than 208,407 — absence-by-coverage is a")
print(f"       resolved outcome, not a failure; the resolved/tensor split is reported, not judged)")

# 4. chi measured everything the cutter produced
t = "/Users/duhokim/NebulaMindData/cutouts_dr10_south/tensors"
nt = sum(1 for _ in os.scandir(t)) if os.path.isdir(t) else 0
x = json.load(open("/Users/duhokim/NebulaMindData/chi_dr10_south/chi_heartbeat.json"))
check("chi measured == tensors", x.get("measured"), nt)
if x.get("measured") != nt:
    print("      (chi trails the cutter by minutes while draining — if the transfer just")
    print("       finished, rerun this script after the chain drains; a persistent gap is real)")

print()
print("VERIFIED — acquisition complete and custody clean." if ok else "PROBLEMS — do not proceed.")
print("STOP HERE. Strata / tertiles are NOT computed by this script. That step is one-shot,")
print("irreversible under condition 1, and waits on Duho's decision about the study.")
sys.exit(0 if ok else 1)
