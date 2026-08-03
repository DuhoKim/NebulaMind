# Overnight Run Plan — 2026-07-23

**Quartet:** Goru (frontier) · Tori (method) · Lana (safety) · Fable (referee) · synthesized by Hwao.
**Status:** PLAN ONLY — not executed, not approved to run. The overnight run needs Duho's explicit go, and by the safety lane it may not publish/deploy/DB-write without a gate.
**Kun review of the prior implementation:** ACCEPT (see bottom).

---

## 1. Target — what to study (Goru)

**Primary: the reionization photon-budget / Lyman-continuum escape-fraction tension** (frontier Cluster 16, f_esc — a promoted-but-uncovered quantity; none of the live A/B/C drafts touch it).

- **Question:** does the ionizing-photon budget for reionization close with star-forming galaxies alone, or is there a genuine shortfall?
- **Live wiki tension to adjudicate (page 57):** claim 2808 ("Lya-forest transmission implies a larger ionizing budget than SF galaxies alone supply") vs. 2836 (SF galaxies suffice), plus low-trust claims 2770/2771 (faint low-mass galaxies need high f_esc). The wiki itself flags these unresolved (trust ~0.5, one at -0.19).
- **Non-circular contribution:** a budget reconciliation — quantify how much of the claimed shortfall/closure survives once indirect-proxy systematics (which proxy — O32 / Lya-EW / beta-slope — its scatter, and low-z->z>6 calibration transportability) are propagated. A genuinely new number, not a restated SMF/MZR systematics budget.

**Backup (next run, not tonight): early-quiescent quenching-timescale mismatch** (Cluster 40) — is the <500 Myr rapid-quenching timescale (from z~0-2 color-bimodality, wiki 2236/2561) fast enough for JWST's z>3 massive quiescents? Different axis from the TNG SMF draft. Needs more DR legwork (wiki has zero sim-side quenching-timescale claims yet).

---

## 2. Method — how to run it (Tori)

**Hard constraint from the runner code** (tools/lab_runner_worker.py, backend/app/routers/lab_runner.py): native pullers only for SDSS TAP + TNG HDF5 — no live JWST catalog puller exists. So:

1. **Frame as forward-model vs. literature-anchored data**, not a live pull. DR-fetch the f_esc/SFRD anchor values from cited JWST papers (JADES/CEERS, LzLCS low-z analogs, Simmonds/Chisholm-style calibrations) as fixed inputs with citation keys. Keep model-side and observed-side values in separate arrays so the draft can't blur "prediction" with "measurement."
2. **Forward model** the model-side prediction (f_esc/SFRD/quenched-fraction vs. z) from existing sim outputs to overlay against the anchors.
3. **Grounding, enforced before queuing:** lit_context() sets lit_grounded = bool(papers) and hard-fails to False (logged reason) on empty retrieval. Run the DR fetch and confirm papers is non-empty and f_esc-specific (not an SDSS backfill) BEFORE submitting — don't let the worker's grounding call be the first retrieval attempt -> avoids the "not grounded" tag honestly.
4. **Referee loop:** revise_loop() (astrosage-70b, MAX_REVISE=3, parses VERDICT:). Referee prompt must auto-MAJOR any significance / sign-certainty claim lacking an error bar or bootstrap (the exact "~4sigma / sign secure 100%" failure caught before). Log review_loop.md each cycle.
5. **No-apply checkpoints** after every stage (port the Page58 write_checkpoint pattern): post-DR-fetch (papers + grounded bool), post-forward-model (array shapes + summary stats), post-each-referee-cycle (verdict + word count), post-citation-gate, pre-compile. Compile only after all checkpoints exist.
6. **Metallicity-scale reconciliation** only if an abundance axis is touched (f_esc likely doesn't): apply the -0.24 dex Tremonti->PP04 (Te-anchored, via galSpecLine O3N2) offset before overlay and record the applied offset in the checkpoint. The runner currently applies NO offset — do not skip this if abundances enter.

---

## 3. Safety, gates & honesty (Lana)

**Runner MAY autonomously:** write only inside its own run dir (.hermes/handoffs/galaxy-evolution/overnight-<slug>-<ts>/); compile LaTeX; run tools/nm_gates.py (novelty / expected-value / citation-entailment) + the referee; produce draft PDFs + machine-readable receipts; local-Ollama + read-only DB reads; self-checkpoint and self-terminate.

**Runner MAY NOT without an explicit human gate:** production DB write · publish/deploy to the live site · claim/trust mutation · git push/merge · service restart / tunnel config · paid API credits (local Ollama only) · cron-driven browser (TCC-blocked) · macOS System Settings · any write outside its run dir.

**Honesty guardrails:** a visible "NOT VALIDATED — pending human sign-off" stamp on every artifact · no fabricated significance (every sigma/p traces to a logged computation, not an LLM assertion; nm_gates.py evidence-grounded judge mandatory) · log EVERY candidate tried and its verdict, not just successes · explicit uncertainty budget (stat + syst) per headline number.

**Metallicity-scale gate:** any draft mixing calibration scales without an explicit conversion note is blocked from the referee pass, not merely flagged.

**Cadence (no mid-flight approval):** per-phase checkpoint files + one rolling STATUS.json; a human reads it at dawn — no live approval during the run.

**Emergency stop:** a STOP sentinel file in the run dir (checked each phase boundary), or orchestrator kill, or any attempt to act out-of-sandbox / git / deploy / paid-credit / browser. On kill, flush STATUS.json first — never delete evidence.

---

## 4. Referee & publishability bar (Fable)

**Acceptance criteria — a draft must clear ALL (else it's descriptive, not a paper):**
1. Motivation cites the live debate (>=3 primary sources, wiki/lit-grounded).
2. One falsifiable NEW claim — not a z=0 anchor re-derivation.
3. Headline number carries a bootstrap/LOO CI that excludes the null (not 16-84 scatter dressed as an error bar).
4. Dominant systematic forward-modelled and bounded (a real MC), not footnoted.
5. >=3 published measurements confronted on one common scale (Te-anchored metallicity, same IMF/aperture).
6. Small-N / Poisson / cosmic-variance flagged with the actual N.
7. The limiting systematic is quantified in the SAME sentence as the claim; "not significant" is computed, not asserted.

**Non-circularity test (the failure mode of the 9 rejects):** swap the key assumption (calibration / selection / aperture) for its next-most-defensible alternative — if the claim moves by more than its CI, it's circular. Name the one alternative universe where the sign would flip; if you can't, it isn't stress-tested. Never compare sim-scale vs obs-scale directly — use two-level differencing (sim-vs-sim delta vs obs-vs-obs delta on the DATA scale).

**astrosage = router, not a pass:** ACCEPT/MINOR -> human queue · MAJOR -> one revise-and-re-refute (mechanical fix ok; if the fix needs re-deriving the whole result, that's a circularity signal — don't patch prose) · REJECT -> abandon or salvage as an explicit REVIEW/methods piece.

**Tonight's bar:** SUCCESS = >=1 draft at ACCEPT/MINOR with all 7 criteria checked AND genuinely new (not an A/B/C rehash); hardening an existing ACCEPT draft (tighter CI / new sample / resolved caveat) also counts. REJECT-AND-RETRY = MAJOR/REJECT after one cycle, or any non-circularity failure -> log as SHELVE with the named failed criterion. "Compiles + lint-clean + astrosage ACCEPT" alone is NOT success (that produced the 9 rejections).

**Dawn checklist (5-minute triage):**
1. Open STATUS.json — how many drafts, what verdicts?
2. Each ACCEPT/MINOR: read the abstract's LAST sentence — bounded claim + number + CI, or unbounded "evidence for X"? Unbounded = fail on sight.
3. Grep "systematic" — dominant one quantified in the SAME paragraph as the headline? Relegated to a caveats section = fail.
4. Non-circularity litmus — does it name the one alternative-assumption universe where its sign flips? Absent = ask before reading further.
5. Small-N? actual N stated next to the claim?
6. Decide: ACCEPT-to-human-queue / REVISE (one named defect) / SHELVE (name the failed criterion).

---

## Kun review of the prior implementation — ACCEPT

All 7 Kun recommendations + 4 candidates + the live map wiring verified empirically (Kun re-ran the suites/validator himself): branch retired + work preserved (PASS) · hygiene deletion executed, .env retained-untouched (PASS) · status/debate map validator PASS 0 errors, 16/16 + counter-evidence incl. the SF-outflow contradiction (PASS) · Lab IA applied (PASS) · FK use_alter on main #108 (PASS) · tool tests 135 passed, 0 failed, fixes are structural/derive-from-constant/real-import with NO hidden skips/xfails/deletions (PASS) · trust semantics #107 (PASS) · map live #109, data faithful, honestly labeled (PASS). No corner-cutting / overreach / regressions / weakened tests / honesty or safety gaps.

**Non-blocking notes:** (1) the working checkout is detached at #107 (behind main) — a local test run still surfaces the FK SAWarning that's fixed on main; rebase before testing this tree. (2) the trust test writes test_trust_debate_stance_caps.db to repo root (gitignored) instead of a tmp path — a cleanliness nit.
