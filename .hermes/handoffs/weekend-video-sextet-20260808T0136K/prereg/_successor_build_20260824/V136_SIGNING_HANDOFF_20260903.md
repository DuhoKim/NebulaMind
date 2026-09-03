# V136 — SIGNING HAND-OFF TO BLANC (Hwao, 2026-09-03 14:1x KST)

**Status.** V136 (BS-2a DESIGN slot fill of the signed successor chain V134 → V135) is SIGNABLE: agy round 1
SIGNABLE-AFTER-REPAIRS (blocks column; schema-chain soundness), round 2 through nm_referee_dispatch.sh with
ACCESS PROVEN: SIGNABLE, F1/F2 CLOSED, minimality PASS, 0 new findings. P0 manifest 30/30; V135's signed bytes
unchanged. Ruling "1b 2b" (direction #58) applied.

**File.** `PREREG_SUCCESSOR_DRAFT_V136_20260903.md` (commit 4ae184264 on feat/paper-workflow-v2).
**Digest to state** (both signature lines blank = the committed file's SHA-256):

    6b3ff1301546f6595582c0f5d5afe8e729f187e753fc1b63653af6eaf7b75377

**One paragraph for Duho.** Nothing in the flagship design changed. V136 fills the second bookkeeping slot,
BS-2a, the acceptance design: it writes into the text the fingerprints of the quality-predicate gate that was
already cleared on 08-28 and the three frozen thresholds it enforces (flux_ivar_r > 8.4000532, psfsize_r <
1.5699703, nobs_r ≥ 3), gives the slot its receipt schema, and files a receipt binding those identities only:
no galaxy row was evaluated, that happens later at BS-2f, which is the one thing BS-2a blocks. The referee
also made the record stronger: every slot's receipt schema now carries its own fingerprint, and any later
version of the schema file must prove it left the earlier entries byte-for-byte untouched. Same signing
sentence as V135.

**Ceremony:** in the Blanc chat, one sentence: "V136 signed: 6b3ff1301546f6595582c0f5d5afe8e729f187e753fc1b63653af6eaf7b75377 at <UTC>". Blanc relays verbatim; Hwao
verifies against the committed bytes, fills both lines, writes V136_AMENDMENT_RECORD_20260903.md, commits.
Next slot after this signature: BS-3g (BS-2k is Duho's own custody slot and is presented separately).
