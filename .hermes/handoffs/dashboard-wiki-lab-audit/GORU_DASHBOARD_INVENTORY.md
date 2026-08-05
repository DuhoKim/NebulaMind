# Dashboard WIKI vs LAB Inventory
This document contains an inventory of code locations mixing the OLD-WIKI-era settings with the CURRENT AI Lab setting.

## (1) Site Middleware and Host Routing
**frontend/src/middleware.ts**
- Line 17: `  if (host.startsWith("lab.")) {`
- Line 18: `    return NextResponse.redirect(\`https://nebulamind.net\${pathname}\${search}\`, 308);`
- Line 21: `  return forward(req, pathname);`
*(Findings: The lab subdomain redirects to root. The default behavior does not implicitly route to /wiki anymore. The root `/` path is passed forward to `page.tsx`, which serves a Lab-focused homepage.)*

## (2) Root Layout and Nav/Tab/Menu Components
### WIKI-ONLY (safe to retire)
**frontend/src/app/autowiki/page.tsx**
- Line 88: `          ⚡ Autowiki Loop`
- Line 91: `          Continuous AI-driven wiki improvement — AstroSage-70B drafts, Atom-7B gates, Rakon judges.`

**frontend/src/app/admin/autowiki/page.tsx**
- Line 637: `        Loading autowiki dashboard…`
- Line 652: `          ⚡ Autowiki Loop`

**frontend/src/app/classic/page.tsx**
- Line 25: `          <strong style={{ color: "#a5b4fc" }}>Early-stage wiki — content is actively being built.</strong>{" "}`
- Line 27: `          <a href="/wiki/galaxy-evolution" style={{ color: "#818cf8", textDecoration: "underline" }}>Galaxy Evolution</a>{" "}`
- Line 53: `              href="/wiki"`
- Line 130: `      {/* Wiki Pages Grid */}`
- Line 153: `              href={\`/wiki/\${p.slug}\`}`

### MIXED (same surface serves both, needs a decision)
**frontend/src/app/layout.tsx**
- Line 84: `  const standalone = pathname === "/" || pathname === "/lab" || pathname.startsWith("/lab/");`
*(Findings: Layout explicitly breaks out `/lab` and root `/` into standalone, but wraps everything else in classic chrome. Needs decision if non-Lab surfaces should persist).*

**frontend/src/app/components/NavBar.tsx**
- Line 6: `  { href: "/wiki", label: "Wiki" },`
- Line 9: `  { href: "https://lab.nebulamind.net", label: "Lab" },`

**frontend/src/app/components/Footer.tsx**
- Line 48: `                ["/wiki", "Wiki"],`
- Line 123: `              llm-wiki`

**frontend/src/app/FeaturedTopics.tsx**
- Line 6: `interface WikiPage {`
- Line 134: `            href={\`/wiki/\${page.slug}\`}`

**frontend/src/app/ActivityFeed.tsx**
- Line 78: `                    href={\`/wiki/\${a.page_slug}\`}`

**frontend/src/app/CommunitySpotlight.tsx**
- Line 93: `                        <Link key={slug} href={\`/wiki/\${slug}\`} style={{ fontSize: "0.75rem", color: "#4f46e5", textDecoration: "none", background: "#eef2ff", padding: "0.1rem 0.4rem", borderRadius: "9999px" }}>`
- Line 111: `              Enter an arXiv ID and our AI will generate a summary and link it to relevant wiki pages.`

**frontend/src/app/LatestResearch.tsx**
- Line 84: `                    <Link key={slug} href={\`/wiki/\${slug}\`}`

**frontend/src/app/explore/layout.tsx**
- Line 7: `  { label: "Cards", href: "/explore/cards" },`
- Line 8: `  { label: "Q&A", href: "/explore/qa" },`

## (3) Lab Surfaces
### LAB-ONLY (leave alone)
**frontend/src/app/lab/* **
*(Findings: The lab surfaces (`frontend/src/app/lab/methodLinks.tsx`, `frontend/src/app/lab/stageData.ts`, `frontend/src/app/lab/page.tsx`) do not link to `/wiki` at all. They correctly use standalone internal state routing.)*

## (4) Method Wikis M1/M2/M3 (PGR/SFA/DMW)
### WIKI-ONLY (safe to retire)
**frontend/src/app/wiki/[slug]/WikiPageClient.tsx**
- Line 135: `    href: "/wiki/galaxy-evolution-method-2-sfa",`
- Line 140: `    href: "/wiki/galaxy-evolution-method-3-dmw",`
- Line 1474: `  const showTopAuditPanels = !["galaxy-evolution","galaxy-evolution-method-1-pgr","galaxy-evolution-method-2-sfa","galaxy-evolution-method-3-dmw","galaxy-evolution-scaffolding"].includes(slug);`
- Line 1492: `      {["galaxy-evolution","galaxy-evolution-method-2-sfa","galaxy-evolution-method-3-dmw"].includes(slug) && <GalaxyMethodResultSelector isMobile={isMobile} currentSlug={slug} />}`

## (5) Surfaces Presenting Wiki as Primary Product
### MIXED (same surface serves both, needs a decision)
**frontend/src/app/page.tsx** (Root Page)
- Line 42: `            <a className="mono" href="/classic">previous version ↗</a>`
- Line 57: `            <a className="h-cta" href="/lab">Explore the pipeline →</a>`
- Line 74: `          IllustrisTNG). Looking for the old encyclopedia? <a href="/classic">Previous version →</a>`
*(Findings: The root page correctly presents the AI scientist/Lab as the primary product via CTA, but retains a "previous version" link pointing to the classic wiki. This fits into MIXED since it links to both paradigms).*

GORU_DASHBOARD_INVENTORY_COMPLETE
