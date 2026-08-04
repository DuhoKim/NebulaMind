"""stdio <-> Unix-domain-socket bridge (Studio-side SSH remote command).

A Mac Pro lane runs: ssh -o BatchMode=yes duhokim@studio \
    'python3 .../uds_proxy.py /path/to/broker.sock'
(outbound authenticated SSH from the Pro — the REVERSE_SSH_OK verified
direction). This proxy connects to the daemon's 0600 UDS and pumps
line-delimited JSON both ways. It opens no listener of any kind. If either
side closes or errors, the proxy exits — the lane client fails closed.
Python 3.9-compatible.
"""
from __future__ import annotations

import socket
import sys
import threading


def main(argv):
    sock_path = argv[1]
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(sock_path)
    f = s.makefile("rwb", buffering=0)

    def pump_out():
        try:
            while True:
                line = f.readline()
                if not line:
                    break
                sys.stdout.buffer.write(line)
                sys.stdout.buffer.flush()
        except (OSError, ValueError):
            pass
        finally:
            try:
                sys.stdout.close()
            except Exception:
                pass

    t = threading.Thread(target=pump_out, daemon=True)
    t.start()
    try:
        for line in sys.stdin.buffer:
            f.write(line)
    except (BrokenPipeError, OSError):
        pass
    finally:
        try:
            s.shutdown(socket.SHUT_WR)
        except OSError:
            pass
        t.join(timeout=5)
        s.close()


if __name__ == "__main__":
    main(sys.argv)
