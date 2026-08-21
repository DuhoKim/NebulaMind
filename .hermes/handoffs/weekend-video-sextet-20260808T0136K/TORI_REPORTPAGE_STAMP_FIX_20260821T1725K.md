# Tori → Blanc: nm_report_page.py now shows the publish time when a report was held

Duho caught it: my report page read "20 Aug 2026 · 23:59 KST", which says it was written at the
last minute of the night before. It was — but it went live at **16:07 on the 21st**, after he told
me to publish it. The page claimed a date on which nobody could have read it.

Cause: `parse_stamp(stem)` derives the header from the FILENAME, which carries the render time.
The publish time was already recorded — `queue.json` has my file twice, `seq 24` (quiet, held) and
`seq 34` (live) — the renderer just never looked.

**Change** (backup `nm_report_page.py.pre-publishstamp`):

- new `publish_stamp(stem)` — finds the first non-quiet queue entry for the file and returns its
  stamp when it differs materially from the render stamp;
- header becomes `written … · published …` in that case, otherwise unchanged;
- **30-minute threshold**, because without it every report grew a dual stamp: Hwao's 15:18 reading
  published at 15:19 and read "written … · published …" for a one-minute render lag. Held readings
  are the case this exists for, not ordinary lag;
- `MON` promoted from a local inside `parse_stamp` to module scope so both use one table. That was
  a real bug in my first attempt — `NameError` on the first render — not a tidy-up.

Verified on three reports: mine shows both stamps; your 10:59 and Hwao's 15:18 are untouched.

This matters beyond my one report. Quiet hours mean **any** overnight reading is published hours
after it is written, so every held report has been carrying a misleading date.

— Tori, 2026-08-21 17:25 KST
