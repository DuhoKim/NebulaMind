#!/usr/bin/env python3
"""Incremental orchestration of the GATED cutout chain (infrastructure only).

Each cycle: rebuild the object manifest from the transfer's receipts (gated builder),
subtract objects the runner has already resolved, then invoke the GATED runner on a
bounded batch. The runner requires manifest keys to equal the positions passed, so each
batch writes a matched (manifest, positions) pair.

Ledger truth is the runner's own per-object receipt, not its exit code: a receipt means
resolved (success or terminal failure) and is never retried; a tensor means success.
Neither gated program is modified. Stops cleanly on SIGTERM.
"""
import csv, json, os, signal, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
BUILDER = LANE / "_objmanifest_20260820/build_object_manifest.py"
POSITIONS = LANE / "_positions_20260820/positions_runner_view.csv"
# Custody-verified geometry sidecar (SHA-256 863e5ded…, matches SIDECAR_CUSTODY_20260819.md)
SIDECAR = LANE / "_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/static/survey-bricks-dr10-south.fits.gz"
DEST = Path("/Users/duhokim/NebulaMindData/dr10_south_image_r")
RECEIPTS = DEST / "receipts.jsonl"
OUT = Path("/Users/duhokim/NebulaMindData/cutouts_dr10_south")
WORK = OUT / "_wrapper"
HEARTBEAT = OUT / "wrapper_heartbeat.json"
CYCLE_SECONDS = 900
BATCH_LIMIT = 2000

stop = False
signal.signal(signal.SIGTERM, lambda *_: globals().__setitem__("stop", True))


def resolved_objects() -> set[str]:
    """Objects the runner has resolved, keyed by ls_id READ FROM the receipt.

    The runner names receipt files object-<hash>, not by ls_id, so the filename is
    not the key — using stems silently deduped nothing and re-offered the same batch
    forever (caught 2026-08-21 at 2,840 tensors by the NO_PROGRESS guard).
    """
    d = OUT / "receipts"
    out: set[str] = set()
    if d.exists():
        for p in d.glob("*.json"):
            try:
                out.add(str(json.loads(p.read_text())["ls_id"]))
            except Exception:
                continue
    return out


def load_positions() -> dict[str, tuple[str, str]]:
    with POSITIONS.open() as f:
        return {r["ls_id"]: (r["ra"], r["dec"]) for r in csv.DictReader(f)}


def build_manifest(dst: Path) -> dict:
    cmd = [sys.executable, str(BUILDER), "--positions", str(POSITIONS),
           "--receipts", str(RECEIPTS), "--destination-root", str(DEST),
           "--output", str(dst), "--sidecar", str(SIDECAR)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        (OUT / "wrapper_builder_error.log").write_text(r.stdout[-4000:] + "\n" + r.stderr[-4000:])
        return {}
    return json.loads(dst.read_text())


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    all_positions = load_positions()
    while not stop:
        status = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        manifest = build_manifest(WORK / "manifest_full.json")
        objects = manifest.get("objects", {})
        done = resolved_objects()
        todo = sorted(set(objects) - done)[:BATCH_LIMIT]
        status.update(ready=len(objects), resolved=len(done), batch=len(todo),
                      tensors=len(list((OUT / "tensors").glob("*.f32le"))) if (OUT / "tensors").exists() else 0)
        if todo:
            batch_manifest = {"schema_version": 1, "objects": {k: objects[k] for k in todo}}
            (WORK / "batch_manifest.json").write_text(json.dumps(batch_manifest, sort_keys=True))
            with (WORK / "batch_positions.csv").open("w", newline="") as g:
                w = csv.writer(g); w.writerow(["ra", "dec", "ls_id"])
                for k in todo:
                    ra, dec = all_positions[k]; w.writerow([ra, dec, k])
            r = subprocess.run([sys.executable, str(HERE / "cutout_runner.py"),
                                "--positions", str(WORK / "batch_positions.csv"),
                                "--brick-manifest", str(WORK / "batch_manifest.json"),
                                "--slots", str(HERE / "ic_slots.json"),
                                "--output-dir", str(OUT)], capture_output=True, text=True)
            status["runner_exit"] = r.returncode
            status["resolved_after"] = len(resolved_objects())
            if status["resolved_after"] == len(done):
                (OUT / "wrapper_last_error.log").write_text(r.stdout[-4000:] + "\n" + r.stderr[-4000:])
                status["state"] = "NO_PROGRESS"
                HEARTBEAT.write_text(json.dumps(status) + "\n")
                time.sleep(600)
                continue
        status["state"] = "OK"
        HEARTBEAT.write_text(json.dumps(status) + "\n")
        for _ in range(CYCLE_SECONDS // 5):
            if stop:
                break
            time.sleep(5)


if __name__ == "__main__":
    main()
