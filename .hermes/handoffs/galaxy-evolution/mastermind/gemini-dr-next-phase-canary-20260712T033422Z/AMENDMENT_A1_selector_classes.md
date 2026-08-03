# AMENDMENT A-1 — Phase A selector-class refinement (narrow)
Packet: `gemini-dr-next-phase-canary-20260712T033422Z` · Author: Hwao · Issued 2026-07-12
Trigger: Tori Phase-A gate issue (no action taken). Evidence pinned: real-DOM
`selector_probe_compact.json` sha256 `6f76c7f93f1ddb81b234889e0002b271ac00c316669e89c57dfd847fa76210ba`;
channel `read_channel_probe.json` sha256 `03d3cf17a5daf2a90f2266a623ac4bcd34c1c2307b917e6f0bb49dff49e53a33`
(both verified on disk).

## Why (the contradiction being fixed)
DIRECTION §3.5 / G-A2 required the **running/stop** indicator AND the three **wall** selectors to be
"FOUND" live, while G-A3 forbids changing state. On a clean, authenticated, completed page the
running/stop control is legitimately absent (it only exists during a live run) and the wall surfaces
are legitimately absent (that is the desired state). Requiring them "FOUND" is unsatisfiable without
either starting a run (G-A3 violation) or inducing a wall (never allowed). Tori correctly refused to
force those states. This amendment resolves the contradiction **without loosening any Start,
verification, quota, custody, or hard-stop rule** — and tightens wall detection.

## Scope
Amends ONLY the selector-validation classification in DIRECTION §3.3–§3.5 and gate **G-A2** for the
running/stop indicator and the three wall detectors. **Unchanged and still binding:** G-A1
(read-channel gate), **G-A3 (zero action in Phase A)**, G-B1 arming gate, the single **human**
Start-research, no second start, no verification bypass, quota preflight/refresh, exact-target
custody, all §6 hard stops, C1-only, no retry.

## Selector classes (replaces the flat "all FOUND" requirement)
1. **Presence-required (must be FOUND now, structural, on the clean/completed surface):** composer
   input; Pro / mode label; Deep-Research active state; plan container; Start-research control
   (presence suffices even if disabled/historical); complete state; answer-body container;
   completion-marker / links region. — All confirmed FOUND per evidence `6f76c7f9…`.
2. **Deferred-positive — running/stop indicator:** it cannot exist on a clean/completed page.
   Requirement: (a) **structurally defined** selector; (b) **negative (absent) on the current clean/
   completed surface** — confirmed; (c) **fixture-tested positive** against the saved `fx_running`
   DOM fixture (proves it matches when a run is live); (d) its **live positive check is deferred to
   immediately after Duho's single Start** (DIRECTION §4 step 5): if the running/stop state is not
   positively present within a bounded wait after that one Start — the R14 "acknowledged, no stable
   control" signature — that is a **hard stop, no re-click**.
3. **Wall detectors (verification/CAPTCHA, billing, login):** (a) **narrow, structural, DOM-scoped
   only** — broad body-text / substring wall matching is **BANNED** (it false-positived on report
   prose; Tori already rejected it, correctly); (b) **negative on the current clean authenticated
   page** — confirmed; (c) **fixture-tested positive** against the saved `fx_verification_wall`,
   `fx_billing_upsell`, `fx_login_wall` fixtures; (d) **any wall detector evaluating true at any point
   in Phase A or Phase B ⇒ immediate `DR_HARD_STOP_<WALL>_<UTC>`**, never "cleared" by any agent
   (verification clearing remains Duho-only, and even then only re-load, never a bypass). Walls are
   **never** required to be FOUND live.

## Revised Phase A PASS — G-A2′
Phase A is VALIDATED when: all **presence-required** selectors are FOUND (structural); the
running/stop indicator and the three wall detectors are each **structurally defined, negative on the
current clean surface, and fixture-tested positive** against the named dev-lane fixtures; the
narrow-structural wall rule (§class 3a) is adopted; and **zero action was taken** (G-A3 intact,
attested). Tori then writes `DR_PHASEA_SELECTORS_VALIDATED_<UTC>` citing evidence `6f76c7f9…` /
`03d3cf17…` and the fixture-test result hashes; otherwise `DR_PHASEA_SELECTORS_FAILED_<UTC>`.

## Explicitly NOT loosened
No change to: the single human Start; the ban on any second Start; verification being cleared only by
Duho and never bypassed; the <80% quota preflight and finally-style refresh; exact-target custody;
the ack-no-control / wall / billing / model-mode / read-channel / TCC hard stops; C1-only; no retry.
The deferred running check and the wall detectors becoming *stricter* (structural, fixture-proven,
hard-stop-on-true) is a tightening, not a relaxation.

## Hwao did / did not
Did: issued this narrow amendment + ledger rows; verified the two evidence hashes on disk. Did NOT:
browse, take any DOM action, write the Phase-A verdict marker, or change any Start/verification/quota/
custody rule. Tori applies G-A2′ (incl. the fixture-tests) and writes the verdict.
