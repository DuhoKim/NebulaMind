#!/usr/bin/env python3
import hashlib, json, pathlib, sys

ROOT = pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind')
HANDOFF = ROOT/'.hermes/handoffs/weekend-video-sextet-20260808T0136K'
CANARIES = HANDOFF/'integrator/canaries'
OUT = HANDOFF/'integrator/CORRECTION_ROUND_AUDIT.json'

CASES = {
    'mzr-census': {
        'name': 'mzr-census-method-overhaul-canary-20260809T0320K',
        'sha': 'd6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b',
        'old_name': 'mzr-census-method-overhaul-canary-20260809T0214K',
        'old_sha': '0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536',
        'blockers': ['LANA-MZR-CENSUS-01', 'LANA-MZR-CENSUS-02'],
    },
    'fesc': {
        'name': 'fesc-method-overhaul-canary-20260809T0327K',
        'sha': '47eb0d0b151b51667a4b29a39da74b947086c925dda7ce7e819240ffde25e42d',
        'old_name': 'fesc-method-overhaul-canary-20260809T0227K',
        'old_sha': 'b900383142c0ddeadc32247282f511798d8c4a449cbf5c7b7aef0a56aff4c168',
        'blockers': ['LANA-FESC-01'],
    },
    'brightend': {
        'name': 'brightend-method-overhaul-canary-20260809T0337K',
        'sha': '6e0f4b098d6c5386d08ab7fb670b8b6564e257edeac5dc1c6fec2cc6b97bc7b4',
        'old_name': 'brightend-method-overhaul-canary-20260809T0235K',
        'old_sha': '9a137c61011a3d9629c96ebbf365955295e11082cededa325ceb38f1ce268a2f',
        'blockers': ['LANA-BRIGHTEND-01'],
    },
    'mzr-anchor': {
        'name': 'mzr-anchor-method-overhaul-canary-20260809T0245K',
        'sha': '973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970',
        'old_name': None,
        'old_sha': None,
        'blockers': ['KUN-RENDERER-PRESERVATION-CAVEAT'],
    },
}

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()

def load(path):
    return json.loads(path.read_text())

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def main():
    report = {'status': 'PASS', 'cases': {}, 'global_checks': {}}
    final_hashes = set()
    for lane, cfg in CASES.items():
        candidate = CANARIES/cfg['name']
        video = candidate/(cfg['name']+'.mp4')
        build = load(candidate/'build_receipt.json')
        qa = load(candidate/'encoded_qa.json')
        actual_sha = sha(video)
        require(actual_sha == cfg['sha'] == build['output_sha256'] == qa['video_sha256'], f'{lane}: candidate hash mismatch')
        require(qa['status'] == 'PASS' and all(qa['checks'].values()), f'{lane}: encoded QA not complete PASS')
        require(105 <= qa['timeline_summary']['delivered_wpm'] <= 125, f'{lane}: WPM out of range')
        require(build['video_reportable_now'] is False, f'{lane}: report gate opened')
        require(build['source_grounded_runtime_percent'] > 99.7, f'{lane}: source grounding below floor')
        require(not list(candidate.rglob('SOURCE_FREEZE.json')), f'{lane}: unauthorized source freeze present')
        if lane != 'mzr-anchor':
            correction = load(candidate/'CORRECTION.json')
            require(correction['video_reportable_now'] is False and correction['method_only'] is True, f'{lane}: correction gates invalid')
            require(set(correction['blockers_addressed']) == set(cfg['blockers']), f'{lane}: blocker coverage mismatch')
            renderer = candidate/build['renderer_path']
            require(sha(renderer) == build['renderer_sha256'], f'{lane}: renderer snapshot mismatch')
            require(sha(candidate/build['render_environment_path']) == build['render_environment_sha256'], f'{lane}: environment snapshot mismatch')
            require((candidate/'provenance/synthesize.py').is_file(), f'{lane}: synthesizer snapshot absent')
            require((candidate/'provenance/assemble.py').is_file(), f'{lane}: assembler snapshot absent')
            require((candidate/'provenance/qa.py').is_file(), f'{lane}: QA snapshot absent')
            require((candidate/'provenance_manifest.json').is_file(), f'{lane}: provenance manifest absent')
            old = CANARIES/cfg['old_name']/(cfg['old_name']+'.mp4')
            require(sha(old) == cfg['old_sha'], f'{lane}: reviewed predecessor drift')
        else:
            archive = HANDOFF/'integrator/renderer-archive/7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53/render.py'
            manifest = load(archive.with_name('ARCHIVE.json'))
            require(sha(archive) == build['renderer_sha256'] == manifest['renderer_sha256'], 'mzr-anchor: archived renderer mismatch')
            require(manifest['candidate_sha256'] == actual_sha and manifest['candidate_mutated'] is False, 'mzr-anchor: archive binding invalid')
        final_hashes.add(actual_sha)
        report['cases'][lane] = {
            'candidate': cfg['name'],
            'sha256': actual_sha,
            'encoded_checks': f"{sum(qa['checks'].values())}/{len(qa['checks'])}",
            'duration_seconds': float(qa['probe']['format']['duration']),
            'delivered_wpm': qa['timeline_summary']['delivered_wpm'],
            'introduction_similarity': qa['introduction_transcription']['similarity'],
            'source_grounded_runtime_percent': build['source_grounded_runtime_percent'],
            'renderer_sha256': build['renderer_sha256'],
            'blockers_addressed': cfg['blockers'],
            'video_reportable_now': False,
        }
    rejected_fesc = CANARIES/'fesc-method-overhaul-canary-20260809T0327K/rejected-attempts/b5013cd3-loudness-hold/fesc-method-overhaul-canary-20260809T0327K.mp4'
    require(sha(rejected_fesc) == 'b5013cd341cab940188db82df0ae57d64f9ec08c0f786a90d6b782bb75599af1', 'FESC rejected loudness attempt missing')
    mzr_hold = CANARIES/'mzr-census-method-overhaul-canary-20260809T0320K/rejected-attempts/qa-loudness-threshold-hold/encoded_qa.HOLD1.json'
    require(mzr_hold.is_file(), 'MZR QA hold not preserved')
    template = CANARIES/'spin-method-overhaul-canary-20260808T1959K/spin-method-overhaul-canary-20260808T1959K.mp4'
    require(sha(template) == 'c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240', 'accepted v3 drift')
    public = ROOT/'frontend/public/videos'
    public_hashes = {sha(p) for p in public.glob('*.mp4')}
    require(not (final_hashes & public_hashes), 'a correction candidate is present in the public video root')
    report['global_checks'] = {
        'all_exact_hashes_bound': True,
        'all_encoded_checks_pass': True,
        'all_method_only': True,
        'all_video_reportable_now_false': True,
        'all_new_candidate_tool_snapshots_preserved': True,
        'mzr_anchor_exact_renderer_archived': True,
        'reviewed_predecessors_preserved': True,
        'rejected_correction_attempts_preserved': True,
        'accepted_v3_hash_unchanged': True,
        'no_correction_hash_in_public_video_root': True,
    }
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'audit': str(OUT), 'audit_sha256': sha(OUT), 'candidate_hashes': sorted(final_hashes)}, indent=2))

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        if OUT.exists(): OUT.unlink()
        print(f'CORRECTION AUDIT HOLD: {exc}', file=sys.stderr)
        raise
