#!/usr/bin/env python3
"""CLOSURE WORKER — the custody boundary for the manifest-closure check.

CODEX-V5 F1 is why this file exists. `close_manifest()` was reduced to a single argument on the
theory that a smaller signature was a custody boundary. It is not: every pin it consults is an
ordinary mutable module global, so a caller sharing its interpreter can set a path and its
expected digest together and nominate the artifact that judges it. That seat demonstrated it
against the count table.

So the presenter no longer executes in the same interpreter as the check. This worker runs under
`python3 -I` — no user site directory, no PYTHON* environment, a fresh module graph — reads ONE
thing from the caller (the candidate manifest, as JSON on stdin), and writes one JSON receipt to
stdout. Nothing the caller can rebind is visible here.

Two things make that checkable rather than merely asserted:

  * the worker verifies the subject module's bytes against SUBJECT_SHA256 below before importing
    it, and refuses if they differ;
  * the receipt carries the digest of THIS FILE and of the subject, measured here, alongside
    every artifact digest the check itself measured.

WHAT THIS BOUNDARY DOES NOT BUY, stated plainly because the last version of this claim was
too strong. `-I` excludes PYTHON* environment variables, the script directory, and the user
site directory — but numpy lives in that user site directory on this machine, so the worker
appends exactly one pinned path back. A caller who can write to that directory can still
influence what numpy is. That is a different and larger threat than the one CODEX-V5 F1
demonstrated (an in-process caller rebinding this module's own globals), and it is not closed
here. The full sys.path the worker ran with is recorded in the receipt so the gate can see it
rather than take my word for it.

A gate outside the presenter compares those numbers with the ones in the committed brief. That
comparison is the part no code inside either process can perform for itself — which is the point
CODEX was making, and it is why the receipt states its own provenance instead of claiming it.

Exit codes: 0 the manifest closes, 2 it is refused, 1 the worker could not run.
Usage: echo '{"manifest": ["0001m250", ...]}' | python3 -I closure_worker_v7.py [--work-dir DIR]
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUBJECT = HERE / "successor_ref_v7.py"
# `-I` gives a minimal sys.path, which excludes the user site directory where numpy lives on
# this machine. Rather than drop isolation, the worker names the ONE directory it adds back.
# What that does and does not buy is stated in the module docstring and recorded in the receipt.
PINNED_SITE_DIR = "/Users/duhokim/Library/Python/3.9/lib/python/site-packages"
SUBJECT_SHA256 = "6be341bd443d45c42eecd6b47e806f652882c971827300d51ff6fcb568069f33"


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def fail(message, code=1, **extra):
    json.dump({"outcome": "WORKER-ERROR", "message": message, **extra}, sys.stdout, indent=2)
    sys.stdout.write("\n")
    sys.exit(code)


def main() -> int:
    ap = argparse.ArgumentParser(description="run one manifest closure in an isolated process")
    ap.add_argument("--work-dir", default="", help="private scratch for verified snapshots")
    ap.add_argument("--self-check", action="store_true",
                    help="print this worker's and the subject's digests, then exit")
    args = ap.parse_args()

    worker_sha = sha256_bytes(Path(__file__).read_bytes())
    if not SUBJECT.is_file():
        fail(f"subject missing: {SUBJECT}")
    subject_bytes = SUBJECT.read_bytes()
    subject_sha = sha256_bytes(subject_bytes)

    if args.self_check:
        json.dump({"outcome": "SELF-CHECK", "worker": str(SUBJECT.parent / "closure_worker_v7.py"),
                   "worker_sha256": worker_sha, "subject_sha256": subject_sha,
                   "subject_pin": SUBJECT_SHA256,
                   "subject_matches_pin": subject_sha == SUBJECT_SHA256},
                  sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
        return 0

    if SUBJECT_SHA256 != "REPLACED_AT_PIN_TIME" and subject_sha != SUBJECT_SHA256:
        fail(f"SUBJECT DIGEST MISMATCH: {subject_sha} != pinned {SUBJECT_SHA256}",
             subject_sha256=subject_sha, subject_pin=SUBJECT_SHA256)

    try:
        request = json.loads(sys.stdin.read() or "{}")
    except ValueError as exc:
        fail(f"stdin is not JSON: {exc}")
    if not isinstance(request, dict) or "manifest" not in request:
        fail("stdin must be a JSON object carrying a 'manifest' key")
    manifest = request["manifest"]
    # KIMI-V6 F6: iterating a JSON object yields its keys, so a dict manifest was accepted and
    # reported 12,117 entries. It cannot under-cover, but an unvalidated type at the trust
    # boundary is the thing R06 and R07 exist to refuse.
    if manifest is not None and not isinstance(manifest, list):
        fail(f"'manifest' must be a JSON array or null, got {type(manifest).__name__}",
             code=1, manifest_type=type(manifest).__name__)

    if PINNED_SITE_DIR not in sys.path:
        sys.path.append(PINNED_SITE_DIR)

    spec = importlib.util.spec_from_file_location("closure_subject", SUBJECT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    provenance = {"worker_sha256": worker_sha, "subject_sha256": subject_sha,
                  "subject_pin": SUBJECT_SHA256, "python": sys.version.split()[0],
                  "isolated": sys.flags.isolated == 1,
                  "ignore_environment": sys.flags.ignore_environment == 1,
                  "no_user_site": sys.flags.no_user_site == 1,
                  # Recorded, not summarised: a gate can see exactly what was importable.
                  "sys_path": [p for p in sys.path if p],
                  "pinned_site_dir": PINNED_SITE_DIR,
                  "manifest_entries": None if manifest is None else len(manifest)}
    if not provenance["isolated"]:
        # Refusing rather than warning: an un-isolated interpreter can inherit a user site
        # directory, which is exactly the shared state this boundary exists to exclude.
        fail("worker was not started with -I; refusing to run outside isolated mode",
             **provenance)

    holder = Path(args.work_dir) if args.work_dir else Path(tempfile.mkdtemp(prefix="closure_"))
    try:
        result = mod.close_manifest(manifest, snapshot_dir=holder)
        out = {"outcome": "PASS", "provenance": provenance, "result": result}
        code = 0
    except mod.ManifestClosureError as exc:
        out = {"outcome": "REFUSE", "provenance": provenance, "message": str(exc),
               "result": getattr(exc, "result", None)}
        code = 2
    json.dump(out, sys.stdout, indent=2, sort_keys=True, default=str)
    sys.stdout.write("\n")
    return code


if __name__ == "__main__":
    sys.exit(main())
