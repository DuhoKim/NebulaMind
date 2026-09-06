# -*- coding: utf-8 -*-
def rp(s, old, new, n=1):
    assert s.count(old) >= 1, old[:90]; return s.replace(old, new, n)
p='track2/provenance_designs_v11.py'; s=open(p,encoding='utf-8').read()
s=rp(s,'"""TRACK 2 v10 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V29 review (V29-1, V29-2, V29-3, V29-4) UNDER BLANC\'S ORDER OF 03:20 KST 09-07',
'"""TRACK 2 v11 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V30 review (V30-1 FATAL, V30-2, V30-3, V30-4), still under Blanc\'s order of 03:20 (one order, one\n'
'resolver). WHAT V11 ADDS. (1) A CLASSIFICATION TABLE, explicit and total over the named refusals of load_identity: `classify_refusal(message)` maps a refusal code to its\n'
'PRECEDENCE class (exact codes first, then prefixes) and FLAGS an unknown code instead of placing it silently; `classify_exception(exc)` maps unnormalized exceptions —\n'
'malformed retained input (JSON / key / type / index / attribute / unicode errors) → LOCAL-TERMINAL MALFORMED-RETAINED-INPUT; I/O and subprocess failures → RETRY-UNAVAILABLE\n'
'IO-UNAVAILABLE; a DataIntegrityFail → classify_refusal; anything else → LOCAL-TERMINAL UNEXPECTED-<type>, flagged. Boundaries spelled out: local integrity and retained-\n'
'input mismatches are class 0; retained CRYPTOGRAPHIC validity of the seed record (REDERIVE-<non-retry>, IDENTITY-SEED-NOT-REDERIVED) is class 4 — it is proven from\n'
'retained bytes but by verification, not by shape; REDERIVE-RETRY (too few verifying bodies) is class 5; WITNESS-FETCH-FAILED and VERIFIER-UNAVAILABLE are class 5 (evidence\n'
'or environment unavailable, never a proven contradiction); WITNESS-NOT-PUSHED and APPROVAL-COMMIT-NOT-PUSHED are class 4 (publication findings from fetched evidence);\n'
'PENDING-PUSH and HISTORY-DIVERGED are class 4 BY POLICY — terminal for this invocation, the remedy is publication and a new invocation; a receipt-path refusal\n'
'(EVENT-EXPIRED-RECEIPT-REFUSED) is class 3 BY POLICY regardless of the receipt\'s failure cause — an expired approval without an acceptable substitute is a loss;\n'
'offline\'s IDENTITY-WITNESS-COMMIT-UNDETERMINED is class 5 by cause (offline names it, offline does not retry). (2) `history_findings_v11` — the history stage as a FINDING\n'
'COLLECTOR: remote head, fetch, genesis-only, the open event\'s delivery and authentication, the extension / batch checks over the fetched objects, the per-entry publication\n'
'checks and the working-tree/remote comparison each contribute; none returns before the others are derived (codex V30-3: a published rewrite is HISTORY-NOT-AN-EXTENSION\n'
'even when the open-event retrieval is empty). (3) ONE EVIDENCE SNAPSHOT: the collector takes the feed already retrieved by the driver (`live`, `prov`) and applies it to\n'
'every predicate — open-event authentication, same-id contradictions, per-entry publication — so retrieval order cannot hide an obtained contradiction; the driver retrieves\n'
'once per invocation. (4) `authenticate_event`: EXPIRED (a loss) is evaluated before UNAVAILABLE for an undetermined delivery (codex V30-3). (5) `validate_continuation_v11`\n'
'is the standalone form (retrieve once, collect, resolve). v10 bytes preserved in provenance_designs_v10.py. v10 was — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V29 review (V29-1, V29-2, V29-3, V29-4) UNDER BLANC\'S ORDER OF 03:20 KST 09-07')
old='    if dv == "UNDETERMINED": return "UNAVAILABLE", "the retained event\'s before..head delivery of the approval commit could not be established here (a git object missing locally, a failed or unlaunchable git command) and no same-id contradiction is in the feed — not evidence of anything; retry with the objects fetched (v7, codex V26-2; v8, codex V27-1)"\n'
assert old in s
s=s.replace(old,'    if dv == "UNDETERMINED" and feed_reaches_back_to is not None and str(retained.get("created_at")) < str(feed_reaches_back_to): return "EXPIRED", "the retained event\'s delivery could not be established and the live feed no longer reaches the event\'s time — a loss, which outranks a retry (v11, codex V30-3); only an independent receipt taken inside the window can stand in"\n'+old)
s=rp(s,'def validate_continuation_v10(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):',
'''CLASS_EXACT = {"IDENTITY-SEED-NOT-REDERIVED": "DERIVED-TERMINAL", "REDERIVE-RETRY": "RETRY-UNAVAILABLE", "WITNESS-FETCH-FAILED": "RETRY-UNAVAILABLE", "VERIFIER-UNAVAILABLE": "RETRY-UNAVAILABLE",
               "IO-UNAVAILABLE": "RETRY-UNAVAILABLE", "IDENTITY-WITNESS-COMMIT-UNDETERMINED": "RETRY-UNAVAILABLE", "WITNESS-NOT-PUSHED": "DERIVED-TERMINAL", "APPROVAL-COMMIT-NOT-PUSHED": "DERIVED-TERMINAL",
               "EVENT-FORGED": "FORGED", "OPEN-EVENT-FORGED": "FORGED", "EVENT-NOT-EARLIEST": "NOT-EARLIEST", "OPEN-EVENT-NOT-EARLIEST": "NOT-EARLIEST", "EVIDENCE-EXPIRED": "EXPIRED",
               "EVIDENCE-INCOMPLETE": "RETRY-INCOMPLETE", "RETRY-EVENTS-INCOMPLETE": "RETRY-INCOMPLETE", "EVIDENCE-UNAVAILABLE": "RETRY-UNAVAILABLE", "OPEN-EVENT-INCONSISTENT-INPUT": "LOCAL-TERMINAL",
               "OPEN-NOT-GENESIS-ONLY": "DERIVED-TERMINAL", "PENDING-PUSH": "DERIVED-TERMINAL", "HISTORY-DIVERGED": "DERIVED-TERMINAL", "STALE-EXPECTED-HEAD": "DERIVED-TERMINAL", "HISTORY-NO-COMMITS": "DERIVED-TERMINAL"}
CLASS_PREFIX = (("EVENT-EXPIRED-", "EXPIRED"), ("RETRY-", "RETRY-UNAVAILABLE"), ("REDERIVE-", "DERIVED-TERMINAL"), ("HISTORY-NOT-AN-EXTENSION", "DERIVED-TERMINAL"), ("HISTORY-DELETED-AT", "DERIVED-TERMINAL"),
                ("HISTORY-BATCH-COMMIT", "DERIVED-TERMINAL"), ("HISTORY-PUBLICATION-", "DERIVED-TERMINAL"), ("HISTORY-OPEN-EVENT-", "LOCAL-TERMINAL"), ("IDENTITY-", "LOCAL-TERMINAL"), ("ADOPTION-", "LOCAL-TERMINAL"),
                ("WITNESS-", "LOCAL-TERMINAL"), ("APPROVAL-", "LOCAL-TERMINAL"), ("PROTOCOL-", "LOCAL-TERMINAL"), ("EVENT-", "LOCAL-TERMINAL"), ("NONCE-", "LOCAL-TERMINAL"), ("COLLECTION-", "LOCAL-TERMINAL"),
                ("HISTORY-", "LOCAL-TERMINAL"), ("BEACON-RECORD-", "LOCAL-TERMINAL"), ("MALFORMED-", "LOCAL-TERMINAL"))
def classify_refusal(message):
    """(class, code, why, unclassified). The code is the refusal name up to the first ':' or space; exact codes first, then prefixes; an unknown code is placed LOCAL-TERMINAL
    and FLAGGED (unclassified=True) so a reviewer sees it — never silently placed (v11, codex V30-2/3)."""
    msg = str(message); code = re.split(r"[:\\s]", msg, 1)[0]; why = msg[len(code):].lstrip(": ").strip() or msg
    if code in CLASS_EXACT: return CLASS_EXACT[code], code, why, False
    for pre, cls in CLASS_PREFIX:
        if code.startswith(pre): return cls, code, why, False
    return "LOCAL-TERMINAL", code, why, True
def classify_exception(exc):
    """(class, code, why, unclassified) for any exception a stage body raised: the driver's DataIntegrityFail → classify_refusal; malformed retained input → LOCAL-TERMINAL;
    I/O and subprocess failures → RETRY-UNAVAILABLE; anything else → LOCAL-TERMINAL UNEXPECTED-<type>, flagged."""
    if type(exc).__name__ == "DataIntegrityFail": return classify_refusal(str(exc))
    if isinstance(exc, (json.JSONDecodeError, ValueError, KeyError, TypeError, IndexError, AttributeError, UnicodeError)): return "LOCAL-TERMINAL", "MALFORMED-RETAINED-INPUT", f"{type(exc).__name__}: {exc}"[:300], False
    if isinstance(exc, (OSError, subprocess.SubprocessError)): return "RETRY-UNAVAILABLE", "IO-UNAVAILABLE", f"{type(exc).__name__}: {exc}"[:300], False
    return "LOCAL-TERMINAL", f"UNEXPECTED-{type(exc).__name__}", str(exc)[:300], True
def history_findings_v11(root, rel, remote_url, ref, open_event, live, prov, repo):
    """THE HISTORY STAGE AS A FINDING COLLECTOR (v11, codex V30-3). Returns (findings, info); findings are (class, composed code, why) triples. Uses the ONE evidence
    snapshot (`live`, `prov`) the driver already retrieved — it retrieves nothing itself. Nothing returns before the others are derived, except where a later
    check needs an object the earlier failure shows to be unobtainable (no remote head → nothing on the remote can be examined)."""
    F = []; info = {"remote_url": remote_url, "ref": ref, "asked_utc": utc()}
    head = remote_head(remote_url, ref); info["remote_head"] = head
    if head is None: F.append(("RETRY-UNAVAILABLE", "HISTORY-CONTINUATION", "RETRY-REMOTE-UNAVAILABLE: the remote did not answer ls-remote; nothing on the remote can be examined until it does")); return F, info
    if not _fetch_witness(root, remote_url, ref, head): F.append(("RETRY-UNAVAILABLE", "HISTORY-CONTINUATION", "RETRY-REMOTE-UNAVAILABLE: could not fetch the remote ref's objects")); return F, info
    rc_, out = _git(root, "log", "--reverse", "--format=%H", head, "--", rel); commits = out.decode().split(); info["remote_commits"] = commits
    if rc_ != 0 or not commits: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", "HISTORY-NO-COMMITS on the remote ref")); return F, info
    oc = commits[0]; open_blob = _blob_at(root, oc, rel) or b""
    try:
        import tempfile; tp = Path(tempfile.mkdtemp()) / "open.jsonl"; tp.write_bytes(open_blob); ents = H.validate(tp)
        if len(ents) != 1 or ents[0].get("stage") != "genesis": F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"OPEN-NOT-GENESIS-ONLY: the first history commit {oc[:12]} carries {len(ents)} entries; a history-open commit carries exactly the genesis — a late first publication of a rebuilt history is refused"))
    except ValueError as e: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"OPEN-NOT-GENESIS-ONLY: the first history commit's blob is not a valid genesis ({e})"))
    # the open event against the open commit, on the snapshot
    dv = delivery(open_event, oc, ref, root); info["open_event_delivery"] = dv
    if dv == "NOT-DELIVERED": F.append(("LOCAL-TERMINAL", "HISTORY-CONTINUATION", f"OPEN-EVENT-INCONSISTENT-INPUT: the retained history-open event positively does not deliver the first history commit {oc[:12]}"))
    o, why = authenticate_event(open_event, live, repo, ref, oc, feed_reaches_back_to=(prov or {}).get("oldest_created_at"), root=root); info["open_event"] = o
    if o == "UNAVAILABLE": F.append(("RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION", f"EVIDENCE-UNAVAILABLE (history-open event): {why}"))
    elif o == "INCOMPLETE": F.append(("RETRY-INCOMPLETE", "RETRY-HISTORY-CONTINUATION", f"EVIDENCE-INCOMPLETE (history-open event): {why}"))
    elif o == "EXPIRED": F.append(("EXPIRED", "HISTORY-CONTINUATION", f"EVIDENCE-EXPIRED (history-open event): {why} — no receipt path exists for the history-open event (Q1)"))
    elif o == "FORGED": F.append(("FORGED", "HISTORY-CONTINUATION", f"OPEN-EVENT-FORGED: {why}"))
    elif o == "INCONSISTENT-INPUT": F.append(("LOCAL-TERMINAL", "HISTORY-CONTINUATION", f"OPEN-EVENT-INCONSISTENT-INPUT: {why}"))
    elif o == "NOT-EARLIEST": F.append(("NOT-EARLIEST", "HISTORY-CONTINUATION", f"OPEN-EVENT-NOT-EARLIEST: {why}"))
    # extension / batch over the fetched objects — independent of the feed
    prev = b""; per = []
    for c in commits:
        blob = _blob_at(root, c, rel)
        if blob is None: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"HISTORY-DELETED-AT {c[:12]} on the remote ref")); break
        if not blob.startswith(prev) or (len(blob) <= len(prev) and c != commits[0]): F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"HISTORY-NOT-AN-EXTENSION at {c[:12]}: the remote's committed blob does not extend the previous one")); break
        added = len(_lines(blob)) - len(_lines(prev)); per.append(added)
        if added != 1: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"HISTORY-BATCH-COMMIT at {c[:12]}: {added} entries in one commit; one acknowledged publication per entry is required")); break
        prev = blob
    info["entries_per_commit"] = per; info["acknowledged_entries"] = len(_lines(prev))
    # per-entry publication on the snapshot (v6 predicate)
    if live is None: F.append(("RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION", "EVIDENCE-UNAVAILABLE: the events feed could not be retrieved this invocation — the per-entry publications cannot be checked; retry"))
    elif not live: F.append(("RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION", "EVIDENCE-UNAVAILABLE: the retrieved feed is EMPTY — the per-entry publications cannot be checked; retry"))
    else:
        times = []
        for i, c in enumerate(commits):
            rc_, parents = _git(root, "rev-list", "--parents", "-n", "1", c); parent = (parents.decode().split() + ["", ""])[1]
            pushes = [e for e in live if isinstance(e, dict) and e.get("type") == "PushEvent" and (e.get("payload") or {}).get("ref") == ref]
            own = [e for e in pushes if (e.get("payload") or {}).get("head") == c and (e.get("payload") or {}).get("before") == parent]
            if not own:
                carried = [e for e in pushes if delivers(e, c, ref, root) and not ((e.get("payload") or {}).get("head") == c and (e.get("payload") or {}).get("before") == parent)]
                if carried: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"HISTORY-PUBLICATION-BATCH: the feed shows history commit {c[:12]} (entry {i}) delivered inside a push that carried other commits ({carried[0].get('id')}; proven by head/commits/before..head ancestry) — not an acknowledged publication of its own; terminal"))
                else: F.append(("RETRY-INCOMPLETE", "RETRY-HISTORY-CONTINUATION", f"EVIDENCE-INCOMPLETE: history commit {c[:12]} (entry {i}) has no push event of its own in the retrieved feed and no evidence of batching — retry within the feed window"))
                break
            times.append(min(str(e.get("created_at")) for e in own))
        else:
            if times != sorted(times): F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", "HISTORY-PUBLICATION-ORDER: the server times of the per-entry pushes are not in the recorded order"))
            info["publications"] = len(commits); info["publication_times"] = times
    # the working tree against the acknowledged history — policy: terminal for this invocation, the remedy is publication
    rc_, local_head = _git(root, "rev-parse", "HEAD"); local_head = local_head.decode().strip(); rc_, unpub = _git(root, "rev-list", f"{head}..{local_head}"); info["local_commits_not_acknowledged"] = unpub.decode().split()
    cur = (Path(root) / rel).read_bytes()
    if cur != prev:
        if cur.startswith(prev): F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"PENDING-PUSH: the working tree extends the acknowledged history by {len(cur) - len(prev)} bytes the remote has not acknowledged; publish and retry — nothing in them governs"))
        else: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", "HISTORY-DIVERGED: the working tree does not extend the history acknowledged by the remote (local reset/rebuild); refuse"))
    elif info["local_commits_not_acknowledged"]: F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", "HISTORY-DIVERGED: local commits exist that the remote never acknowledged; refuse until local state equals the published ref"))
    if not F: info["why"] = f"genesis-only open commit {oc[:12]} delivered by an AUTHENTIC open event; one entry per acknowledged commit; working tree equals the live remote head {head[:12]}; {len(commits)} per-entry publications server-timed in order"
    return F, info
def validate_continuation_v11(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info) — the standalone form of the collector: retrieve ONCE, collect every finding, resolve by PRECEDENCE; `why` is the winner's composed name and reason."""
    try: live, prov = retrieve_events(repo, runner, per_page=per_page, max_pages=max_pages)
    except EventsUnavailable as e: live, prov = None, {"error": f"{e.kind}: {e.why}"}
    F, info = history_findings_v11(root, rel, remote_url, ref, open_event, live, prov, repo)
    if expected_head is not None and info.get("remote_head") not in (None, expected_head): F.append(("DERIVED-TERMINAL", "HISTORY-CONTINUATION", f"STALE-EXPECTED-HEAD: supplied {expected_head[:12]} but the live remote head is {str(info.get('remote_head'))[:12]}"))
    if not F: return True, info.get("why", "ok"), info
    w = resolve([finding(c, code, why, "history", i) for i, (c, code, why) in enumerate(F)]); info["findings"] = [{"class": c, "why": why} for c, code, why in F]
    return False, w["why"] if w["code"].endswith("HISTORY-CONTINUATION") else f"{w['code']}: {w['why']}", info

def validate_continuation_v10(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):''')
open(p,'w',encoding='utf-8').write(s); print("P v11 written")
