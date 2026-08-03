# TORI_VERIFIED_SYNTHESIS — true simultaneous web operation

Packet: `studio-simultaneous-web-research-20260714T011414Z`
Verification target: `HWAO_FINAL_RECOMMENDATION.md`
Decision: **VERIFIED WITH EXPLICIT QUALIFICATIONS**
Scope: research and implementation plan only; no implementation, browser/profile creation, canary, submission, quota use, or live operation was authorized or performed.

## 1. Integrity receipt

- `HWAO_FINAL_RECOMMENDATION.md` and compatibility copy `FINAL_RECOMMENDATION.md` are byte-identical.
- Verified SHA-256 for the canonical recommendation after the late-evidence refinement: `bffa176ee05b49b7d889f66a02421f83a7c325fbcec1cabb4483956345ba415d`.
- All 21 external evidence extracts passed `shasum -a 256 -c evidence/SHA256SUMS` on 2026-07-14.
- Required lane reports and markers are present:
  - Goru: `goru/GORU_COLLISION_INVENTORY.md`; `GORU_SIMWEB_DONE_20260714T011414Z` in `goru/ACK.md`.
  - Lana: `lana/LANA_ARCHITECTURE_SAFETY.md`; final line `LANA_SIMWEB_DONE_20260714T011414Z`.
  - Kun: `kun/KUN_CANARY_DESIGN.md`; final line `KUN_SIMWEB_DONE_20260714T011414Z`.
  - Tori evidence: `TORI_EVIDENCE_NOTES.md`; final line `TORI_SIMWEB_DONE_20260714T011414Z`.
  - Hwao: `HWAO_COMPLETION_MARKER` contains `HWAO_SIMWEB_FINAL_RECOMMENDATION_DONE_20260714T011414Z` and was rewritten after the canonical final recommendation.

## 2. Recommendation claim cross-check

| Hwao recommendation claim | Verdict | Evidence / qualification |
|---|---|---|
| Distinct Chrome processes with distinct non-default user-data directories can run in isolation. | **VERIFIED** | Chrome officially documents isolated multiple instances using separate profiles (`evidence/06`); Playwright says browsers do not allow multiple instances on the same user-data directory (`evidence/04`); Chrome 136+ requires a non-default directory for remote debugging (`evidence/01`). |
| Exact browser targets can be addressed by CDP target ID instead of front window/active tab. | **VERIFIED** | Official CDP target discovery and target-specific endpoints (`evidence/05`). CDP supports multiple clients, but does not serialize writers; the proposed broker remains required. |
| Browser storage contexts alone are enough for authenticated Flow + Gemini writers. | **REJECTED by recommendation, correctly** | Playwright contexts isolate browser storage, not OS-global state or browser crash scope (`evidence/03`, `evidence/04`). Separate processes/profiles are the recommended writer boundary. |
| Background target-addressed cua actions can avoid foreground/cursor movement. | **VERIFIED AS ROUTING, NOT INDEPENDENCE** | Cua Driver documents PID/window/element routing without focus steal, but its pinned 0.7.1 process model says clients still share screen, keyboard, pointer, AX, and recording machinery and “Two agents clicking at once still contend” (`evidence/20`). |
| Multiple cua-driver sessions provide independent simultaneous desktop control. | **FALSE, OFFICIALLY VERIFIED** | Multiple clients may connect, but session identity does not create independent desktop channels (`evidence/20`). Every cua/AX/pointer/keyboard write must therefore hold one exclusive machine-wide desktop-control lease. |
| The general clipboard is safe for parallel agents. | **REJECTED by recommendation, correctly** | Apple states the pasteboard server is shared by all running apps (`evidence/08`). The design bans it by default. |
| Generic System Events keystroke streams are safe as independent channels. | **NOT ESTABLISHED; FOCUS DEPENDENCE VERIFIED** | Apple says most key events go to the first responder of the key window (`evidence/19`) and does not promise simultaneous generic-keystroke isolation (`evidence/07`). The untargeted Flow sequence correctly remains exclusive. |
| The current Flow driver can coexist with another browser writer. | **FALSE, locally VERIFIED** | Direct source read confirms active-tab/front-window targeting (`flow_generator_batch.py:10-13`), `activate`, `close every window`, and new front-window creation (`:37-43`), global clipboard write (`:71`), generic System Events paste/Return (`:82-88`), and shared `~/Downloads` move (`:146-148`). It cannot safely coexist with Tori’s Gemini writer. |
| The current default-profile AppleScript is itself broken by Chrome 136. | **FALSE; final recommendation corrected** | Chrome 136’s restriction applies to remote-debugging switches on the default data directory (`evidence/01`), not to the existing AppleScript. It blocks the proposed exact-target CDP migration unless non-default profiles are provisioned. |
| One Google account’s Flow/AI credits are isolated by browser profile, OS user, or VM. | **FALSE, officially VERIFIED** | Google says Flow/AI credits are shared across the account regardless of device (`evidence/11`). The architecture treats quota as one shared account budget. |
| Gemini Deep Research supports more than one research request running at the same time. | **VERIFIED, subject to product limits** | Google lists a limit on the “Number of research requests you can run at the same time” and says a user can leave the chat while a report runs (`evidence/15`). |
| Flow work can continue after the client app closes. | **VERIFIED for the documented Flow mobile app** | Google Flow documents background successes/failures and notifications after the app closes (`evidence/16`). It also documents multiple variations in one request. |
| Multiple independent Flow requests can run simultaneously. | **UNKNOWN** | The reviewed official Flow pages do not state such a limit or guarantee (`evidence/16`). |
| A Flow job and Gemini Deep Research job can be active simultaneously on one account. | **UNKNOWN** | Per-product background operation is documented, but cross-product active-job overlap is not. C0-C4 cannot prove this because C4 has zero submissions. Only a separately approved bounded live overlap canary can resolve it. |
| Two automated Flow/Gemini submissions at the exact same moment are officially supported. | **UNKNOWN** | No reviewed official source establishes cross-product automated submission concurrency. The account-submission lease is a conservative policy, not a product fact. |
| A challenge is definitely account-scoped. | **UNKNOWN; final recommendation corrected** | Official evidence is Google Search unusual-traffic at network/egress level (`evidence/13`); Flow/Gemini challenge scope is unknown. Freezing same-account and shared-egress leases is deliberately conservative policy. |
| cua-driver multi-session connection is supported and independently reliable on this Studio. | **CONNECTION VERIFIED; INDEPENDENCE FALSE; LOCAL RELIABILITY PARTIAL** | Official 0.7.1 docs support multiple clients but explicitly reject independent desktop control (`evidence/20`). Local R1/R2 bridge-loss symptoms remain unexplained. Kun C0 is correctly the first gate. |
| The proposed minimum Flow + Gemini mechanical boundary is separate profiles/processes plus DOM/CDP writes and an exact-target broker. | **SUPPORTED ARCHITECTURE RECOMMENDATION, NOT YET LIVE-PROVEN** | Playwright officially runs parallel worker processes with separate browsers (`evidence/18`), and Cua’s own browser guidance says the reliable tab path is DOM via CDP (`evidence/20`). Cua/desktop writes remain serialized under the desktop-control lease. |

## 3. What “true simultaneous” means after verification

1. **Mechanical simultaneous browser control: supported on one specific path.** Each writing agent needs its own Chrome process, non-default user-data directory, owned download directory, exact CDP target identity, and browser-native DOM/CDP actions. Multiple cua sessions are not parallel desktop channels; every cua/AX/pointer/keyboard write is machine-wide serialized under the desktop-control lease.
2. **Concurrent Deep Research jobs: officially supported up to Gemini’s product limit.** This is separate from whether two automated surfaces may submit in the exact same instant.
3. **Flow background generation: officially supported per the documented mobile behavior.** Multiple independent Flow jobs and Flow + Gemini cross-product job overlap are still unverified.
4. **Submission moments: serialize for now.** One short account-submission lease is the safe policy until evidence or the bounded live canary establishes more.
5. **Challenges and quota stay shared concerns.** Quota is verified account-wide. Challenge scope is unknown, so any challenge freezes same-account and shared-egress activity pending a user decision.

## 4. Permission-gated path; no step is authorized by this synthesis

- **Phase I — code gate:** implement the broker, target leases, exclusive desktop-control lease, wrappers, fencing, and audit journal without changing browser behavior.
- **Phase II — code + profile-creation gate:** rewrite the Flow driver to Lana R1-R7 using browser-native DOM/CDP, add exact CDP targets, and provision distinct non-default profiles/download directories.
- **Phase III — separate approval for every Kun rung:** C0 dual-bridge soak; C1 dual read-only different apps; C2 dual read-only browser targets; C3 proves parallel DOM/CDP activity while all cua/AX/pointer/keyboard writes have non-overlapping desktop-control leases; C4 two authenticated isolated surfaces with zero submissions. Three comparable repetitions per rung; any invariant breach stops the ladder.
- **Phase IV — fresh live-canary gate:** one minimal Flow job and one minimal Deep Research job, submission clicks serialized, fixed small quota budget, challenge freeze armed, capture-and-stop. This is the first step capable of testing cross-product active-job overlap.
- **Phase V — later cutover gate:** only after Phase IV passes and Hwao/Tori review its receipts.

## 5. Plain-English answer

Yes, the agents can be made to browse at the same time without stealing each other’s windows, but only when browser writes use separate Chrome processes/profiles and browser-native DOM/CDP. The late official Cua Driver evidence is explicit: two cua agents clicking at once still contend for the same desktop, so all cua/AX/pointer/keyboard writes must remain one-at-a-time through the desktop-control lease. The current Flow automation cannot do either safely. Multiple Gemini Deep Research jobs are supported and Flow generation can continue in the background, but Flow + Deep Research overlap on one account still needs the separately approved live canary after C0-C4.

No browser, account, quota, profile, service, or driver behavior was changed by this research.

TORI_VERIFIED_SYNTHESIS_DONE_20260714T011414Z
