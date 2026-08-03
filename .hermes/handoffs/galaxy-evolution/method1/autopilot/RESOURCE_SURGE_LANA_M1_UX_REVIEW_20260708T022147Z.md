# Lana — Method1 evidence/trust UX review (read-only, no edits)

Marker: `RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z`
Candidate order marker reviewed: `AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z`
Role/lane: Method1 Lana — science/prose/UX review pressure. Read-only static verification + this report only. No candidate edits.
User concern under review: missing evidence links + trust leveling; is **3/30 evidence-bound + 27 unbound-local** honest and clear enough, and what no-apply fixes to queue before any mirror.

## Exact paths inspected (read-only)
- `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-20260708T014205Z.html`
- `…/evidence-trust-rebuild/evidence-trust-bindings-20260708T014205Z.md.json`
- `…/same-format-rebuild/page-content-20260707T064500Z.md` (prose source, unchanged)
- `…/pgr-current-page-inventory-20260706T130610Z.json` referenced as ledger of record (not re-fetched)
- `.hermes/…/method1/autopilot/AUTOPILOT_M1_EVIDENCE_TRUST_DISPATCH_20260708T014205Z.md`
- `.hermes/…/method1/autopilot/GORU_M1_EVIDENCE_TRUST_CHECK_20260708T014205Z.md`
- `.hermes/…/method1/HWAO_M1_EVIDENCE_TRUST_VERDICT_20260708T014205Z.md`

## Overall verdict: **WARN** — honest, but not yet clear enough to mirror without two label fixes
The candidate is **honest** (no invention — confirmed independently below) and static-safe (Goru: 0 script/fetch/API). It is **not a FAIL**. But as a reader-facing trust surface it has a small number of clarity defects that can *invert* perceived trust and *overstate* evidence breadth. Recommend mirror only after the two P1 fixes; P2/P3 can follow.

## Dimension scorecard
| # | Dimension | Verdict | Note |
|---|---|:---:|---|
| 1 | No invented evidence/cite/trust IDs | **PASS** | Spot-checked bindings JSON vs preview: trust levels (debated/unverified/reported), scores (+0.34/−0.14/+0.45), stances, arxiv URLs all verbatim from ledger. 0 `<!--cite:-->` injected into page.content. |
| 2 | Unbound state disclosed, not hidden | **PASS** | 27 chips explicitly listed in an "Unbound-local" section + summary tile + prose naming the product layer as a closed gate. |
| 3 | Static-safety / no live calls | **PASS** | Confirms Goru: external host = arxiv.org only; no script/fetch/api. |
| 4 | Chip-level trust label for the 27 unbound | **WARN (P1)** | Badge reads `NNNN · provenance`. See §Finding-1 — reads as a *positive* trust label and inverts the hierarchy. |
| 5 | Bound-vs-unbound trust legibility | **WARN (P1)** | The 3 chips that actually have evidence carry the *cautious-sounding* words (debated/unverified/reported) while the 27 evidence-less chips look neutral → reader may infer the evidence-linked claims are the weak ones. See §Finding-2. |
| 6 | 2929 evidence quality/relevance | **WARN (P2)** | 14 rows, all stance `none`, one disagree vote, dominated by an off-topic MW-ISM "Perseus Arm superbubble" paper (×5) + bare-ID rows. Honest but reader-misleading as "14 evidence." See §Finding-3. |
| 7 | Evidence row counts vs distinct papers | **WARN (P2)** | "20 / 14 / 9 evidence" and headline "43 rows" count duplicates. 2931's 20 rows ≈ 9 distinct papers; 2929's 14 ≈ ~8 distinct. Overstates breadth. See §Finding-4. |
| 8 | Link resolvability | **WARN (P3)** | Malformed ledger IDs reproduced verbatim: `arXiv:arXiv:0901.1880` → `https://arxiv.org/abs/arXiv:0901.1880` (will 404); several bare `arXiv:NNNN` titles. See §Finding-5. |
| 9 | Quality-metric readability | **WARN (P3)** | Row quality chips render as unlabeled numbers (`0.13988  0.85`); header says "relevance·rigor·confidence" but values aren't keyed. See §Finding-6. |

## Findings (reader-facing detail)

**Finding-1 (P1) — "provenance" badge inverts perceived trust.** On scan, a reader sees 27 chips tagged `· provenance` and 3 tagged `· debated / · unverified / · reported`. "Provenance" reads as *verified/backed*, so the 27 unsupported chips look *stronger* than the 3 that carry real evidence. This is the opposite of the true state and directly undercuts the "trust leveling" the user asked for. The dashed `t-baseline` styling + legend ("baseline / unbound-local") mitigate for a careful reader, but the inline word does the damage first. **Fix (no-apply):** relabel the unbound badge to a non-endorsing phrase — e.g. `· trust in app` or `· no local evidence` or `· unbound`. Pure label change, no data invented.

**Finding-2 (P1) — bound claims look weaker than unbound.** Consequence of Finding-1 plus the fact that all 3 bound claims happen to be low/mixed-trust states. Add one plain-English line at the chip/section level (not only in the top summary) clarifying that *unbound-local = trust not shown here, not trust-high*, so the reader doesn't read the evidence-linked trio as "the shaky ones."

**Finding-3 (P2) — 2929's evidence is non-committal and partly off-topic.** Claim 2929 (AGN feedback can regulate/quench) binds to 14 rows, every stance `none`, headlined "14 evidence." The set is dominated by "A large, long-lived, slowly-expanding superbubble across the Perseus Arm" (a Milky-Way ISM paper, ×5) and bare-ID rows — low relevance to the AGN-quench claim. This is the same off-topic-citation contamination pattern I flagged in the T3 review (inventory citation seq 1–5). Faithful to the ledger, but a reader clicking "14 evidence" expecting support finds 14 non-committal, partly-unrelated rows — arguably *worse* for trust than showing none. **Fix (no-apply):** add a caution note on the 2929 panel ("evidence is non-committal / mixed relevance; stance = none across all rows"), or demote 2929's headline from an evidence-count boast to a neutral "14 associated rows (none-stance)."

**Finding-4 (P2) — counts overstate breadth via duplicates.** "20 / 14 / 9 evidence rows" and "43 rows bound" count duplicate paper rows (e.g. 2931: `2605.03008` ×3, `2401.12953` ×3, `1308.5224` ×3). **Fix (no-apply):** show distinct-paper count beside row count ("20 rows · 9 distinct papers") — truthful, computable from the local ledger, no invention.

**Finding-5 (P3) — broken/malformed arxiv links reproduced.** `arXiv:arXiv:0901.1880` and similar produce non-resolving hrefs. **Fix (no-apply):** normalize the display id (strip the duplicated `arXiv:` prefix) so the link resolves, or mark such rows "link may not resolve." Normalization of an existing ID is safe; do **not** substitute a different ID.

**Finding-6 (P3) — unlabeled quality numbers.** Key the `relevance·rigor·confidence` chips (e.g. `rel 0.14 · conf 0.85`) so the reader can read them.

## Pre-mirror queue (recommended order)
1. **P1 — relabel the 27 unbound chips** off the word "provenance" (Finding-1). *Blocker for mirror.*
2. **P1 — add chip/section-level "unbound = trust not shown, not trust-high" clarifier** (Finding-2). *Blocker for mirror.*
3. **P2 — 2929 mixed-relevance/none-stance caution** (Finding-3).
4. **P2 — distinct-paper counts beside row counts** (Findings-4).
5. **P3 — normalize/flag malformed arxiv links** (Finding-5).
6. **P3 — label quality-metric chips** (Finding-6).

All six are label/annotation-only, no-apply, and require **no** new evidence, IDs, DB, or API — they operate on data already in the local ledger. None changes the honest 3-bound/27-unbound structure, which is the correct maximal-honest binding in bounded static scope.

## Answer to the user's question
- **Honest?** Yes — the 3/30 + 27-unbound split is truthful and the unbound state is disclosed, not fabricated (PASS on invention/disclosure).
- **Clear enough?** Not yet — the `provenance` badge and duplicate/off-topic evidence counts can mislead a reader into an inverted trust hierarchy. Ship the two P1 label fixes before mirror; P2/P3 improve it further.

## Safety ledger
- Reads: local candidate + ledger + `.hermes` reports only. Writes: this one report.
- DB/SQL 0 · `/api/pages` 0 · page_versions/publish 0 · live-root/NebulaMind-origin-main-live write 0 · candidate edits 0 · deploy/restart 0 · git 0 · browser 0 · cloud/OAuth/secrets 0 · cron 0.
- No hard gate encountered; nothing prompted. `NO ACTIVE EXECUTION PHRASE`.
