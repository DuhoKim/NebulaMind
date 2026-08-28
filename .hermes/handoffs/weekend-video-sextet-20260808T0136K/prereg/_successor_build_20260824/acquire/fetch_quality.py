#!/usr/bin/env python3
"""Catalogue positions for the selected bricks. CATALOG ONLY — no images, no chi.

Async TAP at NOIRLab Astro Data Lab, the same service and pattern the predecessor's grouped
count run used. Chunked by brickid IN-lists, paced, every response digested and receipted,
with a hard cap on result bytes and on the number of chunks.
"""
import csv, hashlib, io, json, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ENDPOINT = "https://datalab.noirlab.edu/tap/async"
UWS = "{http://www.ivoa.net/xml/UWS/v1.0}"
XLINK = "{http://www.w3.org/1999/xlink}href"
HERE = Path(__file__).resolve().parent
CHUNK = 500                      # brickids per query
PACE_S = 12.0                    # between submissions — the service drops jobs under load
CHUNK_ATTEMPTS = 4               # a lost/404 job is resubmitted, not fatal
MAX_CHUNKS = 20                  # 6,445 / 500 = 13; a hard stop well above it
MAX_BYTES_PER_CHUNK = 20_000_000
COLUMNS = ["ls_id", "brickid", "objid", "flux_ivar_r", "psfsize_r", "nobs_r"]

TEMPLATE = (HERE / "quality_query.adql").read_text()


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


SERVICE_PRESSURE = {429, 500, 502, 503, 504}
MAX_RETRIES = 6


def _with_backoff(fn, what):
    """The service returns 502/503 under load. Back off rather than hammer it (and rather than
    lose the run, as a first version did on chunk 3)."""
    delay = 15.0
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return fn()
        except urllib.error.HTTPError as e:
            if e.code not in SERVICE_PRESSURE or attempt == MAX_RETRIES:
                raise
            print(f"      service pressure HTTP {e.code} on {what}; "
                  f"retry {attempt}/{MAX_RETRIES - 1} in {delay:.0f}s", flush=True)
        except urllib.error.URLError as e:
            if attempt == MAX_RETRIES:
                raise
            print(f"      transport error on {what}: {e.reason}; "
                  f"retry {attempt}/{MAX_RETRIES - 1} in {delay:.0f}s", flush=True)
        time.sleep(delay)
        delay = min(delay * 2, 240.0)


def post(url, data):
    def _do():
        body = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(url, data=body, method="POST")
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, r.geturl(), r.read(), {k.lower(): v for k, v in r.headers.items()}
    return _with_backoff(_do, f"POST {url.rsplit('/', 1)[-1]}")


def get(url):
    def _do():
        with urllib.request.urlopen(urllib.request.Request(url), timeout=180) as r:
            return r.status, r.read()
    return _with_backoff(_do, f"GET {url.rsplit('/', 1)[-1]}")


def run_chunk(bricks, idx, receipts):
    q = TEMPLATE.replace("t.brickid BETWEEN {lo} AND {hi}",
                         "t.brickid IN (" + ",".join(str(int(b)) for b in bricks) + ")")
    st, final, payload, hdrs = post(ENDPOINT, {"REQUEST": "doQuery", "LANG": "ADQL",
                                               "FORMAT": "csv", "phase": "RUN", "QUERY": q})
    if st not in (200, 201, 303):
        raise RuntimeError(f"chunk {idx}: create status {st}")
    job = hdrs.get("location", final).rstrip("/")
    if "/tap/async/" not in job:
        raise RuntimeError(f"chunk {idx}: unexpected job url {job}")
    # A created job can sit at PENDING; it must be told to RUN. (The predecessor's runner does
    # this explicitly; my first version only set phase=RUN in the create form and every job
    # stayed PENDING until the poll gave up.)
    _s, body0 = get(job + "/phase")
    if body0.decode().strip() == "PENDING":
        post(job + "/phase", {"PHASE": "RUN"})
    phase = "PENDING"
    for _ in range(240):
        time.sleep(2.0)
        _s, body = get(job)
        phase = ET.fromstring(body).find(f"{UWS}phase").text
        if phase in ("COMPLETED", "ERROR", "ABORTED"):
            break
    if phase != "COMPLETED":
        raise RuntimeError(f"chunk {idx}: terminal phase {phase}")
    _s, res = get(job + "/results/result")
    if len(res) > MAX_BYTES_PER_CHUNK:
        raise RuntimeError(f"chunk {idx}: result {len(res)} bytes over cap")
    text = res.decode()
    rows = list(csv.DictReader(io.StringIO(text)))
    if rows and list(rows[0].keys()) != COLUMNS:
        raise RuntimeError(f"chunk {idx}: columns {list(rows[0].keys())} != {COLUMNS}")
    receipts.append({"chunk": idx, "utc": utc(), "job": job, "bricks": len(bricks),
                     "rows": len(rows), "bytes": len(res),
                     "query_sha256": hashlib.sha256(q.encode()).hexdigest(),
                     "result_sha256": hashlib.sha256(res).hexdigest()})
    return rows


def main():
    bricks = [int(x) for x in (HERE / "selected_brickids.txt").read_text().split()]
    chunks = [bricks[i:i + CHUNK] for i in range(0, len(bricks), CHUNK)]
    if len(chunks) > MAX_CHUNKS:
        raise SystemExit(f"{len(chunks)} chunks exceeds the cap {MAX_CHUNKS}")
    print(f"{len(bricks):,} bricks in {len(chunks)} chunks of <= {CHUNK}", flush=True)
    ckpt = HERE / "_quality_chunks"
    ckpt.mkdir(exist_ok=True)
    all_rows, receipts = [], []
    for i, ch in enumerate(chunks, 1):
        cf, rf = ckpt / f"chunk_{i:03d}.json", ckpt / f"receipt_{i:03d}.json"
        if cf.exists() and rf.exists():
            rows = json.loads(cf.read_text())
            receipts.append(json.loads(rf.read_text()))
            all_rows.extend(rows)
            print(f"  chunk {i}/{len(chunks)}: {len(rows):,} rows (checkpoint, "
                  f"total {len(all_rows):,})", flush=True)
            continue
        t0 = time.time()
        rows = None
        for attempt in range(1, CHUNK_ATTEMPTS + 1):
            try:
                rows = run_chunk(ch, i, receipts)
                break
            except Exception as exc:
                # A 404 while polling means the service dropped the job (the predecessor's
                # runner names this REMOTE_JOB_LOST). Resubmit rather than lose the run.
                if attempt == CHUNK_ATTEMPTS:
                    raise
                wait = 60.0 * attempt
                print(f"      chunk {i} attempt {attempt} failed ({type(exc).__name__}: "
                      f"{str(exc)[:70]}); resubmitting in {wait:.0f}s", flush=True)
                time.sleep(wait)
        cf.write_text(json.dumps(rows))
        rf.write_text(json.dumps(receipts[-1]))
        all_rows.extend(rows)
        print(f"  chunk {i}/{len(chunks)}: {len(rows):,} rows "
              f"({time.time()-t0:.0f}s, total {len(all_rows):,})", flush=True)
        time.sleep(PACE_S)
    out = HERE / "quality_selected.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(all_rows)
    (HERE / "quality_receipts.json").write_text(json.dumps(
        {"utc": utc(), "endpoint": ENDPOINT, "chunks": receipts,
         "total_rows": len(all_rows), "bricks": len(bricks),
         "output_sha256": hashlib.sha256(out.read_bytes()).hexdigest()}, indent=2) + "\n")
    print(f"\nwrote {out.name}: {len(all_rows):,} rows")


if __name__ == "__main__":
    main()
