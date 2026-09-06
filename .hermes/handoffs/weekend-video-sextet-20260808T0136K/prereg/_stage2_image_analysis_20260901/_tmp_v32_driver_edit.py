# -*- coding: utf-8 -*-
def rp(s, old, new, n=1):
    assert s.count(old) >= 1, old[:90]; return s.replace(old, new, n)
p='fourier_chirality/run_configurations_v16.py'; s=open(p,encoding='utf-8').read()
s=rp(s,'"""run_configurations_v15 — V31 STAGED CANDIDATE (codex V30-1 FATAL / V30-2 / V30-3 / V30-4; Blanc 03:20 still governing): composed mode on provenance_designs_v11 —',
'"""run_configurations_v16 — V32 STAGED CANDIDATE (codex V31-1..5; BLANC 05:02: ONE PROPERTY, NSD — "No Stage Decides": no stage may decide or abort; every stage\n'
'contributes; one resolver decides — made checkable by the INDEPENDENCE / PREREQUISITES table at the end of this file, from which track 12\'s controls are derived):\n'
'composed mode on provenance_designs_v12 — `load_identity_composed` runs every stage on whatever inputs it truly needs: S0 sweeps both retained events WITHOUT git\n'
'(type / pinned repository / protected ref), S0d checks positive non-delivery only if git launches (else BLOCKED), S0b the list checks, S0c the local identity integrity\n'
'(schema, fields, digests, rule, beacon shape, witness fields, times), S1 the witness-bound conjunction as one classified stage whose refusal BLOCKS NOTHING that does not\n'
'need it — S2–S5 run on the locally readable context (the identity\'s own witness fields, the local repository, the retained records) when S1 refuses; S2 ONE retrieval\n'
'that keeps every obtained page (a later page\'s failure is a finding, the obtained events stay); S3 the approval event on the snapshot (both contradiction arms before\n'
'any availability disposition; a partial snapshot yields affirmative findings only) and the open event\'s same-id contradictions; S4 seed re-derivation with PRODUCTION\'s\n'
'own re-deriver on the retained records; S5 history_findings_v12 (no loop stops; open-event checks BLOCKED, not skipped, when no valid open event exists). Exceptions are\n'
'classified by PROVENANCE (retained input vs remote evidence); refusal codes by the explicit CLASS_ALLOWLIST; the helper import itself is the one raise outside the\n'
'collector and is named class 5. Stage states: attempted / completed / refused / blocked; every finding keeps its reason; the whole outcome is recorded in LAST_OUTCOME.\n'
'ACCEPT only when every REQUIRED stage completed, nothing was blocked and nothing was found. v15 was: V31 STAGED CANDIDATE (codex V30-1 FATAL / V30-2 / V30-3 / V30-4; Blanc 03:20 still governing): composed mode on provenance_designs_v11 —')
s=rp(s,'→ v15 (this; V31: the whole composed path as a staged finding collector, provenance_designs_v11).','→ v15 (V31: the whole composed path as a staged finding collector, provenance_designs_v11) → v16 (this; V32: NSD — independent stages, page-preserving snapshot, allowlist classification, provenance_designs_v12).')
s=rp(s,'v10→v6, v11→v7, v12→v8, v13→v9, v14→v10, v15→v11.]','v10→v6, v11→v7, v12→v8, v13→v9, v14→v10, v15→v11, v16→v12.]')
a=s.index('REQUIRED_STAGES = ("S0-local", "S0b-lists", "S1-conjunction", "S2-snapshot", "S3-events", "S4-seed", "S5-history")'); b=s.index('def verify_split_from_catalogue(I, proto):')
new='''REQUIRED_STAGES = ("S0-local", "S0d-delivery", "S0b-lists", "S0c-integrity", "S1-conjunction", "S2-snapshot", "S3-events", "S4-seed", "S5-history")
LAST_OUTCOME = None   # diagnostics of the last composed load: {"winner", "findings": [{class, code, why, stage, unclassified}], "stages": {name: {state, why}}, "blocked": {check: why}} — the exception message is the verdict; this is the whole outcome
def load_identity_composed(identity_path, proto):
    """UNADOPTED COMPOSED MODE, v16 — NSD ("No Stage Decides", Blanc 05:02): NO STAGE MAY DECIDE OR ABORT; EVERY STAGE CONTRIBUTES; ONE RESOLVER DECIDES. Each stage runs
    on the inputs it truly needs (INDEPENDENCE at the end of this file); a prerequisite failure is itself a finding, contributed by the stage that meets it, and the checks
    that needed it are recorded BLOCKED with the reason — never skipped, never permitting acceptance. Stage states: attempted → completed | refused (its body raised: the
    exception classified by PROVENANCE and contributed) | blocked (not attempted: an input it needs was not obtainable). ONE evidence snapshot (S2) serves S3 and S5;
    a partial snapshot keeps every obtained event and yields affirmative findings only. ACCEPT only when every REQUIRED stage completed, nothing is blocked and no finding
    exists; the winner otherwise is provenance_designs_v12.resolve over every finding. LAST_OUTCOME records the whole outcome."""
    global LAST_OUTCOME
    import subprocess, base64
    from datetime import datetime, timezone
    try: P = _P()
    except Exception as e: raise DataIntegrityFail(f"VERIFIER-UNAVAILABLE: the provenance helpers (provenance_designs_v12) cannot be imported ({e!r}) — class 5 by cause; the collector's own dependency, the one raise outside it")
    F = []; stages = {}; blocked = {}; ctx = {}
    def add(cls, code, why, stage, unclassified=False): f = P.finding(cls, code, why, stage, len(F)); f["unclassified"] = unclassified; F.append(f)
    def block(check, why): blocked[check] = why
    def stage(name, body, source="retained"):
        stages[name] = {"state": "attempted"}
        try: body(); stages[name]["state"] = "completed"
        except Exception as e: cls, code, why, unc = P.classify_exception(e, source=source); add(cls, code, why, name, unc); stages[name] = {"state": "refused", "why": f"{code}: {why}"[:200]}
    def mark_blocked(name, why): stages[name] = {"state": "blocked", "why": why}
    # ---- S0: the identity read locally; BOTH retained events swept without git; the open-event file's validity
    def S0():
        p = Path(identity_path)
        if not p.is_file(): raise DataIntegrityFail(f"IDENTITY-MISSING {identity_path}")
        I0 = json.loads(p.read_text())
        if not isinstance(I0, dict): raise DataIntegrityFail("IDENTITY-SCHEMA: the identity file does not hold an object")
        ctx["I0"] = I0; aw = I0.get("approval_witness") if isinstance(I0.get("approval_witness"), dict) else {}; ctx["ev0"] = aw.get("push_event"); ctx["commit0"] = str(aw.get("commit", ""))
        o, x = P.local_precheck_event(ctx["ev0"], proto.events_repo, proto.witness_branch_ref)
        if o is not None: add("LOCAL-TERMINAL", "EVENT-INCONSISTENT", x, "S0-local")
        try: raw = Path(proto.history_open_event_file).read_text()
        except Exception as e: ctx["open_event"] = None; add("LOCAL-TERMINAL", "HISTORY-OPEN-EVENT-MISSING", f"the retained history-open PushEvent file is absent or unreadable ({e!r})", "S0-local"); return
        try: oe = json.loads(raw)
        except Exception as e: ctx["open_event"] = None; add("LOCAL-TERMINAL", "HISTORY-OPEN-EVENT-INVALID", f"the retained history-open file is not JSON ({e!r})", "S0-local"); return
        if not isinstance(oe, dict) or oe.get("type") != "PushEvent" or not isinstance(oe.get("payload"), dict):
            ctx["open_event"] = None; add("LOCAL-TERMINAL", "HISTORY-OPEN-EVENT-INVALID", f"the retained history-open file does not hold a PushEvent object with an object payload (got {type(oe).__name__}: {str(oe)[:40]!r}) — null and every non-object value are refused; the open-event checks are recorded BLOCKED, not skipped (v15/v16, codex V30-1)", "S0-local"); return
        o2, x2 = P.local_precheck_event(oe, proto.events_repo, proto.witness_branch_ref)
        if o2 is not None: add("LOCAL-TERMINAL", "HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT", x2, "S0-local")
        ctx["open_event"] = oe
    stage("S0-local", S0)
    I0 = ctx.get("I0")
    # ---- S0d: positive non-delivery of the approval commit — needs git; blocked if git cannot launch
    def S0d():
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=Path(proto.seal_journal).parent, capture_output=True, text=True); ctx["root0"] = r.stdout.strip() if r.returncode == 0 else None
        if isinstance(ctx.get("ev0"), dict) and ctx.get("root0") and re.fullmatch(r"[0-9a-f]{40}", ctx.get("commit0", "")):
            if P.delivery(ctx["ev0"], ctx["commit0"], proto.witness_branch_ref, ctx["root0"]) == "NOT-DELIVERED": add("LOCAL-TERMINAL", "EVENT-INCONSISTENT", "IDENTITY-WITNESS-COMMIT: the push event positively does not deliver the approval commit (head, commits, or before..head ancestry established false)", "S0d-delivery")
    if I0 is not None: stage("S0d-delivery", S0d)
    else: mark_blocked("S0d-delivery", "the identity file could not be read")
    if stages["S0d-delivery"]["state"] == "refused": block("approval-delivery", "git could not be launched: " + stages["S0d-delivery"].get("why", ""))
    # ---- S0b / S0c: local list checks and local identity integrity — nothing remote, no witness
    if I0 is not None: stage("S0b-lists", lambda: _list_checks(I0, proto))
    else: mark_blocked("S0b-lists", "the identity file could not be read")
    def S0c():
        I = I0
        if I.get("schema_version") != "CORPUS-IDENTITY-2": raise DataIntegrityFail("IDENTITY-SCHEMA")
        for k in ("pool_sha256", "ordering_rule", "seed_hex", "split_mode", "renderability_inputs", "fresh_validation_objids", "exclude_file_sha256", "beacon_record_sha256", "rule_sha256"):
            if k not in I: raise DataIntegrityFail(f"IDENTITY-FIELD-MISSING {k}")
        if I["pool_sha256"] != proto.pool_sha256: raise DataIntegrityFail("IDENTITY-POOL-DIGEST: not the pinned guarded pool")
        if I["exclude_file_sha256"] != proto.exclusion_sha256: raise DataIntegrityFail("IDENTITY-EXCLUSION-DIGEST: not the pinned exclusion file")
        adopted = adopted_rule_sha256(); ctx["adopted"] = adopted
        if proto.rule_sha256 is not None and proto.rule_sha256 != adopted: raise DataIntegrityFail("ADOPTION-MISMATCH: protocol digest differs from the adopted file")
        if I["rule_sha256"] != adopted: raise DataIntegrityFail("IDENTITY-RULE-DIGEST: not the adopted approved rule")
        if proto.require_beacon and (not str(I["split_mode"]).startswith("beacon-seeded") or not re.fullmatch(r"[0-9a-f]{64}", str(I["beacon_record_sha256"] or ""))): raise DataIntegrityFail("IDENTITY-NOT-BEACON-SEEDED: production identities must be derived from an accepted beacon record")
        if I.get("beacon_outcome") != "ACCEPT-DRAND": raise DataIntegrityFail(f"IDENTITY-BEACON-NOT-ACCEPTED {I.get('beacon_outcome')}")
        if I.get("beacon_source") != "drand-mainnet-default": raise DataIntegrityFail("IDENTITY-SOURCE: not the pinned drand chain")
        w = I.get("approval_witness") or {}
        for k in ("commit", "record_path", "record_sha256", "push_event", "push_event_sha256", "events_provenance", "nonce_round", "nonce_randomness", "nonce_bodies_b64"):
            if k not in w: raise DataIntegrityFail(f"IDENTITY-WITNESS-MISSING: {k} absent")
        if not re.fullmatch(r"[0-9a-f]{40}", str(w["commit"])): raise DataIntegrityFail("IDENTITY-WITNESS-COMMIT: malformed")
        ev = w["push_event"]
        if hashlib.sha256(json.dumps(ev, sort_keys=True, separators=(",", ":")).encode()).hexdigest() != w["push_event_sha256"]: raise DataIntegrityFail("EVENT-DIGEST: the retained event's digest is not the witness's")
        try: created = datetime.fromisoformat(str((ev or {}).get("created_at")).replace("Z", "+00:00")).astimezone(timezone.utc)
        except Exception: raise DataIntegrityFail("IDENTITY-WITNESS-TIME: unparsable created_at")
        try: t_pulse = datetime.fromisoformat(str(I.get("T_pulse")).replace("Z", "+00:00")).astimezone(timezone.utc)
        except Exception: raise DataIntegrityFail("IDENTITY-T-PULSE: unparsable T_pulse")
        if created >= t_pulse: raise DataIntegrityFail("IDENTITY-WITNESS-LATE: the approval push time is not before T_pulse")
    if I0 is not None: stage("S0c-integrity", S0c)
    else: mark_blocked("S0c-integrity", "the identity file could not be read")
    # ---- S1: the witness-bound conjunction as ONE classified stage; its refusal blocks nothing that does not need it
    stage("S1-conjunction", lambda: ctx.update(_conjunction_prefix(identity_path, proto)))
    if "rp" in ctx: I, w_root, ev, commit, lp, rp, adopted, ap_bytes, rnd = (ctx[k] for k in ("I", "w_root", "ev", "commit", "lp", "rp", "adopted", "ap_bytes", "rnd")); degraded = False
    else:                                                                                               # the LOCALLY READABLE context (NSD: S2–S5 still run on what they truly need)
        I = I0 or {}; w_root = ctx.get("root0"); ev = ctx.get("ev0"); commit = ctx.get("commit0", ""); lp = Path(proto.collection_log); rp = Path(proto.beacon_record_path); adopted = ctx.get("adopted"); rnd = I.get("beacon_round"); degraded = True
        ap_bytes = None
        if w_root and re.fullmatch(r"[0-9a-f]{40}", commit or "") and isinstance(I.get("approval_witness"), dict):
            r = subprocess.run(["git", "cat-file", "-p", f"{commit}:{I['approval_witness'].get('record_path', '')}"], cwd=w_root, capture_output=True); ap_bytes = r.stdout if r.returncode == 0 else None
        if adopted is None:
            try: adopted = adopted_rule_sha256()
            except Exception: adopted = None
    runner = proto.events_runner or P.gh_runner; snap = {"live": None, "prov": None, "complete": False}
    # ---- S2: ONE evidence snapshot — every obtained page kept; a later page's failure is a finding, not a discard
    def S2():
        try: snap["live"], snap["prov"] = P.retrieve_events(proto.events_repo, runner)
        except P.EventsUnavailable as e: add("RETRY-UNAVAILABLE", "RETRY-EVENTS-UNAVAILABLE", f"{e.kind}: {e.why}", "S2-snapshot"); return
        part = (snap["prov"] or {}).get("partial"); snap["complete"] = part is None
        if part: add("RETRY-UNAVAILABLE", "RETRY-EVENTS-UNAVAILABLE", f"{part['kind']} on page {part['page']}: {part['why']} — a PARTIAL snapshot: the {len(snap['live'])} events obtained are kept and evaluated for affirmative findings; presence, absence, expiry and acceptance are not established from it", "S2-snapshot")
        for m in (snap["prov"] or {}).get("malformed", []): add("RETRY-UNAVAILABLE", "MALFORMED-REMOTE-EVIDENCE", f"an event in the retrieved feed is not a PushEvent-shaped object (page {m['page']}, id {m['id']!r}) — remote evidence unusable, excluded from the predicates", "S2-snapshot")
    stage("S2-snapshot", S2, source="remote")
    live, prov, complete = snap["live"], snap["prov"], snap["complete"]
    # ---- S3: the approval event on the snapshot; the open event's same-id contradictions on the same snapshot
    def S3():
        if live is None: raise _Blocked("approval-live", "the events feed could not be retrieved this invocation")
        if not isinstance(ev, dict) or not re.fullmatch(r"[0-9a-f]{40}", commit or ""): raise _Blocked("approval-live", "no retained approval event / commit to authenticate (the identity's witness block is missing or malformed — a class-0 finding already contributed)")
        o, why = P.authenticate_event(ev, live, proto.events_repo, proto.witness_branch_ref, commit, feed_reaches_back_to=(prov or {}).get("oldest_created_at"), root=w_root, complete=complete); ctx["ev_outcome"] = o
        if o == "AUTHENTIC": pass
        elif o == "UNAVAILABLE": add("RETRY-UNAVAILABLE", "RETRY-EVENTS-UNAVAILABLE", why, "S3-events")
        elif o == "INCOMPLETE": add("RETRY-INCOMPLETE", "RETRY-EVENTS-INCOMPLETE", why, "S3-events")
        elif o == "INCONSISTENT-INPUT": add("LOCAL-TERMINAL", "EVENT-INCONSISTENT", why, "S3-events")
        elif o == "NOT-EARLIEST": add("NOT-EARLIEST", "EVENT-NOT-EARLIEST", why, "S3-events")
        elif o == "EXPIRED":
            if not proto.events_receipt or proto.expected_receipt_origin is None: add("EXPIRED", "EVENT-EXPIRED-NO-RECEIPT-PATH", f"{why}; no independent receipt path is configured (Q1 Option C)", "S3-events")
            else:
                try: ok, rwhy = P.verify_events_receipt(proto.events_receipt, w_root, proto.witness_remote_url, proto.witness_branch_ref, ev, proto.expected_receipt_origin)
                except Exception as e: ok, rwhy = False, f"RECEIPT-MALFORMED: {type(e).__name__}: {str(e)[:120]}"
                if not ok: add("EXPIRED", "EVENT-EXPIRED-RECEIPT-REFUSED", rwhy + " (policy: an expired approval without an acceptable substitute is a loss, whatever the receipt's failure cause)", "S3-events")
        else: add("FORGED", "EVENT-FORGED", why, "S3-events")
        oe = ctx.get("open_event")
        if oe is None: block("open-same-id", "no valid history-open PushEvent object (class-0 finding contributed by S0)")
        elif live and P.same_id_contradictions(oe, live): add("FORGED", "HISTORY-CONTINUATION: OPEN-EVENT-FORGED", f"the live feed carries a push with the retained history-open event's id {oe.get('id')!r} whose canonical bytes DIFFER — an affirmative contradiction on the one snapshot (v16 S3)", "S3-events")
    class _Blocked(Exception):
        def __init__(self, check, why): super().__init__(why); self.check = check
    def run_or_block(name, body, source):
        stages[name] = {"state": "attempted"}
        try: body(); stages[name]["state"] = "completed"
        except _Blocked as e: block(e.check, str(e)); stages[name] = {"state": "blocked", "why": str(e)}
        except Exception as e: cls, code, why, unc = P.classify_exception(e, source=source); add(cls, code, why, name, unc); stages[name] = {"state": "refused", "why": f"{code}: {why}"[:200]}
    run_or_block("S3-events", S3, "remote")
    # ---- S4: seed re-derivation with PRODUCTION's own re-deriver, on the retained records
    def S4():
        if ap_bytes is None or adopted is None or rnd is None: raise _Blocked("seed", "the approval record bytes, the adopted digest or the beacon round are not obtainable locally" + (" (the conjunction refused)" if degraded else ""))
        seed, rv = proto.rederive_seed(rp, adopted, ap_bytes)
        if seed != I.get("seed_hex") or rv.get("round") != rnd: raise DataIntegrityFail("IDENTITY-SEED-NOT-REDERIVED: the seed does not follow from the retained beacon evidence")
    run_or_block("S4-seed", S4, "retained")
    # ---- S5: the history stage as a collector, on the same snapshot; open-event checks blocked (not skipped) without a valid open event
    def S5():
        if not w_root: raise _Blocked("history-remote", "no local repository root (git could not be launched or the seal journal is not in a repository)")
        HF, info = P.history_findings_v12(w_root, Path(lp).resolve().relative_to(Path(w_root).resolve()).as_posix(), proto.witness_remote_url, proto.witness_branch_ref, ctx.get("open_event"), live, prov, proto.events_repo); ctx["hinfo"] = info
        for cls, code, why in HF: add(cls, code, why, "S5-history")
        for k, v in (info.get("blocked") or {}).items(): block(k, v)
    run_or_block("S5-history", S5, "remote")
    if proto.verify_split: stage("S5b-split", lambda: verify_split_from_catalogue(I, proto))
    # ---- the resolver decides
    not_completed = [n for n in REQUIRED_STAGES if stages.get(n, {}).get("state") != "completed"]
    if not F and (blocked or not_completed): add("RETRY-UNAVAILABLE", "STAGE-BLOCKED", "checks blocked, nothing else found — never acceptance: " + "; ".join(f"{k}: {v}" for k, v in blocked.items()) + ("; stages not completed: " + ", ".join(not_completed) if not_completed else ""), "resolver")
    winner = P.resolve(F) if F else None
    LAST_OUTCOME = {"winner": (winner["code"] if winner else "ACCEPT"), "findings": [{k: f[k] for k in ("class", "code", "why", "stage", "unclassified")} for f in F], "stages": stages, "blocked": dict(blocked), "degraded_context": degraded}
    if isinstance(I, dict): I["_findings"] = LAST_OUTCOME["findings"]; I["_stages"] = stages; I["_blocked"] = dict(blocked)
    if winner: raise DataIntegrityFail(f"{winner['code']}: {winner['why']}")
    I["_composed"] = {"event": ctx.get("ev_outcome"), "events_provenance": prov, "history": (ctx.get("hinfo") or {}).get("why"), "remote_head": (ctx.get("hinfo") or {}).get("remote_head"), "precedence": list(P.PRECEDENCE), "stages": {k: v["state"] for k, v in stages.items()}}
    return I, ctx["d"]

'''
s=s[:a]+new+s[b:]
s=rp(s,'| "composed" (track-2 v11 helpers on this call path, ONE resolver, staged collector)','| "composed" (track-2 v12 helpers on this call path, NSD: independent contributing stages, ONE resolver)')
s=rp(s,'(production: provenance_designs_v11.gh_runner;','(production: provenance_designs_v12.gh_runner;')
s=rp(s,'    """the track-2 helpers (v11), imported lazily','    """the track-2 helpers (v12), imported lazily')
s=s.replace('import provenance_designs_v11 as P; return P','import provenance_designs_v12 as P; return P'); assert 'import provenance_designs_v12 as P; return P' in s
for bad in ('import provenance_designs_v11 as P','history_findings_v11('): assert bad not in s, bad
open(p,'w',encoding='utf-8').write(s); print("driver v16 edit script ready (not applied)")
