# agy lane brief — website visual work (Blanc/OPS overhaul, 2026-08-20 night)

You are the agy seat in Blanc's overnight platoon. Repo: /Users/duhokim/NebulaMind/NebulaMind
(Next.js 14 App Router frontend in frontend/). Do the three tasks below, then write
DONE.md in THIS directory and stop. Do not commit — Blanc integrates and commits.

## Exclusive write area (touch NOTHING else)
- frontend/src/app/page.tsx
- frontend/src/app/contribute/page.tsx
- frontend/src/app/labTheme.ts        (new file you create)
- frontend/src/app/lab/page.tsx       (ONLY to import tokens from labTheme.ts)
- .hermes/handoffs/blanc-ops-overhaul-20260820/agy-website-lane/  (notes, _tmp_*, DONE.md)

## Task 1 — shared design tokens (do first)
The --lab-* CSS variable palette is declared twice (page.tsx and lab/page.tsx),
drifting. Create frontend/src/app/labTheme.ts exporting the palette as a single
CSS string constant (e.g. `export const LAB_TOKENS_CSS = ":root{--lab-bg:#0a0d17;...}"`)
using the values currently in lab/page.tsx (that's the canonical set). Both
page.tsx and lab/page.tsx consume it. lab/page.tsx: minimal change only.

## Task 2 — homepage upgrade (the main task)
frontend/src/app/page.tsx is a thin card (hero + one CTA + a YouTube iframe).
Rebuild it as a real landing page, dark, using the shared tokens:
- Hero: keep the honest positioning ("An AI scientist for galaxy evolution" —
  autonomous literature analysis, frontier ranking, draft studies under human
  review). NO invented metrics, NO claims of validated discoveries.
- "How it works" strip: the four Lab stages (topic → data → research → paper) —
  labels/descriptions exist in frontend/src/app/lab/stageData.ts; link each to
  /lab?tab=<stage>.
- Latest outputs section: pull from existing data modules
  (frontend/src/app/lab/FlagshipStudies.tsx constants, lab/paperVideos.ts) —
  show 3-4 items max, honest labels (e.g. "draft under review").
- Keep the intro video embed but below the fold.
- Footer row: links to /lab, /surveys, /news, /contact.
- CSS: import RawStyle from ./lab/rawStyle (NEVER a plain <style>{...}</style> —
  React escapes string children of <style> and breaks hydration).
- Page stays a server component if possible; keep it lightweight (no new deps,
  no client JS unless necessary).

## Task 3 — contribute page dark fix
frontend/src/app/contribute/page.tsx is styled light-on-light (invisible on the
dark chrome). Restyle it to the classic dark palette used by chrome pages
(bg #0f172a, panel #1e293b, border #334155, ink #f8fafc, muted #94a3b8,
accent #6366f1). Content unchanged.

## Verify before DONE
cd frontend && npx tsc --noEmit   (must pass)
Then write DONE.md here: what changed per file, tsc result, anything skipped.
