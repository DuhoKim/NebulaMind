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
PACE_S = 3.0                     # between submissions
MAX_CHUNKS = 20                  # 6,445 / 500 = 13; a hard stop well above it
MAX_BYTES_PER_CHUNK = 20_000_000
COLUMNS = ["ls_id", "brickid", "objid", "ra", "dec"]

TEMPLATE = (HERE / "positions_query.adql").read_text()


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def post(url, data):
    body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status, r.geturl(), r.read(), {k.lower(): v for k, v in r.headers.items()}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url), timeout=180) as r:
        return r.status, r.read()


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
    all_rows, receipts = [], []
    for i, ch in enumerate(chunks, 1):
        t0 = time.time()
        rows = run_chunk(ch, i, receipts)
        all_rows.extend(rows)
        print(f"  chunk {i}/{len(chunks)}: {len(rows):,} rows "
              f"({time.time()-t0:.0f}s, total {len(all_rows):,})", flush=True)
        time.sleep(PACE_S)
    out = HERE / "positions_selected.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(all_rows)
    (HERE / "positions_receipts.json").write_text(json.dumps(
        {"utc": utc(), "endpoint": ENDPOINT, "chunks": receipts,
         "total_rows": len(all_rows), "bricks": len(bricks),
         "output_sha256": hashlib.sha256(out.read_bytes()).hexdigest()}, indent=2) + "\n")
    print(f"\nwrote {out.name}: {len(all_rows):,} rows")


if __name__ == "__main__":
    main()
