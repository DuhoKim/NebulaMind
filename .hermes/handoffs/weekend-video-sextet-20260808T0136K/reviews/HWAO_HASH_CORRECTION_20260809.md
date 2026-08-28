# Hwao correction — one stale hash issued to the review seats

Raised by **Kun**, 2026-08-09 ~12:53. He refused to pass a lane against a hash that did not match
disk, and he was right.

## The error

I dispatched Goru, Kun and Tori against four hashes taken from my own overnight watcher. One was
**stale**:

| lane | hash I issued | true hash (disk == lane freeze) | status |
|---|---|---|---|
| **mzr-census** | `d940a7e8…` | **`0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536`** | **WRONG** |
| fesc | `b9003831…` | `b900383142c0ddea…` | correct |
| brightend | `9a137c61…` | `9a137c61011a3d96…` | correct |
| mzr-anchor | `973daba3…` | `973daba3a6b8ef66…` | correct |

## Cause

My watcher hashed `mzr-census` while the builder was **still writing it**. The stability check
waited 20 s and compared byte size; that was not long enough for this lane. Evidence: the file I
hashed was 9,192,680 bytes; the finished file is 9,421,699 bytes, mtime **02:26:40**, and the lane's
own `POST_ENCODE_FREEZE.json` was written at **02:27:20** recording `0496435a…`.

So the artifact was never wrong — my read of it was, and I published that read as authoritative.

## Consequences

- **Kun — correct.** He measured disk, found the mismatch, and declined to pass the lane against the
  requested hash, marking his section diagnostic-only. That is exactly the behaviour the review
  layer exists for.
- **Goru — needs a correction.** His `mzr-census` section cites `d940a7e8…`. The measurements are
  probably still valid (same artifact, right directory), but the section is labelled with a hash
  that does not exist on disk and must be re-stamped.
- **Tori — unaffected.** She had not yet started; she gets the corrected hash from the outset.

## Fix

Re-issue all four with disk-verified hashes, each cross-checked against that lane's own
`POST_ENCODE_FREEZE.json`. All four now agree disk == freeze.

## Standing lesson

**Do not treat a watcher's hash as authoritative — cross-check the lane's own freeze record.** A
size-stability check can pass mid-write. Every lane writes `POST_ENCODE_FREEZE.json` with
`video_sha256`; that file is the artifact's own claim about itself and is the thing to compare
against disk. This is the fourth time this session a narrow mechanical check produced a confident
wrong answer, and the first time a seat caught it before it propagated into a verdict.
