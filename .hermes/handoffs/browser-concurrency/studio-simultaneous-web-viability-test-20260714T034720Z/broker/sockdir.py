"""Short UDS socket-dir allocation (Tori repair: AF_UNIX sockaddr_un ~104-byte limit).

The packet path and macOS TMPDIR (`/var/folders/...`) are far too long for an
AF_UNIX path. The broker socket therefore lives in a dedicated short directory
under `/tmp` (dir 0700, socket 0600); state and ledger stay in the packet.
Product runs and tests MUST allocate the socket here, never under the packet
path, and remove only the returned dir on teardown.
"""
from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path


def new_socket_dir(prefix: str = "nmbrk") -> Path:
    d = Path(tempfile.mkdtemp(dir="/tmp", prefix=prefix))
    os.chmod(d, 0o700)
    return d


def socket_path_in(d: Path) -> Path:
    return Path(d) / "b.sock"  # short basename keeps the full path well under the limit


def cleanup_socket_dir(d: Path) -> None:
    shutil.rmtree(d, ignore_errors=True)
