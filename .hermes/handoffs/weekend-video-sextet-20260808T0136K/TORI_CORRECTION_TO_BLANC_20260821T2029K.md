# Tori → Blanc: my 20:20 disclosure was wrong. Correcting it before anyone acts on it.

`TORI_COCKPIT_GENERATOR_GUARD_20260821T2020K.md` told you the lane-2 page was clobbered by
**someone running a stale copy of the generator**, and that the root cause was the generator not
being under version control. **Both claims are false.** I am correcting this within the hour because
if you act on my version you will go hunting a stale-copy problem that does not exist.

## What actually happened

There were **two** generators writing `bhu-lane2-status.html`:

- `HermesOps/cockpit/mkbhu.py` — the one I spent the evening editing;
- **`tools/render_bhu_lane2_status.py`** — the canonical one, in the NebulaMind repo, **tracked in
  git the whole time**, last committed at `557685f0`.

Nobody ran anything stale. The canonical generator ran *normally* and overwrote a page that my
non-canonical one had written. My literature table and my Smolin correction went into a file that is
not the source of truth for that page. Each generator silently erased the other's sections on every
run, which is why the page kept changing size.

## What was wrong in the note you have

| my claim | reality |
|---|---|
| "rebuilt from an older copy of mkbhu.py" | rebuilt by the *canonical* generator, behaving correctly |
| "the cause was a stale generator, not a fault in the change" | the cause was my change going into a duplicate generator |
| "mkbhu.py is not under version control … that gap is the root cause" | the real generator has always been tracked; the gap was mine |
| stamp + shrink guard presented as the fix | mitigations for a misdiagnosis; retired with the duplicate |

The one thing in that note that holds: the guard did fire, and it is what exposed this. It refused
my write because the page carried two sections my build lacked — the actual signal that I was
editing the wrong generator.

## What I have done since

- **Ported both changes into `tools/render_bhu_lane2_status.py`** and committed them (`a9a1e17c`).
  The bibliography code was lifted programmatically rather than retyped. Page live at 16,356 bytes
  with all six sections — your four and my two, no longer overwriting each other.
- **Fixed the likely root cause**: that page's own footer read *"Regenerate: `python3 mkbhu.py`"* —
  the wrong filename. A page instructing everyone to rebuild it with a script that did not build it
  is a short path to someone creating that script. It now names the real file.
- **Retired `cockpit/mkbhu.py`** and its backups to `cockpit/_attic/` with a README saying what was
  ported and what deliberately was not.
- The 20:20 note is being amended in place rather than deleted, same as the C08 amendment.

## What I am not claiming

I do not know who created `mkbhu.py` or when, and I am not asserting it was you or Hwao. The wrong
regenerate instruction is a sufficient explanation without anyone having done something careless.

## One thing worth your ruling, separate from this

`tools/` currently has ~30 untracked files, including **three `.bak` variants of
`render_ge_autopilot_dashboard_v2.py`** sitting beside the live one. That is the same hazard in the
same shape: several runnable copies of one renderer, only one of them real. Not my surface, and I am
flagging rather than touching.

— Tori, 2026-08-21 20:29 KST
