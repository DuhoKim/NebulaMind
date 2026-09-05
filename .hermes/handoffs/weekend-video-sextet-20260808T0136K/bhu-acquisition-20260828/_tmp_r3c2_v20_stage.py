#!/usr/bin/env python3
"""V20 stage: codex V19 items 2.1 (literal final-census command) and 7.1 (dispatch inventory lists the pin file and the manifest).
Extend with kimi's V19 items before applying. --check = anchors only."""
import io,re,sys
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding="utf-8").read(); check="--check" in sys.argv
def rx(pat, repl, count=1):
    global s
    ms=list(re.finditer(pat, s)); assert len(ms)==count,(len(ms),pat[:70]); s=re.sub(pat, repl, s)
rx(r"the `census` subcommand run again after limb B with the word `final` verifies that every included\s+candidate carries exactly one §3 outcome, none `PENDING`, and that arithmetic-group outcomes carry both values;",
   "after limb B the seat runs `/usr/bin/python3 r3c2_ledger_tools.py census <candidates.json> <exclusions.json> final`, with\n  all placeholders resolved, and prints its output; that run verifies that every included candidate carries exactly one §3\n  outcome, none is `PENDING`, and arithmetic-group outcomes carry both values;")
rx(r"containing the \*\*seat packet\*\* — not this document — the seat brief `r3c2_seat_packet/SEAT_BRIEF\.md`",
   "containing the **seat packet** — not this document — the seat brief `r3c2_seat_packet/SEAT_BRIEF.md`, `R3C2_SEAT_PACKET.sha256`, `R3C2_CORPUS_MANIFEST.md`")
if check: print("V20 stage (codex items): anchors OK, nothing written")
else: io.open(p,"w",encoding="utf-8").write(s); print("V20 stage (codex items) APPLIED")
