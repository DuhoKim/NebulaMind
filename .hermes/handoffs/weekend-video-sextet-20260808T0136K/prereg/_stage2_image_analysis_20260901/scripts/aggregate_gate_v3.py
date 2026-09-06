#!/usr/bin/env python3
"""AGGREGATE GATE v3 (Blanc 07:33 KST 09-07). v2 fixed the READING of the log; v3 also requires the evidence the v1 runner discarded at the SOURCE — each
child's REAL exit status and its COMPLETE, unfiltered output — as produced by scripts/run_suites.sh. A run PASSES iff ALL THREE hold:
 (1) EXIT STATUS: status.tsv has exactly --suites rows, one per log block in order with the same module names; every rc == 0; every block carries exactly one
     'EXIT <rc>' line and it is 'EXIT 0'; every suite's stdout.txt / stderr.txt exist and their sha256 equal the recorded ones;
 (2) COUNTS: exactly --suites blocks (opened by '== '); the 'Ran N' totals sum to exactly --tests; each block's 'Ran N' equals the 'Ran N' found in that
     suite's own full stderr.txt (unittest writes its summary to stderr);
 (3) GENUINE SUMMARIES: in each block AND in each suite's full stderr.txt: exactly one 'Ran N' line, exactly one result line, equal to exactly 'OK'; no line
     matching FAILED / ERROR / errors= / failures= / Traceback / <Name>Error anywhere in the block or in the full stdout/stderr.
The completion marker '## DONE …' is not a block. v3.1 (Blanc 07:49): suite dirs in status.tsv must be RELATIVE to the status file and are resolved against it; an absolute dir is a FAIL (relocation must be impossible to get wrong); dirs resolving outside the run directory are a FAIL. Any one failure → FAIL (exit 2, every reason printed); 3 = usage. v2 (scripts/aggregate_gate.py) is retained
unchanged and is NECESSARY BUT INSUFFICIENT: it accepts a log whose child exited 17 after printing 'Ran 1 / OK' (codex's probe; fixture gate_fixtures/exit17_ok_text)."""
import re, sys, argparse, hashlib, os
ap = argparse.ArgumentParser(); ap.add_argument("log"); ap.add_argument("--suites", type=int, required=True); ap.add_argument("--tests", type=int, required=True); ap.add_argument("--status", required=True); a = ap.parse_args()
try: text = open(a.log, encoding="utf-8").read(); rows = [l.rstrip("\n").split("\t") for l in open(a.status, encoding="utf-8") if l.strip()]
except OSError as e: print(f"AGGREGATE GATE v3: FAIL — cannot read inputs: {e}"); sys.exit(3)
BAD = re.compile(r"^(FAILED\b|ERROR\b|Traceback|[A-Za-z]+Error\b)|errors=|failures=", re.M)
RAN = re.compile(r"^Ran (\d+) tests? in", re.M); RESULT = re.compile(r"^(OK|OK \(.*\)|FAILED.*)$", re.M); EXIT = re.compile(r"^EXIT (-?\d+)$", re.M)
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
parts = re.split(r"^== ", text, flags=re.M); preamble, blocks = parts[0], parts[1:]; bad = []; ran_total = 0
if BAD.search(preamble): bad.append("a failure indication appears before the first suite block")
if len(blocks) != a.suites: bad.append(f"{len(blocks)} suite blocks, {a.suites} required")
if len(rows) != a.suites: bad.append(f"status.tsv has {len(rows)} rows, {a.suites} required")
for k, b in enumerate(blocks):
    head = b.split("\n", 1)[0]; name = head.split("  [")[0].strip(); body = b.split("\n", 1)[1] if "\n" in b else ""
    rans = RAN.findall(body); results = RESULT.findall(body); exits = EXIT.findall(body)
    if len(rans) != 1: bad.append(f"{name}: {len(rans)} 'Ran N' lines in the block (exactly one required)")
    if len(results) != 1: bad.append(f"{name}: {len(results)} result lines in the block (exactly one required)")
    elif results[0] != "OK": bad.append(f"{name}: block result line is {results[0]!r}, not exactly 'OK'")
    if len(exits) != 1: bad.append(f"{name}: {len(exits)} EXIT lines in the block (exactly one required)")
    elif exits[0] != "0": bad.append(f"{name}: EXIT {exits[0]} — the child did not exit 0")
    m = BAD.search(body)
    if m: bad.append(f"{name}: failure indication in the block: {body[m.start():m.start()+60].splitlines()[0]!r}")
    if k < len(rows):
        r = rows[k]
        if len(r) != 6: bad.append(f"{name}: malformed status row {r!r}"); continue
        idx, mod, rc, sh_out, sh_err, d = r
        if mod != name: bad.append(f"block {k+1} is {name!r} but status row {k+1} is {mod!r}")
        if rc != "0": bad.append(f"{name}: status.tsv rc={rc} (0 required)")
        if exits and exits[0] != rc: bad.append(f"{name}: block EXIT {exits[0]} disagrees with status.tsv rc={rc}")
        if os.path.isabs(d): bad.append(f"{name}: status row records an ABSOLUTE suite dir {d!r} — v3.1 requires dirs RELATIVE to the status file (portable; a relocated copy cannot point at live evidence); historical absolute-path runs are judged only through a VERIFIED portable copy (scripts/make_portable_run_copy.sh)")
        d = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(a.status)), d))
        if not os.path.abspath(d).startswith(os.path.dirname(os.path.abspath(a.status)) + os.sep): bad.append(f"{name}: suite dir resolves outside the run directory: {d!r}")
        so, se = os.path.join(d, "stdout.txt"), os.path.join(d, "stderr.txt")
        if not (os.path.isfile(so) and os.path.isfile(se)): bad.append(f"{name}: full stdout/stderr files missing under {d}"); continue
        if sha(so) != sh_out or sha(se) != sh_err: bad.append(f"{name}: full output files do not match the digests recorded at run time")
        err = open(se, encoding="utf-8", errors="replace").read(); out = open(so, encoding="utf-8", errors="replace").read()
        frans = RAN.findall(err); fres = RESULT.findall(err)
        if len(frans) != 1: bad.append(f"{name}: {len(frans)} 'Ran N' lines in the full stderr (exactly one required)")
        elif rans and frans[0] != rans[0]: bad.append(f"{name}: block says Ran {rans[0]}, full stderr says Ran {frans[0]}")
        if len(fres) != 1 or fres[0] != "OK": bad.append(f"{name}: full stderr result lines {fres!r} (exactly one, equal to 'OK', required)")
        for label, s in (("stderr", err), ("stdout", out)):
            mm = BAD.search(s)
            if mm: bad.append(f"{name}: failure indication in the full {label}: {s[mm.start():mm.start()+60].splitlines()[0]!r}")
    if len(rans) == 1: ran_total += int(rans[0])
if ran_total != a.tests: bad.append(f"{ran_total} tests ran, {a.tests} required")
if bad: print("AGGREGATE GATE v3: FAIL — " + "; ".join(bad)); sys.exit(2)
print(f"AGGREGATE GATE v3: PASS — {len(blocks)} suite blocks (required {a.suites}), each with a status row, EXIT 0 and matching full stdout/stderr files; each block and each full stderr with exactly one 'Ran N' line and exactly one result line equal to 'OK'; no FAILED / ERROR / errors= / failures= / Traceback / *Error line in any block or full output; {ran_total} tests (required {a.tests})"); sys.exit(0)
