import io,sys,re
T,OLD,SCR=sys.argv[1:4]
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read()
E=[]
def E_(o,n,t): E.append((o,n,t))
E_("**Tori, 2026-09-05. Version 11 (see §10; §10.5 for the V10 gate reconciliation).","**Tori, 2026-09-05. Version 12 (see §10; §10.6 for the V11 gate reconciliation).","header")
E_("**A seat may not supply a value for an `ABSENT` input.** Encountering one ends that claim's attempt.",
"**A value the paper does not print but traces to a named source that is itself a text in `R3C2_CORPUS_MANIFEST.md` is\nclassified `PRINTED` from that source, with `origin` `IMPORTED`, `origin_evidence` `ORIG_CITATION` cited to the named\nsource's file and line, and the value machine-matched there.** **A seat may not supply a value for an `ABSENT` input.**\nEncountering one ends that claim's attempt.","§2 cited-from-pinned-source")
E_("what does that\nnumber rest on — derived and standard inputs only, or a chosen, fitted, imported or undeclared one?**","what does that\nnumber rest on — derived, standard or measured inputs only, or a chosen, fitted, imported or undeclared one?**","§1 measured")
E_("**One pass, two tallies (option (c), the principal's ruling 2026-09-05).**","**One pass, two tallies.**","R4 §3 heading")
E_("*(V10, option (c): refusing chosen\n   inputs stopped this being reproduction at all — a paper can direct you to use its own chosen constant, and\n   following that instruction IS reproducing the paper.)*","*(A paper can direct you to use its own chosen constant, and following that instruction is reproducing the\n   paper.)*","R4 §2 note")
E_("**exactly\n`REPRO_EXACT` and `REPRO_FAILED`** (V10; the group had three members under the derivation-only wording).","**exactly\n`REPRO_EXACT` and `REPRO_FAILED`**.","R4 group note")
E_(" *(What `root_origins` implies for a\n  claim's outcome follows from the clause held in §3 and is not decided here; the field is factual either way.)*","","R3 stale parenthetical")
E_("A chain cannot be made to look clean by classifying only its last step.","A chain's root origins are computed from every step, never from its last step alone.","look clean")
E_("`C4_PATTERN_BLIND=PASS` requires that printed path list; any path outside the copy directory is `FAIL`.","`C4_PATTERN_BLIND=PASS` requires that printed path list and means only that the list contains no outside path; it\n  makes no claim that the list is complete. Any path outside the copy directory is `FAIL`.","C4 self-report (pre-rename)")
E_("C4_PATTERN_BLIND","C4_SEAT_ISOLATION","R2 token (all)")
E_("is (equation number, reference number, page/line number, date, or attributed-not-derived).","is (equation number, reference number, page/line number, date, or attributed-not-derived). **The exclusion ledger's\n`kind` is one of `EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`, `ATTRIBUTED_NOT_DERIVED`.**","R7 kinds")
E_("containing the\n  **seat packet** — not this document — the seat brief `SEAT_BRIEF.md`, the script `r3c2_ledger_tools.py`, and the\n  pinned sources of `R3C2_CORPUS_MANIFEST.md`,","containing the\n  **seat packet** — not this document — the seat brief `r3c2_seat_packet/SEAT_BRIEF.md` (committed beside the packet,\n  asserted against the same forbidden list by the builder, and pinned in `R3C2_SEAT_PACKET.sha256`), the script\n  `r3c2_ledger_tools.py`, and the pinned sources of `R3C2_CORPUS_MANIFEST.md`,","R6 brief")
E_("does not judge reachability.** `C0_REACHABILITY=PASS`.","does not judge reachability.** `C0_REACHABILITY=PASS|FAIL|NOT_RUN` — PASS only when every required row has been\n  independently exhibited and verified; FAIL when any required row is absent or cannot produce its declared condition;\n  NOT_RUN when C0 was not reached.","C0 token")
E_("A `rests_on` value written by a seat, or absent, fails this control.","A `rests_on` value present in the seat-authored input ledger fails this control; after a successful `compute` run,\n  a `rests_on` value absent from the script-produced output ledger fails this control.","C3 input/output")
E_("receipt verification fails**. The census is void; report which.","receipt verification fails**. No tally is filed; report which.","void -> neutral")
E_("**asserts that no string on a forbidden list survives anywhere in the output**","**asserts that no string on the forbidden list survives anywhere in the output — the list blocks the enumerated\n  strings and does not establish that every consequence-bearing word is gone; procedural consequences of stop outcomes\n  remain visible while hypothesis mappings, comparison-model preferences and empirical stakes are removed**","forbidden-list claim")
E_("validated by `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> <sources_dir>`","validated by `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .` run from the printed seat working\n  directory (`.` is the sole allowed `sources_dir`); before execution the seat prints the fully resolved command with\n  every angle-bracket placeholder replaced by the actual in-scope path","sources_dir")
E_("`OUT_OF_SCOPE` row fails the control.** `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN`.","`OUT_OF_SCOPE` row fails the control; PASS means the printed list contains no such row and makes no claim that the\n  list is complete.** `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN`.","C5b self-report")
E_("root; the code precedence makes the citation win.","root; the code precedence makes the citation win. A reason code that matches its quotation but misapplies the\n  precedence is caught only by the second seat's independent classification and the C6 re-classification, never by the\n  machine; if every reader misclassifies identically, the record stands — that floor is stated here rather than implied\n  away.","Q2 floor (redacted region)")
m=re.search(r"^\| V11 \| \*this version\* \|.*$",s,re.M); assert m
E_(m.group(0),f"""| V11 | `{OLD[:16]}…` | C0 two seats AGREE (`R3C2_C0_EXHIBITION_V11_codex…`, `…kimi…`); `R3C2_GATE_V11_codex_20260905.md`, `R3C2_GATE_V11_kimi_20260905.md` | C0 PASS+PASS; gate `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS`; codex LEAK=NONE, kimi CONSEQUENCE_VISIBLE=NO | see §10.6 |
| V12 | *this version* | *(C0 by two independent seats, then two-seat gate — pending)* | — | **both V11 lists applied; see §10.6** |""","V11/V12 rows")
E_("R3C2_PREREG_V11_READY_FOR_C0",f"""## 10.6 V12 — the V11 gate reconciled; what is settled, and both lists applied ({T})

**Both V11 verdicts bound to `{OLD[:16]}…` and to the packet `a3516349…`; both ACCESS and PACKET hashes verified by
the lane owner against the files after each seat exited: codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`.**

**Settled, and stated so it is not lost under a run of UNSOUND verdicts:** (1) **the definition question is answered
on both engines** — under option (c) every declared outcome is reachable and the reproduction question is decidable on
every hardest case either seat constructed; the one boundary both found (a value the claiming paper cites from another
pinned text but does not print) is a totality repair, not the tension returning. (2) **The leak is closed on
consequence:** codex, from the packet alone, `LEAK=NONE` — design history and procedural stop consequences only, no
hypothesis, model or preferred outcome; kimi `CONSEQUENCE_VISIBLE=NO` — no sentence makes any outcome weightier than
another. Those two things parked this study for eighteen hours. What remains is ordinary design repair.

**kimi's residual inferences from the packet, each traced to a framing survival and repaired without adding any
framing back:** the token `C4_PATTERN_BLIND` told the seat a pattern exists → renamed `C4_SEAT_ISOLATION` at every
occurrence and "pattern" added to the forbidden list; "the principal's ruling", two V10 notes and "look clean" →
neutral wording; the stale parenthetical pointing at "the clause held in §3" → deleted. The §1 question itself
(derived-or-not) and the Planck-only `STANDARD` list remain: content, not consequence.

**Applied from both lists:** the cited-from-pinned-source input is `PRINTED` from that source with `origin`
`IMPORTED` and the attempt proceeds (kimi R1) — **codex's replacement, which would stop every such claim as
`REPRO_BLOCKED`, is quoted and answered:** under option (c) a paper directing the reader to a value in a pinned text
is directing the reader to use it, and following that direction is reproducing the paper; `REPRO_BLOCKED` keeps the
unobtainable-source domain; exclusion-kind tokens stated (kimi R7); `SEAT_BRIEF.md` authored, committed beside the
packet, asserted by the builder and pinned (kimi R6); the script's usage text corrected for `MEASURED`, a missing
`candidate_id` reported as a failure line, script re-pinned (kimi R5, R9); C0's token three-valued (both); C3's
input-versus-output ledger sentence (codex); "The census is void" → "No tally is filed" and the forbidden-list claim
stated at its true strength (codex Q5); `<sources_dir>` fixed to `.` and resolved commands printed (codex Q4); C4 and
C5b PASS defined as "no outside path in the printed list", completeness not claimed (codex); the judgement floor on
reason-code choice stated, master-only (kimi Q2).

**Escalated, unchanged:** the `REPRO_EXACT` rename — both engines now call the name cosmetic; the principal's.

**V12 has NOT had its own C0 or gate. R3C2 is NOT frozen and NOT run.**

R3C2_PREREG_V12_READY_FOR_C0""","§10.6")
miss=[(t,s.count(o)) for o,n,t in E if o!="C4_PATTERN_BLIND" and s.count(o)!=1]
print("dry-run misses:",miss)
if miss: sys.exit(1)
for o,n,t in E: s=s.replace(o,n); print("  -",t)
n_old=s.count("ab3e2997fdea0b5843dc7f017e9bee2fa0234f21f89b35dab1a7e4b0570d95b8"); s=s.replace("ab3e2997fdea0b5843dc7f017e9bee2fa0234f21f89b35dab1a7e4b0570d95b8",SCR); print("  - script re-pinned at",n_old,"places")
io.open(p,'w',encoding='utf-8').write(s); print("V12 written")
