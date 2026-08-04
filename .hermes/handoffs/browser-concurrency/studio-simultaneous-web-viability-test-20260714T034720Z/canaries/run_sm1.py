"""SM-1 harness (Tori repairs 2+C+final): reviewed Python runner, single broker
authority, every CDP op broker-leased, per-op target re-verification, and a
FRESH pass-specific state/ledger/profile/receipt tree per pass.

Running this file IS the gated browser act — invoke only under renewed Tori
pre-run safety approval. Usage: run_sm1.py <packet_root> <host_id> <pass_id>
"""
from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BROKER = HERE.parent / "broker"
sys.path.insert(0, str(BROKER))
sys.path.insert(0, str(HERE))
from chrome_sandbox import launch, page_target_id, terminate, wait_port, PORT_DEADLINE_S  # noqa: E402
from sockdir import cleanup_socket_dir, new_socket_dir, socket_path_in  # noqa: E402
from transport import ChannelDown, UDSClient  # noqa: E402

PY = sys.executable


def main(argv):
    root = Path(argv[1]).resolve()
    host_id = argv[2]
    pass_id = argv[3]
    if not Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome").exists():
        print(json.dumps({"fatal": "chrome binary missing"})); return 2

    # (2) fresh pass-specific tree — nothing reused across passes; refuse a
    # nonempty passdir rather than silently reusing prior state.
    passdir = root / "receipts/archeval/sm1" / f"pass{pass_id}"
    if passdir.exists() and any(passdir.iterdir()):
        print(json.dumps({"fatal": f"passdir not empty: {passdir}"})); return 5
    (passdir / "profiles" / "writerA").mkdir(parents=True, exist_ok=True)
    (passdir / "profiles" / "writerB").mkdir(parents=True, exist_ok=True)
    (passdir / "logs").mkdir(parents=True, exist_ok=True)
    state = passdir / "broker_state.json"
    bledger = passdir / "broker_ledger.jsonl"
    spec_path = passdir / "_tmp_spec.json"
    sm1_receipt = passdir / "SM1_RECEIPT.json"
    sdir = new_socket_dir()
    sock = socket_path_in(sdir)

    writers = [{"label": "writerA", "profile": passdir / "profiles/writerA"},
               {"label": "writerB", "profile": passdir / "profiles/writerB"}]
    procs, client, daemon, leases = {}, None, None, []
    outcome = {"harness": "run_sm1.py", "host_id": host_id, "pass_id": pass_id,
               "passdir": str(passdir), "teardown": {}, "node_exit": None}
    try:
        daemon = subprocess.Popen([PY, "-B", str(BROKER / "broker_daemon.py"),
                                   str(state), str(bledger), str(sock)],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  text=True, start_new_session=True)
        ready = daemon.stdout.readline()
        if '"ready"' not in ready:
            raise RuntimeError(f"daemon not ready: {ready!r} {daemon.stderr.read()!r}")
        for w in writers:
            procs[w["label"]] = launch(w["profile"], passdir / f"logs/{w['label']}.log")
        deadline = time.monotonic() + PORT_DEADLINE_S
        client = UDSClient(sock)
        for w in writers:
            w["port"] = wait_port(w["profile"], deadline)
            w["target_id"] = page_target_id(w["port"])
            r = client.op({"op": "acquire", "holder": w["label"], "kind": "target",
                           "scope": {"host_id": host_id, "user_data_dir": str(w["profile"]),
                                     "target_id": w["target_id"]}})
            if not r["ok"]:
                raise RuntimeError(f"lease denied for {w['label']}: {r}")
            leases.append(r["lease"]["lease_id"])
            w["lease_id"] = r["lease"]["lease_id"]; w["epoch"] = r["lease"]["epoch"]
        spec = {"socket": str(sock), "rung": "SM-1", "pass_id": pass_id, "writers": [
            {"label": w["label"], "host_id": host_id, "port": w["port"], "cdp_host": "127.0.0.1",
             "expected_target_id": w["target_id"], "lease_id": w["lease_id"], "epoch": w["epoch"]}
            for w in writers]}
        spec_path.write_text(json.dumps(spec))
        node = subprocess.run(["node", str(HERE / "sm1_cdp_parallel.mjs"),
                               str(spec_path), str(sm1_receipt)],
                              capture_output=True, text=True, timeout=180, start_new_session=True)
        outcome["node_exit"] = node.returncode
        outcome["node_stdout"] = node.stdout.strip()[-400:]
        if node.returncode != 0:
            outcome["node_stderr"] = node.stderr.strip()[-600:]
    except (Exception, ChannelDown) as e:
        outcome["fatal"] = f"{type(e).__name__}: {e}"
    finally:
        if client:
            for lid in leases:
                try:
                    client.op({"op": "release", "lease_id": lid})
                except ChannelDown:
                    pass
            client.close()
        for w in writers:
            outcome["teardown"][w["label"]] = terminate(procs.get(w["label"]))
        outcome["teardown"]["both_exited"] = all(
            procs.get(w["label"]) is not None and procs[w["label"]].poll() is not None for w in writers)
        if daemon and daemon.poll() is None:
            try:
                daemon.send_signal(signal.SIGTERM); daemon.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(daemon.pid, signal.SIGKILL)
        outcome["teardown"]["socket_removed"] = not sock.exists()
        cleanup_socket_dir(sdir)
        try:
            spec_path.unlink()
        except OSError:
            pass
        outcome["broker_ledger"] = str(bledger)
        outcome["non_interference"] = ("structural: only spawned pgids signalled; no census scan; "
                                       "default Chrome/Flow window never addressed")
    (passdir / "SM1_HARNESS_RECEIPT.json").write_text(json.dumps(outcome, indent=1))
    print(json.dumps({k: outcome.get(k) for k in ("pass_id", "node_exit", "teardown", "fatal")}))
    ok = outcome.get("node_exit") == 0 and outcome["teardown"]["both_exited"] and "fatal" not in outcome
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
