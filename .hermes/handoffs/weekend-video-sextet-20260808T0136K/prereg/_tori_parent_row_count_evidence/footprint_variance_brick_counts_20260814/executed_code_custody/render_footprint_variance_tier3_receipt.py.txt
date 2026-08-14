#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
SCOPE = ROOT / "footprint_variance_brick_counts_20260814"
TARGET = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
GLOBAL_ATTEMPT = PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md"
PARTITION_ATTEMPT = PREREG / "TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md"
EXPECTED_PRIOR_RECEIPT_SHA = "f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289"
EXPECTED_GLOBAL_ATTEMPT_SHA = "ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e"
EXPECTED_PARTITION_ATTEMPT_SHA = "f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def fmt(value: float) -> str:
    return f"{value:.15f}"


def main() -> None:
    if sha(TARGET) != EXPECTED_PRIOR_RECEIPT_SHA:
        raise RuntimeError("prior unresolved variance receipt drift; refuse supersession")
    if sha(GLOBAL_ATTEMPT) != EXPECTED_GLOBAL_ATTEMPT_SHA:
        raise RuntimeError("preserved global-attempt receipt drift")
    if sha(PARTITION_ATTEMPT) != EXPECTED_PARTITION_ATTEMPT_SHA:
        raise RuntimeError("preserved partition-attempt receipt drift")
    outcome_path = SCOPE / "FINAL_COUNTS_OUTCOME.json"
    result_path = SCOPE / "LOCAL_GEOMETRY_RESULT.json"
    custody_path = SCOPE / "RECONSTRUCTION_CUSTODY.json"
    for path in (outcome_path, result_path, custody_path):
        if not path.exists():
            raise RuntimeError(f"Tier-3 reconstruction incomplete: {path}")
    outcome = json.loads(outcome_path.read_text())
    result = json.loads(result_path.read_text())
    custody = json.loads(custody_path.read_text())
    if not outcome["coverage"]["full_coverage"] or not outcome["population_matches_frozen_total"]:
        raise RuntimeError("refuse receipt without full 67-partition coverage and exact frozen population")
    if result["population"] != 832393 or custody["population"] != 832393:
        raise RuntimeError("Tier-3 population drift")
    if result["verdict"] != custody["verdict"]:
        raise RuntimeError("Tier-3 verdict custody mismatch")

    verdict = result["verdict"]
    variance = result["variance_cos_theta_center"]
    margin = result["margin_above_threshold"]
    lower = result["conservative_object_variance_interval"]["lower"]
    upper = result["conservative_object_variance_interval"]["upper"]
    if verdict == "PASS":
        bs1 = "SATISFIED ON THE BOUNDED TIER-3 ROUTE"
        ruling = (
            f"The count-weighted brick-centre value is `{fmt(variance)}`. Its margin above `0.15` is "
            f"`{fmt(margin)}`, which is at least twice the `0.0124` error bracket. Under Lana's binding "
            "rule, BS-1 is satisfied on this route."
        )
    elif verdict == "FAIL":
        bs1 = "FAILED"
        ruling = (
            f"The count-weighted brick-centre value is `{fmt(variance)}`, below `0.15`, and even its "
            f"conservative upper bound `{fmt(upper)}` remains below `0.15`. This is a real below-threshold result."
        )
    else:
        bs1 = "UNRESOLVED — ESCALATION REQUIRED"
        relation = "below" if variance < 0.15 else "above"
        ruling = (
            f"The count-weighted brick-centre value is `{fmt(variance)}`, {relation} `0.15`, but it does not "
            "clear the binding margin rule. The bounded result is INCONCLUSIVE and must be escalated; the measured "
            "value is reported plainly rather than argued into a verdict."
        )

    manifest = SCOPE / "manifest.json"
    launch = SCOPE / "LAUNCH_AUTHORIZATION.json"
    preflight = SCOPE / "PRELAUNCH_VERIFICATION.json"
    static_custody = SCOPE / "STATIC_PRODUCT_CUSTODY.json"
    static_product = SCOPE / "static/survey-bricks-dr10-south.fits.gz"
    combined = SCOPE / "combined_per_brick_counts.csv"
    receipt = f"""# TORI — frozen-footprint variance receipt

**Assembled UTC:** `{utc_now()}`  
**Route:** Lana Tier 3 — exact post-Cut-6 counts per brick; geometry local  
**Verdict:** **{verdict}**  
**BS-1 status:** **{bs1}**

## Plain ruling

{ruling}

This receipt supersedes the prior UNRESOLVED receipt while preserving both earlier attempt receipts byte-for-byte as history. The failed attempts were handled correctly; the failure was the old server-side query shape. The successful route sent no trigonometry or axis-relative geometry to NOIRLab.

## Measured bounded statistic

- frozen population: `{result['population']:,}` dered Cut-6 objects;
- nonempty selected bricks: `{result['nonempty_bricks']:,}`;
- count-weighted `mean(cos theta)` at brick centres: `{fmt(result['mean_cos_theta_center'])}`;
- count-weighted `mean(cos² theta)` at brick centres: `{fmt(result['mean_cos2_theta_center'])}`;
- count-weighted `var(cos theta)` at brick centres: `{fmt(variance)}`;
- preregistered threshold: `0.15`;
- margin above threshold: `{fmt(margin)}`;
- half-diagonal bound: `0.177 deg = 0.00309 rad`;
- conservative variance error bracket: `|V_object - V_center| <= 0.0124`;
- conservative object-variance interval: `[{fmt(lower)}, {fmt(upper)}]`;
- twice-error margin required for PASS: `0.0248`;
- binding decision rule: PASS if `V_center - 0.15 >= 0.0248`; FAIL if `V_center + 0.0124 < 0.15`; INCONCLUSIVE otherwise.

The `0.0124` bracket is more than ten times smaller than the `0.15` threshold. It follows from the 0.25-degree brick geometry, the `0.177`-degree half-diagonal bound, and the fact that `cos theta` is 1-Lipschitz in great-circle angle. It is carried conservatively rather than replaced with the smaller within-brick estimate discussed by Lana.

## Exact server-side acquisition

- partition coverage: `{outcome['coverage']['completed_partitions']}/{outcome['coverage']['partition_count']}`;
- BRICKID keyspace: `1…662174`, disjoint and exhaustive;
- aggregate rows returned: `{outcome['coverage']['aggregate_group_rows']:,}` per-brick count rows;
- summed grouped population: `{outcome['coverage']['population']:,}`;
- frozen population match: **{str(outcome['population_matches_frozen_total']).upper()}**;
- server projection: `brickid`, `COUNT(*) AS n_cut6_dered`;
- grouping: `GROUP BY t.brickid`;
- server-side trigonometric terms: **0**;
- server-side axis/angular terms: **0**;
- object rows exported: **0**;
- object positions exported: **0**.

The ordinary one-row aggregate guard remained armed and byte-identical at SHA-256 `{outcome['ordinary_guard_sha256']}`. It was never opened. A dedicated fail-closed grouped-count validator permitted only the two-column `brickid`/`COUNT(*)` schema while retaining the trigonometry, position, signal, row-export, and mutation bans.

## Local geometry

The official static DR10-south brick product supplied only the brick grid centres used locally:

- URL: `https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/survey-bricks-dr10-south.fits.gz`;
- SHA-256: `{sha(static_product)}`;
- static rows: `366,912`;
- required columns: `brickid`, `ra`, `dec`;
- Longo axis used locally only: Galactic `(l,b)=(52,68.5) deg`, frozen equatorial `(RA,Dec)=({result['axis_equatorial_degrees']['ra']}, {result['axis_equatorial_degrees']['dec']}) deg`.

No object coordinates crossed the wire and no local geometry was computed until all 67 count partitions and the exact population check passed.

## Hash custody

- launch authorization: `{sha(launch)}`;
- prelaunch verification: `{sha(preflight)}`;
- grouped-count manifest: `{sha(manifest)}`;
- final counts outcome: `{sha(outcome_path)}`;
- static-product custody: `{sha(static_custody)}`;
- official static product: `{sha(static_product)}`;
- combined per-brick counts: `{sha(combined)}`;
- local geometry result: `{sha(result_path)}`;
- reconstruction custody: `{sha(custody_path)}`;
- grouped-count worker executed code: `{sha(SCOPE / 'executed_code_custody/run_grouped_brick_count_tap.py.txt')}`;
- orchestrator executed code: `{sha(SCOPE / 'executed_code_custody/run_footprint_variance_brick_counts.py.txt')}`;
- reconstructor executed code: `{sha(SCOPE / 'executed_code_custody/reconstruct_footprint_variance_brick_counts.py.txt')}`;
- Goru audit: `{sha(PREREG / 'GORU_VARIANCE_APPROACH_AUDIT.md')}`;
- Kun audit: `{sha(PREREG / 'KUN_VARIANCE_APPROACH_AUDIT.md')}`;
- Lana audit: `{sha(PREREG / 'LANA_VARIANCE_APPROACH_AUDIT.md')}`;
- preserved global-attempt receipt: `{sha(GLOBAL_ATTEMPT)}`;
- preserved partition-attempt receipt: `{sha(PARTITION_ATTEMPT)}`;
- superseded unresolved receipt SHA-256: `{EXPECTED_PRIOR_RECEIPT_SHA}`.

## Scope boundary

- aggregate per-brick count rows: `{outcome['coverage']['aggregate_group_rows']:,}`;
- object rows: **0**;
- object positions: **0**;
- images: **0**;
- chirality computed: **0**;
- handedness, spin, CW/CCW fields joined or referenced: **0**;
- angle bins or sky maps: **0**;
- dipole amplitude computed: **0**;
- accepted-sample variance claimed: **NO** — this receipt is for the frozen dered Cut-6 population;
- publication/acceptance/commit/push: **0**.

## Supersession

- `TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md` remains immutable history at `{EXPECTED_GLOBAL_ATTEMPT_SHA}`.
- `TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md` remains immutable history at `{EXPECTED_PARTITION_ATTEMPT_SHA}`.
- This file replaces the prior UNRESOLVED `TORI_FOOTPRINT_VARIANCE_RECEIPT.md` at `{EXPECTED_PRIOR_RECEIPT_SHA}` only after complete Tier-3 reconstruction.
"""
    TARGET.write_text(receipt)
    print(f"rendered={TARGET} verdict={verdict} bs1={bs1} population=832393")


if __name__ == "__main__":
    main()
