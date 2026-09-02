# MINI-PREREG V10 — SIGNING HAND-OFF TO BLANC (Hwao, 2026-09-03 08:0x KST)

**Status.** V10 is SIGNABLE (agy, AGY_V10_SEALGATE_V3_REFEREE_20260903.md: minimality PASS, 0
findings). V10 supersedes V9 before V9 was ever frozen: Duho's 20:10 KST pane statement of the V9
digest (f254b846…) therefore applies to superseded bytes and is void as a signature; nothing was
frozen by it. Ruling "a" stands (validation only, nothing feeds the flagship).

**What changed V9 → V10, one paragraph for Duho.** Nothing about the study changed. The first real
run of the integrity gate on the completed download refused, because the text's description of the
download journal was wrong: it said every receipt has seven fields, but the pinned download script
writes a failure receipt with five. V10 corrects that one section (7.9) to describe exactly the four
receipt kinds the script writes, and says plainly that an unverified receipt does not count as
complete. The gate was updated to match and, on the real journal, now reaches the completion
condition: 17,947 of 17,947 bricks, one transient failure retried and OK.

**File.** `MINI_PREREG_GZ_TIERC_DRAFT_V10_20260902.md` (commit 827fe649c on feat/paper-workflow-v2).
**Preview digest** (both signature-block lines blank): `b212d5b4175009e2589710426ebf8cd7749e8e90213dec4fe7f132b9de31ac24`.
Per §17.1 Duho fills the UTC line first, so the digest he states will differ; recompute after filling:

    python3 miniprereg_sign_digest.py MINI_PREREG_GZ_TIERC_DRAFT_V10_20260902.md

**Ceremony (unchanged, §17 chat signature):** fill `SIGNATURE UTC:`, recompute, state in the Blanc
chat one sentence: "mini-prereg signed: <digest> at <UTC>". Blanc relays verbatim; Hwao records the
freeze record (digest, UTC, relay text, relay timestamp) and commits. Measurement still waits on every
pre-pixel gate (seal gate running now; completeness receipt ~23:30 KST).
