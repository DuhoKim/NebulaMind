"""SSH endpoint construction for the canary (Thunderbolt link, HostKeyAlias).

Studio<->Pro run over a direct Thunderbolt bridge (link-local 169.254.100.0/24).
StrictHostKeyChecking stays ON with no known_hosts churn by pinning the stable
Tailscale identity via HostKeyAlias:
  Studio -> Pro : ssh -o HostKeyAlias=100.122.78.110 duhokim@169.254.100.1
  Pro -> Studio : ssh -o HostKeyAlias=100.84.12.101   duhokim@169.254.100.2
No automatic Tailscale fallback inside a canary — a link failure is a STOP;
Tailscale is recovery-only and never dialed by these harnesses.
"""
from __future__ import annotations

import re

SSH_COMMON = ["-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes",
              "-o", "ConnectTimeout=5", "-o", "ServerAliveInterval=5", "-o", "ServerAliveCountMax=2"]

# Canonical direct Thunderbolt endpoints (net.py OWNS these — harnesses must
# refuse anything else rather than labeling arbitrary CLI endpoints "thunderbolt").
PRO_HOST = "duhokim@169.254.100.1"      # Mac Pro, Thunderbolt link-local
PRO_ALIAS = "100.122.78.110"            # Pro stable Tailscale identity (HostKeyAlias only)
STUDIO_HOST = "duhokim@169.254.100.2"   # Mac Studio, Thunderbolt link-local
STUDIO_ALIAS = "100.84.12.101"          # Studio stable Tailscale identity (HostKeyAlias only)

TRANSPORT_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def ssh_argv(user_host: str, host_key_alias: str, extra=None):
    return ["ssh", *SSH_COMMON, "-o", f"HostKeyAlias={host_key_alias}", *(extra or []), user_host]


def scp_argv(host_key_alias: str):
    return ["scp", *SSH_COMMON, "-o", f"HostKeyAlias={host_key_alias}"]


def matches_pro(user_host: str, host_key_alias: str) -> bool:
    return user_host == PRO_HOST and host_key_alias == PRO_ALIAS


def matches_studio(user_host: str, host_key_alias: str) -> bool:
    return user_host == STUDIO_HOST and host_key_alias == STUDIO_ALIAS


def valid_transport_id(s: str) -> bool:
    return bool(TRANSPORT_ID_RE.match(s or ""))
