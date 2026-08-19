# agy website lane - DONE

## What changed per file:
- `frontend/src/app/labTheme.ts`: Created new file exporting `LAB_TOKENS_CSS` with the canonical dark palette CSS variables.
- `frontend/src/app/lab/page.tsx`: Replaced hardcoded CSS variables with the shared `LAB_TOKENS_CSS` import. Minimal change as requested.
- `frontend/src/app/page.tsx`: Rebuilt the homepage as a dark landing page. Maintained honest positioning in the hero. Added a "How it works" strip linking the four Lab stages to `/lab?tab=<stage>`. Pulled the 4 latest flagship outputs from `FLAGSHIP` in `FlagshipStudies.tsx`. Included the existing YouTube iframe below the fold. Added a footer with the requested links. Kept it as a server component using `RawStyle`.
- `frontend/src/app/contribute/page.tsx`: Translated the light mode palette to the requested classic dark palette (`bg #0f172a`, `panel #1e293b`, `border #334155`, `ink #f8fafc`, `muted #94a3b8`, `accent #6366f1`). Content unchanged.

## Verification
`npx tsc --noEmit` ran in `frontend/` and passed successfully (exit code 0).

## Anything skipped
No requirements were skipped.
