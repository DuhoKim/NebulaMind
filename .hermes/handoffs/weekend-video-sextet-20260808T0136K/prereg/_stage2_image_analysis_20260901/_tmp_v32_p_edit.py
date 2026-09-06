# -*- coding: utf-8 -*-
import re
def rp(s, old, new, n=1):
    assert s.count(old) >= 1, old[:90]; return s.replace(old, new, n)
p='track2/provenance_designs_v12.py'; s=open(p,encoding='utf-8').read()
s=rp(s,'"""TRACK 2 v11 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V30 review (V30-1 FATAL, V30-2, V30-3, V30-4), still under Blanc\'s order of 03:20 (one order, one\nresolver).',
'"""TRACK 2 v12 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V31 review (V31-1..5) under BLANC\'S ORDER OF 05:02 KST 09-07: ONE PROPERTY, named NSD — "No Stage\n'
'Decides": NO STAGE MAY DECIDE OR ABORT; EVERY STAGE CONTRIBUTES; ONE RESOLVER DECIDES. Precedence (PRECEDENCE / resolve, unchanged here) is its ordering half; the\n'
'contribution half is enforced in run_configurations_v16.load_identity_composed and made checkable by its INDEPENDENCE table. Codex\'s four V31 clauses are consequences of\n'
'NSD. WHAT V12 CHANGES, as those consequences: (a) `retrieve_events` KEEPS every obtained page — a later page\'s transport / HTTP / JSON / shape failure is returned as\n'
'prov["partial"] with the events obtained so far, never discarding them (V31-2); a first-page failure still raises EventsUnavailable; malformed events inside an obtained\n'
'page are returned in prov["malformed"] (remote provenance) and excluded from the predicates. (b) `authenticate_event(..., complete=True)`: BOTH contradiction arms\n'
'(same-id; absent + same delivered commit on the pinned ref) are evaluated before any availability disposition, including for an undetermined retained delivery\n'
'(V31-3); with complete=False (a partial snapshot) only affirmative findings are returned (FORGED, NOT-EARLIEST) — presence, absence, expiry and AUTHENTIC are never\n'
'established from a partial snapshot (V31-2). (c) `history_findings_v12`: NO LOOP STOPS — every adjacent extension relation, every per-entry publication and the ordering\n'
'relation are evaluated and every finding kept (V31-3); the open-event checks are recorded as BLOCKED (not skipped) when no valid open event exists; a partial snapshot\n'
'contributes unavailability for the per-entry presence checks while proven batches are still reported. (d) `validate_continuation_v12` (standalone) sweeps the open event\n'
'locally BEFORE consulting the remote, sharing the composed path\'s obligation (V31-3). (e) CLASSIFICATION IS AN ALLOWLIST: `CLASS_ALLOWLIST` names every refusal code the\n'
'driver and these helpers actually raise (extracted from the sources; the track-12 test re-extracts and compares) with its class; `classify_refusal` places only\n'
'allowlisted codes and FLAGS every other code (no family prefixes); `classify_exception(exc, source)` classifies by PROVENANCE — source="retained" → MALFORMED-RETAINED-INPUT\n'
'(class 0), source="remote" → MALFORMED-REMOTE-EVIDENCE (class 5, evidence unusable, not a local contradiction); I/O and subprocess failures → IO-UNAVAILABLE (class 5)\n'
'(V31-4). (f) `verify_events_receipt` normalizes every internal failure (malformed nested values included) to (False, "RECEIPT-…") so the driver\'s receipt policy (class 3)\n'
'holds for exceptions too (V31-4). v11 bytes preserved in provenance_designs_v11.py. v11 was — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V30 review (V30-1 FATAL, V30-2, V30-3, V30-4), still under Blanc\'s order of 03:20 (one order, one\nresolver).')
# ---- retrieve_events: keep obtained pages
a=s.index('def retrieve_events(repo, runner=gh_runner, per_page=100, max_pages=3):'); b=s.index('def delivery(e, commit, branch_ref, root=None):')
s=s[:a]+'''def retrieve_events(repo, runner=gh_runner, per_page=100, max_pages=3):
    """Read-only retrieval with pagination — ONE logical retrieval that KEEPS every obtained page (v12, codex V31-2). Returns (events newest-first, provenance).
    A FIRST-page failure raises EventsUnavailable(kind). A LATER page's failure is recorded in prov["partial"] = {"page", "kind", "why"} and the events obtained so far
    are returned; callers must treat a partial snapshot as evidence for affirmative findings only. Events that are not PushEvent-shaped objects (a non-dict
    payload, a non-string ref) are removed from the returned list and recorded in prov["malformed"] — REMOTE provenance, never retained input."""
    out = []; prov = {"repo": repo, "endpoints": [], "retrieved_utc": utc(), "per_page": per_page, "pages_fetched": 0, "truncated_by_max_pages": False, "oldest_created_at": None, "partial": None, "malformed": []}
    for page in range(1, max_pages + 1):
        ep = f"repos/{repo}/events?per_page={per_page}&page={page}"; prov["endpoints"].append(ep)
        def fail(kind, why):
            if page == 1: raise EventsUnavailable(kind, why)
            prov["partial"] = {"page": page, "kind": kind, "why": why}; return True
        try: rc, so, se = runner(["gh", "api", ep])
        except Exception as e:
            if fail("TRANSPORT", repr(e)[:120]): break
        if rc != 0:
            m = re.search(r"HTTP (\\d{3})", se or ""); code = int(m.group(1)) if m else None
            kind = "RATE-LIMITED" if (code == 403 and "rate limit" in (se or "").lower()) or code == 429 else "AUTH" if code == 401 else "NOT-FOUND" if code == 404 else "SERVER-ERROR" if code and code >= 500 else "HTTP"
            if fail(kind, (se or "").strip()[:160]): break
        try: body = json.loads(so)
        except Exception as e:
            if fail("MALFORMED", "response is not JSON: " + repr(e)[:80]): break
        if not isinstance(body, list):
            if fail("MALFORMED", "response is not a list of events"): break
        good = []
        for x in body:
            if isinstance(x, dict) and (x.get("type") != "PushEvent" or (isinstance(x.get("payload"), dict) and isinstance(x["payload"].get("ref", ""), str))): good.append(x)
            else: prov["malformed"].append({"page": page, "id": x.get("id") if isinstance(x, dict) else None, "why": "not a PushEvent-shaped object"})
        prov["pages_fetched"] += 1; out.extend(good)
        if len(body) < per_page: break
    else: prov["truncated_by_max_pages"] = True
    times = [str(e.get("created_at")) for e in out if e.get("created_at")]; prov["oldest_created_at"] = min(times) if times else None
    return out, prov
'''+s[b:]
# ---- authenticate_event: both arms before availability; complete flag
s=rp(s,'def authenticate_event(retained, live_events, repo, branch_ref, commit, feed_reaches_back_to=None, root=None):','def authenticate_event(retained, live_events, repo, branch_ref, commit, feed_reaches_back_to=None, root=None, complete=True):')
old_und = s[s.index('    if dv == "UNDETERMINED" and feed_reaches_back_to is not None'):s.index('    if live_events is None: return "UNAVAILABLE", "the live feed could not be retrieved; retry — nothing else changes"')]
new_und = '''    present = bool(live_events) and any(canon(e) == d for e in live_events)
    if live_events and not present:                                                                     # (v12, codex V31-3) the ABSENT + same-commit arm is evaluated before ANY availability disposition
        same_commit = [e for e in live_events if isinstance(e, dict) and e.get("type") == "PushEvent" and delivery(e, commit, branch_ref, root) == "DELIVERED" and canon(e) != d]
        if same_commit: return "FORGED", f"the retained event is absent and the live feed carries a push on the pinned ref delivering the same commit with different canonical bytes (e.g. {same_commit[0].get('id')}) — an affirmative contradiction, evaluated before any retry (v7, codex V26-1; v12, codex V31-3)"
    if not complete:                                                                                    # (v12, codex V31-2) a PARTIAL snapshot establishes affirmative findings only
        if present and dv == "DELIVERED":
            qualifying = [e for e in live_events if isinstance(e, dict) and e.get("type") == "PushEvent" and delivery(e, commit, branch_ref, root) == "DELIVERED"]
            earlier = [e for e in qualifying if str(e.get("created_at")) < str(retained.get("created_at"))]
            if earlier: return "NOT-EARLIEST", f"a strictly earlier qualifying event was obtained ({earlier[0].get('id')} at {earlier[0].get('created_at')}) — affirmative even on a partial snapshot"
        return "UNAVAILABLE", "the events retrieval was PARTIAL (a later page failed) and nothing obtained contradicts the retained event — presence, absence, expiry and acceptance are never established from a partial snapshot; retry"
    if dv == "UNDETERMINED" and feed_reaches_back_to is not None and str(retained.get("created_at")) < str(feed_reaches_back_to): return "EXPIRED", "the retained event's delivery could not be established and the live feed no longer reaches the event's time — a loss, which outranks a retry (v11, codex V30-3); only an independent receipt taken inside the window can stand in"
    if dv == "UNDETERMINED": return "UNAVAILABLE", "the retained event's before..head delivery of the approval commit could not be established here (a git object missing locally, a failed or unlaunchable git command) and nothing obtained contradicts it (both arms evaluated) — not evidence of anything; retry with the objects fetched (v7, codex V26-2; v8, codex V27-1; v12, codex V31-3)"
'''
s=s.replace(old_und,new_und,1)
s=s.replace('''    if not any(canon(e) == d for e in live_events):
        same_commit = [e for e in live_events if isinstance(e, dict) and e.get("type") == "PushEvent" and delivery(e, commit, branch_ref, root) == "DELIVERED" and canon(e) != d]   # scoped to the pinned ref by `delivery`; absent-only (rule iii)
        if same_commit: return "FORGED", f"the retained event is absent and the live feed carries a push on the pinned ref delivering the same commit with different canonical bytes (e.g. {same_commit[0].get('id')}) — an affirmative contradiction (v7, codex V26-1)"
        if feed_reaches_back_to''','''    if not present:
        if feed_reaches_back_to''',1)
assert 'if not present:\n        if feed_reaches_back_to' in s
# authenticate_event_live passes complete
s=rp(s,"    o, why = authenticate_event(retained, live, repo, branch_ref, commit, feed_reaches_back_to=prov.get(\"oldest_created_at\"), root=root); return o, why, prov","    o, why = authenticate_event(retained, live, repo, branch_ref, commit, feed_reaches_back_to=prov.get(\"oldest_created_at\"), root=root, complete=prov.get(\"partial\") is None); return o, why, prov")
# ---- receipt: normalize internal failures
s=rp(s,'def verify_events_receipt(receipt_path, root, remote_url, ref, retained_event, expected_origin):','''def verify_events_receipt(receipt_path, root, remote_url, ref, retained_event, expected_origin):
    """(ok, why). v12: every internal failure — malformed nested values, unexpected types, I/O — is normalized to (False, "RECEIPT-MALFORMED: …") so the driver's receipt
    policy (class 3) holds for exceptions as for refusals (codex V31-4)."""
    try: return _verify_events_receipt_inner(receipt_path, root, remote_url, ref, retained_event, expected_origin)
    except Exception as e: return False, f"RECEIPT-MALFORMED: the receipt could not be verified ({type(e).__name__}: {str(e)[:120]})"
def _verify_events_receipt_inner(receipt_path, root, remote_url, ref, retained_event, expected_origin):''')
s=rp(s,'    origin = rec.get("origin") or {}\n','    origin = rec.get("origin") if isinstance(rec.get("origin"), dict) else {}\n    if not isinstance(rec.get("origin"), dict): return False, f"RECEIPT-ORIGIN: receipt origin is not an object ({type(rec.get(\'origin\')).__name__})"\n')
# ---- classification: allowlist
a=s.index('CLASS_EXACT = {'); b=s.index('def history_findings_v11(')
s=s[:a]+'''LOCAL = "LOCAL-TERMINAL"; DERIVED = "DERIVED-TERMINAL"; RETRY = "RETRY-UNAVAILABLE"
CLASS_ALLOWLIST = {
    # --- driver: local integrity of retained input (class 0)
    **{c: LOCAL for c in ("ADOPTION-MISSING", "ADOPTION-MALFORMED", "ADOPTION-MISMATCH", "ADOPTION-NOT-AT-APPROVAL-COMMIT", "ADOPTION-DIGEST", "WITNESS-MISSING", "WITNESS-COMMIT-MALFORMED", "WITNESS-NOT-A-GIT-REPO", "WITNESS-COMMIT-LACKS-JOURNAL", "WITNESS-COMMIT-LACKS-RECORD", "WITNESS-REMOTE-URL",
        "IDENTITY-MISSING", "IDENTITY-NOT-SEALED", "IDENTITY-NOT-IN-WITNESS-COMMIT", "IDENTITY-SCHEMA", "IDENTITY-FIELD-MISSING", "IDENTITY-POOL-DIGEST", "IDENTITY-EXCLUSION-DIGEST", "PROTOCOL-NO-REDERIVER", "IDENTITY-RULE-DIGEST", "IDENTITY-NOT-BEACON-SEEDED", "IDENTITY-BEACON-NOT-ACCEPTED", "IDENTITY-SOURCE",
        "IDENTITY-WITNESS-MISSING", "IDENTITY-WITNESS-COMMIT", "APPROVAL-RECORD-MISSING", "APPROVAL-RECORD-DIGEST", "APPROVAL-RECORD-NOT-AT-COMMIT", "APPROVAL-RECORD-HISTORY", "APPROVAL-NOT-FIRST", "APPROVAL-RULE-LINE", "APPROVAL-T-SIGN-LINE", "APPROVAL-NONCE-LINE", "IDENTITY-T-SIGN", "IDENTITY-T-PULSE", "IDENTITY-ROUND",
        "IDENTITY-T-SIGN-PREDATES-AMENDMENT", "IDENTITY-T-PULSE-EXCLUDED", "IDENTITY-WITNESS-TIME", "IDENTITY-WITNESS-LATE", "EVENT-DIGEST", "EVENT-INCONSISTENT", "EVENT-PROVENANCE", "IDENTITY-WITNESS-NONCE", "NONCE-UNAUTHENTICATED", "COLLECTION-LOG-DIGEST", "COLLECTION-LOG-NOT-IN-WITNESS-COMMIT", "HISTORY-INVALID",
        "HISTORY-GENESIS", "HISTORY-COUNT", "COLLECTION-LOG-EMPTY", "IDENTITY-LOCK-MISMATCH", "COLLECTION-CLOSED", "COLLECTION-LOG-CONFLICT", "BEACON-RECORD-DIGEST", "BEACON-RECORD-NOT-IN-WITNESS-COMMIT", "BEACON-RECORD-UNREADABLE", "BEACON-RECORD-BINDING", "BEACON-RECORD-STATEMENT", "BEACON-RECORD-RELAYS",
        "HISTORY-OPEN-EVENT-MISSING", "HISTORY-OPEN-EVENT-INVALID", "IDENTITY-tuning_objids-SIZE-OR-TYPE", "IDENTITY-holdout_objids-SIZE-OR-TYPE", "IDENTITY-fresh_validation_objids-SIZE-OR-TYPE", "IDENTITY-OVERLAP", "SPLIT-INPUTS", "SPLIT-NOT-REPRODUCED", "MALFORMED-RETAINED-INPUT", "STAGE-NOT-RUN", "OPEN-EVENT-INCONSISTENT-INPUT",
        # driver refusals OUTSIDE load_identity (tuning / holdout / manifests / environment): class 0 by cause, listed so the table is total over the driver's raises
        "ENV-MISMATCH", "ENV-LOCK-HASH-MISMATCH", "ESTIMATOR-CHANGED-SINCE-TUNING", "HOLDOUT-OVERLAPS-TUNING", "HOLDOUT-ALREADY-INVOKED", "IDENTITY-DIFFERS-FROM-TUNING", "LABEL-NOT-PM1", "MANIFEST-COLUMNS", "MANIFEST-DUPLICATE-OBJID", "MANIFEST-IDENTITY-MISMATCH", "MANIFEST-MISSING", "MANIFEST-SIZE", "NO-TUNING-WINNER",
        "RENDER-JOURNAL-COUNT", "RENDER-JOURNAL-INCOMPLETE", "RENDER-JOURNAL-MALFORMED", "RENDER-JOURNAL-NOT-ENDED", "RENDER-JOURNAL-REFUSAL-SHAPE", "RUN-ROOT-MISMATCH", "RUN-ROOT-PARTS-DIFFER", "SENTINEL-JOURNAL-MISMATCH", "SENTINEL-WITHOUT-RENDER-JOURNAL", "TENSOR-DIR-MISSING", "TENSOR-MISSING", "TENSOR-SHA-MISMATCH", "TENSOR-SIZE",
        "TUNING-FILE-NOT-IN-WITNESS-COMMIT", "TUNING-JOURNAL-DUPLICATE", "TUNING-NOT-SEALED", "TUNING-RECEIPT-HASHES", "TUNING-RECEIPT-MODE", "TUNING-RECEIPT-MISSING", "TUNING-RECEIPT-CONFIG", "TUNING-RECEIPTS-COUNT", "WINNER-SUBSTITUTED",
        # helpers: producer / receipt refusals that name a local input defect
        "PUBLISH-BATCH", "PUBLISH-UNRELATED-COMMITS", "PUBLISH-COMMIT-FAILED", "RECEIPT-MALFORMED", "RECEIPT-DIGEST", "RECEIPT-ORIGIN", "RECEIPT-EVENT-ABSENT", "RECEIPT-MODIFIED", "RECEIPT-NOT-FIRST", "RECEIPT-NOT-PUBLISHED", "HISTORY-OPEN-COMMIT-MISMATCH", "HISTORY-OPEN-NOT-PUBLISHED", "OPEN-EVENT-DOES-NOT-DELIVER")},
    # --- affirmative contradictions in obtained live evidence (class 1), ordering (class 2), loss (class 3)
    "EVENT-FORGED": "FORGED", "OPEN-EVENT-FORGED": "FORGED", "EVENT-NOT-EARLIEST": "NOT-EARLIEST", "OPEN-EVENT-NOT-EARLIEST": "NOT-EARLIEST", "EVENT-EXPIRED-NO-RECEIPT-PATH": "EXPIRED", "EVENT-EXPIRED-RECEIPT-REFUSED": "EXPIRED", "EVIDENCE-EXPIRED": "EXPIRED",
    # --- derived from obtained remote / retained evidence by verification (class 4) — policies named in §3c
    **{c: DERIVED for c in ("IDENTITY-SEED-NOT-REDERIVED", "REDERIVE-REFUSE", "REDERIVE-CLOSED", "REDERIVE-REFUSE-ROUND", "WITNESS-NOT-PUSHED", "APPROVAL-COMMIT-NOT-PUSHED", "HISTORY-NOT-AN-EXTENSION", "HISTORY-DELETED-AT", "HISTORY-BATCH-COMMIT", "HISTORY-PUBLICATION-BATCH", "HISTORY-PUBLICATION-ORDER", "HISTORY-NO-COMMITS", "OPEN-NOT-GENESIS-ONLY", "PENDING-PUSH", "HISTORY-DIVERGED", "STALE-EXPECTED-HEAD", "HISTORY-CONTINUATION")},
    # --- evidence or environment not obtainable now (class 5) / absent, nothing contradicts (class 6)
    **{c: RETRY for c in ("REDERIVE-RETRY", "WITNESS-FETCH-FAILED", "VERIFIER-UNAVAILABLE", "IO-UNAVAILABLE", "IDENTITY-WITNESS-COMMIT-UNDETERMINED", "RETRY-EVENTS-UNAVAILABLE", "RETRY-REMOTE-UNAVAILABLE", "EVIDENCE-UNAVAILABLE", "MALFORMED-REMOTE-EVIDENCE", "RETRY-HISTORY-CONTINUATION", "STAGE-BLOCKED")},
    "EVIDENCE-INCOMPLETE": "RETRY-INCOMPLETE", "RETRY-EVENTS-INCOMPLETE": "RETRY-INCOMPLETE",
}
# 'HISTORY-CONTINUATION' / 'RETRY-HISTORY-CONTINUATION' are COMPOSED names whose reason carries the specific token; the driver classifies those findings from the token via classify_history.
def classify_refusal(message):
    """(class, code, why, unclassified). The code is the refusal name up to the first ':' or space. ONLY allowlisted codes are placed; every other code — including a new
    member of a known family — is placed LOCAL-TERMINAL and FLAGGED (unclassified=True) so a reviewer sees it (v12, codex V31-4: no family prefixes)."""
    msg = str(message); code = re.split(r"[:\\s]", msg, 1)[0]; why = msg[len(code):].lstrip(": ").strip() or msg
    if code in CLASS_ALLOWLIST:
        cls = CLASS_ALLOWLIST[code]
        if code in ("HISTORY-CONTINUATION", "RETRY-HISTORY-CONTINUATION"): cls = classify_history(why)[0]
        return cls, code, why, False
    return "LOCAL-TERMINAL", code, why, True
def classify_exception(exc, source="retained"):
    """(class, code, why, unclassified) for any exception a stage body raised, BY PROVENANCE (v12, codex V31-4): the driver's DataIntegrityFail → classify_refusal; a shape /
    type / key / value error over RETAINED input → LOCAL-TERMINAL MALFORMED-RETAINED-INPUT; the same over REMOTE evidence (source="remote") → RETRY-UNAVAILABLE
    MALFORMED-REMOTE-EVIDENCE (unusable evidence is not a local contradiction); I/O and subprocess failures → RETRY-UNAVAILABLE IO-UNAVAILABLE; anything else flagged."""
    if type(exc).__name__ == "DataIntegrityFail": return classify_refusal(str(exc))
    if isinstance(exc, (OSError, subprocess.SubprocessError)): return "RETRY-UNAVAILABLE", "IO-UNAVAILABLE", f"{type(exc).__name__}: {exc}"[:300], False
    if isinstance(exc, (json.JSONDecodeError, ValueError, KeyError, TypeError, IndexError, AttributeError, UnicodeError)):
        if source == "remote": return "RETRY-UNAVAILABLE", "MALFORMED-REMOTE-EVIDENCE", f"{type(exc).__name__}: {exc}"[:300], False
        return "LOCAL-TERMINAL", "MALFORMED-RETAINED-INPUT", f"{type(exc).__name__}: {exc}"[:300], False
    return "LOCAL-TERMINAL", f"UNEXPECTED-{type(exc).__name__}", str(exc)[:300], True
'''+s[b:]
# ---- history_findings_v12: no loop stops; blocked open checks; partial handling
s=rp(s,'def history_findings_v11(root, rel, remote_url, ref, open_event, live, prov, repo):','''def history_findings_v12(root, rel, remote_url, ref, open_event, live, prov, repo):
    """THE HISTORY STAGE AS A COLLECTOR, v12 (codex V31-3): NO LOOP STOPS — every adjacent extension relation, every per-entry publication and the ordering relation are
    evaluated and every finding kept; when no valid open event exists (None) the open-event checks are reported BLOCKED in info["blocked"], not skipped; on a PARTIAL
    snapshot (prov["partial"]) proven batches are still reported while a missing own-publication contributes unavailability, not incompleteness. Returns (findings, info)."""
    F = []; info = {"remote_url": remote_url, "ref": ref, "asked_utc": utc(), "blocked": {}}; complete = live is not None and not (prov or {}).get("partial")
    head = remote_head(remote_url, ref); info["remote_head"] = head
    if head is None:
        F.append(("RETRY-UNAVAILABLE", "HISTORY-CONTINUATION", "RETRY-REMOTE-UNAVAILABLE: the remote did not answer ls-remote; nothing on the remote can be examined until it does")); info["blocked"].update({"open-delivery-auth": "remote-head unavailable", "history-remote": "remote-head unavailable", "per-entry": "remote-head unavailable"}); return F, info
    if not _fetch_witness(root, remote_url, ref, head):
        F.append(("RETRY-UNAVAILABLE", "HISTORY-CONTINUATION", "RETRY-REMOTE-UNAVAILABLE: could not fetch the remote ref's objects")); info["blocked"].update({"open-delivery-auth": "remote objects not fetched", "history-remote": "remote objects not fetched", "per-entry": "remote objects not fetched"}); return F, info
    rc_, out = _git(root, "log", "--reverse", "--format=%H", head, "--", rel); commits = out.decode().split(); info["remote_commits"] = commits
    if rc_ != 0 or not commits: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", "HISTORY-NO-COMMITS on the remote ref")); return F, info
    oc = commits[0]; open_blob = _blob_at(root, oc, rel) or b""
    try:
        import tempfile; tp = Path(tempfile.mkdtemp()) / "open.jsonl"; tp.write_bytes(open_blob); ents = H.validate(tp)
        if len(ents) != 1 or ents[0].get("stage") != "genesis": F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"OPEN-NOT-GENESIS-ONLY: the first history commit {oc[:12]} carries {len(ents)} entries; a history-open commit carries exactly the genesis — a late first publication of a rebuilt history is refused"))
    except ValueError as e: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"OPEN-NOT-GENESIS-ONLY: the first history commit's blob is not a valid genesis ({e})"))
    if isinstance(open_event, dict):
        dv = delivery(open_event, oc, ref, root); info["open_event_delivery"] = dv
        if dv == "NOT-DELIVERED": F.append(("LOCAL-TERMINAL", "HISTORY-CONTINUATION", f"OPEN-EVENT-INCONSISTENT-INPUT: the retained history-open event positively does not deliver the first history commit {oc[:12]}"))
        o, why = authenticate_event(open_event, live, repo, ref, oc, feed_reaches_back_to=(prov or {}).get("oldest_created_at"), root=root, complete=complete); info["open_event"] = o
        if o == "UNAVAILABLE": F.append(("RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION", f"EVIDENCE-UNAVAILABLE (history-open event): {why}"))
        elif o == "INCOMPLETE": F.append(("RETRY-INCOMPLETE", "RETRY-HISTORY-CONTINUATION", f"EVIDENCE-INCOMPLETE (history-open event): {why}"))
        elif o == "EXPIRED": F.append(("EXPIRED", "HISTORY-CONTINUATION", f"EVIDENCE-EXPIRED (history-open event): {why} — no receipt path exists for the history-open event (Q1)"))
        elif o == "FORGED": F.append(("FORGED", "HISTORY-CONTINUATION", f"OPEN-EVENT-FORGED: {why}"))
        elif o == "INCONSISTENT-INPUT": F.append(("LOCAL-TERMINAL", "HISTORY-CONTINUATION", f"OPEN-EVENT-INCONSISTENT-INPUT: {why}"))
        elif o == "NOT-EARLIEST": F.append(("NOT-EARLIEST", "HISTORY-CONTINUATION", f"OPEN-EVENT-NOT-EARLIEST: {why}"))
    else: info["blocked"]["open-delivery-auth"] = "no valid history-open PushEvent object (class-0 finding contributed by S0); the open event's delivery and authentication cannot be evaluated"
    prev = b""; per = []
    for i, c in enumerate(commits):                                                                 # every adjacent relation, no break
        blob = _blob_at(root, c, rel)
        if blob is None: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"HISTORY-DELETED-AT {c[:12]} on the remote ref")); per.append(None); continue
        if i > 0 and (not blob.startswith(prev) or len(blob) <= len(prev)): F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"HISTORY-NOT-AN-EXTENSION at {c[:12]}: the remote's committed blob does not extend the previous one"))
        added = len(_lines(blob)) - len(_lines(prev)); per.append(added)
        if added != 1 and blob.startswith(prev): F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"HISTORY-BATCH-COMMIT at {c[:12]}: {added} entries in one commit; one acknowledged publication per entry is required"))
        prev = blob
    info["entries_per_commit"] = per; info["acknowledged_entries"] = len(_lines(prev))
    if live is None: F.append(("RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION", "EVIDENCE-UNAVAILABLE: the events feed could not be retrieved this invocation — the per-entry publications cannot be checked; retry")); info["blocked"]["per-entry"] = "events feed unavailable"
    else:
        times = {}
        pushes = [e for e in live if isinstance(e, dict) and e.get("type") == "PushEvent" and isinstance(e.get("payload"), dict) and e["payload"].get("ref") == ref]
        for i, c in enumerate(commits):                                                             # every entry, no break
            rc_, parents = _git(root, "rev-list", "--parents", "-n", "1", c); parent = (parents.decode().split() + ["", ""])[1]
            own = [e for e in pushes if e["payload"].get("head") == c and e["payload"].get("before") == parent]
            if own: times[i] = min(str(e.get("created_at")) for e in own); continue
            carried = [e for e in pushes if delivers(e, c, ref, root) and not (e["payload"].get("head") == c and e["payload"].get("before") == parent)]
            if carried: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"HISTORY-PUBLICATION-BATCH: the feed shows history commit {c[:12]} (entry {i}) delivered inside a push that carried other commits ({carried[0].get('id')}; proven by head/commits/before..head ancestry) — not an acknowledged publication of its own; terminal"))
            elif not complete or not live: F.append(("RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION", f"EVIDENCE-UNAVAILABLE: history commit {c[:12]} (entry {i}) has no push event of its own in the {'PARTIAL' if live else 'EMPTY'} retrieved feed — its presence cannot be judged from a partial snapshot; retry"))
            else: F.append(("RETRY-INCOMPLETE", "RETRY-HISTORY-CONTINUATION", f"EVIDENCE-INCOMPLETE: history commit {c[:12]} (entry {i}) has no push event of its own in the retrieved feed and no evidence of batching — retry within the feed window"))
        seq = [times[i] for i in sorted(times)]
        if seq != sorted(seq): F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", "HISTORY-PUBLICATION-ORDER: the server times of the per-entry pushes that were found are not in the recorded order"))
        info["publications"] = len(times); info["publication_times"] = seq
    rc_, local_head = _git(root, "rev-parse", "HEAD"); local_head = local_head.decode().strip(); rc_, unpub = _git(root, "rev-list", f"{head}..{local_head}"); info["local_commits_not_acknowledged"] = unpub.decode().split()
    cur = (Path(root) / rel).read_bytes()
    if cur != prev:
        if cur.startswith(prev): F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"PENDING-PUSH: the working tree extends the acknowledged history by {len(cur) - len(prev)} bytes the remote has not acknowledged; publish and retry — nothing in them governs"))
        else: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", "HISTORY-DIVERGED: the working tree does not extend the history acknowledged by the remote (local reset/rebuild); refuse"))
    elif info["local_commits_not_acknowledged"]: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", "HISTORY-DIVERGED: local commits exist that the remote never acknowledged; refuse until local state equals the published ref"))
    if not F and not info["blocked"]: info["why"] = f"genesis-only open commit {oc[:12]} delivered by an AUTHENTIC open event; one entry per acknowledged commit; working tree equals the live remote head {head[:12]}; {len(commits)} per-entry publications server-timed in order"
    return F, info
def validate_continuation_v12(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info) — the standalone form, sharing the composed path's obligation (v12, codex V31-3): the open event is swept LOCALLY first (type / pinned repository /
    protected ref — a class-0 finding needing no remote), then ONE retrieval (partial pages kept), then the collector; the winner by PRECEDENCE."""
    F = []
    o0, x0 = local_precheck_event(open_event, repo, ref)
    if o0 is not None: F.append(("LOCAL-TERMINAL", "HISTORY-CONTINUATION", f"OPEN-EVENT-INCONSISTENT-INPUT: {x0}"))
    try: live, prov = retrieve_events(repo, runner, per_page=per_page, max_pages=max_pages)
    except EventsUnavailable as e: live, prov = None, {"error": f"{e.kind}: {e.why}"}
    HF, info = history_findings_v12(root, rel, remote_url, ref, open_event if o0 is None else None, live, prov, repo); F += HF
    if expected_head is not None and info.get("remote_head") not in (None, expected_head): F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"STALE-EXPECTED-HEAD: supplied {expected_head[:12]} but the live remote head is {str(info.get('remote_head'))[:12]}"))
    if not F and not info.get("blocked"): return True, info.get("why", "ok"), info
    if not F: F.append(("RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION", "EVIDENCE-UNAVAILABLE: checks blocked: " + "; ".join(f"{k}: {v}" for k, v in info["blocked"].items())))
    w = resolve([finding(c, code, why, "history", i) for i, (c, code, why) in enumerate(F)]); info["findings"] = [{"class": c, "code": code, "why": why} for c, code, why in F]
    return False, w["why"] if w["code"].endswith("HISTORY-CONTINUATION") else f"{w['code']}: {w['why']}", info

def history_findings_v11(root, rel, remote_url, ref, open_event, live, prov, repo):''')
open(p,'w',encoding='utf-8').write(s); print("P v12 edit script ready (not applied)")
