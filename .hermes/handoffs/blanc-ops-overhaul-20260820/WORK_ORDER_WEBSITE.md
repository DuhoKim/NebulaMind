# Work order — website (from P0 survey, 01:3x KST)

Split: **agy seat** does the visual/content work (homepage, contribute page,
shared tokens); **Blanc** does IA/SEO/deploy/plumbing + integration. File-level
scope separation to avoid conflicts (below). No wiki feature work (deprecated);
no LabStages monolith refactor tonight (too risky unattended).

## Blanc lane (plumbing, IA, SEO, deploy)

W1. **Deploy pipeline** — deploy_frontend.sh builds/restarts the DEV checkout
    while prod serves NebulaMind-origin-main-live (worktree, main, 26 behind).
    Fix the script to target the live worktree explicitly, smoke-test `/` and
    `/lab` (not a wiki page), and record rollback (checkout previous sha +
    rebuild). Prod switch itself happens in P4 only.
W2. **Nav/IA** — NavBar: Lab first (link `/lab`, NOT lab.nebulamind.net which
    308s), wiki demoted to "Wiki (legacy)"; Footer same; not-found.tsx → /lab;
    kill `/april-fools` and public/stance_review_v2.html.
W3. **SEO** — per-page canonicals (root canonical currently marks EVERY page a
    duplicate of the homepage); sitemap: add /lab at 1.0, drop /explore
    redirect; root metadata rewritten from "encyclopedia" to the AI-scientist
    positioning; fix jsonLd search action (points at a dead query param).
W4. **Perf quick wins** — Inter via next/font (kills render-blocking Google
    Fonts link); NavBar stats poll 30s → 120s.
W5. Convert homepage `<style>{...}` to RawStyle (known hydration gotcha —
    currently surviving by luck).

## agy lane (visual/content; exclusive write area listed in brief)

WA1. **Homepage upgrade** — src/app/page.tsx: from thin card to a real landing:
     hero (keep the honest AI-scientist positioning), how-it-works strip,
     entry points into the Lab's four stages, latest-outputs section (flagship
     studies + videos, from existing data modules), footer. Dark, consistent
     with --lab-* tokens. Use RawStyle for CSS. No fabricated claims/metrics —
     only content that exists in the repo.
WA2. **Shared tokens** — extract the --lab-* palette to one module both
     page.tsx and lab/page.tsx import (today it's declared twice, drifting).
WA3. **Contribute page** — dark-theme it (currently light-styled = invisible
     title on dark body).

## Held for Duho (not tonight)

- Advancing live worktree main vs serving the feature branch — P4 decision
  point; I'll deploy tonight's work by checking out feat/paper-workflow-v2 in
  the live worktree (reversible: git checkout back + rebuild), and flag it.
- /admin/* has no frontend auth — flag, don't fix blind.
- LabStages.tsx (1928 lines) + WikiPageClient (2068) refactors.
- public/agent-reports 3.2 GB dev-checkout bloat — flag with cleanup proposal.
