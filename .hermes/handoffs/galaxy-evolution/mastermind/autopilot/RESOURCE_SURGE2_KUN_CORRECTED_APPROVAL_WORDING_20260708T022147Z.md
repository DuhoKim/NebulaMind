# Corrected approval wording — evidence/trust mirror

Marker: RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z_SECOND_WAVE

Status: PASS

## Sources Read

- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z_FINAL_NO_APPLY_PACKET.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE_LANA_M2_APPROVAL_WORDING_REVIEW_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE2_GORU_RESTART_VISIBILITY_AUDIT_20260708T022147Z.md`

## Corrected Approval Gate Wording

> Approve a live-root static mirror of the 10 Galaxy Evolution evidence/trust candidate files from the working repo into `NebulaMind-origin-main-live/frontend/public/...`, creating three new `evidence-trust-rebuild/` directories for Method1, Method2, and Method3. This is a file-copy mirror into the live-served static root only. It does not publish to the product wiki, does not call `/api/pages`, does not write `page_versions`, does not touch the product DB/SQL, and does not run git/build/deploy.
>
> Important visibility caveat: because these are new static subdirectories under the running Next `public/` tree, the new URLs may continue to return 404 after the mirror until a separate `:3000` server restart is approved and performed. This approval covers only the static file mirror. Restart remains a separate deploy/restart hard gate unless explicitly approved in the same user instruction.
>
> Method limitations remain visible: Method2 has the strongest local source-first evidence binding. Method1 has real local evidence for only 3 of its 30 claim chips; the other 27 stay marked as unbound/local until the product claim/evidence database is opened under a separate gate. Method3 is docs-only by design: it provides debate-map trust framing and local provenance navigation, not product claim/citation evidence binding. Method3 P3 product claim/citation binding remains a separate future gate.
>
> This mirror is reversible from backup. Product-wiki publication, `/api/pages`, `page_versions`, product DB/SQL, full Method1 binding, Method3 P3 binding, git, build/deploy, and any restart not explicitly approved remain closed.

## Why This Corrects The Prior Wording

- Removes the false "served immediately / no restart" promise.
- States that new directories may still 404 until a separately approved `:3000` restart.
- Separates static mirror approval from deploy/restart approval.
- States the M1 ratio plainly: only 3 of 30 locally evidence-bound.
- States M3 plainly: docs-only trust framing, not product evidence binding.

## Safety Ledger

Read-only review plus this standalone `.hermes` report write only. No edits to the final packet. No writes to `NebulaMind-origin-main-live`; no mirror/copy live action; no restart/deploy; no `/api/pages`, `page_versions`, product DB/SQL, git, browser automation, cloud/OAuth/secrets, or cron.
