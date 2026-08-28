#!/usr/bin/env python3
"""
nm_dispersion_v2.py -- MEASUREMENT-DISPERSION controversy signal (v2) for NebulaMind
galaxy-evolution frontier ranking.

WHAT THIS DOES
--------------
v1 (rank_frontiers_v3.py -> frontier_map_v3.json, field `score_v1`) detects controversy
with a WORD LEXICON ("tension", "discrepancy", ...) mined from titles+abstracts. That
rewards papers that *say* they disagree. v2 instead reads the actual NUMBERS off abstracts
for a curated set of galaxy-evolution observables and detects where independent measurements
of the SAME quantity disagree beyond their quoted error bars -- the PDG scale-factor idea:

    chi2 = sum_i (x_i - x_wmean)^2 / sigma_i^2       (x_wmean = inverse-variance weighted mean)
    S    = sqrt( chi2 / (N-1) )                      (PDG "scale factor")
    S ~ 1  -> measurements consistent within errors
    S >> 1 -> over-dispersed => contested (OR heterogeneous population / calibration offset)

For metallicity 12+log(O/H) we also SPLIT BY CALIBRATION. Cross-calibration offsets
(T04/Tremonti sits ~+0.2 dex above Te/PP04) show up as a SYSTEMATIC OFFSET between the
per-calibration weighted means; the all-in S shrinks once you compute S *within* each
calibration group. This is the known-answer validator.

PIPELINE (each stage documented in code below)
    1. PREFILTER  : regex-match all 120,676 abstracts per quantity -> candidate yield table.
    2. EXTRACT    : bounded Ollama extraction on up to CAP_PER_Q candidates/quantity
                    (prioritised by citation_count, global cap MAX_TOTAL). Cached to disk so
                    re-runs are cheap. Parses {value, err_low, err_high, redshift, method,
                    is_measurement}; defaults a per-quantity sigma when none given (FLAGGED).
    3. DISPERSE   : per quantity -> N, weighted mean, all-in S, split-by-(calibration|z) S,
                    verdict (contested / systematic-offset / consistent).
    4. ATTRIBUTE  : map each measurement's paper -> cluster -> per-GA-cluster v2 tension.
    5. RESCORE    : score_v2 = sat(activity) * tractable * (0.6*tension_v2_norm + 0.4*growth_norm),
                    i.e. the v1 formula with the lexicon tension term swapped for dispersion
                    tension. Ablation vs score_v1.

REPRODUCIBLE: temperature 0, fixed candidate ordering (citation desc, bibcode tiebreak),
bounded compute (scale knobs --cap-per-quantity / --max-total). Does NOT modify the corpus,
cluster labels, or any v2/v3 file. Writes only:
    <corpus>/dispersion_v2.json
    /Users/duhokim/.claude/jobs/a2199266/tmp/v2_ablation.json
    <cache dir>/dispersion_v2_cache.json   (LLM response cache; safe to delete)

USAGE
    python nm_dispersion_v2.py                      # full run, defaults
    python nm_dispersion_v2.py --cap-per-quantity 80 --max-total 700
    python nm_dispersion_v2.py --prefilter-only     # just the yield table, no LLM
    python nm_dispersion_v2.py --model llama3.1:8b  # fallback extraction model
"""
import argparse, json, math, os, re, sys, time, urllib.request, collections

# --------------------------------------------------------------------------- paths
ROOT = '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718/'
CORPUS = ROOT + 'corpus_ga_co_2009_2026.jsonl'
LABELS = ROOT + 'cluster_labels_v2.json'
V3 = ROOT + 'frontier_map_v3.json'
OUT_DISP = ROOT + 'dispersion_v2.json'
JOB_TMP = '/Users/duhokim/.claude/jobs/a2199266/tmp/'
OUT_ABLATION = JOB_TMP + 'v2_ablation.json'
CACHE = ROOT + 'dispersion_v2_cache.json'

OLLAMA_GEN = 'http://localhost:11434/api/generate'
FAST_MODEL = 'qwen3:30b-a3b-instruct-2507-q4_K_M'

VERSION = 'v2.2'   # v2.2: STELLAR-MASS axis added to same-epoch binning for mass-dependent
                   # quantities (metallicity via the MZR is the point). v2.1 = 19 quantities +
                   # redshift-binned dispersion; v2.2 re-extracts log_mstar for the 6 mass-dependent
                   # characteristic quantities and bins cells by (z x mass [x calibration]).
OUT_V21_RANKING = JOB_TMP + 'v21_ga_ranking.json'
OUT_V22_RANKING = JOB_TMP + 'v22_ga_ranking.json'

# v2.2 cache key is versioned: mass-augmented quantities (mass_ext=True) use a DIFFERENT prompt
# (adds log_mstar), so their cache entries carry a trailing '|m'. This keeps the v2.1 cache intact
# and forces a clean re-extraction of only the mass-dependent quantities.
def cache_key(q, bib):
    return '%s|%s%s' % (q['key'], bib, '|m' if q.get('mass_ext') else '')

# --------------------------------------------------------------------------- quantity registry
# Each quantity:
#   key         : short id
#   name        : human label
#   patterns    : list of regex (case-insensitive) - ANY match => candidate abstract
#   target      : plain-English description of the scalar to extract (goes in the prompt)
#   lo, hi      : sane numeric range for a real measurement (drop out-of-range values)
#   unit        : label for the report
#   default_sig : absolute sigma to assume when a measurement quotes no error (FLAGGED)
#   min_sig     : floor on sigma so a spuriously tiny error can't dominate chi2
#   split       : 'calibration' (metallicity) or 'zbin' (everything else)
QUANTITIES = [
    dict(key='metallicity', name='Gas-phase metallicity 12+log(O/H)',
         patterns=[r'12\s*\+\s*log', r'log\s*\(?\s*O\s*/\s*H', r'oxygen abundance', r'metallicit'],
         # prioritise abstracts that actually print a numeric 12+log(O/H) so extraction yield of
         # real values (and their calibrations) is high -- this is the known-answer validator.
         priority=[r'12\s*\+\s*log\s*\(?\s*O\s*/\s*H', r'log\s*\(\s*O\s*/\s*H\s*\)\s*[=~]',
                   r'\b8\.\d\b.{0,30}O/H', r'oxygen abundance.{0,40}\d'],
         cap=380, mass_ext=True, mass_cap=340,
         target=('the gas-phase oxygen abundance 12+log(O/H) (a value between 7.0 and 9.3). '
                 'Record the metallicity CALIBRATION in "method": one of Te/direct, PP04-O3N2, '
                 'PP04-N2, KK04, T04/Tremonti, R23, Sanders, other-strong-line'),
         lo=7.0, hi=9.3, unit='12+log(O/H) [dex]', default_sig=0.10, min_sig=0.02,
         split='calibration'),
    dict(key='ms_slope', name='Star-forming main-sequence slope (d log SFR / d log M*)',
         patterns=[r'main[-\s]?sequence', r'star[-\s]?forming sequence', r'\bSFR\b.{0,25}\bM', r'sSFR'],
         target=('the SLOPE of the star-forming main sequence, i.e. d log SFR / d log M* '
                 '(a dimensionless value typically between 0.4 and 1.1). '
                 'In "method" put the redshift-independent method/tracer if stated, else null'),
         lo=0.3, hi=1.3, unit='MS slope [dimensionless]', default_sig=0.08, min_sig=0.02,
         split='zbin'),
    dict(key='smf_mstar', name='Stellar mass function Schechter log M* (knee)',
         patterns=[r'mass function', r'Schechter', r'characteristic mass', r'M_?\*'],
         target=('the Schechter characteristic (knee) stellar mass log10(M*/Msun) of the '
                 'galaxy stellar mass function (a value between 10.0 and 11.6). '
                 'Do NOT extract the faint-end slope here'),
         lo=10.0, hi=11.6, unit='log M*_knee [log Msun]', default_sig=0.12, min_sig=0.03,
         split='zbin'),
    dict(key='fesc', name='LyC escape fraction f_esc',
         patterns=[r'escape fraction', r'f_?\s*esc', r'\bLyC\b', r'Lyman continuum'],
         target=('the Lyman-continuum escape fraction f_esc. Report it as a FRACTION between '
                 '0 and 1 (if the abstract gives a percent, divide by 100)'),
         lo=0.0, hi=1.0, unit='f_esc [fraction]', default_sig=0.08, min_sig=0.01,
         split='zbin'),
    dict(key='sfrd', name='Cosmic SFR density log psi(z)',
         patterns=[r'star formation rate density', r'\bSFRD\b', r'cosmic star formation'],
         target=('the cosmic star formation rate density, reported as log10(SFRD) in '
                 'log(Msun/yr/Mpc^3), a value typically between -3.5 and 0.0. '
                 'ALWAYS record the redshift z in "redshift"'),
         lo=-3.5, hi=0.2, unit='log SFRD [log Msun/yr/Mpc^3]', default_sig=0.15, min_sig=0.03,
         split='zbin'),
    dict(key='uvlf_alpha', name='UV luminosity-function faint-end slope alpha',
         patterns=[r'luminosity function', r'faint[-\s]?end slope', r'\balpha\b'],
         target=('the faint-end slope alpha of the (rest-frame UV) galaxy luminosity function, '
                 'a NEGATIVE value typically between -2.6 and -1.0. Record redshift in "redshift"'),
         lo=-2.8, hi=-1.0, unit='UVLF alpha [dimensionless]', default_sig=0.10, min_sig=0.02,
         split='zbin'),
    dict(key='quiescent_frac', name='Quiescent / quenched fraction',
         patterns=[r'quiescent fraction', r'quenched fraction', r'passive fraction'],
         mass_ext=True, mass_cap=92,
         target=('the quiescent (quenched/passive) fraction of galaxies at a stated mass and '
                 'redshift, a FRACTION between 0 and 1 (percent -> divide by 100). '
                 'Record redshift in "redshift"'),
         lo=0.0, hi=1.0, unit='quiescent fraction', default_sig=0.08, min_sig=0.01,
         split='zbin'),
    # ----------------------------------------------------------------- v2.1 WIDENED registry
    # 12 new quantities chosen to COVER GA clusters that had no measured quantity in v2
    # (clusters 53,50,28,13,51,52,54,31,35,40). Each keeps the original schema; cap=120
    # bounds NEW LLM calls per quantity. z_dependent flags whether z-binning is expected to
    # matter (local abundance/IMF quantities collapse to a single z-bin -> coverage, not de-mixing).
    dict(key='stellar_feh', name='Stellar metallicity [Fe/H]',
         patterns=[r'\[Fe/H\]', r'metallicit', r'iron abundance'],
         priority=[r'\[Fe/H\]\s*[=~<>]', r'\[Fe/H\]\s*(of|=)', r'mean\s*\[Fe/H\]'],
         cap=120, z_dependent=False,
         target=('the stellar iron abundance [Fe/H] in dex (a value typically between -4.0 and +0.6). '
                 'In "method" put the survey/pipeline if stated (APOGEE, GALAH, LAMOST, isochrone), else null'),
         lo=-4.0, hi=0.7, unit='[Fe/H] [dex]', default_sig=0.12, min_sig=0.02, split='zbin'),
    dict(key='alpha_fe', name='Alpha-element ratio [alpha/Fe]',
         patterns=[r'\[alpha/Fe\]', r'\[α/Fe\]', r'\[[A-Za-z]{1,2}/Fe\]', r'alpha[-\s]?enhanc', r'abundance ratio'],
         cap=120, z_dependent=False,
         target=('the alpha-to-iron abundance ratio [alpha/Fe] (or a specific [X/Fe] such as [Mg/Fe], [O/Fe]) '
                 'in dex, a value typically between -0.2 and +0.7'),
         lo=-0.3, hi=0.8, unit='[alpha/Fe] [dex]', default_sig=0.08, min_sig=0.02, split='zbin'),
    dict(key='edd_ratio', name='AGN Eddington ratio log(L/L_Edd)',
         patterns=[r'Eddington ratio', r'Eddington[-\s]?limited', r'L/L_?Edd', r'lambda_?Edd', r'\bEddington\b'],
         cap=120, z_dependent=True,
         target=('the AGN Eddington ratio, reported as log10(L_bol/L_Edd) (a value typically between -4 and +0.5); '
                 'if given as a linear fraction, take its base-10 log. Skip pure black-hole masses'),
         lo=-4.0, hi=0.6, unit='log Eddington ratio', default_sig=0.3, min_sig=0.05, split='zbin'),
    dict(key='gas_fraction', name='Molecular/cold gas fraction f_gas',
         patterns=[r'gas fraction', r'molecular gas', r'depletion time', r'f_?gas', r'\bH2\b', r'H_?2 mass'],
         cap=120, z_dependent=True, mass_ext=True, mass_cap=92,
         target=('the molecular (or cold) gas fraction f_gas = M_gas/(M_gas+M_star) OR M_gas/M_star, '
                 'reported as a FRACTION between 0 and 3 (if a percent, divide by 100). '
                 'Do NOT report depletion times or absolute gas masses here'),
         lo=0.0, hi=3.0, unit='gas fraction', default_sig=0.15, min_sig=0.03, split='zbin'),
    dict(key='size_re', name='Galaxy effective radius R_e',
         patterns=[r'size-mass', r'mass-size', r'effective radius', r'half-light radius',
                   r'half-mass radius', r'\bR_e\b', r'R_\{?e', r'r_?eff\b'],
         cap=120, z_dependent=True, mass_ext=True, mass_cap=92,
         target=('the galaxy effective (half-light) radius R_e in kiloparsec (kpc), a value typically 0.3-30 kpc. '
                 'Only extract sizes already in kpc; skip arcsec-only values'),
         lo=0.2, hi=30.0, unit='R_e [kpc]', default_sig=0.3, min_sig=0.05, split='zbin'),
    dict(key='tully_fisher', name='Rotation velocity (Tully-Fisher)',
         patterns=[r'Tully-Fisher', r'rotation velocity', r'v_?rot', r'V_?max', r'rotation curve', r'circular velocity'],
         cap=120, z_dependent=True,
         target=('the galaxy maximum rotation / circular velocity V_rot (or V_max) in km/s, typically 30-500 km/s'),
         lo=20.0, hi=600.0, unit='V_rot [km/s]', default_sig=15.0, min_sig=3.0, split='zbin'),
    dict(key='veldisp', name='Stellar velocity dispersion sigma',
         patterns=[r'velocity dispersion', r'dynamical mass', r'sigma_?\*', r'sigma_?star', r'\bsigma_?0\b'],
         cap=120, z_dependent=True, mass_ext=True, mass_cap=92,
         target=('the stellar velocity dispersion sigma in km/s (a value typically 5-400 km/s). '
                 'Do NOT report galaxy-cluster velocity dispersions of thousands of km/s'),
         lo=3.0, hi=450.0, unit='sigma [km/s]', default_sig=15.0, min_sig=3.0, split='zbin'),
    dict(key='imf_slope', name='IMF high-mass slope',
         patterns=[r'initial mass function', r'\bIMF\b', r'IMF slope', r'high-mass slope', r'mass function slope'],
         cap=120, z_dependent=False,
         target=('the stellar initial mass function (IMF) high-mass power-law slope (Salpeter = 2.35), '
                 'a value typically between 1.5 and 3.5. Report the |slope| as a positive number'),
         lo=1.5, hi=3.5, unit='IMF slope', default_sig=0.2, min_sig=0.05, split='zbin'),
    dict(key='dust_atten', name='Dust attenuation A_V',
         patterns=[r'attenuation', r'\bIRX\b', r'A_?V\b', r'dust law', r'extinction curve', r'E\(B-V\)'],
         cap=120, z_dependent=True, mass_ext=True, mass_cap=92,
         target=('the dust attenuation A_V in magnitudes (typically 0-6 mag). '
                 'If only E(B-V) is given, multiply by ~4.05 to get A_V'),
         lo=0.0, hi=6.0, unit='A_V [mag]', default_sig=0.3, min_sig=0.05, split='zbin'),
    dict(key='metal_gradient', name='Radial metallicity gradient',
         patterns=[r'metallicity gradient', r'abundance gradient', r'dex/kpc', r'radial gradient', r'radial metallicity'],
         cap=120, z_dependent=True,
         target=('the radial metallicity (abundance) gradient in dex/kpc, typically a NEGATIVE value '
                 'between -0.2 and +0.1'),
         lo=-0.2, hi=0.1, unit='gradient [dex/kpc]', default_sig=0.02, min_sig=0.005, split='zbin'),
    dict(key='massloss', name='Evolved-star mass-loss rate log Mdot',
         patterns=[r'mass-loss rate', r'mass loss rate', r'\bMdot\b', r'dM/dt', r'wind.{0,15}mass'],
         cap=120, z_dependent=False,
         target=('the stellar mass-loss rate, reported as log10(Mdot) in log(Msun/yr), typically between -9 and -3. '
                 'If given as a linear rate, take its base-10 log'),
         lo=-9.0, hi=-3.0, unit='log Mdot [log Msun/yr]', default_sig=0.4, min_sig=0.05, split='zbin'),
    dict(key='tde_mbh', name='TDE black-hole mass log M_BH',
         patterns=[r'tidal disruption', r'\bTDE\b', r'\bTDEs\b', r'disrupt'],
         priority=[r'tidal disruption', r'M_?BH'],
         cap=120, z_dependent=False,
         target=('the central black hole mass inferred for a tidal disruption event (TDE) host, '
                 'reported as log10(M_BH/Msun), typically between 5.0 and 8.5'),
         lo=4.5, hi=8.8, unit='log M_BH [log Msun]', default_sig=0.4, min_sig=0.1, split='zbin'),
]

# --------------------------------------------------------------------------- calibration canonicalization
_CAL_RULES = [
    ('Te/direct', [r'\bt_?e\b', r'direct', r'electron temperature', r'auroral', r'\[?o\s*iii\]?\s*4363', r'4363']),
    ('T04/Tremonti', [r'tremonti', r'\bt04\b', r'\bt0?4\b']),
    ('PP04-O3N2', [r'o3n2']),
    ('PP04-N2', [r'\bn2\b', r'pp04.*n2', r'pettini.*pagel']),
    ('KK04', [r'\bkk04\b', r'kobulnicky', r'kewley.*kobulnicky']),
    ('R23', [r'\br23\b', r'r_?23']),
    ('Sanders', [r'sanders']),
    ('Maiolino', [r'maiolino']),
    ('Curti', [r'curti']),
    ('other-strong-line', [r'strong[-\s]?line', r'\bn2\b', r'\bo3\b', r'bpt', r'calibrat']),
]
_QMAP = {q['key']: q for q in QUANTITIES}

def canon_calibration(method):
    if not method:
        return 'unknown'
    m = str(method).lower()
    for name, pats in _CAL_RULES:
        for p in pats:
            if re.search(p, m):
                return name
    return 'unknown'

# --------------------------------------------------------------------------- redshift parsing
_ZNUM = re.compile(r'[-+]?\d+(?:\.\d+)?')
def parse_redshift(z):
    """Return a representative float redshift from a value/string, or None."""
    if z is None:
        return None
    if isinstance(z, (int, float)):
        return float(z)
    s = str(z).lower().replace('~', ' ').replace('=', ' ')
    nums = [float(x) for x in _ZNUM.findall(s)]
    nums = [x for x in nums if -0.01 <= x <= 20]
    if not nums:
        return None
    return sum(nums) / len(nums)          # midpoint of a range

# v2.1 redshift bins: compare measurements of the SAME quantity at the SAME epoch.
Z_EDGES = [(0.0, 0.3), (0.3, 1.0), (1.0, 2.0), (2.0, 3.0), (3.0, 5.0), (5.0, 7.0), (7.0, 99.0)]
def zbin_label(zf):
    if zf is None:
        return 'z?'
    for lo, hi in Z_EDGES:
        if lo <= zf < hi:
            return 'z%g-%g' % (lo, hi)
    return 'z?'

# --------------------------------------------------------------------------- v2.2 stellar-mass axis
# Mass-dependent quantities (esp. gas metallicity via the mass-metallicity relation) conflate the
# MASS SEQUENCE with genuine measurement disagreement. Binning by log(M*/Msun) removes the MZR so
# residual over-dispersion at fixed (z, mass[, calibration]) is genuine tension.
MASS_EDGES = [8.0, 9.0, 10.0, 11.0]     # bin boundaries -> <8, 8-9, 9-10, 10-11, >=11, plus mass-unknown
def massbin_label(m):
    if m is None:
        return 'm?'
    if m < 8.0:
        return 'mlt8'
    if m < 9.0:
        return 'm8-9'
    if m < 10.0:
        return 'm9-10'
    if m < 11.0:
        return 'm10-11'
    return 'mge11'

def parse_logmstar(m):
    """Return a representative log10(M*/Msun) float, or None.

    Accepts a number (log already, or linear mass -> take log10), or a string that may hold a
    single value or a RANGE/bin (take the midpoint). Guards to a sane 4.0-13.5 dex window.
    """
    if m is None:
        return None
    if isinstance(m, (int, float)):
        v = float(m)
        if v > 20:                       # linear mass mistakenly returned -> log it
            v = math.log10(v) if v > 0 else None
        return v if (v is not None and 4.0 <= v <= 13.5) else None
    s = str(m).strip().lower()
    if not s or s in ('null', 'none', 'nan'):
        return None
    try:                                 # direct float handles exponent forms like 3e10
        v = float(s.replace('~', '').replace('=', ''))
        if v > 20:
            v = math.log10(v) if v > 0 else None
        return v if (v is not None and 4.0 <= v <= 13.5) else None
    except Exception:
        pass
    s2 = s.replace('~', ' ').replace('=', ' ').replace(' to ', ' ')
    s2 = re.sub(r'(\d)\s*[-–]\s*(\d)', r'\1 \2', s2)   # hyphen/en-dash between digits = RANGE, not minus
    nums = [abs(float(x)) for x in _ZNUM.findall(s2)]       # masses are positive
    nums = [x for x in nums if 0.0 < x < 14.0]              # keep log-scale numbers, drop stray digits
    if not nums:
        return None
    v = sum(nums) / len(nums)            # midpoint of a range/bin
    return v if 4.0 <= v <= 13.5 else None

# --------------------------------------------------------------------------- Ollama extraction
def _ollama(prompt, model, n=520, temp=0.0, timeout=120):
    body = json.dumps({'model': model, 'prompt': prompt, 'stream': False,
                       'options': {'num_predict': n, 'temperature': temp}}).encode()
    req = urllib.request.Request(OLLAMA_GEN, data=body, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return (json.loads(r.read().decode()).get('response') or '').strip()

def _parse_json_array(text):
    i, j = text.find('['), text.rfind(']')
    if 0 <= i < j:
        try:
            d = json.loads(text[i:j + 1])
            if isinstance(d, list):
                return d
        except Exception:
            pass
    out = []
    for m in re.finditer(r'\{[^{}]*\}', text):
        try:
            out.append(json.loads(m.group(0)))
        except Exception:
            pass
    return out

def build_prompt(q, abstract):
    # v2.2: mass-augmented quantities additionally capture the stellar mass the value refers to,
    # so cells can bin by (z x mass[ x calibration]). Non-mass quantities keep the v2.1 prompt/schema
    # EXACTLY (so their v2.1 cache stays valid and is reused).
    if q.get('mass_ext'):
        return (
            'You extract measured NUMERIC results from an astronomy abstract. Extract ' + q['target'] + '.\n'
            'Also record log_mstar: the stellar mass log10(M*/Msun) that THIS value refers to (e.g. the '
            'mass bin, sample median, or stated stellar mass). If a mass RANGE or bin is given, use its '
            'midpoint. If the value is a linear mass, take log10. Set log_mstar=null if no stellar mass '
            'is stated for that value.\n'
            'Return ONLY a JSON array. Each element:\n'
            '{"value": number, "err_low": number|null, "err_high": number|null, '
            '"redshift": "z value or range as string"|null, "method": "calibration/method"|null, '
            '"log_mstar": number|null, "is_measurement": true|false}\n'
            'Rules: include ONLY concrete measured or fitted values that a reader could read off this '
            'abstract; set is_measurement=false for values that are assumed/adopted/from a model or prior '
            'work; skip anything that is not this specific quantity; skip sample sizes and bin counts. '
            'If the abstract reports none, return [].\n\n'
            'ABSTRACT:\n' + abstract[:2600] + '\n\nJSON array only:')
    return (
        'You extract measured NUMERIC results from an astronomy abstract. Extract ' + q['target'] + '.\n'
        'Return ONLY a JSON array. Each element:\n'
        '{"value": number, "err_low": number|null, "err_high": number|null, '
        '"redshift": "z value or range as string"|null, "method": "calibration/method"|null, '
        '"is_measurement": true|false}\n'
        'Rules: include ONLY concrete measured or fitted values that a reader could read off this '
        'abstract; set is_measurement=false for values that are assumed/adopted/from a model or prior '
        'work; skip anything that is not this specific quantity; skip sample sizes and bin counts. '
        'If the abstract reports none, return [].\n\n'
        'ABSTRACT:\n' + abstract[:2600] + '\n\nJSON array only:')

# --------------------------------------------------------------------------- PDG dispersion math
def weighted_mean(vals, sigs):
    w = [1.0 / (s * s) for s in sigs]
    sw = sum(w)
    xm = sum(v * wi for v, wi in zip(vals, w)) / sw
    return xm, sw

def pdg_scale(vals, sigs):
    """Return (N, wmean, wmean_err, chi2, S, robust_overdisp)."""
    n = len(vals)
    if n < 2:
        return n, (vals[0] if vals else None), None, None, None, None
    xm, sw = weighted_mean(vals, sigs)
    chi2 = sum((v - xm) ** 2 / (s * s) for v, s in zip(vals, sigs))
    S = math.sqrt(chi2 / (n - 1))
    # robust over-dispersion: MAD-based scatter of values / median sigma
    med = sorted(vals)[n // 2]
    mad = sorted(abs(v - med) for v in vals)[n // 2] * 1.4826
    med_sig = sorted(sigs)[n // 2]
    robust = (mad / med_sig) if med_sig > 0 else None
    return n, xm, math.sqrt(1.0 / sw), chi2, S, robust

# --------------------------------------------------------------------------- stage 1: prefilter
def compile_patterns(q):
    return [re.compile(p, re.IGNORECASE) for p in q['patterns']]

def prefilter(labels):
    """Stream corpus once. Return per-quantity candidate lists [(citation, bibcode, cluster, prio)]."""
    comp = {q['key']: compile_patterns(q) for q in QUANTITIES}
    prio = {q['key']: [re.compile(p, re.IGNORECASE) for p in q.get('priority', [])] for q in QUANTITIES}
    cands = {q['key']: [] for q in QUANTITIES}
    n = 0
    with open(CORPUS) as f:
        for line in f:
            n += 1
            r = json.loads(line)
            ab = r.get('abstract') or ''
            if not ab:
                continue
            bib = r['bibcode']
            cl = labels.get(bib)
            cit = r.get('citation_count') or 0
            for q in QUANTITIES:
                for rx in comp[q['key']]:
                    if rx.search(ab):
                        p = 1 if any(px.search(ab) for px in prio[q['key']]) else 0
                        cands[q['key']].append((cit, bib, cl, p))
                        break
    return cands, n

# --------------------------------------------------------------------------- stage 2: extract
def load_cache():
    if os.path.exists(CACHE):
        try:
            return json.load(open(CACHE))
        except Exception:
            return {}
    return {}

def save_cache(cache):
    tmp = CACHE + '.tmp'
    json.dump(cache, open(tmp, 'w'))
    os.replace(tmp, CACHE)

def fetch_abstracts(need_bibcodes):
    """Second corpus pass: pull abstracts (+cluster already known) for the selected bibcodes."""
    out = {}
    need = set(need_bibcodes)
    with open(CORPUS) as f:
        for line in f:
            r = json.loads(line)
            b = r['bibcode']
            if b in need:
                out[b] = r.get('abstract') or ''
                if len(out) == len(need):
                    break
    return out

def extract_all(cands, labels, model, cap_per_q, max_total, verbose=True):
    cache = load_cache()
    # select candidates: dedupe by bibcode (a paper can appear once per quantity), citation desc
    plan = []          # (qkey, bibcode, cluster)
    for q in QUANTITIES:
        seen = set()
        # priority-matching abstracts first (prio desc), then citation desc, bibcode tiebreak
        ranked = sorted(cands[q['key']], key=lambda t: (-t[3], -t[0], t[1]))
        # v2.2: mass-augmented quantities use mass_cap (bounds the NEW mass re-extraction);
        # all others keep their existing cap so their v2.1 cache is reused with no new calls.
        qcap = q.get('mass_cap') if q.get('mass_ext') else q.get('cap', cap_per_q)
        picked = 0
        for cit, bib, cl, prio in ranked:
            if bib in seen:
                continue
            seen.add(bib)
            plan.append((q['key'], bib, cl, cit))
            picked += 1
            if picked >= qcap:
                break
    # enforce global cap while keeping a balanced round-robin across quantities
    if len(plan) > max_total:
        byq = collections.defaultdict(list)
        for item in plan:
            byq[item[0]].append(item)
        balanced, i = [], 0
        keys = [q['key'] for q in QUANTITIES]
        while len(balanced) < max_total:
            adv = False
            for k in keys:
                if i < len(byq[k]):
                    balanced.append(byq[k][i]); adv = True
                    if len(balanced) >= max_total:
                        break
            if not adv:
                break
            i += 1
        plan = balanced

    # bibcodes whose (qkey,bib) extraction is not cached -> need their abstract text
    need = set()
    for qkey, bib, cl, cit in plan:
        if cache_key(_QMAP[qkey], bib) not in cache:
            need.add(bib)
    abstracts = fetch_abstracts(need) if need else {}

    qmap = _QMAP
    results = []       # flat measurement records
    t0 = time.time()
    n_calls = 0
    for idx, (qkey, bib, cl, cit) in enumerate(plan):
        ck = cache_key(_QMAP[qkey], bib)
        if ck in cache:
            raw = cache[ck]
        else:
            ab = abstracts.get(bib, '')
            if not ab:
                cache[ck] = []
                continue
            try:
                resp = _ollama(build_prompt(qmap[qkey], ab), model)
                raw = _parse_json_array(resp)
                n_calls += 1
            except Exception as e:
                raw = []
                if verbose:
                    sys.stderr.write('  extract fail %s: %s\n' % (bib, e))
            cache[ck] = raw
            if n_calls % 25 == 0:
                save_cache(cache)
                if verbose:
                    rate = n_calls / max(1e-9, time.time() - t0)
                    sys.stderr.write('  [%d/%d] %d LLM calls, %.2f/s\n' % (idx + 1, len(plan), n_calls, rate))
        # normalize this paper's extractions for this quantity
        q = qmap[qkey]
        for e in (raw or []):
            if not isinstance(e, dict):
                continue
            v = e.get('value')
            if isinstance(v, str):
                mm = _ZNUM.findall(v.replace('%', ''))
                v = float(mm[0]) if mm else None
            if v is None or not isinstance(v, (int, float)):
                continue
            v = float(v)
            # fesc / fractions given as percent
            if q['key'] in ('fesc', 'quiescent_frac') and v > 1.0:
                v = v / 100.0
            if not (q['lo'] <= v <= q['hi']):
                continue
            if e.get('is_measurement') is False:
                continue
            el, eh = e.get('err_low'), e.get('err_high')
            def _num(x):
                if isinstance(x, (int, float)):
                    return abs(float(x))
                if isinstance(x, str):
                    mm = _ZNUM.findall(x.replace('%', ''))
                    return abs(float(mm[0])) if mm else None
                return None
            el, eh = _num(el), _num(eh)
            if q['key'] in ('fesc', 'quiescent_frac'):
                if el and el > 1: el /= 100.0
                if eh and eh > 1: eh /= 100.0
            defaulted = False
            if el is None and eh is None:
                sig = q['default_sig']; defaulted = True
            else:
                sig = ((el or eh) + (eh or el)) / 2.0
            sig = max(sig, q['min_sig'])
            results.append(dict(
                quantity=qkey, bibcode=bib, cluster=cl, citation=cit,
                value=v, sigma=sig, defaulted_err=defaulted,
                redshift=parse_redshift(e.get('redshift')),
                method_raw=e.get('method'),
                calibration=canon_calibration(e.get('method')),
                log_mstar=(parse_logmstar(e.get('log_mstar')) if q.get('mass_ext') else None),
            ))
    save_cache(cache)
    return results, plan, n_calls

# --------------------------------------------------------------------------- stage 3: dispersion
def cell_of(q, r):
    """Primary same-epoch cell key.

    v2.2: for mass-dependent (mass_ext) quantities the cell gains a STELLAR-MASS axis, so the
    finest cell is (z-bin, mass-bin[, calibration]). Non-mass quantities are unchanged from v2.1:
    z-bin, or (z-bin, calibration) for the calibration-axis quantity (metallicity).
        metallicity     -> (z, mass, calibration)
        other mass_ext  -> (z, mass)
        everything else -> (z,)
    """
    parts = [zbin_label(r['redshift'])]
    if q.get('mass_ext'):
        parts.append(massbin_label(r.get('log_mstar')))
    if q['split'] == 'calibration':
        parts.append(r['calibration'])
    return tuple(parts)

def pooled_over(rs, keyfn):
    """Pool within-group chi2 over the groups induced by keyfn -> one 'within' scale factor S."""
    groups = collections.defaultdict(list)
    for r in rs:
        groups[keyfn(r)].append(r)
    return pooled_S(groups)

def pooled_S(groups):
    """Pool within-group chi2 over groups with N>=2 -> one 'within' scale factor S (and dof)."""
    pc, pd = 0.0, 0
    for gr in groups.values():
        if len(gr) >= 2:
            _, _, _, gchi2, _, _ = pdg_scale([x['value'] for x in gr], [x['sigma'] for x in gr])
            pc += gchi2
            pd += (len(gr) - 1)
    return (math.sqrt(pc / pd) if pd > 0 else None), pd

def disperse(results):
    """v2.1: dispersion computed WITHIN same-epoch cells (z-bin, or z-bin x calibration).

    Per quantity we report:
        S_all      : old all-in PDG scale factor (all measurements pooled) -- the confounded number.
        S_zonly    : pooled within z-bin (removes redshift-mixing).
        S_calonly  : pooled within calibration (metallicity diagnostic; ~S_all for others).
        S_zcal     : pooled within the PRIMARY cell (z, or z x calibration) -- fully de-mixed.
        S_contest  : citation-weighted mean of per-cell S over WELL-POPULATED cells (N>=3).
                     This is the genuine same-epoch disagreement used to score clusters.
    """
    byq = collections.defaultdict(list)
    for r in results:
        byq[r['quantity']].append(r)
    out = []
    for q in QUANTITIES:
        rs = byq.get(q['key'], [])
        vals = [r['value'] for r in rs]
        sigs = [r['sigma'] for r in rs]
        N = len(rs)
        mass_ext = q.get('mass_ext', False)
        rec = dict(quantity=q['key'], name=q['name'], unit=q['unit'], split_axis=q['split'],
                   z_dependent=q.get('z_dependent', True), mass_ext=mass_ext, N=N, reported=(N >= 5),
                   n_zunknown=sum(1 for r in rs if r['redshift'] is None),
                   n_massunknown=(sum(1 for r in rs if r.get('log_mstar') is None) if mass_ext else None),
                   mass_unknown_frac=(round(sum(1 for r in rs if r.get('log_mstar') is None) / N, 3)
                                      if (mass_ext and N) else None))
        if N >= 2:
            n, xm, xe, chi2, S, robust = pdg_scale(vals, sigs)
            rec.update(weighted_mean=round(xm, 4), wmean_err=(round(xe, 4) if xe else None),
                       chi2=round(chi2, 2), S_all=round(S, 3),
                       robust_overdisp=(round(robust, 2) if robust else None),
                       value_min=round(min(vals), 4), value_max=round(max(vals), 4),
                       defaulted_err_frac=round(sum(r['defaulted_err'] for r in rs) / N, 3))
        # ---- grouping axes (v2.2 adds the mass axis for mass_ext quantities)
        zg = collections.defaultdict(list)     # z-bin only
        cg = collections.defaultdict(list)     # calibration only
        cells = collections.defaultdict(list)  # primary cell = finest (z[, mass][, cal])
        for r in rs:
            zg[zbin_label(r['redshift'])].append(r)
            cg[r['calibration']].append(r)
            cells[cell_of(q, r)].append(r)
        S_zonly, _ = pooled_S(zg)
        S_calonly, _ = pooled_S(cg)
        # named cascade axes (computed regardless so metallicity's known-answer cascade is explicit)
        S_zcal, _ = pooled_over(rs, lambda r: (zbin_label(r['redshift']), r['calibration']))
        S_massonly = S_zmass = S_zmasscal = None
        if mass_ext:
            S_massonly, _ = pooled_over(rs, lambda r: (massbin_label(r.get('log_mstar')),))
            S_zmass, _ = pooled_over(rs, lambda r: (zbin_label(r['redshift']),
                                                    massbin_label(r.get('log_mstar'))))
            S_zmasscal, _ = pooled_over(rs, lambda r: cell_of(q, r))   # z x mass [x cal] = primary
        S_primary, _ = pooled_S(cells)   # pooled within the finest cell
        # ---- per-cell detail + well-populated (N>=3) cells
        cell_rec = {}
        well = []                              # (S, N, cite, zbin)
        for ck, cr in sorted(cells.items(), key=lambda kv: -len(kv[1])):
            gv = [x['value'] for x in cr]; gs = [x['sigma'] for x in cr]; gN = len(cr)
            cite = sum(x['citation'] for x in cr)
            label = '|'.join(ck)
            if gN >= 2:
                _, gxm, _, _, gS, _ = pdg_scale(gv, gs)
                cell_rec[label] = dict(N=gN, wmean=round(gxm, 4), S=round(gS, 3), cite=cite, well=(gN >= 3))
                if gN >= 3:
                    well.append((gS, gN, cite, ck[0]))
            else:
                cell_rec[label] = dict(N=gN, wmean=round(gv[0], 4), S=None, cite=cite, well=False)
        rec['cells'] = cell_rec
        # ---- aggregated contestation over well-populated cells
        if well:
            num = den = 0.0; mx = 0.0; zbset = set()
            for gS, gN, cite, zb in well:
                w = math.log1p(cite) + gN
                num += gS * w; den += w
                mx = max(mx, gS)
                if zb != 'z?':
                    zbset.add(zb)
            rec['S_contest'] = round(num / den, 3)
            rec['S_contest_max'] = round(mx, 3)
            rec['n_wellcells'] = len(well)
            rec['n_zbins_pop'] = len(zbset) if zbset else (1 if well else 0)
        else:
            rec['S_contest'] = None; rec['S_contest_max'] = None
            rec['n_wellcells'] = 0; rec['n_zbins_pop'] = 0
        rec['S_zonly'] = round(S_zonly, 3) if S_zonly is not None else None
        rec['S_calonly'] = round(S_calonly, 3) if S_calonly is not None else None
        rec['S_zcal'] = round(S_zcal, 3) if S_zcal is not None else None            # within (z x cal); v2.1 number
        rec['S_massonly'] = round(S_massonly, 3) if S_massonly is not None else None
        rec['S_zmass'] = round(S_zmass, 3) if S_zmass is not None else None          # within (z x mass)
        rec['S_zmasscal'] = round(S_zmasscal, 3) if S_zmasscal is not None else None # within (z x mass x cal) v2.2
        # mass-attributable drop for metallicity: how much the MASS axis removes beyond (z x cal)
        if mass_ext and S_zcal is not None and S_zmasscal is not None:
            rec['mass_drop'] = round(S_zcal - S_zmasscal, 3)
            rec['mass_drop_frac'] = round((S_zcal - S_zmasscal) / S_zcal, 3) if S_zcal > 0 else None
        else:
            rec['mass_drop'] = None; rec['mass_drop_frac'] = None
        rec['S_split'] = round(S_primary, 3) if S_primary is not None else None      # backward-compat: finest de-mixed
        rec['zbin_N'] = {k: len(v) for k, v in sorted(zg.items())}
        rec['massbin_N'] = ({k: c for k, c in sorted(collections.Counter(
            massbin_label(r.get('log_mstar')) for r in rs).items())} if mass_ext else None)
        # ---- between-group offsets (regime-mixing evidence)
        def _means(groups, drop_unknown=False):
            ms = []
            for k, v in groups.items():
                if drop_unknown and k in ('unknown', 'z?'):
                    continue
                if len(v) >= 2:
                    _, m, _, _, _, _ = pdg_scale([x['value'] for x in v], [x['sigma'] for x in v])
                    ms.append(m)
            return ms
        zms = _means(zg, drop_unknown=True)
        cms = _means(cg, drop_unknown=True)
        rec['between_z_offset'] = round(max(zms) - min(zms), 4) if len(zms) >= 2 else None
        rec['between_cal_offset'] = round(max(cms) - min(cms), 4) if len(cms) >= 2 else None
        # legacy field name kept so old readers don't break (calibration for metallicity, else z)
        rec['between_group_offset'] = (rec['between_cal_offset'] if q['split'] == 'calibration'
                                       else rec['between_z_offset'])
        rec['verdict'] = verdict(rec)
        out.append(rec)
    return out

def verdict(rec):
    N = rec.get('N', 0)
    if N < 5:
        return 'insufficient (N<5)'
    S_all = rec.get('S_all')
    Sc = rec.get('S_contest')
    if S_all is None:
        return 'insufficient'
    if Sc is None:
        return 'no same-epoch cell (N>=3); cannot isolate (raw S_all=%.1f)' % S_all
    frac_removed = (S_all - Sc) / S_all if S_all > 0 else 0.0
    if Sc > 2.0:
        base = 'contested (same-epoch)'
    elif Sc > 1.4:
        base = 'mild same-epoch over-dispersion'
    else:
        base = 'consistent within epoch'
    if S_all > 1.5 and frac_removed >= 0.25:
        base += ' + raw S inflated by regime-mixing'
    return base

# --------------------------------------------------------------------------- stage 4+5: attribute + rescore
def minmax(x, lo, hi):
    return (x - lo) / (hi - lo) if hi > lo else 0.0

def attribute_and_rescore(results, disp, fm):
    clusters = fm['clusters']
    by_cl = {c['cluster']: c for c in clusters}
    # per-quantity tension amplitude = S_contest (citation-weighted within-(z[,cal]) cell S).
    # This is GENUINE same-epoch disagreement: z-mixing and calibration offsets are removed.
    qS = {}
    for d in disp:
        s = d.get('S_contest')
        if s is not None:
            qS[d['quantity']] = dict(S=s, z_cells=d.get('n_zbins_pop', 0),
                                     wellcells=d.get('n_wellcells', 0))
    # aggregate measurements to clusters
    cl_hits = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
    for r in results:
        cl = r['cluster']
        if cl is None or cl == -1:
            continue
        if r['quantity'] not in qS:
            continue
        h = cl_hits[cl][r['quantity']]
        h[0] += 1
        h[1] += r['citation']
    cl_tension = {}
    for cl, qd in cl_hits.items():
        # citation-weighted mean S over the quantities this cluster measures, needs >=3 meas of a q
        num, den, contrib = 0.0, 0.0, {}
        best = 0.0
        for qk, (nh, cw) in qd.items():
            if nh < 3:
                continue
            s = qS[qk]['S']
            w = math.log1p(cw) + nh
            num += s * w
            den += w
            contrib[qk] = dict(n=nh, S=round(s, 3), cite=cw, z_cells=qS[qk]['z_cells'])
            best = max(best, s)
        if den > 0:
            cl_tension[cl] = dict(tension_v2_cwmean=num / den, tension_v2_max=best, contrib=contrib)
    # build rows in the v1 style, add tension_v2
    rows = []
    for c in clusters:
        cl = c['cluster']
        t = cl_tension.get(cl)
        rows.append(dict(
            cluster=cl, keywords=c.get('keywords', []),
            activity=c.get('recent_cites_per_paper') or 0.0,
            recent_frac=c.get('recent_frac') or 0.0,
            frontier_score_cite=c.get('frontier_score_cite') or 0.0,
            sat_activity=c.get('sat_activity') or 0.0,
            tractable=c.get('tractable', 0),
            growth_norm=c.get('growth_norm') or 0.0,
            strict_tension=c.get('strict_tension') or 0.0,
            tension_norm_v1=c.get('tension_norm') or 0.0,
            score_v1=c.get('score_v1') or 0.0,
            tension_v2_raw=(t['tension_v2_cwmean'] if t else 0.0),
            tension_v2_max=(t['tension_v2_max'] if t else 0.0),
            v2_contrib=(t['contrib'] if t else {}),
        ))
    # normalize tension_v2 across GA-dominant clusters (min-max), mirror v1's approach
    ga = [r for r in rows if r['tractable'] == 1]
    tv = [r['tension_v2_raw'] for r in ga]
    tmin, tmax = (min(tv), max(tv)) if tv else (0.0, 1.0)
    for r in rows:
        r['tension_v2_norm'] = minmax(r['tension_v2_raw'], tmin, tmax) if r['tractable'] == 1 else 0.0
        r['score_v2'] = r['sat_activity'] * r['tractable'] * (0.6 * r['tension_v2_norm'] + 0.4 * r['growth_norm'])
    return rows, (tmin, tmax)

# --------------------------------------------------------------------------- reporting
def kw(r, k=6):
    return ', '.join(r['keywords'][:k])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cap-per-quantity', type=int, default=120)
    ap.add_argument('--max-total', type=int, default=1000)
    ap.add_argument('--model', default=FAST_MODEL)
    ap.add_argument('--prefilter-only', action='store_true')
    args = ap.parse_args()

    print('== loading labels + frontier_map_v3 ==')
    labels = json.load(open(LABELS))
    fm = json.load(open(V3))

    print('== STAGE 1: prefilter (streaming %s abstracts) ==' % '120,676')
    t0 = time.time()
    cands, ntot = prefilter(labels)
    print('   scanned %d lines in %.1fs' % (ntot, time.time() - t0))
    print('\n   PREFILTER YIELD TABLE')
    print('   %-16s %10s %10s' % ('quantity', 'candidates', 'unique'))
    yield_tbl = {}
    for q in QUANTITIES:
        c = cands[q['key']]
        uniq = len(set(t[1] for t in c))
        yield_tbl[q['key']] = dict(candidates=len(c), unique=uniq)
        print('   %-16s %10d %10d' % (q['key'], len(c), uniq))

    if args.prefilter_only:
        json.dump(dict(yield_table=yield_tbl, scanned=ntot), open(JOB_TMP + 'prefilter_yield.json', 'w'), indent=2)
        print('\nprefilter-only: wrote', JOB_TMP + 'prefilter_yield.json')
        return

    print('\n== STAGE 2: extract (model=%s, cap/q=%d, max_total=%d) ==' % (args.model, args.cap_per_quantity, args.max_total))
    t0 = time.time()
    results, plan, n_calls = extract_all(cands, labels, args.model, args.cap_per_quantity, args.max_total)
    print('   planned %d (quantity,paper) extractions; %d new LLM calls in %.1fs' % (len(plan), n_calls, time.time() - t0))
    print('   kept %d clean measurement records' % len(results))
    byq = collections.Counter(t[0] for t in plan)
    kept = collections.Counter(r['quantity'] for r in results)
    print('   %-16s %8s %8s %8s' % ('quantity', 'planned', 'meas', 'yield'))
    for q in QUANTITIES:
        pl = byq[q['key']]
        print('   %-16s %8d %8d %8s' % (q['key'], pl, kept[q['key']],
              ('%.2f' % (kept[q['key']] / pl) if pl else 'n/a')))

    # v2.2: mass-extraction yield + mass-unknown fraction for the re-extracted mass-dependent quantities
    print('\n   MASS-EXTRACTION YIELD (v2.2 re-extracted quantities)')
    print('   %-16s %6s %8s %8s %10s' % ('quantity', 'meas', 'mass_ok', 'mass_%', 'mass_unk_%'))
    for q in QUANTITIES:
        if not q.get('mass_ext'):
            continue
        rs = [r for r in results if r['quantity'] == q['key']]
        n = len(rs)
        mok = sum(1 for r in rs if r.get('log_mstar') is not None)
        print('   %-16s %6d %8d %8s %10s' % (
            q['key'], n, mok,
            ('%.2f' % (mok / n)) if n else 'n/a',
            ('%.2f' % ((n - mok) / n)) if n else 'n/a'))

    print('\n== STAGE 3: z x MASS-binned dispersion (PDG scale factor within same-epoch same-mass cells) ==')
    disp = disperse(results)
    print('   %-14s %4s %8s %8s %8s %8s %8s %5s %6s  %s' % (
        'quantity', 'N', 'S_all', 'S_zonly', 'S_zmass', 'S_zmc', 'S_cont', 'well', 'munk%', 'verdict'))
    for d in disp:
        if d['N'] < 2:
            print('   %-14s %4d   (too few)' % (d['quantity'], d['N']))
            continue
        # for mass_ext quantities show S_zmass / S_zmasscal; else fall back to S_zonly / S_zcal
        s_zm = d.get('S_zmass') if d.get('mass_ext') else d.get('S_zonly')
        s_zmc = d.get('S_zmasscal') if d.get('mass_ext') else d.get('S_zcal')
        print('   %-14s %4d %8s %8s %8s %8s %8s %5d %6s  %s' % (
            d['quantity'], d['N'],
            ('%.2f' % d['S_all']) if d.get('S_all') else 'n/a',
            ('%.2f' % d['S_zonly']) if d.get('S_zonly') else 'n/a',
            ('%.2f' % s_zm) if s_zm else 'n/a',
            ('%.2f' % s_zmc) if s_zmc else 'n/a',
            ('%.2f' % d['S_contest']) if d.get('S_contest') else 'n/a',
            d.get('n_wellcells', 0),
            ('%.0f' % (100 * d['mass_unknown_frac'])) if d.get('mass_unknown_frac') is not None else '-',
            d['verdict']))
    # metallicity known-answer decomposition -- THE POINT of v2.2: does the MASS axis (the MZR)
    # finally make S readable as genuine tension?
    md = next((d for d in disp if d['quantity'] == 'metallicity'), None)
    if md and md['N'] >= 2:
        def _f(x):
            return ('%.2f' % x) if x else 'n/a'
        print('\n   METALLICITY KNOWN-ANSWER CASCADE (12+log(O/H), N=%d, on the v2.2 mass-extracted set):' % md['N'])
        print('      S_all                          = %s   (raw, everything pooled -- confounded)' % _f(md['S_all']))
        print('      within z                S_zonly = %s   (removes redshift-mixing)' % _f(md['S_zonly']))
        print('      within (z x cal)        S_zcal  = %s   (removes z + calibration; v2.1 gave ~7.85)' % _f(md['S_zcal']))
        print('      within (z x mass x cal) S_zmc   = %s   <== v2.2: adds the STELLAR-MASS axis (MZR)' % _f(md['S_zmasscal']))
        drop = md.get('mass_drop'); dropf = md.get('mass_drop_frac')
        print('      -> MASS axis removes  Delta S = %s  (%.0f%% of the within-(z x cal) over-dispersion)' % (
            (('%.2f' % drop) if drop is not None else 'n/a'), (100 * dropf) if dropf is not None else 0.0))
        print('      contestation S_contest (cwmean over well (z x mass x cal) cells N>=3) = %s' % _f(md['S_contest']))
        print('      between-calibration offset = %s dex ; between-z offset = %s dex' % (
            ('%.3f' % md['between_cal_offset']) if md['between_cal_offset'] is not None else 'n/a',
            ('%.3f' % md['between_z_offset']) if md['between_z_offset'] is not None else 'n/a'))
        print('      mass-unknown fraction = %s   (honesty metric: values with NO stated stellar mass)' % (
            ('%.2f' % md['mass_unknown_frac']) if md.get('mass_unknown_frac') is not None else 'n/a'))
        print('      mass-bin populations: %s' % (md.get('massbin_N')))
        print('      best-populated (z x mass x cal) cells [genuine same-z same-mass O/H tension]:')
        for lbl, g in sorted(md['cells'].items(), key=lambda kv: -kv[1]['N'])[:12]:
            if g['N'] >= 3:
                print('         %-30s N=%-4d wmean=%7.3f  within-S=%s' % (
                    lbl, g['N'], g['wmean'], ('%.2f' % g['S']) if g['S'] else 'n/a'))

    print('\n== STAGE 4+5: attribute to clusters + v2 rescore ==')
    rows, (tmin, tmax) = attribute_and_rescore(results, disp, fm)
    ga = [r for r in rows if r['tractable'] == 1]
    v1_ga = sorted(ga, key=lambda r: -r['score_v1'])
    v2_ga = sorted(ga, key=lambda r: -r['score_v2'])
    rank_v1 = {r['cluster']: i + 1 for i, r in enumerate(v1_ga)}
    rank_v2 = {r['cluster']: i + 1 for i, r in enumerate(v2_ga)}

    print('\n   TOP-12 GA by score_v2 (dispersion tension):')
    print('   %-4s %-4s %-8s %-8s %-8s %-8s  %s' % ('rk', 'cl', 'score_v2', 'tenV2', 'tenV1', 'rk_v1', 'keywords'))
    for i, r in enumerate(v2_ga[:12]):
        print('   %-4d %-4d %-8.4f %-8.3f %-8.3f %-8d  %s' % (
            i + 1, r['cluster'], r['score_v2'], r['tension_v2_norm'], r['tension_norm_v1'],
            rank_v1[r['cluster']], kw(r)))

    print('\n   ABLATION MOVERS (v1 rank -> v2 rank, GA only):')
    movers = sorted(ga, key=lambda r: (rank_v2[r['cluster']] - rank_v1[r['cluster']]))
    print('   -- RISE under v2 (dispersion says more contested) --')
    for r in movers[:6]:
        d = rank_v1[r['cluster']] - rank_v2[r['cluster']]
        print('   cl %-3d  v1#%-3d -> v2#%-3d  (%+d)  tenV2=%.3f  %s' % (
            r['cluster'], rank_v1[r['cluster']], rank_v2[r['cluster']], d, r['tension_v2_norm'], kw(r)))
    print('   -- FALL under v2 --')
    for r in movers[::-1][:6]:
        d = rank_v1[r['cluster']] - rank_v2[r['cluster']]
        print('   cl %-3d  v1#%-3d -> v2#%-3d  (%+d)  tenV2=%.3f  %s' % (
            r['cluster'], rank_v1[r['cluster']], rank_v2[r['cluster']], d, r['tension_v2_norm'], kw(r)))
    c41 = next((r for r in rows if r['cluster'] == 41), None)
    if c41:
        print('\n   JWST high-z (cl 41): v1#%s -> v2#%s  score_v1=%.4f score_v2=%.4f tenV2=%.3f' % (
            rank_v1.get(41), rank_v2.get(41), c41['score_v1'], c41['score_v2'], c41['tension_v2_norm']))

    # ----------------------------------------------------------------- COVERAGE of top-12 GA
    top12 = v1_ga[:12]                     # the 12 highest-priority GA frontiers (by v1)
    covered = [r for r in top12 if r['tension_v2_raw'] > 0]
    print('\n   COVERAGE of top-12 GA frontiers (by score_v1): %d/12 now have tension_v2>0' % len(covered))
    print('   %-4s %-10s %-9s  %s' % ('cl', 'tenV2_raw', 'drivers', 'keywords'))
    for r in top12:
        drv = ','.join('%s(S%.1f,N%d)' % (qk, c['S'], c['n']) for qk, c in r['v2_contrib'].items())
        print('   %-4d %-10.3f %-9s  %s' % (
            r['cluster'], r['tension_v2_raw'], ('yes' if r['tension_v2_raw'] > 0 else 'NO'),
            (kw(r, 4) + ('  <- ' + drv if drv else '  <- (none)'))))

    # ----------------------------------------------------------------- write outputs
    disp_out = dict(
        version=VERSION,
        generated=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        model=args.model, cap_per_quantity=args.cap_per_quantity, max_total=args.max_total,
        n_measurements=len(results), scanned=ntot,
        z_edges=[list(e) for e in Z_EDGES],
        mass_edges=MASS_EDGES,
        mass_ext_quantities=[q['key'] for q in QUANTITIES if q.get('mass_ext')],
        prefilter_yield=yield_tbl,
        dispersion=disp,
        measurements=results,
        note=('v2.2: S = PDG scale factor sqrt(chi2/(N-1)) computed WITHIN same-epoch (and, for the 6 '
              'mass-dependent quantities, same-MASS) cells. Mass-dependent quantities '
              '(metallicity, quiescent_frac, gas_fraction, dust_atten, size_re, veldisp) were '
              're-extracted with a log_mstar field (cache key suffix "|m"); their primary cell is '
              '(z-bin x mass-bin[ x calibration for metallicity]). mass_edges = [8,9,10,11] -> bins '
              'mlt8/m8-9/m9-10/m10-11/mge11 plus m? (mass-unknown). Per-quantity S fields: '
              'S_all=all pooled (confounded); S_zonly=within z; S_calonly=within calibration; '
              'S_zcal=within (z x cal) [=v2.1 number]; S_massonly=within mass; S_zmass=within (z x mass); '
              'S_zmasscal=within (z x mass x cal) [v2.2 fully de-mixed]; mass_drop=S_zcal-S_zmasscal '
              '(over-dispersion the MZR/mass axis removes); S_contest=citation-weighted mean of per-cell '
              'S over well-populated finest cells (N>=3) -- the genuine same-epoch same-mass disagreement '
              'used to score clusters. "cells" holds per-finest-cell detail; massbin_N/mass_unknown_frac '
              'report mass coverage. Non-mass quantities are unchanged from v2.1 (their cache is reused). '
              'PROTOTYPE: treat S as a RELATIVE controversy amplitude, not an absolute goodness-of-fit; '
              'finer (z x mass) binning thins cells so some quantities lose N>=3 cells (reported).'),
    )
    json.dump(disp_out, open(OUT_DISP, 'w'), indent=1)
    print('\nwrote', OUT_DISP)

    ablation = dict(
        version=VERSION,
        generated=disp_out['generated'],
        tension_v2_minmax=[tmin, tmax],
        top12_ga_coverage=dict(covered=len(covered), total=len(top12),
                               covered_clusters=[r['cluster'] for r in covered]),
        mass_edges=MASS_EDGES,
        quantity_S={d['quantity']: dict(N=d['N'], S_all=d.get('S_all'), S_zonly=d.get('S_zonly'),
                                        S_zcal=d.get('S_zcal'), S_zmass=d.get('S_zmass'),
                                        S_zmasscal=d.get('S_zmasscal'), mass_drop=d.get('mass_drop'),
                                        mass_drop_frac=d.get('mass_drop_frac'),
                                        S_contest=d.get('S_contest'),
                                        mass_unknown_frac=d.get('mass_unknown_frac'),
                                        mass_ext=d.get('mass_ext', False),
                                        n_wellcells=d.get('n_wellcells', 0), verdict=d['verdict'])
                    for d in disp},
        ga_ranking=[dict(
            cluster=r['cluster'], keywords=kw(r), score_v1=round(r['score_v1'], 5),
            score_v2=round(r['score_v2'], 5), rank_v1=rank_v1[r['cluster']], rank_v2=rank_v2[r['cluster']],
            rank_delta=rank_v1[r['cluster']] - rank_v2[r['cluster']],
            tension_v1=round(r['tension_norm_v1'], 4), tension_v2=round(r['tension_v2_norm'], 4),
            tension_v2_raw=round(r['tension_v2_raw'], 4), tension_v2_max=round(r['tension_v2_max'], 4),
            drivers=[dict(q=qk, S=c['S'], N=c['n'], z_cells=c.get('z_cells', 0))
                     for qk, c in r['v2_contrib'].items()],
            v2_contrib=r['v2_contrib']) for r in v2_ga],
    )
    json.dump(ablation, open(OUT_ABLATION, 'w'), indent=2)
    print('wrote', OUT_ABLATION)

    # website payload: top-12 GA by v2.1 score
    v21_ranking = [dict(
        rank=i + 1, cluster=r['cluster'], label_keywords=r['keywords'][:6],
        score_v2=round(r['score_v2'], 5), tension_v2=round(r['tension_v2_norm'], 4),
        drivers=[dict(q=qk, S=c['S'], N=c['n'], z_cells=c.get('z_cells', 0))
                 for qk, c in r['v2_contrib'].items()],
    ) for i, r in enumerate(v2_ga[:12])]
    json.dump(dict(version=VERSION, generated=disp_out['generated'], ranking=v21_ranking),
              open(OUT_V21_RANKING, 'w'), indent=2)
    print('wrote', OUT_V21_RANKING)

    # ----------------------------------------------------------------- v2.2 characteristic-value rescore
    # Score GA tension ONLY on characteristic-value / gas-cycle quantities the field pins to one number.
    # EXCLUDE population-spread quantities whose S is intrinsic range, not disagreement:
    #   stellar_feh, alpha_fe, metal_gradient, tully_fisher, veldisp, size_re, massloss, imf_slope, tde_mbh
    KEEP_CHARVAL = {'sfrd', 'fesc', 'quiescent_frac', 'ms_slope', 'uvlf_alpha', 'smf_mstar',
                    'metallicity', 'gas_fraction', 'dust_atten', 'edd_ratio'}
    cv_rows = []
    for r in ga:
        kept = [dict(q=qk, S=round(c['S'], 3), N=c['n'])
                for qk, c in r['v2_contrib'].items() if qk in KEEP_CHARVAL]
        kept.sort(key=lambda d: -d['S'])
        tclean = max((d['S'] for d in kept), default=0.0)
        kq = {d['q'] for d in kept}
        # provisional: the cluster's contested signal rests SOLELY on metallicity (mass-only-fixable)
        provisional = bool(kept) and kq == {'metallicity'}
        cv_rows.append(dict(cluster=r['cluster'], label_keywords=r['keywords'][:6],
                            sat=r['sat_activity'], grow=r['growth_norm'],
                            tclean=tclean, drivers=kept, provisional_bool=provisional))
    tcmax = max((x['tclean'] for x in cv_rows), default=0.0) or 1.0
    for x in cv_rows:
        tn = x['tclean'] / tcmax
        x['tension'] = round(tn, 4)
        x['score'] = round(x['sat'] * (0.6 * tn + 0.4 * x['grow']), 5)
    cv_rows.sort(key=lambda x: -x['score'])
    v22_ranking = []
    for i, x in enumerate(cv_rows[:12]):
        v22_ranking.append(dict(rank=i + 1, cluster=x['cluster'], label_keywords=x['label_keywords'],
                                score=x['score'], tension=x['tension'],
                                drivers=x['drivers'], provisional_bool=x['provisional_bool']))
    json.dump(v22_ranking, open(OUT_V22_RANKING, 'w'), indent=2)
    print('wrote', OUT_V22_RANKING)

    print('\n   TOP-12 GA (v2.2 characteristic-value-only rescore; population quantities excluded):')
    print('   %-4s %-4s %-9s %-7s %-5s  %s' % ('rk', 'cl', 'score', 'tens', 'prov', 'top drivers / keywords'))
    for x in v22_ranking:
        drv = ' '.join('%s(S%.1f,N%d)' % (d['q'], d['S'], d['N']) for d in x['drivers'][:3])
        print('   %-4d %-4d %-9.5f %-7.3f %-5s  %s' % (
            x['rank'], x['cluster'], x['score'], x['tension'],
            ('PROV' if x['provisional_bool'] else '-'),
            drv + '  | ' + ', '.join(x['label_keywords'][:4])))

if __name__ == '__main__':
    main()
