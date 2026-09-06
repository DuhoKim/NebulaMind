# -*- coding: utf-8 -*-
def rp(s, old, new, n=1):
    assert s.count(old) >= 1, old[:90]; return s.replace(old, new, n)
CLAUSE1 = ("On both the approval and history-open paths, locally decidable retained-event mismatches are terminal before any evidence-unavailability return. In composed mode, unresolved delivery does not bypass live authentication: a same-ID canonical contradiction obtained from the live feed is terminal before an undetermined-delivery retry. Only when no higher-priority inconsistency is established may undetermined delivery or unavailable retrieval return the stage's retry disposition. Offline mode retains its explicitly named undetermined-delivery refusal.")
CLAUSE2 = ("Same-commit contradiction is scoped to the pinned protected ref and evaluated only when the retained event is absent. If it is present verbatim, distinct qualifying events are resolved by earliest-event ordering; a later event does not invalidate an authentic earliest event. Conflicting same-ID evidence is refused even beside a verbatim copy, without asserting that this alone identifies which producer supplied false evidence.")
# ---------------- provenance_designs_v9
p='track2/provenance_designs_v9.py'; s=open(p,encoding='utf-8').read()
s=rp(s,'"""TRACK 2 v8 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V27 review (V27-1, V27-2, V27-3)',
'"""TRACK 2 v9 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V28 review (V28-1, V28-2, V28-3) — two UNREPAIRED CONTRADICTIONS the lane\'s own V27-2 repair had\n'
'introduced (a tri-state precheck that returned a retry before the precedence rules could run), now repaired on the complete paths; codex\'s clause text carried verbatim:\n'
'(1) "' + CLAUSE1 + '"\n'
'(2) "' + CLAUSE2 + '"\n'
'IMPLEMENTATION: `validate_continuation_v9` — when the retained history-open event\'s delivery of the open commit is UNDETERMINED, the stage CONSULTS THE FEED through\n'
'`authenticate_event_live` (local_precheck first, then retrieval, then same-id contradictions) and returns OPEN-EVENT-INCONSISTENT-INPUT / OPEN-EVENT-FORGED /\n'
'OPEN-EVENT-NOT-EARLIEST (terminal) or EVIDENCE-EXPIRED (loss) before it may return EVIDENCE-UNAVAILABLE / EVIDENCE-INCOMPLETE (retry); run_configurations_v13\'s\n'
'witness-commit precheck, in composed mode, DEFERS an UNDETERMINED delivery to composed provenance (the same three steps) instead of raising the retry itself; offline\n'
'mode keeps IDENTITY-WITNESS-COMMIT-UNDETERMINED (no feed, no repository pinning there). RULE (iii) RESTATED (V28-3): when the retained event is present verbatim, a later\n'
'distinct qualifying push is AUTHENTIC-compatible — a later event does not invalidate an authentic earliest event — and NOT-EARLIEST arises only when an EARLIER qualifying\n'
'event exists; the v8 header\'s shorter phrasing ("another delivering push is an ORDERING question … (NOT-EARLIEST)") is superseded by clause (2). v8 bytes preserved in\n'
'provenance_designs_v8.py. v8 was — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V27 review (V27-1, V27-2, V27-3)')
s=rp(s,'def validate_continuation_v8(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):',
'''def validate_continuation_v9(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info). v8 PLUS (codex V28-2): an UNDETERMINED open-event delivery CONSULTS THE FEED before retrying. `authenticate_event_live` runs local_precheck
    first (not a PushEvent / wrong repository → OPEN-EVENT-INCONSISTENT-INPUT, terminal), then retrieval, then same-id contradictions (→ OPEN-EVENT-FORGED, terminal),
    NOT-EARLIEST → OPEN-EVENT-NOT-EARLIEST (terminal), EXPIRED → EVIDENCE-EXPIRED (a loss); only when nothing higher is established does the stage return
    EVIDENCE-UNAVAILABLE / EVIDENCE-INCOMPLETE (retry). Positive non-delivery stays OPEN-EVENT-INCONSISTENT-INPUT (v8). Everything else passes through."""
    ok, why, info = validate_continuation_v8(root, rel, remote_url, ref, open_event, runner, repo, expected_head=expected_head, per_page=per_page, max_pages=max_pages)
    if not ok and info.get("open_event_delivery") == "UNDETERMINED":
        oc = (info.get("remote_commits") or [None])[0]
        o, awhy, prov = authenticate_event_live(open_event, repo, runner, ref, oc, per_page=per_page, max_pages=max_pages, root=root); info["open_event"] = o; info["open_event_provenance"] = prov
        if o in ("UNAVAILABLE", "INCOMPLETE"): return False, f"EVIDENCE-{o}: the retained history-open event's delivery of the first history commit {str(oc)[:12]} could not be established and the live feed establishes nothing higher — {awhy} (v9, codex V28-2)", info
        if o == "EXPIRED": return False, f"EVIDENCE-EXPIRED: {awhy}", info
        if o == "AUTHENTIC": return False, why, info                                                        # unreachable with an undetermined delivery (authenticate_event returns UNAVAILABLE then); the v8 retry stands
        return False, f"OPEN-EVENT-{o}: {awhy} (decided before any retry; v9, codex V28-2)", info
    return ok, why, info

def validate_continuation_v8(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):''')
open(p,'w',encoding='utf-8').write(s); print("P v9 written")
# ---------------- run_configurations_v13
p='fourier_chirality/run_configurations_v13.py'; s=open(p,encoding='utf-8').read()
s=rp(s,'"""run_configurations_v12 — V28 STAGED CANDIDATE (codex V27-1/2/3; Blanc 02:06 KST 09-07: contradictions between text and code, REPAIRED, not disclosed as limits):',
'"""run_configurations_v13 — V29 STAGED CANDIDATE (codex V28-1/2/3): composed mode on provenance_designs_v9 — the witness-commit precheck no longer pre-empts the precedence\n'
'rules: on an UNDETERMINED delivery in composed mode it DEFERS to composed provenance (local_precheck → retrieval → same-id contradictions → only then RETRY-EVENTS-UNAVAILABLE);\n'
'positive non-delivery stays terminal (EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT); offline keeps IDENTITY-WITNESS-COMMIT-UNDETERMINED; the open-event stage is\n'
'validate_continuation_v9 (feed consulted before any retry). v12 was: V28 STAGED CANDIDATE (codex V27-1/2/3; Blanc 02:06 KST 09-07: contradictions between text and code, REPAIRED, not disclosed as limits):')
s=rp(s,'→ v12 (this; V28: composed on provenance_designs_v8, tri-state witness precheck).','→ v12 (V28: composed on provenance_designs_v8, tri-state witness precheck) → v13 (this; V29: composed on provenance_designs_v9, precheck defers UNDETERMINED to live authentication).')
s=rp(s,'v10→v6, v11→v7, v12→v8.]','v10→v6, v11→v7, v12→v8, v13→v9.]')
s=rp(s,'        if dvw == "UNDETERMINED": raise DataIntegrityFail(("RETRY-EVENTS-UNAVAILABLE: " if proto.provenance_mode == "composed" else "") + "IDENTITY-WITNESS-COMMIT-UNDETERMINED:',
'''        if dvw == "UNDETERMINED" and proto.provenance_mode == "composed": I["_witness_delivery"] = "UNDETERMINED"   # v13 (codex V28-1): composed mode DEFERS — live authentication (local_precheck, retrieval, same-id contradictions) decides first; composed_provenance maps UNAVAILABLE to RETRY-EVENTS-UNAVAILABLE only when nothing higher is established
        elif dvw == "UNDETERMINED": raise DataIntegrityFail("IDENTITY-WITNESS-COMMIT-UNDETERMINED:''')
s=rp(s,'| "composed" (track-2 v8 helpers on this call path)','| "composed" (track-2 v9 helpers on this call path)')
s=rp(s,'(production: provenance_designs_v8.gh_runner;','(production: provenance_designs_v9.gh_runner;')
s=rp(s,'# v6, UNADOPTED: the track-2 helpers (v8 now) ON THIS CALL PATH','# v6, UNADOPTED: the track-2 helpers (v9 now) ON THIS CALL PATH')
s=rp(s,'"""UNADOPTED COMPOSED MODE (v12 on provenance_designs_v8;','"""UNADOPTED COMPOSED MODE (v13 on provenance_designs_v9;')
s=rp(s,'(`validate_continuation_v8`: ls-remote on the pinned URL, push-acknowledgement boundary, tri-state open-event stage)','(`validate_continuation_v9`: ls-remote on the pinned URL, push-acknowledgement boundary, tri-state open-event stage that consults the feed before any retry)')
s=rp(s,'    ok, hwhy, info = P.validate_continuation_v8(w_root,','    ok, hwhy, info = P.validate_continuation_v9(w_root,')
s=rp(s,'    """the track-2 helpers (v8), imported lazily','    """the track-2 helpers (v9), imported lazily')
s=s.replace('import provenance_designs_v8 as P; return P','import provenance_designs_v9 as P; return P')   # already renamed by the copy step's sed; tolerant
assert 'import provenance_designs_v9 as P; return P' in s
for bad in ('provenance_designs_v8 as P','validate_continuation_v8(','RETRY-EVENTS-UNAVAILABLE: " if proto.provenance_mode == "composed" else "") + "IDENTITY-WITNESS-COMMIT-UNDETERMINED'): assert bad not in s, bad
open(p,'w',encoding='utf-8').write(s); print("driver v13 written")
# ---------------- driver fixture v13 header (codex V28-3 item 3)
p='fourier_chirality/test_run_configurations_v13.py'; s=open(p,encoding='utf-8').read()
s=rp(s,'"""Fixture for the STAGED driver v8 (V24 candidate; NOT GATED, NOT ADOPTED): composed mode on provenance_designs_v4','"""Fixture for the STAGED driver v13 (V29 candidate; NOT GATED, NOT ADOPTED): composed mode on provenance_designs_v9 — the fixture text below is inherited unchanged from the v8 fixture (V24) onward; only the import lines changed at each successor (codex V28-3: the header had kept calling itself the v8/V24 fixture). It was — Fixture for the STAGED driver v8 (V24 candidate; NOT GATED, NOT ADOPTED): composed mode on provenance_designs_v4')
open(p,'w',encoding='utf-8').write(s); print("driver fixture v13 header written")
# ---------------- coherent_attacks_v29
src=open('track1/coherent_attacks_v28.py',encoding='utf-8').read()
s=src.replace('import run_configurations_v12 as rc, test_run_configurations_v12 as TF, history_v2 as H, provenance_designs_v8 as P, verify_drand_v2 as vd','import run_configurations_v13 as rc, test_run_configurations_v13 as TF, history_v2 as H, provenance_designs_v9 as P, verify_drand_v2 as vd').replace('import beacon_record_drand_v28 as BD','import beacon_record_drand_v29 as BD')
s=rp(s,'"""COHERENT-ATTACK INSPECTION of the STAGED V28 candidate (driver v12, verdict v28, provenance_designs_v8; supersedes the V27 inspection;','"""COHERENT-ATTACK INSPECTION of the STAGED V29 candidate (driver v13, verdict v29, provenance_designs_v9; supersedes the V28 inspection;')
s=rp(s,'against DRIVER v12 with PRODUCTION\'s own re-deriver, and the\nstandalone v8 helpers','against DRIVER v13 with PRODUCTION\'s own re-deriver, and the\nstandalone v9 helpers')
s=rp(s,'V28_CANDIDATE_ATTACK_INSPECTION_20260907.md','V29_CANDIDATE_ATTACK_INSPECTION_20260907.md')
s=rp(s,'print("| attack | staged V28 candidate (driver v12 / verdict v28 / provenance v8) | note |")','print("| attack | staged V29 candidate (driver v13 / verdict v29 / provenance v9) | note |")')
s=rp(s,'TRACK 2(a): authenticate_event → FORGED (see below)','TRACK 2(a): codex\'s wrong-repository forgery → INCONSISTENT-INPUT (row 9b); a same-id / same-commit contradiction → FORGED (rows 9s–9u; see below)')
for bad in ('run_configurations_v12','provenance_designs_v8','beacon_record_drand_v28','V28 candidate','authenticate_event → FORGED (see below)'): assert bad not in s, bad
open('track1/coherent_attacks_v29.py','w',encoding='utf-8').write(s); print("attacks v29 written")
