# Hwao Method1 — evidence/trust candidate verdict

## Verdict: **PASS (candidate ready) — READY_FOR_USER_APPROVAL for M1 mirror**

Order marker: AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Lane: Method1 Hwao. Scope: static evidence-linking + trust-leveling candidate; not live publish.

## What M1 delivered
An additive static candidate under `evidence-trust-rebuild/` that gives the M1 page visible trust leveling and real evidence links, honestly bounded:
- **3 of 30 chips evidence-bound** to real local evidence with per-claim trust: 2931 (debated, 20 rows), 2929 (unverified, 14 rows), 2946 (reported, 9 rows) = 43 evidence rows, each linking to the paper (arxiv) and to the local ledger.
- **Per-page trust summary** (tiles + prose) computed from the real ledger counts.
- **27 chips labeled `unbound-local`** — real provenance chips whose per-claim trust/evidence resolves only in the product claim/evidence layer (a closed gate). Not given fabricated evidence.
- **No invention:** trust levels, evidence, arxiv URLs, votes, quality all copied verbatim from `pgr-current-page-inventory-20260706T130610Z.json`. No `<!--cite:-->` markers injected into page.content (product cite IDs not locally resolvable; inventing forbidden).

## Quality-requirement compliance (order §60–75)
- Trust leveling plain-English + visible (per-page + per-claim chips where markers exist): ✅
- Evidence links useful + static-safe (local ledger + real arxiv; disabled/`unbound-local` labels where unresolved): ✅
- No live API/fetch/script/DB: ✅ (Goru: 0 real script/handler/fetch; external host = arxiv.org only)
- Did not invent evidence/cite/claim/source IDs/DOIs/trust: ✅

## Honest limitation (not a blocker)
Only 3/30 chips have local evidence; full per-claim binding of the other 27 requires the product claim/evidence layer (DB/API) — a **closed gate**. This is disclosed on-page and in the bindings sidecar, not hidden. This is the maximum honest evidence/trust binding achievable in bounded static scope.

## Recommendation
M1 candidate contributes **READY_FOR_USER_APPROVAL** to the final no-apply packet. Applying it to the live root is a static file mirror behind the same (closed) live-root-write gate as the prior repair packet.

## Safety ledger
DB/SQL 0 · /api/pages 0 · page_versions/publish 0 · live-root write 0 · deploy/restart 0 · git 0 · cockpit/shared-parent 0 · cloud/OAuth/secrets 0 · browser 0 · cron 0 · M3 P3 0. Writes: `.hermes` + additive `evidence-trust-rebuild/` static candidate.
