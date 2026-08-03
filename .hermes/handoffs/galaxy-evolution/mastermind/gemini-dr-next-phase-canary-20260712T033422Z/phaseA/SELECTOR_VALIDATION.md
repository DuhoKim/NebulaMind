# Phase A selector validation

Packet: `gemini-dr-next-phase-canary-20260712T033422Z`
UTC: 2026-07-12T03:55:29Z
Rule: `G-A2′` from `AMENDMENT_A1_selector_classes.md`
Verdict: `VALIDATED_READ_ONLY`

## Read channel

- Trusted tab-scoped Chrome execute-JavaScript channel: FOUND and operational.
- Desktop capture returned 0×0 and was not used.
- Explicit Chrome window ID + tab index used for every read.

## Presence-required selectors

| Selector class | Result | Live evidence |
|---|---|---|
| Composer | FOUND | one structural match on completed and clean app tabs |
| Pro mode | FOUND | one `currently Pro` mode selector on both tabs |
| Deep Research active | FOUND | two structural active-state matches on both tabs |
| Plan | FOUND | two structural matches on completed research tab |
| Start control | FOUND | two historical disabled matches on completed research tab; presence-only per amendment |
| Complete state | FOUND | completed structural state present |
| Answer body | FOUND | `#extended-response-markdown-content` present |
| Marker/links region | FOUND | answer body plus 150 link elements present |

## Deferred-positive selector

- Running/Stop: structurally defined; correctly absent on completed and clean tabs.
- Frozen `fx_running.html` selector test: PASS.
- Positive live check remains mandatory immediately after Duho’s one Start click. Absence then is a hard stop with no re-click.

## Wall detectors

- Verification/CAPTCHA: structural detector defined; negative live; frozen verification fixture PASS.
- Billing/upsell: narrow visible-dialog/control detector defined; negative live; frozen billing fixture PASS.
- Login: structural/URL detector defined; negative live; frozen login fixture PASS.
- Broad body-text wall matching is banned and regression-tested.

## Exact classifications

- `https://gemini.google.com/app/a70838d8e117de1d` → `COMPLETE`
- `https://gemini.google.com/app` → `DR_ACTIVE`

## Zero-action attestation

No click, focus change, typing, navigation, reload, submission, mode toggle, Start action, account action, verification interaction, cookie/profile access, or undocumented API use occurred during Phase A.

G-A1 PASS. G-A2′ PASS. G-A3 PASS. Phase B is still NOT_ARMED pending fresh quota and remaining G-B1 checks.
