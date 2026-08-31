**STATUS: ONE ITEM WAITS ON YOU — the mapping four-value confirmation.** In plain words: before the sweep can ever run, four small conventions inside the gain mapping had to be picked (which calibration number is the baseline, what "center of the colour range" means, how the physical clamp works, and how the calibration summary is recomputed). I picked them BLIND — committed before any data could be seen, with written reasons why none was shopped — and filed them in `ref/MAPPING_CONVENTION_COMMIT_20260831.md`. The architecture around them you already ruled ("Sweep runner owns it", 2026-08-31 morning). **Your choices: say "mapping conventions confirmed" — the sweep machinery unblocks and the replay manifest flag flips, nothing else changes — or name any convention you want changed, and it becomes a new commitment plus a fresh referee pass.** Codex read the four and called them defensible-but-underdetermined, which is exactly why the confirm is yours, not mine. Everything else is ruled: γ RATIFIED (Γ = 0.25) · terminal signature APPROVED (ceremony at run end) · map widening confirmed · exhaustion→ABSTAIN · stopping rule "option 2" · FORM-echo "Freeze with disclosure" — the text phase is COMPLETE and the freeze package (V124 + KNOWN_DEBT_APPENDIX final) awaits the build items, Sep-5's BS-1 rule, and your P0 signature.

**SCHEDULED, not open: BS-1 release choice resolves BY RULE on 2026-09-05** (DR10.1 auto-selects unless DR11 photo-z appears first — measured absent 2026-08-30; plain-words brief: `BS1_RELEASE_CHOICE_BRIEF_20260830.md`; override anytime before the date). (γ record:
`GAMMA_RATIFICATION_20260830.md`, verbatim words recorded). Everything else from the seven-item
sitting of 2026-08-30 10:46 is RULED AND BEING APPLIED (V85). This is a plain-language index, not a
source; if it and an underlying file disagree, the file is right.**

# Where the lane stands after the seven rulings

## RATIFIED 2026-08-30 20:19 KST — the one item the sitting created (was PENDING)

| what | where |
|---|---|
| **RATIFIED — the a-priori γ range ±0.25** (Duho, verbatim: *"γ range approved as proposed, ±0.25 in 50 steps"*). Was: ratify the proposed ±0.25, derived from the per-bin calibration floor (any gradient steeper than ≈0.21 cannot pass `a_LB_b ≥ 0.85` and never reaches a verdict; ±0.25 sweeps the whole admissible region with margin, at Δγ = 0.01 → 51 points). | `PROPOSAL_GAMMA_RANGE.md` · `GAMMA_RATIFICATION_20260830.md` |

## RULED 2026-08-30 10:46 — applied in V85, on me to keep repairing

1. **Partition → option (c).** The overlap is REAL; both rulings recorded; the open ORDERING rule
   decides by what the failure demonstrates, VOID winning where both descriptions hold.
2. **BS-3g sitting**: `n_draws = 99` · bound = **a-priori frozen range** (`k_γ` moot) · **common
   random variates** · seed/generator/Δγ committed blind in `ref/DRAW_MECHANICS_COMMIT_20260830.md`.
   **The draw discipline is UNFROZEN**; the five-round freeze's reason is gone.
3. **`REFUSED-INTEGRITY-MISMATCH` → the refusal owns it.** Log and continue; every mismatch
   enumerated at freeze; an unexplained mismatch BLOCKS the freeze; the digest-deviation VOID
   antecedent scoped by the ordering rule (wording in V85 §6.1, reported).
4. **The four object codes stay; the principle is rebuilt** — storage state allowed,
   content-derived forbidden, safe only under the precommitted χ-blind schedule.
5. **The lost request → WRITE-AHEAD ARRIVAL RECEIPT** — the second event class, authorised; no real
   request can vanish; N2 retired after eleven revisions.
6. **The rulings collision → option (a).** A post-χ recurring catch-all class **terminates the run**
   as `TERMINATED-UNNAMEABLE-REFUSAL-CLASS` — a third thing, neither VOID nor INCONCLUSIVE.
7. **Strata → option (A).** χ-derived accepted; **Row D2** produces the sealed stratum-index
   artifact (**slot BS-SI**, class P, UNFILLED); Row F consumes; Row F's void clause amended;
   **class counts moved 16/8 → 17/8, reported**; typed/capability barrier keeps the artifact out of
   `calibration_bins()`.

## STILL-OPEN REPAIRS the rulings do NOT absorb (mine, from the review loop)

The request state machine's remaining edges · the write-side surface on Rows C2/H ·
`REFUSED-SCHEMA-NONCONFORMING`'s home · the anti-drift guard — plus whatever the live V84 round and
the next rounds return.

## Standing blockers (build-owned, not decision-owned)

BS-3g emission: γ endpoints RATIFIED (2026-08-30) · `gates/replay_harness.py` digest (set when built) ·
BS-SI schema (written when filled). BS-6 and the first image byte remain blocked; γ̂ unmeasured;
**v9 frozen at `6a9abbbd` throughout — nothing in the seven rulings touched it.**

## Flagged, not blocking (V92, 2026-08-30)

**Hand-check re-views are now SINGLE-PASS, forward-only** — the sealed interface delivers each allocated object's render exactly once per member, because an unrestricted re-view count was a content-driven multiplicity exported into the non-χ access log (GPT56-V91 F3), colliding with the ruled χ-blind traversal. **Cost: a checker cannot revisit an earlier cutout — a labeling-ergonomics change to the hand-check protocol.** Taken as the least-invasive engineering fix; **reversible by ruling any time before BS-2k fills**. If second looks matter to the protocol, the alternatives are fixed-K padding (every object rendered exactly K times) or accepting a named multiplicity leak — both costlier.

**UPDATE (V93):** the single-pass rule above is SUPERSEDED — both seats broke it against the spec's own occlude-and-restore requirement (an interrupted member had no route to a terminal label). The rule is now CONSTANT MULTIPLICITY BY PADDING: exactly `R_max` renders per object per member (BS-2k constant ≥ 2), interruptions consume replays, unconsumed replays issued as padding commits. Cost now: bounded replays instead of none, plus log inflation. Still reversible until BS-2k fills.

**CONFIRMED 2026-08-30 20:45 KST — Duho, verbatim: *"map widening confirmed as filed"* (`MAP_WIDENING_CONFIRMATION_20260830.md`). The original filing (V93, per the coordinator's standing instruction on the binding map):** the (iv-c) map schema is WIDENED by two fields — the decision's `(boot_epoch, monotonic_reading)` — because the decide-within-D law needs per-decision clock evidence and widening the RULED access-log schema is not authorised; the map carries it instead. Non-χ by construction (bounded decimals). Was reversible-awaiting-confirmation; reversal is now a new ruling, not a lapse.

**RULED 2026-08-30 20:54 KST — ABSTAIN (Duho, verbatim: *"abstain"*; `EXHAUSTION_ABSTAIN_RULING_20260830.md`): a replay-exhausted object takes an ABSTAIN label and the run continues; the hard halt is superseded for that one case; member replacement not taken. The flag as it stood: UPDATE (V94):** padding is now PER-OBJECT AND PRE-LABEL (end-clustered timing leaked the count; session-set end was undefined) — every object shows the identical R_max-renders-then-label pattern. **And exhaustion has a named terminal: the run HALTS pre-BS-8f** (the absent-label path the earlier flag assumed did not exist). Softening the halt — an ABSTAIN label, or member replacement — would change the labeling protocol and is YOURS to rule; R_max ≥ 2 makes the halt the rare storm case.

**RULED 2026-08-30 20:22 KST — APPROVED (was FILED V100, recommended): the TERMINAL SIGNATURE.** Duho, verbatim: *"terminal signature approved, I'll do the ceremony at run end"* — taken in the V101 amended (recomputation-hardened) form; record: `TERMINAL_SIGNATURE_RULING_20260830.md`. Original filing: Both seats broke the successor-as-closing-eye answer (a programme-ending run has no successor; an existing one reads only the enumerator key's self-consistent endgame bytes). Recommended ruling: when a run ends, **Duho signs the disclosure pass record's digest** — one additional signing act that closes the P7→P9 suffix under his own key. Until ruled, the spec states the suffix is machine testimony with no closing waypoint, in exactly those words. (This absorbs the earlier Clause-6 filing: the terminal signature is the stronger and simpler of the two.)

**AMENDED (V101, and RULED as amended — see above):** the terminal-signature recommendation is strengthened per both V100 seats: the signing ceremony RECOMPUTES the terminal head from the chain bytes under a pinned verifier, and the signature covers (recomputed head, recomputation transcript digest) — signing what the enumerator presents would notarize testimony rather than check anything. The ask to Duho is unchanged in size: one signing act at run end.

