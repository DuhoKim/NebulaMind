# Overnight parallel-papers campaign — 2026-08-03 23:28 KST → hard stop 09:00 KST

> **Status: PLAN — awaiting Duho's gate phrase.** Nothing below launches without it.
> Proposed phrase: **"APPROVE PAPERS OVERNIGHT — LANES PER PLAN; ARTIFACTS ONLY; HARD STOP 09:00 KST."**
> That phrase also constitutes `APPROVE C41 STEP 4` and `APPROVE C41 STEP 5` (Lane A only), per
> the C41 plan's own gate vocabulary. Every other surface stays gated for morning.

## Campaign rules (DESI-campaign culture, adapted)

- **Artifacts only**: all writes confined to lane dirs + engine caches. NO git writes, NO DB, NO
  product/live/wiki surfaces, NO Deep Research, NO /credits, NO new cron/launchd, NO Codex.
- Hard stop 09:00 KST: watchers stand down; unfinished lanes write an honest partial report.
- Append-only campaign ledger: `.hermes/handoffs/papers-overnight-20260803T2328K/LEDGER.md` —
  every lane start/finish/failure with real `date` timestamps (no estimated times).
- Keep-awake: `caffeinate` armed for the full window and **verified via `pmset -g`** before launch
  (the slept-through-overnight lesson).
- A lane that FAILS halts itself and is recorded; it never blocks sibling lanes.
- Morning packet: one summary file linking every artifact + every decision waiting on Duho.

## Lanes

### L-A (flagship) — C41 Steps 4–5: claim ledger + stance verification
**Contingent on Tori's V2 re-check = PASS** (pending at plan time; if FAIL, L-A becomes
"repair round 2" and stops there).
1. **Step 4 — ledger build.** Goru (Antigravity, mechanical): distill the V2 span table
   (16,177 candidates, 180 records) into C41 claim-ledger entries per contract v1 schema
   (enums, links, spans, certainty dimensions), machine-validated by a lane validator script;
   target: honest coverage of the three axes, quality over count. Lana (Claude CLI): no-overclaim
   pass over every entry (modality ≤ span evidence). Deliverables: `C41_LEDGER.jsonl` +
   validation receipt + Lana pass log.
2. **Step 5 — stance verification.** Kun (Kimi K3, verifier ≠ extractor): claim↔source stance
   matrix over the ledger, adversarial, flipping `verification_status` off `pending` — the field
   the AGN pilot showed must never be skipped. Deliverable: `C41_STANCE_MATRIX.jsonl` + refutation
   log.
3. If both land before ~07:00, DO NOT start Step 6 — the map is a Duho-morning stage by design.

### L-B — AGN thread advance: Step 7 wording contract → prose-preview packet
Lana applies the wording contract to the patched AGN map (v1-final) producing the prose-preview
packet (sentence↔ledger bindings, modality-capped), per the roadmap's next AGN stage; Kun
red-teams. Docs-only; the P0 apply gate stays HELD — this produces the packet the gate would act
on, nothing more. Deliverables in a new `agn-step7-prose-preview-*` lane dir.

### L-C — f_esc decision packets for the 3 REVIEW candidates
For each of z=7/8/9: merit-panel scoring (4-member overnight variant — DR seat abstains, recorded
as such) + one Kun adversarial referee pass per candidate (fresh-context, findings-only).
Deliverable: per-candidate decision packet (scores, verdicts, defects found) so the morning
keep/shelve call is one read. No draft edits; candidates judged as-is.

### L-D — overnight_loop second sweep (small)
Queue: z=10 lit-grounding retry (it SHELVED honestly on grounding; one retry with the grounding
path warmed by tonight's 138 fresh C41 fulltexts) + z=6.5 anchor point for the sweep's low-z end.
Same sandbox rules; triage bar unchanged; max 4 runs / 90 minutes.

### L-E — watchdog + ledger + morning packet (Hwao)
Marker-watchers on every lane with the established narrow auto-approvals; campaign LEDGER
append-only; at 08:3x KST compose `MORNING_PACKET.md` (+ optional HTML mirror on the Tailscale
review page) summarizing: what sealed, what failed, every artifact path, and the ordered list of
morning gates (Step 3 seal → Step 6 map, f_esc keep/shelve, AGN prose-preview gate, git-capture
PRs, 14:00 R4 check).

## Seat map (corrected crew map; all subscription-only)

Goru %40 (agy) → L-A Step 4 build. Lana (CLI spawns) → L-A no-overclaim + L-B. Kun %38 (kimi-k3)
→ L-A Step 5 + L-B red-team + L-C referee passes (serialized on his seat, in that order). Tori %39
→ finishes the V2 re-check, then L-A validation receipts verifier. Yui %25 → held in reserve
(her Step-2 lane is done; reserve = wedge-recovery capacity, not idle-tasking). overnight_loop →
L-D. Hwao → L-E.

## Honest risks

- L-A Step 4 is the real unknown: 16k spans → ledger entries is the largest semantic distillation
  the pipeline has attempted; the AGN pilot produced 16 entries from 26 papers. Overnight target
  is honest coverage, not a number; if Goru's build stalls, the lane ships a partial ledger with
  the shortfall stated (shrink-before-quality, again).
- Kun's seat is the bottleneck (three assignments); order is fixed L-A5 → L-B → L-C, and L-C may
  not finish by 09:00 — acceptable, packets ship partial.
- The 3 f_esc candidates are judged without DR; the panel's 5th seat abstention is recorded, not
  papered over.
