#!/usr/bin/env python3
"""One/two-worker, resumable executor and finalizer for the completeness gate."""
from __future__ import annotations

import argparse
import queue
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from completeness_gate import (GateError, PINNED_DIGESTS, run_pinned_files,
                               sha256_file)
from tap_source import (CHUNK_SIZE, CREATE_INTERVAL_SECONDS, DEFAULT_TAP, TOTAL_ROWS, HttpClient,
                        OutageBudgetExhausted, TAPCandidateSource, load_probe,
                        append_jsonl, probe, read_checkpoint, read_gz_tables, validate_manifest,
                        write_manifest)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULTS = {
    "table2": ROOT / "scratch/gz1_t2.csv.gz",
    "table3": ROOT / "scratch/gz1_t3.csv.gz",
    "tier_a": ROOT.parent / "_successor_build_20260824/acquire/positions_selected_cut.csv",
    "parent": ROOT.parent / "_successor_build_20260824/acquire/positions_selected.csv",
    "prior": HERE / "prior_unresolved_13725.json",
    "artifacts": HERE / "artifacts_full",
}


def fail(message: str) -> None:
    raise GateError(f"COMPLETENESS-FAIL: {message}")


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_prior(path: Path, expected: int = 13_725) -> tuple[list[int], str, Mapping[str, object]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("objids"), list):
        fail("prior-unresolved file has invalid schema")
    objids = raw["objids"]
    if any(not isinstance(x, int) or isinstance(x, bool) for x in objids):
        fail("prior-unresolved OBJID is not an integer")
    if len(objids) != expected:
        fail(f"expected {expected} prior-unresolved OBJIDs, got {len(objids)}")
    if len(set(objids)) != expected:
        fail("duplicate prior-unresolved OBJID")
    return objids, sha256_file(path), raw.get("provenance", {})


def _checkpoint_map(artifacts: Path, manifest: Mapping[str, object],
                    repair_tail: bool = False) -> dict[int, dict]:
    path = artifacts / "checkpoint.jsonl"
    entries = read_checkpoint(path, repair_tail=repair_tail,
                              run_log=artifacts / "run.log.jsonl")
    allowed = {c["chunk_id"]: c for c in manifest["chunks"]}
    out: dict[int, dict] = {}
    for entry in entries:
        cid = entry.get("chunk_id")
        if cid not in allowed:
            fail(f"checkpoint contains unknown chunk {cid}")
        if cid in out:
            fail(f"every chunk must be admitted exactly once; duplicate chunk {cid}")
        raw = artifacts / entry.get("raw_result", "")
        if not raw.is_file() or sha256_file(raw) != entry.get("raw_sha256"):
            fail(f"resume hash mismatch for chunk {cid}")
        chunk = allowed[cid]
        if entry.get("rows_in") != chunk["rows"]:
            fail(f"checkpoint rows disagree with manifest for chunk {cid}")
        out[cid] = entry
    return out


def _gap(manifest: Mapping[str, object], admitted: Mapping[int, dict]) -> dict:
    missing = [c["chunk_id"] for c in manifest["chunks"] if c["chunk_id"] not in admitted]
    covered = []
    for c in manifest["chunks"]:
        if c["chunk_id"] in admitted:
            covered.extend(range(c["start"], c["stop"]))
    total = int(manifest["total_rows"])
    missing_summary = None if not missing else {"count": len(missing), "first": missing[0], "last": missing[-1]}
    return {"admitted_chunks": len(admitted), "expected_chunks": len(manifest["chunks"]),
            "covered_input_indices": len(covered), "expected_input_indices": total,
            "missing_chunks": missing_summary, "complete": covered == list(range(total))}


def execute(*, table2: Path, table3: Path, tier_a: Path, parent: Path,
            prior: Path, artifacts: Path, tap_base: str = DEFAULT_TAP,
            probe_receipt: Path | None = None, max_chunks: int | None = None,
            resume: bool = False, dry_finalise: bool = False,
            workers: int = 1,
            total_rows: int = TOTAL_ROWS, chunk_size: int = CHUNK_SIZE,
            expected_prior: int = 13_725, client: HttpClient | None = None) -> dict:
    if workers not in (1, 2):
        fail("workers must be 1 or 2")
    started = time.monotonic()
    paths = {"table2": table2, "table3": table3, "tier_a": tier_a, "parent": parent}
    for name, path in paths.items():
        expected = PINNED_DIGESTS.get(name)
        if total_rows == TOTAL_ROWS and expected and sha256_file(path) != expected:
            fail(f"pinned input hash mismatch: {name}")
    records = read_gz_tables([table2, table3])
    if len(records) != total_rows or [r.input_index for r in records] != list(range(total_rows)):
        fail(f"pinned GZ1 input_index set is not exactly 0..{total_rows - 1}")
    prior_ids, prior_sha, prior_prov = load_prior(prior, expected_prior)
    manifest = write_manifest(artifacts / "chunk_manifest.json", total_rows, chunk_size)
    validate_manifest(manifest, total_rows)
    admitted = _checkpoint_map(artifacts, manifest, repair_tail=resume)
    if admitted and not (resume or dry_finalise):
        fail("checkpoint exists; use --resume")

    if dry_finalise:
        gap = _gap(manifest, admitted)
        if not gap["complete"]:
            fail("dry-finalise gap: " + json.dumps(gap, sort_keys=True, separators=(",", ":")))
    else:
        if probe_receipt:
            pr = load_probe(probe_receipt)
        else:
            pr = probe(tap_base, artifacts / "probe", client=client)
        sync = pr.get("advertised_sync_endpoint")
        if not sync:
            fail("capabilities/probe receipt lacks advertised TAP sync endpoint")
        columns = [r["column_name"] for r in pr["columns"]]
        todo = [c for c in manifest["chunks"] if c["chunk_id"] not in admitted]
        if max_chunks is not None:
            todo = todo[:max_chunks]
        append_jsonl(artifacts / "run.log.jsonl", {"event": "worker_mode",
                     "workers": workers, "timestamp_utc": datetime.now(timezone.utc).isoformat()})
        pending_lock = threading.Lock()
        creation_lock = threading.Lock()
        last_creation = [0.0]
        state = {"next": 0, "active_workers": workers, "stop": False}
        completed: queue.Queue[tuple[str, object]] = queue.Queue()

        def downgrade(detail: Mapping[str, object]) -> None:
            with pending_lock:
                if state["active_workers"] == 1:
                    return
                state["active_workers"] = 1
            append_jsonl(artifacts / "run.log.jsonl", {"event": "workers_downgraded",
                         "from_workers": 2, "to_workers": 1, **detail,
                         "timestamp_utc": datetime.now(timezone.utc).isoformat()})

        if client is not None:
            previous_retryable = client.on_retryable
            def on_retryable(detail: Mapping[str, object]) -> None:
                downgrade(detail)
                if previous_retryable is not None:
                    previous_retryable(detail)
            client.on_retryable = on_retryable

        def pace_request() -> None:
            with creation_lock:
                wait = CREATE_INTERVAL_SECONDS - (time.monotonic() - last_creation[0])
                if wait > 0:
                    (client.sleep if client is not None else time.sleep)(wait)
                last_creation[0] = time.monotonic()

        def fetcher(worker_id: int) -> None:
            source = TAPCandidateSource(sync, pr["relation"], columns, artifacts,
                                        client=client, before_request=pace_request)
            if client is None:
                source.client.on_retryable = downgrade
            while True:
                with pending_lock:
                    if (state["stop"] or worker_id >= state["active_workers"]
                            or state["next"] >= len(todo)):
                        return
                    chunk = todo[state["next"]]
                    state["next"] += 1
                try:
                    metadata = source.fetch_chunk(
                        chunk["chunk_id"], records[chunk["start"]:chunk["stop"]])
                    completed.put(("ok", metadata))
                except BaseException as exc:
                    with pending_lock:
                        state["stop"] = True
                    completed.put(("error", exc))
                    return

        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(fetcher, worker_id) for worker_id in range(workers)]
            written = 0
            while written < len(todo):
                kind, value = completed.get()
                if kind == "error":
                    raise value
                append_jsonl(artifacts / "checkpoint.jsonl", value)
                written += 1
            for future in futures:
                future.result()
        admitted = _checkpoint_map(artifacts, manifest)
        gap = _gap(manifest, admitted)
        if not gap["complete"]:
            return {"status": "BOUNDED", "gap": gap, "prior_sha256": prior_sha,
                    "chunks_run": len(todo), "rows_out": sum(x.get("client_row_count", 0) for x in admitted.values()),
                    "wall_s": time.monotonic() - started}

    # Reconstruct every admitted chunk from its hash-verified raw bytes.
    if probe_receipt:
        pr = load_probe(probe_receipt)
    elif dry_finalise:
        receipts = sorted((artifacts / "probe").glob("probe_receipt_*.json"))
        if not receipts:
            fail("no capabilities-derived probe receipt available for finalisation")
        pr = load_probe(receipts[-1])
    sync = pr.get("advertised_sync_endpoint")
    if not sync:
        fail("capabilities/probe receipt lacks advertised TAP sync endpoint")
    source = TAPCandidateSource(sync, pr["relation"], [r["column_name"] for r in pr["columns"]], artifacts, client=client)
    for c in manifest["chunks"]:
        source.run_chunk(c["chunk_id"], records[c["start"]:c["stop"]])
    pairs, receipt = run_pinned_files(table2, table3, tier_a, parent, prior_ids, source)
    receipt.update({"prior_unresolved_file": str(prior), "prior_unresolved_sha256": prior_sha,
                    "prior_unresolved_provenance": prior_prov, "chunk_manifest_sha256": sha256_file(artifacts / "chunk_manifest.json"),
                    "admitted_chunks": len(admitted), "checkpoint_sha256": sha256_file(artifacts / "checkpoint.jsonl")})
    stamp = utc_stamp()
    pair_path = artifacts / f"tier_c_pairs_{stamp}.csv"
    pair_path.write_text("GZ1_OBJID,DR10_RELEASE,DR10_BRICKID,DR10_OBJID,LABEL\n" + "".join(
        f"{p.gz1_objid},{p.dr10_release},{p.dr10_brickid},{p.dr10_objid},{p.label}\n" for p in pairs), encoding="utf-8")
    receipt["tier_c_pair_file"] = str(pair_path)
    receipt["tier_c_pair_file_sha256"] = sha256_file(pair_path)
    receipt_path = artifacts / f"completeness_receipt_{stamp}.json"
    receipt_path.write_text(json.dumps(receipt, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    return {"status": "PASS", "receipt": str(receipt_path), "pairs": len(pairs),
            "wall_s": time.monotonic() - started}


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    for name in ("table2", "table3", "tier_a", "parent", "prior", "artifacts"):
        p.add_argument("--" + name.replace("_", "-"), type=Path, default=DEFAULTS[name])
    p.add_argument("--tap-base", default=DEFAULT_TAP)
    p.add_argument("--probe-receipt", type=Path)
    p.add_argument("--max-chunks", type=int)
    p.add_argument("--resume", action="store_true")
    p.add_argument("--dry-finalise", action="store_true")
    p.add_argument("--workers", type=int, choices=(1, 2), default=1)
    p.add_argument("--max-outage-minutes", type=float, default=180)
    a = p.parse_args(argv)
    if a.max_chunks is not None and a.max_chunks < 0:
        p.error("--max-chunks must be non-negative")
    if a.max_outage_minutes <= 0:
        p.error("--max-outage-minutes must be positive")
    outage_minutes = a.max_outage_minutes
    delattr(a, "max_outage_minutes")
    client = HttpClient(max_outage_minutes=outage_minutes,
                        capture_dir=a.artifacts / "http",
                        run_log=a.artifacts / "run.log.jsonl")
    try:
        result = execute(**vars(a), client=client)
    except OutageBudgetExhausted:
        print(json.dumps({"status": "outage_budget_exhausted"}), file=sys.stderr)
        return 75
    except (GateError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
