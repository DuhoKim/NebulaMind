# -*- coding: utf-8 -*-
import re
def rp(s, old, new, n=1):
    assert s.count(old) >= 1, old[:90]; return s.replace(old, new, n)
# ---------------- provenance_designs_v8
p='track2/provenance_designs_v8.py'; s=open(p,encoding='utf-8').read()
s=rp(s,'"""TRACK 2 v7 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V26 review (V26-1, V26-2, V26-3):',
'"""TRACK 2 v8 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V27 review (V27-1, V27-2, V27-3) — Blanc 02:06 KST 09-07: these were CONTRADICTIONS between\n'
'the text and the code, REPAIRED here, never disclosed as limits. (V27-1) PRECEDENCE, stated and tested — the only three rules: (i) LOCALLY DECIDABLE input mismatches\n'
'(not a PushEvent; wrong repository; positive non-delivery of the commit) are decided BEFORE any retrieval: `authenticate_event_live` runs `local_precheck` first, so a\n'
'failed retrieval can never turn them into a retry; (ii) a SAME-ID contradiction (a live PushEvent carrying the retained event\'s id with different canonical bytes) needs\n'
'no ancestry and is evaluated BEFORE the undetermined-delivery return and BEFORE the verbatim-presence shortcut — FORGED, terminal; (iii) the SAME-COMMIT arm (a live\n'
'push on the PINNED PROTECTED REF delivering the same commit with different bytes) is evaluated only when the retained event is ABSENT from the feed — when it is present\n'
'verbatim, another delivering push is an ORDERING question decided by the earliest-qualifying rule (NOT-EARLIEST), not a forgery; the arm is scoped to the pinned ref\n'
'because `delivery` answers NOT-DELIVERED for any other ref. (V27-2) TRI-STATE THROUGH EVERY STAGE: `delivery` answers UNDETERMINED for a git process-launch exception\n'
'(OSError) exactly as for a missing object; `validate_continuation_v8` re-derives the retained history-open event\'s delivery tri-state for the open commit —\n'
'UNDETERMINED is EVIDENCE-UNAVAILABLE (retry), positive non-delivery is OPEN-EVENT-INCONSISTENT-INPUT (terminal) — replacing v3\'s Boolean OPEN-EVENT-DOES-NOT-DELIVER on\n'
'this path; the driver\'s witness-commit precheck (run_configurations_v12) uses the same tri-state. (V27-3) the docstrings below that describe CURRENT code are corrected;\n'
'historical paragraphs are kept verbatim and marked as such. v7 bytes preserved in provenance_designs_v7.py. v7 was — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V26 review (V26-1, V26-2, V26-3):')
s=rp(s,'maps UNAVAILABLE/INCOMPLETE/EXPIRED to EVIDENCE-* dispositions (retry)','maps UNAVAILABLE/INCOMPLETE/EXPIRED to EVIDENCE-* dispositions (retry) [HISTORICAL v6 wording, kept verbatim; corrected in v7 and since: EVIDENCE-EXPIRED is a LOSS, not a retry]')
s=rp(s,"then `authenticate_event` (v1's pure decision, unchanged): AUTHENTIC | FORGED | UNAVAILABLE | EXPIRED (the retained event is older than the",
"then `authenticate_event` (the pure decision — v8 has SEVEN outcomes with the precedence stated in the header: AUTHENTIC | UNAVAILABLE | INCOMPLETE | EXPIRED | FORGED | INCONSISTENT-INPUT | NOT-EARLIEST; EXPIRED = the retained event is older than the")
old_delivery = s[s.index('    if not root: return "UNDETERMINED"\n    for obj in (before, head, commit):'):s.index('def delivers(e, commit, branch_ref, root=None):')]
new_delivery = '''    if not root: return "UNDETERMINED"
    try:                                                                                                # v8 (codex V27-2): a git process-launch exception is evidence that could not be established
        for obj in (before, head, commit):
            if subprocess.run(["git", "cat-file", "-e", obj + "^{commit}"], cwd=root, capture_output=True).returncode != 0: return "UNDETERMINED"
        r1 = subprocess.run(["git", "merge-base", "--is-ancestor", before, commit], cwd=root, capture_output=True); r2 = subprocess.run(["git", "merge-base", "--is-ancestor", commit, head], cwd=root, capture_output=True)
    except (OSError, subprocess.SubprocessError): return "UNDETERMINED"
    if r1.returncode not in (0, 1) or r2.returncode not in (0, 1): return "UNDETERMINED"
    return "DELIVERED" if (r1.returncode == 0 and r2.returncode == 0) else "NOT-DELIVERED"
'''
s=s.replace(old_delivery,new_delivery,1)
s=rp(s,'    """TRI-STATE delivery check (v7, codex V26-2):','    """TRI-STATE delivery check (v7, codex V26-2; v8: an OSError launching git is UNDETERMINED, codex V27-2):')
a=s.index('def authenticate_event(retained, live_events, repo, branch_ref, commit, feed_reaches_back_to=None, root=None):'); b=s.index('# ------------------------------------------------------------------ (b) v3: producer boundary')
new_auth = '''def local_precheck(retained, repo, branch_ref, commit, root=None):
    """(v8, codex V27-1 rule i) The LOCALLY DECIDABLE part of `authenticate_event`, evaluated BEFORE any retrieval: returns ("INCONSISTENT-INPUT", why) for a positive
    input mismatch, else (None, delivery_state) with delivery_state ∈ DELIVERED | UNDETERMINED — nothing local contradicts, the feed decides."""
    if not isinstance(retained, dict) or retained.get("type") != "PushEvent": return "INCONSISTENT-INPUT", "retained object is not a PushEvent"
    if (retained.get("repo") or {}).get("name") != repo: return "INCONSISTENT-INPUT", f"retained event names repository {(retained.get('repo') or {}).get('name')!r}, not the pinned {repo!r}"
    dv = delivery(retained, commit, branch_ref, root)
    if dv == "NOT-DELIVERED": return "INCONSISTENT-INPUT", "the retained event positively does not deliver the approval commit to the protected ref"
    return None, dv
def same_id_contradictions(retained, live_events):
    """(v8, codex V27-1 rule ii) live PushEvents carrying the retained event's id with DIFFERENT canonical bytes — decidable without any ancestry."""
    d = canon(retained); return [e for e in (live_events or []) if isinstance(e, dict) and e.get("type") == "PushEvent" and e.get("id") == retained.get("id") and canon(e) != d]
def authenticate_event(retained, live_events, repo, branch_ref, commit, feed_reaches_back_to=None, root=None):
    """The pure decision (v8): (outcome, why). Outcomes: AUTHENTIC | UNAVAILABLE (feed missing/empty, or delivery UNDETERMINED with no same-id contradiction — retry) |
    INCOMPLETE (absent, nothing contradicts — retry) | EXPIRED (older than the feed reaches — a loss) | FORGED (an affirmative contradiction: same id, or — only when
    the retained event is absent — same delivered commit on the pinned ref, with different bytes) | INCONSISTENT-INPUT (not a PushEvent for the pinned repository, or
    positive non-delivery) | NOT-EARLIEST. PRECEDENCE (codex V27-1): local mismatches first; same-id contradictions next (before UNDETERMINED and before the verbatim
    shortcut); then unavailability; then absence (same-commit contradiction / expiry / incompleteness); then ordering. No other precedence exception exists."""
    o, x = local_precheck(retained, repo, branch_ref, commit, root)
    if o is not None: return o, x
    dv = x; d = canon(retained)
    same = same_id_contradictions(retained, live_events)
    if same: return "FORGED", f"the live feed carries a push with the retained event's id {retained.get('id')!r} whose canonical bytes DIFFER from the retained event (e.g. before/head {(same[0].get('payload') or {}).get('before', '')[:12]}..{(same[0].get('payload') or {}).get('head', '')[:12]}) — an affirmative contradiction, decided before any retry (v8, codex V27-1)"
    if dv == "UNDETERMINED": return "UNAVAILABLE", "the retained event's before..head delivery of the approval commit could not be established here (a git object missing locally, a failed or unlaunchable git command) and no same-id contradiction is in the feed — not evidence of anything; retry with the objects fetched (v7, codex V26-2; v8, codex V27-1)"
    if live_events is None: return "UNAVAILABLE", "the live feed could not be retrieved; retry — nothing else changes"
    if not live_events: return "UNAVAILABLE", "the live feed is EMPTY — no evidence either way (v3, codex V22 F); retry"
    if not any(canon(e) == d for e in live_events):
        same_commit = [e for e in live_events if isinstance(e, dict) and e.get("type") == "PushEvent" and delivery(e, commit, branch_ref, root) == "DELIVERED" and canon(e) != d]   # scoped to the pinned ref by `delivery`; absent-only (rule iii)
        if same_commit: return "FORGED", f"the retained event is absent and the live feed carries a push on the pinned ref delivering the same commit with different canonical bytes (e.g. {same_commit[0].get('id')}) — an affirmative contradiction (v7, codex V26-1)"
        if feed_reaches_back_to is not None and str(retained.get("created_at")) < feed_reaches_back_to: return "EXPIRED", "the live feed no longer reaches the event's time; only an independent receipt taken inside the window can stand in"
        return "INCOMPLETE", "the retained event is absent from the retrieved feed and nothing in the feed contradicts it — absence is not proof of fabrication; retry within the window (v6, codex V25 P2)"
    qualifying = [e for e in live_events if isinstance(e, dict) and e.get("type") == "PushEvent" and delivery(e, commit, branch_ref, root) == "DELIVERED"]
    earliest = min(qualifying, key=lambda e: e["created_at"])
    if canon(earliest) != d: return "NOT-EARLIEST", "an earlier qualifying event exists in the live feed; the retained one is not the earliest (an input inconsistency, not 'different bytes')"
    return "AUTHENTIC", "retained event present verbatim in the live feed of the pinned repository, earliest qualifying, no same-id contradiction"
def authenticate_event_live(retained, repo, runner, branch_ref, commit, per_page=100, max_pages=3, root=None):
    """(v8, codex V27-1 rule i) decide the locally decidable part FIRST, then retrieve, then decide. (outcome, why, provenance)."""
    o, x = local_precheck(retained, repo, branch_ref, commit, root)
    if o is not None: return o, x, None
    try: live, prov = retrieve_events(repo, runner, per_page=per_page, max_pages=max_pages)
    except EventsUnavailable as e: return "UNAVAILABLE", f"{e.kind}: {e.why}", None
    o, why = authenticate_event(retained, live, repo, branch_ref, commit, feed_reaches_back_to=prov.get("oldest_created_at"), root=root); return o, why, prov

'''
s=s[:a]+new_auth+s[b:]
s=rp(s,'def validate_continuation_v7(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):',
'''def validate_continuation_v8(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info). v7 PLUS (codex V27-2): the OPEN-EVENT STAGE IS TRI-STATE. v3's stage decides the open event's delivery of the first history commit with the
    Boolean `delivers` (OPEN-EVENT-DOES-NOT-DELIVER); v8 re-derives the tri-state for that SAME commit (info['remote_commits'][0], after v3's fetch of the remote ref):
    UNDETERMINED → EVIDENCE-UNAVAILABLE (retry; nothing is established), NOT-DELIVERED → OPEN-EVENT-INCONSISTENT-INPUT (positive, terminal). Everything else passes through."""
    ok, why, info = validate_continuation_v7(root, rel, remote_url, ref, open_event, runner, repo, expected_head=expected_head, per_page=per_page, max_pages=max_pages)
    if not ok and why.startswith("OPEN-EVENT-DOES-NOT-DELIVER"):
        oc = (info.get("remote_commits") or [None])[0]; dv = delivery(open_event, oc, ref, root) if oc else "UNDETERMINED"; info["open_event_delivery"] = dv
        if dv == "UNDETERMINED": return False, f"EVIDENCE-UNAVAILABLE: the retained history-open event's delivery of the first history commit {str(oc)[:12]} could not be established here (a git object missing locally, a failed or unlaunchable git command) — not evidence of anything; retry with the objects fetched (v8, codex V27-2)", info
        return False, f"OPEN-EVENT-INCONSISTENT-INPUT: the retained history-open event positively does not deliver the first history commit {str(oc)[:12]} (v8, codex V27-2)", info
    return ok, why, info

def validate_continuation_v7(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):''')
open(p,'w',encoding='utf-8').write(s); print("P v8 written")
# ---------------- run_configurations_v12
p='fourier_chirality/run_configurations_v12.py'; s=open(p,encoding='utf-8').read()
s=rp(s,'"""run_configurations_v11 — V27 STAGED CANDIDATE (codex V26-1/2/3): composed mode on provenance_designs_v7 —',
'"""run_configurations_v12 — V28 STAGED CANDIDATE (codex V27-1/2/3; Blanc 02:06 KST 09-07: contradictions between text and code, REPAIRED, not disclosed as limits):\n'
'composed mode on provenance_designs_v8 — locally decidable input mismatches are decided BEFORE any retrieval; same-id contradictions before any retry shortcut; delivery\n'
'is TRI-STATE through the witness-commit precheck (UNDETERMINED → RETRY-EVENTS-UNAVAILABLE in composed mode / IDENTITY-WITNESS-COMMIT-UNDETERMINED offline, where no\n'
'retry vocabulary exists; positive non-delivery → EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT in composed mode / IDENTITY-WITNESS-COMMIT offline) and through the open-event\n'
'stage (validate_continuation_v8: EVIDENCE-UNAVAILABLE retry / OPEN-EVENT-INCONSISTENT-INPUT terminal). v11 was: V27 STAGED CANDIDATE (codex V26-1/2/3): composed mode on provenance_designs_v7 —')
s=rp(s,'→ v10 (V26: composed on provenance_designs_v7) → v11 (this).','→ v10 (V26: composed on provenance_designs_v6) → v11 (V27: composed on provenance_designs_v7) → v12 (this; V28: composed on provenance_designs_v8, tri-state witness precheck).\n[V27-3, codex: the v11 table\'s v10 row said provenance_designs_v7; v10\'s bytes import provenance_designs_v6. This table was re-verified row by row against each retained driver\'s own\n`import provenance_designs_vN as P` line: v6→v2, v7→v3, v8→v4, v9→v5, v10→v6, v11→v7, v12→v8.]')
s=rp(s,'| "composed" (track-2 v6 helpers on this call path)','| "composed" (track-2 v8 helpers on this call path)')
s=rp(s,'(production: provenance_designs_v7.gh_runner;','(production: provenance_designs_v8.gh_runner;')
s=rp(s,'        if not AW.delivers(ev, commit, proto.witness_branch_ref, w_root): raise DataIntegrityFail("IDENTITY-WITNESS-COMMIT: the push event does not deliver the approval commit (head, commits, or before..head ancestry)")',
'''        dvw = _P().delivery(ev, commit, proto.witness_branch_ref, w_root)                                   # v12 (codex V27-2): TRI-STATE on the complete path — the same predicate composed mode uses
        if dvw == "NOT-DELIVERED": raise DataIntegrityFail(("EVENT-INCONSISTENT: " if proto.provenance_mode == "composed" else "") + "IDENTITY-WITNESS-COMMIT: the push event positively does not deliver the approval commit (head, commits, or before..head ancestry established false)")
        if dvw == "UNDETERMINED": raise DataIntegrityFail(("RETRY-EVENTS-UNAVAILABLE: " if proto.provenance_mode == "composed" else "") + "IDENTITY-WITNESS-COMMIT-UNDETERMINED: the push event's before..head delivery of the approval commit could not be established here (a git object missing locally, a failed or unlaunchable git command) — not evidence of anything; fetch the objects and retry")''')
s=rp(s,'# v6, UNADOPTED: the track-2 v6 helpers ON THIS CALL PATH (default "offline")','# v6, UNADOPTED: the track-2 helpers (v8 now) ON THIS CALL PATH (default "offline")')
s=rp(s,'"""UNADOPTED COMPOSED MODE (v11 on provenance_designs_v7;','"""UNADOPTED COMPOSED MODE (v12 on provenance_designs_v8;')
s=rp(s,'(`validate_continuation_v6`: ls-remote on the pinned URL, push-acknowledgement boundary)','(`validate_continuation_v8`: ls-remote on the pinned URL, push-acknowledgement boundary, tri-state open-event stage)')
s=rp(s,'    sys.path.insert(0, str(HERE.parents[0] / "track2")); import provenance_designs_v8 as P\n    runner = proto.events_runner or P.gh_runner','    P = _P(); runner = proto.events_runner or P.gh_runner')
s=rp(s,'    ok, hwhy, info = P.validate_continuation_v7(w_root,','    ok, hwhy, info = P.validate_continuation_v8(w_root,')
s=rp(s,'HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))','HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))\ndef _P():\n    """the track-2 helpers (v8), imported lazily: used by the witness-commit precheck in every mode and by composed mode."""\n    sys.path.insert(0, str(HERE.parents[0] / "track2")); import provenance_designs_v8 as P; return P')
for bad in ('provenance_designs_v7 as P','validate_continuation_v7(','validate_continuation_v6`','track-2 v6 helpers','AW.delivers(ev, commit'): assert bad not in s, bad
open(p,'w',encoding='utf-8').write(s); print("driver v12 written")
