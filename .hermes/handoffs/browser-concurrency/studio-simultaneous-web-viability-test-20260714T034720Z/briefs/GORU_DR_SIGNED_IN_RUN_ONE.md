# GORU — signed-in Pro CDP target: run one bounded Deep Research job

Authority: `receipts/DUHO_PRO_CDP_SIGNED_IN.md`
Authority SHA-256: `4696ab43f6f4c3b9e21c2baa64f6e8e9f3c2dc5aa2f3a5c5d77f6fc55705c064`

Tori independently verified the loopback forward and page-only preflight:

- Studio CDP: `http://127.0.0.1:19223`
- Exact page target: `C92443095EE9116210C178D855DF3329`
- URL: `https://gemini.google.com/app`
- Title: `Google Gemini`
- Prompt editor: visible, role `textbox`, aria-label `Enter a prompt for Gemini`
- Relevant controls: `Upload & tools`; `Open mode picker, currently Pro`
- Page challenge: false — no page password input, reCAPTCHA, accounts redirect, or challenge dialog
- Chrome toolbar/profile UI was not inspected and is out of scope
- Studio broker UDS: `/tmp/nmbrk-live-20260714/b.sock`
- Broker is unfrozen; no account-submission lease was live at the verified snapshot

Bounded canary prompt:

> Using official Apple and Google Chrome documentation, explain in no more than eight bullets how a direct Thunderbolt Bridge between two Macs can support isolated browser automation. Include two limitations and source links.

Execution custody:

1. Attach only through Studio loopback port 19223. Before every write, rediscover `/json/list` and require the exact target ID and Gemini origin/path. Target drift is fail-closed.
2. Acquire one broker target write lease scoped to host `pro`, bundle `com.google.Chrome`, user-data-dir `dr-live-cdp-20260714`, window `pid-65195`, and exact target ID above. Maintain heartbeat while live.
3. Under target checks, open the page `Upload & tools` control and select the exact visible `Deep Research` option. If unavailable or ambiguous, stop. Confirm the page UI indicates Deep Research before entering the prompt.
4. Enter exactly the bounded prompt through DOM/CDP only. No clipboard, CUA, pointer, or global keyboard.
5. Immediately before the single submit, acquire the global broker `account-submission` lease. If held by Flow, do not submit; wait/report. With both leases checked and the target reverified, perform exactly one submit, capture submit UTC, and release the account-submission lease promptly.
6. After submit, capture the run-owned conversation's exact route/ID, exact title, and submit UTC. A real page-content challenge, CAPTCHA, sign-in wall, 2FA, permission prompt, accounts redirect, or target drift means broker freeze + STOP; do not solve.
7. Poll only the exact conversation until the DR result completes. Keep the target lease alive. No second submit, retry, or scale.
8. Save the complete result plus sources and exact conversation identity to a packet receipt/artifact. Compute SHA-256, append the result-save ledger entry, and require full ledger `VERIFY_OK`.
9. STOP BEFORE deletion and report the saved receipt/hash/ledger epoch to Tori. Tori will independently verify custody and then issue an exact-conversation deletion authorization. Never bulk delete or infer identity from title alone.
10. After a later Tori custody-verification dispatch only, delete exactly the positively matched run-owned conversation and ledger the deletion. If identity/custody is ambiguous, do not delete.

No agent may inspect credentials/cookies/tokens/profile files or touch account settings/passwords. One bounded run only.

GORU_DR_SIGNED_IN_RUN_ONE_20260714
