import LabConfigurator from "./LabConfigurator";
import RecentRuns from "./RecentRuns";

export const metadata = {
  title: "NebulaMind Lab — Autonomous Galaxy-Evolution Research",
  description:
    "An autonomous pipeline that reads the literature, maps the open frontiers, runs studies on public data, and writes peer-review-style papers.",
};

const STEPS = [
  { n: "01", t: "Read the literature", d: "Pull ~12,000 refereed galaxy-evolution papers from NASA ADS and embed every abstract into a vector space." },
  { n: "02", t: "Map the frontiers", d: "Cluster the corpus into research topics and overlay open debates + unknowns from the review base — the unsettled areas rise to the top." },
  { n: "03", t: "Run the study", d: "Pick a frontier and analyze real public data — SDSS SkyServer, JWST catalogs via VizieR, IllustrisTNG — end to end." },
  { n: "04", t: "Write the paper", d: "Draft an AASTeX manuscript with figures and honest caveats, compiled to PDF." },
  { n: "05", t: "Adversarial review", d: "Iterate against a Deep-Research review loop that flags overclaims and errors until the science holds." },
];

const STUDIES = [
  { title: "Open Research Frontiers", tag: "the map", href: "https://nebulamind.net/wiki/galaxy-evolution-open-research-frontiers",
    d: "A bottom-up map of where the field is most actively unsettled, drawn from 12k papers + the review base." },
  { title: "Does IllustrisTNG make enough massive galaxies early enough?", tag: "DR-reviewed · native measurement", href: "https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-massive-galaxies-draft.pdf",
    d: "A stellar-mass-function stress test vs the JWST massive-galaxy tension, with a Boylan-Kolchin baryon-budget check and a native centrals+M200c efficiency. Passed a 6-cycle Deep-Research review." },
  { title: "Scaling relations from z≈0 to the JWST frontier", tag: "calibration-verified", href: "https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf",
    d: "The main sequence & mass–metallicity relation from SDSS out to JWST z≈4–9, on a matched Tₑ-anchored abundance scale." },
  { title: "Calibration is not validation: IllustrisTNG vs SDSS + JWST", tag: "calibration-verified", href: "https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf",
    d: "Confronting the flagship simulation with observed scaling-relation evolution across z≈0–6." },
  { title: "SDSS mass–metallicity relation & the FMR aperture", tag: "z≈0 anchor", href: "https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-mzr-fmr-draft.pdf",
    d: "The local chemical-evolution anchor the frontier studies are measured against." },
];

export default function LabPage() {
  return (
    <main style={{ minHeight: "100vh", background: "var(--lab-bg)", color: "var(--lab-ink)" }}>
      <style>{`
        :root{ --lab-bg:#0a0d17; --lab-panel:#111524; --lab-ink:#e8ecf5; --lab-soft:#9aa3b8; --lab-line:#242a3d; --lab-accent:#7c86ff; --lab-accent2:#4ad6c4; }
        .lab-wrap{max-width:1000px;margin:0 auto;padding:0 1.25rem}
        .lab-hero{padding:5rem 0 3rem;border-bottom:1px solid var(--lab-line)}
        .lab-eyebrow{font-family:ui-monospace,monospace;font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:var(--lab-accent2);margin:0 0 1rem}
        .lab-h1{font-size:clamp(2.1rem,6vw,3.5rem);line-height:1.05;font-weight:700;letter-spacing:-.02em;margin:0 0 1rem;text-wrap:balance}
        .lab-h1 b{background:linear-gradient(120deg,var(--lab-accent),var(--lab-accent2));-webkit-background-clip:text;background-clip:text;color:transparent;font-weight:700}
        .lab-lede{font-size:clamp(1.05rem,2.5vw,1.3rem);color:var(--lab-soft);max-width:60ch;line-height:1.6;margin:0 0 1.75rem}
        .lab-cta{display:inline-flex;gap:.5rem;align-items:center;background:var(--lab-accent);color:#0a0d17;font-weight:600;padding:.7rem 1.2rem;border-radius:10px;text-decoration:none;font-size:.95rem}
        .lab-cta.ghost{background:transparent;color:var(--lab-ink);border:1px solid var(--lab-line);margin-left:.6rem}
        .lab-sec{padding:3.25rem 0;border-bottom:1px solid var(--lab-line)}
        .lab-kicker{font-family:ui-monospace,monospace;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--lab-soft);margin:0 0 1.25rem}
        .lab-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1px;background:var(--lab-line);border:1px solid var(--lab-line);border-radius:14px;overflow:hidden}
        .lab-step{background:var(--lab-panel);padding:1.3rem 1.15rem}
        .lab-step .num{font-family:ui-monospace,monospace;font-size:.8rem;color:var(--lab-accent);margin:0 0 .55rem}
        .lab-step h3{font-size:1rem;margin:0 0 .4rem;font-weight:650}
        .lab-step p{font-size:.85rem;color:var(--lab-soft);margin:0;line-height:1.5}
        .lab-studies{display:flex;flex-direction:column;gap:.8rem}
        .lab-card{display:block;background:var(--lab-panel);border:1px solid var(--lab-line);border-radius:12px;padding:1.1rem 1.25rem;text-decoration:none;transition:border-color .15s,transform .15s}
        .lab-card:hover{border-color:var(--lab-accent);transform:translateY(-1px)}
        .lab-card .row{display:flex;justify-content:space-between;gap:1rem;align-items:baseline;flex-wrap:wrap}
        .lab-card h3{font-size:1.02rem;margin:0;color:var(--lab-ink);font-weight:650;line-height:1.3}
        .lab-card .tag{font-family:ui-monospace,monospace;font-size:.68rem;letter-spacing:.06em;color:var(--lab-accent2);white-space:nowrap;flex-shrink:0}
        .lab-card p{font-size:.88rem;color:var(--lab-soft);margin:.5rem 0 0;line-height:1.55}
        .lab-note{font-size:.85rem;color:var(--lab-soft);line-height:1.65;max-width:62ch}
        .lab-foot{padding:2.5rem 0 4rem;color:var(--lab-soft);font-size:.83rem}
        .lab-foot a{color:var(--lab-accent)}
        .lab-topbar{height:56px;position:sticky;top:0;z-index:10;border-bottom:1px solid var(--lab-line);background:rgba(10,13,23,.82);backdrop-filter:blur(8px)}
        .lab-topbar .row{display:flex;justify-content:space-between;align-items:center;height:100%}
        .lab-brand{font-weight:600;font-size:.95rem;letter-spacing:-.01em;color:var(--lab-ink);text-decoration:none}
        .lab-brand b{color:var(--lab-accent2);font-weight:600}
        .lab-back{color:var(--lab-soft);text-decoration:none;font-size:.82rem;font-family:ui-monospace,monospace}
        .lab-back:hover{color:var(--lab-ink)}
      `}</style>

      <nav className="lab-topbar">
        <div className="lab-wrap row">
          <a className="lab-brand" href="/">◆ NebulaMind&nbsp;<b>Lab</b></a>
          <a className="lab-back" href="https://nebulamind.net">nebulamind.net ↗</a>
        </div>
      </nav>

      <div className="lab-wrap">
        <header className="lab-hero">
          <p className="lab-eyebrow">NebulaMind Lab</p>
          <h1 className="lab-h1">Autonomous <b>galaxy-evolution research.</b></h1>
          <p className="lab-lede">
            A pipeline that reads the literature, maps where the field is unsettled, runs the studies on public
            data, and writes peer-review-style papers — then defends them against an adversarial review loop.
          </p>
          <div>
            <a className="lab-cta" href="https://nebulamind.net/wiki/galaxy-evolution-open-research-frontiers">Explore the frontier map →</a>
            <a className="lab-cta ghost" href="https://nebulamind.net/research">See the papers</a>
          </div>
        </header>

        <section className="lab-sec">
          <p className="lab-kicker">Configure a run</p>
          <p className="lab-note" style={{ margin: "0 0 1.25rem" }}>
            Compose a study stage by stage — topic → data → research → paper — and assemble a
            reproducible run spec.
          </p>
          <LabConfigurator />
        </section>

        <section className="lab-sec">
          <p className="lab-kicker">How it works</p>
          <div className="lab-steps">
            {STEPS.map((s) => (
              <div className="lab-step" key={s.n}>
                <p className="num">{s.n}</p>
                <h3>{s.t}</h3>
                <p>{s.d}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="lab-sec">
          <p className="lab-kicker">Studies produced so far</p>
          <div className="lab-studies">
            {STUDIES.map((s) => (
              <a className="lab-card" href={s.href} key={s.title}>
                <div className="row">
                  <h3>{s.title}</h3>
                  <span className="tag">{s.tag}</span>
                </div>
                <p>{s.d}</p>
              </a>
            ))}
          </div>

          <p className="lab-note" style={{ margin: "1.75rem 0 1rem", color: "var(--lab-soft)" }}>
            Runs from the configurator above — each is a live study with its figure, compiled AASTeX
            manuscript, and the automated referee&rsquo;s review–revise verdict.
          </p>
          <RecentRuns />
        </section>

        <section className="lab-sec">
          <p className="lab-kicker">Desktop companion</p>
          <a className="lab-card" href="https://github.com/star4citizen/Astro-NoteAI" target="_blank" rel="noopener noreferrer">
            <div className="row">
              <h3>Astro-Note AI — turn your own papers into a local LLM wiki</h3>
              <span className="tag">open source · macOS/Win/Linux</span>
            </div>
            <p>
              An open-source desktop app that turns your research-paper PDFs into a private, LLM-powered wiki
              — with summaries, a knowledge graph, and chat over your papers. The local companion to NebulaMind, by Suk Kim.
            </p>
            <p style={{ margin: ".6rem 0 0", color: "var(--lab-accent)", fontFamily: "ui-monospace,monospace", fontSize: ".8rem" }}>
              Get Astro-Note AI on GitHub →
            </p>
          </a>
        </section>

        <section className="lab-sec">
          <p className="lab-kicker">What this is</p>
          <p className="lab-note">
            NebulaMind Lab is the research-automation engine behind <a href="https://nebulamind.net" style={{ color: "var(--lab-accent)" }}>nebulamind.net</a>.
            Where the wiki organizes what is known, the Lab pushes on what isn&rsquo;t — turning a corpus of papers into
            a ranked map of open questions, then working those questions with real public data. Every study is
            reproducible from public queries, states its caveats plainly, and is hardened through iterative review
            before it is presented as anything more than a draft.
          </p>
        </section>

        <footer className="lab-foot">
          <p>
            NebulaMind Lab · part of <a href="https://nebulamind.net">nebulamind.net</a> · studies use public data
            (SDSS, VizieR/JWST, IllustrisTNG) and are fully reproducible.
          </p>
        </footer>
      </div>
    </main>
  );
}
