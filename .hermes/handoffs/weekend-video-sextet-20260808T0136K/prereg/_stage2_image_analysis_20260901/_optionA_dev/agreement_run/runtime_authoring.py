"""Bounded authoring commands, with readiness always computed by the predicate.

refresh: measure runtime and refresh dependent pins, preserving obligation state.
resolve: require matching resolved A1 prose and verified evidence, then record the
         runtime obligation's evidence and the predicate's resulting readiness.
No run stages, network requests or protected data decoding occur here.
"""
import json
from pathlib import Path
import sys

from _optionA_dev.agreement_run import run_path as rp
from _optionA_dev.agreement_run.runtime_probe import measure, pin

BASE = rp.ROOT / "_optionA_dev/agreement_run"


def refresh():
    path = BASE / "RUNTIME_PINS_A1_CORE.json"
    runtime = json.loads(path.read_bytes())
    runtime["representation"] = measure()
    evidence = runtime["representation"]
    runtime["counts"]["representation_files"] = len(evidence["files"])
    runtime["counts"]["observed_module_names"] = len(evidence["modules"])
    runtime["counts"]["dyld_images"] = len(evidence["images"])
    runtime["counts"]["shared_cache_images"] = sum(r["binding"] == "DYLD-CACHE-IDENTITY" for r in evidence["images"])
    runtime["guarantees"] = [
        "All compact pins and individually recorded import/native artifact SHA-256 pins are verified at runtime; mismatches name the path.",
        "Loaded module paths, standard cache candidates and dyld image identities are matched against the observed register at pre-access and pre-record boundaries; unregistered entries refuse.",
        "Missing-file dyld images use " + rp.runtime_binding.CACHE_MECHANISM + ". This is identity binding, not per-image byte binding.",
        "Invocation, scientific env_lock and version checks remain enforced. Runtime obligation resolution also requires the registered evidence to pass these checks in input_readiness."
    ]
    runtime["limits"] = evidence["limits"]
    runtime["current_driver_compatibility"] = {"compatible": True, "driver_modified": True,
        "reason": "V49 retains compact pins and additionally requires A1-RUNTIME-REPRESENTATION-1; historical sweeps are not authorities."}
    path.write_bytes(rp.canonical(runtime))
    cpath = BASE / "INPUT_MANIFEST_A1_CORE.json"
    c = json.loads(cpath.read_bytes())
    # Re-pin only mutable authoring code/evidence and A1, never study inputs.
    for rel in rp.CODE:
        if rel.startswith("_optionA_dev/agreement_run/"):
            actual = pin(rp.ROOT / rel)
            c["code"][rel] = actual["sha256"]
            c["files"] = [p for p in c["files"] if Path(p["path"]).resolve() != Path(actual["path"])]
            c["files"].append({**actual, "status": "REAL", "kind": "our_source_code"})
    for name, actual in (("runtime", pin(path)), ("a1", pin(rp.ROOT / rp.A1_SOURCE))):
        c["files"] = [p for p in c["files"] if Path(p["path"]).resolve() != Path(actual["path"])]
        c["files"].append({**actual, "status": "REAL",
                           "kind": "runtime_register_reference" if name == "runtime" else "a1_obligation_source"})
        if name == "runtime":
            c["inputs"][name] = actual
        else:
            c["a1_obligations_source"] = actual
    for row in c["current_preparation_obligations"]:
        if row["id"] == "RUNTIME_REPRESENTATION" and "evidence_pin" in row:
            row["evidence_pin"] = c["inputs"]["runtime"]
    c["counts"]["real"] = len(c["files"])
    c["counts"]["our_source_code"] = len(c["code"])
    c["scope"]["runtime"] = "Runtime register includes mandatory per-artifact byte pins and dyld cache/image identity evidence, checked by the predicate and the environment consumer; see its precise limits."
    c["scope"]["own_bytecode"] = "CORE retains local cache SHA-256 and source-code equality checks. Runtime additionally pins observed source files and existing standard cache candidates of all imported packages; no installed-library tree sweep. TOCTOU and in-memory limits remain."
    record(cpath, c)
    print(json.dumps({"runtime_pin": pin(path), "counts": runtime["counts"],
                      "shared_cache": evidence["shared_cache"]}, sort_keys=True))


def record(path, c):
    computed = rp.input_readiness(c)
    c["ready_for_input_freeze"] = computed["ready_for_input_freeze"]
    c["readiness"]["checks"] = computed["checks"]
    c["readiness"]["reason"] = "; ".join(computed["reasons"])
    c["readiness"]["formula"] = " AND ".join(computed["checks"])
    c["readiness"]["source"] = "Rehashed CORE; declared registry; pinned A1; registered runtime evidence verified against this process and platform"
    c["counts"]["current_unresolved_preparation_obligations"] = sum(not p["resolved"] for p in c["current_preparation_obligations"])
    path.write_bytes(rp.canonical(c))
    print(json.dumps({"computed_readiness": computed, "core_pin": pin(path)}, sort_keys=True))


def resolve():
    path = BASE / "INPUT_MANIFEST_A1_CORE.json"
    c = json.loads(path.read_bytes())
    rp.require(rp._a1_obligations(c, rp._file_register(c["files"], "CORE"))["RUNTIME_REPRESENTATION"],
               "RUNTIME-A1-NOT-RESOLVED")
    verified = rp._environment(c["inputs"]["env_lock"], c["inputs"]["runtime"])
    row = next(r for r in c["current_preparation_obligations"] if r["id"] == "RUNTIME_REPRESENTATION")
    row["evidence_pin"] = c["inputs"]["runtime"]
    row["resolved"] = verified["runtime_representation"]["schema"] == rp.runtime_binding.SCHEMA
    row["evidence"] = "A1-RUNTIME-REPRESENTATION-1: individually rehashed import/native artifacts, checked module origins and dyld active-cache/per-image identities. input_readiness re-verifies this registered evidence; a boolean or prose claim alone cannot resolve the obligation."
    record(path, c)


if __name__ == "__main__":
    rp.require(sys.argv[1:] in (["refresh"], ["resolve"]), "AUTHORING-USAGE: refresh | resolve")
    (refresh if sys.argv[1] == "refresh" else resolve)()
