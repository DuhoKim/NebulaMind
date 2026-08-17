# R3 CLOSED — per-brick checksums WERE refreshed for the DR10.1-replaced bricks

**Resolved 2026-08-17 by direct measurement, without waiting for the survey team.**

## The question

Were the per-brick `.sha256sum` files regenerated for the 598 bricks replaced in place by DR10.1,
or do they still describe pre-replacement bytes? A checksum consistent with *superseded* bytes
verifies cleanly while not being the data the study intends to consume — a silent failure, which
is why it gated manifest approval as R3 of `MANIFEST_GATE_REQUIREMENTS_20260816.md`.

Earlier evidence pointed the wrong way: per-brick digests were written in one sequential pass
18–26 Nov 2022, ten months before the September 2023 release update, and no sampled brick deviated.
The affected bricks are published as a map rather than a list, and directory listings carry no
mtimes, so the tree could not be scanned for outliers.

## How it was closed

The DR10 issues page states that sources updated for DR10.1 carry `RELEASE = 10002`. Data Lab's
`ls_dr10.tractor_s` exposes a `release` column — so a replaced brick can be *identified* rather than
hunted. Aggregate/keyspace query only; no rows, positions, images or catalogue values consumed.

    SELECT TOP 1 brickname, brickid FROM ls_dr10.tractor_s WHERE release = 10002 AND brickid > <lo>

Then one HEAD request per brick at the portal.

## Result — the checksums are CURRENT

    brick        brickid   image-r written      its .sha256sum written
    0037m392     121421    19 Jul 2023 00:46    26 Jul 2023 18:07      +7 days
    2393m140     251409    18 Jul 2023 19:25    26 Jul 2023 18:31      +8 days

    control (unreplaced, same AAA as the first)
    0030m167               —                    18 Nov 2022 20:27      original bulk pass

Two replaced bricks from widely separated keyspace ranges both carry digests written **26 July
2023**, after their images were regenerated on 18–19 July 2023. An untouched neighbour retains its
November 2022 digest.

**That is a targeted re-hash of the replaced set, not a blanket re-run and not an omission.** The
digest tracks the file it covers.

## Ruling

**R3 is CLOSED, favourably.** Published per-brick SHA-256 digests are current with respect to the
DR10.1 in-place replacements. The silent-verification hazard named in
`ACQUISITION_ROUTE_DECISION_20260816.md` §3 does not obtain for DR10.1.

Consequences:

- **Route B's custody story is intact.** Lana's condition — per-file digests covering every required
  product, current against the replacements — is now satisfied on both limbs, coverage and currency.
- The manifest gate is no longer blocked by R3. R1, R2 and R4 remain open.
- The outstanding question to Dustin Lang on DR10 checksum currency is **answered by measurement**
  and no longer needs his reply. The DR11 questions are moot under
  `DR10_1_RETAINED_DECISION_20260817.md`.

## Scope and residual caution

Two bricks are a pattern, not a census. This does not prove every one of the 598 was re-hashed; it
proves the re-hash happened and was targeted, and it removes the specific hazard that motivated R3.

**The operative protection is not this finding but the design already in place:** every transferred
file's local digest must equal the approved manifest digest, and a mismatch is terminal. If some
brick were missed by the July re-hash, that brick fails verification loudly at transfer time rather
than passing silently. R3 asked whether the published digests are *systematically* stale. They are
not.

Re-verify digest currency at manifest time regardless — this is a measurement of the tree as it
stands today, and a future in-place fix would reopen the question.

## Boundary

TAP aggregate/keyspace queries and HEAD requests only. Zero image bytes fetched, zero FITS
downloaded, zero catalogue rows consumed, no endpoint activated, no transfer. K-8 untripped.
