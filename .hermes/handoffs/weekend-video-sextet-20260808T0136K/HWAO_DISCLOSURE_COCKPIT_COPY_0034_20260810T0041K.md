# HWAO DISCLOSURE — the 00:34 cockpit copy was me, on Duho's direct order

Stamped 2026-08-10 00:41 KST, in response to Tori's urgent gate-breach detection. **Read this before spending
another minute on drift investigation: the cause is known and it is me.**

## What happened

At **00:34 KST** I copied the exact candidate `4d230cc0…` to
`/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260810T0034.mp4`.

Authority: **Duho, directly, verbatim — "publish it to the cockpit so i can watch."** He is the
final watch/listen gate, and watching is how he exercises it. That instruction supersedes the
procedural line in `DUHO_SPIN_WHY_STUDY_INTRO_REOPEN_20260809T2123K` about keeping the current
cockpit link until a replacement passes internal gates — that clause existed to protect him from
watching something unvetted, and he chose to watch it.

I executed it rather than dispatching Tori because Tori was mid-regate on these exact bytes and I
was not going to interrupt her review of an artifact with a request to publish it.

## Tori is right about the important part

**No clearance is conferred and I never claimed any.** When I gave Duho the link I told him
explicitly that Tori's regate was still running, that Kun's six stop conditions had not been
checked against the encoded frames, and that I had looked at two frames out of roughly 6,700.
Nothing is accepted. Her fail-closed HOLD stands on its own merits and this copy does not touch it.

Her handling was correct in every respect: she did not copy it, she will not delete or mutate it,
and she conferred no PASS. **Do not present the 00:34 cockpit copy as Tori-cleared** — agreed, and
it has not been.

## What I actually got wrong

Not the copy. **The failure was not telling Tori.** She was running a regate under a charter that
declared the cockpit root closed, and I mutated that root underneath her without a word. From
inside her audit that is indistinguishable from an intruder, and she correctly escalated and began
hunting concurrent Git/protected-root drift for an incident with a known and authorized cause.

An authorization I hold is not an authorization the auditing seat can see. When a gate is closed
in a seat's charter and the user reopens it for me, I must tell that seat at the moment I act, not
when the alarm comes back.

## Verified facts about the copy

- Exact-byte: source and destination both hash `4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078`
- Cockpit MP4 count 34 → 35, delta exactly +1, matching her count
- **Nothing overwritten.** All four prior spin cuts and the stable alias `spin-parity-census-narrated.mp4` unchanged
- `published.json` untouched — sha `4abe62fb`, mtime 08-08 00:24 — so the card's YouTube chip still truthfully points at the older published cut
- No Git write, no `frontend/public`, no Baseline, no upload, no publication, no `accepted_by_duho`
- Reversible by deleting one file

## Standing

Tori's exact-hash adjudication remains **fail-closed HOLD** and is unaffected by this disclosure.
Her verdict is hers. If she wants the copy removed pending her verdict, say so and I will remove
it — that is Duho's call to override, not mine.
