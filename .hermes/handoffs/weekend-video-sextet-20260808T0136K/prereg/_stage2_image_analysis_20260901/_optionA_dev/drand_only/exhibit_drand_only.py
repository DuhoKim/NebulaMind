#!/usr/bin/env python3
"""EXHIBIT for the drand-only proposal: (A) the prospective round rule computed from a HYPOTHETICAL approval time; (B) ACTUAL BLS verification
of an already-public historical round (6441924) retrieved from two relays by the chain-hash path — verifies under the pinned key; a tampered
signature FAILS; the same response under a wrong key FAILS; (C) the same verification run twice gives identical results (deterministic).
No beacon read for any run is performed; the round used is public history. Output is deterministic and its digest is filed."""
import json, hashlib, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import verify_drand as vd
def run():
    out = {}
    out["A_prospective_round"] = vd.prospective_round(datetime(2026, 9, 7, 1, 0, 7, tzinfo=timezone.utc))      # hypothetical approval 2026-09-07T01:00:07Z
    a = json.loads((HERE / "round_6441924_api.drand.sh.json").read_text()); b = json.loads((HERE / "round_6441924_api2.drand.sh.json").read_text())
    out["B_two_relays_agree_bytewise"] = a == b
    out["B_verify_api"] = vd.verify(a, 6441924, vd.round_url("https://api.drand.sh", 6441924))
    out["B_verify_api2"] = vd.verify(b, 6441924, vd.round_url("https://api2.drand.sh", 6441924))
    t = dict(a); t["signature"] = a["signature"][:-2] + ("00" if a["signature"][-2:] != "00" else "11"); out["B_tampered_signature"] = vd.verify(t, 6441924)
    wrong_url = vd.verify(a, 6441924, "https://api.drand.sh/public/6441924"); out["B_unbound_path_refused"] = wrong_url["accepted"] is False and wrong_url["url_bound_to_chain_hash"] is False
    saved = vd.PUBLIC_KEY_HEX; vd.PUBLIC_KEY_HEX = "8" + saved[1:] if saved[0] != "8" else "9" + saved[1:]
    try: out["B_wrong_key"] = vd.verify(a, 6441924)["bls_verifies_under_pinned_key"]
    finally: vd.PUBLIC_KEY_HEX = saved
    out["C_run_twice_identical"] = vd.verify(a, 6441924) == vd.verify(a, 6441924)
    out["pinned"] = {"chain_hash": vd.CHAIN_HASH, "public_key": vd.PUBLIC_KEY_HEX, "genesis": vd.GENESIS, "period": vd.PERIOD, "scheme": vd.SCHEME, "dst": vd.G2Basic.DST.decode()}
    return out
if __name__ == "__main__":
    res = run(); text = json.dumps(res, indent=1, sort_keys=True) + "\n"; print(text)
    ok = res["B_verify_api"]["accepted"] and res["B_verify_api2"]["accepted"] and not res["B_tampered_signature"]["accepted"] and res["B_unbound_path_refused"] and res["B_wrong_key"] is False and res["C_run_twice_identical"] and not res["A_prospective_round"]["exists_at_approval"]
    print("EXHIBIT OK:", ok); print("EXHIBIT-DIGEST:", hashlib.sha256(text.encode()).hexdigest())
