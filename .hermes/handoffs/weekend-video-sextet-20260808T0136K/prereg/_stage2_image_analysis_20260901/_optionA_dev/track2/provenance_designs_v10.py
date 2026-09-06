"""TRACK 2 v10 — RECOMMENDED, UNADOPTED designs, repaired after codex's V29 review (V29-1, V29-2, V29-3, V29-4) UNDER BLANC'S ORDER OF 03:20 KST 09-07
(BLANC_ORDER_PRECEDENCE_IS_ONE_PATTERN): V27-1, V27-2, V28-1/2, V29-1 and V29-2 are ONE pattern — a check returning before the rule that governs it — so this
version does not add a sixth point fix. THE PRECEDENCE ORDER, STATED ONCE (module constant PRECEDENCE; when two or more verdict classes are simultaneously derivable
the higher one wins, top to bottom, no exceptions): 0 LOCAL-TERMINAL — locally decidable refusals needing no external evidence: identity integrity (digests, seals,
bindings, schema), retained-event input mismatches (not a PushEvent, wrong pinned repository, wrong protected ref, positive non-delivery), a missing or unreadable
retained file; 1 FORGED — an affirmative contradiction in OBTAINED live evidence (same id, or absent + same delivered commit on the pinned ref, different bytes);
2 NOT-EARLIEST — an ordering refusal from obtained live evidence (a STRICTLY earlier qualifying event); 3 EXPIRED — a loss (the feed no longer reaches the event);
4 DERIVED-TERMINAL — refusals proven from obtained remote or retained evidence (HISTORY-NOT-AN-EXTENSION / DIVERGED / BATCH / OPEN-NOT-GENESIS-ONLY /
PUBLICATION-BATCH / PENDING-PUSH, REDERIVE-<non-retry>, IDENTITY-SEED-NOT-REDERIVED); 5 RETRY-UNAVAILABLE — evidence not obtainable now (feed or remote down,
undetermined delivery with nothing contradicting, seed re-derivation RETRY); 6 RETRY-INCOMPLETE — absent, nothing contradicts; 7 ACCEPT. ONE PLACE ENFORCES IT:
`resolve(findings)` — every evidence stage of the driver's composed path (run_configurations_v14.composed_resolver: A local sweep of both retained events; B one
retrieval, approval authentication and the open event's same-id check; C seed re-derivation; D history continuation) CONTRIBUTES findings and none decides;
class-0 findings raised in the driver's fixed offline check sequence before the resolver runs are consistent with the order because nothing outranks class 0;
within one class the FIXED stage sequence (the contribution index) decides, never retrieval order. EXHIBITED PAIRWISE: track10/test_track10_fail_first.Resolver
contributes every co-occurring pair in both orders; track10/exhibit_precedence_pairs.py prints the table; the complete-path pairs codex built are executed in
test_track10_fail_first.V29_1_2_CompletePaths. Codex's clause texts, verbatim, in force: (1) "Before any retry is returned from load_identity, the implementation checks locally decidable type, repository and protected-ref mismatches in both retained approval and history-open events. This obligation applies before seed re-derivation availability returns, approval-feed availability returns, and history remote-head or fetch availability returns. Delivery checks that require unavailable remote objects remain undetermined; they do not excuse other locally decidable mismatches. In composed mode, deferred approval or open-event delivery must not bypass obtainable same-ID authentication merely because another stage has queued a retry. A retry is emitted only after the applicable higher-priority terminal checks have run. Offline undetermined delivery retains its explicitly named refusal." (2) "NOT-EARLIEST requires a strictly earlier qualifying event under the explicitly specified ordering. Equal timestamps alone do not prove that another event is earlier; feed iteration order is not an unstated tie-break."
(V29-4) `authenticate_event`: NOT-EARLIEST only when a qualifying event has a STRICTLY earlier created_at than the retained event; equal timestamps are not earlier;
feed iteration order is not an unstated tie-break. (V29-3) text only. v9 bytes preserved in provenance_designs_v9.py. v9 was — RECOMMENDED, UNADOPTED designs, repaired after codex's V28 review (V28-1, V28-2, V28-3) — two UNREPAIRED CONTRADICTIONS the lane's own V27-2 repair had
introduced (a tri-state precheck that returned a retry before the precedence rules could run), now repaired on the complete paths; codex's clause text carried verbatim:
(1) "On both the approval and history-open paths, locally decidable retained-event mismatches are terminal before any evidence-unavailability return. In composed mode, unresolved delivery does not bypass live authentication: a same-ID canonical contradiction obtained from the live feed is terminal before an undetermined-delivery retry. Only when no higher-priority inconsistency is established may undetermined delivery or unavailable retrieval return the stage's retry disposition. Offline mode retains its explicitly named undetermined-delivery refusal."
(2) "Same-commit contradiction is scoped to the pinned protected ref and evaluated only when the retained event is absent. If it is present verbatim, distinct qualifying events are resolved by earliest-event ordering; a later event does not invalidate an authentic earliest event. Conflicting same-ID evidence is refused even beside a verbatim copy, without asserting that this alone identifies which producer supplied false evidence."
IMPLEMENTATION: `validate_continuation_v9` — when the retained history-open event's delivery of the open commit is UNDETERMINED, the stage CONSULTS THE FEED through
`authenticate_event_live` (local_precheck first, then retrieval, then same-id contradictions) and returns OPEN-EVENT-INCONSISTENT-INPUT / OPEN-EVENT-FORGED /
OPEN-EVENT-NOT-EARLIEST (terminal) or EVIDENCE-EXPIRED (loss) before it may return EVIDENCE-UNAVAILABLE / EVIDENCE-INCOMPLETE (retry); run_configurations_v13's
witness-commit precheck, in composed mode, DEFERS an UNDETERMINED delivery to composed provenance (the same three steps) instead of raising the retry itself; offline
mode keeps IDENTITY-WITNESS-COMMIT-UNDETERMINED (no feed, no repository pinning there). RULE (iii) RESTATED (V28-3): when the retained event is present verbatim, a later
distinct qualifying push is AUTHENTIC-compatible — a later event does not invalidate an authentic earliest event — and NOT-EARLIEST arises only when an EARLIER qualifying
event exists; the v8 header's shorter phrasing ("another delivering push is an ORDERING question … (NOT-EARLIEST)") is superseded by clause (2). v8 bytes preserved in
provenance_designs_v8.py. v8 was — RECOMMENDED, UNADOPTED designs, repaired after codex's V27 review (V27-1, V27-2, V27-3) — Blanc 02:06 KST 09-07: these were CONTRADICTIONS between
the text and the code, REPAIRED here, never disclosed as limits. (V27-1) PRECEDENCE, stated and tested — the only three rules: (i) LOCALLY DECIDABLE input mismatches
(not a PushEvent; wrong repository; positive non-delivery of the commit) are decided BEFORE any retrieval: `authenticate_event_live` runs `local_precheck` first, so a
failed retrieval can never turn them into a retry; (ii) a SAME-ID contradiction (a live PushEvent carrying the retained event's id with different canonical bytes) needs
no ancestry and is evaluated BEFORE the undetermined-delivery return and BEFORE the verbatim-presence shortcut — FORGED, terminal; (iii) the SAME-COMMIT arm (a live
push on the PINNED PROTECTED REF delivering the same commit with different bytes) is evaluated only when the retained event is ABSENT from the feed — when it is present
verbatim, another delivering push is an ORDERING question decided by the earliest-qualifying rule (NOT-EARLIEST), not a forgery; the arm is scoped to the pinned ref
because `delivery` answers NOT-DELIVERED for any other ref. (V27-2) TRI-STATE THROUGH EVERY STAGE: `delivery` answers UNDETERMINED for a git process-launch exception
(OSError) exactly as for a missing object; `validate_continuation_v8` re-derives the retained history-open event's delivery tri-state for the open commit —
UNDETERMINED is EVIDENCE-UNAVAILABLE (retry), positive non-delivery is OPEN-EVENT-INCONSISTENT-INPUT (terminal) — replacing v3's Boolean OPEN-EVENT-DOES-NOT-DELIVER on
this path; the driver's witness-commit precheck (run_configurations_v12) uses the same tri-state. (V27-3) the docstrings below that describe CURRENT code are corrected;
historical paragraphs are kept verbatim and marked as such. v7 bytes preserved in provenance_designs_v7.py. v7 was — RECOMMENDED, UNADOPTED designs, repaired after codex's V26 review (V26-1, V26-2, V26-3): (V26-1) CONTRADICTION PREDICATE, stated: a
live event is a contradiction of the retained event if it carries the SAME event id, or DELIVERS the same commit (by the tri-state delivery check below),
and its canonical bytes differ — including a difference only in `before` or `head`; such a contradiction is FORGED, terminal; plain absence stays
INCOMPLETE (retry). (V26-2) DELIVERY IS TRI-STATE — `delivery()` returns DELIVERED / NOT-DELIVERED / UNDETERMINED; UNDETERMINED (a git object missing
locally, a failed git command, no repository root for an ancestry claim) is EVIDENCE that could not be established and yields UNAVAILABLE (retry), never
FORGED; a retained event that positively does not deliver the commit, or names the wrong repository/type, is INCONSISTENT-INPUT (an input mismatch, named
as such, not "different bytes"); a verbatim-present event that is not the earliest qualifying one is NOT-EARLIEST. (V26-3) EVIDENCE-EXPIRED is a LOSS,
not a retry, at every stage. v6 bytes preserved in provenance_designs_v6.py. v6 was — RECOMMENDED, UNADOPTED designs, repaired after codex's V25 review (P1, P2): (P1) batch classification uses the SAME delivery evidence as
authentication — a history commit is "carried" if any push event delivers it by `delivers` (head, payload.commits, or before..head ancestry) while not being
its own publication (head ≠ commit or before ≠ parent): HISTORY-PUBLICATION-BATCH, terminal; GitHub's documented PushEvent shape may omit `payload.commits`,
so ancestry counts; absence with no such event is EVIDENCE-INCOMPLETE (retry); (P2) ABSENCE IS NEVER FORGERY: `authenticate_event` returns INCOMPLETE when the
retained event is missing from a non-empty feed that covers its time, and FORGED only on an AFFIRMATIVE contradiction — the feed carries a push delivering the
same commit with different canonical bytes; the open-event stage of the validator maps UNAVAILABLE/INCOMPLETE/EXPIRED to EVIDENCE-* dispositions (retry) [HISTORICAL v6 wording, kept verbatim; corrected in v7 and since: EVIDENCE-EXPIRED is a LOSS, not a retry] and
keeps FORGED for contradiction, so all three retrieval stages use one vocabulary. v5 bytes preserved in provenance_designs_v5.py. v5 was — RECOMMENDED, UNADOPTED designs, repaired after codex's V24 review (N1, N2, N3). THE COVENANT, stated as codex's clause (N1): the validator
authenticates the published append-only history and distinct, ordered publication events; it does not authenticate when the underlying operations occurred,
nor the completeness of unpublished observations or decisions — whether before the genesis was published or between later publications; an unpublished
absence-based CLOSED decision can be removed before its publication; the fixed-round seed is unchanged by any of this, and an authentic LATE approval
event remains disqualifying; stronger decision completeness would require independently retained decision evidence, which is NOT implemented.
(N2) `validate_continuation_v5` dispositions: an EMPTY per-entry retrieval is EVIDENCE-UNAVAILABLE (retry); a history commit with no push event of its own
is HISTORY-PUBLICATION-BATCH only when the feed itself shows that commit delivered inside a multi-commit push (proven), otherwise EVIDENCE-INCOMPLETE
(retry within the feed window — a delayed honest event and a missing one are indistinguishable until the window closes). (N3) `publish_entry` refuses
PUBLISH-UNRELATED-COMMITS when unpublished local commits other than the pending history entry exist — the producer enforces the validator's
exact-parent predicate before pushing. v4 bytes preserved in provenance_designs_v4.py. v4 was — RECOMMENDED, UNADOPTED designs, repaired after codex's V23 review (M1, M2, M3): (M1) PER-ENTRY PUBLICATION IS PROVEN BY THE SERVER —
`validate_continuation_v4` requires, for EVERY remote commit touching the history, a PushEvent in the live feed whose payload delivered exactly that
commit (head == commit, before == the previous history commit), server-timed in the recorded order; four single-entry commits delivered by one late push
have one event and three commits without one → HISTORY-PUBLICATION-BATCH; out-of-order server times → HISTORY-PUBLICATION-ORDER; (M2) `publish_entry`
pushes an EXISTING pending commit instead of committing again, and `reconcile_pending` publishes a single pending entry (or refuses PUBLISH-BATCH) and is
called by the collector and builder BEFORE any operation; outer collector refusal/error entries are published too; (M3) RESIDUAL, stated exactly: work
done BEFORE the genesis was published — attempts, and absence-based terminal decisions (a CLOSED decided because the feed was empty) — is unauthenticated by
any validator; under drand-only such work cannot change the fixed-round seed; an authentic LATE approval event remains disqualifying whatever the
history says; a stronger guarantee would need an independently retained decision anchor, which is NOT staged. v3 bytes preserved in provenance_designs_v3.py.
v3 was — RECOMMENDED, UNADOPTED designs, repaired after codex's V22 review (findings A, B, C, F): (A) the history-open anchor is AUTHENTICATED —
the first remote commit touching the history must carry a GENESIS-ONLY blob and must be delivered by a PushEvent that is itself authenticated in the
live feed (`validate_continuation_v3`); a late first publication of a rebuilt history is refused (OPEN-NOT-GENESIS-ONLY); (B) the PRODUCER BOUNDARY
is built: `publish_entry` commits and pushes exactly ONE new history entry and returns only when `ls-remote` acknowledges it (PUBLISH-BATCH refuses
two unpublished entries; PENDING-PUSH refuses to proceed when the remote does not acknowledge), and the validator requires one entry per acknowledged
commit (HISTORY-BATCH-COMMIT); (C) ONE delivery predicate — `approval_witness_v4.delivers` incl. before..head ancestry — in every mode;
(F) an EMPTY live feed is UNAVAILABLE (no evidence either way), never FORGED. RESIDUAL (v3 wording, superseded by the v4 statement above): attempts made before the genesis was published are undetectable by any validator; under
drand-only they cannot change the seed; the v3 claim that they could not hide a CLOSED witness state was too strong (codex V23 M3) — an absence-based
CLOSED decided before first publication can be erased; only a late approval event stays disqualifying. v2 bytes preserved in provenance_designs_v2.py.
v2 was — RECOMMENDED, UNADOPTED designs for the two provenance boundaries, REPAIRED after codex's probe of 21:00 KST (the v1 history
validator walked LOCAL HEAD and trusted the supplied open commit; it never asked the remote — a protection ASSUMED, not CHECKED) and BUILT out
after Blanc's 21:04 correction (retrieval, pagination, error handling and the expired-event receipt were prose in v1). v1 bytes preserved in
provenance_designs.py. Wired into the production driver (v11) ONLY behind `Protocol.provenance_mode = 'composed'` (default 'offline'); UNADOPTED.

(a) EVENTS — `retrieve_events(repo, runner)` executes the read-only retrieval through a RUNNER (production: `gh api` via subprocess; the tests
    inject a fixture runner, labelled) with PAGINATION (pages until a short/empty page or max_pages) and ERROR HANDLING that names its path:
    EventsUnavailable(kind ∈ RATE-LIMITED | SERVER-ERROR | AUTH | NOT-FOUND | HTTP | MALFORMED | TRANSPORT). `authenticate_event_live` = retrieve,
    then `authenticate_event` (the pure decision — v8 has SEVEN outcomes with the precedence stated in the header: AUTHENTIC | UNAVAILABLE | INCOMPLETE | EXPIRED | FORGED | INCONSISTENT-INPUT | NOT-EARLIEST; EXPIRED = the retained event is older than the
    oldest event the feed still serves). EXPIRED path: `write_events_receipt` (taken INSIDE the window by an independent party — the OPS session —
    naming its origin) and `verify_events_receipt`: the receipt file must be added ONCE by one commit and never touched (like the approval record),
    that commit must be an ancestor of the LIVE remote head (ls-remote, not local refs), its events digest recomputes, its origin equals the
    EXPECTED ORIGIN — the label {actor: ops-witness, session: OPS}, PROPOSED BY THE LANE for the OPS session's receipts, unadopted, not a user
    decision (QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md) — and the retained event is in it verbatim. RESIDUAL TRUST, stated:
    with a single GitHub account the receipt's pusher cannot be distinguished by GitHub from the lane; a lane that REPLACES a receipt is caught
    (RECEIPT-NOT-FIRST); a lane that FORGES the first receipt in the named party's name is NOT caught by this code — it is caught only by OPS's own retained
    copy (outside the code); closing it BY CODE needs an expected-receipt identity the driver can check (a second GitHub identity's PushEvent actor,
    or a key the lane cannot read) — the ONE step only Duho can provide; no per-receipt human confirmation is proposed. Stated, not hidden.
(b) HISTORY — `validate_continuation_v2(root, rel, open_commit, remote_url, ref)`: (1) the CURRENT remote head is obtained INDEPENDENTLY with
    `git ls-remote <pinned url> <ref>` (production: https://github.com/DuhoKim/NebulaMind.git over TLS; the tests use a local bare repository
    with non-fast-forward receives denied, labelled); an operator-supplied `expected_head` that differs from the live head is refused as STALE;
    an unreachable remote is RETRY-REMOTE-UNAVAILABLE, never a pass; (2) the ref is fetched into a private witness ref so its objects are local;
    (3) `open_commit` must be an ancestor of the REMOTE head (HISTORY-OPEN-NOT-PUBLISHED otherwise); (4) the file's commit chain is walked on the
    REMOTE ref's history — first commit = open_commit, every later blob a strict prefix-extension of the previous one (append-only through git
    objects); (5) PUSH-ACKNOWLEDGEMENT BOUNDARY: the acknowledged history is the blob at the remote head; the working tree must EQUAL it — any
    local-only bytes (an uncommitted extension, or a commit the remote never acknowledged) are PENDING-PUSH and nothing in them governs
    acceptance until the push is acknowledged; local commits not on the remote are reported. States: OK | PENDING-PUSH | STALE-EXPECTED-HEAD |
    RETRY-REMOTE-UNAVAILABLE | HISTORY-OPEN-NOT-PUBLISHED | HISTORY-NOT-AN-EXTENSION | HISTORY-DIVERGED.
    COST (corrected — Blanc's summary to Duho said "one push per freeze"): ONE PUSH PER COLLECTOR/BUILDER ATTEMPT, i.e. per history entry; a
    failed push leaves the entry PENDING-PUSH — the builder must retry the push, never rebuild; the driver refuses while PENDING-PUSH stands.
    TRUSTED afterwards: the remote's answer to ls-remote (TLS to github.com for the pinned URL) and server-side branch protection (no force
    push, no deletion); the PushEvent witnessing the open commit (design (a)). NOT trusted: local refs, local HEAD, the file's own chain, the
    operator's clock."""
from __future__ import annotations
import hashlib, json, re, subprocess, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "corpus_identity")); sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "drand_only"))
import history_v2 as H
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def utc(): return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

# ------------------------------------------------------------------ (a) events
class EventsUnavailable(Exception):
    def __init__(self, kind, why): super().__init__(f"{kind}: {why}"); self.kind = kind; self.why = why
def gh_runner(cmd, timeout=60):
    """PRODUCTION runner: `gh api …` via subprocess. Returns (returncode, stdout, stderr)."""
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout); return r.returncode, r.stdout, r.stderr
def retrieve_events(repo, runner=gh_runner, per_page=100, max_pages=3):
    """Read-only retrieval with pagination. Returns (events newest-first, provenance). Every failure mode raises EventsUnavailable(kind)."""
    out = []; prov = {"repo": repo, "endpoints": [], "retrieved_utc": utc(), "per_page": per_page, "pages_fetched": 0, "truncated_by_max_pages": False, "oldest_created_at": None}
    for page in range(1, max_pages + 1):
        ep = f"repos/{repo}/events?per_page={per_page}&page={page}"; prov["endpoints"].append(ep)
        try: rc, so, se = runner(["gh", "api", ep])
        except Exception as e: raise EventsUnavailable("TRANSPORT", repr(e)[:120])
        if rc != 0:
            m = re.search(r"HTTP (\d{3})", se or ""); code = int(m.group(1)) if m else None
            kind = "RATE-LIMITED" if (code == 403 and "rate limit" in (se or "").lower()) or code == 429 else "AUTH" if code == 401 else "NOT-FOUND" if code == 404 else "SERVER-ERROR" if code and code >= 500 else "HTTP"
            raise EventsUnavailable(kind, (se or "").strip()[:160])
        try: body = json.loads(so)
        except Exception as e: raise EventsUnavailable("MALFORMED", "response is not JSON: " + repr(e)[:80])
        if not isinstance(body, list) or not all(isinstance(x, dict) for x in body): raise EventsUnavailable("MALFORMED", "response is not a list of events")
        prov["pages_fetched"] += 1; out.extend(body)
        if len(body) < per_page: break
    else: prov["truncated_by_max_pages"] = True
    times = [str(e.get("created_at")) for e in out if e.get("created_at")]; prov["oldest_created_at"] = min(times) if times else None
    return out, prov
def delivery(e, commit, branch_ref, root=None):
    """TRI-STATE delivery check (v7, codex V26-2; v8: an OSError launching git is UNDETERMINED, codex V27-2): 'DELIVERED' (head == commit, commit in payload.commits, or before..head ancestry ESTABLISHED via git),
    'NOT-DELIVERED' (the event positively does not deliver the commit: wrong type/ref, or ancestry established false), 'UNDETERMINED' (an ancestry claim that
    cannot be decided: no repository root given, a git object missing locally, or a failed git command). Same evidence as approval_witness_v4.delivers,
    but 'cannot establish' is no longer collapsed into 'false'."""
    if not isinstance(e, dict) or e.get("type") != "PushEvent": return "NOT-DELIVERED"
    p = e.get("payload") or {}
    if p.get("ref") != branch_ref: return "NOT-DELIVERED"
    if p.get("head") == commit or any(c.get("sha") == commit for c in p.get("commits", [])): return "DELIVERED"
    before, head = p.get("before"), p.get("head")
    if not (re.fullmatch(r"[0-9a-f]{40}", str(before)) and re.fullmatch(r"[0-9a-f]{40}", str(head)) and re.fullmatch(r"[0-9a-f]{40}", str(commit))): return "NOT-DELIVERED"
    if before == commit: return "NOT-DELIVERED"
    if not root: return "UNDETERMINED"
    try:                                                                                                # v8 (codex V27-2): a git process-launch exception is evidence that could not be established
        for obj in (before, head, commit):
            if subprocess.run(["git", "cat-file", "-e", obj + "^{commit}"], cwd=root, capture_output=True).returncode != 0: return "UNDETERMINED"
        r1 = subprocess.run(["git", "merge-base", "--is-ancestor", before, commit], cwd=root, capture_output=True); r2 = subprocess.run(["git", "merge-base", "--is-ancestor", commit, head], cwd=root, capture_output=True)
    except (OSError, subprocess.SubprocessError): return "UNDETERMINED"
    if r1.returncode not in (0, 1) or r2.returncode not in (0, 1): return "UNDETERMINED"
    return "DELIVERED" if (r1.returncode == 0 and r2.returncode == 0) else "NOT-DELIVERED"
def delivers(e, commit, branch_ref, root=None):
    """Boolean view of `delivery` for callers that only ask 'is it delivered?' (batch classification): UNDETERMINED counts as False here; the callers that
    must distinguish it (authenticate_event) use `delivery` directly."""
    return delivery(e, commit, branch_ref, root) == "DELIVERED"
def local_precheck(retained, repo, branch_ref, commit, root=None):
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
    earlier = [e for e in qualifying if str(e.get("created_at")) < str(retained.get("created_at"))]                     # v10 (codex V29-4): STRICTLY earlier; equal timestamps are not earlier; feed order is no tie-break
    if earlier: return "NOT-EARLIEST", f"a strictly earlier qualifying event exists in the live feed ({earlier[0].get('id')} at {earlier[0].get('created_at')}); the retained one is not the earliest (an input inconsistency, not 'different bytes')"
    return "AUTHENTIC", "retained event present verbatim in the live feed of the pinned repository, earliest qualifying, no same-id contradiction"
def authenticate_event_live(retained, repo, runner, branch_ref, commit, per_page=100, max_pages=3, root=None):
    """(v8, codex V27-1 rule i) decide the locally decidable part FIRST, then retrieve, then decide. (outcome, why, provenance)."""
    o, x = local_precheck(retained, repo, branch_ref, commit, root)
    if o is not None: return o, x, None
    try: live, prov = retrieve_events(repo, runner, per_page=per_page, max_pages=max_pages)
    except EventsUnavailable as e: return "UNAVAILABLE", f"{e.kind}: {e.why}", None
    o, why = authenticate_event(retained, live, repo, branch_ref, commit, feed_reaches_back_to=prov.get("oldest_created_at"), root=root); return o, why, prov

# ------------------------------------------------------------------ (b) v3: producer boundary + authenticated history-open anchor
def _blob_at(root, commit, rel):
    rc_, blob = _git(root, "cat-file", "-p", f"{commit}:{rel}"); return blob if rc_ == 0 else None
def _lines(b): return [l for l in (b or b"").split(b"\n") if l]
def publish_entry(root, rel, remote_url, ref, message):
    """PRODUCER BOUNDARY (v3, codex V22 B): commit and push EXACTLY ONE new history entry; return its commit only when the live remote acknowledges it.
    Two unpublished entries → PUBLISH-BATCH (nothing pushed); no acknowledgment → PENDING-PUSH (the caller must not proceed)."""
    root = Path(root); head = remote_head(remote_url, ref)
    if head is None: raise SystemExit("PENDING-PUSH: the remote did not answer ls-remote; nothing may proceed until it acknowledges")
    _fetch_witness(root, remote_url, ref, head); published = _lines(_blob_at(root, head, rel)); cur = _lines((root / rel).read_bytes())
    if cur[:len(published)] != published: raise SystemExit("HISTORY-DIVERGED: the working tree does not extend the published history; refuse (never rebuild)")
    new = cur[len(published):]
    if len(new) != 1: raise SystemExit(f"PUBLISH-BATCH: {len(new)} unpublished entries; exactly one entry is published per acknowledged commit")
    rc0, lh = _git(root, "rev-parse", "HEAD"); lh = lh.decode().strip(); head_blob = _lines(_blob_at(root, lh, rel) or b"")
    rcu, unpub = _git(root, "rev-list", f"{head}..{lh}"); unpub = unpub.decode().split()
    pending_is_head = head_blob == cur and lh != head and subprocess.run(["git", "merge-base", "--is-ancestor", head, lh], cwd=root, capture_output=True).returncode == 0
    if [c for c in unpub if not (pending_is_head and c == lh)]: raise SystemExit(f"PUBLISH-UNRELATED-COMMITS: {len(unpub)} unpublished local commit(s) would ride along with the history entry and break the exact-parent publication predicate; publish or drop them first (v5, codex V24 N3)")
    if pending_is_head:
        local = lh                                                                                          # v4 (codex V23 M2): the pending entry is already committed at HEAD — push it, do not commit again
    else:
        rc_, _ = _git(root, "add", "--", rel); rc2, _ = _git(root, "commit", "-q", "-m", message)
        if rc_ or rc2: raise SystemExit("PUBLISH-COMMIT-FAILED")
        rc3, local = _git(root, "rev-parse", "HEAD"); local = local.decode().strip()
    _git(root, "push", "-q", remote_url, f"HEAD:{ref}")
    ack = remote_head(remote_url, ref)
    if ack != local: raise SystemExit(f"PENDING-PUSH: the remote head is {str(ack)[:12]}, not the published commit {local[:12]}; retry the push — nothing in this entry governs until acknowledged")
    return local
def reconcile_pending(root, rel, remote_url, ref):
    """v4 (codex V23 M2): BEFORE any collector/builder operation — publish a single pending entry (committed or not) so the remote acknowledges it;
    refuse PUBLISH-BATCH if more than one entry is pending (never rebuild); refuse PENDING-PUSH if the remote does not answer. Returns {'published': n}."""
    root = Path(root); head = remote_head(remote_url, ref)
    if head is None: raise SystemExit("PENDING-PUSH: the remote did not answer ls-remote; nothing may proceed")
    _fetch_witness(root, remote_url, ref, head); published = _lines(_blob_at(root, head, rel)); cur = _lines((root / rel).read_bytes()) if (root / rel).exists() else []
    if not cur or cur == published: return {"published": 0, "remote_head": head}
    if cur[:len(published)] != published: raise SystemExit("HISTORY-DIVERGED: the working tree does not extend the published history; refuse (never rebuild)")
    if len(cur) - len(published) != 1: raise SystemExit(f"PUBLISH-BATCH: {len(cur) - len(published)} unpublished entries pending; cannot reconcile without rebuilding — refuse")
    c = publish_entry(root, rel, remote_url, ref, "history: reconcile pending entry"); return {"published": 1, "commit": c}

PRECEDENCE = ("LOCAL-TERMINAL", "FORGED", "NOT-EARLIEST", "EXPIRED", "DERIVED-TERMINAL", "RETRY-UNAVAILABLE", "RETRY-INCOMPLETE", "ACCEPT")   # v10 (Blanc 03:20): stated ONCE; see the header
def finding(cls, code, why, stage, seq):
    """One contribution to the resolver: a verdict CLASS (from PRECEDENCE), the composed refusal NAME, its reason, the stage that found it and its position in the fixed stage sequence."""
    assert cls in PRECEDENCE, cls; return {"class": cls, "rank": PRECEDENCE.index(cls), "code": code, "why": why, "stage": stage, "seq": seq}
def resolve(findings):
    """THE ONE RESOLVER (Blanc 03:20): the finding of the highest class wins; within a class the fixed stage sequence (seq) decides; retrieval order and list order play no part."""
    return min(findings, key=lambda f: (f["rank"], f["seq"]))
def classify_history(why):
    """Map a validate_continuation refusal to (class, composed name)."""
    if why.startswith("EVIDENCE-UNAVAILABLE"): return "RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION"
    if why.startswith("EVIDENCE-INCOMPLETE"): return "RETRY-INCOMPLETE", "RETRY-HISTORY-CONTINUATION"
    if why.startswith("RETRY-REMOTE-UNAVAILABLE"): return "RETRY-UNAVAILABLE", "HISTORY-CONTINUATION"
    if why.startswith("EVIDENCE-EXPIRED"): return "EXPIRED", "HISTORY-CONTINUATION"
    if why.startswith("OPEN-EVENT-FORGED"): return "FORGED", "HISTORY-CONTINUATION"
    if why.startswith("OPEN-EVENT-INCONSISTENT-INPUT"): return "LOCAL-TERMINAL", "HISTORY-CONTINUATION"
    if why.startswith("OPEN-EVENT-NOT-EARLIEST"): return "NOT-EARLIEST", "HISTORY-CONTINUATION"
    return "DERIVED-TERMINAL", "HISTORY-CONTINUATION"
def local_precheck_event(e, repo, branch_ref):
    """(v10) The locally decidable part for a retained event whose delivered commit is not yet known (the history-open event before the remote is consulted): type, pinned repository, protected ref."""
    if not isinstance(e, dict) or e.get("type") != "PushEvent": return "INCONSISTENT-INPUT", "retained object is not a PushEvent"
    if (e.get("repo") or {}).get("name") != repo: return "INCONSISTENT-INPUT", f"retained event names repository {(e.get('repo') or {}).get('name')!r}, not the pinned {repo!r}"
    if (e.get("payload") or {}).get("ref") != branch_ref: return "INCONSISTENT-INPUT", f"retained event names ref {(e.get('payload') or {}).get('ref')!r}, not the protected {branch_ref!r}"
    return None, None
def validate_continuation_v10(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info). The SAME decision as v9. In v10 this stage is a CONTRIBUTOR: the driver's resolver (run_configurations_v14.composed_resolver) has already swept the
    open event locally and checked its same-id contradictions against the one retrieval, so a refusal returned here is classified by `classify_history` and resolved
    against the other stages' findings — it no longer decides on its own."""
    return validate_continuation_v9(root, rel, remote_url, ref, open_event, runner, repo, expected_head=expected_head, per_page=per_page, max_pages=max_pages)

def validate_continuation_v9(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
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

def validate_continuation_v8(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info). v7 PLUS (codex V27-2): the OPEN-EVENT STAGE IS TRI-STATE. v3's stage decides the open event's delivery of the first history commit with the
    Boolean `delivers` (OPEN-EVENT-DOES-NOT-DELIVER); v8 re-derives the tri-state for that SAME commit (info['remote_commits'][0], after v3's fetch of the remote ref):
    UNDETERMINED → EVIDENCE-UNAVAILABLE (retry; nothing is established), NOT-DELIVERED → OPEN-EVENT-INCONSISTENT-INPUT (positive, terminal). Everything else passes through."""
    ok, why, info = validate_continuation_v7(root, rel, remote_url, ref, open_event, runner, repo, expected_head=expected_head, per_page=per_page, max_pages=max_pages)
    if not ok and why.startswith("OPEN-EVENT-DOES-NOT-DELIVER"):
        oc = (info.get("remote_commits") or [None])[0]; dv = delivery(open_event, oc, ref, root) if oc else "UNDETERMINED"; info["open_event_delivery"] = dv
        if dv == "UNDETERMINED": return False, f"EVIDENCE-UNAVAILABLE: the retained history-open event's delivery of the first history commit {str(oc)[:12]} could not be established here (a git object missing locally, a failed or unlaunchable git command) — not evidence of anything; retry with the objects fetched (v8, codex V27-2)", info
        return False, f"OPEN-EVENT-INCONSISTENT-INPUT: the retained history-open event positively does not deliver the first history commit {str(oc)[:12]} (v8, codex V27-2)", info
    return ok, why, info

def validate_continuation_v7(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info). v6 PLUS (codex V26-1/2/3): the open-event stage maps the v7 outcomes — UNAVAILABLE/INCOMPLETE → EVIDENCE-* (retry), EXPIRED → EVIDENCE-EXPIRED
    (a loss, not a retry), FORGED / INCONSISTENT-INPUT / NOT-EARLIEST → terminal with their own names (passed through unchanged)."""
    return validate_continuation_v6(root, rel, remote_url, ref, open_event, runner, repo, expected_head=expected_head, per_page=per_page, max_pages=max_pages)

def validate_continuation_v6(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info). v5 PLUS (codex V25 P1/P2): batch classification by the shared delivery predicate (ancestry counts, `payload.commits` may be absent);
    the open-event stage reports EVIDENCE-UNAVAILABLE / EVIDENCE-INCOMPLETE (retry) or EVIDENCE-EXPIRED (a loss, not a retry) and OPEN-EVENT-FORGED only on contradiction."""
    ok, why, info = validate_continuation_v3(root, rel, remote_url, ref, open_event, runner, repo, expected_head=expected_head, per_page=per_page, max_pages=max_pages)
    if not ok:
        if why.startswith("OPEN-EVENT-UNAVAILABLE"): return False, "EVIDENCE-UNAVAILABLE (history-open event): " + why.split(":", 1)[-1].strip(), info
        if why.startswith("OPEN-EVENT-INCOMPLETE"): return False, "EVIDENCE-INCOMPLETE (history-open event): " + why.split(":", 1)[-1].strip(), info
        if why.startswith("OPEN-EVENT-EXPIRED"): return False, "EVIDENCE-EXPIRED (history-open event): " + why.split(":", 1)[-1].strip() + " — no receipt path exists for the history-open event (Q1)", info
        return ok, why, info
    try: live, prov = retrieve_events(repo, runner, per_page=per_page, max_pages=max_pages)
    except EventsUnavailable as e: return False, f"EVIDENCE-UNAVAILABLE: {e.kind}: {e.why} — retry; nothing else changes", info
    if not live: return False, "EVIDENCE-UNAVAILABLE: the per-entry retrieval returned an EMPTY feed — no evidence either way; retry", info
    commits = info["remote_commits"]; times = []
    for i, c in enumerate(commits):
        rc_, parents = _git(root, "rev-list", "--parents", "-n", "1", c); parent = (parents.decode().split() + ["", ""])[1]
        pushes = [e for e in live if e.get("type") == "PushEvent" and (e.get("payload") or {}).get("ref") == ref]
        own = [e for e in pushes if (e.get("payload") or {}).get("head") == c and (e.get("payload") or {}).get("before") == parent]
        if not own:
            carried = [e for e in pushes if delivers(e, c, ref, root) and not ((e.get("payload") or {}).get("head") == c and (e.get("payload") or {}).get("before") == parent)]
            if carried: return False, f"HISTORY-PUBLICATION-BATCH: the feed shows history commit {c[:12]} (entry {i}) delivered inside a push that carried other commits ({carried[0].get('id')}; proven by head/commits/before..head ancestry) — not an acknowledged publication of its own; terminal", info
            return False, f"EVIDENCE-INCOMPLETE: history commit {c[:12]} (entry {i}) has no push event of its own in the retrieved feed and no evidence of batching — retry within the feed window; if the window closes without it, the identity cannot be loaded", info
        times.append(min(str(e.get("created_at")) for e in own))
    if times != sorted(times): return False, "HISTORY-PUBLICATION-ORDER: the server times of the per-entry pushes are not in the recorded order", info
    info["publications"] = len(commits); info["publication_times"] = times
    return True, why + f"; {len(commits)} per-entry publications server-timed in order", info

def validate_continuation_v5(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info). v3's checks, then per-commit publication evidence with v5's DISPOSITIONS (codex V24 N2): EVIDENCE-UNAVAILABLE (empty/unavailable
    per-entry retrieval — retry), EVIDENCE-INCOMPLETE (a commit without its own event and no proof of batching — retry within the window),
    HISTORY-PUBLICATION-BATCH (the feed shows the commit delivered inside a multi-commit push — terminal), HISTORY-PUBLICATION-ORDER."""
    ok, why, info = validate_continuation_v3(root, rel, remote_url, ref, open_event, runner, repo, expected_head=expected_head, per_page=per_page, max_pages=max_pages)
    if not ok: return ok, why, info
    try: live, prov = retrieve_events(repo, runner, per_page=per_page, max_pages=max_pages)
    except EventsUnavailable as e: return False, f"EVIDENCE-UNAVAILABLE: {e.kind}: {e.why} — retry; nothing else changes", info
    if not live: return False, "EVIDENCE-UNAVAILABLE: the per-entry retrieval returned an EMPTY feed — no evidence either way; retry", info
    commits = info["remote_commits"]; times = []
    for i, c in enumerate(commits):
        rc_, parents = _git(root, "rev-list", "--parents", "-n", "1", c); parent = (parents.decode().split() + ["", ""])[1]
        pushes = [e for e in live if e.get("type") == "PushEvent" and (e.get("payload") or {}).get("ref") == ref]
        own = [e for e in pushes if (e.get("payload") or {}).get("head") == c and (e.get("payload") or {}).get("before") == parent]
        if not own:
            carried = [e for e in pushes if any(x.get("sha") == c for x in (e.get("payload") or {}).get("commits", [])) and ((e.get("payload") or {}).get("head") != c or (e.get("payload") or {}).get("before") != parent)]
            if carried: return False, f"HISTORY-PUBLICATION-BATCH: the feed shows history commit {c[:12]} (entry {i}) delivered inside a push that carried other commits ({carried[0].get('id')}) — not an acknowledged publication of its own; terminal", info
            return False, f"EVIDENCE-INCOMPLETE: history commit {c[:12]} (entry {i}) has no push event of its own in the retrieved feed and no evidence of batching — retry within the feed window; if the window closes without it, the identity cannot be loaded", info
        times.append(min(str(e.get("created_at")) for e in own))
    if times != sorted(times): return False, "HISTORY-PUBLICATION-ORDER: the server times of the per-entry pushes are not in the recorded order", info
    info["publications"] = len(commits); info["publication_times"] = times
    return True, why + f"; {len(commits)} per-entry publications server-timed in order", info

def validate_continuation_v4(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info). v3's checks PLUS (codex V23 M1): every remote commit touching the history must have its OWN PushEvent in the live feed
    delivering exactly it (head == commit; before == its parent commit), and those events' server times must be in the recorded order.
    One late push delivering several commits is HISTORY-PUBLICATION-BATCH."""
    ok, why, info = validate_continuation_v3(root, rel, remote_url, ref, open_event, runner, repo, expected_head=expected_head, per_page=per_page, max_pages=max_pages)
    if not ok: return ok, why, info
    try: live, prov = retrieve_events(repo, runner, per_page=per_page, max_pages=max_pages)
    except EventsUnavailable as e: return False, f"RETRY-EVENTS-UNAVAILABLE: {e.kind}: {e.why}", info
    commits = info["remote_commits"]; times = []
    for i, c in enumerate(commits):
        rc_, parents = _git(root, "rev-list", "--parents", "-n", "1", c); parent = (parents.decode().split() + ["", ""])[1]
        hits = [e for e in live if e.get("type") == "PushEvent" and (e.get("payload") or {}).get("ref") == ref and (e.get("payload") or {}).get("head") == c and (e.get("payload") or {}).get("before") == parent]
        if not hits: return False, f"HISTORY-PUBLICATION-BATCH: history commit {c[:12]} (entry {i}) has no push event of its own delivering exactly it — it was delivered together with others or never acknowledged on its own", info
        times.append(min(str(e.get("created_at")) for e in hits))
    if times != sorted(times): return False, "HISTORY-PUBLICATION-ORDER: the server times of the per-entry pushes are not in the recorded order", info
    info["publications"] = len(commits); info["publication_times"] = times
    return True, why + f"; {len(commits)} per-entry publications server-timed in order", info

def validate_continuation_v3(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):
    """(ok, why, info). v2's remote-consulted continuation PLUS (codex V22 A/B): the open commit is the first remote commit touching the file, its blob
    is GENESIS-ONLY, it is delivered by `open_event` which is AUTHENTIC in the live feed (same predicate as W3), and every later remote commit adds
    EXACTLY ONE entry (one acknowledged publication per entry)."""
    info = {"remote_url": remote_url, "ref": ref, "asked_utc": utc()}
    head = remote_head(remote_url, ref); info["remote_head"] = head
    if head is None: return False, "RETRY-REMOTE-UNAVAILABLE: the remote did not answer ls-remote; nothing governs until it does", info
    if expected_head is not None and expected_head != head: return False, f"STALE-EXPECTED-HEAD: supplied {expected_head[:12]} but the live remote head is {head[:12]}", info
    if not _fetch_witness(root, remote_url, ref, head): return False, "RETRY-REMOTE-UNAVAILABLE: could not fetch the remote ref's objects", info
    rc_, out = _git(root, "log", "--reverse", "--format=%H", head, "--", rel); commits = out.decode().split(); info["remote_commits"] = commits
    if rc_ != 0 or not commits: return False, "HISTORY-NO-COMMITS on the remote ref", info
    oc = commits[0]; open_blob = _blob_at(root, oc, rel) or b""
    try:
        import tempfile; tp = Path(tempfile.mkdtemp()) / "open.jsonl"; tp.write_bytes(open_blob); ents = H.validate(tp)
    except ValueError as e: return False, f"OPEN-NOT-GENESIS-ONLY: the first history commit's blob is not a valid genesis ({e})", info
    if len(ents) != 1 or ents[0].get("stage") != "genesis": return False, f"OPEN-NOT-GENESIS-ONLY: the first history commit {oc[:12]} carries {len(ents)} entries; a history-open commit carries exactly the genesis — a late first publication of a rebuilt history is refused", info
    if not isinstance(open_event, dict) or not delivers(open_event, oc, ref, root): return False, f"OPEN-EVENT-DOES-NOT-DELIVER: the retained history-open event does not deliver the first history commit {oc[:12]}", info
    o, why, prov = authenticate_event_live(open_event, repo, runner, ref, oc, per_page=per_page, max_pages=max_pages, root=root); info["open_event"] = o; info["open_event_provenance"] = prov
    if o != "AUTHENTIC": return False, f"OPEN-EVENT-{o}: {why}", info
    prev = b""; per = []
    for c in commits:
        blob = _blob_at(root, c, rel)
        if blob is None: return False, f"HISTORY-DELETED-AT {c[:12]} on the remote ref", info
        if not blob.startswith(prev) or (len(blob) <= len(prev) and c != commits[0]): return False, f"HISTORY-NOT-AN-EXTENSION at {c[:12]}: the remote's committed blob does not extend the previous one", info
        added = len(_lines(blob)) - len(_lines(prev)); per.append(added)
        if added != 1: return False, f"HISTORY-BATCH-COMMIT at {c[:12]}: {added} entries in one commit; one acknowledged publication per entry is required", info
        prev = blob
    info["entries_per_commit"] = per; info["acknowledged_entries"] = len(_lines(prev))
    rc_, local_head = _git(root, "rev-parse", "HEAD"); local_head = local_head.decode().strip(); rc_, unpub = _git(root, "rev-list", f"{head}..{local_head}"); info["local_commits_not_acknowledged"] = unpub.decode().split()
    cur = (Path(root) / rel).read_bytes()
    if cur != prev:
        if cur.startswith(prev): return False, f"PENDING-PUSH: the working tree extends the acknowledged history by {len(cur) - len(prev)} bytes the remote has not acknowledged; publish and retry — nothing in them governs", info
        return False, "HISTORY-DIVERGED: the working tree does not extend the history acknowledged by the remote (local reset/rebuild); refuse", info
    if info["local_commits_not_acknowledged"]: return False, "HISTORY-DIVERGED: local commits exist that the remote never acknowledged; refuse until local state equals the published ref", info
    return True, f"genesis-only open commit {oc[:12]} delivered by an AUTHENTIC open event; one entry per acknowledged commit; working tree equals the live remote head {head[:12]}", info
def write_events_receipt(path, events, provenance, origin):
    """The independent receipt (taken by the OPS session inside the window): events verbatim + provenance + origin + digest. Returns the path."""
    body = {"schema": "EVENTS-RECEIPT-1", "origin": origin, "provenance": provenance, "events": events, "events_sha256": hashlib.sha256(json.dumps(events, sort_keys=True, separators=(",", ":")).encode()).hexdigest(), "written_utc": utc()}
    Path(path).write_text(json.dumps(body, sort_keys=True, indent=1) + "\n"); return Path(path)
def _git(root, *a):
    r = subprocess.run(["git", *a], cwd=root, capture_output=True); return r.returncode, r.stdout
def remote_head(remote_url, ref):
    """The CURRENT head of `ref` at `remote_url`, obtained NOW with ls-remote (independent of every local ref). None if unreachable."""
    try: r = subprocess.run(["git", "ls-remote", "--exit-code", remote_url, ref], capture_output=True, text=True, timeout=60)
    except Exception: return None
    if r.returncode != 0: return None
    for l in r.stdout.splitlines():
        sha, name = (l.split("\t") + [""])[:2]
        if name == ref and re.fullmatch(r"[0-9a-f]{40}", sha): return sha
    return None
def _fetch_witness(root, remote_url, ref, head):
    rc, _ = _git(root, "fetch", "-q", remote_url, f"+{ref}:refs/witness/{ref.replace('refs/', '')}")
    return rc == 0 and subprocess.run(["git", "cat-file", "-e", head + "^{commit}"], cwd=root, capture_output=True).returncode == 0
def verify_events_receipt(receipt_path, root, remote_url, ref, retained_event, expected_origin):
    """(ok, why). The receipt must be added once by one commit and never touched; that commit an ancestor of the LIVE remote head; digest recomputes;
    origin equals the expected origin; the retained event is in it verbatim."""
    p = Path(receipt_path)
    try: rec = json.loads(p.read_text())
    except Exception as e: return False, f"RECEIPT-MALFORMED: {e!r}"[:160]
    if not isinstance(rec, dict) or rec.get("schema") != "EVENTS-RECEIPT-1" or not isinstance(rec.get("events"), list): return False, "RECEIPT-MALFORMED: not an EVENTS-RECEIPT-1"
    if hashlib.sha256(json.dumps(rec["events"], sort_keys=True, separators=(",", ":")).encode()).hexdigest() != rec.get("events_sha256"): return False, "RECEIPT-DIGEST: events digest does not recompute"
    origin = rec.get("origin") or {}
    if any(origin.get(k) != v for k, v in (expected_origin or {}).items()): return False, f"RECEIPT-ORIGIN: receipt origin {origin!r} is not the expected {expected_origin!r}"
    if not any(canon(e) == canon(retained_event) for e in rec["events"]): return False, "RECEIPT-EVENT-ABSENT: the retained event is not in the receipt verbatim"
    head = remote_head(remote_url, ref)
    if head is None: return False, "RETRY-REMOTE-UNAVAILABLE: the remote could not be asked for its head"
    if not _fetch_witness(root, remote_url, ref, head): return False, "RETRY-REMOTE-UNAVAILABLE: could not fetch the remote ref"
    rc, top = _git(root, "rev-parse", "--show-toplevel"); rel = p.resolve().relative_to(Path(top.decode().strip()).resolve()).as_posix()
    rc, adds = _git(root, "log", "--all", "--diff-filter=A", "--format=%H", "--", rel); adds = adds.decode().split()
    rc, touches = _git(root, "log", "--all", "--format=%H", "--", rel); touches = touches.decode().split()
    if len(adds) != 1 or touches != adds: return False, f"RECEIPT-NOT-FIRST: the receipt path was added or touched by {len(touches)} commits; the first receipt is final"
    c = adds[0]
    if subprocess.run(["git", "merge-base", "--is-ancestor", c, head], cwd=root, capture_output=True).returncode != 0: return False, f"RECEIPT-NOT-PUBLISHED: commit {c[:12]} is not an ancestor of the live remote head"
    rc, blob = _git(root, "cat-file", "-p", f"{c}:{rel}")
    if rc != 0 or blob != p.read_bytes(): return False, "RECEIPT-MODIFIED: on-disk bytes differ from the committed blob"
    return True, f"receipt added once by {c[:12]} (published at the live remote head {head[:12]}), origin {origin.get('actor')!r}, event present verbatim"

# ------------------------------------------------------------------ (b) history
def validate_continuation_v2(root, rel, open_commit, remote_url, ref, expected_head=None):
    """(ok, why, info). See the module docstring. The remote is ASKED (ls-remote); local refs and local HEAD are never trusted."""
    info = {"remote_url": remote_url, "ref": ref, "asked_utc": utc()}
    head = remote_head(remote_url, ref); info["remote_head"] = head
    if head is None: return False, "RETRY-REMOTE-UNAVAILABLE: the remote did not answer ls-remote; nothing governs until it does", info
    if expected_head is not None and expected_head != head: return False, f"STALE-EXPECTED-HEAD: supplied {expected_head[:12]} but the live remote head is {head[:12]}", info
    if not _fetch_witness(root, remote_url, ref, head): return False, "RETRY-REMOTE-UNAVAILABLE: could not fetch the remote ref's objects", info
    if not re.fullmatch(r"[0-9a-f]{40}", str(open_commit)) or subprocess.run(["git", "merge-base", "--is-ancestor", open_commit, head], cwd=root, capture_output=True).returncode != 0:
        return False, f"HISTORY-OPEN-NOT-PUBLISHED: open commit {str(open_commit)[:12]} is not an ancestor of the live remote head", info
    rc, out = _git(root, "log", "--reverse", "--format=%H", head, "--", rel); commits = out.decode().split(); info["remote_commits"] = commits
    if rc != 0 or not commits: return False, "HISTORY-NO-COMMITS on the remote ref", info
    if commits[0] != open_commit: return False, f"HISTORY-OPEN-COMMIT-MISMATCH: first remote commit touching the file is {commits[0][:12]}, not the open commit", info
    prev = b""
    for c in commits:
        rc, blob = _git(root, "cat-file", "-p", f"{c}:{rel}")
        if rc != 0: return False, f"HISTORY-DELETED-AT {c[:12]} on the remote ref", info
        if not blob.startswith(prev) or (len(blob) <= len(prev) and c != commits[0]): return False, f"HISTORY-NOT-AN-EXTENSION at {c[:12]}: the remote's committed blob does not extend the previous one", info
        prev = blob
    info["acknowledged_entries"] = sum(1 for l in prev.split(b"\n") if l)
    rc, local_head = _git(root, "rev-parse", "HEAD"); local_head = local_head.decode().strip()
    rc, unpub = _git(root, "rev-list", f"{head}..{local_head}"); info["local_commits_not_acknowledged"] = unpub.decode().split()
    cur = (Path(root) / rel).read_bytes()
    if cur != prev:
        if cur.startswith(prev): return False, f"PENDING-PUSH: the working tree extends the acknowledged history by {len(cur) - len(prev)} bytes that the remote has not acknowledged ({len(info['local_commits_not_acknowledged'])} local commits unpublished); push and retry — nothing in them governs", info
        return False, "HISTORY-DIVERGED: the working tree does not extend the history acknowledged by the remote (local reset/rebuild); refuse", info
    if info["local_commits_not_acknowledged"]: return False, "HISTORY-DIVERGED: local commits exist that the remote never acknowledged although the file bytes match; refuse until local state equals the published ref", info
    return True, f"append-only continuation from the published open commit; working tree equals the history acknowledged by the live remote head {head[:12]}", info
