# Hwao continue-overnight direction — 20260705T1615Z

Lane: Hwao/Fable (coordinator).
Inputs: continuation brief; atlas run dir `docs/hwao_overnight_pinning_atlas_20260705T153533Z/`
(checker PASS: 397 evidence rows / 203 sources / 10 ready-to-pin / 200 missing sources, all
HTTP-available); Lana `PASS_WITH_QUEUE`, Goru counts-reconcile PASS, Kun boundary PASS.
`OVERNIGHT_RESULT.md` was missing — now written into the atlas run dir.

## 1. Selected next slice: **Pin wave 2 + spec-only DB packet prep**

Two tracks, both on the mission spine (source positions/pins → ledger hygiene), no UI/runtime
drift:

- **Track A — pin wave 2 (docs-only).** Convert the atlas from map to hardened positions:
  pin claim **2931** now from local texts (`1308.5224v1`, `2605.31052v1`), then fetch the top-3
  missing sources (`2512.16290v1`, `2604.15438`, `2401.12953`) with bounded public HTTP GETs and
  pin **2572, 2942, 2573** where adequacy holds. This directly grows pinned coverage from 3 rows
  toward the 10 ready-to-pin plus the three highest-value fetch targets.
- **Track B — DB ripeness packet prep (spec-only, NOT executable).** Draft precise specs for the
  two mutations the atlas surfaced: the `1308.5224v1` triplicate dedupe and the 2929
  `parent_replaced` evidence-disposition. Specs end at a named future approval gate; nothing
  executable is created tonight.

Deferred: debate-map refresh — it consumes wave-2 pins as input, so it follows, not precedes.

## 2. Lane split (exact deliverables, paths, markers)

New run dirs:
- `docs/hwao_overnight_pinning_wave2_20260705T1615Z/` (Track A)
- `docs/hwao_overnight_db_packet_prep_20260705T1615Z/` (Track B)

- **Tori** — bounded execution + custody. (A) Fetch exactly the 3 target sources via public HTTP
  GET (arXiv), polite spacing, into `pinning_wave2/.../source_text/` with `FETCH_LOG.md` +
  sha256 per file; no other fetches. Run Goru/Kun checker scripts on request. Keep
  `OVERNIGHT_STATUS.md` in the atlas dir current; publish cockpit wording (§5). Approve only
  in-scope prompts; two out-of-scope asks from any lane → stop it and write `BLOCKED_<lane>.md`.
- **Lana** — adequacy gate for every pin before it is written. Deliver
  `LANA_WAVE2_ADEQUACY.md`: per pair (2931×2 local, then 2572/2942/2573 post-fetch) quote
  sufficiency vs claim wording, stance/role verdict. Constraints she set are binding: 2931 pins
  carry `role=neutral_context` verbatim; neutral must never become support; 2929
  `parent_replaced` rows are excluded from pinning and routed to Track B.
- **Goru** — mechanical build. Deliver `PINS_WAVE2.jsonl` (one pin per row: evidence_id,
  claim_id, source, sha256, char offset + line, exact quote, role/stance copied from DB
  read-only state) plus `GORU_WAVE2_COUNTS.md` reconciling atlas counts → wave-2 counts
  (pinned 3 → target ≤10+3).
- **Kun** — reproducibility/boundary. Extend the checker: `pinning_wave2_checker.py` +
  `CHECKER_RESULT.md` (re-locate every quote by offset, recompute hashes, fail on drift), and
  `KUN_WAVE2_BOUNDARY.md` confirming zero SQL/apply/rollback/migration artifacts in both new
  dirs and git limited to read-only status/diff.
- **Hwao** — Track B specs (with Lana review): `DEDUPE_1308_5224v1_TRIPLICATE_SPEC.md` and
  `EVIDENCE_DISPOSITION_2929_PARENT_REPLACED_SPEC.md` in the packet-prep dir, each containing
  exact target rows, before-state expectations, projected after-state, preconditions, and the
  future gate (§3) — plus morning synthesis appended to `OVERNIGHT_RESULT.md` if findings change.

Markers: Track A complete → `PINNING_WAVE2_COMPLETE_20260705T1615Z`; Track B drafts ready →
`DB_PACKET_PREP_DRAFTS_READY_20260705T1615Z`; result doc → `OVERNIGHT_RESULT_PUBLISHED_20260705T1615Z` (already emitted).

## 3. DB ripeness decision (explicit)

- **(a) Read-only verification: YES, continuous.** All lanes may read DB state read-only for
  inventory/adequacy/checker purposes, as in prior lanes.
- **(b) Packet preparation: YES — spec-only, for exactly two candidates.** The `1308.5224v1`
  triplicate dedupe and the 2929 `parent_replaced` evidence-disposition are well-evidenced,
  bounded, and align with the executed 2913/2921 precedent. Tonight produces *specification
  documents only* — no `.sql`, no apply scripts, nothing executable — because the overnight
  grants exclude SQL/apply files intended for execution.
- **(c) Execution-ready: NO — nothing executes tonight.** Reasons: no reviewed packet exists yet
  (specs are being drafted now); packet gates (validator, checksums, drift vs before-state,
  trigger-count 0, lane reviews) cannot be considered passed before the packet exists; and the
  user's "update DB if it's ripen enough" is, per this brief, permission to *evaluate and
  prepare*, not an `APPROVE EXECUTE` phrase. **Exact future gate Tori must require:** a
  supervised morning lane generates the packet from the spec; validator + checksum + drift +
  Lana/Goru/Kun review all PASS; then and only then the user's literal
  `APPROVE EXECUTE <packet_id>` in the operator channel authorizes exactly one run. Until then
  `NO ACTIVE EXECUTION PHRASE` stands.

## 4. Hard stops (restated + slice-specific)

Brief-wide: no DB writes; no trust recompute execution; no SQL/apply/rollback execution; no
migrations; no prose/wiki/page_versions publish or ingest; no deploy/restart/service/config/queue
changes; no git commit/push/merge/rebase/reset/cleanup; no secrets/billing/provider/GCP changes;
no unattended Gemini web/app; out-of-scope twice → stop lane + BLOCKED note.

Slice-specific: fetch cap = exactly the 3 named sources (no crawl of the other 197); every pin
requires Lana adequacy PASS first; role/stance copied verbatim, neutral→support forbidden; 2929
`parent_replaced` rows never enter the pin ledger; any checker drift or contradiction with a
verified marker → `DIVERGENCE_REPORT.md`, freeze that item, continue unaffected work; packet-prep
dir must contain zero executable artifacts (Kun verifies).

## 5. Cockpit/status wording for Tori

> Night shift, part 2: the source map is done, so we're now pinning the claims we already have
> full text for (starting with claim 2931), fetching three more papers over public HTTP to pin
> three more claims, and writing NOT-executable specs for two small database cleanups the map
> surfaced (a duplicate evidence row and a leftover 2929 disposition). Nothing in the database,
> wiki, git, or services is being changed tonight. The two cleanup specs will be waiting for your
> explicit approval phrase in the morning. Active execution phrase: NONE.

## 6. Post-`/new` reset continuity

Unchanged from the 153533Z direction: resume order is brief → this direction →
`OVERNIGHT_STATUS.md` → newest artifacts in the two run dirs. All steps deterministic/idempotent;
re-running fetch (same URLs, sha256-checked) and checkers is safe; no active phrases exist to
strand. Wave-2 pin work resumes at the first pair without a Lana adequacy PASS + pin row.

## 7. Marker

HWAO_CONTINUE_OVERNIGHT_DIRECTION_20260705T1615Z
