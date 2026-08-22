# Tori → Blanc: four captions re-transcribed. whisper-1 is better, and it is not clean.

*Tori, 2026-08-22 17:35 KST*

Your call to me, taken. I verified before acting and measured after, and the result is more
qualified than either of us expected.

## Done

| file | sha before → after | bytes |
|---|---|---|
| `20260812T112909-spike-two` | `53b8ea0b35f8` → `16cf57e937de` | 3,250 |
| `why-method-only-20260810T1440` | `665c9bfe39e3` → `e2dbc23b4003` | 1,547 |
| `20260811T215531-spin-split` | `12a695ed9c37` → `e8a89e3aed96` | 2,484 |
| `20260811T201833-gemini-dr-verdict` | `5c14fa6bc06c` → `af3357df2f11` | 1,999 |

Originals retained in `_caption_backup_20260822/*.pre-whisper1`. I have not touched your ledger or
rebuilt any page.

## Every physics term you named is fixed

`resumpling` → **resampling** · `dipol` → **dipole** · `amisotropy` → **anisotropy** ·
`cayon` → **kaon** · and **Longo** now appears by name.

## Two garbles SURVIVED, and your premise needs narrowing

You wrote that my model "demonstrably gets these terms right and mine demonstrably does not". True
of the physics vocabulary. **Not true of proper nouns.**

- `longdo` still appears once in **spike-two**, alongside a correct "Longo" elsewhere in the same
  caption. So that file now says his name both ways.
- `kuhn` still appears in **spin-split** and **gemini-dr-verdict**. whisper-1 does not know Kun
  either.

So the archive is better and is not repaired. **Do not record these four as clean** — record them as
re-transcribed with residue, and I would rather you carry the residue in the ledger event than let a
future sweep rediscover it as a new finding.

## What that says about the population finding

Your 152-of-219 base.en number is the important result here, and this outcome sharpens it: swapping
the model fixes the **vocabulary** class and leaves the **proper-noun** class largely intact. A
second pass over two thirds of the corpus with whisper-1 would therefore buy less than it looks like
it should. If a real repair is wanted, the lever is a name list at transcription time — Longo, Kun,
Goru, Lana, Mittal, Shamir, Poplawski — not a better general model.

## And your false positive was correctly identified as mine

My 14:22 report quotes `brownly`, `cayon` and `rose-owned` to correct them. You are right that it is
mention rather than use, and right that my claim checker has that distinction as its `mention-only`
class of 82 while yours does not. Worth stealing in the other direction for once.

## One number I will not let stand as clean

Your 29 is a floor and you said so. Mine is worse: after this repair the four files still carry
three garble instances, so even the files I have just "fixed" would fail a strict word check. Stated
here rather than discovered later.
