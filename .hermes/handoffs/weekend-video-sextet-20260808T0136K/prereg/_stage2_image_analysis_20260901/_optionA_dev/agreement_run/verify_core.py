"""Read-only consumer CLI: verify_core.py CORE_PATH EXPECTED_CORE_SHA256.

Start as a source script with the prescribed interpreter. Bootstrap integrity
checks precede own-module imports; stale gate bytecode cannot decide readiness.
No authoring, cache regeneration, study stage, or network operation runs here.
"""
import hashlib
import importlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read_pin(pin):
    path = Path(pin["path"])
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise ValueError("MISSING-FILE: " + str(path)) from exc
    require(hashlib.sha256(raw).hexdigest() == pin["sha256"],
            "DIGEST-MISMATCH: " + str(path))
    return raw


def source_module(name, code):
    """Execute verified source, retaining ordinary module origin metadata."""
    rel = name.replace(".", "/") + ".py"
    path = ROOT / rel
    require(rel in code, "MISSING-CORE-ENTRY: " + str(path))
    raw = read_pin({"path": str(path), "sha256": code[rel]})
    parent, _, child = name.rpartition(".")
    package = importlib.import_module(parent)
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    setattr(package, child, module)
    exec(compile(raw, str(path), "exec", dont_inherit=True), module.__dict__)
    return module


def verify(core_path, expected_sha256):
    raw = read_pin({"path": str(core_path), "sha256": expected_sha256})
    core = json.loads(raw)
    # A stale A1 digest is already a decisive refusal; never print a saved
    # readiness value while waiting for the full consumer consistency gate.
    read_pin(core["a1_obligations_source"])
    code = core["code"]
    own_rel = "_optionA_dev/agreement_run/verify_core.py"
    require(own_rel in code, "MISSING-CORE-ENTRY: " + str(ROOT / own_rel))
    read_pin({"path": str(ROOT / own_rel), "sha256": code[own_rel]})
    # The helper is source-loaded after its digest check, never cache-loaded.
    bc = source_module("_optionA_dev.agreement_run.bytecode_correspondence", code)
    files = {}
    for row in core["files"]:
        path = str(Path(row["path"]).resolve())
        require(path not in files, "DUPLICATE-CORE-ENTRY: " + path)
        files[path] = row
    caches = bc.verify(ROOT, code, files, read_pin, require)
    source_module("_optionA_dev.agreement_run.runtime_binding", code)
    rp = source_module("_optionA_dev.agreement_run.run_path", code)
    computed = rp._core(core, return_evidence=True)
    # Recheck the exact manifest bytes after verification, too.
    read_pin({"path": str(core_path), "sha256": expected_sha256})
    return {"status": "PASS", "core_path": str(core_path),
            "core_sha256": expected_sha256, **computed,
            "verified_bytecode": caches,
            "a1_pin": core["a1_obligations_source"]}


def main():
    try:
        require(len(sys.argv) == 3, "VERIFY-USAGE: CORE_PATH EXPECTED_CORE_SHA256")
        sys.path.insert(0, str(ROOT))
        result = verify(Path(sys.argv[1]).resolve(), sys.argv[2])
    except Exception as exc:
        print(json.dumps({"status": "REFUSED", "reason": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
