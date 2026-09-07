# Metadata-only input derivation receipt — 2026-09-07

**Eligible count / population of the requested eligible file: 11837.**

Authoring only. No pixels or evaluation labels interpreted; no anchor, round, draw, split, holdout opening or attempt.

Scope: the current task explicitly requests the entire guarded pool restricted ONLY by brick existence and the no-r registry. No failed-set or dry-run subtraction is applied to eligible_ids. A1 describes a post-exclusion subset of 7,410 instead; this file implements the explicit current task, so its count must not be represented as that post-exclusion A1 population. The dry-run exclusion file was not read. No existing document is amended.

## Exact command (produces both ID outputs and both reports)

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/_venv_bls/lib/python3.9/site-packages /Library/Developer/CommandLineTools/usr/bin/python3 /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/agreement_run/inputs/BUILD_INPUTS_20260907.py
```

Interpreter: `/Library/Developer/CommandLineTools/usr/bin/python3`; Python `3.9.6 (default, May 22 2026, 11:13:45)  [Clang 21.0.0 (clang-2100.1.1.101)]`; NumPy `1.26.4`; Astropy `6.0.1`.

## Counts at every stage

| Output | Stage | Rows |
|---|---|---:|
| eligible_ids_20260907.txt | Guarded pool | 12054 |
| eligible_ids_20260907.txt | After half-open brick test | 11841 |
| eligible_ids_20260907.txt | After no-r registry | 11837 |
| eligible_ids_20260907.txt | Final ascending unique IDs | 11837 |
| failed_set_ids_20260907.txt | Source CSV data rows / projected IDs | 2000 |
| failed_set_ids_20260907.txt | After deduplication | 2000 |
| failed_set_ids_20260907.txt | Final ascending unique IDs | 2000 |

Failed-set pool/brick/no-r stages: not applicable; this output is exactly the source ID column.
Pool provenance receipt: original 12100; guard removed 46; guarded 12054 (existing receipt; not rebuilt).
Survey-bricks rows: 93548. No-r registry rows: 4; unique bricks: 4. Brick-test removals: 213; no-r removals: 4.

## Deterministic procedure

Read the existing guarded pool, projecting only GZ1_OBJID, RA, DEC. Apply dec1 <= DEC < dec2 and ra1 <= RA < ra2, with RA-wrap intervals using RA >= ra1 OR RA < ra2. All coordinates and boundaries use binary64. Require at most one matching survey brick; retain only matching bricks absent from the no-r registry. No exposure or checksum-catalogue filter. Project only GZ1_OBJID from the failed CSV. Sort both outputs numerically, deduplicate, and write ASCII decimal IDs with LF endings.

Known CSV headers are checked; only the unquoted numeric prefixes are decoded. Label-bearing suffixes are discarded without parsing or display. Whole-file hashing is opaque. The legacy builder is hashed/read as provenance, never imported or executed. Reruns recompute all outputs and compare existing bytes, refusing differences without overwriting.

## SHA-256 of every task input read

| Input | SHA-256 |
|---|---|
| `AGREEMENT_RUN_AMENDMENT_A1_20260907.md` | `61e253cef941de58b6be805faacc12822d0a31900ae8309f160ad976618ac069` |
| `AGREEMENT_RUN_INPUT_CONTRACT_20260907.md` | `b2d9ecf56b78febc86cc52ecf73240f3e9c83ba11729dcd76b2dc46219b42cc9` |
| `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md` | `fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1` |
| `_optionA_dev/corpus_identity/build_guarded_pool.py` | `e9b00ef4f50ce93c980cf6c5e0581276c46e6fa9a56ed46daa6d4eb95d2f52f3` |
| `_optionA_dev/corpus_identity/guarded_pool_receipt.json` | `2ee4399ce791540bd1cb26a73f0bbf5a77362df9be670886811e38c171d8936d` |
| `_optionA_dev/corpus_identity/guarded_pool.csv` | `2cc94a29562270fcb5043f4ce942e303696f359b5fb0c59fdee48578ebb34155` |
| `scratch/survey-bricks-dr9-north.fits.gz` | `2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb` |
| `validation_bricks/_bricks_without_r_coverage.txt` | `ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe` |
| `VALIDATION_SELECTION_V29_20260905.csv` | `5643555c75670a695cd9144455a956440125c1019ebd1fb028a7ee21889014c7` |
| `/Library/Developer/CommandLineTools/usr/bin/python3` | `bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e` |

The table covers all task data and instruction/provenance inputs; package imports are the named environment, not a claimed complete runtime dependency closure.

## SHA-256 of producer and generated ID outputs

| Output | SHA-256 |
|---|---|
| `_optionA_dev/agreement_run/inputs/BUILD_INPUTS_20260907.py` | `b8cf29f29fe2a929dce26881fe2db7efd887e4de27000accf30ae4f8e6d79ad3` |
| `_optionA_dev/agreement_run/inputs/eligible_ids_20260907.txt` | `15f34e4ef21b47a5393786a404ecc45aa07f347d548c4811fcc92932a258611d` |
| `_optionA_dev/agreement_run/inputs/failed_set_ids_20260907.txt` | `f459d2fd996047ac8470ba2309062f98d9ce21c5adf5d28d609f14126bad3f5d` |

Both ID files use the exact command above. The script is the retained authoring source; it is executed, not self-generated.

A report cannot embed its own final SHA-256 without a self-reference. The receipt digest is in _tmp_v39_inputs_REPORT.md; the evidence-report digest is emitted on stdout. No requested metadata count or ID digest is uncomputed. The post-exclusion A1 population is not computed because that subtraction is outside the current output definition and its dry-run input was not read.
