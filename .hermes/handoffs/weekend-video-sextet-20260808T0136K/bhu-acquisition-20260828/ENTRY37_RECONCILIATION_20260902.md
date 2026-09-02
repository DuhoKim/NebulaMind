# Entry-37 deep audit — reconciliation (Tori, 2026-09-02, STEP 3, queue draw #3)

**Entry 37 — J. Smoller & B. Temple (2003), "Shock-wave cosmology inside a black hole," PNAS 100, 11216–11218**
(arXiv astro-ph/0210105). Tier **CONSISTENCY-ONLY**. Brief `ENTRY37_AUDIT_BRIEF_20260902.md`.

## Verdict — BOTH SEATS AGREE, tier holds; the 2026-08-28 blind flag is ADJUDICATED and does not survive
| seat | token |
|---|---|
| codex (`ENTRY37_codex_RESULT.md`) | `AUDIT_HOLDS_CONSISTENCY_ONLY` |
| claude-seat (`ENTRY37_claude_RESULT.md`, blind) | `AUDIT_HOLDS_CONSISTENCY_ONLY` |

## What both derived independently (Tori verified the citations)
1. **What is proved:** a global exact FRW–TOV matching with an outgoing shock beyond one Hubble length inside a
   black hole; Theorem 1 (existence/uniqueness under the entropy inequalities), Theorem 2 (everywhere-subluminal
   iff σ ≤ 1/3, lines 223–229), Theorem 3 (Big-Bang shock-speed limits; σ = 1/3 launches at light speed);
   conditional bounds at the first-visibility epoch t₀: the shock lies within 4.5 Hubble lengths and exits the
   white hole by 4.5 t₀ (lines 288–291). The shock's distance at a given H is set by one free parameter
   (lines 296–297); the authors call these "only rough qualitative models" (lines ~324–341).
2. **The one observation-facing sentence** — the shock "would thermalize the radiation in a region well beyond the
   light cone … even though the model does not invoke inflation" (lines 43–44) — is followed at once by "Details
   will appear in our forthcoming paper [8]" (lines 44–45). No CMB scale, profile, sign or statistic is derived;
   the homogeneity the sentence leans on is the FRW ansatz (lines 23–24), not a shock-derived mechanism.
3. **The blind flag (08-28, QUALITATIVE-DIRECTIONAL):** every derived direction is model-internal — the entropy
   condition selecting explosion over implosion is imposed by hypothesis; the weakening shock, the white-hole
   exit and the interior mass function are never mapped to the sign of an observable; the "visibility" epoch is
   the moment the shock's launch point enters the particle horizon, an infinite-redshift image behind last
   scattering (claude-seat re-derived eq. 6.1). Under ruling A(a) none earns the tier. **Flag closed: not a finding.**
4. **Not PROSPECT either:** reaching an observation would require the lane to supply the physics (an off-centre
   observer, radiative transfer, a mapping from shock to temperature field), not merely a threshold. The
   honest route to the deferred claim is the forthcoming paper [8] itself — Smoller & Temple 2004,
   "Cosmology, black holes and shock waves beyond the Hubble length" (math-ph/0302036), which is **entry 38**,
   already in the corpus (CONSISTENCY-ONLY; full-read receipt `b43_entry38_fullread.py`). Its own deep audit is
   the proper follow-up, by the queue.

## Applied
Dated deep-audit annotation on entry 37: tier word untouched; the BLIND-FLAGGED note is marked ADJUDICATED.
Queue recomputed; next draw: entry 19.
