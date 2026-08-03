# GORU_COLLISION_INVENTORY — Local Collision Inventory

## 1. Flow/Veo driver dissection
Based on the `grep_search` and manual inspection of `/Users/duhokim/HermesOps/scripts/`, the scripts classify as follows:
- **Current Drivers** (seen running during prior tracing): `clips/flow_generator_batch.py`, `watch_clip05.sh`, `agent_watch.sh`.
- **Candidate/Legacy Drivers**: `video_driver_auto.py`, `check_omni.py`, `test_gemini_bubble.py`, `flow_generate_clip_05.py`.

**Offending operations quoted from `flow_generator_batch.py`:**
- **Front-window / Active-tab targeting:**
  ```applescript
  # Lines 10-13
          tell application "Google Chrome"
              set target to active tab of front window
              return execute target javascript jsCode
          end tell
  ```
- **Activate (Focus Stealing) & Close All Windows:**
  ```applescript
  # Lines 37-43
      tell application "Google Chrome"
          activate
          close every window
          make new window
          set URL of active tab of front window to "https://labs.google/fx/tools/flow"
      end tell
  ```
- **Global Clipboard Use:**
  ```python
  # Line 71
      subprocess.run(['osascript', '-e', f'set the clipboard to "{prompt}"'])
  ```
- **Global System Events Keystrokes:**
  ```applescript
  # Lines 82-88
      tell application "System Events"
          keystroke "v" using {command down}
          delay 2
          keystroke return
      end tell
  ```

## 2. Chrome instance/profile facts
- **Running Chrome tree:** Chrome processes run under the `duhokim` user account.
- **Profile singletons:** Inspection of `$HOME/Library/Application Support/Google/Chrome` confirms the presence and mtime updates of `SingletonLock`, `SingletonSocket`, and `SingletonCookie`. These lock files enforce a strict one-running-process-per-profile constraint.
- **Window/tab count:** UNKNOWN (Cannot be obtained without driving Chrome via scripting, which is prohibited by the read-only directive).

## 3. Automation-stack census
**Point-in-Time Process Census** (`2026-07-14T01:47:20Z` via `ps -axo pid,ppid,etime,comm`):
- `81657 ... /Applications/CuaDriver.app/Contents/MacOS/cua-driver`
- `85086 ... /Users/duhokim/.local/bin/cua-driver`
- `59914 ... /Users/duhokim/.hermes/hermes-agent/venv/bin/python3` (Hermes profile)
- `94962 ... /Users/duhokim/.hermes/hermes-agent/venv/bin/python3` (Hermes main)
- `35430 ... /Users/duhokim/.hermes/hermes-agent/venv/bin/python` (Hermes gateway)

**Collision Matrix:**
| Resource | Consumer | Exclusive/Shared | Evidence Ref |
|---|---|---|---|
| Keyboard (System Events) | Flow Driver (`flow_generator_batch.py`) | Exclusive (OS-global) | `flow_generator_batch.py:L82-88` |
| Clipboard | Flow Driver (`flow_generator_batch.py`) | Exclusive (OS-global) | `flow_generator_batch.py:L71` |
| Screen Recording / AX | `cua-driver` | Shared (OS-global) | Process census PID `81657` |
| Focus / Frontmost App | Flow Driver (`flow_generator_batch.py`) | Exclusive (OS-global) | `flow_generator_batch.py:L39` (`activate`) |
| Downloads Directory | Flow Driver (`flow_generator_batch.py`) | Shared (OS-global) | `flow_generator_batch.py:L148` |

*(Note: "Active tab" targeting relies on window state but is not cited here as evidence of actively stealing frontmost focus.)*

## 4. Bridge-loss dossier
Collation of `TORI_COMPUTER_USE_DIAGNOSTIC.md` (R1) and `TORI_R2_BROWSER_BRIDGE_BLOCKER.md` (R2):
- **Symptoms:** `computer_use capture app="Google Chrome" mode=ax` yields `0x0`, zero elements. Immediate `computer_use list_apps` yields zero applications.
- **Diagnostics:** `hermes computer-use doctor` is fully GREEN (cua-driver 0.7.1, active MCP session, macOS support, ScreenCaptureKit, Accessibility reachable).
- **Timing/Lineage:** The `hermes` process lineage sporadically loses its process-local computer-use bridge. The most recent incidence in R2 was logged at `2026-07-14T00:39:01Z`.

## 5. Local isolation candidates
Mechanical isolation controls that exist locally today (no installs required):
- **Separate Browser Bundles:** Eliminates profile Singleton collisions and domain cookie collisions.
- **Separate `user-data-dir` (Chrome Profiles):** Eliminates profile Singleton lock collisions, shared cookies, and auth states.
- **Additional OS Users or VMs:** Using separate interactive local macOS user accounts completely eliminates collisions across Keyboard, Clipboard, Focus, and Singleton domains by providing isolated OS sessions. *(System accounts like `nobody` are excluded as they cannot host interactive UI sessions).*
- **Displays/Spaces:** Mitigates screen real estate overlap but does not solve global keyboard, focus, or clipboard exclusivity.

## 6. Evidence Table
| Claim | Local Command / Path Reference |
|---|---|
| Driver offending behaviors | `/Users/duhokim/HermesOps/scripts/clips/flow_generator_batch.py` |
| Point-in-time process census | `ps -axo pid,ppid,etime,comm` filtered for `cua-driver|hermes|computer-use` |
| Installed Browser Bundles | `/Applications/Google Chrome.app`, `/Applications/Safari.app` |
| Bridge-loss incident R2 | `../gemini-dr-content-expert-gate-r2-20260714T002603Z/TORI_R2_BROWSER_BRIDGE_BLOCKER.md` |
| Profile Singleton constraints | `$HOME/Library/Application Support/Google/Chrome/SingletonLock` |

GORU_SIMWEB_DONE_20260714T011414Z
