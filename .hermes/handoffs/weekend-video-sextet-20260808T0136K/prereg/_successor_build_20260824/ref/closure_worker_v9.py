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
    every artifact digest the check itself measured, AND the interpreter state -- the flags and
    the full sys.path -- captured before the isolation gate so that even a refusal carries it.
    `closure_receipt()` returns that provenance beside the result, which is what makes the
    sys.path claim true of every receipt rather than of none (KIMI-V8 F3: in v8 it was true of
    none, and two written claims said otherwise).

WHAT THIS BOUNDARY DOES NOT BUY, stated plainly because the last version of this claim was
too strong. `-I` excludes PYTHON* environment variables, the script directory, and the user
site directory — but numpy lives in that user site directory on this machine, so the worker
appends exactly one pinned path back. numpy is not the whole of it: astropy, which PARSES the
geometry sidecar, resolves from the same unpinned directory, as do erfa, scipy and yaml. The
sidecar's bytes are pinned; its parser is not. A caller who can write to that directory, or to
the CommandLineTools site-packages that still precedes the add-back, can influence what those
modules are. That is a different and larger threat than the one CODEX-V5 F1 demonstrated (an
in-process caller rebinding this module's own globals), and it is NOT closed here.

The full sys.path the worker ran with is recorded in the receipt — and in a refusal, since the
interpreter state is captured before the isolation gate — so the gate can see it rather than
take my word for it. Probes W03 and B04 assert that; this paragraph does not establish it.

A gate outside the presenter compares those numbers with the ones in the committed brief. That
comparison is the part no code inside either process can perform for itself — which is the point
CODEX was making, and it is why the receipt states its own provenance instead of claiming it.

Exit codes: 0 the manifest closes, 2 it is refused, 1 the worker could not run.
Usage: echo '{"manifest": ["0001m250", ...]}' | python3 -I closure_worker_v9.py [--work-dir DIR]
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
SUBJECT = HERE / "successor_ref_v9.py"
# `-I` gives a minimal sys.path, which excludes the user site directory where numpy lives on
# this machine. Rather than drop isolation, the worker names the ONE directory it adds back.
# What that does and does not buy is stated in the module docstring and recorded in the receipt.
PINNED_SITE_DIR = "/Users/duhokim/Library/Python/3.9/lib/python/site-packages"
SUBJECT_SHA256 = "6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148"


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

    # KIMI-V7 F2: this check used to run AFTER the subject was imported, so an un-isolated
    # interpreter executed the code the check exists to distrust. That seat demonstrated it with
    # a poisoned numpy on PYTHONPATH: the sentinel fired during the import and the worker then
    # died with an uncaught traceback instead of a JSON receipt. The flag is fixed at
    # interpreter startup, so nothing is lost by asking first.
    # v9 (KIMI-V8 F3): interpreter-state provenance needs no file reads, so it can be built
    # before the isolation check and carried by the refusal. In v8 the check refused first and
    # provenance was built after, which was right for isolation and silently removed the only
    # sys.path record any receipt carried -- while the docstring still promised one.
    interpreter = {"python": sys.version.split()[0],
                   "isolated": sys.flags.isolated == 1,
                   "ignore_environment": sys.flags.ignore_environment == 1,
                   "no_user_site": sys.flags.no_user_site == 1,
                   "sys_path": [q for q in sys.path if q],
                   "pinned_site_dir": PINNED_SITE_DIR}
    if sys.flags.isolated != 1:
        fail("worker was not started with -I; refusing before reading or importing anything",
             **interpreter)

    worker_sha = sha256_bytes(Path(__file__).read_bytes())
    if not SUBJECT.is_file():
        fail(f"subject missing: {SUBJECT}")
    subject_bytes = SUBJECT.read_bytes()
    subject_sha = sha256_bytes(subject_bytes)

    if args.self_check:
        json.dump({"outcome": "SELF-CHECK", "worker": str(SUBJECT.parent / "closure_worker_v9.py"),
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

    # KIMI-V7 F1: the worker hashed SUBJECT's bytes and then imported the PATH, which opens and
    # reads the file a second time. Verification and consumption were two reads with a window
    # between them, so verified code was not provably the code executed -- the one place in this
    # mechanism where I5 was asserted rather than held by construction. That seat demonstrated
    # the two opens with an audit hook.
    #
    # The already-verified bytes are executed instead. __file__ is the real subject path because
    # the subject resolves every pinned artifact relative to it
    # (Path(__file__).resolve().parents[2]); __loader__ and __spec__ stay unset, which is what
    # marks this module as not having come from the import system.
    import types
    mod = types.ModuleType("closure_subject")
    mod.__file__ = str(SUBJECT)
    sys.modules["closure_subject"] = mod
    exec(compile(subject_bytes, str(SUBJECT), "exec"), mod.__dict__)

    # Recorded, not summarised: a gate sees exactly what was importable. sys_path is the one
    # captured before the isolation gate; sys_path_at_import is after the pinned add-back.
    provenance = {"worker_sha256": worker_sha, "subject_sha256": subject_sha,
                  "subject_pin": SUBJECT_SHA256,
                  "manifest_entries": None if manifest is None else len(manifest),
                  **interpreter,
                  "sys_path_at_import": [q for q in sys.path if q]}

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
