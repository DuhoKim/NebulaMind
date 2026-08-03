# TORI_EVIDENCE_NOTES — official support for simultaneous web operation

Packet: `studio-simultaneous-web-research-20260714T011414Z`
Access date for all external sources: 2026-07-14
Raw, hash-pinned extracts: `evidence/01_*.md` through `evidence/14_*.md`; hashes in `evidence/SHA256SUMS`.

## 1. Chrome / Chromium

### 1.1 One running browser owner per user-data directory — VERIFIED

Playwright’s current API documentation states: “browsers do not allow launching multiple instances with the same User Data Directory.” Chromium’s POSIX singleton source describes the second process notifying the first and then exiting. This supports a hard rule: never give two browser processes the same `user-data-dir`.

Sources:
- https://playwright.dev/docs/api/class-browsertype (`evidence/04_playwright_persistent_cdp.md`)
- https://chromium.googlesource.com/chromium/src/+/HEAD/chrome/browser/process_singleton_posix.cc (`evidence/02_chromium_process_singleton.md`)

### 1.2 Distinct browser instances with distinct data directories — VERIFIED for process/profile isolation; PARTIAL for all failure domains

Chrome’s official DevTools MCP article explicitly lists: “Run multiple Chrome instances in isolation with each instance running in a temporary profile.” This verifies independent instances/profile state. It does not prove independent Google-account quota, IP reputation, Chrome bundle update, machine resource, or macOS permission behavior.

Source: https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session (`evidence/06_chrome_devtools_mcp_isolation.md`)

### 1.3 Chrome 136+ remote-debugging constraint — VERIFIED

Chrome states that `--remote-debugging-port` and `--remote-debugging-pipe` are ignored for the default Chrome data directory from Chrome 136, and require a non-standard `--user-data-dir`. Chrome recommends Chrome for Testing for automation.

Source: https://developer.chrome.com/blog/remote-debugging-port (`evidence/01_chrome_remote_debugging.md`)

### 1.4 DevToolsActivePort and exact target discovery — VERIFIED

The official CDP site states that port `0` writes the browser endpoint to stderr and `DevToolsActivePort` in the profile folder. It exposes page targets with target IDs and target-specific close/activate endpoints.

Source: https://chromedevtools.github.io/devtools-protocol/ (`evidence/05_cdp_targets_multiclient.md`)

### 1.5 Updates/crashes across distinct instances — UNKNOWN/PARTIAL

Official material verifies profile/process isolation, not independent Chrome application-bundle updates or total crash isolation. Separate browser bundles or OS sessions provide a larger failure boundary than separate data directories.

## 2. CDP / Playwright

### 2.1 Browser contexts isolate browser storage — VERIFIED

Playwright describes contexts as incognito-like profiles that isolate cookies, local storage, and session storage, even inside one browser, and supports multiple contexts in one scenario.

Source: https://playwright.dev/docs/browser-contexts (`evidence/03_playwright_contexts.md`)

Boundary: this is browser-state isolation only. It does not isolate the browser process, native dialogs, account quota, network identity, macOS clipboard, focus, downloads unless separately configured, or a browser crash.

### 2.2 Persistent authenticated automation needs its own directory — VERIFIED

`launchPersistentContext(userDataDir)` returns the only persistent context for that directory. Playwright warns that the default Chrome profile is unsupported for automation and recommends a separate directory.

Source: https://playwright.dev/docs/api/class-browsertype (`evidence/04_playwright_persistent_cdp.md`)

### 2.3 CDP multiple clients — VERIFIED, but not a write-safety guarantee

The official protocol site says Chrome 63 introduced multiple-client support. Multiple clients may attach, but that does not serialize conflicting navigation, input, close, or submission commands. A broker is still required for multiple writers.

Source: https://chromedevtools.github.io/devtools-protocol/ (`evidence/05_cdp_targets_multiclient.md`)

### 2.4 Playwright `connectOverCDP` — VERIFIED with limits

Playwright calls CDP connection “significantly lower fidelity” than its own protocol connection. It can attach to an existing Chromium browser and expose the default context. The newer `noDefaults` option is intended to avoid some state interference when attaching to a daily-driver browser, but it does not make concurrent writers safe.

Source: https://playwright.dev/docs/api/class-browsertype (`evidence/04_playwright_persistent_cdp.md`)

### 2.5 Downloads can be segregated — VERIFIED

Playwright exposes `downloadsPath` / artifact directories. Future agents can therefore use one owned download directory per browser lease rather than moving files from the shared `~/Downloads` directory.

Source: https://playwright.dev/docs/api/class-browsertype (`evidence/04_playwright_persistent_cdp.md`)

## 3. macOS interaction boundaries

### 3.1 Accessibility can target process/window/element — VERIFIED

Apple’s UI-scripting guide identifies the hierarchy as “button X of window Y of process Z” and requires Accessibility approval per controlling app. This supports exact process/window/element addressing instead of “front window / active tab.”

Source: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/AutomatetheUserInterface.html (`evidence/07_apple_ui_scripting.md`)

### 3.2 Generic System Events keystrokes are safe for concurrent agents — NOT VERIFIED

Apple documents UI scripts as simulated mouse clicks and keystrokes and shows explicit process targeting for safe UI hierarchy operations. Apple's event architecture also states that most key events are delivered to the first responder of the key window. It does not promise that two independent generic `System Events` keystroke streams can safely target different web windows. The current Flow script’s untargeted paste/Return sequence must therefore be treated as an exclusive keyboard/focus operation.

Source: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/EventArchitecture/EventArchitecture.html (`evidence/19_apple_key_focus_routing.md`)

### 3.3 Clipboard is shared system state — VERIFIED

Apple states: “The pasteboard server is shared by all running apps.” Concurrent agents must ban the general pasteboard or acquire an exclusive clipboard lease with compare-and-restore semantics.

Source: https://developer.apple.com/documentation/appkit/nspasteboard (`evidence/08_apple_pasteboard_permissions.md`)

### 3.4 Accessibility and Screen Recording grants are app-scoped — VERIFIED; helper inheritance details PARTIAL

Apple says Accessibility must be granted to the third-party app and screen recording can be enabled “for each app listed.” This supports signing/running a stable driver app rather than spawning arbitrary untrusted binaries. Whether every child helper identity inherits a grant depends on code-signing/responsible-process identity and is not established by these sources.

Sources:
- https://support.apple.com/guide/mac-help/allow-accessibility-apps-to-access-your-mac-mh43185/mac
- https://support.apple.com/guide/mac-help/control-access-screen-system-audio-recording-mchld6aa7d23/mac
- `evidence/08_apple_pasteboard_permissions.md`

### 3.5 Multiple simultaneous AX clients — UNKNOWN

No official Apple source located in this research explicitly guarantees conflict-free simultaneous mutation by multiple Accessibility clients. Read-only observers are plausible but remain a canary requirement.

## 4. cua-driver

### 4.1 Background app/process/window/element addressing — VERIFIED

The official project article and pinned 0.7.1 contracts document background operation without moving the user’s cursor or foreground and actions addressed by `{pid, window_id, element_index}`. This verifies target routing, but not independent desktop channels: the same official process-model documentation says multiple clients still share screen, keyboard, pointer, accessibility tree, and recording machinery.

Sources:
- https://github.com/trycua/cua/blob/main/blog/inside-macos-window-internals.md (`evidence/09_cua_macos_targeting.md`)
- `evidence/20_cua_driver_shared_desktop_contract.md`

### 4.2 Durable browser-tab identity — UNKNOWN

The documented primary key is PID + native window ID + snapshot element index. A browser tab is not documented as a durable cua-driver target. Element indices are snapshot-scoped. Exact browser tab/target identity therefore needs CDP or browser-specific tab identity in addition to cua-driver’s native window identity.

### 4.3 Multi-session connection support — VERIFIED; independent concurrent desktop control — FALSE

The pinned Cua Driver 0.7.1 process model explicitly says multiple MCP clients can connect at the same time, but session identity does not make their control independent and “Two agents clicking at once still contend for the same desktop.” Session identity isolates narrower mutable state such as recordings, config overrides, and agent cursors. Installed Studio reliability under two long-lived bridges remains PARTIAL because of the unexplained local bridge losses.

Sources:
- `evidence/20_cua_driver_shared_desktop_contract.md`
- https://github.com/trycua/cua/issues/1777 (`evidence/10_cua_sessions.md`)

### 4.4 Bridge loss/session invalidation — LOCAL VERIFIED, official root cause UNKNOWN

Studio R1/R2 observed `list_apps=0` and `0x0` captures while `hermes computer-use doctor` remained green. The official sources reviewed do not identify this exact failure. Any broker must fail closed when a session cannot re-verify PID/window/target identity; it must never fall back to the frontmost window.

Local source: `goru/GORU_COLLISION_INVENTORY.md` §4, subject to Kun’s designed reproduction.

### 4.5 Browser-tab writes should use DOM/CDP; cua desktop writes must remain brokered — VERIFIED

The Cua Driver 0.7.1 tool reference says: “For a browser TAB the reliable path is the `page` tool (drives the DOM via CDP).” Therefore the true parallel writer path is separate browser processes with separate profiles and per-browser DOM/CDP actions. Any cua/AX/pointer/keyboard action still touches shared desktop machinery and must be serialized or separately canary-proven by the broker.

Source: `evidence/20_cua_driver_shared_desktop_contract.md`

## 5. Google authenticated/account behavior

### 5.1 Multiple Google sessions — VERIFIED; same-account concurrent automation UNKNOWN

Google says it is normal to have multiple sessions on the same device and that a new browser, app, service, or private window can create a separate session. It also supports signing in to multiple distinct accounts at once, while warning that a new window may use the default account when Google cannot tell which account is intended. None of these statements guarantees simultaneous automated control on one account.

Sources:
- https://support.google.com/accounts/answer/3067630?hl=en (`evidence/21_google_sessions_and_cross_chat.md`)
- https://support.google.com/accounts/answer/1721977?hl=en (`evidence/14_google_accounts.md`)

### 5.2 Flow credits are account-wide — VERIFIED

Google states Flow/AI credits “are shared across your account, regardless of which device you use.” Different browser profiles or machines therefore do not isolate quota.

Source: https://support.google.com/flow/answer/16526234?hl=en&co=GENIE.Platform%3DDesktop (`evidence/11_google_flow_credits.md`)

### 5.3 Gemini usage is account/product-coupled — VERIFIED; concurrent submission support UNKNOWN

Gemini Apps use compute-based limits; media generation and Deep Research consume more usage. Google’s public page does not promise safe concurrent Deep Research or Flow/Gemini submissions for one account.

Source: https://support.google.com/gemini/answer/16275805?hl=en (`evidence/12_google_gemini_limits.md`)

### 5.4 Automated traffic can trigger challenges — VERIFIED for Google Search; Flow/Gemini specificity UNKNOWN

Google Search documents automated traffic causing unusual-traffic messages and reCAPTCHA. Google Terms prohibit automated access that violates machine-readable instructions. No official Flow/Gemini source found in this pass states a supported concurrency limit or blanket permission for consumer-web automation.

Sources:
- https://support.google.com/websearch/answer/86640?hl=en
- https://policies.google.com/terms?hl=en-US
- `evidence/13_google_traffic_terms.md`

### 5.5 Multiple Gemini Deep Research requests and background continuation — VERIFIED

Google's current Deep Research help explicitly lists a limit on the “Number of research requests you can run at the same time.” It also says a user can leave the chat while a report runs and receive a notification when it is ready. This verifies product-supported concurrent Deep Research requests, subject to plan/product limits, and background continuation after submission. It does not prove cross-product Flow + Gemini concurrency or safe simultaneous browser automation.

Source: https://support.google.com/gemini/answer/15719111?hl=en&co=GENIE.Platform%3DDesktop (`evidence/15_gemini_deep_research_concurrency.md`)

### 5.6 Flow background generation — VERIFIED; multiple independent Flow requests UNKNOWN

Google Flow's mobile help documents background generation notifications and notification after the app is closed. Flow's computer help says the Agent can create multiple video variations in one request. These establish background continuation and multi-output generation. The reviewed public pages do not state a limit for multiple independent Flow requests running simultaneously or guarantee cross-product Flow + Gemini overlap.

Sources:
- https://support.google.com/flow/answer/16353335?hl=en&co=GENIE.Platform%3DiOS
- https://support.google.com/flow/answer/16353334?hl=en&co=GENIE.Platform%3DDesktop
- `evidence/16_flow_background_generation.md`

### 5.7 Gemini video generation allows other-chat activity — VERIFIED narrowly

Google says a user cannot interact with the same chat while a Gemini video is generating, but can start a new chat and return later. This supports concurrent client activity in another chat, not a guarantee that multiple video jobs or Flow + Deep Research jobs execute simultaneously.

Source: https://support.google.com/gemini/answer/16126339?hl=en (`evidence/21_google_sessions_and_cross_chat.md`)

## Evidence-grounded conclusion for downstream lanes

1. True browser-workflow parallelism is technically supported when each writer owns a distinct browser process and distinct non-default `user-data-dir`, with exact CDP target IDs, browser-native DOM/CDP actions, and separate download directories. It is not supplied by multiple cua-driver sessions alone.
2. A tab or window alone is not a sufficient boundary for two writing agents because the current tools and scripts still share process, profile, account state, clipboard, focus, permission dialogs, and crash scope.
3. Separate Playwright contexts are sufficient for isolated unauthenticated/read-only testing inside one browser, but not for this authenticated Flow + Gemini case.
4. Separate browser processes/profiles do not isolate the Google account’s credits/compute limits. Gemini Deep Research officially supports multiple research requests running at the same time, subject to limits, but cross-product Flow + Gemini concurrent submission and challenge scope remain undocumented. Serialize cross-product submission moments until a gated canary verifies the account behavior.
5. cua-driver can address native PID/window/element targets in the background, but its official process model says multiple clients share desktop machinery and can contend. Browser-tab writes should use DOM/CDP; any cua/AX/pointer/keyboard write remains broker-serialized until the Studio’s bridge and multi-client canaries pass.

TORI_SIMWEB_DONE_20260714T011414Z
