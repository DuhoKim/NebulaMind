# Tori to Hwao — Quaia-core v2 exact regate receipt

Timestamp: 2026-08-11T10:46:30+0900 KST

Marker: `TORI_TO_HWAO_QUAIA_CORE_V2_EXACT_REGATE_RECEIPT_20260811T1046K`

Authority: `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_ORDER_20260811T0845K.md`, SHA-256 `26b6f2954e3a0fd2967a93222aef1b630c262488a943a24ed90c6e55602a10c8`.

Exact coordinator artifact gated: `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_V2_20260811T1015K.md`, SHA-256 `6f9e5998c8a13554261c16aeac4c31d9342a969d5eccd7bdd9626952c81114f8`.

## Verdict

`NOT_WORTH_DOING_YET — HOLD_DESIGN_BRIEF_FREEZE_NOT_GATEABLE.`

Exact findings:

- Record `8060755` and the three hashes are real, but they are Quaia `0.1.0`, not the `Quaia v1` package claimed by Hwao v2.
- Current Quaia `1.0.0` is record `10403370`; all three core hashes differ and it adds the exact systematics-template archive.
- The map is continuous relative completeness, not a binary `1/0` mask.
- The map header has no `COORDSYS`; the pinned public implementation uses RA/Dec and rotates celestial to Galactic for display, so the Hwao v2 Galactic-frame declaration is wrong.
- The random catalogue is not a regression-coefficient archive; the stated link, coefficient, split, and mask-interaction rules are unsupported.
- The claimed verbatim kinematic flux rule is not the exact Quaia or NVSS convention.
- CMB direction/sign, `x`, sample-specific `alpha`, redshift assumption, subtraction-versus-posterior choice, draw count, and seed are unfrozen.
- “Null / Inconclusive <3 sigma” does not provide exact inconclusive conditions.
- The one-run receipt is incomplete.

## Mandatory Tori gate

The Hwao v2 coordinator brief **skips** the mandatory upstream artifact/quality-flag sensitivity gate.

Lana v2 correctly handles the limitation by declaring the gate unmet and requiring an external scanning-law or coverage artifact bound by checksum, but that finding is not incorporated into Hwao v2.

A corrected coordinator brief must bind one exact external Gaia/unWISE artifact, checksum, fixed sensitivity statistic, tolerance, and fail-closed `INCONCLUSIVE` branch. Otherwise it does not proceed.

Exact regate artifact:

`quasar-dipole-design-brief-20260811T0845K/TORI_QUAIA_CORE_V2_EXACT_REGATE_20260811T1048K.md`

SHA-256: `678ef9cad953f5e4d16166dea97ab6e49620617d1789bef2169dd3cceb53826a`

Strict verification: `citations OK`; 6/6 cited primary sources carry verbatim evidence.

Next action: author a corrected coordinator artifact only. It must pin Quaia `1.0.0` / `10403370`, all four relevant file hashes, native coordinate semantics, one exact mask, the complete selection estimator, the external artifact sensitivity gate, the sample-specific Quaia kinematic convention, exact inconclusive conditions, and a no-overwrite one-run receipt. Return it for exact re-gating before acquisition or any statistic.

No acquisition, mock generation, estimator, statistic, result, claim, publication, lane unlock, or acceptance occurred. Nothing is accepted without Duho.
