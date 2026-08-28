#!/usr/bin/env python3
"""
nm_fulltext_mass_mine.py -- v2.3 of the NebulaMind measurement-dispersion signal.

THE PROBLEM v2.3 FIXES
----------------------
v2.2 (nm_dispersion_v2.py -> dispersion_v2.json) mines gas-phase metallicity 12+log(O/H)
and the stellar mass it refers to from ABSTRACTS. But abstracts are mass-starved: ~70% of
metallicity values have NO stated stellar mass, so the mass axis of the (z x mass x cal)
cell collapses -- almost everything piles into the m? (mass-unknown) column. Result: adding
the mass axis removed essentially ZERO over-dispersion (Delta S = -0.04), the biggest cell
was z?|m?|Te/direct (N=72, within-S=11.8), and we could NOT tell whether metallicity is
genuinely contested or just the mass-metallicity relation (MZR) masquerading as disagreement.

WHAT v2.3 DOES
--------------
Mine (stellar mass, gas metallicity) PAIRS from FULL TEXT -- especially [TABLE] chunks, which
list per-galaxy rows with BOTH log M* and 12+log(O/H) in the same row. This finally lets us
control the MZR with REAL masses and ask: at fixed (redshift x mass x calibration), do
independent studies still disagree on O/H beyond their errors?

PIPELINE
    1. SELECT   : metallicity-prefilter papers (regex 12+log|log(O/H)|oxygen abundance|metallicit)
                  that have cached full text; take the top ~150 by citation_count (bounds the run).
    2. MINE     : per paper, feed the [TABLE] chunks (per-galaxy rows) + the most O/H-relevant prose
                  chunks to Ollama (qwen3:30b-a3b-instruct); extract a JSON array of PAIRED tuples
                  {log_mstar, oh, redshift, calibration, is_measurement}. <=2 LLM calls/paper,
                  <=~300 total. Cached to dispersion_v23_cache.json. Keep only rows with BOTH a
                  numeric stellar mass and a numeric 12+log(O/H).
    3. DISPERSE : bin pairs into (z x mass x cal) cells (z_edges [0,.3,1,2,3,5,7,inf],
                  mass_edges [8,9,10,11]). PDG scale factor S=sqrt(chi2/(N-1)) per well-populated
                  cell (N>=4, ideally spanning >=2 papers). Metallicity tension = citation-weighted
                  S over MULTI-PAPER cells (genuine cross-study disagreement at fixed mass+epoch).
                  Also report the intrinsic MZR (cell weighted-mean O/H vs mass at each z).
    4. FIRM-UP  : recompute whether metallicity is now a trustworthy contested signal and whether the
                  metallicity-driven frontiers (CGM/DLA cl 19, ram-pressure cl 17, JWST high-z cl 41)
                  firm up; emit an updated characteristic-value GA ranking.

Reproducible: temperature 0, citation-desc ordering, bounded compute. Reuses the PDG math and
parsers from nm_dispersion_v2 (imported). Does NOT modify the corpus or any v2/v3 file. Writes:
    <corpus>/dispersion_v23.json
    <corpus>/dispersion_v23_cache.json          (LLM response cache; safe to delete)
    /Users/duhokim/.claude/jobs/a2199266/tmp/v23_metallicity.json   (website payload)

USAGE
    python nm_fulltext_mass_mine.py                     # full run (top 150 papers)
    python nm_fulltext_mass_mine.py --n-papers 150 --max-calls 300
    python nm_fulltext_mass_mine.py --select-only       # just the paper-selection table, no LLM
"""
import argparse, json, math, os, re, sys, time, urllib.request, collections

_TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _TOOLS)
import nm_dispersion_v2 as v2   # reuse PDG math + parsers (module-level is import-safe)

# ---------------------------------------------------------------- paths / constants
ROOT = '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718/'
CORPUS = ROOT + 'corpus_ga_co_2009_2026.jsonl'
CACHE_DIR = ROOT + 'fulltext_cache/'
LABELS = ROOT + 'cluster_labels_v2.json'
V3 = ROOT + 'frontier_map_v3.json'
DISP_V22 = ROOT + 'dispersion_v2.json'
OUT_DISP = ROOT + 'dispersion_v23.json'
CACHE = ROOT + 'dispersion_v23_cache.json'
JOB_TMP = '/Users/duhokim/.claude/jobs/a2199266/tmp/'
OUT_PAYLOAD = JOB_TMP + 'v23_metallicity.json'
V22_ABLATION = JOB_TMP + 'v2_ablation.json'   # per-cluster v2.2 charval drivers (to update metallicity)

OLLAMA_GEN = 'http://localhost:11434/api/generate'
FAST_MODEL = 'qwen3:30b-a3b-instruct-2507-q4_K_M'
VERSION = 'v2.3'
# mining_pass bumps each time we widen the mined paper set (cache-preserving):
#   1 = top-150-by-citation metallicity-full-text papers (21 yielded table pairs, S_cross=2.52)
#   2 = ALL ~500 metallicity-full-text papers (the individual survey/measurement papers that
#       carry per-galaxy (mass, O/H) tables, mined in citation order; top-150 reuse cache)
MINING_PASS = 2

ARX = re.compile(r'arXiv:(\d{4}\.\d{4,5})', re.I)
PREFILTER = re.compile(r'12\s*\+\s*log|log\(O/H\)|oxygen abundance|metallicit', re.I)
_ZNUM = re.compile(r'[-+]?\d+(?:\.\d+)?')

# O/H metallicity range + mass range (galaxy stellar masses) for gating mined rows
OH_LO, OH_HI = 7.0, 9.3
M_LO, M_HI = 6.0, 13.0
DEFAULT_OH_SIG = 0.10     # dex sigma assumed when a table row quotes no O/H error (FLAGGED)
MIN_OH_SIG = 0.02

# chunk-relevance keyword sets
_RX_OH = re.compile(r'12\s*\+\s*log|log\s*\(?\s*o\s*/\s*h|oxygen abundance|\bo/h\b|metallicit|\bz\s*=\s*8\.', re.I)
_RX_MASS = re.compile(r'log\s*\(?\s*m|m_?\*|m_?star|stellar mass|\blog\s*m_?\*|m\*/m|\bmass\b', re.I)


# ---------------------------------------------------------------- stage 1: select papers
def load_have():
    have = set()
    for fn in os.listdir(CACHE_DIR):
        if fn.endswith('.chunks.json'):
            have.add(fn[:-len('.chunks.json')])
    return have


def select_papers(n_papers):
    """metallicity-prefilter papers WITH cached full text, top n by citation_count."""
    have = load_have()
    cands = []
    with open(CORPUS) as f:
        for line in f:
            r = json.loads(line)
            ab = r.get('abstract') or ''
            if not PREFILTER.search(ab):
                continue
            ident = r.get('identifier') or []
            aid = next((ARX.search(str(s)).group(1) for s in ident if ARX.search(str(s))), None)
            if not aid or aid not in have:
                continue
            cands.append(dict(citation=r.get('citation_count') or 0, bibcode=r['bibcode'],
                              arxiv=aid, title=' '.join(r.get('title') or [])[:140]))
    cands.sort(key=lambda d: (-d['citation'], d['bibcode']))
    return cands[:n_papers], len(cands)


# ---------------------------------------------------------------- stage 2: mine pairs from full text
def _ollama(prompt, model, n=1400, temp=0.0, timeout=240):
    body = json.dumps({'model': model, 'prompt': prompt, 'stream': False,
                       'options': {'num_predict': n, 'temperature': temp}}).encode()
    req = urllib.request.Request(OLLAMA_GEN, data=body, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return (json.loads(r.read().decode()).get('response') or '').strip()


def _chunk_score(c):
    """Rank chunks by paired-(mass,O/H) likelihood. Tables >> prose; both-keyword >> single."""
    is_tab = c.startswith('[TABLE]')
    has_oh = bool(_RX_OH.search(c))
    has_m = bool(_RX_MASS.search(c))
    n_num = len(_ZNUM.findall(c))
    s = 0
    if is_tab:
        s += 40
    if has_oh:
        s += 20
    if has_m:
        s += 20
    if has_oh and has_m:
        s += 40           # a row carrying BOTH is exactly what we want
    s += min(n_num, 60) * 0.3
    return s


def pack_batches(chunks, budget=7000, max_batches=2):
    """Pick the most paired-relevant chunks; pack into <=max_batches text blocks of ~budget chars.

    A chunk must mention O/H OR be a table to be eligible (prose with no metallicity is useless).
    Tables that mention both mass and O/H are always tried first.
    """
    elig = [c for c in chunks if c.startswith('[TABLE]') or _RX_OH.search(c)]
    elig.sort(key=_chunk_score, reverse=True)
    batches, cur, cur_len = [], [], 0
    for c in elig:
        piece = c[:2200]
        if cur and cur_len + len(piece) > budget:
            batches.append('\n\n'.join(cur))
            if len(batches) >= max_batches:
                cur = []
                break
            cur, cur_len = [], 0
        cur.append(piece)
        cur_len += len(piece)
    if cur and len(batches) < max_batches:
        batches.append('\n\n'.join(cur))
    return batches[:max_batches]


PROMPT = (
    'You extract PAIRED galaxy measurements from an astronomy paper\'s tables and passages. Each table '
    'row (or grid cell) is usually one galaxy, or one bin in stellar mass / SFR / redshift. I want, for '
    'every object/row/bin that reports BOTH a stellar mass AND a gas-phase oxygen abundance, one JSON '
    'object:\n'
    '{"log_mstar": number, "oh": number, "redshift": "z value or range as string"|null, '
    '"calibration": "metallicity diagnostic e.g. Te/direct, PP04-O3N2, PP04-N2, KK04, R23, T04, '
    'Sanders, Maiolino, Curti, or null", "kind": "obs"|"model"}\n'
    'Field rules:\n'
    '- log_mstar = log10(M*/Msun), a value typically 6 to 12. If a linear stellar mass is given '
    '(e.g. 3e10), take log10. If a mass RANGE/bin is given, use its midpoint. A mass/SFR GRID table '
    '(mass values as column headers, O/H values in the cells) is a rich source -- emit one object per '
    'populated cell, pairing its column-header mass with the cell O/H.\n'
    '- oh = the gas-phase oxygen abundance 12+log(O/H), a value between 7.0 and 9.3. Do NOT report '
    'stellar [Fe/H], solar-scaled [O/H], SSP model metallicity [M/H], or Cepheid/stellar abundances.\n'
    '- ONLY emit an object when the SAME galaxy/row/bin has BOTH a stellar mass and a 12+log(O/H). If a '
    'row has only one of them, skip it.\n'
    '- kind = "obs" for anything derived from OBSERVED galaxies -- individual measurements, sample '
    'medians, binned medians of a survey, or a relation fitted to real data (this is the common case, '
    'include these). kind = "model" ONLY if the value is a prediction of a hydrodynamical/semi-analytic '
    'SIMULATION or a purely theoretical model.\n'
    'Return ONLY a JSON array (possibly with many objects if the table has many galaxies/bins). If '
    'there are no paired (mass, O/H) rows, return [].\n\n'
    'PAPER TABLES/PASSAGES:\n%s\n\nJSON array only:')


def load_cache():
    if os.path.exists(CACHE):
        try:
            return json.load(open(CACHE))
        except Exception:
            return {}
    return {}


def save_cache(c):
    tmp = CACHE + '.tmp'
    json.dump(c, open(tmp, 'w'))
    os.replace(tmp, CACHE)


def _num(x):
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        mm = _ZNUM.findall(x.replace('%', ''))
        return float(mm[0]) if mm else None
    return None


def mine_paper(paper, cache, model, calls_left, verbose=False):
    """Return (rows, n_calls). rows: kept paired measurement records for this paper."""
    aid = paper['arxiv']
    try:
        chunks = json.load(open(CACHE_DIR + aid + '.chunks.json'))
    except Exception:
        return [], 0
    batches = pack_batches(chunks)
    if not batches:
        return [], 0
    batches = batches[:max(1, min(len(batches), calls_left))]
    raw_all, n_calls = [], 0
    for bi, batch in enumerate(batches):
        ck = '%s|%d' % (aid, bi)
        if ck in cache:
            raw = cache[ck]
        else:
            if calls_left - n_calls <= 0:
                break
            try:
                resp = _ollama(PROMPT % batch[:7200], model, n=2400)
                raw = v2._parse_json_array(resp)
                n_calls += 1
            except Exception as e:
                raw = []
                if verbose:
                    sys.stderr.write('  mine fail %s b%d: %s\n' % (aid, bi, e))
            cache[ck] = raw
        raw_all.extend(raw or [])
    # normalize + gate: keep rows with BOTH numeric mass and numeric O/H in range
    rows = []
    for e in raw_all:
        if not isinstance(e, dict):
            continue
        # drop only genuine simulation/theory predictions; keep observed (incl. binned medians / fits)
        if str(e.get('kind', 'obs')).lower().startswith('model'):
            continue
        m = v2.parse_logmstar(e.get('log_mstar'))
        oh = _num(e.get('oh'))
        if m is None or oh is None:
            continue
        if not (M_LO <= m <= M_HI):
            continue
        if not (OH_LO <= oh <= OH_HI):
            continue
        # FABRICATED-DUPLICATE GUARD: when a table lists 12+log(O/H) but NO stellar-mass column, the
        # model tends to copy the O/H value into log_mstar. log M* and 12+log(O/H) are physically
        # different quantities; an EXACT match (within 0.02 dex) across rows is that failure mode, not
        # a real coincidence. Spot-check found this in abundance-only tables (e.g. 1205.6782 Table 4,
        # the 1403.0007 MZR-evolution table). Drop these unpaired rows.
        if abs(m - oh) < 0.02:
            continue
        # optional per-row O/H error
        sig = None
        for k in ('oh_err', 'err', 'sigma', 'oh_sigma'):
            v = _num(e.get(k))
            if v:
                sig = abs(v); break
        defaulted = sig is None
        if defaulted:
            sig = DEFAULT_OH_SIG
        sig = max(sig, MIN_OH_SIG)
        rows.append(dict(
            bibcode=paper['bibcode'], arxiv=aid, citation=paper['citation'],
            value=round(oh, 4), sigma=round(sig, 4), defaulted_err=defaulted,
            log_mstar=round(m, 4),
            redshift=v2.parse_redshift(e.get('redshift')),
            calibration=v2.canon_calibration(e.get('calibration')),
            method_raw=e.get('calibration')))
    return rows, n_calls


def mine_all(papers, model, max_calls, verbose=True):
    cache = load_cache()
    all_rows = []
    n_calls = 0
    t0 = time.time()
    per_paper = []
    for i, p in enumerate(papers):
        if n_calls >= max_calls:
            if verbose:
                sys.stderr.write('  reached max-calls=%d at paper %d/%d\n' % (max_calls, i, len(papers)))
            break
        rows, c = mine_paper(p, cache, model, max_calls - n_calls, verbose)
        n_calls += c
        all_rows.extend(rows)
        per_paper.append((p['bibcode'], len(rows)))
        if c and (n_calls % 20 == 0 or n_calls < 3):
            save_cache(cache)
            rate = n_calls / max(1e-9, time.time() - t0)
            print('   [paper %d/%d] %d LLM calls, %d pairs so far, %.2f calls/s'
                  % (i + 1, len(papers), n_calls, len(all_rows), rate), flush=True)
    save_cache(cache)
    return all_rows, n_calls, per_paper


# ---------------------------------------------------------------- stage 3: MZR-controlled dispersion
def cell_key(r):
    return (v2.zbin_label(r['redshift']), v2.massbin_label(r['log_mstar']), r['calibration'])


def pooled_over(rs, keyfn, min_n=2):
    groups = collections.defaultdict(list)
    for r in rs:
        groups[keyfn(r)].append(r)
    pc, pd = 0.0, 0
    for gr in groups.values():
        if len(gr) >= min_n:
            _, _, _, gchi2, _, _ = v2.pdg_scale([x['value'] for x in gr], [x['sigma'] for x in gr])
            pc += gchi2
            pd += (len(gr) - 1)
    return (math.sqrt(pc / pd) if pd > 0 else None), pd


def disperse(rows):
    vals = [r['value'] for r in rows]
    sigs = [r['sigma'] for r in rows]
    N = len(rows)
    out = dict(N=N,
               n_papers=len(set(r['bibcode'] for r in rows)),
               n_massknown=sum(1 for r in rows if r['log_mstar'] is not None),
               n_zknown=sum(1 for r in rows if r['redshift'] is not None),
               defaulted_err_frac=round(sum(r['defaulted_err'] for r in rows) / N, 3) if N else None)
    if N >= 2:
        n, xm, xe, chi2, S, robust = v2.pdg_scale(vals, sigs)
        out.update(weighted_mean=round(xm, 4), wmean_err=round(xe, 4) if xe else None,
                   chi2=round(chi2, 2), S_all=round(S, 3),
                   robust_overdisp=round(robust, 2) if robust else None,
                   value_min=round(min(vals), 3), value_max=round(max(vals), 3))
    # cascade
    S_z, _ = pooled_over(rows, lambda r: (v2.zbin_label(r['redshift']),))
    S_zmass, _ = pooled_over(rows, lambda r: (v2.zbin_label(r['redshift']), v2.massbin_label(r['log_mstar'])))
    S_zmasscal, _ = pooled_over(rows, cell_key)
    S_cal, _ = pooled_over(rows, lambda r: (r['calibration'],))
    out.update(S_zonly=_r(S_z), S_zmass=_r(S_zmass), S_zmasscal=_r(S_zmasscal), S_calonly=_r(S_cal))
    if out.get('S_zcal_missing') is None and out.get('S_all') and S_zmasscal is not None:
        out['mass_drop'] = round((out.get('S_zonly') or 0) - S_zmasscal, 3)
    # per-cell detail
    cells = collections.defaultdict(list)
    for r in rows:
        cells[cell_key(r)].append(r)
    cell_rec = {}
    well_multi = []       # (S, N, cite, n_papers, label) for cross-study residual: N>=4 AND papers>=2
    for ck, cr in sorted(cells.items(), key=lambda kv: -len(kv[1])):
        gv = [x['value'] for x in cr]
        gs = [x['sigma'] for x in cr]
        gN = len(cr)
        npap = len(set(x['bibcode'] for x in cr))
        cite = sum(x['citation'] for x in cr)
        label = '|'.join(ck)
        if gN >= 2:
            _, gxm, _, _, gS, _ = v2.pdg_scale(gv, gs)
            rec = dict(N=gN, n_papers=npap, wmean=round(gxm, 4), S=round(gS, 3), cite=cite,
                       well=(gN >= 4), multi_paper=(npap >= 2))
            cell_rec[label] = rec
            if gN >= 4 and npap >= 2:
                well_multi.append((gS, gN, cite, npap, label))
        else:
            cell_rec[label] = dict(N=gN, n_papers=npap, wmean=round(gv[0], 4), S=None, cite=cite,
                                   well=False, multi_paper=False)
    out['cells'] = cell_rec
    out['n_cells'] = len(cell_rec)
    out['n_wellcells'] = sum(1 for c in cell_rec.values() if c['well'])
    out['n_wellcells_multipaper'] = len(well_multi)
    # cross-study residual: citation-weighted mean S over multi-paper well cells
    if well_multi:
        num = den = 0.0
        mx = 0.0
        for gS, gN, cite, npap, lbl in well_multi:
            w = math.log1p(cite) + gN
            num += gS * w
            den += w
            mx = max(mx, gS)
        out['S_cross'] = round(num / den, 3)
        out['S_cross_max'] = round(mx, 3)
    else:
        out['S_cross'] = None
        out['S_cross_max'] = None
    # between-calibration offset (context)
    cal_means = {}
    for cal in set(r['calibration'] for r in rows):
        gr = [r for r in rows if r['calibration'] == cal and cal != 'unknown']
        if len(gr) >= 2:
            _, m, _, _, _, _ = v2.pdg_scale([x['value'] for x in gr], [x['sigma'] for x in gr])
            cal_means[cal] = round(m, 4)
    out['cal_means'] = cal_means
    out['between_cal_offset'] = (round(max(cal_means.values()) - min(cal_means.values()), 4)
                                 if len(cal_means) >= 2 else None)
    # massbin populations
    out['massbin_N'] = dict(collections.Counter(v2.massbin_label(r['log_mstar']) for r in rows))
    out['zbin_N'] = dict(collections.Counter(v2.zbin_label(r['redshift']) for r in rows))
    return out, cells


def _r(x):
    return round(x, 3) if x is not None else None


def mzr_table(cells):
    """Intrinsic MZR sanity check: per (z-bin), weighted-mean O/H vs mass-bin (pooled over cal)."""
    by_zmass = collections.defaultdict(list)
    for ck, cr in cells.items():
        zb, mb, cal = ck
        by_zmass[(zb, mb)].extend(cr)
    mzr = collections.defaultdict(dict)
    for (zb, mb), cr in by_zmass.items():
        if len(cr) < 2:
            if cr:
                mzr[zb][mb] = dict(N=len(cr), wmean=round(cr[0]['value'], 3))
            continue
        _, m, _, _, _, _ = v2.pdg_scale([x['value'] for x in cr], [x['sigma'] for x in cr])
        mzr[zb][mb] = dict(N=len(cr), wmean=round(m, 3))
    return {zb: dict(sorted(d.items(), key=lambda kv: _massorder(kv[0]))) for zb, d in mzr.items()}


_MORDER = {'mlt8': 0, 'm8-9': 1, 'm9-10': 2, 'm10-11': 3, 'mge11': 4, 'm?': 9}


def _massorder(mb):
    return _MORDER.get(mb, 5)


# ---------------------------------------------------------------- stage 4: firm-up frontiers
def firm_up(disp, rows):
    """Re-decide whether metallicity is trustworthy and update the characteristic-value GA ranking.

    Uses the v2.2 per-GA-cluster charval drivers (v2_ablation.json), swapping the metallicity driver
    S for the v2.3 full-text mass-controlled cross-study residual, and re-deciding KEEP/EXCLUDE
    metallicity by whether that residual is now readable (defensible) tension.
    """
    labels = json.load(open(LABELS))
    S_cross = disp.get('S_cross')
    S_zmasscal = disp.get('S_zmasscal')
    # trustworthy if controlling REAL mass leaves a bounded, cross-study (multi-paper) residual that
    # is de-mixed of calibration -- i.e. not just the MZR or a calibration offset.
    metric = S_cross if S_cross is not None else S_zmasscal
    trustworthy = bool(metric is not None and disp.get('n_wellcells_multipaper', 0) >= 2)
    readable = bool(metric is not None and metric <= 3.0)

    # per-cluster metallicity signal from the mined pairs (attribute via cluster labels)
    for r in rows:
        r['cluster'] = labels.get(r['bibcode'])
    cl_rows = collections.defaultdict(list)
    for r in rows:
        if r['cluster'] not in (None, -1):
            cl_rows[r['cluster']].append(r)
    cl_met_S = {}
    for cl, rs in cl_rows.items():
        if len(rs) < 4:
            continue
        d, _ = disperse(rs)
        cl_met_S[cl] = dict(S_cross=d.get('S_cross'), S_zmasscal=d.get('S_zmasscal'),
                            N=d['N'], n_papers=d['n_papers'],
                            n_wellcells_multipaper=d.get('n_wellcells_multipaper', 0))

    # rebuild characteristic-value GA ranking from v2.2 drivers, updating metallicity S
    ranking = None
    try:
        ab = json.load(open(V22_ABLATION))
    except Exception:
        ab = None
    if ab and 'ga_ranking' in ab:
        KEEP_CHARVAL = {'sfrd', 'fesc', 'quiescent_frac', 'ms_slope', 'uvlf_alpha', 'smf_mstar',
                        'metallicity', 'gas_fraction', 'dust_atten', 'edd_ratio'}
        # per-cluster metallicity S to substitute: cluster-specific if available, else global
        def met_S_for(cl):
            c = cl_met_S.get(cl)
            if c and c.get('S_cross') is not None:
                return c['S_cross'], c['N'], True
            if c and c.get('S_zmasscal') is not None:
                return c['S_zmasscal'], c['N'], True
            return (metric, disp['N'], False) if metric is not None else (None, 0, False)
        # need sat/grow per GA cluster
        fm = json.load(open(V3))
        cinfo = {c['cluster']: c for c in fm['clusters']}
        cv_rows = []
        for row in ab['ga_ranking']:
            cl = row['cluster']
            ci = cinfo.get(cl, {})
            sat = ci.get('sat_activity') or 0.0
            grow = ci.get('growth_norm') or 0.0
            drivers = []
            for qk, c in (row.get('v2_contrib') or {}).items():
                if qk not in KEEP_CHARVAL:
                    continue
                if qk == 'metallicity':
                    if not (trustworthy and readable):
                        continue   # EXCLUDE metallicity if still not trustworthy
                    mS, mN, cluster_specific = met_S_for(cl)
                    if mS is None:
                        continue
                    drivers.append(dict(q='metallicity', S=round(mS, 3), N=mN,
                                        cluster_specific=cluster_specific, v23_controlled=True))
                else:
                    drivers.append(dict(q=qk, S=round(c['S'], 3), N=c['n']))
            drivers.sort(key=lambda d: -d['S'])
            tclean = max((d['S'] for d in drivers), default=0.0)
            cv_rows.append(dict(cluster=cl, label_keywords=row.get('keywords', ''),
                                sat=sat, grow=grow, tclean=tclean, drivers=drivers))
        tcmax = max((x['tclean'] for x in cv_rows), default=0.0) or 1.0
        for x in cv_rows:
            tn = x['tclean'] / tcmax
            x['tension'] = round(tn, 4)
            x['score'] = round(x['sat'] * (0.6 * tn + 0.4 * x['grow']), 5)
        cv_rows.sort(key=lambda x: -x['score'])
        ranking = [dict(rank=i + 1, cluster=x['cluster'], label_keywords=x['label_keywords'],
                        score=x['score'], tension=x['tension'], drivers=x['drivers'][:5])
                   for i, x in enumerate(cv_rows[:12])]
    return dict(metallicity_trustworthy=bool(trustworthy and readable),
                trustworthy_flag=trustworthy, readable_flag=readable,
                metric_used=('S_cross' if S_cross is not None else 'S_zmasscal'),
                metric_value=metric,
                per_cluster_metallicity_S=cl_met_S,
                charval_ranking=ranking)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n-papers', type=int, default=500)   # pass 2: ALL metallicity-full-text papers
    ap.add_argument('--max-calls', type=int, default=600)  # bound NEW LLM calls (~1-2/paper, cache reused)
    ap.add_argument('--model', default=FAST_MODEL)
    ap.add_argument('--select-only', action='store_true')
    args = ap.parse_args()

    print('== STAGE 1: select metallicity-prefilter papers WITH full text ==', flush=True)
    papers, total = select_papers(args.n_papers)
    print('   %d metallicity papers have full text; taking top %d by citation (cutoff %d cites)'
          % (total, len(papers), papers[-1]['citation'] if papers else 0), flush=True)
    print('   top 5:', [(p['bibcode'], p['citation']) for p in papers[:5]], flush=True)
    if args.select_only:
        json.dump([dict(bibcode=p['bibcode'], arxiv=p['arxiv'], citation=p['citation'],
                        title=p['title']) for p in papers],
                  open(JOB_TMP + 'v23_selected.json', 'w'), indent=2)
        print('select-only: wrote', JOB_TMP + 'v23_selected.json')
        return

    print('\n== STAGE 2: mine (mass, O/H) pairs from full text (tables first) ==', flush=True)
    t0 = time.time()
    rows, n_calls, per_paper = mine_all(papers, args.model, args.max_calls)
    papers_with_pairs = sum(1 for b, n in per_paper if n > 0)
    print('   %d LLM calls in %.1fs; mined %d paired (mass,O/H) rows from %d/%d papers'
          % (n_calls, time.time() - t0, len(rows), papers_with_pairs, len(per_paper)), flush=True)
    if not rows:
        print('   NO pairs mined -- aborting.'); return
    mass_known = sum(1 for r in rows if r['log_mstar'] is not None)
    print('   MASS-KNOWN fraction: %d/%d = %.3f  (vs ~0.30 from abstracts in v2.2)'
          % (mass_known, len(rows), mass_known / len(rows)), flush=True)

    print('\n== STAGE 3: MZR-controlled dispersion (PDG S within z x mass x cal cells) ==', flush=True)
    disp, cells = disperse(rows)
    print('   pairs=%d  from %d papers  |  cells=%d  well(N>=4)=%d  multi-paper-well=%d'
          % (disp['N'], disp['n_papers'], disp['n_cells'], disp['n_wellcells'],
             disp['n_wellcells_multipaper']), flush=True)
    print('\n   METALLICITY S CASCADE (12+log(O/H), full-text masses):')
    print('      S_all                          = %s   (raw, everything pooled)' % disp.get('S_all'))
    print('      within z                S_zonly= %s' % disp.get('S_zonly'))
    print('      within (z x mass)      S_zmass = %s   <-- MZR controlled with REAL masses' % disp.get('S_zmass'))
    print('      within (z x mass x cal) S_zmc  = %s   <-- fully de-mixed' % disp.get('S_zmasscal'))
    print('      cross-study residual  S_cross  = %s   (cite-wtd S over MULTI-PAPER N>=4 cells)'
          % disp.get('S_cross'))
    print('      between-calibration offset = %s dex' % disp.get('between_cal_offset'))
    print('      massbin populations: %s' % disp['massbin_N'])
    print('      zbin populations:    %s' % disp['zbin_N'])
    print('\n   Multi-paper well cells (genuine same-z same-mass same-cal O/H tension):')
    for lbl, c in sorted(disp['cells'].items(), key=lambda kv: -kv[1]['N']):
        if c.get('well') and c.get('multi_paper'):
            print('      %-34s N=%-3d papers=%-2d wmean=%6.3f  S=%s cite=%d'
                  % (lbl, c['N'], c['n_papers'], c['wmean'], c['S'], c['cite']))

    mzr = mzr_table(cells)
    print('\n   INTRINSIC MZR sanity (weighted-mean O/H vs mass, should RISE with mass):')
    for zb in sorted(mzr.keys(), key=lambda z: (z == 'z?', z)):
        seq = mzr[zb]
        cells_str = '  '.join('%s:%.2f(N%d)' % (mb, d['wmean'], d['N'])
                              for mb, d in seq.items() if mb != 'm?')
        if cells_str:
            print('      %-8s  %s' % (zb, cells_str))

    print('\n== STAGE 4: firm-up frontiers ==', flush=True)
    fu = firm_up(disp, rows)
    print('   metallicity trustworthy now? %s  (metric %s=%s, multi-paper wells=%d)'
          % (fu['metallicity_trustworthy'], fu['metric_used'], fu['metric_value'],
             disp['n_wellcells_multipaper']))
    if fu.get('charval_ranking'):
        print('\n   UPDATED TOP-12 GA characteristic-value ranking (metallicity %s):'
              % ('KEPT' if fu['metallicity_trustworthy'] else 'EXCLUDED'))
        print('   %-4s %-4s %-9s %-7s  %s' % ('rk', 'cl', 'score', 'tens', 'top drivers | keywords'))
        for x in fu['charval_ranking']:
            drv = ' '.join('%s(S%.1f,N%d)' % (d['q'], d['S'], d['N']) for d in x['drivers'][:3])
            print('   %-4d %-4d %-9.5f %-7.3f  %s'
                  % (x['rank'], x['cluster'], x['score'], x['tension'],
                     drv + ' | ' + str(x['label_keywords'])[:46]))

    # ---- spot-check payload (10 mined rows for table-parse audit) ----
    spot = [dict(bibcode=r['bibcode'], arxiv=r['arxiv'], log_mstar=r['log_mstar'],
                 oh=r['value'], z=r['redshift'], cal=r['calibration']) for r in rows[:10]]

    # ---------------------------------------------------------------- write outputs
    out = dict(
        version=VERSION,
        mining_pass=MINING_PASS,
        generated=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        model=args.model, n_papers_selected=len(papers), n_papers_available=total,
        max_calls=args.max_calls, n_llm_calls=n_calls,
        z_edges=[list(e) for e in v2.Z_EDGES], mass_edges=v2.MASS_EDGES,
        oh_range=[OH_LO, OH_HI], mass_range=[M_LO, M_HI],
        default_oh_sigma=DEFAULT_OH_SIG,
        n_pairs=len(rows), papers_with_pairs=papers_with_pairs,
        mass_known_frac=round(mass_known / len(rows), 4),
        dispersion=disp,
        mzr=mzr,
        firm_up=fu,
        spot_check_rows=spot,
        per_paper_pairs=[dict(bibcode=b, n=n) for b, n in per_paper if n > 0],
        pairs=rows,
        note=('v2.3: (mass, O/H) pairs mined from FULL TEXT (tables) instead of abstracts, to control '
              'the mass-metallicity relation (MZR) with REAL stellar masses. S = PDG scale factor '
              'sqrt(chi2/(N-1)). Cascade: S_all (pooled) -> S_zonly (within z) -> S_zmass (within z x '
              'mass, MZR-controlled) -> S_zmasscal (within z x mass x calibration, fully de-mixed) -> '
              'S_cross (citation-weighted S over well-populated N>=4 cells spanning >=2 papers = genuine '
              'cross-study disagreement at fixed epoch+mass+calibration). "cells" holds per-(z x mass x '
              'cal) detail incl. n_papers and multi_paper flag. "mzr" is the intrinsic MZR sanity check '
              '(weighted-mean O/H vs mass per z-bin). Rows lacking a per-row O/H error default to sigma='
              '%.2f dex (defaulted_err flag). Does not modify any v2/v3 file.' % DEFAULT_OH_SIG))
    json.dump(out, open(OUT_DISP, 'w'), indent=1)
    print('\nwrote', OUT_DISP, flush=True)

    payload = dict(
        version=VERSION, mining_pass=MINING_PASS, generated=out['generated'],
        coverage=dict(n_pairs=len(rows), n_papers=disp['n_papers'],
                      papers_with_pairs=papers_with_pairs, papers_selected=len(papers),
                      mass_known_frac=out['mass_known_frac'],
                      n_cells=disp['n_cells'], n_wellcells=disp['n_wellcells'],
                      n_wellcells_multipaper=disp['n_wellcells_multipaper']),
        metallicity_cascade=dict(
            S_all=disp.get('S_all'), S_zonly=disp.get('S_zonly'), S_zmass=disp.get('S_zmass'),
            S_zmasscal=disp.get('S_zmasscal'), S_cross=disp.get('S_cross'),
            between_cal_offset=disp.get('between_cal_offset'),
            v22_baseline=dict(S_all=9.55, S_zcal=7.72, S_zmasscal=7.76, S_contest=6.04,
                              mass_unknown_frac=0.70)),
        metallicity_trustworthy=fu['metallicity_trustworthy'],
        firm_up=dict(metric_used=fu['metric_used'], metric_value=fu['metric_value'],
                     trustworthy_flag=fu['trustworthy_flag'], readable_flag=fu['readable_flag'],
                     per_cluster_metallicity_S=fu['per_cluster_metallicity_S']),
        charval_ranking=fu.get('charval_ranking'),
        mzr=mzr,
        multi_paper_cells=[dict(cell=lbl, **c) for lbl, c in disp['cells'].items()
                           if c.get('well') and c.get('multi_paper')],
    )
    os.makedirs(JOB_TMP, exist_ok=True)
    json.dump(payload, open(OUT_PAYLOAD, 'w'), indent=2)
    print('wrote', OUT_PAYLOAD, flush=True)


if __name__ == '__main__':
    main()
