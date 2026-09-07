# Render-coordinate derivation receipt — 2026-09-07

Label-free authoring only. Numeric GZ1_OBJID/RA/DEC prefixes of the already pinned guarded pool supply positions; IDs and brick boundaries alone cannot supply galaxy positions. The source is hashed opaquely and its label suffix is never decoded, parsed, displayed or emitted. No pixels, failed-source CSV, historical V15–V34 file, ranking, seed, draw or access stage is read or run.

Procedure: binary64 dec1 <= DEC < dec2; nonwrapping ra1 <= RA < ra2; wrapping RA >= ra1 OR RA < ra2. Multiple matches stop. Exclude no-r bricks, require exact equality with pinned eligible membership, then emit numeric ID order. No checksum/exposure lookup or historical exclusion subtraction.

## Command

Run from the lane root:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/_optionA_dev/_venv_bls/lib/python3.9/site-packages" /Library/Developer/CommandLineTools/usr/bin/python3 _optionA_dev/agreement_run/inputs/BUILD_RENDER_COORDINATES_20260907.py
```

Existing outputs are recomputed and byte-compared without overwriting. JSON bytes use sorted keys, compact separators, finite numbers, UTF-8 and one terminal LF; no timestamp enters the output.

## Row counts

```json
{
  "after_half_open_brick": 11841,
  "after_no_r": 11837,
  "coordinate_prefix_rows": 12054,
  "eligible_missing_coordinates": 0,
  "eligible_rows": 11837,
  "no_r_rows": 4,
  "no_r_unique": 4,
  "output_rows": 11837,
  "qualified_not_eligible": 0,
  "removed_no_r": 4,
  "survey_bricks": 93548,
  "unique_coordinate_ids": 12054,
  "without_brick": 213
}
```

## Actual data-input pins

| Path | SHA-256 |
|---|---|
| `_optionA_dev/agreement_run/inputs/eligible_ids_20260907.txt` | `15f34e4ef21b47a5393786a404ecc45aa07f347d548c4811fcc92932a258611d` |
| `_optionA_dev/corpus_identity/guarded_pool.csv` | `2cc94a29562270fcb5043f4ce942e303696f359b5fb0c59fdee48578ebb34155` |
| `scratch/survey-bricks-dr9-north.fits.gz` | `2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb` |
| `validation_bricks/_bricks_without_r_coverage.txt` | `ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe` |

## Producer, output and runtime

Producer SHA-256: `52eab8f00ae68eefd99dd5d08d29abf28598078c3b5a9e6089d302273488944b`.
Coordinate JSON SHA-256: `ec5c9dec352c5ce7320b34c443084c503fe826c07e6df37febc5e3bf42740991`; bytes: 1106408.
Interpreter: `/Library/Developer/CommandLineTools/usr/bin/python3`; SHA-256: `bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e`.
Python 3.9.6; NumPy 1.26.4; Astropy 6.0.1.
Package files are covered by the separate runtime inventory, not claimed by the four-data-input table.
Receipt full-byte SHA-256 is printed after creation and retained in the v42 report; no self-digest is invented.
