# -*- coding: utf-8 -*-
def rp(s, old, new, n=1):
    assert s.count(old) >= 1, old[:90]; return s.replace(old, new, n)
CL1 = ("Before any retry is returned from load_identity, the implementation checks locally decidable type, repository and protected-ref mismatches in both retained approval and history-open events. This obligation applies before seed re-derivation availability returns, approval-feed availability returns, and history remote-head or fetch availability returns. Delivery checks that require unavailable remote objects remain undetermined; they do not excuse other locally decidable mismatches. In composed mode, deferred approval or open-event delivery must not bypass obtainable same-ID authentication merely because another stage has queued a retry. A retry is emitted only after the applicable higher-priority terminal checks have run. Offline undetermined delivery retains its explicitly named refusal.")
CL2 = ("NOT-EARLIEST requires a strictly earlier qualifying event under the explicitly specified ordering. Equal timestamps alone do not prove that another event is earlier; feed iteration order is not an unstated tie-break.")
# ---------------- provenance_designs_v10
p='track2/provenance_designs_v10.py'; s=open(p,encoding='utf-8').read()
if 'TRACK 2 v10' in s: print('P v10 already written'); s=None
if s is not None:
  s=rp(s,'"""TRACK 2 v9 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V28 review (V28-1, V28-2, V28-3)',
  '"""TRACK 2 v10 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V29 review (V29-1, V29-2, V29-3, V29-4) UNDER BLANC\'S ORDER OF 03:20 KST 09-07\n'
  '(BLANC_ORDER_PRECEDENCE_IS_ONE_PATTERN): V27-1, V27-2, V28-1/2, V29-1 and V29-2 are ONE pattern — a check returning before the rule that governs it — so this\n'
  'version does not add a sixth point fix. THE PRECEDENCE ORDER, STATED ONCE (module constant PRECEDENCE; when two or more verdict classes are simultaneously derivable\n'
  'the higher one wins, top to bottom, no exceptions): 0 LOCAL-TERMINAL — locally decidable refusals needing no external evidence: identity integrity (digests, seals,\n'
  'bindings, schema), retained-event input mismatches (not a PushEvent, wrong pinned repository, wrong protected ref, positive non-delivery), a missing or unreadable\n'
  'retained file; 1 FORGED — an affirmative contradiction in OBTAINED live evidence (same id, or absent + same delivered commit on the pinned ref, different bytes);\n'
  '2 NOT-EARLIEST — an ordering refusal from obtained live evidence (a STRICTLY earlier qualifying event); 3 EXPIRED — a loss (the feed no longer reaches the event);\n'
  '4 DERIVED-TERMINAL — refusals proven from obtained remote or retained evidence (HISTORY-NOT-AN-EXTENSION / DIVERGED / BATCH / OPEN-NOT-GENESIS-ONLY /\n'
  'PUBLICATION-BATCH / PENDING-PUSH, REDERIVE-<non-retry>, IDENTITY-SEED-NOT-REDERIVED); 5 RETRY-UNAVAILABLE — evidence not obtainable now (feed or remote down,\n'
  'undetermined delivery with nothing contradicting, seed re-derivation RETRY); 6 RETRY-INCOMPLETE — absent, nothing contradicts; 7 ACCEPT. ONE PLACE ENFORCES IT:\n'
  '`resolve(findings)` — every evidence stage of the driver\'s composed path (run_configurations_v14.composed_resolver: A local sweep of both retained events; B one\n'
  'retrieval, approval authentication and the open event\'s same-id check; C seed re-derivation; D history continuation) CONTRIBUTES findings and none decides;\n'
  'class-0 findings raised in the driver\'s fixed offline check sequence before the resolver runs are consistent with the order because nothing outranks class 0;\n'
  'within one class the FIXED stage sequence (the contribution index) decides, never retrieval order. EXHIBITED PAIRWISE: track10/test_track10_fail_first.Resolver\n'
  'contributes every co-occurring pair in both orders; track10/exhibit_precedence_pairs.py prints the table; the complete-path pairs codex built are executed in\n'
  'test_track10_fail_first.V29_1_2_CompletePaths. Codex\'s clause texts, verbatim, in force: (1) "' + CL1 + '" (2) "' + CL2 + '"\n'
  '(V29-4) `authenticate_event`: NOT-EARLIEST only when a qualifying event has a STRICTLY earlier created_at than the retained event; equal timestamps are not earlier;\n'
  'feed iteration order is not an unstated tie-break. (V29-3) text only. v9 bytes preserved in provenance_designs_v9.py. v9 was — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V28 review (V28-1, V28-2, V28-3)')
  old_earliest = '''    qualifying = [e for e in live_events if isinstance(e, dict) and e.get("type") == "PushEvent" and delivery(e, commit, branch_ref, root) == "DELIVERED"]
      earliest = min(qualifying, key=lambda e: e["created_at"])
      if canon(earliest) != d: return "NOT-EARLIEST", "an earlier qualifying event exists in the live feed; the retained one is not the earliest (an input inconsistency, not 'different bytes')"
  '''
  assert old_earliest in s
  s=s.replace(old_earliest,'''    qualifying = [e for e in live_events if isinstance(e, dict) and e.get("type") == "PushEvent" and delivery(e, commit, branch_ref, root) == "DELIVERED"]
      earlier = [e for e in qualifying if str(e.get("created_at")) < str(retained.get("created_at"))]                     # v10 (codex V29-4): STRICTLY earlier; equal timestamps are not earlier; feed order is no tie-break
      if earlier: return "NOT-EARLIEST", f"a strictly earlier qualifying event exists in the live feed ({earlier[0].get('id')} at {earlier[0].get('created_at')}); the retained one is not the earliest (an input inconsistency, not 'different bytes')"
  ''')
  s=rp(s,'def validate_continuation_v9(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):',
  '''PRECEDENCE = ("LOCAL-TERMINAL", "FORGED", "NOT-EARLIEST", "EXPIRED", "DERIVED-TERMINAL", "RETRY-UNAVAILABLE", "RETRY-INCOMPLETE", "ACCEPT")   # v10 (Blanc 03:20): stated ONCE; see the header
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

  def validate_continuation_v9(root, rel, remote_url, ref, open_event, runner, repo, expected_head=None, per_page=100, max_pages=3):''')
  open(p,'w',encoding='utf-8').write(s); print("P v10 written")
  # ---------------- run_configurations_v14
  p='fourier_chirality/run_configurations_v14.py'; s=open(p,encoding='utf-8').read()
  s=rp(s,'"""run_configurations_v13 — V29 STAGED CANDIDATE (codex V28-1/2/3): composed mode on provenance_designs_v9 —',
  '"""run_configurations_v14 — V30 STAGED CANDIDATE (codex V29-1/2/3/4; Blanc 03:20: precedence is ONE pattern): composed mode on provenance_designs_v10 — every evidence\n'
  'stage (A local sweep of both retained events, B one retrieval with approval authentication and the open event\'s same-id check, C seed re-derivation, D history\n'
  'continuation) CONTRIBUTES findings to ONE resolver (`composed_resolver` → provenance_designs_v10.resolve) that applies the precedence order stated once in the v10\n'
  'header; no stage decides; the seed re-derivation and the history stage no longer return a retry before the local sweep and the same-id checks have been weighed;\n'
  'the v13 `composed_provenance` (which decided stage by stage) is removed, not retained as dead code. v13 was: V29 STAGED CANDIDATE (codex V28-1/2/3): composed mode on provenance_designs_v9 —')
  s=rp(s,'→ v13 (this; V29: composed on provenance_designs_v9, precheck defers UNDETERMINED to live authentication).','→ v13 (V29: composed on provenance_designs_v9, precheck defers UNDETERMINED to live authentication) → v14 (this; V30: ONE resolver over four contributing stages, provenance_designs_v10).')
  s=rp(s,'v10→v6, v11→v7, v12→v8, v13→v9.]','v10→v6, v11→v7, v12→v8, v13→v9, v14→v10.]')
  old_tail='''        seed, rv = proto.rederive_seed(rp, adopted, ap_bytes)
          if seed != I["seed_hex"] or rv.get("round") != rnd: raise DataIntegrityFail("IDENTITY-SEED-NOT-REDERIVED: the seed does not follow from the retained beacon evidence")
          if proto.verify_split: verify_split_from_catalogue(I, proto)                                  # v6, UNADOPTED: off by default
          if proto.provenance_mode == "composed": composed_provenance(I, proto, w_root, ev, commit, lp)   # v6, UNADOPTED: the track-2 helpers (v9 now) ON THIS CALL PATH (default "offline")
  '''
  assert old_tail in s
  s=s.replace(old_tail,'''        if proto.provenance_mode == "composed": composed_resolver(I, proto, w_root, ev, commit, lp, rp, adopted, ap_bytes, rnd)   # v14 (Blanc 03:20): ONE resolver — seed re-derivation is stage C of it, contributing, not deciding
          else:
              seed, rv = proto.rederive_seed(rp, adopted, ap_bytes)
              if seed != I["seed_hex"] or rv.get("round") != rnd: raise DataIntegrityFail("IDENTITY-SEED-NOT-REDERIVED: the seed does not follow from the retained beacon evidence")
          if proto.verify_split: verify_split_from_catalogue(I, proto)                                  # v6, UNADOPTED: off by default
  ''')
  a=s.index('def composed_provenance(I, proto, w_root, ev, commit, log_path):'); b=s.index('def verify_split_from_catalogue(I, proto):')
  new_fn='''def composed_resolver(I, proto, w_root, ev, commit, log_path, rp, adopted, ap_bytes, rnd):
      """UNADOPTED COMPOSED MODE, v14 — Blanc 03:20 KST 09-07: precedence is ONE pattern (a check returning before the rule that governs it); state the order once,
      enforce it in one place, exhibit it pairwise. Every evidence stage CONTRIBUTES findings and none decides:
      (A) LOCAL SWEEP of both retained events — approval: `local_precheck` (type / pinned repository / positive non-delivery of the approval commit); history-open:
          `local_precheck_event` (type / pinned repository / protected ref); a missing or unreadable open file is a LOCAL-TERMINAL finding;
      (B) ONE RETRIEVAL of the pinned repository's events (production `gh api`; fixtures inject a labelled runner) — the approval event authenticated against it
          (`authenticate_event`: AUTHENTIC / FORGED / NOT-EARLIEST / EXPIRED (receipt path if configured, else EVENT-EXPIRED-NO-RECEIPT-PATH, Q1 Option C) /
          UNAVAILABLE / INCOMPLETE / INCONSISTENT-INPUT) and the open event's same-id contradictions checked against the SAME feed; a failed retrieval is one
          RETRY-UNAVAILABLE finding;
      (C) SEED RE-DERIVATION from the retained beacon record with PRODUCTION's own re-deriver — REDERIVE-RETRY is a RETRY-UNAVAILABLE finding, any other REDERIVE-*
          refusal and a seed mismatch are DERIVED-TERMINAL findings;
      (D) HISTORY CONTINUATION against the LIVE remote (`validate_continuation_v10`: ls-remote on the pinned URL, push-acknowledgement boundary, tri-state open-event
          stage) — classified by `classify_history`.
      Then `provenance_designs_v10.resolve` picks the winner by the PRECEDENCE order; the winner keeps the composed name reviewers know. Every finding is recorded in
      I['_findings'] so a reader sees what else was derivable. On ACCEPT, I['_composed'] carries the approval outcome, the provenance block, the history verdict and the order."""
      P = _P(); runner = proto.events_runner or P.gh_runner; F = []
      def add(cls, code, why, stage): F.append(P.finding(cls, code, why, stage, len(F)))
      # (A) local sweep — nothing external
      o, x = P.local_precheck(ev, proto.events_repo, proto.witness_branch_ref, commit, w_root)
      if o is not None: add("LOCAL-TERMINAL", "EVENT-INCONSISTENT", x, "A-approval")
      try: open_event = json.loads(Path(proto.history_open_event_file).read_text())
      except Exception as e: open_event = None; add("LOCAL-TERMINAL", "HISTORY-OPEN-EVENT-MISSING", f"the retained history-open PushEvent is absent or unreadable ({e!r})", "A-open")
      if open_event is not None:
          o2, x2 = P.local_precheck_event(open_event, proto.events_repo, proto.witness_branch_ref)
          if o2 is not None: add("LOCAL-TERMINAL", "HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT", x2, "A-open")
      # (B) one retrieval — approval authentication + the open event's same-id check against the same feed
      live = prov = None; ev_outcome = None
      try: live, prov = P.retrieve_events(proto.events_repo, runner)
      except P.EventsUnavailable as e: add("RETRY-UNAVAILABLE", "RETRY-EVENTS-UNAVAILABLE", f"{e.kind}: {e.why}", "B-retrieval")
      if live is not None:
          ev_outcome, why = P.authenticate_event(ev, live, proto.events_repo, proto.witness_branch_ref, commit, feed_reaches_back_to=prov.get("oldest_created_at"), root=w_root)
          if ev_outcome == "AUTHENTIC": pass
          elif ev_outcome == "UNAVAILABLE": add("RETRY-UNAVAILABLE", "RETRY-EVENTS-UNAVAILABLE", why, "B-approval")
          elif ev_outcome == "INCOMPLETE": add("RETRY-INCOMPLETE", "RETRY-EVENTS-INCOMPLETE", why, "B-approval")
          elif ev_outcome == "INCONSISTENT-INPUT": add("LOCAL-TERMINAL", "EVENT-INCONSISTENT", why, "B-approval")
          elif ev_outcome == "NOT-EARLIEST": add("NOT-EARLIEST", "EVENT-NOT-EARLIEST", why, "B-approval")
          elif ev_outcome == "EXPIRED":
              if not proto.events_receipt or proto.expected_receipt_origin is None: add("EXPIRED", "EVENT-EXPIRED-NO-RECEIPT-PATH", f"{why}; no independent receipt path is configured (Q1 Option C)", "B-approval")
              else:
                  ok, rwhy = P.verify_events_receipt(proto.events_receipt, w_root, proto.witness_remote_url, proto.witness_branch_ref, ev, proto.expected_receipt_origin)
                  if not ok: add("EXPIRED", "EVENT-EXPIRED-RECEIPT-REFUSED", rwhy, "B-approval")
          else: add("FORGED", "EVENT-FORGED", why, "B-approval")
          if open_event is not None and P.same_id_contradictions(open_event, live): add("FORGED", "HISTORY-CONTINUATION: OPEN-EVENT-FORGED", f"the live feed carries a push with the retained history-open event's id {open_event.get('id')!r} whose canonical bytes DIFFER — an affirmative contradiction, weighed before any retry (v14 stage B)", "B-open")
      # (C) seed re-derivation — contributing, not deciding
      try:
          seed, rv = proto.rederive_seed(rp, adopted, ap_bytes)
          if seed != I["seed_hex"] or rv.get("round") != rnd: add("DERIVED-TERMINAL", "IDENTITY-SEED-NOT-REDERIVED", "the seed does not follow from the retained beacon evidence", "C-seed")
      except DataIntegrityFail as e:
          msg = str(e); code, _, rest = msg.partition(": "); add("RETRY-UNAVAILABLE" if code == "REDERIVE-RETRY" else "DERIVED-TERMINAL", code, rest or msg, "C-seed")
      # (D) history continuation against the live remote
      hwhy = None; info = {}
      if open_event is not None:
          ok, hwhy, info = P.validate_continuation_v10(w_root, Path(log_path).resolve().relative_to(Path(w_root).resolve()).as_posix(), proto.witness_remote_url, proto.witness_branch_ref, open_event, runner, proto.events_repo)
          if not ok: cls, code = P.classify_history(hwhy); add(cls, code, hwhy, "D-history")
      I["_findings"] = [{k: f[k] for k in ("class", "code", "stage")} for f in F]
      if F: w = P.resolve(F); raise DataIntegrityFail(f"{w['code']}: {w['why']}")
      I["_composed"] = {"event": ev_outcome, "events_provenance": prov, "history": hwhy, "remote_head": info.get("remote_head"), "precedence": list(P.PRECEDENCE)}

  '''
  s=s[:a]+new_fn+s[b:]
  s=rp(s,'| "composed" (track-2 v9 helpers on this call path)','| "composed" (track-2 v10 helpers on this call path, ONE resolver)')
  s=rp(s,'(production: provenance_designs_v9.gh_runner;','(production: provenance_designs_v10.gh_runner;')
  s=rp(s,'    """the track-2 helpers (v9), imported lazily','    """the track-2 helpers (v10), imported lazily')
  s=s.replace('import provenance_designs_v9 as P; return P','import provenance_designs_v10 as P; return P'); assert 'import provenance_designs_v10 as P; return P' in s
  for bad in ('composed_provenance(','validate_continuation_v9(','import provenance_designs_v9 as P'): assert bad not in s, bad   # historical 'v13 was … v9' wording stays
  open(p,'w',encoding='utf-8').write(s); print("driver v14 written")
