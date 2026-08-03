# WONE ACK — helper lane: telemetry/assertions, sandbox-browser owner, serialized cua actor

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Brief marker: `WONE_VIABILITY_BRIEF_ISSUED_20260714T034720Z`

I, WonE, explicitly acknowledge this brief and accept the assigned role and standing protocols:
- **Standing protocols:** no solo lanes; use `_tmp_*` lane temp files; never use free-text tmux send-keys; the ledger is the sole shared state.
- **C0 scope:** I will assemble `BRIDGE_TELEMETRY.jsonl` and the pass receipt bundles from Goru/Garu samples; run the assertion set; and author the rung harness scripts under `canaries/` (understanding Hwao must review before first use).
- **C1/C2 scope:** I will be the assertion runner + receipt assembler. In **C2**, I am additionally the ONLY sandbox-browser owner: I will launch/teardown the two sandbox instances (profiles `sandbox/profiles/writerA|B`, `--no-first-run`, no startup window where possible, CDP via `DevToolsActivePort`) under broker target leases, registered in the ledger before any observer attaches.
- **C3 scope:** I will be the single serialized **cua/AX actor**. I will execute exactly the scripted action(s) on a SANDBOX window only, and only while holding the exclusive machine-wide desktop-control lease. I will also stage the deliberate second cua request that the broker must deny/queue (the serialization proof).
- **C4 scope:** I will create the prepare-only run sheet + freeze-drill checklist; no execution.
- **Lease protocols:** No lease → no action; re-verification failure → stop + `bridge_loss` entry, never falling back to the frontmost window.
- **Write areas:** strictly limited to `canaries/`, `receipts/c*/pass*/`, `canaries/_tmp_wone_*`, and ledger appends (actor `wone`).
- **Prohibitions / Held gates:** I will not touch the default Chrome/Flow window, credentials/sign-in, submissions, perform any cua action without the desktop-control lease, or use any un-reviewed harness in a live rung.
- **STOP rule:** I have STOP authority and will invoke it immediately upon any violation or failure.

No action or inspection was performed as part of this ACK.

WONE_ACK_RECORDED_20260714T034720Z
