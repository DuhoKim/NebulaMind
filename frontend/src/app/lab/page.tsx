import LabStages from "./LabStages";
import LabTopTabs from "./LabTopTabs";
import DesktopCompanion from "./DesktopCompanion";
import { RawStyle } from "./rawStyle";

export const metadata = {
  title: "The pipeline — NebulaMind",
  description: "How NebulaMind composes a study: topic → data → research → paper, on real public data.",
};

export default function PipelinePage() {
  return (
    <main style={{ minHeight: "100vh", background: "var(--lab-bg)", color: "var(--lab-ink)" }}>
      <RawStyle css={`
        :root{ --lab-bg:#0a0d17; --lab-panel:#111524; --lab-ink:#e8ecf5; --lab-soft:#9aa3b8; --lab-line:#242a3d; --lab-accent:#7c86ff; --lab-accent2:#4ad6c4; }
        .lab-wrap{max-width:1000px;margin:0 auto;padding:0 1.25rem}
        .lab-sec{padding:2.1rem 0;border-bottom:1px solid var(--lab-line)}
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
        .lab-back{color:var(--lab-soft);text-decoration:none;font-size:.82rem;font-family:ui-monospace,monospace}
        .lab-back:hover{color:var(--lab-ink)}
        .lab-toptabs{display:flex;gap:.1rem}
        .lab-toptab{position:relative;background:transparent;border:none;color:var(--lab-soft);font-size:.86rem;font-weight:500;padding:.45rem .75rem;border-radius:7px;cursor:pointer;font-family:inherit;transition:color .12s}
        .lab-toptab:hover{color:var(--lab-ink)}
        .lab-toptab.on{color:var(--lab-ink)}
        .lab-toptab.on::after{content:"";position:absolute;left:.75rem;right:.75rem;bottom:-.55rem;height:2px;background:var(--lab-accent);border-radius:2px}
        .lab-tt{position:relative}
        .lab-caret{font-size:.58rem;opacity:.55;margin-left:.12rem}
        .lab-dd{position:absolute;top:calc(100% + .45rem);left:0;min-width:230px;background:var(--lab-panel);border:1px solid var(--lab-line);border-radius:10px;padding:.3rem;z-index:30;box-shadow:0 10px 28px rgba(0,0,0,.45);display:flex;flex-direction:column;gap:.08rem}
        .lab-dd button{background:transparent;border:none;color:var(--lab-soft);text-align:left;font-size:.85rem;padding:.45rem .6rem;border-radius:7px;cursor:pointer;font-family:inherit;white-space:nowrap}
        .lab-dd button:hover{background:rgba(124,134,255,.12);color:var(--lab-ink)}
        .lab-dd button.on{color:var(--lab-ink);font-weight:600}
        .lab-dd button.on::before{content:"›";color:var(--lab-accent);margin-right:.4rem;margin-left:-.15rem}
        .lab-dd-sep{height:1px;background:var(--lab-line);margin:.25rem .35rem}
        .lab-toptab.on::after{content:"";position:absolute;left:.75rem;right:.75rem;bottom:-.55rem;height:2px;background:var(--lab-accent);border-radius:2px}
        #pipeline{scroll-margin-top:72px}
        @media(max-width:760px){.lab-back{display:none}}
        @media(max-width:560px){.lab-toptab{padding:.4rem .5rem;font-size:.8rem}}
      `} />

      <nav className="lab-topbar">
        <div className="lab-wrap row">
          <a className="lab-brand" href="/">NebulaMind</a>
          <LabTopTabs />
          <a className="lab-back" href="/">← home</a>
        </div>
      </nav>

      <div className="lab-wrap">
        <section className="lab-sec" id="pipeline" style={{ paddingTop: "1.6rem" }}>
          <LabStages />
        </section>

        <DesktopCompanion />
      </div>
    </main>
  );
}
