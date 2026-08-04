"""Single broker authority: Unix-domain-socket daemon, serialized ops, 0600.

One daemon process owns the Broker state; ALL clients (local Studio lanes via
UDS, Mac Pro lanes via outbound authenticated SSH Pro→Studio running
uds_proxy.py) reach THIS process. No TCP listener exists anywhere. Concurrent
connections are accepted, but every broker operation executes under one global
lock — a single serialized authority, eliminating the multi-process state race
Tori's pre-run review identified.

Usage: broker_daemon.py <state.json> <ledger.jsonl> <socket_path>
"""
from __future__ import annotations

import atexit
import fcntl
import json
import os
import signal
import socket
import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from broker import Broker, Deny  # noqa: E402

OPS_LOCK = threading.Lock()


def handle_request(b: Broker, req: dict) -> dict:
    try:
        op = req["op"]
        with OPS_LOCK:
            if op == "acquire":
                lease = b.acquire(req["holder"], req["kind"], req.get("mode", "write"),
                                  req.get("scope"), req.get("ttl", 300.0),
                                  req.get("heartbeat_interval", 60.0))
                return {"ok": True, "lease": lease}
            if op == "heartbeat":
                b.heartbeat(req["lease_id"])
                return {"ok": True}
            if op == "check":
                b.check(req["lease_id"], req["epoch"], req["action"],
                        req.get("uses_desktop", False), req.get("target_verified", True))
                return {"ok": True}
            if op == "release":
                b.release(req["lease_id"])
                return {"ok": True}
            if op == "freeze":
                b.freeze(req.get("declared_by", "remote"), req.get("reason", ""))
                return {"ok": True}
            if op == "ping":
                return {"ok": True, "pong": True, "pid": os.getpid()}
        return {"ok": False, "error": f"unknown op {op}"}
    except Deny as d:
        return {"ok": False, "deny": str(d)}
    except Exception as e:  # refuse malformed input; never crash the authority
        return {"ok": False, "error": f"bad request: {e}"}


def serve_conn(b: Broker, conn: socket.socket):
    try:
        buf = b""
        f = conn.makefile("rwb", buffering=0)
        while True:
            line = f.readline()
            if not line:
                break
            try:
                req = json.loads(line.decode())
            except json.JSONDecodeError as e:
                resp = {"ok": False, "error": f"bad json: {e}"}
            else:
                resp = handle_request(b, req)
            f.write((json.dumps(resp) + "\n").encode())
    except (BrokenPipeError, ConnectionResetError, OSError):
        pass  # client vanished; its leases die by heartbeat staleness (fail closed)
    finally:
        conn.close()


def main(argv):
    state, ledger, sock_path = Path(argv[1]), Path(argv[2]), Path(argv[3])
    # Authority identity is the STABLE state path, not the ephemeral short socket
    # dir — otherwise a run that allocates a fresh /tmp socket dir would bypass the
    # singleton. Two daemons on the same state can never both run, whatever socket.
    lock_path = Path(str(Path(state).resolve()) + ".authority.lock")

    # (A) Prove single authority BEFORE touching the socket: hold an exclusive
    # flock for the whole process lifetime. A second daemon cannot acquire it,
    # so it refuses instead of orphaning the live authority / splitting brain.
    lock_fd = os.open(str(lock_path), os.O_CREAT | os.O_RDWR, 0o600)
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        os.close(lock_fd)
        sys.stdout.write(json.dumps({"daemon": "refused",
                        "reason": "authority already running (lock held)"}) + "\n")
        sys.stdout.flush()
        return 3
    os.write(lock_fd, f"{os.getpid()}\n".encode())

    b = Broker(state, ledger, clock=time.time)

    # Only now — with the lock held — is any existing socket provably stale.
    if sock_path.exists():
        sock_path.unlink()

    old_umask = os.umask(0o177)  # socket file created 0600
    srv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        srv.bind(str(sock_path))
    finally:
        os.umask(old_umask)
    os.chmod(sock_path, 0o600)
    srv.listen(8)

    def _cleanup(*_):
        try:
            srv.close()
        finally:
            for p in (sock_path,):
                try:
                    p.unlink()
                except OSError:
                    pass
            try:
                fcntl.flock(lock_fd, fcntl.LOCK_UN)
                os.close(lock_fd)
            except OSError:
                pass

    atexit.register(_cleanup)
    signal.signal(signal.SIGTERM, lambda *_: (_cleanup(), sys.exit(0)))

    sys.stdout.write(json.dumps({"daemon": "ready", "pid": os.getpid()}) + "\n")
    sys.stdout.flush()
    try:
        while True:
            conn, _ = srv.accept()
            threading.Thread(target=serve_conn, args=(b, conn), daemon=True).start()
    finally:
        _cleanup()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
