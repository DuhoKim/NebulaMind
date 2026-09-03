# V135 AMENDMENT RECORD — chat signature (V135 preamble mechanism)

document: PREREG_SUCCESSOR_DRAFT_V135_20260903.md (revision of P0-signed V134; P0 manifest d1be4a3b… untouched)
digest (SIGNATURE UTC and DUHO SIGNATURE lines blank): 0a09ba938e42412860a55d70f12c640d1f56c4e2801486a8dc200f3017a84598
UTC stated by Duho: 2026-09-03T04:30:00Z
recomputed by Hwao at record time: 0a09ba938e42412860a55d70f12c640d1f56c4e2801486a8dc200f3017a84598  (MATCH)

## Blanc's verbatim relay (RELAY FROM DUHO), relay timestamp 2026-09-03 13:27:39 KST (relay UTC 2026-09-03T04:27:39Z)
```
RELAY FROM DUHO (via Blanc, chat channel, 2026-09-03 13:27:39 KST; relay UTC 2026-09-03T04:27:39Z) — V135
AMENDMENT SIGNATURE. Duho's statement in the Blanc chat channel, verbatim
(his terminal wrapped the digest once; the characters are contiguous):

    V135 signed: 0a09ba938e42412860a55d70f12c640d1f56c4e2801486a8dc200f3017a84598 at 2026-09-03T04:30:00Z

Blanc's check before relaying: shasum -a 256 of the committed
PREREG_SUCCESSOR_DRAFT_V135_20260903.md (both signature lines blank) =
0a09ba938e42412860a55d70f12c640d1f56c4e2801486a8dc200f3017a84598 — MATCH.

Per V135's amendment paragraph and your V135_SIGNING_HANDOFF: verify the
digest against the committed bytes, fill both signature lines, write the
amendment record (digest, stated UTC, this relay text, relay timestamp),
commit and push. V134's P0 ssh-signed manifest is unchanged. Rulings stand:
"1b 2b" — next slot one at a time (BS-2a/BS-2k/BS-3g in your order), each via
hostile referee to SIGNABLE, then Duho's one sentence via Blanc. No pixel.
ACK one line: "HWAO ACK V135 signed, digest match <yes/no>".
```

## Effect
V135 binds: BS-2v is FILLED (registry 315ef019…, converter 001cd944…, receipt_strict f50d8c1d…, receipt a1ad1790…). V134's P0 freeze stands; V135 changes only the BS-2v fill and the amendment mechanism. Ruling "1b 2b" (direction #58) applied. No pixel opened.

recorded by: Hwao, 2026-09-03 13:28:01 KST
