"""Deterministic browser broker — lease registry with fail-closed fencing.

Contract (per HWAO_FINAL_RECOMMENDATION + Lana §2, Kun's parallel-write rule):
- Target leases: hierarchical scope (bundle, user_data_dir, window_id, target_id).
  Write leases are exclusive at any overlapping scope; read leases may share.
- Global singleton leases (machine-wide, one holder each):
  desktop-control (every cua/AX/pointer/keyboard write), account-submission,
  clipboard, focus.
- DOM/CDP browser writes need only their target lease (parallel-safe path).
- Epoch fencing: every grant carries a monotonic epoch; actions bearing a stale
  epoch are refused.
- TTL + heartbeat: a lease is live only while heartbeat is fresh.
- freeze(): emergency stop — denies everything until user-gated reset().
- Fail-closed: unknown lease, expired lease, frozen broker, scope overlap,
  unverified target => DENY. Never a frontmost/active-tab fallback.
State persists to a JSON file in the sandbox; every mutation is journaled to
the run ledger.
"""
from __future__ import annotations

import json
from pathlib import Path

import ledger as ledger_mod

# Host-aware model (Tori review B):
# - desktop-control / clipboard / focus are singletons PER HOST (one holder per host_id)
# - account-submission is GLOBAL (one holder across all hosts — the shared Google account)
PER_HOST_SINGLETONS = {"desktop-control", "clipboard", "focus"}
GLOBAL_SINGLETONS = {"account-submission"}
SINGLETON_KINDS = PER_HOST_SINGLETONS | GLOBAL_SINGLETONS
SCOPE_KEYS = ("host_id", "bundle", "user_data_dir", "window_id", "target_id")


class Deny(Exception):
    pass


class Broker:
    def __init__(self, state_path: Path, ledger_path: Path, clock=None):
        self.state_path = Path(state_path)
        self.ledger_path = Path(ledger_path)
        self._clock = clock or (lambda: 0.0)
        self.state = {"epoch_counter": 0, "frozen": False, "leases": {}}
        if self.state_path.exists():
            self.state = json.loads(self.state_path.read_text())

    # -- persistence / journal ------------------------------------------------
    def _save(self):
        self.state_path.write_text(json.dumps(self.state, sort_keys=True, indent=1))

    def _journal(self, etype, payload):
        ledger_mod.append(self.ledger_path, "broker", etype, payload)

    # -- helpers ---------------------------------------------------------------
    def _now(self):
        return float(self._clock())

    def _live(self, lease):
        if lease["state"] != "live":
            return False
        if self._now() > lease["granted_at"] + lease["ttl"]:
            return False
        if self._now() > lease["last_heartbeat"] + lease["heartbeat_interval"]:
            return False
        return True

    @staticmethod
    def _scopes_overlap(a: dict, b: dict) -> bool:
        """Hierarchical overlap: conflict unless a key both sides specify differs."""
        for key in SCOPE_KEYS:
            va, vb = a.get(key), b.get(key)
            if va is not None and vb is not None and va != vb:
                return False
        return True

    # -- API --------------------------------------------------------------------
    def acquire(self, holder: str, kind: str, mode: str = "write",
                scope: dict | None = None, ttl: float = 300.0,
                heartbeat_interval: float = 60.0) -> dict:
        if self.state["frozen"]:
            raise Deny("frozen: emergency stop active; user gate required")
        scope = scope or {}
        if kind == "target":
            if not scope.get("host_id") or not scope.get("user_data_dir"):
                raise Deny("target lease requires host_id and user_data_dir scope")
            for l in self.state["leases"].values():
                if l["kind"] != "target" or not self._live(l):
                    continue
                if self._scopes_overlap(l["scope"], scope) and ("write" in (mode, l["mode"])):
                    raise Deny(f"scope overlap with live lease {l['lease_id']}")
        elif kind in PER_HOST_SINGLETONS:
            if not scope.get("host_id"):
                raise Deny(f"{kind} lease requires a host_id scope")
            for l in self.state["leases"].values():
                if (l["kind"] == kind and self._live(l)
                        and l["scope"].get("host_id") == scope["host_id"]):
                    raise Deny(f"{kind} already held on host {scope['host_id']} by {l['holder']}")
        elif kind in GLOBAL_SINGLETONS:
            for l in self.state["leases"].values():
                if l["kind"] == kind and self._live(l):
                    raise Deny(f"{kind} already held (global) by {l['holder']}")
        else:
            raise Deny(f"unknown lease kind: {kind}")
        self.state["epoch_counter"] += 1
        lease = {
            "lease_id": f"L{self.state['epoch_counter']:05d}",
            "holder": holder, "kind": kind, "mode": mode, "scope": scope,
            "epoch": self.state["epoch_counter"],
            "granted_at": self._now(), "ttl": ttl,
            "heartbeat_interval": heartbeat_interval,
            "last_heartbeat": self._now(), "state": "live",
        }
        self.state["leases"][lease["lease_id"]] = lease
        self._save()
        self._journal("lease_granted", {k: lease[k] for k in
                      ("lease_id", "holder", "kind", "mode", "scope", "epoch")})
        return lease

    def heartbeat(self, lease_id: str):
        lease = self.state["leases"].get(lease_id)
        if not lease or not self._live(lease):
            raise Deny("heartbeat on non-live lease")
        lease["last_heartbeat"] = self._now()
        self._save()

    def check(self, lease_id: str, epoch: int, action: str,
              uses_desktop: bool = False, target_verified: bool = True) -> bool:
        """Fail-closed action gate. Every automation action calls this first."""
        if self.state["frozen"]:
            raise Deny("frozen")
        lease = self.state["leases"].get(lease_id)
        if not lease or not self._live(lease):
            raise Deny("no live lease")
        if epoch != lease["epoch"]:
            raise Deny("stale epoch (fencing)")
        if not target_verified:
            self._journal("bridge_loss", {"lease_id": lease_id, "action": action})
            lease["state"] = "revoked"
            self._save()
            raise Deny("target re-verification failed: fail closed, lease revoked")
        if uses_desktop and lease["kind"] != "desktop-control":
            raise Deny("desktop write without desktop-control lease")
        self._journal("action_allowed", {"lease_id": lease_id, "action": action})
        return True

    def release(self, lease_id: str):
        lease = self.state["leases"].get(lease_id)
        if lease and lease["state"] == "live":
            lease["state"] = "released"
            self._save()
            self._journal("lease_released", {"lease_id": lease_id})

    def freeze(self, declared_by: str, reason: str):
        """Emergency stop: anyone may call; broker freezes both sides at once."""
        self.state["frozen"] = True
        for l in self.state["leases"].values():
            if l["state"] == "live":
                l["state"] = "revoked"
        self._save()
        self._journal("emergency_stop", {"declared_by": declared_by, "reason": reason})

    def reset_after_user_gate(self, user_gate_ref: str):
        self.state["frozen"] = False
        self._save()
        self._journal("frozen_reset", {"user_gate_ref": user_gate_ref})
