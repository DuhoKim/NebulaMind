#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
RUN = ROOT / "footprint_variance_partitioned_20260813"
OUTCOME = RUN / "FINAL_OUTCOME_20260814.json"
OUTPUT = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
ATTEMPT = PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def short_job(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def main() -> None:
    o = json.loads(OUTCOME.read_text())
    assert o["status"] == "UNRESOLVED"
    assert o["threshold_verdict"] == "NONE"
    assert o["completed_partitions"] == 0
    assert o["aggregate_result_rows"] == 0
    assert o["guard_state"] == "CLOSED"
    assert sha(ATTEMPT) == o["hashes"]["attempt_history"]

    rows = []
    for range_key in sorted(o["attempts_by_range"], key=lambda x: int(x.split("-")[0])):
        for index, attempt in enumerate(o["attempts_by_range"][range_key], start=1):
            remote = attempt["remote_checked_phase"]
            remote_text = (
                f"HTTP {remote['http_status']} / {remote['phase']}"
                if remote.get("phase")
                else f"HTTP {remote['http_status']} / no phase"
            )
            rows.append(
                f"| `{range_key}` | {index} | `{short_job(attempt['job_url'])}` | "
                f"`{attempt['query_sha256']}` | `{attempt['terminal_custody']}` | {remote_text} |"
            )
    table = "\n".join(rows)

    md = f"""# TORI — Longo-axis footprint-variance receipt

**Superseding receipt assembled UTC:** `{utc_now()}`  
**Status:** **UNRESOLVED — PARTITIONED RE-RUN REACHED THE 06:00 KST DEADLINE WITH ZERO LANDED PARTITIONS**  
**Kun BS-1 threshold:** `var(cos theta) >= 0.15`  
**Threshold verdict:** **NONE — no additive moments were returned**

## Plain ruling

Duho freshly authorized a partitioned re-run of the same Longo-axis statistic over the same frozen dered Cut-6 population. The frozen manifest contained **67 disjoint BRICKID ranges covering `1…662174`**. Each query could return one aggregate row containing only `n`, `SUM(cos theta)`, and `SUM(cos theta * cos theta)`.

The service returned **zero partition aggregate rows** before the stop rule fired at `2026-08-14T06:00:04+09:00` (`2026-08-13T21:00:04Z`). Completed coverage is therefore **0 of 67 partitions / 0 of 662,174 BRICKID keyspace units**. No mean or variance can be reconstructed.

Accordingly:

- `mean(cos theta)`: **UNMEASURED**;
- population `var(cos theta)`: **UNMEASURED**;
- comparison with `0.15`: **NONE**;
- Kun's footprint-variance requirement: **UNRESOLVED**.

This is not a below-threshold result and not a pass. A value below `0.15` would have been reported as a real failure without changing the population, but no numeric value exists. No partial subset, friendlier range, extrapolation, density assumption, or rescaled result is used.

## Supersession and preserved history

This receipt supersedes the live filename previously occupied by the one-global-query attempt receipt. That attempt remains byte-for-byte at:

- `TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md` — SHA-256 `{o['hashes']['attempt_history']}`.

The original global job `v0d4e15lm8hkz7zv` was one authorized query, ran `03:09:56`, was explicitly aborted, and returned zero moments. It is history, not one of the nine partition UWS jobs below.

## Authorized statistic and exact recombination

Population: the same frozen dered Cut-6 catalogue population whose prior count certificate gives **832,393** objects. That number is an expected population check from `TORI_FULL_KEYSPACE_SWEEP_20260813.md`; it is **not** a returned contributing count from this variance run.

Axis: Longo's Galactic `(l,b)=(52°,68.5°)`.

For each object, `x = cos(theta)` used the same frozen axis-relative expression. Each disjoint partition requested only:

- `n = COUNT(x)`;
- `SUM(x)`;
- `SUM(x*x)`.

Had all 67 partitions landed, exact recombination would have been:

- `mean = sum(SUM(x)) / sum(n)`;
- `var_pop = sum(SUM(x*x)) / sum(n) - mean^2`.

This is exact additive-moment recombination, not approximation or extrapolation. It could not be performed because `sum(n)`, `sum(SUM(x))`, and `sum(SUM(x*x))` were all absent.

## Manifest and deadline custody

- manifest: `footprint_variance_partitioned_20260813/manifest.json` — SHA-256 `{o['hashes']['manifest']}`;
- manifest partitions: `67`;
- frozen coverage: `BRICKID 1…662174`;
- expected prior Cut-6 count: `832393`;
- frozen full-query hash: `5d4c7812331419eff0ec7dca4e40f690203cb94cc71b6309d7b8694299249ff1`;
- frozen cos-expression hash: `ddf9bd2550fdde7d9d285e5e03833186bb9a9393fb5d45857b59873bf70b8663`;
- deadline: `2026-08-14T06:00:00+09:00` / `2026-08-13T21:00:00Z`;
- stop recorded: `deadline_reached` at `2026-08-13T21:00:04Z`;
- status record: SHA-256 `{o['hashes']['status']}`;
- final machine outcome: `FINAL_OUTCOME_20260814.json` — SHA-256 `{sha(OUTCOME)}`.

Where BRICKID coverage is stated, **BRICKID keyspace is not sky area**.

## Service-pressure and job history

Nine unique partition UWS jobs were created across only the first three disjoint ranges. Eight jobs encountered HTTP 502 pressure, were later missing at their recorded phase URLs, and are preserved as `LOST_404_AFTER_502`. One final first-range job was explicitly aborted by the deadline handler and independently rechecked as remote phase `ABORTED`.

No job produced a result CSV or partition receipt.

| BRICKID range | Attempt in range | UWS job id | Immutable query SHA-256 | Terminal custody | Independent remote recheck |
|---|---:|---|---|---|---|
{table}

Final reconciliation:

- UWS submission records: **{o['submission_records']}**;
- unique UWS job URLs: **{o['unique_job_urls']}**;
- lost after HTTP 502 and rechecked HTTP 404: **{o['lost_jobs_404_after_pressure']}**;
- deadline-aborted and rechecked `ABORTED`: **{o['deadline_aborted_jobs']}**;
- landed result CSVs: **{o['aggregate_result_rows']}**;
- partition receipts: **0**;
- reconciliation artifact: `FINAL_JOB_RECONCILIATION_20260814.json` — SHA-256 `{o['hashes']['job_reconciliation']}`.

Concurrency was initially at most three, dropped to serial after pressure, and was later explicitly raised back to three after health checks. The raised jobs remained scheduler-pending; no fourth active range was added while three were pending. New pressure again forced serial. No landed partition was ever re-queried because none landed.

## Guard lift, restoration, and physical closure

- exception state: **CLOSED**;
- ordinary guard SHA-256 before: `{o['ordinary_guard_sha256_before']}`;
- ordinary guard SHA-256 after: `{o['ordinary_guard_sha256_after']}`;
- hashes identical: **YES**;
- ordinary guard independently verified to reject the trigonometric query after close: **YES**;
- guard lifecycle: SHA-256 `{o['hashes']['guard_lifecycle']}`;
- executed orchestrator custody: SHA-256 `{o['hashes']['orchestrator_executed']}`;
- executed worker custody: SHA-256 `{o['hashes']['worker_executed']}`;
- active Python variance processes after close: **0**;
- current orchestrator entry point: **disabled refusal stub**;
- current partition-worker entry point: **disabled refusal stub**.

The executed source bytes are retained under `footprint_variance_partitioned_20260813/executed_code_custody/` and match the manifest hashes. Retention is custody, not standing execution permission.

## Boundary ledger

- aggregate moment rows returned: **0**;
- object rows exported: **0**;
- positions exported: **0**;
- images requested: **0**;
- chirality computed: **0**;
- handedness fields joined or referenced: **0**;
- spin or CW/CCW fields joined or referenced: **0**;
- dipole amplitude computed: **0**;
- sky maps or angle bins: **0**;
- directional statistic beyond the authorized variance: **0**;
- population/axis/threshold change: **0**;
- publication/acceptance/commit/push: **0**.

## Exact next action

Kun's footprint-variance item remains open. This run has ended and grants no standing permission for another submission. Any later empirical attempt requires a new explicit authorization and a new closed-loop guard receipt. Until then, the BS-1/freeze packet must carry the variance item as **UNRESOLVED**, never as pass or fail.
"""
    OUTPUT.write_text(md)
    print(f"rendered={OUTPUT} status=UNRESOLVED submissions={o['submission_records']} results=0 guard=CLOSED")


if __name__ == "__main__":
    main()
