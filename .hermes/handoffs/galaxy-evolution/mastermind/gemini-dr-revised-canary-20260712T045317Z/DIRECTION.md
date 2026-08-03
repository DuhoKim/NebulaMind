# DIRECTION — Revised Deep Research canary (FRESH lane; explicitly NOT a retry of the closed packet)
Handoff: `gemini-dr-revised-canary-20260712T045317Z` · **Hwao leads** · commissioned: Duho approval 2026-07-12
Supersedes-not-resumes the CLOSED FAIL packet `gemini-dr-next-phase-canary-20260712T033422Z`
(`DR_C1_FAILED_20260712T042138Z`). That packet and every artifact in it stay **immutable and closed**;
nothing here reopens, retries, or edits it. This lane authors a **new prompt (C1r)** and a **separate
live gate**.

## 0. Preserved standing invariants (verbatim, binding)
- **One Duho Start; zero Tori Start; no follow-up; no retry.** A run here is a NEW prompt C1r, not a
  retry of closed C1.
- **Exact-target custody**; **finally-style postflight quota**; **artifact-first exact-ID chat
  cleanup** per the standing post-capture cleanup rule (already in Tori user pref + supervised
  workflow): remove the exact conversation only AFTER result saved + custody/hashes verified +
  exact-ID provenance; prefer Archive/Hide else permanent-delete + verify absence; never title-only,
  never Duho-owned.
- **Goru LOCAL-ONLY.** Incident artifacts quarantined. Verification cleared by Duho only, never
  bypassed. No DB/product/git/deploy/cron. No cookies/profiles/undocumented-API/stealth.

## 1. Objective (two safe steps, Hwao-led)
(A) **Offline post-mortem** of the failed C1 body against ALL binding clauses. (B) Prepare a
**revised** canary — new prompt C1r, a **TDD-green rendered-body validator**, pinned custody, fresh
exact-burn quota, and a **new arming marker** — with the live run behind a **SEPARATE gate**.
**No browser / live Gemini action until §5 arming completes.**

## 2. Roles / ACKs (quintet; ACK before Phase A)
- **Hwao:** leads; authors packet + post-mortem; executes/browses nothing.
- **Tori:** verifier; sole browser operator for the separate live gate (§6); quota preflight/postflight;
  capture/receipt; runs the validator; exact-ID cleanup; hard stops.
- **Goru:** LOCAL-ONLY; may author validator/prompt/adapter code behind an un-invoked boundary; no live.
- **Duho:** the one Start; verification/CAPTCHA clear.
`TORI_ACK` + `GORU_ACK` (role locks quoted) required before Phase A.

## 3. Phase A — offline post-mortem (local, read-only; NO browser)
Immutable inputs (from the closed packet): C1 body sha256
`9933638616c9fc4dfb8306849f1ed91bf2d008f819c2623b831aec672da347d3`; final receipt
`d93f2855ff95ce7968cdacf912409ee8d32a435f1cb8bfa5476ed14c7f9b758e`; sealed manifest
`727764ecf1cef1eb3bd0180b615b6bbfc4eb6ff77eeeb5f993d05ebf049bd84c`.
Audit the C1 body against **ALL** binding clauses C1–C8 (and any others in the contract), not only
the two flagged. Output `postmortem/POSTMORTEM.md`: per-clause verdict + body line refs; confirm the
known FAILs (C5 own-voice "established" L117; C4 missing same-line citation/`UNCITED_NOT_USABLE` L129)
and surface any additional latent issues to fold into C1r + the validator. Marker
`POSTMORTEM_DONE_<UTC>`.

## 4. Phase B — revised preparation (local, TDD; NO browser)
- **B1 rendered-body validator** (`validator/`): a **deterministic** checker for the mechanically
  decidable parts of the contract, plus explicit **`MANUAL_REVIEW_REQUIRED`** flags for semantic/
  ambiguous cases — it does **NOT** mechanically prove the full semantic contract. Correct clause
  mapping (C1 calibration contract):
  - C1 — meta header present (deterministic).
  - **C2** — per-section structure/order; **empty fields → `NONE_FOUND`** (deterministic
    presence/order; `NONE_FOUND` is C2's empty-field device, not C3).
  - **C3** — every number carries a source uncertainty **or** the same-line label
    `UNCERTAINTY_NOT_QUOTED_BY_SOURCE` (deterministic: flag a number with neither;
    `MANUAL_REVIEW_REQUIRED` to judge whether an unlabeled figure is genuinely a source-quoted value).
  - **C4** — every **calibration/validation statement** carries a same-line checkable citation
    (arXiv/DOI/ADS/URL) **or** `UNCITED_NOT_USABLE` (deterministic: flag such a statement with neither
    on its line; `MANUAL_REVIEW_REQUIRED` to judge whether a present citation is genuinely
    checkable/relevant). **Do NOT conflate with C3's numbers.**
  - **C5** — banned own-voice settled/causal register (establish(es/ed/ing)/proves/proven/confirms
    that/settles/settled question/resolves the debate/definitively/conclusively/is now known/
    "demonstrates that … causes") — deterministic grep; `MANUAL_REVIEW_REQUIRED` to triage an
    attributed quote-with-citation vs own-voice.
  - **C6** — estimand / non-commensurable labels + four qualifiers (`MANUAL_REVIEW_REQUIRED`, semantic).
  - **C7** — links ledger present (deterministic). **C8** — marker exactly once + final non-blank line
    (deterministic).
  **TDD: RED first, then GREEN**; fixtures MUST include the failed C1 body (must deterministically FAIL
  C5 L117 and flag C4 L129) and a clean-pass fixture. Marker `VALIDATOR_TDD_GREEN_<UTC>` (else
  `VALIDATOR_TDD_RED_<UTC>`).
- **B2 revised prompt C1r** (`prompt/C1r.md`): derived from original C1 (`adeaa369…`) but tightening
  C3/C4/C5 and any post-mortem findings (per-number uncertainty-or-`UNCERTAINTY_NOT_QUOTED_BY_SOURCE`
  reminder; same-line citation-or-`UNCITED_NOT_USABLE` for every calibration/validation statement;
  expanded banned-register reminder; final-line marker reminder). **New REQ id + new marker string.**
  `prompt/C1r.md` **IS the exact paste-ready submitted payload — no wrapper, no BEGIN/END sentinels,
  no code fence** — so that at run time `runs/c1r/prompt_submitted.md` is a **byte-identical copy whose
  sha256 equals the pinned C1r** (this removes the prior wrapper-vs-payload hash conflict). Pinned by
  sha256 in `MANIFEST.json`. At submit, additionally **verify the normalized composer text equals the
  normalized C1r payload** (guards against invisible composer transforms). Explicitly **NOT** closed C1
  and **NOT** a retry.
- **B3 reuse:** local capture tool `wait_and_extract.py` `c42df80e…` (LOCAL_CORE_PASS) + the
  Phase-A-validated real-DOM adapter, re-reviewed by Tori.

## 5. Arming gate (Phase C; ALL hold ⇒ `DR_C1R_ARMED_<UTC>`, else `DR_C1R_NOT_ARMED_<REASON>_<UTC>`)
- `POSTMORTEM_DONE` + `VALIDATOR_TDD_GREEN` present.
- C1r prompt custody pinned (sha match); validator + tool sha pinned.
- Verification confirmed clear (Duho / clean load, no wall in evidence).
- **Fresh consumer quota exact-burn preflight** captured + hashed (`evidence/quota_preflight_<UTC>`);
  PROCEED only < 80% used (non-responsive meter logged, all stops still apply).
- `TORI_ACK` + `GORU_ACK`; ≥ 60 min to reset; no hard-stop trigger; exact-target custody plan ready;
  standing cleanup rule loaded.

## 6. SEPARATE live-canary gate (Phase D — only after `DR_C1R_ARMED`; one supervised conversation)
1. Tori: NEW conversation; record exact URL/tab **immediately**; every read targets it.
   `runs/c1r/prompt_submitted.md` is a **byte-identical copy of `prompt/C1r.md`** — its sha256 **==**
   pinned C1r (no wrapper/sentinels) — AND the **normalized composer text == normalized C1r** before
   submit. Any mismatch ⇒ hard stop.
2. Positively select **Pro + Deep Research**; capture `model_mode`. Uncertain ⇒ hard stop.
3. Submit C1r **once** → `plan_snapshot`.
4. **The one Start — Duho (human). Zero Tori Start. No second start ever.**
5. Verify active state; ack-no-control ⇒ hard stop, no re-click.
6. Read-only monitor to completion; capture `body.md` exactly as produced. At most ONE
   packet-authorized neutral "continue" on visible truncation; **no follow-up, no retry.**
7. **Rendered-body validator gate + manual clause review (NEW, decisive):** run the validator on
   `body.md`. It emits **deterministic PASS/FAIL** per mechanical clause and `MANUAL_REVIEW_REQUIRED`
   for semantic C3/C4/C6 cases. **Acceptance REQUIRES BOTH: (a) deterministic PASS on every mechanical
   clause (incl. C8 marker once + final), AND (b) a clause-by-clause MANUAL review verdict PASS on
   every clause, resolving every `MANUAL_REVIEW_REQUIRED`.** Any deterministic FAIL, or any
   clause not manually PASS, ⇒ `runs/c1r/RUN_FAILED` (no acceptance marker), immutable, no retry.
   **Fail closed on ambiguity.**
8. Immutable `CAPTURE_RECEIPT` (`wc -c` + sha256 every file); `meta.md` (who Started, quota lines,
   anomalies, reload/continue log).
9. **Finally-style postflight quota** (regardless of outcome) → `evidence/quota_postflight_<UTC>`, hashed.
10. **Artifact-first exact-ID cleanup:** ONLY after receipt custody verified + exact C1r
    conversation-ID provenance ⇒ prefer Archive/Hide else permanent-delete that exact conversation +
    verify absence. Never title-only, never Duho-owned.
Terminal: `DR_C1R_DONE_<UTC>` (validator PASS + marker + cleanup) · `DR_C1R_FAILED_<UTC>` ·
`DR_HARD_STOP_<REASON>_<UTC>`. **No acceptance marker unless validator PASS.**

## 7. Write roots · markers · acceptance
- **Write root:** THIS lane only; temp `_tmp_*` here. No writes elsewhere; closed packet untouched.
- **Markers (zero-byte unless noted, this root unless noted):** `HWAO_DR_REVISED_CANARY_READY_20260712T045317Z`
  · `DR_REVISED_NOT_ARMED_20260712T045317Z` (initial) · `TORI_ACK`/`GORU_ACK` (ledger) ·
  `POSTMORTEM_DONE_<UTC>` · `VALIDATOR_TDD_GREEN_<UTC>`/`VALIDATOR_TDD_RED_<UTC>` ·
  `DR_C1R_ARMED_<UTC>`/`DR_C1R_NOT_ARMED_<REASON>_<UTC>` ·
  `runs/c1r/RUN_CAPTURED`/`RUN_FAILED`/`RUN_VOID` (+reason) · `DR_C1R_DONE_<UTC>`/`DR_C1R_FAILED_<UTC>` ·
  `DR_HARD_STOP_<REASON>_<UTC>`.
- **Acceptance:** §6.7 deterministic-PASS on ALL mechanical clauses **AND** clause-by-clause
  manual-review PASS + marker once/final + custody verified + exact-ID cleanup done. Fail closed otherwise.
- **Failure markers at every gate; no retry, no bypass; C1r-only (one run).**

## 8. Hard stops
Verification/CAPTCHA/unusual-traffic/login/billing reappears · model/mode uncertainty · capture-target
uncertainty · quota-source uncertainty or ≥80% · read-channel loss · TCC denial · any second-Start
pressure · validator/tool integrity mismatch · operator doubt · weekly reset ⇒
`DR_HARD_STOP_<REASON>_<UTC>` + reason; no bypass, no retry.

## 9. Hwao did / did not
Did: commissioned this lane (DIRECTION + MANIFEST + ledger seed + READY & NOT_ARMED markers +
`postmortem/`,`validator/`,`prompt/`,`runs/c1r/`,`evidence/`,`tori/` scaffolding), pinned inputs by
sha256. Did NOT: browse, run any phase, execute the post-mortem/validator, author C1r, touch the
closed packet, or write outside this lane. Phase A begins on Tori+Goru ACK.
