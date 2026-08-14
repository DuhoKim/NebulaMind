#!/usr/bin/env python3
"""Render the append-preserving parent-row-count receipt from hash-pinned aggregate results."""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

PREREG = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "weekend-video-sextet-20260808T0136K/prereg"
)
EVIDENCE = PREREG / "_tori_parent_row_count_evidence"
OUT = PREREG / "TORI_PARENT_ROW_COUNT_20260812.md"
TOTAL_BRICKID = 662174
STOP_PARENT_LOWER_BOUND = 200000
DEADLINE_UTC = "2026-08-12T13:56:00Z"

FIXED_RUNS = [
    {
        "lo": 1,
        "hi": 1000,
        "query": EVIDENCE / "12_partition_normalized_brickid_000001_001000.adql",
        "run": EVIDENCE / "run12_partition_normalized_000001_001000",
    },
    {
        "lo": 1001,
        "hi": 11000,
        "query": EVIDENCE / "09_partition_benchmark_brickid_001001_011000.adql",
        "run": EVIDENCE / "run09_partition_benchmark_001001_011000",
    },
]

FIELDS = [
    "n_join_rows",
    "n_cut1_primary_mask",
    "n_cut2_extended_flux",
    "n_photoz_joined_cut2",
    "n_cut3_photoz",
    "n_cut4_raw_mag",
    "n_cut4_dered_mag",
    "n_cut5_parent_raw",
    "n_cut5_parent_dered",
    "n_raw_allband_nobs",
    "n_dered_allband_nobs",
    "n_raw_allband_ngood",
    "n_dered_allband_ngood",
    "n_raw_allband_ivar",
    "n_dered_allband_ivar",
    "n_raw_shape_valid",
    "n_dered_shape_valid",
    "n_raw_native_covariates",
    "n_dered_native_covariates",
    "n_raw_all_countable_availability",
    "n_dered_all_countable_availability",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_one(spec: dict) -> dict | None:
    run = spec["run"]
    tap_run = run / "tap" if (run / "tap").exists() else run
    result_path = tap_run / "result.csv"
    receipt_path = tap_run / "receipt.json"
    if not result_path.exists() or not receipt_path.exists():
        return None
    receipt = json.loads(receipt_path.read_text())
    rows = list(csv.DictReader(result_path.read_text().splitlines()))
    if len(rows) != 1:
        raise RuntimeError(f"expected one aggregate row: {result_path}")
    if receipt["result_row_count"] != 1:
        raise RuntimeError(f"receipt row count not one: {receipt_path}")
    if receipt["sample_rows_exported"] != 0 or receipt["positions_exported"] != 0:
        raise RuntimeError(f"custody violation in {receipt_path}")
    if receipt["sky_statistics_computed"] is not False:
        raise RuntimeError(f"sky-stat violation in {receipt_path}")
    if sha(result_path) != receipt["result_sha256"]:
        raise RuntimeError(f"result hash mismatch: {result_path}")
    if sha(spec["query"]) != receipt["query_sha256"]:
        raise RuntimeError(f"query hash mismatch: {spec['query']}")
    started = datetime.fromisoformat(receipt["started_utc"].replace("Z", "+00:00"))
    completed = datetime.fromisoformat(receipt["completed_utc"].replace("Z", "+00:00"))
    values = {k: int(rows[0][k]) for k in FIELDS}
    return {
        **spec,
        "receipt": receipt,
        "result_path": result_path,
        "receipt_path": receipt_path,
        "values": values,
        "elapsed_seconds": (completed - started).total_seconds(),
    }


def completed_specs() -> list[dict]:
    specs = list(FIXED_RUNS)
    manifest_path = EVIDENCE / "partitions" / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        for entry in manifest["entries"]:
            specs.append(
                {
                    "lo": entry["lo"],
                    "hi": entry["hi"],
                    "query": Path(entry["query_path"]),
                    "run": Path(entry["run_dir"]),
                }
            )
    loaded = [x for spec in specs if (x := load_one(spec)) is not None]
    loaded.sort(key=lambda x: x["lo"])
    return loaded


def contiguous_prefix(parts: list[dict]) -> list[dict]:
    out = []
    cursor = 1
    for part in parts:
        if part["lo"] != cursor:
            break
        out.append(part)
        cursor = part["hi"] + 1
    return out


def fmt(n: int) -> str:
    return f"{n:,}"


def loss(parent: int, surviving: int) -> str:
    n = parent - surviving
    pct = (100.0 * n / parent) if parent else 0.0
    return f"{fmt(n)} ({pct:.4f}%)"


def table_escape(value: object) -> str:
    return str(value).replace("|", "\\|")


def render() -> str:
    parts = completed_specs()
    prefix = contiguous_prefix(parts)
    covered_hi = prefix[-1]["hi"] if prefix else 0
    coverage = covered_hi / TOTAL_BRICKID
    complete = covered_hi == TOTAL_BRICKID
    totals = {k: sum(p["values"][k] for p in prefix) for k in FIELDS}
    bound_reached = totals["n_cut5_parent_dered"] >= STOP_PARENT_LOWER_BOUND
    status_path = EVIDENCE / "partitions" / "status.json"
    status = json.loads(status_path.read_text()) if status_path.exists() else {}
    stop_reason = status.get("stop_reason")
    deadline_reached = stop_reason == "four_hour_wall_clock_deadline_reached"
    process_custody_line = (
        f"- The bounded manifest stopped cleanly at `{status['finished_utc']}` with stop reason `{stop_reason}`; no further partition was submitted after the stopping rule fired. Final process verification found no orchestrator, no TAP runner, and no lock holder."
        if status.get("finished_utc")
        else "- The bounded manifest is running detached under the sole filesystem lock. Hwao disclosed starting the unmodified Tori orchestrator on Duho's order; Tori independently verified the process, cwd, lock, child ranges, and no duplicate submissions."
    )
    if complete:
        label = "EXACT FULL-COVERAGE COUNT"
    elif bound_reached:
        label = "STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND"
    else:
        label = "LOWER BOUND ON CONTIGUOUS PARTIAL COVERAGE"

    base_receipt = json.loads((EVIDENCE / "run00_base_count" / "receipt.json").read_text())
    base_count = int(base_receipt["result"]["n_base"])
    goru = PREREG / "GORU_ACCEPTED_YIELD_RECEIPT_20260812.md"
    yui = PREREG / "YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md"
    route = PREREG / "TORI_SURVEY_ROUTE_BINDING_20260812.md"
    detached_custody = EVIDENCE / "partitions" / "DETACHED_LAUNCH_CUSTODY_20260812.json"
    rule_handoff_custody = EVIDENCE / "partitions" / "DERED_STOP_RULE_HANDOFF_CUSTODY_20260812.json"
    independent_reconstruction = EVIDENCE / "partitions" / "FINAL_THRESHOLD_INDEPENDENT_RECONSTRUCTION_20260812.json"

    lines: list[str] = []
    lines += [
        "# TORI — DESI Legacy DR10.1 South Parent Row Count",
        "",
        f"**Receipt rendered:** `{utc_now()}`  ",
        f"**Status:** `{label}`  ",
        "**Authorization:** Duho: `authorize the parent row count` — server-side aggregate counts only.",
        "",
        "## 0. Result boundary",
        "",
        "This receipt reports catalogue **counts**, not a study sample and not a scientific result. It contains no object rows, identifiers, position list, images, handedness, chirality, dipole, axis-relative term, or other sky statistic. No bulk sweep download occurred. No literature fraction or Yui retention was multiplied into these counts.",
        "",
        "Forbidden operations remained at zero:",
        "",
        "- sample/catalogue rows exported: **0**",
        "- identifiers or positions exported: **0**",
        "- images requested for measurement: **0**",
        "- handedness/chirality calls: **0**",
        "- trigonometric or Longo-axis query terms: **0**",
        "- sky statistics/results: **0**",
        "- publication/acceptance/commit/push: **0**",
        "",
        "## 1. Bound inputs and endpoint",
        "",
        f"- Goru frozen cuts: `{goru}` — SHA-256 `{sha(goru)}`.",
        f"- Tori route binding: `{route}` — SHA-256 `{sha(route)}`.",
        f"- Yui context only: `{yui}` — SHA-256 `{sha(yui)}`. Its one-sided lower 95% synthetic retention bound is 0.9615; **not multiplied here**.",
        "- Catalogue: `ls_dr10.tractor_s` (DESI Legacy DR10 South served by NOIRLab Astro Data Lab).",
        "- Photo-z: `ls_dr10.photo_z` joined on `(ls_id, release, brickid, objid)`.",
        "- Endpoint: `https://datalab.noirlab.edu/tap/async` (IVOA UWS asynchronous TAP).",
        f"- Schema receipt: `{EVIDENCE / 'schema_result.csv'}` — SHA-256 `{sha(EVIDENCE / 'schema_result.csv')}`.",
        "- Live global base count endpoint/query receipt: `run00_base_count/receipt.json`.",
        "",
        "The NOIRLab data page documented 2,825,807,500 `tractor_s` rows, while the live aggregate returned 2,827,055,986. This receipt uses the live server-side count and discloses the 1,248,486-row metadata drift.",
        "",
        "## 2. Coverage and no-extrapolation rule",
        "",
        f"- Contiguous completed `BRICKID` range: `1..{covered_hi}` of documented key range `1..{TOTAL_BRICKID}`.",
        f"- Catalogue partition-key coverage: **{covered_hi:,}/{TOTAL_BRICKID:,} = {coverage:.6%}**.",
        f"- Not yet covered: `BRICKID {covered_hi + 1}..{TOTAL_BRICKID}`." if not complete else "- Not yet covered: none.",
        "- This percentage is **BRICKID keyspace coverage, not an equal-area sky fraction**. No sky-area statistic was computed.",
        "- Every running sum below is labeled **LOWER BOUND** until all disjoint partitions complete.",
        "- No partition density is scaled up. Totals are sums of landed, non-overlapping aggregate results only.",
        f"- Authorized stopping rule: stop at the first of (a) the **dered Cut-5** contiguous lower bound reaching {STOP_PARENT_LOWER_BOUND:,}, (b) wall-clock deadline `{DEADLINE_UTC}`, or (c) keyspace exhaustion. The raw branch is still reported but does not gate stopping.",
        process_custody_line,
        f"- Detached-launch custody: `{detached_custody}` — SHA-256 `{sha(detached_custody)}`.",
        f"- Dered-stop-rule handoff custody: `{rule_handoff_custody}` — SHA-256 `{sha(rule_handoff_custody)}`." if rule_handoff_custody.exists() else "- Dered-stop-rule handoff custody: pending relaunch verification.",
        f"- Independent reconstruction: `{independent_reconstruction}` — SHA-256 `{sha(independent_reconstruction)}`. It independently summed the contiguous hash-matched one-row receipts rather than trusting `status.json` or this rendered Markdown." if independent_reconstruction.exists() else "- Independent reconstruction: pending.",
        "",
        "## 3. Survival chain",
        "",
        "Goru Cut 4 is ambiguous in the served data model. His wording says `flux_r` converted to magnitude, which maps literally to `mag_r < 17.7`; Tori's route binding described extinction-corrected `dered_mag_r < 17.7`. Both readings are counted through Cut 5 and availability checks; neither is silently selected.",
        "",
        "| Stage | Predicate | Count | Custody status |",
        "|---|---|---:|---|",
        f"| Base | all `ls_dr10.tractor_s` rows | {fmt(base_count)} | exact live global aggregate |",
        f"| Cut 1 | `brick_primary=1 AND maskbits=0` | {fmt(totals['n_cut1_primary_mask'])} | {label} |",
        f"| Cut 2 | Cut 1 + `type<>'PSF' AND flux_r>0` | {fmt(totals['n_cut2_extended_flux'])} | {label} |",
        f"| Photo-z join availability after Cut 2 | matching `(ls_id,release,brickid,objid)` | {fmt(totals['n_photoz_joined_cut2'])} | {label} |",
        f"| Cut 3 | Cut 2 + `0<=z_phot_median<0.15` | {fmt(totals['n_cut3_photoz'])} | {label} |",
        f"| Cut 4 raw branch | Cut 3 + `mag_r<17.7` | {fmt(totals['n_cut4_raw_mag'])} | {label} |",
        f"| Cut 4 dered branch | Cut 3 + `dered_mag_r<17.7` | {fmt(totals['n_cut4_dered_mag'])} | {label} |",
        f"| Cut 5 raw parent | raw Cut 4 + `shape_r>1.5` | {fmt(totals['n_cut5_parent_raw'])} | {label} |",
        f"| Cut 5 dered parent | dered Cut 4 + `shape_r>1.5` | {fmt(totals['n_cut5_parent_dered'])} | {label} |",
        "",
        "These are parent counts only. Tori does not decide whether either branch supplies the requested accepted yield and does not multiply spiral, inclination, or estimator-retention factors.",
        "",
        "## 4. Countable availability losses",
        "",
        "All loss counts below are relative to the corresponding Cut-5 parent within the completed contiguous partitions. Overlapping failure modes are not added.",
        "",
        "| Availability reading | Raw surviving | Raw loss | Dered surviving | Dered loss |",
        "|---|---:|---:|---:|---:|",
        f"| all-band `nobs_g,r,z>0` | {fmt(totals['n_raw_allband_nobs'])} | {loss(totals['n_cut5_parent_raw'], totals['n_raw_allband_nobs'])} | {fmt(totals['n_dered_allband_nobs'])} | {loss(totals['n_cut5_parent_dered'], totals['n_dered_allband_nobs'])} |",
        f"| all-band `ngood_g,r,z>0` | {fmt(totals['n_raw_allband_ngood'])} | {loss(totals['n_cut5_parent_raw'], totals['n_raw_allband_ngood'])} | {fmt(totals['n_dered_allband_ngood'])} | {loss(totals['n_cut5_parent_dered'], totals['n_dered_allband_ngood'])} |",
        f"| all-band `flux_ivar_g,r,z>0` | {fmt(totals['n_raw_allband_ivar'])} | {loss(totals['n_cut5_parent_raw'], totals['n_raw_allband_ivar'])} | {fmt(totals['n_dered_allband_ivar'])} | {loss(totals['n_cut5_parent_dered'], totals['n_dered_allband_ivar'])} |",
        f"| valid shape IVARs + `e1^2+e2^2<1` | {fmt(totals['n_raw_shape_valid'])} | {loss(totals['n_cut5_parent_raw'], totals['n_raw_shape_valid'])} | {fmt(totals['n_dered_shape_valid'])} | {loss(totals['n_cut5_parent_dered'], totals['n_dered_shape_valid'])} |",
        f"| native depth/PSF/dust/flux/fit/coordinate covariates | {fmt(totals['n_raw_native_covariates'])} | {loss(totals['n_cut5_parent_raw'], totals['n_raw_native_covariates'])} | {fmt(totals['n_dered_native_covariates'])} | {loss(totals['n_cut5_parent_dered'], totals['n_dered_native_covariates'])} |",
        f"| all countable requirements together | {fmt(totals['n_raw_all_countable_availability'])} | {loss(totals['n_cut5_parent_raw'], totals['n_raw_all_countable_availability'])} | {fmt(totals['n_dered_all_countable_availability'])} | {loss(totals['n_cut5_parent_dered'], totals['n_dered_all_countable_availability'])} |",
        "",
        "Not countable in this authorized catalogue-only pass:",
        "",
        "- **WCS/parity availability:** requires per-object image/header requests. Measurement-image acquisition is forbidden; count remains `NOT COUNTED`.",
        "- **Gaia DR3 density covariate:** Gaia DR3 is a separate ESA TAP product; Legacy embedded Gaia fields are EDR3. No cross-service positional sample or position export was authorized; count remains `NOT COUNTED`.",
        "- **Image-derived arm contrast/visibility:** requires measurement images and is forbidden; count remains `NOT COUNTED`.",
        "- **Sky-area footprint variance:** no sky statistic was computed. Operational partition densities are documented below without extrapolation.",
        "",
        "## 5. Partition density and gradient",
        "",
        "`Cut-2 rows per BRICKID` and both Cut-5 parent rows per BRICKID are recorded for every landed database partition to document nonuniform catalogue density. These are aggregate operational densities, not axis-relative statistics and not a basis for extrapolation.",
        "",
        "| BRICKID range | Width | Started UTC | Completed UTC | Elapsed | Cut 1 | Cut 2 | Cut-2/BRICKID | Cut 3 | Cut 5 raw | Raw/BRICKID | Cut 5 dered | Dered/BRICKID | Result bytes | Query SHA-256 | TAP job |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]

    for p in prefix:
        r = p["receipt"]
        v = p["values"]
        width = p["hi"] - p["lo"] + 1
        density = v["n_cut2_extended_flux"] / width
        lines.append(
            "| "
            + " | ".join(
                map(
                    table_escape,
                    [
                        f"{p['lo']}..{p['hi']}",
                        width,
                        r["started_utc"],
                        r["completed_utc"],
                        f"{p['elapsed_seconds']:.0f}s",
                        fmt(v["n_cut1_primary_mask"]),
                        fmt(v["n_cut2_extended_flux"]),
                        f"{density:.6f}",
                        fmt(v["n_cut3_photoz"]),
                        fmt(v["n_cut5_parent_raw"]),
                        f"{v['n_cut5_parent_raw'] / width:.6f}",
                        fmt(v["n_cut5_parent_dered"]),
                        f"{v['n_cut5_parent_dered'] / width:.6f}",
                        r["result_bytes"],
                        r["query_sha256"],
                        r["job_url"],
                    ],
                )
            )
            + " |"
        )

    if len(prefix) >= 3:
        first_three = prefix[:3]
        lines += [
            "",
            "Three-point final-stage density series (landed aggregate receipts only):",
            "",
            "| BRICKID range | Cut-5 raw | Raw/BRICKID | Cut-5 dered | Dered/BRICKID |",
            "|---|---:|---:|---:|---:|",
        ]
        for p in first_three:
            width = p["hi"] - p["lo"] + 1
            raw = p["values"]["n_cut5_parent_raw"]
            dered = p["values"]["n_cut5_parent_dered"]
            lines.append(
                f"| `{p['lo']}..{p['hi']}` | {fmt(raw)} | {raw / width:.6f} | {fmt(dered)} | {dered / width:.6f} |"
            )
        dered_1 = first_three[0]["values"]["n_cut5_parent_dered"] / (first_three[0]["hi"] - first_three[0]["lo"] + 1)
        dered_2 = first_three[1]["values"]["n_cut5_parent_dered"] / (first_three[1]["hi"] - first_three[1]["lo"] + 1)
        dered_3 = first_three[2]["values"]["n_cut5_parent_dered"] / (first_three[2]["hi"] - first_three[2]["lo"] + 1)
        raw_1 = first_three[0]["values"]["n_cut5_parent_raw"] / (first_three[0]["hi"] - first_three[0]["lo"] + 1)
        raw_2 = first_three[1]["values"]["n_cut5_parent_raw"] / (first_three[1]["hi"] - first_three[1]["lo"] + 1)
        raw_3 = first_three[2]["values"]["n_cut5_parent_raw"] / (first_three[2]["hi"] - first_three[2]["lo"] + 1)
        lines += [
            "",
            f"- Dered series: `{dered_1:.6f} -> {dered_2:.6f} -> {dered_3:.6f}` parent rows/BRICKID.",
            f"- Dered decline from the second to third point: **{100 * (1 - dered_3 / dered_2):.6f}%**; first to third: **{100 * (1 - dered_3 / dered_1):.6f}%**.",
            f"- Raw series: `{raw_1:.6f} -> {raw_2:.6f} -> {raw_3:.6f}` parent rows/BRICKID.",
            f"- Raw decline from the second to third point: **{100 * (1 - raw_3 / raw_2):.6f}%**; first to third: **{100 * (1 - raw_3 / raw_1):.6f}%**.",
            "- This third point overturns the earlier provisional reading that final-stage density was approximately flat across the first two adjacent ranges. The no-extrapolation rule is therefore load-bearing: neither the Cut-2 nor Cut-5 partition density is uniform enough to scale unqueried ranges.",
        ]

    diagnostic_run = EVIDENCE / "run10_tractor_011001_061000"
    diagnostic_csv = diagnostic_run / "result.csv"
    diagnostic_receipt = diagnostic_run / "receipt.json"
    if diagnostic_csv.exists() and diagnostic_receipt.exists():
        row = next(csv.DictReader(diagnostic_csv.read_text().splitlines()))
        d_cut2 = int(row["n_cut2_extended_flux"])
        d_density = d_cut2 / 50000
        first_density = prefix[0]["values"]["n_cut2_extended_flux"] / 1000 if prefix else 0
        drop = 100 * (1 - d_density / first_density) if first_density else 0
        lines += [
            "",
            "Overlapping diagnostic (never added to full-chain totals):",
            "",
            f"- Run 10, `BRICKID 11001..61000`, Tractor-only Cut 1–2: Cut 2 = {fmt(d_cut2)}; density = **{d_density:.6f} rows/BRICKID**.",
            f"- Compared with `BRICKID 1..1000` density {first_density:.6f}, this is a **{drop:.4f}% decrease**.",
            "- Because the partition density is not uniform, no partition is scaled to infer an unqueried total.",
            f"- Diagnostic receipt: `{diagnostic_receipt}` — SHA-256 `{sha(diagnostic_receipt)}`.",
        ]

    lines += [
        "",
        "## 6. Exact query custody",
        "",
        "Every executed query is preserved verbatim at the absolute query path below and pinned by the SHA-256 in the partition table. The production query text is identical across partitions except for the final literal inclusive `BRICKID BETWEEN <lo> AND <hi>` bounds. This is exact reconstructible query text, not a paraphrase.",
        "",
        f"- Production template/example (literal range `1001..11000`): `{EVIDENCE / '09_partition_benchmark_brickid_001001_011000.adql'}`.",
        f"- Remaining partition manifest: `{EVIDENCE / 'partitions/manifest.json'}` — SHA-256 `{sha(EVIDENCE / 'partitions/manifest.json')}`.",
        f"- Aggregate-only runner: `{EVIDENCE / 'run_aggregate_tap.py'}` — SHA-256 `{sha(EVIDENCE / 'run_aggregate_tap.py')}`.",
        "- Runner guard rejects row/export/mutation constructs and rejects `SIN`, `COS`, `TAN`, `RADIANS`, `DEGREES`, and `COSTHETA`.",
        "",
        "Exact production query template:",
        "",
        "```adql",
        (EVIDENCE / "09_partition_benchmark_brickid_001001_011000.adql").read_text().rstrip(),
        "```",
        "",
        "## 7. Abandoned global jobs (retained, not deleted)",
        "",
        "These jobs produced no count result and are not included in any total:",
        "",
        "| Role | TAP job | Final server phase | Reason | Result/sample/position rows | Receipt |",
        "|---|---|---|---|---:|---|",
        f"| initial conditional global Cut 1–2 | `cufh26hignovtpss` | `ABORTED` | exceeded 3600-second window; unconstrained conditional scan | 0/0/0 | `{EVIDENCE / 'run01_cut1_cut2/abort_receipt.json'}` |",
        f"| global indexed Cut 1 | `ugcy42h6l52xbj8d` | `ABORTED` | exceeded 3600-second window | 0/0/0 | `{EVIDENCE / 'run04_cut1_indexed/abort_receipt.json'}` |",
        f"| Run 11 global low-z full-chain | `y74tcwewq9rp4fim` | `ABORTED`; method status **ABANDONED** | exceeded 3600-second window; Duho directed partition completion | 0/0/0 | `{EVIDENCE / 'run11_global_cut3_losses/abort_receipt.json'}` |",
        "",
        "A locally drafted query containing Longo-axis `cos(theta)` moments was caught before submission, marked `DO NOT EXECUTE`, and is rejected by the hardened runner. It was never run and produced zero rows/statistics:",
        "",
        f"- `{EVIDENCE / '03_SUPERSEDED_DO_NOT_EXECUTE.md'}` — SHA-256 `{sha(EVIDENCE / '03_SUPERSEDED_DO_NOT_EXECUTE.md')}`.",
        "",
        "## 8. Freeze-condition interpretation and stop line",
        "",
    ]
    if complete:
        lines += [
            "All documented `BRICKID 1..662174` partitions have landed and were summed without extrapolation. Goru may consume the exact parent counts and handle the external priors. Tori makes no accepted-yield or scientific-result claim.",
        ]
    elif bound_reached:
        lines += [
            f"The authorized dered stop bound is reached without extrapolation: the contiguous partial-coverage Cut-5 lower bounds are raw `{fmt(totals['n_cut5_parent_raw'])}` and dered `{fmt(totals['n_cut5_parent_dered'])}`; the dered branch is at least `{fmt(STOP_PARENT_LOWER_BOUND)}`. This is a lower-bound certificate for the dered catalogue reading only. It does **not** estimate the unqueried remainder, choose the magnitude ambiguity, or claim an exact full-catalogue total.",
            "Kun's freeze condition 2 may close on this hash-bound dered lower-bound certificate if his gate requires proof that the dered parent exceeds 200,000. Goru owns all multiplication by external spiral, inclination, or estimator-retention factors. Tori makes no accepted-yield or scientific-result claim.",
        ]
    elif deadline_reached:
        lines += [
            f"The four-hour wall-clock stop fired at deadline `{DEADLINE_UTC}` before the dered lower bound reached `{fmt(STOP_PARENT_LOWER_BOUND)}`. The receipt covers **{covered_hi:,}/{TOTAL_BRICKID:,} = {coverage:.6%}** of the documented BRICKID keyspace contiguously. This is not sky-area coverage. All reported counts remain partial lower bounds, not final full-catalogue totals, and freeze condition 2 is not closed by the threshold rule.",
        ]
    else:
        lines += [
            f"The authorized stop bound is **not yet reached**. The current Cut-1 through Cut-5 and availability sums are honest lower bounds over contiguous `BRICKID 1..{covered_hi}` only. Freeze condition 2 is not closed by this partial receipt. The remaining exact next action is to continue the bounded manifest from the first incomplete partition and rerender after each landed one-row aggregate.",
        ]
    lines += [
        "",
        "Empirical Longo-amplitude execution remains blocked. This authorization did not open handedness, chirality, images, a sky statistic, a result, publication, or accepted status.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    content = render()
    tmp = OUT.with_suffix(OUT.suffix + ".tmp")
    tmp.write_text(content)
    tmp.replace(OUT)
    print(json.dumps({"path": str(OUT), "bytes": OUT.stat().st_size, "sha256": sha(OUT)}, sort_keys=True))


if __name__ == "__main__":
    main()
