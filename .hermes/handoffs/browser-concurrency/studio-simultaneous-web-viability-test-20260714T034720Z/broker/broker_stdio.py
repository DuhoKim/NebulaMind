"""DEV/TEST TOOL ONLY — single-client stdio Broker (superseded for real use).

Tori pre-run review finding: spawning one of these per channel against a
shared state file is NOT a single authority and can race. Production path is
broker_daemon.py (one UDS daemon, serialized ops) + uds_proxy.py for SSH
channels. This file remains only for single-client harness experiments.

Serve a Broker over stdin/stdout as line-delimited JSON (one op per line).

Transport model: NO listener, NO bound socket, ever. The channel is a pipe —
locally a subprocess pipe; cross-machine the stdio of an outbound
`ssh -o BatchMode=yes` invocation (initiated from the Studio, the proven auth
direction). Logical roles stay: broker authority on the Studio state file,
acting lane on the far end. Any malformed request gets {"ok": false} and the
server keeps fail-closed semantics; the client side stops on ANY channel error.
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from broker import Broker, Deny  # noqa: E402


def main(argv):
    state = Path(argv[1])
    ledger = Path(argv[2])
    b = Broker(state, ledger, clock=time.time)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            op = req["op"]
            if op == "acquire":
                lease = b.acquire(req["holder"], req["kind"], req.get("mode", "write"),
                                  req.get("scope"), req.get("ttl", 300.0),
                                  req.get("heartbeat_interval", 60.0))
                resp = {"ok": True, "lease": lease}
            elif op == "heartbeat":
                b.heartbeat(req["lease_id"])
                resp = {"ok": True}
            elif op == "check":
                b.check(req["lease_id"], req["epoch"], req["action"],
                        req.get("uses_desktop", False), req.get("target_verified", True))
                resp = {"ok": True}
            elif op == "release":
                b.release(req["lease_id"])
                resp = {"ok": True}
            elif op == "freeze":
                b.freeze(req.get("declared_by", "remote"), req.get("reason", ""))
                resp = {"ok": True}
            elif op == "ping":
                resp = {"ok": True, "pong": True}
            else:
                resp = {"ok": False, "error": f"unknown op {op}"}
        except Deny as d:
            resp = {"ok": False, "deny": str(d)}
        except Exception as e:  # malformed input: refuse, never crash the authority
            resp = {"ok": False, "error": f"bad request: {e}"}
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main(sys.argv)
