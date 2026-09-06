# Hwao branch protection verification

**PASS: GitHub rejected the non-fast-forward push, and the remote branch tip remained unchanged.**

Verified: 2026-09-06 10:46:31 KST

- Repository: `DuhoKim/NebulaMind`
- Branch: `feat/paper-workflow-v2`
- Authenticated GitHub account: `DuhoKim`
- Performed by: Codex, at the user's explicit request to enable and verify protection.

## Protection settings

Fresh GitHub API reads before and after the test confirmed:

| Setting | Verified value |
|---|---|
| Administrator enforcement | Enabled |
| Force pushes | Blocked |
| Branch deletion | Blocked |

## Actual rejection evidence

The probe used a temporary bare clone, separate from the shared working tree. A replacement commit kept the original file tree and parent commit, but changed the tip's identity. A local ancestry check confirmed that the proposed update was non-fast-forward. An explicit lease required the remote tip to match the recorded original revision.

Push exit code: **1**.

```text
To https://github.com/DuhoKim/NebulaMind.git
!	d883682d27a6064456349ed9fe2a4fd28e8fd79f:refs/heads/feat/paper-workflow-v2	[remote rejected] (protected branch hook declined)
Done
remote: error: GH006: Protected branch update failed for refs/heads/feat/paper-workflow-v2.        
remote: 
remote: - Cannot force-push to this branch        
error: failed to push some refs to 'https://github.com/DuhoKim/NebulaMind.git'
```

## Branch integrity

- Original tip: `92f27d3fad18d2fd1a01dc33d9b00211316d1bed`
- Proposed test tip: `d883682d27a6064456349ed9fe2a4fd28e8fd79f`
- Remote tip after rejection: `92f27d3fad18d2fd1a01dc33d9b00211316d1bed`
- Original and proposed file trees: identical.
- Original and final remote tips: identical.

Original graph (commit, parents):

```text
92f27d3fad18d2fd1a01dc33d9b00211316d1bed f3af0c896041a6f595f2d6684dd68b5a2059061e
f3af0c896041a6f595f2d6684dd68b5a2059061e
```

Proposed graph (commit, parents):

```text
d883682d27a6064456349ed9fe2a4fd28e8fd79f f3af0c896041a6f595f2d6684dd68b5a2059061e
f3af0c896041a6f595f2d6684dd68b5a2059061e
```

The JSON receipt retains all observed settings and response details. The server-side copy is at `/private/tmp/hwao-branch-protection-bmoackf7/verification_receipt.json`.

This is Codex's execution receipt. It does not substitute for a principal signature, decide the outstanding study-review questions, or authorize resuming the research run. No branch deletion test was performed.

---
## Addendum by Hwao — who enabled protection, and independent confirmation (2026-09-06 10:55 KST)
**Duho enabled it via the codex CLI, confirmed in chat 2026-09-06 10:52 KST.** Blanc put the line "Performed by: Codex, at the user's explicit request to enable and verify protection" to Duho and asked whether he had asked codex to do it; Duho's verbatim answer: "yes, that was me, via Codex CLI Astra". Recorded in these terms, not as "a seat enabled protection": the principal acted, through the codex CLI, on his own account (`DuhoKim`).

Independent confirmations, three routes:
- Blanc, GitHub API before asking Duho: enforce_admins=true, allow_force_pushes=false, allow_deletions=false.
- Hwao, GitHub API at 2026-09-06T01:55:07Z (`gh api …/branches/feat/paper-workflow-v2/protection`): `{"allow_deletions":false,"allow_force_pushes":false,"enforce_admins":true}`.
- Hwao, remote tip at 10:53 KST: `92f27d3fad18…` = the receipt's original and post-rejection tip. Unchanged.

Receipt digests at filing: md (before this addendum) bb99d311a9cc2753…, json 99d32a913dcaa3ce…. The JSON's `result` = `VERIFIED_REJECTED_UNCHANGED`, `remote_tip_unchanged` = true. This satisfies the signed V15 §7 "Freeze witness" (line 56): verbatim server rejection of a non-fast-forward push, the local graphs proving it non-fast-forward, and Duho's chat confirmation. Item 3 DONE.
