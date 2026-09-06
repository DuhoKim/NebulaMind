# Seat brief — reproduction census (V33: one session per ownership batch)

You are one of two independent seats, and this session is ONE of your batch sessions. Work only from the files in this directory:
`R3C2_SEAT_PACKET.md` (the rules), this brief, `r3c2_ledger_tools.py` (the pinned tool), `r3c2_manifest.py` (the pinned manifest
script), `r3c2_timeout.py` (the pinned wrapper), `R3C2_CORPUS_MANIFEST.md`, ALL the source texts it lists, and `OWNERSHIP_b<k>.txt` —
the list of the texts THIS session owns. Scope: you may read any file in this directory; read the pinned environment (the interpreter
and the site-packages directory the packet's C5 prints); and execute the commands the packet prints verbatim, with whatever they
themselves load — executing a printed command is the instruction, not a scope choice. Executing a printed command does not authorise
other reads: every placeholder you resolve, every command you hand to the wrapper, every import or data path you select is your
choice and must lie inside this directory or the pinned environment. Any path you CHOOSE to open beyond those is an outside path. Do
not open any other path. Print the working directory and every path you open.

Ownership, not access: you ENUMERATE only the texts in `OWNERSHIP_b<k>.txt` (read each completely); for the packet's section 2
named-source rule you may read the cited line of ANY text the manifest lists, and you print every such lookup as
`LOOKUP <file>:<line>`. Reference-only access creates no candidate. Every candidate id, claim id and input id begins with the owned
file's name followed by `#`.

Order of work (limb A session):
1. Print `shasum -a 256` of the packet, this brief, the three pinned scripts, the manifest and every text you read; compare each
   source digest to the manifest row. Print `ACCESS_SHA=<sha256 of the packet>` and the owned-file list.
2. Execute the C5 harness commands exactly as printed in the packet; print stdout and exit codes.
3. Enumerate every candidate passage of your OWNED texts under the packet's section 1 rule; record inclusion or exclusion for each in
   `candidates_b<k>.json` and `exclusions_b<k>.json` (JSON, with the declared counts the packet names); run
   `/usr/bin/python3 -E r3c2_ledger_tools.py census candidates_b<k>.json exclusions_b<k>.json` and print its output.
4. Build `ledger_b<k>.json` (one record per input) under the packet's C3 schema, with `origin_evidence` for every record and no field
   outside the schema; use globally qualified `derived_from` ids (a parent in another batch is named by its own id). Do NOT run `validate`
   in this session: C2/C3 are NOT_RUN per session, because a cross-batch `derived_from` resolves only in the joined ledger. After the
   custodian has sealed and joined all your limb-A batches, you run, in your integration working directory holding all pinned texts,
   `/usr/bin/python3 -E r3c2_ledger_tools.py validate <joined_ledger.json> . <joined_candidates.json>` and print its output.
5. Print the path list with the scope mark for each row, every `LOOKUP` line, and every control's token in the exact form the packet gives.
6. Write `SEAT_REPORT_b<k>.md`: `ACCESS_SHA`, the owned files, digests, control tokens, declared counts, and the artefact list with
   digests. Final line: `R3C2_SEAT_B<k>_LIMB_A_COMPLETE`. Do not start the arithmetic in this session.

Order of work (limb B session, dispatched only after the custodian's limb-A agreement and receipt): this session's directory is
SEPARATE from the sealed limb-A session directory; the custodian has copied the agreed limb-A artefacts into it under the canonical
names `candidates_b<k>.json`, `exclusions_b<k>.json`, `ledger_b<k>.json`, `SEAT_REPORT_b<k>.md`. Update only these copies: for each
included claim, attempt the arithmetic exactly as the packet's section 2 prescribes, launching every symbolic operation through the
wrapper as the packet states; record one per-claim outcome from section 3 with both numbers where the packet asks for them, into
`candidates_b<k>.json`; keep `exclusions_b<k>.json` and `ledger_b<k>.json` as agreed; then run
`/usr/bin/python3 -E r3c2_ledger_tools.py census candidates_b<k>.json exclusions_b<k>.json final` and print its output; write
`SEAT_REPORT_b<k>.md` as in step 6, final line `R3C2_SEAT_B<k>_LIMB_B_COMPLETE`. No `_limbB` filename suffix is used.

Negative outcomes are worded "unreproduced from the stated inputs". Apply the rules as written; where a rule and this brief differ,
the packet governs.
