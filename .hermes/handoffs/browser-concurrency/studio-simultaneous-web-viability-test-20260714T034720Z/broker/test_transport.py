"""Transport tests against the SINGLE broker authority (UDS daemon).

Covers Tori's required repairs: two simultaneous clients (no race/corruption),
daemon loss, channel (proxy) loss, lease expiry, freeze propagation,
unreachable/auth-failure fail-closed. No browser, no network, no listener —
UDS + subprocess pipes only.
"""
import json
import os
import signal
import subprocess
import sys
import threading
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import ledger as ledger_mod
from broker import Broker
from sockdir import cleanup_socket_dir, new_socket_dir, socket_path_in
from transport import ChannelDown, RemoteLaneClient, UDSClient

PY = sys.executable
HERE = Path(__file__).parent
DAEMON = HERE / "broker_daemon.py"
PROXY = HERE / "uds_proxy.py"


def _start_daemon(state, ledger, sock, errfile):
    """Start a daemon with a SHORT socket path; capture stderr for diagnosis."""
    errf = open(errfile, "w")
    proc = subprocess.Popen([PY, "-B", str(DAEMON), str(state), str(ledger), str(sock)],
                            stdout=subprocess.PIPE, stderr=errf,
                            text=True, start_new_session=True)
    line = proc.stdout.readline()
    if '"ready"' not in line:
        errf.flush()
        err = Path(errfile).read_text()
        raise AssertionError(f"daemon not ready: stdout={line!r} stderr={err!r}")
    return proc


@pytest.fixture()
def daemon(tmp_path):
    state, ledger = tmp_path / "state.json", tmp_path / "ledger.jsonl"
    sdir = new_socket_dir()            # short /tmp dir (0700), NOT under the packet
    sock = socket_path_in(sdir)
    proc = _start_daemon(state, ledger, sock, tmp_path / "daemon.stderr")
    deadline = time.time() + 5
    while not sock.exists() and time.time() < deadline:
        time.sleep(0.02)
    yield {"proc": proc, "state": state, "ledger": ledger, "sock": sock, "sdir": sdir}
    if proc.poll() is None:
        os.killpg(proc.pid, signal.SIGKILL)
    proc.wait(timeout=5)
    cleanup_socket_dir(sdir)           # remove only this short dir


def test_socket_is_0600(daemon):
    mode = daemon["sock"].stat().st_mode & 0o777
    assert mode == 0o600, oct(mode)


def test_round_trip_via_uds(daemon):
    c = UDSClient(daemon["sock"])
    assert c.op({"op": "ping"})["ok"]
    r = c.op({"op": "acquire", "holder": "studio-lane", "kind": "target",
              "scope": {"host_id": "studio", "user_data_dir": "/sb/profiles/writerA"}})
    lease = r["lease"]
    assert c.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"],
                 "action": "cdp:evaluate"})["ok"]
    assert c.op({"op": "release", "lease_id": lease["lease_id"]})["ok"]
    c.close()
    ok, msg = ledger_mod.verify(daemon["ledger"])
    assert ok, msg


def test_two_simultaneous_clients_serialize_without_corruption(daemon):
    N = 25
    results = {"a": [], "b": [], "errors": []}

    def worker(name, profile):
        try:
            c = UDSClient(daemon["sock"])
            for i in range(N):
                r = c.op({"op": "acquire", "holder": name, "kind": "target",
                          "scope": {"host_id": "studio", "user_data_dir": profile, "target_id": f"{name}-{i}"}})
                assert r["ok"], r
                lease = r["lease"]
                assert c.op({"op": "check", "lease_id": lease["lease_id"],
                             "epoch": lease["epoch"], "action": "cdp:evaluate"})["ok"]
                assert c.op({"op": "release", "lease_id": lease["lease_id"]})["ok"]
                results[name].append(lease["epoch"])
            c.close()
        except Exception as e:  # pragma: no cover
            results["errors"].append(f"{name}: {e}")

    ta = threading.Thread(target=worker, args=("a", "/sb/profiles/writerA"))
    tb = threading.Thread(target=worker, args=("b", "/sb/profiles/writerB"))
    ta.start(); tb.start(); ta.join(30); tb.join(30)
    assert not results["errors"], results["errors"]
    epochs = results["a"] + results["b"]
    assert len(epochs) == 2 * N
    assert len(set(epochs)) == 2 * N, "epoch collision => authority raced"
    json.loads(daemon["state"].read_text())  # state file is intact JSON
    ok, msg = ledger_mod.verify(daemon["ledger"])
    assert ok, msg


def test_same_scope_write_conflict_still_denied_under_concurrency(daemon):
    c1, c2 = UDSClient(daemon["sock"]), UDSClient(daemon["sock"])
    r1 = c1.op({"op": "acquire", "holder": "a", "kind": "target",
                "scope": {"host_id": "studio", "user_data_dir": "/sb/p/SAME"}})
    assert r1["ok"]
    r2 = c2.op({"op": "acquire", "holder": "b", "kind": "target",
                "scope": {"host_id": "studio", "user_data_dir": "/sb/p/SAME"}})
    assert not r2["ok"] and "overlap" in r2["deny"]
    c1.close(); c2.close()


def test_daemon_loss_fails_closed_and_lease_expires(daemon):
    c = UDSClient(daemon["sock"])
    r = c.op({"op": "acquire", "holder": "lane", "kind": "target",
              "scope": {"host_id": "studio", "user_data_dir": "/sb/p/A"}, "ttl": 30.0, "heartbeat_interval": 0.3})
    lease = r["lease"]
    os.killpg(daemon["proc"].pid, signal.SIGKILL)  # simulated authority loss
    daemon["proc"].wait(timeout=5)
    with pytest.raises(ChannelDown):
        c.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"],
              "action": "cdp:evaluate"})
    assert c.stopped
    time.sleep(0.4)
    b = Broker(daemon["state"], daemon["ledger"], clock=time.time)
    assert not b._live(b.state["leases"][lease["lease_id"]])


def test_proxy_channel_round_trip_and_partition(daemon):
    # Pro lane reaches the ONE Studio authority via the uds_proxy (local pipe
    # stands in for outbound SSH); a Pro-host target coexists with a Studio one.
    argv = [PY, "-B", str(PROXY), str(daemon["sock"])]
    studio = UDSClient(daemon["sock"])
    assert studio.op({"op": "acquire", "holder": "studio-w", "kind": "target",
                      "scope": {"host_id": "studio", "user_data_dir": "/sb/p/dr"}})["ok"]
    c = RemoteLaneClient(argv)
    assert c.op({"op": "ping"})["ok"]
    r = c.op({"op": "acquire", "holder": "pro-lane", "kind": "target",
              "scope": {"host_id": "macpro", "user_data_dir": "/sb/p/dr"}})
    assert r["ok"], r  # same profile path, different host => allowed cross-host
    c._proc.kill()  # channel partition (ssh drop)
    with pytest.raises(ChannelDown):
        c.op({"op": "ping"})
    assert c.stopped
    studio.close()


def test_second_daemon_refuses_single_authority(daemon, tmp_path):
    # (A) a second authority on the same socket/lock must refuse, not orphan.
    p2 = subprocess.Popen([PY, "-B", str(DAEMON), str(daemon["state"]),
                           str(daemon["ledger"]), str(daemon["sock"])],
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                          text=True, start_new_session=True)
    out = p2.stdout.readline()
    rc = p2.wait(timeout=5)
    assert '"refused"' in out, out
    assert rc == 3
    # original authority still serves
    c = UDSClient(daemon["sock"])
    assert c.op({"op": "ping"})["ok"]
    c.close()


def test_same_state_different_socket_dir_refuses(daemon, tmp_path):
    # (A, strengthened) singleton is anchored to the STABLE state path: a second
    # authority on the same state but a FRESH short socket dir must still refuse.
    sdir2 = new_socket_dir()
    sock2 = socket_path_in(sdir2)
    try:
        p2 = subprocess.Popen([PY, "-B", str(DAEMON), str(daemon["state"]),
                               str(daemon["ledger"]), str(sock2)],
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                              text=True, start_new_session=True)
        out = p2.stdout.readline()
        rc = p2.wait(timeout=5)
        assert '"refused"' in out, out
        assert rc == 3
        assert not sock2.exists(), "refused daemon must not create a second socket"
    finally:
        cleanup_socket_dir(sdir2)


def test_daemon_sigterm_cleans_socket(tmp_path):
    state, ledger = tmp_path / "s.json", tmp_path / "l.jsonl"
    sdir = new_socket_dir()
    sock = socket_path_in(sdir)
    try:
        proc = _start_daemon(state, ledger, sock, tmp_path / "d.stderr")
        assert sock.exists()
        proc.send_signal(signal.SIGTERM)
        proc.wait(timeout=5)
        assert not sock.exists(), "SIGTERM must remove the socket file"
    finally:
        cleanup_socket_dir(sdir)


def test_freeze_from_one_client_denies_the_other(daemon):
    c1, c2 = UDSClient(daemon["sock"]), UDSClient(daemon["sock"])
    assert c1.op({"op": "freeze", "declared_by": "yui", "reason": "drill"})["ok"]
    r = c2.op({"op": "acquire", "holder": "x", "kind": "target",
               "scope": {"host_id": "studio", "user_data_dir": "/p"}})
    assert not r["ok"] and "frozen" in r["deny"]
    c1.close(); c2.close()


def test_unreachable_socket_means_no_action(tmp_path):
    with pytest.raises(ChannelDown):
        UDSClient(tmp_path / "missing.sock")


def test_ssh_auth_failure_like_exit_stops_client():
    c = RemoteLaneClient(["/usr/bin/false"])  # exits like ssh auth 255
    with pytest.raises(ChannelDown):
        c.op({"op": "ping"})
    assert c.stopped
