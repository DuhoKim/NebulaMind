> **AMENDED — this note's diagnosis is WRONG. See `TORI_CORRECTION_TO_BLANC_20260821T2029K.md`.**
> The page was not clobbered by a stale copy, and the generator was not un-versioned. There
> were two generators writing the same page, and I edited the non-canonical one. The stamp and
> guard described below were mitigations for a misdiagnosis and are retired. Kept unrewritten
> because the reasoning it records is what led to finding the real cause.

# Tori → Blanc + acquisition session: the lane-2 generator now stamps and guards itself

Disclosing as I act. **Cockpit rendering is the acquisition session's, not mine.** Duho directed
both changes; this records them because the generator itself cannot be committed — see the last
section, which is the part worth arguing about.

## What happened first

At **20:13 KST** `bhu-lane2-status.html` was rebuilt by something running an **older copy of
mkbhu.py**. It dropped from 12,791 to 8,314 bytes and silently lost two sections: the published-
literature table added this afternoon, and the factual correction to the Smolin sentence. Nothing on
the page indicated a regression — **a shorter page looks like a quieter day, not a stale build.**
Duho noticed it was missing; I did not.

Diagnosed and ruled out: `bibliography()` works (returns 41 elements standalone), the current
generator still calls it, `mkindex.py` only links to the page rather than writing it, and no cron
job touches the cockpit. The cause was a stale generator, not a fault in the change.

## Two changes, both tested

**1. Generator hash stamp.** The page footer now carries the sha12 of the script that built it, plus
a section census: `Built by mkbhu.py `539a991ed274` · sections: 3 gates · literature 28 · CNS correction
present`. The hash is computed from the running file, so it cannot misreport itself.
*Negative control:* rebuilding from the pre-bibliography generator produced a 4,773-byte page with no
stamp and no literature section — a stale build is now identifiable two ways.

**2. Shrink guard.** `refuse_if_shrinking()` compares the `<h2>` census of the new build against
the page already on disk and **refuses to write** if a section would be lost, exiting 3 and naming
what would go. It compares sections, not bytes, so content churn passes. Override is
`NM_ALLOW_SHRINK=1`, for when a section is genuinely meant to disappear.
*Tested three ways:* refuses a section-losing build; honours the override; no false positive on an
unchanged build.

**Limitation, stated in the docstring because it is the important one:** the guard lives in the
generator, so it only protects the path that runs *that* file. **An older copy has no guard and will
still overwrite.** That is exactly the 20:13 mechanism. I therefore parked the two pre-today
generators in `cockpit/_attic/`, matching the convention already used there. Remaining runnable:
`mkbhu.py` plus same-day rollbacks `.pre-genstamp` and `.pre-guard`, both of which contain the
literature section and would trip the guard rather than shrink the page.

Backups: `mkbhu.py.pre-genstamp`, `mkbhu.py.pre-guard`. Page live at 13,081 bytes, serving 200.

## The part worth arguing about

**`mkbhu.py` is not under version control.** HermesOps is not a git repository and the cockpit is
not mirrored into the NebulaMind repo. So:

- "an older copy of the generator" exists as loose `.pre-*` files rather than as history;
- nobody can diff what changed between two renders of a monitored surface;
- this disclosure note is the *only* durable record of tonight's change, and it lives in a different
  repository from the thing it describes.

The stamp and the guard are mitigations for a problem version control would remove. If the
acquisition session wants it, the cockpit generators are small and would sit naturally under
`tools/` or a `cockpit/` path in the main repo. **That is your surface and your call — I am
flagging it, not proposing to do it.**

— Tori, 2026-08-21 20:20 KST. Generator sha12 at time of writing: `539a991ed274`
