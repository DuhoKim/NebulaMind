# Lana review — M2 approval-wording clarity / plain-English / M1+M3 limitation transparency

Marker: RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z
Reviewer: Lana (resource-surge copywriting lane, read-only / static)
Written: 2026-07-08 ~02:22Z
Scope: **copywriting review only, no edits.** Read-only static verification of one packet's user-facing
approval wording. No live-root, no `/api/pages`, no DB/SQL, no git, no deploy/restart, no browser, no cron.
Target reviewed: `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z_FINAL_NO_APPLY_PACKET.md`
Question asked: is the user-approval wording clear, plain-English, and does it hide the M1/M3 limitations?

## Verdict: REVISE BEFORE APPROVAL — wording is mostly honest but has one self-contradiction and two understatements

The approval box (packet §"Approval gate wording", line 72) is **partly good**: it explicitly names M1's 27
product-DB-gated chips and M3's P3 binding as "separate gates," lists them again in §"Separate gates," and states
"Reversible." That is more transparent than most gate wording. However it is **not yet safe to put in front of the
user as written**, for the reasons below — one is a factual contradiction with the packet's own later correction.

## Findings, most important first

### F1 — BLOCKER: the approval box promises "served immediately / no restart," which the packet itself later proves false
- Approval box (line 72): *"Static file copy served immediately — **no** build, deploy, restart, git, DB, `/api/pages`, `page_versions`, or product-wiki publish."*
- Correction #2 (lines 96–105), appended later by the Method2 Hwao pane: this "no restart" claim is
  **"empirically false for new subdirectories"** — the three `evidence-trust-rebuild/` dirs are brand-new, so after
  mirroring they **404 on :3000 until the process is restarted**, and restart is its own deploy/restart hard gate.
- The correction explicitly says the approval-gate wording *should* add a restart approval — **but the approval box
  at line 72 was never updated.** A user reading top-to-bottom hits the approval sentence first and would approve
  believing the trust chips + evidence links "become visible on :3000" immediately. They will not; the pages will
  still 404. This is exactly the kind of hidden limitation the review is meant to catch — not an M1/M3 limitation,
  but a visibility limitation buried 25 lines below the approval box.
- Fix direction (for the authoring lane, not applied here): reconcile line 72 with Correction #2 — remove "served
  immediately" and the word "restart" from the "no ..." list, and either (a) state plainly that the files will 404
  until a **separately approved :3000 restart**, or (b) fold the restart into this same approval as a named second
  action. As written the box and its own correction disagree.

### F2 — M1 limitation is understated: "27 product-DB-gated chips" hides that only 3 of 30 are actually bound
- The approval box names "M1's 27 product-DB-gated chips" as a separate gate — technically disclosed. But it never
  states the **magnitude**: per §M1 (line 31), only **3 of 30 claim chips** are evidence-bound; **27 of 30 (90%)
  render as `unbound-local`.** A plain-English reader sees "27 chips remain a separate gate" and can reasonably
  assume M1 is mostly complete with a small remainder — the opposite of reality.
- Plain-English gap: "product-DB-gated" is jargon. A lay approver will not know it means "per-claim evidence only
  resolves inside the closed product claim/evidence database, which this copy does not touch."
- Fix direction: put the ratio in the approval box, e.g. *"M1 shows real evidence for only 3 of its 30 claims; the
  other 27 stay marked 'unbound' until the product evidence database is opened (a separate gate)."*

### F3 — M3 limitation is understated: the box lumps M3 in with "evidence links become visible" but M3 has zero product evidence binding
- Approval box headline treats M1+M2+M3 uniformly: *"so the trust chips + evidence links become visible."* Per §M3
  (line 48), M3 is **docs-only** with **"0 product claim/cite markers by design"** — its trust chips are *framing*
  (debate-map axis statuses), and its "Evidence basis →" links point to a **local provenance ledger, not product
  evidence.** A reader approving "evidence links" for all three would over-trust M3.
- The box does name "M3's P3 claim/citation binding" as a separate gate, so it is not fully hidden — but the headline
  wording implies parity of evidence backing across the three methods that does not exist.
- Fix direction: distinguish in the headline that M3's trust chips are **framing from the debate map, not
  product-verified evidence**, whereas M2 is the only one fully bound to real accepted/rejected source adjudication.

### F4 — plain-English / jargon (minor, cross-cutting)
- The approval box is one dense ~90-word sentence carrying: two repo names, a path fragment, and the terms
  `evidence-trust-rebuild/`, `:3000`, `/api/pages`, `page_versions`, "product-DB-gated," "P3 claim/citation binding."
  These are meaningful to the lanes but not to a non-technical approver.
- Fix direction: lead with one plain sentence of *what the user gets* and *what stays unfinished*, then keep the
  technical exclusion list as a second line for the record.

## What the wording gets RIGHT (keep)
- It does list M1's 27 chips, M3's P3 binding, and any product-wiki publish as **separate, still-closed gates** —
  both inside the approval sentence and in the dedicated §"Separate gates." The limitations are named, not omitted.
- "Reversible" is stated.
- The exclusion list (no git / DB / `/api/pages` / `page_versions` / product-wiki publish) is explicit and matches
  the safety ledger.

## Bottom line for the approver
- The wording does **not maliciously hide** M1/M3 — both limits are named. But it (F2/F3) **understates their scale**
  so the plain-English reader would over-estimate how "done" M1 and M3 are, and (F1) it **overstates the immediate
  benefit** by promising visibility with no restart that the packet's own correction refutes.
- Recommend the wording be revised (by the owning autopilot lane, not this read-only lane) on F1 before it is shown
  to the user, with F2/F3 magnitude/nature added; F4 is polish. STATUS `READY_FOR_USER_APPROVAL` is premature while
  the approval box and Correction #2 contradict each other.

## Lane safety ledger
Read-only static read of one packet + this single `.hermes` report write. Zero live-root writes/copies, zero
`/api/pages`/`page_versions`/DB/SQL, zero git/deploy/restart, zero browser/cron/cloud/OAuth/secrets, zero keystrokes
into panes, zero edits to any M1/M2/M3 candidate or packet file. No blocker encountered.

RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z
