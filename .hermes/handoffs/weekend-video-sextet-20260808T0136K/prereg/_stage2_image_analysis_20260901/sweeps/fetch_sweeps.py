#!/usr/bin/env python3
"""Resumable, published-SHA-verified DR10-south sweep acquisition.

This is acquisition-only: it never opens or interprets a FITS payload.  For
V11 section 7.9 receipt compatibility, the ``brick`` field contains the sweep
filename, which is the identity key for this acquisition.
"""
import argparse
import concurrent.futures as cf
import hashlib
import http.client
import json
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_HASHES = ("https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/"
                  "south/sweep/10.0/legacysurvey_dr10_south_sweep_10.0.sha256sum")
UA = {"User-Agent": "NebulaMind-spin-parity/1.0 (academic; contact duhokim81@gmail.com)"}
SHA_LINE = re.compile(r"^([0-9a-fA-F]{64})\s+[*]?(.+?)\s*$")


def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path, chunk=8 * 1024 * 1024):
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            block = fh.read(chunk)
            if not block:
                return digest.hexdigest()
            digest.update(block)


def fetch_hashes(url, timeout):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        text = response.read().decode("utf-8", "strict")
    hashes = {}
    for line in text.splitlines():
        match = SHA_LINE.match(line)
        if match:
            hashes[Path(match.group(2)).name] = match.group(1).lower()
    if not hashes:
        raise RuntimeError("published checksum list contained no SHA-256 lines")
    return hashes


def append_receipt(path, record, lock):
    path.parent.mkdir(parents=True, exist_ok=True)
    with lock, path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
        fh.flush()


class AdaptiveThrottle:
    """A condition-based global concurrency gate shared by all workers."""
    def __init__(self, maximum, log=print, clock=time.monotonic,
                 pressure_window=300, clean_window=1800):
        self.maximum = maximum
        self.limit = maximum
        self.active = 0
        self.log = log
        self.clock = clock
        self.pressure_window = pressure_window
        self.clean_window = clean_window
        self.events = deque()
        self.last_pressure = None
        self.last_step = clock()
        self.cv = threading.Condition()

    def _recover_locked(self, now):
        clean_since = self.last_pressure if self.last_pressure is not None else self.last_step
        if self.limit < self.maximum and now - clean_since >= self.clean_window \
                and now - self.last_step >= self.clean_window:
            self.limit += 1
            self.last_step = now
            self.log(f"THROTTLE active worker limit increased to {self.limit} after 30 clean minutes")
            self.cv.notify_all()

    def enter(self):
        with self.cv:
            while True:
                self._recover_locked(self.clock())
                if self.active < self.limit:
                    self.active += 1
                    return
                self.cv.wait(timeout=1.0)

    def leave(self):
        with self.cv:
            self.active -= 1
            self.cv.notify_all()

    def pressure(self, status):
        now = self.clock()
        with self.cv:
            self.last_pressure = now
            self.events.append(now)
            while self.events and now - self.events[0] > self.pressure_window:
                self.events.popleft()
            if len(self.events) >= 3:
                new_limit = max(2, self.limit // 2)
                self.events.clear()
                if new_limit < self.limit:
                    self.limit = new_limit
                    self.last_step = now
                    self.log(f"THROTTLE active worker limit halved to {self.limit} after HTTP {status} pressure")
            self.cv.notify_all()

    def recover_if_due(self):
        with self.cv:
            self._recover_locked(self.clock())


class Fetcher:
    def __init__(self, args, published, entries, log=print, sleeper=time.sleep,
                 rng=random.random):
        self.args = args
        self.published = published
        self.entries = entries
        self.log = log
        self.sleeper = sleeper
        self.rng = rng
        self.journal_lock = threading.Lock()
        self.state_lock = threading.Lock()
        self.throttle = AdaptiveThrottle(args.workers, log=log)
        self.completed = 0
        self.ok = 0
        self.failed = 0
        self.skipped = 0
        self.bytes_done = 0
        self.events = deque()
        self.started = time.monotonic()
        self.last_progress = self.started
        self.total_bytes = sum(int(e.get("bytes") or 0) for e in entries)
        self.stop_reporter = threading.Event()

    def receipt_failed(self, filename, url, error):
        rec = {"brick": filename, "error": error, "url": url,
               "utc": utc(), "verdict": "FETCH-FAILED"}
        append_receipt(self.args.journal, rec, self.journal_lock)

    def _backoff(self, attempt):
        self.sleeper(min(120.0, 2.0 ** attempt + self.rng()))

    def _download_attempt(self, entry, part):
        req = urllib.request.Request(entry["url"], headers=UA)
        self.throttle.enter()
        try:
            with urllib.request.urlopen(req, timeout=self.args.timeout) as response, \
                    part.open("wb") as out:
                declared = response.headers.get("Content-Length")
                expected_length = int(declared) if declared is not None else None
                digest = hashlib.sha256()
                count = 0
                while True:
                    block = response.read(8 * 1024 * 1024)
                    if not block:
                        break
                    out.write(block)
                    digest.update(block)
                    count += len(block)
                out.flush()
            if expected_length is not None and count < expected_length:
                raise EOFError(f"truncated transfer: received {count} bytes; Content-Length {expected_length}")
            return count, digest.hexdigest()
        finally:
            self.throttle.leave()

    def one(self, entry):
        filename = entry["filename"]
        url = entry["url"]
        expected = self.published[filename]
        out = self.args.dest / filename
        part = self.args.dest / (filename + ".part")
        if out.exists() and sha256_file(out) == expected:
            with self.state_lock:
                self.skipped += 1
                self._completed_locked(out.stat().st_size)
            return "skip"
        if out.exists():
            quarantine = self.args.quarantine / (filename + ".preexisting-mismatch")
            out.replace(quarantine)

        for attempt in range(4):              # initial attempt + up to three retries
            try:
                count, got = self._download_attempt(entry, part)
            except urllib.error.HTTPError as exc:
                if exc.code == 429 or 500 <= exc.code <= 599:
                    self.throttle.pressure(exc.code)
                self.receipt_failed(filename, url, f"HTTPError: HTTP {exc.code}: {exc.reason}")
                if attempt < 3 and (exc.code == 429 or 500 <= exc.code <= 599):
                    self._backoff(attempt)
                    continue
                with self.state_lock:
                    self.failed += 1
                    self._completed_locked(0)
                part.unlink(missing_ok=True)
                return "fail"
            except (urllib.error.URLError, TimeoutError, OSError, EOFError,
                    http.client.IncompleteRead) as exc:
                self.receipt_failed(filename, url, f"{type(exc).__name__}: {exc}")
                if attempt < 3:
                    self._backoff(attempt)
                    continue
                with self.state_lock:
                    self.failed += 1
                    self._completed_locked(0)
                part.unlink(missing_ok=True)
                return "fail"

            rec = {"brick": filename, "bytes": count, "computed_sha256": got,
                   "published_sha256": expected, "url": url, "utc": utc(),
                   "verdict": "OK"}
            if got != expected:
                quarantine = self.args.quarantine / filename
                if quarantine.exists():
                    quarantine = self.args.quarantine / f"{filename}.{int(time.time())}"
                part.replace(quarantine)
                rec["verdict"] = "SHA-MISMATCH-QUARANTINED"
                append_receipt(self.args.journal, rec, self.journal_lock)
                with self.state_lock:
                    self.failed += 1
                    self._completed_locked(0)
                return "fail"
            part.replace(out)
            append_receipt(self.args.journal, rec, self.journal_lock)
            with self.state_lock:
                self.ok += 1
                self._completed_locked(count)
            if self.args.delay:
                self.sleeper(self.args.delay)
            return "ok"

    def _completed_locked(self, byte_count):
        now = time.monotonic()
        self.completed += 1
        self.bytes_done += byte_count
        self.events.append((now, byte_count))
        if self.completed % 10 == 0 or now - self.last_progress >= 300:
            self._progress_locked(now)

    def _progress_locked(self, now=None):
        now = now or time.monotonic()
        cutoff = now - 900
        while self.events and self.events[0][0] < cutoff:
            self.events.popleft()
        if self.events:
            span = min(900, max(now - self.events[0][0], 1.0))
            rate = sum(x[1] for x in self.events) / 2**30 * 3600 / span
        else:
            rate = 0.0
        remaining = max(0, self.total_bytes - self.bytes_done)
        eta = remaining / 2**30 / rate if rate else float("inf")
        eta_text = f"{eta:.1f}h" if eta != float("inf") else "unknown"
        self.log(f"PROGRESS files done {self.completed}/{len(self.entries)} | "
                 f"{self.bytes_done / 2**30:.2f} GiB | last-15-min {rate:.2f} GiB/h | ETA {eta_text}")
        self.last_progress = now

    def reporter(self):
        while not self.stop_reporter.wait(60):
            self.throttle.recover_if_due()
            with self.state_lock:
                if time.monotonic() - self.last_progress >= 300:
                    self._progress_locked()

    def run(self):
        reporter = threading.Thread(target=self.reporter, daemon=True)
        reporter.start()
        try:
            with cf.ThreadPoolExecutor(max_workers=self.args.workers) as pool:
                list(pool.map(self.one, self.entries))
        finally:
            self.stop_reporter.set()
            reporter.join(timeout=1)
        with self.state_lock:
            self._progress_locked()
        return 1 if self.failed else 0


def select_entries(manifest, footprint):
    prefix = footprint + "_"
    return [e for e in manifest["files"]
            if footprint in e.get("footprints", [])
            or any(x == footprint or x.startswith(prefix) for x in e.get("footprints", []))]


def parse_args(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest", type=Path, default=HERE / "sweep_manifest_v1.json")
    ap.add_argument("--footprint", default="a")
    ap.add_argument("--dest", type=Path, default=HERE / "data")
    ap.add_argument("--journal", type=Path, default=HERE / "sweep_fetch_receipts.jsonl")
    ap.add_argument("--published-hashes", default=DEFAULT_HASHES)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--delay", type=float, default=0.2)
    ap.add_argument("--timeout", type=float, default=600.0)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--quarantine", type=Path, default=HERE / "quarantine",
                    help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    if args.workers < 2:
        ap.error("--workers must be at least 2 (global throttle minimum is 2)")
    if args.limit < 0:
        ap.error("--limit must be nonnegative")
    return args


def main(argv=None):
    args = parse_args(argv)
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    entries = select_entries(manifest, args.footprint)
    if args.limit:
        entries = entries[:args.limit]
    print(f"PLAN footprint={args.footprint} files={len(entries)} "
          f"GiB={sum(int(e.get('bytes') or 0) for e in entries) / 2**30:.3f} "
          f"workers={args.workers} dest={args.dest}")
    print(f"published hashes (fetched once): {args.published_hashes}")
    if args.dry_run:
        for entry in entries:
            print(f"  {entry['filename']} <- {entry['url']}")
        return 0
    args.dest.mkdir(parents=True, exist_ok=True)
    args.quarantine.mkdir(parents=True, exist_ok=True)
    published = fetch_hashes(args.published_hashes, args.timeout)
    missing = [e["filename"] for e in entries if e["filename"] not in published]
    if missing:
        raise RuntimeError(f"{len(missing)} selected files absent from published checksum list: {missing[:3]}")
    disagreements = [e["filename"] for e in entries
                     if e.get("published_sha256") and
                     e["published_sha256"].lower() != published[e["filename"]]]
    if disagreements:
        raise RuntimeError(f"manifest/published checksum disagreement: {disagreements[:3]}")
    return Fetcher(args, published, entries).run()


if __name__ == "__main__":
    sys.exit(main())
