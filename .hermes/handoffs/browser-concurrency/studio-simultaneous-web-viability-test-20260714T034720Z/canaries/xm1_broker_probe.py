"""XM-1 broker probe (NO BROWSER): prove a real Pro->Studio authenticated broker
round-trip over the Thunderbolt link, AND that a LIVE lease held by the remote
lane goes non-live on the authority when the SSH channel is cut mid-session.

Channel: Studio -> ssh Pro -> ssh back to Studio -> uds_proxy -> local daemon.
Both hops use Thunderbolt link-local endpoints with StrictHostKeyChecking=yes
pinned by HostKeyAlias (net.py). No Tailscale fallback — link failure is a STOP.

A transport_id (e.g. thunderbolt-pass1r1) scopes fresh state/ledger and a
distinct receipt file so prior (Tailscale) proofs are preserved, never overwritten.

EXECUTION-GATED: refuses without --armed <token>. No browser, no account.
Usage: xm1_broker_probe.py --armed <token> <root> <transport_id> <pro_user_host> <pro_alias> <studio_from_pro> <studio_alias> <studio_pkg_abs>
"""
from __future__ import annotations

import json
import signal
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BROKER = HERE.parent / "broker"
sys.path.insert(0, str(BROKER))
sys.path.insert(0, str(HERE))
from net import matches_pro, matches_studio, ssh_argv, valid_transport_id  # noqa: E402
from sockdir import cleanup_socket_dir, new_socket_dir, socket_path_in  # noqa: E402
from transport import ChannelDown, RemoteLaneClient, UDSClient  # noqa: E402

PY = sys.executable


def main(argv):
    if len(argv) < 10 or argv[1] != "--armed":
        print(json.dumps({"probe": "REFUSED",
              "reason": "usage: --armed <token> <root> <transport_id> <pro_user_host> <pro_alias> <studio_from_pro> <studio_alias> <studio_pkg_abs>"}))
        return 4
    token, root = Path(argv[2]), Path(argv[3]).resolve()
    transport_id = argv[4]
    pro_user_host, pro_alias, studio_from_pro, studio_alias, studio_pkg = (
        argv[5], argv[6], argv[7], argv[8], argv[9])
    if not token.exists():
        print(json.dumps({"probe": "REFUSED", "reason": "approval token absent"})); return 4
    if not valid_transport_id(transport_id):
        print(json.dumps({"probe": "REFUSED", "reason": f"invalid transport_id: {transport_id!r}"})); return 4
    if not matches_pro(pro_user_host, pro_alias):
        print(json.dumps({"probe": "REFUSED", "reason": "pro endpoint/alias != canonical Thunderbolt Pro"})); return 4
    if not matches_studio(studio_from_pro, studio_alias):
        print(json.dumps({"probe": "REFUSED", "reason": "studio endpoint/alias != canonical Thunderbolt Studio"})); return 4

    rung = root / "receipts/archeval"; rung.mkdir(parents=True, exist_ok=True)
    tid = transport_id.upper().replace("-", "_")
    state = rung / f"probe_{transport_id}_state.json"
    bledger = rung / f"probe_{transport_id}_ledger.jsonl"
    receipt_path = rung / f"XM1_BROKER_PROBE_{tid}_RECEIPT.json"
    sdir = new_socket_dir(); sock = socket_path_in(sdir)
    daemon = lane = None
    outcome = {"probe": "xm1_broker_probe", "transport_id": transport_id,
               "transport": "thunderbolt", "fallback": "none",
               "endpoints": {"pro": {"host": pro_user_host, "host_key_alias": pro_alias},
                             "studio_from_pro": {"host": studio_from_pro, "host_key_alias": studio_alias}},
               "results": {}}
    try:
        daemon = subprocess.Popen([PY, "-B", str(BROKER / "broker_daemon.py"),
                                   str(state), str(bledger), str(sock)],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  text=True, start_new_session=True)
        if '"ready"' not in daemon.stdout.readline():
            raise RuntimeError("daemon not ready")

        inner = [*ssh_argv(studio_from_pro, studio_alias),
                 "python3", f"{studio_pkg}/broker/uds_proxy.py", str(sock)]
        channel = [*ssh_argv(pro_user_host, pro_alias), *inner]
        lane = RemoteLaneClient(channel, op_timeout=20.0)

        outcome["results"]["ping"] = lane.op({"op": "ping"})
        r1 = lane.op({"op": "acquire", "holder": "pro-probe", "kind": "target",
                      "scope": {"host_id": "macpro", "user_data_dir": "/pro/probe/p1"}})
        outcome["results"]["transport_acquire"] = r1
        if r1.get("ok"):
            lease1 = r1["lease"]
            outcome["results"]["transport_check"] = lane.op({"op": "check", "lease_id": lease1["lease_id"],
                                                             "epoch": lease1["epoch"], "action": "probe:noop"})
            outcome["results"]["transport_release"] = lane.op({"op": "release", "lease_id": lease1["lease_id"]})

        r2 = lane.op({"op": "acquire", "holder": "pro-probe-live", "kind": "target",
                      "scope": {"host_id": "macpro", "user_data_dir": "/pro/probe/p2"},
                      "ttl": 30.0, "heartbeat_interval": 0.3})
        outcome["results"]["live_acquire"] = r2
        live_failclosed = live_nonlive = False
        if r2.get("ok"):
            lease2 = r2["lease"]
            lane._proc.kill()  # partition while lease2 is live
            try:
                lane.op({"op": "ping"})
            except ChannelDown:
                live_failclosed = True
            time.sleep(0.5)  # exceed heartbeat -> authority expires it
            local = UDSClient(sock)
            chk = local.op({"op": "check", "lease_id": lease2["lease_id"],
                            "epoch": lease2["epoch"], "action": "probe:post-partition"})
            live_nonlive = (not chk["ok"]) and "no live lease" in chk.get("deny", "")
            outcome["results"]["authority_post_partition_check"] = chk
            local.close()
        outcome["results"]["live_partition_failclosed"] = live_failclosed
        outcome["results"]["authority_reports_lease_nonlive"] = live_nonlive
    except Exception as e:
        outcome["fatal"] = f"{type(e).__name__}: {e}"
    finally:
        if lane is not None:
            try:
                if getattr(lane, "_proc", None) and lane._proc.poll() is None:
                    lane._proc.kill()
            except Exception:
                pass
        if daemon and daemon.poll() is None:
            daemon.send_signal(signal.SIGTERM)
            try:
                daemon.wait(timeout=5)
            except subprocess.TimeoutExpired:
                daemon.kill()
        cleanup_socket_dir(sdir)
    ok = (outcome["results"].get("ping", {}).get("ok")
          and outcome["results"].get("transport_acquire", {}).get("ok")
          and outcome["results"].get("transport_check", {}).get("ok")
          and outcome["results"].get("transport_release", {}).get("ok")
          and outcome["results"].get("live_partition_failclosed")
          and outcome["results"].get("authority_reports_lease_nonlive")
          and "fatal" not in outcome)
    outcome["pass"] = bool(ok)
    receipt_path.write_text(json.dumps(outcome, indent=1))
    print(json.dumps({"transport_id": transport_id, "pass": outcome["pass"], "fatal": outcome.get("fatal")}))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
