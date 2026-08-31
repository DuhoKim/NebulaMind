#!/usr/bin/env python3
"""bs2k_stage — stages BS-2k provisioning (Row A) so the principal's custody acts
are short. MACHINE-SIDE ONLY: creates the store layout, generates the two machine
keypairs INTO the escrow layout (never leaving it — the ban binds), writes the
mediator configuration, materializes the committed constants and rosters, and
STAGES (does not append) Row B's epoch-1 opening. The LIVE chain starts only at
the principal's seal-state act; his required acts are printed at the end.

Everything here derives from P0-covered bytes: the constants from
ref/BS2K_CONSTANTS_COMMIT_20260831.md (ruled), the rosters from the same ruling
+ his pubkey from P0_FREEZE_SIGNATURE_20260831.md, the epoch discipline from the
frozen spec (first epoch 1, predecessor "0" — the reserved pre-first value)."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent      # run/
BASE = HERE.parent

CONSTANTS = {
    "g": 1000000, "commit_bound": 1000000000, "budget": 5000000000, "Q": 16,
    "detection": 2000000000, "D": 120000000000, "enforcement_lag": 30000000000,
    "GATE_PASS_BUDGET": 10000000000, "PASS_RETRY_MAX": 3, "R_max": 2,
    "A_max": 3, "conveyance_retry_limit": 3, "M_max": 3,
    "first_epoch": 1, "first_epoch_predecessor": "0",
}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    prov = HERE / "bs2k"
    for d in ("stores/main_sealed", "stores/receipt", "stores/label_sealed",
              "escrow", "mediator", "chain"):
        (prov / d).mkdir(parents=True, exist_ok=True)

    # the committed constants, machine-readable, digest-bound to the ruled commit
    commit_file = BASE / "ref" / "BS2K_CONSTANTS_COMMIT_20260831.md"
    constants = dict(CONSTANTS)
    constants["_source_commit_sha256"] = sha(commit_file.read_bytes())
    (prov / "constants.json").write_text(
        json.dumps(constants, indent=1, sort_keys=True) + "\n")

    # rosters from the P0 artifact (Option A, the principal alone)
    p0 = (BASE / "P0_FREEZE_SIGNATURE_20260831.md").read_text()
    pub = next(l for l in p0.splitlines() if l.startswith("ssh-ed25519 "))
    rosters = {
        "reviewer_roster": [{"reviewer_identity": "Duho Kim",
                             "reviewer_pubkey": pub}],
        "custody_holder_roster": [{"holder_identity": "Duho Kim",
                                   "holder_pubkey": pub}],
        "_rule": "Option A per the constants-and-rosters ruling; machine keys "
                 "excluded; change = re-freeze",
    }
    (prov / "rosters.json").write_text(
        json.dumps(rosters, indent=1, sort_keys=True) + "\n")

    # the two MACHINE keypairs, generated INTO the escrow (no share leaves it)
    for name in ("enumerator", "sealed_interface"):
        key = prov / "escrow" / f"{name}_ed25519"
        if not key.exists():
            subprocess.run(["ssh-keygen", "-t", "ed25519", "-N", "", "-C",
                            f"nmpr-{name}", "-f", str(key)],
                           check=True, capture_output=True)
    escrow_listing = sorted(p.name for p in (prov / "escrow").iterdir())

    # the mediator configuration: every store path reachable ONLY through it
    mediator = {
        "stores": {"main_sealed": "stores/main_sealed",
                   "receipt": "stores/receipt",
                   "label_sealed": "stores/label_sealed"},
        "rule": "no holder or run host may possess a raw-store read path "
                "outside this pinned mediator (frozen Row-A clause; "
                "enforceability is a BS-2k gate condition)",
        "verifier_tools_sha256": {
            f: sha((BASE / "gates" / f).read_bytes())
            for f in ("enumeration_verifier.py", "canonical_decoder.py",
                      "replay_harness.py")},
    }
    (prov / "mediator" / "mediator.json").write_text(
        json.dumps(mediator, indent=1, sort_keys=True) + "\n")

    # Row B's epoch-1 opening — STAGED, not appended; the chain goes live at the
    # principal's seal-state act
    opening = {"k": "epoch-opening", "epoch": 1, "reading": 0,
               "predecessor": constants["first_epoch_predecessor"],
               "gap_declared": False, "gap_epochs": []}
    (prov / "chain" / "STAGED_epoch1_opening.json").write_text(
        json.dumps(opening, indent=1, sort_keys=True) + "\n")

    # the seal-state body the principal signs at his act (holder-roster digest in)
    seal_state = {
        "archive_identity": "spin-parity predecessor archive + successor stores",
        "seal_id": "nmpr-seal-1", "seal_version": 1,
        "holder_roster_digest": sha(json.dumps(
            rosters["custody_holder_roster"], sort_keys=True).encode()),
        "checkpoint_predecessor_digest":
            "d1be4a3b61975c79f75d6bfafa75e117f69ae86e00dc81ea139a4884f62dc72a",
        "constants_digest": sha((prov / "constants.json").read_bytes()),
        "mediator_digest": sha((prov / "mediator" / "mediator.json").read_bytes()),
    }
    (prov / "STAGED_seal_state.json").write_text(
        json.dumps(seal_state, indent=1, sort_keys=True) + "\n")

    print("BS-2k STAGED under run/bs2k/:")
    print(f"  constants.json (source commit {constants['_source_commit_sha256'][:12]}…)")
    print(f"  rosters.json (his pubkey from the P0 artifact)")
    print(f"  escrow/: {escrow_listing} — machine keys generated in place")
    print(f"  mediator/mediator.json ({seal_state['mediator_digest'][:12]}…)")
    print(f"  chain/STAGED_epoch1_opening.json (epoch 1, predecessor \"0\")")
    print(f"  STAGED_seal_state.json (roots at the P0 digest)")
    print()
    print("DUHO'S ACTS (surfaced via Blanc, plain words):")
    print("  A. Review the escrow layout; the ban binds from now: no key share")
    print("     outside run/bs2k/escrow/.")
    print("  B. Sign STAGED_seal_state.json's sha256 under nmpr-p0 (one command,")
    print("     same form as P0) -> the seal state is RECORDED, the chain opens,")
    print("     provisioning is DONE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
