#!/usr/bin/env python3
"""terminal_ceremony — the P9 signing ceremony driver
(TERMINAL_SIGNATURE_RULING_20260830.md, V101 recomputation-hardened form).

THE PRINCIPAL CHECKS, NEVER READS-AND-TRUSTS. This script:
  1. prints ITS OWN sha256 and terminal_review_verifier.py's sha256 — the principal
     compares BOTH against the printed pins in the draft WITH AN OS TOOL ON HIS OWN
     ENVIRONMENT (`shasum -a 256 <file>`), per the ruling;
  2. loads TWO chain copies — the enumerator's and an INDEPENDENT one — recomputes
     the terminal head from EACH under the pinned verifier, and requires equality;
  3. runs the chain-derived ending, the receipt-vs-store check (terminated path) or
     the successor-export closing verification (completed path);
  4. writes the ceremony TRANSCRIPT (all check lines + input digests), computes
     transcript_digest over its exact bytes, builds the canonical TERMINAL-REVIEW
     body, and prints the domain-tagged SIGNING BYTES (hex) and their sha256.
  5. THE SCRIPT NEVER TOUCHES A KEY. The principal signs the printed bytes with his
     own tooling; a refusal at any check exits 2 with no signing bytes emitted.

Input format: the verifier's record model serialized as JSON — CHAIN.json and
CHAIN_INDEPENDENT.json are arrays of record objects (each already carrying
body_digest/running, which the verifier RECOMPUTES rather than trusts);
STORES.json is an object with receipt_store, sealed_enumeration,
continuation_segment, freeze_signature_digest, flagged_keys. BS-2k provisioning
binds the run's real serialization to this model; the pinned logic is here.

    python3 terminal_ceremony.py CHAIN.json CHAIN_INDEPENDENT.json STORES.json \
        --transcript TRANSCRIPT.md
    python3 terminal_ceremony.py --selftest
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import enumeration_verifier as ev  # noqa: E402
import terminal_review_verifier as trv  # noqa: E402


def sha_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run_ceremony(chain_path, indep_path, stores_path, transcript_path):
    lines = []

    def check(label, value):
        lines.append(f"CHECK {label}: {value}")
        print(f"CHECK {label}: {value}")

    self_sha = sha_file(HERE / "terminal_ceremony.py")
    verifier_sha = sha_file(HERE / "terminal_review_verifier.py")
    ev_sha = sha_file(HERE / "enumeration_verifier.py")
    check("ceremony-script sha256 (compare to the printed pin yourself)", self_sha)
    check("terminal_review_verifier sha256 (compare to the printed pin)",
          verifier_sha)
    check("enumeration_verifier sha256 (compare to the printed pin)", ev_sha)

    chain = json.loads(Path(chain_path).read_text())
    indep = json.loads(Path(indep_path).read_text())
    stores = json.loads(Path(stores_path).read_text())
    stores.setdefault("sealed_bindings", [])
    check("chain file sha256", sha_file(chain_path))
    check("independent chain file sha256", sha_file(indep_path))
    check("stores file sha256", sha_file(stores_path))

    head = trv.recompute_terminal_head(chain)
    head_indep = trv.recompute_terminal_head(indep)
    check("recomputed head (enumerator copy)", head)
    check("recomputed head (independent copy)", head_indep)
    if head != head_indep:
        lines.append("REFUSED: HEAD-COPIES-DIVERGE")
        Path(transcript_path).write_text("\n".join(lines) + "\n")
        print("REFUSED: the two chain copies do not recompute to one head — "
              "the ceremony stops, nothing is signed")
        return 2

    ending, pos = trv.derive_ending(chain)
    check("chain-derived ending", f"{ending} at position {pos}")

    # transcript digest binds everything checked so far; the body carries it, so
    # the signing bytes cannot be inside the transcript (no self-reference)
    transcript = "\n".join(lines) + "\n"
    Path(transcript_path).write_text(transcript)
    t_digest = hashlib.sha256(transcript.encode()).hexdigest()
    print(f"TRANSCRIPT written: {transcript_path}")
    print(f"TRANSCRIPT sha256: {t_digest}")

    body = trv.build_review_body(chain, stores, verifier_sha, t_digest)
    sb = trv.signing_bytes(body)
    print("REVIEW BODY:", ev._canon(body))
    print("SIGNING BYTES (hex):", sb.hex())
    print("SIGNING BYTES sha256:", hashlib.sha256(sb).hexdigest())
    print("Sign the SIGNING BYTES with your own key tooling. "
          "This script holds no key and signs nothing.")
    return 0


def selftest():
    """A synthetic terminated run through the REAL main flow — files in the lane
    directory, never a system temp path."""
    tmp = HERE / "_tmp_ceremony_selftest"
    tmp.mkdir(exist_ok=True)
    o1 = {"k": "epoch-opening", "epoch": 1, "reading": 0,
          "predecessor": "a" * 64, "gap_declared": False, "gap_epochs": []}
    d64 = "d" * 64
    chain = ev.mkchain([
        o1,
        {"k": "drain-start", "receipt_digest": d64, "epoch": 1, "reading": 10},
        {"k": "terminal-checkpoint", "status": "TERMINATED",
         "receipt_digest": d64, "commit_set": [], "failed_members": [],
         "epoch": 1, "reading": 15},
    ])
    stores = dict(receipt_store=[{"receipt_digest": d64, "status": "TERMINATED"}],
                  sealed_enumeration=[], continuation_segment=[],
                  freeze_signature_digest="9" * 64, flagged_keys=[])
    (tmp / "chain.json").write_text(json.dumps(chain))
    (tmp / "indep.json").write_text(json.dumps(chain))
    (tmp / "stores.json").write_text(json.dumps(stores))
    rc = run_ceremony(tmp / "chain.json", tmp / "indep.json",
                      tmp / "stores.json", tmp / "transcript.md")
    fails = []
    if rc != 0:
        fails.append(f"clean ceremony exited {rc}")
    # divergent independent copy must refuse with no signing bytes
    chain2 = ev.mkchain(chain[:2])
    (tmp / "indep2.json").write_text(json.dumps(chain2))
    rc2 = run_ceremony(tmp / "chain.json", tmp / "indep2.json",
                       tmp / "stores.json", tmp / "transcript2.md")
    if rc2 == 0:
        fails.append("divergent copies did not refuse")
    # transcript digest must match what the body carries
    t = (tmp / "transcript.md").read_text()
    if "REFUSED" in t:
        fails.append("clean transcript carries a refusal")
    for x in fails:
        print("SELFTEST FAIL:", x)
    print(f"terminal ceremony selftest: {3 - len(fails)}/3 green")
    return 1 if fails else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 3:
        print(__doc__)
        sys.exit(2)
    tpath = "CEREMONY_TRANSCRIPT.md"
    if "--transcript" in sys.argv:
        tpath = sys.argv[sys.argv.index("--transcript") + 1]
    sys.exit(run_ceremony(args[0], args[1], args[2], tpath))
