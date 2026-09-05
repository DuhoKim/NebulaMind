# Seat brief — reproduction census

You are one of two independent seats. Work only from the files in this directory: `R3C2_SEAT_PACKET.md` (the rules),
this brief, `r3c2_ledger_tools.py` (the pinned tool), `r3c2_timeout.py` (the pinned wrapper), and the source texts listed
in `R3C2_CORPUS_MANIFEST.md`. Do not open any other path. Print the working directory and every path you open.

Order of work:
1. Print `shasum -a 256` of the packet, this brief, both tools and every source text you read; compare each source
   digest to the manifest row.
2. Execute the C5 harness commands exactly as printed in the packet; print stdout and exit codes.
3. Limb A: enumerate every candidate passage under the packet's section 1 rule; record inclusion or exclusion for
   each in the candidate and exclusion ledgers (JSON, with the declared counts the packet names); run the `census`
   subcommand and print its output.
4. Build the input ledger (JSON, one record per input) under the packet's C3 schema, with `origin_evidence` for
   every record and no field outside the schema; run `validate` and print its output.
5. Limb B: for each included claim, attempt the arithmetic exactly as the packet's section 2 prescribes, launching
   every symbolic operation through the wrapper as the packet states; record one per-claim outcome from section 3
   with both numbers where the packet asks for them.
6. Print the path list with the scope mark for each row, and every control's token in the exact form the packet
   gives.
7. Write your report as `SEAT_REPORT.md` in this directory: digests, control tokens, the tally with its
   denominator, and the artefact list with digests. Final line: `R3C2_SEAT_COMPLETE`.

Negative outcomes are worded "unreproduced from the stated inputs". Apply the rules as written; where a rule and this
brief differ, the packet governs.
