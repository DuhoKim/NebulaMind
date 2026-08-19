# Digest-currency re-verification — 2026-08-19

DIGEST_CURRENCY_PASS

- identified replacement population: **598**
- identified replacements in working set: **397**
- in-working-set late-pattern checksums: **397**
- stale-checksum hazard: **0**
- late-pattern anomaly: **0**
- non-replaced control clean: **59,911** (zero non-Nov-2022 exceptions)

The retained cross-check therefore shows exact bidirectional equality between the 397 replaced working-set bricks and the 397 July-2023 checksum records. The §11.4c digest-currency verdict is PASS for the manifest-time harvested tree.

## Verdict and independent gate, first lines quoted exactly

From `CROSSCHECK_VERDICT_20260819.md`:

> `CROSSCHECK_PASS`

From `KUN_CC_GATE_20260819.md`:

> `PASS_CROSSCHECK_GATE`

## Frozen verdict/gate hashes

- `CROSSCHECK_VERDICT_20260819.md`: `b312b9d48d83ef2fc8e1e4354e4d12a2e3e305835d43422091a436f277d05b4d`
- `KUN_CC_GATE_20260819.md`: `10875889ae5a309691edd273b369e5c2b6df1f6b197a4b4147916638bc972a87`

## Underlying receipt hashes

- `_tmp_crosscheck_receipts/01_output.txt`: `bdb1ac73c73841cac4f7d2ee41c371bde584a303028d3388e6427bddae6699a1`
- `_tmp_crosscheck_receipts/release10002_bricknames.csv`: `452c0bd4ad7d293977dc4028ad8b6209b4e30c9a48cc6bfc7d5165c01424fc68`
- `_tmp_crosscheck_receipts/intersection_result.json`: `1a1e22b325c94d977c5fa3c2c8d71e8a5f5c5c26dbadeb1ff1f25874d04e38b0`
- `_tmp_crosscheck_receipts/05_output.txt`: `6a338161208ce2b6be9484cab3abb6d9313b61834dcc1773f6ced31954b74c30`
- `_tmp_crosscheck_receipts/06_output.txt`: `f784346913aa4624019181120e3cd33427f0e8b7d0d0b7cddb9cf8e7919c84c6`
- `_tmp_crosscheck_receipts/JOB_RECORD.md`: `db6aa04ef95846fa2c9aa0b7e860c998529c54897f842e32609a2b8ddd977a74`
- `_tori_harvest_20260817/receipts.jsonl`: `d3ffc2c2a05d710f247ca253cb7b645b75acc83991042e6e1897e03be06e14ef`

## Machine-readable cross-check quote

From `_tmp_crosscheck_receipts/intersection_result.json`:

> `"replaced_total": 598`
> `"replaced_in_ws": 397`
> `"late": 397`
> `"hazard": []`
> `"anomaly": []`
> `"control_nonreplaced": 59911`
> `"control_late_violations": 0`
> `"component_verdict": "PASS"`

This artifact packages §11.4c only. It authorizes no transfer and moves no image bytes.
