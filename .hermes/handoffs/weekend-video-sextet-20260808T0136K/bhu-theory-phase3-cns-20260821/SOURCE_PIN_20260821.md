# Source pin — the 2026 J1913+1102 mass update, and what pinning it revealed

Duho: *"pin the A&A masses"*. Done, and it settles the outstanding Gate B note (c) — but not in
the direction I expected.

## The pin

| field | value |
|---|---|
| cited in our record as | "2026 update, accepted A&A (arXiv:2606.19276)" |
| actual title | *Improved proper motion and gravity tests with PSR J1913+1102* |
| authors | Miao, Freire, Wex, Meng, et al. |
| submitted | 2026-06-17 |
| pinned file | `sources/ar5iv_2606.19276.html` |
| sha256 | `ad8fba272ad619971a3bb8dca7d257e5bbd66d17dcdf097a87b00450d81539ce` |

**The masses check out exactly.** Verbatim from the abstract: "the pulsar mass m_p = 1.599(8) M⊙,
the companion mass m_c = 1.290(8) M⊙ and thus the mass ratio, q = 0.807(8)". Those are precisely the
values the 2026-08-17 adjudication carried. Nothing our record said about them is wrong.
(Minor: the parameter table lists m_c = 1.291(8) against the abstract's 1.290 — a rounding
difference between fit solutions, immaterial at our precision. Total system mass 2.88965(17) M⊙.)

## What pinning revealed — it is a preprint

**arXiv lists no journal_ref and no DOI. INSPIRE has no publication_info and no DOI.** Our record
described it as "accepted A&A", which may well be true — acceptance often precedes indexing — but it
is not, today, a published paper. Under the standing rule (peer-reviewed journal articles are the
base layer; preprints are context) **the tightest masses in our chain are context-grade.**

## Consequence — the margin depends on the source class, and must be quoted that way

| masses | class | ceiling (Tauris budget, 0.0134 M⊙) | exceedance |
|---|---|---|---|
| Ferdman et al. 2020, Nature **583**, 211 | **published** | 0.064 M⊙ | **6.7σ** |
| Miao et al. 2026, arXiv:2606.19276 | preprint (pinned here) | 0.065 M⊙ | 21.6σ |

**Limb 2 fires on either.** But the number quotable against the published record is **~7σ, not
~21σ**. The 21σ figure — which the C08 adjudication used as its headline confidence, and which I
repeated all through Phase 3 — rests on preprint masses.

## What this does to the record

- **No verdict changes.** The chain is still falsified as its source states it, on both readings.
- **The C08 adjudication's "≈21σ on the deciding limb" should be attributed**, not corrected: it is
  right about the preprint measurement and should say so. On published masses it is ~7σ.
- Gate B note (c) is **resolved**: the masses are now pinned and hash-checkable in the lane, and the
  answer to "is the margin measurement-dependent?" is yes, and now quantified.
- This is the *third* place in Phase 3 where a number our record leaned on turned out to sit one
  source-class below where it was being quoted. The pattern is worth naming: **tightest available
  number ≠ best-supported number.**

— Tori, 2026-08-21 KST.
