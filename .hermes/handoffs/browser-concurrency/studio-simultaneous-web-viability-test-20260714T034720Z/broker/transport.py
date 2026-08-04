"""Fail-closed lane client over a pipe/SSH channel to the broker authority.

Rules (Lana §2 / two-machine assessment):
- Outbound channel only (subprocess pipe locally; `ssh -o BatchMode=yes` for
  cross-machine). NO listener, NO unauthenticated port — there is nothing to
  connect to; we only ever dial out over authenticated SSH.
- FAIL CLOSED: any spawn failure, write/read error, timeout, EOF, or non-JSON
  reply permanently stops this client (`stopped=True`); every subsequent call
  raises. A stopped lane performs no action and never falls back.
"""
import json
import subprocess
from pathlib import Path


class ChannelDown(Exception):
    pass


def ssh_channel_argv(user_host: str, remote_cmd: list[str]) -> list[str]:
    return ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=5",
            "-o", "ServerAliveInterval=5", "-o", "ServerAliveCountMax=2",
            user_host, *remote_cmd]


def local_channel_argv(python: str, stdio_py: Path, state: Path, ledger: Path) -> list[str]:
    return [python, "-B", str(stdio_py), str(state), str(ledger)]


class UDSClient:
    """Local Studio lane client: connects to the single broker-daemon UDS.

    Same fail-closed contract as RemoteLaneClient: ANY connect/write/read
    error, timeout, EOF, or non-JSON reply permanently stops the client.
    """

    def __init__(self, sock_path, op_timeout: float = 10.0):
        import socket as _socket
        self.stopped = False
        self.stop_reason = None
        self._timeout = op_timeout
        try:
            self._sock = _socket.socket(_socket.AF_UNIX, _socket.SOCK_STREAM)
            self._sock.settimeout(op_timeout)
            self._sock.connect(str(sock_path))
            self._file = self._sock.makefile("rwb", buffering=0)
        except OSError as e:
            self.stopped = True
            self.stop_reason = f"uds connect failed: {e}"
            raise ChannelDown(self.stop_reason)

    def _stop(self, reason: str):
        self.stopped = True
        self.stop_reason = reason
        try:
            self._sock.close()
        except Exception:
            pass

    def op(self, request: dict) -> dict:
        if self.stopped:
            raise ChannelDown(f"lane stopped (fail-closed): {self.stop_reason}")
        try:
            self._file.write((json.dumps(request) + "\n").encode())
            line = self._file.readline()
        except (OSError, ValueError) as e:
            self._stop(f"uds channel error: {e}")
            raise ChannelDown(self.stop_reason)
        if not line:
            self._stop("uds EOF (daemon loss)")
            raise ChannelDown(self.stop_reason)
        try:
            return json.loads(line.decode())
        except json.JSONDecodeError as e:
            self._stop(f"non-JSON reply: {e}")
            raise ChannelDown(self.stop_reason)

    def close(self):
        try:
            self._sock.close()
        except Exception:
            pass


class RemoteLaneClient:
    def __init__(self, channel_argv: list[str], op_timeout: float = 10.0):
        self.stopped = False
        self.stop_reason = None
        self._timeout = op_timeout
        try:
            self._proc = subprocess.Popen(
                channel_argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL, text=True, bufsize=1)
        except OSError as e:
            self._proc = None
            self._stop(f"channel spawn failed: {e}")
            raise ChannelDown(self.stop_reason)

    def _stop(self, reason: str):
        self.stopped = True
        self.stop_reason = reason
        if getattr(self, "_proc", None) and self._proc.poll() is None:
            self._proc.kill()

    def op(self, request: dict) -> dict:
        if self.stopped:
            raise ChannelDown(f"lane stopped (fail-closed): {self.stop_reason}")
        try:
            self._proc.stdin.write(json.dumps(request) + "\n")
            self._proc.stdin.flush()
        except (BrokenPipeError, ValueError, OSError) as e:
            self._stop(f"channel write failed: {e}")
            raise ChannelDown(self.stop_reason)
        import select
        ready, _, _ = select.select([self._proc.stdout], [], [], self._timeout)
        if not ready:
            self._stop("channel timeout")
            raise ChannelDown(self.stop_reason)
        line = self._proc.stdout.readline()
        if not line:
            self._stop("channel EOF (partition or auth failure)")
            raise ChannelDown(self.stop_reason)
        try:
            return json.loads(line)
        except json.JSONDecodeError as e:
            self._stop(f"non-JSON reply: {e}")
            raise ChannelDown(self.stop_reason)

    def close(self):
        if getattr(self, "_proc", None):
            try:
                self._proc.stdin.close()
            except Exception:
                pass
            self._proc.wait(timeout=5)
