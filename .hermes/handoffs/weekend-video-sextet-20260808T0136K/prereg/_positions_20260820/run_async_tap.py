#!/usr/bin/env python3
"""Submit one NOIRLab Data Lab async TAP job, poll to terminal state, then retrieve CSV."""

import argparse
import csv
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

ENDPOINT = "https://datalab.noirlab.edu/tap/async"
TERMINAL_PHASES = {"COMPLETED", "ERROR", "ABORTED"}
TRANSIENT_HTTP = {429, 502, 503, 504}
UWS = "{http://www.ivoa.net/xml/UWS/v1.0}"
XLINK = "{http://www.w3.org/1999/xlink}href"


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def request(url, data=None, timeout=180, stream_to=None):
    body = urllib.parse.urlencode(data).encode("utf-8") if data is not None else None
    headers = {"User-Agent": "NebulaMind-GPT1-position-custody/1.0"}
    for attempt in range(1, 9):
        req = urllib.request.Request(url, data=body, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                response_headers = {k.lower(): v for k, v in response.headers.items()}
                if stream_to is None:
                    payload = response.read()
                else:
                    with stream_to.open("wb") as output:
                        while True:
                            block = response.read(1024 * 1024)
                            if not block:
                                break
                            output.write(block)
                    payload = b""
                return response.status, response.geturl(), response_headers, payload
        except urllib.error.HTTPError as exc:
            payload = exc.read()
            if exc.code not in TRANSIENT_HTTP or attempt == 8:
                raise RuntimeError("HTTP {} for {}: {!r}".format(exc.code, url, payload[:2000])) from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == 8:
                raise
        time.sleep(min(15 * attempt, 60))
    raise AssertionError("unreachable")


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=Path)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--output-name", default="result.csv")
    parser.add_argument("--poll-seconds", type=float, default=15.0)
    parser.add_argument("--max-wait-seconds", type=int, default=21600)
    args = parser.parse_args()

    args.run_dir.mkdir(parents=True, exist_ok=False)
    query_bytes = args.query.read_bytes()
    query_text = query_bytes.decode("utf-8")
    if "portal.nersc.gov" in query_text or "datalab.noirlab.edu" in query_text:
        raise RuntimeError("query text contains a network route; only table ADQL is permitted")
    (args.run_dir / "query.adql").write_bytes(query_bytes)
    query_sha = hashlib.sha256(query_bytes).hexdigest()
    submitted_utc = utc_now()

    status, final_url, headers, _ = request(
        ENDPOINT,
        data={
            "REQUEST": "doQuery",
            "LANG": "ADQL",
            "FORMAT": "csv",
            "QUERY": query_text,
        },
    )
    if status not in (200, 201, 303):
        raise RuntimeError("unexpected submit status {}".format(status))
    job_url = headers.get("location", final_url).rstrip("/")
    if not job_url.startswith(ENDPOINT + "/"):
        raise RuntimeError("unexpected job URL {}".format(job_url))
    write_json(
        args.run_dir / "submission.json",
        {
            "endpoint": ENDPOINT,
            "job_url": job_url,
            "query_bytes": len(query_bytes),
            "query_sha256": query_sha,
            "submitted_utc": submitted_utc,
        },
    )

    _, _, _, phase_payload = request(job_url + "/phase")
    phase = phase_payload.decode("utf-8").strip()
    if phase == "PENDING":
        request(job_url + "/phase", data={"PHASE": "RUN"})

    poll_path = args.run_dir / "poll_log.jsonl"
    deadline = time.monotonic() + args.max_wait_seconds
    terminal_utc = None
    while True:
        _, _, _, phase_payload = request(job_url + "/phase")
        phase = phase_payload.decode("utf-8").strip()
        event = {"phase": phase, "timestamp_utc": utc_now()}
        with poll_path.open("a", encoding="utf-8") as log:
            log.write(json.dumps(event, sort_keys=True) + "\n")
        print(json.dumps({"job_url": job_url, **event}, sort_keys=True), flush=True)
        if phase in TERMINAL_PHASES:
            terminal_utc = event["timestamp_utc"]
            break
        if time.monotonic() >= deadline:
            raise TimeoutError("job {} still {} after timeout".format(job_url, phase))
        time.sleep(args.poll_seconds)

    _, _, _, job_xml = request(job_url)
    (args.run_dir / "job.xml").write_bytes(job_xml)
    if phase != "COMPLETED":
        write_json(
            args.run_dir / "terminal.json",
            {
                "job_url": job_url,
                "phase": phase,
                "submitted_utc": submitted_utc,
                "terminal_utc": terminal_utc,
            },
        )
        raise RuntimeError("job ended {}: {!r}".format(phase, job_xml[:4000]))

    root = ET.fromstring(job_xml)
    result_node = root.find("{}results/{}result".format(UWS, UWS))
    if result_node is not None and XLINK in result_node.attrib:
        result_url = urljoin(job_url + "/", result_node.attrib[XLINK])
    else:
        result_url = job_url + "/results/result"
    output_path = args.run_dir / args.output_name
    request(result_url, timeout=1200, stream_to=output_path)

    with output_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        row_count = sum(1 for _ in reader)
    completed_utc = utc_now()
    receipt = {
        "completed_utc": completed_utc,
        "endpoint": ENDPOINT,
        "header": header,
        "job_url": job_url,
        "output_bytes": output_path.stat().st_size,
        "output_path": str(output_path.resolve()),
        "output_sha256": sha256_file(output_path),
        "phase": phase,
        "query_sha256": query_sha,
        "result_row_count": row_count,
        "result_url": result_url,
        "submitted_utc": submitted_utc,
        "terminal_utc": terminal_utc,
    }
    write_json(args.run_dir / "receipt.json", receipt)
    print(json.dumps(receipt, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
