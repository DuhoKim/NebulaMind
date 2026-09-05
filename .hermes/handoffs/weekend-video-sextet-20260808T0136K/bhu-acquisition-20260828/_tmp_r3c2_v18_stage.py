#!/usr/bin/env python3
"""V18 stage: codex V17 gate items 7.1 (stale seat-tool compute/merge in the lane-only C3 block), 2.1 (C3 PASS predicate),
2.2 (C6 audit artefact). Extend with kimi's V17 items before applying. --check = verify anchors only, write nothing."""
import io, re, sys
p = "R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"
s = io.open(p, encoding="utf-8").read()
check = "--check" in sys.argv
def one(a):
    n = s.count(a); assert n == 1, (n, a[:70]); return a
# 7.1 — the whole stale redacted block, from the pin sentence to the end of its span
start = one("<!--SEAT-REDACT--> **The script is `r3c2_ledger_tools.py`,")
i = s.index(start); j = s.index("<!--/SEAT-REDACT-->", i) + len("<!--/SEAT-REDACT-->")
old_block = s[i:j]; assert "compute <ledger.json>" in old_block and "merge <ledger_seatA.json>" in old_block
new_block = ("<!--SEAT-REDACT--> **Lane side, after both seats have exited: the lane owner runs "
 "`/usr/bin/python3 r3c2_lane_tools.py merge <ledger_seatA.json> <ledger_seatB.json> <merged.json>` and then "
 "`/usr/bin/python3 r3c2_lane_tools.py compute <merged.json> <out.json>`, printing for each the working directory, the resolved "
 "command, complete stdout and stderr, and the exit status. `merge` exits 1 if the two `input_id` sets differ — **if `merge` exits 1, "
 "the two seats reconcile their input lists against the paper's stated equation once; an input-set difference surviving that "
 "reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations**; "
 "where the two `origin` classifications differ the merged record carries `origin_alt` and `origin_evidence_alt`. `compute` derives "
 "each claim's `root_origins` and `rests_on` and prints the root-origin set beside it; it REJECTS (exit 2) a ledger that arrives with "
 "`root_origins` or `rests_on` already set; it FAILS (exit 1) on a `derived_from` id that names no record, on a cycle, and on a "
 "`DERIVED` record with no `derived_from`, so an empty root set cannot occur; a disputed pair is computed under both origins and marked "
 "`DISPUTED`. The seat tool `r3c2_ledger_tools.py` has no `compute` and no `merge`; a seat that runs either has left its packet. "
 "A `rests_on` value present in a seat-authored input ledger fails this control; after a successful `compute` run, a `rests_on` value "
 "absent from the script-produced output ledger fails this control.**<!--/SEAT-REDACT-->")
s = s[:i] + new_block + s[j:]
# 7.1b — §9 names the seat tool for merge
a = one("a named command, `r3c2_ledger_tools.py merge`,"); s = s.replace(a, "a named command, `r3c2_lane_tools.py merge`,")
# 2.1 — C3 PASS predicate
a = one("  `C3_NO_SUBSTITUTION=PASS|FAIL|NOT_RUN`.")
s = s.replace(a, "  Each seat runs `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> <sources_dir>` with the placeholders\n"
 "  resolved and prints the working directory, the resolved command, complete stdout and stderr, and the exit status; the\n"
 "  control's printed artefact is that run.<!--SEAT-REDACT--> The lane's `merge` and `compute` runs are printed the same way and are\n"
 "  part of the same artefact.<!--/SEAT-REDACT--> `C3_NO_SUBSTITUTION=PASS` only on exit 0 from every printed run in the artefact; a\n"
 "  token asserted without the printed run is FAIL.\n" + a)
# 2.2 — C6 audit artefact
a = one("  **Classes are cited by name, never by number**. `C6_AUDIT_SAMPLE=PASS|FAIL|NOT_RUN`.")
s = s.replace(a, "  The auditor writes and prints `C6_AUDIT.json` containing: the sealed denominator, receipt T and the seed; the sorted\n"
 "  arithmetic-group ids and the sorted remaining ids; the computed k and the sampled ids; a completeness disposition for every\n"
 "  candidate and every exclusion; and, for every audited claim, the auditor's independently re-derived per-claim outcome, the\n"
 "  re-classified `origin` of each of its inputs, and `MATCH` or `MISMATCH` against the sealed record. `C6_AUDIT_SAMPLE=PASS` only if\n"
 "  that artefact exists, is printed, and carries no `MISMATCH` and no incompleteness; a token without the artefact is FAIL.\n" + a)
if check:
    print("V18 stage (codex items): anchors OK, nothing written")
else:
    io.open(p, "w", encoding="utf-8").write(s); print("V18 stage (codex items) APPLIED")
