"""Broker + ledger unit tests (local, sandbox-only; no browser, no network)."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import broker as broker_mod
import ledger as ledger_mod
from broker import Broker, Deny


@pytest.fixture()
def bk(tmp_path):
    clock = {"t": 100.0}
    b = Broker(tmp_path / "state.json", tmp_path / "ledger.jsonl",
               clock=lambda: clock["t"])
    b._test_clock = clock
    return b


def test_ledger_chain_appends_and_verifies(tmp_path):
    p = tmp_path / "l.jsonl"
    ledger_mod.append(p, "hwao", "genesis", {"n": 0}, utc="2026-07-14T00:00:00Z")
    ledger_mod.append(p, "hwao", "note", {"n": 1}, utc="2026-07-14T00:00:01Z")
    ok, msg = ledger_mod.verify(p)
    assert ok, msg
    entries = ledger_mod.read_entries(p)
    assert [e["epoch"] for e in entries] == [0, 1]


def test_ledger_detects_tamper(tmp_path):
    p = tmp_path / "l.jsonl"
    ledger_mod.append(p, "a", "x", {"v": 1})
    ledger_mod.append(p, "a", "x", {"v": 2})
    lines = p.read_text().splitlines()
    lines[0] = lines[0].replace('"v": 1', '"v": 9') if '"v": 1' in lines[0] else lines[0].replace('"v":1', '"v":9')
    p.write_text("\n".join(lines) + "\n")
    ok, _ = ledger_mod.verify(p)
    assert not ok


def test_two_dom_cdp_writers_separate_profiles_parallel(bk):
    a = bk.acquire("writerA", "target", scope={"host_id": "studio", "user_data_dir": "/sb/profiles/writerA", "target_id": "T1"})
    b = bk.acquire("writerB", "target", scope={"host_id": "studio", "user_data_dir": "/sb/profiles/writerB", "target_id": "T2"})
    assert bk.check(a["lease_id"], a["epoch"], "cdp:type", uses_desktop=False)
    assert bk.check(b["lease_id"], b["epoch"], "cdp:type", uses_desktop=False)


def test_target_lease_requires_host_id(bk):
    with pytest.raises(Deny, match="host_id"):
        bk.acquire("writerA", "target", scope={"user_data_dir": "/sb/p/A"})


def test_same_host_same_profile_second_writer_denied(bk):
    bk.acquire("writerA", "target", scope={"host_id": "studio", "user_data_dir": "/sb/p/A", "target_id": "T1"})
    with pytest.raises(Deny):
        bk.acquire("writerB", "target", scope={"host_id": "studio", "user_data_dir": "/sb/p/A"})


def test_same_profile_path_different_hosts_allowed(bk):
    # Studio and Mac Pro can each own an identically-named sandbox profile path.
    a = bk.acquire("studio-w", "target", scope={"host_id": "studio", "user_data_dir": "/sb/p/dr"})
    b = bk.acquire("pro-w", "target", scope={"host_id": "macpro", "user_data_dir": "/sb/p/dr"})
    assert a["state"] == "live" and b["state"] == "live"


def test_read_leases_may_share_a_target(bk):
    bk.acquire("obs1", "target", mode="read", scope={"host_id": "studio", "user_data_dir": "/sb/p/A", "window_id": "W1"})
    obs2 = bk.acquire("obs2", "target", mode="read", scope={"host_id": "studio", "user_data_dir": "/sb/p/A", "window_id": "W1"})
    assert obs2["state"] == "live"


def test_desktop_control_singleton_per_host(bk):
    s = bk.acquire("studio-hlp", "desktop-control", scope={"host_id": "studio"})
    # same host: denied
    with pytest.raises(Deny, match="host studio"):
        bk.acquire("studio-hlp2", "desktop-control", scope={"host_id": "studio"})
    # different host: allowed concurrently
    p = bk.acquire("pro-hlp", "desktop-control", scope={"host_id": "macpro"})
    assert p["state"] == "live"
    bk.release(s["lease_id"])
    assert bk.acquire("studio-hlp2", "desktop-control", scope={"host_id": "studio"})["state"] == "live"


def test_desktop_control_requires_host_id(bk):
    with pytest.raises(Deny, match="host_id"):
        bk.acquire("hlp", "desktop-control")


def test_account_submission_is_global_across_hosts(bk):
    s = bk.acquire("studio", "account-submission", scope={"host_id": "studio"})
    with pytest.raises(Deny, match="global"):
        bk.acquire("pro", "account-submission", scope={"host_id": "macpro"})
    bk.release(s["lease_id"])
    assert bk.acquire("pro", "account-submission", scope={"host_id": "macpro"})["state"] == "live"


def test_desktop_write_without_desktop_lease_denied(bk):
    t = bk.acquire("writerA", "target", scope={"host_id": "studio", "user_data_dir": "/sb/p/A"})
    with pytest.raises(Deny, match="desktop-control"):
        bk.check(t["lease_id"], t["epoch"], "ax:click", uses_desktop=True)


def test_stale_epoch_fenced(bk):
    t = bk.acquire("writerA", "target", scope={"host_id": "studio", "user_data_dir": "/sb/p/A"})
    with pytest.raises(Deny, match="stale epoch"):
        bk.check(t["lease_id"], t["epoch"] - 1, "cdp:navigate")


def test_ttl_and_heartbeat_expiry(bk):
    t = bk.acquire("writerA", "target", scope={"host_id": "studio", "user_data_dir": "/sb/p/A"}, ttl=50, heartbeat_interval=10)
    bk._test_clock["t"] += 11
    with pytest.raises(Deny):
        bk.check(t["lease_id"], t["epoch"], "cdp:type")


def test_failed_reverify_revokes_and_fails_closed(bk):
    t = bk.acquire("writerA", "target", scope={"host_id": "studio", "user_data_dir": "/sb/p/A"})
    with pytest.raises(Deny, match="fail closed"):
        bk.check(t["lease_id"], t["epoch"], "cdp:type", target_verified=False)
    with pytest.raises(Deny):
        bk.check(t["lease_id"], t["epoch"], "cdp:type")


def test_emergency_stop_freezes_everything_and_needs_user_gate(bk):
    t = bk.acquire("writerA", "target", scope={"host_id": "studio", "user_data_dir": "/sb/p/A"})
    bk.freeze(declared_by="yui", reason="challenge banner observed")
    with pytest.raises(Deny, match="frozen"):
        bk.check(t["lease_id"], t["epoch"], "cdp:type")
    with pytest.raises(Deny, match="frozen"):
        bk.acquire("writerB", "target", scope={"host_id": "macpro", "user_data_dir": "/sb/p/B"})
    bk.reset_after_user_gate("DUHO_GATE_REF")
    n = bk.acquire("writerB", "target", scope={"host_id": "macpro", "user_data_dir": "/sb/p/B"})
    assert n["state"] == "live"


def test_broker_journal_is_verifiable(bk, tmp_path):
    t = bk.acquire("writerA", "target", scope={"host_id": "studio", "user_data_dir": "/sb/p/A"})
    bk.check(t["lease_id"], t["epoch"], "cdp:type")
    bk.release(t["lease_id"])
    ok, msg = ledger_mod.verify(bk.ledger_path)
    assert ok, msg
