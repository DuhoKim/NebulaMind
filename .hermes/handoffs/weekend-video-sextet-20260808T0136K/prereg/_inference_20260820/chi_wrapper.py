#!/usr/bin/env python3
"""Incremental chi production over verified cutout tensors (infrastructure only).

Each cycle: diff the cutter's tensors against chi results already written, then invoke the
GATED inference runner on a bounded batch via its manifest transport. The runner is resumable
and writes its own per-object receipts; those receipts are the ledger, never this wrapper's
bookkeeping. Neither gated program is modified.

Binding condition from K8_CROSSING_AUTHORIZATION_20260820.md: per-object chi only. This wrapper
computes no tertile, no aggregate, no summary statistic of any kind over chi — it counts objects
and nothing else. Stops cleanly on SIGTERM.
"""
import json, signal, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
PY = LANE / "venv_torch/bin/python"
AUTH = LANE / "K8_CROSSING_AUTHORIZATION_20260820.md"
TENSORS = Path("/Users/duhokim/NebulaMindData/cutouts_dr10_south/tensors")
OUT = Path("/Users/duhokim/NebulaMindData/chi_dr10_south")
WORK = OUT / "_wrapper"
HEARTBEAT = OUT / "chi_heartbeat.json"
CYCLE_SECONDS = 900
BATCH_LIMIT = 4000

stop = False
signal.signal(signal.SIGTERM, lambda *_: globals().__setitem__("stop", True))


def done_tensor_hashes() -> set[str]:
    """Objects already measured, keyed by the input tensor sha the runner receipts."""
    p = OUT / "results.jsonl"
    out = set()
    if p.exists():
        with p.open() as f:
            for line in f:
                try:
                    out.add(json.loads(line)["input_tensor_sha256"])
                except Exception:
                    continue
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    while not stop:
        status = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        all_t = sorted(TENSORS.glob("*.f32le"))
        measured = len(done_tensor_hashes())
        # The runner is resumable by tensor hash; hand it everything and let it skip.
        batch = [str(p) for p in all_t][: measured + BATCH_LIMIT]
        status.update(tensors_available=len(all_t), measured=measured, offered=len(batch))
        if len(batch) > measured:
            man = WORK / "batch_manifest.txt"
            man.write_text("\n".join(batch) + "\n")
            r = subprocess.run([str(PY), str(HERE / "inference_runner.py"),
                                "--input-manifest", str(man),
                                "--output-dir", str(OUT),
                                "--authorization", str(AUTH)],
                               capture_output=True, text=True, cwd=str(HERE))
            status["runner_exit"] = r.returncode
            status["measured_after"] = len(done_tensor_hashes())
            if r.returncode != 0 and status["measured_after"] == measured:
                (OUT / "chi_last_error.log").write_text(r.stdout[-4000:] + "\n" + r.stderr[-4000:])
                status["state"] = "RUNNER_ERROR"
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
