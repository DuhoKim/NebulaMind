# Hwao-director progress — evidence links + trust leveling supervision

Order marker: AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Role: Hwao-director — SUPERVISOR + final no-apply packet owner (NOT solo content author; candidate authoring is method-lane work). Snapshot 2026-07-08 ~01:47Z (10:47 KST).
Class: bounded docs/static, additive, no-apply. Hard gates closed.

## Coordination model
Method Hwao controllers author their `evidence-trust-rebuild/` candidate (page content + preview + manifest + validation receipt) or an explicit hard-blocked method receipt, plus a Goru mechanical check; autopilot `--auto-approve-safe` + Tori handle safe prompts/keystrokes. This director sets honest bindability guidance (below), keeps Goru busy, independently verifies, and writes the final no-apply packet. No keystrokes into panes; no candidate authoring by director.

## No-invent bar (binding on every lane)
Use ONLY existing local ledgers, claim markers, accepted/limited/rejected/excluded positions, and present source metadata. Do **not** invent cite IDs, claim IDs, source IDs, DOI/ADS links, or trust levels. Where binding isn't locally available, mark it **unbound/unmatched** and name the missing gate/data. Static-safe only: no live API, `<script>`, fetch/XHR/WebSocket, or product DB routes.

## Per-method bindability (director assessment from existing local ledgers)

### M2 source-first — STRONGLY BINDABLE (real local evidence + trust)
- Source: `method2/lana/LANA_SFA_SOURCE_ADJUDICATION_20260707.md` (RATIFIED WITH NOTES) + `method2/hwao/SOURCE_POSITION_LEDGER_PLAN_20260707.md` + the P1 ledger (36 rows / 13 arXiv groups) + the conversion claim→evidence map (`HWAO_M2_SAME_FORMAT_CONVERSION_ROLE_SPLIT…`).
- Bindable: 6 claim chips {2942–2947} → their accepted/`accepted_limited` evidence rows; **trust leveling is real and must be visibly distinguished — full `accepted` (only 28141, 28095), `accepted_limited`, `rejected` (12 rows), `background_only` (28133), 28/36 `abstract_only_verified` caps.** Evidence links → the local source-adjudication ledger rows / arXiv group IDs.
- Honest constraints (must survive into the candidate): the 7 `cite-unmatched` stay unmatched (28xxx are local source-adjudication rows, not product cite IDs — link to the local ledger row, do not fabricate a product cite); F1 (28133 background-only, no public-sentence use), F2 (28095 review-synthesis attribution), F3 (≤1 support use of 2009.11175 for 2947), F4 (M51 scoping), F5 (abstract-only caps), F6 (2946 model-dependent).

### M1 packet-gated — LIKELY PRODUCT-GATED (mark unbound honestly)
- M1's 30 claims {2905–2923,2925,2926,2929–2936,2946} are baseline/product-page IDs; local `method1/` has no per-claim evidence ledger (only same-format ledgers + `P4_TRUST_LEVEL_ROUTE_CONSISTENCY_GUARD_SPEC`). Their evidence/trust live in the **product wiki DB** (`/api/pages`/trust tables) — a closed hard gate.
- Honest candidate: per-page/section trust framing from whatever local trust data exists, with claim chips explicitly labeled **unbound — evidence resides in product wiki DB (separate gate)**. The M1 lane must confirm local availability; if none, do NOT fabricate — mark unbound and name the DB gate.

### M3 debate-map — DOCS-ONLY / P3-GATED (framing + navigation, no claim binding)
- M3 has 0 claim/cite markers (P2 docs-only). Candidate: plain-English docs-only trust framing (a synthesis, not per-claim-bound) + source navigation to the local debate map / evidence source inventory. **Do NOT pretend P3 claim/citation binding exists.** If stronger binding is wanted, state it needs the P3 gate.

## Plan to final no-apply packet
1. Autopilot dispatches the method lanes (currently idle; watch-ticking). Each produces an `evidence-trust-rebuild/` candidate (M2 fully bound; M1 unbound-honest; M3 docs-only-framing) or a hard-blocked receipt, + a Goru mechanical check (hrefs, evidence-ish hrefs, trust chips, unmatched markers, static-safety, non-empty, old pages preserved).
2. Director independently verifies each candidate honors the no-invent bar + static-safety.
3. Write the final no-apply packet: per-method candidate paths + checksums, what changed, exact mirror/apply steps for the working-repo candidates (and, if a live-root mirror is later wanted, source/target/sha/backup/validation), and STATUS. Expected: `READY_FOR_USER_APPROVAL` for the bindable/honest candidates, with explicit gate notes for M1 full binding (product DB) and M3 P3.

## Safety ledger (this pass)
Read-only inspection + this one progress note. Zero live-root writes; zero product DB/SQL, `/api/pages`, `page_versions`, live-wiki publish, deploy/restart, git, cockpit/global/Baseline/shared-parent, cloud/GCP/OAuth/secrets, browser, cron; zero invented evidence/IDs; zero Method3 P3 binding; zero keystrokes into panes. Hard gates closed.

AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z
