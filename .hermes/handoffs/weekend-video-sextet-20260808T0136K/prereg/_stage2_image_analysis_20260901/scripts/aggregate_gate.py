#!/usr/bin/env python3
"""AGGREGATE GATE v2 (Blanc 05:48 KST 09-07 — v1 accepted an 'OK' PREFIX and never rejected FAILED; it passed a synthetic failing log while printing 'every block
OK'. v1 is retained as scripts/_aggregate_gate_v1_RETAINED_defective.py; its two controls live in scripts/gate_fixtures/ and scripts/test_aggregate_gate.py).
PREDICATE — a log PASSES iff every one of these holds: the log splits into exactly --suites blocks (each opened by a line beginning '== '); every block contains
exactly ONE 'Ran N test(s)' line and exactly ONE result line, and that result line is EXACTLY 'OK' (a full-line match; 'OK (skipped=…)' does not count); no block
contains any line matching FAILED / ERROR / errors= / failures= / Traceback / <Name>Error / 'exit code' / 'exited with'; the Ran totals sum to exactly --tests.
The printed sentence names only those verified facts. Exit 0 = PASS; 2 = FAIL (every reason printed); 3 = usage."""
import re, sys, argparse
ap = argparse.ArgumentParser(); ap.add_argument("log"); ap.add_argument("--suites", type=int, required=True); ap.add_argument("--tests", type=int, required=True); a = ap.parse_args()
try: text = open(a.log, encoding="utf-8").read()
except OSError as e: print(f"AGGREGATE GATE: FAIL — cannot read log: {e}"); sys.exit(3)
BAD = re.compile(r"^(FAILED\b|ERROR\b|Traceback|[A-Za-z]+Error\b)|errors=|failures=|exit code|exited with", re.M)
RAN = re.compile(r"^Ran (\d+) tests? in", re.M); RESULT = re.compile(r"^(OK|OK \(.*\)|FAILED.*)$", re.M)
parts = re.split(r"^== ", text, flags=re.M); preamble, blocks = parts[0], parts[1:]; bad = []; ran_total = 0
if BAD.search(preamble): bad.append("a failure indication appears before the first suite block")
for b in blocks:
    name = b.split("\n", 1)[0].strip(); body = b.split("\n", 1)[1] if "\n" in b else ""
    rans = RAN.findall(body); results = RESULT.findall(body)
    if len(rans) != 1: bad.append(f"{name}: {len(rans)} 'Ran N' lines (exactly one required)")
    else: ran_total += int(rans[0])
    if len(results) != 1: bad.append(f"{name}: {len(results)} result lines (exactly one required)")
    elif results[0] != "OK": bad.append(f"{name}: result line is {results[0]!r}, not exactly 'OK'")
    for m in BAD.finditer(body): bad.append(f"{name}: failure indication: {body[m.start():m.start()+60].splitlines()[0]!r}"); break
if len(blocks) != a.suites: bad.append(f"{len(blocks)} suite blocks, {a.suites} required")
if ran_total != a.tests: bad.append(f"{ran_total} tests ran, {a.tests} required")
if bad: print("AGGREGATE GATE: FAIL — " + "; ".join(bad)); sys.exit(2)
print(f"AGGREGATE GATE: PASS — {len(blocks)} suite blocks (required {a.suites}); each with exactly one 'Ran N' line and exactly one result line equal to 'OK'; no FAILED / ERROR / errors= / failures= / Traceback / *Error / exit-code line anywhere; {ran_total} tests (required {a.tests})"); sys.exit(0)
