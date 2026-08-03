# Studio shared-browser coexistence hold

Packet: `gemini-dr-content-expert-gate-r3-20260714T004227Z`
Decision: **Tori Deep Research remains stopped; Flow owns the shared Chrome browser until idle**

Live inspection on `Duhoui-MacStudio.local` found active Flow/Veo web-generation work in the `ge-mastermind` / Goru lanes and one shared Google Chrome application.

The current Flow batch driver is not concurrency-safe:

- `flow_generator_batch.py:10-13` executes JavaScript against the active tab of the front Chrome window;
- `flow_generator_batch.py:37-43` activates Chrome, closes every Chrome window, creates a new window, and navigates it to Flow;
- `flow_generator_batch.py:71` uses the global clipboard;
- `flow_generator_batch.py:82-88` sends global System Events paste/Return keystrokes.

Those actions can close or retarget Gemini, steal the active tab, overwrite prompt custody, or submit into the wrong web surface. Therefore Flow generation and Gemini Deep Research must not be driven concurrently by separate agents under the present automation.

Safety action taken: the idle, blocked detached Tori process `tori-dr-r3-004227` was exact-target terminated and absence verified as `TORI_DR_STOPPED_NO_USER_WINDOW_CHANGE`. The user's Terminal window was not closed or replaced. R3 remains NOT_ARMED; no Gemini prompt was submitted and no quota was consumed.

Safe parallelism remains allowed for non-browser lanes. Browser work may resume only after Flow has stopped driving Chrome and one exact browser owner is assigned, or after the Flow automation is redesigned and verified to use a dedicated browser/profile plus exact window/tab identity with no close-all, front-tab, global clipboard, or global keystroke operations.

TORI_STUDIO_SHARED_BROWSER_HOLD_20260714T004227Z
