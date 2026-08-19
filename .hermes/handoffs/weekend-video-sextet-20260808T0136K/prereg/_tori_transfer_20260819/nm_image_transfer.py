#!/usr/bin/env python3
"""Fail-closed DR10 South image-r transfer under the frozen route-B binding.

Building, manifest derivation, preflight, and tests are offline. Network transfer is
possible only through the explicit ``run``/``launch`` commands after an external
approval record pins the manifest hash, destination, file count, byte ceiling, and
frozen pacing. No image request is made by import, manifest build, or preflight.
"""
from __future__ import annotations

import argparse
import base64
import binascii
import csv
import fcntl
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable, Mapping, NamedTuple, Protocol, Sequence
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
HARVEST = PREREG / "_tori_harvest_20260817"
WORKING_SET = PREREG / "_tori_r1_workingset_evidence" / "workingset_bricks.csv"
WORKING_SET_SHA256 = "78ee99d6824bf4f5126b9ffd9eb622ad8201df2c64c3f232d99c1791b5f36b74"
EXPECTED_FILE_COUNT = 60_308
BINDING_SHA256 = "1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b"
BINDING_PATH = PREREG / "TORI_ROUTE_BINDING_SUCCESSOR_20260817.md"
CROSSCHECK_GATE = PREREG / "CROSSCHECK_VERDICT_20260819.md"
KUN_CC_GATE = PREREG / "KUN_CC_GATE_20260819.md"
RELEASE = "dr10.1-latest-byte-bound"
MANIFEST_FORMAT_VERSION = "nm-image-transfer-manifest-v1"
BASE_URL = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd"
PORTAL_HOST = "portal.nersc.gov"
PACING_SECONDS = 2.0
BACKOFF_SECONDS = (30.0, 60.0, 120.0)
BANDWIDTH_LIMIT = "25000000"
PACIFIC = ZoneInfo("America/Los_Angeles")
BUILD_PREFLIGHT_BYTES = 700_000_000_000
APPROVAL_STATUS = "APPROVED_FOR_IMAGE_RETRIEVAL"
EXECUTION_ACK = "I_UNDERSTAND_THIS_FETCHES_MANIFESTED_IMAGE_BYTES"
BRICK_RE = re.compile(r"^[0-9]{4}[pm][0-9]{3}$")
SHA_LINE_RE = re.compile(r"^([0-9a-f]{64})[ \t*]+(\S+)$")


class CampaignBlocked(RuntimeError):
    """A terminal custody event stopped the complete campaign."""


class TransportResult(NamedTuple):
    status: int | None
    headers: Mapping[str, str]
    bytes_received: int
    curl_returncode: int
    stderr: str = ""
    tls_peer: Mapping[str, str] | None = None


class Transport(Protocol):
    def fetch(
        self,
        url: str,
        destination: Path,
        *,
        max_bytes: int,
        max_time_seconds: int,
    ) -> TransportResult:
        ...


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256_file(path: Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        while True:
            chunk = source.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def verify_frozen_build_gates() -> None:
    if CROSSCHECK_GATE.read_text().splitlines()[0] != "CROSSCHECK_PASS":
        raise ValueError("crosscheck gate is not CROSSCHECK_PASS")
    if KUN_CC_GATE.read_text().splitlines()[0] != "PASS_CROSSCHECK_GATE":
        raise ValueError("Kun/CC gate is not PASS_CROSSCHECK_GATE")
    if sha256_file(BINDING_PATH) != BINDING_SHA256:
        raise ValueError("frozen successor binding SHA-256 mismatch")
    if BINDING_PATH.stat().st_mode & 0o777 != 0o444:
        raise ValueError("frozen successor binding mode is not 444")


def image_filename(brickname: str) -> str:
    if BRICK_RE.fullmatch(brickname) is None:
        raise ValueError(f"invalid brickname: {brickname!r}")
    return f"legacysurvey-{brickname}-image-r.fits.fz"


def image_url(brickname: str, filename: str | None = None) -> str:
    expected = image_filename(brickname)
    if filename is not None and filename != expected:
        raise ValueError(f"unmanifested product name for {brickname}: {filename!r}")
    aaa = brickname[:3]
    return f"{BASE_URL}/{aaa}/{brickname}/{expected}"


def validate_manifest_record(record: Mapping[str, object]) -> None:
    brick = record.get("brickname")
    if not isinstance(brick, str) or BRICK_RE.fullmatch(brick) is None:
        raise ValueError("manifest has invalid brickname")
    filename = image_filename(brick)
    expected_url = image_url(brick, filename)
    expected_rel = f"coadd/{brick[:3]}/{brick}/{filename}"
    required = {
        "release": RELEASE,
        "aaa": brick[:3],
        "product": "image-r",
        "coverage_class": "required",
        "source_url": expected_url,
        "destination_relative_path": expected_rel,
        "manifest_format_version": MANIFEST_FORMAT_VERSION,
    }
    for key, expected in required.items():
        if record.get(key) != expected:
            raise ValueError(f"manifest {brick} field {key} is not frozen value {expected!r}")
    digest = record.get("survey_sha256")
    if not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
        raise ValueError(f"manifest {brick} has invalid SHA-256")
    created = record.get("manifest_created_utc")
    if not isinstance(created, str) or not created.endswith("Z"):
        raise ValueError(f"manifest {brick} has invalid creation time")
    inclusion = record.get("private_object_ids_or_hash")
    if (
        not isinstance(inclusion, dict)
        or inclusion.get("working_set_sha256") != record.get("working_set_sha256")
    ):
        raise ValueError(f"manifest {brick} lacks the working-set inclusion hash")
    if "*" in expected_url or "?" in expected_url or "[" in expected_url or "]" in expected_url:
        raise ValueError("wildcards or query strings are forbidden in image URLs")


def _load_harvest_receipts(path: Path) -> dict[str, dict]:
    receipts: dict[str, dict] = {}
    with path.open() as source:
        for line_number, line in enumerate(source, 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"harvest receipt line {line_number} is invalid JSON") from exc
            brick = record.get("brickname")
            if not isinstance(brick, str) or brick in receipts:
                raise ValueError(f"invalid/duplicate harvest brick on line {line_number}")
            if record.get("outcome") != "OK_CONFIRMED" or record.get("image_r_listed") is not True:
                raise ValueError(f"harvest receipt is not accepted for {brick}")
            receipts[brick] = record
    return receipts


def _listed_image_digest(checksum_path: Path, brickname: str) -> str:
    expected = image_filename(brickname)
    matches: list[str] = []
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        match = SHA_LINE_RE.fullmatch(line)
        if match and match.group(2).rsplit("/", 1)[-1] == expected:
            matches.append(match.group(1))
    if len(matches) != 1:
        raise ValueError(f"{checksum_path}: expected exactly one {expected} listing, found {len(matches)}")
    return matches[0]


def build_manifest_records(
    working_set_path: Path,
    checksum_root: Path,
    harvest_receipts_path: Path,
    *,
    expected_count: int = EXPECTED_FILE_COUNT,
) -> list[dict]:
    """Derive only exact image-r URLs and digests from the harvested local listings."""
    harvest = _load_harvest_receipts(harvest_receipts_path)
    working_set_digest = sha256_file(working_set_path)
    manifest_created_utc = utc_now()
    with working_set_path.open(newline="") as source:
        rows = list(csv.DictReader(source))
    if len(rows) != expected_count:
        raise ValueError(f"working set count {len(rows)} != {expected_count}")
    records: list[dict] = []
    seen: set[str] = set()
    for row in rows:
        brick = row.get("brickname", "")
        if BRICK_RE.fullmatch(brick) is None or brick in seen:
            raise ValueError(f"invalid/duplicate working-set brick: {brick!r}")
        seen.add(brick)
        if row.get("coverage_class_exact_indicator") != "required":
            raise ValueError(f"working-set brick {brick} is not required coverage")
        receipt = harvest.get(brick)
        if receipt is None:
            raise ValueError(f"missing harvest receipt for {brick}")
        checksum_path = checksum_root / brick[:3] / f"{brick}.sha256sum"
        if not checksum_path.is_file():
            raise ValueError(f"missing harvested checksum file for {brick}")
        checksum_sha256 = sha256_file(checksum_path)
        if checksum_sha256 != receipt.get("sha256_of_checksum_file"):
            raise ValueError(f"harvested checksum file digest changed for {brick}")
        checksum_bytes = checksum_path.stat().st_size
        if checksum_bytes != receipt.get("bytes_received"):
            raise ValueError(f"harvested checksum file size changed for {brick}")
        filename = image_filename(brick)
        record = {
            "release": RELEASE,
            "portal_host": PORTAL_HOST,
            "source_url": image_url(brick, filename),
            "destination_relative_path": f"coadd/{brick[:3]}/{brick}/{filename}",
            "brickname": brick,
            "aaa": brick[:3],
            "product": "image-r",
            "survey_sha256": _listed_image_digest(checksum_path, brick),
            "checksum_source": {
                "url": receipt["url"],
                "bytes": checksum_bytes,
                "sha256": checksum_sha256,
                "retrieval_utc": receipt.get("utc"),
            },
            "reason": "working-set intersecting source",
            "working_set_sha256": working_set_digest,
            "private_object_ids_or_hash": {"working_set_sha256": working_set_digest},
            "coverage_class": "required",
            "manifest_format_version": MANIFEST_FORMAT_VERSION,
            "manifest_created_utc": manifest_created_utc,
        }
        validate_manifest_record(record)
        records.append(record)
    if set(harvest) != seen:
        raise ValueError("harvest receipt set and working set differ")
    records.sort(key=lambda item: item["brickname"])
    return records


def manifest_bytes(records: Sequence[Mapping[str, object]]) -> bytes:
    return b"".join(
        (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        for record in records
    )


def write_manifest(records: Sequence[Mapping[str, object]], output: Path) -> str:
    data = manifest_bytes(records)
    digest = hashlib.sha256(data).hexdigest()
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".tmp")
    temporary.write_bytes(data)
    os.replace(temporary, output)
    output.with_suffix(output.suffix + ".sha256").write_text(f"{digest}  {output.name}\n")
    return digest


def load_manifest(path: Path, expected_sha256: str) -> list[dict]:
    observed = sha256_file(path)
    if observed != expected_sha256:
        raise ValueError(f"manifest hash mismatch {observed} != {expected_sha256}")
    records: list[dict] = []
    seen: set[str] = set()
    with path.open() as source:
        for line_number, line in enumerate(source, 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"manifest line {line_number} is invalid JSON") from exc
            validate_manifest_record(record)
            brick = record["brickname"]
            if brick in seen:
                raise ValueError(f"duplicate manifest brick {brick}")
            seen.add(brick)
            records.append(record)
    if records != sorted(records, key=lambda item: item["brickname"]):
        raise ValueError("manifest is not sorted by brickname")
    return records


def in_window(now: datetime | None = None) -> bool:
    current = now or datetime.now(PACIFIC)
    if current.tzinfo is None:
        raise ValueError("window time must be timezone-aware")
    current = current.astimezone(PACIFIC)
    if current.weekday() >= 5:
        return True
    return current.hour >= 20 or current.hour < 8


def seconds_until_window_close(now: datetime | None = None) -> int:
    current = (now or datetime.now(PACIFIC)).astimezone(PACIFIC)
    if not in_window(current):
        return 0
    if current.weekday() >= 5 or (current.weekday() == 4 and current.hour >= 20):
        days_to_monday = (7 - current.weekday()) % 7
        close = (current + timedelta(days=days_to_monday)).replace(
            hour=8, minute=0, second=0, microsecond=0
        )
    elif current.hour < 8:
        close = current.replace(hour=8, minute=0, second=0, microsecond=0)
    else:
        close = (current + timedelta(days=1)).replace(
            hour=8, minute=0, second=0, microsecond=0
        )
    return max(1, int((close - current).total_seconds()))


class RateLimiter:
    def __init__(
        self,
        *,
        min_interval_seconds: float = PACING_SECONDS,
        clock: Callable[[], float] = time.monotonic,
        sleeper: Callable[[float], None] = time.sleep,
    ) -> None:
        self.min_interval_seconds = min_interval_seconds
        self.clock = clock
        self.sleeper = sleeper
        self.last_start: float | None = None
        self.request_times: list[float] = []

    def before_request(self) -> float:
        now = self.clock()
        if self.last_start is not None:
            remaining = self.min_interval_seconds - (now - self.last_start)
            if remaining > 0:
                self.sleeper(remaining)
                now = self.clock()
            if now - self.last_start + 1e-9 < self.min_interval_seconds:
                raise RuntimeError("rate limiter sleeper did not advance time")
        self.last_start = now
        self.request_times.append(now)
        return now


class MockTransport:
    """Local fixture transport. It never opens a socket."""
    def __init__(self, responses: Mapping[str, object]) -> None:
        self.responses = {key: (list(value) if isinstance(value, list) else [value]) for key, value in responses.items()}
        self.calls: list[str] = []

    def fetch(
        self,
        url: str,
        destination: Path,
        *,
        max_bytes: int,
        max_time_seconds: int,
    ) -> TransportResult:
        self.calls.append(url)
        if url not in self.responses or not self.responses[url]:
            raise OSError(f"no mock response for {url}")
        outcome = self.responses[url].pop(0)
        if isinstance(outcome, BaseException):
            raise outcome
        if isinstance(outcome, bytes):
            if len(outcome) > max_bytes:
                destination.write_bytes(outcome[:max_bytes])
                return TransportResult(200, {"content-length": str(len(outcome))}, max_bytes, 63)
            destination.write_bytes(outcome)
            return TransportResult(200, {"content-length": str(len(outcome))}, len(outcome), 0)
        if isinstance(outcome, TransportResult):
            destination.write_bytes(b"x" * outcome.bytes_received)
            return outcome
        raise TypeError("mock outcome must be bytes, exception, or TransportResult")


class CurlTransport:
    """Explicit one-URL full-file GET transport; not used by the test suite."""
    def command_for(
        self,
        url: str,
        destination: Path,
        headers: Path,
        metadata: Path,
        *,
        max_bytes: int = 2**63 - 1,
        max_time_seconds: int = 0,
    ) -> list[str]:
        _validate_runtime_url(url)
        if max_bytes <= 0:
            raise ValueError("curl maximum bytes must be positive")
        return [
            "/usr/bin/curl", "--disable", "--silent", "--show-error", "--globoff",
            "--proxy", "", "--proto", "=https", "--proto-redir", "=https",
            "--request", "GET",
            "--connect-timeout", "60", "--max-time", str(max_time_seconds),
            "--max-filesize", str(max_bytes),
            "--limit-rate", BANDWIDTH_LIMIT,
            "--dump-header", str(headers),
            "--output", str(destination),
            "--write-out", "%{json}",
            url,
        ]

    def fetch(
        self,
        url: str,
        destination: Path,
        *,
        max_bytes: int,
        max_time_seconds: int,
    ) -> TransportResult:
        headers_path = destination.with_suffix(destination.suffix + ".headers")
        metadata_path = destination.with_suffix(destination.suffix + ".curl.json")
        command = self.command_for(
            url, destination, headers_path, metadata_path,
            max_bytes=max_bytes, max_time_seconds=max_time_seconds,
        )
        environment = dict(os.environ)
        for key in list(environment):
            if key.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy"):
                environment.pop(key, None)
        for key in ("CURL_HOME", "CURL_CA_BUNDLE", "SSL_CERT_FILE", "SSL_CERT_DIR"):
            environment.pop(key, None)
        completed = subprocess.run(
            command, capture_output=True, text=True, env=environment
        )
        metadata: dict = {}
        if completed.stdout.strip():
            try:
                metadata = json.loads(completed.stdout)
            except json.JSONDecodeError:
                metadata = {}
        metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
        headers = _parse_last_header_block(headers_path)
        status_value = metadata.get("http_code")
        status = int(status_value) if isinstance(status_value, (int, str)) and str(status_value).isdigit() else None
        file_bytes = destination.stat().st_size if destination.exists() else 0
        reported_download = metadata.get("size_download")
        try:
            network_bytes = int(float(reported_download))
        except (TypeError, ValueError):
            network_bytes = 0
        received = max(file_bytes, network_bytes)
        certs = str(metadata.get("certs", ""))
        tls_peer = {
            "certificate_details_sha256": hashlib.sha256(certs.encode()).hexdigest(),
            "subject": _certificate_field(certs, "Subject"),
            "issuer": _certificate_field(certs, "Issuer"),
            "fingerprint": _leaf_certificate_fingerprint(certs),
        }
        headers_path.unlink(missing_ok=True)
        metadata_path.unlink(missing_ok=True)
        return TransportResult(status, headers, received, completed.returncode, completed.stderr[-2000:], tls_peer)


def _certificate_field(certs: str, label: str) -> str:
    for line in certs.splitlines():
        if line.lower().startswith(label.lower() + ":"):
            return line.split(":", 1)[1].strip()
    return "UNAVAILABLE"


def _leaf_certificate_fingerprint(certs: str) -> str:
    match = re.search(
        r"-----BEGIN CERTIFICATE-----\s*(.*?)\s*-----END CERTIFICATE-----",
        certs,
        flags=re.DOTALL,
    )
    if match is None:
        return "UNAVAILABLE"
    try:
        der = base64.b64decode(re.sub(r"\s+", "", match.group(1)), validate=True)
    except (ValueError, binascii.Error):
        return "UNAVAILABLE"
    return hashlib.sha256(der).hexdigest()


def _parse_last_header_block(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    blocks = re.split(r"\r?\n\r?\n", path.read_text(errors="replace"))
    for block in reversed(blocks):
        if block.startswith("HTTP/"):
            headers: dict[str, str] = {}
            for line in block.splitlines()[1:]:
                if ":" in line:
                    key, value = line.split(":", 1)
                    headers[key.strip().lower()] = value.strip()
            return headers
    return {}


def _validate_runtime_url(url: str) -> None:
    if url != image_url(_brickname_from_url(url)):
        raise ValueError(f"URL is not exact frozen image-r URL: {url}")


def _brickname_from_url(url: str) -> str:
    prefix = BASE_URL + "/"
    if not url.startswith(prefix):
        raise ValueError("URL host/root is not frozen portal root")
    parts = url[len(prefix):].split("/")
    if len(parts) != 3:
        raise ValueError("URL is not one explicit image file")
    aaa, brick, filename = parts
    if aaa != brick[:3] or filename != image_filename(brick):
        raise ValueError("URL path is not the manifested brick image-r path")
    return brick


def disk_preflight(target: Path, required_bytes: int) -> dict:
    probe = target.resolve()
    while not probe.exists() and probe != probe.parent:
        probe = probe.parent
    usage = shutil.disk_usage(probe)
    return {
        "utc": utc_now(),
        "target": str(target.resolve()),
        "probed_existing_parent": str(probe),
        "required_bytes": int(required_bytes),
        "available_bytes": usage.free,
        "pass": usage.free >= required_bytes,
    }


def append_jsonl(path: Path, record: Mapping[str, object]) -> None:
    data = (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    try:
        os.write(descriptor, data)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    directory = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


def atomic_json(path: Path, record: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    data = (json.dumps(record, indent=2, sort_keys=True) + "\n").encode()
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        os.write(descriptor, data)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    os.replace(temporary, path)
    directory = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


def fsync_file_and_parent(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    directory = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


@contextmanager
def campaign_lock(path: Path):
    """Hold an exclusive process lock for the complete serial campaign."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT, 0o600)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise CampaignBlocked("another image-transfer process holds the campaign lock") from exc
        os.ftruncate(descriptor, 0)
        os.write(descriptor, f"pid={os.getpid()} utc={utc_now()}\n".encode())
        os.fsync(descriptor)
        yield
    finally:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        finally:
            os.close(descriptor)


class TransferRunner:
    def __init__(
        self,
        campaign_root: Path,
        transport: Transport,
        *,
        approved_byte_ceiling: int,
        enforce_window: bool = True,
        clock: Callable[[], float] = time.monotonic,
        sleeper: Callable[[float], None] = time.sleep,
        finalize_on_complete: bool = False,
        require_network_custody: bool = False,
        manifest_sha256: str | None = None,
        wall_clock: Callable[[], float] = time.time,
    ) -> None:
        self.root = campaign_root.resolve()
        self.transport = transport
        self.ceiling = int(approved_byte_ceiling)
        self.enforce_window = enforce_window
        self.sleeper = sleeper
        self.rate_limiter = RateLimiter(clock=clock, sleeper=sleeper)
        self.finalize_on_complete = finalize_on_complete
        self.require_network_custody = require_network_custody
        self.manifest_sha256 = manifest_sha256
        self.active_manifest_sha256: str | None = None
        self.wall_clock = wall_clock
        self.last_request_epoch: float | None = None
        self.receipts = self.root / "receipts.jsonl"
        self.heartbeat = self.root / "heartbeat.json"
        self.block_event = self.root / "BLOCK_EVENT.json"
        self.inflight = self.root / "inflight.json"
        self.staging = self.root / "staging"
        self.accepted_root = self.root / "accepted"
        self.quarantine = self.root / "quarantine"
        self.campaign_binding = self.root / "campaign_binding.json"
        self.lock_path = self.root / "campaign.lock"

    def _block(self, reason: str, record: Mapping[str, object], **details: object) -> None:
        event = {
            "utc": utc_now(),
            "reason": reason,
            "brickname": record.get("brickname"),
            "url": record.get("source_url"),
            "pacing_seconds": PACING_SECONDS,
            "bandwidth_ceiling_bytes_per_second": int(BANDWIDTH_LIMIT),
            "resumption": "requires Duho's decision; never retry automatically",
            **details,
        }
        atomic_json(self.block_event, event)
        atomic_json(self.heartbeat, {"utc": utc_now(), "state": "BLOCKED", **event})
        raise CampaignBlocked(reason)

    def _load_state(
        self,
        records_by_brick: Mapping[str, Mapping[str, object]],
    ) -> tuple[dict[str, dict], int, dict[str, list[dict]]]:
        accepted: dict[str, dict] = {}
        retry_attempts: dict[str, list[dict]] = {}
        finalized: set[str] = set()
        cumulative = 0
        if self.receipts.exists():
            with self.receipts.open() as source:
                for line_number, line in enumerate(source, 1):
                    try:
                        receipt = json.loads(line)
                    except json.JSONDecodeError as exc:
                        raise CampaignBlocked(f"invalid receipt JSON at line {line_number}") from exc
                    brick = receipt.get("brickname")
                    if brick not in records_by_brick or brick in finalized:
                        raise CampaignBlocked(f"invalid/finalized receipt brick at line {line_number}")
                    receipt_cumulative = int(receipt.get("cumulative_received_bytes", -1))
                    if receipt_cumulative < cumulative:
                        raise CampaignBlocked(f"non-monotonic cumulative bytes at receipt line {line_number}")
                    cumulative = receipt_cumulative
                    for attempt in receipt.get("attempts", []):
                        started_epoch = attempt.get("request_started_epoch")
                        if isinstance(started_epoch, (int, float)):
                            self.last_request_epoch = max(
                                self.last_request_epoch or float(started_epoch),
                                float(started_epoch),
                            )
                    outcome = receipt.get("outcome")
                    if outcome == "TRANSIENT_RETRY_SCHEDULED":
                        retry_attempts.setdefault(str(brick), []).extend(receipt.get("attempts", []))
                        if len(retry_attempts[str(brick)]) > len(BACKOFF_SECONDS):
                            raise CampaignBlocked(f"too many retry receipts for {brick}")
                        continue
                    finalized.add(str(brick))
                    if outcome != "ACCEPTED":
                        raise CampaignBlocked(f"terminal receipt already exists for {brick}")
                    accepted[str(brick)] = receipt
        if self.block_event.exists():
            raise CampaignBlocked("BLOCK_EVENT exists; human decision required")
        if self.inflight.exists():
            raise CampaignBlocked("unresolved in-flight request; received byte count is uncertain")
        if self.accepted_root.exists() and len(accepted) != len(records_by_brick):
            raise CampaignBlocked("accepted root exists for an incomplete receipt set")
        for brick, receipt in accepted.items():
            record = records_by_brick[brick]
            relative = Path(str(record["destination_relative_path"]))
            path = self.accepted_root / relative if self.accepted_root.exists() else self.staging / relative
            if not path.is_file():
                self._block("RECEIPTED_FILE_MISSING", record, expected_path=str(path))
            observed = sha256_file(path)
            if observed != record["survey_sha256"]:
                self._block(
                    "RECEIPTED_FILE_DIGEST_MISMATCH", record,
                    expected_sha256=record["survey_sha256"], observed_sha256=observed,
                )
            if receipt.get("local_sha256") != observed:
                self._block("RECEIPT_DIGEST_CONTRADICTION", record)
        active_root = self.accepted_root if self.accepted_root.exists() else self.staging
        expected_paths = {
            Path(str(record["destination_relative_path"])): brick
            for brick, record in records_by_brick.items()
        }
        actual_paths = {
            path.relative_to(active_root)
            for path in active_root.rglob("*")
            if path.is_file()
        }
        extra = sorted(str(path) for path in actual_paths - set(expected_paths))
        if extra:
            first = next(iter(records_by_brick.values()))
            self._block(
                "EXTRA_DESTINATION_FILE", first,
                extra_paths=extra[:100], extra_count=len(extra),
            )
        for relative, brick in expected_paths.items():
            if relative in actual_paths and brick not in accepted:
                self._block(
                    "UNRECEIPTED_STAGED_FILE", records_by_brick[brick],
                    path=str(active_root / relative),
                )
        return accepted, cumulative, retry_attempts

    def _wait_for_window(self, brick: str, accepted: int, total: int, cumulative: int) -> None:
        while self.enforce_window and not in_window():
            atomic_json(self.heartbeat, {
                "utc": utc_now(), "state": "PAUSED_WINDOW", "next_brick": brick,
                "accepted": accepted, "total": total, "cumulative_received_bytes": cumulative,
                "approved_byte_ceiling": self.ceiling,
            })
            self.sleeper(60.0)

    def run(self, records: Sequence[Mapping[str, object]]) -> dict:
        if self.ceiling <= 0:
            raise ValueError("approved byte ceiling must be positive")
        self.root.mkdir(parents=True, exist_ok=True)
        with campaign_lock(self.lock_path):
            return self._run_locked(records)

    def _run_locked(self, records: Sequence[Mapping[str, object]]) -> dict:
        if not records:
            raise ValueError("empty manifest is not executable")
        records_by_brick: dict[str, Mapping[str, object]] = {}
        for record in records:
            validate_manifest_record(record)
            brick = str(record["brickname"])
            if brick in records_by_brick:
                raise ValueError(f"duplicate record {brick}")
            records_by_brick[brick] = record
        observed_manifest_sha256 = hashlib.sha256(manifest_bytes(records)).hexdigest()
        if self.manifest_sha256 is not None and observed_manifest_sha256 != self.manifest_sha256:
            raise ValueError("runner records do not match the approved manifest SHA-256")
        binding = {
            "binding_sha256": BINDING_SHA256,
            "manifest_sha256": self.manifest_sha256 or observed_manifest_sha256,
            "exact_file_count": len(records),
            "approved_byte_ceiling": self.ceiling,
            "pacing_seconds": PACING_SECONDS,
            "bandwidth_ceiling_bytes_per_second": int(BANDWIDTH_LIMIT),
        }
        self.active_manifest_sha256 = str(binding["manifest_sha256"])
        if self.campaign_binding.exists():
            if json.loads(self.campaign_binding.read_text()) != binding:
                raise CampaignBlocked("campaign binding changed across resume")
        else:
            atomic_json(self.campaign_binding, binding)
        self.staging.mkdir(parents=True, exist_ok=True)
        self.quarantine.mkdir(parents=True, exist_ok=True)
        accepted, cumulative, retry_attempts = self._load_state(records_by_brick)
        if cumulative > self.ceiling:
            raise CampaignBlocked("receipted cumulative bytes already exceed approved ceiling")
        started = utc_now()
        for record in records:
            brick = str(record["brickname"])
            if brick in accepted:
                continue
            self._wait_for_window(brick, len(accepted), len(records), cumulative)
            relative = Path(str(record["destination_relative_path"]))
            final_path = self.staging / relative
            final_path.parent.mkdir(parents=True, exist_ok=True)
            part_path = final_path.with_suffix(final_path.suffix + ".part")
            if part_path.exists():
                self._block("ORPHAN_PART_FILE", record, path=str(part_path))
            attempts = list(retry_attempts.get(brick, []))
            retry_count = len(attempts)
            if retry_count:
                self.sleeper(BACKOFF_SECONDS[retry_count - 1])
            result: TransportResult | None = None
            for attempt_number in range(retry_count, len(BACKOFF_SECONDS) + 1):
                self._wait_for_window(brick, len(accepted), len(records), cumulative)
                remaining_ceiling = self.ceiling - cumulative
                if remaining_ceiling <= 0:
                    self._block(
                        "BYTE_CEILING_EXHAUSTED", record,
                        cumulative_received_bytes=cumulative,
                        approved_byte_ceiling=self.ceiling,
                    )
                request_space = disk_preflight(self.root, remaining_ceiling)
                if not request_space["pass"]:
                    self._block(
                        "DISK_SPACE_PREFLIGHT_FAILED", record,
                        available_bytes=request_space["available_bytes"],
                        required_bytes=request_space["required_bytes"],
                        checked_path=request_space["probed_existing_parent"],
                    )
                self.rate_limiter.before_request()
                wall_now = self.wall_clock()
                if self.last_request_epoch is not None:
                    remaining_spacing = PACING_SECONDS - (wall_now - self.last_request_epoch)
                    if remaining_spacing > 0:
                        self.sleeper(remaining_spacing)
                request_started_epoch = self.wall_clock()
                self.last_request_epoch = request_started_epoch
                request_started_utc = datetime.fromtimestamp(
                    request_started_epoch, timezone.utc
                ).isoformat(timespec="milliseconds").replace("+00:00", "Z")
                atomic_json(self.inflight, {
                    "utc": request_started_utc, "brickname": brick, "url": record["source_url"],
                    "attempt": attempt_number + 1, "cumulative_received_bytes_before": cumulative,
                    "maximum_response_bytes": remaining_ceiling,
                })
                transfer_started = self.wall_clock()
                try:
                    result = self.transport.fetch(
                        str(record["source_url"]), part_path,
                        max_bytes=remaining_ceiling,
                        max_time_seconds=(
                            seconds_until_window_close() if self.enforce_window else 0
                        ),
                    )
                except OSError as exc:
                    received = part_path.stat().st_size if part_path.exists() else 0
                    result = TransportResult(None, {}, received, 1, str(exc))
                request_completed_epoch = self.wall_clock()
                cumulative += result.bytes_received
                duration = max(0.0, request_completed_epoch - transfer_started)
                attempt = {
                    "attempt": attempt_number + 1,
                    "request_started_utc": request_started_utc,
                    "request_started_epoch": request_started_epoch,
                    "request_completed_utc": datetime.fromtimestamp(
                        request_completed_epoch, timezone.utc
                    ).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
                    "duration_seconds": duration,
                    "http_status": result.status,
                    "transport_returncode": result.curl_returncode,
                    "bytes_received": result.bytes_received,
                    "content_length": result.headers.get("content-length"),
                    "last_modified": result.headers.get("last-modified"),
                    "retry_after": result.headers.get("retry-after"),
                    "tls_peer": dict(result.tls_peer or {}),
                    "stderr_tail": result.stderr,
                    "observed_bytes_per_second": (
                        result.bytes_received / duration if duration > 0 else None
                    ),
                }
                attempts.append(attempt)
                if cumulative > self.ceiling:
                    terminal = self._terminal_receipt(record, "BYTE_CEILING_EXCEEDED", attempts, cumulative)
                    append_jsonl(self.receipts, terminal)
                    self.inflight.unlink(missing_ok=True)
                    self._block("BYTE_CEILING_EXCEEDED", record, cumulative_received_bytes=cumulative, approved_byte_ceiling=self.ceiling)
                if result.curl_returncode == 63:
                    terminal = self._terminal_receipt(
                        record, "FILE_EXCEEDS_REMAINING_CEILING", attempts, cumulative
                    )
                    append_jsonl(self.receipts, terminal)
                    self.inflight.unlink(missing_ok=True)
                    self._block(
                        "FILE_EXCEEDS_REMAINING_CEILING", record,
                        remaining_ceiling_before_request=remaining_ceiling,
                    )
                if result.status in (403, 429):
                    terminal = self._terminal_receipt(record, f"HTTP_{result.status}", attempts, cumulative)
                    append_jsonl(self.receipts, terminal)
                    self.inflight.unlink(missing_ok=True)
                    self._block(f"HTTP_{result.status}", record, http_status=result.status)
                if result.status == 503 and result.headers.get("retry-after") is not None:
                    terminal = self._terminal_receipt(record, "RATE_LIMIT_SIGNAL", attempts, cumulative)
                    append_jsonl(self.receipts, terminal)
                    self.inflight.unlink(missing_ok=True)
                    self._block("RATE_LIMIT_SIGNAL", record, http_status=503)
                content_type = result.headers.get("content-type", "").lower()
                if "text/html" in content_type or "text/plain" in content_type:
                    terminal = self._terminal_receipt(record, "CHALLENGE_OR_BLOCK_PAGE", attempts, cumulative)
                    append_jsonl(self.receipts, terminal)
                    self.inflight.unlink(missing_ok=True)
                    self._block("CHALLENGE_OR_BLOCK_PAGE", record, content_type=content_type)
                content_length = result.headers.get("content-length")
                length_matches = content_length is not None and content_length.isdigit() and int(content_length) == result.bytes_received
                success = result.curl_returncode == 0 and result.status == 200 and length_matches
                if success and self.require_network_custody:
                    tls_peer = result.tls_peer or {}
                    required_tls = ("subject", "issuer", "fingerprint")
                    tls_complete = all(
                        isinstance(tls_peer.get(field), str)
                        and bool(tls_peer[field])
                        and tls_peer[field] != "UNAVAILABLE"
                        for field in required_tls
                    )
                    if not tls_complete or not result.headers.get("last-modified"):
                        terminal = self._terminal_receipt(
                            record, "NETWORK_CUSTODY_METADATA_MISSING", attempts, cumulative
                        )
                        append_jsonl(self.receipts, terminal)
                        self.inflight.unlink(missing_ok=True)
                        self._block(
                            "NETWORK_CUSTODY_METADATA_MISSING", record,
                            tls_peer=dict(tls_peer),
                            last_modified=result.headers.get("last-modified"),
                        )
                if success:
                    break
                transient = (
                    result.status in (None, 0, 500, 502, 503, 504)
                    or (result.status == 200 and not length_matches)
                )
                if transient and attempt_number < len(BACKOFF_SECONDS):
                    retry_count += 1
                    append_jsonl(self.receipts, {
                        "utc": utc_now(),
                        "outcome": "TRANSIENT_RETRY_SCHEDULED",
                        "brickname": brick,
                        "url": record["source_url"],
                        "attempts": [attempt],
                        "cumulative_received_bytes": cumulative,
                        "approved_byte_ceiling": self.ceiling,
                        "next_backoff_seconds": BACKOFF_SECONDS[attempt_number],
                        "manifest_sha256": binding["manifest_sha256"],
                    })
                    part_path.unlink(missing_ok=True)
                    self.inflight.unlink(missing_ok=True)
                    self.sleeper(BACKOFF_SECONDS[attempt_number])
                    continue
                terminal = self._terminal_receipt(record, "REQUIRED_FILE_TRANSFER_FAILED", attempts, cumulative)
                append_jsonl(self.receipts, terminal)
                self.inflight.unlink(missing_ok=True)
                self._block("REQUIRED_FILE_TRANSFER_FAILED", record, attempts=attempts)
            if result is None or not part_path.is_file():
                self._block("MISSING_STAGED_RESPONSE", record)
            observed = sha256_file(part_path)
            fsync_file_and_parent(part_path)
            if observed != record["survey_sha256"]:
                quarantine_path = self.quarantine / f"{brick}.{int(time.time())}.sha256-mismatch"
                os.replace(part_path, quarantine_path)
                fsync_file_and_parent(quarantine_path)
                terminal = self._terminal_receipt(
                    record, "SHA256_MISMATCH", attempts, cumulative,
                    observed_sha256=observed, quarantine_path=str(quarantine_path),
                )
                append_jsonl(self.receipts, terminal)
                self.inflight.unlink(missing_ok=True)
                self._block(
                    "SHA256_MISMATCH", record,
                    expected_sha256=record["survey_sha256"], observed_sha256=observed,
                    quarantine_path=str(quarantine_path),
                )
            os.replace(part_path, final_path)
            fsync_file_and_parent(final_path)
            receipt = {
                "utc": utc_now(), "outcome": "ACCEPTED", "brickname": brick,
                "url": record["source_url"], "destination_relative_path": str(relative),
                "http_status": result.status, "content_length": result.headers.get("content-length"),
                "bytes_received": result.bytes_received,
                "bytes_received_all_attempts": sum(item["bytes_received"] for item in attempts),
                "last_modified": result.headers.get("last-modified"),
                "tls_peer": dict(result.tls_peer or {}), "retry_count": retry_count,
                "attempts": attempts, "local_sha256": observed,
                "expected_sha256": record["survey_sha256"], "digest_verified": True,
                "cumulative_received_bytes": cumulative, "approved_byte_ceiling": self.ceiling,
                "manifest_sha256": self.active_manifest_sha256,
                "pacing_seconds": PACING_SECONDS,
                "bandwidth_ceiling_bytes_per_second": int(BANDWIDTH_LIMIT),
            }
            append_jsonl(self.receipts, receipt)
            self.inflight.unlink(missing_ok=True)
            accepted[brick] = receipt
            atomic_json(self.heartbeat, {
                "utc": utc_now(), "state": "RUNNING", "accepted": len(accepted),
                "total": len(records), "last_brick": brick,
                "cumulative_received_bytes": cumulative, "approved_byte_ceiling": self.ceiling,
                "pacing_seconds": PACING_SECONDS,
                "bandwidth_ceiling_bytes_per_second": int(BANDWIDTH_LIMIT),
                "in_window": in_window() if self.enforce_window else None,
                "campaign_started_utc": started,
            })
        if self.finalize_on_complete and not self.accepted_root.exists():
            os.replace(self.staging, self.accepted_root)
        summary = {
            "utc": utc_now(), "state": "COMPLETE", "accepted": len(accepted),
            "total": len(records), "cumulative_received_bytes": cumulative,
            "approved_byte_ceiling": self.ceiling,
            "manifest_sha256": self.active_manifest_sha256,
            "accepted_root": str(self.accepted_root if self.accepted_root.exists() else self.staging),
        }
        atomic_json(self.heartbeat, summary)
        atomic_json(self.root / "TRANSFER_COMPLETE.json", summary)
        return summary

    def _terminal_receipt(
        self,
        record: Mapping[str, object],
        outcome: str,
        attempts: Sequence[Mapping[str, object]],
        cumulative: int,
        **extra: object,
    ) -> dict:
        return {
            "utc": utc_now(), "outcome": outcome, "brickname": record["brickname"],
            "url": record["source_url"], "attempts": list(attempts),
            "bytes_received_all_attempts": sum(int(item["bytes_received"]) for item in attempts),
            "cumulative_received_bytes": cumulative, "approved_byte_ceiling": self.ceiling,
            "manifest_sha256": self.active_manifest_sha256,
            **extra,
        }


def load_approval(
    path: Path,
    *,
    approval_sha256: str,
    manifest_sha256: str,
    destination: Path,
    file_count: int,
    ceiling: int,
) -> dict:
    if sha256_file(path) != approval_sha256:
        raise ValueError("retrieval approval SHA-256 mismatch")
    if path.stat().st_mode & 0o777 != 0o444:
        raise ValueError("retrieval approval must be frozen mode 444")
    approval = json.loads(path.read_text())
    expected = {
        "status": APPROVAL_STATUS,
        "decision_authority": "Duho",
        "kun_transport_gate": "PASS_TRANSPORT_BUILD",
        "binding_sha256": BINDING_SHA256,
        "manifest_sha256": manifest_sha256,
        "destination": str(destination.resolve()),
        "exact_file_count": file_count,
        "approved_byte_ceiling": ceiling,
        "concurrency": 1,
        "image_request_spacing_seconds": PACING_SECONDS,
        "bandwidth_ceiling_bytes_per_second": int(BANDWIDTH_LIMIT),
        "weekday_window_us_pacific": "20:00-08:00",
        "weekend_window_us_pacific": "any hour",
        "size_sample_count": 1024,
    }
    for key, value in expected.items():
        if approval.get(key) != value:
            raise ValueError(f"approval field {key} must equal {value!r}")
    for key in (
        "size_sample_receipt_sha256",
        "coverage_census_sha256",
        "geometry_sidecar_receipt_sha256",
    ):
        value = approval.get(key)
        if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
            raise ValueError(f"approval field {key} must be a pinned SHA-256")
    return approval


def command_build_manifest(args: argparse.Namespace) -> int:
    verify_frozen_build_gates()
    if sha256_file(WORKING_SET) != WORKING_SET_SHA256:
        raise ValueError("frozen working-set SHA-256 mismatch")
    records = build_manifest_records(
        WORKING_SET, HARVEST / "checksum_files", HARVEST / "receipts.jsonl"
    )
    digest = write_manifest(records, args.output)
    print(json.dumps({"state": "UNSEALED_BUILD_CANDIDATE", "records": len(records), "sha256": digest, "path": str(args.output.resolve())}, sort_keys=True))
    return 0


def command_preflight(args: argparse.Namespace) -> int:
    result = disk_preflight(args.destination, args.required_bytes)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 90


def _run_gated(args: argparse.Namespace) -> int:
    verify_frozen_build_gates()
    if args.execute_gated_transfer != EXECUTION_ACK:
        raise ValueError("explicit execution acknowledgement missing")
    if args.approved_byte_ceiling <= 0:
        raise ValueError("approved byte ceiling must be positive")
    records = load_manifest(args.manifest, args.manifest_sha256)
    if len(records) != EXPECTED_FILE_COUNT:
        raise ValueError(f"manifest must contain exactly {EXPECTED_FILE_COUNT} image-r files")
    load_approval(
        args.approval_file,
        approval_sha256=args.approval_sha256,
        manifest_sha256=args.manifest_sha256,
        destination=args.destination,
        file_count=len(records),
        ceiling=args.approved_byte_ceiling,
    )
    preflight = disk_preflight(args.destination, args.approved_byte_ceiling)
    if not preflight["pass"]:
        raise CampaignBlocked("disk-space preflight failed before network transport construction")
    runner = TransferRunner(
        args.destination,
        CurlTransport(),
        approved_byte_ceiling=args.approved_byte_ceiling,
        enforce_window=True,
        finalize_on_complete=True,
        require_network_custody=True,
        manifest_sha256=args.manifest_sha256,
    )
    summary = runner.run(records)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def command_launch(args: argparse.Namespace) -> int:
    verify_frozen_build_gates()
    if args.execute_gated_transfer != EXECUTION_ACK:
        raise ValueError("explicit execution acknowledgement missing")
    if args.approved_byte_ceiling <= 0:
        raise ValueError("approved byte ceiling must be positive")
    records = load_manifest(args.manifest, args.manifest_sha256)
    if len(records) != EXPECTED_FILE_COUNT:
        raise ValueError(f"manifest must contain exactly {EXPECTED_FILE_COUNT} image-r files")
    load_approval(
        args.approval_file,
        approval_sha256=args.approval_sha256,
        manifest_sha256=args.manifest_sha256,
        destination=args.destination,
        file_count=len(records),
        ceiling=args.approved_byte_ceiling,
    )
    preflight = disk_preflight(args.destination, args.approved_byte_ceiling)
    if not preflight["pass"]:
        raise CampaignBlocked("disk-space preflight failed; detached process not started")
    command = [
        "/usr/bin/nohup", sys.executable, str(Path(__file__).resolve()), "run",
        "--manifest", str(args.manifest), "--manifest-sha256", args.manifest_sha256,
        "--approval-file", str(args.approval_file),
        "--approval-sha256", args.approval_sha256,
        "--destination", str(args.destination),
        "--approved-byte-ceiling", str(args.approved_byte_ceiling),
        "--execute-gated-transfer", args.execute_gated_transfer,
    ]
    log = args.log.resolve()
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("ab", buffering=0) as stream:
        process = subprocess.Popen(
            command, stdin=subprocess.DEVNULL, stdout=stream, stderr=subprocess.STDOUT,
            start_new_session=True, close_fds=True,
        )
    print(json.dumps({"state": "DETACHED", "pid": process.pid, "log": str(log), "command": command[:-1] + ["<execution-ack>"]}, sort_keys=True))
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    sub = result.add_subparsers(dest="command", required=True)
    manifest = sub.add_parser("build-manifest", help="offline derivation from harvested checksum files")
    manifest.add_argument("--output", type=Path, default=HERE / "candidate_image_manifest.jsonl")
    manifest.set_defaults(function=command_build_manifest)
    preflight = sub.add_parser("preflight", help="offline target-volume free-space check")
    preflight.add_argument("--destination", type=Path, default=HERE / "campaign")
    preflight.add_argument("--required-bytes", type=int, default=BUILD_PREFLIGHT_BYTES)
    preflight.set_defaults(function=command_preflight)
    for name, function in (("run", _run_gated), ("launch", command_launch)):
        child = sub.add_parser(name)
        child.add_argument("--manifest", type=Path, required=True)
        child.add_argument("--manifest-sha256", required=True)
        child.add_argument("--approval-file", type=Path, required=True)
        child.add_argument("--approval-sha256", required=True)
        child.add_argument("--destination", type=Path, required=True)
        child.add_argument("--approved-byte-ceiling", type=int, required=True)
        child.add_argument("--execute-gated-transfer", required=True)
        if name == "launch":
            child.add_argument("--log", type=Path, default=HERE / "transfer_stdout.log")
        child.set_defaults(function=function)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    return int(args.function(args))


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (CampaignBlocked, ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"STOP: {exc}", file=sys.stderr)
        raise SystemExit(86)
