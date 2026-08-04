"""Exact-argv tests for Thunderbolt SSH endpoint construction (net.py).

Assert HostKeyAlias pinning, StrictHostKeyChecking on, direct link-local host,
extra-before-host ordering, and NO Tailscale endpoint leaking into the argv.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import net
from net import (PRO_ALIAS, PRO_HOST, STUDIO_ALIAS, STUDIO_HOST, matches_pro,
                 matches_studio, scp_argv, ssh_argv, valid_transport_id)


def _pairs(argv):
    """Parse every `-o NAME=VALUE` into {NAME: VALUE}."""
    out = {}
    for i, tok in enumerate(argv):
        if tok == "-o" and i + 1 < len(argv):
            name, _, value = argv[i + 1].partition("=")
            out[name] = value
    return out


def test_ssh_argv_pins_hostkeyalias_and_strict():
    a = ssh_argv(PRO_HOST, PRO_ALIAS)
    assert a[0] == "ssh"
    assert a[-1] == PRO_HOST                       # host is last
    opts = _pairs(a)
    assert opts["HostKeyAlias"] == PRO_ALIAS
    assert opts["StrictHostKeyChecking"] == "yes"
    assert opts["BatchMode"] == "yes"


def test_ssh_argv_uses_direct_link_local_not_tailscale_endpoint():
    a = ssh_argv(PRO_HOST, PRO_ALIAS)
    # the dialed host is the Thunderbolt link-local address...
    assert a[-1] == "duhokim@169.254.100.1"
    # ...and the Tailscale IP appears ONLY as the HostKeyAlias value, never as a host to dial
    assert not any(tok == PRO_HOST.replace("169.254.100.1", PRO_ALIAS) for tok in a)
    assert f"duhokim@{PRO_ALIAS}" not in a
    # no ProxyJump / Tailscale hostname fallback smuggled in
    joined = " ".join(a)
    assert "taila27502" not in joined and "ProxyJump" not in joined and "ProxyCommand" not in joined


def test_ssh_argv_extra_before_host():
    a = ssh_argv(PRO_HOST, PRO_ALIAS, extra=["-N", "-L", "127.0.0.1:5599:127.0.0.1:9222"])
    assert a[-1] == PRO_HOST
    assert a.index("-N") < a.index(PRO_HOST)
    assert a.index("-L") < a.index(PRO_HOST)


def test_scp_argv_pins_alias_and_strict():
    s = scp_argv(STUDIO_ALIAS)
    assert s[0] == "scp"
    opts = _pairs(s)
    assert opts["HostKeyAlias"] == STUDIO_ALIAS
    assert opts["StrictHostKeyChecking"] == "yes"


def test_distinct_aliases_per_direction():
    to_pro = ssh_argv(PRO_HOST, PRO_ALIAS)
    to_studio = ssh_argv(STUDIO_HOST, STUDIO_ALIAS)
    assert _pairs(to_pro)["HostKeyAlias"] == "100.122.78.110"
    assert _pairs(to_studio)["HostKeyAlias"] == "100.84.12.101"
    assert to_pro[-1] == "duhokim@169.254.100.1"
    assert to_studio[-1] == "duhokim@169.254.100.2"


def test_canonical_constants_are_link_local_hosts_with_tailscale_aliases():
    assert PRO_HOST == "duhokim@169.254.100.1" and PRO_ALIAS == "100.122.78.110"
    assert STUDIO_HOST == "duhokim@169.254.100.2" and STUDIO_ALIAS == "100.84.12.101"


def test_matches_pro_studio_exact_only():
    assert matches_pro(PRO_HOST, PRO_ALIAS)
    assert matches_studio(STUDIO_HOST, STUDIO_ALIAS)
    # swapped host/alias, tailscale-as-host, or wrong alias must all be rejected
    assert not matches_pro("duhokim@100.122.78.110", PRO_ALIAS)   # dialing the Tailscale IP
    assert not matches_pro(PRO_HOST, "100.84.12.101")             # wrong alias
    assert not matches_pro(STUDIO_HOST, STUDIO_ALIAS)             # that's the Studio
    assert not matches_studio(PRO_HOST, PRO_ALIAS)


def test_transport_id_regex():
    assert valid_transport_id("thunderbolt-pass1r1")
    assert valid_transport_id("t0")
    assert not valid_transport_id("")
    assert not valid_transport_id("-leading-hyphen")
    assert not valid_transport_id("has space")
    assert not valid_transport_id("semi;colon")
    assert not valid_transport_id("slash/x")
    assert not valid_transport_id("Upper")  # lowercase-only
