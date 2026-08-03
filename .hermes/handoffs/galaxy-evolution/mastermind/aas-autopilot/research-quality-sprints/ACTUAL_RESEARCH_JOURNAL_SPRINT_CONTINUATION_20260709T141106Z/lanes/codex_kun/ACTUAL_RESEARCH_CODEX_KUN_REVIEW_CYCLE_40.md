# codex-kun-readonly-cycle-40
Started UTC: 2026-07-09T19:19:10Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['codex', 'exec', '-m', 'gpt-5.4-mini', '--sandbox', 'read-only', '--cd', '/Users/duhokim/NebulaMind/NebulaMind']

Reading additional input from stdin...
OpenAI Codex v0.143.0
--------
workdir: /Users/duhokim/NebulaMind/NebulaMind
model: gpt-5.4-mini
provider: openai
approval: never
sandbox: read-only
reasoning effort: none
reasoning summaries: none
session id: 019f4851-d681-7933-982c-6bcc61f0b9af
--------
user
Review this local manuscript package in read-only mode.

Output marker: ACTUAL_RESEARCH_CODEX_KUN_REVIEW_CYCLE_40

You are Kun/Codex: reproducibility, TeX, provenance, and no-mock-data audit.

Read only these roots unless needed for harmless metadata checks:
- candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package
- real-data inventory: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/real-data-inventory/REAL_DATA_INVENTORY_CYCLE_40.json
- integrated context: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z
- original real-data runs: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs

Tasks:
- inspect TeX/prose for compile risks and journal-paper weaknesses
- verify that numeric claims remain traceable to real local files or cited public sources
- check core invariants: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage
- scan for forbidden use of mock/synthetic/fake/placeholder/toy data
- recommend safe candidate-only edits for the integrator

Forbidden: file edits, public/live edits, DB/API/wiki/trust/deploy/git/cron/billing/OAuth/account changes, external submission, credential reads.

codex
I’m checking the package structure first, then I’ll trace the stated invariants back to local sources and look for TeX compile risks and any synthetic-data wording. After that I’ll summarize only candidate-safe edits and provenance gaps.
exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/real-data-inventory/REAL_DATA_INVENTORY_CYCLE_40.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "counts": {
    "csv_files": 35,
    "integrated_tex_files": 9,
    "json_files": 167,
    "pdf_files": 43
  },
  "created_utc": "2026-07-09T19:19:10Z",
  "csv_files": [
    {
      "bytes": 20342898,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
      "rows": 60000,
      "sha256": "6f982fa5778c3900239149b28729f701390fe393a164b95236229adc1e422883"
    },
    {
      "bytes": 1109824,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv",
      "rows": 8146,
      "sha256": "4ea53af867cccccb2b68b81557ff84fe90ec3f13e0512ffbdc977fa7216996fd"
    },
    {
      "bytes": 10621597,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv",
      "rows": 60000,
      "sha256": "5b880ee86d9c5c33e49e94336eae8c7c5a5f6183a08749ece56ce795d39c0bb1"
    },
    {
      "bytes": 91674,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/alternate_mass_redshift_sn_target_vector_20260708T183643Z.csv",
      "rows": 198,
      "sha256": "0eed2b78a83e3edd4c59b3713c1ed2c8dd0b4f5ceae4f8a4b8c3c6a64c8b57f5"
    },
    {
      "bytes": 7426,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bootstrap_summary_key_metrics_20260708T162615Z.csv",
      "rows": 24,
      "sha256": "fac8b2c443917c37eb03ae12c7753ee9ee08719b200ad034db9441822759574f"
    },
    {
      "bytes": 700,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bpt_boundary_margin_counts_20260708T162615Z.csv",
      "rows": 3,
      "sha256": "19b3f1acc707e94af24b87b42b01fac163a5c2c58c1bf389d3a0962baef04fe4"
    },
    {
      "bytes": 6911,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bpt_class_sensitivity_matched_offsets_20260708T162615Z.csv",
      "rows": 15,
      "sha256": "029b015f5907f308f62a64b76f868b5b7140c3204bcb2081c53a626d2a305b67"
    },
    {
      "bytes": 3260,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bpt_demarcation_crosswalk_20260708T162615Z.csv",
      "rows": 12,
      "sha256": "1171f7348a0b0865ebd8415e2589feadfa665ad04c337224d01fe131a2986812"
    },
    {
      "bytes": 2228,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bpt_flux_error_mc_matched_pair_sensitivity_20260708T232006Z.csv",
      "rows": 4,
      "sha256": "3ea9fe8e6f918467bc28530de5da811f193b05d97407f7b723ef6221fa6079f8"
    },
    {
      "bytes": 2083,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bpt_flux_error_mc_paper_metrics_20260708T232006Z.csv",
      "rows": 6,
      "sha256": "232dd384664492fdabb5d4b5869ee1364989b4bd33c4068cdcd6aea9d807c9ac"
    },
    {
      "bytes": 2932,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bpt_flux_error_mc_sn_summary_20260708T232006Z.csv",
      "rows": 28,
      "sha256": "e7df8f1ec52b527858689475da1045ab811b460f9bf0037cf2a23f830b02bd20"
    },
    {
      "bytes": 4514,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bpt_flux_error_mc_stability_by_sn_20260708T232006Z.csv",
      "rows": 24,
      "sha256": "20b6df1667ee136d0c29a48006544e00183fba26d39c9e3bbc92e5346d0cadb7"
    },
    {
      "bytes": 1465,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bpt_flux_error_mc_transition_20260708T232006Z.csv",
      "rows": 16,
      "sha256": "fccb7c0423cfdc822d46c7d2bb13e6d47f18b9f376bd9fe56e63b5506bb59c9f"
    },
    {
      "bytes": 3760,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/bpt_sensitivity_20260708T141459Z.csv",
      "rows": 33,
      "sha256": "01cb39253c5105affca3ff7f739b2f8fd03eee1048c4222ff44896db1a752d1e"
    },
    {
      "bytes": 2390,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/control_reuse_distribution_20260708T205859Z.csv",
      "rows": 6,
      "sha256": "9cf5a897e1d2a7393672960e93ebce7546b262e21fd7e42a9151308e9ce552e9"
    },
    {
      "bytes": 34980,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/figure_table_inventory_20260708T141459Z.csv",
      "rows": 86,
      "sha256": "3becba4e88dd9d4532ec90e4d56c8383fa1929a7cc9d8d049dc83042865c22d9"
    },
    {
      "bytes": 56727,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/figure_table_inventory_deep_20260708T162615Z.csv",
      "rows": 230,
      "sha256": "a48caf78111fb47860da0b29c688d834c5b089ab13e2b7799fb27e6f8efcbe42"
    },
    {
      "bytes": 2832,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/goru_bpt_flux_error_mc_inventory_20260708T232006Z.csv",
      "rows": 10,
      "sha256": "80fbbe87f89b148cf2786e0230dac35bae71274cd4c5ad76a63fb74bac22ed21"
    },
    {
      "bytes": 3296,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/goru_matching_control_inventory_20260708T205859Z.csv",
      "rows": 9,
      "sha256": "160dc56775082fe97b3e84dca4f2cc9381c51740b93a16406fb94fec3a5d8f21"
    },
    {
      "bytes": 2962,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/goru_tick_output_inventory_20260708T183643Z.csv",
      "rows": 8,
      "sha256": "dbf07e70f910a71764e50790f0c2ae898620c31a577bd1e496c7d722c5c6f268"
    },
    {
      "bytes": 27203,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/high_excitation_denominators_20260708T162615Z.csv",
      "rows": 135,
      "sha256": "214c5400c99ce2d9153c51064573f6a654aacb48f47269e1633996725be11487"
    },
    {
      "bytes": 58732,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/matched_control_by_strata_20260708T162615Z.csv",
      "rows": 144,
      "sha256": "fdc59b3cc8dd92fc25f2c5a7c2e647ea679943dae00279fbc6de85848f735309"
    },
    {
      "bytes": 71390,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/matched_control_caliper_sensitivity_20260708T205859Z.csv",
      "rows": 90,
      "sha256": "8d939a4d8034d19d6d2a6d706027367011659b51aaa7a24dc23bd6cc27aa1bde"
    },
    {
      "bytes": 4246,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/matched_sfr_offset_robustness_20260708T141459Z.csv",
      "rows": 13,
      "sha256": "ef3270abd664ede81d40bb85eb1a570b2953ba84c177e85ecb3cc797d1486d8f"
    },
    {
      "bytes": 4906,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/paper_ready_matching_rows_20260708T205859Z.csv",
      "rows": 9,
      "sha256": "ca379cfe5d01bd24849ca9d83f89f762c4deaae4a62de1a2e4feb04de4da3da0"
    },
    {
      "bytes": 17362,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/paper_table_candidate_rows_20260708T183643Z.csv",
      "rows": 35,
      "sha256": "680695bcfb8722fdaacf2e4cfaca97853ab0d837b1ab9d3bea76645f3a06f538"
    },
    {
      "bytes": 38758,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/regression_lpm_sensitivity_20260708T183643Z.csv",
      "rows": 63,
      "sha256": "31cee9dcc519921638919ded76db74fc57122e7d19bae28969e07123bef8a940"
    },
    {
      "bytes": 673,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/sample_counts_by_cut_20260708T141459Z.csv",
      "rows": 3,
      "sha256": "06854c5f2ad9eca063e5fac08df69d9c5948e7bff91c2e0db8da4dd6f9cf82ae"
    },
    {
      "bytes": 4732,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/sdss_bptclass_numeric_crosscheck_20260708T162615Z.csv",
      "rows": 30,
      "sha256": "dd770500bb4633a3023e1c20ab391788a4c3e9bf234e9539e4915b77558c822d"
    },
    {
      "bytes": 6978,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/selection_caution_overlay_20260708T162615Z.csv",
      "rows": 15,
      "sha256": "281924fdb4982b3c7793e7aff88295448e8b3aac30ba13831dac9486e4a244ea"
    },
    {
      "bytes": 4058,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/simulation_target_vector_cells_20260708T141459Z.csv",
      "rows": 15,
      "sha256": "6bf59bb6026d11ec14f1f6f2c56b329a43b9db055e681778a9badecc0fc960d5"
    },
    {
      "bytes": 9872,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/sn_redshift_mass_bins_20260708T141459Z.csv",
      "rows": 45,
      "sha256": "84ce5d1bd9c6b17916e124b9b91098bc5b030f0609a0e766537459087aa8fe71"
    },
    {
      "bytes": 20242,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/stratified_agn_fraction_by_mass_z_sn_20260708T162615Z.csv",
      "rows": 45,
      "sha256": "192eb57a4ec7c4cd742383e393610c657a72d0791dcf3e53b31dbeda3c6a57a6"
    },
    {
      "bytes": 40902,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/topic_bootstrap_summary_20260708T183643Z.csv",
      "rows": 84,
      "sha256": "b3b90e81d29b827ad3b45d01f57c7cb37593e12e5f7b3ce3c41658d16897cc9f"
    },
    {
      "bytes": 23934,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/tables/topic_metric_robustness_20260708T141459Z.csv",
      "rows": 89,
      "sha256": "5ab10fd4a6e09defd3f58f5a1c874ea8ab437f4ea08d7341af739dd3a1a51cda"
    }
  ],
  "cycle": 40,
  "integrated_root": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z",
  "integrated_tex_summaries": [
    {
      "abstract": "We integrate the strongest Galaxy Evolution pilot into a selection-aware short-paper draft: a matched-control comparison of catalog specific star formation in broad BPT optical AGN hosts and star-forming controls in SDSS DR17. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a flagship short-paper draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "bytes": 9666,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
      "sha256": "69409b90a0479f23a84991da03dc514daec083c93145505a4b4d2dd8ca58e51b",
      "title": "Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot"
    },
    {
      "abstract": "We integrate the active proposal 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "bytes": 9257,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
      "sha256": "6f879108b0889194069d7f56cfa194433db87cb751ec50a51e758652f06c2de2",
      "title": "SDSS density proxy for environmental quenching: selection-aware SDSS optical proxy integration"
    },
    {
      "abstract": "We integrate the active proposal 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "bytes": 9253,

exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package | sed 's#"'^/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/##'"' | sort" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
CYCLE_01_ACTUAL_RESEARCH_AUDIT.json
CYCLE_01_ACTUAL_RESEARCH_AUDIT.md
CYCLE_01_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_01_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_01_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_01_QUALITY_AUDIT.json
CYCLE_01_QUALITY_AUDIT.md
CYCLE_01_REVIEW_RESPONSE.md
CYCLE_01_SUMMARY.json
CYCLE_01_SUMMARY.md
CYCLE_02_ACTUAL_RESEARCH_AUDIT.json
CYCLE_02_ACTUAL_RESEARCH_AUDIT.md
CYCLE_02_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_02_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_02_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_02_QUALITY_AUDIT.json
CYCLE_02_QUALITY_AUDIT.md
CYCLE_02_REVIEW_RESPONSE.md
CYCLE_02_SUMMARY.json
CYCLE_02_SUMMARY.md
CYCLE_03_ACTUAL_RESEARCH_AUDIT.json
CYCLE_03_ACTUAL_RESEARCH_AUDIT.md
CYCLE_03_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_03_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_03_QUALITY_AUDIT.json
CYCLE_03_QUALITY_AUDIT.md
CYCLE_03_REVIEW_RESPONSE.md
CYCLE_03_SUMMARY.json
CYCLE_03_SUMMARY.md
CYCLE_04_ACTUAL_RESEARCH_AUDIT.json
CYCLE_04_ACTUAL_RESEARCH_AUDIT.md
CYCLE_04_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_04_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_04_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_04_QUALITY_AUDIT.json
CYCLE_04_QUALITY_AUDIT.md
CYCLE_04_REVIEW_RESPONSE.md
CYCLE_04_SUMMARY.json
CYCLE_04_SUMMARY.md
CYCLE_05_ACTUAL_RESEARCH_AUDIT.json
CYCLE_05_ACTUAL_RESEARCH_AUDIT.md
CYCLE_05_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_05_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_05_QUALITY_AUDIT.json
CYCLE_05_QUALITY_AUDIT.md
CYCLE_05_REVIEW_RESPONSE.md
CYCLE_05_SUMMARY.json
CYCLE_05_SUMMARY.md
CYCLE_06_ACTUAL_RESEARCH_AUDIT.json
CYCLE_06_ACTUAL_RESEARCH_AUDIT.md
CYCLE_06_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_06_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_06_QUALITY_AUDIT.json
CYCLE_06_QUALITY_AUDIT.md
CYCLE_06_REVIEW_RESPONSE.md
CYCLE_06_SUMMARY.json
CYCLE_06_SUMMARY.md
CYCLE_07_ACTUAL_RESEARCH_AUDIT.json
CYCLE_07_ACTUAL_RESEARCH_AUDIT.md
CYCLE_07_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_07_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_07_QUALITY_AUDIT.json
CYCLE_07_QUALITY_AUDIT.md
CYCLE_07_REVIEW_RESPONSE.md
CYCLE_07_SUMMARY.json
CYCLE_07_SUMMARY.md
CYCLE_08_ACTUAL_RESEARCH_AUDIT.json
CYCLE_08_ACTUAL_RESEARCH_AUDIT.md
CYCLE_08_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_08_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_08_QUALITY_AUDIT.json
CYCLE_08_QUALITY_AUDIT.md
CYCLE_08_REVIEW_RESPONSE.md
CYCLE_08_SUMMARY.json
CYCLE_08_SUMMARY.md
CYCLE_09_ACTUAL_RESEARCH_AUDIT.json
CYCLE_09_ACTUAL_RESEARCH_AUDIT.md
CYCLE_09_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_09_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_09_QUALITY_AUDIT.json
CYCLE_09_QUALITY_AUDIT.md
CYCLE_09_REVIEW_RESPONSE.md
CYCLE_09_SUMMARY.json
CYCLE_09_SUMMARY.md
CYCLE_10_ACTUAL_RESEARCH_AUDIT.json
CYCLE_10_ACTUAL_RESEARCH_AUDIT.md
CYCLE_10_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_10_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_10_QUALITY_AUDIT.json
CYCLE_10_QUALITY_AUDIT.md
CYCLE_10_REVIEW_RESPONSE.md
CYCLE_10_SUMMARY.json
CYCLE_10_SUMMARY.md
CYCLE_11_ACTUAL_RESEARCH_AUDIT.json
CYCLE_11_ACTUAL_RESEARCH_AUDIT.md
CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_11_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_11_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_11_QUALITY_AUDIT.json
CYCLE_11_QUALITY_AUDIT.md
CYCLE_11_REVIEW_RESPONSE.md
CYCLE_11_SUMMARY.json
CYCLE_11_SUMMARY.md
CYCLE_12_ACTUAL_RESEARCH_AUDIT.json
CYCLE_12_ACTUAL_RESEARCH_AUDIT.md
CYCLE_12_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_12_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_12_QUALITY_AUDIT.json
CYCLE_12_QUALITY_AUDIT.md
CYCLE_12_REVIEW_RESPONSE.md
CYCLE_12_SUMMARY.json
CYCLE_12_SUMMARY.md
CYCLE_13_ACTUAL_RESEARCH_AUDIT.json
CYCLE_13_ACTUAL_RESEARCH_AUDIT.md
CYCLE_13_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_13_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_13_QUALITY_AUDIT.json
CYCLE_13_QUALITY_AUDIT.md
CYCLE_13_REVIEW_RESPONSE.md
CYCLE_13_SUMMARY.json
CYCLE_13_SUMMARY.md
CYCLE_14_ACTUAL_RESEARCH_AUDIT.json
CYCLE_14_ACTUAL_RESEARCH_AUDIT.md
CYCLE_14_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_14_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_14_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_14_QUALITY_AUDIT.json
CYCLE_14_QUALITY_AUDIT.md
CYCLE_14_REVIEW_RESPONSE.md
CYCLE_14_SUMMARY.json
CYCLE_14_SUMMARY.md
CYCLE_15_ACTUAL_RESEARCH_AUDIT.json
CYCLE_15_ACTUAL_RESEARCH_AUDIT.md
CYCLE_15_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_15_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_15_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_15_QUALITY_AUDIT.json
CYCLE_15_QUALITY_AUDIT.md
CYCLE_15_REVIEW_RESPONSE.md
CYCLE_15_SUMMARY.json
CYCLE_15_SUMMARY.md
CYCLE_16_ACTUAL_RESEARCH_AUDIT.json
CYCLE_16_ACTUAL_RESEARCH_AUDIT.md
CYCLE_16_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_16_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_16_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_16_QUALITY_AUDIT.json
CYCLE_16_QUALITY_AUDIT.md
CYCLE_16_REVIEW_RESPONSE.md
CYCLE_16_SUMMARY.json
CYCLE_16_SUMMARY.md
CYCLE_17_ACTUAL_RESEARCH_AUDIT.json
CYCLE_17_ACTUAL_RESEARCH_AUDIT.md
CYCLE_17_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_17_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_17_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_17_QUALITY_AUDIT.json
CYCLE_17_QUALITY_AUDIT.md
CYCLE_17_REVIEW_RESPONSE.md
CYCLE_17_SUMMARY.json
CYCLE_17_SUMMARY.md
CYCLE_18_ACTUAL_RESEARCH_AUDIT.json
CYCLE_18_ACTUAL_RESEARCH_AUDIT.md
CYCLE_18_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_18_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_18_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_18_QUALITY_AUDIT.json
CYCLE_18_QUALITY_AUDIT.md
CYCLE_18_REVIEW_RESPONSE.md
CYCLE_18_SUMMARY.json
CYCLE_18_SUMMARY.md
CYCLE_19_ACTUAL_RESEARCH_AUDIT.json
CYCLE_19_ACTUAL_RESEARCH_AUDIT.md
CYCLE_19_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_19_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_19_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_19_QUALITY_AUDIT.json
CYCLE_19_QUALITY_AUDIT.md
CYCLE_19_REVIEW_RESPONSE.md
CYCLE_19_SUMMARY.json
CYCLE_19_SUMMARY.md
CYCLE_20_ACTUAL_RESEARCH_AUDIT.json
CYCLE_20_ACTUAL_RESEARCH_AUDIT.md
CYCLE_20_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_20_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_20_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_20_QUALITY_AUDIT.json
CYCLE_20_QUALITY_AUDIT.md
CYCLE_20_REVIEW_RESPONSE.md
CYCLE_20_SUMMARY.json
CYCLE_20_SUMMARY.md
CYCLE_21_ACTUAL_RESEARCH_AUDIT.json
CYCLE_21_ACTUAL_RESEARCH_AUDIT.md
CYCLE_21_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_21_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_21_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_21_QUALITY_AUDIT.json
CYCLE_21_QUALITY_AUDIT.md
CYCLE_21_REVIEW_RESPONSE.md
CYCLE_21_SUMMARY.json
CYCLE_21_SUMMARY.md
CYCLE_22_ACTUAL_RESEARCH_AUDIT.json
CYCLE_22_ACTUAL_RESEARCH_AUDIT.md
CYCLE_22_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_22_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_22_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_22_QUALITY_AUDIT.json
CYCLE_22_QUALITY_AUDIT.md
CYCLE_22_REVIEW_RESPONSE.md
CYCLE_22_SUMMARY.json
CYCLE_22_SUMMARY.md
CYCLE_23_ACTUAL_RESEARCH_AUDIT.json
CYCLE_23_ACTUAL_RESEARCH_AUDIT.md
CYCLE_23_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_23_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_23_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_23_QUALITY_AUDIT.json
CYCLE_23_QUALITY_AUDIT.md
CYCLE_23_REVIEW_RESPONSE.md
CYCLE_23_SUMMARY.json
CYCLE_23_SUMMARY.md
CYCLE_24_ACTUAL_RESEARCH_AUDIT.json
CYCLE_24_ACTUAL_RESEARCH_AUDIT.md
CYCLE_24_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_24_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_24_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_24_QUALITY_AUDIT.json
CYCLE_24_QUALITY_AUDIT.md
CYCLE_24_REVIEW_RESPONSE.md
CYCLE_24_SUMMARY.json
CYCLE_24_SUMMARY.md
CYCLE_25_ACTUAL_RESEARCH_AUDIT.json
CYCLE_25_ACTUAL_RESEARCH_AUDIT.md
CYCLE_25_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_25_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_25_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_25_QUALITY_AUDIT.json
CYCLE_25_QUALITY_AUDIT.md
CYCLE_25_REVIEW_RESPONSE.md
CYCLE_25_SUMMARY.json
CYCLE_25_SUMMARY.md
CYCLE_26_ACTUAL_RESEARCH_AUDIT.json
CYCLE_26_ACTUAL_RESEARCH_AUDIT.md
CYCLE_26_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_26_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_26_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_26_QUALITY_AUDIT.json
CYCLE_26_QUALITY_AUDIT.md
CYCLE_26_REVIEW_RESPONSE.md
CYCLE_26_SUMMARY.json
CYCLE_26_SUMMARY.md
CYCLE_27_ACTUAL_RESEARCH_AUDIT.json
CYCLE_27_ACTUAL_RESEARCH_AUDIT.md
CYCLE_27_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_27_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_27_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_28_ACTUAL_RESEARCH_AUDIT.json
CYCLE_28_ACTUAL_RESEARCH_AUDIT.md
CYCLE_28_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_28_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_28_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_29_ACTUAL_RESEARCH_AUDIT.json
CYCLE_29_ACTUAL_RESEARCH_AUDIT.md
CYCLE_29_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_29_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_29_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_30_ACTUAL_RESEARCH_AUDIT.json
CYCLE_30_ACTUAL_RESEARCH_AUDIT.md
CYCLE_30_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_30_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_30_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_31_ACTUAL_RESEARCH_AUDIT.json
CYCLE_31_ACTUAL_RESEARCH_AUDIT.md
CYCLE_31_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_31_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_31_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_32_ACTUAL_RESEARCH_AUDIT.json
CYCLE_32_ACTUAL_RESEARCH_AUDIT.md
CYCLE_32_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_32_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_32_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_33_ACTUAL_RESEARCH_AUDIT.json
CYCLE_33_ACTUAL_RESEARCH_AUDIT.md
CYCLE_33_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_33_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_33_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_34_ACTUAL_RESEARCH_AUDIT.json
CYCLE_34_ACTUAL_RESEARCH_AUDIT.md
CYCLE_34_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_34_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_34_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_35_ACTUAL_RESEARCH_AUDIT.json
CYCLE_35_ACTUAL_RESEARCH_AUDIT.md
CYCLE_35_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_35_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_35_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_36_ACTUAL_RESEARCH_AUDIT.json
CYCLE_36_ACTUAL_RESEARCH_AUDIT.md
CYCLE_36_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_36_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_36_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_37_ACTUAL_RESEARCH_AUDIT.json
CYCLE_37_ACTUAL_RESEARCH_AUDIT.md
CYCLE_37_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_37_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_37_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_38_ACTUAL_RESEARCH_AUDIT.json
CYCLE_38_ACTUAL_RESEARCH_AUDIT.md
CYCLE_38_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_38_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_38_ACTUAL_RESEARCH_SUMMARY.md
CYCLE_39_ACTUAL_RESEARCH_AUDIT.json
CYCLE_39_ACTUAL_RESEARCH_AUDIT.md
CYCLE_39_ACTUAL_RESEARCH_RESPONSE.md
CYCLE_39_ACTUAL_RESEARCH_SUMMARY.json
CYCLE_39_ACTUAL_RESEARCH_SUMMARY.md
FINAL_GUARDRAIL_CLEANUP_AUDIT.json
FINAL_GUARDRAIL_CLEANUP_AUDIT.md
FINAL_HANDOFF.md
PACKAGE_AUDIT.json
PACKAGE_AUDIT.md
PACKAGE_MANIFEST_PRECOMPILE.json
README.md
flagship_rp1/aastex/rp1_flagship_polished.pdf
flagship_rp1/aastex/rp1_flagship_polished.tex
flagship_rp1/figures/fig-bpt.pdf
flagship_rp1/figures/fig-matched-offsets.pdf
supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf
supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
supplementary_denominator_atlas/figures/topic-01.pdf
supplementary_denominator_atlas/figures/topic-02.pdf
supplementary_denominator_atlas/figures/topic-03.pdf
supplementary_denominator_atlas/figures/topic-04.pdf
supplementary_denominator_atlas/figures/topic-05.pdf
supplementary_denominator_atlas/figures/topic-06.pdf
supplementary_denominator_atlas/figures/topic-07.pdf
supplementary_denominator_atlas/figures/topic-08.pdf

exec
/bin/zsh -lc "find /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z -maxdepth 2 -type f | sed 's#"'^/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/##'"' | sort" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
FLAGSHIP_REVIEW_DECISION_20260709T013510Z.md
INTEGRATION_AUDIT.json
INTEGRATION_AUDIT.md
INTEGRATION_HANDOFF.md
INTEGRATION_MANIFEST_PRECOMPILE.json
README.md
build_flagship_decision_package.py

codex
I’ve got the inventory and package layout. Next I’m pulling the manuscript text plus the package audit so I can check whether the core numbers are cited back to local CSVs and whether the TeX has obvious compile breakpoints.
exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/README.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z

Decision package: one polished RP-1 flagship draft plus one supplementary denominator/proxy atlas.

Compile with Tectonic from each aastex directory, then run package audit.

exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/PACKAGE_AUDIT.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# Decision package audit

Package: `RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`
Audit UTC: 2026-07-09T01:41:23Z

## Counts
- outputs: 2
- pdfs_ok: 2
- logs_ok: 2
- figures_ok: 10
- total_figures: 10
- fatal_failures: 0

## Outputs
- flagship: PDF bytes 236847; SHA256 `3392f53534d8452ebb3db4191dff7855ebb13428dff768d45d847be9d5d8efac`; warnings 10; figures 2
- supplement: PDF bytes 527135; SHA256 `403a69d8fcf02c56bd3266db0de0363ea9c45c659d5a305861cfba7144b705e2`; warnings 19; figures 8

## Failures
- none

Safety: local decision package only; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes.

 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Selection-aware SDSS BPT/sSFR study}
\shortauthors{NebulaMind}
\begin{document}

\title{Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Pilot Matched-Control Study}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We present a selection-aware SDSS DR17 matched-control pilot that measures the association between broad optical BPT-selected galaxies and catalog specific star-formation rate within a selection-limited denominator. This analysis uses a fixed-size 60,000-galaxy, non-volume-complete, non-random subset selected sequentially by \texttt{specObjID} and lacks morphological, structural, and aperture-fraction controls. Because structural proxies such as concentration index and \texttt{fracDeV} were not retained in the cache, the reported -1.309 dex sSFR offset is an association-only measurement within this fixed-size, morphology-uncontrolled optical denominator and cannot be disentangled from a morphology or bulge-fraction association. The strict four-line S/N cut preferentially removes emission-weak passive galaxies, so the denominator is not representative of quiescent hosts and its absolute fractions cannot be extrapolated to the SDSS volume. Broad optical BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, with no morphology, structural-proxy, aperture-fraction, or environment control; the star-forming control pool uses the conservative \citep{kauffmann2003bpt} demarcation, and the 67 unclassified objects are retained in denominator counts but excluded from control pairing. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex; the moderate mass--redshift caliper variant leaves the median essentially unchanged at -1.318 dex for 7,867 pairs. The stricter line-S/N ($S/N \geq 10$) variant yields -0.744 dex, while the Seyfert-like subset yields -0.763 dex after the lower-excitation tail is removed by the stricter cut, so the larger broad-denominator offset shrinks by more than 0.5 dex under the tighter excitation cuts. BPT classification is an optical excitation diagnostic, not a direct proxy for bolometric accretion power or Eddington ratio. The companion supplement inventories the missing structural, environmental, and multiwavelength observables needed for future real-data tests, including morphology, aperture fraction, halo or group labels, CO/HI gas measurements, radio and X-ray proxies, and IFU kinematics.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper addresses a narrow association-only question within a low-redshift SDSS DR17 optical emission-line denominator: do broad optical BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a negative catalog-sSFR offset within the analyzed denominator. The result is not a causal claim or inference; it is an association in a fixed-size optical sample and does not test feedback-related quenching scenarios, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling in this dataset. The 60,000-galaxy subset is non-volume-complete, so it is not normalized into a luminosity or mass function.


The present scope also excludes morphology or aperture controls, structural-proxy matching, Seyfert/LINER separation, bolometric accretion-luminosity proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; as seen in previous literature, retired stellar populations ionized by hot post-AGB stars, as well as low-ionization nuclear emission-line region (LINER)-like ionization, can contaminate broad low-ionization classes and mimic active-nucleus signatures \citep{cidfernandes2011,stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT-selected galaxies'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label. Because structural proxies were not retained in the 60,000-galaxy cache, the present optical denominator cannot separate the measured offset from bulge-fraction or central-velocity-dispersion associations. Because the sample is restricted to $0.02<z<0.12$, the standard local BPT demarcations are used here without any redshift-evolution correction.

\subsection{Scope and limitations}
The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or bolometric accretion-luminosity proxies as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.

\section{Missing observables for future causal inference}
The present SDSS-only analysis is deliberately restricted to an optical association pilot, so the observables needed for any causal interpretation are not measured here. The remaining requirements are morphology and structural proxies, aperture-fraction control, group or halo membership, CO/HI gas masses, radio and X-ray proxies, resolved IFU kinematics, and matched simulation comparisons passed through the same selection function. These are the real-data inputs that the companion supplement inventories as future follow-up targets; they are not results of this paper.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}. It is a selection-limited pilot subset used to estimate the association within the available SDSS cache, not a volume-limited census. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this non-random subset is not a random sky sample and introduces survey-plate and sky-coverage bias. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the subset is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy; the fixed 3-arcsec aperture systematically misses extended star-forming disks at low redshift \citep{kewley2005}. If broad optical BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a galaxy-wide star-formation comparison.
The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Although \texttt{PhotoObj} was joined in the catalog backbone, structural quantities such as \(R_{90}/R_{50}\) and \texttt{fracDeV} were not retained in the 60,000-galaxy cache, so morphology cannot be controlled in this cycle. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}. We use variance-normalized Euclidean matching, with each coordinate standardized by its sample standard deviation before distance calculation, because the feature space is only two variables, $(\log M_\star,z)$, so the rule stays transparent and the resulting nearest-neighbor control remains easy to interpret as an association baseline.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade for the flagship analysis sample.\label{tab:selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines with valid flux measurements (\texttt{ivar} $> 0$) & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The 416,554-to-373,445 drop when requiring \texttt{ivar} $> 0$ reflects the removal of rows with unusable line-flux uncertainties; this table does not distinguish masking, edge-of-chip loss, or missing spectral coverage. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. This preferentially increases the relative share of star-forming objects among the surviving denominator and therefore inflates the relative weight of star-forming controls available for matching. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the fixed-size-sample limitation.

\section{Classification and matching}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The intermediate/composite galaxies are retained in the denominator counts but are not part of the star-forming control pool used for matching. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing; this cycle does not tabulate a separate failure mode for them. Here, the star-forming control pool is defined as objects below the Kauffmann et al.\ (2003) demarcation, which is a conservative optical cut and may still include weak or obscured active-nucleus contaminants. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control by variance-normalized Euclidean distance in standardized $(\log M_\star,z)$ space, with replacement. In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), and the unrestricted Euclidean match has median absolute separations of 0.0045 dex in $\log M_\star$ and 0.00021 in redshift, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, accretion-luminosity proxy, or duty-cycle phase; these missing dimensions define follow-up requirements. The preferred estimate does not impose a maximum mass--redshift caliper; the caliper row in Table~\ref{tab:robust} is a sensitivity variant. The moderate mass--redshift caliper sensitivity variant uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.
Here, ``broad optical BPT-selected'' means the inclusive optical-emission-line class under the standard BPT demarcations, while the Seyfert-like sensitivity check uses the stricter Kewley et al.\ (2006) high-excitation cut to remove most of the low-excitation LINER/retired branch by construction rather than to define a separate accretion-power measurement.

\begin{figure*}
\centering
\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the SDSS DR17 analysis denominator. The matched controls are paired in stellar mass and redshift only, not in morphology, so the diagram verifies the optical-excitation classes used for matching but does not by itself establish an accretion-based interpretation.}
\label{fig:bpt}
\end{figure*}

\section{Matched-control result}
The preferred broad optical BPT comparison gives a large negative catalog-sSFR offset for the broad optical BPT-selected galaxies relative to star-forming controls.
    \par\noindent\textbf{Morphology and aperture caveat.} Without controlling for structural morphology or aperture fraction, a median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fixed-size, morphology-uncontrolled optical denominator and fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology, structural proxies, or aperture fraction, the observed sSFR offset is highly degenerate with the known correlation between stellar mass and galaxy morphology and the transition from disk-dominated to bulge-dominated systems, including bulge prominence or central velocity dispersion associations \citep{schawinski2010,bluck2014,belfiore2016,piotrowska2022}. The lack of concentration-index or \texttt{fracDeV}-style structural matching limits the result's ability to separate bulge-linked structural associations from excitation-linked associations. Single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, so spatially resolved integral-field spectroscopy is required to resolve the aperture-morphology degeneracy \citep{penny2018,cheung2016,bundy2015}. Within the present data, the association is therefore still not separable from a morphology or bulge-fraction association. The robustness interval in Table~\ref{tab:robust} is a 95\% confidence interval on the median offset.

\begin{deluxetable*}{lrrrr}
\tabletypesize{\scriptsize}
\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
\startdata
Broad optical BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
Broad optical BPT-selected targets, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
\enddata
\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$, and it leaves the median offset essentially unchanged at -1.318 dex for 7,867 pairs. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
\end{deluxetable*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Distribution of matched-pair catalog-sSFR offsets for the preferred broad optical BPT-selected galaxy minus nearest star-forming control estimate ($N=8{,}146$ pairs, without a maximum mass--redshift caliper). The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
\label{fig:offsets}
\end{figure*}

\section{Interpretation}
The result is directly measured in the capped sample and remains falsifiable within the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset persists under a moderate mass--redshift caliper, which is already reflected by the 7,867-pair, -1.318 dex sensitivity row. Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude to -0.744 dex and -0.763 dex, respectively (Table~\ref{tab:robust}), a reduction of $>0.5$ dex relative to the preferred association estimate. The Kewley et al.\ (2006) demarcation explicitly removes the retired/LINER-like low-ionization tail, so the larger -1.309 dex offset reflects in part that broader low-ionization branch rather than solely Seyfert-like excitation. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad optical BPT-selected sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be biased high relative to a galaxy-wide star-formation comparison. Matching on mass and redshift alone leaves morphology uncontrolled, and the fixed 3-arcsec fiber can under-sample extended disk star formation at low redshift; this is a known source of central-to-global mismatch \citep[e.g.,][]{harrison2017,ellison2021}. The central-kiloparsec aperture restriction is one reason this remains a local association rather than a galaxy-wide star-formation measurement. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size, selection-limited, morphology-uncontrolled 60,000-galaxy pilot sample. Any mechanistic interpretation requires additional real data, including morphology and aperture controls, Seyfert/LINER separation, bolometric accretion-luminosity proxy, gas mass, environment, and time-domain/duty-cycle modelling. These are missing observables in the present catalog and are required for future mechanism tests.
The choice of variance-normalized Euclidean matching is deliberate: with only two standardized coordinates, it preserves a simple nearest-neighbor control rule without introducing an additional model layer that would not be better constrained by the available data.

\section{Conclusion}
RP-1 is a selection-aware pilot association paper. This analysis is bounded by a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}, and lacks morphological, structural, and aperture-fraction controls. Without controlling for structural morphology or aperture fraction, the reported -1.309 dex sSFR offset is an association-only measurement within this fixed-size, morphology-uncontrolled optical denominator and is currently indistinguishable from a morphology or bulge-fraction association. Its key results are the preferred -1.309 dex offset, the persistence of the offset under a moderate mass--redshift caliper, and the reduction to -0.744 dex for the stricter line-S/N variant and -0.763 dex for the Seyfert-like subset. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} is a denominator/proxy atlas and follow-up target list for the missing-observable requirements of future real-data tests. See the supplement's neighbor-rank/fiber-collision and CO/HI entries, summarized in its atlas overview, for the clearest examples of the remaining constraints.
In practice, future follow-up requires integration with the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation comparisons passed through the same selection functions \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,ellison2011,piotrowska2022,wetzel2013,dekel2006}; these references are cited as examples of missing observables for future follow-up, not as validation of any mechanism in this SDSS-only denominator. These are missing observables in the present catalog and are required for future mechanism tests. The result remains association-only until morphology, aperture fraction, and the missing multiwavelength or IFU observables are added. The fixed 60,000-galaxy cache remains a non-random selection-limited subset, so the reported offsets should continue to be read as denominator-bound associations rather than population-wide trends within this morphology-uncontrolled optical denominator.

\section*{Data Availability}
This paper uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. The 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and the manuscript conclusions remain conditional on the optical-emission-line denominator. No mock, synthetic, fake, placeholder, or toy data were used.

\facilities{SDSS}

\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Belfiore et al.(2016)]{belfiore2016} Belfiore, A., Maiolino, R., Maraston, C., et al. 2016, MNRAS, 461, 3111
\bibitem[Bluck et al.(2014)]{bluck2014} Bluck, A.~F.~L., Bruce, V.~A., Pilkington, K., et al. 2014, MNRAS, 441, 599
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Bundy et al.(2015)]{bundy2015} Bundy, K., Law, D.~R., Yan, R., et al. 2015, ApJ, 798, 7
\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasi{\'n}ska, G., Schlickmann, S., et al. 2011, MNRAS, 413, 1687
\bibitem[Cheung et al.(2016)]{cheung2016} Cheung, E., Bundy, K., Cappellari, M., et al. 2016, Nature, 533, 504
\bibitem[Ellison et al.(2011)]{ellison2011} Ellison, S.~L., Patton, D.~R., Mendel, J.~T., et al. 2011, MNRAS, 418, 2043
\bibitem[Ellison et al.(2021)]{ellison2021} Ellison, S.~L., Lin, L., Rosario, D.~J., et al. 2021, MNRAS, 501, 4777
\bibitem[Harrison(2017)]{harrison2017} Harrison, C.~M. 2017, Nature Astronomy, 1, 0165
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Dav{\'e} et al.(2019)]{simba2019} Dav{\'e}, R., Angl{\'e}s-Alc{\'a}zar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2005)]{kewley2005} Kewley, L.~J., Jansen, R.~A., \& Geller, M.~J. 2005, PASP, 117, 227
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Penny et al.(2018)]{penny2018} Penny, S.~J., Davies, R.~L., Houghton, R.~C.~W., et al. 2018, MNRAS, 476, 979
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\bibitem[Schawinski et al.(2010)]{schawinski2010} Schawinski, K., Evans, D.~A., Virani, S., et al. 2010, ApJ, 711, 284
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Stasi{\'n}ska et al.(2008)]{stasinska2008} Stasi{\'n}ska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasi{\'n}ska et al.(2015)]{stasinska2015} Stasi{\'n}ska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodr{\'e}, L. 2015, MNRAS, 449, 559
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}

exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex | sed -n '261,520p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
codex
I’ve read the flagship draft. Now I’m checking the supplement, the package manifest, and the surrounding run outputs for two things: whether the headline numbers are consistent across files and whether anything in the package slips into mock/synthetic language.
exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS denominator/proxy atlas}
\shortauthors{NebulaMind}
\begin{document}

\title{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
This supplement is the companion to the selection-aware SDSS BPT/sSFR pilot study and organizes eight SDSS DR17 denominator and proxy notes into one coherent, association-only optical baseline atlas for future real-data follow-up. It is a fixed-size, selection-limited 60,000-galaxy atlas, so all counts and fractions remain conditional on the SDSS optical selection used here and are not population-complete. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this non-random subset is not a random sky sample and introduces survey-plate and sky-coverage bias. The 55-arcsec SDSS fiber-collision limit also biases projected-neighbor statistics in dense regions, so the environment-related ranks later in the atlas are explicitly selection-limited before any physical interpretation is attempted. The atlas preserves follow-up targets for environment, broad optical BPT-selected incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-based comparison data are treated as missing observables for future tests rather than as measurements in this package. The sample coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one atlas with eight linked entries, not eight independent causal-mechanism papers. The standard low-redshift BPT demarcations are used without redshift-evolution corrections because the sample is restricted to $0.02<z<0.12$. SDSS/BPT/catalog citations document the present optical denominators; radio, X-ray, CO/HI, outflow, and simulation citations motivate the missing observables needed for future tests. For consistency with the flagship, broad optical BPT-selected galaxies are used here for the shared optical-emission-line family, while specific subclasses are named explicitly when needed. Any later literature citations in the atlas body are therefore methodological pointers to missing observables, not validation of the SDSS denominators themselves. Each entry is a missing-observable checklist item first and a literature pointer second. \textbf{This atlas provides observational baselines only; it is a selection-biased optical denominator and follow-up checklist, not a causal-mechanism test, and it cannot independently confirm or refute causal models of feedback without the integration of the listed missing observables.}
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical association between BPT classification and catalog sSFR. These eight entries are distinct baseline-and-follow-up atlas notes: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the entries span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. For consistency with the flagship, the atlas uses the broad optical BPT-selected family when the full optical-emission-line denominator is meant and names specific subsets only when the stricter selection matters. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. These are missing observables in the present catalog and are required for future mechanism tests. This is an association-only optical baseline atlas and a single internal follow-up checklist for future causal inference, not a collection of standalone mechanism papers.

\section{Shared denominator limitations}
The atlas uses the same analyzed public-data backbone as the main paper: 60,000 galaxies in a fixed, selection-limited subset from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, i.e. 24.0\% sample coverage. The four-line selection is sSFR-dependent and the sample is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The galaxy-by-galaxy stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. Although \texttt{PhotoObj} was joined in the catalog backbone, structural quantities such as \(R_{90}/R_{50}\) and \texttt{fracDeV} were not retained in the 60,000-row cache, so morphology cannot be controlled in this cycle. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing.

The shared limitations are the same ones that appear throughout the atlas notes and should be read once here rather than repeated in each subsection. The fixed 3-arcsec SDSS fiber makes all derived optical quantities central-fiber proxies rather than global measurements, the strict four-line S/N cuts preferentially remove low-equivalent-width or passive systems, and the 55-arcsec fiber-collision limit distorts any projected-neighbor statistic in dense regions. Because the subset is sequentially selected by \texttt{specObjID}, it is also not a random sky sample and can inherit survey-plate and sky-coverage bias. These are denominator limitations, not physical results, and they apply to every subsection below.

The eight subsections below are intentionally parallel baseline-plus-follow-up notes: each one states the observed optical denominator or target vector, then names the missing observables that a future multiwavelength or simulation-based test would need before any physical inference can be made. In other words, the sections are distinct follow-up domains bounded by the same optical selection bias, and their role is to organize the atlas rather than to stand as separate papers.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade shared by the atlas; the cache cap is summarized in the main paper.\label{tab:supp-selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines with valid flux measurements (\texttt{ivar} $> 0$) & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The 416,554-to-373,445 drop when requiring \texttt{ivar} $> 0$ reflects the removal of rows with unusable line-flux uncertainties; this table does not distinguish masking, edge-of-chip loss, or missing spectral coverage. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

\section{Atlas summary}
Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight entries. All eight entries are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or forward-model comparison data are added, so their present role is to organize follow-up rather than to establish causal physical claims.

\begin{deluxetable*}{llll}
\tabletypesize{\scriptsize}
\tablecaption{Atlas-level follow-up menu. Each row summarizes the present optical role and the missing observables needed before any physical inference. This is a selection-dependent optical baseline, not a physical density metric.\label{tab:atlas-summary}}
\tablehead{\colhead{Topic} & \colhead{Observed baseline} & \colhead{Missing observables} & \colhead{Future Follow-up Domain}}
\startdata
Environment & low-sSFR vs.\ 10th-neighbor rank (60,000 total; 15,000 per quartile) & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test \\
Maintenance heating & broad optical BPT-selected hosts in massive low-sSFR galaxies (maintenance-heating baseline; 9,298 massive; 5,695 low-sSFR) & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
Outflow kinematics & high-excitation broad optical BPT-selected subset (4,440/60,000) & resolved velocities; halo potentials; multiphase gas; CGM tracers & kinematic follow-up \\
Env.\ jets & density-stratified broad optical BPT-selected fraction in massive hosts & radio morphology/age; cavity energetics; hot-gas density & radio-jet follow-up \\
Mass bin & low-sSFR and broad optical BPT-selected incidence by $M_\star$ bin (15 cells with $n\geq50$) & gas fractions; baryon deficits; halo masses; physical-observable constraints & selection diagnostic \\
Tracer census & tracer prevalence in 60k sample (0.136 to 0.418) & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
Gas depletion & gas-depletion low-sSFR baseline; H$\alpha$ proxy (6,729 galaxies) & CO/dust gas masses; aperture-matched SFRs; morphology; environment & CO/HI follow-up \\
Simulation vector & mass-redshift target vector (15 cells with $n\geq50$) & simulations through SDSS/MaNGA/ALMA/X-ray/radio selection; aperture/noise models & forward model \\
\enddata
\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects the optical emission-line selection function, which preferentially removes low-equivalent-width or passive systems from the denominator; the surviving sample therefore becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

\section{Atlas notes}
As a reminder, each atlas entry is a baseline-plus-follow-up checklist, not a standalone physical-mechanism result.

\subsection{Relative neighbor-count baseline: SDSS 10th-neighbor index for low-sSFR incidence}
See Table~\ref{tab:atlas-summary}; we establish a relative neighbor-count baseline within the emission-line denominator that can later be joined to group catalogs and halo masses. The 10th-neighbor index is the rank of the 10th nearest companion in projected sky separation within this redshift-limited sample; it is an internal ordinal rank within this selection-biased sample and should not be interpreted as a physical environmental volume density or halo density. Because no additional line-of-sight velocity window is imposed beyond the redshift slice, the statistic is especially susceptible to projection effects. The projected-neighbor ranking is computed within the full $0.02<z<0.12$ redshift slice, with no additional line-of-sight velocity window imposed beyond those sample limits. The SDSS 55-arcsec fiber-collision limit systematically removes close neighbors in dense regions, so the 10th-neighbor proxy is biased before any physical interpretation is attempted. We emphasize that the SDSS 55-arcsec fiber collision limit systematically biases this index in dense environments, precluding its use as a physical density metric without forward-modeled corrections. In this sense, the 10th-neighbor index is a fiber-collision-biased projected-neighbor rank rather than a physical density estimate. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004 coefficient uncertainty. The follow-up ingredients are group catalogues, robust central/satellite labels, halo masses, a spectroscopic fiber-collision correction at the 55-arcsec scale, morphology, and multi-redshift selection functions. Within this selection-biased emission-line sample, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up.}
\label{fig:m1-rp2-neighbor-count-baseline}
\end{figure}


\subsection{Maintenance-heating denominator: broad optical BPT-selected hosts in massive SDSS galaxies}
See Table~\ref{tab:atlas-summary}; we isolate the broad optical BPT-selected duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the broad optical BPT-selected fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The broad optical BPT-selected fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. This optical fraction represents an observational baseline pool, not the active maintenance-heating duty cycle. See the next subsection for the related radio-jet baseline that uses the same projected-density proxy. The follow-up ingredients are X-ray cavity or cooling-luminosity measurements \citep{fabian2012}, calibrated radio jet mechanical powers \citep[e.g.,][]{best2005,hardcastle2020}, halo-selected parent catalogues, and nondetection modelling. Those observables are missing here; this entry remains an optical baseline only, and future follow-up requires those real observables before any physical inference. Optical broad BPT selection primarily traces the radiative-mode denominator, so it cannot isolate the mechanically dominated jet-mode population without contemporaneous X-ray and radio measurements \citep{heckmanbest2014}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements.}
\label{fig:m1-rp3-maintenance-heating}
\end{figure}


\subsection{High-excitation broad optical BPT-selected baseline: resolved kinematics follow-up}
See Table~\ref{tab:atlas-summary}; we isolate the high-excitation broad optical BPT-selected denominator that resolved kinematics would need to test escape versus recycling. High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The follow-up ingredients are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers. Without IFU kinematics to decouple non-circular outflow components from host rotation, optical excitation alone cannot determine whether the gas exceeds the halo escape speed \citep{harrison2018}. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
\caption{SDSS optical emission-line denominator: the high-excitation BPT-selected subset used to define an observational baseline for future resolved-kinematic measurements.}
\label{fig:m2-p1-outflow-escape-recycling}
\end{figure}


\subsection{Radio-jet environment baseline: broad optical BPT-selected fraction vs. 10th-neighbor index in massive hosts}
See Table~\ref{tab:atlas-summary}; we define the environment-stratified optical denominator that future radio and X-ray work could test. This subsection reuses the same projected-neighbor ranking described in the relative neighbor-count baseline above and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has a broad optical BPT-selected fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The follow-up ingredients are radio jet morphology and age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
\caption{SDSS optical emission-line denominator: the high- and low-density quartile comparison among massive SDSS hosts, used as a baseline for future radio-jet and X-ray work.}
\label{fig:m2-p2-radio-jet-environment}
\end{figure}


\subsection{Stellar-mass selection diagnostic: low-sSFR and broad optical BPT-selected incidence}
See Table~\ref{tab:atlas-summary}; in this optical-emission-line denominator, the peak in the stellar-mass range \(11.0 \le \log(M_\star/M_\odot) \le 12.5\) is consistent with a selection-function bias: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is concentrated in that mass bin. It must not be interpreted as a universal physical threshold. We identify the mass bin where a future gas-inclusive study should look for a selection-sensitive change in incidence. The note measures the incidence of low catalog-sSFR and broad optical BPT-selected classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the broad optical BPT-selected incidence peaks in the 11.0--12.5 bin at 0.520 within this selection-limited, SpecObjID-capped pilot sample. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The follow-up ingredients are gas fractions, baryon deficits, halo masses, central velocity dispersion proxies \citep{piotrowska2022}, stellar-regulation observables, and high-redshift extensions. The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and broad optical BPT-selected incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up.}
\label{fig:m2-p3-transition-mass}
\end{figure}


\subsection{Tracer-threshold census for multiphase follow-up}
See Table~\ref{tab:atlas-summary}; we compare optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred broad optical BPT-selected prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The follow-up ingredients are ionized, molecular, and neutral tracers, X-ray or radio tracers, a shared parent denominator, and a consistent aperture model. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work.}
\label{fig:m3-p1-multiphase-census}
\end{figure}


\subsection{Low-sSFR optical denominator: baseline for future CO/HI gas measurements}
See Table~\ref{tab:atlas-summary}; we define the denominator for CO/HI gas-fraction and depletion-time follow-up. Using the gas-depletion note's low-sSFR baseline, the massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. This denominator is note-specific and should not be conflated with the \(\log M_\star \geq 10.8\) maintenance-heating subset summarized above. Its broad optical BPT-selected fraction is 0.549, and the median H-alpha luminosity proxy is \(\log (L_{\mathrm{H}\alpha}/\mathrm{erg\,s^{-1}}) = 40.06\). Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value rather than raw fiber flux; that catalog-level correction extrapolates the fiber measurement beyond the aperture in a model-dependent way and assumes line emission broadly tracks the broadband light profile. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency or measure total cold-gas mass \citep{tacconi2018}; this note identifies the CO/HI follow-up denominator and optical baseline required for spatially resolved gas tests. The follow-up ingredients are global CO or dust-based molecular gas masses \citep[e.g., xCOLD GASS;][]{xcoldgass2017}, atomic hydrogen masses \citep[e.g., xGASS;][]{xgass2018}, aperture-matched SFRs, morphology, and environment labels, together with radio, X-ray, and IFU observables that are still missing here. As with any H$\alpha$-based proxy, residual dust attenuation and stellar-absorption systematics can still affect the optical denominator, so this value should be read as a line-luminosity proxy rather than a direct total cold-gas-mass measurement. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference. No mock, synthetic, fake, placeholder, or toy data were used in compiling this atlas.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
\caption{SDSS optical emission-line denominator: the massive low-sSFR SDSS galaxies available for CO/HI depletion-time follow-up.}
\label{fig:m3-p2-gas-depletion-efficiency}
\end{figure}


\subsection{Simulation target vector for forward-model comparison}
See Table~\ref{tab:atlas-summary}; we provide a compact observed target vector for forward modelling. The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, broad optical BPT-selected incidence, and colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and broad optical BPT-selected fractions span 0.003-0.520. The follow-up ingredients are simulations \citep{eagle2015} passed through the exact optical S/N and fiber-aperture selection function used here, including the sequential 60,000-row \texttt{specObjID} cache cap, then through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions, together with aperture models and noise models. Without those matched selection steps, any simulation comparison is not a valid test. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
\caption{SDSS optical emission-line denominator: low-sSFR fraction, broad optical BPT-selected incidence, and colour versus mass and redshift in the SDSS emission-line sample. This is an observed target vector for forward modelling.}
\label{fig:m3-p3-simulation-validation}
\end{figure}

\section{Package decision}
These eight entries should remain supplementary until the missing observables are added. They are best treated as a single internal follow-up checklist: suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-mechanism papers in their current SDSS-only form. The observational role of each subsection is therefore to define what real data are still needed, not to expand the current SDSS-only measurement set. In particular, the atlas does not convert optical denominators into physical densities, depletion rates, or causal feedback claims.

\section*{Data Availability}
This atlas uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. The 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and all eight notes remain conditional on the optical-selection denominators summarized in this atlas. No mock, synthetic, fake, placeholder, or toy data were used.

\facilities{SDSS}

\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasi{\'n}ska, G., Schlickmann, S., et al. 2011, MNRAS, 413, 1687
\bibitem[Hardcastle \& Croston(2020)]{hardcastle2020} Hardcastle, M.~J., \& Croston, J.~H. 2020, New Astronomy Reviews, 88, 101539
\bibitem[Harrison et al.(2018)]{harrison2018} Harrison, C.~M., Costa, T., Tadhunter, C.~N., et al. 2018, Nature Astronomy, 2, 198
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Stasi{\'n}ska et al.(2008)]{stasinska2008} Stasi{\'n}ska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasi{\'n}ska et al.(2015)]{stasinska2015} Stasi{\'n}ska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodr{\'e}, L. 2015, MNRAS, 449, 559
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Tacconi et al.(2018)]{tacconi2018} Tacconi, L.~J., Genzel, R., Saintonge, A., et al. 2018, ApJ, 853, 179
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}

exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/PACKAGE_MANIFEST_PRECOMPILE.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "created_utc": "2026-07-09T01:40:44Z",
  "decision": "one polished RP-1 flagship draft plus one supplementary denominator/proxy atlas for the other eight",
  "flagship": {
    "expected_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.pdf",
    "figures": [
      {
        "bytes": 86693,
        "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/figures/fig-bpt.pdf",
        "sha256": "99cc2411c43dcd41895d6cb55234648a8b8ffc498eaf8ffeea8ec534c119b999",
        "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf"
      },
      {
        "bytes": 78775,
        "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/figures/fig-matched-offsets.pdf",
        "sha256": "83d16bcbeada88091c5c68a4fd98fd96af9d3b8971bd361a55d0f1b16ca95661",
        "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf"
      }
    ],
    "slug": "m1_rp1_sdss_agn_sfr",
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.tex"
  },
  "package_id": "RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z",
  "safety": "local-only files under handoff tree; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes",
  "source_integration_run": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z",
  "supplement": {
    "expected_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf",
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex",
    "topics": [
      {
        "fig_name": "topic-01.pdf",
        "figure": {
          "bytes": 14881,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-01.pdf",
          "sha256": "1fd192eed0643ae73b54e06c311117fb6c3241c1f952bade758e56e32fe02d9f",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/figures/fig-topic.pdf"
        },
        "label": "m1-rp2-environment-quenching",
        "slug": "m1_rp2_environment_quenching",
        "status": "guarded proxy/denominator draft",
        "title": "SDSS density proxy for environmental quenching: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-02.pdf",
        "figure": {
          "bytes": 14966,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-02.pdf",
          "sha256": "596db86bacb484ebec5750f3ef41ceb490d5b7c8a870b0c5cb4638f2aab92fe8",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf"
        },
        "label": "m1-rp3-maintenance-heating",
        "slug": "m1_rp3_maintenance_heating",
        "status": "guarded proxy/denominator draft",
        "title": "Optical-AGN denominator for maintenance-heating follow-up: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-03.pdf",
        "figure": {
          "bytes": 247680,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-03.pdf",
          "sha256": "31e5c88cd1e02bf868b18000814317477bbdf14cbbbb95b8f1708f0f107f4670",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf"
        },
        "label": "m2-p1-outflow-escape-recycling",
        "slug": "m2_p1_outflow_escape_recycling",
        "status": "guarded proxy/denominator draft",
        "title": "SDSS high-excitation AGN denominator for outflow escape tests: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-04.pdf",
        "figure": {
          "bytes": 15267,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-04.pdf",
          "sha256": "8bd1b0248cf0939fb2ba0a64155586b3f13a0dc2eff581e2ab63ae750481694c",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf"
        },
        "label": "m2-p2-radio-jet-environment",
        "slug": "m2_p2_radio_jet_environment",
        "status": "guarded proxy/denominator draft",
        "title": "Environment proxy for optical AGN in massive SDSS hosts: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-05.pdf",
        "figure": {
          "bytes": 14913,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-05.pdf",
          "sha256": "725dfb62948db7d4b868eef7b18ba9739ad814d821cc507d3a19c53c556943f9",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf"
        },
        "label": "m2-p3-feedback-transition-mass",
        "slug": "m2_p3_feedback_transition_mass",
        "status": "guarded proxy/denominator draft",
        "title": "SDSS mass transition in quenching and optical AGN incidence: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-06.pdf",
        "figure": {
          "bytes": 16341,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-06.pdf",
          "sha256": "abfc743a35167e4247288ffe0571531f839989078861f94c2fa49ed9914d79f2",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/figures/fig-topic.pdf"
        },
        "label": "m3-p1-multiphase-census",
        "slug": "m3_p1_multiphase_census",
        "status": "guarded proxy/denominator draft",
        "title": "Common-denominator optical tracer census in SDSS: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-07.pdf",
        "figure": {
          "bytes": 139945,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-07.pdf",
          "sha256": "a20bf97de10b49f6c662f5e6c7f403d935b8615abf1c8dc9daddc7174f861d4a",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf"
        },
        "label": "m3-p2-gas-depletion-efficiency",
        "slug": "m3_p2_gas_depletion_efficiency",
        "status": "guarded proxy/denominator draft",
        "title": "Optical denominator for gas-fraction versus efficiency tests: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-08.pdf",
        "figure": {
          "bytes": 16385,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-08.pdf",
          "sha256": "eef8a9b385dfb97aa0cef8df24f363712f28140f8988a6a2b6cac169f1b8d61d",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/figures/fig-topic.pdf"
        },
        "label": "m3-p3-simulation-validation",
        "slug": "m3_p3_simulation_validation",
        "status": "guarded proxy/denominator draft",
        "title": "SDSS target vector for feedback-model validation: selection-aware SDSS optical proxy integration"
      }
    ]
  }
}
exec
/bin/zsh -lc "rg -n \"mock|synthetic|fake|placeholder|toy|random|simulated|dummy\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py:201:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{{york2000,sdssdr17,brinchmann2004}}. The cached analysis table is capped at {fmt(selection['cached_rows'])} rows and ordered by \texttt{{specObjID}}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains {fmt(selection['strict_sdss_sn_ge_3_total'])} rows, so the cache covers {pct(selection['cached_coverage_of_strict_sdss_sn_ge_3'])}\% of that strict parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py:249:RP-1 should be the flagship paper from the current local package. It should be polished further as a concise, selection-aware association paper. The other eight active topics should be packaged as a supplementary denominator/proxy atlas, not as independent causal feedback papers, because their original claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables not present in the current SDSS-only analysis.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py:294:This supplement packages the eight non-flagship Galaxy Evolution drafts as denominator/proxy notes rather than standalone physical-feedback papers. All notes share the same capped 60,000-row SDSS DR17 optical emission-line cache and the same selection-function caveats. The atlas preserves useful follow-up targets--environment proxies, optical AGN denominators, transition-mass vectors, tracer-threshold censuses, gas-follow-up denominators, and simulation target vectors--while explicitly refusing claims that require radio, X-ray, molecular/neutral gas, resolved outflow, halo/group, or simulation-mock data not analyzed here.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py:303:The atlas uses the same cached public-data backbone as the flagship: {fmt(selection['cached_rows'])} cached rows from a strict public four-line S/N$\geq3$ parent of {fmt(selection['strict_sdss_sn_ge_3_total'])} rows, i.e. {pct(selection['cached_coverage_of_strict_sdss_sn_ge_3'])}\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped/non-random, so all counts and fractions are conditional denominators rather than population-complete measurements.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_33_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:8:  "full_proposal_requires": "simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_RESPONSE.md:11:- I did not add any new measurements, mock values, invented citations, or synthetic denominators.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_RESPONSE.md:22:- The flagship and supplement are now slightly more explicit about the morphology degeneracy and the non-physical nature of the neighbor proxy while preserving all reported real-data results and the no-mock policy.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/FLAGSHIP_REVIEW_DECISION_20260709T013510Z.md:35:- It must foreground the capped/non-random cache and four-line emission-line selection.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/FLAGSHIP_REVIEW_DECISION_20260709T013510Z.md:49:- `m3_p3_simulation_validation`: lacks forward-modelled simulation mocks.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_24_ACTUAL_RESEARCH_RESPONSE.md:4:- Updated the flagship abstract and conclusion to state the association-only boundary more explicitly, including the non-random 60,000-galaxy cap and the lack of morphology, structure, and aperture-fraction controls.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/FINAL_HANDOFF.md:86:- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_HANDOFF.md:84:- Cached-vs-public marginal differences did not exceed 5 percentage points in redshift, stellar mass, or sSFR, but the cache remains capped and non-random.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_HANDOFF.md:164:- explicitly state that the 60,000-row cache is capped and non-random;
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_RESPONSE.md:21:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_RESPONSE.md:24:- The flagship and supplement are now slightly more explicit about their real-data provenance limits and future-observable requirements while preserving all reported results and the no-mock policy.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex:70:SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex:72:Simulation suites and mock-observation methods define the future comparison problem; no simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,imanga2023,donnari2021,dubois2013,dubois2016}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_AUDIT.json:92:      "non-random"
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_REVIEW_RESPONSE.md:9:- Supplement abstract now states that the 60,000-row cache is an arbitrary, non-random pilot cap, and Section 3.1 now folds the 55-arcsec fiber-collision correction into the missing-observables list.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_REVIEW_RESPONSE.md:17:- Any attempt to add morphology, aperture-matched SFRs, CO/HI, X-ray, radio, halo/group, outflow, or simulation-mock measurements not present in this package.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_RESPONSE.md:14:- I did not introduce any mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_17_REVIEW_RESPONSE.md:11:- In [`supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`](./supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex), I reworded the 60,000-row cap description to say it is a local, non-random pilot cap.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_20_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_RESPONSE.md:12:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_REVIEW_RESPONSE.md:5:- Clarified in both TeX files that the 60,000-row cache is a computational, non-random pilot cap rather than a physical selection threshold.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_REVIEW_RESPONSE.md:18:- The remaining morphology, gas-phase, environment, and mock-observation requirements still need new data if they are to be promoted beyond association-only or baseline language.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_RESPONSE.md:23:- No mock, synthetic, placeholder, or toy data language was added beyond the existing real-data guardrails.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_RESPONSE.md:20:- No mock, synthetic, placeholder, or toy data were added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_RESPONSE.md:27:- I checked the edited prose for the banned mock/synthetic language and for the main causal overstatements targeted by the review.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.tex:24:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The cached analysis table is capped at 60,000 rows and ordered by \texttt{specObjID}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the cache covers 24.0\% of that strict parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.tex:82:RP-1 should be the flagship paper from the current local package. It should be polished further as a concise, selection-aware association paper. The other eight active topics should be packaged as a supplementary denominator/proxy atlas, not as independent causal feedback papers, because their original claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables not present in the current SDSS-only analysis.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_20_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_20_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_20_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_20_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_REVIEW_RESPONSE.md:19:- Any stronger claim about feedback, quenching, or outflow physics still requires new morphology, aperture, multiwavelength, or mock-observation data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/FINAL_HANDOFF.md:86:- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_REVIEW_RESPONSE.md:8:- Split the flagship conclusion citations into role-separated groups: radio/X-ray maintenance heating, CO/HI gas follow-up, outflow/kinematics, simulation-mock comparisons, and environment/context references.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_REVIEW_RESPONSE.md:17:- Any attempt to add morphology matching, aperture-matched SFRs, halo/group catalogs, CO/HI, X-ray, radio, or simulation-mock observables that are not present in this package.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_RESPONSE.md:15:- No mock, synthetic, placeholder, or toy data were added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_REVIEW_RESPONSE.md:5:- Flagship abstract now states that the 60k-row pilot cache is non-random, non-volume-limited, and cannot be normalized into absolute volume densities or luminosity functions.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_REVIEW_RESPONSE.md:7:- In [`flagship_rp1/aastex/rp1_flagship_polished.tex`](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/flagship_rp1/aastex/rp1_flagship_polished.tex), I clarified that the 60,000-row pilot cache is sequentially selected by `specObjID`, which is the source of the non-random cap.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md:6:- Added an explicit warning that the 60,000-row cache cap is non-random and non-extrapolatable to the SDSS volume.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md:8:- Added an explicit no-mock-data statement to the flagship data-availability section.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md:10:- Added an explicit no-mock-data statement to the supplement data-availability section and to the CO/HI follow-up note.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_33_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_33_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_33_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_RESPONSE.md:15:- No mock, synthetic, placeholder, toy, or invented real-data values were added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_RESPONSE.md:4:- Updated [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_31_package/flagship_rp1/aastex/rp1_flagship_polished.tex) to add explicit non-random / non-volume-complete selection language in the abstract, data backbone, and conclusion.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_RESPONSE.md:6:- Updated [supplementary_denominator_atlas.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_31_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex) to mirror the same non-random selection wording in the abstract and keep the atlas framed as a selection-biased optical denominator.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_RESPONSE.md:20:- No mock, synthetic, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_RESPONSE.md:17:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_33_ACTUAL_RESEARCH_RESPONSE.md:11:- No mock, synthetic, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_26_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],

exec
/bin/zsh -lc "rg -n \"8,146|8146|-1\\.309|\\[-1\\.334,\\-1\\.283\\]|60,000|249,917|24\\.0%|7,867|7,419|1,530|2,114|0\\.763|0\\.744|0\\.744|0\\.763\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py:190:We present a local, selection-aware SDSS DR17 pilot measuring the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of {fmt(selection['strict_sdss_sn_ge_3_total'])} galaxies. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift. The preferred matched comparison yields {fmt(base['matched_pairs'])} pairs and a median $\Delta\log {{\rm sSFR}}$ of {fmt(base['median_delta_log_sSFR'])} dex, with a bootstrap interval of [{fmt(base.get('median_delta_ci95_low'))},{fmt(base.get('median_delta_ci95_high'))}] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py:294:This supplement packages the eight non-flagship Galaxy Evolution drafts as denominator/proxy notes rather than standalone physical-feedback papers. All notes share the same capped 60,000-row SDSS DR17 optical emission-line cache and the same selection-function caveats. The atlas preserves useful follow-up targets--environment proxies, optical AGN denominators, transition-mass vectors, tracer-threshold censuses, gas-follow-up denominators, and simulation target vectors--while explicitly refusing claims that require radio, X-ray, molecular/neutral gas, resolved outflow, halo/group, or simulation-mock data not analyzed here.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json:18:    "High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/METHODS_AND_SCOPE.md:23:- BPT AGN rows: 8146
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/METHODS_AND_SCOPE.md:25:- matched pairs: 8146
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/METHODS_AND_SCOPE.md:26:- median matched delta log sSFR: -1.309 dex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:100:305188175578425344,668850824549525504,0.04901973,0.04799621,11.52727,11.41945,-12.36629,-11.54585,-0.8204399999999996,0.19814671966055536
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:247:310837466758146048,853548715418347520,0.03886399,0.041528,11.03133,11.04883,-12.02262,-10.83901,-1.1836099999999998,0.10660363891008323
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:313:314185755800922112,651932094292846592,0.06885027,0.06909105,10.75399,10.74413,-10.34167,-10.79299,0.45131999999999906,0.020006438526503977
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:417:318703098904209408,831005433010350080,0.09338817,0.09326141,10.74464,10.74813,-11.78773,-10.29962,-1.488109999999999,0.00793800154660576
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:421:318723164991416320,863702155528267776,0.07458969,0.07443131,10.76302,10.77009,-12.31719,-10.63509,-1.6821000000000002,0.014102775336958352
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:462:321042034527856640,541594720841787392,0.06206989,0.06206039,10.76667,10.76381,-11.05592,-10.67958,-0.3763400000000008,0.005165279165115207
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:509:324394721533257728,815187854253647872,0.118139,0.1179329,10.80869,10.80475,-11.37714,-10.63233,-0.7448100000000011,0.010604424360158233
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:575:327809528563263488,323171790111139840,0.08174095,0.08193589,10.76318,10.76567,-11.61394,-10.17894,-1.4349999999999987,0.008697869334116195
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:710:336649597738838016,843468942117726208,0.08845632,0.08821125,10.74432,10.74646,-11.41934,-9.859128,-1.560212,0.010130397033541275
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:768:338987164006115328,300714533029177344,0.1022681,0.1023372,10.38461,10.3856,-10.76345,-10.56824,-0.19521000000000122,0.0031871965623176297
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:835:344607037696534528,318731686206531584,0.07253711,0.07479393,11.20723,11.20711,-11.23844,-11.65,0.4115599999999997,0.08626987498146921
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:873:346944324958709760,675589186123753472,0.09935354,0.09938594,10.59422,10.59259,-12.13152,-10.43786,-1.6936599999999995,0.003187060760888146
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:932:350255779153995776,624890978989271040,0.0610249,0.06109975,10.7577,10.76348,-10.3568,-10.06179,-0.29500999999999955,0.010799030955291956
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:938:351281623905363968,651932094292846592,0.06896829,0.06909105,10.75137,10.74413,-11.93956,-10.79299,-1.1465700000000005,0.013861848067527846
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:977:354667294648985600,382960757974788096,0.0952584,0.09524147,10.77719,10.77322,-10.39474,-9.695767,-0.6989730000000005,0.007181463016816966
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:992:367110754563811328,844576425355798528,0.09458435,0.09471482,10.96752,10.98449,-11.20181,-10.04129,-1.16052,0.03097681465160703
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1152:376098980834076672,437996809231558656,0.07117269,0.07138146,10.8553,10.85601,-10.97945,-10.45957,-0.5198800000000006,0.008082338069676698
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1242:379570688865888256,437996809231558656,0.07106858,0.07138146,10.86724,10.85601,-12.6809,-10.45957,-2.22133,0.023502481210538856
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1294:382832939748059136,661020652173551616,0.02691544,0.02723799,10.75211,10.72154,-11.6384,-10.74431,-0.8940900000000003,0.05643738977138704
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1433:389707081462081536,425667166604388352,0.05765377,0.058154,10.85689,10.85964,-11.55918,-10.20205,-1.3571299999999997,0.019753269996454426
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1437:389727422427195392,507814150223718400,0.04767711,0.04901946,10.90574,10.90475,-12.21905,-10.58611,-1.6329399999999996,0.0513438981463192
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1561:399739851781466112,427961016798701568,0.1137336,0.1132302,10.9842,10.98259,-10.92448,-10.37023,-0.5542500000000015,0.019460431027363792
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1779:421250147561793536,835507379041757184,0.1114782,0.1114666,10.76359,10.76034,-10.27204,-10.32486,0.05281999999999876,0.00587187778949036
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1787:422349390166910976,872700559411406848,0.1114068,0.111325,11.35476,11.33345,-10.74462,-10.80785,0.06323000000000079,0.03851864111783715
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1846:426892016568264704,407717636814694400,0.1138768,0.1132999,10.94203,10.9324,-10.82351,-9.987679,-0.8358310000000007,0.02805910906492299
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1847:427865909042898944,325485711778146304,0.0265881,0.02657746,9.975391,9.973599,-12.08138,-10.15945,-1.9219299999999997,0.0032539375987604307
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1927:433621577385404416,664385158274639872,0.03718052,0.03715232,9.810019,9.814687,-10.84858,-9.833186,-1.0153940000000006,0.008478548165465227
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1961:435873927089121280,380556121078786048,0.08778825,0.08665504,11.19137,11.19045,-11.91698,-10.28146,-1.6355200000000014,0.04334998477222717
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1967:436855516128372736,380556121078786048,0.08646432,0.08665504,11.19024,11.19045,-11.71648,-10.28146,-1.4350200000000015,0.007300306620846532
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2182:447078500382304256,459431788851259392,0.04743296,0.04779232,10.2597,10.25667,-11.81111,-10.50136,-1.3097499999999993,0.014781818943152267
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2345:458262458218342400,877208832751724544,0.05021771,0.05012466,10.7443,10.73608,-11.99177,-9.62011,-2.3716600000000003,0.015230107558280989
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2346:458264932119504896,352447380840278016,0.05380823,0.05342876,10.91763,10.92934,-12.14938,-10.33469,-1.8146900000000006,0.025602220891896874
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2504:467284775590193152,560822981463402496,0.03046692,0.03116767,10.54334,10.54362,-12.39737,-10.82357,-1.5738000000000003,0.026791743837638146
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2726:481906082441095168,672331603720038400,0.04112215,0.04207922,10.75393,10.76367,-12.15802,-12.12908,-0.02894000000000041,0.04057560812947077
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2871:488757964061042688,672331603720038400,0.04227205,0.04207922,10.76847,10.76367,-12.225,-12.12908,-0.09591999999999956,0.011362834413180744
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3023:498880892538742784,319885898269353984,0.07701694,0.07699241,10.81467,10.81797,-12.66683,-10.56905,-2.0977799999999984,0.006018682431379214
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3028:499903438520346624,843393900449130496,0.1143072,0.1150079,11.05899,11.08267,-12.30161,-11.53776,-0.7638499999999997,0.05037283009380899
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3161:504539254706169856,380556121078786048,0.087492,0.08665504,11.18528,11.19045,-12.42798,-10.28146,-2.1465200000000006,0.033321991718226814
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3310:512346886926002176,838820482370267136,0.04239265,0.04218137,10.20811,10.20989,-11.25489,-10.49182,-0.763069999999999,0.008689777567521508
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3320:513412313710094336,815214242532714496,0.03085805,0.03239601,10.64419,10.6348,-11.01833,-10.895,-0.12333000000000105,0.061175814685313565
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3330:513522814628685824,478669670216394752,0.07148712,0.07127721,10.17616,10.17616,-11.07908,-10.34068,-0.7383999999999986,0.00802405712323577
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3334:513557724122867712,811863205532952576,0.07215024,0.07246102,10.64067,10.64388,-10.89854,-10.1347,-0.7638400000000001,0.01321273714919919
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3388:518075892514187264,636162621753550848,0.1010155,0.1011402,10.31525,10.31034,-12.04412,-10.73488,-1.309239999999999,0.010048343790936935
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3429:521318901791877120,862556464328239104,0.02797847,0.02885592,10.73735,10.74413,-11.88678,-12.42908,0.5423000000000009,0.035696417757403766
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3456:522573169681262592,421248498294351872,0.09576819,0.09547753,10.47686,10.47246,-10.24555,-10.74488,0.4993300000000005,0.013648677439719162
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3498:526973965038544896,672331603720038400,0.04112945,0.04207922,10.75498,10.76367,-12.00519,-12.12908,0.12388999999999939,0.03953771794082933
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3570:533706001333905408,437996809231558656,0.07097828,0.07138146,10.86657,10.85601,-11.42438,-10.45957,-0.96481,0.02448400185057724
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3635:541575479388301312,661020652173551616,0.02746993,0.02723799,10.71868,10.72154,-10.86103,-10.74431,-0.11671999999999905,0.010254627089510722
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3650:543936680877385728,849020926182844416,0.09943593,0.09948342,10.74469,10.74431,-10.64782,-10.53257,-0.11524999999999963,0.0019401572618448254
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3726:551709953291741184,748818307301271552,0.04230468,0.04198322,10.74487,10.74014,-11.66985,-11.95724,0.28739000000000026,0.014953744021005135
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3869:557330107966973952,557355671612319744,0.1046841,0.1045914,10.75333,10.7522,-9.664137,-10.42798,0.7638429999999996,0.004086716704038426
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3976:564100904714790912,651932094292846592,0.06871629,0.06909105,10.75812,10.74413,-10.6728,-10.79299,0.12018999999999913,0.028990786241535123
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3982:564142411278739456,810789806937237504,0.08158107,0.08146018,10.37177,10.37031,-11.68105,-10.18926,-1.49179,0.005317292719772218
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4399:584366828965357568,828784964244891648,0.02557745,0.02535995,10.18438,10.18734,-10.76392,-10.93719,0.1732699999999987,0.009877399813175591
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4462:587734628735936512,421165485166454784,0.09268145,0.09257279,10.74401,10.75226,-12.31591,-10.06992,-2.245990000000001,0.015432461155322794
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4531:592240981974214656,395329159326361600,0.08231244,0.08225238,10.86392,10.86591,-10.19768,-9.784113,-0.41356700000000046,0.0042572463081465275
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4537:592286336828860416,701483230250952704,0.05081615,0.05036505,10.76392,10.75863,-12.01047,-9.96567,-2.0448000000000004,0.019702198445330724
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4633:595771783873849344,868146108629542912,0.1153621,0.1154251,10.73852,10.74137,-11.97727,-10.31387,-1.663400000000001,0.005671205241742022
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4683:600229478370666496,661020652173551616,0.02685711,0.02723799,10.72747,10.72154,-11.64143,-10.74431,-0.8971199999999993,0.018058654809192408
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4703:601329814682494976,327806779784194048,0.08926485,0.08953594,10.68021,10.67975,-11.55236,-10.69465,-0.8577100000000009,0.010395819034091421
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4727:602463411204286464,380556121078786048,0.08679624,0.08665504,11.19059,11.19045,-11.91339,-10.28146,-1.6319300000000005,0.005403426154244813
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4738:603529388146845696,550650298977249280,0.09304417,0.09329706,10.35645,10.35839,-11.94655,-10.14229,-1.804260000000001,0.010279427158511927
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4828:611389521778468864,512303456216705024,0.04481464,0.04422837,10.57115,10.58859,-12.27424,-10.1306,-2.1436400000000013,0.038593096000088256
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5107:630603217276790784,560822981463402496,0.03097543,0.03116767,10.53957,10.54362,-10.59472,-10.82357,0.22884999999999955,0.010355623160336608
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5144:635089773265971200,327665492540024832,0.08035741,0.08043308,10.74438,10.74562,-12.2092,-9.475,-2.7341999999999995,0.0036547944408332677
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5267:642949633177315328,380556121078786048,0.08676762,0.08665504,11.18917,11.19045,-12.61205,-10.28146,-2.330590000000001,0.004882400554798046
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5282:644074708500768768,475132814728128512,0.07233783,0.07194958,10.7637,10.76113,-12.32939,-10.19198,-2.137410000000001,0.015546764297361085
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5421:653188011952990208,372835086858479616,0.09580312,0.09581001,10.61188,10.61022,-11.00316,-9.623291,-1.3798689999999993,0.0030021857738146834
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5468:655395551004616704,328802382211213312,0.08225836,0.08250629,10.74404,10.74084,-10.5801,-10.13711,-0.44299,0.011093106859754329
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5625:664380760228128768,831005433010350080,0.0931543,0.09326141,10.74442,10.74813,-11.75924,-10.29962,-1.4596199999999993,0.007838226958014413
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5656:665495389553584128,444814605756164096,0.1094802,0.1093835,10.98843,10.98383,-12.38023,-10.21764,-2.16259,0.009074257430938875
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5861:680090032979077120,560822981463402496,0.03100145,0.03116767,10.54021,10.54362,-12.14286,-10.82357,-1.3192900000000005,0.008838192838282901
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:5992:691313595580966912,437996809231558656,0.07059561,0.07138146,10.85842,10.85601,-12.25407,-10.45957,-1.794500000000001,0.030352187477424145
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:6241:703751249438205952,386267259317807104,0.05710424,0.05442572,11.38146,11.26721,-12.76988,-12.4255,-0.344380000000001,0.22989014696721702
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:6259:704846636420982784,560822981463402496,0.03104844,0.03116767,10.54457,10.54362,-11.3475,-10.82357,-0.52393,0.004868460441436257
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:6282:706050603113015296,407717636814694400,0.1132667,0.1132999,10.94447,10.9324,-12.22243,-9.987679,-2.2347509999999993,0.021781984499591015
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:6374:711691096538769408,624890978989271040,0.06126045,0.06109975,10.76464,10.76348,-12.23316,-10.06179,-2.1713699999999996,0.006488694909592607
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:6638:733080172286208000,316469435244242944,0.06990718,0.07005271,10.16512,10.16594,-10.94969,-10.18591,-0.7637800000000006,0.005755864285509106
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:6744:739821003802175488,612600911801378816,0.09707759,0.09708965,10.63953,10.63997,-11.03017,-10.28557,-0.7446000000000002,0.0009169997975513729
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:6785:742089021781469184,810676557239576576,0.06835963,0.06873026,10.48155,10.47468,-11.99764,-10.83064,-1.1669999999999998,0.018812520733504694
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:6859:746607463909844992,839986239238072320,0.04212121,0.04199245,10.47516,10.4784,-11.78146,-10.10439,-1.6770699999999987,0.0076352990520875096
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7101:807408538199549952,380556121078786048,0.08615456,0.08665504,11.18188,11.19045,-12.6656,-10.28146,-2.3841400000000004,0.024584331756933475
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7167:811842314812024832,532702146026563584,0.05664973,0.05709619,10.74444,10.75521,-11.82321,-9.863687,-1.959522999999999,0.02584062702320096
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7184:811932474765502464,378412078521673728,0.08221833,0.08229963,10.85344,10.84856,-12.03963,-9.960556,-2.0790740000000003,0.009324799458146401
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7285:817478136504543232,567579760864028672,0.09864715,0.0984591,10.72283,10.726,-10.74493,-10.18143,-0.5634999999999994,0.009180899644817291
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7327:821981465280538624,843360640222390272,0.04657033,0.04640814,10.59509,10.59071,-12.30318,-10.67106,-1.6321199999999987,0.010035184174526198
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7408:828673363814672384,664393129733941248,0.07962948,0.07950005,10.28286,10.28594,-9.965397,-10.06872,0.10332300000000139,0.007434282240743239
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7417:828773969128613888,308671154040629248,0.09937443,0.09914839,10.73513,10.72994,-10.90055,-10.13745,-0.7631000000000014,0.01273131093631366
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7427:829835827465971712,379599001290303488,0.1186557,0.1187088,10.74471,10.74597,-10.55029,-9.903836,-0.6464540000000003,0.003045151038565374
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7433:829910044500846592,437996809231558656,0.07168929,0.07138146,10.86739,10.85601,-12.067,-10.45957,-1.6074300000000008,0.02363882205107382
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7458:832143977284134912,831088171260340224,0.03665775,0.03762546,10.76396,10.7593,-12.15,-9.790215,-2.3597850000000005,0.03793255707727841
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7538:838822681393522688,672331603720038400,0.0425145,0.04207922,10.77571,10.76367,-12.87111,-12.12908,-0.7420299999999997,0.027337812097577602
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7648:844562681460451328,738761074106460160,0.1198257,0.1197765,10.8004,10.79358,-10.97074,-9.993653,-0.9770869999999992,0.012429833150443645
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7660:845586327054346240,380556121078786048,0.0859194,0.08665504,11.18639,11.19045,-11.85158,-10.28146,-1.570120000000001,0.029056399061800516
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:7693:846848841280940032,529174088090937344,0.07805469,0.07799067,10.76458,10.76393,-10.89013,-10.67939,-0.21073999999999948,0.0027129829194831485
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:8062:872577414109095936,706077541147895808,0.05007601,0.04938756,10.93036,10.93768,-10.95044,-10.20546,-0.74498,0.029436118655926928
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:28:    "The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.tex:20:We execute a bounded pilot version of a proposed galaxy-evolution study: whether optically selected active galactic nucleus (AGN) hosts show a star-formation deficit relative to matched inactive emission-line galaxies.  Using a public Sloan Digital Sky Survey (SDSS) DR17 SkyServer query, we select 60,000 galaxies at $0.02<z<0.12$ with signal-to-noise ratio $\geq 3$ in H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$, plus finite MPA/JHU-style stellar-mass and specific-star-formation-rate estimates.  Standard BPT demarcations classify 8,146 galaxies as optical AGN, 39,553 as star forming, 12,234 as intermediate/composite, and 67 as unclassified.  Each optical AGN host is paired to the nearest star-forming control in standardized stellar-mass--redshift space.  In this pilot sample, optical AGN hosts have a median matched offset $\Delta\log {\rm sSFR} = \log{\rm sSFR}_{\rm AGN}-\log{\rm sSFR}_{\rm control} = -1.31$ dex, with a bootstrap 95\% interval of $[-1.33,-1.28]$ dex.  A simple linear model adjusted for stellar mass and redshift gives an AGN coefficient of $-1.20\pm 0.01$ dex.  The result demonstrates a reproducible survey-analysis path from the proposal to a measurable quantity, but it should not be read as causal evidence for AGN feedback: optical selection, aperture effects, star-formation estimator assumptions, morphology, halo environment, and AGN duty-cycle timing remain uncontrolled.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.tex:33:The selection requires spectroscopic class \texttt{GALAXY}, $0.02<z<0.12$, positive H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ fluxes, and signal-to-noise ratio $\geq3$ in all four lines.  We also require $8.0 < \log(M_\star/M_\odot) < 12.5$ and $-14 < \log({\rm sSFR}/{\rm yr}^{-1}) < -7$ in the catalog median estimates.  The query returns 60,000 rows; all satisfy the analysis cuts after finite-value filtering.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.tex:56:Figure~\ref{fig:bpt} shows the BPT classification.  The finite analysis sample contains 39,553 star-forming galaxies, 12,234 intermediate objects, 8,146 optical AGN, and 67 unclassified sources.  The optical AGN population is redder and more massive than the star-forming population before matching: the median optical AGN host has $z=0.076$, $\log M_\star=10.79$, $\log{\rm sSFR}=-11.77$, and $u-r=2.76$, while the star-forming sample has median $z=0.069$, $\log M_\star=10.02$, $\log{\rm sSFR}=-9.91$, and $u-r=1.81$.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.tex:82:Optical AGN & 8,146 & 0.076 & 10.79 & -11.77 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.tex:96:\item A reproducible emission-line sample of 60,000 galaxies was built from public SDSS spectroscopy, photometry, and derived stellar-mass/sSFR quantities.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.tex:97:\item BPT cuts classify 8,146 objects as optical AGN and 39,553 as star-forming controls.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p1_outflow_escape_recycling/analysis_results.json:18:    "High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json:11:    "agn": 8146,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json:30:      "n": 8146,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json:44:  "matched_pairs": 8146,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_aas.tex:18:The input table is the SDSS DR17 emission-line sample from run SDSS-AGN-SFR-PILOT-20260708T122000Z.  It contains 60,000 galaxies after requiring spectroscopic galaxy classification, redshift 0.02--0.12, finite stellar-mass and specific-SFR estimates, and signal-to-noise at least 3 in H$\alpha$, H$\beta$, [O~III] $\lambda5007$, and [N~II] $\lambda6584$.  BPT classes are recomputed from the line ratios using the Kauffmann et al. and Kewley et al. demarcations.  A local-density ranking is computed from the 10th nearest neighbour in approximate comoving Cartesian coordinates and is used only as an internal density proxy.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_aas.tex:22:\item High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex:35:four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex:36:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex:35:four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex:36:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex:56:\item The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex:35:four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex:36:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex:56:\item High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex:35:four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex:36:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_REVIEW_RESPONSE.md:4:- In [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex), I streamlined the abstract so the 60,000-row cap is described once as a capped subset, not repeatedly as a "pilot sample".
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex:35:four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex:36:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_24_ACTUAL_RESEARCH_RESPONSE.md:4:- Updated the flagship abstract and conclusion to state the association-only boundary more explicitly, including the non-random 60,000-galaxy cap and the lack of morphology, structure, and aperture-fraction controls.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_24_ACTUAL_RESEARCH_RESPONSE.md:15:- The manuscript text still preserves the required core invariants: 8,146 pairs, -1.309 dex, [-1.334,-1.283], 60,000 cached rows, 249,917 strict parent, and 24.0% coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_REVIEW_RESPONSE.md:5:- Clarified in both TeX files that the 60,000-row cache is a computational, non-random pilot cap rather than a physical selection threshold.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_REVIEW_RESPONSE.md:13:- I did not alter the 8,146 pair count, the -1.309 dex and -0.763 dex offsets, the [-1.334,-1.283] interval, the 60,000 cached rows, the 249,917 strict parent count, or the 24.0% coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_aas.tex:18:The input table is the SDSS DR17 emission-line sample from run SDSS-AGN-SFR-PILOT-20260708T122000Z.  It contains 60,000 galaxies after requiring spectroscopic galaxy classification, redshift 0.02--0.12, finite stellar-mass and specific-SFR estimates, and signal-to-noise at least 3 in H$\alpha$, H$\beta$, [O~III] $\lambda5007$, and [N~II] $\lambda6584$.  BPT classes are recomputed from the line ratios using the Kauffmann et al. and Kewley et al. demarcations.  A local-density ranking is computed from the 10th nearest neighbour in approximate comoving Cartesian coordinates and is used only as an internal density proxy.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_RESPONSE.md:4:- Updated [`flagship_rp1/aastex/rp1_flagship_polished.tex`](./flagship_rp1/aastex/rp1_flagship_polished.tex) to state more explicitly that the `-1.309 dex` sSFR offset cannot be disentangled from a morphology or bulge-fraction effect because structural proxies such as concentration index and `fracDeV` were not retained in the cache.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_RESPONSE.md:12:- I did not change any numeric invariants, including `8,146`, `-1.309 dex`, `[-1.334,-1.283]`, `60,000`, `249,917`, or `24.0%`.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2:299489677444933632,0.02122228,146.7142,-1.041304,3,10.29471,-0.5273424,-10.87671,17.15123,15.49701,14.67864,472.5904,10.04917,119.4956,6.650275,68.39606,6.610639,224.1136,8.453454
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:24:299528160351905792,0.05290708,146.3738,-0.3683868,3,11.09292,0.1309832,-10.97797,19.39033,17.22124,16.25918,737.1107,8.049224,149.5079,4.917249,95.27357,4.747185,407.2752,6.169335
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:33:299532558398416896,0.021758,146.3009,0.03547963,1,9.370238,-0.2561884,-9.67175,17.80842,16.67454,16.06488,2292.528,16.9811,638.0527,8.117599,780.1143,9.821332,465.8451,5.742815
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:102:299638661270497280,0.0200758,146.8068,0.6656352,3,9.863219,-0.6832175,-10.57909,17.34683,15.63673,14.6184,853.0652,10.24324,156.3904,5.302642,70.22443,5.325087,515.1613,8.314297
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:284:300766484953589760,0.03460572,148.643,0.6917834,1,8.854539,-0.7284839,-9.639919,19.35935,18.31045,17.89483,30.74401,1.404338,12.34943,1.697297,15.28888,1.80099,5.731369,1.06876
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:345:301762917785692160,0.08995679,150.3354,-0.1828773,5,10.96092,-0.8050386,-11.79124,19.03924,17.2045,16.2881,161.2923,5.90004,40.63863,4.197399,21.24576,4.565125,110.7447,5.346798
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:365:301781884361271296,0.08827484,150.1844,-0.03102159,3,10.50967,-0.1608541,-10.71244,20.34405,18.67566,17.75258,146.5363,2.762363,23.97026,2.063216,35.55265,2.400281,85.52791,2.384567
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:494:301886063088003072,0.05667516,149.716,1.16211,5,10.66669,-1.380255,-12.10802,18.55428,16.7459,15.88485,59.41175,5.087317,18.81611,3.814679,26.18031,4.179987,49.42261,4.870375
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:527:301911076977534976,0.03256777,150.1405,0.85608,1,9.16299,-0.3923685,-9.613316,18.21564,17.08146,16.73425,235.5378,3.075078,74.14877,2.481694,59.46356,2.410907,52.97992,1.73406
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:551:302882500147963904,0.03225636,151.4464,-1.18057,1,9.119048,-0.342147,-9.527263,18.22088,17.27114,16.90005,545.075,6.08659,152.6431,3.758352,163.6821,4.067122,114.4559,2.563276
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:715:304027366613608448,0.09686861,153.1661,-1.106351,3,11.25404,0.581752,-10.74412,19.32251,17.55657,16.52177,354.96,5.899241,51.71258,3.63146,47.55017,3.605553,199.2943,4.717848
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:1144:306391866906011648,0.02161491,156.4256,0.7630448,1,10.04825,0.2283809,-9.863538,15.9949,14.74302,14.20571,2028.662,16.72582,441.7184,6.854961,371.3156,7.47776,797.3146,8.798363
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:1285:307490554168502272,0.1096851,157.5458,0.01049055,1,10.51504,1.062644,-9.506054,19.47074,18.17282,17.49238,890.5579,9.045177,170.7632,4.165943,54.1951,3.492877,372.3336,5.007252
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:1436:308581543842965504,0.08239438,159.2419,-0.6447772,1,10.61739,0.7444607,-9.916896,19.04746,17.67665,16.89921,315.873,3.124143,60.42138,2.087081,11.999,1.817774,155.1218,2.276958
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:1535:309627454228555776,0.05616885,162.2842,-1.052108,1,9.752226,0.2359551,-9.583333,18.15765,17.03508,16.64332,114.2385,1.832337,31.78441,1.752717,12.80361,1.684937,35.05289,1.469227
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:1775:310799258729080832,0.02149814,163.1155,-0.6067328,1,8.576334,-1.009909,-9.64039,19.21814,18.12746,17.6847,419.37,3.730681,108.6634,2.217705,265.1246,3.795955,48.37356,1.530294
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:1793:310814651891869696,0.1092024,162.8897,-1.246688,2,10.67136,-1.512257,-12.25833,21.09566,18.83887,17.84115,54.7962,5.380339,15.56086,3.740117,18.81481,2.909529,20.00836,3.1704
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:1799:310817675548846080,0.0823582,162.9444,-0.9200227,1,10.04354,0.2237165,-9.877825,19.04675,17.8448,17.28803,106.2218,1.973549,23.37895,1.643194,16.43402,1.687527,35.50032,1.408146
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:1806:310822073595357184,0.06314798,162.496,-0.6545601,1,9.814636,0.08070177,-9.78434,18.92344,17.77052,17.26542,392.1307,3.803732,103.2082,2.292815,38.04576,2.021518,158.1926,2.277256
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:1823:310837466758146048,0.03886399,162.4594,1.204653,4,11.03133,-0.9501078,-12.02262,16.88659,14.91878,14.08931,88.18241,4.364748,27.23517,3.186493,35.26771,3.552368,83.95886,4.321998
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2051:312019441741228032,0.09574383,165.9007,0.7697915,4,10.81246,-0.283599,-11.14643,19.27056,17.57314,16.65879,90.90263,4.43138,21.49492,3.680382,31.62049,4.229942,114.6052,4.487479
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2058:312026588566808576,0.04955553,166.0898,0.1996974,1,9.776976,-0.2512524,-10.07149,20.05268,18.56241,17.81462,196.3095,3.173245,39.66076,2.064419,19.78969,1.905739,71.98965,2.161101
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2157:313107408362694656,0.03907105,166.9552,0.7443973,3,10.40812,-0.2565342,-10.72661,18.84987,17.08325,16.20378,97.31052,2.613556,19.27301,1.927467,10.65868,2.177532,49.64413,2.485523
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2180:313130223228971008,0.03854868,167.285,0.7072945,1,10.64478,0.6588923,-10.036,17.07377,15.54805,14.8146,740.9831,8.290664,120.7856,3.863946,22.06023,3.474789,322.1586,5.692175
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2226:314129680707905536,0.1061499,169.8568,-1.07489,1,9.587908,0.2586432,-9.385729,20.05926,18.87492,18.50844,238.9999,3.081889,66.19807,2.364156,78.21207,2.707642,49.01275,2.381465
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2455:315287460210829312,0.07401707,170.475,-0.9381466,2,11.00699,0.2647449,-10.78699,18.36688,16.67468,15.83401,277.0449,5.656233,49.62381,3.84795,14.21749,3.90062,99.84331,4.614012
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2604:315402084298024960,0.1000844,171.0775,0.7443563,1,9.914332,0.3099831,-9.661704,19.08006,18.1045,17.69537,530.6656,4.844416,155.557,2.687537,137.9082,2.839427,129.6081,2.49258
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2634:316383123581462528,0.1050031,172.6083,-0.8328589,3,10.40284,-0.01609076,-10.46988,19.61176,18.13866,17.42521,89.51517,2.336153,19.49509,1.780229,23.82891,2.028937,43.3447,2.736541
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2708:316464762319824896,0.06859364,170.7635,0.05741816,4,11.47928,-1.206569,-12.71963,17.90964,15.77263,14.80698,116.997,5.947316,37.48052,4.094765,64.92342,4.299127,133.2947,5.483058
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2864:317588463941609472,0.07702655,172.7941,-0.7631814,1,10.06154,0.2709739,-9.846894,19.06532,17.79982,17.25984,195.0654,2.526154,43.38261,1.725441,10.50216,1.530879,71.39112,1.68148
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2908:317661581464856576,0.09762309,174.5012,0.9181455,1,10.15364,0.4206276,-9.782073,19.10633,17.95438,17.43495,247.0786,2.856415,56.91674,1.877239,10.72029,1.519765,72.21176,1.741005
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:2986:318703098904209408,0.09338817,175.4477,-0.7746503,5,10.74464,-1.002816,-11.78773,19.64268,17.88965,16.96441,21.45923,1.997552,6.418715,1.774586,8.711115,2.495779,19.54866,2.37942
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3003:318723164991416320,0.07458969,175.1169,1.00644,-1,10.76302,-1.499885,-12.31719,19.35437,17.48447,16.56363,13.40758,3.3903,15.46492,3.575856,12.88259,4.248824,19.23313,4.185139
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3337:321032138923206656,0.1080858,180.2166,-0.07065564,3,10.46141,-0.4033145,-10.91178,20.31031,18.65093,17.76542,43.43808,3.149659,10.76345,1.55504,10.76294,1.636219,27.61245,1.813192
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3535:323173989134395392,0.07883006,183.5178,-0.7449945,1,9.558855,0.2931679,-9.32,18.68697,17.80209,17.54298,444.6528,3.269917,134.2646,2.235841,184.6485,2.614982,81.40825,1.400412
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3565:323216320332064768,0.07945877,182.4975,-0.8969609,5,10.94198,-1.00941,-11.9933,18.69212,16.85308,15.96914,50.74466,3.401253,11.84389,2.819796,12.37161,2.773142,42.717,3.059717
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3632:323279267372754944,0.09581669,183.4162,0.763227,1,10.09245,0.2326988,-9.918661,19.34494,18.20905,17.66333,327.3324,3.111798,83.58546,2.31905,35.77294,2.168898,112.8974,2.072582
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3650:323296859558799360,0.07179181,184.25,-0.05160811,1,10.07277,0.04651959,-10.08022,19.33797,18.09132,17.44054,255.0717,2.672636,60.77284,1.953792,13.81462,1.723609,93.11658,1.897913
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3690:324298514265827328,0.07273933,185.1205,-0.6881465,5,10.6663,-1.569679,-12.31033,19.40874,17.55519,16.63888,25.69945,2.718315,8.62144,2.423227,17.59427,3.221483,28.57173,3.187667
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3720:324334523271636992,0.07134468,184.142,-0.2014198,5,10.62563,-0.4300559,-11.10811,18.65327,16.98146,16.20449,57.21043,3.275443,14.73844,2.632325,19.86945,3.206626,54.03826,3.613589
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3734:324350741068146688,0.07556944,184.4066,1.240283,1,9.874903,0.1464374,-9.785832,18.89739,17.74959,17.30016,75.22549,1.789681,20.50386,1.816081,8.131487,1.582148,22.45761,1.331935
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3752:324369157887911936,0.04050813,183.9735,0.08161584,1,8.906006,-0.1848262,-9.144288,18.67249,17.71375,17.49362,435.6,3.898442,114.4411,2.316548,355.4637,4.16187,35.28786,1.256514
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3790:324403792504186880,0.08504529,185.0934,0.9699958,1,9.892371,0.3370672,-9.599386,18.73447,17.71735,17.34468,375.2189,3.956382,106.1904,2.569417,57.22667,2.254602,114.5368,2.049705
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3865:325454925452568576,0.0486598,186.4777,-1.133399,1,9.018315,-0.3549019,-9.435349,19.15625,18.08972,17.7972,114.5254,2.384025,34.45473,1.991446,51.24951,2.428987,13.63699,1.45749
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3879:325485711778146304,0.02657746,186.0493,1.213017,2,9.973599,-0.1286026,-10.15945,16.80723,15.53628,14.99383,70.40808,2.081279,23.03306,2.095464,8.335167,2.126575,27.45729,1.752756
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3893:325506327621167104,0.1082719,186.6315,0.9860818,5,11.16746,-1.003478,-12.22473,19.53869,17.57029,16.59427,64.0707,6.106242,11.70492,2.814626,14.13194,3.192764,70.82928,3.719712
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:3958:326539592851286016,0.08146943,189.6414,-0.5518563,1,10.21386,0.4395315,-9.823917,18.47582,17.29695,16.71785,298.4251,3.5967,67.1312,2.58963,12.09298,2.123263,126.5772,2.468488
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4123:327696553743509504,0.04762306,190.6508,-0.7444674,1,9.718091,-0.2229804,-9.993506,18.61364,17.46428,16.93722,73.47366,2.004808,21.62228,1.54062,14.98362,1.555929,17.79574,1.304845
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4167:327749880057456640,0.08152342,190.5751,0.8672818,1,10.0086,0.4470311,-9.616881,18.5571,17.51826,17.06336,250.087,2.790056,60.18394,2.044291,26.81464,1.890399,87.55962,1.781168
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4193:327767472243501056,0.04581346,190.7384,0.4972424,1,10.15381,-0.2930018,-10.49357,18.6211,17.20407,16.45369,339.6425,3.949072,87.68684,2.378345,32.08146,2.056466,155.3672,2.771653
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4244:327799907836520448,0.08896293,191.7445,0.1163429,3,11.06134,0.3515386,-10.77944,18.23957,16.68146,15.84209,89.32201,2.727301,22.0507,2.155732,16.8487,2.269247,59.94487,2.603654
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4258:327809528563263488,0.08174095,192.0509,0.3127653,5,10.76318,-0.7772473,-11.61394,19.26081,17.43837,16.55046,37.59949,2.504638,7.149846,2.138725,13.22936,2.255802,42.94404,2.362394
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4394:328903537280968704,0.08132457,192.5794,0.1961001,4,10.69197,-0.3748389,-11.13849,19.69732,17.85671,16.92752,134.2874,3.365519,21.51901,2.546236,100.3054,3.223757,160.7443,3.202578
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4471:331068207123163136,0.09438194,196.8038,-0.08114844,3,10.37687,-0.2581468,-10.6864,19.70383,18.19292,17.42007,79.37133,2.412282,23.89431,1.921793,12.86585,2.127406,51.26819,2.268325
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4490:331084974675486720,0.08378702,196.1267,-0.7392073,3,10.81465,0.02760744,-10.83555,20.82817,17.64463,16.66076,269.6509,5.015788,56.78355,3.158159,33.62905,3.335777,161.2279,4.252883
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4560:331166338535942144,0.08025688,197.4372,0.3106023,5,10.39103,-0.7634315,-11.20303,19.78216,18.01185,17.18936,57.11413,2.88932,9.340191,2.379118,10.30354,2.795394,44.97574,2.842338
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4657:332225168216713216,0.08182288,197.2377,-0.7442754,1,9.835608,0.07972224,-9.818688,19.29044,18.00238,17.50918,77.84228,1.901797,20.37921,1.911353,12.00642,1.811377,21.41202,1.405485
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4658:332225717972527104,0.08453557,197.2911,-0.6140063,1,10.12865,0.4110861,-9.766302,19.60258,18.22023,17.58619,335.3088,3.566403,67.41512,2.60991,36.4722,2.556558,146.3112,2.544745
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4776:333288121066088448,0.07909299,200.7637,-0.1852464,1,10.04425,0.3688506,-9.729426,18.56202,17.385,16.95685,260.523,3.556762,76.44511,2.5998,75.54945,2.708001,50.85499,1.790025
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4792:333301590083528704,0.07313969,199.984,-1.153937,1,10.14627,0.1176068,-10.08223,18.95441,17.77113,17.15055,243.9434,4.031869,60.18497,3.399159,20.08146,3.155339,95.95187,2.890542
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4848:333355191275382784,0.07291679,199.2785,0.7872083,5,10.76337,0.1818783,-10.63561,18.48686,16.90286,16.12362,52.83646,2.365077,10.61318,2.102894,11.72925,2.420879,35.67607,2.391135
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:4897:333405219054446592,0.04799633,200.512,0.6532387,1,9.585303,-0.03932138,-9.689473,18.31516,17.21592,16.8202,114.8769,2.661676,37.65556,2.368932,18.60484,2.295668,45.47055,2.108009
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5060:334514350989535232,0.08339652,201.6811,1.137691,5,11.24137,-1.372285,-12.65328,18.7994,16.68962,15.70544,36.02884,4.526877,20.19678,4.025494,14.32544,3.957803,30.76307,4.338429
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5062:334516550012790784,0.0842166,201.6567,1.128491,3,10.41307,-0.02882241,-10.49617,19.54207,18.08427,17.2957,239.0484,4.080785,55.04045,2.905876,78.75027,3.393458,146.1485,3.418928
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5176:335599019143227392,0.1027568,202.6322,-0.734216,5,10.9852,0.2081468,-10.82083,18.76121,17.17069,16.30593,45.84672,5.119117,8.091022,2.277189,40.66413,2.818987,37.99324,2.330722
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5177:335599568899041280,0.08708939,202.6486,-0.7016835,4,10.54218,0.1310879,-10.46021,19.09383,17.5853,16.84627,31.17885,1.735429,10.57841,1.812157,30.74484,2.15109,35.88906,1.622723
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5232:335657843015313408,0.0826788,203.8146,0.3679126,1,9.827127,-0.00377602,-9.880307,19.42827,18.31112,17.80166,117.5392,1.967492,32.83185,1.940606,16.77839,2.006738,33.8218,1.456847
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5270:336649597738838016,0.08845632,206.3704,-0.7982918,5,10.74432,-0.6287056,-11.41934,19.15242,17.42991,16.57173,39.10942,2.500033,11.12551,2.358975,13.65151,2.445516,32.76258,2.314249
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5335:336714743802783744,0.08846776,205.2861,-0.744854,1,10.36605,0.3975505,-10.02594,18.7144,17.39182,16.83607,125.9156,2.15568,33.27121,1.699907,8.642968,1.659427,40.41351,1.663486
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5597:338953903779375104,0.06943162,209.2658,-0.8146596,2,10.2412,-0.1931854,-10.49181,19.74604,18.13457,17.35879,106.3231,2.504904,25.50554,1.989424,9.559011,2.059029,48.29049,2.139624
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5618:338987164006115328,0.1022681,208.4189,0.621407,4,10.38461,-0.312096,-10.76345,19.79601,18.22808,17.44545,108.9757,3.704965,25.39838,2.864423,168.3557,4.257154,130.9165,3.397553
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5641:339030319837505536,0.03319905,209.6799,0.3195585,1,10.10109,0.02422258,-10.11744,17.88737,16.53541,15.85198,1460.65,11.81524,321.0733,5.11275,111.0852,4.247958,676.6927,7.14916
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5702:340050937244575744,0.05368676,212.6099,-0.5885592,1,9.621859,-0.1946681,-9.873244,19.07918,17.90726,17.40428,146.9291,2.699636,37.53531,2.177832,34.94231,2.257905,32.01292,1.734203
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5807:340157864750376960,0.08538663,211.994,0.02440769,1,10.32496,0.51438,-9.862745,18.49655,17.21605,16.69724,441.3972,4.284714,110.2622,2.621734,46.76633,2.339948,146.9065,2.430482
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:5869:341207347374352384,0.1160944,213.3934,-0.8797737,5,10.73925,-0.6657178,-11.47793,24.63741,22.18093,17.16104,140.7445,4.670975,31.97963,2.759501,13.49801,3.011193,94.11348,4.9125
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6057:342448146145634304,0.03595384,215.5132,0.8620778,1,9.542488,-0.08333317,-9.692021,17.70315,16.60741,16.17405,164.135,2.479153,50.90699,2.133532,35.77982,2.077022,47.96521,1.625952
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6113:343455023985879040,0.07895102,216.234,-0.3760499,3,10.32085,0.7630536,-9.60228,17.6484,17.08707,16.7639,2322.275,15.79734,645.6293,6.900238,371.7676,5.635554,1334.764,8.550327
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6157:343522643950987264,0.05541833,216.4862,0.6129311,5,11.12195,-0.5725861,-11.73028,17.8263,15.94364,15.01791,70.85098,5.543643,18.52819,3.674779,13.6226,4.281462,59.80103,6.139319
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6478:346850866470348800,0.0449921,220.736,-0.8108983,1,9.284286,-0.8660714,-10.2168,18.86021,17.68553,17.28192,114.0256,2.157806,37.52702,1.838121,30.08203,1.81302,29.25488,1.476917
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6585:347948459522811904,0.08326733,223.8144,-0.5421847,2,10.76377,0.2872197,-10.53632,18.94405,17.44761,16.60739,128.0937,2.342325,27.87214,1.946455,5.404611,1.791086,46.65741,1.944976
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6685:348057311173961728,0.03495155,224.1224,1.163401,-1,10.63723,-1.110254,-11.77414,17.47261,15.65798,14.84389,19.9985,2.81461,8.631517,2.49242,13.1793,2.964061,25.50771,3.173245
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6771:349120538850912256,0.0280654,225.1093,0.7443174,1,8.921501,-0.7842316,-9.76717,18.9251,17.81131,17.37154,58.98971,1.601043,21.18112,1.706039,21.73188,1.960863,8.179016,1.053252
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6851:350187609433073664,0.05309742,228.0206,0.02130507,4,10.36238,-0.2800509,-10.6928,19.07674,17.45717,16.63235,217.9479,4.484406,51.35948,3.451231,357.8146,5.798313,158.3539,3.828868
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6864:350206576008652800,0.07188617,227.7052,-0.1281462,2,9.772913,0.08408286,-9.750167,19.37158,18.08418,17.55601,39.27647,1.618719,8.658297,1.626298,5.439485,1.539658,12.35606,1.267835
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:6940:350284091578411008,0.1183296,227.7828,0.6118146,2,10.90485,-1.463966,-12.43538,20.23863,18.21524,17.19732,33.74141,5.770067,15.81228,4.14716,14.64709,3.706244,19.82855,4.323866
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7045:351364362155354112,0.09987765,228.8177,-0.2405145,2,10.30996,0.07665022,-10.28402,19.93468,18.5587,17.81568,146.4835,2.579099,36.85918,2.194658,7.367036,2.164165,61.00072,5.008775
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7185:352471020340275200,0.1106239,230.8146,0.03880824,1,10.65708,0.5562502,-10.14436,19.6149,17.93869,17.20927,188.1728,3.889759,45.59478,2.421672,13.85694,2.389976,66.82095,3.372032
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7193:352481465700739072,0.09085951,230.746,-0.5630765,3,10.80929,0.05862906,-10.79496,19.45569,17.75253,16.81474,56.43748,2.396787,14.63324,2.078128,16.21669,3.012372,34.34331,2.40141
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7246:352546886642591744,0.07723882,231.4837,0.5636799,5,10.92493,0.03622461,-10.95673,19.23488,17.33521,16.38146,87.03328,3.488091,14.22344,3.202095,18.7773,3.463292,55.5331,3.449916
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7248:352547711276312576,0.05086304,231.7491,0.7447495,1,9.840222,-0.07858359,-9.972631,18.73988,17.61889,17.08677,323.6558,3.825939,79.63284,2.726381,26.73452,2.246068,126.1626,2.562056
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7287:354673616840845312,0.05655788,235.1754,-0.7638435,2,10.38052,-1.203665,-11.64911,19.57001,17.69873,16.76399,25.75843,3.76521,12.90617,4.00534,19.48485,3.979328,12.61413,3.078284
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7446:367172602092873728,0.04587778,171.6383,-1.636269,3,10.5607,-0.7443264,-11.36043,18.12324,16.425,15.60429,226.1669,5.646115,53.71753,3.814461,23.77215,3.787956,115.0613,4.76271
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7467:367201464273102848,0.1096643,172.4246,-1.425602,2,10.35659,0.5383563,-9.870209,19.0271,17.82631,17.27368,163.4334,3.484778,43.06551,2.281461,6.988067,2.083148,55.04513,2.433087
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7672:369316648206755840,0.05169177,176.3766,-2.622733,1,9.715967,0.3767315,-9.393438,17.88196,16.80944,16.48146,1592.957,9.358794,416.1226,3.921684,749.3721,5.889852,266.2653,3.082014
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7700:369337538927683584,0.05319243,175.6351,-2.506601,3,10.43598,-0.1343308,-10.62454,18.21399,16.59717,15.81722,114.5082,2.595939,26.27464,1.785827,25.75151,2.022613,69.64757,2.192227
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7832:369450788625344512,0.1076033,175.9976,-1.711499,3,10.91184,-0.1237198,-11.08374,19.45303,17.61406,16.69386,71.67233,2.802282,14.31455,1.815505,11.67011,2.118146,47.12323,2.767148
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7907:370484875519617024,0.09564467,176.7203,-2.578151,1,10.40545,0.5798333,-9.879346,19.63596,18.24617,17.51865,258.1288,3.846849,52.51144,2.549274,15.48942,2.596392,114.8363,2.786068
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7970:370550846217283584,0.1013586,176.6383,-1.997936,1,10.51172,0.5814693,-9.97395,19.49323,17.75912,17.07585,159.8233,3.157136,30.26943,2.188956,11.40722,2.289839,70.79922,2.866984
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:7982:370566239380072448,0.09444396,176.9599,-1.619814,2,10.76361,-0.8903056,-11.72112,19.60839,17.73272,16.83822,93.52549,3.064221,13.7874,2.587128,12.71036,2.608632,46.89248,2.548569
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:8149:372714965213145088,0.08146095,180.62,-2.755332,1,10.09582,0.4334648,-9.706082,18.93514,17.70886,17.19719,219.3305,3.223198,53.77706,2.423825,30.85129,2.289546,77.9107,2.126788
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:8492:375079464045930496,0.1164402,185.2845,-1.517237,1,10.74452,0.5227833,-10.28189,19.20831,17.84409,17.07489,144.729,3.704149,32.41516,2.151801,13.69756,2.409222,59.92727,3.075623
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:8588:376151207636396032,0.06249416,186.6957,-1.315019,1,10.22375,0.7631433,-9.522762,19.39511,17.89421,17.18745,596.4304,5.771415,96.84756,2.880443,25.99126,2.44946,221.0791,3.268561
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:8743:377313941300209664,0.06403038,190.024,-2.008993,1,10.53542,0.2329883,-10.3668,18.90949,17.30947,16.56088,146.5793,3.196207,27.68118,2.234289,17.04314,2.464753,59.7734,2.621905
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:8971:379494547685664768,0.07032359,192.3324,-3.315859,1,9.571912,0.03229677,-9.601378,18.92861,18.05721,17.71771,328.9196,4.083592,114.3332,2.883265,112.8279,3.035195,77.48653,2.063289
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9017:379545125220542464,0.08146244,192.7304,-1.932408,3,9.967473,0.338421,-9.690244,18.85612,18.20492,17.84895,1019.155,9.200056,269.0923,5.272862,871.2556,9.597457,303.066,4.013529
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9066:380556121078786048,0.08665504,195.3195,-3.473248,1,11.19045,0.9584161,-10.28146,19.63048,17.74686,16.75116,318.9206,4.048131,48.38624,2.944779,14.79167,3.088065,144.2458,3.040246
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9138:380639409084590080,0.08615244,193.3474,-2.420309,3,10.76392,-1.516508,-12.32217,19.57137,17.59178,16.69267,55.13962,3.182775,20.73674,3.064055,26.41184,3.4799,34.35596,2.985853
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9173:380681465404352512,0.08631442,194.5193,-2.252376,3,10.82385,0.4503759,-10.40365,19.07648,17.5337,16.72469,224.7202,3.469773,42.59101,2.706117,33.70759,2.946145,137.7018,3.112199
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9228:381702361917188096,0.0764561,196.1818,-3.451541,1,10.08973,0.5344446,-9.606107,18.09797,16.98935,16.60093,509.0274,4.947786,152.4977,3.268146,79.47032,2.950728,158.1552,2.584027
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9280:381759811399739392,0.08641947,195.3171,-3.474768,4,10.77722,0.7424278,-10.07816,17.74916,16.61869,16.04087,1632.675,11.85831,340.9819,5.814613,919.7296,9.661819,1016.968,8.049847
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9323:381813687469500416,0.08807568,196.2926,-2.587872,5,10.76358,-0.4453266,-11.2614,19.46047,17.77651,16.87523,68.94926,2.213272,10.10819,1.989393,11.44149,1.993881,48.60489,1.965757
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9584:384046520674052096,0.05918783,200.0387,-1.332369,1,10.29526,0.5286544,-9.814964,18.81467,17.55494,16.86383,914.7048,8.124507,195.9702,4.130413,54.2413,3.41274,389.8025,4.903461
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9621:384083354313582592,0.08480088,200.7637,-1.87562,1,10.60697,0.6399767,-10.02011,18.09844,17.05264,16.44011,270.8479,3.186425,64.58548,2.167139,14.83561,1.956841,96.28403,2.07461
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9623:384085278458931200,0.07615708,200.6795,-2.169424,3,10.47803,-0.2330608,-10.76319,19.40219,17.70095,16.9095,78.53174,2.965019,23.37319,2.535441,21.65606,2.850669,66.69283,2.897062
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9682:385111122824423424,0.07758146,236.7115,-0.3046466,2,10.60629,0.2574767,-10.4,19.17666,17.63932,16.82358,232.5054,3.376796,43.02221,2.863562,12.08169,2.714373,87.54395,2.717935
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9761:385207879847667712,0.06061311,237.4021,0.1660728,1,9.845552,-0.009152954,-9.905074,18.81176,17.60724,17.07629,103.1898,1.707929,29.65135,1.617332,10.81466,1.484852,33.7331,1.338347
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9860:386260662248040448,0.07724694,238.3628,-0.4602998,2,10.11396,0.09181527,-10.07832,19.78634,18.25003,17.55762,114.025,2.195603,34.25845,2.228213,8.605404,2.225843,38.71447,1.627935
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9982:387345055607711744,0.05750092,240.6693,-0.8276015,1,10.31388,0.7448854,-9.605591,18.03215,16.9934,16.41687,1712.974,12.07026,411.858,6.336649,118.6407,4.76919,606.6491,5.936194
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9993:387354126578640896,0.0591345,240.9365,-0.318726,1,10.64881,0.7444158,-9.961268,18.837,17.1907,16.32329,539.075,6.270298,96.53884,4.287004,28.96484,4.131394,207.9321,4.655707
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv:9998:387357425113524224,0.05894107,240.7638,-0.5561788,1,9.835024,-0.4674937,-10.3584,20.14611,18.64782,17.90205,156.0383,3.346196,42.40351,2.848034,21.07806,2.765921,62.87457,2.765131

codex
I’ve confirmed the manuscript language is consistent with the broader integration run. I’m now validating the numeric claims directly from the local CSVs and the run summaries so I can separate well-traced facts from statements that are only asserted in prose.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/METHODS_AND_SCOPE.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# SDSS AGN/sSFR pilot methods and scope

Marker: `SDSS_AGN_SFR_PILOT_20260708T122000Z`

This run is a bounded pilot execution of the AGN-feedback research proposal. It uses public SDSS DR17 spectroscopy and derived quantities to test whether optically selected BPT AGN hosts show a specific-SFR offset relative to nearest star-forming controls matched in stellar mass proxy and redshift.

Data source: SDSS DR17 SkyServer queried through `astroquery.sdss`.

Main cuts:
- spectroscopic class `GALAXY`
- redshift 0.02--0.12
- positive Halpha, Hbeta, [O III] 5007, [N II] 6584 line fluxes
- S/N >= 3 in all four BPT lines
- `lgm_tot_p50` between 8.0 and 12.5
- `specsfr_tot_p50` between -14 and -7

Classification: BPT line-ratio cuts using Kauffmann et al. (2003) and Kewley et al. (2001) demarcations. AGN includes the high-excitation optical AGN/LINER side as a single pilot class.

Matched-control test: every BPT AGN host is paired to the nearest BPT star-forming galaxy in standardized `(logM, z)` space, with replacement. The primary statistic is the median difference `log sSFR_AGN - log sSFR_control`.

Key result from this run:
- analysis rows: 60000
- BPT AGN rows: 8146
- BPT star-forming rows: 39553
- matched pairs: 8146
- median matched delta log sSFR: -1.309 dex
- 95% bootstrap CI for median delta: -1.334, -1.282 dex

Scope guard: this pilot measures an optical-classification-associated sSFR offset. It does not establish causal AGN feedback, duty-cycle timing, molecular-gas depletion, or halo-scale energy coupling.

SDSS_AGN_SFR_PILOT_20260708T122000Z

exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/summary_metrics.json" in /Users/duhokim/NebulaMind/NebulaMind
 exited 1 in 0ms:
sed: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/summary_metrics.json: No such file or directory

exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/RESULTS_SUMMARY.md" in /Users/duhokim/NebulaMind/NebulaMind
 exited 1 in 0ms:
sed: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/RESULTS_SUMMARY.md: No such file or directory

codex
One quick correction: a couple of expected summary filenames weren’t present where I first looked, so I’m locating the actual run artifacts before I judge traceability. I’m also avoiding shell forms that need temp files in this read-only sandbox.
exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z | sed 's#"'^/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/##'"' | sort" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
METHODS_AND_SCOPE.md
aastex/sdss_agn_sfr_pilot_aas.pdf
aastex/sdss_agn_sfr_pilot_aas.tex
analysis_results.json
data/analysis_sample_bpt.csv
data/matched_agn_sf_pairs.csv
data/query.sql
data/sdss_dr17_emission_line_sample.csv
figures/figure1_bpt.pdf
figures/figure1_bpt.png
figures/figure2_matched_offsets.pdf
figures/figure2_matched_offsets.png

exec
/bin/zsh -lc "python3 -c \"import csv,pathlib; p=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv'); f=p.open(); r=csv.DictReader(f); cols=r.fieldnames; print(cols)\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-OSohppLX' (errno=Operation not permitted)
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-naqKWi9T' (errno=Operation not permitted)
['specObjID', 'z', 'ra', 'dec', 'bptclass', 'lgm_tot_p50', 'sfr_tot_p50', 'specsfr_tot_p50', 'modelMag_u', 'modelMag_g', 'modelMag_r', 'h_alpha_flux', 'h_alpha_flux_err', 'h_beta_flux', 'h_beta_flux_err', 'oiii_5007_flux', 'oiii_5007_flux_err', 'nii_6584_flux', 'nii_6584_flux_err', 'sn_ha', 'sn_hb', 'sn_oiii', 'sn_nii', 'log_nii_ha', 'log_oiii_hb', 'u_minus_r', 'g_minus_r', 'bpt_label']

exec
/bin/zsh -lc "python3 -c \"import csv,collections,pathlib; p=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv'); f=p.open(); r=csv.DictReader(f); c=collections.Counter(); n=0; 
for row in r:
    n+=1
    c[row.get('bpt_class','')] += 1
print('n',n); print(c)\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 238ms:
n 60000
Counter({'': 60000})

codex
I have the key run files now. The next pass is a focused consistency check: exact counts, the matched-offset statistic, and whether the manuscript cites numbers that only exist in prose versus numbers that are anchored in the run’s CSV/JSON outputs.
exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "run_id": "SDSS_AGN_SFR_PILOT_20260708T122000Z",
  "revision_marker": "AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z",
  "data_release": "SDSS DR17 SkyServer via astroquery.sdss",
  "query_top_n": 60000,
  "raw_rows": 60000,
  "analysis_rows": 60000,
  "bpt_counts": {
    "star-forming": 39553,
    "intermediate": 12234,
    "agn": 8146,
    "unclassified": 67
  },
  "group_medians": {
    "star-forming": {
      "n": 39553,
      "median_z": 0.06887668,
      "median_logM": 10.01737,
      "median_log_sSFR": -9.909236,
      "median_u_minus_r": 1.814429999999998
    },
    "intermediate": {
      "n": 12234,
      "median_z": 0.079609505,
      "median_logM": 10.62895,
      "median_log_sSFR": -10.8564,
      "median_u_minus_r": 2.5431500000000007
    },
    "agn": {
      "n": 8146,
      "median_z": 0.075976265,
      "median_logM": 10.79099,
      "median_log_sSFR": -11.769829999999999,
      "median_u_minus_r": 2.7576649999999994
    },
    "unclassified": {
      "n": 67,
      "median_z": 0.08311625,
      "median_logM": 10.87501,
      "median_log_sSFR": -12.06685,
      "median_u_minus_r": 2.8580700000000014
    }
  },
  "matched_pairs": 8146,
  "matched_delta_log_sSFR_median_dex": -1.3088869999999995,
  "matched_delta_log_sSFR_mean_dex": -1.201557615885097,
  "matched_delta_log_sSFR_median_ci95_bootstrap": [
    -1.3341385500000003,
    -1.2821399375
  ],
  "matched_delta_log_sSFR_mean_ci95_bootstrap": [
    -1.2194772019150502,
    -1.1835793853118095
  ],
  "match_distance_scaled_median": 0.013706693336996863,
  "match_abs_delta_logM_median": 0.0044599999999999085,
  "match_abs_delta_z_median": 0.00021079499999999973,
  "ols_adjusted_for_logM_z": {
    "n_regression": 47699,
    "coef_is_agn_log_sSFR_dex": -1.1988420719680595,
    "coef_is_agn_se": 0.005853704278258507,
    "coef_is_agn_ci95": [
      -1.2103153323534461,
      -1.1873688115826728
    ],
    "coef_logM": -0.6590074792789541,
    "coef_z": 6.926838817644406
  },
  "files": {
    "raw_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv",
    "analysis_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
    "matched_pairs_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv",
    "figure1_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/figures/figure1_bpt.pdf",
    "figure2_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/figures/figure2_matched_offsets.pdf"
  },
  "safety": "read-only public SDSS query; local artifact writes only; no DB/API/page_versions/live wiki publish/deploy/git/cron"
}
exec
/bin/zsh -lc "python3 -c \"import csv,pathlib,collections; p=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv'); f=p.open(); r=csv.DictReader(f); print(r.fieldnames); first=next(r); print(first);\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-Yzn2QNQ4' (errno=Operation not permitted)
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-J4wC7DZv' (errno=Operation not permitted)
['agn_specObjID', 'control_specObjID', 'agn_z', 'control_z', 'agn_logM', 'control_logM', 'agn_log_sSFR', 'control_log_sSFR', 'delta_log_sSFR_agn_minus_control', 'match_distance_scaled']
{'agn_specObjID': '299500947439118336', 'control_specObjID': '371626173857294336', 'agn_z': '0.09755617', 'control_z': '0.09769211', 'agn_logM': '10.67565', 'control_logM': '10.67249', 'agn_log_sSFR': '-11.52902', 'control_log_sSFR': '-10.05759', 'delta_log_sSFR_agn_minus_control': '-1.4714299999999998', 'match_distance_scaled': '0.007707993703913137'}

exec
/bin/zsh -lc "python3 -c \"import csv,statistics,pathlib; p=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv'); f=p.open(); r=csv.DictReader(f); print(r.fieldnames); rows=list(r); f.close(); print('rows',len(rows));
for key in ['delta_log_sSFR','delta_log_ssfr','delta_sSFR','delta_specsfr','delta_logsfr']:
    if key in rows[0]:
        vals=[float(x[key]) for x in rows];
        print(key, statistics.median(vals), min(vals), max(vals))
\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-0uc3PUOD' (errno=Operation not permitted)
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-PGN353Jw' (errno=Operation not permitted)
['agn_specObjID', 'control_specObjID', 'agn_z', 'control_z', 'agn_logM', 'control_logM', 'agn_log_sSFR', 'control_log_sSFR', 'delta_log_sSFR_agn_minus_control', 'match_distance_scaled']
rows 8146

exec
/bin/zsh -lc "python3 -c \"import csv,pathlib,collections; p=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv'); f=p.open(); r=csv.DictReader(f); c=collections.Counter(row['bptclass'] for row in r); print(c)\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 229ms:
Counter({'1': 32459, '2': 9808, '3': 7247, '5': 5863, '4': 3452, '-1': 1171})

codex
The core pilot numbers are now anchored in `analysis_results.json` and the matched-pair CSV. I’m doing one last trace check for the robustness rows and then a static TeX sanity pass for unresolved references or file-path problems.
exec
/bin/zsh -lc "rg -n \"7,867|7\\.867|1\\.318|7,419|1\\.446|1,530|2,114|0\\.744|0\\.763|96\\.6%|0\\.05|0\\.002\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:3:    0.0027030347708563705,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py:166:        ("Moderate mass--redshift caliper", cal["matched_pairs"], cal["median_delta_log_sSFR"], None, None, "96.6% target coverage"),
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:13:    0.059135
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:30:    "The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2:299500947439118336,371626173857294336,0.09755617,0.09769211,10.67565,10.67249,-11.52902,-10.05759,-1.4714299999999998,0.007707993703913137
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:8:299591932026316800,873715409046497280,0.06256682,0.0624647,10.66407,10.66449,-12.11176,-12.16429,0.05252999999999908,0.0039763143452389476
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:13:300622998686164992,613661665661052928,0.07061857,0.07063993,10.16462,10.16344,-10.14339,-10.12031,-0.02308000000000021,0.002277268717934139
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:14:300626572098955264,306314076458346496,0.0934706,0.09348612,10.18171,10.18059,-11.50098,-9.845624,-1.6553559999999994,0.002103171497400901
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:23:300699414744295424,817528164283607040,0.08420008,0.08295473,11.29601,11.31012,-12.34337,-10.47035,-1.8730200000000004,0.05396683543124002
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:46:301790680454293504,668850824549525504,0.04747756,0.04799621,11.39217,11.41945,-12.29907,-11.54585,-0.7532200000000007,0.05299517338926388
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:47:301793154355456000,377326035928115200,0.07045922,0.07068226,10.48178,10.48309,-11.05688,-10.05432,-1.002559999999999,0.008846580942419876
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:61:301851428471728128,637370710372673536,0.08606229,0.0860952,10.26033,10.25834,-11.67688,-10.05567,-1.6212100000000014,0.0037994442424146967
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:65:301886063088003072,811802457515517952,0.05667516,0.05697191,10.66669,10.6644,-12.10802,-11.12523,-0.9827899999999996,0.012070553653729907
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:71:301903655274047488,518072868857210880,0.03264382,0.033669,11.07523,11.05264,-12.44944,-10.2951,-2.1543399999999995,0.05649817537347009
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:75:302928679636330496,443692831198963712,0.06687512,0.06657331,11.00019,11.01062,-12.02222,-10.05115,-1.971070000000001,0.02204954817736545
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:76:302965513275860992,345785439719811072,0.03367684,0.03369356,10.68048,10.65219,-10.56604,-10.28008,-0.2859599999999993,0.05097049624243701
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:88:304038361729886208,484282126968055808,0.04348949,0.04381835,10.73248,10.7368,-10.31641,-10.05564,-0.26076999999999906,0.014785244424160293
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:97:305140621700524032,663319456595863552,0.05594477,0.05588206,10.84155,10.85623,-11.32089,-10.48684,-0.8340499999999995,0.026555502987502786
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:101:305191748991215616,409940574464927744,0.05991426,0.06000083,10.72888,10.73611,-12.4292,-10.41382,-2.0153800000000004,0.013439171554829127
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:102:305196696793540608,787112648599693312,0.05959919,0.05968505,10.61416,10.6125,-12.30479,-10.74348,-1.5613100000000006,0.004440262333295754
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:104:305201094840051712,702714413865527296,0.05830636,0.05837893,10.69239,10.69453,-10.68723,-10.47315,-0.21407999999999916,0.0047496660277684295
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:118:305275036997019648,443771446280349696,0.0645521,0.06455159,10.53891,10.53747,-11.06852,-9.859509,-1.2090110000000003,0.0025943377941790406
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:119:305279984799344640,466231994196453376,0.02134296,0.02174366,10.25161,10.25262,-10.77698,-10.05933,-0.7176500000000008,0.015424928777417638
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:120:305288506014459904,737588170312411136,0.05533539,0.05376796,11.06421,11.04717,-12.08448,-12.17079,0.086310000000001,0.067323444107856
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:130:306353109121132544,739731943360325632,0.05654917,0.05717795,10.8882,10.87615,-12.25899,-10.13734,-2.1216500000000007,0.03238828337890056
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:139:306414681772288000,345785439719811072,0.03443834,0.03369356,10.67639,10.65219,-12.13318,-10.28008,-1.8530999999999995,0.05207049811015176
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:150:307473511738271744,836691278170187776,0.05115105,0.05121873,10.32803,10.33024,-10.55966,-10.16038,-0.3992799999999992,0.004748208109168545
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:159:307513369034778624,498862475718977536,0.09637783,0.09679849,10.96139,10.96681,-12.29897,-10.05692,-2.2420500000000008,0.01881274914734282
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:181:308595012860405760,588877571106564096,0.08264635,0.08252977,10.34723,10.35172,-11.07197,-10.05637,-1.015600000000001,0.0092353927185041
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:192:308634870156912640,566466225144621056,0.05951072,0.05944737,10.46303,10.4622,-10.26933,-9.672817,-0.5965129999999998,0.0028460888868246654
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:212:309692600292501504,388463258882828288,0.06067357,0.0593444,11.11955,11.09359,-12.82321,-10.81322,-2.00999,0.06905712528556615
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:214:309695349071570944,458286647474153472,0.05955937,0.05974426,10.77996,10.78203,-12.26453,-10.23807,-2.02646,0.007991173493321554
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:216:309709367844825088,381724077271836672,0.1131658,0.1131433,10.87891,10.87162,-11.93889,-10.0554,-1.88349,0.01316159702916
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:229:310753354118621184,573119926051563520,0.09671573,0.09677893,10.73822,10.74213,-11.75233,-10.05432,-1.69801,0.007446917440312123
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:232:310764074356992000,773629892565690368,0.07376982,0.07268552,11.16173,11.1432,-11.5937,-11.58102,-0.01267999999999958,0.05322052473518396
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:239:310791562147686400,315334739210823680,0.04096115,0.04033846,11.09812,11.12417,-11.58592,-10.5402,-1.0457199999999993,0.052622250157697704
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:252:310869077717444608,490986124341176320,0.0501174,0.04953062,10.53543,10.53708,-12.23349,-10.208,-2.0254899999999996,0.022626471999016927
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:261:310910309403486208,588946290583300096,0.06543402,0.06537198,10.72819,10.72918,-11.70481,-10.08755,-1.61726,0.0029673783957613474
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:313:314185755800922112,651932094292846592,0.06885027,0.06909105,10.75399,10.74413,-10.34167,-10.79299,0.45131999999999906,0.020006438526503977
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:317:314224238707894272,519151489529178112,0.03726012,0.03747749,10.06055,10.05741,-11.73125,-10.09289,-1.6383599999999987,0.01005207229822852
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:322:314240181626497024,443718394844309504,0.07685738,0.07682026,10.05342,10.05605,-10.85784,-9.926133,-0.9317069999999994,0.004946045649220982
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:325:314254200399751168,381724077271836672,0.1130199,0.1131433,10.87649,10.87162,-10.93911,-10.0554,-0.8837099999999989,0.009961336018839374
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:334:314299005498583040,391918473854347264,0.02445948,0.02424728,9.638014,9.626187,-10.87708,-10.00298,-0.8740999999999985,0.02279900676855326
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:367:316419407465179136,744386175845820416,0.05013775,0.05010149,10.4816,10.48708,-11.5916,-10.08142,-1.51018,0.009969443530829786
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:371:316441122819827712,864716455491430400,0.04872853,0.04889076,10.24134,10.23319,-10.00274,-10.12352,0.12077999999999989,0.01593872254284423
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:383:316528259116328960,315355355053844480,0.07401329,0.07410746,10.30136,10.30217,-10.46951,-10.05,-0.41950999999999894,0.003884294856326481
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:387:317508199592781824,565377158172665856,0.05253265,0.05295245,10.78547,10.78705,-12.49951,-12.34649,-0.1530200000000015,0.01629784980660944
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:389:317519469586966528,475296916838574080,0.04639931,0.04568637,11.1955,11.16705,-12.59667,-11.23628,-1.3603899999999989,0.05804974491784835
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:391:317532663726499840,321012897469720576,0.07645354,0.07641456,10.44067,10.43956,-11.56835,-10.36242,-1.2059300000000004,0.0024938425355701156
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:394:317567573220681728,535994090299353088,0.05013565,0.05047424,10.43248,10.43676,-11.62892,-10.29475,-1.3341700000000003,0.01506574469224104
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:401:317615401976489984,603508772303824896,0.05005798,0.05008364,9.824159,9.827188,-10.07472,-10.08012,0.005400000000001626,0.005544419041413138
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:417:318703098904209408,831005433010350080,0.09338817,0.09326141,10.74464,10.74813,-11.78773,-10.29962,-1.488109999999999,0.00793800154660576
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:421:318723164991416320,863702155528267776,0.07458969,0.07443131,10.76302,10.77009,-12.31719,-10.63509,-1.6821000000000002,0.014102775336958352
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:453:320935107022055424,522423910977792000,0.0768301,0.07675339,10.61738,10.61735,-11.34062,-10.66517,-0.6754499999999997,0.0029328281930367196
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:462:321042034527856640,541594720841787392,0.06206989,0.06206039,10.76667,10.76381,-11.05592,-10.67958,-0.3763400000000008,0.005165279165115207
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:464:321055228667389952,444900092785223680,0.08165723,0.0804886,11.12828,11.13138,-11.4958,-11.55092,0.0551200000000005,0.045020012761053205
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:480:323212197163460608,452755278899734528,0.06013782,0.05985662,10.37414,10.37822,-11.93,-10.81756,-1.1124399999999994,0.013022056245404999
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:482:323216870087878656,444900092785223680,0.07915194,0.0804886,11.12376,11.13138,-12.55813,-11.55092,-1.0072100000000006,0.052907445639065825
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:490:323302906872752128,586716486035335168,0.07851025,0.07860699,9.971076,9.972449,-9.850426,-9.791266,-0.05916000000000032,0.004449011435359903
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:492:323304006384379904,490905585114441728,0.05048371,0.05028698,10.15675,10.15153,-9.755471,-9.89403,0.13855900000000076,0.012041307952963567
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:498:324306760603035648,737631326143801344,0.05043545,0.05036066,10.40652,10.41388,-11.33667,-10.16982,-1.1668500000000002,0.013564284939292437
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:509:324394721533257728,815187854253647872,0.118139,0.1179329,10.80869,10.80475,-11.37714,-10.63233,-0.7448100000000011,0.010604424360158233
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:528:325554981010696192,369333415759079424,0.1068853,0.1085365,11.39963,11.39581,-12.42194,-10.05453,-2.3674099999999996,0.0634931374581249
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:543:327682809848162304,641784425394235392,0.1181914,0.1181413,10.97926,10.97442,-10.82478,-10.05352,-0.7712599999999998,0.008927449326613638
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:545:327690781307463680,377249619869984768,0.04841816,0.04849259,10.55864,10.5589,-12.20054,-10.16206,-2.03848,0.0028834743980331026
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:562:327765273220245504,438105660882708480,0.06388531,0.06353395,11.29359,11.32122,-12.57041,-12.38812,-0.18229000000000006,0.051557641655381105
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:564:327775168824895488,340107562093406208,0.08230726,0.0821012,10.73736,10.73638,-12.13084,-10.05852,-2.0723199999999995,0.008072327662832177
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:573:327804580760938496,326662738153596928,0.07198845,0.07200869,10.40595,10.40473,-11.57933,-10.10267,-1.4766600000000007,0.0023301189698982884
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:575:327809528563263488,323171790111139840,0.08174095,0.08193589,10.76318,10.76567,-11.61394,-10.17894,-1.4349999999999987,0.008697869334116195
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:604:331074254437115904,602518936541489152,0.08432848,0.08407099,11.34383,11.37357,-12.33956,-11.14456,-1.1950000000000003,0.05447537395008998
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:607:331098718570833920,426777117603162112,0.083649,0.08360787,10.46611,10.46475,-10.73795,-10.28998,-0.44796999999999976,0.0029112071372074115
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:630:332216097245784064,313112081287112704,0.09048326,0.08803225,11.46243,11.39815,-12.45618,-12.51279,0.05661000000000094,0.14896022523938454
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:637:332240561379502080,486403634771290112,0.07090392,0.07092067,10.46692,10.46571,-11.09157,-10.39864,-0.6929300000000005,0.0022719915857712823
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:654:333337324211431424,588958385211205632,0.08161739,0.08178187,10.73943,10.74137,-12.29536,-10.05801,-2.237350000000001,0.007193559982966051
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:673:334402200803502080,871566138138454016,0.05615278,0.05526646,10.74368,10.74096,-12.04832,-10.20871,-1.8396100000000004,0.03423316479089194
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:675:334409072751175680,511219887490754560,0.05416252,0.0542786,10.65615,10.65558,-9.971319,-10.53541,0.5640910000000012,0.004554569276624455
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:709:336646024326047744,386256539079436288,0.07644577,0.0778144,11.21862,11.22202,-12.01887,-10.54223,-1.4766399999999997,0.052674852820360565
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:710:336649597738838016,843468942117726208,0.08845632,0.08821125,10.74432,10.74646,-11.41934,-9.859128,-1.560212,0.010130397033541275
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:730:336785662302775296,335617985718806528,0.07806308,0.07800532,10.28911,10.2888,-11.34882,-9.83742,-1.5114,0.0022774822291878717
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:746:337842847296284672,532607862904481792,0.08793359,0.08778377,11.32171,11.29124,-12.08736,-12.625,0.5376399999999997,0.055191858026074146
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:755:337915140185810944,336658118953953280,0.08873814,0.08863404,11.10783,11.07986,-12.44529,-10.432,-2.0132899999999996,0.05054686773717656
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:761:338907449413101568,747630559966029824,0.07834522,0.07828191,10.77448,10.77542,-10.68867,-10.40479,-0.2838799999999999,0.0029537686892790265
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:768:338987164006115328,300714533029177344,0.1022681,0.1023372,10.38461,10.3856,-10.76345,-10.56824,-0.19521000000000122,0.0031871965623176297
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:774:340055610168993792,740989234386593792,0.05508721,0.05420237,10.92726,10.93962,-12.21146,-10.14254,-2.0689200000000003,0.04049574351428588
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:775:340056159924807680,663201808851691520,0.05385043,0.04925624,11.46091,11.39035,-12.57341,-11.45037,-1.1230400000000014,0.2167972033857109
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:776:340058908703877120,748762781964068864,0.05477432,0.05452603,10.42628,10.42353,-11.24818,-10.66127,-0.5869099999999996,0.01070643683798067
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:779:340079524546897920,828775618396055552,0.05899673,0.05834416,10.67981,10.68653,-12.30185,-10.40854,-1.8933099999999996,0.027727871296723747
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:780:340086671372478464,772384970541918208,0.0592591,0.05792373,10.9309,10.93044,-12.45796,-10.20825,-2.2497100000000003,0.05105281858582989
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:781:340088045762013184,857940439385270272,0.0543637,0.05446631,10.79402,10.80131,-12.35688,-10.40553,-1.9513499999999997,0.013706677650828343
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:784:340105912825964544,388463258882828288,0.05943118,0.0593444,11.11349,11.09359,-12.42281,-10.81322,-1.6095900000000007,0.03600443860792935
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:790:340182878639908864,738602744432060416,0.05459604,0.05519211,11.00148,11.01721,-12.11337,-10.88081,-1.2325599999999994,0.03636292110424584
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:791:340184527907350528,845668240670615552,0.05380791,0.05356275,11.23868,11.24563,-12.74483,-10.19914,-2.5456900000000005,0.01563966911963728
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:795:341241981990627328,845668240670615552,0.05291578,0.05356275,11.26584,11.24563,-12.44158,-10.19914,-2.24244,0.044014816090212974
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:796:341263147589462016,512426876396922880,0.05287682,0.0530049,10.4731,10.47344,-11.39425,-10.10695,-1.2873,0.004934176959512924
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:798:341285687577831424,496631291664427008,0.05264126,0.05240386,10.89325,10.88922,-12.15469,-10.53732,-1.617370000000001,0.011621799206768391
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:799:341286512211552256,477543495347759104,0.05245277,0.05251931,10.71737,10.7142,-10.83523,-10.30665,-0.5285799999999998,0.006251807674167712
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:803:341309876833642496,675605129042356224,0.05027221,0.05040107,10.5624,10.56103,-12.03678,-12.26,0.22321999999999953,0.005509586364103515
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:804:342280470622398464,871566138138454016,0.0549181,0.05526646,10.73866,10.74096,-11.79829,-10.20871,-1.5895799999999998,0.013946253108060861
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:805:342337645227042816,706077541147895808,0.05027898,0.04938756,10.92934,10.93768,-11.53889,-10.20546,-1.33343,0.037241096231546915
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:809:342375578378201088,666607820493318144,0.05273196,0.0524849,10.82873,10.83287,-12.16957,-10.20297,-1.9665999999999997,0.012034181790725197
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:811:342398668122384384,501173924038469632,0.05493557,0.05482313,10.5424,10.53759,-12.28606,-9.887704,-2.3983560000000015,0.009672957632497505
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:814:343409394253326336,441431683523176448,0.06053828,0.06060154,10.7689,10.7691,-12.12202,-9.399796,-2.722223999999999,0.0024448844552176032
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:819:343431934241695744,737614008835663872,0.05517551,0.05575849,10.88813,10.86938,-10.74612,-11.41107,0.664950000000001,0.04046825005621917
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:820:343466843735877632,307417436645255168,0.05047373,0.05050373,10.90101,10.87995,-10.78935,-10.65638,-0.13297000000000025,0.03795844601291377
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:827:343572671730051072,341214769077839872,0.05437197,0.05383033,10.85859,10.86747,-11.51471,-10.50117,-1.013539999999999,0.026165334851923783
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:833:344550412847704064,742017278647756800,0.05591327,0.05471943,10.80412,10.79707,-11.97383,-9.793043,-2.1807869999999987,0.047370420191934104
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:839:344633151097694208,386267259317807104,0.05574698,0.05442572,11.38044,11.26721,-12.57112,-12.4255,-0.14562000000000097,0.21015159193400856
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:842:344644146213971968,476408798139934720,0.05449581,0.05411638,10.89544,10.88005,-12.2,-10.56505,-1.63495,0.03129078010838514
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:843:344646070359320576,511219887490754560,0.05484671,0.0542786,10.65866,10.65558,-12.05393,-10.53541,-1.5185199999999988,0.022414361600332763
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:848:344688676434896896,841100869083621376,0.05632764,0.05667125,10.58705,10.58959,-11.9755,-10.2824,-1.6930999999999994,0.013909178582474464
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:849:344697472527919104,637433657413363712,0.05590431,0.05721708,10.92333,10.91217,-12.35235,-10.07258,-2.279769999999999,0.05406000712519153
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:853:345727715359352832,856964111513184256,0.05597249,0.05598931,10.53723,10.5421,-11.66261,-10.93547,-0.7271400000000003,0.008797186348572994
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:854:345753828760512512,526965443823429632,0.1078605,0.1078503,10.3504,10.34893,-11.6617,-10.0714,-1.5902999999999992,0.0026768605601914493
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:860:346780772604078080,657696279152846848,0.0265715,0.02685087,10.88053,10.90811,-12.3399,-10.50655,-1.8333499999999994,0.05082205517922545
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:861:346787094795937792,448213471176189952,0.04321273,0.04426393,11.09869,11.10135,-11.9561,-12.013,0.05690000000000062,0.04046810280102461
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:868:346857188662208512,444765677488728064,0.04977922,0.05002153,10.72415,10.73456,-11.13411,-9.87631,-1.2577999999999996,0.020917024387722166
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:870:346905842051737600,855709805707290624,0.10961,0.1095726,10.45127,10.4524,-11.10114,-10.24367,-0.8574699999999993,0.002487632050209164
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:880:347939388551882752,817528164283607040,0.0837642,0.08295473,11.28624,11.31012,-11.69949,-10.47035,-1.229140000000001,0.05299358363982647
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:897:348049064836753408,484282126968055808,0.04373896,0.04381835,10.74149,10.7368,-12.23537,-10.05564,-2.1797299999999993,0.008977851271653393
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:903:348073803848378368,319870230228658176,0.1058049,0.1058687,11.08608,11.08636,-11.98093,-10.31377,-1.6671600000000009,0.0024904523130000315
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:908:349060340589291520,409886698395166720,0.05445118,0.0541275,10.27699,10.2728,-12.0162,-10.17167,-1.844529999999999,0.014493914289875015
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:910:349074359362545664,742053012775659520,0.055158,0.05522581,10.34712,10.34901,-11.88918,-10.14398,-1.7451999999999988,0.004279358264546338
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:911:349076008629987328,532626554602153984,0.05463576,0.05471885,10.60688,10.60663,-12.33333,-10.14159,-2.1917399999999994,0.0032079875446111706
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:912:349091401792776192,315334739210823680,0.04093848,0.04033846,11.09604,11.12417,-12.50583,-10.5402,-1.965629999999999,0.055627020937052706
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:923:350187609433073664,734219541160159232,0.05309742,0.05348988,10.36238,10.35878,-10.6928,-10.82922,0.13641999999999932,0.01634414844548938
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:925:350211798688884736,564250438296168448,0.0595574,0.05910273,10.82899,10.8271,-12.51856,-10.72934,-1.7892200000000003,0.017710690119369658
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:926:350217296247023616,476408798139934720,0.05436617,0.05411638,10.90625,10.88005,-12.14333,-10.56505,-1.5782800000000012,0.04815732197600768
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:928:350224717950511104,452699753562531840,0.05495768,0.05519342,10.65547,10.64579,-12.11296,-9.662132,-2.4508279999999996,0.019629888668239188
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:932:350255779153995776,624890978989271040,0.0610249,0.06109975,10.7577,10.76348,-10.3568,-10.06179,-0.29500999999999955,0.010799030955291956
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:933:350279418653992960,563043720241375232,0.07277717,0.0733472,11.25309,11.28352,-12.76068,-9.787225,-2.9734550000000013,0.05899358257132237
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:935:350316802049337344,806154540742109184,0.09974685,0.0997948,10.8683,10.86958,-12.58989,-10.55208,-2.0378100000000003,0.002945739964762473
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:938:351281623905363968,651932094292846592,0.06896829,0.06909105,10.75137,10.74413,-11.93956,-10.79299,-1.1465700000000005,0.013861848067527846
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:941:351317632911173632,487644708336592896,0.1156088,0.1168378,11.30713,11.32095,-11.81765,-10.56307,-1.2545800000000007,0.05316968139972708
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:950:351408892376279040,843379331920062464,0.05289865,0.05337321,10.64207,10.64985,-12.08726,-10.61417,-1.473090000000001,0.02292458855781824
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:951:351435555533252608,845668240670615552,0.05263391,0.05356275,11.21225,11.24563,-12.43167,-10.19914,-2.2325300000000006,0.06983605177935032
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:954:351446000893716480,454935885654288384,0.05042199,0.05007917,10.68266,10.66512,-10.86802,-10.17248,-0.6955399999999994,0.0342091624246439
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:955:351451223573948416,710558049940563968,0.05661005,0.05645438,10.26217,10.26372,-12.06482,-10.35737,-1.7074499999999997,0.0065732922738798135
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:959:352442158160046080,567473657991948288,0.05208707,0.05201305,10.47755,10.47331,-10.52724,-10.40266,-0.12458000000000169,0.008145877862190086
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:964:352491911061202944,787100004215973888,0.05709462,0.05695822,10.45603,10.45705,-10.69432,-10.47448,-0.2198399999999996,0.005528391611349831
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:972:352546336886777856,322016752743507968,0.05069121,0.05038764,10.84808,10.8617,-10.56648,-11.52121,0.9547299999999996,0.027143050446964995
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:973:352554583223986176,587770087985932288,0.05049714,0.04937889,11.11555,11.09542,-11.81398,-11.12786,-0.6861200000000007,0.05605760080269616
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:976:352564478828636160,675605129042356224,0.05062211,0.05040107,10.56896,10.56103,-11.42966,-12.26,0.8303399999999996,0.016598118586349974
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:982:354756355090835456,815250526416431104,0.08120854,0.08245505,11.15985,11.17127,-12.3629,-11.03065,-1.3322500000000002,0.05190129951475253
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:997:367170403069618176,300660382081509376,0.04578008,0.04565335,10.61346,10.62687,-12.01205,-10.05282,-1.9592299999999998,0.024640004186872837
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1002:367214933290543104,575472610452727808,0.05017426,0.05003875,9.981252,9.981629,-12.21327,-9.72731,-2.4859600000000004,0.005224366756298887
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1006:368192397768681472,404274238288062464,0.06239973,0.06225554,10.55993,10.55776,-10.46651,-10.05021,-0.41629999999999967,0.006757499969937025
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1023:368321865262852096,668889582334404608,0.1106468,0.1106237,10.60841,10.60691,-10.3393,-9.828558,-0.5107420000000005,0.002842969623910064
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1026:369296307241641984,710544580923123712,0.05656424,0.05719944,10.79521,10.78693,-12.21957,-10.32771,-1.8918599999999994,0.028497324829141083
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1027:369300430410246144,439118037975590912,0.05694161,0.0579423,11.17682,11.15833,-12.43476,-10.52352,-1.9112400000000012,0.0507236217546521
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1028:369302079677687808,532702146026563584,0.05732402,0.05709619,10.74367,10.75521,-10.89231,-9.863687,-1.0286229999999996,0.022540588945563725
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1034:369333965514893312,663319456595863552,0.05565897,0.05588206,10.85522,10.85623,-10.77672,-10.48684,-0.28987999999999836,0.008719839878690336
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1036:369339737950939136,476398902535284736,0.05560879,0.05536479,10.09752,10.10327,-11.14401,-10.00867,-1.1353399999999993,0.013939375451669168
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1037:369341662096287744,476408798139934720,0.0546039,0.05411638,10.8753,10.88005,-12.30872,-10.56505,-1.7436699999999998,0.020506871409299583
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1053:369413130352093184,369333415759079424,0.1072041,0.1085365,11.43816,11.39581,-12.63286,-10.05453,-2.578330000000001,0.09173492681634715
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1056:369426324491626496,605820495585110016,0.04738104,0.04882566,11.14899,11.16166,-12.34222,-10.68357,-1.6586499999999997,0.05975387415759314
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1075:370519510135891968,572079513039562752,0.05324219,0.05316895,11.13953,11.14275,-12.66364,-11.90137,-0.7622699999999991,0.006441318088414526
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1086:370563765478909952,466295765870864384,0.08479486,0.08489854,10.90065,10.89847,-11.26958,-10.05889,-1.2106899999999996,0.005579638149318373
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1093:371616278252644352,739837771354499072,0.07730743,0.07757486,11.1113,11.1228,-12.09709,-10.0571,-2.0399899999999995,0.023102926909070867
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1099:372703695218960384,386267259317807104,0.052211,0.05442572,11.3339,11.26721,-12.51386,-12.4255,-0.08835999999999977,0.14697834983365493
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1105:372835361736386560,592376496782338048,0.08253887,0.08249935,10.64259,10.64151,-12.356,-10.07944,-2.27656,0.002463321431038531
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1112:373842239492745216,621505303212484608,0.08984703,0.089917,10.68927,10.6899,-12.20343,-10.86386,-1.3395700000000001,0.0029055374046898425
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1123:373943669440407552,472910152979212288,0.1027886,0.1027444,10.37177,10.37086,-11.41888,-9.885537,-1.5333430000000003,0.0023542456415102785
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1162:376180894450345984,814158710480857088,0.08191913,0.08056218,11.09582,11.09948,-12.28626,-10.45568,-1.8305800000000012,0.05228842693647096
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1163:376181444206159872,829883381343873024,0.08313815,0.08350301,11.09239,11.0601,-12.51774,-10.5,-2.01774,0.059821373518568595
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1168:377180900393248768,301860774320564224,0.066246,0.06574579,10.26587,10.26718,-11.23882,-10.05269,-1.1861300000000004,0.01926621366157074
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1174:377241923288590336,854658122667550720,0.09165128,0.09141654,10.12167,10.12468,-10.10549,-10.04862,-0.056869999999999976,0.010484492970261723
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1176:377256766695565312,409940574464927744,0.05999574,0.06000083,10.73189,10.73611,-11.79891,-10.41382,-1.38509,0.0076051257552272305
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1178:377262539131611136,511319118415161344,0.05875403,0.058948,10.85918,10.85483,-11.98594,-10.08071,-1.9052299999999995,0.010788620027240757
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1186:377295799358351360,836609089676011520,0.02288939,0.02430492,10.66873,10.68308,-12.44091,-10.61211,-1.828800000000001,0.059968992301866295
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1189:377344727625787392,496663452379539456,0.07147668,0.07151441,10.50253,10.50159,-9.896485,-9.98491,0.08842499999999909,0.002224414985391453
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1204:378431319975159808,337937130418366464,0.04810476,0.04841949,10.05319,10.05419,-11.09877,-10.03087,-1.0678999999999998,0.012165065713548884
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1214:378468978248411136,602362805890344960,0.07790178,0.07787939,10.26234,10.26122,-11.14789,-9.675303,-1.4725870000000008,0.0021917797254449845
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1216:378470627515852800,569797745762658304,0.06039347,0.05992184,10.46408,10.46434,-11.69847,-9.862066,-1.836404,0.018034696489450584
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1221:379441221371717632,865821502409304064,0.04650351,0.04612083,10.05165,10.04508,-12.00202,-10.24363,-1.7583900000000003,0.018817243823372114
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1223:379450567220553728,317556303226497024,0.1179219,0.1178732,10.50089,10.49913,-10.03155,-10.05271,0.021160000000000068,0.0036768707197971603
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1226:379499220610082816,650933737751603200,0.05508272,0.05537228,10.84845,10.85723,-12.38814,-10.3302,-2.0579400000000003,0.019305977069310434
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1243:379570963743795200,536015530776094720,0.04736894,0.04726655,10.44094,10.43896,-11.67819,-10.05102,-1.6271700000000013,0.005295613988020883
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1247:380571514241574912,318667089898399744,0.07880192,0.07875134,10.31754,10.31712,-11.22652,-10.19345,-1.0330700000000004,0.00207626598120239
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1257:380643257375287296,536012232241211392,0.04703142,0.04833313,11.05117,11.04772,-11.92,-11.15102,-0.7689799999999991,0.05014607941498651
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1260:380668271264819200,474023957419288576,0.05791375,0.05782307,10.51435,10.50604,-11.83821,-10.38455,-1.4536599999999993,0.015367122941974667
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1268:380728744404346880,829883381343873024,0.08437574,0.08350301,11.08333,11.0601,-11.77207,-10.5,-1.2720699999999994,0.05352039016653979
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1291:381849421597403136,380583333991573504,0.08098383,0.08100672,10.42748,10.42633,-11.43167,-10.21783,-1.2138400000000011,0.0022490021257712276
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1293:382817546585270272,466295765870864384,0.08519673,0.08489854,10.89329,10.89847,-11.16183,-10.05889,-1.1029400000000003,0.014731547603891396
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1294:382832939748059136,661020652173551616,0.02691544,0.02723799,10.75211,10.72154,-11.6384,-10.74431,-0.8940900000000003,0.05643738977138704
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1304:382936843596883968,334468171501168640,0.08204804,0.08204828,10.34176,10.34029,-10.12442,-9.979167,-0.1452530000000003,0.002648327612210935
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1306:382939042620139520,628315133931710464,0.08171601,0.08049799,11.20154,11.18827,-12.70309,-12.36563,-0.3374600000000001,0.05233923220340336
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1312:383947289749645312,593367981896001536,0.07909684,0.07797395,11.16822,11.14703,-12.25,-9.969646,-2.280354000000001,0.05744394979446232
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1339:385115520870934528,620480833270081536,0.07114893,0.07224516,11.13039,11.10883,-11.49414,-11.78411,0.2899700000000003,0.05713751931284352
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1348:386183971312003072,452699753562531840,0.05525919,0.05519342,10.64671,10.64579,-12.2425,-9.662132,-2.580368,0.0030113134140584558
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1349:386192767405025280,740989234386593792,0.0543775,0.05420237,10.942,10.93962,-12.46395,-10.14254,-2.32141,0.007949952605274632
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1351:386213658125953024,368220985071003648,0.05160759,0.05189672,10.78287,10.77928,-11.88671,-10.50851,-1.3782000000000014,0.01280564518412394
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1352:386219430561998848,752111894281611264,0.05595941,0.05566004,10.26608,10.26242,-10.93495,-10.29006,-0.6448900000000002,0.01320747933016102
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1356:386286500771293184,737631326143801344,0.05060026,0.05036066,10.41323,10.41388,-10.76282,-10.16982,-0.593,0.009233549374852277
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1360:386330481236404224,454935885654288384,0.05073542,0.05007917,10.68227,10.66512,-11.70148,-10.17248,-1.529,0.03979857567058237
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1361:386333230015473664,432487706656794624,0.05804547,0.05796046,10.42593,10.42478,-11.51311,-10.22507,-1.2880399999999987,0.0038538732308548013
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1362:387317567817017344,822012801361930240,0.07456175,0.07454052,10.4493,10.45079,-10.48066,-9.720096,-0.7605640000000005,0.002804335628230815
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1366:387334610247247872,835523596838266880,0.0944719,0.09355395,11.16709,11.14512,-12.34109,-10.34225,-1.9988399999999995,0.05289525901478484
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1368:387338733415852032,439118037975590912,0.05811602,0.0579423,11.17758,11.15833,-11.85841,-10.52352,-1.3348899999999997,0.035310332184680805
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1371:387376391689103360,671201036106491904,0.05815966,0.05724575,11.19145,11.21574,-12.60674,-11.55828,-1.0484600000000004,0.05599490360336859
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1372:387383263636776960,593484805006452736,0.05611989,0.05573779,10.35631,10.3562,-10.78481,-10.11671,-0.6681000000000008,0.014607567109351448
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1373:387386837049567232,491019934323730432,0.05121299,0.05101316,10.97683,10.96198,-12.2817,-10.49409,-1.7876100000000008,0.02782251262975525
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1374:387390410462357504,846839220554196992,0.1167837,0.1168557,11.00083,11.00126,-11.31147,-9.945758,-1.3657120000000003,0.0028592298155772386
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1375:387407727770494976,491019934323730432,0.05109033,0.05101316,10.94456,10.96198,-12.32619,-10.49409,-1.8321000000000005,0.0315217298978161
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1379:387440713119328256,636193682957035520,0.05909625,0.05821722,11.04908,11.03632,-12.33182,-11.16629,-1.1655300000000004,0.040712931045118396
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1381:387451983113512960,621620202177587200,0.05828073,0.05786454,10.15559,10.15571,-10.7536,-10.00487,-0.7487300000000001,0.015910822021310563
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1383:387478371392579584,616014616467630080,0.05541354,0.05546028,10.72892,10.72958,-12.423,-10.15313,-2.269869999999999,0.0021461775261330846
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1385:388442643039807488,638553510241134592,0.05740494,0.05733588,10.21809,10.21196,-10.23016,-10.03436,-0.1958000000000002,0.011354781224027305
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1386:388444842063063040,573187820894578688,0.0573527,0.05733616,10.84793,10.83534,-12.53172,-10.17162,-2.360099999999999,0.022690609537386427
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1392:388476453022361600,486539699335227392,0.070324,0.0702659,10.16013,10.16107,-11.04449,-9.942613,-1.101877,0.0027929280962394223
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1393:388478377167710208,586720334326032384,0.06001066,0.05990209,10.14469,10.14322,-11.19174,-10.09431,-1.0974299999999992,0.00492319504532277
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1399:388520433487472640,864745317671659520,0.05942294,0.05940515,10.26908,10.25524,-11.85591,-10.30591,-1.549999999999999,0.02494303681417868
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1402:388527855190960128,451562308699711488,0.05667758,0.05662025,10.62472,10.62986,-11.48597,-9.998369,-1.4876009999999997,0.009515873174693122
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1403:388534452260726784,828775618396055552,0.0591639,0.05834416,10.68736,10.68653,-12.15489,-10.40854,-1.7463499999999996,0.03137118461434494
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1408:388556992249096192,370523358426589184,0.02783617,0.02839467,10.97053,10.94213,-11.75549,-10.36843,-1.38706,0.05544020304385613
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1413:388588603208394752,432418712302151680,0.0580112,0.05792902,11.07837,11.05632,-12.25278,-10.29424,-1.9585399999999993,0.03984869426911311
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1418:389608400293488640,514596212704307200,0.05749664,0.05754197,10.07368,10.07842,-9.982047,-9.913437,-0.06860999999999962,0.008713486509142197
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1423:389641385642321920,826519145708283904,0.0307668,0.03032968,10.64989,10.68131,-12.19899,-10.56063,-1.6383600000000005,0.059020145025078644
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1425:389674096113248256,432418712302151680,0.05825833,0.05792902,11.05508,11.05632,-12.41406,-10.29424,-2.119819999999999,0.012784947941144162
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1426:389677944403945472,814077621498308608,0.05734747,0.05694076,10.41406,10.41628,-12.18299,-10.09909,-2.0839,0.0160531671693601
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1429:389683167084177408,704982151229106176,0.05713054,0.05686669,10.26867,10.26276,-11.66325,-10.09723,-1.56602,0.01466600854907998

exec
/bin/zsh -lc "rg -n \"\\\\cite[p|t]?\\{|\\\\ref\\{|\\\\label\\{\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
rg: regex parse error:
    (?:\cite[p|t]?\{|\ref\{|\label\{)
       ^^
error: unrecognized escape sequence

exec
/bin/zsh -lc "rg -n \"hardcastle2020|harrison2018|tacconi2018|kauffmann2003bpt|sdssdr17|brinchmann2004|york2000|kewley2006|kewley2001|bluck2014|penny2018\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present a selection-aware SDSS DR17 matched-control pilot that measures the association between broad optical BPT-selected galaxies and catalog specific star-formation rate within a selection-limited denominator. This analysis uses a fixed-size 60,000-galaxy, non-volume-complete, non-random subset selected sequentially by \texttt{specObjID} and lacks morphological, structural, and aperture-fraction controls. Because structural proxies such as concentration index and \texttt{fracDeV} were not retained in the cache, the reported -1.309 dex sSFR offset is an association-only measurement within this fixed-size, morphology-uncontrolled optical denominator and cannot be disentangled from a morphology or bulge-fraction association. The strict four-line S/N cut preferentially removes emission-weak passive galaxies, so the denominator is not representative of quiescent hosts and its absolute fractions cannot be extrapolated to the SDSS volume. Broad optical BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, with no morphology, structural-proxy, aperture-fraction, or environment control; the star-forming control pool uses the conservative \citep{kauffmann2003bpt} demarcation, and the 67 unclassified objects are retained in denominator counts but excluded from control pairing. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex; the moderate mass--redshift caliper variant leaves the median essentially unchanged at -1.318 dex for 7,867 pairs. The stricter line-S/N ($S/N \geq 10$) variant yields -0.744 dex, while the Seyfert-like subset yields -0.763 dex after the lower-excitation tail is removed by the stricter cut, so the larger broad-denominator offset shrinks by more than 0.5 dex under the tighter excitation cuts. BPT classification is an optical excitation diagnostic, not a direct proxy for bolometric accretion power or Eddington ratio. The companion supplement inventories the missing structural, environmental, and multiwavelength observables needed for future real-data tests, including morphology, aperture fraction, halo or group labels, CO/HI gas measurements, radio and X-ray proxies, and IFU kinematics.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:31:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}. It is a selection-limited pilot subset used to estimate the association within the available SDSS cache, not a volume-limited census. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this non-random subset is not a random sky sample and introduces survey-plate and sky-coverage bias. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the subset is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:34:The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Although \texttt{PhotoObj} was joined in the catalog backbone, structural quantities such as \(R_{90}/R_{50}\) and \texttt{fracDeV} were not retained in the 60,000-galaxy cache, so morphology cannot be controlled in this cycle. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}. We use variance-normalized Euclidean matching, with each coordinate standardized by its sample standard deviation before distance calculation, because the feature space is only two variables, $(\log M_\star,z)$, so the rule stays transparent and the resulting nearest-neighbor control remains easy to interpret as an association baseline.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:55:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The intermediate/composite galaxies are retained in the denominator counts but are not part of the star-forming control pool used for matching. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing; this cycle does not tabulate a separate failure mode for them. Here, the star-forming control pool is defined as objects below the Kauffmann et al.\ (2003) demarcation, which is a conservative optical cut and may still include weak or obscured active-nucleus contaminants. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control by variance-normalized Euclidean distance in standardized $(\log M_\star,z)$ space, with replacement. In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), and the unrestricted Euclidean match has median absolute separations of 0.0045 dex in $\log M_\star$ and 0.00021 in redshift, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, accretion-luminosity proxy, or duty-cycle phase; these missing dimensions define follow-up requirements. The preferred estimate does not impose a maximum mass--redshift caliper; the caliper row in Table~\ref{tab:robust} is a sensitivity variant. The moderate mass--redshift caliper sensitivity variant uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:67:    \par\noindent\textbf{Morphology and aperture caveat.} Without controlling for structural morphology or aperture fraction, a median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fixed-size, morphology-uncontrolled optical denominator and fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology, structural proxies, or aperture fraction, the observed sSFR offset is highly degenerate with the known correlation between stellar mass and galaxy morphology and the transition from disk-dominated to bulge-dominated systems, including bulge prominence or central velocity dispersion associations \citep{schawinski2010,bluck2014,belfiore2016,piotrowska2022}. The lack of concentration-index or \texttt{fracDeV}-style structural matching limits the result's ability to separate bulge-linked structural associations from excitation-linked associations. Single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, so spatially resolved integral-field spectroscopy is required to resolve the aperture-morphology degeneracy \citep{penny2018,cheung2016,bundy2015}. Within the present data, the association is therefore still not separable from a morphology or bulge-fraction association. The robustness interval in Table~\ref{tab:robust} is a 95\% confidence interval on the median offset.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:104:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:108:\bibitem[Bluck et al.(2014)]{bluck2014} Bluck, A.~F.~L., Bruce, V.~A., Pilkington, K., et al. 2014, MNRAS, 441, 599
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:109:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:124:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:125:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:127:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:131:\bibitem[Penny et al.(2018)]{penny2018} Penny, S.~J., Davies, R.~L., Houghton, R.~C.~W., et al. 2018, MNRAS, 476, 979
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex:141:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:19:The main paper measures an optical association between BPT classification and catalog sSFR. These eight entries are distinct baseline-and-follow-up atlas notes: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the entries span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. For consistency with the flagship, the atlas uses the broad optical BPT-selected family when the full optical-emission-line denominator is meant and names specific subsets only when the stricter selection matters. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. These are missing observables in the present catalog and are required for future mechanism tests. This is an association-only optical baseline atlas and a single internal follow-up checklist for future causal inference, not a collection of standalone mechanism papers.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:22:The atlas uses the same analyzed public-data backbone as the main paper: 60,000 galaxies in a fixed, selection-limited subset from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, i.e. 24.0\% sample coverage. The four-line selection is sSFR-dependent and the sample is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The galaxy-by-galaxy stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. Although \texttt{PhotoObj} was joined in the catalog backbone, structural quantities such as \(R_{90}/R_{50}\) and \texttt{fracDeV} were not retained in the 60,000-row cache, so morphology cannot be controlled in this cycle. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:78:See Table~\ref{tab:atlas-summary}; we isolate the broad optical BPT-selected duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the broad optical BPT-selected fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The broad optical BPT-selected fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. This optical fraction represents an observational baseline pool, not the active maintenance-heating duty cycle. See the next subsection for the related radio-jet baseline that uses the same projected-density proxy. The follow-up ingredients are X-ray cavity or cooling-luminosity measurements \citep{fabian2012}, calibrated radio jet mechanical powers \citep[e.g.,][]{best2005,hardcastle2020}, halo-selected parent catalogues, and nondetection modelling. Those observables are missing here; this entry remains an optical baseline only, and future follow-up requires those real observables before any physical inference. Optical broad BPT selection primarily traces the radiative-mode denominator, so it cannot isolate the mechanically dominated jet-mode population without contemporaneous X-ray and radio measurements \citep{heckmanbest2014}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:89:See Table~\ref{tab:atlas-summary}; we isolate the high-excitation broad optical BPT-selected denominator that resolved kinematics would need to test escape versus recycling. High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The follow-up ingredients are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers. Without IFU kinematics to decouple non-circular outflow components from host rotation, optical excitation alone cannot determine whether the gas exceeds the halo escape speed \citep{harrison2018}. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:133:See Table~\ref{tab:atlas-summary}; we define the denominator for CO/HI gas-fraction and depletion-time follow-up. Using the gas-depletion note's low-sSFR baseline, the massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. This denominator is note-specific and should not be conflated with the \(\log M_\star \geq 10.8\) maintenance-heating subset summarized above. Its broad optical BPT-selected fraction is 0.549, and the median H-alpha luminosity proxy is \(\log (L_{\mathrm{H}\alpha}/\mathrm{erg\,s^{-1}}) = 40.06\). Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value rather than raw fiber flux; that catalog-level correction extrapolates the fiber measurement beyond the aperture in a model-dependent way and assumes line emission broadly tracks the broadband light profile. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency or measure total cold-gas mass \citep{tacconi2018}; this note identifies the CO/HI follow-up denominator and optical baseline required for spatially resolved gas tests. The follow-up ingredients are global CO or dust-based molecular gas masses \citep[e.g., xCOLD GASS;][]{xcoldgass2017}, atomic hydrogen masses \citep[e.g., xGASS;][]{xgass2018}, aperture-matched SFRs, morphology, and environment labels, together with radio, X-ray, and IFU observables that are still missing here. As with any H$\alpha$-based proxy, residual dust attenuation and stellar-absorption systematics can still affect the optical denominator, so this value should be read as a line-luminosity proxy rather than a direct total cold-gas-mass measurement. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference. No mock, synthetic, fake, placeholder, or toy data were used in compiling this atlas.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:162:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:165:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:167:\bibitem[Hardcastle \& Croston(2020)]{hardcastle2020} Hardcastle, M.~J., \& Croston, J.~H. 2020, New Astronomy Reviews, 88, 101539
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:168:\bibitem[Harrison et al.(2018)]{harrison2018} Harrison, C.~M., Costa, T., Tadhunter, C.~N., et al. 2018, Nature Astronomy, 2, 198
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:176:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:177:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:178:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:183:\bibitem[Tacconi et al.(2018)]{tacconi2018} Tacconi, L.~J., Genzel, R., Saintonge, A., et al. 2018, ApJ, 853, 179
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:185:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579

codex
I’ve confirmed the main numbers are in the local run JSON. I’m doing a static citation-key check now so I can say whether the TeX is likely to compile cleanly or whether there are unresolved bibliography references lurking behind the prose.
exec
/bin/zsh -lc "perl -ne 'while(/\\\\cite(?:p|t)?(?:\\[["'^'"\\]]*\\])?(?:\\[["'^'"\\]]*\\])?\\{(["'^}]*)'"\\}/g){print \""'$1'"\\n\"}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | tr ',' '\\n' | sed 's/"'^ *//;s/ *$//'"' | sort -u" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
baldwin1981
belfiore2016
best2005
bluck2014
brinchmann2004
bundy2015
carniani2017
cheung2016
cicone2014
cidfernandes2011
dekel2006
eagle2015
ellison2011
ellison2021
fabian2012
fiore2017
hardcastle2020
harrison2017
harrison2018
heckmanbest2014
kauffmann2003bpt
kewley2001
kewley2005
kewley2006
lamassa2013
mcnamara2007
peng2010
penny2018
piotrowska2022
schawinski2010
sdssdr17
simba2019
stasinska2008
stasinska2015
tacconi2018
tng2019
veilleux2005
wetzel2013
xcoldgass2017
xgass2018
york2000

exec
/bin/zsh -lc "perl -ne 'if(/"'^'"\\\\bibitem.*\\}\\{(["'^}]+)'"\\}/){print \""'$1'"\\n\"}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | sort -u" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
exec
/bin/zsh -lc "python3 -c \"import json,pathlib; p=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json'); d=json.load(p.open()); print(d['bpt_counts']); print(d['matched_pairs'], d['matched_delta_log_sSFR_median_dex'], d['matched_delta_log_sSFR_median_ci95_bootstrap'], d['match_abs_delta_logM_median'], d['match_abs_delta_z_median'])\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-wai0lfDJ' (errno=Operation not permitted)
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-iiS8y8hG' (errno=Operation not permitted)
{'star-forming': 39553, 'intermediate': 12234, 'agn': 8146, 'unclassified': 67}
8146 -1.3088869999999995 [-1.3341385500000003, -1.2821399375] 0.0044599999999999085 0.00021079499999999973

exec
/bin/zsh -lc "python3 -c \"import csv,pathlib; p=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv'); n=0; import collections; c=collections.Counter(); f=p.open(); r=csv.DictReader(f); 
for row in r:
    n+=1
    c[row['bpt_label']] += 1
print(n); print(c)\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 293ms:
60000
Counter({'star-forming': 39553, 'intermediate': 12234, 'agn': 8146, 'unclassified': 67})

codex
The bibliography keys appear to be present, so I’m switching to provenance of the robustness rows. The key question there is not whether the numbers are plausible, but whether they’re backed by a local artifact or just narrated from prior runs.
exec
/bin/zsh -lc "rg -n '7867|7419|1530|2114|0\\.744|0\\.763|96\\.6|matched_pairs|caliper|S/N' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json:14:    "matched_pairs_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json:60:  "matched_pairs": 8146,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:36:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:37:four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:38:four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:43:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:58:\item Broad BPT optical AGN vs. star-forming controls at S/N$\geq3$: $N=8,146$ matched pairs, median $\Delta\log {\rm sSFR}=-1.309$ dex with 95\% bootstrap interval $[-1.334,-1.283]$ dex.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:59:\item Moderate mass-redshift caliper $|\Delta\log M_\star|\leq0.05$, $|\Delta z|\leq0.002$: $N=7,867$ retained pairs (96.6\% target coverage), median offset -1.318 dex.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:61:\item Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to -0.744 dex, showing sensitivity to the emission-line selection function.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:62:\item A narrower [N II] Seyfert-like proxy gives $N=2,114$ pairs and median offset -0.763 dex, reinforcing that subclass definitions change the effect size.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json:14:    "matched_pairs_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json:60:  "matched_pairs": 8146,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:25:All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:36:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:37:four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:38:four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:43:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:58:\item Broad BPT optical AGN vs. star-forming controls at S/N$\geq3$: $N=8,146$ matched pairs, median $\Delta\log {\rm sSFR}=-1.309$ dex with 95\% bootstrap interval $[-1.334,-1.283]$ dex.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:59:\item Moderate mass-redshift caliper $|\Delta\log M_\star|\leq0.05$, $|\Delta z|\leq0.002$: $N=7,867$ retained pairs (96.6\% target coverage), median offset -1.318 dex.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:61:\item Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to -0.744 dex, showing sensitivity to the emission-line selection function.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:62:\item A narrower [N II] Seyfert-like proxy gives $N=2,114$ pairs and median offset -0.763 dex, reinforcing that subclass definitions change the effect size.

exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/FLAGSHIP_REVIEW_DECISION_20260709T013510Z.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# Flagship review and package decision

Marker: `FLAGSHIP_REVIEW_DECISION_20260709T013510Z`

## User directive

Proceed with the recommended next decision after the 9-paper local integration run.

## Reviewed artifacts

- Integration handoff: `INTEGRATION_HANDOFF.md`
- Integration audit: `INTEGRATION_AUDIT.md`
- RP-1 integrated TeX/PDF/source JSON
- 8 guarded proxy/denominator TeX/PDF/source JSON records
- Shared selection-function, representativeness, and Goru robustness outputs already folded into the integration run

## Decision

Proceed with **one flagship paper plus one supplementary denominator/proxy atlas**, not 9 standalone papers.

### Approved flagship candidate

`m1_rp1_sdss_agn_sfr`

Why:

- It has the clearest direct measurement in the available data: a catalog-sSFR offset for broad optical BPT AGN hosts relative to mass-redshift matched star-forming controls.
- It has a real row-level SDSS DR17 analysis table, BPT classifications, matching design, robustness checks, and figures.
- It can be written honestly as an association/selection-aware SDSS short paper.
- The result is strong enough to polish locally: median delta log sSFR = -1.309 dex for 8,146 matched pairs, with bootstrap interval [-1.334, -1.283] dex.

Required flagship guard:

- The paper must not claim causal AGN feedback.
- It must foreground the capped/non-random cache and four-line emission-line selection.
- It must explicitly state subclass and S/N sensitivity: S/N>=10 and narrower Seyfert-like proxies reduce the median offset magnitude.

### Not approved as standalone physical-feedback papers

The other 8 drafts should not stay as independent papers because each lacks at least one core physical observable required by its original proposal:

- `m1_rp2_environment_quenching`: lacks group/halo and central-satellite information.
- `m1_rp3_maintenance_heating`: lacks radio jets, X-ray cavities, cooling luminosity, and halo gas.
- `m2_p1_outflow_escape_recycling`: lacks resolved outflow velocities and multiphase gas/CGM tracers.
- `m2_p2_radio_jet_environment`: lacks radio jet and hot-gas coupling measurements.
- `m2_p3_feedback_transition_mass`: lacks gas fractions, baryon deficits, halo masses, and high-redshift extension.
- `m3_p1_multiphase_census`: lacks molecular/neutral/X-ray/radio phases.
- `m3_p2_gas_depletion_efficiency`: lacks CO/HI/dust gas masses and aperture-matched gas depletion times.
- `m3_p3_simulation_validation`: lacks forward-modelled simulation mocks.

### Packaging decision

Package the other 8 as **supplementary denominator/proxy notes under one combined atlas**, not standalone claims.

Reason:

- Their shared value is methodological: they define denominators, target vectors, proxy baselines, and missing-observable checklists for follow-up.
- A combined supplement prevents overclaiming while preserving the useful work.
- It keeps the public/science narrative simple: one flagship SDSS result, one transparent atlas of what the current data can and cannot support.

## Action authorized locally by this decision

Create a local-only decision package with:

1. A polished RP-1 flagship AASTeX source/PDF.
2. A combined supplementary denominator/proxy atlas AASTeX source/PDF for the other 8.
3. A compile/audit manifest with hashes.

Do not publish, mirror, replace public PDFs, write DB/API/page_versions, deploy/restart, git commit/push/merge, create cron jobs, change billing/OAuth/API keys, or externally submit.

exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "analysis_rows": 60000,
  "bpt_counts": {
    "agn": 8146,
    "intermediate": 12234,
    "star-forming": 39553,
    "unclassified": 67
  },
  "data_release": "SDSS DR17 SkyServer via astroquery.sdss",
  "files": {
    "analysis_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
    "figure1_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/figures/figure1_bpt.pdf",
    "figure2_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/figures/figure2_matched_offsets.pdf",
    "matched_pairs_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv",
    "raw_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv"
  },
  "group_medians": {
    "agn": {
      "median_logM": 10.79099,
      "median_log_sSFR": -11.769829999999999,
      "median_u_minus_r": 2.7576649999999994,
      "median_z": 0.075976265,
      "n": 8146
    },
    "intermediate": {
      "median_logM": 10.62895,
      "median_log_sSFR": -10.8564,
      "median_u_minus_r": 2.5431500000000007,
      "median_z": 0.079609505,
      "n": 12234
    },
    "star-forming": {
      "median_logM": 10.01737,
      "median_log_sSFR": -9.909236,
      "median_u_minus_r": 1.814429999999998,
      "median_z": 0.06887668,
      "n": 39553
    },
    "unclassified": {
      "median_logM": 10.87501,
      "median_log_sSFR": -12.06685,
      "median_u_minus_r": 2.8580700000000014,
      "median_z": 0.08311625,
      "n": 67
    }
  },
  "match_abs_delta_logM_median": 0.0044599999999999085,
  "match_abs_delta_z_median": 0.00021079499999999973,
  "match_distance_scaled_median": 0.013706693336996863,
  "matched_delta_log_sSFR_mean_ci95_bootstrap": [
    -1.2194772019150502,
    -1.1835793853118095
  ],
  "matched_delta_log_sSFR_mean_dex": -1.201557615885097,
  "matched_delta_log_sSFR_median_ci95_bootstrap": [
    -1.3341385500000003,
    -1.2821399375
  ],
  "matched_delta_log_sSFR_median_dex": -1.3088869999999995,
  "matched_pairs": 8146,
  "ols_adjusted_for_logM_z": {
    "coef_is_agn_ci95": [
      -1.2103153323534461,
      -1.1873688115826728
    ],
    "coef_is_agn_log_sSFR_dex": -1.1988420719680595,
    "coef_is_agn_se": 0.005853704278258507,
    "coef_logM": -0.6590074792789541,
    "coef_z": 6.926838817644406,
    "n_regression": 47699
  },
  "query_top_n": 60000,
  "raw_rows": 60000,
  "revision_marker": "AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z",
  "run_id": "SDSS_AGN_SFR_PILOT_20260708T122000Z",
  "safety": "read-only public SDSS query; local artifact writes only; no DB/API/page_versions/live wiki publish/deploy/git/cron"
}
exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS optical AGN/sSFR matched-control pilot}
\shortauthors{NebulaMind local integration}
\begin{document}

\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot}
\author{NebulaMind Research Autopilot}
\affiliation{Local reproducible integration run; public SDSS DR17 data only}

\begin{abstract}
We integrate the strongest Galaxy Evolution pilot into a selection-aware short-paper draft: a matched-control comparison of catalog specific star formation in broad BPT optical AGN hosts and star-forming controls in SDSS DR17. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a flagship short-paper draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Purpose and claim contract}\label{sec:purpose}
This is the flagship local integration draft. It tests an optical-classification-associated catalog-sSFR offset, not causal AGN feedback, gas depletion, or halo maintenance heating.

The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.

The preferred estimator matches every broad optical AGN host to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. This is an association design; controls are not matched in morphology, halo mass, gas mass, aperture scale, AGN luminosity, or duty-cycle phase.

\begin{itemize}
\item Broad BPT optical AGN vs. star-forming controls at S/N$\geq3$: $N=8,146$ matched pairs, median $\Delta\log {\rm sSFR}=-1.309$ dex with 95\% bootstrap interval $[-1.334,-1.283]$ dex.
\item Moderate mass-redshift caliper $|\Delta\log M_\star|\leq0.05$, $|\Delta z|\leq0.002$: $N=7,867$ retained pairs (96.6\% target coverage), median offset -1.318 dex.
\item A deterministic no-replacement diagnostic uses $N=7,419$ pairs and gives median offset -1.446 dex, but with visibly poorer mass balance; it is a stress test, not the preferred estimator.
\item Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to -0.744 dex, showing sensitivity to the emission-line selection function.
\item A narrower [N II] Seyfert-like proxy gives $N=2,114$ pairs and median offset -0.763 dex, reinforcing that subclass definitions change the effect size.
\end{itemize}


\begin{figure*}
\centering
\includegraphics[width=0.73\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used by the flagship RP-1 integration. This figure verifies the measured line-ratio denominator and broad optical classification; it does not by itself identify causal AGN feedback.}
\label{fig:bpt}
\end{figure*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
\label{fig:offsets}
\end{figure*}


\section{Reproducibility and safety}\label{sec:repro}
This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.

\section{Conclusion}\label{sec:conclusion}
The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579

\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
\end{thebibliography}

\end{document}

codex
I’m checking a representative subset of the supplement’s topic-level numbers against the per-topic source analyses. If those line up, I can treat the atlas as provenance-safe and focus only on any wording or packaging risks.
exec
/bin/zsh -lc "rg -n \"3456|2710|0\\.230|0\\.181|0\\.041|0\\.059|0\\.032|0\\.004|9,298|5,695|0\\.430|0\\.607|4,440|0\\.074|6,729|40\\.06|0\\.549|0\\.136|0\\.418|3\\.1|11\\.0|12\\.5|15 cells|n >= 50|0\\.005|0\\.729|0\\.003|0\\.520\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/*/data/source_analysis_results.json | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/data/source_analysis_results.json:11:    "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/data/source_analysis_results.json:12:    "The widest-to-narrowest prevalence ratio is 3.1, before adding molecular, neutral, or X-ray/radio phases.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/data/source_analysis_results.json:46:      "fraction": 0.4182666666666667,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:7:    0.5202082816761716
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:17:    "10.5-11.0",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:18:    "11.0-12.5"
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:21:  "peak_agn_fraction": 0.5202082816761716,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:22:  "peak_agn_mass_bin": "11.0-12.5",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:26:    0.005283204324855633,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:30:    0.7292338209769402
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:33:    "The first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:34:    "The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:42:  "transition_mass_bin_quenched_fraction_gt_0p5": "11.0-12.5"
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:4:    0.5202082816761716
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:14:    0.005283204324855633,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:15:    0.7292338209769402
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:18:    "The pilot writes 15 mass-redshift cells with n >= 50 as a compact validation vector.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:19:    "Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:73:      "quenched_fraction": 0.003200731595793324,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:102:      "mass_bin": "10.5-11.0",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:110:      "mass_bin": "10.5-11.0",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:118:      "mass_bin": "10.5-11.0",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:126:      "mass_bin": "11.0-12.5",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:134:      "mass_bin": "11.0-12.5",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:142:      "mass_bin": "11.0-12.5",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json:13:  "median_log_lha_denominator": 40.06117405071403,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json:19:    "The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json:20:    "Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json:6:    "fraction": 0.074,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json:18:    "High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json:10:    "se": 0.005134068554795429
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json:13:    "fraction": 0.6073748902546093,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json:24:    "The massive subset (logM >= 10.8) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json:25:    "The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json:47:  "match_abs_delta_logM_median": 0.0044599999999999085,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json:67:    "coef_is_agn_se": 0.005853704278258507,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:6:    "fraction": 0.2304,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:7:    "k": 3456,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:9:    "se": 0.003438176260752203
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:13:    0.059135
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:18:    "k": 2710,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:20:    "se": 0.0031414033193486656
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:22:  "lpm_high_density_coeff": 0.03249480778035638,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:23:  "lpm_high_density_se": 0.003707733046841099,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:29:    "The high-density quartile has quenched fraction 0.230 (3,456/15,000); the low-density quartile has 0.181 (2,710/15,000).",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:30:    "The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json:31:    "A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004."

exec
/bin/zsh -lc "perl -ne 'while(/\\\\cite(?:p|t)?(?:\\[["'^'"\\]]*\\])?(?:\\[["'^'"\\]]*\\])?\\{(["'^}]*)'"\\}/g){print \""'$1'"\\n\"}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | tr ',' '\\n' | sed 's/"'^ *//;s/ *$//'"' | sort -u > /dev/null; echo ok" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
ok

exec
/bin/zsh -lc "rg -n \"topic-01|topic-02|topic-03|topic-04|topic-05|topic-06|topic-07|topic-08\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/*/data/source_analysis_results.json | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
exec
/bin/zsh -lc "rg -n \"bad_mock_or_synthetic_data_use|forbidden mock|No mock, synthetic\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_19_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_39_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_RESPONSE.md:23:- No mock, synthetic, placeholder, or toy data language was added beyond the existing real-data guardrails.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_RESPONSE.md:20:- No mock, synthetic, placeholder, or toy data were added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_20_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_20_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_20_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_20_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_RESPONSE.md:21:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_21_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_RESPONSE.md:15:- No mock, synthetic, placeholder, or toy data were added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_RESPONSE.md:12:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_33_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_33_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_RESPONSE.md:17:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_RESPONSE.md:15:- No mock, synthetic, placeholder, toy, or invented real-data values were added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_29_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_33_ACTUAL_RESEARCH_RESPONSE.md:11:- No mock, synthetic, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_24_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_24_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_24_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_24_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_36_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_37_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_18_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_28_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_28_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_27_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_RESPONSE.md:13:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_15_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_24_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_24_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_06_ACTUAL_RESEARCH_RESPONSE.md:17:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_AUDIT.json:42:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_AUDIT.json:43:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_25_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_07_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_32_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_34_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_35_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_35_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_35_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_35_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_13_ACTUAL_RESEARCH_RESPONSE.md:10:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_02_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_22_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_SUMMARY.json:43:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_30_ACTUAL_RESEARCH_SUMMARY.json:44:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_16_ACTUAL_RESEARCH_RESPONSE.md:19:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_38_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_31_ACTUAL_RESEARCH_RESPONSE.md:20:- No mock, synthetic, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/CYCLE_23_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],

codex
ACTUAL_RESEARCH_CODEX_KUN_REVIEW_CYCLE_40

**Findings**
- No blocking issues found in this read-only review.
- The core RP1 numbers are traceable to the local run artifacts: `[analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json)` records `60000` rows, BPT counts of `39553 / 12234 / 8146 / 67`, `8146` matched pairs, median `-1.3088869999999995` dex, and bootstrap CI `[-1.33413855, -1.2821399375]`.
- The matched-pair file is consistent with that summary: `[matched_agn_sf_pairs.csv](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv)` has `8146` rows and the expected pairwise columns.
- The manuscript text itself matches the run outputs, especially in `[rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13)` and `[rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L55)`, where the counts, offset, and CI are stated consistently.
- The supplement’s topic-level numbers are likewise traceable to per-topic local source analyses, for example `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json)`, and `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json)`. The headline values in `[supplementary_denominator_atlas.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L19)` and later subsections line up with those artifacts.
- I did not find forbidden mock/synthetic/toy/placeholder data use in the manuscript content. The `rg` hits are overwhelmingly in historical audit files and review responses, not in the actual TeX manuscripts.

**Compile / TeX**
- Static pass looks clean: figure paths are present in the package, and the cited keys used in both TeX files appear to have matching `\bibitem`s in the inlined bibliography.
- `[PACKAGE_AUDIT.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/PACKAGE_AUDIT.md)` reports `pdfs_ok: 2`, `logs_ok: 2`, `fatal_failures: 0`.

**Residual risk**
- I did not run a fresh LaTeX build in this read-only sandbox, so there is still a small chance of a class/package-specific compile issue that static inspection would miss.
- The main substantive risk is not compilation, but interpretation, the manuscript correctly keeps the result association-only, so that boundary should stay intact in any later edit.

If you want a stricter second pass, I can do a line-by-line provenance crosswalk for every numeric claim in the supplement against its specific `source_analysis_results.json` file.
tokens used
128,965
ACTUAL_RESEARCH_CODEX_KUN_REVIEW_CYCLE_40

**Findings**
- No blocking issues found in this read-only review.
- The core RP1 numbers are traceable to the local run artifacts: `[analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json)` records `60000` rows, BPT counts of `39553 / 12234 / 8146 / 67`, `8146` matched pairs, median `-1.3088869999999995` dex, and bootstrap CI `[-1.33413855, -1.2821399375]`.
- The matched-pair file is consistent with that summary: `[matched_agn_sf_pairs.csv](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv)` has `8146` rows and the expected pairwise columns.
- The manuscript text itself matches the run outputs, especially in `[rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13)` and `[rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L55)`, where the counts, offset, and CI are stated consistently.
- The supplement’s topic-level numbers are likewise traceable to per-topic local source analyses, for example `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/data/source_analysis_results.json)`, `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json)`, and `[source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json)`. The headline values in `[supplementary_denominator_atlas.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L19)` and later subsections line up with those artifacts.
- I did not find forbidden mock/synthetic/toy/placeholder data use in the manuscript content. The `rg` hits are overwhelmingly in historical audit files and review responses, not in the actual TeX manuscripts.

**Compile / TeX**
- Static pass looks clean: figure paths are present in the package, and the cited keys used in both TeX files appear to have matching `\bibitem`s in the inlined bibliography.
- `[PACKAGE_AUDIT.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_40_package/PACKAGE_AUDIT.md)` reports `pdfs_ok: 2`, `logs_ok: 2`, `fatal_failures: 0`.

**Residual risk**
- I did not run a fresh LaTeX build in this read-only sandbox, so there is still a small chance of a class/package-specific compile issue that static inspection would miss.
- The main substantive risk is not compilation, but interpretation, the manuscript correctly keeps the result association-only, so that boundary should stay intact in any later edit.

If you want a stricter second pass, I can do a line-by-line provenance crosswalk for every numeric claim in the supplement against its specific `source_analysis_results.json` file.


# command_result
exit_code=0
elapsed_s=238.0
timed_out=False
finished_utc=2026-07-09T19:23:08Z
