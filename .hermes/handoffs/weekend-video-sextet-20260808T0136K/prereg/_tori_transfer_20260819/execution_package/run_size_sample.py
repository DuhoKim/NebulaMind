#!/usr/bin/env python3
"""Run and receipt the frozen §11.4d HEAD-only size sample.

Sampling rule implemented from TORI_ROUTE_BINDING_SUCCESSOR_20260817.md
§5.1.1/§11.4d: exactly 1,024 manifest-listed image URLs, stratified across
all AAA values. The binding does not specify stratum allocation or within-
stratum selection, so this script gives every AAA stratum one sample, assigns
the remaining slots by Hamilton proportional allocation, and uses seeded
uniform sampling without replacement inside each stratum.

Ceiling arithmetic, exactly from §5.1.1.2:
  sample_mean = sum(content_length) / valid_size_observation_count
  unrounded_ceiling = sample_mean * 60_308 * 1.25
                      = sum(content_length) * 60_308 * 5
                        / (valid_size_observation_count * 4)
  approved_byte_ceiling = ceil(unrounded_ceiling)
The integer ceiling rounds upward so enforcement cannot understate the frozen
formula by a fractional byte.
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import random
import subprocess
import tempfile
import time
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from zoneinfo import ZoneInfo

SAMPLE_COUNT = 1_024
REQUIRED_FILE_COUNT = 60_308
SEED = 20_260_819
MIN_START_SPACING_SECONDS = 1.0
MAX_NON_200 = math.floor(SAMPLE_COUNT * 0.01)  # 10; the 11th is >1%.
EXPECTED_MANIFEST_SHA256 = "ff75636cf8fe14f14bcd35721491cbdf225d31d706325c114ecba4e91cf0dde2"
EXPECTED_BINDING_SHA256 = "1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b"
PACKAGE_DIR = Path(__file__).resolve().parent
PREREG_DIR = PACKAGE_DIR.parent.parent
MANIFEST = PACKAGE_DIR.parent / "candidate_image_manifest.jsonl"
BINDING = PREREG_DIR / "TORI_ROUTE_BINDING_SUCCESSOR_20260817.md"
PLAN = PACKAGE_DIR / "size_sample_plan.json"
RECEIPTS = PACKAGE_DIR / "receipts.jsonl"
SUMMARY = PACKAGE_DIR / "SIZE_SAMPLE_SUMMARY.json"
LOCK = PACKAGE_DIR / ".size_sample.lock"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def in_window() -> bool:
    pacific = datetime.now(ZoneInfo("America/Los_Angeles"))
    return pacific.weekday() >= 5 or pacific.hour >= 20 or pacific.hour < 8


def atomic_json(path: Path, value: object) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(value, f, indent=2, sort_keys=True)
        f.write("\n")
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def append_receipt(value: dict) -> None:
    line = json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"
    fd = os.open(RECEIPTS, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        os.write(fd, line.encode("utf-8"))
        os.fsync(fd)
    finally:
        os.close(fd)


def load_manifest() -> list[dict]:
    if sha256(BINDING) != EXPECTED_BINDING_SHA256 or (BINDING.stat().st_mode & 0o777) != 0o444:
        raise SystemExit("HOLD: frozen binding hash or mode mismatch")
    if sha256(MANIFEST) != EXPECTED_MANIFEST_SHA256:
        raise SystemExit("HOLD: candidate manifest hash mismatch")
    rows = [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines()]
    if len(rows) != REQUIRED_FILE_COUNT:
        raise SystemExit(f"HOLD: manifest row count {len(rows)} != {REQUIRED_FILE_COUNT}")
    if len({r["source_url"] for r in rows}) != REQUIRED_FILE_COUNT:
        raise SystemExit("HOLD: manifest source URLs are not unique")
    return rows


def hamilton_allocation(groups: dict[str, list[dict]]) -> dict[str, int]:
    """One per AAA, then Hamilton-allocate remaining slots by stratum size."""
    keys = sorted(groups)
    if len(keys) > SAMPLE_COUNT:
        raise SystemExit("HOLD: more AAA strata than sample slots")
    allocation = {key: 1 for key in keys}
    remaining = SAMPLE_COUNT - len(keys)
    total_weight = sum(len(groups[key]) for key in keys)
    quotas = {key: Fraction(remaining * len(groups[key]), total_weight) for key in keys}
    for key in keys:
        allocation[key] += quotas[key].numerator // quotas[key].denominator
    leftovers = SAMPLE_COUNT - sum(allocation.values())
    ranked = sorted(
        keys,
        key=lambda key: (-(quotas[key] - int(quotas[key])), key),
    )
    for key in ranked[:leftovers]:
        allocation[key] += 1
    if sum(allocation.values()) != SAMPLE_COUNT:
        raise AssertionError("allocation does not total 1,024")
    if any(allocation[key] > len(groups[key]) for key in keys):
        raise SystemExit("HOLD: stratum allocation exceeds population")
    return allocation


def build_plan(rows: list[dict]) -> dict:
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        groups[row["aaa"]].append(row)
    allocation = hamilton_allocation(groups)
    rng = random.Random(SEED)
    selected: dict[str, list[dict]] = {}
    for aaa in sorted(groups):
        selected[aaa] = sorted(rng.sample(groups[aaa], allocation[aaa]), key=lambda r: r["brickname"])
    ordered: list[dict] = []
    for round_index in range(max(allocation.values())):
        for aaa in sorted(selected):
            if round_index < len(selected[aaa]):
                row = selected[aaa][round_index]
                ordered.append({
                    "sample_index": len(ordered),
                    "aaa": aaa,
                    "brickname": row["brickname"],
                    "url": row["source_url"],
                })
    plan = {
        "binding_sha256": EXPECTED_BINDING_SHA256,
        "manifest_path": str(MANIFEST),
        "manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "manifest_rows": len(rows),
        "sample_count": SAMPLE_COUNT,
        "seed": SEED,
        "sampling_rule": "all-AAA stratified: one per AAA, remaining slots Hamilton proportional by stratum population; seeded uniform without replacement within stratum; round-robin request order across AAA",
        "aaa_strata": len(groups),
        "allocation": allocation,
        "requests": ordered,
    }
    return plan


def load_or_create_plan(rows: list[dict]) -> dict:
    expected = build_plan(rows)
    if PLAN.exists():
        actual = json.loads(PLAN.read_text(encoding="utf-8"))
        if actual != expected:
            raise SystemExit("HOLD: existing sample plan differs from deterministic reconstruction")
        return actual
    atomic_json(PLAN, expected)
    return expected


def parse_last_headers(raw: str) -> dict[str, str]:
    blocks = [block for block in raw.replace("\r\n", "\n").split("\n\n") if block.strip()]
    if not blocks:
        return {}
    lines = blocks[-1].splitlines()
    headers: dict[str, str] = {}
    for line in lines[1:]:
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip().lower()] = value.strip()
    return headers


def request_head(url: str) -> tuple[int, dict[str, str], int, str, int]:
    with tempfile.NamedTemporaryFile(prefix="head-", suffix=".headers", dir=PACKAGE_DIR, delete=False) as tf:
        header_path = Path(tf.name)
    command = [
        "/usr/bin/curl", "--disable", "--globoff", "--silent", "--show-error",
        "--head", "--http1.1", "--proxy", "", "--proto", "=https",
        "--connect-timeout", "30", "--max-time", "120", "--output", "/dev/null",
        "--dump-header", str(header_path),
        "--write-out", "%{http_code}\t%{ssl_verify_result}",
        url,
    ]
    env = os.environ.copy()
    for key in list(env):
        if key.lower() in {"http_proxy", "https_proxy", "all_proxy", "no_proxy"}:
            env.pop(key, None)
    try:
        proc = subprocess.run(command, capture_output=True, text=True, env=env, check=False)
        raw_headers = header_path.read_text(encoding="iso-8859-1")
    finally:
        header_path.unlink(missing_ok=True)
    status = 0
    ssl_verify_result = -1
    parts = proc.stdout.strip().split("\t")
    if parts and parts[0].isdigit():
        status = int(parts[0])
    if len(parts) > 1 and parts[1].lstrip("-").isdigit():
        ssl_verify_result = int(parts[1])
    return status, parse_last_headers(raw_headers), proc.returncode, proc.stderr.strip(), ssl_verify_result


def load_receipts(plan: dict) -> list[dict]:
    if not RECEIPTS.exists():
        return []
    receipts = [json.loads(line) for line in RECEIPTS.read_text(encoding="utf-8").splitlines()]
    for index, receipt in enumerate(receipts):
        expected = plan["requests"][index]
        if receipt["sample_index"] != index or receipt["url"] != expected["url"]:
            raise SystemExit(f"HOLD: receipt/plan contradiction at index {index}")
        if receipt.get("method") != "HEAD" or receipt.get("body_bytes") != 0:
            raise SystemExit(f"HOLD: non-HEAD or nonzero-body receipt at index {index}")
    if len(receipts) > SAMPLE_COUNT:
        raise SystemExit("HOLD: more than 1,024 receipts")
    return receipts


def derive(plan: dict, receipts: list[dict]) -> dict:
    if len(receipts) != SAMPLE_COUNT:
        raise SystemExit(f"HOLD: cannot derive before 1,024 receipts; have {len(receipts)}")
    non_200 = sum(r["status"] != 200 for r in receipts)
    if non_200 > MAX_NON_200:
        raise SystemExit(f"HOLD: non-200 count {non_200} exceeds 1% threshold")
    sizes = [r["content-length"] for r in receipts if r["status"] == 200 and isinstance(r["content-length"], int)]
    if not sizes:
        raise SystemExit("HOLD: no valid HTTP-200 Content-Length observations")
    total = sum(sizes)
    n = len(sizes)
    mean = Fraction(total, n)
    unrounded = mean * REQUIRED_FILE_COUNT * Fraction(5, 4)
    ceiling = (unrounded.numerator + unrounded.denominator - 1) // unrounded.denominator
    if n > 1:
        sample_variance = sum((size - float(mean)) ** 2 for size in sizes) / (n - 1)
        standard_error = math.sqrt(sample_variance / n)
    else:
        standard_error = None
    starts = [r["request_start_epoch"] for r in receipts]
    spacings = [starts[i] - starts[i - 1] for i in range(1, len(starts))]
    result = {
        "status": "COMPLETE",
        "binding_sha256": EXPECTED_BINDING_SHA256,
        "manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "plan_sha256": sha256(PLAN),
        "receipts_sha256": sha256(RECEIPTS),
        "sample_count": SAMPLE_COUNT,
        "http_200": SAMPLE_COUNT - non_200,
        "non_200": non_200,
        "non_200_fraction": non_200 / SAMPLE_COUNT,
        "valid_size_observation_count": n,
        "content_length_sum_bytes": total,
        "sample_mean_bytes_exact": f"{mean.numerator}/{mean.denominator}",
        "sample_mean_bytes_decimal": float(mean),
        "sample_standard_error_bytes": standard_error,
        "ceiling_formula": "ceil((content_length_sum / valid_size_observation_count) * 60308 * 1.25)",
        "ceiling_unrounded_exact": f"{unrounded.numerator}/{unrounded.denominator}",
        "ceiling_unrounded_decimal": float(unrounded),
        "approved_byte_ceiling": ceiling,
        "minimum_observed_start_spacing_seconds": min(spacings) if spacings else None,
        "required_minimum_start_spacing_seconds": MIN_START_SPACING_SECONDS,
        "body_bytes_transferred": sum(r["body_bytes"] for r in receipts),
        "completed_utc": utc_now(),
    }
    atomic_json(SUMMARY, result)
    return result


def run() -> None:
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    with LOCK.open("a+") as lock_file:
        fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        rows = load_manifest()
        plan = load_or_create_plan(rows)
        receipts = load_receipts(plan)
        if len(receipts) == SAMPLE_COUNT:
            print(json.dumps(derive(plan, receipts), sort_keys=True))
            return
        non_200 = sum(r["status"] != 200 for r in receipts)
        if non_200 > MAX_NON_200:
            raise SystemExit(f"HOLD: prior non-200 count {non_200} exceeds 1% threshold")
        last_start_epoch = receipts[-1]["request_start_epoch"] if receipts else None
        last_start_monotonic = None
        for request in plan["requests"][len(receipts):]:
            if not in_window():
                raise SystemExit("HOLD: outside frozen Pacific retrieval window")
            if last_start_monotonic is not None:
                delay = MIN_START_SPACING_SECONDS - (time.monotonic() - last_start_monotonic)
                if delay > 0:
                    time.sleep(delay)
            elif last_start_epoch is not None:
                delay = MIN_START_SPACING_SECONDS - (time.time() - last_start_epoch)
                if delay > 0:
                    time.sleep(delay)
            start_monotonic = time.monotonic()
            start_epoch = time.time()
            started_utc = utc_now()
            status, headers, curl_exit, curl_stderr, ssl_verify_result = request_head(request["url"])
            content_length_raw = headers.get("content-length")
            content_length = int(content_length_raw) if content_length_raw and content_length_raw.isdigit() else None
            receipt = {
                "sample_index": request["sample_index"],
                "aaa": request["aaa"],
                "brickname": request["brickname"],
                "method": "HEAD",
                "url": request["url"],
                "status": status,
                "content-length": content_length,
                "last-modified": headers.get("last-modified"),
                "content-type": headers.get("content-type"),
                "body_bytes": 0,
                "request_start_utc": started_utc,
                "request_start_epoch": start_epoch,
                "request_elapsed_seconds": time.monotonic() - start_monotonic,
                "spacing_from_previous_start_seconds": None if last_start_epoch is None else start_epoch - last_start_epoch,
                "curl_exit": curl_exit,
                "curl_stderr": curl_stderr or None,
                "ssl_verify_result": ssl_verify_result,
                "pacing_minimum_seconds": MIN_START_SPACING_SECONDS,
            }
            append_receipt(receipt)
            receipts.append(receipt)
            last_start_monotonic = start_monotonic
            last_start_epoch = start_epoch
            if status != 200:
                non_200 += 1
                if non_200 > MAX_NON_200:
                    raise SystemExit(f"HOLD: non-200 count reached {non_200}, irreversibly >1% of 1,024")
        print(json.dumps(derive(plan, receipts), sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--derive-only", action="store_true")
    args = parser.parse_args()
    rows = load_manifest()
    plan = load_or_create_plan(rows)
    receipts = load_receipts(plan)
    if args.derive_only:
        print(json.dumps(derive(plan, receipts), indent=2, sort_keys=True))
    else:
        run()


if __name__ == "__main__":
    main()
