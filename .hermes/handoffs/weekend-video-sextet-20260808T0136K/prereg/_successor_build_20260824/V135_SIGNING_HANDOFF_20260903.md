# V135 — SIGNING HAND-OFF TO BLANC (Hwao, 2026-09-03 12:2x KST)

**Status.** V135 (BS-2v DESIGN slot fill of the P0-signed successor prereg V134) is SIGNABLE: agy round 1
SIGNABLE-AFTER-REPAIRS (one wording-only finding), round 2 SIGNABLE with minimality PASS, F1 CLOSED,
0 new findings. P0 manifest still 30/30 OK; V134 bytes unchanged. Ruling "1b 2b" (direction #58) applied.

**File.** `PREREG_SUCCESSOR_DRAFT_V135_20260903.md` (commit 13ce21e2f on feat/paper-workflow-v2).

**Digest to state** (V135's own mechanism hashes the file with BOTH the `SIGNATURE UTC:` and
`DUHO SIGNATURE:` lines blank, so the digest is exactly the committed file's SHA-256 — no line to fill first):

    0a09ba938e42412860a55d70f12c640d1f56c4e2801486a8dc200f3017a84598

Check: `shasum -a 256 PREREG_SUCCESSOR_DRAFT_V135_20260903.md` prints that value.

**One paragraph for Duho.** Nothing in the flagship design changed. V135 fills one bookkeeping slot, BS-2v,
the VOID converter: the program that turns each of the 60 enumerated "this voids the run" conditions in the
text into a machine check. The converter itself was built and verified SOUND on 09-01; what was missing was
the text's own record of it. V135 writes into section 7 the four fingerprints that pin it (the registry of
void conditions, the converter program, its receipt schema, and its receipt), adds the trace row for the
V133-to-V134 step that V134 could not carry, and states how amendments to the signed text are signed from now
on: your one sentence in Blanc's chat with the digest and a UTC, relayed verbatim, recorded by Hwao; a wrong
digest signs nothing, and the repository holds no cryptographic proof of a chat statement. P0's ssh signature
of V134 stands untouched. Next slot after this signature: BS-2a, BS-2k, or BS-3g, one at a time.

**Ceremony:** in the Blanc chat, one sentence: "successor V135 signed: 0a09ba938e42412860a55d70f12c640d1f56c4e2801486a8dc200f3017a84598 at <UTC>". Blanc relays; Hwao
verifies the digest against the committed bytes, fills both signature lines, writes
V135_AMENDMENT_RECORD_20260903.md with the relay text and timestamp, commits.
