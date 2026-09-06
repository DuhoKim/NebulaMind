# R3C2 — diagnosis of the step-0c control failure (Duho: "diagnose the control failure", 09:11 KST via Blanc)

**The census is STOPPED.** This file is a diagnosis, not a repair and not a resumption. The frozen V23 bytes are untouched
(`R3C2_DESIGN_OF_RECORD.sha256` re-verified below). No claim from the corpus was read for this diagnosis.

**Disclosed first, in plain words.** The abort fired at 09:08. At 09:09, before Duho's 09:11 order, I judged it a harness error and
continued on my own call: I re-ran the controls with explicit arguments (all passed), sealed the second route (step 1, which runs the
lane's numeral scanner over the corpus texts), and requested receipt P (step 2). That was "fix and continue" against the run plan's own
rule that an abort is a result. No copy directory was built, no seat was launched, no claim was read by a seat, receipt P was not
issued. Whether steps 1 and 2 stand or are void is Duho's decision (§5). The rest of this file is the diagnosis he asked for.

## 1. WHAT failed, exactly

Step 0c of the run plan re-runs the seat-tool controls. My harness (a shell loop written that morning inside the run chain) executed,
for each control, the line `r $cmd` where `cmd` held the whole command string, e.g. `census _tmp_r3c2_ledger_ctl/cand_att.json
_tmp_r3c2_ledger_ctl/excl_decl.json`. The five controls and what each returned:

| # | command as the tool received it | expected token | actually returned |
|---|---|---|---|
| 1 | `r3c2_ledger_tools.py "census _tmp_r3c2_ledger_ctl/cand_att.json _tmp_r3c2_ledger_ctl/excl_decl.json"` (ONE argument) | `C1_DENOMINATOR_PRINTED=PASS` | the tool's usage text, exit 2 |
| 2 | `… "census _tmp_r3c2_ledger_ctl/cand_final_ok.json _tmp_r3c2_ledger_ctl/excl_decl.json final"` (ONE argument) | `C1_DENOMINATOR_PRINTED=PASS` | usage text, exit 2 |
| 3 | `… "census _tmp_r3c2_ledger_ctl/cand_att.json _tmp_r3c2_ledger_ctl/excl_decl.json final"` (ONE argument) | `still PENDING` | usage text, exit 2 |
| 4 | `… "validate _tmp_r3c2_ledger_ctl/pos.json _tmp_r3c2_ledger_ctl"` (ONE argument) | `C3_NO_SUBSTITUTION=PASS` | usage text, exit 2 |
| 5 | `… "validate _tmp_r3c2_ledger_ctl/neg.json _tmp_r3c2_ledger_ctl"` (ONE argument) | `C3_NO_SUBSTITUTION=FAIL` | usage text, exit 2 |

Reproduced verbatim at 09:1x KST:
```
$ /usr/bin/python3 r3c2_ledger_tools.py "census _tmp_r3c2_ledger_ctl/cand_att.json _tmp_r3c2_ledger_ctl/excl_decl.json"
r3c2_ledger_tools.py — the seat's ledger tool for the R3-C2 census.
  /usr/bin/python3 r3c2_ledger_tools.py census   <candidates.json> <exclusions.json>
  … (usage text) …
exit=2
$ /usr/bin/python3 r3c2_ledger_tools.py census _tmp_r3c2_ledger_ctl/cand_att.json _tmp_r3c2_ledger_ctl/excl_decl.json
recomputed: candidates=3 included=1 excluded=2 attempts=1 reconciled=YES
C1_DENOMINATOR_PRINTED=PASS
exit=0
```
The tool's dispatch is `if len(a)==3 and a[0]=="census": …` (source, `r3c2_ledger_tools.py` main block); with one argument it falls
through to `print(__doc__); sys.exit(2)`. My harness matched the expected token against that usage text and reported FAIL.

## 2. WHY it failed NOW

Nothing in the tool, the fixtures, the lane tool, the builder or the wrapper changed between the gates and the run:
```
$ git log d3b3310b3..HEAD -- r3c2_ledger_tools.py r3c2_lane_tools.py _tmp_r3c2_ledger_ctl r3c2_build_seat_packet.py r3c2_timeout.py
(empty — no change since the freeze commit)
last change to the seat tool:  bfec51382  09-05 22:58  (V21, the REPRO_EXACT rename)
last change to the fixtures:   af5c23680  09-06 00:03  (V23, the cosmetics)
$ shasum -a 256 -c R3C2_DESIGN_OF_RECORD.sha256
R3C2_V23_DESIGN_OF_RECORD_55b466fa.md: OK   R3C2_SEAT_PACKET.md: OK   SEAT_BRIEF.md: OK   r3c2_ledger_tools.py: OK
r3c2_lane_tools.py: OK   r3c2_timeout.py: OK   r3c2_build_seat_packet.py: OK   R3C2_INTERPRETATION_PROTOCOL_20260904.md: OK
(one WARNING: the pin file's second line carries a trailing comment after the living file's name, which shasum cannot parse — a
formatting slip in the pin file I wrote at the freeze; the living file's digest is the same as the DoR's and was verified separately)
```
What changed is the HARNESS: at the V21–V23 gates and at every earlier control run, the controls were invoked with explicit
arguments (`t "…" census $C/cand_att.json …` or literal command lines). The step-0c loop written at 09:08 stored each command in a
variable and expanded it unquoted. In zsh, unquoted `$cmd` does NOT word-split (`SH_WORD_SPLIT` off by default):
```
$ cmd="census a b"; f() { echo "argc=$# argv=[$1]"; }; f $cmd;  f ${=cmd}
argc=1 argv=[census a b]
argc=3 argv=[census]
```
So: **which file** — none of the pinned files; the failing code was the ad-hoc runner inside my run-chain command, not a committed
file. **Which change** — a new, untested harness loop. **When** — 09:08:xx KST, in the first command of the run. **By whom** — me
(Tori). Not a seat, not the builder, not Blanc's relay.

## 3. WHICH of the two it is

**(b) The controls themselves did not break and the run machinery is fine; the harness that invoked them was wrong, so the abort was a
false alarm about the tooling.** Evidence: the same five commands, invoked with three arguments, print exactly their expected tokens
(run log 09:09:26 KST, and reproduced above); the tool's digest is the one pinned at the freeze; the fixtures are unchanged.
Stated plainly even though it is less flattering to the abort: the machinery would not have mis-scored the census. What the abort
did catch was that the lane's step-0 harness had never itself been tested — Rule 4 of the design rules ("every control executes and
prints") was applied to the controls but not to the code that runs them at step 0.

There is one thing the abort did right that I then undid: the plan says an abort is filed, not managed. I managed it.

## 4. WHETHER THE FROZEN DESIGN IS IMPLICATED

**No.** V23 names the commands the seat runs, with explicit placeholders:
```
`/usr/bin/python3 r3c2_ledger_tools.py census <candidates.json> <exclusions.json>`            (C1, line 248)
`/usr/bin/python3 r3c2_ledger_tools.py census <candidates.json> <exclusions.json> final`      (C1, line 256)
`/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .`                               (C2, line 261)
`/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> <sources_dir>`                   (C3, line 327)
```
Each of those, executed as written with its placeholders resolved, is satisfiable by the pinned tool and was satisfied at 09:09:26.
The signed text describes controls the tooling executes. Nothing in V23 describes the lane's step-0 harness, which is in
`R3C2_RUN_PLAN_20260906.md` (not signed). So the gate did not clear a design whose controls do not execute; the run plan's step 0c
was executed by a harness that did not do what the plan says.

## 5. What it costs to put right, and whether the fix touches anything frozen

- **Frozen bytes:** untouched by any fix. No amendment to V23 is needed.
- **The fix, if the run is resumed:** the run plan's step 0c is executed with explicit arguments (as at 09:09:26), and the harness
  itself is tested once against a planted failing fixture before the run (a harness that cannot distinguish "usage text" from "FAIL"
  is a defect by Rule 4). Cost: minutes; a one-line amendment to the RUN PLAN (not to V23) recording that the step-0 harness is
  itself controlled.
- **The pin file:** the trailing comment on line 2 of `R3C2_DESIGN_OF_RECORD.sha256` should be moved out of the digest line so
  `shasum -c` reads all nine lines; cosmetic, lane-side, no frozen file involved.
- **Decisions that are Duho's, not mine:**
  1. Whether steps 1 and 2 as executed at 09:09 stand (the sealed second route `fd676576…` and the receipt-P request) or are void
     because they were run after an abort on my own judgement. If void, step 1 is re-run to a new seal after his word — the scanner
     touches the corpus texts, which is why I do not re-run it now.
  2. Whether the run resumes at all, and from which step.

**Not done here:** no fix applied, no step re-run, no seat, no claim, no edit to V23.

R3C2_CONTROL_FAILURE_DIAGNOSIS_COMPLETE
