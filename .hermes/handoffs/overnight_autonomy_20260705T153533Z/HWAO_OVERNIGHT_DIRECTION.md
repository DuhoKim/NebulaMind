# Hwao overnight direction — 20260705T153533Z

Lane: Hwao/Fable (coordinator). Basis: overnight brief + closed-out state of the 2929 remap,
2929/2942–2947 trust recompute, prose-delta gate (closed), 2913/2921 dispositions (complete),
and 2913/2921 full-text pinning (complete: 6 pins / 3 sources / checker PASS).

## 1. Selected overnight slice and why

**Board-wide full-text pinning atlas v1 — an evidence source-hardening inventory and prioritized
pinning backlog. Docs-only, read-only inputs, deterministic outputs.**

Why this is next:
- The pinning method was just validated end-to-end on 2913/2921 (quotes + sha256 + offsets +
  no-SQL checker, all four lane reviews PASS). The highest-value move is to scale that method from
  3 sources to the whole board while it is fresh — starting with an inventory of where it is needed.
- It sits exactly on the mission spine (papers → claim/status ledger → …): it hardens the
  papers→claims link that every downstream stage (debate map, prose, derived trust) depends on.
- It is the safest possible unattended work: read-only DB queries, local file scans, hashing,
  public HTTP GET checks. No approval phrases, no mutation risk, fully resumable, artifact-first.
- Its output directly generates the next several work packets: adequacy gaps → future
  disposition/wording packets; pinned-quote coverage → prose-readiness; unpinnable claims →
  trust-review candidates. Morning-Duho gets a ranked queue, not just a report.

Alternate considered and deferred: a post-change refresh of the research-status/debate map
(step6-style). Deferred because it is synthesis-heavy and benefits from the pinning atlas as input;
it is the natural slice *after* this one.

## 2. Lane split

- **Tori** — custody + bounded execution. Runs the read-only inventory queries against the DB,
  file-existence/hash scans over `docs/**/source_text/`, and public HTTP GETs (arXiv abs pages)
  for sources lacking local full text. Approves exec-lane permission prompts only inside §4 scope;
  denies and re-steers anything else. Records markers and keeps `OVERNIGHT_STATUS.md` current.
- **Goru** — mechanical counts/maps. Builds the evidence × source × local-full-text coverage
  matrix, reconciles counts against the read-only snapshot method used in the 2913/2921 lane,
  dedups sources cited by multiple claims.
- **Kun** — reproducibility/boundary. Ships `pinning_atlas_checker.py` (recompute hashes, re-run
  inventory deterministically, fail on drift), confirms zero SQL/apply artifacts exist in the run
  dir, writes the boundary report.
- **Lana** — high-reasoning adequacy. Reviews the top ~20 prioritized claim↔source pairs: does the
  locally stored text actually support the claim wording; flags wording-contract risks that should
  become future packets rather than silent pins.
- **Hwao** — this direction; mid-shift synthesis if lanes surface a fork; morning next-move
  recommendation in `OVERNIGHT_RESULT.md`.

## 3. Exact artifact outputs

New docs-only run dir: `docs/hwao_overnight_pinning_atlas_20260705T153533Z/`

1. `evidence_source_inventory.{json,csv}` — every active evidence row: evidence_id, claim_id,
   claim section/trust/rewrite_status, source id, local full-text present (path + sha256),
   snippets present, already-pinned (2913/2921 lane pins counted), pin status.
2. `pinning_backlog_prioritized.{md,json}` — ranked pinning queue with scoring rationale
   (claim trust status, section weight, stance, source availability).
3. `missing_fulltext_sources.md` — sources with no local full text + HTTP GET availability result;
   fetch remains a listed *proposal* for morning, not an overnight action beyond GET checks.
4. `pinning_atlas_checker.py` + `CHECKER_RESULT.md` — Kun's deterministic no-SQL checker and its
   PASS/FAIL output.
5. `LANA_ADEQUACY_TOP20.md` — Lana's adequacy verdicts and gap list.
6. `OVERNIGHT_STATUS.md` (rolling) and `OVERNIGHT_RESULT.md` (final synthesis + recommended next
   packet), both also linked from the handoff dir.

Reference inputs (read-only): `docs/galaxy_2913_2921_readonly_decision_packet_20260704T131018Z/source_text/`,
`.hermes/handoffs/2913_2921_docs_first_20260705T143217Z/full_text_pinning_docs_only/`, and the
snapshot files in that same handoff dir.

## 4. Permission boundaries and hard stops

In scope (Tori may approve): repo/artifact reads; Markdown/JSON/JSONL/CSV/checker writes only under
the run/handoff dirs above; local deterministic read-only/checker scripts, hashing, parsing, static
validation; public HTTP GET verification; read-only `git status/diff/stat`.

Out of scope (deny, no exceptions overnight): DB writes, SQL apply files intended for execution,
migrations, trust recompute execution, rollback; wiki_pages/page_versions/prose publish or product
ingest; deploy/restart/service/config/queue changes; git commit/push/merge/rebase/reset/cleanup;
secrets/account/billing/GCP/API-key/provider-route changes; unattended Gemini web/app operation;
any persistent "always allow" grant beyond this packet.

Hard stops (park for morning, do not self-heal): (a) any checker or inventory result that
contradicts a verified marker (e.g., 2913/2921 pins failing re-verification, trust state diverging
from the recompute record) → write `DIVERGENCE_REPORT.md`, freeze the affected work item, continue
unaffected items; (b) any need to fetch new full texts beyond HTTP GET availability checks;
(c) any lane requesting an out-of-scope action twice → stop that lane.

## 5. Initial cockpit status wording (plain English)

> Overnight shift: building a board-wide map of which claims' evidence is pinned to exact quotes
> in stored source texts and which still needs hardening. Read-only — nothing is being changed in
> the database, wiki, git, or running services. Output is a prioritized pinning backlog and
> checker, queued for your morning review. No approval phrases are active.

## 6. Safe to continue after a Hermes `/new` reset

Everything is artifact-first, so a fresh session resumes from disk, not from chat memory:
- Re-read, in order: this brief → this direction file → `OVERNIGHT_STATUS.md` → newest artifacts
  in `docs/hwao_overnight_pinning_atlas_20260705T153533Z/`.
- All steps are deterministic and idempotent: re-running the inventory or checker on unchanged
  inputs reproduces identical outputs (Kun's checker proves it), so repeating a step after reset is
  safe; half-written artifacts are simply regenerated.
- No execution phrases are active and none may be created overnight, so a reset cannot strand a
  half-approved mutation — there is nothing mutating to strand.
- The locks in §4 are restated in every artifact header Tori writes, so a post-reset session
  inherits the boundaries even before re-reading this file.

## 7. Marker

HWAO_OVERNIGHT_DIRECTION_20260705T153533Z
