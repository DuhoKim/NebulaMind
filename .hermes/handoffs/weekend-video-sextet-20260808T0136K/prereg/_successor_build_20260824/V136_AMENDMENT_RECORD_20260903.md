# V136 AMENDMENT RECORD — chat signature (V136 preamble mechanism)

document: PREREG_SUCCESSOR_DRAFT_V136_20260903.md (revision of chat-signed V135 (itself a revision of P0-signed V134); P0 manifest d1be4a3b… untouched)
digest (SIGNATURE UTC and DUHO SIGNATURE lines blank): 6b3ff1301546f6595582c0f5d5afe8e729f187e753fc1b63653af6eaf7b75377
UTC stated by Duho: 2026-09-03T05:15:00Z
recomputed by Hwao at record time: 6b3ff1301546f6595582c0f5d5afe8e729f187e753fc1b63653af6eaf7b75377  (MATCH)

## Blanc's verbatim relay (RELAY FROM DUHO), relay timestamp 2026-09-03 14:32:21 KST (relay UTC 2026-09-03T05:32:21Z)
```
RELAY FROM DUHO (via Blanc, chat channel, 2026-09-03 14:32:21 KST; relay UTC 2026-09-03T05:32:21Z) — V136
AMENDMENT SIGNATURE. Duho's statement in the Blanc chat channel, verbatim
(his terminal wrapped the digest once; the characters are contiguous):

    V136 signed: 6b3ff1301546f6595582c0f5d5afe8e729f187e753fc1b63653af6eaf7b75377 at 2026-09-03T05:15:00Z

Blanc's check before relaying: shasum -a 256 of the committed
PREREG_SUCCESSOR_DRAFT_V136_20260903.md (both signature lines blank) =
6b3ff1301546f6595582c0f5d5afe8e729f187e753fc1b63653af6eaf7b75377 — MATCH; the referee's ACCESS_SHA in
AGY_V136_REFEREE_V2_20260903.md is the same value; VERDICT: SIGNABLE, COUNT: 0.

Per V136's amendment paragraph: verify the digest against the committed bytes,
fill both signature lines, write the amendment record (digest, stated UTC, this
relay text, relay timestamp), commit and push. V134's P0 manifest unchanged.
Rulings stand: "1b 2b" — next slot one at a time (BS-2k or BS-3g, your
order), hostile referee through nm_referee_dispatch.sh to SIGNABLE, then Duho's
one sentence via Blanc. No pixel. ACK one line: "HWAO ACK V136 signed, digest
match <yes/no>".
```

## Effect
V136 binds: BS-2a is FILLED (quality gate dfbd63d1…, thresholds flux_ivar_r > 8.4000532 / psfsize_r < 1.5699703 / nobs_r >= 3, receipt_strict 27e88520…, candidate f0d9bcce…); V135's BS-2v fill stands. V134's P0 freeze stands; V136 changes only the BS-2v fill and the amendment mechanism. Ruling "1b 2b" (direction #58) applied. No pixel opened.

recorded by: Hwao, 2026-09-03 14:32:57 KST
