export const metadata = {
  title: "NebulaMind — an AI scientist for galaxy evolution",
  description:
    "NebulaMind is an AI scientist that automates astronomical research — reading the literature, mapping open frontiers, running studies on public data, and writing peer-review-style papers. Its focus: galaxy evolution.",
};

export default function HomePage() {
  return (
    <main className="home">
      <style>{`
        :root{ --lab-bg:#0a0d17; --lab-panel:#111524; --lab-ink:#e8ecf5; --lab-soft:#9aa3b8; --lab-line:#242a3d; --lab-accent:#7c86ff; --lab-accent2:#4ad6c4; }
        .home{min-height:100vh;background:var(--lab-bg);color:var(--lab-ink);display:flex;flex-direction:column}
        .h-wrap{max-width:1000px;margin:0 auto;padding:0 1.25rem;width:100%}
        .h-topbar{height:56px;position:sticky;top:0;z-index:10;border-bottom:1px solid var(--lab-line);background:rgba(10,13,23,.82);backdrop-filter:blur(8px)}
        .h-topbar .row{display:flex;justify-content:space-between;align-items:center;height:100%}
        .h-brand{font-weight:600;font-size:.95rem;color:var(--lab-ink);text-decoration:none}
        .h-nav{display:flex;gap:1.3rem;align-items:center}
        .h-nav a{color:var(--lab-soft);text-decoration:none;font-size:.85rem;transition:color .12s}
        .h-nav a:hover{color:var(--lab-ink)}
        .h-nav a.mono{font-family:ui-monospace,monospace;font-size:.8rem}
        .h-main{flex:1;display:flex;align-items:flex-start;padding:clamp(2rem,8vh,4rem) 0 2.5rem}
        .h-eyebrow{font-family:ui-monospace,monospace;font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:var(--lab-accent2);margin:0 0 .8rem}
        .h-h1{font-size:clamp(2.1rem,6vw,3.5rem);line-height:1.05;font-weight:700;letter-spacing:-.025em;margin:0 0 1rem;text-wrap:balance}
        .h-h1 b{background:linear-gradient(120deg,var(--lab-accent),var(--lab-accent2));-webkit-background-clip:text;background-clip:text;color:transparent;font-weight:700}
        .h-lede{font-size:clamp(1rem,2.2vw,1.2rem);color:var(--lab-soft);max-width:62ch;line-height:1.6;margin:0 0 1.6rem}
        .h-cta{display:inline-flex;gap:.5rem;align-items:center;background:var(--lab-accent);color:#0a0d17;font-weight:600;padding:.75rem 1.35rem;border-radius:10px;text-decoration:none;font-size:.98rem}
        .h-cta.ghost{background:transparent;color:var(--lab-ink);border:1px solid var(--lab-line);margin-left:.6rem}
        .h-cta.ghost:hover{border-color:var(--lab-accent)}
        .h-video{width:100%;max-width:720px;aspect-ratio:16/9;margin:1.9rem 0 0;border:1px solid var(--lab-line);border-radius:12px;overflow:hidden;background:#000}
        .h-video iframe{width:100%;height:100%;border:0;display:block}
        .h-foot{padding:1.4rem 0;border-top:1px solid var(--lab-line);color:var(--lab-soft);font-size:.8rem}
        .h-foot a{color:var(--lab-accent)}
        @media(max-width:560px){.h-nav a:not(.mono){display:none}}
      `}</style>

      <nav className="h-topbar">
        <div className="h-wrap row">
          <a className="h-brand" href="/">◆ NebulaMind</a>
          <div className="h-nav">
            <a href="/lab">The pipeline</a>
            <a href="/lab">The papers</a>
            <a className="mono" href="/classic">previous version ↗</a>
          </div>
        </div>
      </nav>

      <section className="h-main">
        <div className="h-wrap">
          <p className="h-eyebrow">AI Scientist · Astronomy</p>
          <h1 className="h-h1">An AI scientist for <b>galaxy evolution.</b></h1>
          <p className="h-lede">
            NebulaMind automates the research loop — reading the literature, mapping where the field is
            unsettled, running studies on real public data, and writing peer-review-style papers. Its focus:
            how galaxies form and evolve across cosmic time.
          </p>
          <div>
            <a className="h-cta" href="/lab">Explore the pipeline →</a>
          </div>
          <div className="h-video">
            <iframe
              src="https://www.youtube.com/embed/aa4SLbMn1z4"
              title="NebulaMind — An AI Scientist for Galaxy Evolution"
              loading="lazy"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            />
          </div>
        </div>
      </section>

      <footer className="h-foot">
        <div className="h-wrap">
          NebulaMind · an AI scientist automating astronomical research on public data (SDSS, VizieR/JWST,
          IllustrisTNG). Looking for the old encyclopedia? <a href="/classic">Previous version →</a>
        </div>
      </footer>
    </main>
  );
}
