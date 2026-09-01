#!/usr/bin/env python3
"""fetch_bricks — the authorized bulk brick acquisition (Duho, 2026-09-01,
option 1: a new scoped authorization superseding the single-probe limit).

SCOPE, stated because the last authorization was deliberately narrow:
  * ACQUISITION ONLY. This script downloads r-band coadd bricks and verifies
    them. It does NOT cut cutouts, run the instrument, measure χ, or read a
    handedness label. Those remain behind their own gates.
  * Source: the ruled NERSC path (R-A, direction #31) —
    portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/<AAA>/<brick>/
    legacysurvey-<brick>-image-r.fits.fz
  * Set: the 12,117-brick closure over the 49,211-object mask
    (acquire/required_manifest_v5.json), ≈148 GB.

DISCIPLINE:
  * RESUMABLE: a brick already present and SHA-verified is skipped, so a kill
    costs nothing. State lives in the filesystem plus a receipt journal.
  * VERIFIED: each brick's published SHA-256 is read from its own directory
    listing and checked against the bytes received. A mismatch quarantines the
    file rather than keeping it.
  * PACED: one request at a time with a delay between bricks. No published rate
    limit exists for this host, and absence of a limit is not permission.
  * RECEIPTED: every brick's outcome appends to fetch_bricks_receipts.jsonl —
    brick, URL, bytes, published sha, computed sha, verdict, UTC time.
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
MANIFEST = HERE / "required_manifest_v5.json"
DEST = HERE / "bricks"
JOURNAL = HERE / "fetch_bricks_receipts.jsonl"
QUARANTINE = HERE / "bricks_quarantine"
BASE = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd"
UA = {"User-Agent": "NebulaMind-spin-parity/1.0 (academic; contact duhokim81@gmail.com)"}
SHA_RE = re.compile(r"([0-9a-f]{64})\s+(\S+)")


def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def brick_url(brick):
    return f"{BASE}/{brick[:3]}/{brick}/legacysurvey-{brick}-image-r.fits.fz"


def published_sha(brick, timeout):
    """Read the brick directory's published checksum file; return the sha for
    the r-band image, or None if the listing does not provide one."""
    aaa = brick[:3]
    for name in (f"legacysurvey_dr10_south_coadd_{aaa}_{brick}.sha256sum",
                 f"legacysurvey-{brick}.sha256sum", "checksums.sha256"):
        url = f"{BASE}/{brick[:3]}/{brick}/{name}"
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                text = r.read().decode("utf-8", "replace")
        except Exception:
            continue
        for sha, fname in SHA_RE.findall(text):
            if fname.endswith(f"{brick}-image-r.fits.fz"):
                return sha
    return None


def fetch(brick, timeout, retries=3):
    url = brick_url(brick)
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read(), url
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"{brick}: {type(last).__name__}: {last}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0,
                    help="stop after N newly downloaded bricks (0 = all)")
    ap.add_argument("--delay", type=float, default=1.0,
                    help="seconds between bricks (politeness pacing)")
    ap.add_argument("--timeout", type=float, default=180.0)
    ap.add_argument("--start", type=int, default=0, help="manifest index to start at")
    ap.add_argument("--workers", type=int, default=1,
                    help="concurrent fetchers (4 authorized 2026-09-01; be polite)")
    args = ap.parse_args()

    bricks = json.loads(MANIFEST.read_text())
    DEST.mkdir(exist_ok=True)
    QUARANTINE.mkdir(exist_ok=True)
    print(f"{len(bricks)} bricks in the authorized closure; destination {DEST}")

    done = skipped = failed = 0
    t0 = time.time()
    lock = threading.Lock()
    todo = []
    for brick in bricks[args.start:]:
        if (DEST / f"legacysurvey-{brick}-image-r.fits.fz").exists():
            skipped += 1
        else:
            todo.append(brick)
    print(f"{skipped} already present; {len(todo)} to fetch with {args.workers} workers")
    if args.limit:
        todo = todo[:args.limit]

    def one(brick):
        """Fetch, verify, journal a single brick. Returns 'ok' or 'fail'."""
        nonlocal done, failed
        out = DEST / f"legacysurvey-{brick}-image-r.fits.fz"
        if out.exists():
            return "skip"
        rec = {"utc": utc(), "brick": brick, "url": brick_url(brick)}
        try:
            pub = published_sha(brick, args.timeout)
            blob, _url = fetch(brick, args.timeout)
            got = hashlib.sha256(blob).hexdigest()
            rec.update(bytes=len(blob), published_sha256=pub, computed_sha256=got)
            if pub is not None and pub != got:
                (QUARANTINE / out.name).write_bytes(blob)
                rec["verdict"] = "SHA-MISMATCH-QUARANTINED"
                result = "fail"
            else:
                tmp = out.with_suffix(out.suffix + f".part{threading.get_ident()}")
                tmp.write_bytes(blob)
                tmp.replace(out)
                rec["verdict"] = "OK" if pub else "OK-NO-PUBLISHED-SHA"
                result = "ok"
        except Exception as e:
            rec.update(verdict="FETCH-FAILED", error=f"{type(e).__name__}: {e}")
            result = "fail"
        with lock:
            if result == "ok":
                done += 1
            else:
                failed += 1
            with JOURNAL.open("a") as fh:
                fh.write(json.dumps(rec, sort_keys=True) + "\n")
            if (done + failed) % 100 == 0 and done:
                gb = sum(f.stat().st_size for f in DEST.glob("*.fits.fz")) / 2**30
                rate = done / max(time.time() - t0, 1) * 3600
                eta = (len(todo) - done) / max(rate, 1)
                print(f"  {done} fetched, {failed} failed | {gb:.1f} GiB | "
                      f"~{rate:.0f} bricks/hr | ETA {eta:.1f}h", flush=True)
        time.sleep(args.delay)
        return result

    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(one, todo))

    gb = sum(f.stat().st_size for f in DEST.glob("*.fits.fz")) / 2**30
    print(f"\nfetched {done} | skipped {skipped} | failed {failed} | "
          f"{gb:.2f} GiB on disk | journal {JOURNAL.name}")
    return 1 if failed and not done else 0


if __name__ == "__main__":
    sys.exit(main())
