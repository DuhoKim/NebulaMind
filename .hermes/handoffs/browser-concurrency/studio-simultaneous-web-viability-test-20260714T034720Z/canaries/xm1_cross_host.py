"""XM-1 (Tori repairs D + review-4): cross-machine sandbox parallelism, ONE
Studio broker authority, central CDP control, per-pass fresh trees.

Real sandbox Chrome on each host:
  - Studio: local writerA (host_id=studio), driven by the local Studio node.
  - Mac Pro: writerB (host_id=macpro) via the copied Python controller
    remote_chrome_controller.py over authenticated SSH (remote `setsid` MISSING,
    so Python start_new_session + finally killpg; no setsid/ps/pkill). Its CDP
    port is reached from the Studio through an authenticated `ssh -L` local
    forward (StrictHostKeyChecking=yes, ExitOnForwardFailure=yes); the node
    rewrites each WS URL to the forwarded endpoint. Both writers' leases come
    from the one Studio authority; Pro->Studio broker transport is proven
    separately by xm1_broker_probe.py (required PASS on record).

Drills: parallel leased in-flight writes; cross-host freeze (denies BOTH);
partition (drop the ssh -L forward -> writerB fails closed). Remote controller
teardown receipt (stopped:true) is a REQUIRED pass assertion.

EXECUTION-GATED: refuses without --armed <token>; no account/default-Chrome/
Flow/cua on either host; refuses a nonempty passdir or an occupied forward port.
Usage: xm1_cross_host.py --armed <token> <root> <pro_user_host> <pro_pkg_abs> <local_forward_port> <pass_id>
"""
from __future__ import annotations

import hashlib
import json
import os
import select
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BROKER = HERE.parent / "broker"
sys.path.insert(0, str(BROKER))
sys.path.insert(0, str(HERE))
from chrome_sandbox import launch, page_target_id, terminate, wait_port, PORT_DEADLINE_S  # noqa: E402
from net import matches_pro, scp_argv, ssh_argv, valid_transport_id  # noqa: E402
from remote_exec import preflight_empty_dir_script, run_python_stdin, sha256_script  # noqa: E402
from sockdir import cleanup_socket_dir, new_socket_dir, socket_path_in  # noqa: E402
from transport import ChannelDown, UDSClient  # noqa: E402

PY = sys.executable


def _port_free(host: str, port: int) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port)); return True
    except OSError:
        return False
    finally:
        s.close()


def _readline_timeout(pipe, timeout: float) -> str:
    ready, _, _ = select.select([pipe], [], [], timeout)
    if not ready:
        raise TimeoutError("remote read timed out")
    return pipe.readline()


def _local_sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(argv):
    if len(argv) < 10 or argv[1] != "--armed":
        print(json.dumps({"xm1": "REFUSED",
              "reason": "usage: --armed <token> <root> <transport_id> <pro_user_host> <pro_host_key_alias> <pro_pkg_abs> <local_forward_port> <pass_id>"}))
        return 4
    token = Path(argv[2]); root = Path(argv[3]).resolve()
    transport_id = argv[4]
    pro_user_host, pro_alias, pro_pkg = argv[5], argv[6], argv[7]
    lp = int(argv[8]); pass_id = argv[9]
    SSH_TO_PRO = ssh_argv(pro_user_host, pro_alias)
    SCP_TO_PRO = scp_argv(pro_alias)
    if not token.exists():
        print(json.dumps({"xm1": "REFUSED", "reason": "approval token absent"})); return 4
    if not valid_transport_id(transport_id):
        print(json.dumps({"xm1": "REFUSED", "reason": f"invalid transport_id: {transport_id!r}"})); return 4
    if not matches_pro(pro_user_host, pro_alias):
        print(json.dumps({"xm1": "REFUSED", "reason": "pro endpoint/alias != canonical Thunderbolt Pro"})); return 4
    # Require the EXACT fresh Thunderbolt probe PASS (not the old Tailscale proof),
    # and confirm its recorded endpoint+alias match THIS invocation.
    tid = transport_id.upper().replace("-", "_")
    probe = root / "receipts/archeval" / f"XM1_BROKER_PROBE_{tid}_RECEIPT.json"
    if not probe.exists():
        print(json.dumps({"xm1": "REFUSED", "reason": f"probe receipt missing: {probe.name}"})); return 4
    pj = json.loads(probe.read_text())
    ep = pj.get("endpoints", {}).get("pro", {})
    if not (pj.get("pass") and pj.get("transport") == "thunderbolt" and pj.get("fallback") == "none"
            and pj.get("transport_id") == transport_id):
        print(json.dumps({"xm1": "REFUSED",
              "reason": f"probe receipt not a PASS thunderbolt/no_fallback for {transport_id}"})); return 4
    if ep.get("host") != pro_user_host or ep.get("host_key_alias") != pro_alias:
        print(json.dumps({"xm1": "REFUSED",
              "reason": "probe receipt pro endpoint/alias != this invocation"})); return 4
    if not _port_free("127.0.0.1", lp):
        print(json.dumps({"xm1": "REFUSED", "reason": f"local forward port {lp} occupied"})); return 4

    rung = root / "receipts/archeval/xm1" / f"pass{pass_id}"
    if rung.exists() and any(rung.iterdir()):
        print(json.dumps({"xm1": "REFUSED", "reason": f"passdir not empty: {rung}"})); return 5
    (rung / "profiles/writerA").mkdir(parents=True, exist_ok=True)
    state, bledger = rung / "broker_state.json", rung / "broker_ledger.jsonl"
    spec_path, xm1_receipt = rung / "_tmp_spec.json", rung / "XM1_RECEIPT.json"
    a_profile = rung / "profiles/writerA"
    pro_pass = f"{pro_pkg}/xm1_sandbox/pass{pass_id}"
    pro_profile = f"{pro_pass}/writerB"
    sdir = new_socket_dir(); sock = socket_path_in(sdir)

    daemon = a_proc = ctrl = fwd = client = freezer = None
    leases = []
    outcome = {"xm1": "run", "pass_id": pass_id, "transport_id": transport_id,
               "transport": {"mode": "thunderbolt", "fallback": "none",
                             "pro": {"host": pro_user_host, "host_key_alias": pro_alias},
                             "local_forward_port": lp, "probe_receipt": probe.name},
               "teardown": {}, "drills": {}, "node_exit": None}
    try:
        daemon = subprocess.Popen([PY, "-B", str(BROKER / "broker_daemon.py"),
                                   str(state), str(bledger), str(sock)],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  text=True, start_new_session=True)
        if '"ready"' not in daemon.stdout.readline():
            raise RuntimeError("daemon not ready")
        client = UDSClient(sock)

        # Studio writerA
        a_proc = launch(a_profile, rung / "writerA.log")
        deadline = time.monotonic() + PORT_DEADLINE_S
        a_port = wait_port(a_profile, deadline)
        a_tid = page_target_id(a_port)
        ra = client.op({"op": "acquire", "holder": "writerA", "kind": "target",
                        "scope": {"host_id": "studio", "user_data_dir": str(a_profile), "target_id": a_tid}})
        if not ra["ok"]:
            raise RuntimeError(f"writerA lease denied: {ra}")
        leases.append(ra["lease"]["lease_id"])

        # Pro writerB: refuse a nonempty remote passdir BEFORE copying anything,
        # then create exact remote dir, copy controller, verify sha256, launch.
        # All remote Python runs are STDIN-FED (`python3 -`) so the remote shell
        # never reparses code (XM-1 pass1 STOP repair). mkdir/scp use fixed
        # no-space task-path args only.
        rc, _, err = run_python_stdin(SSH_TO_PRO,
                                      preflight_empty_dir_script(pro_pass), timeout=20)
        if rc == 2:
            raise RuntimeError(f"remote passdir not empty: {pro_pass}")
        if rc != 0:
            raise RuntimeError(f"remote passdir preflight failed (rc={rc}): {err.strip()[:200]}")
        ctrl_local = HERE / "remote_chrome_controller.py"
        subprocess.run([*SSH_TO_PRO, "mkdir", "-p", pro_pass], check=True, timeout=30)
        subprocess.run([*SCP_TO_PRO, str(ctrl_local), f"{pro_user_host}:{pro_pass}/remote_chrome_controller.py"],
                       check=True, timeout=30)
        rc, sha_out, err = run_python_stdin(SSH_TO_PRO,
                                            sha256_script(f"{pro_pass}/remote_chrome_controller.py"), timeout=20)
        if rc != 0:
            raise RuntimeError(f"remote sha check failed (rc={rc}): {err.strip()[:200]}")
        remote_sha = sha_out.strip()
        if remote_sha != _local_sha(ctrl_local):
            raise RuntimeError(f"remote controller sha mismatch: {remote_sha}")
        outcome["remote_controller_sha256"] = remote_sha

        ctrl = subprocess.Popen([*SSH_TO_PRO, "python3",
                                 f"{pro_pass}/remote_chrome_controller.py", pro_profile,
                                 f"{pro_pass}/writerB.log"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True, start_new_session=True)
        ready = json.loads(_readline_timeout(ctrl.stdout, 30) or "{}")
        if not ready.get("ready"):
            raise RuntimeError(f"pro controller not ready: {ready}")
        pro_port = ready["port"]

        # authenticated ssh -L forward (fail if forward can't bind)
        fwd = subprocess.Popen(ssh_argv(pro_user_host, pro_alias,
                                        extra=["-N", "-o", "ExitOnForwardFailure=yes",
                                               "-L", f"127.0.0.1:{lp}:127.0.0.1:{pro_port}"]),
                               stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, start_new_session=True)
        fdeadline = time.monotonic() + 10
        b_tid = None
        while time.monotonic() < fdeadline:
            if fwd.poll() is not None:
                raise RuntimeError("ssh -L forward exited (ExitOnForwardFailure)")
            try:
                b_tid = page_target_id(lp, host="127.0.0.1"); break
            except Exception:
                time.sleep(0.3)
        if b_tid is None:
            raise RuntimeError("ssh -L forward to Pro CDP not reachable")
        rb = client.op({"op": "acquire", "holder": "writerB", "kind": "target",
                        "scope": {"host_id": "macpro", "user_data_dir": pro_profile, "target_id": b_tid}})
        if not rb["ok"]:
            raise RuntimeError(f"writerB lease denied: {rb}")
        leases.append(rb["lease"]["lease_id"])

        # parallel leased in-flight writes (node rewrites writerB's WS to localhost:lp)
        spec = {"socket": str(sock), "rung": "XM-1", "pass_id": pass_id, "writers": [
            {"label": "writerA", "host_id": "studio", "port": a_port, "cdp_host": "127.0.0.1",
             "expected_target_id": a_tid, "lease_id": ra["lease"]["lease_id"], "epoch": ra["lease"]["epoch"]},
            {"label": "writerB", "host_id": "macpro", "port": lp, "cdp_host": "127.0.0.1",
             "expected_target_id": b_tid, "lease_id": rb["lease"]["lease_id"], "epoch": rb["lease"]["epoch"]}]}
        spec_path.write_text(json.dumps(spec))
        node = subprocess.run(["node", str(HERE / "sm1_cdp_parallel.mjs"), str(spec_path), str(xm1_receipt)],
                              capture_output=True, text=True, timeout=180, start_new_session=True)
        outcome["node_exit"] = node.returncode
        outcome["node_stdout"] = node.stdout.strip()[-400:]
        if node.returncode != 0:
            outcome["node_stderr"] = node.stderr.strip()[-600:]

        # cross-host freeze drill
        freezer = UDSClient(sock)
        freezer.op({"op": "freeze", "declared_by": "xm1-drill", "reason": "cross-host freeze test"})
        d_s = client.op({"op": "acquire", "holder": "pf-studio", "kind": "target",
                         "scope": {"host_id": "studio", "user_data_dir": "/x"}})
        d_p = client.op({"op": "acquire", "holder": "pf-macpro", "kind": "target",
                         "scope": {"host_id": "macpro", "user_data_dir": "/y"}})
        outcome["drills"]["freeze_denies_both"] = (
            (not d_s["ok"]) and "frozen" in d_s.get("deny", "")
            and (not d_p["ok"]) and "frozen" in d_p.get("deny", ""))

        # partition drill: drop the forward; writerB CDP unreachable
        fwd.terminate()
        try:
            fwd.wait(timeout=5)
        except subprocess.TimeoutExpired:
            fwd.kill()
        part = False
        try:
            page_target_id(lp, host="127.0.0.1")
        except Exception:
            part = True
        outcome["drills"]["partition_failclosed"] = part
    except Exception as e:
        outcome["fatal"] = f"{type(e).__name__}: {e}"
    finally:
        if client:
            for lid in leases:
                try:
                    client.op({"op": "release", "lease_id": lid})
                except ChannelDown:
                    pass
            client.close()
        if freezer:
            freezer.close()
        # Pro controller STOP -> its finally killpg's the Pro Chrome group; require receipt
        if ctrl and ctrl.poll() is None:
            try:
                ctrl.stdin.write("STOP\n"); ctrl.stdin.flush()
                stop_line = _readline_timeout(ctrl.stdout, 15)
                outcome["teardown"]["pro_controller"] = json.loads(stop_line or "{}")
                ctrl.wait(timeout=10)
                outcome["teardown"]["pro_controller_exit"] = ctrl.returncode
            except Exception as e:
                outcome["teardown"]["pro_controller_error"] = str(e)
                try:
                    os.killpg(ctrl.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
        if fwd and fwd.poll() is None:
            fwd.kill()
        outcome["teardown"]["writerA"] = terminate(a_proc)
        if daemon and daemon.poll() is None:
            daemon.send_signal(signal.SIGTERM)
            try:
                daemon.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(daemon.pid, signal.SIGKILL)
        cleanup_socket_dir(sdir)
        try:
            spec_path.unlink()
        except OSError:
            pass
        outcome["broker_ledger"] = str(bledger)
    (rung / "XM1_HARNESS_RECEIPT.json").write_text(json.dumps(outcome, indent=1))
    pro_td = outcome["teardown"].get("pro_controller", {})
    remote_teardown_ok = bool(pro_td.get("stopped")) and outcome["teardown"].get("pro_controller_exit") == 0
    print(json.dumps({k: outcome.get(k) for k in ("node_exit", "drills", "fatal")}))
    ok = (outcome.get("node_exit") == 0 and outcome["drills"].get("freeze_denies_both")
          and outcome["drills"].get("partition_failclosed") and remote_teardown_ok
          and "fatal" not in outcome)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
