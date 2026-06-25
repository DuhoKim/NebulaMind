# KUN C1+C2 RE-CERT VERDICT — page58 slice-2b SIGN-SUPPRESSED gate

- **Reviewer:** Kun 🔬 (independent exit-gate; implementer must not self-certify)
- **Date:** 2026-06-23 ~16:34 KST (073409Z)
- **Host:** Duhoui-MacStudio.local (NebulaMind local), NM HEAD `4ba9675` (re-checked at write time)
- **Re-open trigger:** the C1+C2 conditions from `KUN_STANCE_EXITGATE_VERDICT_legABC_20260623T0715Z.md`
  (CONDITIONAL → "ship only a sign-suppressed, rdf-only neutral auto-seed, conditioned on C1 + C2").
- **Scored artifacts (hashes RE-VERIFIED, all match the brief):**
  - C2 JSON `sign_suppressed_gate_c2_score_20260623T071214Z.json` sha256 `812ccb98…b596ed` ✓
  - C2 MD   `…071214Z.md` sha256 `e7d17b67…97d5b` ✓
  - Seed plan `sign_suppressed_seed_plan_20260623T071214Z.jsonl` sha256 `2396a2ed…ead5d5` ✓
  - Locked gold `stance_gold_LOCKED_v1.jsonl` sha256 `de7ec421…dbe27` — **unchanged** ✓
- **Containment:** read-only. db_write 0, no Alembic, no page57/58 live write, no stance-lock, paid lane untouched.
  My verification ran stdlib-only python over the locked gold + seed plan (`/tmp`, not the live tree).
  **Kun authorizes NEITHER seed NOR live write.** Live write remains a separate Papa-gated step (out of scope).

---

## 0. INDEPENDENT REPRODUCTION (byte-independent of Tori's scorer)
Recomputed every headline directly from the locked gold; did not trust the scorer's own output.
- Stage-1 related **P 0.9333 / R 0.8909** (tp98 fp7 fn12 tn12; true-related 110) — match. Predicted-related = **105** = the auto-seed target; predicted-unrelated = 24.
- Sign-suppressed Stage-2 on the 110 true-related: predicted rdf 98, rdf TP 76, true-rdf 88 → **rdf P 0.7755 / R 0.8636** — **byte-match** to the C2 artifact.
- The 22 non-rdf truths that collapse INTO rdf = **{supports 21, contradicts 1}** — i.e. the rdf "precision drop" from 1.0→0.7755 is *entirely* true signs deliberately under-labeled to neutral. **That is the intended SAFE-failure mode, not an error** (see C2 below).
- Sentinel `stance2b-001` (true contradicts): auto label rdf, suppressed + queued, trust-neutral. Confirmed.
The re-scored artifact is faithful to the locked gold.

---

## C1 — rdf/stance-"none" auto-seed is genuinely TRUST-NEUTRAL → **CONCUR (verified first-hand, both calculators)**

I did **not** rubber-stamp HwaO's read; I read the live trust code myself at NM HEAD `4ba9675`.

**v2 (the LIVE path).** `app/routers/claims.py` `recalculate_trust()` (L56) is a shim into `recalculate_trust_v2()` (L121); the live `POST /evidence` add path (L434–445) calls it. In v2:
- **E component** (L143–149): `E_sup`/`E_chal` sum quality **only** for `stance=="supports"` / `"challenges"`; explicit code comment L146 *"neutral counts as 0 in the numerator (context only)."* `n_supports`/`n_challenges` count only those two stances.
- No no-evidence penalty to remove: baseline `E = 0.0` (L141), and L206 keeps a no-/neutral-evidence claim at `unverified`. Adding a neutral rdf row leaves E, TS **and** tier unchanged.
- **T** (L168) only reads supports' years; **H** (L177) is human override; neither is touched by a neutral write.

**Phase-1 module** (`app/services/trust_calculator.py`, secondary/older): same stance gate (L34–39, L48–53 count only supports/challenges). Its one interaction — adding *any* evidence row removes the `E=-0.2` no-evidence penalty (L31) — is **tier-preserving** (a neutral-only claim still computes to `unverified`, can't reach `accepted` without real supports ≥ TS 0.30) and is **moot for the live v2 path** (no such penalty there).

**Net C1:** under both calculators, only `stance ∈ {supports, challenges}` moves the E component or the user-facing tier. A seed row written with stance `none` (or even `related_different_facet`) is non-voting. The seed plan honors this exactly (C2 below). **CONCUR.**

**One forward-caveat (NON-BLOCKING for the seed, flag for whoever wires voting):** the v2 **V component** (L151–165) counts *votes* on an evidence row regardless of that row's stance. The seed itself casts no votes, so the seed is non-voting and the cert holds — but once 105 neutral rows are live, a later automated/human vote loop voting on them **would** move trust independent of their neutral stance. Do not point an auto-vote job at the seeded neutral set without its own gate. (This is the same stance-independent V-vote surface flagged in prior page-58 work.)

---

## C2 — re-scored sign-suppressed config clears the re-open bar → **PASS (for neutral-only auto-seed; live write Papa-gated)**

The relevant bar for a **neutral-only** seed is NOT the 0.90 sign-precision bar (that bar governed *auto-written sign*, which is now suppressed). It is: **zero trust-bearing auto-writes AND rdf genuinely non-voting.** Audited the seed plan invariants byte-independently — all hold:

| Invariant | Result |
|---|---|
| auto_seed / no_seed split | **105 / 24** ✓ (matches predicted-related / -unrelated) |
| **trust-bearing auto-writes** (stance ∈ supports/challenges) | **0** ✓ *(cardinal)* |
| auto_seed rows whose write stance ≠ `none` | **0** ✓ (all 105 write `none`) |
| auto_seed rows not flagged `neutral_non_voting` | **0** ✓ |
| auto_seed label ≠ rdf | **0** ✓ |
| no_seed rows that write anything | **0** ✓ (all write-stance `None`) |
| future confirmed-contradiction write stance ≠ `challenges` | **0** ✓ *(landmine #2 honored — writes `challenges`, never `contradicts`)* |
| human queue | contradicts **18** + supports **43** = 61 ✓ (both collapsed to rdf for the auto pass) |
| tau_vote tuned? | **no** (0.7 unchanged) ✓ |

This implements my minimal-change spec exactly (auto-seed rdf-only; suppress local supports + contradicts to human queue; sentinel → neutral; no threshold tuning), and adds the correct `contradicts→challenges` write-stance mapping. **rdf P 0.7755 is not a fail signal here** — it reflects 21 supports + 1 contradicts intentionally seeded as neutral (safe under-labeling, the design goal), not fabricated context.

**Therefore both re-open conditions are satisfied: C1 verified, C2 re-scored + reproduced.** The CONDITIONAL on the prior verdict resolves to **PASS** for the artifact-level neutral seed.

### Conditions that ride to the (separate, Papa-gated) live write
- **E1 (execution-time, highest leverage):** the `POST /evidence` `EvidenceCreate` default is `stance="supports"` (claims.py L353 — landmine #1). The seed executor MUST pass `stance="none"` **explicitly** on every write and never fall through to the default. **Post-seed, spot-check the `stance` column of every newly written evidence row == `none`** (0 in {supports, challenges}). The plan is correct; this guards the *executor*.
- **E2 (belt-and-suspenders):** confirm `none` is stored verbatim by the Evidence model/endpoint (not coerced). Even a coercion to `related_different_facet` stays non-voting, so this is low-risk, but read it back once post-seed.
- **E3:** C1 was verified against trust code at HEAD `4ba9675`. If the trust calculator changes before the live write (e.g. V wired to an auto-vote loop, or any weight given to neutral stance), **re-verify C1** first.
- **Non-blocking residual:** 7 Stage-1 unrelated-leaks seed as neutral off-topic context (no trust move). Optional light human skim of the auto-rdf set on this flagship page.

---

## LEG-A GAP QUESTION — does the earlier gold-audit scope block the neutral seed? → **NO. It only ever constrained a FUTURE auto-SIGN. HwaO's read CONFIRMED.**

Two parts:
1. **Scope correction:** my LEG-A was a **census of every supports/contradicts-relevant row**, including the Claude-tiebroken ones (15 of 22 false-supports and 5 of 17 false-contradicts were `claude_tiebreak`-sourced — read first-hand). What I did *not* exhaustively re-audit is the rdf↔unrelated interior of the 71 `qwen_gpt_agree` rows. So the gap is narrower than "took the gold as ground truth," but it is real for that interior.
2. **Why it does not block the neutral seed:** because **no sign is auto-written.** Whether any given row is "really" supports, contradicts, or rdf, the auto pass seeds it as the *same* neutral non-voting context. Gold-label accuracy on the supports↔facet (and facet↔contradicts) boundary is therefore **immaterial to the safety of a neutral-only seed** — it cannot produce a false `supports` or false `contradicts` because it writes neither. The only failure a wrong gold label could cause here is a truly-*unrelated* row being shown as neutral context (the 7 Stage-1 leaks), which is the non-blocking residual above.
3. **What the gap DOES still gate:** any future **auto-SIGN** pass (where supports/contradicts precision is load-bearing) requires the gold to be airtight first — i.e. re-audit the rdf interior and/or a Claude-in-loop sign stage with contradicts n large enough to measure (n ≥ ~10). That precondition is unchanged.

**Confirm HwaO: the LEG-A scope does not block the neutral-only seed; it remains a precondition for a future auto-sign.**

---

## BOTTOM LINE
- **C1 → CONCUR.** Verified first-hand in both live trust calculators (v2 is the live path): only `stance ∈ {supports, challenges}` moves E/tier; neutral `none`/rdf is non-voting; no penalty interaction in v2. Forward-caveat: stance-independent **votes** on seeded neutral rows can move trust later — gate any auto-vote job separately.
- **C2 → PASS** for an artifact-level **neutral-only (stance "none") auto-seed**. Metrics reproduce byte-for-byte; seed-plan cardinal invariant **trust_bearing_auto_writes = 0** holds; supports/contradicts correctly suppressed to human queue; `contradicts→challenges` mapping correct; no tau_vote tuning. rdf P 0.7755 is the intended safe under-label, not a fail.
- **LEG-A → does NOT block the neutral seed** (no sign written ⇒ gold sign-boundary accuracy is moot for safety); it remains a precondition only for a future auto-sign. HwaO's read confirmed.
- **Both re-open conditions from the prior CONDITIONAL are now satisfied.** The neutral-only seed is cleared to proceed to the separate, **Papa-gated** live write, under execution conditions E1–E3 (explicit `stance="none"` + post-seed stance-column read-back the load-bearing one).
- **Kun authorizes NEITHER seed NOR live write.** Gate re-opens for a future auto-SIGN only on an airtight re-audited gold (rdf interior) and/or a Claude-in-loop sign stage with contradicts n ≥ ~10.

— 🔬 Kun
