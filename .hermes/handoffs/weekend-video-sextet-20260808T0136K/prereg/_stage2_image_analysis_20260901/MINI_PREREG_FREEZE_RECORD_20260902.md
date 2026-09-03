# MINI-PREREG FREEZE RECORD — 2026-09-02 (chat signature, §17.1/17.3/17.7)

signed document: MINI_PREREG_GZ_TIERC_DRAFT_V10_20260902.md
digest (blank `DUHO SIGNATURE:` line, SIGNATURE UTC filled): 1647d1de0f66adb40b597bb6de58ae914cd6b9011cb406baad9b9de4b964b073
UTC stated by Duho: 2026-09-02T23:05:00Z
recomputed by Hwao at record time: 1647d1de0f66adb40b597bb6de58ae914cd6b9011cb406baad9b9de4b964b073  (MATCH)
SIGNATURE UTC line filled by: Hwao from the stated UTC (line was blank)

## Blanc's verbatim relay (RELAY FROM DUHO), relay timestamp 2026-09-03 10:45:51 KST (relay UTC 2026-09-03T01:45:51Z)
```
RELAY FROM DUHO (via Blanc, chat channel, 2026-09-03 10:45:51 KST; relay UTC 2026-09-03T01:45:51Z) — V10
PRINCIPAL SIGNATURE, §17.1. Duho's statement in the Blanc chat channel,
verbatim (his terminal wrapped the line at two points; the characters are
contiguous):

    mini-prereg signed: 1647d1de0f66adb40b597bb6de58ae914cd6b9011cb406baad9b9de4b964b073 at 2026-09-02T23:05:00Z

Blanc's check before relaying: the staged copy of
MINI_PREREG_GZ_TIERC_DRAFT_V10_20260902.md with "SIGNATURE UTC: 2026-09-02T23:05:00Z"
filled and the DUHO SIGNATURE: line blank hashes to exactly
1647d1de0f66adb40b597bb6de58ae914cd6b9011cb406baad9b9de4b964b073 (helper and
shasum agree; only the UTC line differs from the canonical V10 file).

Per §17.1/17.3/17.7: fill SIGNATURE UTC with exactly 2026-09-02T23:05:00Z in
the canonical V10 file, recompute the blank-signature-line digest, confirm it
equals the stated digest, and record digest + stated UTC + this relay text +
relay timestamp in the freeze record; commit and push. The freeze (§17.5) is in
force from your record. Rulings unchanged: validation only (his "a"), nothing
feeds the flagship; no pixel until every pre-pixel gate passes. Audio hold
still in force. ACK one line: "HWAO ACK V10 signed, digest match <yes/no>".
```

## Effect
§17.5: every constant, threshold, source, order, exclusion, formula, verdict and custody rule
in V9 is frozen. Ruling "a" stands: validation study only; nothing feeds the flagship, the parent
run, or â. §17.7 custody limit acknowledged: this record is the repository's witness of the chat
statement. Measurement remains blocked until §7.11 acquisition completion and every pre-pixel gate.

recorded by: Hwao, 2026-09-03 10:46:20 KST

## Pins in force at freeze (recorded by Hwao)
```
a2b4fd3f646d4f3524e71607557a561b49d70ab1e8a6b8427b55b4a78418b5e8  MINI_PREREG_GZ_TIERC_DRAFT_V10_20260902.md
c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b  miniprereg_pins/bs4_sign_anchor_spec.md
587870e9f35d2c096f68cd10a769ab9c7eee6580d8b9cdee580b521cae63b070  miniprereg_pins/concordance_verdict.py
0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9  miniprereg_pins/env_record_schema.json
35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99  miniprereg_pins/fetch_bricks_pinned.py
8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7  miniprereg_pins/render_config.json
2373e122c458d3b0a2cda85560f87741a07bd99ea013922667d8c08e23f24f1d  miniprereg_pins/test_concordance_verdict.py
```

Run-side tooling refereed for this freeze (not part of the signed text): seal gate V3 (SEAL_GATE_PIN_20260903.md), completeness gate (COMPLETENESS_GATE_PIN_20260903.md).

Superseded: V9 digest statement of 2026-09-02 20:10 KST (void; V9 replaced before any freeze).
