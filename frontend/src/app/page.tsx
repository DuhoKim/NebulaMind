import { RawStyle } from "./lab/rawStyle";
import { LAB_TOKENS_CSS } from "./labTheme";
import { FLAGSHIP } from "./lab/flagshipData";
import { PAPER_VIDEOS } from "./lab/paperVideos";

export const metadata = {
  title: "NebulaMind — an AI scientist for galaxy evolution",
  description:
    "NebulaMind is an AI scientist that automates astronomical research — reading the literature, mapping open frontiers, running studies on public data, and writing peer-review-style papers.",
};

const LAB_STAGES = [
  { id: "topic", label: "Topic", desc: "Mapping the literature to find open frontiers." },
  { id: "data", label: "Data", desc: "Sourcing public data from SDSS, JWST, and IllustrisTNG." },
  { id: "research", label: "Research", desc: "Running the analysis and scaling relations." },
  { id: "paper", label: "Paper", desc: "Drafting the peer-review-style manuscript." }
];

export default function HomePage() {
  const latestOutputs = FLAGSHIP.slice(0, 4);

  return (
    <main className="home">
      <RawStyle css={`
        ${LAB_TOKENS_CSS}
        .home { min-height: 100vh; background: var(--lab-bg); color: var(--lab-ink); display: flex; flex-direction: column; }
        .h-wrap { max-width: 1000px; margin: 0 auto; padding: 0 1.25rem; width: 100%; }
        .h-topbar { height: 56px; position: sticky; top: 0; z-index: 10; border-bottom: 1px solid var(--lab-line); background: rgba(10,13,23,.82); backdrop-filter: blur(8px); }
        .h-topbar .row { display: flex; justify-content: space-between; align-items: center; height: 100%; }
        .h-brand { font-weight: 600; font-size: .95rem; color: var(--lab-ink); text-decoration: none; }
        .h-nav { display: flex; gap: 1.3rem; align-items: center; }
        .h-nav a { color: var(--lab-soft); text-decoration: none; font-size: .85rem; transition: color .12s; }
        .h-nav a:hover { color: var(--lab-ink); }
        .h-nav a.mono { font-family: ui-monospace, monospace; font-size: .8rem; }
        
        .hero { padding: clamp(3rem, 8vh, 6rem) 0; }
        .hero-eyebrow { font-family: ui-monospace, monospace; font-size: .72rem; letter-spacing: .22em; text-transform: uppercase; color: var(--lab-accent2); margin: 0 0 .8rem; }
        .hero-h1 { font-size: clamp(2.1rem, 6vw, 3.5rem); line-height: 1.05; font-weight: 700; letter-spacing: -.025em; margin: 0 0 1rem; text-wrap: balance; }
        .hero-h1 b { background: linear-gradient(120deg, var(--lab-accent), var(--lab-accent2)); -webkit-background-clip: text; background-clip: text; color: transparent; font-weight: 700; }
        .hero-lede { font-size: clamp(1rem, 2.2vw, 1.2rem); color: var(--lab-soft); max-width: 62ch; line-height: 1.6; margin: 0 0 2rem; }
        .h-cta { display: inline-flex; gap: .5rem; align-items: center; background: var(--lab-accent); color: #0a0d17; font-weight: 600; padding: .75rem 1.35rem; border-radius: 10px; text-decoration: none; font-size: .98rem; }
        
        .section { padding: 4rem 0; border-top: 1px solid var(--lab-line); }
        .sec-h2 { font-size: 1.5rem; font-weight: 650; margin: 0 0 1.5rem; }
        
        .steps-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }
        .step-card { background: var(--lab-panel); border: 1px solid var(--lab-line); padding: 1.5rem; border-radius: 12px; text-decoration: none; display: block; transition: border-color 0.2s, transform 0.2s; }
        .step-card:hover { border-color: var(--lab-accent); transform: translateY(-2px); }
        .step-label { font-family: ui-monospace, monospace; font-size: .75rem; color: var(--lab-accent); margin-bottom: .5rem; display: block; text-transform: uppercase; letter-spacing: .05em; }
        .step-title { font-size: 1.1rem; font-weight: 600; color: var(--lab-ink); margin: 0 0 .5rem; }
        .step-desc { font-size: .9rem; color: var(--lab-soft); line-height: 1.5; margin: 0; }
        
        .outputs-grid { display: flex; flex-direction: column; gap: 1rem; }
        .output-card { display: block; background: var(--lab-panel); border: 1px solid var(--lab-line); border-radius: 12px; padding: 1.5rem; text-decoration: none; transition: border-color .15s; }
        .output-card:hover { border-color: var(--lab-accent); }
        .out-status { font-family: ui-monospace, monospace; font-size: .75rem; color: var(--lab-accent2); margin-bottom: .8rem; display: block; text-transform: uppercase; letter-spacing: .05em; }
        .out-title { font-size: 1.1rem; font-weight: 650; margin: 0 0 .5rem; color: var(--lab-ink); line-height: 1.3; }
        .out-summary { font-size: .9rem; color: var(--lab-soft); line-height: 1.6; margin: 0 0 1rem; }
        .out-meta { font-size: .8rem; color: var(--lab-soft); font-family: ui-monospace, monospace; opacity: 0.8; }
        
        .video-sec { padding: 4rem 0; border-top: 1px solid var(--lab-line); }
        .h-video { width: 100%; max-width: 800px; aspect-ratio: 16/9; margin: 0 auto; border: 1px solid var(--lab-line); border-radius: 12px; overflow: hidden; background: #000; }
        .h-video iframe { width: 100%; height: 100%; border: 0; display: block; }
        
        .h-foot { padding: 2rem 0; border-top: 1px solid var(--lab-line); margin-top: 2rem; }
        .foot-links { display: flex; gap: 1.5rem; flex-wrap: wrap; }
        .foot-links a { color: var(--lab-soft); text-decoration: none; font-size: .9rem; transition: color .12s; }
        .foot-links a:hover { color: var(--lab-ink); }
      `} />

      <nav className="h-topbar">
        <div className="h-wrap row">
          <a className="h-brand" href="/">NebulaMind</a>
          <div className="h-nav">
            <a href="/lab">The pipeline</a>
            <a href="/lab">The papers</a>
            <a className="mono" href="/classic">previous version ↗</a>
          </div>
        </div>
      </nav>

      <section className="hero h-wrap">
        <p className="hero-eyebrow">AI Scientist · Astronomy</p>
        <h1 className="hero-h1">An AI scientist for <b>galaxy evolution.</b></h1>
        <p className="hero-lede">
          NebulaMind automates the research loop — reading the literature, mapping where the field is unsettled, 
          running studies on real public data, and writing peer-review-style papers. All current studies are 
          descriptive drafts under human review; nothing is claimed as a validated discovery.
        </p>
        <a className="h-cta" href="/lab">Explore the pipeline →</a>
      </section>

      <section className="section h-wrap">
        <h2 className="sec-h2">How it works</h2>
        <div className="steps-grid">
          {LAB_STAGES.map((step, i) => (
            <a key={step.id} href={`/lab?tab=${step.id}`} className="step-card">
              <span className="step-label">Stage {i + 1}</span>
              <h3 className="step-title">{step.label}</h3>
              <p className="step-desc">{step.desc}</p>
            </a>
          ))}
        </div>
      </section>

      <section className="section h-wrap">
        <h2 className="sec-h2">Latest outputs</h2>
        <div className="outputs-grid">
          {latestOutputs.map(out => (
            <a key={out.pdf} href={out.pdf} target="_blank" rel="noopener noreferrer" className="output-card">
              <span className="out-status">Descriptive draft under review — {out.verdict}</span>
              <h3 className="out-title">{out.title}</h3>
              <p className="out-summary">{out.summary}</p>
              <div className="out-meta">{out.meta}</div>
            </a>
          ))}
        </div>
      </section>

      <section className="video-sec h-wrap">
        <div className="h-video">
          <iframe
            src="https://www.youtube.com/embed/aa4SLbMn1z4"
            title="NebulaMind — An AI Scientist for Galaxy Evolution"
            loading="lazy"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>
      </section>

      <footer className="h-foot">
        <div className="h-wrap foot-links">
          <a href="/lab">Lab</a>
          <a href="/surveys">Surveys</a>
          <a href="/news">News</a>
          <a href="/contact">Contact</a>
        </div>
      </footer>
    </main>
  );
}
