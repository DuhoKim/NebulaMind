"""Bounded authoring commands, with readiness always computed by the predicate.

refresh: measure runtime and refresh dependent pins; compute every obligation.
resolve: recompute every evidence predicate against existing pins.
Both commands cross-check A1 only after computing evidence, and refuse disagreement.
No run stages, network requests or protected data decoding occur here.
"""
import json
from pathlib import Path
import sys

from _optionA_dev.agreement_run import run_path as rp
from _optionA_dev.agreement_run.runtime_probe import measure, pin

BASE = rp.ROOT / "_optionA_dev/agreement_run"


def refresh():
    cpath = BASE / "INPUT_MANIFEST_A1_CORE.json"
    c = json.loads(cpath.read_bytes())
    # Check correspondence BEFORE measuring/importing dependencies or writing
    # either register. Registration alone cannot bless a stale program.
    bytecode_rows = []
    for rel in sorted(set(rp.CODE) | set(c["code"])):
        source = (rp.ROOT / rel).resolve()
        raw = source.read_bytes()
        for cache in rp.bytecode_correspondence.candidates(source):
            rp.bytecode_correspondence.corresponds(source, raw, cache, rp.require)
            bytecode_rows.append({**pin(cache), "status": "REAL",
                                  "kind": "our_imported_bytecode", "source": rel})
    path = BASE / "RUNTIME_PINS_A1_CORE.json"
    runtime = json.loads(path.read_bytes())
    runtime["representation"] = measure()
    evidence = runtime["representation"]
    runtime["counts"]["representation_files"] = len(evidence["files"])
    runtime["counts"]["observed_module_names"] = len(evidence["modules"])
    runtime["counts"]["dyld_images"] = len(evidence["images"])
    runtime["counts"]["shared_cache_images"] = sum(r["binding"] == "DYLD-CACHE-FILE-SHA256" for r in evidence["images"])
    runtime["counts"]["shared_cache_files"] = len(evidence["cache_bytes"]["files"])
    runtime["counts"]["shared_cache_bytes"] = sum(p["bytes"] for p in evidence["cache_bytes"]["files"])
    runtime["guarantees"] = [
        "All compact pins and individually recorded import/native artifact SHA-256 pins are verified at runtime; mismatches name the path.",
        "Loaded module paths, standard cache candidates and dyld image identities are matched against the observed register at pre-access and pre-record boundaries; unregistered entries refuse.",
        "Cache-resident images bind to SHA-256 of the main active cache and every UUID-linked subcache file, in full. Every check rehashes their bytes; UUID/build identity checks are retained.",
        "Invocation, scientific env_lock and version checks remain enforced. Runtime obligation resolution also requires the registered evidence to pass these checks in input_readiness."
    ]
    runtime["limits"] = evidence["limits"]
    runtime["current_driver_compatibility"] = {"compatible": True, "driver_modified": True,
        "reason": "V50 retains compact pins and additionally requires A1-RUNTIME-REPRESENTATION-2; historical sweeps are not authorities."}
    path.write_bytes(rp.canonical(runtime))
    # Re-pin only mutable authoring code/evidence and A1, never study inputs.
    for rel in rp.CODE:
        if rel.startswith("_optionA_dev/agreement_run/"):
            actual = pin(rp.ROOT / rel)
            c["code"][rel] = actual["sha256"]
            c["files"] = [p for p in c["files"] if Path(p["path"]).resolve() != Path(actual["path"])]
            c["files"].append({**actual, "status": "REAL", "kind": "our_source_code"})
    for actual in bytecode_rows:
        c["files"] = [p for p in c["files"] if Path(p["path"]).resolve() != Path(actual["path"])]
        c["files"].append(actual)
    for name, actual in (("runtime", pin(path)), ("a1", pin(rp.ROOT / rp.A1_SOURCE))):
        c["files"] = [p for p in c["files"] if Path(p["path"]).resolve() != Path(actual["path"])]
        c["files"].append({**actual, "status": "REAL",
                           "kind": "runtime_register_reference" if name == "runtime" else "a1_obligation_source"})
        if name == "runtime":
            c["inputs"][name] = actual
        else:
            c["a1_obligations_source"] = actual
    for row in c["current_preparation_obligations"]:
        if row["id"] == "RUNTIME_REPRESENTATION":
            row["evidence_pin"] = c["inputs"]["runtime"]
    c["counts"]["real"] = len(c["files"])
    c["counts"]["our_source_code"] = len(c["code"])
    c["counts"]["our_imported_bytecode"] = sum(p.get("kind") == "our_imported_bytecode" for p in c["files"])
    c["scope"]["runtime"] = "Runtime register includes mandatory per-artifact byte pins and full dyld cache-family file-byte evidence, checked by the predicate and the environment consumer; see its precise limits."
    c["scope"]["own_bytecode"] = "CORE requires SHA-256 registration and code-object equality to compilation of current pinned source for every own-module cache in __pycache__, the macOS com.apple.python cache, the active interpreter cache prefix, legacy adjacent bytecode and reported loaded cache paths. Existing optimization variants are checked at their respective optimization levels. Missing rows, relabeled rows and non-corresponding programs refuse by module and path; no location is exempted. TOCTOU and in-memory limits remain."
    record(cpath, c)
    print(json.dumps({"runtime_pin": pin(path), "counts": runtime["counts"],
                      "shared_cache": evidence["shared_cache"]}, sort_keys=True))


def record(path, c):
    computed = rp.input_readiness(c)
    for row in c["current_preparation_obligations"]:
        row["resolved"] = computed["obligation_evidence"][row["id"]]
        row["required_work"] = rp.OBLIGATION_REGISTRY[row["id"]]
        row["evidence"] = "Evaluated by run_path.EVIDENCE_PREDICATES[" + row["id"] + "]; declarations do not resolve this obligation."
    rp._a1_consistency(c, computed)
    c["ready_for_input_freeze"] = computed["ready_for_input_freeze"]
    c["readiness"]["checks"] = computed["checks"]
    c["readiness"]["reason"] = "; ".join(computed["reasons"])
    c["readiness"]["formula"] = " AND ".join(computed["checks"])
    c["readiness"]["source"] = "Evidence predicates over CORE, retained MEDIUM producer bytes, and freshly verified runtime/cache-file bytes; A1 is a separate refusal-only consistency gate"
    c["counts"]["current_unresolved_preparation_obligations"] = sum(not p["resolved"] for p in c["current_preparation_obligations"])
    path.write_bytes(rp.canonical(c))
    print(json.dumps({"computed_readiness": computed, "core_pin": pin(path)}, sort_keys=True))


def resolve():
    path = BASE / "INPUT_MANIFEST_A1_CORE.json"
    c = json.loads(path.read_bytes())
    record(path, c)


if __name__ == "__main__":
    rp.require(sys.argv[1:] in (["refresh"], ["resolve"]), "AUTHORING-USAGE: refresh | resolve")
    (refresh if sys.argv[1] == "refresh" else resolve)()
