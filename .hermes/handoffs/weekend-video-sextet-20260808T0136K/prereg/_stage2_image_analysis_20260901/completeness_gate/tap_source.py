#!/usr/bin/env python3
"""Artifact-backed NOIRLab TAP source for the catalogue-only completeness gate."""
from __future__ import annotations

import argparse
import csv
import email.utils
import hashlib
import io
import json
import math
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import xml.etree.ElementTree as ET
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterable, Mapping, Sequence

from completeness_gate import (Candidate, CandidateSource, GateError, GZRecord,
                               PINNED_DIGESTS, read_gz_tables, separation_arcsec,
                               sha256_file)

DEFAULT_TAP = "https://datalab.noirlab.edu/tap"
TOTAL_ROWS = 893_212
CHUNK_SIZE = 1_000
POLL_SECONDS = 5.0
CREATE_INTERVAL_SECONDS = 2.0
SERVER_RADIUS_DEG = math.nextafter(1.0 / 3600.0, math.inf)
NS = {"v": "http://www.ivoa.net/xml/VOTable/v1.3"}


def _fail(message: str) -> None:
    raise GateError(f"COMPLETENESS-FAIL: {message}")


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_manifest(total_rows: int = TOTAL_ROWS,
                       chunk_size: int = CHUNK_SIZE) -> dict:
    if total_rows < 0 or chunk_size <= 0:
        _fail("invalid manifest dimensions")
    chunks = []
    for chunk_id, start in enumerate(range(0, total_rows, chunk_size)):
        stop = min(start + chunk_size, total_rows)
        chunks.append({"chunk_id": chunk_id, "start": start, "stop": stop,
                       "rows": stop - start})
    manifest = {"version": 1, "total_rows": total_rows,
                "chunk_size": chunk_size, "chunks": chunks}
    validate_manifest(manifest, total_rows)
    return manifest


def validate_manifest(manifest: Mapping[str, object], total_rows: int) -> None:
    observed: list[int] = []
    chunks = manifest.get("chunks")
    if not isinstance(chunks, list):
        _fail("manifest chunks is not a list")
    for expected_id, chunk in enumerate(chunks):
        if not isinstance(chunk, dict) or chunk.get("chunk_id") != expected_id:
            _fail("manifest chunk identifiers are not canonical")
        start, stop = chunk.get("start"), chunk.get("stop")
        if not isinstance(start, int) or not isinstance(stop, int):
            _fail("manifest bounds are not integers")
        if chunk.get("rows") != stop - start:
            _fail("manifest row count disagrees with bounds")
        observed.extend(range(start, stop))
    if observed != list(range(total_rows)):
        _fail("manifest input_index set is not exactly 0..N-1")


def write_manifest(path: Path, total_rows: int = TOTAL_ROWS) -> dict:
    manifest = canonical_manifest(total_rows)
    encoded = json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") != encoded:
        _fail("existing chunk manifest is not canonical")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(encoded, encoding="utf-8")
    return manifest


def votable_upload(records: Sequence[GZRecord]) -> bytes:
    root = ET.Element("VOTABLE", xmlns="http://www.ivoa.net/xml/VOTable/v1.3",
                      version="1.3")
    resource = ET.SubElement(root, "RESOURCE", type="results")
    table = ET.SubElement(resource, "TABLE", name="gz_chunk")
    for name, dtype in (("input_index", "long"), ("OBJID", "long"),
                        ("ra", "double"), ("dec", "double")):
        ET.SubElement(table, "FIELD", name=name, datatype=dtype)
    data = ET.SubElement(table, "DATA")
    tabledata = ET.SubElement(data, "TABLEDATA")
    for r in records:
        tr = ET.SubElement(tabledata, "TR")
        for value in (r.input_index, r.objid, repr(r.ra), repr(r.dec)):
            ET.SubElement(tr, "TD").text = str(value)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def make_adql(relation: str, include_ls_id: bool) -> str:
    selected = "t.release, t.brickid, t.objid, t.brickname, t.ra, t.dec"
    if include_ls_id:
        selected += ", t.ls_id"
    return f"""SELECT g.input_index, {selected}
FROM TAP_UPLOAD.gz_chunk AS g
JOIN {relation} AS t
  ON 1 = CONTAINS(
       POINT('ICRS', t.ra, t.dec),
       CIRCLE('ICRS', g.ra, g.dec, {SERVER_RADIUS_DEG!r}))
ORDER BY g.input_index, t.brickid, t.objid"""


def multipart(fields: Mapping[str, str], upload: bytes) -> tuple[bytes, str]:
    boundary = "----completeness-" + uuid.uuid4().hex
    out = io.BytesIO()
    for name, value in fields.items():
        out.write(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n".encode())
    out.write(f"--{boundary}\r\nContent-Disposition: form-data; name=\"gz_chunk\"; filename=\"gz_chunk.xml\"\r\nContent-Type: application/x-votable+xml\r\n\r\n".encode())
    out.write(upload)
    out.write(f"\r\n--{boundary}--\r\n".encode())
    return out.getvalue(), f"multipart/form-data; boundary={boundary}"


class HttpClient:
    def __init__(self, sleep: Callable[[float], None] = time.sleep,
                 rng: Callable[[], float] = random.random, max_retries: int = 6):
        self.sleep, self.rng, self.max_retries = sleep, rng, max_retries

    def request(self, url: str, *, method: str = "GET", data: bytes | None = None,
                headers: Mapping[str, str] | None = None) -> tuple[bytes, Mapping[str, str], str, int]:
        for attempt in range(self.max_retries + 1):
            req = urllib.request.Request(url, data=data, method=method,
                                         headers=dict(headers or {}))
            try:
                with urllib.request.urlopen(req, timeout=180) as response:
                    return response.read(), dict(response.headers), response.geturl(), response.status
            except urllib.error.HTTPError as exc:
                if exc.code != 429 and not 500 <= exc.code < 600:
                    raise
                if attempt == self.max_retries:
                    raise
                retry = exc.headers.get("Retry-After")
                delay = None
                if retry:
                    try:
                        delay = float(retry)
                    except ValueError:
                        dt = email.utils.parsedate_to_datetime(retry)
                        delay = max(0.0, dt.timestamp() - time.time())
                self.sleep(delay if delay is not None else (2 ** attempt) + self.rng())


def discover_async_endpoint(capabilities: bytes, requested_base: str) -> tuple[str, list[dict]]:
    root = ET.fromstring(capabilities)
    interfaces = []
    async_url = None
    for interface in root.iter():
        if interface.tag.rsplit("}", 1)[-1] != "interface":
            continue
        role = interface.attrib.get("role", "")
        itype = next((v for k, v in interface.attrib.items() if k.endswith("type")), "")
        urls = [e.text.strip() for e in interface.iter()
                if e.tag.rsplit("}", 1)[-1] == "accessURL" and e.text]
        interfaces.append({"role": role, "type": itype, "access_urls": urls})
        for url in urls:
            if role == "std" and url.rstrip("/").endswith("/async"):
                async_url = url.rstrip("/")
    if not async_url:
        # This service advertises a legacy /ivoa-dal base, not an async
        # accessURL. The operational UWS child belongs to the requested TAP
        # base; retain interfaces verbatim so the discrepancy is auditable.
        async_url = requested_base.rstrip("/") + "/async"
    return async_url, interfaces


def parse_votable(raw: bytes) -> tuple[list[dict[str, str]], dict]:
    root = ET.fromstring(raw)
    statuses = []
    for info in root.iter():
        if info.tag.rsplit("}", 1)[-1] == "INFO" and info.attrib.get("name", "").upper() == "QUERY_STATUS":
            statuses.append({"value": info.attrib.get("value", ""),
                             "text": (info.text or "").strip()})
    overflow = any(s["value"].upper() == "OVERFLOW" or "overflow" in s["text"].lower()
                   or "truncat" in s["text"].lower() for s in statuses)
    table = next((e for e in root.iter() if e.tag.rsplit("}", 1)[-1] == "TABLE"), None)
    if table is None:
        return [], {"query_status": statuses, "overflow": overflow}
    fields = [e.attrib.get("name", "") for e in table
              if e.tag.rsplit("}", 1)[-1] == "FIELD"]
    rows = []
    for tr in table.iter():
        if tr.tag.rsplit("}", 1)[-1] != "TR":
            continue
        vals = [(td.text or "") for td in tr if td.tag.rsplit("}", 1)[-1] == "TD"]
        rows.append(dict(zip(fields, vals)))
    return rows, {"query_status": statuses, "overflow": overflow}


def sync_query(client: HttpClient, sync_url: str, query: str) -> bytes:
    body = urllib.parse.urlencode({"REQUEST": "doQuery", "LANG": "ADQL",
                                  "FORMAT": "votable", "QUERY": query}).encode()
    raw, _, _, _ = client.request(sync_url, method="POST", data=body,
                                   headers={"Content-Type": "application/x-www-form-urlencoded"})
    return raw


def probe(base_url: str, output_dir: Path, client: HttpClient | None = None) -> dict:
    client = client or HttpClient()
    requested = base_url.rstrip("/")
    capabilities_url = requested + "/capabilities"
    caps, cap_headers, resolved_caps, _ = client.request(capabilities_url)
    async_url, interfaces = discover_async_endpoint(caps, requested)
    sync_url = requested + "/sync"
    tq = "SELECT table_name, description FROM TAP_SCHEMA.tables WHERE table_name IN ('ls_dr10.tractor','ls_dr10.tractor_s') ORDER BY table_name"
    table_rows, table_status = parse_votable(sync_query(client, sync_url, tq))
    found = {r.get("table_name", "").lower(): r for r in table_rows}
    if "ls_dr10.tractor_s" not in found:
        _fail("complete south relation ls_dr10.tractor_s not exposed by TAP_SCHEMA")
    relation = "ls_dr10.tractor_s"
    cq = f"SELECT column_name, datatype, description FROM TAP_SCHEMA.columns WHERE table_name='{relation}' ORDER BY column_name"
    column_rows, column_status = parse_votable(sync_query(client, sync_url, cq))
    cols = [r.get("column_name", "").lower() for r in column_rows]
    required = {"release", "brickid", "objid", "brickname", "ra", "dec"}
    if not required.issubset(cols):
        _fail("selected Tractor relation lacks required identity/position columns")
    # TAP_SCHEMA has no standard row-count field. Check for a service extension,
    # otherwise record null rather than issuing a catalogue COUNT during the probe.
    row_count = None
    row_count_source = "not exposed by TAP_SCHEMA.tables"
    for key in ("nrows", "row_count", "rows"):
        if found[relation].get(key):
            row_count = int(found[relation][key])
            row_count_source = f"TAP_SCHEMA.tables.{key}"
    if row_count is None:
        match = re.search(r"\(([0-9,]+) rows\)", found[relation].get("description", ""))
        if match:
            row_count = int(match.group(1).replace(",", ""))
            row_count_source = "TAP_SCHEMA.tables.description parenthetical row count"
    cap_hints = []
    cap_text = caps.decode("utf-8", "replace")
    for pattern in (r"(?is)<outputLimit.*?</outputLimit>", r"(?is)<executionDuration.*?</executionDuration>"):
        cap_hints.extend(re.sub(r"\s+", " ", x).strip() for x in re.findall(pattern, cap_text))
    receipt = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "requested_tap_base": requested, "capabilities_url": resolved_caps,
        "capabilities_sha256": sha256_bytes(caps), "capabilities_headers": dict(cap_headers),
        "async_endpoint": async_url, "interfaces": interfaces,
        "relation": relation,
        "relation_justification": "The explicit south-only Tractor relation is exposed and is the complete DR10-south relation; the unsuffixed relation is not substituted.",
        "tap_schema_tables": table_rows, "columns": column_rows,
        "row_count": row_count, "row_count_source": row_count_source,
        "result_cap_hints": cap_hints or ["none found in capabilities document"],
        "metadata_query_status": [table_status, column_status],
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"probe_receipt_{utc_stamp()}.json"
    path.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    receipt["receipt_path"] = str(path)
    return receipt


class TAPCandidateSource(CandidateSource):
    """One-worker async TAP runner backed by immutable chunk artifacts."""
    def __init__(self, async_url: str, relation: str, columns: Iterable[str],
                 artifacts: Path, *, client: HttpClient | None = None,
                 poll_seconds: float = POLL_SECONDS,
                 create_interval: float = CREATE_INTERVAL_SECONDS):
        self.async_url, self.relation = async_url.rstrip("/"), relation
        self.columns = {c.lower() for c in columns}
        self.artifacts = artifacts
        self.client = client or HttpClient()
        self.poll_seconds, self.create_interval = poll_seconds, create_interval
        self._last_creation = 0.0
        self._results: dict[int, list[Candidate]] = {}

    @property
    def provenance(self) -> Mapping[str, object]:
        return {"backend": "NOIRLab-Astro-Data-Lab-async-TAP",
                "release_identity": self.relation,
                "enumeration": "complete-all-candidates", "query_artifacts": [],
                "magnitude_predicate": False, "truncated": False,
                "async_endpoint": self.async_url}

    def _checkpoint_entries(self) -> list[dict]:
        path = self.artifacts / "checkpoint.jsonl"
        if not path.exists():
            return []
        entries = [json.loads(line) for line in path.read_text().splitlines() if line]
        for entry in entries:
            raw_path = self.artifacts / entry["raw_result"]
            if not raw_path.exists() or sha256_file(raw_path) != entry["raw_sha256"]:
                _fail(f"resume hash mismatch for chunk {entry['chunk_id']}")
        return entries

    def run_chunk(self, chunk_id: int, records: Sequence[GZRecord]) -> dict:
        self.artifacts.mkdir(parents=True, exist_ok=True)
        entries = self._checkpoint_entries()
        completed = [e for e in entries if e["chunk_id"] == chunk_id]
        if len(completed) > 1:
            _fail(f"multiple successful checkpoint entries for chunk {chunk_id}")
        if completed:
            return completed[0] | {"resumed": True}
        expected = list(range(records[0].input_index, records[0].input_index + len(records))) if records else []
        if [r.input_index for r in records] != expected:
            _fail("chunk input_index sequence is not contiguous")
        attempt = f"chunk_{chunk_id:04d}_{utc_stamp()}"
        attempt_dir = self.artifacts / attempt
        attempt_dir.mkdir()
        upload = votable_upload(records)
        query = make_adql(self.relation, "ls_id" in self.columns)
        (attempt_dir / "upload.xml").write_bytes(upload)
        (attempt_dir / "query.adql").write_text(query + "\n", encoding="utf-8")
        wait = self.create_interval - (time.monotonic() - self._last_creation)
        if wait > 0:
            self.client.sleep(wait)
        fields = {"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "votable",
                  "QUERY": query, "UPLOAD": "gz_chunk,param:gz_chunk", "PHASE": "RUN"}
        body, ctype = multipart(fields, upload)
        started = time.monotonic()
        submit_raw, headers, final_url, submit_status = self.client.request(
            self.async_url, method="POST", data=body, headers={"Content-Type": ctype})
        self._last_creation = time.monotonic()
        (attempt_dir / "submission_response.bin").write_bytes(submit_raw)
        (attempt_dir / "submission.json").write_text(json.dumps({
            "status": submit_status, "headers": dict(headers), "final_url": final_url,
            "response_sha256": sha256_bytes(submit_raw)}, sort_keys=True, indent=2) + "\n")
        job_url = headers.get("Location") or final_url
        if not job_url.startswith("http"):
            job_url = urllib.parse.urljoin(self.async_url + "/", job_url)
        job_id = job_url.rstrip("/").rsplit("/", 1)[-1]
        if job_url.rstrip("/") == self.async_url or not headers.get("Location"):
            _fail("async TAP submission returned no UWS job Location")
        phases = []
        while True:
            phase_raw, _, _, _ = self.client.request(job_url.rstrip("/") + "/phase")
            phase = phase_raw.decode("utf-8", "replace").strip().upper()
            if phase not in {"PENDING", "QUEUED", "EXECUTING", "COMPLETED", "ERROR", "ABORTED", "UNKNOWN", "HELD", "SUSPENDED"}:
                _fail(f"TAP job {job_id} returned invalid UWS phase")
            phases.append({"at_utc": datetime.now(timezone.utc).isoformat(), "phase": phase})
            if phase in {"COMPLETED", "ERROR", "ABORTED"}:
                break
            self.client.sleep(max(5.0, self.poll_seconds))
        if phase != "COMPLETED":
            _fail(f"TAP job {job_id} ended in phase {phase}")
        raw, result_headers, _, _ = self.client.request(job_url.rstrip("/") + "/results/result")
        rows, status = parse_votable(raw)
        (attempt_dir / "phase_log.json").write_text(json.dumps(phases, indent=2) + "\n")
        (attempt_dir / "result.vot").write_bytes(raw)
        if status["overflow"]:
            _fail(f"TAP result overflow/truncation for chunk {chunk_id}")
        clean = []
        by_index = {r.input_index: r for r in records}
        for row in rows:
            idx = int(row["input_index"])
            if idx not in by_index:
                _fail("TAP returned unknown input_index")
            c = Candidate(int(row["release"]), int(row["brickid"]), int(row["objid"]),
                          float(row["ra"]), float(row["dec"]), row.get("brickname", ""))
            if separation_arcsec(by_index[idx].ra, by_index[idx].dec, c.ra, c.dec) <= 1.0:
                clean.append((idx, c))
        metadata = {"chunk_id": chunk_id, "attempt": attempt, "job_id": job_id,
                    "job_url": job_url, "rows_in": len(records),
                    "service_row_count": len(rows), "client_row_count": len(clean),
                    "overflow": False, "query_status": status["query_status"],
                    "result_headers": dict(result_headers), "phase_log": phases,
                    "wall_s": time.monotonic() - started,
                    "raw_result": f"{attempt}/result.vot", "raw_sha256": sha256_bytes(raw)}
        (attempt_dir / "metadata.json").write_text(json.dumps(metadata, sort_keys=True, indent=2) + "\n")
        with (self.artifacts / "checkpoint.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(metadata, sort_keys=True, separators=(",", ":")) + "\n")
            f.flush(); os.fsync(f.fileno())
        for idx, c in clean:
            self._results.setdefault(idx, []).append(c)
        return metadata

    def candidates(self, record: GZRecord, radius_arcsec: float) -> Sequence[Candidate]:
        if radius_arcsec != 1.0:
            _fail("TAP source is fixed at the preregistered 1.0 arcsec radius")
        return tuple(self._results.get(record.input_index, ()))


def load_probe(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("probe")
    p.add_argument("--tap-base", default=DEFAULT_TAP)
    p.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
    d = sub.add_parser("dry-run-chunk")
    d.add_argument("--probe-receipt", type=Path, required=True)
    d.add_argument("--table2", type=Path, default=Path(__file__).parent.parent / "scratch/gz1_t2.csv.gz")
    d.add_argument("--table3", type=Path, default=Path(__file__).parent.parent / "scratch/gz1_t3.csv.gz")
    d.add_argument("--rows", type=int, choices=(50, 1000), default=50)
    d.add_argument("--artifacts", type=Path, default=Path(__file__).parent / "artifacts")
    args = parser.parse_args(argv)
    if args.command == "probe":
        receipt = probe(args.tap_base, args.output_dir)
        print(json.dumps(receipt, sort_keys=True))
        return 0
    for name, path in (("table2", args.table2), ("table3", args.table3)):
        if sha256_file(path) != PINNED_DIGESTS[name]:
            _fail(f"pinned input hash mismatch: {name}")
    rows = read_gz_tables([args.table2, args.table3])
    if len(rows) != TOTAL_ROWS or [r.input_index for r in rows] != list(range(TOTAL_ROWS)):
        _fail("pinned GZ1 input_index set is not exactly 0..893211")
    write_manifest(args.artifacts / "chunk_manifest.json")
    receipt = load_probe(args.probe_receipt)
    columns = [r["column_name"] for r in receipt["columns"]]
    source = TAPCandidateSource(receipt["async_endpoint"], receipt["relation"], columns,
                                args.artifacts)
    result = source.run_chunk(0, rows[:args.rows])
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
