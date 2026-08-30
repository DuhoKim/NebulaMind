#!/usr/bin/env python3
"""B63 -- STANDING curvature tripwire for entry 54's falsifier. Self-computing, data-driven.

Duho: "wire the standing curvature check." This recomputes entry 54's curvature-falsifier verdict
from `curvature_constraints_ledger.json` on EVERY battery run. Entry 54 predicts a CLOSED universe
(Omega_k < 0) and refutes on a CONFIRMED Omega_k > 0 (OPEN). The tripwire tracks the max open-side
significance across the current-best constraints:

  - while it stays below the ledger's re-gate threshold (3 sigma), the check PASSES -- falsifier
    LIVE but NOT FIRED (current state, driven by DESI+CMB at ~2.1 sigma open);
  - when a future ledger update (a new DESI/Planck/ACT release added to the ledger) pushes the
    open-side to >= 3 sigma, this check FAILS the battery -- a loud halt that says "the tension
    crossed from hint to significant preference; run a fresh two-seat gate and take it to Duho."

The tripwire does NOT itself fire the falsifier or change any tier -- a FAIL means "re-adjudicate",
which is a Duho decision (tier/status change = MUST-STOP). It also tracks the conditional closed
limb (Omega_k <= -0.09). This is the standing check; the weekly cron watcher is the human-facing
twin, but this one lives in the battery so it cannot be forgotten (register 1ag).
"""
import json, os
_HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(_HERE, "curvature_constraints_ledger.json")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B63 -- standing curvature tripwire (entry 54 falsifier)"); print("=" * 98)

L = json.load(open(LEDGER))
THRESH = float(L["open_side_sigma_regate_threshold"])
CLOSED_LIMB = -0.09
rows = [c for c in L["constraints"] if c.get("omega_k") is not None and c.get("sigma")]

open_sig, closed_hits = {}, []
for c in rows:
    sig = c["omega_k"] / c["sigma"]          # signed significance (Omega_k>0 = open)
    if c["omega_k"] > 0:
        open_sig[c["dataset"]] = sig
    if c["omega_k"] <= CLOSED_LIMB and abs(sig) >= THRESH:
        closed_hits.append(c["dataset"])

max_open = max(open_sig.values(), default=0.0)
max_open_ds = max(open_sig, key=open_sig.get, default="(none)")
print(f"  ledger: {len(rows)} numeric constraints | re-gate threshold = {THRESH}σ open-side")
for ds, s in sorted(open_sig.items(), key=lambda kv: -kv[1]):
    print(f"    open-side  {ds:28} {s:.2f}σ")
print(f"  MAX open-side significance = {max_open:.2f}σ  ({max_open_ds})")

chk(f"OPEN-SIDE TRIPWIRE: max open-side curvature significance ({max_open:.2f}σ) is below the "
    f"{THRESH}σ re-gate threshold — entry 54 curvature falsifier LIVE but NOT FIRED",
    max_open < THRESH,
    f"TRIPPED by {max_open_ds} at {max_open:.2f}σ — run a fresh two-seat gate; a confirmed Ω_k>0 "
    f"is a REFUTATION/tier decision for Duho (MUST-STOP)" if max_open >= THRESH else "")
chk("CLOSED-LIMB TRIPWIRE: no constraint confirms the conditional closed-limb refutation "
    f"(Ω_k ≤ {CLOSED_LIMB} at ≥{THRESH}σ)",
    closed_hits == [],
    f"closed-limb TRIPPED by {closed_hits} — re-gate (conditional on the authors' χ_* identification)" if closed_hits else "")
chk("LEDGER INTEGRITY: the current-best open constraint is DESI+CMB and it is recorded as flat-"
    "consistent per the collaboration (the reason 2.1σ is a hint, not a detection)",
    any(c["dataset"] == "DESI DR2 + CMB" and c.get("collaboration_calls_flat_consistent") for c in rows))

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
