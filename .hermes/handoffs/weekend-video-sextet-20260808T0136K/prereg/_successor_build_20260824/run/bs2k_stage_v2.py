#!/usr/bin/env python3
"""Stage the frozen BS-2k Row-A materials, without opening the live chain.

Frozen sources (PREREG_SUCCESSOR_DRAFT_V134_20260831.md):

* Row A: "creates the two new stores' containers and brings the predecessor
  archive under the mediator; generates, splits and escrows the keys" and
  records its identity/seal state "by non-content metadata operation".
* Row B is "the only path" to "any of the three" sealed stores and "Opens
  every epoch with a RECOVERY CHECKPOINT".
* Clause 7: "The canonical authenticated seal-state schema binds archive
  identity, seal identifier/version, holder-roster digest, checkpoint
  predecessor digest, and monotonic event/epoch data."
* Row L designates holders at BS-2k.  This is discharged by reference to the
  ruled option label: "Option A (principal alone)" in the constants-and-
  rosters ruling.  No new principal signature is requested or made.

P0_FREEZE_SIGNATURE_20260831.md already discharges Row A's Duho-keypair clause
and binds his public half.  Machine authentication uses ssh-keygen -Y sign,
namespace nmpr-rowa, only at the explicit --go-live transition.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import secrets
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import re
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PROV = HERE / "bs2k"
ESCROW = PROV / "escrow"
CHAIN = PROV / "chain"
MANIFEST = PROV / "STAGED_manifest.json"
P0_DIGEST = "d1be4a3b61975c79f75d6bfafa75e117f69ae86e00dc81ea139a4884f62dc72a"
V9_REFERENCE = BASE / "ref" / "successor_ref_v9.py"
X2_COMMIT = HERE / "OPERATION_SET_COMMIT_20260831.md"
SEAL_FIELDS = frozenset(("archive_identity", "seal_identifier_version",
                         "holder_roster_digest", "checkpoint_predecessor_digest",
                         "monotonic_event_epoch_data"))
OPENING_FIELDS = frozenset(("boot_epoch", "monotonic_reading",
                            "predecessor_epoch", "gap_declaration"))
REFUSAL_CORRUPT_SHARE = "REFUSED-CORRUPT-SHARE"
REFUSAL_SCHEMA = "REFUSED-SCHEMA-NONCONFORMING"
REFUSAL_DRIFT = "REFUSED-STAGED-DRIFT"
REFUSAL_DIRECT = "REFUSED-RAW-STORE-PATH"
REFUSAL_TRAVERSAL = "REFUSED-STORE-PATH-TRAVERSAL"


class Refusal(RuntimeError):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":"),
                       sort_keys=True) + "\n").encode()


def atomic_write(path: Path, data: bytes, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(data)
    os.chmod(tmp, mode)
    os.replace(tmp, path)


def monotonic_ms() -> int:
    return time.monotonic_ns() // 1_000_000


def validate_exact(obj: dict[str, Any], fields: frozenset[str]) -> None:
    if set(obj) != fields:
        raise Refusal(REFUSAL_SCHEMA)


def canonical_roster(kind: str, entries: list[tuple[str, str]]) -> bytes:
    if kind not in ("reviewer-roster", "holder-roster"):
        raise Refusal(REFUSAL_SCHEMA)
    ordered = sorted(entries, key=lambda pair: pair[0].encode("utf-8"))
    if len({identity for identity, _ in ordered}) != len(ordered):
        raise Refusal(REFUSAL_SCHEMA)
    field = lambda s: str(len(s.encode("utf-8"))).encode() + b":" + s.encode()
    return field(kind) + str(len(ordered)).encode() + b":" + b"".join(
        field(identity) + field(pubkey) for identity, pubkey in ordered)


def x2_encoding(tokens: tuple[str, ...]) -> bytes:
    if tuple(sorted(tokens)) != tokens or len(set(tokens)) != len(tokens):
        raise Refusal(REFUSAL_SCHEMA)
    return f"{len(tokens)}:{','.join(tokens)}".encode()


def v9_literal(name: str) -> str | None:
    tree = ast.parse(V9_REFERENCE.read_bytes(), filename=str(V9_REFERENCE))
    found: str | None = None
    # The v9 constants are module-top-level by inspection. Nested scopes and
    # assignments inside compound statements are intentionally out of scope.
    for node in tree.body:
        if (isinstance(node, (ast.Assign, ast.AnnAssign)) and
                ((isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name
                                                       for t in node.targets)) or
                 (isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name)
                  and node.target.id == name))):
            value = ast.literal_eval(node.value)
            if not isinstance(value, str):
                raise Refusal(REFUSAL_SCHEMA)
            found = value
    return found


def x2_material() -> tuple[tuple[str, ...], bytes, str, str]:
    raw = X2_COMMIT.read_bytes()
    text = raw.decode("utf-8")
    blocks = re.findall(r"```[^\n]*\n(.*?)```", text, flags=re.DOTALL)
    candidates = [tuple(line.strip() for line in block.splitlines() if line.strip())
                  for block in blocks]
    candidates = [tokens for tokens in candidates if len(tokens) == 6]
    if len(candidates) != 1:
        raise Refusal(REFUSAL_SCHEMA)
    tokens = candidates[0]
    canonical = x2_encoding(tokens)
    match = re.search(r"\*\*Set digest[^\n]*:\*\*\s*`([0-9a-f]{64})`", text)
    if match is None or sha(canonical) != match.group(1):
        raise Refusal(REFUSAL_DRIFT)
    return tokens, canonical, match.group(1), sha(raw)


def xor_bytes(left: bytes, right: bytes) -> bytes:
    if len(left) != len(right):
        raise Refusal(REFUSAL_CORRUPT_SHARE)
    return bytes(a ^ b for a, b in zip(left, right))


def recombine_private(name: str) -> bytes:
    meta_path = ESCROW / f"{name}_shares.json"
    try:
        meta = json.loads(meta_path.read_bytes())
        a = (ESCROW / meta["shares"][0]).read_bytes()
        b = (ESCROW / meta["shares"][1]).read_bytes()
        private = xor_bytes(a, b)
    except (OSError, KeyError, ValueError, TypeError, json.JSONDecodeError):
        raise Refusal(REFUSAL_CORRUPT_SHARE)
    if len(private) != meta.get("private_length") or sha(private) != meta.get("private_sha256"):
        raise Refusal(REFUSAL_CORRUPT_SHARE)
    return private


def secure_remove(path: Path) -> None:
    if not path.exists():
        return
    size = path.stat().st_size
    with path.open("r+b", buffering=0) as stream:
        stream.write(b"\0" * size)
        stream.flush()
        os.fsync(stream.fileno())
    path.unlink()


def provision_key(name: str) -> str:
    ESCROW.mkdir(parents=True, exist_ok=True)
    os.chmod(ESCROW, 0o700)
    meta = ESCROW / f"{name}_shares.json"
    public = ESCROW / f"{name}_ed25519.pub"
    unsplit = ESCROW / f"{name}_ed25519"
    if not meta.exists():
        if not unsplit.exists():
            subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "",
                            "-C", f"nmpr-{name}", "-f", str(unsplit)], check=True)
        private = unsplit.read_bytes()
        share_a = secrets.token_bytes(len(private))
        share_b = xor_bytes(private, share_a)
        a_name, b_name = f"{name}.share-a", f"{name}.share-b"
        atomic_write(ESCROW / a_name, share_a)
        atomic_write(ESCROW / b_name, share_b)
        atomic_write(meta, canonical_json({"private_length": len(private),
                                           "private_sha256": sha(private),
                                           "shares": [a_name, b_name]}))
        secure_remove(unsplit)
    elif unsplit.exists():
        secure_remove(unsplit)
    recombine_private(name)
    return public.read_text().strip()


def archive_identity() -> dict[str, Any]:
    receipt_rel = v9_literal("PINNED_PARENT_RECEIPTS_REL")
    if receipt_rel is None:
        raise Refusal(REFUSAL_SCHEMA)
    # v9's path is relative to the prereg lane, one level above BASE.
    receipt = BASE.parent / receipt_rel
    raw = receipt.read_bytes()  # metadata only; archive contents are never read
    live_digest = sha(raw)
    pinned_digest = v9_literal("PINNED_PARENT_RECEIPTS_SHA256")
    if pinned_digest is None:
        raise Refusal(REFUSAL_SCHEMA)
    if live_digest != pinned_digest:
        raise Refusal(REFUSAL_DRIFT)
    body = json.loads(raw)
    identity = {"pinned_parent_receipts_rel": receipt_rel,
                "live_parent_receipts_sha256": live_digest,
                "receipt_output_sha256": body.get("output_sha256")}
    identity["v9_pinned_parent_receipts_sha256"] = pinned_digest
    return identity


def mediator_read(root: Path, relative: str = ".boundary-probe") -> bytes:
    allowed = {p.resolve() for p in store_roots()}
    resolved_root = root.resolve()
    if resolved_root not in allowed:
        raise Refusal(REFUSAL_DIRECT)
    requested = Path(relative)
    if requested.is_absolute() or ".." in requested.parts:
        raise Refusal(REFUSAL_TRAVERSAL)
    resolved_target = (resolved_root / requested).resolve()
    try:
        resolved_target.relative_to(resolved_root)
    except ValueError:
        raise Refusal(REFUSAL_TRAVERSAL)
    return resolved_target.read_bytes()


def store_roots() -> tuple[Path, ...]:
    return tuple(PROV / "stores" / name for name in
                 ("main_sealed", "committee_sealed", "predecessor_archive"))


def staged_paths() -> tuple[Path, ...]:
    return (PROV / "constants.json", PROV / "rosters.json",
            PROV / "mediator" / "mediator.json", PROV / "STAGED_seal_state.json",
            PROV / "STAGED_RowA_receipt.json",
            CHAIN / "STAGED_epoch1_opening.json")


def manifest_materials() -> dict[str, Path]:
    materials = {str(path.relative_to(PROV)): path for path in staged_paths()}
    materials["../OPERATION_SET_COMMIT_20260831.md"] = X2_COMMIT
    return materials


def stage() -> dict[str, str]:
    for root in store_roots():
        root.mkdir(parents=True, exist_ok=True)
        os.chmod(root, 0o700)
        atomic_write(root / ".boundary-probe", b"mediator-boundary-green\n")
    enumerator_pub = provision_key("enumerator")
    interface_pub = provision_key("sealed_interface")
    p0_text = (BASE / "P0_FREEZE_SIGNATURE_20260831.md").read_text()
    duho_pub = next(line for line in p0_text.splitlines() if line.startswith("ssh-ed25519 "))

    roster_entries = [("Duho Kim", duho_pub)]
    rosters = []
    roster_digests: dict[str, str] = {}
    for kind in ("reviewer-roster", "holder-roster"):
        canonical = canonical_roster(kind, roster_entries)
        roster_digests[kind] = sha(canonical)
        rosters.append({"kind": kind,
                        "roster_entries": [{"identity": i, "pubkey": p} for i, p in roster_entries],
                        "canonical_encoding": canonical.decode(), "sha256": sha(canonical)})
    atomic_write(PROV / "rosters.json", canonical_json(rosters))

    x2_tokens, x2_canonical, x2_digest, x2_commit_digest = x2_material()
    constants_commit = BASE / "ref" / "BS2K_CONSTANTS_COMMIT_20260831.md"
    constants = {"g": 1_000_000, "commit_bound": 1_000_000_000,
                 "budget": 5_000_000_000, "Q": 16,
                 "detection": 2_000_000_000, "D": 120_000_000_000,
                 "enforcement_lag": 30_000_000_000,
                 "GATE_PASS_BUDGET": 10_000_000_000, "PASS_RETRY_MAX": 3,
                 "R_max": 2, "A_max": 3, "conveyance_retry_limit": 3,
                 "M_max": 3, "boot_epoch": 1, "predecessor_epoch": 0,
                 "holder_designation": "Option A (principal alone)",
                 "p0_keypair_discharge": "P0_FREEZE_SIGNATURE_20260831.md",
                 "p0_public_key": duho_pub,
                 "source_commit_sha256": sha(constants_commit.read_bytes())}
    atomic_write(PROV / "constants.json", canonical_json(constants))
    mediator = {
        "stores": {name: str(root.relative_to(PROV)) for name, root in zip(
            ("main_sealed", "committee_sealed", "predecessor_archive"), store_roots())},
        "store_root_mode": "0700", "boundary": "mediator-capability-process-model",
        "posix_residual": "On a single-user POSIX machine, owner/root can bypass directory modes.",
        "machine_signers": {
            "enumerator": {"identity": "nmpr-enumerator", "public_key": enumerator_pub,
                           "signature_namespace": "nmpr-rowa"},
            "sealed_interface": {"identity": "nmpr-sealed-interface", "public_key": interface_pub},
        }}
    atomic_write(PROV / "mediator" / "mediator.json", canonical_json(mediator))
    materials = {
        "constants_sha256": sha((PROV / "constants.json").read_bytes()),
        "mediator_sha256": sha(canonical_json(mediator)),
        "reviewer_roster_sha256": roster_digests["reviewer-roster"],
        "machine_signers": mediator["machine_signers"],
        "machine_public_keys_sha256": sha(canonical_json(mediator["machine_signers"])),
        "x2": {"tokens": list(x2_tokens), "canonical_encoding": x2_canonical.decode(),
               "set_sha256": x2_digest, "commit_file_sha256": x2_commit_digest},
    }
    seal = {
        "archive_identity": archive_identity(),
        "seal_identifier_version": {"identifier": "nmpr-bs2k-seal-state", "version": 1},
        "holder_roster_digest": roster_digests["holder-roster"],
        "checkpoint_predecessor_digest": P0_DIGEST,
        "monotonic_event_epoch_data": {"boot_epoch": 1, "monotonic_reading": monotonic_ms(),
                                       "provisioning_materials": materials},
    }
    validate_exact(seal, SEAL_FIELDS)
    atomic_write(PROV / "STAGED_seal_state.json", canonical_json(seal))
    rowa_receipt = {"seal_state_sha256": sha(canonical_json(seal)),
                    "signer_identity": "nmpr-enumerator",
                    "signature_namespace": "nmpr-rowa",
                    "authentication_state": "STAGED-NOT-SIGNED"}
    atomic_write(PROV / "STAGED_RowA_receipt.json", canonical_json(rowa_receipt))
    opening = {"boot_epoch": 1, "monotonic_reading": monotonic_ms(),
               "predecessor_epoch": 0, "gap_declaration": ""}
    validate_exact(opening, OPENING_FIELDS)
    atomic_write(CHAIN / "STAGED_epoch1_opening.json", canonical_json(opening))
    digests = {name: sha(path.read_bytes()) for name, path in manifest_materials().items()}
    atomic_write(MANIFEST, canonical_json({"artifacts": digests}))
    return digests


def verify_staged() -> dict[str, str]:
    try:
        expected = json.loads(MANIFEST.read_bytes())["artifacts"]
    except (OSError, KeyError, json.JSONDecodeError):
        raise Refusal(REFUSAL_DRIFT)
    actual = {name: sha(path.read_bytes()) for name, path in manifest_materials().items()}
    if actual != expected:
        raise Refusal(REFUSAL_DRIFT)
    validate_exact(json.loads((PROV / "STAGED_seal_state.json").read_bytes()), SEAL_FIELDS)
    validate_exact(json.loads((CHAIN / "STAGED_epoch1_opening.json").read_bytes()), OPENING_FIELDS)
    return actual


def go_live() -> None:
    verify_staged()  # mandatory drift check before any live write
    opening = {"boot_epoch": 1, "monotonic_reading": monotonic_ms(),
               "predecessor_epoch": 0, "gap_declaration": ""}
    atomic_write(CHAIN / "epoch1_opening.json", canonical_json(opening))
    seal_bytes = (PROV / "STAGED_seal_state.json").read_bytes()
    body_digest = sha(seal_bytes)
    temp_key = ESCROW / ".enumerator.recombined"
    atomic_write(temp_key, recombine_private("enumerator"))
    try:
        digest_file = CHAIN / "RowA_seal_state.sha256"
        atomic_write(digest_file, (body_digest + "\n").encode())
        subprocess.run(["ssh-keygen", "-Y", "sign", "-f", str(temp_key),
                        "-n", "nmpr-rowa", str(digest_file)], check=True,
                       capture_output=True)
    finally:
        secure_remove(temp_key)
    receipt = {"opening_sha256": sha((CHAIN / "epoch1_opening.json").read_bytes()),
               "rowa_seal_body_sha256": body_digest,
               "rowa_signature": "RowA_seal_state.sha256.sig",
               "signer_identity": "nmpr-enumerator"}
    atomic_write(CHAIN / "GO_LIVE_receipt.json", canonical_json(receipt))
    print(json.dumps(receipt, sort_keys=True))


def expect_refusal(code: str, fn) -> None:
    try:
        fn()
    except Refusal as exc:
        if exc.code == code:
            return
    raise AssertionError(f"expected {code}")


def fixtures() -> tuple[int, int]:
    checks = []
    def check(fn):
        fn(); checks.append(True)
    check(lambda: all(mediator_read(root) == b"mediator-boundary-green\n" for root in store_roots()))
    check(lambda: all(stat.S_IMODE(root.stat().st_mode) == 0o700 for root in store_roots()))
    check(lambda: all((expect_refusal(REFUSAL_TRAVERSAL,
                                     lambda r=root: mediator_read(r, "../.boundary-probe")) or True)
                      for root in store_roots()))
    check(lambda: expect_refusal(REFUSAL_DIRECT,
                                 lambda: mediator_read(PROV.parent / "unallowed-sibling")))
    def symlink_escape():
        root = store_roots()[0]
        with tempfile.TemporaryDirectory(dir=HERE) as outside:
            target = Path(outside) / "outside"
            target.write_bytes(b"must-not-be-readable")
            link = root / ".boundary-symlink"
            try:
                link.symlink_to(target)
                expect_refusal(REFUSAL_TRAVERSAL,
                               lambda: mediator_read(root, link.name))
            finally:
                link.unlink(missing_ok=True)
    check(symlink_escape)
    check(lambda: all((root / ".boundary-probe").read_bytes() ==
                      b"mediator-boundary-green\n" for root in store_roots()))
    check(lambda: all(recombine_private(name).startswith(b"-----BEGIN OPENSSH PRIVATE KEY-----")
                      for name in ("enumerator", "sealed_interface")))
    def corrupt():
        name = "enumerator"; meta = json.loads((ESCROW / f"{name}_shares.json").read_bytes())
        path = ESCROW / meta["shares"][0]; original = path.read_bytes()
        try:
            atomic_write(path, bytes([original[0] ^ 1]) + original[1:])
            expect_refusal(REFUSAL_CORRUPT_SHARE, lambda: recombine_private(name))
        finally:
            atomic_write(path, original)
    check(corrupt)
    seal = json.loads((PROV / "STAGED_seal_state.json").read_bytes())
    check(lambda: (validate_exact(seal, SEAL_FIELDS),
                   expect_refusal(REFUSAL_SCHEMA, lambda: validate_exact({**seal, "extra": 1}, SEAL_FIELDS)),
                   expect_refusal(REFUSAL_SCHEMA, lambda: validate_exact({k:v for k,v in seal.items() if k != "archive_identity"}, SEAL_FIELDS))))
    opening = json.loads((CHAIN / "STAGED_epoch1_opening.json").read_bytes())
    check(lambda: (validate_exact(opening, OPENING_FIELDS),
                   expect_refusal(REFUSAL_SCHEMA, lambda: validate_exact({**opening, "extra": 1}, OPENING_FIELDS))))
    check(lambda: canonical_roster("holder-roster", [("b", "k2"), ("a", "k1")]) ==
                  canonical_roster("holder-roster", [("a", "k1"), ("b", "k2")]))
    check(lambda: sha(canonical_roster("holder-roster", [("a", "k1")])) !=
                  sha(canonical_roster("holder-roster", [("a", "k2")])) )
    check(lambda: sha(x2_material()[1]) == x2_material()[2])
    def missing_v9_pin():
        global V9_REFERENCE
        original = V9_REFERENCE
        with tempfile.TemporaryDirectory(dir=HERE) as tmp:
            copy = Path(tmp) / "v9.py"
            source = re.sub(r"^PINNED_PARENT_RECEIPTS_SHA256\s*=.*\n", "",
                            original.read_text(), flags=re.MULTILINE)
            copy.write_text(source)
            try:
                V9_REFERENCE = copy
                expect_refusal(REFUSAL_SCHEMA, archive_identity)
            finally:
                V9_REFERENCE = original
    check(missing_v9_pin)
    def last_v9_assignment():
        global V9_REFERENCE
        original = V9_REFERENCE
        with tempfile.TemporaryDirectory(dir=HERE) as tmp:
            copy = Path(tmp) / "v9.py"
            copy.write_text('VALUE = "first"\nVALUE = "second"\n')
            try:
                V9_REFERENCE = copy
                assert v9_literal("VALUE") == "second"
            finally:
                V9_REFERENCE = original
    check(last_v9_assignment)
    def drift():
        target = PROV / "constants.json"; original = target.read_bytes()
        try:
            target.write_bytes(original + b"x")
            expect_refusal(REFUSAL_DRIFT, verify_staged)
        finally:
            target.write_bytes(original)
    check(drift)
    def commitment_drift():
        original = X2_COMMIT.read_bytes()
        try:
            X2_COMMIT.write_bytes(original + b"\n")
            expect_refusal(REFUSAL_DRIFT, verify_staged)
        finally:
            X2_COMMIT.write_bytes(original)
    check(commitment_drift)
    return len(checks), 17


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--go-live", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.go_live:
            go_live()
            return 0
        digests = stage()
        green, total = fixtures()
        if green != total:
            raise AssertionError((green, total))
        for name, digest in sorted(digests.items()):
            print(f"{name} sha256 {digest}")
        print(f"staging-v2 fixtures: {green}/{total} green")
        return 0
    except Refusal as exc:
        print(exc.code, file=sys.stderr)
        return {REFUSAL_CORRUPT_SHARE: 21, REFUSAL_SCHEMA: 22,
                REFUSAL_DRIFT: 23, REFUSAL_DIRECT: 24,
                REFUSAL_TRAVERSAL: 25}.get(exc.code, 20)


if __name__ == "__main__":
    sys.exit(main())
