# PUBLICATION OF THE FAILED ATTEMPT — what is verified, and what is not (2026-09-07 20:42 KST)
**This is publication of a FAILED ATTEMPT. It is NOT an INPUT anchor**, and nothing here is used to designate a round.
## VERIFIED
Codex fetched the remote bytes and compared them (`hwao-seed-abort-publication-20260907.json`, observed `2026-09-07T11:40:26.836Z`):
- commit `01a4ef889f8b6bf9280505ab9e6553b308aca8f7` carries `OUT_A1_FRESH/seed.abort.json`, 849 bytes, sha256 `bd212ede89e73a15905b04f4df7396d99c39362fe555b615cea6b43be87e4380`
- `local_remote_byte_equal: true` — the published bytes are the bytes we hold
## NOT VERIFIED, AND NOT CLAIMED
`push_event: null` — **no PushEvent was returned for that commit, so there is no verified provider publication time.** The commit's authored date (`11:28:56Z`) is **not** a provider publication timestamp and is not used as one. My earlier report cited that date next to the publication; I am correcting that here rather than leaving the two adjacent and letting a reader fuse them. The anchor commit `c962508e` did have a returned event (`20327776882`, `11:16:49Z`); this one did not, and absence of a returned event is not evidence of non-publication — the bytes are demonstrably on the remote.
## THE MINIMAL ABORT TIMESTAMP, RETAINED
The one time that matters for the failed attempt is the abort's own, produced by the run: **`2026-09-07T11:27:19.953808Z`**, `UNREGISTERED-RUNTIME-MODULE: encodings.idna`, in `OUT_A1_FRESH/seed.abort.json`. It is retained as-is.

## CORRECTION (2026-09-07 20:46 KST) — I WAS WRONG THAT AN ABORT NEEDS NO EXTERNAL TIMESTAMP
I wrote that the failed attempt "does not need one". **A1's Attempts and refusals clause says the opposite, verbatim:** *"Apply the SAME minimal anchor rule above to every record: a third party records the pushed commit's server-side timestamp, OR someone who is not the lane owner externally states the record's digest with a provider timestamp; the external-statement alternative does not waive the required push."* Every attempt and abort record carries the same anchor obligation as the input freeze.
**Status of that obligation for this abort — split into its two halves:**
- **Required push: SATISFIED.** The record is on the public remote at commit `01a4ef889f8b…`, remote bytes byte-equal to ours (`bd212ede…`).
- **Third-party timestamp: UNRESOLVED.** No PushEvent was returned for that commit, and no non-owner has externally stated the record's digest with a provider timestamp. The commit's authored date is not one, and the abort's own `11:27:19.953808Z` is the failure time, not a publication time.
**This obligation stays OPEN in the record rather than being explained away.** An ABORT-EVIDENCE ANCHOR is a different thing from a fresh INPUT anchor: it timestamps a failure that already happened and designates nothing, so satisfying it is not a restart and does not touch the unauthorized-restart boundary. I have not created either one, and I am not treating the gap as harmless.
Round 6444980 remains exposed and unusable for this study. Both journals and every frozen byte are untouched. Repair job `bh12roicm` continues.


## RESOLVED (2026-09-07 21:06 KST) — the third-party timestamp exists after all
GitHub's **repository activity** feed (`GET /repos/DuhoKim/NebulaMind/activity?activity_type=push`) supplies it: activity `42813554986`, ref `refs/heads/feat/paper-workflow-v2`, `after 01a4ef889f8b6bf9280505ab9e6553b308aca8f7`, **`timestamp 2026-09-07T11:29:02Z`** — a server-side time, not the commit author date and not a local file time. With the push already satisfied and the bytes byte-equal (`bd212ede…`, 849 bytes), **the abort record's anchor obligation is now MET**.
The earlier `push_event: null` from the *events* feed stays in this record as historical evidence and is not overwritten: the events feed returned nothing, the activity feed did. I had treated the events feed as the only witness; it was not. Obtaining this changed nothing about the run — it timestamps a failure that already happened and designates nothing.
