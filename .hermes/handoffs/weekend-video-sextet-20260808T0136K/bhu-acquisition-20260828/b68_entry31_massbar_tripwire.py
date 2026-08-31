#!/usr/bin/env python3
"""B68 -- STANDING neutron-star mass-bar tripwire for entry 31's falsifier (RQ-E, BHU Lane 2).
Self-computing, data-driven -- the mass-bar twin of b63's curvature tripwire.

Entry 31 (Smolin CNS) predicts NO securely-measured neutron star above 2.5 Msun and is REFUTED by a
confirmed, method-agnostic, secure NS whose CENTRAL mass >= the bar. This recomputes the verdict from
entry31_massbar_ledger.json on every battery run:
  - while the heaviest SECURE central mass stays below the bar, the check PASSES -- falsifier LIVE but
    NOT FIRED (current state: 2.35 +/- 0.11 Msun, 1.36 sigma short and drifting away);
  - the moment a secure row with central >= 2.5 is added, this FAILS the battery -- a loud halt that
    says 're-gate and take it to Duho' (a refutation / tier decision = MUST-STOP).
The tripwire does NOT itself fire the falsifier or change any tier. GW secondaries of unresolved
NS-vs-BH nature (GW190814) are tracked secure=false and deliberately NOT counted; the check also
asserts that conditional row is not silently dropped nor flipped to secure."""
import json, os
_HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(_HERE, "entry31_massbar_ledger.json")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B68 -- standing NS mass-bar tripwire (entry 31 falsifier)"); print("=" * 98)

L = json.load(open(LEDGER))
BAR = float(L["bar_msun"])
secure = [m for m in L["measurements"] if m.get("secure") and m.get("mass_msun") is not None]
cond = [m for m in L["measurements"] if not m.get("secure")]

top = max(secure, key=lambda m: m["mass_msun"])
max_central = top["mass_msun"]
gap_sigma = (BAR - max_central) / top["sigma"]
crossed = [m["object"] for m in secure if m["mass_msun"] >= BAR]

print(f"  bar = {BAR} Msun | {len(secure)} secure, {len(cond)} conditional")
for m in sorted(secure, key=lambda x: -x["mass_msun"]):
    print(f"    secure   {m['object']:20} {m['mass_msun']:.2f} +/- {m['sigma']:.2f}  "
          f"({(BAR - m['mass_msun']) / m['sigma']:.2f} sigma below bar)")
for m in cond:
    print(f"    COND'L   {m['object']:20} {m['mass_msun']:.2f}  [{m['method']}] -- tracked, not counted")
print(f"  heaviest SECURE = {top['object']} at {max_central:.2f} Msun "
      f"({gap_sigma:.2f} sigma below the {BAR} bar)")

chk(f"MASS-BAR TRIPWIRE: heaviest secure NS central mass ({max_central:.2f}) is below the {BAR} Msun "
    "bar -- entry 31 CNS falsifier LIVE but NOT FIRED",
    max_central < BAR,
    (f"TRIPPED by {crossed} at/above the bar -- run a fresh two-seat gate; a confirmed secure NS "
     ">= 2.5 is a REFUTATION/tier decision for Duho (MUST-STOP)") if crossed else "")

chk("CONDITIONAL TRACKED: the GW190814 secondary (central above the bar) is present and flagged "
    "secure=false -- not silently dropped, not flipped to secure",
    any("GW190814" in m.get("object", "") and not m.get("secure") for m in L["measurements"]))

chk(f"LEDGER<->RECORD BINDING: computed gap ({gap_sigma:.2f} sigma) matches entry 31's recorded "
    "'1.36 sigma short'",
    abs(gap_sigma - 1.36) < 0.05, f"gap={gap_sigma:.3f}")

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
