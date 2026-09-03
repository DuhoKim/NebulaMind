# MINI-PREREG FREEZE RECORD — 2026-09-02 (chat signature, §17.1/17.3/17.7)

signed document: MINI_PREREG_GZ_TIERC_DRAFT_V11_20260902.md
digest (blank `DUHO SIGNATURE:` line, SIGNATURE UTC filled): 622d08a0c475b21edf3d8d53c569fd2ff7e840a9cfbabf3f384e1d16948042f3
UTC stated by Duho: 2026-09-03T07:05:00Z
recomputed by Hwao at record time: 622d08a0c475b21edf3d8d53c569fd2ff7e840a9cfbabf3f384e1d16948042f3  (MATCH)
SIGNATURE UTC line filled by: Hwao from the stated UTC (line was blank)

## Blanc's verbatim relay (RELAY FROM DUHO), relay timestamp 2026-09-03 15:57:27 KST (relay UTC 2026-09-03T06:57:27Z)
```
RELAY FROM DUHO (via Blanc, chat channel, 2026-09-03 15:57:27 KST; relay UTC 2026-09-03T06:57:27Z) — V11
PRINCIPAL SIGNATURE, §17.1. Duho's statement in the Blanc chat channel,
verbatim (his terminal wrapped the line at two points; the characters are
contiguous):

    mini-prereg V11 signed: 622d08a0c475b21edf3d8d53c569fd2ff7e840a9cfbabf3f384e1d16948042f3 at 2026-09-03T07:05:00Z

Blanc's check before relaying: the staged copy of
MINI_PREREG_GZ_TIERC_DRAFT_V11_20260902.md with "SIGNATURE UTC: 2026-09-03T07:05:00Z"
filled and the DUHO SIGNATURE: line blank hashes to exactly
622d08a0c475b21edf3d8d53c569fd2ff7e840a9cfbabf3f384e1d16948042f3 (helper and
shasum agree; only the UTC line differs from the canonical file, whose
blank-UTC hash a4b5f557eff5de1db72dc574a8be1787c1873f23163f2dae6186067b6576ac99 equals the referee's ACCESS_SHA).

Per §17.1/17.3/17.7: fill SIGNATURE UTC with exactly 2026-09-03T07:05:00Z in
the canonical V11 file, recompute, confirm equality, record digest + stated
UTC + this relay text + relay timestamp in the freeze record, commit and push.
The V11 freeze (§17.5) is in force from your record; V10's is superseded.
Then per Duho's "b" ruling (15:20): stop the inverse-variance download,
quarantine its partial files (archive, never delete), fetch nexp-r + maskbits
for all 17,947 bricks (4 workers, receipts), re-run the seal gate over three
planes. No real pixel until every gate passes. Validation only; nothing
feeds the flagship. ACK one line: "HWAO ACK V11 signed, digest match
<yes/no>, companions switched".
```

## Effect
§17.5: every constant, threshold, source, order, exclusion, formula, verdict and custody rule
in V9 is frozen. Ruling "a" stands: validation study only; nothing feeds the flagship, the parent
run, or â. §17.7 custody limit acknowledged: this record is the repository's witness of the chat
statement. Measurement remains blocked until §7.11 acquisition completion and every pre-pixel gate.

recorded by: Hwao, 2026-09-03 15:58:04 KST

## Supersession + pins (Hwao)
V10's freeze (MINI_PREREG_FREEZE_RECORD_20260902.md, digest 1647d1de…) is SUPERSEDED by this V11 freeze. Pins in force:
```
209be0e5a4e6d09f9e1aba557ab406cec2bda787bf19bc4c3e078b84cd7e288a  MINI_PREREG_GZ_TIERC_DRAFT_V11_20260902.md
c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b  miniprereg_pins/bs4_sign_anchor_spec.md
587870e9f35d2c096f68cd10a769ab9c7eee6580d8b9cdee580b521cae63b070  miniprereg_pins/concordance_verdict.py
0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9  miniprereg_pins/env_record_schema.json
35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99  miniprereg_pins/fetch_bricks_pinned.py
8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7  miniprereg_pins/render_config.json
2373e122c458d3b0a2cda85560f87741a07bd99ea013922667d8c08e23f24f1d  miniprereg_pins/test_concordance_verdict.py
02e410b0ca512398ad21bdcf279a7ff77068a16d820c9eeffca4ba1ea339530c  ../_successor_build_20260824/acquire/tier_c_manifest_v3.json
```
Run-side tooling refereed for this freeze: seal gate V4 (3 planes, --known-extras-journal), renderer (nexp coverage), anchor gate V3, companion fetcher — pinned by their referee sheets/records; seal gate V4 pin sheet to be written after its next PINNABLE referee.
