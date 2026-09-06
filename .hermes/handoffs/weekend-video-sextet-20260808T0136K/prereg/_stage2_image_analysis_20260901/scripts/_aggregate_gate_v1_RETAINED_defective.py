#!/usr/bin/env python3
"""AGGREGATE GATE (Blanc 05:30 KST 09-07, after the V32 filing on a partial read): a staging record, a candidate text's aggregate claim, a commit and a review
dispatch are permitted ONLY if this gate passes on the aggregate log. It parses every `== <suite>` block and requires: every block ends in OK; no Error/NameError/
Traceback line anywhere; the number of blocks equals --suites; the summed `Ran N` equals --tests. Exit 0 = pass; exit 2 = fail (prints why). Never reads a tail —
the whole file."""
import re, sys, argparse
ap = argparse.ArgumentParser(); ap.add_argument("log"); ap.add_argument("--suites", type=int, required=True); ap.add_argument("--tests", type=int, required=True); a = ap.parse_args()
s = open(a.log, encoding="utf-8").read(); blocks = re.split(r"^== ", s, flags=re.M)[1:]; bad = []
if any(re.search(r"^(Traceback|NameError|ImportError|AttributeError|SyntaxError)", l) for l in s.split("\n")): bad.append("an exception line appears in the log")
ran = 0
for b in blocks:
    name = b.split("\n", 1)[0].strip(); m = re.search(r"^Ran (\d+) tests?", b, re.M); ok = re.search(r"^OK", b, re.M)
    if not m: bad.append(f"{name}: no 'Ran N' line"); continue
    ran += int(m.group(1))
    if not ok: bad.append(f"{name}: not OK")
if len(blocks) != a.suites: bad.append(f"{len(blocks)} suites in the log, {a.suites} expected")
if ran != a.tests: bad.append(f"{ran} tests ran, {a.tests} expected")
if bad: print("AGGREGATE GATE: FAIL — " + "; ".join(bad)); sys.exit(2)
print(f"AGGREGATE GATE: PASS — {len(blocks)} suites, {ran} tests, every block OK, no exception lines"); sys.exit(0)
