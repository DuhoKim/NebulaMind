#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
SCOPE = ROOT / "footprint_variance_20260813"
RUN = SCOPE / "run"
QUERY_SOURCE = SCOPE / "query.adql"
OUTPUT = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
ORDINARY_GUARD = ROOT / "run_aggregate_tap.py"
EXPECTED_QUERY_SHA256 = "5d4c7812331419eff0ec7dca4e40f690203cb94cc71b6309d7b8694299249ff1"
EXPECTED_COUNT = 832393
EXPECTED_COLUMNS = ["n_cut6_dered", "mean_cos_theta", "var_pop_cos_theta"]
EXPECTED_INPUTS = {
    PREREG / "TORI_SURVEY_ROUTE_BINDING_20260812.md": "3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87",
    PREREG / "TORI_CUT6_INCLINATION_COUNT_20260812.md": "ed6b6e5e957903473c7692d5973f3b2d05a991916ce3aa247365938b0f414651",
    PREREG / "TORI_FULL_KEYSPACE_SWEEP_20260813.md": "9d62960718b4f7aa1bb2eb67a9fddb83d6712698e1bc323fb1d21d1f4965e020",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for path, digest in EXPECTED_INPUTS.items():
        if not path.exists() or sha(path) != digest:
            raise RuntimeError(f"frozen input missing or changed: {path}")
    for path in (QUERY_SOURCE, RUN / "query.adql", RUN / "submission.json", RUN / "job.xml", RUN / "result.csv", RUN / "receipt.json", RUN / "guard_lifecycle.json", RUN / "execution_runner.py.txt"):
        if not path.exists():
            raise RuntimeError(f"missing custody artifact: {path}")
    if sha(QUERY_SOURCE) != EXPECTED_QUERY_SHA256 or sha(RUN / "query.adql") != EXPECTED_QUERY_SHA256:
        raise RuntimeError("query hash drift")
    if QUERY_SOURCE.read_bytes() != RUN.joinpath("query.adql").read_bytes():
        raise RuntimeError("source/executed query mismatch")

    submission = json.loads(RUN.joinpath("submission.json").read_text())
    machine = json.loads(RUN.joinpath("receipt.json").read_text())
    lifecycle = json.loads(RUN.joinpath("guard_lifecycle.json").read_text())
    rows = list(csv.DictReader(RUN.joinpath("result.csv").read_text().splitlines()))
    if len(rows) != 1 or list(rows[0]) != EXPECTED_COLUMNS:
        raise RuntimeError("result must be one exact aggregate row")
    n = int(rows[0]["n_cut6_dered"])
    mean_text = rows[0]["mean_cos_theta"]
    variance_text = rows[0]["var_pop_cos_theta"]
    mean = float(mean_text)
    variance = float(variance_text)
    if n != EXPECTED_COUNT or machine["population_count_returned"] != EXPECTED_COUNT:
        raise RuntimeError("Cut-6 population mismatch")
    if not (math.isfinite(mean) and -1 <= mean <= 1 and math.isfinite(variance) and 0 <= variance <= 1):
        raise RuntimeError("invalid moments")
    if machine["threshold_met"] is not (variance >= 0.15):
        raise RuntimeError("threshold verdict mismatch")
    if submission["submission_attempts"] != 1 or submission["submission_limit"] != 1:
        raise RuntimeError("one-submission contract violated")
    if lifecycle.get("exception_state") != "CLOSED" or not lifecycle.get("ordinary_guard_unchanged") or not lifecycle.get("ordinary_guard_verified_rejects_query_after"):
        raise RuntimeError("guard not closed/restored")
    if not lifecycle.get("exception_runner_disabled"):
        raise RuntimeError("one-time exception runner remains enabled")
    if lifecycle.get("ordinary_guard_sha256_after") != sha(ORDINARY_GUARD):
        raise RuntimeError("ordinary guard post-run drift")
    if lifecycle.get("exception_runner_execution_sha256") != sha(RUN / "execution_runner.py.txt"):
        raise RuntimeError("execution runner custody mismatch")

    verdict = "PASS" if variance >= 0.15 else "FAIL"
    interpretation = (
        "The measured Cut-6 footprint has the preregistered minimum spread around Longo's axis. This closes only Kun's geometry requirement; it is not a handedness or dipole result."
        if variance >= 0.15
        else
        "The measured Cut-6 footprint does not support the test as designed. This is the finding; the population, axis, or threshold is not changed or reframed."
    )
    query_text = RUN.joinpath("query.adql").read_text().rstrip()
    md = f"""# TORI — Longo-axis footprint-variance receipt

**Status:** COMPLETE NARROW ONE-QUERY GEOMETRY EXCEPTION  
**Completed UTC:** `{machine['completed_utc']}`  
**Kun BS-1 variance verdict: {verdict}.**  
Requirement: `var(cos theta) >= 0.15`.

## Result

| Aggregate moment | Returned value |
|---|---:|
| Cut-6 rows contributing a finite/non-null `cos(theta)` | {n:,} |
| `mean(cos theta)` | `{mean_text}` |
| population `var(cos theta)` | `{variance_text}` |
| threshold | `0.15` |
| threshold met | **{'YES' if variance >= 0.15 else 'NO'}** |

{interpretation}

The returned contributing count equals the independently certified exact full-keyspace dered Cut-6 count, `{EXPECTED_COUNT:,}`. No coordinate-validity predicate was added to redefine the population; `COUNT(cos_theta)` proves that every selected Cut-6 row contributed to the moments.

## Exact population definition

The population is the frozen **dered Cut-6** population over the documented full catalogue keyspace `BRICKID 1…662174`:

1. `brick_primary = 1`;
2. `maskbits = 0`;
3. `type <> 'PSF'`;
4. `flux_r > 0`;
5. photo-z left join on `(ls_id, release, brickid, objid)`;
6. `0 <= z_phot_median < 0.15`;
7. `dered_mag_r < 17.7`;
8. `shape_r > 1.5`;
9. `POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551`, the frozen `b/a > 0.4` Cut 6.

Population custody:

- `TORI_FULL_KEYSPACE_SWEEP_20260813.md` — SHA-256 `{EXPECTED_INPUTS[PREREG / 'TORI_FULL_KEYSPACE_SWEEP_20260813.md']}`; exact dered Cut-6 count `{EXPECTED_COUNT:,}` with direct zero-tail closure.
- `TORI_CUT6_INCLINATION_COUNT_20260812.md` — SHA-256 `{EXPECTED_INPUTS[PREREG / 'TORI_CUT6_INCLINATION_COUNT_20260812.md']}`; frozen Cut-6 predicate and initial fixed-range receipt.
- `TORI_SURVEY_ROUTE_BINDING_20260812.md` — SHA-256 `{EXPECTED_INPUTS[PREREG / 'TORI_SURVEY_ROUTE_BINDING_20260812.md']}`; DR10.1 South route, catalogue records, joins, and Longo-axis transform custody.

Where catalogue coverage is mentioned, **BRICKID keyspace is not sky area**. The full count certificate directly measured `BRICKID 1…541000` (81.700580% of keyspace) and separately proved the remaining keyspace tail contained zero joined parent rows. This variance is computed over selected object positions; it is not inferred from keyspace percentage.

## Axis and statistic

- Frozen Longo axis: Galactic `(l,b) = (52°, 68.5°)`.
- Astropy 6.0.1 Galactic-to-ICRS transform reproduced: `(RA,Dec) = (216.98443429552697°, 32.060611193471175°)`.
- ICRS unit vector used in the query: `(-0.6769717798726208, -0.5098465358556549, 0.5308160878610257)`.
- Per selected object, `cos(theta)` is the dot product of its ICRS sky-position unit vector and that fixed axis vector.
- Server-side population variance: `AVG(cos_theta^2) - POWER(AVG(cos_theta),2)`.
- Only the count, mean, and population variance were returned.

This is a survey-geometry adequacy check. It reveals the selected footprint's angular spread relative to one preregistered axis. It cannot reveal chirality, handedness, CW/CCW labels, a dipole amplitude, or any signal because none of those fields or quantities enters the query.

## Narrow exception and guard lifecycle

Authorization recorded: Duho authorized one server-side aggregate computation over the exact Cut-6 population, relayed by the user in this session. The repeated authorization text was treated as one permission, not two.

- ordinary counts-only guard before: SHA-256 `{lifecycle['ordinary_guard_sha256_before']}`; verified to reject the exact variance query;
- exception state opened: `{lifecycle['opened_utc']}`;
- authorized query hash: `{EXPECTED_QUERY_SHA256}`;
- submission attempts / limit: `{lifecycle['submission_attempts']}/{lifecycle['submission_limit']}`;
- one-time execution runner preserved as non-`.py` custody text: SHA-256 `{lifecycle['exception_runner_execution_sha256']}`;
- exception state closed: `{lifecycle['closed_utc']}`;
- ordinary guard after: SHA-256 `{lifecycle['ordinary_guard_sha256_after']}`;
- ordinary guard unchanged: **{'YES' if lifecycle['ordinary_guard_unchanged'] else 'NO'}**;
- ordinary guard restored and verified: **YES**;
- one-time exception runner disabled: **YES**; disabled stub SHA-256 `{lifecycle['exception_runner_disabled_sha256']}`;
- exception state: **CLOSED**.

The normal runner was never weakened. It rejected this query before submission and rejects it after closure. The separate exact-hash exception path is now fail-closed and cannot submit again.

## UWS job and immutable artifact custody

- endpoint: `{machine['endpoint']}`;
- job: `{machine['job_url']}`;
- result URL: `{machine['result_url']}`;
- submitted UTC: `{machine['started_utc']}`;
- completed UTC: `{machine['completed_utc']}`;
- terminal phase: `COMPLETED`;
- query SHA-256: `{EXPECTED_QUERY_SHA256}`;
- result SHA-256: `{sha(RUN / 'result.csv')}`;
- job XML SHA-256: `{sha(RUN / 'job.xml')}`;
- submission record SHA-256: `{sha(RUN / 'submission.json')}`;
- machine receipt SHA-256: `{sha(RUN / 'receipt.json')}`;
- guard lifecycle receipt SHA-256: `{sha(RUN / 'guard_lifecycle.json')}`.

## Exact executed query

```adql
{query_text}
```

## Boundary ledger

- aggregate result rows returned: **1**
- sample rows exported: **0**
- positions exported: **0**
- images requested: **0**
- chirality computed: **0**
- handedness joined or referenced: **0**
- CW/CCW labels joined or referenced: **0**
- dipole amplitude computed: **0**
- directional outputs beyond count/mean/variance: **0**
- sky maps or angular bins: **0**
- publication/acceptance/commit/push: **0**

Nothing in this receipt authorizes a real handedness run, publication, acceptance, commit, or push.
"""
    OUTPUT.write_text(md)
    print(f"rendered={OUTPUT} variance={variance_text} verdict={verdict}")


if __name__ == "__main__":
    main()
