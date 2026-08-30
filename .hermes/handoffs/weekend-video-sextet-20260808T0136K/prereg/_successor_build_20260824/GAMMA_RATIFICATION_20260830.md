# γ ENDPOINTS RATIFICATION — 2026-08-30 20:19 KST

**The principal's words, verbatim (direct message to Hwao's session, 2026-08-30 ~20:18 KST):**

> γ range approved as proposed, ±0.25 in 50 steps

**What this fixes.** `PROPOSAL_GAMMA_RANGE.md` (v2, pre-reconciled to AMENDMENT 2) asks the
ratification for ONE number, Γ. That number is now ratified: **Γ = 0.25**. With the committed
step count `n_steps = 50` (`ref/DRAW_MECHANICS_COMMIT_20260830.md`, AMENDMENT 2), everything
else is DERIVED, nothing else was decided tonight because nothing else was open:

- Δγ = 2Γ/n_steps = **0.01 exactly** (canonical decimal arithmetic: Γ·4/100, a digit shift)
- manifest = the 51-point grid γ_j = −0.25 + j·0.01, j ∈ [0, 50], zero-based
- baseline j₀ = 25, manifest value the canonical zero string `0`
- "in 50 steps" in the principal's sentence is the committed STEP COUNT (51 manifest points
  including the baseline) — "approved as proposed" binds the reading to the proposal's own
  Amendment-2 form, so no fresh interpretation is introduced here.

**Status change.** BS-3g's emission preconditions were: γ endpoints (ratification) ·
`gates/replay_harness.py` digest (set when built) · BS-SI schema (written when filled).
**The first is DONE.** The other two stand. BS-6 and the first image byte remain blocked;
γ̂ remains unmeasured; v9 remains frozen at `6a9abbbd…` — this ratification touches none of
them.

**Fold plan (next build, V112 — NOT applied to V111, which is sha-pinned in a live round):**
every draft site that says the endpoints are proposed/awaiting ratification is re-derived to
RATIFIED quoting this record, the superseded phrases quoted dead per the sweep discipline
(new DRAFT-scoped sweep tokens: "await ratification", "awaiting ratification", "the proposed
Γ", "proposed ±0.25"). Known sites: the BS-3g row (§7 table: "what remains open is Γ's
ratification and the harness pin" → the harness pin), the draw-discipline banner ("await
ratification — the one item still open"), the manifest clause ("the proposed Γ"), the grid
sentence ("0.01 at the proposed Γ = 0.25"), the §11 open-item line ("awaiting ratification —
the one item the sitting created"), plus `DECISIONS_FOR_DUHO.md` (updated with this record)
and `PROPOSAL_GAMMA_RANGE.md` (gains a status pointer, body preserved as history).

**Recorded also in the track's human-direction history**
(`.hermes/handoffs/spin-parity-census-20260805T1922K/spin-parity_history.json`, direction #9).

---

**CORRECTION (dated addendum, 2026-08-30 ~21:25 KST — CODEX-V112 F7).** The "Status change"
paragraph above understated BS-3g's remaining preconditions: beside the harness pin and the
BS-SI schema, **THE PINNED EXECUTABLE MAPPING remains open** — mapping A is ruled but exists
as no module, `mapping_id` stays `MAPPING-NOT-PREREGISTERED`, and §11's refusals block BS-6
until the pinned artifact and its verifier contract exist. The ratification itself — Γ =
0.25 — is unaffected; only this record's inventory sentence was incomplete. The draft's
BS-3g row now carries the full inventory.
