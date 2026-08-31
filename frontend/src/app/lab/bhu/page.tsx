import { RawStyle } from "../rawStyle";
import { LAB_TOKENS_CSS } from "../../labTheme";

export const metadata = {
  title: "Black-hole-universe — a personal side-interest · NebulaMind",
  description:
    "An adversarial audit of the published black-hole-universe literature: 58 papers tiered and double-gated. A personal side-interest, not a NebulaMind research programme.",
};

export default function BhuLabPage() {
  return (
    <main style={{ minHeight: "100vh", background: "var(--lab-bg)", color: "var(--lab-ink)" }}>
      <RawStyle
        css={`
        ${LAB_TOKENS_CSS}
        .bhu-wrap{max-width:900px;margin:0 auto;padding:0 1.25rem}
        .bhu-topbar{height:56px;position:sticky;top:0;z-index:10;border-bottom:1px solid var(--lab-line);background:rgba(10,13,23,.82);backdrop-filter:blur(8px)}
        .bhu-topbar .row{display:flex;justify-content:space-between;align-items:center;height:100%}
        .bhu-brand{font-weight:600;font-size:.95rem;color:var(--lab-ink);text-decoration:none}
        .bhu-back{color:var(--lab-soft);text-decoration:none;font-size:.82rem;font-family:ui-monospace,monospace}
        .bhu-back:hover{color:var(--lab-ink)}
        .bhu-hero{padding:2.4rem 0 1.4rem;border-bottom:1px solid var(--lab-line)}
        .bhu-kicker{font-family:ui-monospace,monospace;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--lab-soft);margin:0 0 .7rem}
        .bhu-hero h1{font-size:1.8rem;margin:0 0 .5rem;font-weight:680;letter-spacing:-.01em}
        .bhu-personal{display:inline-block;font-size:.76rem;color:#f0d9a8;background:#2a1f0e;border:1px solid #5a4415;border-radius:999px;padding:.2rem .7rem;margin-bottom:.9rem}
        .bhu-lede{font-size:1rem;color:var(--lab-soft);line-height:1.6;max-width:66ch;margin:0}
        .bhu-sec{padding:2rem 0;border-bottom:1px solid var(--lab-line)}
        .bhu-sec h2{font-size:1.15rem;margin:0 0 .3rem;font-weight:660;color:#9db8e8}
        .bhu-sec h2 .n{font-family:ui-monospace,monospace;color:var(--lab-accent);font-size:.9rem;margin-right:.5rem}
        .bhu-sub{font-size:.85rem;color:var(--lab-soft);margin:.1rem 0 1.1rem}
        .bhu-sec p{font-size:.92rem;color:var(--lab-ink);line-height:1.62;max-width:70ch}
        .bhu-sec p.soft{color:var(--lab-soft)}
        .bhu-scroll{overflow-x:auto;margin:1.1rem 0}
        table.bhu{border-collapse:collapse;width:100%;font-size:.85rem;min-width:520px}
        table.bhu th,table.bhu td{text-align:left;padding:.5rem .65rem;border-bottom:1px solid var(--lab-line);vertical-align:top}
        table.bhu th{color:var(--lab-soft);font-weight:500;font-size:.78rem;text-transform:uppercase;letter-spacing:.04em}
        .num{font-family:ui-monospace,monospace;color:var(--lab-accent2)}
        .fired{color:#ffb59e}.live{color:#8ee6b8}.warnt{color:#f0d9a8}
        ol.bhu,ul.bhu{margin:.9rem 0;padding-left:1.3rem}
        ol.bhu li,ul.bhu li{font-size:.92rem;color:var(--lab-ink);line-height:1.6;margin:.5rem 0;max-width:70ch}
        ol.bhu li b,ul.bhu li b{color:var(--lab-ink)}
        .bhu-foot{padding:2.2rem 0 4rem;color:var(--lab-soft);font-size:.83rem;line-height:1.65}
        .bhu-foot a{color:var(--lab-accent)}
        code{background:#1b212b;padding:.08em .35em;border-radius:4px;font-size:.85em;font-family:ui-monospace,monospace}
      `}
      />

      <nav className="bhu-topbar">
        <div className="bhu-wrap row">
          <a className="bhu-brand" href="/">NebulaMind</a>
          <a className="bhu-back" href="/lab">← lab</a>
        </div>
      </nav>

      <div className="bhu-wrap">
        <header className="bhu-hero">
          <p className="bhu-kicker">Corpus synthesis · 31 Aug 2026</p>
          <h1>The black-hole-universe literature, audited</h1>
          <div className="bhu-personal">Duho&rsquo;s personal side-interest — not a NebulaMind research programme</div>
          <p className="bhu-lede">
            An adversarial, paper-by-paper audit of the published &ldquo;is our universe inside a black
            hole?&rdquo; literature. <b>58 entries</b> &mdash; 51 papers plus 7 imported measurement
            instruments &mdash; each tiered under one preregistered rule and double-checked by two
            independent reviewers. <b>55 read in full</b>; every figure below traces to a primary source
            or a two-seat verdict.
          </p>
        </header>

        <section className="bhu-sec">
          <h2><span className="n">1</span>What the base layer actually contains</h2>
          <p className="bhu-sub">Peer-reviewed journal articles only. Parsed from the record, not recited.</p>
          <div className="bhu-scroll">
            <table className="bhu">
              <thead>
                <tr><th>Tier</th><th>Count</th><th>What it means</th></tr>
              </thead>
              <tbody>
                <tr><td>Consistency-only</td><td className="num">32</td><td>a construction shown compatible with observation &mdash; <b>predicts nothing measurable</b></td></tr>
                <tr><td>Qualitative-directional</td><td className="num">7</td><td>a direction (sign, inequality) but no calibrated window</td></tr>
                <tr><td>Calibrated-falsifier</td><td className="num">4</td><td>a number <b>and</b> a threshold a measurement can cross &mdash; entries 7, 31, 44, 51</td></tr>
                <tr><td>Theoretical-obstruction</td><td className="num">3</td><td>a no-go theorem &mdash; entries 5, 22, 48</td></tr>
                <tr><td>Prospect</td><td className="num">3</td><td>a &ldquo;detectable&rdquo; claim whose amplitude is not yet computed</td></tr>
                <tr><td>Support (no tier)</td><td className="num">7</td><td>imported measurement instruments, not BHU-claim papers</td></tr>
                <tr><td>Gated (unread)</td><td className="num">2</td><td>entries 42, 47 &mdash; paywalled, left gated</td></tr>
              </tbody>
            </table>
          </div>
          <p>
            The field is dominated by prose: <b>32 of 58 entries predict nothing measurable</b>. They show
            the idea is <i>not ruled out</i> &mdash; which is not the same as evidence for it. Only <b>four</b>
            entries put a number against a threshold. A fifth, Gazta&ntilde;aga&rsquo;s <code>&Lambda; = 3/r<sub>S</sub>&sup2;</code>,
            displays a number that is <b>fixed <i>from</i> the measured &Lambda; rather than predicting it</b>.
          </p>
          <p className="soft">Five ways a &ldquo;prediction&rdquo; dissolved under audit, each with an exemplar:</p>
          <ol className="bhu">
            <li><b>Fitted-not-predicted</b> (25): a number read off the datum it &ldquo;explains&rdquo; &mdash; the number and the reason it cannot fail are the same clause.</li>
            <li><b>Instrument-fired, not the claim</b> (7): the falsifier crosses an <i>instrument&rsquo;s</i> threshold (a mass ceiling), while the source only says a heavy star &ldquo;would put in serious doubt or simply falsify&rdquo; the cosmology.</li>
            <li><b>Correction sized to the measurement</b> (44): when the base model died at 8&sigma;, the fix offered is an uncomputed ~4% correction whose size is read off the datum it must reproduce.</li>
            <li><b>Unreproduced from the stated inputs</b> (51): a printed threshold no route from the paper&rsquo;s own inputs reaches; the connecting step omitted.</li>
            <li><b>Attributed threshold</b> (31): the falsifying number is credited to <i>others</i>, not derived by the claimant.</li>
          </ol>
        </section>

        <section className="bhu-sec">
          <h2><span className="n">2</span>The live-falsifier ledger</h2>
          <p className="bhu-sub">Two FIRED, two LIVE, plus the directional curvature watch. Each threshold has a primary receipt.</p>
          <div className="bhu-scroll">
            <table className="bhu">
              <thead>
                <tr><th>Entry</th><th>Status</th><th>Threshold</th><th>Current data</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>7 · Brown&ndash;Lee&ndash;Rho (CNS)</td>
                  <td className="fired">FIRED</td>
                  <td>neutron star M &gtrsim; <span className="num">2 M&#9737;</span> falsifies the kaon-condensation chain (PRL 101, 091101)</td>
                  <td>fires the <b>M<sub>max</sub>&asymp;1.5 M&#9737; instrument</b>, not CNS &mdash; the source gives CNS only &ldquo;serious doubt&rdquo;</td>
                </tr>
                <tr>
                  <td>44 · Pourhasan et al. (white hole)</td>
                  <td className="fired">FIRED</td>
                  <td>exact scale invariance, <span className="num">n<sub>s</sub> = 1</span> (JCAP 04(2014)005 &sect;4)</td>
                  <td>Planck 2018 VI eq (19): <span className="num">n<sub>s</sub> = 0.9649 &plusmn; 0.0042, 8&sigma;</span> from 1. Successor is an uncomputed ~4% correction.</td>
                </tr>
                <tr>
                  <td>31 · Smolin (CNS)</td>
                  <td className="live">LIVE, 1.36&sigma; short</td>
                  <td>a neutron star above <span className="num">2.5 M&#9737;</span> refutes CNS (Smolin &sect;4)</td>
                  <td>heaviest well-measured NS <span className="num">2.35 &plusmn; 0.11 M&#9737;</span>; <b>moving <i>away</i> from firing</b> as the error tightens</td>
                </tr>
                <tr>
                  <td>51 · Pop&#322;awski (torsion)</td>
                  <td className="live">LIVE, unfired</td>
                  <td>a minimum black-hole mass floor <span className="num">~10&sup1;&#8310; kg</span> (PLB 690, 73)</td>
                  <td><b>unreproduced from the stated inputs</b> &mdash; six routes tested, none reaches the floor; connecting step omitted</td>
                </tr>
                <tr>
                  <td>54 · Gazta&ntilde;aga (curvature)</td>
                  <td className="warnt">LIVE, not fired</td>
                  <td>predicts <b>closed</b> curvature, &Omega;<sub>k</sub> &lt; 0; refutes on a confirmed &Omega;<sub>k</sub> &gt; 0 (PRD 111, 103537 Eq. 27)</td>
                  <td>DESI DR2+CMB <span className="num">&Omega;<sub>k</sub> = +0.0023 &plusmn; 0.0011 (~2.1&sigma; open)</span> &mdash; adverse but not a detection. Watched by a standing tripwire.</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p>
            Read honestly: exactly two calibrated falsifiers remain LIVE (31, 51), and neither is close &mdash; one
            is drifting away from its bar, the other&rsquo;s number cannot be reproduced from its own inputs. The two
            FIRED ones each killed a <i>sub-model</i>, not the cosmological framework. <b>Nothing in the base layer
            is currently refuted at the framework level, and nothing is on the edge of firing.</b>
          </p>
        </section>

        <section className="bhu-sec">
          <h2><span className="n">3</span>The three paywalled papers, ranked by what a read would unlock</h2>
          <p className="bhu-sub">All pre-2010, ~a few thousand won each by interlibrary copy.</p>
          <ol className="bhu">
            <li><b>Entry 47 &mdash; Sato, Kodama, Sasaki &amp; Maeda (1982).</b> Highest value: the earliest false-vacuum multi-universe mechanism, and the missing member of the branch the Farhi&ndash;Guth <b>no-go (entry 48)</b> is about. Reading it answers one real question &mdash; does the 1982 mechanism fall inside that no-go, or predate and sidestep it?</li>
            <li><b>Entry 42 &mdash; Gonz&aacute;lez-D&iacute;az (1991).</b> Medium: a baby-universe metric-equivalence claim; a read decides whether it adds a result the branch lacks or is another consistency construction.</li>
            <li><b>Entry 2 &mdash; Good (1972).</b> Lowest: a one-page note on nested universes. Provenance only &mdash; no mechanism, no observable.</li>
          </ol>
          <p className="soft">If any single paper is worth an ILL, it is <b>47</b> &mdash; it converts an assumed obstruction relationship into a checked one.</p>
        </section>

        <section className="bhu-sec">
          <h2><span className="n">4</span>Falsifiers the family&rsquo;s own texts imply but never state</h2>
          <p className="bhu-sub">Testable edges the primary papers gesture at without committing to a number. None is yet a stated falsifier.</p>
          <ul className="bhu">
            <li><b>The Pop&#322;awski interior transfer function.</b> The only published multi-paper mechanism with explicit field equations &mdash; yet the transfer function from parent-hole parameters through the bounce to any interior observable was never written. Deriving it would state whether <i>any</i> finite-amplitude signature survives.</li>
            <li><b>The Roupas amplitude.</b> A published &ldquo;detectable&rdquo; claim with a named band (&micro;Hz&ndash;Hz, LISA-class) but no computed amplitude. If a number exists, it becomes a fifth calibrated falsifier; if not, it is a prospect without one.</li>
            <li><b>The Gazta&ntilde;aga cutoff.</b> A power-spectrum cutoff tied to the CMB low quadrupole &mdash; a falsifier only if the cutoff scale is fixed <i>independently</i> of the anomalies it explains.</li>
            <li><b>The preferred-axis / spin-parity edge.</b> Longo&rsquo;s handedness dipole is the instrument for the rotating-parent family&rsquo;s preferred-axis prediction &mdash; the amplitude a DESI spin-parity test would confront. This is the one live cross-check.</li>
            <li><b>Easson&rsquo;s cross-programme no-go map.</b> A 2026 obstruction theorem that, mapped across the other published interiors, could retire several rows at once &mdash; a theory-internal falsifier rather than a data one.</li>
          </ul>
        </section>

        <footer className="bhu-foot">
          <p>
            This is a <b>note on the corpus, not a study of the cosmology</b> &mdash; the measurements are the
            source communities&rsquo;, the thresholds are the papers&rsquo;, and the analysis is arithmetic on
            published posteriors. Every figure traces to a pinned primary source or a two-seat gate verdict in the
            audit lane. It belongs as the closing synthesis of a personal reading project, kept deliberately separate
            from NebulaMind&rsquo;s galaxy-evolution research.
          </p>
        </footer>
      </div>
    </main>
  );
}
