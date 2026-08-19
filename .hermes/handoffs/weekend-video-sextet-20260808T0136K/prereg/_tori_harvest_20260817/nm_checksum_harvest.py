#!/usr/bin/env python3
"""Checksum harvest (frozen successor binding §11 step 4a). AUTHORIZED 2026-08-17.

One .sha256sum GET per working-set brick. Zero image bytes — hard invariant.
Frozen §5.4 rules implemented verbatim: serial, >=1.0 s between request
starts (checksum tier), retrieval windows 20:00-08:00 US/Pacific weekdays +
any hour weekends (pause cleanly at boundaries), transient backoff
30/60/120 s then terminal per file, and STOP-ON-FIRST-BLOCK: any 429, 403,
rate-limit signal, or unparseable/challenge response halts the ENTIRE
campaign with a custody receipt; resumption is Duho's decision.

Detached and resumable: append-only receipts.jsonl is the state; on start,
already-receipted bricks are never re-requested. Heartbeat rewritten
periodically for progress checks without attaching.
"""
import csv
import hashlib
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
WORKINGSET = PREREG / "_tori_r1_workingset_evidence" / "workingset_bricks.csv"
WORKINGSET_SHA256 = "78ee99d6824bf4f5126b9ffd9eb622ad8201df2c64c3f232d99c1791b5f36b74"
RECEIPTS = HERE / "receipts.jsonl"
HEARTBEAT = HERE / "heartbeat.json"
BLOCK_EVENT = HERE / "BLOCK_EVENT.json"
DONE_MARKER = HERE / "HARVEST_COMPLETE.json"

URL = ("https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/"
       "{aaa}/{b}/legacysurvey_dr10_south_coadd_{aaa}_{b}.sha256sum")
PACING_SECONDS = 1.0                    # frozen §5.4 checksum/metadata tier
BACKOFF = (30.0, 60.0, 120.0)           # frozen §5.4 transient ladder
PACIFIC = ZoneInfo("America/Los_Angeles")
SHA_LINE = re.compile(r"^[0-9a-f]{64}[ \t*]+\S+", re.M)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def in_window(now=None) -> bool:
    t = (now or datetime.now(PACIFIC))
    if t.weekday() >= 5:                # Sat/Sun: any hour
        return True
    return t.hour >= 20 or t.hour < 8   # weekday overnight window


def write_heartbeat(done, total, state, last_brick, started, window_pauses, rate):
    HEARTBEAT.write_text(json.dumps({
        "utc": utc_now(),
        "state": state,
        "completed": done,
        "total": total,
        "last_brick": last_brick,
        "recent_rate_req_per_s": rate,
        "in_window": in_window(),
        "window_pauses": window_pauses,
        "campaign_started_utc": started,
        "pacing_seconds": PACING_SECONDS,
    }, indent=2, sort_keys=True) + "\n")


def stop_on_block(brick, url, status, body_head, done, reason):
    BLOCK_EVENT.write_text(json.dumps({
        "utc": utc_now(),
        "reason": reason,
        "brickname": brick,
        "url": url,
        "http_status": status,
        "response_body_head": body_head[:500],
        "completed_before_stop": done,
        "pacing_seconds": PACING_SECONDS,
        "resumption": "requires Duho's decision (frozen §5.4.6); do not retry, do not slow and continue",
    }, indent=2, sort_keys=True) + "\n")
    print(f"BLOCK_EVENT {reason} at {brick} status={status}; campaign halted", flush=True)
    sys.exit(86)


def fetch(brick):
    url = URL.format(aaa=brick[:3], b=brick)
    header_file = HERE / "_last_headers.txt"
    out = subprocess.run(
        ["curl", "-s", "--max-time", "60", "-D", str(header_file),
         "-o", str(HERE / "_last_body.bin"), "-w", "%{http_code}", url],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        return url, None, None, b"", {}
    status = out.stdout.strip()
    body = (HERE / "_last_body.bin").read_bytes()
    headers = {}
    for line in header_file.read_text(errors="replace").splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            headers[key.strip().lower()] = value.strip()
    return url, out.returncode, status, body, headers


def main():
    observed = hashlib.sha256(WORKINGSET.read_bytes()).hexdigest()
    if observed != WORKINGSET_SHA256:
        print(f"WORKINGSET HASH MISMATCH {observed} != {WORKINGSET_SHA256}; refusing to start", flush=True)
        sys.exit(87)
    bricks = [r["brickname"] for r in csv.DictReader(open(WORKINGSET))]
    total = len(bricks)

    done = set()
    if RECEIPTS.exists():
        for line in RECEIPTS.open():
            try:
                done.add(json.loads(line)["brickname"])
            except Exception:
                pass
    started = utc_now()
    print(f"harvest start {started}: {len(done)}/{total} already receipted", flush=True)

    window_pauses = 0
    recent = []
    last_start = 0.0
    processed = 0
    with RECEIPTS.open("a") as receipts:
        for brick in bricks:
            if brick in done:
                continue
            while not in_window():
                write_heartbeat(len(done), total, "PAUSED_WINDOW", brick, started, window_pauses, 0.0)
                time.sleep(60)
            # frozen pacing: >=1.0 s between request STARTS, strictly serial
            wait = PACING_SECONDS - (time.monotonic() - last_start)
            if wait > 0:
                time.sleep(wait)

            attempt = 0
            while True:
                last_start = time.monotonic()
                url, rc, status, body, headers = fetch(brick)
                record = {
                    "brickname": brick, "url": url, "utc": utc_now(),
                    "http_status": status, "curl_rc": rc,
                    "content_length_header": headers.get("content-length"),
                    "bytes_received": len(body),
                    "last_modified": headers.get("last-modified"),
                }
                if rc is None or rc != 0:
                    # transport-level transient (timeout/reset), no block signal
                    if attempt < len(BACKOFF):
                        time.sleep(BACKOFF[attempt]); attempt += 1; continue
                    record["outcome"] = "TERMINAL_TRANSIENT_EXHAUSTED"
                    break
                if status in ("429", "403"):
                    stop_on_block(brick, url, status, body.decode(errors="replace"), len(done), f"HTTP {status}")
                if status == "503" and "retry-after" in headers:
                    stop_on_block(brick, url, status, body.decode(errors="replace"), len(done), "503 with Retry-After (rate-limit signal)")
                if status in ("500", "502", "503", "504"):
                    if attempt < len(BACKOFF):
                        time.sleep(BACKOFF[attempt]); attempt += 1; continue
                    record["outcome"] = "TERMINAL_TRANSIENT_EXHAUSTED"
                    break
                if status == "404":
                    record["outcome"] = "CHECKSUM_FILE_MISSING"   # R2 contradiction class
                    break
                if status != "200":
                    stop_on_block(brick, url, status, body.decode(errors="replace"), len(done), f"unexpected status {status}")
                # 200: verify as we store
                text = body.decode(errors="replace")
                clen = headers.get("content-length")
                if clen is not None and int(clen) != len(body):
                    if attempt < len(BACKOFF):
                        time.sleep(BACKOFF[attempt]); attempt += 1; continue
                    record["outcome"] = "TERMINAL_LENGTH_MISMATCH"
                    break
                if not SHA_LINE.search(text):
                    stop_on_block(brick, url, status, text, len(done), "200 with non-checksum body (challenge/block page)")
                record["sha256_of_checksum_file"] = hashlib.sha256(body).hexdigest()
                record["entries"] = len(SHA_LINE.findall(text))
                has_image_r = f"legacysurvey-{brick}-image-r.fits.fz" in text
                record["image_r_listed"] = has_image_r
                record["outcome"] = "OK_CONFIRMED" if has_image_r else "OK_CONTRADICTED_NO_IMAGE_R"
                (HERE / "checksum_files" / brick[:3]).mkdir(parents=True, exist_ok=True)
                (HERE / "checksum_files" / brick[:3] / f"{brick}.sha256sum").write_bytes(body)
                break

            receipts.write(json.dumps(record, sort_keys=True) + "\n")
            receipts.flush()
            done.add(brick)
            processed += 1
            recent.append(time.monotonic())
            recent = recent[-100:]
            if processed % 25 == 0:
                rate = round((len(recent) - 1) / max(1e-9, recent[-1] - recent[0]), 3) if len(recent) > 1 else 0.0
                write_heartbeat(len(done), total, "RUNNING", brick, started, window_pauses, rate)
            if record["outcome"] not in ("OK_CONFIRMED",):
                print(f"NOTE {brick}: {record['outcome']}", flush=True)

    write_heartbeat(len(done), total, "COMPLETE", "-", started, window_pauses, 0.0)
    DONE_MARKER.write_text(json.dumps({"utc": utc_now(), "completed": len(done), "total": total}, indent=2) + "\n")
    print(f"HARVEST COMPLETE {len(done)}/{total}", flush=True)


if __name__ == "__main__":
    main()
