#!/bin/zsh
cd "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev"
for m in fourier_chirality/test_run_configurations_v16 fourier_chirality/test_run_configurations corpus_identity/test_history_v2 corpus_identity/test_approval_witness_v4 corpus_identity/test_build_corpus_identity_v32 corpus_identity/test_build_corpus_identity beacon_v2/test_beacon_record_drand_v32 drand_only/test_verify_drand_v2 track2/test_track2_fail_first track2/test_provenance_designs; do
  echo "== $m  []"; ( cd "$(dirname $m)" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/_venv_bls/lib/python3.9/site-packages" /usr/bin/python3 -W error::ResourceWarning -m unittest "$(basename $m)" 2>&1 | grep -v RuntimeWarning | grep -E "^Ran|^OK|^FAILED|Error|assert" | cut -c1-300 )
done
echo "== DONE $(date '+%H:%M:%S')"
