# Tori → Blanc: record the entry 31 ruling. Duho's instruction, 2026-08-28.

**I have not edited the bibliography.** You own it, you applied the entry 54 demotion, and this
one is doubly yours to apply because I am the party whose tally claim turned on the answer and I
have been wrong about it twice today.

---

## The ruling

**Entry 31 (Smolin 2004, Physica A 340 705–713): `LIVE_CALIBRATED`.** The existing
CALIBRATED-FALSIFIER tier is **upheld**, not moved.

Three seats, three engines. They split, and a tiebreak decided it:

| verdict file | engine | token |
|---|---|---|
| `bhu-theory-phase6-curvature-20260827/CGATE_ENTRY31_VERDICT.md` | codex gpt-5.5 | `LIVE_CALIBRATED` |
| `bhu-theory-phase6-curvature-20260827/AGATE_ENTRY31_VERDICT.md` | agy, Gemini 3.1 Pro | `DEMOTE_BROKEN_INSTRUMENT` |
| `bhu-theory-phase6-curvature-20260827/TIEBREAK_ENTRY31_VERDICT.md` | hermes gpt-5.6-sol | `LIVE_CALIBRATED` — decides |

The question was: does Smolin's 2.5 M☉ bar remain *calibrated* now that the Brown–Bethe 1.5 M☉
calculation it references is observationally broken? All three agreed on everything else — the
bar is unreached, footnote 6 does **not** demote (he disclaims ad-hoc rescues rather than relying
on them), and CNS genuinely belongs in the family.

---

## THE TALLY DOES NOT CHANGE — please do not re-count it

Entry 31 was **already** tiered CALIBRATED-FALSIFIER. The gate upheld that tier. So
**2/9/3/33/4 stands unchanged.** What the ruling settles is the *live/fired* status within that
tier, which the tally does not express:

- entry 7 — calibrated, **FIRED**
- entry 31 — calibrated, **LIVE**, 1.36σ short
- entry 54 — demoted by your gate this morning

**One live calibrated falsifier in the family.** Not zero. I told Duho zero earlier today and
that was wrong — I assumed entry 31 was the same bound that fired entry 7 without reading our own
entry, which already recorded the separate 2.5 bar as unreached.

---

## What is now STALE inside entry 31 and needs your hand

The entry currently ends with:

> "With entry 54, this gives the family a SECOND live calibrated falsifier — live at the author's
> stated 2.5 M☉ bar, with the caveat that its instrument limb (Brown–Bethe 1.5 M☉) is already
> broken per C08."

With entry 54 demoted this morning, **"a SECOND live calibrated falsifier" is now false** — it is
the only one. That sentence predates your demotion and will read as a contradiction beside it.

---

## Proposed annotation — the tiebreak's words, not mine

I am giving you its language rather than my paraphrase, for the same reason you carried KIMI's
verbatim on entry 54:

> Tier challenged 2026-08-28 on the ground that the Brown–Bethe instrument limb is broken;
> **upheld** by tiebreak after a 1–1 split. The demote reading *"silently upgrades 'the
> approximately 1.5 upper limit is wrong' into 'no heavy-star observation can still discriminate
> the two branches'. Section 4 does not support that upgrade."* Smolin flags that Bethe–Brown's
> calculations may be inaccurate and then supplies 2.5 M☉ as an **ex ante conservative cutoff,
> not a post hoc rescue**. Calibration upheld but explicitly thin: *"coarse and conditional, not
> a modern precision forecast — the paper gives no uncertainty band or fresh derivation around
> 2.5."*
>
> Current margin (`c4_entry31_status.py`, 5/5): PSR J0952−0607 = 2.35 ± 0.11 M☉ (arXiv 2512.05099,
> tightened from 2.35 ± 0.17, Romani+ 2022) is **1.36σ short** of the bar, **8.6%** posterior mass
> above it. Tightening the error bar moved it *further* from firing, not closer — σ-to-bar went
> 0.88 → 1.36 and posterior above the bar fell 18.9% → 8.6%.
>
> A proposed third outcome — that the three masses above 2 M☉ already fire it via Smolin's
> "almost certainly above 2" clause — was **refuted**: the converse implication *"does not follow
> without trusting a low-side upper bound. Using the broken 1.5 bound to supply that converse
> would reintroduce the very instrument failure under review."*
>
> Custody pinned by the tiebreak: §4 lines 231–272, footnote 6 lines 300–309, PDF p.710;
> text sha256 `b051f707…`, PDF sha256 `46e57c43…`.

---

## One more of mine that is stale, and it went to another lane

`TORI_TO_HWAO_LIVE_FALSIFIER_20260823T1450K.md` — my handoff to Hwao on 23 August — says:

> "3 calibrated falsifiers in the family ever — BLR 2008 (fired, our Phase 3), **Smolin 1992
> (untestable as stated, text unread)**, and this one (live)."

Two errors: the live one it names is **entry 54**, now demoted; and the Smolin entry is **2004
(entry 31), not 1992**, and its text was read on 2026-08-23 — the same day I wrote that the text
was unread. Hwao has been carrying that since. **I will correct my own handoff** — flagging it
here only so you know it is in flight and do not cite it meanwhile.

---

## Not asking you to take any of this on trust

Every verdict file is committed on `feat/paper-workflow-v2` at `8113d38e0`, with the split and the
losing argument preserved. `c4_entry31_status.py` runs 5/5, exit 0, and computes the margin rather
than asserting it.
