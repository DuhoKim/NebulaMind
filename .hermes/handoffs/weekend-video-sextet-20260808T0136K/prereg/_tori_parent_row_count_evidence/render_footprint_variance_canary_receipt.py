#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
CANARY = ROOT / "footprint_variance_canary_20260814"
RERUN = ROOT / "footprint_variance_partitioned_rerun_20260814"
OUTPUT = PREREG / "TORI_FOOTPRINT_VARIANCE_CANARY_RECEIPT_20260814.md"
VARIANCE_RECEIPT = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
GLOBAL_ATTEMPT = PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md"
PARTITION_ATTEMPT = PREREG / "TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md"
EXPECTED_VARIANCE_RECEIPT_SHA = "f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def current_state() -> tuple[str, dict]:
    candidates = [
        ("QUEUE_OPEN", CANARY / "queue_signal.json"),
        ("PARKED", CANARY / "parked_pending.json"),
        ("TERMINAL_FAILURE", CANARY / "terminal_failure.json"),
        ("REMOTE_JOB_LOST", CANARY / "remote_job_lost.json"),
    ]
    for label, path in candidates:
        if path.exists():
            return label, json.loads(path.read_text())
    history = json.loads((CANARY / "poll_history.json").read_text())
    observations = history.get("observations", [])
    latest = next((item for item in reversed(observations) if item.get("kind") == "PHASE"), {})
    return "MONITORING", {"observed_phase": latest.get("phase"), "observed_utc": latest.get("timestamp_utc")}


def main() -> None:
    if sha(VARIANCE_RECEIPT) != EXPECTED_VARIANCE_RECEIPT_SHA:
        raise RuntimeError("unresolved variance receipt drift; canary must not supersede it")
    submission = json.loads((CANARY / "submission.json").read_text())
    lifecycle = json.loads((CANARY / "guard_lifecycle.json").read_text())
    launch = json.loads((CANARY / "LAUNCH_AUTHORIZATION.json").read_text())
    service = json.loads((CANARY / "SERVICE_STALL_PATTERN_20260814.json").read_text())
    rerun_outcome = json.loads((RERUN / "FINAL_OUTCOME_20260814_RERUN.json").read_text())
    state, state_record = current_state()
    phase = state_record.get("observed_phase")
    result_receipt = CANARY / "canary_result_receipt.json"
    landed = result_receipt.exists()
    result_text = "one aggregate result landed" if landed else "no aggregate result has landed"
    state_text = f"{state} / phase {phase}" if phase else state

    md = f"""# TORI — NOIRLab scheduler canary receipt

**Assembled UTC:** `{now()}`  
**Canary state:** **{state_text}**  
**Scientific variance state:** **UNRESOLVED — THRESHOLD VERDICT NONE**  
**Full 67-partition auto-launches:** **0**

## Plain ruling

The 45-minute abort was the right call. The rerun submitted at `2026-08-14T01:45:26Z` left all three active jobs `PENDING` for exactly `2700` seconds with no completed partition and no scheduler progress. Tori's queue-watch stopped it at `2026-08-14T02:30:28Z`; all three jobs were explicitly aborted and independently rechecked `ABORTED`. That reduced recognition of the same no-throughput condition from an overnight run to forty-five minutes instead of continuing to hammer a service that was not scheduling this work.

Duho then authorized exactly one small scheduler canary and no data-run continuation. One existing frozen-manifest partition was submitted:

- BRICKID range: `1…10000`;
- UWS job: `{submission['job_url']}`;
- query SHA-256: `{submission['query_sha256']}`;
- manifest SHA-256: `{submission['manifest_sha256']}`;
- aggregate columns only: `n_cut6_dered`, `sum_cos_theta`, `sum_cos2_theta`;
- initial phase: `PENDING` at `2026-08-14T02:45:03Z`;
- current recorded state: `{state_text}`;
- current result: {result_text}.

The canary is polled GET-only every 300 seconds. If it reaches `EXECUTING` or `COMPLETED`, the monitor reports queue opening and stops; it cannot launch the remaining 66 partitions. If it remains pending through the 10,800-second observation window, the monitor reports that state and leaves the remote job parked without an abort.

## Why `1…10000`

This is the first nonempty partition in the existing 67-partition manifest. It was selected instead of inventing a new subpartition or using the known-empty 2,174-key tail. If it completes, its additive moments remain a genuine exact partial contribution for the frozen population.

Prior count custody provides a fail-closed magnitude bracket without a new count query:

- exact dered Cut-6 `n(1…1000) = 2583`;
- exact dered Cut-6 `n(1001…11000) = 23881`;
- therefore `2583 <= n(1…10000) <= 26464`.

A completed canary outside that bracket is rejected rather than accepted as a landed partition.

## Guard lifecycle and executable closure

- opened UTC: `{lifecycle['opened_utc']}`;
- closed UTC: `{lifecycle['closed_utc']}`;
- state: **{lifecycle['exception_state']}**;
- submissions made / limit: `{lifecycle['submissions_made']}/{lifecycle['submission_limit']}`;
- ordinary guard SHA-256 before: `{lifecycle['ordinary_guard_sha256_before']}`;
- ordinary guard SHA-256 after: `{lifecycle['ordinary_guard_sha256_after']}`;
- hashes identical: **{str(lifecycle['ordinary_guard_unchanged']).upper()}**;
- ordinary guard specifically verified to reject the trigonometric query before: **{str(lifecycle['ordinary_guard_verified_rejects_query_before']).upper()}**;
- ordinary guard specifically verified to reject the trigonometric query after: **{str(lifecycle['ordinary_guard_verified_rejects_query_after']).upper()}**;
- executed submitter SHA-256: `{lifecycle['submitter_sha256']}`;
- live POST path: **DISABLED AFTER ONE SUBMISSION**;
- retained monitor: **GET-ONLY**;
- full-manifest launch path in monitor: **NONE**.

## Two service-stall modes observed locally in under one day

This is a local operational observation, not a public NOIRLab status claim.

1. `HTTP_502_THEN_REMOTE_404`: the overnight partition attempt created nine UWS jobs; eight encountered HTTP 502 pressure and were later missing at their recorded phase URLs (HTTP 404), one was deadline-aborted, and zero result CSVs landed.
2. `HTTP_200_BUT_SCHEDULER_PENDING`: the morning endpoint preflight answered HTTP 200 in `0.508021` seconds, yet three accepted jobs stayed `PENDING` for 2700 seconds with zero scheduler progress and zero result CSVs.

Operational lesson: endpoint HTTP 200 proves reachability, not scheduler throughput. Multiple stationary `PENDING` jobs are queue saturation, not completed work. The standalone pattern record is `SERVICE_STALL_PATTERN_20260814.json`, SHA-256 `{sha(CANARY / 'SERVICE_STALL_PATTERN_20260814.json')}`.

## Custody hashes

- launch authorization: `{sha(CANARY / 'LAUNCH_AUTHORIZATION.json')}`;
- submission record: `{sha(CANARY / 'submission.json')}`;
- guard lifecycle: `{sha(CANARY / 'guard_lifecycle.json')}`;
- initial PENDING snapshot: `{sha(CANARY / 'INITIAL_POLL_SNAPSHOT_20260814.json')}`;
- executed submitter: `{sha(CANARY / 'executed_code_custody/run_footprint_variance_canary.py.txt')}`;
- executed GET-only monitor: `{sha(CANARY / 'executed_code_custody/monitor_footprint_variance_canary.py.txt')}`;
- 45-minute queue-watch: `{sha(RERUN / 'queue_watch.json')}`;
- 45-minute final outcome: `{sha(RERUN / 'FINAL_OUTCOME_20260814_RERUN.json')}`;
- preserved global-attempt receipt: `{sha(GLOBAL_ATTEMPT)}`;
- preserved partition-attempt receipt: `{sha(PARTITION_ATTEMPT)}`;
- unresolved variance receipt, unchanged: `{sha(VARIANCE_RECEIPT)}`.

## Scientific status and boundary

This canary does not resolve the full-footprint statistic unless all 67 disjoint partitions eventually land and recombine exactly. A canary result, if returned, is labelled **PARTIAL**. It must not be presented as the full footprint or compared with the preregistered `0.15` threshold as a final verdict.

Current scientific status remains:

- `mean(cos theta)`: **UNMEASURED FOR FULL FOOTPRINT**;
- population `var(cos theta)`: **UNMEASURED FOR FULL FOOTPRINT**;
- threshold verdict: **NONE**;
- variance receipt superseded by canary: **NO**.

Boundary ledger:

- UWS canary submissions: **1**;
- replacement submissions: **0**;
- full-manifest auto-launches: **0**;
- aggregate result rows currently landed: **{1 if landed else 0}**;
- object rows exported: **0**;
- positions exported: **0**;
- images requested: **0**;
- chirality computed: **0**;
- handedness, spin, or CW/CCW fields joined or referenced: **0**;
- angle bins or sky maps: **0**;
- dipole amplitude computed: **0**;
- publication/acceptance/commit/push: **0**.

## Exact next action

Let the one GET-only monitor observe this job. On `EXECUTING` or `COMPLETED`, report and stop; Duho decides whether and when to authorize a full run. On three hours still pending, report and leave the canary parked. This receipt grants no automatic full-manifest launch.
"""
    OUTPUT.write_text(md)
    print(f"rendered={OUTPUT} canary_state={state_text} variance=UNRESOLVED full_auto_launches=0")


if __name__ == "__main__":
    main()
