#!/usr/bin/env python3
"""Acquire the authorized Tier-C invvar-r or maskbits companion plane.

This is the companion-plane adaptation of the read-only pinned fetcher.  It
downloads no image-r files and requires the selected plane's published hash.
"""
import argparse
import concurrent.futures as cf
import hashlib
import json
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "tier_c_manifest_v1.json"
DEST = HERE / "bricks_tier_c"
QUARANTINE = HERE / "bricks_tier_c_quarantine"
BASE = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd"
UA = {"User-Agent": "NebulaMind-spin-parity/1.0 (academic; contact duhokim81@gmail.com)"}
SHA_RE = re.compile(r"([0-9a-f]{64})\s+(\S+)")
PLANES = ("invvar-r", "maskbits")


def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plane_filename(brick, plane):
    return f"legacysurvey-{brick}-{plane}.fits.fz"


def brick_url(brick, plane):
    return f"{BASE}/{brick[:3]}/{brick}/{plane_filename(brick, plane)}"


def checksum_url(brick):
    aaa = brick[:3]
    name = f"legacysurvey_dr10_south_coadd_{aaa}_{brick}.sha256sum"
    return f"{BASE}/{aaa}/{brick}/{name}"


def published_sha(brick, plane, timeout):
    """Return the selected plane's SHA from the canonical per-brick file."""
    url = checksum_url(brick)
    with urllib.request.urlopen(
            urllib.request.Request(url, headers=UA), timeout=timeout) as response:
        listing = response.read().decode("utf-8", "replace")
    wanted = plane_filename(brick, plane)
    matches = [sha for sha, filename in SHA_RE.findall(listing)
               if filename == wanted]
    if len(matches) != 1:
        raise RuntimeError(
            f"published checksum line count for {wanted}: {len(matches)}")
    return matches[0]


def fetch(brick, plane, timeout, retries=3):
    url = brick_url(brick, plane)
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(url, headers=UA), timeout=timeout) as response:
                return response.read(), url
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
            time.sleep(2 ** attempt)
    raise RuntimeError(f"{brick}: {type(last).__name__}: {last}")


def manifest_bricks(path):
    parsed = json.loads(path.read_text())
    if isinstance(parsed, list):
        bricks = parsed
    else:
        bricks = [record["brick"] for record in parsed["bricks"]]
    if len(bricks) != len(set(bricks)):
        raise ValueError("manifest bricks are not unique")
    return bricks


def run(args):
    bricks = manifest_bricks(args.manifest)
    journal = args.journal or HERE / f"tier_c_fetch_receipts_{args.plane}.jsonl"
    args.dest.mkdir(exist_ok=True)
    args.quarantine.mkdir(exist_ok=True)
    print(f"{len(bricks)} bricks in the authorized closure; destination {args.dest}")

    done = skipped = failed = 0
    t0 = time.time()
    lock = threading.Lock()
    todo = []
    published = {}
    for brick in bricks[args.start:]:
        out = args.dest / plane_filename(brick, args.plane)
        if out.exists():
            try:
                pub = published_sha(brick, args.plane, args.timeout)
                got = hashlib.sha256(out.read_bytes()).hexdigest()
                if got == pub:
                    skipped += 1
                    continue
                quarantine = args.quarantine / out.name
                if quarantine.exists():
                    quarantine = args.quarantine / f"{out.name}.{int(time.time_ns())}"
                out.replace(quarantine)
                published[brick] = pub
            except Exception:
                # Keep the existing file until its published checksum can be
                # obtained; the attempt below will journal the exact failure.
                pass
        todo.append(brick)
    print(f"{skipped} present and verified; {len(todo)} to fetch with {args.workers} workers")
    if args.limit:
        todo = todo[:args.limit]

    def one(brick):
        nonlocal done, failed
        out = args.dest / plane_filename(brick, args.plane)
        rec = {"utc": utc(), "brick": brick, "url": brick_url(brick, args.plane)}
        try:
            pub = published.get(brick) or published_sha(
                brick, args.plane, args.timeout)
            blob, _url = fetch(brick, args.plane, args.timeout)
            got = hashlib.sha256(blob).hexdigest()
            rec.update(bytes=len(blob), published_sha256=pub,
                       computed_sha256=got)
            if pub != got:
                quarantine = args.quarantine / out.name
                if quarantine.exists():
                    quarantine = args.quarantine / f"{out.name}.{int(time.time_ns())}"
                quarantine.write_bytes(blob)
                rec["verdict"] = "SHA-MISMATCH-QUARANTINED"
                result = "fail"
            else:
                tmp = out.with_suffix(out.suffix + f".part{threading.get_ident()}")
                tmp.write_bytes(blob)
                tmp.replace(out)
                rec["verdict"] = "OK"
                result = "ok"
        except Exception as exc:
            rec.update(verdict="FETCH-FAILED",
                       error=f"{type(exc).__name__}: {exc}")
            result = "fail"
        with lock:
            if result == "ok":
                done += 1
            else:
                failed += 1
            with journal.open("a") as stream:
                stream.write(json.dumps(rec, sort_keys=True) + "\n")
            attempted = done + failed
            if attempted % 100 == 0:
                gib = sum(path.stat().st_size
                          for path in args.dest.glob(f"*-{args.plane}.fits.fz")) / 2**30
                rate = attempted / max(time.time() - t0, 1) * 3600
                eta = (len(todo) - attempted) / max(rate, 1)
                print(f"  {done} fetched, {failed} failed | {gib:.1f} GiB | "
                      f"~{rate:.0f} bricks/hr | ETA {eta:.1f}h", flush=True)
        time.sleep(args.delay)
        return result

    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(one, todo))

    gib = sum(path.stat().st_size
              for path in args.dest.glob(f"*-{args.plane}.fits.fz")) / 2**30
    print(f"\nfetched {done} | skipped {skipped} | failed {failed} | "
          f"{gib:.2f} GiB on disk | journal {journal.name}")
    return 1 if failed and not done else 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--plane", required=True, choices=PLANES)
    parser.add_argument("--limit", type=int, default=0,
                        help="stop after N newly downloaded bricks (0 = all)")
    parser.add_argument("--delay", type=float, default=0.5,
                        help="seconds between bricks (politeness pacing)")
    parser.add_argument("--timeout", type=float, default=180.0)
    parser.add_argument("--start", type=int, default=0,
                        help="manifest index to start at")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--dest", type=Path, default=DEST)
    parser.add_argument("--journal", type=Path, default=None,
                        help="default: tier_c_fetch_receipts_<plane>.jsonl")
    parser.add_argument("--quarantine", type=Path, default=QUARANTINE,
                        help=argparse.SUPPRESS)
    return run(parser.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
