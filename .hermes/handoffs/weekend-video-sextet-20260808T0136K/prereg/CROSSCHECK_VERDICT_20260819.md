CROSSCHECK_PASS

# Known-issues cross-check — DR10.1 replacements vs harvested checksums (pre-auth condition 2)

**Lana (science seat), 2026-08-19 15:50 KST.** Executed per `KICKOFF_LANA_CROSSCHECK.txt`
against `ACQUISITION_PREAUTH_20260818.md` condition 2 and the cross-check clause of
`ACQUISITION_ROUTE_DECISION_20260816.md`. All scripts and outputs in
`_tmp_crosscheck_receipts/`. Network use: Astro Data Lab TAP only (datalab.noirlab.edu —
aggregate/keyspace queries, the established RELEASE=10002 route of
`CHECKSUM_FRESHNESS_RESOLVED_20260817.md`). **Zero contact with portal.nersc.gov. Zero image
bytes, zero catalogue rows consumed, no endpoint activated, no transfer. K-8 untripped.**

## Verdict basis — the four checks, all clean

**1. Harvest state (condition-1 side-verification).** `receipts.jsonl`: 60,308/60,308 receipts,
parse-clean, every outcome `OK_CONFIRMED`; `HARVEST_COMPLETE.json` = 60,308/60,308
(receipt 01).

**2. Authoritative replaced-brick identification.** Full-table async TAP job
(`ihcjir1h8s4lu7z2`): `SELECT DISTINCT brickname FROM ls_dr10.tractor_s WHERE release = 10002`
→ **598 bricknames** — exactly the DR10 known-issues replacement count. Positive controls: the
two bricks proven replaced on 2026-08-17 (0037m392, 2393m140) are both in the list (also
independently returned by the 26-id calibration query, `inlist_test.csv`). A working-set-
constrained parallel variant was started per Duho's 15:40 KST fallback instruction and
abandoned when the full-table job returned first; both job URLs and outcomes are in
`JOB_RECORD.md` (receipts 02–04, 07).

**3. The replaced∩working-set verification (the hazard check).** Intersection (receipt 06,
`intersection_result.json`):

- replaced ∩ working set = **397 bricks**.
- **Every one of the 397 carries the post-replacement re-hash pattern**: harvested
  `.sha256sum` Last-Modified **26 Jul 2023, 18:07–18:45 UTC** — the exact targeted re-hash
  window proven on 2026-08-17 (images regenerated 18–19 Jul 2023, digests written 26 Jul 2023).
- **Hazard set — replaced working-set bricks with pre-replacement (Nov 2022) checksum
  evidence: EMPTY (0).**
- The correspondence is **bidirectional and exact**: the set of working-set bricks with
  2023-dated checksums (397, receipt 01) equals the replaced∩working-set set (397) with zero
  anomalies in either direction — no replaced brick missed by the re-hash, and no re-hashed
  brick outside the replacement list.

**4. Control.** Not a sample but the full census: all **59,911** non-replaced working-set
bricks carry Nov 2022 (18–26 Nov 2022 bulk-pass) checksum dates; zero exceptions (receipts
01, 06). Additionally, on-disk content verification: all 397 replaced-brick checksum files and
a seeded 400-brick control sample re-hash exactly to the receipts' recorded
`sha256_of_checksum_file` digests (receipt 05).

## Interpretation

The silent-verification hazard named in the route decision — the portal serving
pre-replacement bytes confirmed by their own stale checksum — **does not obtain for any brick
of the working set.** The 2026-08-17 two-brick pattern is now a census: the July 2023 re-hash
covered the replaced set completely within the working set (397/397), and only the replaced
set. The residual caution recorded in `CHECKSUM_FRESHNESS_RESOLVED_20260817.md` ("two bricks
are a pattern, not a census") is closed for the working set by this cross-check.

## Notes, disclosed

- The 49-vs-58 checksum-entry split (526 bricks with 49 entries) appears proportionally in
  both the replaced (22/397) and non-replaced (504/59,911) populations — a directory-content
  variation, uncorrelated with replacement; `image_r_listed` is true for all 60,308 receipts,
  so the required product is covered everywhere (receipts 01, 05).
- The transfer-time protection stands regardless of this pass: every transferred file must
  match its harvested per-brick digest, and a mismatch is terminal (the design's operative
  guarantee; this cross-check removes the *silent* branch, the design removes the loud one).
- One tooling defect disclosed: the first poller saved a 0-byte result by not following the
  UWS 303 redirect; re-fetched with `-L` (5,392 bytes). Recorded in `JOB_RECORD.md`; no
  bearing on the result.

## Consequence

Pre-auth condition 1 (harvest complete, parse-clean) and condition 2 (this cross-check:
**PASS**) both hold. Per `ACQUISITION_PREAUTH_20260818.md`, the acquisition may proceed to the
next recorded step — Tori's transport build and **Kun's transport gate against the frozen
successor binding before the first image byte** — which this verdict does not skip and does
not perform.

— Lana, 2026-08-19 15:50 KST.
