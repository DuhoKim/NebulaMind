#!/usr/bin/env python3
"""Render the superseding footprint-variance receipt from the closed rerun outcome."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
RUN = ROOT / "footprint_variance_partitioned_rerun_20260814"
OUTCOME_PATH = RUN / "FINAL_OUTCOME_20260814_RERUN.json"
OUTPUT = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
GLOBAL_HISTORY = PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md"
PARTITION_HISTORY = PREREG / "TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def result_ruling(outcome: dict) -> tuple[str, str]:
    status = outcome["status"]
    verdict = outcome["threshold_verdict"]
    combined = outcome.get("combined_moments")
    if status == "COMPLETE":
        if verdict not in {"PASS", "FAIL"} or combined is None:
            raise RuntimeError("complete outcome lacks numeric verdict")
        variance = combined["var_pop_cos_theta"]
        if verdict == "PASS":
            return (
                f"FULL RESULT: var(cos theta) = {variance} >= 0.15 — PASS",
                "The full frozen footprint meets Kun's preregistered angular-spread threshold.",
            )
        return (
            f"FULL RESULT: var(cos theta) = {variance} < 0.15 — FAIL",
            "This is a real below-threshold result: the frozen footprint cannot support the Longo-amplitude test as designed.",
        )
    if verdict != "NONE":
        raise RuntimeError("incomplete outcome has a threshold verdict")
    if status == "PARTIAL":
        return (
            "PARTIAL RESULT ONLY — FULL-FOOTPRINT THRESHOLD VERDICT NONE",
            "The landed additive moments are exact for the listed completed ranges only. They are not the full footprint and do not pass or fail 0.15.",
        )
    if status == "UNRESOLVED":
        return (
            "UNRESOLVED — NO PARTITION MOMENTS LANDED; THRESHOLD VERDICT NONE",
            "No numeric variance exists. This is neither a pass nor a below-threshold failure.",
        )
    raise RuntimeError(f"unknown outcome status: {status}")


def main() -> None:
    outcome = json.loads(OUTCOME_PATH.read_text())
    if outcome["guard_state"] != "CLOSED":
        raise RuntimeError("refuse receipt while exception is not CLOSED")
    if not outcome["ordinary_guard_unchanged"] or not outcome["ordinary_guard_verified_rejects_query_after"]:
        raise RuntimeError("refuse receipt without guard restoration proof")
    title, ruling = result_ruling(outcome)
    combined = outcome.get("combined_moments")
    moments = (
        "- returned contributing count: **NONE**;\n"
        "- `SUM(x)`: **NONE**;\n"
        "- `SUM(x*x)`: **NONE**;\n"
        "- `mean(cos theta)`: **UNMEASURED**;\n"
        "- population `var(cos theta)`: **UNMEASURED**."
        if combined is None
        else (
            f"- returned contributing count: `{combined['n_cut6_dered']}`;\n"
            f"- `SUM(x)`: `{combined['sum_cos_theta']}`;\n"
            f"- `SUM(x*x)`: `{combined['sum_cos2_theta']}`;\n"
            f"- `mean(cos theta)`: `{combined['mean_cos_theta']}`;\n"
            f"- population `var(cos theta)`: `{combined['var_pop_cos_theta']}`."
        )
    )
    jobs = []
    for row in outcome["jobs"]:
        job_id = row["job_url"].rstrip("/").split("/")[-1]
        remote = row["remote"]
        remote_text = f"HTTP {remote.get('http_status')} / {remote.get('phase') or 'no phase'}"
        abort = row.get("abort_record")
        abort_text = "none" if not abort else f"{abort.get('reason')} / {abort.get('phase_after', 'phase unrecorded')}"
        r = row["brickid_range"]
        jobs.append(
            f"| `{r['lo']}–{r['hi']}` | `{job_id}` | `{row['query_sha256']}` | {abort_text} | {remote_text} |"
        )
    job_table = "\n".join(jobs) or "| none | none | none | none | none |"
    landed = []
    for row in outcome["landed_partitions"]:
        r = row["brickid_range"]
        landed.append(
            f"| `{r['lo']}–{r['hi']}` | {row['n_cut6_dered']} | `{row['sum_cos_theta']}` | "
            f"`{row['sum_cos2_theta']}` | `{row['result_sha256']}` |"
        )
    landed_table = "\n".join(landed) or "| none | none | none | none | none |"

    text = f"""# TORI — Longo-axis footprint-variance receipt

**Status:** **{title}**  
**Frozen threshold:** `var(cos theta) >= 0.15`  
**Threshold verdict:** **{outcome['threshold_verdict']}**

## Plain ruling

{ruling}

The freshly authorized rerun used the same frozen dered Cut-6 population, same Longo axis `(l,b)=(52°,68.5°)`, same 67 disjoint BRICKID partitions, and same hash-pinned `cos(theta)` expression. The population, axis, threshold, and scientific framing were not changed.

Stop reason: `{outcome['stop_reason']}`. Completed coverage: **{outcome['completed_partitions']} of {outcome['partition_count']} partitions**, **{outcome['completed_keyspace_units']} of {outcome['full_keyspace_units']} BRICKID keyspace units**. BRICKID keyspace is not sky area.

## Additive moments

{moments}

Exact recombination is `mean = sum(SUM(x))/sum(n)` and `var = sum(SUM(x*x))/sum(n) - mean^2`. Any partial combination is labelled PARTIAL and applies only to its listed disjoint completed ranges; it is never presented as the full footprint and carries threshold verdict NONE.

## Preserved supersession history

- original global attempt: `TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md` — SHA-256 `{sha(GLOBAL_HISTORY)}`;
- first partitioned attempt: `TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md` — SHA-256 `{sha(PARTITION_HISTORY)}`;
- current machine outcome: `FINAL_OUTCOME_20260814_RERUN.json` — SHA-256 `{sha(OUTCOME_PATH)}`.

Both prior receipts remain byte-for-byte history. This file supersedes only the live receipt filename.

## Manifest and execution custody

- source 67-partition manifest SHA-256: `{outcome['hashes']['source_manifest']}`;
- rerun manifest SHA-256: `{outcome['hashes']['manifest']}`;
- status SHA-256: `{outcome['hashes']['status']}`;
- guard lifecycle SHA-256: `{outcome['hashes']['guard_lifecycle']}`;
- executed orchestrator SHA-256: `{outcome['hashes']['orchestrator']}`;
- executed worker SHA-256: `{outcome['hashes']['worker']}`;
- expected full-population count from the independent count certificate: `832393`.

The expected count is not described as returned `n` unless all 67 partitions actually returned it.

## UWS job reconciliation

| BRICKID range | UWS job id | Query SHA-256 | Abort custody | Independent remote recheck |
|---|---|---|---|---|
{job_table}

Unique UWS jobs: **{outcome['unique_job_urls']}**. Result CSVs: **{outcome['result_csv_count']}**. Partition receipts: **{outcome['receipt_json_count']}**.

## Landed partition moments

| BRICKID range | n | SUM(x) | SUM(x*x) | Result SHA-256 |
|---|---:|---:|---:|---|
{landed_table}

## Guard restoration and physical closure

- exception state: **{outcome['guard_state']}**;
- ordinary guard SHA-256 before: `{outcome['ordinary_guard_sha256_before']}`;
- ordinary guard SHA-256 after: `{outcome['ordinary_guard_sha256_after']}`;
- hashes identical: **{'YES' if outcome['ordinary_guard_unchanged'] else 'NO'}**;
- ordinary guard independently verified to reject the query after close: **{'YES' if outcome['ordinary_guard_verified_rejects_query_after'] else 'NO'}**.

Executed runner bytes are custody, not standing permission. The current exception entry points are disabled refusal stubs.

## Boundary ledger

- aggregate result rows returned: **{outcome['result_csv_count']}**;
- object rows exported: **{outcome['object_rows_exported']}**;
- positions exported: **{outcome['positions_exported']}**;
- images requested: **{outcome['images_requested']}**;
- angle bins: **{outcome['angle_bins']}**;
- sky maps: **{outcome['sky_maps']}**;
- dipole amplitudes: **{outcome['dipole_amplitudes']}**;
- extra directional outputs: **{outcome['extra_directional_outputs']}**;
- publication/acceptance/commit/push: **{outcome['publication_acceptance_commit_push']}**.

No chirality, handedness, spin, CW/CCW, or signal-bearing field entered any query.

## Exact next action

{'Use the full measured verdict in the preregistration gate without rescoping.' if outcome['status'] == 'COMPLETE' else 'Keep the footprint-variance item open. Any further empirical attempt requires new explicit authorization; this receipt grants none.'}
"""
    OUTPUT.write_text(text)
    print(f"rendered={OUTPUT} status={outcome['status']} verdict={outcome['threshold_verdict']} sha256={sha(OUTPUT)}")


if __name__ == "__main__":
    main()
