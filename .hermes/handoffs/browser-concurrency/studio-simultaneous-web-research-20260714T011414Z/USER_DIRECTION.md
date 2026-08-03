# User direction — research true simultaneous web operation

Packet: `studio-simultaneous-web-research-20260714T011414Z`

User direction: research how multiple agents can operate web workflows simultaneously on the Mac Studio without interfering with each other.

Observed local problem to solve:

- Flow/Veo and Gemini Deep Research currently share one Google Chrome application/profile.
- Existing Flow driver targets the active tab of the front window, activates Chrome, closes every Chrome window, uses the global clipboard, and sends global System Events keystrokes.
- Tori's current computer-use path scopes to an app/frontmost window rather than a durable exact browser tab.
- Multiple cua-driver/Hermes processes have also shown process-local bridge loss.

Research-only boundaries:

- Hwao coordinates; Lana reviews architecture/safety; Goru inventories local collision points and candidate mechanical isolation controls; Kun evaluates reproducibility/test design; Tori verifies evidence and synthesizes.
- Web research must use non-GUI `web_search`/`web_extract` or official docs; do not drive Chrome during Flow work.
- Read-only local inspection is allowed.
- No browser/profile creation, install, code change, service restart, account/OAuth/billing action, login, permission-dialog interaction, DB, deploy, cron, git write, or live experiment in this packet.
- Do not expose cookies, tokens, profile contents, browsing history, or unrelated tabs.

Questions to answer:

1. Can separate agents reliably control independent browser instances/windows/profiles on macOS at the same time?
2. Which isolation boundary is sufficient: tab, window, profile, separate browser app/bundle, Playwright browser context, or separate OS user/VM?
3. How should authenticated Google Flow/Gemini sessions, shared quota, downloads, clipboard, focus, permission prompts, CAPTCHA, and account challenges be handled?
4. What do Chrome, Playwright/CDP, and cua-driver officially support, including current remote-debugging/profile constraints?
5. What browser-broker/lease architecture would prevent two agents from touching the same browser target or global OS resources?
6. What exact changes are needed to replace close-all/front-tab/global-keystroke automation?
7. What staged canary and rollback gates would prove non-interference before live use?

Deliverables inside this packet:

- `HWAO_RESEARCH_PLAN.md`
- lane reports for Hwao-designated Lana/Goru/Kun work
- `TORI_EVIDENCE_NOTES.md`
- `HWAO_FINAL_RECOMMENDATION.md`
- `TORI_VERIFIED_SYNTHESIS.md`

End state is a recommendation and permission-gated implementation plan only, not implementation.

USER_SIMULTANEOUS_WEB_RESEARCH_APPROVED_20260714T011414Z
