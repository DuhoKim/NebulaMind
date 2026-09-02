#!/usr/bin/env python3
"""Draft V9 Tier-C freeze-time seal gate.  It never opens image pixels."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

ZERO_DIGEST = "0" * 64
EXPECTED_BLOB_ID = "df704bed1c5fd872cf9dee9f4be2e88f64bb94a0"
SHA_RE = re.compile(rb"^([0-9a-f]{64})[ \t]+(?:\*)?(\S+)[ \t]*$")
ACQUISITION_KEYS = {
    "brick", "bytes", "computed_sha256", "published_sha256", "url", "utc", "verdict"
}
BASE = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd"


class GateFailure(Exception):
    pass


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_bytes(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode() + b"\n"


# V9 §7.11 line 215: "For the seal check, no fallback name is allowed: … the
# fetched filename MUST be `legacysurvey_dr10_south_coadd_<AAA>_<brick>.sha256sum`
# at the §2.14 URL."
def checksum_url(brick: str) -> str:
    aaa = brick[:3]
    name = f"legacysurvey_dr10_south_coadd_{aaa}_{brick}.sha256sum"
    return f"{BASE}/{aaa}/{brick}/{name}"


def network_fetcher(url: str, timeout: float) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "NebulaMind-seal-gate-draft/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def _manifest_entries(path: Path) -> list[tuple[str, str]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise GateFailure("manifest_not_list")
    result = []
    for item in raw:
        if isinstance(item, str):
            brick = item
            filename = f"legacysurvey-{brick}-image-r.fits.fz"
        elif isinstance(item, dict):
            brick = item.get("brick") or item.get("brickname")
            rel = item.get("relative_path") or item.get("path")
            filename = Path(rel).name if isinstance(rel, str) else f"legacysurvey-{brick}-image-r.fits.fz"
        else:
            raise GateFailure("malformed_manifest_record")
        if not isinstance(brick, str) or not brick or not isinstance(filename, str):
            raise GateFailure("malformed_manifest_record")
        result.append((brick, filename))
    bricks = [entry[0] for entry in result]
    if len(set(bricks)) != len(bricks):
        raise GateFailure("duplicate_manifest_brick")
    return result


def _journal(path: Path) -> tuple[list[dict], bytes]:
    raw = path.read_bytes()
    lines = raw.splitlines()
    records = []
    for line in lines:
        try:
            record = json.loads(line)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise GateFailure("malformed_journal") from exc
        if not isinstance(record, dict) or set(record) != ACQUISITION_KEYS:
            raise GateFailure("malformed_journal_schema")
        records.append(record)
    return records, raw


def process_running() -> bool:
    proc = subprocess.run(["ps", "ax", "-o", "pid=,args="], capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise GateFailure("process_check_failed")
    needle = re.compile(r"fetch_bricks[.]py --manifest(?:\s|$)")
    return any(needle.search(line) and not line.lstrip().startswith(str(os.getpid()) + " ")
               for line in proc.stdout.splitlines())


def _git_custody(live: Path, pinned: Path, expected_blob_id: str,
                 git_runner: Callable[..., subprocess.CompletedProcess]) -> dict:
    ls = git_runner(["git", "ls-files", "-s", "--", str(live)], capture_output=True)
    text = ls.stdout.decode() if isinstance(ls.stdout, bytes) else ls.stdout
    match = re.fullmatch(r"100644 ([0-9a-f]{40,64}) 0\t.+\n?", text or "")
    if ls.returncode != 0 or not match:
        raise GateFailure("git_ls_files_mismatch")
    blob_id = match.group(1)
    if blob_id != expected_blob_id:
        raise GateFailure("git_blob_id_mismatch")
    cat = git_runner(["git", "cat-file", "-p", blob_id], capture_output=True)
    if cat.returncode != 0:
        raise GateFailure("git_blob_unreadable")
    blob_bytes = cat.stdout.encode() if isinstance(cat.stdout, str) else cat.stdout
    diff = git_runner(["git", "diff", "--quiet", "--", str(live)], capture_output=True)
    values = {
        "git_blob_id": blob_id,
        "git_blob_content_sha256": sha256_bytes(blob_bytes),
        "live_file_sha256": sha256_file(live),
        "pinned_copy_sha256": sha256_file(pinned),
        "git_diff_quiet_exit": diff.returncode,
    }
    if len({values["git_blob_content_sha256"], values["live_file_sha256"], values["pinned_copy_sha256"]}) != 1:
        values.update(passed=False, failure="git_custody_digest_mismatch")
    elif diff.returncode != 0:
        values.update(passed=False, failure="git_worktree_dirty")
    else:
        values.update(passed=True, failure=None)
    return values


def _seal_predecessor(path: Path) -> str:
    if not path.exists() or path.stat().st_size == 0:
        return ZERO_DIGEST
    try:
        raw = path.read_bytes()
        lines = raw.splitlines(keepends=True)
        if not lines or any(not line.strip() for line in lines):
            raise ValueError("empty seal-journal record")
        last_line = lines[-1]
        record = json.loads(last_line)
        if not isinstance(record, dict) or not isinstance(record.get("receipt_digest"), str):
            raise ValueError("invalid seal-journal record")
        if last_line != canonical_bytes(record):
            raise ValueError("non-canonical seal-journal record")
        body = dict(record)
        recorded_digest = body.pop("receipt_digest")
        if recorded_digest != sha256_bytes(canonical_bytes(body)):
            raise ValueError("seal-journal receipt digest mismatch")
        return recorded_digest
    except Exception as exc:
        if isinstance(exc, GateFailure):
            raise
        raise GateFailure("seal_journal_chain_broken") from exc


def _published_line(payload: bytes, wanted_filename: str) -> tuple[bytes, str]:
    hits = []
    for raw_line in payload.splitlines():
        match = SHA_RE.fullmatch(raw_line)
        if match and match.group(2).decode("utf-8", "strict") == wanted_filename:
            hits.append((raw_line.rstrip(b"\r\n") + b"\n", match.group(1).decode()))
    if len(hits) != 1:
        raise GateFailure("missing_or_malformed_checksum_line")
    return hits[0]


def run_gate(*, manifest: Path, journal: Path, bricks_dir: Path, live_script: Path,
             pinned_copy: Path, seal_journal: Path, expected_manifest_count: int = 17947,
             expected_blob_id: str = EXPECTED_BLOB_ID,
             fetch: bool = False, fetcher: Callable[[str, float], bytes] | None = None,
             timeout: float = 30.0, delay: float = 0.0,
             process_checker: Callable[[], bool] = process_running,
             git_runner: Callable[..., subprocess.CompletedProcess] = subprocess.run,
             timestamp: str | None = None) -> dict:
    timestamp = timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    counts = {"manifest_count": 0, "files_checked": 0, "mismatches": 0,
              "receipt_count": 0, "published_checksum_disagreements": 0,
              "published_checksum_refetch_complete": False}
    observed = {}
    expected = {"brick_file_sha256": "fresh NERSC published SHA-256",
                "receipt_sha256_values": "fresh NERSC published SHA-256",
                "git_blob_live_pin_sha256": "identical"}
    expected_counts = {"manifest_count": expected_manifest_count, "mismatches": 0,
                       "published_checksum_disagreements": 0}
    status, verdict, failure = "PASS", "PASS", None
    acquisition_completion = False
    git_custody = {"passed": False}
    predecessor_digest = ZERO_DIGEST
    try:
        predecessor_digest = _seal_predecessor(seal_journal)
        entries = _manifest_entries(manifest)
        counts["manifest_count"] = len(entries)
        if len(entries) != expected_manifest_count:
            raise GateFailure("manifest_count_mismatch")
        records, journal_raw = _journal(journal)
        counts["receipt_count"] = len(records)
        observed["journal_head_sha256"] = sha256_bytes(journal_raw)
        by_brick: dict[str, list[tuple[int, dict]]] = {}
        for index, record in enumerate(records):
            by_brick.setdefault(record.get("brick"), []).append((index, record))
            if record["verdict"] == "OK" and record["computed_sha256"] != record["published_sha256"]:
                raise GateFailure("ok_receipt_digest_mismatch")
        manifest_bricks = {brick for brick, _ in entries}
        ok_bricks = {brick for brick, rows in by_brick.items() if any(r["verdict"] == "OK" for _, r in rows)}
        if ok_bricks != manifest_bricks:
            raise GateFailure("acquisition_set_incomplete")
        for rows in by_brick.values():
            ok_indices = [i for i, row in rows if row["verdict"] == "OK"]
            if any(row["verdict"] != "OK" and not any(j > i for j in ok_indices) for i, row in rows):
                raise GateFailure("non_ok_without_later_ok")
        final_ok = {}
        for brick in manifest_bricks:
            rows = by_brick[brick]
            final_ok[brick] = next(row for _, row in reversed(rows) if row["verdict"] == "OK")
        if process_checker():
            raise GateFailure("acquisition_process_running")
        acquisition_completion = True
        git_custody = _git_custody(live_script, pinned_copy, expected_blob_id, git_runner)
        if not git_custody["passed"]:
            raise GateFailure(git_custody["failure"])
        if not fetch:
            raise GateFailure("published_checksum_refetch_not_requested")
        fetcher = fetcher or network_fetcher
        wanted_files = {filename for _, filename in entries}
        actual_files = {p.name for p in bricks_dir.iterdir() if p.is_file()}
        if actual_files - wanted_files:
            counts["mismatches"] += len(actual_files - wanted_files)
            raise GateFailure("extra_brick_file")
        bound_lines = []
        for position, (brick, filename) in enumerate(entries):
            try:
                payload = fetcher(checksum_url(brick), timeout)
                line, published = _published_line(payload, filename)
            except Exception as exc:
                if isinstance(exc, GateFailure):
                    raise
                raise GateFailure(
                    f"published_checksum_fetch_failed: {type(exc).__name__}: {exc}"
                ) from exc
            bound_lines.append(line)
            receipt = final_ok[brick]
            if receipt["computed_sha256"] != published or receipt["published_sha256"] != published:
                counts["published_checksum_disagreements"] += 1
                raise GateFailure("fresh_published_receipt_disagreement")
            disk_path = bricks_dir / filename
            if not disk_path.is_file():
                counts["mismatches"] += 1
                raise GateFailure("missing_brick_file")
            counts["files_checked"] += 1
            if sha256_file(disk_path) != published:
                counts["mismatches"] += 1
                raise GateFailure("disk_hash_mismatch")
            if delay and position + 1 < len(entries):
                time.sleep(delay)
        observed["published_checksum_lines_sha256"] = sha256_bytes(b"".join(bound_lines))
        counts["published_checksum_refetch_complete"] = True
    except Exception as exc:
        status, verdict = "REFUSE", "DATA-INTEGRITY-FAIL"
        failure = (str(exc) or type(exc).__name__) if isinstance(exc, GateFailure) else \
            f"{type(exc).__name__}: {exc}"
    data_integrity_pass = bool(
        status == "PASS" and counts["files_checked"] == counts["manifest_count"] == expected_manifest_count
        and counts["mismatches"] == 0 and counts["published_checksum_refetch_complete"]
        and counts["published_checksum_disagreements"] == 0 and git_custody.get("passed")
        and acquisition_completion
    )
    body = {
        "timestamp": timestamp,
        "operation": "tier-c-freeze-time-seal-gate",
        "paths": {"manifest": str(manifest), "journal": str(journal),
                  "seal_journal": str(seal_journal), "bricks_dir": str(bricks_dir),
                  "live_acquisition_script": str(live_script), "pinned_acquisition_copy": str(pinned_copy)},
        "expected_digests": expected,
        "observed_digests": observed,
        "expected_counts": expected_counts,
        "counts": counts,
        "git_custody": git_custody,
        "acquisition_completion_set_condition": acquisition_completion,
        "status": status,
        "verdict": verdict,
        "failure": failure,
        "data_integrity_pass": data_integrity_pass,
        "predecessor_receipt_digest": predecessor_digest,
    }
    body["receipt_digest"] = sha256_bytes(canonical_bytes(body))
    return body


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--bricks-dir", type=Path, required=True)
    parser.add_argument("--live-script", type=Path, required=True)
    parser.add_argument("--pinned-copy", type=Path, required=True)
    parser.add_argument("--seal-journal", type=Path, required=True)
    parser.add_argument("--expected-manifest-count", type=int, default=17947)
    parser.add_argument("--expected-blob-id", default=EXPECTED_BLOB_ID)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--fetch", action="store_true", help="authorize fresh checksum-file network reads")
    parser.add_argument("--append", action="store_true", help="append the receipt to --seal-journal")
    args = parser.parse_args(argv)
    receipt = run_gate(manifest=args.manifest, journal=args.journal, bricks_dir=args.bricks_dir,
                       live_script=args.live_script, pinned_copy=args.pinned_copy,
                       seal_journal=args.seal_journal,
                       expected_manifest_count=args.expected_manifest_count, fetch=args.fetch,
                       expected_blob_id=args.expected_blob_id,
                       timeout=args.timeout, delay=args.delay)
    encoded = canonical_bytes(receipt)
    if args.append:
        try:
            with args.seal_journal.open("ab") as stream:
                stream.write(encoded)
        except Exception as exc:
            receipt["status"] = "REFUSE"
            receipt["verdict"] = "DATA-INTEGRITY-FAIL"
            receipt["failure"] = f"{type(exc).__name__}: {exc}"
            receipt["data_integrity_pass"] = False
            receipt.pop("receipt_digest")
            receipt["receipt_digest"] = sha256_bytes(canonical_bytes(receipt))
            encoded = canonical_bytes(receipt)
    sys.stdout.buffer.write(encoded)
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
