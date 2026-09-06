import io,sys,re
T,SEAT,LANE,MANI,BLD,NC,NP,PROT=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 26 — LIVING DRAFT: V25 + D1 wording B + the stronger D7 + ownership batching, the three APPROVED by Duho","Version 27 — LIVING DRAFT: V26 + the repairs from the two-seat gate on V26 and the routine `rests_on` label (§10.22); V26 = V25 + D1 wording B + the stronger D7 + ownership batching, the three APPROVED by Duho")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
rep("the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `8e990c7a22fb4b093d5e74218e9bfcee4b108c52bbc2df615ed3b6b2aaefa848`: `/usr/bin/python3 -E r3c2_lane_tools.py merge <ledger_seatA.json> <ledger_seatB.json> <merged.json>` and then `/usr/bin/python3 -E r3c2_lane_tools.py compute <merged.json> <out.json>`",
    "the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`: `/usr/bin/python3 -E r3c2_lane_tools.py merge <ledger_seatA.json> <ledger_seatB.json> <merged.json>` and then `/usr/bin/python3 -E r3c2_lane_tools.py compute <merged.json> <out.json> <candidates.json>` (the candidate argument is mandatory; compute without it exits 2 and writes no output)")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;\s+merge, then","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`; merge, then")
rep("`r3c2_manifest.py` is committed beside this document, sha256 `19a8ce4750bb47655868ef15b55f2b168833147b460c03ad56f84dd3c9bc56f2`, delivered in the seat's working directory and pinned in `R3C2_SEAT_PACKET.sha256`",
    "`r3c2_manifest.py` is committed beside this document, sha256 `"+MANI+"`, delivered in the seat's working directory and pinned in `R3C2_SEAT_PACKET.sha256`")
repx(r"this document,\s+sha256\s+`[0-9a-f]{64}`\s+\(it accepts explicit `--master`, `--out` and `--brief` arguments; the printed build command names them\);","this document, sha256 `"+BLD+"` (it accepts explicit `--master`, `--out` and `--brief` arguments; the printed build command names them);")
rep("command, run from this directory: `/usr/bin/python3 -E r3c2_build_seat_packet.py`; expected first line of output","command, run from this directory: `/usr/bin/python3 -E r3c2_build_seat_packet.py --master R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md --out r3c2_seat_packet/R3C2_SEAT_PACKET.md --brief r3c2_seat_packet/SEAT_BRIEF.md`; expected first line of output")
rep("the manifest command fails with `ERROR=<path>` and exit 1 on any symlink or non-regular entry, including a symlinked directory, rather than skipping it;",
    "the manifest command first rejects a root path that is a symlink or is not a directory, printing `ERROR=<path>` and exiting 1, then rejects every symlink or non-regular entry below that root, including symlinked directories, never following or silently skipping them;")
rep("for EVERY record whatever its status: `validate` requires a non-empty quotation and matches it at `origin_evidence.source_file`/`source_line`; for `STANDARD` it additionally requires the value as a numeric token at the record's own cited line and closed-list membership; for `BLOCKED` it checks the claiming paper's naming quotation while requiring an empty value.",
    "before any status-specific branch, `validate` requires every non-`ORIG_SILENT` record — `PRINTED`, `STANDARD`, `ABSENT` and `BLOCKED` alike — to carry a non-empty quotation occurring at the positive, one-based `origin_evidence.source_line` in `origin_evidence.source_file` (an `ABSENT` input keeps whatever origin its evidence supports — an unprinted measurement is `MEASURED` with its describing sentence quoted — and is not forced into `UNDECLARED` to close the corner); value-line checks are separate and never substitute for this evidence check; `STANDARD` additionally requires the value as a numeric token at the record's own cited line and closed-list membership; `BLOCKED` additionally requires an empty value and naming evidence in the claiming file.")
rep("For an import it then checks: the citing file is the claiming file; the two files differ; the source is an exact manifest row with verified bytes; the quotation is non-empty and present at the cited claiming line; the value is a numeric token at the cited source line; some line of the source carries both symbol and numeral, and the cited line is the first such line.",
    "For an external import, whose value line is outside the claiming file, validate checks that the evidence file is the claiming file, the external source is an exact manifest row with verified bytes, the non-empty quotation occurs at the cited claiming line, and the cited source line is the first line carrying both the symbol and the numeric value token. A locally printed import instead follows the local-import branch above.")
rep("the auditor re-derives each assigned claim and re-classifies each of its inputs' `origin` from the pinned sources, and the custodian seals those re-derivations by digest (`audit seal-rederivation`) BEFORE any sealed ledger is released.",
    "the auditor independently reconstructs each assigned claim's complete input records and dependency closure from the pinned sources, including cross-claim dependencies, recording status, value, source coordinates, origin evidence and `derived_from` for each input, and the custodian seals this reconstruction by digest (`audit seal-rederivation`) BEFORE any sealed ledger is released; `audit compare` compares those reconstructed fields and dependency edges against the sealed ledger, carrying a declared origin alternative explicitly, and a missing input, a differing dependency edge or an unsupported record is `MISMATCH`; it recomputes `root_origins` from both reconstructions and prints the comparison.")
rep("Limb B resumes the same ownership batches in separate sessions, writing final outcomes into separate limb-B copies of the four files, sealed in a separate ordered LIMB-B chain bound to the agreed limb-A seals; a sealed limb-A file is never overwritten; `join` of the limb-B chain verifies that binding.",
    "Limb B uses a separate directory from limb A: the custodian copies the agreed limb-A batch artefacts into that directory under the canonical names `candidates_b<k>.json`, `exclusions_b<k>.json`, `ledger_b<k>.json` and `SEAT_REPORT_b<k>.md`; the seat updates only these limb-B copies, records final outcomes, and runs `census … final` on them; the custodian seals and joins that directory in a separate ordered LIMB-B chain bound to the agreed limb-A seals file; the limb-A directory and seals remain unchanged; no `_limbB` filename suffix is used; `join` of the limb-B chain verifies the binding. The ownership list `OWNERSHIP_b<k>.txt` a session reads is the custodian's extract of the pinned partition, listed with its digest in the dispatch record.")
rep("validated by `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> . <candidates.json>` run from the printed seat working directory (`.` is the sole allowed `sources_dir`; the third argument is the seat's candidate file of C1 — per session its batch file, over the joined ledger the joined file)",
    "validated — after all limb-A batches are sealed and joined, since a cross-batch `derived_from` resolves only in the joined ledger (per-session validation is `NOT_RUN`) — by `/usr/bin/python3 -E r3c2_ledger_tools.py validate <joined_ledger.json> . <joined_candidates.json>` run from the seat's integration working directory holding all pinned texts (`.` is the sole allowed `sources_dir`); both seats' joined validation must PASS before limb-A agreement or arithmetic")
head,sep,hist=m.partition("\n## 10")
assert head.count("DERIVED_ONLY")>=1
head=head.replace("`DERIVED_ONLY` when every root origin is `DERIVED`, `STANDARD` or","`DERIVED_STANDARD_OR_MEASURED_ONLY` (the token `DERIVED_ONLY` of V10–V26, identical membership) when every root origin is `DERIVED`, `STANDARD` or")
head=head.replace("DERIVED_ONLY","DERIVED_STANDARD_OR_MEASURED_ONLY")
m=head+sep+hist
m=m.rstrip("\n")+f"""

## 10.22 V27 — the two-seat gate on V26, reconciled and repaired here; the `rests_on` label ({T})

C0 on V26: codex PASS, kimi PASS. Gate on V26: codex `PREREG_UNSOUND` (seven findings, three cosmetics; LEAK=NONE), kimi
`PREREG_SOUND_WITH_REPAIRS` (two non-cosmetic, one cosmetic, one corner; blind intact); both C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES, PRIOR_FINDINGS_CLOSED=NO. Reconciled BY TOPIC (`R3C2_V26_GATE_RECONCILIATION_20260906.md`); all routine, all
repaired here and in the tools (kit: {NC} controls, {NP} deletion probes, PASS), the graph bypass and the cross-batch lifecycle first as
Blanc's 23:44 order prioritised: the audit compares reconstructed input records and dependency edges and recomputes root origins
(codex F2 — the property D7 was approved for); limb B in a separate directory under canonical names (codex F4 / kimi F2); per-session
validation NOT_RUN, joined validation before limb-A agreement (codex F5); the shared evidence check for every non-silent record before
any status branch — extended, not bent: an `ABSENT` input keeps the origin its evidence supports and is not forced into `UNDECLARED`
(codex F1 / kimi F4; Blanc 23:44 §3); C3's second copy of the lane-tool pin and the two-argument compute, now mandatory three-argument
(codex F3 / kimi F1 / N2); C5's manifest pin (codex F6 / kimi F3); the manifest's root check (codex F7); the local-import summary
sentence (codex C1); the printed build command (codex C2); tool docstrings (kimi N1); the ownership list's provenance (kimi N3).

**The `rests_on` label, implemented as routine.** `DERIVED_ONLY` is renamed `DERIVED_STANDARD_OR_MEASURED_ONLY` in this version, the lane
tool (`{LANE[:16]}…`), the interpretation protocol (V5, `{PROT[:16]}…`, the receipt-P seal of the voided run superseded) and the kit; the
membership is unchanged (every root origin `DERIVED`, `STANDARD` or `MEASURED`). Both V26 gate reviewers found the rename LABEL-ONLY: no
class, passability, reachability or conclusion changes. It was therefore implemented under standing authority as routine work, not ruled
on (Blanc's order of 23:45, correcting his 23:44 hold); the historical token is preserved wherever a record states what an earlier
version said (§10, the V23 design of record, protocol V1–V4). Still Duho's: whether the census runs, and the signature on any successor
to V23. **Next:** C0 and the gate on V27; then the completed plan and digest to Blanc for the final-adoption checkpoint.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V27 master written; live DERIVED_ONLY before §10:", m.partition("\n## 10")[0].count("DERIVED_ONLY"))
b=io.open("r3c2_seat_packet/SEAT_BRIEF.md",encoding="utf-8").read()
def brep(a,c):
    global b; assert b.count(a)==1,a[:50]; b=b.replace(a,c)
brep("(V26: one session per ownership batch)","(V27: one session per ownership batch)")
brep("""4. Build `ledger_b<k>.json` (one record per input) under the packet's C3 schema, with `origin_evidence` for every record and no field
   outside the schema; run `/usr/bin/python3 -E r3c2_ledger_tools.py validate ledger_b<k>.json . candidates_b<k>.json` and print its output.""",
"""4. Build `ledger_b<k>.json` (one record per input) under the packet's C3 schema, with `origin_evidence` for every record and no field
   outside the schema; use globally qualified `derived_from` ids (a parent in another batch is named by its own id). Do NOT run `validate`
   in this session: C2/C3 are NOT_RUN per session, because a cross-batch `derived_from` resolves only in the joined ledger. After the
   custodian has sealed and joined all your limb-A batches, you run, in your integration working directory holding all pinned texts,
   `/usr/bin/python3 -E r3c2_ledger_tools.py validate <joined_ledger.json> . <joined_candidates.json>` and print its output.""")
brep("""Order of work (limb B session, dispatched only after the custodian's limb-A agreement and receipt): the same directory holds the
agreed `candidates_b<k>.json`; write final outcomes into a COPY `candidates_b<k>_limbB.json` (never modify the sealed limb-A file):
for each included claim, attempt the arithmetic exactly as the packet's section 2 prescribes, launching every symbolic operation
through the wrapper as the packet states; record one per-claim outcome from section 3 with both numbers where the packet asks for
them; then run `/usr/bin/python3 -E r3c2_ledger_tools.py census candidates_b<k>_limbB.json exclusions_b<k>.json final` and print its
output; write `SEAT_REPORT_b<k>_limbB.md` as in step 6, final line `R3C2_SEAT_B<k>_LIMB_B_COMPLETE`.""",
"""Order of work (limb B session, dispatched only after the custodian's limb-A agreement and receipt): this session's directory is
SEPARATE from the sealed limb-A session directory; the custodian has copied the agreed limb-A artefacts into it under the canonical
names `candidates_b<k>.json`, `exclusions_b<k>.json`, `ledger_b<k>.json`, `SEAT_REPORT_b<k>.md`. Update only these copies: for each
included claim, attempt the arithmetic exactly as the packet's section 2 prescribes, launching every symbolic operation through the
wrapper as the packet states; record one per-claim outcome from section 3 with both numbers where the packet asks for them, into
`candidates_b<k>.json`; keep `exclusions_b<k>.json` and `ledger_b<k>.json` as agreed; then run
`/usr/bin/python3 -E r3c2_ledger_tools.py census candidates_b<k>.json exclusions_b<k>.json final` and print its output; write
`SEAT_REPORT_b<k>.md` as in step 6, final line `R3C2_SEAT_B<k>_LIMB_B_COMPLETE`. No `_limbB` filename suffix is used.""")
io.open("r3c2_seat_packet/SEAT_BRIEF.md","w",encoding="utf-8").write(b); print("brief repaired")
