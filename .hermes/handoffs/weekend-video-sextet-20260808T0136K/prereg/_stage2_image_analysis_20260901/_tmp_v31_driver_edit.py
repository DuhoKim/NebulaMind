# -*- coding: utf-8 -*-
def rp(s, old, new, n=1):
    assert s.count(old) >= 1, old[:90]; return s.replace(old, new, n)
p='fourier_chirality/run_configurations_v15.py'; s=open(p,encoding='utf-8').read()
s=rp(s,'"""run_configurations_v14 — V30 STAGED CANDIDATE (codex V29-1/2/3/4; Blanc 03:20: precedence is ONE pattern): composed mode on provenance_designs_v10 —',
'"""run_configurations_v15 — V31 STAGED CANDIDATE (codex V30-1 FATAL / V30-2 / V30-3 / V30-4; Blanc 03:20 still governing): composed mode on provenance_designs_v11 —\n'
'THE COMPOSED PATH IS A STAGED FINDING COLLECTOR (`load_identity_composed`): S0 the identity file read locally and BOTH retained events swept (approval: type / pinned\n'
'repository / positive non-delivery; history-open: the file must hold a PushEvent OBJECT — null, a list, a scalar or any other value is HISTORY-OPEN-EVENT-INVALID, class 0,\n'
'and nothing is skipped; type / pinned repository / protected ref); S0b the list shape / disjointness checks (class 0, now BEFORE anything remote); S1 the witness-bound\n'
'offline conjunction (`_conjunction_prefix`) as ONE classified stage — WITNESS-FETCH-FAILED / VERIFIER-UNAVAILABLE become RETRY-UNAVAILABLE findings after the local sweep,\n'
'every other refusal is classified by provenance_designs_v11.classify_refusal, every exception by classify_exception; S2 ONE evidence snapshot (one retrieval per\n'
'invocation); S3 the approval event authenticated on the snapshot and the open event\'s same-id contradictions on the same snapshot; S4 seed re-derivation with PRODUCTION\'s\n'
'own re-deriver; S5 the history stage as a collector (history_findings_v11) on the same snapshot. ACCEPT only when every required stage RAN and contributed nothing;\n'
'a stage that could not run (its inputs failed) is recorded as NOT RUN and can never be skipped into acceptance. Every finding is recorded in I["_findings"]; the\n'
'winner is resolved by provenance_designs_v11.resolve. Offline mode is unchanged in behaviour: `_conjunction_prefix` + seed re-derivation + verify_split + list checks.\n'
'v14 was: V30 STAGED CANDIDATE (codex V29-1/2/3/4; Blanc 03:20: precedence is ONE pattern): composed mode on provenance_designs_v10 —')
s=rp(s,'→ v14 (this; V30: ONE resolver over four contributing stages, provenance_designs_v10).','→ v14 (V30: ONE resolver over four contributing stages, provenance_designs_v10) → v15 (this; V31: the whole composed path as a staged finding collector, provenance_designs_v11).')
s=rp(s,'v10→v6, v11→v7, v12→v8, v13→v9, v14→v10.]','v10→v6, v11→v7, v12→v8, v13→v9, v14→v10, v15→v11.]')
s=rp(s,'def load_identity(identity_path, proto):\n    """Corpus identity: ordered objid lists frozen BEFORE development; its digest must be sealed in the journal."""',
'def _conjunction_prefix(identity_path, proto):\n    """The witness-bound OFFLINE CONJUNCTION (every check of the V15 driver and its successors up to the beacon record), unchanged in content since v14: returns the\n    context the seed re-derivation and the composed stages need. Extracted in v15 so the composed path can run it as ONE classified stage (a refusal here is a finding,\n    classified by provenance_designs_v11.classify_refusal) instead of a decision. Offline load_identity calls it directly."""')
old_tail='''        if proto.provenance_mode == "composed": composed_resolver(I, proto, w_root, ev, commit, lp, rp, adopted, ap_bytes, rnd)   # v14 (Blanc 03:20): ONE resolver — seed re-derivation is stage C of it, contributing, not deciding
        else:
            seed, rv = proto.rederive_seed(rp, adopted, ap_bytes)
            if seed != I["seed_hex"] or rv.get("round") != rnd: raise DataIntegrityFail("IDENTITY-SEED-NOT-REDERIVED: the seed does not follow from the retained beacon evidence")
        if proto.verify_split: verify_split_from_catalogue(I, proto)                                  # v6, UNADOPTED: off by default
'''
assert old_tail in s
s=s.replace(old_tail,'''        return {"I": I, "d": d, "w_root": w_root, "ev": ev, "commit": commit, "lp": lp, "rp": rp, "adopted": adopted, "ap_bytes": ap_bytes, "rnd": rnd}
''')
old_lists='''    for k, n in (("tuning_objids", proto.n_tune), ("holdout_objids", proto.n_hold), ("fresh_validation_objids", proto.n_fresh)):
        if len(I.get(k, [])) != n or len(set(I[k])) != n or not all(isinstance(x, int) for x in I[k]): raise DataIntegrityFail(f"IDENTITY-{k}-SIZE-OR-TYPE")
    a, b, c = set(I["tuning_objids"]), set(I["holdout_objids"]), set(I["fresh_validation_objids"])
    if (a & b) or (a & c) or (b & c): raise DataIntegrityFail("IDENTITY-OVERLAP")
    return I, d
'''
assert old_lists in s
s=s.replace(old_lists,'''    return {"I": I, "d": d}

def _list_checks(I, proto):
    """The local list shape / type / disjointness checks (class 0). Offline: after the conjunction, as before. Composed: stage S0b, BEFORE anything remote (codex V30-2)."""
    for k, n in (("tuning_objids", proto.n_tune), ("holdout_objids", proto.n_hold), ("fresh_validation_objids", proto.n_fresh)):
        if len(I.get(k, [])) != n or len(set(I[k])) != n or not all(isinstance(x, int) for x in I[k]): raise DataIntegrityFail(f"IDENTITY-{k}-SIZE-OR-TYPE")
    a, b, c = set(I["tuning_objids"]), set(I["holdout_objids"]), set(I["fresh_validation_objids"])
    if (a & b) or (a & c) or (b & c): raise DataIntegrityFail("IDENTITY-OVERLAP")

def load_identity(identity_path, proto):
    """Corpus identity: ordered objid lists frozen BEFORE development; its digest must be sealed in the journal. Offline (PRODUCTION default): the conjunction, the seed
    re-derived by PRODUCTION's own re-deriver, verify_split (UNADOPTED, off), the list checks. Composed (UNADOPTED): `load_identity_composed`."""
    if proto.provenance_mode == "composed": return load_identity_composed(identity_path, proto)
    c = _conjunction_prefix(identity_path, proto); I = c["I"]
    if "rp" in c:
        seed, rv = proto.rederive_seed(c["rp"], c["adopted"], c["ap_bytes"])
        if seed != I["seed_hex"] or rv.get("round") != c["rnd"]: raise DataIntegrityFail("IDENTITY-SEED-NOT-REDERIVED: the seed does not follow from the retained beacon evidence")
        if proto.verify_split: verify_split_from_catalogue(I, proto)                                  # v6, UNADOPTED: off by default
    _list_checks(I, proto)
    return I, c["d"]

REQUIRED_STAGES = ("S0-local", "S0b-lists", "S1-conjunction", "S2-snapshot", "S3-events", "S4-seed", "S5-history")
def load_identity_composed(identity_path, proto):
    """UNADOPTED COMPOSED MODE, v15 — the whole path as a STAGED FINDING COLLECTOR under the one precedence order (Blanc 03:20; codex V30-1/2/3). Stages, in a fixed
    sequence; each CONTRIBUTES findings (a refusal raised inside a stage is classified, never decides); a stage whose inputs failed is NOT RUN; acceptance requires every
    stage in REQUIRED_STAGES to have run and contributed nothing — no stage can be skipped into acceptance (codex V30-1). ONE evidence snapshot per invocation (S2) serves
    S3 and S5. The winner is provenance_designs_v11.resolve over every finding; I["_findings"] records them all."""
    import subprocess
    P = _P(); F = []; ran = set(); ctx = {}
    def add(cls, code, why, stage, unclassified=False): f = P.finding(cls, code, why, stage, len(F)); f["unclassified"] = unclassified; F.append(f)
    def stage(name, body):
        try: body(); ran.add(name)
        except Exception as e: cls, code, why, unc = P.classify_exception(e); add(cls, code, why, name, unc); ran.add(name)
    # ---- S0: the identity file read LOCALLY, both retained events swept, the open-event file's validity (nothing remote, no witness)
    def S0():
        p = Path(identity_path)
        if not p.is_file(): raise DataIntegrityFail(f"IDENTITY-MISSING {identity_path}")
        I0 = json.loads(p.read_text())
        if not isinstance(I0, dict): raise DataIntegrityFail("IDENTITY-SCHEMA: the identity file does not hold an object")
        ctx["I0"] = I0; aw = I0.get("approval_witness") if isinstance(I0.get("approval_witness"), dict) else {}
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=Path(proto.seal_journal).parent, capture_output=True, text=True); ctx["root0"] = r.stdout.strip() if r.returncode == 0 else None
        o, x = P.local_precheck(aw.get("push_event"), proto.events_repo, proto.witness_branch_ref, str(aw.get("commit", "")), ctx["root0"])
        if o is not None: add("LOCAL-TERMINAL", "EVENT-INCONSISTENT", x, "S0-local")
        try: raw = Path(proto.history_open_event_file).read_text()
        except Exception as e: ctx["open_event"] = None; add("LOCAL-TERMINAL", "HISTORY-OPEN-EVENT-MISSING", f"the retained history-open PushEvent file is absent or unreadable ({e!r})", "S0-local"); return
        try: oe = json.loads(raw)
        except Exception as e: ctx["open_event"] = None; add("LOCAL-TERMINAL", "HISTORY-OPEN-EVENT-INVALID", f"the retained history-open file is not JSON ({e!r})", "S0-local"); return
        if not isinstance(oe, dict) or oe.get("type") != "PushEvent":
            ctx["open_event"] = None; add("LOCAL-TERMINAL", "HISTORY-OPEN-EVENT-INVALID", f"the retained history-open file does not hold a PushEvent object (got {type(oe).__name__}: {str(oe)[:40]!r}) — null and every non-object value are refused and nothing downstream is skipped (v15, codex V30-1)", "S0-local"); return
        o2, x2 = P.local_precheck_event(oe, proto.events_repo, proto.witness_branch_ref)
        if o2 is not None: add("LOCAL-TERMINAL", "HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT", x2, "S0-local")
        ctx["open_event"] = oe
    stage("S0-local", S0)
    if "I0" in ctx: stage("S0b-lists", lambda: _list_checks(ctx["I0"], proto))
    # ---- S1: the witness-bound conjunction as ONE classified stage
    stage("S1-conjunction", lambda: ctx.update(_conjunction_prefix(identity_path, proto)))
    have = "rp" in ctx
    if have:
        I, w_root, ev, commit, lp, rp, adopted, ap_bytes, rnd = (ctx[k] for k in ("I", "w_root", "ev", "commit", "lp", "rp", "adopted", "ap_bytes", "rnd"))
        runner = proto.events_runner or P.gh_runner; snap = {"live": None, "prov": None}
        # ---- S2: ONE evidence snapshot
        def S2():
            try: snap["live"], snap["prov"] = P.retrieve_events(proto.events_repo, runner)
            except P.EventsUnavailable as e: add("RETRY-UNAVAILABLE", "RETRY-EVENTS-UNAVAILABLE", f"{e.kind}: {e.why}", "S2-snapshot")
        stage("S2-snapshot", S2)
        # ---- S3: the approval event on the snapshot; the open event's same-id contradictions on the same snapshot
        def S3():
            live, prov = snap["live"], snap["prov"]
            o, why = P.authenticate_event(ev, live, proto.events_repo, proto.witness_branch_ref, commit, feed_reaches_back_to=(prov or {}).get("oldest_created_at"), root=w_root); ctx["ev_outcome"] = o
            if o == "AUTHENTIC": pass
            elif o == "UNAVAILABLE": add("RETRY-UNAVAILABLE", "RETRY-EVENTS-UNAVAILABLE", why, "S3-events")
            elif o == "INCOMPLETE": add("RETRY-INCOMPLETE", "RETRY-EVENTS-INCOMPLETE", why, "S3-events")
            elif o == "INCONSISTENT-INPUT": add("LOCAL-TERMINAL", "EVENT-INCONSISTENT", why, "S3-events")
            elif o == "NOT-EARLIEST": add("NOT-EARLIEST", "EVENT-NOT-EARLIEST", why, "S3-events")
            elif o == "EXPIRED":
                if not proto.events_receipt or proto.expected_receipt_origin is None: add("EXPIRED", "EVENT-EXPIRED-NO-RECEIPT-PATH", f"{why}; no independent receipt path is configured (Q1 Option C)", "S3-events")
                else:
                    ok, rwhy = P.verify_events_receipt(proto.events_receipt, w_root, proto.witness_remote_url, proto.witness_branch_ref, ev, proto.expected_receipt_origin)
                    if not ok: add("EXPIRED", "EVENT-EXPIRED-RECEIPT-REFUSED", rwhy + " (policy: an expired approval without an acceptable substitute is a loss, whatever the receipt's failure cause)", "S3-events")
            else: add("FORGED", "EVENT-FORGED", why, "S3-events")
            oe = ctx.get("open_event")
            if oe is not None and live and P.same_id_contradictions(oe, live): add("FORGED", "HISTORY-CONTINUATION: OPEN-EVENT-FORGED", f"the live feed carries a push with the retained history-open event's id {oe.get('id')!r} whose canonical bytes DIFFER — an affirmative contradiction on the one snapshot (v15 S3)", "S3-events")
        stage("S3-events", S3)
        # ---- S4: seed re-derivation with PRODUCTION's own re-deriver
        def S4():
            seed, rv = proto.rederive_seed(rp, adopted, ap_bytes)
            if seed != I["seed_hex"] or rv.get("round") != rnd: raise DataIntegrityFail("IDENTITY-SEED-NOT-REDERIVED: the seed does not follow from the retained beacon evidence")
        stage("S4-seed", S4)
        # ---- S5: the history stage as a collector, on the same snapshot
        def S5():
            oe = ctx.get("open_event")
            if oe is None: raise DataIntegrityFail("HISTORY-OPEN-EVENT-INVALID: no valid history-open PushEvent — the history stage cannot run and is not skipped (v15, codex V30-1)")
            HF, info = P.history_findings_v11(w_root, Path(lp).resolve().relative_to(Path(w_root).resolve()).as_posix(), proto.witness_remote_url, proto.witness_branch_ref, oe, snap["live"], snap["prov"], proto.events_repo); ctx["hinfo"] = info
            for cls, code, why in HF: add(cls, code, why, "S5-history")
        stage("S5-history", S5)
        if proto.verify_split: stage("S5b-split", lambda: verify_split_from_catalogue(I, proto))
    I_any = ctx.get("I") or ctx.get("I0") or {}
    not_run = [n for n in REQUIRED_STAGES if n not in ran]
    if not F and not_run: add("LOCAL-TERMINAL", "STAGE-NOT-RUN", f"required stages did not run: {not_run} — nothing is skipped into acceptance", "resolver")
    if isinstance(I_any, dict): I_any["_findings"] = [{k: f[k] for k in ("class", "code", "stage", "unclassified")} for f in F]; I_any["_stages_run"] = sorted(ran)
    if F: w = P.resolve(F); raise DataIntegrityFail(f"{w['code']}: {w['why']}")
    I = ctx["I"]; I["_composed"] = {"event": ctx.get("ev_outcome"), "events_provenance": snap["prov"], "history": (ctx.get("hinfo") or {}).get("why"), "remote_head": (ctx.get("hinfo") or {}).get("remote_head"), "precedence": list(P.PRECEDENCE), "stages": list(REQUIRED_STAGES)}
    return I, ctx["d"]
''')
a=s.index('def composed_resolver(I, proto, w_root, ev, commit, log_path, rp, adopted, ap_bytes, rnd):'); b=s.index('def verify_split_from_catalogue(I, proto):'); s=s[:a]+s[b:]
s=rp(s,'| "composed" (track-2 v10 helpers on this call path, ONE resolver)','| "composed" (track-2 v11 helpers on this call path, ONE resolver, staged collector)')
s=rp(s,'(production: provenance_designs_v10.gh_runner;','(production: provenance_designs_v11.gh_runner;')
s=rp(s,'    """the track-2 helpers (v10), imported lazily','    """the track-2 helpers (v11), imported lazily')
s=s.replace('import provenance_designs_v10 as P; return P','import provenance_designs_v11 as P; return P'); assert 'import provenance_designs_v11 as P; return P' in s
for bad in ('composed_resolver(','import provenance_designs_v10 as P'): assert bad not in s, bad
open(p,'w',encoding='utf-8').write(s); print("driver v15 written")
