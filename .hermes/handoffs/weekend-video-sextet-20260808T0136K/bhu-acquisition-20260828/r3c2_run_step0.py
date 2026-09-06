#!/usr/bin/env python3
"""r3c2_run_step0.py — the run plan's step-0c harness, as a tested script (Duho 09:33 KST: fix the quoting, then test the harness).
Usage: r3c2_run_step0.py <spec.json>   spec = [{"name", "argv": [...], "expect": "<token substring>"}]
Each control is one subprocess with an EXPLICIT argv list (never a joined string). PASS = the expected token appears in
stdout+stderr. Any FAIL → exit 1. Usage text from the tool (exit 2) is reported as FAIL with the reason, never as a pass."""
import json, subprocess, sys
spec = json.load(open(sys.argv[1])); fails = []
for c in spec:
    r = subprocess.run(c["argv"], capture_output=True, text=True); out = (r.stdout + r.stderr)
    ok = c["expect"] in out
    why = "" if ok else (" — tool returned usage text (exit 2): the command reached it mal-formed" if r.returncode == 2 and "Usage" in out or "usage" in out.lower() and r.returncode == 2 else f" — expected token absent; last line: {out.strip().splitlines()[-1][:120] if out.strip() else '(no output)'}")
    print(("PASS " if ok else "FAIL ") + c["name"] + "  $ " + " ".join(c["argv"]) + "  → " + c["expect"] + why)
    if not ok: fails.append(c["name"])
print(f"\nSTEP0C_HARNESS={'PASS' if not fails else 'FAIL'}  {len(spec)-len(fails)}/{len(spec)}" + (f"  FAILING: {fails}" if fails else ""))
sys.exit(1 if fails else 0)
