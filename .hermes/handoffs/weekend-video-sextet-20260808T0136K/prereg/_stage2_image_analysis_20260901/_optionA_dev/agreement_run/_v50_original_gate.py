def input_readiness(c):
    """Rehash every CORE row; compute completeness, resolution and A1 agreement.

    Returns FALSE and named reasons for incomplete/unresolved obligations.
    Malformed schemas, invalid pins and unfamiliar A1 prose revisions refuse.
    Recorded flags/checks/counts are never operands of the computed predicate.
    """
    require(c.get("schema") == "A1-INPUT-CORE-DRAFT-1", "INPUT-SCHEMA")
    files = _file_register(c.get("files"), "CORE")
    code, inputs = c.get("code", {}), c.get("inputs", {})
    require(isinstance(code, dict) and isinstance(inputs, dict), "CORE-ALIASES-SCHEMA")
    for rel in CODE:
        require(rel in code, "MISSING-CORE-ENTRY: " + str(ROOT / rel))
    for rel, digest in code.items():
        source = ROOT / rel
        _registered_pin(files, {"path": str(source), "sha256": digest})
        # -B suppresses cache WRITES only. Any existing standard cache for our
        # code must itself be pinned; no package/cache tree is swept.
        cache = Path(importlib.util.cache_from_source(str(source.resolve())))
        if cache.is_file():
            require(str(cache.resolve()) in files, "MISSING-CORE-ENTRY: " + str(cache))
    for name in INPUTS:
        require(name in inputs, "MISSING-CORE-INPUT: " + name)
    for pin in inputs.values():
        _registered_pin(files, pin)
    require(Path(inputs["render_config"]["path"]).resolve() ==
            (ROOT / "miniprereg_pins/render_config_v2.json").resolve(),
            "CONFIG-PATH-MISMATCH: " + inputs["render_config"]["path"])
    for entry in files.values():
        require(entry.get("status") == "REAL", "CORE-ENTRY-STATUS: " + entry["path"])
        if entry.get("kind") == "our_imported_bytecode":
            source = entry.get("source")
            require(source in code, "CACHE-SOURCE-MISSING: " + entry["path"])
            raw = read_pin(entry)
            source_path = (ROOT / source).resolve()
            source_raw = read_pin({"path": str(source_path), "sha256": code[source]})
            try:
                equal = (raw[:4] == importlib.util.MAGIC_NUMBER and
                         marshal.loads(raw[16:]) == compile(source_raw, str(source_path),
                             "exec", dont_inherit=True, optimize=sys.flags.optimize))
            except (ValueError, EOFError, TypeError):
                equal = False
            require(equal, "CACHE-SOURCE-MISMATCH: " + entry["path"])
    placeholders = c.get("placeholders")
    obligations = c.get("current_preparation_obligations")
    require(isinstance(placeholders, list) and isinstance(obligations, list),
            "CORE-READINESS-SCHEMA")
    require(all(isinstance(p, dict) for p in placeholders), "CORE-READINESS-SCHEMA")
    by_id, duplicates = {}, []
    for p in obligations:
        require(isinstance(p, dict) and isinstance(p.get("id"), str) and p["id"] and
                type(p.get("resolved")) is bool, "CORE-OBLIGATION-SCHEMA")
        if p["id"] in by_id:
            duplicates.append(p["id"])
        by_id[p["id"]] = p
    missing = sorted(set(OBLIGATION_REGISTRY) - set(by_id))
    undeclared = sorted(set(by_id) - set(OBLIGATION_REGISTRY))
    a1 = _a1_obligations(c, files)
    disagreements = sorted(oid for oid, row in by_id.items()
                           if oid in a1 and row["resolved"] is not a1[oid])
    reasons = ["INPUT placeholder: " + str(p.get("name", p.get("path")))
               for p in placeholders if p.get("due_stage") == "INPUT" or
               p.get("blocks_input_freeze") is not False]
    reasons += [str(p.get("id")) + ": " + str(p.get("evidence", "unresolved"))
                for p in obligations if p.get("resolved") is not True]
    reasons += ["MISSING-OBLIGATION: " + oid for oid in missing]
    reasons += ["DUPLICATE-OBLIGATION: " + oid for oid in sorted(set(duplicates))]
    reasons += ["UNDECLARED-OBLIGATION: " + oid for oid in undeclared]
    reasons += ["A1-OBLIGATION-MISMATCH: " + oid + "; A1 resolved=" + str(a1[oid]) +
                ", manifest resolved=" + str(by_id[oid]["resolved"]) for oid in disagreements]
    # A declaration and matching A1 prose cannot discharge runtime work alone.
    # Re-read the registered evidence and measure this process/platform now.
    runtime_evidenced = False
    runtime_row = by_id.get("RUNTIME_REPRESENTATION", {})
    if runtime_row.get("resolved") is True:
        evidence_pin = runtime_row.get("evidence_pin")
        if not _same_pin(evidence_pin, inputs["runtime"]):
            reasons.append("MISSING-RUNTIME-EVIDENCE: RUNTIME_REPRESENTATION")
        else:
            _registered_pin(files, evidence_pin)
            _environment(inputs["env_lock"], evidence_pin)
            runtime_evidenced = True
    checks = {"all_real_entries_rehashed_and_matched": True,
              "input_due_placeholders_resolved": not any(
                  p.get("due_stage") == "INPUT" or p.get("blocks_input_freeze") is not False
                  for p in placeholders),
              "declared_obligation_set_complete": not (missing or undeclared or duplicates),
              "current_preparation_obligations_resolved": all(
                  p.get("resolved") is True for p in obligations),
              "runtime_representation_evidenced": runtime_evidenced,
              "a1_manifest_obligations_agree": not (missing or undeclared or duplicates or disagreements)}
    return {"ready_for_input_freeze": all(checks.values()), "checks": checks,
            "reasons": reasons, "a1_obligations": a1,
            "declared_obligation_ids": list(OBLIGATION_REGISTRY)}


def _core(c):
    """Enforce computed readiness and the recorded flag/checks; no stage access here."""
    computed = input_readiness(c)
    readiness = c.get("readiness", {})
    reason = "; ".join(computed["reasons"]) or str(
        readiness.get("reason", "CORE readiness flag is false or missing"))
    require(c.get("ready_for_input_freeze") is True and computed["ready_for_input_freeze"],
            "CORE-NOT-READY: " + reason)
    require(readiness.get("checks") == computed["checks"], "CORE-READINESS-CHECKS-MISMATCH")
    return c["inputs"]

