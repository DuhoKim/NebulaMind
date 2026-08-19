LANA_CROSSCHECK_COMPLETE

Lana, 2026-08-19 15:52 KST. Deliverable: `CROSSCHECK_VERDICT_20260819.md`, first line
**CROSSCHECK_PASS**. Receipts (scripts + outputs): `_tmp_crosscheck_receipts/` (24 files,
inventoried in the verdict).

- Identification: authoritative RELEASE=10002 list via the established Data Lab TAP route —
  full-table async job returned **598 replaced bricknames** (exactly the known-issues count;
  both 2026-08-17 positive-control bricks present). Duho's 15:40 KST fallback (parallel
  working-set-constrained variant) was executed and abandoned when the full-table job returned
  first; both jobs recorded in `_tmp_crosscheck_receipts/JOB_RECORD.md`.
- Hazard check: replaced ∩ working set = **397 bricks; all 397** carry the proven
  post-replacement re-hash pattern (26 Jul 2023 18:07–18:45 UTC). **Hazard set empty.**
  Bidirectional exact match with the local timestamp census (zero anomalies either direction).
- Control: full census, not a sample — all 59,911 non-replaced working-set bricks at the
  Nov 2022 bulk-pass dates, zero exceptions. On-disk checksum-file contents re-hash to the
  receipts' digests (397 replaced + 400-control sample, all match).
- Boundary: datalab.noirlab.edu only; **portal.nersc.gov untouched**; zero image bytes, zero
  catalogue rows, no endpoint, no transfer; K-8 untripped.

Both pre-auth conditions now hold. Next per `ACQUISITION_PREAUTH_20260818.md`: Tori builds the
transport, Kun gates it against the frozen successor binding before the first image byte.
