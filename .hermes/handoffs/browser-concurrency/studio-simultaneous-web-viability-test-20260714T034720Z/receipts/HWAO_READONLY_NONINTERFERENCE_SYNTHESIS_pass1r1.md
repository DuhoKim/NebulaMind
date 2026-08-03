# HWAO read-only non-interference synthesis — XM-1 pass1r1

**Authorship: this is a Hwao read-only synthesis from existing receipts and recovery process-state. It is NOT an independent Yui observation and Yui did not countersign.** No browser interaction was performed to produce it.

Evidence reviewed:
- `receipts/archeval/xm1/pass1r1/XM1_HARNESS_RECEIPT.json`: `writerA=term-clean`; `pro_controller stopped=true / term-clean / exit 0`; drills `freeze_denies_both=true`, `partition_failclosed=true`; `node_exit=0`; transport `thunderbolt / fallback none`; `remote_controller_sha256` recorded (matched local).
- `receipts/archeval/xm1/pass1r1/XM1_RECEIPT.json`: writers scoped `host_id=studio` (writerA) and `host_id=macpro` (writerB), each an exact CDP `target_id` in a **non-default sandbox profile**; DOM/CDP only; every op broker-checked.
- Tori post-Ctrl-C recovery state (as reported): 0 local/remote task processes, `/tmp` nmbrk dirs = 0, pass1r1 absent both hosts pre-run, forward port free.

Findings (what the receipts/state support):
1. **The harness did not address the default Chrome profile or the user Flow window.** By construction it targets only the sandbox non-default profiles (`…/xm1/pass1r1/profiles/writerA` on Studio; `…/xm1_sandbox/pass1r1/writerB` on the Pro) and exact CDP target ids; DOM/CDP only, no `activate`, no global keyboard/pointer/clipboard. This is a statement about what the code does — **not** an observational "untouched throughout" sweep of those applications, which was not performed.
2. **Clean lifecycle on both hosts:** Studio writerA and the Pro controller terminated clean (exit 0) per the receipts; no orphaned sandbox Chrome or leftover sockets reported.
3. **Duplicate Hwao invocation REFUSED before execution** (nonempty-passdir guard) — the second call performed no browser/host action.
4. **No account/quota/sign-in/CAPTCHA surface and no submissions** appear in the run; writes were sandbox DOM/CDP to inert `about:blank` targets.

Note: an independent Flow-side Yui witness pass was not run in this scope; a genuine Yui non-interference observation would require Yui's own read-only check and is not represented here.

HWAO_READONLY_NONINTERFERENCE_SYNTHESIS_PASS1R1_20260714T034720Z
