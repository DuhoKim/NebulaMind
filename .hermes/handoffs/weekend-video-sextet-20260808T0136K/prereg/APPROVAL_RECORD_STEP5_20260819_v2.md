# §11 step-5 execution approval record v2 — route-B image transfer (APPROVED AND FROZEN)

Supersedes v1 (`APPROVAL_RECORD_STEP5_20260819.md`, SHA-256
`a9e63f9fb72a2df3e2d852e383628c2cb45c78f4714a31a50e2fa686b4831c1b`, retained frozen, unedited)
per seal-gate repairs 1–3 of `KUN_SEAL_GATE_20260819.md`. Substance is UNCHANGED from v1 (same
manifest, count, destination, ceiling, pacing, dispositions, approval basis); v2 adds only the
two mandated §5.4 restatements, the machine-readable companion, and the reconciled gate token.

## Everything in v1 §1–§6 is incorporated by reference, plus:

- **Bandwidth ceiling, restated as a value (binding §5.4.3):** 25 MB/s = 25,000,000 bytes/second
  sustained.
- **Transient-error backoff ladder, restated as values (binding §5.4.5):** 30 s, then 60 s, then
  120 s, then terminal for that file.
- **Gate-token reconciliation (seal repair 2):** the transport gate's issued verdict is
  `PASS_TRANSPORT_BUILD`; `nm_image_transfer.py` line 1045 corrected to expect exactly that
  (one line; `TOKEN_RECONCILIATION_NOTE_20260819.md`; 18/18 tests re-pass; diff subject to the
  fresh re-seal).
- **Machine-readable companion (seal repair 1):** `RETRIEVAL_APPROVAL_20260819.json`, SHA-256
  `fe042a41aca5da0510a807c7431528b3034f1f3e095ca33e63f20c6fc6ebff9e`, frozen mode 444 — the exact 14 fields + 3 pins `load_approval` enforces; the
  runner is launched against that file and this SHA.

## Approval

Duho's standing conditional approval (v1 §6 verbatim: "destination is fine, approve when the
package lands") covers this v2: the substance he approved is unchanged, and the additions are
the seal gate's mandated formalizations of already-frozen binding values. Completed and frozen
2026-08-19 17:2x KST; any veto before the re-seal completes voids both records.
