#!/usr/bin/env python
"""
rank_frontiers_v3.py  --  Frontier-ranking score v1 for the NebulaMind galaxy-evolution pipeline.

WHAT THIS DOES (reproducible; all real data, no LLM)
----------------------------------------------------
The current/v2 frontier score (`frontier_score_cite`) is purely citation-graph derived:
    frontier_score_cite = 0.6*recent(2023+) cites-per-paper  +  0.4*recent-paper growth.
It rewards crowded, well-cited-but-settled measurement programs (Gaia/APOGEE abundances,
SMBH scaling relations, disk kinematics, RR Lyrae ...) just as much as genuinely contested
frontiers. v1 fixes that by folding in (a) a *strict tension rate* mined from the corpus,
(b) a *scope veto* (in-scope galaxy-evolution vs out-of-scope cosmology), and (c) a saturating
activity FLOOR so a topic must have some real recent citation activity to score at all.

    a_half        = median(activity) over the 57 clusters              (activity = recent_cites_per_paper)
    sat(a)        = a / (a + a_half)                                    # saturating activity floor in [0,1)
    tension_norm  = minmax(strict_tension) over the 57 clusters        # [0,1]
    growth_norm   = minmax(recent_frac)    over the 57 clusters        # [0,1]
    tractable     = 1 if GA-dominant (ga_frac >= co_frac) else 0       # scope veto
    score_v1      = sat(activity) * tractable * (0.6*tension_norm + 0.4*growth_norm)

STRICT TENSION (mined from corpus title+abstract, word-boundary, case-insensitive)
    lexicon: tension / discrepan / contradict / inconsisten / "cannot explain" /
             "fail to reproduce" / overpredict / underpredict
    STRING-TENSION FIX: the token "tension" is a *physics quantity* (not a disagreement)
    when preceded by string / strings / brane / branes / surface / domain-wall.
    Those "<quantity> tension" phrases are stripped BEFORE counting so cosmic-string
    clusters (e.g. cluster 30) are not falsely flagged as contested.

SCOPE (GA vs CO) from the corpus `keyword` field
    GA-dominant  = fraction of members whose keyword list contains
                   "Astrophysics of Galaxies"  >=  fraction containing
                   "Cosmology and Nongalactic Astrophysics".
    GA-dominant => in scope & broadly tractable with SDSS/JWST/TNG/COSMOS (tractable=1).
    CO-dominant => out of scope => vetoed (tractable=0 => score_v1=0).

OUTPUTS
    frontier_map_v3.json  (corpus dir) : v2 structure + per-cluster
                                         strict_tension, ga_frac, co_frac, tractable,
                                         score_v1 ; clusters re-sorted by score_v1.
    v1_ga_ranking.json    (job tmp)    : top-12 GA clusters for the website.
Does NOT modify any v2 file or the corpus jsonl.
"""
import json, re, math, collections, os

ROOT = '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718/'
CORPUS = ROOT + 'corpus_ga_co_2009_2026.jsonl'
LABELS = ROOT + 'cluster_labels_v2.json'
V2 = ROOT + 'frontier_map_v2.json'
TMP = '/Users/duhokim/.claude/jobs/a2199266/tmp/'

# ----------------------------------------------------------------------------- lexicon / regex
STRICT_TERMS = ["tension", "discrepan", "contradict", "inconsisten",
                "cannot explain", "fail to reproduce", "overpredict", "underpredict"]
strict_re = {t: re.compile(r'(?<![a-z])' + re.escape(t), re.IGNORECASE) for t in STRICT_TERMS}
# physics "<quantity> tension" that must NOT count as disagreement
PHYS_TENSION = re.compile(
    r'(?<![a-z])(?:strings?|branes?|surface|domain[-\s]?walls?)\s+tension', re.IGNORECASE)

GA_KEY = "astrophysics of galaxies"
CO_KEY = "cosmology and nongalactic astrophysics"

# ----------------------------------------------------------------------------- load inputs
labels = json.load(open(LABELS))                       # bibcode -> cluster int (-1 = noise)
fm = json.load(open(V2))
cluster_info = {c['cluster']: c for c in fm['clusters']}
CLUSTERS = sorted(cluster_info.keys())                 # the 57

agg = {cl: {'n': 0, 'strict_hit': 0, 'tension_fire': 0, 'tension_phys_only': 0,
            'ga': 0, 'co': 0} for cl in CLUSTERS}

# ----------------------------------------------------------------------------- stream corpus once
n = 0
with open(CORPUS) as f:
    for line in f:
        n += 1
        r = json.loads(line)
        cl = labels.get(r['bibcode'])
        if cl is None or cl == -1 or cl not in agg:
            continue
        a = agg[cl]
        a['n'] += 1

        # ---- scope (keyword field) ----
        kws = r.get('keyword') or []
        low = ' || '.join(k.lower() for k in kws) if isinstance(kws, list) else str(kws).lower()
        if GA_KEY in low:
            a['ga'] += 1
        if CO_KEY in low:
            a['co'] += 1

        # ---- strict tension (title + abstract) ----
        title = r.get('title') or []
        if isinstance(title, list):
            title = ' '.join(title)
        text = title + ' ' + (r.get('abstract') or '')
        # STRING-TENSION FIX: strip physics "<quantity> tension" before counting tension
        cleaned = PHYS_TENSION.sub(' ', text)

        fired = False
        for t in STRICT_TERMS:
            hay = cleaned if t == "tension" else text
            if strict_re[t].search(hay):
                fired = True
                break
        if fired:
            a['strict_hit'] += 1
        # diagnostics for the cl-30 fix check
        if strict_re['tension'].search(text):
            a['tension_fire'] += 1
            if not strict_re['tension'].search(cleaned):
                a['tension_phys_only'] += 1

print('processed %d corpus lines' % n)

# ----------------------------------------------------------------------------- per-cluster metrics
rows = []
for cl in CLUSTERS:
    a = agg[cl]
    ci = cluster_info[cl]
    nn = a['n'] or 1
    rows.append({
        'cluster': cl,
        'size': ci.get('size'),
        'keywords': ci.get('keywords', []),
        'activity': ci.get('recent_cites_per_paper') or 0.0,
        'recent_frac': ci.get('recent_frac') or 0.0,
        'frontier_score_cite': ci.get('frontier_score_cite') or 0.0,
        'n_members': a['n'],
        'strict_tension': a['strict_hit'] / nn,
        'ga_frac': a['ga'] / nn,
        'co_frac': a['co'] / nn,
        'tension_fire_raw': a['tension_fire'],
        'tension_phys_only': a['tension_phys_only'],
    })

# ----------------------------------------------------------------------------- v1 score
def median(xs):
    s = sorted(xs); m = len(s)
    return s[m // 2] if m % 2 else 0.5 * (s[m // 2 - 1] + s[m // 2])

activities = [r['activity'] for r in rows]
tensions   = [r['strict_tension'] for r in rows]
growths    = [r['recent_frac'] for r in rows]

a_half = median(activities)
t_min, t_max = min(tensions), max(tensions)
g_min, g_max = min(growths), max(growths)

def minmax(x, lo, hi):
    return (x - lo) / (hi - lo) if hi > lo else 0.0

for r in rows:
    r['sat_activity'] = r['activity'] / (r['activity'] + a_half) if (r['activity'] + a_half) else 0.0
    r['tension_norm'] = minmax(r['strict_tension'], t_min, t_max)
    r['growth_norm']  = minmax(r['recent_frac'], g_min, g_max)
    r['tractable']    = 1 if r['ga_frac'] >= r['co_frac'] else 0
    r['score_v1'] = r['sat_activity'] * r['tractable'] * (0.6 * r['tension_norm'] + 0.4 * r['growth_norm'])

# ----------------------------------------------------------------------------- rankings (GA only)
def kw(r, k=5):
    return ', '.join(r['keywords'][:k])

ga_rows = [r for r in rows if r['tractable'] == 1]
v2_ga = sorted(ga_rows, key=lambda r: -r['frontier_score_cite'])
v1_ga = sorted(ga_rows, key=lambda r: -r['score_v1'])
rank_v2 = {r['cluster']: i + 1 for i, r in enumerate(v2_ga)}
rank_v1 = {r['cluster']: i + 1 for i, r in enumerate(v1_ga)}

if __name__ == '__main__':
    print("\n=== normalization constants ===")
    print("a_half (median activity, recent_cites_per_paper) = %.4f" % a_half)
    print("tension minmax: min=%.4f  max=%.4f" % (t_min, t_max))
    print("growth  minmax: min=%.4f  max=%.4f" % (g_min, g_max))
    print("GA-dominant clusters: %d / %d" % (len(ga_rows), len(rows)))

    print("\n=== TABLE A: CURRENT v2 ranking (GA-dominant only, top 15) ===")
    print("%-4s %-4s %-9s %-8s %-7s  %s" % ("rk", "cl", "v2score", "activity", "tension", "keywords"))
    for i, r in enumerate(v2_ga[:15]):
        print("%-4d %-4d %-9.3f %-8.2f %-7.3f  %s" % (
            i + 1, r['cluster'], r['frontier_score_cite'], r['activity'], r['strict_tension'], kw(r)))

    print("\n=== TABLE B: v1 ranking (GA-dominant only, top 15) ===")
    print("%-4s %-4s %-8s %-7s %-7s %-7s  %s" % ("rk", "cl", "score_v1", "sat(a)", "tenN", "grwN", "keywords"))
    for i, r in enumerate(v1_ga[:15]):
        print("%-4d %-4d %-8.4f %-7.3f %-7.3f %-7.3f  %s" % (
            i + 1, r['cluster'], r['score_v1'], r['sat_activity'], r['tension_norm'], r['growth_norm'], kw(r)))

    print("\n=== TABLE C: MOVERS (GA clusters, v2 rank vs v1 rank) ===")
    movers = sorted(ga_rows, key=lambda r: (rank_v1[r['cluster']] - rank_v2[r['cluster']]))
    print("-- RISE most (contested / previously buried) --")
    print("%-4s %-7s %-7s %-6s %-7s %-8s  %s" % ("cl", "rk_v2", "rk_v1", "delta", "tension", "activity", "keywords"))
    for r in movers[:8]:
        d = rank_v1[r['cluster']] - rank_v2[r['cluster']]
        print("%-4d %-7d %-7d %+-6d %-7.3f %-8.2f  %s" % (
            r['cluster'], rank_v2[r['cluster']], rank_v1[r['cluster']], d, r['strict_tension'], r['activity'], kw(r)))
    print("-- FALL most (settled measurement programs) --")
    print("%-4s %-7s %-7s %-6s %-7s %-8s  %s" % ("cl", "rk_v2", "rk_v1", "delta", "tension", "activity", "keywords"))
    for r in movers[::-1][:8]:
        d = rank_v1[r['cluster']] - rank_v2[r['cluster']]
        print("%-4d %-7d %-7d %+-6d %-7.3f %-8.2f  %s" % (
            r['cluster'], rank_v2[r['cluster']], rank_v1[r['cluster']], d, r['strict_tension'], r['activity'], kw(r)))

    print("\n=== TABLE D: SANITY CHECKS ===")
    c41 = next((r for r in rows if r['cluster'] == 41), None)
    if c41:
        print("JWST high-z (cl 41): v1 rank among GA = %s ; v2 rank = %s ; score_v1=%.4f tension=%.3f" % (
            rank_v1.get(41), rank_v2.get(41), c41['score_v1'], c41['strict_tension']))
    print("Fringe/CO veto check (must be tractable=0, absent from GA ranking):")
    for cid, name in [(6, "MOND"), (34, "interacting DE"), (30, "cosmic strings"), (33, "Hubble/dark-energy")]:
        r = next((x for x in rows if x['cluster'] == cid), None)
        if r:
            print("  cl %-3d %-18s tractable=%d ga_frac=%.3f co_frac=%.3f  in_GA_rank=%s | %s" % (
                cid, name, r['tractable'], r['ga_frac'], r['co_frac'], cid in rank_v1, kw(r)))
    c30 = next((r for r in rows if r['cluster'] == 30), None)
    if c30:
        print("String-tension FIX (cl 30 cosmic strings):")
        print("  raw tension-firing papers=%d ; physics-only (stripped)=%d ; strict_tension AFTER fix=%.3f" % (
            c30['tension_fire_raw'], c30['tension_phys_only'], c30['strict_tension']))

    # ------------------------------------------------------------------- write frontier_map_v3.json
    out = {
        'n_clusters': fm['n_clusters'], 'n_papers': fm['n_papers'], 'noise': fm.get('noise'),
        'note': ('score_v1 = sat(activity) * tractable(GA-dominant) * (0.6*tension_norm + 0.4*growth_norm). '
                 'a_half=%.4f (median activity); tension minmax [%.4f,%.4f]; growth minmax [%.4f,%.4f]. '
                 'strict_tension mined from title+abstract with string-tension fix. '
                 'tractable=1 iff ga_frac>=co_frac (CO-dominant vetoed).' % (
                     a_half, t_min, t_max, g_min, g_max)),
        'v1_constants': {'a_half': a_half, 'tension_min': t_min, 'tension_max': t_max,
                         'growth_min': g_min, 'growth_max': g_max},
        'clusters': [],
    }
    by_cl = {r['cluster']: r for r in rows}
    for ci in fm['clusters']:
        r = by_cl[ci['cluster']]
        c = dict(ci)
        c['strict_tension'] = round(r['strict_tension'], 5)
        c['ga_frac'] = round(r['ga_frac'], 5)
        c['co_frac'] = round(r['co_frac'], 5)
        c['tractable'] = r['tractable']
        c['sat_activity'] = round(r['sat_activity'], 5)
        c['tension_norm'] = round(r['tension_norm'], 5)
        c['growth_norm'] = round(r['growth_norm'], 5)
        c['score_v1'] = round(r['score_v1'], 5)
        out['clusters'].append(c)
    out['clusters'].sort(key=lambda c: -c['score_v1'])
    json.dump(out, open(ROOT + 'frontier_map_v3.json', 'w'), indent=2)
    print("\nwrote", ROOT + 'frontier_map_v3.json')

    # ------------------------------------------------------------------- write website top-12
    top12 = []
    for r in v1_ga[:12]:
        top12.append({
            'label_keywords': kw(r, 6),
            'cluster': r['cluster'],
            'score_v1': round(r['score_v1'], 5),
            'activity': round(r['activity'], 3),
            'growth': round(r['recent_frac'], 4),
            'tension': round(r['strict_tension'], 4),
            'rank_v2': rank_v2[r['cluster']],
            'rank_v1': rank_v1[r['cluster']],
        })
    json.dump(top12, open(TMP + 'v1_ga_ranking.json', 'w'), indent=2)
    print("wrote", TMP + 'v1_ga_ranking.json')
