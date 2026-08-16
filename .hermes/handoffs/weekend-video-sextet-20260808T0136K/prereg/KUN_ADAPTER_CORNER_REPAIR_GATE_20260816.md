PASS_ADAPTER_CORNER_REPAIR

# KUN ADAPTER CORNER-BOUNDARY REPAIR GATE -- 2026-08-16

## Verdict

**PASS_ADAPTER_CORNER_REPAIR.**

The pinned hashes match the repair brief, the original Yui fixture oracle is
byte-identical to the pre-repair version, and both independent cross-runs now
pass all 29 fixture cases, including all eight exact/beyond-corner stress cases.

This pass remains build-only. It authorizes no network, no Globus endpoint, no
real survey data, no source manifest, no sky statistic, no publication, no
commit/push, and no accepted status.

## Hashes Measured First

- gate brief `prereg/_tmp_kun_gate_brief_corner_repair_20260816.md`
  - SHA-256 `539bd3b0b2df4e935f6c39af4772e959c6f05774a667093d32477a0566b7f7cb`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `f3c71021f9e01051363dad5a0bd5128b5f398234b5f37c552d267fade7fb658a`
- original fixtures `prereg/boundary_fixtures/make_boundary_fixtures.py`
  - SHA-256 `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- Kun scratch cross-runner `prereg/_tmp_kun_cross_adapter_fixtures_20260816.py`
  - SHA-256 `69115bc3133b50c195db77e6ae6ea070f4ee1b989675b8da1bf4fb850157ae7a`
- route binding `prereg/TORI_ROUTE_BINDING_20260815.md`
  - SHA-256 `c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`
- frozen V3 contract `prereg/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
  - SHA-256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`

Additional repaired artifacts:

- adapter test `prereg/adapter/test_nm_brick_cutout_adapter.py`
  - SHA-256 `9b8b6fd0706bb81651b0c928554a1e3f4c663717d1f0689dabbe696b3fb9e39c`
- adapter formal cross-runner `prereg/adapter/cross_check_yui_boundary.py`
  - SHA-256 `8a1a77b61a71adb36699e56ba05167736425760935c4534a1b80fb946432e4ab`
- adapter formal cross receipt `prereg/adapter/CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json`
  - SHA-256 `c4c167138d89cbfac088cbcd6d26444db77c99cc2c0cdf4a0ff0cf338ec07967`

## Commands Run

Adapter suite:

- `python3 -m unittest prereg.adapter.test_nm_brick_cutout_adapter`
- result: `30/30` passed

Original and round-2 fixture suites:

- working directory: `prereg/boundary_fixtures`
- command: `python3 -m unittest test_boundary_fixtures test_boundary_fixtures_round2`
- result: `12/12` passed

Kun scratch cross-run:

- command: `python3 prereg/_tmp_kun_cross_adapter_fixtures_20260816.py`
- result: `29/29` passed, `0` failed

Adapter formal cross-run:

- command: `python3 prereg/adapter/cross_check_yui_boundary.py`
- result: `{"cases_failed": 0, "cases_passed": 29, "cases_total": 29, "status": "PASS"}`

## Repair Reading

The old failure was caused by `plan_object` requiring exactly one rectangular
unique-area primary before the polygon-intersection working set could proceed.
That failed exact/beyond-corner cases before rendering.

The repaired adapter now makes polygon intersection the only source-selection
rule. The rectangular/catologue-style primary is no longer a gate. It is
recorded only as metadata in `unique_area_primary_bricknames`. The grouping
primary is chosen from the already-planned source rows by nearest angular
separation, with lexicographic tie break.

That is the right repair. It relaxes an over-strict guard rather than deleting a
real safety property, because complete source selection still depends on
polygon intersection, not on the grouping primary. The grouping primary can
affect ordering and reason labels; it no longer decides whether pixels are
available.

## Degenerate Plan Check

The repaired path does not quietly accept no-source or partial-source plans.

Evidence:

- `plan_object` raises `FAILED_PLAN_NO_SOURCES` when no source image intersects
  the output footprint.
- adapter tests include `test_empty_intersection_is_terminal_plan_failure`.
- source-set equality is checked in both my scratch cross-run and Tori's formal
  cross receipt.
- PC-3 receipts require planned/opened/contributing sets and coverage.
- all 29 Yui cases now report `coverage_min >= 1` and `coverage_zero_count = 0`.
- corner exact cases report four contributing sources with `coverage_min = 2`;
  corner beyond cases report four contributing sources with `coverage_min = 1`.

I do not see a new quiet-degenerate path in this repair.

## PC-3 And PC-4

PC-3 remains atomic. The staged output bytes are parsed before acceptance, and
the receipt still checks exact WCS constants, determinant sign, CRVAL centre
mapping, perturbation directions, round-trip residuals, source-set accounting,
coverage minimum, and zero coverage.

PC-4 remains atomic twice:

- source headers are raw-card audited before a source WCS object is constructed;
- synthesized output headers are audited again in `pc3_output_receipt`;
- the output tamper path remains covered by the adapter suite.

The repair does not bypass either gate.

## Pixel-Equality Scope Gap

The cross-runs compare planning/source-set equality and PC-3 coverage, not
byte-equal image values. That is acceptable for this repair gate because the
held defect was planning-time corner rejection and potential truncated coverage.

The gap is real and must stay named: Yui's oracle uses Astropy WCS with bilinear
sampling, while Tori's adapter declares a nearest-neighbour renderer stand-in.
Pixel equality therefore belongs to the later environment/resampler gate, after
the pinned Imagine/astrometry.net resampler replaces the stand-in. It does not
block this corner-boundary repair gate.

## Remaining Boundaries

Still not authorized:

- source manifest against the real parent set;
- Globus endpoint activation or transfer;
- real DR10 image reads;
- production cutouts;
- sky statistics;
- publication or acceptance.

The next valid step is still build-only/environment-lock work or a later
manifest-only gate after the remaining route prerequisites are satisfied.
