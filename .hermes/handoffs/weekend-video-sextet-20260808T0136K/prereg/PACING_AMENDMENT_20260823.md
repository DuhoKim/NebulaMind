# PACING AMENDMENT — 2.0 s → 0.25 s, by Duho's order, 2026-08-23 22:37 KST

**Duho, verbatim: "why? make it fast."** This record is the amendment artifact; the change is one
constant in the gated transport plus a re-issued approval, gated below before restart.

## The change, in full

- `nm_image_transfer.py`: `PACING_SECONDS = 2.0` → `0.25` (single line; new file sha256
  `a4e4c4af669520e63651c281eaede42e66109f06add976b8cb8ea8517a136ad2`).
- `RETRIEVAL_APPROVAL_20260823_PACING.json` (sha256 `ff242cc42cf495e858e6857239165fdb8f2d9a7461c2c2f78cdb19a7e17ce6b3`,
  mode 444): identical to `RETRIEVAL_APPROVAL_20260819.json` except
  `image_request_spacing_seconds` 2.0→0.25 and the provenance fields. Untouched: concurrency 1,
  bandwidth ceiling, byte ceiling, windows, manifest pin, binding pin, the three receipt pins.

## Why this is safe, measured not asserted

Diagnosis from 22,894+ receipts: per-stream throughput is ~2 MB/s (connection-limited), far under
the 25 MB/s ceiling; the 2.0 s pacing is ~30% of each brick's ~6.6 s wall. At 0.25 s the stream
runs ~735 bricks/hour — **one request every ~4.9 s**, versus the checksum harvest's proven and
uncomplained-at 1 request/second. Single stream, same windows, same ceilings: the NERSC profile
remains far gentler than what this campaign already ran for two days.

Transport speed cannot alter content: bytes are digest-verified per brick against the published
per-directory sha256sum and, post-hoc, the producer's own list (20,929/20,929 to date). F-9
governs measurement parameters; pacing is not one, and no chi-side artifact changes.

## Effect

Remaining ~24,850 bricks at ~735/hr ≈ 34 running hours → projected completion **Tuesday evening
KST**, about a day earlier. Restart resumes from receipts; nothing re-downloads.
