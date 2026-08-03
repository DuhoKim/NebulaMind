# codex-kun-readonly-cycle-16
Started UTC: 2026-07-09T16:12:13Z
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
session id: 019f47a6-ae4f-7093-95ae-9d7a77ebd20c
--------
user
Review this local manuscript package in read-only mode.

Output marker: ACTUAL_RESEARCH_CODEX_KUN_REVIEW_CYCLE_16

You are Kun/Codex: reproducibility, TeX, provenance, and no-mock-data audit.

Read only these roots unless needed for harmless metadata checks:
- candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package
- real-data inventory: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/real-data-inventory/REAL_DATA_INVENTORY_CYCLE_16.json
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
I’m going to inspect the candidate package, the inventory, and the integrated context to verify the stated counts and look for TeX/reproducibility risks. Then I’ll check for any mock-data language or numeric claims that are not grounded in local files or cited sources.
exec
/bin/zsh -lc 'cat /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/real-data-inventory/REAL_DATA_INVENTORY_CYCLE_16.json' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "counts": {
    "csv_files": 35,
    "integrated_tex_files": 9,
    "json_files": 167,
    "pdf_files": 43
  },
  "created_utc": "2026-07-09T16:12:13Z",
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
  "cycle": 16,
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
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
      "sha256": "0cab9f8bd9614a68ed067043f211be6f4d0372ca97c8d41004b3c9fb49da9583",
      "title": "Optical-AGN denominator for maintenance-heating follow-up: selection-aware SDSS optical proxy integration"
    },
    {
      "abstract": "We integrate the active proposal 'Escape versus recycling: the fate of AGN-driven multiphase outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "bytes": 9180,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
      "sha256": "53136bb1594ca816064601098db5378e48d276d2ed27561911c7560201d2c90f",
      "title": "SDSS high-excitation AGN denominator for outflow escape tests: selection-aware SDSS optical proxy integration"
    },
    {
      "abstract": "We integrate the active proposal 'Environmental dependence of radio-jet coupling efficiency in galaxy gas' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "bytes": 9039,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
      "sha256": "560b68a8e59f35d9195c18216618a5491d3683cb13120c06ce10a27ad2b23e4e",
      "title": "Environment proxy for optical AGN in massive SDSS hosts: selection-aware SDSS optical proxy integration"
    },
    {
      "abstract": "We integrate the active proposal 'Locating the transition from stellar-feedback to AGN-feedback regulation' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "bytes": 9247,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
      "sha256": "b7916767462d58a17c5aa36371e5857d802fa6c685ffddb23f326dcd817495b3",
      "title": "SDSS mass transition in quenching and optical AGN incidence: selection-aware SDSS optical proxy integration"
    },
    {
      "abstract": "We integrate the active proposal 'A multiphase, common-denominator census of AGN-driven outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "bytes": 9303,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
      "sha256": "24c8adf2a69c03a0c942f1c10c9ee873d1cd2450d4e63e0c8449954995063204",
      "title": "Common-denominator optical tracer census in SDSS: selection-aware SDSS optical proxy integration"
    },
    {
      "abstract": "We integrate the active proposal 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "bytes": 9313,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
      "sha256": "c5ac387b4b6aea82f434889b58cc9ea99896e1fbc8c3390ba6950babbde54c9d",
      "title": "Optical denominator for gas-fraction versus efficiency tests: selection-aware SDSS optical proxy integration"
    },
    {
      "abstract": "We integrate the active proposal 'Forward-modelled validation of cosmological feedback prescriptions' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "bytes": 9357,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex",
      "sha256": "1486032a4182c2203a5a3f18546e712b7a9489a8b357a085f98b0b5ae0d48784",
      "title": "SDSS target vector for feedback-model validation: selection-aware SDSS optical proxy integration"
    }
  ],
  "json_files": [
    {
      "bytes": 3111,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json",
      "sha256": "668ad7a67290600ff5028ae587d32ef239a09bd8627a480539f37e1927d659df",
      "top_keys": [
        "run_id",
        "revision_marker",
        "data_release",
        "query_top_n",
        "raw_rows",
        "analysis_rows",
        "bpt_counts",
        "group_medians",
        "matched_pairs",
        "matched_delta_log_sSFR_median_dex",
        "matched_delta_log_sSFR_mean_dex",
        "matched_delta_log_sSFR_median_ci95_bootstrap",
        "matched_delta_log_sSFR_mean_ci95_bootstrap",
        "match_distance_scaled_median",
        "match_abs_delta_logM_median",
        "match_abs_delta_z_median",
        "ols_adjusted_for_logM_z",
        "files",
        "safety"
      ]
    },
    {
      "bytes": 11554,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json",
      "sha256": "d3999062a83c676b89cf47e6368dfe07008e23d652be438983d8db25113c7031",
      "top_keys": [
        "run_id",
        "source_csv",
        "topics"
      ]
    },
    {
      "bytes": 2155,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp2_environment_quenching/analysis_results.json",
      "sha256": "c0421620f67f3c227955affa3f4c1876cb85f8b31874d219f2cd2e35a7f9cec0",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "high_density_quenched",
        "high_minus_low_ci",
        "interpretation_guard",
        "low_density_quenched",
        "lpm_high_density_coeff",
        "lpm_high_density_se",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 1998,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/analysis_results.json",
      "sha256": "06291f82c3fbe0f7fe84f7249568882ca4fa44972bcc25a55e367ef1fdcc7e6e",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "massive_agn_fraction",
        "massive_quenched_agn_fraction",
        "massive_quenched_rows",
        "massive_rows",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 1827,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p1_outflow_escape_recycling/analysis_results.json",
      "sha256": "44b2407aa691d64fd6de22eb49a8c0a185c86bb1f3b538c7bf066e904d0a3210",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "high_excitation_agn",
        "interpretation_guard",
        "median_log_sSFR_all",
        "median_log_sSFR_high_excitation",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 1957,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p2_radio_jet_environment/analysis_results.json",
      "sha256": "4e1ff701bb5b98af4945d5adad2e543e00005e1ab3907e8fae7d15e70c93e351",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "high_density_massive_agn",
        "high_minus_low_ci",
        "interpretation_guard",
        "low_density_massive_agn",
        "massive_rows",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 2112,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p3_feedback_transition_mass/analysis_results.json",
      "sha256": "204ec46dc838e5e69a34b4dc2f790cb0b5e0f7fc1cb4eaa71f830779a2c92b67",
      "top_keys": [
        "agn_fraction_by_mass",
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "mass_bin_labels",
        "method",
        "peak_agn_fraction",
        "peak_agn_mass_bin",
        "pilot_question",
        "proposal_title",
        "quenched_fraction_by_mass",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample",
        "transition_mass_bin_quenched_fraction_gt_0p5"
      ]
    },
    {
      "bytes": 2375,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p1_multiphase_census/analysis_results.json",
      "sha256": "e711563011102657b6d5cab279c1b2ab7ed087dfc734e50932ad4edfe90d0683",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "method",
        "pilot_question",
        "prevalence_ratio_widest_to_narrowest",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample",
        "tracer_prevalence"
      ]
    },
    {
      "bytes": 2101,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p2_gas_depletion_efficiency/analysis_results.json",
      "sha256": "42965b6f359c23b56098f5f9845561f4a4a2ba81e1e00df09fbae4acf3bcc2d9",
      "top_keys": [
        "agn_fraction_in_denominator",
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "massive_transition_quenched_rows",
        "median_log_lha_denominator",
        "median_log_lha_offset_vs_massive_sf",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 5079,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json",
      "sha256": "6f289f8c68da425eb3d8005e673bf5c5c02cf917eaa2bc6feedd053535de8f52",
      "top_keys": [
        "agn_fraction_range",
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "method",
        "pilot_question",
        "proposal_title",
        "quenched_fraction_range",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample",
        "target_vector_cells"
      ]
    },
    {
      "bytes": 5940,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/artifacts/goru_actual_data_robustness_20260708T141459Z.json",
      "sha256": "a38f9863060660f595163c02e959f2fb01e19a49c2faf56d366511a14735ac5d",
      "top_keys": [
        "base_counts",
        "bpt_sensitivity_rows",
        "compiled_pdf_entries",
        "csv_entries",
        "density_k10_diff",
        "figure_entries",
        "inventory_rows",
        "marker",
        "matched_baseline",
        "matched_rows",
        "matched_sn10",
        "matched_sn5",
        "outputs",
        "proxy_limits",
        "safety",
        "sample_count_rows",
        "sn_redshift_mass_rows",
        "source_csv",
        "target_vector_rows",
        "timestamp_utc"
      ]
    },
    {
      "bytes": 6610,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/artifacts/goru_bpt_flux_error_mc_20260708T232006Z.json",
      "sha256": "54af58dc5ff3424442ad2b448ace62e25739049230fc097a034a71ada1bef0ad",
      "top_keys": [
        "key_results",
        "marker",
        "matched_pairs_csv",
        "matched_pairs_csv_sha256",
        "method",
        "outputs",
        "proxy_limits",
        "row_counts",
        "safety",
        "source_csv",
        "source_csv_sha256",
        "timestamp_utc"
      ]
    },
    {
      "bytes": 2657,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/artifacts/goru_literature_wave3_validation_20260708T170557Z.json",
      "sha256": "69f8bf15118bae78f3004d795125cc8bd62e69b639ec0910f89e8c742f6ca1cd",
      "top_keys": [
        "arxiv_fetch_errors",
        "availability_counts",
        "coverage_ready",
        "dedupe_keys_unique",
        "duplicate_dedupe_keys",
        "gate",
        "jsonl_parse_ok",
        "jsonl_rows",
        "marker",
        "missing_ads_records",
        "raw_payload_files_exist",
        "records_by_paper_role_credit",
        "row_count_matches_summary",
        "safety_no_write_boundaries",
        "summary_records_total",
        "utc"
      ]
    },
    {
      "bytes": 10967,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/artifacts/goru_matching_control_robustness_20260708T205859Z.json",
      "sha256": "8fb9d9cb6a52a4068ad78009af8cc7583a42f03aabe068077f59c86caa186b45",
      "top_keys": [
        "key_results",
        "marker",
        "outputs",
        "proxy_limits",
        "row_counts",
        "safety",
        "sn_threshold_counts",
        "source_csv",
        "source_results_analysis_rows",
        "source_results_bpt_counts",
        "source_rows",
        "timestamp_utc"
      ]
    },
    {
      "bytes": 6198,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/artifacts/goru_regression_bin_sensitivity_20260708T183643Z.json",
      "sha256": "f1c22938a259c3f73c6f6dfd94b626699549fcb6f3f58c6b5b433149a7c96422",
      "top_keys": [
        "key_results",
        "marker",
        "outputs",
        "proxy_limits",
        "row_counts",
        "safety",
        "sn_threshold_counts",
        "source_csv",
        "source_results_analysis_rows",
        "source_results_bpt_counts",
        "source_rows",
        "timestamp_utc"
      ]
    },
    {
      "bytes": 9548,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/artifacts/goru_stratified_bpt_robustness_20260708T162615Z.json",
      "sha256": "bacc5b41fcb40158631863238ee60bb99faab2df16fe1fbaf4de5431848818d3",
      "top_keys": [
        "boundary_near_counts_sn3",
        "marker",
        "matched_bpt_agn_baseline_sn3",
        "matched_bpt_agn_sn10",
        "matched_high_excitation_y_gt_0p25_sn3",
        "matched_nii_seyfert_like_proxy_sn3",
        "outputs",
        "proxy_limits",
        "row_counts",
        "safety",
        "selection_overlay",
        "sn_threshold_counts",
        "source_csv",
        "source_results_analysis_rows",
        "source_results_bpt_counts",
        "source_rows",
        "timestamp_utc"
      ]
    },
    {
      "bytes": 4075,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/cached_public_representativeness_manifest_20260708T220242Z.json",
      "sha256": "46907940c551be4b2810586cd9a9799e501e7e18716d1770cbd00e0a13ad597e",
      "top_keys": [
        "artifacts",
        "manifest_self_hash_note",
        "marker",
        "raw_payload_count_json",
        "raw_payload_count_sql",
        "safety",
        "scope",
        "timestamp_utc",
        "verification"
      ]
    },
    {
      "bytes": 10072,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/cached_public_representativeness_summary_20260708T220242Z.json",
      "sha256": "38867993c98180541734bdd8a40c278efb9e71f9ffea82b55c32e7b2a48d4c03",
      "top_keys": [
        "cached_total",
        "dimension_summary",
        "flagged_bins",
        "global_cached_coverage",
        "marginal_rows",
        "marker",
        "public_total",
        "safety",
        "sdss_endpoint",
        "source_csv",
        "timestamp_utc",
        "verification"
      ]
    },
    {
      "bytes": 840,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/redshift_0p020m0p050.json",
      "sha256": "173f94c82e2ea438dbc6f558054f0ff45482f98300d67aef1034ce9927f979b4"
    },
    {
      "bytes": 840,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/redshift_0p050m0p080.json",
      "sha256": "c17c10429377de2fd9e8a5db5ae04f2530a1e6b66184132bda1b5cdc27066f78"
    },
    {
      "bytes": 841,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/redshift_0p080m0p120.json",
      "sha256": "ed5361b9c668a972df2710007a71b4cbb01eb2ab55311fed91b5d10811284ab7"
    },
    {
      "bytes": 867,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/ssfr_m10p0mm9p5.json",
      "sha256": "9d46e341cfd2963a8e7a85881a97ea516451148b0992d75eb16cbf4e3037c0b1"
    },
    {
      "bytes": 868,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/ssfr_m10p5mm10p0.json",
      "sha256": "ec3971e4b5c79524752813ca07e191f4f2f295c637338eaa4b3f72bac80eb26f"
    },
    {
      "bytes": 868,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/ssfr_m11p0mm10p5.json",
      "sha256": "33c4e0976dd02423a876b0bd8f34f1609239dcd6af6ead1c13765d39cc74d047"
    },
    {
      "bytes": 866,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/ssfr_m12p0mm11p0.json",
      "sha256": "94ca1ed216b3367dd0c8d69db4c303c0d156652bb587286c8714020112c68e8a"
    },
    {
      "bytes": 866,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/ssfr_m14p0mm12p0.json",
      "sha256": "2d350109b2744a9a44669cf4becfc04e309997e5f7828d80fd5445344de0c77f"
    },
    {
      "bytes": 864,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/ssfr_m9p0mm7p0.json",
      "sha256": "340acd2698a3dbfbfd0b59104c835507fae051163a493108de0c6c079b19c287"
    },
    {
      "bytes": 866,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/ssfr_m9p5mm9p0.json",
      "sha256": "143e9df603cde8e4b98f5cd6ad814d9233c28898aa06c0ee5474c9c2812eb125"
    },
    {
      "bytes": 858,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/stellar_mass_10p0m10p5.json",
      "sha256": "5b06398943b32f8be1489e1717d56252f18e861ee29b3ee15dbc5f5d0a757e52"
    },
    {
      "bytes": 858,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/stellar_mass_10p5m11p0.json",
      "sha256": "9304d897d07e93748e885887ba00448cd1e8927287e0aeaa43b6612df894c9b5"
    },
    {
      "bytes": 859,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/stellar_mass_11p0m12p5.json",
      "sha256": "54b1cb22d28bae2eb1f31fe7523b1026acccea33dde8a789adb1c807d427c79e"
    },
    {
      "bytes": 856,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/stellar_mass_8p0m9p5.json",
      "sha256": "02bfdee241177988359d651712ff2f6efb0b765af100463c1776d8b8ff028868"
    },
    {
      "bytes": 857,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/stellar_mass_9p5m10p0.json",
      "sha256": "fb48fd00b5c187401516bb934e6b671d73028b0af8f78b476be56607b905c3ce"
    },
    {
      "bytes": 814,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads/strict_public_total.json",
      "sha256": "965ee947bbae84a33bf6fe01245275fe824576903fc7ede662f728466c7b7be4"
    },
    {
      "bytes": 3956,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/historical-topic-extension-map/20260708T231242Z/historical_topic_extension_manifest_20260708T231242Z.json",
      "sha256": "09964573155e266e3b2b965bad304571be74c096db89296bb52e95641e8587f3",
      "top_keys": [
        "artifacts",
        "generated_utc",
        "manifest_file",
        "marker",
        "outdir",
        "safety",
        "validation"
      ]
    },
    {
      "bytes": 67834,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/historical-topic-extension-map/20260708T231242Z/historical_topic_extension_map_20260708T231242Z.json",
      "sha256": "30cdfef2d82c57c60c77d06d9e1576ca9648691cdfa00c81ef58a5320f84b417",
      "top_keys": [
        "active_papers",
        "counts",
        "generated_utc",
        "historical_crosswalk",
        "marker",
        "purpose",
        "safety",
        "scope_guard",
        "source_files"
      ]
    },
    {
      "bytes": 1712,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/historical-topic-extension-map/20260708T231242Z/historical_topic_extension_validation_20260708T231242Z.json",
      "sha256": "f16c5e89eadd00d35a487874e80f493ff88d1398da1338c3517e18e819b29138",
      "top_keys": [
        "active_slug_set_matches_expected",
        "active_slugs_expected",
        "active_slugs_seen",
        "all_source_files_exist",
        "artifact_hash_note",
        "counts",
        "curated_mapping_keys_expected",
        "curated_mapping_keys_used",
        "safety",
        "source_files_count",
        "timestamp_utc",
        "unmapped_source_keys",
        "unused_mapping_keys"
      ]
    },
    {
      "bytes": 20012,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/m2p3_m3p1_selection_ci_manifest_20260708T193507Z.json",
      "sha256": "e3ab9407f0d2327128f7cef87453e874ed722254c9c1968d7e405a205593056b",
      "top_keys": [
        "artifacts",
        "compiled_revisions",
        "data_source_grounding",
        "figures_copied",
        "generated_tables",
        "inputs",
        "marker",
        "mechanical_counts",
        "original_public_linked_pdf_checks",
        "proxy_guard",
        "safety",
        "scope",
        "summary_md",
        "tick_report",
        "timestamp_utc"
      ]
    },
    {
      "bytes": 4313,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/rp1_robustness_selection_manifest_20260708T181833Z.json",
      "sha256": "3b5d5308662956b03b42b99244b8ad22256d92dcd7ecce7005af601fd7346596",
      "top_keys": [
        "compile_exit_code",
        "compile_log",
        "copied_figures",
        "fatal_markers",
        "inputs",
        "inserted_key_values",
        "local",
        "marker",
        "output_root",
        "pdf",
        "pdf_bytes",
        "pdf_magic_ok",
        "pdf_sha256",
        "safety",
        "scope",
        "source_tex",
        "tex",
        "utc"
      ]
    },
    {
      "bytes": 500,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/join_complete_mass_ssfr_bounds.json",
      "sha256": "2ff3058ce38f3d2cc5422eeaebbab5f767de8f7ac0f5b780e2624472d1dcac4c"
    },
    {
      "bytes": 546,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/join_complete_with_line_table.json",
      "sha256": "6325c426c222921b06cd32c34a2b52db4ca09d8f381738eff2227f3ac6356cdd"
    },
    {
      "bytes": 525,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_parent_m10p6_s10p7.json",
      "sha256": "b7f9869851d50ed9524a5b60fb9cd64e7a99f8df6db0d9f2eafc79fc8dc25f17"
    },
    {
      "bytes": 523,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_parent_m10p6_s11p0.json",
      "sha256": "a7aa894378083e785812eb5bfc0a98ef0ba54d40af82348d2f33b576d9e9d838"
    },
    {
      "bytes": 524,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_parent_m10p8_s10p7.json",
      "sha256": "06748b8b951db4584892c61c4d81e4e2e66697df2de980a7eed02f6d12aba282"
    },
    {
      "bytes": 522,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_parent_m10p8_s11p0.json",
      "sha256": "26948eeb844b2e802397a49471b0322ee1c4f0a090cafcf4562f91b989dd6dbe"
    },
    {
      "bytes": 522,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_parent_m11p0_s10p7.json",
      "sha256": "2cbd03acc75f15ddd9a5bd83b937893d498cea8882c9354ebb762bc28119f87a"
    },
    {
      "bytes": 520,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_parent_m11p0_s11p0.json",
      "sha256": "4f56d167295c81350593f4c6ea73b1b8e2864fbe98c6052ecd6affede91cae13"
    },
    {
      "bytes": 840,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_sn3_m10p6_s10p7.json",
      "sha256": "a7caa261f42b290d8d1d179e6864e80f027b978cfc0b475ca4c40fa3c53c947e"
    },
    {
      "bytes": 838,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_sn3_m10p6_s11p0.json",
      "sha256": "ad6f5f83031c29c8b4e7ecc44c1638fedd7e885221e6b41ac14289e385c62b90"
    },
    {
      "bytes": 840,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_sn3_m10p8_s10p7.json",
      "sha256": "81a86c505360e9861478d9f95f9ba778f0da2e4f207d1808825c67525999d56c"
    },
    {
      "bytes": 838,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_sn3_m10p8_s11p0.json",
      "sha256": "e654d54ca92a2ea7ca97fd4e3778446b04e1a203b66dd2c777cdc50ff3a5e20a"
    },
    {
      "bytes": 838,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_sn3_m11p0_s10p7.json",
      "sha256": "41b7e68153a9d2821ecd4d157ba2150f852639fc3f07d3f92307c1c3f511a083"
    },
    {
      "bytes": 836,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p2_sn3_m11p0_s11p0.json",
      "sha256": "35477ebf8bd270c6a84f33d4f1ac1e1768e88fe7a4a41469a73f44e7e82419b9"
    },
    {
      "bytes": 503,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p3_small_parent_m11p0_12p5_z0p02_0p05.json",
      "sha256": "f3fe4357b1d6f63d33a2d8382f228aa71d2c2a7a60d04de406498ef2d141d9b5"
    },
    {
      "bytes": 501,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p3_small_parent_m8p0_9p5_z0p08_0p12.json",
      "sha256": "44d2ca54d0de1a08d658f6620849bd0c23d0acba339126bb93e884588d53d272"
    },
    {
      "bytes": 819,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p3_small_sn3_m11p0_12p5_z0p02_0p05.json",
      "sha256": "44a7ae511247291b9e697f2ed05d6976e381617555e0a6e66edbb488f168e6bd"
    },
    {
      "bytes": 817,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/m3p3_small_sn3_m8p0_9p5_z0p08_0p12.json",
      "sha256": "4a7a6baf2556b5aee87a203cf3e10420fc708828323a9b94868be23a1b41b435"
    },
    {
      "bytes": 511,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/massive_parent_m10p6.json",
      "sha256": "6c335e787bf513345109dfc951a356e206afe38ce449a4c61afc0c92fab14629"
    },
    {
      "bytes": 510,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/massive_parent_m10p8.json",
      "sha256": "0fffd40f88201e478cb7b82a201847b18f4ccdabccc6a81b04a90a24761dee62"
    },
    {
      "bytes": 508,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/massive_parent_m11p0.json",
      "sha256": "c9b816b812c66a740e1e95b1cef3608bd74e304122d8ccdcd2a49ffd3b5e345c"
    },
    {
      "bytes": 826,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/massive_sn3_m10p6.json",
      "sha256": "959381d3394cf6ec339e8d0ca9b98ba19ed3aa65be483502bc2a6791ad681af7"
    },
    {
      "bytes": 826,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/massive_sn3_m10p8.json",
      "sha256": "73f93f235009136d4f6e30ff6bec00d5d17d7b93b2a6d85d97d0bb5cef930d42"
    },
    {
      "bytes": 824,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/massive_sn3_m11p0.json",
      "sha256": "1c4df9a5f92c7e6fd4b33e902dc840a3f000e1baef9202e4c4c6d8b8b5b60713"
    },
    {
      "bytes": 734,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/positive_four_bpt_fluxes_and_errors.json",
      "sha256": "d68fcbf9c6700f937e83b3302082abaf5ebea3ad64650d856f67b3efbbfaef3a"
    },
    {
      "bytes": 819,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/sn_ge_10_four_bpt_lines.json",
      "sha256": "d3cb823d389615297bbf3e5bc2d3571a75c682376df3f3883375a9d6a7cef060"
    },
    {
      "bytes": 816,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/sn_ge_3_four_bpt_lines.json",
      "sha256": "b134e4d0a5b93f473ace780f3a4c9b1d04e63b500cfd5c5a8a3bd4a23cec63b0"
    },
    {
      "bytes": 816,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/sn_ge_5_four_bpt_lines.json",
      "sha256": "3d25bb0542d477d2adc9ec9df65a15d043472a361912377f022eeb37d7822420"
    },
    {
      "bytes": 290,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/spectro_galaxy_z_window.json",
      "sha256": "09a5a25358b991b8de8231815cafa5525be69435eb06a041354fc3bc3299897a"
    },
    {
      "bytes": 512,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_parent_m10p0_to_m9p5.json",
      "sha256": "141d00c01a53cc78245bc3dee04374bd67c915048730dd083bda87e083538331"
    },
    {
      "bytes": 513,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_parent_m10p5_to_m10p0.json",
      "sha256": "3b88de6b51e19609b5e84e41cffed7e3001c6f1da8e0996becfa7a90dcd4993a"
    },
    {
      "bytes": 513,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_parent_m11p0_to_m10p5.json",
      "sha256": "b1dba4599941e87e24260b78c78d1ef46c160f9c7e9fe19b6b64a4fd7f7a6b67"
    },
    {
      "bytes": 511,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_parent_m12p0_to_m11p0.json",
      "sha256": "baa50d9ff5f145f4f724c3bac040647a2cb20d4e17ef9d6cc673b3f6b01c77c2"
    },
    {
      "bytes": 511,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_parent_m14p0_to_m12p0.json",
      "sha256": "351070bb5972517619f9ddeb027b46e30f5dc7c31b65ce5c504374a83b97bc5a"
    },
    {
      "bytes": 508,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_parent_m9p0_to_m7p0.json",
      "sha256": "858901b6ab6d2105b30fed4893680a41fac5a5ed892d01baee284ce5c2236499"
    },
    {
      "bytes": 511,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_parent_m9p5_to_m9p0.json",
      "sha256": "2c0802f060688d209b9a8c0384a409f8681a63f9345e7fa22289f357174fc2d1"
    },
    {
      "bytes": 828,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_sn3_m10p0_to_m9p5.json",
      "sha256": "7ba0221076488bbfa0968ffb1daba25c22232c86d639fde94482413ad9806500"
    },
    {
      "bytes": 829,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_sn3_m10p5_to_m10p0.json",
      "sha256": "3ad58316f4f3545d769178542332497cc237c3f1b4fd3afaa130de52ef0f65f4"
    },
    {
      "bytes": 829,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_sn3_m11p0_to_m10p5.json",
      "sha256": "95858ebcc6076ed73077587dff7201c8ca6a50e2e4e4eb75def7b873734d86c7"
    },
    {
      "bytes": 827,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_sn3_m12p0_to_m11p0.json",
      "sha256": "b735b9ee4f181732fe452c0e63c9cbf5235e625c1578b00534112ca55ad04a61"
    },
    {
      "bytes": 827,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_sn3_m14p0_to_m12p0.json",
      "sha256": "e6cae0aaaaba097938e3ad3fd61c7306a003ae461a5b35c531246489df3d6bba"
    },
    {
      "bytes": 824,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_sn3_m9p0_to_m7p0.json",
      "sha256": "ad5001954482b3105e495f3e1cff8b7393b4302835373655e3decea22ac243bb"
    },
    {
      "bytes": 827,
      "list_len": 2,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads/ssfr_sn3_m9p5_to_m9p0.json",
      "sha256": "1f6ad65c70ffc44a75b01bdfa1d309ed041ae8ee4ca355bec0b04f60a6d9c5fa"
    },
    {
      "bytes": 3340,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/selection_function_attrition_artifact_manifest_20260708T155514Z.json",
      "sha256": "08574696cd6134a0631aed6781c76e86ad7257358fd072f1df5002ce819f4705",
      "top_keys": [
        "artifact_count",
        "artifacts",
        "first_attempt_note",
        "marker",
        "raw_payload_count_json",
        "raw_payload_count_sql",
        "timestamp_utc"
      ]
    },
    {
      "bytes": 7999,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/selection_function_attrition_summary_20260708T155514Z.json",
      "sha256": "cb58d3f1eb2f4f05ba14516b51b2af0dae4cec377a23cd6f594220c1f114f6fe",
      "top_keys": [
        "cached_coverage_of_strict_sdss_sn_ge_3",
        "cached_rows",
        "files",
        "m3_p2_default_denominator",
        "m3_p2_strict_denominator",
        "m3_p3_small_cell_count",
        "marker",
        "safety",
        "sdss_endpoint",
        "source_csv",
        "ssfr_low_bin_reference",
        "ssfr_star_forming_bin_reference",
        "stage_counts",
        "strict_sdss_sn_ge_3_total",
        "timestamp_utc"
      ]
    },
    {
      "bytes": 19321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/shared_selection_data_dictionary_20260708T204717Z.json",
      "sha256": "8305bb2288363e7186e5d622f7151d30c92f8244eef607a8536731998a9afa23",
      "top_keys": [
        "column_dictionary",
        "paper_use_contracts",
        "selection_stage_counts_verified",
        "ssfr_retention_rows",
        "summary"
      ]
    },
    {
      "bytes": 8063,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/shared_selection_module_manifest_20260708T204717Z.json",
      "sha256": "f52451134d0d48c3bad0cf6d1e1fbeaef04445bb11651ae476f2a6afa4efbeb0",
      "top_keys": [
        "artifacts",
        "manifest_json_path",
        "manifest_self_hash_note",
        "marker",
        "safety",
        "scope",
        "summary_values",
        "timestamp_utc",
        "verification"
      ]
    },
    {
      "bytes": 9636,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/wave2-result-table-drafts/20260708T143512Z/tori_wave2_result_table_manifest_20260708T143512Z.json",
      "sha256": "b6c291ab05fc5269149d53261a3a6d4bba506ded012b0f65e560a920e879c0f8",
      "top_keys": [
        "drafts",
        "inputs",
        "marker",
        "outputs",
        "safety",
        "scope",
        "timestamp_utc"
      ]
    },
    {
      "bytes": 3111,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json",
      "sha256": "0f6bb1374129b72d28bcae59cfe432243f00a1a9712d8b1b74938c62626456eb",
      "top_keys": [
        "analysis_rows",
        "bpt_counts",
        "data_release",
        "files",
        "group_medians",
        "match_abs_delta_logM_median",
        "match_abs_delta_z_median",
        "match_distance_scaled_median",
        "matched_delta_log_sSFR_mean_ci95_bootstrap",
        "matched_delta_log_sSFR_mean_dex",
        "matched_delta_log_sSFR_median_ci95_bootstrap",
        "matched_delta_log_sSFR_median_dex",
        "matched_pairs",
        "ols_adjusted_for_logM_z",
        "query_top_n",
        "raw_rows",
        "revision_marker",
        "run_id",
        "safety"
      ]
    },
    {
      "bytes": 2155,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json",
      "sha256": "c0421620f67f3c227955affa3f4c1876cb85f8b31874d219f2cd2e35a7f9cec0",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "high_density_quenched",
        "high_minus_low_ci",
        "interpretation_guard",
        "low_density_quenched",
        "lpm_high_density_coeff",
        "lpm_high_density_se",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 1998,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json",
      "sha256": "06291f82c3fbe0f7fe84f7249568882ca4fa44972bcc25a55e367ef1fdcc7e6e",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "massive_agn_fraction",
        "massive_quenched_agn_fraction",
        "massive_quenched_rows",
        "massive_rows",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 1827,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json",
      "sha256": "44b2407aa691d64fd6de22eb49a8c0a185c86bb1f3b538c7bf066e904d0a3210",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "high_excitation_agn",
        "interpretation_guard",
        "median_log_sSFR_all",
        "median_log_sSFR_high_excitation",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 1957,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/data/source_analysis_results.json",
      "sha256": "4e1ff701bb5b98af4945d5adad2e543e00005e1ab3907e8fae7d15e70c93e351",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "high_density_massive_agn",
        "high_minus_low_ci",
        "interpretation_guard",
        "low_density_massive_agn",
        "massive_rows",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 2112,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json",
      "sha256": "204ec46dc838e5e69a34b4dc2f790cb0b5e0f7fc1cb4eaa71f830779a2c92b67",
      "top_keys": [
        "agn_fraction_by_mass",
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "mass_bin_labels",
        "method",
        "peak_agn_fraction",
        "peak_agn_mass_bin",
        "pilot_question",
        "proposal_title",
        "quenched_fraction_by_mass",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample",
        "transition_mass_bin_quenched_fraction_gt_0p5"
      ]
    },
    {
      "bytes": 2375,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/data/source_analysis_results.json",
      "sha256": "e711563011102657b6d5cab279c1b2ab7ed087dfc734e50932ad4edfe90d0683",
      "top_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "method",
        "pilot_question",
        "prevalence_ratio_widest_to_narrowest",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample",
        "tracer_prevalence"
      ]
    },
    {
      "bytes": 2101,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json",
      "sha256": "42965b6f359c23b56098f5f9845561f4a4a2ba81e1e00df09fbae4acf3bcc2d9",
      "top_keys": [
        "agn_fraction_in_denominator",
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "massive_transition_quenched_rows",
        "median_log_lha_denominator",
        "median_log_lha_offset_vs_massive_sf",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ]
    },
    {
      "bytes": 5079,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json",
      "sha256": "6f289f8c68da425eb3d8005e673bf5c5c02cf917eaa2bc6feedd053535de8f52",
      "top_keys": [
        "agn_fraction_range",
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "method",
        "pilot_question",
        "proposal_title",
        "quenched_fraction_range",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample",
        "target_vector_cells"
      ]
    },
    {
      "bytes": 22125,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_AUDIT.json",
      "sha256": "9a86c71ff4c396aaf76a04621241e083b5cd3aee30a679e31ecf5896abccf024",
      "top_keys": [
        "audit_utc",
        "counts",
        "failures",
        "papers",
        "run_id",
        "warnings"
      ]
    },
    {
      "bytes": 17583,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_MANIFEST_PRECOMPILE.json",
      "sha256": "38255be94b516db7a1a29559d2b1b2d09ddab01c8a39b5aeeb561dd147b3faeb",
      "top_keys": [
        "created_utc",
        "papers",
        "run_id",
        "scope",
        "shared_counts",
        "source_artifacts"
      ]
    },
    {
      "bytes": 6977,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.json",
      "sha256": "860c4f73527db2c6fae57c662d6eae429038e706f323b3994b57cad273d6f02f",
      "top_keys": [
        "audit_utc",
        "counts",
        "failures",
        "figures",
        "outputs",
        "package_id"
      ]
    },
    {
      "bytes": 10922,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_MANIFEST_PRECOMPILE.json",
      "sha256": "8d5bac7875b81d1e38f30554de042e0428e26f0658f7c925bfa538049b1de92d",
      "top_keys": [
        "created_utc",
        "decision",
        "flagship",
        "package_id",
        "safety",
        "source_integration_run",
        "supplement"
      ]
    },
    {
      "bytes": 8213,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.json",
      "sha256": "658db8b6d07d0b260f599e2e62af1608e58c0a3ee5e808c7dccbda90c87558fa",
      "top_keys": [
        "audit_utc",
        "bad_mock_or_synthetic_data_use_flagship",
        "bad_mock_or_synthetic_data_use_supplement",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "flagship_required_missing",
        "goru_preintegrator_report",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 11192,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_01_ACTUAL_RESEARCH_SUMMARY.json",
      "sha256": "d05bb27287e75475d1f9c563cef0e6be0b6020804c7fbc7b26aeb123bb5ceb88",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6244,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_01_QUALITY_AUDIT.json",
      "sha256": "6476d19a4b23588e2fb85fb1c215da09a5bd5b6c2be0535b0c50f1d26ce67a1c",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9315,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_01_SUMMARY.json",
      "sha256": "a401551747fdea01b8a817492101a03a6ef1fd5c8491a4365ac3a3f40097669b",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 8213,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json",
      "sha256": "5d6514c33c8ba691dd5b950994c08df20d53a10fd391bcddf3522b843513be33",
      "top_keys": [
        "audit_utc",
        "bad_mock_or_synthetic_data_use_flagship",
        "bad_mock_or_synthetic_data_use_supplement",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "flagship_required_missing",
        "goru_preintegrator_report",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 11192,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_02_ACTUAL_RESEARCH_SUMMARY.json",
      "sha256": "e6ac7c59f5c66efc9d54ff1fc3e224ccbd7befa2edeecaae94e38de68cd06d8a",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6244,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_02_QUALITY_AUDIT.json",
      "sha256": "efc2b7192b1f3c9cbd4283b770f6573245d140cb1ea21ade52a25d9f6ba7f049",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9315,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_02_SUMMARY.json",
      "sha256": "e0a8c95410a536225f9b67cb5b8e51f60ee71a70066e1a10c2e3fbf9bfd140ef",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 8213,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json",
      "sha256": "c9c10f999a96ca1cfd7a9beec29c4ef04296142da57c3b47a516f30771f162c7",
      "top_keys": [
        "audit_utc",
        "bad_mock_or_synthetic_data_use_flagship",
        "bad_mock_or_synthetic_data_use_supplement",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "flagship_required_missing",
        "goru_preintegrator_report",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 11192,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json",
      "sha256": "8275d43501616255ebdd1e49bda466c78ce476de7282dfc8b52e2edb9e5e2902",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6348,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_03_QUALITY_AUDIT.json",
      "sha256": "6f88ea516718ab044a8be11789524755acc756156f7884024509d4b11f2235b5",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9435,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_03_SUMMARY.json",
      "sha256": "51b40a36e2ce4e6001997c79c3c163c97470d729b379229cfb651a4867ee7390",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 8213,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json",
      "sha256": "03dbd7b693e7f70d706269468ff8c1be075d3e56960f42caf8e923dc4f32b8d4",
      "top_keys": [
        "audit_utc",
        "bad_mock_or_synthetic_data_use_flagship",
        "bad_mock_or_synthetic_data_use_supplement",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "flagship_required_missing",
        "goru_preintegrator_report",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 11192,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_04_ACTUAL_RESEARCH_SUMMARY.json",
      "sha256": "5ed82a72f9e654738954705d712628c1034e5c82c0c67cf2c148592bf0454189",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6244,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_04_QUALITY_AUDIT.json",
      "sha256": "0265cc34075bd91dde7343c36e1d831a37269889fe7f76a4dea5aa8df1908f49",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9315,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_04_SUMMARY.json",
      "sha256": "3851a80f8afbf08a59d2eefbeea803a9a024cc04d6267c8cda9dbe4a0d759678",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 8213,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.json",
      "sha256": "13f8ca1cc1be86604f4f31856a5c0923bef24263611449a16c7b0df017fe88aa",
      "top_keys": [
        "audit_utc",
        "bad_mock_or_synthetic_data_use_flagship",
        "bad_mock_or_synthetic_data_use_supplement",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "flagship_required_missing",
        "goru_preintegrator_report",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 11192,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json",
      "sha256": "94a11f4bf7964e555ed074f8b5ce5a49bccf29ea6e03fda25f6f7b04d803e4a3",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6244,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_05_QUALITY_AUDIT.json",
      "sha256": "cb0e1770d74d9e7ab058064153200cedb4db307012688722d5f3da388906f959",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9315,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_05_SUMMARY.json",
      "sha256": "335f355a01076bfdc444f5f6951a83f1ceb1cb8dc2dcd55cb7a0d771800329a9",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 8213,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.json",
      "sha256": "4b70f8b366a25037c3b9cfb099c7947e9f66c3efaaae8731b2e2d80ce720b84c",
      "top_keys": [
        "audit_utc",
        "bad_mock_or_synthetic_data_use_flagship",
        "bad_mock_or_synthetic_data_use_supplement",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "flagship_required_missing",
        "goru_preintegrator_report",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 11192,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json",
      "sha256": "a930acffe3c10ff4155ac461ad38138bfb441766b8e872357e27d385e53348a9",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6244,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_06_QUALITY_AUDIT.json",
      "sha256": "c43198ab8bbf17c6fda2eb5ec4c2d227e6259906615ce26943c70434b819bb88",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9315,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_06_SUMMARY.json",
      "sha256": "fcbfe26e35445362ad5e9914bc205a833ac4d663d5f3ade8cc9b956b5c47d577",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6244,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_07_QUALITY_AUDIT.json",
      "sha256": "ce7d0f7d2b2ea43cd55b8e042f869841d491b71d26bf9992198c3922a1332b11",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9315,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_07_SUMMARY.json",
      "sha256": "58a8cd23bea962ada4a60a2b38f84b7e56dc6ef4c99c04e00d69202e9e65957e",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6244,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_08_QUALITY_AUDIT.json",
      "sha256": "441399e0297c275fe88b6add35e982d28c1cf8211b50958d10a205600ec74d4b",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9315,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_08_SUMMARY.json",
      "sha256": "91b60143b0525cba47cd51d3837bf5b1fdadefdcd097810b5236670101f4898a",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6244,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_09_QUALITY_AUDIT.json",
      "sha256": "1907891a7ba6228f7427ddbef7bffb54533623738ecda27da01c04494992af78",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9315,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_09_SUMMARY.json",
      "sha256": "6dcdd8fa342dd757af053d6a56dbaf575476a330f5361eb649d1a40c049d0947",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_10_QUALITY_AUDIT.json",
      "sha256": "c01bc0e33d291c69d70a545e9be24da4ad339dccdfba4a329127daab9117a784",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_10_SUMMARY.json",
      "sha256": "de83c3045fee727e379d3446db7b98165cd05a66756285ce981e00a52765822d",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_11_QUALITY_AUDIT.json",
      "sha256": "f39ec385d95451fac4a4e49eb3e12907042e014d3969fa992849ed2467cd63e5",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_11_SUMMARY.json",
      "sha256": "6c77b8bf4cb5d224e4001eead8c855c1ba4ca98821fcfd0bbc47a5badbc64132",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_12_QUALITY_AUDIT.json",
      "sha256": "a6ebcb92611dcb7a709bb2e038fcec82a064ccccc6e0685edf4df6abc1e8dfde",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_12_SUMMARY.json",
      "sha256": "f9dc448434d2b6831177d0f0290ccc8cab18e579254be9b8f3c86b5f1a8fe169",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_13_QUALITY_AUDIT.json",
      "sha256": "4693ad42d7260d4bcfd9492dd16788fa0efb3c24feb079053778fb6aa2ee7b20",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_13_SUMMARY.json",
      "sha256": "e97a2d17ee5d16d085ae5c8e4751000def22f29ca2172c1a6715a5868aa4fdcb",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_14_QUALITY_AUDIT.json",
      "sha256": "ab4f4e80dde2f4e57c4be7048c28dd0324d58ea8ecdca3cb5fd728d299b25c8a",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_14_SUMMARY.json",
      "sha256": "a2ea88e51be0a5e163f85477d6d8a1a6ec1476990b87a0accd5d1f5cbc1cc047",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_15_QUALITY_AUDIT.json",
      "sha256": "f095bc6e6ff51a86bea1d9e5c4069a1e397bd0e1635f6a8befea2fc18a088fe2",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_15_SUMMARY.json",
      "sha256": "13017f79c8d92f8f970e16106f0a9d6f4ad79c59bb5d59d396a947cbbe48d108",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_16_QUALITY_AUDIT.json",
      "sha256": "cb707747c905fa90b83f76e1c8063b7a6b09a24f3920f0c4c64c24a4960e45af",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_16_SUMMARY.json",
      "sha256": "441c0d1d832057d8776f67507051b6460ecf2be1dfc8b36d52ca63c3aace35c1",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_17_QUALITY_AUDIT.json",
      "sha256": "df23b2a22edf9520f6f150bd7dde4d56f01df365cb7bef191a3a7c7c6f346a5a",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_17_SUMMARY.json",
      "sha256": "2df044cf025748d1bb8615190049f1adc4bb27b81a4d3bc71a6ec106110ca53a",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_18_QUALITY_AUDIT.json",
      "sha256": "517fc14bfaf3276fd851246f9e0a62fb09525eecb3c5031cbb15504940130c19",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_18_SUMMARY.json",
      "sha256": "3fdf8b314be0ebf8627689e76dcdc69843aa961adb1e74f7d5c4ecc07e8a70d9",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_19_QUALITY_AUDIT.json",
      "sha256": "39da45f4ba017aed7ee4d1af6b8fb07812b42ce6b6a820e2a9374a4ccb90fe64",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_19_SUMMARY.json",
      "sha256": "4ea4572ebb7d87839fa06213d3c30d8cfa80c5407a4aeb3b57a399c64fc69e3e",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_20_QUALITY_AUDIT.json",
      "sha256": "702e72c7e555d63bd48c7f5243534b81c5c8393b1019e2657d5c3cdd2dbdf1ff",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_20_SUMMARY.json",
      "sha256": "4a8a925077494ab979f09f4cd9feb2a5e25c529372bd342a6391de2208515fa2",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6349,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_21_QUALITY_AUDIT.json",
      "sha256": "87de40bb126ae0e9c84de3aad67d73e554cb36b19a0f431d1db0da96b0ed408d",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9441,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_21_SUMMARY.json",
      "sha256": "842a2977d0b323248ff80bb209e619f8bf02b5cb7db3f09438f9b820bb329468",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_22_QUALITY_AUDIT.json",
      "sha256": "fdde5a0ecd1a828d210b6b75875d6bd391756386e71f548dd6b213d216b8726f",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9320,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_22_SUMMARY.json",
      "sha256": "b5f7a9fb114566cd1c442b0c77ad9efd9dedec14e538268a1c4212f27efb7519",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_23_QUALITY_AUDIT.json",
      "sha256": "d641dcc0ea44d126925a98dee672b04209288e1eef76b71065d45123b427b0f8",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_23_SUMMARY.json",
      "sha256": "d288891acf13ce2c3e3d19877d597d098f9294feab62f6ae5432cfbd8c0ff13c",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6245,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_24_QUALITY_AUDIT.json",
      "sha256": "1e62095168a46acbaae6651b451eea17be2a9bed8fadfa8667815d089d222d48",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9321,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_24_SUMMARY.json",
      "sha256": "cad55be17a8432222976bf4239d4de28bed5269c0c259b2d962cf5a426ef41c8",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6349,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_25_QUALITY_AUDIT.json",
      "sha256": "7026d4a1b15aa22d6715304b83580d8656c7160a1a0fa3da92e31e49b77a18b9",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9441,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_25_SUMMARY.json",
      "sha256": "4be83fa3228ae16fc8e2a74848965c5dd825d8c856f274dfc860997d8fa0b6db",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 6349,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_26_QUALITY_AUDIT.json",
      "sha256": "38752cec7bc3fe0bdd8eeafa7df954e8caeae86086804e1ccb039035c4657e09",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "cycle",
        "fatal_failures",
        "figures",
        "flagship_required_missing",
        "numeric_invariants_missing_flagship",
        "supplement_required_missing"
      ]
    },
    {
      "bytes": 9441,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/CYCLE_26_SUMMARY.json",
      "sha256": "80d1ac2e6411f0c1ce56f2643d875bd3cb6c5b57ecd29203ae32c7b2fd5cb2c3",
      "top_keys": [
        "audit",
        "candidate",
        "cycle",
        "finished_utc",
        "integrator_result",
        "lane_results"
      ]
    },
    {
      "bytes": 3207,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/FINAL_GUARDRAIL_CLEANUP_AUDIT.json",
      "sha256": "8f0707c55980a20b75b32f765d90901f9920f67c3bb6692968a0730900c65f6c",
      "top_keys": [
        "audit_utc",
        "candidate",
        "compile_results",
        "compiler",
        "fatal_failures",
        "figure_count",
        "marker",
        "safety",
        "source_candidate"
      ]
    },
    {
      "bytes": 6977,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/PACKAGE_AUDIT.json",
      "sha256": "860c4f73527db2c6fae57c662d6eae429038e706f323b3994b57cad273d6f02f",
      "top_keys": [
        "audit_utc",
        "counts",
        "failures",
        "figures",
        "outputs",
        "package_id"
      ]
    },
    {
      "bytes": 10922,
      "parse_ok": true,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/PACKAGE_MANIFEST_PRECOMPILE.json",
      "sha256": "8d5bac7875b81d1e38f30554de042e0428e26f0658f7c925bfa538049b1de92d",
      "top_keys": [
        "created_utc",
        "decision",
        "flagship",
        "package_id",
        "safety",
        "source_integration_run",
        "supplement"
      ]
    }
  ],
  "overnight_root": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708",
  "pdf_files": [
    {
      "bytes": 262957,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.pdf",
      "sha256": "df98f3c1bfd727017fd186c5849c8f0cbe2f0ebb806a56e2b840fac1491f4a05"
    },
    {
      "bytes": 86693,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/flagship_rp1/figures/fig-bpt.pdf",
      "sha256": "99cc2411c43dcd41895d6cb55234648a8b8ffc498eaf8ffeea8ec534c119b999"
    },
    {
      "bytes": 78775,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/flagship_rp1/figures/fig-matched-offsets.pdf",
      "sha256": "83d16bcbeada88091c5c68a4fd98fd96af9d3b8971bd361a55d0f1b16ca95661"
    },
    {
      "bytes": 551025,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf",
      "sha256": "0d43a550d770f71ab7cfc8cd124cc9f2774e92849742606f1dcdf8175f340cd3"
    },
    {
      "bytes": 14881,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/supplementary_denominator_atlas/figures/topic-01.pdf",
      "sha256": "1fd192eed0643ae73b54e06c311117fb6c3241c1f952bade758e56e32fe02d9f"
    },
    {
      "bytes": 14966,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/supplementary_denominator_atlas/figures/topic-02.pdf",
      "sha256": "596db86bacb484ebec5750f3ef41ceb490d5b7c8a870b0c5cb4638f2aab92fe8"
    },
    {
      "bytes": 247680,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/supplementary_denominator_atlas/figures/topic-03.pdf",
      "sha256": "31e5c88cd1e02bf868b18000814317477bbdf14cbbbb95b8f1708f0f107f4670"
    },
    {
      "bytes": 15267,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/supplementary_denominator_atlas/figures/topic-04.pdf",
      "sha256": "8bd1b0248cf0939fb2ba0a64155586b3f13a0dc2eff581e2ab63ae750481694c"
    },
    {
      "bytes": 14913,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/supplementary_denominator_atlas/figures/topic-05.pdf",
      "sha256": "725dfb62948db7d4b868eef7b18ba9739ad814d821cc507d3a19c53c556943f9"
    },
    {
      "bytes": 16341,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/supplementary_denominator_atlas/figures/topic-06.pdf",
      "sha256": "abfc743a35167e4247288ffe0571531f839989078861f94c2fa49ed9914d79f2"
    },
    {
      "bytes": 139945,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/supplementary_denominator_atlas/figures/topic-07.pdf",
      "sha256": "a20bf97de10b49f6c662f5e6c7f403d935b8615abf1c8dc9daddc7174f861d4a"
    },
    {
      "bytes": 16385,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package/supplementary_denominator_atlas/figures/topic-08.pdf",
      "sha256": "eef8a9b385dfb97aa0cef8df24f363712f28140f8988a6a2b6cac169f1b8d61d"
    },
    {
      "bytes": 229429,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
      "sha256": "775111b2b7802dfa562eefe96f7b85b43e6d7513a712eec6bf4026babcd4be7a"
    },
    {
      "bytes": 86693,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf",
      "sha256": "99cc2411c43dcd41895d6cb55234648a8b8ffc498eaf8ffeea8ec534c119b999"
    },
    {
      "bytes": 78775,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf",
      "sha256": "83d16bcbeada88091c5c68a4fd98fd96af9d3b8971bd361a55d0f1b16ca95661"
    },
    {
      "bytes": 82149,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
      "sha256": "4f21a374f59c5242789dd9f2c371d2ff0e79242f76668a5300fd82cda0c4b1d2"
    },
    {
      "bytes": 14881,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/figures/fig-topic.pdf",
      "sha256": "1fd192eed0643ae73b54e06c311117fb6c3241c1f952bade758e56e32fe02d9f"
    },
    {
      "bytes": 82450,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
      "sha256": "5c0f16a7bf37dc5a8826eb155df75079dd591e07c905f11d911364d9ec3344b5"
    },
    {
      "bytes": 14966,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf",
      "sha256": "596db86bacb484ebec5750f3ef41ceb490d5b7c8a870b0c5cb4638f2aab92fe8"
    },
    {
      "bytes": 311419,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
      "sha256": "853b83d305b2c6ab2f69ef3f0f97edd84e9876ae1a7e88edd8589ee59176bb45"
    },
    {
      "bytes": 247680,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf",
      "sha256": "31e5c88cd1e02bf868b18000814317477bbdf14cbbbb95b8f1708f0f107f4670"
    },
    {
      "bytes": 82698,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
      "sha256": "a686c95f782f669a9af7863ecded77bd5b890abf06d925cf6138934055ef307b"
    },
    {
      "bytes": 15267,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf",
      "sha256": "8bd1b0248cf0939fb2ba0a64155586b3f13a0dc2eff581e2ab63ae750481694c"
    },
    {
      "bytes": 82412,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
      "sha256": "6e6606eaa61c90b2eb5a4b19650e3bd32e21acb4060252473a6606142782e31f"
    },
    {
      "bytes": 14913,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf",
      "sha256": "725dfb62948db7d4b868eef7b18ba9739ad814d821cc507d3a19c53c556943f9"
    },
    {
      "bytes": 82864,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
      "sha256": "50f4c5dee581c6b93c5b2fcb5f1e33b445b0353392f96f6fc489037b66ca809f"
    },
    {
      "bytes": 16341,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/figures/fig-topic.pdf",
      "sha256": "abfc743a35167e4247288ffe0571531f839989078861f94c2fa49ed9914d79f2"
    },
    {
      "bytes": 205145,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
      "sha256": "f5c970a0307410b5f35ce9a5b22470adbfae621850650c80b41244d99d717444"
    },
    {
      "bytes": 139945,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf",
      "sha256": "a20bf97de10b49f6c662f5e6c7f403d935b8615abf1c8dc9daddc7174f861d4a"
    },
    {
      "bytes": 83154,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf",
      "sha256": "d9fe74cac5aaaab5bc1f8ea994752d6f92d8d2431559d50411e38830584be958"
    },
    {
      "bytes": 16385,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/figures/fig-topic.pdf",
      "sha256": "eef8a9b385dfb97aa0cef8df24f363712f28140f8988a6a2b6cac169f1b8d61d"
    },
    {
      "bytes": 236847,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.pdf",
      "sha256": "3392f53534d8452ebb3db4191dff7855ebb13428dff768d45d847be9d5d8efac"
    },
    {
      "bytes": 86693,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/figures/fig-bpt.pdf",
      "sha256": "99cc2411c43dcd41895d6cb55234648a8b8ffc498eaf8ffeea8ec534c119b999"
    },
    {
      "bytes": 78775,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/figures/fig-matched-offsets.pdf",
      "sha256": "83d16bcbeada88091c5c68a4fd98fd96af9d3b8971bd361a55d0f1b16ca95661"
    },
    {
      "bytes": 527135,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf",
      "sha256": "403a69d8fcf02c56bd3266db0de0363ea9c45c659d5a305861cfba7144b705e2"
    },
    {
      "bytes": 14881,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-01.pdf",
      "sha256": "1fd192eed0643ae73b54e06c311117fb6c3241c1f952bade758e56e32fe02d9f"
    },
    {
      "bytes": 14966,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-02.pdf",
      "sha256": "596db86bacb484ebec5750f3ef41ceb490d5b7c8a870b0c5cb4638f2aab92fe8"
    },
    {
      "bytes": 247680,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-03.pdf",
      "sha256": "31e5c88cd1e02bf868b18000814317477bbdf14cbbbb95b8f1708f0f107f4670"
    },
    {
      "bytes": 15267,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-04.pdf",
      "sha256": "8bd1b0248cf0939fb2ba0a64155586b3f13a0dc2eff581e2ab63ae750481694c"
    },
    {
      "bytes": 14913,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-05.pdf",
      "sha256": "725dfb62948db7d4b868eef7b18ba9739ad814d821cc507d3a19c53c556943f9"
    },
    {
      "bytes": 16341,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-06.pdf",
      "sha256": "abfc743a35167e4247288ffe0571531f839989078861f94c2fa49ed9914d79f2"
    },
    {
      "bytes": 139945,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-07.pdf",
      "sha256": "a20bf97de10b49f6c662f5e6c7f403d935b8615abf1c8dc9daddc7174f861d4a"
    },
    {
      "bytes": 16385,
      "header": "%PDF",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-08.pdf",
      "sha256": "eef8a9b385dfb97aa0cef8df24f363712f28140f8988a6a2b6cac169f1b8d61d"
    }
  ],
  "real_data_policy": [
    "Never use mock, synthetic, fake, placeholder, or toy data.",
    "Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.",
    "New quantitative claims must be traceable to the real local SDSS artifacts inventoried by this sprint or to a cited public source with URL/DOI/arXiv/ADS metadata.",
    "If a value is not present in the local real-data inventory or a cited public source, write 'not measured here' or 'needs real data'.",
    "Literature-only sources may motivate future work; they do not become measured NebulaMind results.",
    "The RP-1 flagship remains an optical SDSS/BPT association pilot unless real additional observables are supplied."
  ],
  "source_package": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_06_package",
  "sprint_id": "ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z"
}
exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package | sed -n '1,200p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_16_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_22_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_21_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_16_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_18_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_17_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_18_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/PACKAGE_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_20_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_25_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_18_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_22_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_25_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_17_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_18_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_16_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_23_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_17_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_20_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_23_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/PACKAGE_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_19_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/PACKAGE_MANIFEST_PRECOMPILE.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_23_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_20_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_16_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_25_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_20_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/README.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_21_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_24_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_18_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_21_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-02.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-03.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-01.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-04.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-05.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-07.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-06.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-08.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_19_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_22_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_23_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_20_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_22_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_19_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_25_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_19_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_22_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_25_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_24_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_24_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_19_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_SUMMARY.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_QUALITY_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_SUMMARY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_REVIEW_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_RESPONSE.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_24_QUALITY_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json

exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z | sed -n '1,200p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/README.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_MANIFEST_PRECOMPILE.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/FLAGSHIP_REVIEW_DECISION_20260709T013510Z.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_HANDOFF.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/README.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_MANIFEST_PRECOMPILE.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/FINAL_HANDOFF.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-02.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-03.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-01.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-04.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-05.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-07.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-06.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-08.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex

codex
I’ve confirmed the inventory contains the expected local SDSS artifacts, including the 60,000-row samples and the 8,146 matched pairs. Next I’m reading the flagship TeX and package audits to see whether the manuscript’s quantitative claims and citations line up with those artifacts and whether any compile risks are obvious.
exec
/bin/zsh -lc 'cat /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/PACKAGE_AUDIT.md' in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex" in /Users/duhokim/NebulaMind/NebulaMind
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
We present a selection-aware SDSS DR17 matched-control pilot that measures the association between broad optical BPT-selected galaxies and catalog specific star-formation rate. The analysis is shaped by the SDSS 3-arcsec fiber aperture and by a non-random 60,000-galaxy computational pilot cap sequentially selected by \texttt{specObjID} from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies; the cap is an arbitrary cache limit for local workflow validation and cache budgeting, not a physically motivated or volume-complete subsample. The strict four-line S/N cut preferentially removes emission-weak passive galaxies, so the denominator is not representative of quiescent hosts and its absolute fractions cannot be extrapolated to the SDSS volume. Broad optical BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, with no morphology, aperture-fraction, or environment control. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex; stricter line-S/N and Seyfert-like subsets reduce the offset magnitude to -0.763 dex. This fiber-centered offset is highly degenerate with the well-known mass-morphology relation, as morphology is not controlled in the match. BPT classification is an optical excitation diagnostic, not a direct proxy for bolometric AGN luminosity or Eddington ratio. This result is association-only, not causal. The companion supplement organizes the missing structural, environmental, and multiwavelength observables needed for future follow-up tests, including morphology, aperture fraction, halo or group labels, CO/HI gas measurements, radio and X-ray proxies, and IFU kinematics.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper addresses a narrow association-only question within a low-redshift SDSS DR17 optical emission-line denominator: do broad optical BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a negative catalog-sSFR offset within the analyzed denominator. The result is not a causal claim or inference; it is an association in a capped optical sample and does not test AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling in this dataset.
The 60,000-galaxy computational pilot cap is an arbitrary cache limit rather than a volume-complete census, so it is not normalized into a luminosity or mass function. The cap is retained for local workflow validation and cache budgeting, not to tune the science result.


The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations powered by hot post-AGB stars, as well as low-ionization nuclear emission-line region (LINER)-like ionization, can contaminate broad low-ionization classes \citep{cidfernandes2011,stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT-selected galaxies'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label. Because the sample is restricted to $0.02<z<0.12$, the standard local BPT demarcations are used here without any redshift-evolution correction.

\subsection{Scope and limitations}
The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a 60,000-galaxy computational pilot cap selected sequentially by \texttt{specObjID}. It is a local pilot subset used to validate the analysis workflow and establish the relative association within an arbitrary fixed cache budget, not a volume-limited census. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this cap is not a random sky sample and introduces survey-plate and sky-coverage bias. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the cap is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy; the fixed 3-arcsec aperture systematically misses extended star-forming disks at low redshift \citep{kewley2005}. If broad optical BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a galaxy-wide star-formation comparison.
The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}. We use variance-normalized Euclidean matching because the feature space is only two standardized variables, $(\log M_\star,z)$, so the rule stays transparent and the resulting nearest-neighbor control remains easy to interpret as an association baseline.

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

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the fixed-size-sample limitation.

\section{Classification and matching}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Here, the star-forming control pool is defined as objects below the Kauffmann et al.\ (2003) demarcation. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control by variance-normalized Euclidean distance in standardized $(\log M_\star,z)$ space, with replacement. In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), and the unrestricted Euclidean match has median absolute separations of 0.0045 dex in $\log M_\star$ and 0.00021 in redshift, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements. The preferred estimate does not impose a maximum mass--redshift caliper; the caliper row in Table~\ref{tab:robust} is a sensitivity variant. The moderate mass--redshift caliper sensitivity variant uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.
Here, ``broad optical BPT-selected'' means the inclusive optical-emission-line class under the standard BPT demarcations, while the Seyfert-like sensitivity check uses the stricter Kewley et al.\ (2006) high-excitation cut to remove the low-excitation LINER/retired branch by construction.

\begin{figure*}
\centering
\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the SDSS DR17 analysis denominator. The matched controls are paired in stellar mass and redshift only, not in morphology, so the diagram verifies the optical-excitation classes used for matching but does not by itself prove accretion-driven feedback.}
\label{fig:bpt}
\end{figure*}

\section{Matched-control result}
The preferred broad optical BPT comparison gives a large negative catalog-sSFR offset for the broad optical BPT-selected galaxies relative to star-forming controls.
\par\noindent\textbf{Morphology and aperture caveat.} A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the observed sSFR offset is highly degenerate with the known mass--morphology relation and the transition from disk-dominated to bulge-dominated systems, including bulge prominence or central velocity dispersion effects \citep{schawinski2010,bluck2014,belfiore2016}. Single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, an ambiguity that requires spatially resolved integral-field spectroscopy to resolve \citep{penny2018,cheung2016}. The robustness interval in Table~\ref{tab:robust} is a 95\% confidence interval on the median offset.

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
The result is directly measured in the capped sample and remains falsifiable within the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset persists under a moderate mass--redshift caliper, which is already reflected by the 7,867-pair, -1.318 dex sensitivity row. Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. The Kewley et al.\ (2006) demarcation explicitly removes the retired/LINER-like low-ionization tail, so the larger -1.309 dex offset is driven in part by that broader low-ionization branch rather than solely by Seyfert-like excitation. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad optical BPT-selected sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a galaxy-wide star-formation comparison. Matching on mass and redshift alone leaves morphology uncontrolled, and the fixed 3-arcsec fiber can under-sample extended disk star formation at low redshift; this is a known source of central-to-global mismatch \citep[e.g.,][]{harrison2017,ellison2021}. The central-kiloparsec aperture restriction is one reason this remains a local association rather than a galaxy-wide star-formation measurement. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size, SpecObjID-capped 60,000-galaxy pilot sample. Any causal star-formation change claim requires additional real data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
The choice of variance-normalized Euclidean matching is deliberate: with only two standardized coordinates, it preserves a simple nearest-neighbor control rule without introducing an additional model layer that would not be better constrained by the available data.

\section{Conclusion}
RP-1 is a selection-aware pilot association paper. Its key results are the preferred -1.309 dex offset, the persistence of the offset under a moderate mass--redshift caliper, and the reduction from -1.309 dex to -0.763 dex under stricter line-S/N and Seyfert-like subsets. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} collects the missing-observable requirements for future physical tests. See Supplement Sections 4.1 and 4.7 for the neighbor-rank/fiber-collision caveat and CO/HI follow-up requirements.
In practice, future follow-up requires integration with the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation comparisons passed through the same selection functions \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,ellison2011,piotrowska2022,wetzel2013,dekel2006}; these references are cited as examples of missing observables for future follow-up, not as validation of any mechanism in this SDSS-only denominator. The result remains association-only until morphology, aperture fraction, and the missing multiwavelength or IFU observables are added.

\section*{Data Availability}
This paper uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. The 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and the manuscript conclusions remain conditional on the optical-emission-line denominator.
No mock, synthetic, fake, placeholder, or toy data were used.

\facilities{SDSS}

\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Belfiore et al.(2016)]{belfiore2016} Belfiore, A., Maiolino, R., Maraston, C., et al. 2016, MNRAS, 461, 3111
\bibitem[Bluck et al.(2014)]{bluck2014} Bluck, A.~F.~L., Bruce, V.~A., Pilkington, K., et al. 2014, MNRAS, 441, 599
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasi{\'n}ska, G., Schlickmann, S., et al. 2011, MNRAS, 413, 1687
\bibitem[Cheung et al.(2016)]{cheung2016} Cheung, E., Bundy, K., Cappellari, M., et al. 2016, Nature, 533, 504
\bibitem[Ellison et al.(2011)]{ellison2011} Ellison, S.~L., Patton, D.~R., Mendel, J.~T., et al. 2011, MNRAS, 418, 2043
\bibitem[Ellison et al.(2021)]{ellison2021} Ellison, S.~L., Lin, L., Rosario, D.~J., et al. 2021, MNRAS, 501, 4777
\bibitem[Harrison(2017)]{harrison2017} Harrison, C.~M. 2017, Nature Astronomy, 1, 0165
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
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
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}

exec
/bin/zsh -lc 'cat /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_16_QUALITY_AUDIT.json' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "audit_utc": "2026-07-09T04:49:11Z",
  "candidate": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package",
  "compile_results": [
    {
      "bad_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.quality.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.pdf",
      "pdf_bytes": 259097,
      "returncode": 0,
      "sha256": "b2aacebb7cd46dc730af728acea7e86c0604ca346afc8b5d80aff049a883601b",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex"
    },
    {
      "bad_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf",
      "pdf_bytes": 552296,
      "returncode": 0,
      "sha256": "36dc703596989913b62810e12fa00ae5683e293f00ff49353f3858783d5e7236",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex"
    }
  ],
  "cycle": 16,
  "fatal_failures": [],
  "figures": [
    {
      "bytes": 86693,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/figures/fig-bpt.pdf",
      "sha256": "99cc2411c43dcd41895d6cb55234648a8b8ffc498eaf8ffeea8ec534c119b999"
    },
    {
      "bytes": 78775,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/figures/fig-matched-offsets.pdf",
      "sha256": "83d16bcbeada88091c5c68a4fd98fd96af9d3b8971bd361a55d0f1b16ca95661"
    },
    {
      "bytes": 16385,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-08.pdf",
      "sha256": "eef8a9b385dfb97aa0cef8df24f363712f28140f8988a6a2b6cac169f1b8d61d"
    },
    {
      "bytes": 16341,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-06.pdf",
      "sha256": "abfc743a35167e4247288ffe0571531f839989078861f94c2fa49ed9914d79f2"
    },
    {
      "bytes": 139945,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-07.pdf",
      "sha256": "a20bf97de10b49f6c662f5e6c7f403d935b8615abf1c8dc9daddc7174f861d4a"
    },
    {
      "bytes": 14913,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-05.pdf",
      "sha256": "725dfb62948db7d4b868eef7b18ba9739ad814d821cc507d3a19c53c556943f9"
    },
    {
      "bytes": 15267,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-04.pdf",
      "sha256": "8bd1b0248cf0939fb2ba0a64155586b3f13a0dc2eff581e2ab63ae750481694c"
    },
    {
      "bytes": 14881,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-01.pdf",
      "sha256": "1fd192eed0643ae73b54e06c311117fb6c3241c1f952bade758e56e32fe02d9f"
    },
    {
      "bytes": 247680,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-03.pdf",
      "sha256": "31e5c88cd1e02bf868b18000814317477bbdf14cbbbb95b8f1708f0f107f4670"
    },
    {
      "bytes": 14966,
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/figures/topic-02.pdf",
      "sha256": "596db86bacb484ebec5750f3ef41ceb490d5b7c8a870b0c5cb4638f2aab92fe8"
    }
  ],
  "flagship_required_missing": [],
  "numeric_invariants_missing_flagship": [],
  "supplement_required_missing": []
}
codex
I’ve got the main manuscript and the decision audit. I’m now checking the supplement and the source-analysis outputs for the exact invariants and for any wording that could overclaim beyond the local real-data artifacts.
exec
/bin/zsh -lc 'cat /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json' in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
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
This supplement is the companion to the selection-aware SDSS BPT/sSFR pilot study and organizes eight SDSS DR17 denominator and proxy notes into one coherent, association-only optical baseline atlas built around the same 60,000-galaxy computational pilot cap and selection-function caveats. The 60,000-galaxy sample is a local, non-random computational pilot cap kept for local workflow validation and cache budgeting rather than as a physical or volume-limited census, so all counts and fractions remain conditional on the SDSS optical selection used here. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this cap is not a random sky sample and introduces survey-plate and sky-coverage bias. The atlas preserves follow-up targets for environment, broad optical BPT-selected incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-based comparison data are treated as missing observables for future tests rather than as measurements in this package. The sample coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one atlas with eight linked entries, not eight independent causal-feedback papers. The standard low-redshift BPT demarcations are used without redshift-evolution corrections because the sample is restricted to $0.02<z<0.12$. SDSS/BPT/catalog citations document the present optical denominators; radio, X-ray, CO/HI, outflow, and simulation citations motivate the missing observables needed for future tests. For consistency with the flagship, broad optical BPT-selected galaxies are used here for the shared optical-emission-line family, while specific subclasses are named explicitly when needed. Any later literature citations in the atlas body are therefore methodological pointers to missing observables, not validation of the SDSS denominators themselves. \textbf{This atlas provides observational baselines only; it is a selection-biased optical denominator, not a physical feedback test, and it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical association between BPT classification and catalog sSFR. These eight entries are distinct baseline-and-follow-up atlas notes: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the entries span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. For consistency with the flagship, the atlas uses the broad optical BPT-selected family when the full optical-emission-line denominator is meant and names specific subsets only when the stricter selection matters. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. This is an association-only optical baseline atlas, and keeping the notes in one supplement keeps the atlas coherent and gives future work a single checklist of what still must be added.

\section{Shared denominator}
The atlas uses the same analyzed public-data backbone as the main paper: 60,000 galaxies in a computational pilot cap from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, i.e. 24.0\% sample coverage. The four-line selection is sSFR-dependent and the sample is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The galaxy-by-galaxy stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing. The 60,000-row cache is an arbitrary computational pilot cap, not a physical selection threshold.

The eight subsections below are intentionally parallel baseline-plus-follow-up notes: each one states the observed optical denominator or target vector, then names the missing observables that a future multiwavelength or simulation-based test would need before any physical inference can be made. In other words, the sections are distinct follow-up domains bounded by the same optical selection effect, and their role is to organize the atlas rather than to stand as separate papers.

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
\tablecaption{Atlas-level follow-up menu. Each row summarizes the present optical role and the missing observables needed before any physical inference.\label{tab:atlas-summary}}
\tablehead{\colhead{Topic} & \colhead{Observed baseline} & \colhead{Missing observables} & \colhead{Future Follow-up Domain}}
\startdata
Environment & low-sSFR vs.\ 10th-neighbor rank (60,000 total; 15,000 per quartile) & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test \\
Maintenance heating & broad optical BPT-selected hosts in massive low-sSFR galaxies (maintenance-heating baseline; 9,298 massive; 5,695 low-sSFR) & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
Outflow kinematics & high-excitation broad optical BPT-selected subset (4,440/60,000) & resolved velocities; halo potentials; multiphase gas; CGM tracers & kinematic follow-up \\
Env.\ jets & density-stratified broad optical BPT-selected fraction in massive hosts & radio morphology/age; cavity energetics; hot-gas density & radio-jet follow-up \\
Mass bin & low-sSFR and broad optical BPT-selected incidence by $M_\star$ bin (15 cells with $n\geq50$) & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
Tracer census & tracer prevalence in 60k sample (0.136 to 0.418) & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
Gas depletion & gas-depletion low-sSFR baseline; H$\alpha$ proxy (6,729 galaxies) & CO/dust gas masses; aperture-matched SFRs; morphology; environment & CO/HI follow-up \\
Simulation vector & mass-redshift target vector (15 cells with $n\geq50$) & simulations through SDSS/MaNGA/ALMA/X-ray/radio selection; aperture/noise models & forward model \\
\enddata
\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects the optical emission-line selection function, which preferentially removes low-equivalent-width or passive systems from the denominator; the surviving sample therefore becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

\section{Atlas notes}
As a reminder, each atlas entry is a baseline-plus-follow-up checklist, not a standalone physical-feedback result.

\subsection{Relative neighbor-count baseline: SDSS 10th-neighbor index for low-sSFR incidence}
We establish a relative neighbor-count baseline within the emission-line denominator that can later be joined to group catalogs and halo masses. The 10th-neighbor index is the rank of the 10th nearest companion in projected sky separation within this redshift-limited sample; it is an internal ordinal rank within this selection-biased sample and does not map to physical environmental volume density or halo density. Because no additional line-of-sight velocity window is imposed beyond the redshift slice, the statistic is especially susceptible to projection effects. The projected-neighbor ranking is computed within the full $0.02<z<0.12$ redshift slice, with no additional line-of-sight velocity window imposed beyond those sample limits. The SDSS 55-arcsec fiber-collision limit systematically removes close neighbors in dense regions, so the 10th-neighbor proxy is biased before any physical interpretation is attempted. We emphasize that the SDSS 55-arcsec fiber collision limit systematically biases this index in dense environments, precluding its use as a physical density metric without forward-modeled corrections. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004 coefficient uncertainty. The follow-up ingredients are group catalogues, robust central/satellite labels, halo masses, a spectroscopic fiber-collision correction at the 55-arcsec scale, morphology, and multi-redshift selection functions. Within this selection-biased emission-line sample, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up.}
\label{fig:m1-rp2-neighbor-count-baseline}
\end{figure}


\subsection{Maintenance-heating denominator: broad optical BPT-selected hosts in massive SDSS galaxies}
We isolate the broad optical BPT-selected duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the broad optical BPT-selected fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The broad optical BPT-selected fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. This optical fraction represents an observational baseline pool, not the active maintenance-heating duty cycle. See the next subsection for the related radio-jet baseline that uses the same projected-density proxy. The follow-up ingredients are X-ray cavity or cooling-luminosity measurements, radio jet powers \citep[e.g.,][]{hardcastle2020}, halo-selected parent catalogues, and nondetection modelling. Those observables are missing here; this entry remains an optical baseline only, and future follow-up requires those real observables before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements.}
\label{fig:m1-rp3-maintenance-heating}
\end{figure}


\subsection{High-excitation broad optical BPT-selected baseline: resolved kinematics follow-up}
We isolate the high-excitation broad optical BPT-selected denominator that resolved kinematics would need to test escape versus recycling. High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The follow-up ingredients are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
\caption{SDSS optical emission-line denominator: the high-excitation BPT-selected subset used to define an observational baseline for future resolved-kinematic measurements.}
\label{fig:m2-p1-outflow-escape-recycling}
\end{figure}


\subsection{Radio-jet environment baseline: broad optical BPT-selected fraction vs. 10th-neighbor index in massive hosts}
We define the environment-stratified optical denominator that future radio and X-ray work could test. This subsection reuses the same projected-neighbor ranking described in the relative neighbor-count baseline above and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has a broad optical BPT-selected fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The follow-up ingredients are radio jet morphology and age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
\caption{SDSS optical emission-line denominator: the high- and low-density quartile comparison among massive SDSS hosts, used as a baseline for future radio-jet and X-ray work.}
\label{fig:m2-p2-radio-jet-environment}
\end{figure}


\subsection{Stellar-mass selection diagnostic: low-sSFR and broad optical BPT-selected incidence}
In this optical-emission-line denominator, the 11.0--12.5 dex peak is consistent with a selection-function effect: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is concentrated in that mass bin. It must not be interpreted as a universal physical threshold. We identify the mass bin where a future gas-inclusive study should look for a selection-sensitive change in incidence. The note measures the incidence of low catalog-sSFR and broad optical BPT-selected classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the broad optical BPT-selected incidence peaks in the 11.0--12.5 bin at 0.520 within this selection-limited, SpecObjID-capped pilot sample. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The follow-up ingredients are gas fractions, baryon deficits, halo masses, central velocity dispersion proxies \citep{piotrowska2022}, stellar-feedback observables, and high-redshift extensions. The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and broad optical BPT-selected incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up.}
\label{fig:m2-p3-feedback-transition-mass}
\end{figure}


\subsection{Tracer-threshold census for multiphase follow-up}
We compare optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred broad optical BPT-selected or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The follow-up ingredients are ionized, molecular, and neutral tracers, X-ray or radio tracers, a shared parent denominator, and a consistent aperture model. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work.}
\label{fig:m3-p1-multiphase-census}
\end{figure}


\subsection{Low-sSFR optical denominator: baseline for future CO/HI gas measurements}
We define the denominator for CO/HI gas-fraction and depletion-time follow-up. Using the gas-depletion note's low-sSFR baseline, the massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its broad optical BPT-selected fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency or measure total cold-gas mass \citep{tacconi2018}; this note identifies the CO/HI follow-up denominator and optical baseline required for spatially resolved gas tests. The follow-up ingredients are CO or dust-based molecular gas masses \citep[e.g., xCOLD GASS;][]{xcoldgass2017}, atomic hydrogen masses \citep[e.g., xGASS;][]{xgass2018}, aperture-matched SFRs, morphology, and environment labels, together with radio, X-ray, and IFU observables that are still missing here. As with any H$\alpha$-based proxy, residual dust attenuation and stellar-absorption systematics can still affect the optical denominator, so this value should be read as a line-luminosity proxy rather than a direct total cold-gas-mass measurement. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference. No mock, synthetic, fake, placeholder, or toy data were used in compiling this atlas.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
\caption{SDSS optical emission-line denominator: the massive low-sSFR SDSS galaxies available for CO/HI depletion-time follow-up.}
\label{fig:m3-p2-gas-depletion-efficiency}
\end{figure}


\subsection{Simulation target vector for forward-model comparison}
We provide a compact observed target vector for forward modelling. The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, broad optical BPT-selected incidence, and colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and broad optical BPT-selected fractions span 0.003-0.520. The follow-up ingredients are simulations \citep{eagle2015} passed through the exact optical S/N and fiber-aperture selection function used here, including the sequential 60,000-row \texttt{specObjID} cache cap, then through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions, together with aperture models and noise models. Without those matched selection steps, any simulation comparison is not a valid test. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
\caption{SDSS optical emission-line denominator: low-sSFR fraction, broad optical BPT-selected incidence, and colour versus mass and redshift in the SDSS emission-line sample. This is an observed target vector for forward modelling.}
\label{fig:m3-p3-simulation-validation}
\end{figure}

\section{Package decision}
These eight entries should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.

\section*{Data Availability}
This atlas uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. No mock, synthetic, fake, placeholder, or toy data were used. The 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and all eight notes remain conditional on the optical-selection denominators summarized in this atlas.

\facilities{SDSS}

\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Ellison et al.(2021)]{ellison2021} Ellison, S.~L., Lin, L., Rosario, D.~J., et al. 2021, MNRAS, 501, 4777
\bibitem[Hardcastle \& Croston(2020)]{hardcastle2020} Hardcastle, M.~J., \& Croston, J.~H. 2020, New Astronomy Reviews, 88, 101539
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\bibitem[Tacconi et al.(2018)]{tacconi2018} Tacconi, L.~J., Genzel, R., Saintonge, A., et al. 2018, ApJ, 853, 179
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}

exec
/bin/zsh -lc "rg -n \"mock|synthetic|fake|placeholder|toy|8,146|8146|-1\\.309|-1\\.334|-1\\.283|60,000|60000|249,917|249917|24\\.0%|24\\.0|sSFR|coverage|caliper|Seyfert|LINER\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_16_REVIEW_RESPONSE.md:4:- In [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex), I streamlined the abstract so the 60,000-row cap is described once as a capped subset, not repeatedly as a "pilot sample".
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_REVIEW_RESPONSE.md:6:- Flagship abstract now front-loads the morphology and 3-arcsec fiber aperture caveat while preserving the same 8,146 pair result and `-1.309 dex` median offset.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_REVIEW_RESPONSE.md:8:- Flagship interpretation now keeps the result at the denominator-level association boundary while retaining the same `-1.309 dex` to `-0.763 dex` sensitivity comparison.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_REVIEW_RESPONSE.md:9:- Supplement abstract now states that the 60,000-row cache is an arbitrary, non-random pilot cap, and Section 3.1 now folds the 55-arcsec fiber-collision correction into the missing-observables list.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_REVIEW_RESPONSE.md:17:- Any attempt to add morphology, aperture-matched SFRs, CO/HI, X-ray, radio, halo/group, outflow, or simulation-mock measurements not present in this package.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_REVIEW_RESPONSE.md:6:- Flagship abstract and conclusion now say the result is an association paper, not a causal study, while preserving the same 8,146-pair result, `-1.309 dex` median offset, and `[-1.334,-1.283]` bootstrap interval.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_REVIEW_RESPONSE.md:8:- Flagship Table 2 comments now identify the Seyfert-like proxy with the Kewley et al. (2006) high-excitation demarcation and note that the `-0.763 dex` drop reflects systematic removal of the most quenched, bulge-dominated LINER-like systems.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_24_REVIEW_RESPONSE.md:12:- I did not change any numeric results, table values, confidence intervals, sample counts, coverage fractions, or figure paths.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_REVIEW_RESPONSE.md:4:- Tightened the RP-1 abstract so the morphology and aperture-fraction mismatch is named as a primary unmitigated confounder, alongside the LINER/retired-stellar-population caveat.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_REVIEW_RESPONSE.md:6:- Strengthened the RP-1 matching and interpretation sections so the -1.309 dex offset is explicitly described as vulnerable to bulge-dominated versus disk-dominated structural mismatch, not just fiber coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_REVIEW_RESPONSE.md:7:- Added language in the RP-1 interpretation section tying the weaker -0.763 dex Seyfert-like result to LINER-like emission from retired stellar populations in massive bulges.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_REVIEW_RESPONSE.md:7:- Moved the moderate mass-redshift caliper dimensions into the flagship main text: `|\Delta\log M_\star|\leq0.05` and `|\Delta z|\leq0.002`.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_REVIEW_RESPONSE.md:8:- Added the matched-pair count to the flagship Figure 2 caption: `N=8,146` pairs.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_REVIEW_RESPONSE.md:9:- Kept the flagship numeric results unchanged: `8,146` pairs, `-1.309 dex`, `[-1.334,-1.283]`, `60,000` cached rows, `249,917` strict parent, and `24.0%` coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_REVIEW_RESPONSE.md:18:- Running the flagship on the full `249,917`-galaxy parent sample.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_REVIEW_RESPONSE.md:20:- Resolving Seyfert versus LINER contamination with additional diagnostic lines.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_26_REVIEW_RESPONSE.md:22:- Changing any reported offsets, pair counts, or coverage numbers.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_18_REVIEW_RESPONSE.md:6:- Added an explicit sentence in the flagship interpretation that the moderate mass-redshift caliper row is `7,867` pairs with a median offset of `-1.318 dex`, so the caliper sensitivity is stated in prose as well as in the table.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_18_REVIEW_RESPONSE.md:7:- Reworded the flagship caveat language so the `-0.763 dex` Seyfert-like sensitivity result is explained as a consequence of removing LINER-like and retired, bulge-dominated systems from the broader denominator.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_18_REVIEW_RESPONSE.md:20:- I did not attempt to resolve the morphology/aperture question, the volume-complete parent-sample question, or any multiwavelength validation claim, because those require new observations or a re-run without the 60,000-row cap.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_ACTUAL_RESEARCH_RESPONSE.md:23:- The preserved numeric invariants remain: 8,146 pairs, -1.309 dex, [-1.334, -1.283], 60,000 cached rows, 249,917 strict parent, and 24.0% coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_17_REVIEW_RESPONSE.md:7:- In [`flagship_rp1/aastex/rp1_flagship_polished.tex`](./flagship_rp1/aastex/rp1_flagship_polished.tex), I clarified that the 60,000-row cap is a local pilot subset used to validate the workflow within a fixed cache budget.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_17_REVIEW_RESPONSE.md:8:- In the same flagship file, I added an explicit note that the preferred matched estimate has 100% target coverage because matching is done with replacement, and I stated that the preferred estimate does not enforce a caliper.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_17_REVIEW_RESPONSE.md:9:- In the flagship table comments, I added a brief explanation for the `ivar > 0` row drop, noting that the table does not distinguish masking, edge-of-chip loss, or missing spectral coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_17_REVIEW_RESPONSE.md:10:- In the flagship interpretation, I softened the LINER/retired-galaxy wording so the 0.55 dex change is described as a lower bound on contamination and related selection effects, not a direct physical estimate.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_17_REVIEW_RESPONSE.md:11:- In [`supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`](./supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex), I reworded the 60,000-row cap description to say it is a local, non-random pilot cap.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_17_REVIEW_RESPONSE.md:17:- I did not change any numeric results, including 8,146 pairs, -1.309 dex, [-1.334, -1.283], 60,000 cached rows, 249,917 parent rows, or 24.0% coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_RESPONSE.md:10:- Tightened the flagship abstract to be shorter and clearer while preserving the same real-data claims, the 8,146-pair result, the -1.309 dex median offset, the [-1.334,-1.283] interval, and the 60,000-row cap.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_RESPONSE.md:23:- No mock, synthetic, placeholder, or toy data language was added beyond the existing real-data guardrails.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md:6:- Added an explicit warning that the 60,000-row cache cap is non-random and non-extrapolatable to the SDSS volume.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md:8:- Added an explicit no-mock-data statement to the flagship data-availability section.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md:10:- Added an explicit no-mock-data statement to the supplement data-availability section and to the CO/HI follow-up note.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md:14:- I did not change any numeric invariants, counts, offsets, confidence intervals, or sample coverage values.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_RESPONSE.md:15:- I did not re-rank the broad BPT result versus the Seyfert-like sensitivity track.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_RESPONSE.md:19:- The package already satisfies the core numerical invariants and the review reports did not identify compile blockers or mock-data use.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_REVIEW_RESPONSE.md:5:- Tightened the flagship abstract so it states the capped `60k`-row pilot cache, the `8,146` matched pairs, the `-1.309 dex` median offset, and the `-0.763 dex` Seyfert-like sensitivity result without the earlier defensive repetition.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_REVIEW_RESPONSE.md:8:- Split the flagship conclusion citations into role-separated groups: radio/X-ray maintenance heating, CO/HI gas follow-up, outflow/kinematics, simulation-mock comparisons, and environment/context references.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_07_REVIEW_RESPONSE.md:17:- Any attempt to add morphology matching, aperture-matched SFRs, halo/group catalogs, CO/HI, X-ray, radio, or simulation-mock observables that are not present in this package.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_REVIEW_RESPONSE.md:6:- Strengthened the flagship aperture caveat in the main text by describing catalog sSFR as an aperture-extrapolated proxy and by making the bulge/disk mismatch language more explicit.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_REVIEW_RESPONSE.md:7:- Revised the robustness discussion so the shift from `-1.309 dex` to `-0.763 dex` is framed as a change in the emission-line denominator and subclass definition, not as a purity or causal upgrade.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_REVIEW_RESPONSE.md:14:- I did not change any numeric results, sample counts, intervals, or coverage fractions.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_REVIEW_RESPONSE.md:24:- CO/HI, outflow, or simulation-mock additions needed for physical inference.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/FINAL_HANDOFF.md:83:- Core claim: broad optical BPT AGN hosts in the capped SDSS DR17 optical emission-line denominator have lower catalog sSFR than mass-redshift matched star-forming controls.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/FINAL_HANDOFF.md:84:- Main number: 8,146 matched pairs, median delta log sSFR = -1.309 dex, bootstrap interval [-1.334, -1.283] dex.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/FINAL_HANDOFF.md:86:- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/FINAL_HANDOFF.md:87:- Required caveat: S/N>=10 and narrower Seyfert-like definitions reduce the offset magnitude, so subclass/selection dependence is real.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/FINAL_HANDOFF.md:139:During compile, the supplement built cleanly first. The flagship initially failed because a generated table row began with `[N II]`, which TeX parsed as optional row spacing after a line break. The generator was fixed to use `N II Seyfert-like proxy` instead. Both PDFs then compiled successfully.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_RESPONSE.md:5:- Kept all existing numeric invariants unchanged in the flagship: `8,146` pairs, `-1.309` dex, `[-1.334,-1.283]`, `60,000` cached rows, `249,917` strict parent, and `24.0%` coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_08_ACTUAL_RESEARCH_RESPONSE.md:12:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_20_REVIEW_RESPONSE.md:4:- Recast the abstract and opening framing into a more affirmative observational tone while keeping the same 8,146-pair result, the -1.309 dex median offset, the [-1.334, -1.283] dex interval, and the 60,000-row cap.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_20_REVIEW_RESPONSE.md:6:- Tightened the BPT and Seyfert language in Sections 3 and 5 so the Kewley et al. (2006) cut is described as removing the low-excitation LINER/retired branch by construction.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_20_REVIEW_RESPONSE.md:17:- I did not change any numeric result, sample count, confidence interval, coverage fraction, figure path, or table structure that would alter the core claims.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_REVIEW_RESPONSE.md:7:- Updated Table 2 interpretation wording so the `-0.763 dex` Seyfert-like proxy is described as excluding retired/LINER-like bulges.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_REVIEW_RESPONSE.md:16:- No numeric values were changed, including 8,146 pairs, -1.309 dex, [-1.334,-1.283], 60,000 cached rows, 249,917 strict parent rows, or 24.0% coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_REVIEW_RESPONSE.md:5:- Clarified in both TeX files that the 60,000-row cache is a computational, non-random pilot cap rather than a physical selection threshold.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_REVIEW_RESPONSE.md:13:- I did not alter the 8,146 pair count, the -1.309 dex and -0.763 dex offsets, the [-1.334,-1.283] interval, the 60,000 cached rows, the 249,917 strict parent count, or the 24.0% coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_REVIEW_RESPONSE.md:18:- The remaining morphology, gas-phase, environment, and mock-observation requirements still need new data if they are to be promoted beyond association-only or baseline language.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_15_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_RESPONSE.md:10:- No mock, synthetic, fake, placeholder, or toy data were introduced.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_RESPONSE.md:17:- The manuscript remains an optical BPT/sSFR association pilot, and the supplement remains a denominator/proxy atlas for future real-data follow-up.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_25_REVIEW_RESPONSE.md:16:- No table counts, coverage values, or matched-pair totals were changed.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_25_REVIEW_RESPONSE.md:24:- The package still contains the same core quantitative claims: 8,146 matched pairs, median \(\Delta\log {\rm sSFR}=-1.309\) dex, confidence interval \([-1.334,-1.283]\) dex, 60,000 cached rows, 249,917 strict-parent rows, and 24.0\% coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_RESPONSE.md:9:- Replaced `strong negative sSFR offset` with `negative catalog-sSFR offset`.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_RESPONSE.md:11:- Reworded the flagship interpretation paragraph so the offset is described as persisting under the caliper, not as `large`.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_RESPONSE.md:20:- No mock, synthetic, placeholder, or toy data were added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_RESPONSE.md:27:- I checked the edited prose for the banned mock/synthetic language and for the main causal overstatements targeted by the review.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:4:\shorttitle{Selection-aware SDSS BPT/sSFR study}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present a selection-aware SDSS DR17 matched-control pilot that measures the association between broad optical BPT-selected galaxies and catalog specific star-formation rate. The analysis is shaped by the SDSS 3-arcsec fiber aperture and by a non-random 60,000-galaxy computational pilot cap sequentially selected by \texttt{specObjID} from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies; the cap is an arbitrary cache limit for local workflow validation and cache budgeting, not a physically motivated or volume-complete subsample. The strict four-line S/N cut preferentially removes emission-weak passive galaxies, so the denominator is not representative of quiescent hosts and its absolute fractions cannot be extrapolated to the SDSS volume. Broad optical BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, with no morphology, aperture-fraction, or environment control. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex; stricter line-S/N and Seyfert-like subsets reduce the offset magnitude to -0.763 dex. This fiber-centered offset is highly degenerate with the well-known mass-morphology relation, as morphology is not controlled in the match. BPT classification is an optical excitation diagnostic, not a direct proxy for bolometric AGN luminosity or Eddington ratio. This result is association-only, not causal. The companion supplement organizes the missing structural, environmental, and multiwavelength observables needed for future follow-up tests, including morphology, aperture fraction, halo or group labels, CO/HI gas measurements, radio and X-ray proxies, and IFU kinematics.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:19:This paper addresses a narrow association-only question within a low-redshift SDSS DR17 optical emission-line denominator: do broad optical BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a negative catalog-sSFR offset within the analyzed denominator. The result is not a causal claim or inference; it is an association in a capped optical sample and does not test AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling in this dataset.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:20:The 60,000-galaxy computational pilot cap is an arbitrary cache limit rather than a volume-complete census, so it is not normalized into a luminosity or mass function. The cap is retained for local workflow validation and cache budgeting, not to tune the science result.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:23:The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations powered by hot post-AGB stars, as well as low-ionization nuclear emission-line region (LINER)-like ionization, can contaminate broad low-ionization classes \citep{cidfernandes2011,stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT-selected galaxies'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label. Because the sample is restricted to $0.02<z<0.12$, the standard local BPT demarcations are used here without any redshift-evolution correction.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:29:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a 60,000-galaxy computational pilot cap selected sequentially by \texttt{specObjID}. It is a local pilot subset used to validate the analysis workflow and establish the relative association within an arbitrary fixed cache budget, not a volume-limited census. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this cap is not a random sky sample and introduces survey-plate and sky-coverage bias. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the cap is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:30:Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:31:Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy; the fixed 3-arcsec aperture systematically misses extended star-forming disks at low redshift \citep{kewley2005}. If broad optical BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a galaxy-wide star-formation comparison.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:32:The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}. We use variance-normalized Euclidean matching because the feature space is only two standardized variables, $(\log M_\star,z)$, so the rule stays transparent and the resulting nearest-neighbor control remains easy to interpret as an association baseline.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:40:plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:42:four BPT lines with valid flux measurements (\texttt{ivar} $> 0$) & 373,445 & 60,000 & 74.5\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:43:four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:47:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The 416,554-to-373,445 drop when requiring \texttt{ivar} $> 0$ reflects the removal of rows with unusable line-flux uncertainties; this table does not distinguish masking, edge-of-chip loss, or missing spectral coverage. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:50:The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the fixed-size-sample limitation.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:53:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Here, the star-forming control pool is defined as objects below the Kauffmann et al.\ (2003) demarcation. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control by variance-normalized Euclidean distance in standardized $(\log M_\star,z)$ space, with replacement. In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), and the unrestricted Euclidean match has median absolute separations of 0.0045 dex in $\log M_\star$ and 0.00021 in redshift, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements. The preferred estimate does not impose a maximum mass--redshift caliper; the caliper row in Table~\ref{tab:robust} is a sensitivity variant. The moderate mass--redshift caliper sensitivity variant uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:54:Here, ``broad optical BPT-selected'' means the inclusive optical-emission-line class under the standard BPT demarcations, while the Seyfert-like sensitivity check uses the stricter Kewley et al.\ (2006) high-excitation cut to remove the low-excitation LINER/retired branch by construction.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:64:The preferred broad optical BPT comparison gives a large negative catalog-sSFR offset for the broad optical BPT-selected galaxies relative to star-forming controls.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:65:\par\noindent\textbf{Morphology and aperture caveat.} A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the observed sSFR offset is highly degenerate with the known mass--morphology relation and the transition from disk-dominated to bulge-dominated systems, including bulge prominence or central velocity dispersion effects \citep{schawinski2010,bluck2014,belfiore2016}. Single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, an ambiguity that requires spatially resolved integral-field spectroscopy to resolve \citep{penny2018,cheung2016}. The robustness interval in Table~\ref{tab:robust} is a 95\% confidence interval on the median offset.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:69:\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:70:\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:72:Broad optical BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:73:Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:76:N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:78:\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$, and it leaves the median offset essentially unchanged at -1.318 dex for 7,867 pairs. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:84:\caption{Distribution of matched-pair catalog-sSFR offsets for the preferred broad optical BPT-selected galaxy minus nearest star-forming control estimate ($N=8{,}146$ pairs, without a maximum mass--redshift caliper). The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:89:The result is directly measured in the capped sample and remains falsifiable within the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset persists under a moderate mass--redshift caliper, which is already reflected by the 7,867-pair, -1.318 dex sensitivity row. Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. The Kewley et al.\ (2006) demarcation explicitly removes the retired/LINER-like low-ionization tail, so the larger -1.309 dex offset is driven in part by that broader low-ionization branch rather than solely by Seyfert-like excitation. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad optical BPT-selected sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a galaxy-wide star-formation comparison. Matching on mass and redshift alone leaves morphology uncontrolled, and the fixed 3-arcsec fiber can under-sample extended disk star formation at low redshift; this is a known source of central-to-global mismatch \citep[e.g.,][]{harrison2017,ellison2021}. The central-kiloparsec aperture restriction is one reason this remains a local association rather than a galaxy-wide star-formation measurement. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size, SpecObjID-capped 60,000-galaxy pilot sample. Any causal star-formation change claim requires additional real data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:93:RP-1 is a selection-aware pilot association paper. Its key results are the preferred -1.309 dex offset, the persistence of the offset under a moderate mass--redshift caliper, and the reduction from -1.309 dex to -0.763 dex under stricter line-S/N and Seyfert-like subsets. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} collects the missing-observable requirements for future physical tests. See Supplement Sections 4.1 and 4.7 for the neighbor-rank/fiber-collision caveat and CO/HI follow-up requirements.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:97:This paper uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. The 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and the manuscript conclusions remain conditional on the optical-emission-line denominator.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:98:No mock, synthetic, fake, placeholder, or toy data were used.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_REVIEW_RESPONSE.md:6:- In the flagship abstract/context, I kept the numeric results unchanged and bound the `-1.309 dex` result more tightly to the fiber-centered aperture caveat.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_REVIEW_RESPONSE.md:15:- I did not alter any core numeric claims: `8,146` matched pairs, `-1.309 dex`, `[-1.334,-1.283]`, `60,000` cached rows, `249,917` strict parent rows, or `24.0%` coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_RESPONSE.md:10:- I did not alter any numeric invariants, pair counts, confidence intervals, cached-row counts, or coverage fractions.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_RESPONSE.md:12:- I did not introduce any mock, synthetic, placeholder, toy, or invented data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_RESPONSE.md:8:- I preserved the existing association-only boundary, the capped 60,000-row cache framing, the 24.0% coverage statement, the 8,146-pair result, and the -1.309 dex / [-1.334, -1.283] / -0.763 dex values exactly as written.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_RESPONSE.md:11:- No mock, synthetic, fake, placeholder, or toy data were added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_06_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_RESPONSE.md:7:- Clarified the 60,000-row cap as a local workflow-validation and cache-budgeting limit, not a science-tuning choice.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_09_ACTUAL_RESEARCH_RESPONSE.md:8:- Updated the matched-offset figure caption to identify the preferred estimate explicitly and note that it is the no-max-caliper result.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_19_REVIEW_RESPONSE.md:5:- Rephrased the flagged offset interpretation so the LINER-like / retired-galaxy contribution is described as consistent with, not driving, the larger offset.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_19_REVIEW_RESPONSE.md:8:- Standardized the supplement’s purpose sentence to state the main paper measures an association between BPT class and catalog sSFR.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_19_REVIEW_RESPONSE.md:12:- No table counts, confidence bounds, or coverage fractions were changed.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_19_REVIEW_RESPONSE.md:19:- Any stronger claim about feedback, quenching, or outflow physics still requires new morphology, aperture, multiwavelength, or mock-observation data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:3:  "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:4:  "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:34:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_14_ACTUAL_RESEARCH_AUDIT.json:35:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_04_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_REVIEW_RESPONSE.md:12:- Strengthened the flagship aperture caveat so the -1.309 dex offset is explicitly framed as possibly partial or entirely driven by comparing bulge-dominated broad-BPT hosts to disk-dominated controls under a fixed 3-arcsec fiber.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_11_REVIEW_RESPONSE.md:13:- Simplified the flagship LINER/retired-host sensitivity note so the -0.763 dex reduction is attributed to narrower Seyfert-like selection excluding LINER-like and retired bulge-dominated hosts by construction.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_22_REVIEW_RESPONSE.md:15:- I did not change any numeric results, counts, intervals, coverage fractions, or sample sizes.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_01_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:4:    "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:5:    "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:35:      "bad_mock_or_synthetic_data_use_flagship": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_03_ACTUAL_RESEARCH_SUMMARY.json:36:      "bad_mock_or_synthetic_data_use_supplement": [],
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.md:14:- forbidden mock/synthetic data-use hits flagship: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.md:15:- forbidden mock/synthetic data-use hits supplement: []
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_05_ACTUAL_RESEARCH_AUDIT.md:20:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_13_ACTUAL_RESEARCH_SUMMARY.md:18:- Never use mock, synthetic, fake, placeholder, or toy data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:5:- Reworded the flagship matched-control discussion to avoid `global quenching threshold` language and to frame the `-1.309 dex` result as a selection-limited association.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:6:- Replaced the `roughly half the preferred broad-BPT estimate` phrasing with the requested `>0.5 dex` / `~3.5` linear-sSFR clarification.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:7:- Expanded the flagship LINER discussion to make the retired/post-AGB, bulge-dominated interpretation explicit without turning it into a causal feedback claim.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:13:- I did not rerun the analysis on the full `249,917`-row parent sample or change the `60,000`-row pilot cap.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:14:- I did not add CO/HI, radio, X-ray, resolved-outflow, halo, or simulation-mock data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:18:- `8,146` matched pairs
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:19:- `-1.309 dex` preferred offset
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:20:- `[-1.334,-1.283]` bootstrap interval
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:21:- `60,000` cached rows
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:22:- `249,917` strict parent rows
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_10_REVIEW_RESPONSE.md:23:- `24.0%` cache coverage
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_REVIEW_RESPONSE.md:6:- Tightened the flagship matched-control caveat to state that the `-1.309 dex` offset is a relative fiber-aperture comparison, not a global quenching measurement.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_REVIEW_RESPONSE.md:7:- Clarified that the smaller Seyfert-like offset reflects contamination in the broad low-ionization class, especially LINER-like emission from retired stellar populations.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_02_REVIEW_RESPONSE.md:8:- Revised the supplement abstract to state that the `60,000`-row cache is an arbitrary pilot-query cap, not a physical or volume-limited selection effect.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_REVIEW_RESPONSE.md:7:- In [`flagship_rp1/aastex/rp1_flagship_polished.tex`](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/flagship_rp1/aastex/rp1_flagship_polished.tex), I clarified that the 60,000-row pilot cache is sequentially selected by `specObjID`, which is the source of the non-random cap.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_REVIEW_RESPONSE.md:9:- In the flagship Interpretation section, I added an explicit statement that the reduction from `-1.309 dex` to `-0.763 dex` is a practical estimate of LINER-like/retired-galaxy contamination within this cache, not evidence for a different feedback mechanism.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/CYCLE_12_REVIEW_RESPONSE.md:15:- I did not alter any core claims or numeric results, including `8,146` pairs, `-1.309 dex`, `[-1.334,-1.283]`, `60,000` cached rows, `249,917` strict-parent rows, or `24.0%` coverage.

codex
The main-paper invariant set matches the local analysis summary. I’m now checking whether the supplement’s extra counts are actually backed by local analysis files, because those are the easiest place for traceability gaps to hide even when the flagship numbers are solid.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_AUDIT.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "audit_utc": "2026-07-09T01:30:15Z",
  "counts": {
    "compile_logs_ok": 9,
    "fatal_failures": 0,
    "figures_ok": 10,
    "json_ok": 9,
    "papers": 9,
    "pdfs_ok": 9,
    "total_figures": 10
  },
  "failures": [],
  "papers": [
    {
      "caption_count": 2,
      "compile_error_lines": [],
      "compile_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.compile.log",
      "compile_log_bytes": 1415,
      "compile_log_exists": true,
      "compile_warning_count": 11,
      "figure_ref_count": 2,
      "figures": [
        {
          "bytes": 86693,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf",
          "exists": true,
          "header": "%PDF",
          "sha256": "99cc2411c43dcd41895d6cb55234648a8b8ffc498eaf8ffeea8ec534c119b999"
        },
        {
          "bytes": 78775,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf",
          "exists": true,
          "header": "%PDF",
          "sha256": "83d16bcbeada88091c5c68a4fd98fd96af9d3b8971bd361a55d0f1b16ca95661"
        }
      ],
      "missing_required_tex_phrases": [],
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
      "pdf_bytes": 229429,
      "pdf_exists": true,
      "pdf_header": "%PDF",
      "pdf_sha256": "775111b2b7802dfa562eefe96f7b85b43e6d7513a712eec6bf4026babcd4be7a",
      "slug": "m1_rp1_sdss_agn_sfr",
      "source_json_keys": [
        "analysis_rows",
        "bpt_counts",
        "data_release",
        "files",
        "group_medians",
        "match_abs_delta_logM_median",
        "match_abs_delta_z_median",
        "match_distance_scaled_median",
        "matched_delta_log_sSFR_mean_ci95_bootstrap",
        "matched_delta_log_sSFR_mean_dex",
        "matched_delta_log_sSFR_median_ci95_bootstrap",
        "matched_delta_log_sSFR_median_dex",
        "matched_pairs",
        "ols_adjusted_for_logM_z",
        "query_top_n",
        "raw_rows",
        "revision_marker",
        "run_id",
        "safety"
      ],
      "source_json_parsed": true,
      "status": "flagship short-paper draft",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
      "tex_exists": true,
      "title": "Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot"
    },
    {
      "caption_count": 1,
      "compile_error_lines": [],
      "compile_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.compile.log",
      "compile_log_bytes": 2206,
      "compile_log_exists": true,
      "compile_warning_count": 17,
      "figure_ref_count": 1,
      "figures": [
        {
          "bytes": 14881,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/figures/fig-topic.pdf",
          "exists": true,
          "header": "%PDF",
          "sha256": "1fd192eed0643ae73b54e06c311117fb6c3241c1f952bade758e56e32fe02d9f"
        }
      ],
      "missing_required_tex_phrases": [],
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
      "pdf_bytes": 82149,
      "pdf_exists": true,
      "pdf_header": "%PDF",
      "pdf_sha256": "4f21a374f59c5242789dd9f2c371d2ff0e79242f76668a5300fd82cda0c4b1d2",
      "slug": "m1_rp2_environment_quenching",
      "source_json_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "high_density_quenched",
        "high_minus_low_ci",
        "interpretation_guard",
        "low_density_quenched",
        "lpm_high_density_coeff",
        "lpm_high_density_se",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ],
      "source_json_parsed": true,
      "status": "guarded proxy/denominator draft",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
      "tex_exists": true,
      "title": "SDSS density proxy for environmental quenching: selection-aware SDSS optical proxy integration"
    },
    {
      "caption_count": 1,
      "compile_error_lines": [],
      "compile_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.compile.log",
      "compile_log_bytes": 2460,
      "compile_log_exists": true,
      "compile_warning_count": 19,
      "figure_ref_count": 1,
      "figures": [
        {
          "bytes": 14966,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf",
          "exists": true,
          "header": "%PDF",
          "sha256": "596db86bacb484ebec5750f3ef41ceb490d5b7c8a870b0c5cb4638f2aab92fe8"
        }
      ],
      "missing_required_tex_phrases": [],
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
      "pdf_bytes": 82450,
      "pdf_exists": true,
      "pdf_header": "%PDF",
      "pdf_sha256": "5c0f16a7bf37dc5a8826eb155df75079dd591e07c905f11d911364d9ec3344b5",
      "slug": "m1_rp3_maintenance_heating",
      "source_json_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "interpretation_guard",
        "massive_agn_fraction",
        "massive_quenched_agn_fraction",
        "massive_quenched_rows",
        "massive_rows",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ],
      "source_json_parsed": true,
      "status": "guarded proxy/denominator draft",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
      "tex_exists": true,
      "title": "Optical-AGN denominator for maintenance-heating follow-up: selection-aware SDSS optical proxy integration"
    },
    {
      "caption_count": 1,
      "compile_error_lines": [],
      "compile_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.compile.log",
      "compile_log_bytes": 2177,
      "compile_log_exists": true,
      "compile_warning_count": 16,
      "figure_ref_count": 1,
      "figures": [
        {
          "bytes": 247680,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf",
          "exists": true,
          "header": "%PDF",
          "sha256": "31e5c88cd1e02bf868b18000814317477bbdf14cbbbb95b8f1708f0f107f4670"
        }
      ],
      "missing_required_tex_phrases": [],
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
      "pdf_bytes": 311419,
      "pdf_exists": true,
      "pdf_header": "%PDF",
      "pdf_sha256": "853b83d305b2c6ab2f69ef3f0f97edd84e9876ae1a7e88edd8589ee59176bb45",
      "slug": "m2_p1_outflow_escape_recycling",
      "source_json_keys": [
        "card_id",
        "figure_pdf",
        "full_proposal_requires",
        "high_excitation_agn",
        "interpretation_guard",
        "median_log_sSFR_all",
        "median_log_sSFR_high_excitation",
        "method",
        "pilot_question",
        "proposal_title",
        "result_bullets",
        "run_id",
        "sample_rows",
        "short_title",
        "slug",
        "source_sample"
      ],
      "source_json_parsed": true,
      "status": "guarded proxy/denominator draft",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
      "tex_exists": true,
      "title": "SDSS high-excitation AGN denominator for outflow escape tests: selection-aware SDSS optical proxy integration"
    },
    {
      "caption_count": 1,

exec
/bin/zsh -lc "sed -n '1,200p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.md" in /Users/duhokim/NebulaMind/NebulaMind
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

exec
/bin/zsh -lc "rg -n \"9298|5,695|5695|4,440|4440|15 cells|0\\.136|0\\.418|0\\.230|0\\.181|3\\.1|6,729|6729|0\\.549|40\\.06|0\\.66 dex|0\\.520|0\\.074|0\\.509|0\\.367|0\\.032 \\+/- 0\\.004|11\\.0--12\\.5|0\\.005-0\\.729|0\\.003-0\\.520|15,000 per quartile|60,000 total\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 205ms:
9.908502,-0.45911800000000014,0.01037656388483131
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:16:300638391848953856,478590230501287936,0.08362079,0.08324894,11.02841,11.03442,-10.77185,-10.63504,-0.13681000000000054,0.017868491723396388
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:40:301767315832203264,504476857421293568,0.08543276,0.0858082,11.03913,11.03121,-12.11881,-10.36737,-1.7514400000000006,0.020237546206305374
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:48:301796452890339328,379528357668218880,0.08473924,0.08486461,10.86919,10.87024,-12.40961,-10.36709,-2.0425200000000014,0.005152241788293884
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:102:305196696793540608,787112648599693312,0.05959919,0.05968505,10.61416,10.6125,-12.30479,-10.74348,-1.5613100000000006,0.004440262333295754
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:125:306294835004860416,586724182616729600,0.09556105,0.09509919,10.9885,10.99383,-11.58788,-10.33369,-1.2541899999999995,0.02009750746106609
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:129:306347061807179776,739817155511478272,0.07387309,0.07409444,10.68089,10.68322,-11.91742,-9.811358,-2.1060619999999997,0.009445373224737017
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:136:306388293493221376,748736118807095296,0.09929239,0.09907762,10.3293,10.32591,-11.0585,-10.18123,-0.8772700000000011,0.010232346076300814
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:140:307388574465026048,665552564158228480,0.03587253,0.03530985,10.54996,10.5562,-12.20357,-10.39967,-1.8038999999999987,0.02426973434900626
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:146:307453995406878720,586724182616729600,0.09517123,0.09509919,10.98837,10.99383,-11.72366,-10.33369,-1.38997,0.010214789418693384
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:173:308559828488316928,498814097207355392,0.07704032,0.07741307,10.52013,10.51928,-10.41481,-10.14595,-0.2688600000000001,0.014330859090552327
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:185:308612879924357120,710466240719644672,0.09729245,0.09739702,11.17866,11.16448,-11.58407,-10.37644,-1.20763,0.025857144377199298
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:203:308662357947607040,734100793904359424,0.09888165,0.09897681,11.05879,11.06122,-11.26519,-10.07455,-1.1906400000000001,0.005691878160132122
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:234:310775344351176704,626061404503304192,0.07433612,0.07412116,10.09415,10.09662,-11.45555,-9.499059,-1.9564909999999998,0.009344634384525187
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:245:310828945543030784,817536410620815360,0.06308059,0.0632806,10.51679,10.52028,-12.25446,-10.3054,-1.9490599999999993,0.009898888016950966
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:266:311906192043567104,575398118539945984,0.08387153,0.08389309,10.33194,10.33123,-10.95075,-10.07414,-0.8766099999999994,0.0015216349503895028
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:307:314169538004412416,606964812110391296,0.03931824,0.03976713,10.29224,10.28859,-10.33498,-10.18144,-0.15353999999999957,0.018376169982971022
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:311:314176409952086016,699193222475311104,0.08849179,0.08875,10.92511,10.92455,-12.30464,-10.52085,-1.7837899999999998,0.009921807899339713
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:324:314252001376495616,646310016747333632,0.04569846,0.04634382,10.80113,10.78885,-12.14474,-11.77681,-0.3679300000000012,0.033136571535739685
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:335:315265744856180736,412190450418477056,0.02933633,0.02904564,10.50676,10.52003,-10.10514,-10.24393,0.1387900000000002,0.0263631216930841
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:360:315386416257329152,583304975594055680,0.07347418,0.07463136,10.94424,10.94059,-11.325,-10.08837,-1.23663,0.04472066042859342
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:364:315395487228258304,448138154629687296,0.07407503,0.07411313,10.47232,10.47301,-10.55128,-10.17545,-0.37583000000000055,0.0019147877670395407
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:379:316490875720984576,744385076334192640,0.04921554,0.04888875,11.04148,11.0598,-12.44798,-9.293333,-3.154646999999999,0.0352897417315111

codex
I’ve confirmed the extra counts appear in the higher-level prompt/source artifacts, so the main question is whether the manuscript text is internally consistent and whether anything depends on a file that is not actually present locally. I’m checking the compile logs now for unresolved citations, missing figures, or other LaTeX failures that would make the package brittle.
exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "rg -n \"Warning|undefined|Citation|Reference|Overfull|Underfull|Missing|LaTeX Error|File .* not found|rerun|multiply\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.compile.log | sed -n '1,120p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
3:warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
4:warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
7:warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
8:warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
11:warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
12:warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86

exec
/bin/zsh -lc "rg -n \"Warning|undefined|Citation|Reference|Overfull|Underfull|Missing|LaTeX Error|File .* not found|rerun|multiply\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log | sed -n '1,160p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Selection-aware SDSS BPT/sSFR study}
     5	\shortauthors{NebulaMind}
     6	\begin{document}
     7	
     8	\title{Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Pilot Matched-Control Study}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We present a selection-aware SDSS DR17 matched-control pilot that measures the association between broad optical BPT-selected galaxies and catalog specific star-formation rate. The analysis is shaped by the SDSS 3-arcsec fiber aperture and by a non-random 60,000-galaxy computational pilot cap sequentially selected by \texttt{specObjID} from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies; the cap is an arbitrary cache limit for local workflow validation and cache budgeting, not a physically motivated or volume-complete subsample. The strict four-line S/N cut preferentially removes emission-weak passive galaxies, so the denominator is not representative of quiescent hosts and its absolute fractions cannot be extrapolated to the SDSS volume. Broad optical BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, with no morphology, aperture-fraction, or environment control. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex; stricter line-S/N and Seyfert-like subsets reduce the offset magnitude to -0.763 dex. This fiber-centered offset is highly degenerate with the well-known mass-morphology relation, as morphology is not controlled in the match. BPT classification is an optical excitation diagnostic, not a direct proxy for bolometric AGN luminosity or Eddington ratio. This result is association-only, not causal. The companion supplement organizes the missing structural, environmental, and multiwavelength observables needed for future follow-up tests, including morphology, aperture fraction, halo or group labels, CO/HI gas measurements, radio and X-ray proxies, and IFU kinematics.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}
    17	
    18	\section{Question and claim boundary}
    19	This paper addresses a narrow association-only question within a low-redshift SDSS DR17 optical emission-line denominator: do broad optical BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a negative catalog-sSFR offset within the analyzed denominator. The result is not a causal claim or inference; it is an association in a capped optical sample and does not test AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling in this dataset.
    20	The 60,000-galaxy computational pilot cap is an arbitrary cache limit rather than a volume-complete census, so it is not normalized into a luminosity or mass function. The cap is retained for local workflow validation and cache budgeting, not to tune the science result.
    21	
    22	
    23	The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations powered by hot post-AGB stars, as well as low-ionization nuclear emission-line region (LINER)-like ionization, can contaminate broad low-ionization classes \citep{cidfernandes2011,stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT-selected galaxies'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label. Because the sample is restricted to $0.02<z<0.12$, the standard local BPT demarcations are used here without any redshift-evolution correction.
    24	
    25	\subsection{Scope and limitations}
    26	The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.
    27	
    28	\section{Data and shared selection}
    29	The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a 60,000-galaxy computational pilot cap selected sequentially by \texttt{specObjID}. It is a local pilot subset used to validate the analysis workflow and establish the relative association within an arbitrary fixed cache budget, not a volume-limited census. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this cap is not a random sky sample and introduces survey-plate and sky-coverage bias. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the cap is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
    30	Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
    31	Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy; the fixed 3-arcsec aperture systematically misses extended star-forming disks at low redshift \citep{kewley2005}. If broad optical BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a galaxy-wide star-formation comparison.
    32	The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}. We use variance-normalized Euclidean matching because the feature space is only two standardized variables, $(\log M_\star,z)$, so the rule stays transparent and the resulting nearest-neighbor control remains easy to interpret as an association baseline.
    33	
    34	\begin{deluxetable*}{lrrr}
    35	\tabletypesize{\scriptsize}
    36	\tablecaption{Selection cascade for the flagship analysis sample.\label{tab:selection}}
    37	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    38	\startdata
    39	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
    40	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
    41	plus galSpecLine join & 416,554 & -- & 83.1\% \\
    42	four BPT lines with valid flux measurements (\texttt{ivar} $> 0$) & 373,445 & 60,000 & 74.5\% \\
    43	four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
    44	four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
    45	four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
    46	\enddata
    47	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The 416,554-to-373,445 drop when requiring \texttt{ivar} $> 0$ reflects the removal of rows with unusable line-flux uncertainties; this table does not distinguish masking, edge-of-chip loss, or missing spectral coverage. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
    48	\end{deluxetable*}
    49	
    50	The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the fixed-size-sample limitation.
    51	
    52	\section{Classification and matching}
    53	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Here, the star-forming control pool is defined as objects below the Kauffmann et al.\ (2003) demarcation. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control by variance-normalized Euclidean distance in standardized $(\log M_\star,z)$ space, with replacement. In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), and the unrestricted Euclidean match has median absolute separations of 0.0045 dex in $\log M_\star$ and 0.00021 in redshift, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements. The preferred estimate does not impose a maximum mass--redshift caliper; the caliper row in Table~\ref{tab:robust} is a sensitivity variant. The moderate mass--redshift caliper sensitivity variant uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.
    54	Here, ``broad optical BPT-selected'' means the inclusive optical-emission-line class under the standard BPT demarcations, while the Seyfert-like sensitivity check uses the stricter Kewley et al.\ (2006) high-excitation cut to remove the low-excitation LINER/retired branch by construction.
    55	
    56	\begin{figure*}
    57	\centering
    58	\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
    59	\caption{BPT line-ratio diagram for the SDSS DR17 analysis denominator. The matched controls are paired in stellar mass and redshift only, not in morphology, so the diagram verifies the optical-excitation classes used for matching but does not by itself prove accretion-driven feedback.}
    60	\label{fig:bpt}
    61	\end{figure*}
    62	
    63	\section{Matched-control result}
    64	The preferred broad optical BPT comparison gives a large negative catalog-sSFR offset for the broad optical BPT-selected galaxies relative to star-forming controls.
    65	\par\noindent\textbf{Morphology and aperture caveat.} A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the observed sSFR offset is highly degenerate with the known mass--morphology relation and the transition from disk-dominated to bulge-dominated systems, including bulge prominence or central velocity dispersion effects \citep{schawinski2010,bluck2014,belfiore2016}. Single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, an ambiguity that requires spatially resolved integral-field spectroscopy to resolve \citep{penny2018,cheung2016}. The robustness interval in Table~\ref{tab:robust} is a 95\% confidence interval on the median offset.
    66	
    67	\begin{deluxetable*}{lrrrr}
    68	\tabletypesize{\scriptsize}
    69	\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
    70	\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
    71	\startdata
    72	Broad optical BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
    73	Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
    74	Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
    75	Broad optical BPT-selected targets, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
    76	N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
    77	\enddata
    78	\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$, and it leaves the median offset essentially unchanged at -1.318 dex for 7,867 pairs. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
    79	\end{deluxetable*}
    80	
    81	\begin{figure*}
    82	\centering
    83	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    84	\caption{Distribution of matched-pair catalog-sSFR offsets for the preferred broad optical BPT-selected galaxy minus nearest star-forming control estimate ($N=8{,}146$ pairs, without a maximum mass--redshift caliper). The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
    85	\label{fig:offsets}
    86	\end{figure*}
    87	
    88	\section{Interpretation}
    89	The result is directly measured in the capped sample and remains falsifiable within the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset persists under a moderate mass--redshift caliper, which is already reflected by the 7,867-pair, -1.318 dex sensitivity row. Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. The Kewley et al.\ (2006) demarcation explicitly removes the retired/LINER-like low-ionization tail, so the larger -1.309 dex offset is driven in part by that broader low-ionization branch rather than solely by Seyfert-like excitation. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad optical BPT-selected sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a galaxy-wide star-formation comparison. Matching on mass and redshift alone leaves morphology uncontrolled, and the fixed 3-arcsec fiber can under-sample extended disk star formation at low redshift; this is a known source of central-to-global mismatch \citep[e.g.,][]{harrison2017,ellison2021}. The central-kiloparsec aperture restriction is one reason this remains a local association rather than a galaxy-wide star-formation measurement. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size, SpecObjID-capped 60,000-galaxy pilot sample. Any causal star-formation change claim requires additional real data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
    90	The choice of variance-normalized Euclidean matching is deliberate: with only two standardized coordinates, it preserves a simple nearest-neighbor control rule without introducing an additional model layer that would not be better constrained by the available data.
    91	
    92	\section{Conclusion}
    93	RP-1 is a selection-aware pilot association paper. Its key results are the preferred -1.309 dex offset, the persistence of the offset under a moderate mass--redshift caliper, and the reduction from -1.309 dex to -0.763 dex under stricter line-S/N and Seyfert-like subsets. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} collects the missing-observable requirements for future physical tests. See Supplement Sections 4.1 and 4.7 for the neighbor-rank/fiber-collision caveat and CO/HI follow-up requirements.
    94	In practice, future follow-up requires integration with the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation comparisons passed through the same selection functions \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,ellison2011,piotrowska2022,wetzel2013,dekel2006}; these references are cited as examples of missing observables for future follow-up, not as validation of any mechanism in this SDSS-only denominator. The result remains association-only until morphology, aperture fraction, and the missing multiwavelength or IFU observables are added.
    95	
    96	\section*{Data Availability}
    97	This paper uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. The 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and the manuscript conclusions remain conditional on the optical-emission-line denominator.
    98	No mock, synthetic, fake, placeholder, or toy data were used.
    99	
   100	\facilities{SDSS}
   101	
   102	\begin{thebibliography}{}
   103	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   104	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   105	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   106	\bibitem[Belfiore et al.(2016)]{belfiore2016} Belfiore, A., Maiolino, R., Maraston, C., et al. 2016, MNRAS, 461, 3111
   107	\bibitem[Bluck et al.(2014)]{bluck2014} Bluck, A.~F.~L., Bruce, V.~A., Pilkington, K., et al. 2014, MNRAS, 441, 599
   108	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   109	\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasi{\'n}ska, G., Schlickmann, S., et al. 2011, MNRAS, 413, 1687
   110	\bibitem[Cheung et al.(2016)]{cheung2016} Cheung, E., Bundy, K., Cappellari, M., et al. 2016, Nature, 533, 504
   111	\bibitem[Ellison et al.(2011)]{ellison2011} Ellison, S.~L., Patton, D.~R., Mendel, J.~T., et al. 2011, MNRAS, 418, 2043
   112	\bibitem[Ellison et al.(2021)]{ellison2021} Ellison, S.~L., Lin, L., Rosario, D.~J., et al. 2021, MNRAS, 501, 4777
   113	\bibitem[Harrison(2017)]{harrison2017} Harrison, C.~M. 2017, Nature Astronomy, 1, 0165
   114	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   115	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   116	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   117	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   118	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   119	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   120	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   121	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   122	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   123	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   124	\bibitem[Kewley et al.(2005)]{kewley2005} Kewley, L.~J., Jansen, R.~A., \& Geller, M.~J. 2005, PASP, 117, 227
   125	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   126	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   127	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   128	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   129	\bibitem[Penny et al.(2018)]{penny2018} Penny, S.~J., Davies, R.~L., Houghton, R.~C.~W., et al. 2018, MNRAS, 476, 979
   130	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   131	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   132	\bibitem[Schawinski et al.(2010)]{schawinski2010} Schawinski, K., Evans, D.~A., Virani, S., et al. 2010, ApJ, 711, 284
   133	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   134	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   135	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   136	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   137	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   138	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   139	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   140	\end{thebibliography}
   141	
   142	\end{document}

 succeeded in 0ms:
3:warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
4:warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
5:warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
6:warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
7:warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
8:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
9:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
10:warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232
13:warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
14:warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
15:warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
16:warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
17:warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
18:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
19:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
20:warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232

exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "card_id": "rp-2",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp2_environment_quenching/figures/m1_rp2_environment_quenching_figure1.pdf",
  "full_proposal_requires": "group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions.",
  "high_density_quenched": {
    "fraction": 0.2304,
    "k": 3456,
    "n": 15000,
    "se": 0.003438176260752203
  },
  "high_minus_low_ci": [
    0.04059666666666669,
    0.059135
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "low_density_quenched": {
    "fraction": 0.18066666666666667,
    "k": 2710,
    "n": 15000,
    "se": 0.0031414033193486656
  },
  "lpm_high_density_coeff": 0.03249480778035638,
  "lpm_high_density_se": 0.003707733046841099,
  "method": "packet-gated-paper-to-wiki-reconciliation",
  "pilot_question": "Does a nearest-neighbour density proxy add quenched-fraction information beyond stellar mass in the SDSS emission-line sample?",
  "proposal_title": "Separating internal and environmental quenching across stellar mass, halo mass, and redshift",
  "result_bullets": [
    "The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.",
    "The high-density quartile has quenched fraction 0.230 (3,456/15,000); the low-density quartile has 0.181 (2,710/15,000).",
    "The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].",
    "A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "SDSS density proxy for environmental quenching",
  "slug": "m1_rp2_environment_quenching",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS denominator/proxy atlas}
     5	\shortauthors{NebulaMind}
     6	\begin{document}
     7	
     8	\title{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	This supplement is the companion to the selection-aware SDSS BPT/sSFR pilot study and organizes eight SDSS DR17 denominator and proxy notes into one coherent, association-only optical baseline atlas built around the same 60,000-galaxy computational pilot cap and selection-function caveats. The 60,000-galaxy sample is a local, non-random computational pilot cap kept for local workflow validation and cache budgeting rather than as a physical or volume-limited census, so all counts and fractions remain conditional on the SDSS optical selection used here. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this cap is not a random sky sample and introduces survey-plate and sky-coverage bias. The atlas preserves follow-up targets for environment, broad optical BPT-selected incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-based comparison data are treated as missing observables for future tests rather than as measurements in this package. The sample coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one atlas with eight linked entries, not eight independent causal-feedback papers. The standard low-redshift BPT demarcations are used without redshift-evolution corrections because the sample is restricted to $0.02<z<0.12$. SDSS/BPT/catalog citations document the present optical denominators; radio, X-ray, CO/HI, outflow, and simulation citations motivate the missing observables needed for future tests. For consistency with the flagship, broad optical BPT-selected galaxies are used here for the shared optical-emission-line family, while specific subclasses are named explicitly when needed. Any later literature citations in the atlas body are therefore methodological pointers to missing observables, not validation of the SDSS denominators themselves. \textbf{This atlas provides observational baselines only; it is a selection-biased optical denominator, not a physical feedback test, and it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}
    17	
    18	\section{Purpose}
    19	The main paper measures an optical association between BPT classification and catalog sSFR. These eight entries are distinct baseline-and-follow-up atlas notes: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the entries span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. For consistency with the flagship, the atlas uses the broad optical BPT-selected family when the full optical-emission-line denominator is meant and names specific subsets only when the stricter selection matters. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. This is an association-only optical baseline atlas, and keeping the notes in one supplement keeps the atlas coherent and gives future work a single checklist of what still must be added.
    20	
    21	\section{Shared denominator}
    22	The atlas uses the same analyzed public-data backbone as the main paper: 60,000 galaxies in a computational pilot cap from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, i.e. 24.0\% sample coverage. The four-line selection is sSFR-dependent and the sample is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The galaxy-by-galaxy stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing. The 60,000-row cache is an arbitrary computational pilot cap, not a physical selection threshold.
    23	
    24	The eight subsections below are intentionally parallel baseline-plus-follow-up notes: each one states the observed optical denominator or target vector, then names the missing observables that a future multiwavelength or simulation-based test would need before any physical inference can be made. In other words, the sections are distinct follow-up domains bounded by the same optical selection effect, and their role is to organize the atlas rather than to stand as separate papers.
    25	
    26	\begin{deluxetable*}{lrrr}
    27	\tabletypesize{\scriptsize}
    28	\tablecaption{Selection cascade shared by the atlas; the cache cap is summarized in the main paper.\label{tab:supp-selection}}
    29	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    30	\startdata
    31	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
    32	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
    33	plus galSpecLine join & 416,554 & -- & 83.1\% \\
    34	four BPT lines with valid flux measurements (\texttt{ivar} $> 0$) & 373,445 & 60,000 & 74.5\% \\
    35	four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
    36	four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
    37	four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
    38	\enddata
    39	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The 416,554-to-373,445 drop when requiring \texttt{ivar} $> 0$ reflects the removal of rows with unusable line-flux uncertainties; this table does not distinguish masking, edge-of-chip loss, or missing spectral coverage. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
    40	\end{deluxetable*}
    41	
    42	\section{Atlas summary}
    43	Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight entries. All eight entries are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or forward-model comparison data are added, so their present role is to organize follow-up rather than to establish causal physical claims.
    44	
    45	\begin{deluxetable*}{llll}
    46	\tabletypesize{\scriptsize}
    47	\tablecaption{Atlas-level follow-up menu. Each row summarizes the present optical role and the missing observables needed before any physical inference.\label{tab:atlas-summary}}
    48	\tablehead{\colhead{Topic} & \colhead{Observed baseline} & \colhead{Missing observables} & \colhead{Future Follow-up Domain}}
    49	\startdata
    50	Environment & low-sSFR vs.\ 10th-neighbor rank (60,000 total; 15,000 per quartile) & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test \\
    51	Maintenance heating & broad optical BPT-selected hosts in massive low-sSFR galaxies (maintenance-heating baseline; 9,298 massive; 5,695 low-sSFR) & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
    52	Outflow kinematics & high-excitation broad optical BPT-selected subset (4,440/60,000) & resolved velocities; halo potentials; multiphase gas; CGM tracers & kinematic follow-up \\
    53	Env.\ jets & density-stratified broad optical BPT-selected fraction in massive hosts & radio morphology/age; cavity energetics; hot-gas density & radio-jet follow-up \\
    54	Mass bin & low-sSFR and broad optical BPT-selected incidence by $M_\star$ bin (15 cells with $n\geq50$) & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
    55	Tracer census & tracer prevalence in 60k sample (0.136 to 0.418) & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
    56	Gas depletion & gas-depletion low-sSFR baseline; H$\alpha$ proxy (6,729 galaxies) & CO/dust gas masses; aperture-matched SFRs; morphology; environment & CO/HI follow-up \\
    57	Simulation vector & mass-redshift target vector (15 cells with $n\geq50$) & simulations through SDSS/MaNGA/ALMA/X-ray/radio selection; aperture/noise models & forward model \\
    58	\enddata
    59	\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects the optical emission-line selection function, which preferentially removes low-equivalent-width or passive systems from the denominator; the surviving sample therefore becomes less representative of quiescent hosts as the cut tightens.}
    60	\end{deluxetable*}
    61	
    62	\section{Atlas notes}
    63	As a reminder, each atlas entry is a baseline-plus-follow-up checklist, not a standalone physical-feedback result.
    64	
    65	\subsection{Relative neighbor-count baseline: SDSS 10th-neighbor index for low-sSFR incidence}
    66	We establish a relative neighbor-count baseline within the emission-line denominator that can later be joined to group catalogs and halo masses. The 10th-neighbor index is the rank of the 10th nearest companion in projected sky separation within this redshift-limited sample; it is an internal ordinal rank within this selection-biased sample and does not map to physical environmental volume density or halo density. Because no additional line-of-sight velocity window is imposed beyond the redshift slice, the statistic is especially susceptible to projection effects. The projected-neighbor ranking is computed within the full $0.02<z<0.12$ redshift slice, with no additional line-of-sight velocity window imposed beyond those sample limits. The SDSS 55-arcsec fiber-collision limit systematically removes close neighbors in dense regions, so the 10th-neighbor proxy is biased before any physical interpretation is attempted. We emphasize that the SDSS 55-arcsec fiber collision limit systematically biases this index in dense environments, precluding its use as a physical density metric without forward-modeled corrections. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004 coefficient uncertainty. The follow-up ingredients are group catalogues, robust central/satellite labels, halo masses, a spectroscopic fiber-collision correction at the 55-arcsec scale, morphology, and multi-redshift selection functions. Within this selection-biased emission-line sample, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
    67	\begin{figure}
    68	\centering
    69	\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
    70	\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up.}
    71	\label{fig:m1-rp2-neighbor-count-baseline}
    72	\end{figure}
    73	
    74	
    75	\subsection{Maintenance-heating denominator: broad optical BPT-selected hosts in massive SDSS galaxies}
    76	We isolate the broad optical BPT-selected duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the broad optical BPT-selected fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The broad optical BPT-selected fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. This optical fraction represents an observational baseline pool, not the active maintenance-heating duty cycle. See the next subsection for the related radio-jet baseline that uses the same projected-density proxy. The follow-up ingredients are X-ray cavity or cooling-luminosity measurements, radio jet powers \citep[e.g.,][]{hardcastle2020}, halo-selected parent catalogues, and nondetection modelling. Those observables are missing here; this entry remains an optical baseline only, and future follow-up requires those real observables before any physical inference.
    77	
    78	\begin{figure}
    79	\centering
    80	\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
    81	\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements.}
    82	\label{fig:m1-rp3-maintenance-heating}
    83	\end{figure}
    84	
    85	
    86	\subsection{High-excitation broad optical BPT-selected baseline: resolved kinematics follow-up}
    87	We isolate the high-excitation broad optical BPT-selected denominator that resolved kinematics would need to test escape versus recycling. High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The follow-up ingredients are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
    88	
    89	\begin{figure}
    90	\centering
    91	\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
    92	\caption{SDSS optical emission-line denominator: the high-excitation BPT-selected subset used to define an observational baseline for future resolved-kinematic measurements.}
    93	\label{fig:m2-p1-outflow-escape-recycling}
    94	\end{figure}
    95	
    96	
    97	\subsection{Radio-jet environment baseline: broad optical BPT-selected fraction vs. 10th-neighbor index in massive hosts}
    98	We define the environment-stratified optical denominator that future radio and X-ray work could test. This subsection reuses the same projected-neighbor ranking described in the relative neighbor-count baseline above and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has a broad optical BPT-selected fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The follow-up ingredients are radio jet morphology and age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
    99	
   100	\begin{figure}
   101	\centering
   102	\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
   103	\caption{SDSS optical emission-line denominator: the high- and low-density quartile comparison among massive SDSS hosts, used as a baseline for future radio-jet and X-ray work.}
   104	\label{fig:m2-p2-radio-jet-environment}
   105	\end{figure}
   106	
   107	
   108	\subsection{Stellar-mass selection diagnostic: low-sSFR and broad optical BPT-selected incidence}
   109	In this optical-emission-line denominator, the 11.0--12.5 dex peak is consistent with a selection-function effect: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is concentrated in that mass bin. It must not be interpreted as a universal physical threshold. We identify the mass bin where a future gas-inclusive study should look for a selection-sensitive change in incidence. The note measures the incidence of low catalog-sSFR and broad optical BPT-selected classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the broad optical BPT-selected incidence peaks in the 11.0--12.5 bin at 0.520 within this selection-limited, SpecObjID-capped pilot sample. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The follow-up ingredients are gas fractions, baryon deficits, halo masses, central velocity dispersion proxies \citep{piotrowska2022}, stellar-feedback observables, and high-redshift extensions. The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
   110	
   111	\begin{figure}
   112	\centering
   113	\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
   114	\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and broad optical BPT-selected incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up.}
   115	\label{fig:m2-p3-feedback-transition-mass}
   116	\end{figure}
   117	
   118	
   119	\subsection{Tracer-threshold census for multiphase follow-up}
   120	We compare optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred broad optical BPT-selected or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The follow-up ingredients are ionized, molecular, and neutral tracers, X-ray or radio tracers, a shared parent denominator, and a consistent aperture model. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
   121	
   122	\begin{figure}
   123	\centering
   124	\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
   125	\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work.}
   126	\label{fig:m3-p1-multiphase-census}
   127	\end{figure}
   128	
   129	
   130	\subsection{Low-sSFR optical denominator: baseline for future CO/HI gas measurements}
   131	We define the denominator for CO/HI gas-fraction and depletion-time follow-up. Using the gas-depletion note's low-sSFR baseline, the massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its broad optical BPT-selected fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency or measure total cold-gas mass \citep{tacconi2018}; this note identifies the CO/HI follow-up denominator and optical baseline required for spatially resolved gas tests. The follow-up ingredients are CO or dust-based molecular gas masses \citep[e.g., xCOLD GASS;][]{xcoldgass2017}, atomic hydrogen masses \citep[e.g., xGASS;][]{xgass2018}, aperture-matched SFRs, morphology, and environment labels, together with radio, X-ray, and IFU observables that are still missing here. As with any H$\alpha$-based proxy, residual dust attenuation and stellar-absorption systematics can still affect the optical denominator, so this value should be read as a line-luminosity proxy rather than a direct total cold-gas-mass measurement. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference. No mock, synthetic, fake, placeholder, or toy data were used in compiling this atlas.
   132	
   133	\begin{figure}
   134	\centering
   135	\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
   136	\caption{SDSS optical emission-line denominator: the massive low-sSFR SDSS galaxies available for CO/HI depletion-time follow-up.}
   137	\label{fig:m3-p2-gas-depletion-efficiency}
   138	\end{figure}
   139	
   140	
   141	\subsection{Simulation target vector for forward-model comparison}
   142	We provide a compact observed target vector for forward modelling. The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, broad optical BPT-selected incidence, and colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and broad optical BPT-selected fractions span 0.003-0.520. The follow-up ingredients are simulations \citep{eagle2015} passed through the exact optical S/N and fiber-aperture selection function used here, including the sequential 60,000-row \texttt{specObjID} cache cap, then through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions, together with aperture models and noise models. Without those matched selection steps, any simulation comparison is not a valid test. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
   143	
   144	\begin{figure}
   145	\centering
   146	\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
   147	\caption{SDSS optical emission-line denominator: low-sSFR fraction, broad optical BPT-selected incidence, and colour versus mass and redshift in the SDSS emission-line sample. This is an observed target vector for forward modelling.}
   148	\label{fig:m3-p3-simulation-validation}
   149	\end{figure}
   150	
   151	\section{Package decision}
   152	These eight entries should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.
   153	
   154	\section*{Data Availability}
   155	This atlas uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. No mock, synthetic, fake, placeholder, or toy data were used. The 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and all eight notes remain conditional on the optical-selection denominators summarized in this atlas.
   156	
   157	\facilities{SDSS}
   158	
   159	\begin{thebibliography}{}
   160	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   161	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   162	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   163	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   164	\bibitem[Ellison et al.(2021)]{ellison2021} Ellison, S.~L., Lin, L., Rosario, D.~J., et al. 2021, MNRAS, 501, 4777
   165	\bibitem[Hardcastle \& Croston(2020)]{hardcastle2020} Hardcastle, M.~J., \& Croston, J.~H. 2020, New Astronomy Reviews, 88, 101539
   166	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   167	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   168	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   169	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   170	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   171	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   172	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   173	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   174	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   175	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   176	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   177	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   178	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   179	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   180	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   181	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   182	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   183	\bibitem[Tacconi et al.(2018)]{tacconi2018} Tacconi, L.~J., Genzel, R., Saintonge, A., et al. 2018, ApJ, 853, 179
   184	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   185	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   186	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   187	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   188	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   189	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   190	\end{thebibliography}
   191	
   192	\end{document}

exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "card_id": "rp-3",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/figures/m1_rp3_maintenance_heating_figure1.pdf",
  "full_proposal_requires": "X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.",
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "massive_agn_fraction": {
    "fraction": 0.4298773929877393,
    "k": 3997,
    "n": 9298,
    "se": 0.005134068554795429
  },
  "massive_quenched_agn_fraction": {
    "fraction": 0.6073748902546093,
    "k": 3459,
    "n": 5695,
    "se": 0.006470987903713825
  },
  "massive_quenched_rows": 5695,
  "massive_rows": 9298,
  "method": "packet-gated-paper-to-wiki-reconciliation",
  "pilot_question": "Among massive, low-sSFR SDSS emission-line galaxies, what optical AGN fraction is available as a denominator for X-ray/radio maintenance-heating follow-up?",
  "proposal_title": "Empirical duty-cycle constraints on AGN maintenance heating in massive halos",
  "result_bullets": [
    "The massive subset (logM >= 10.8) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.",
    "The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.",
    "This provides an optical duty-cycle denominator for X-ray/radio maintenance-heating follow-up, not a heating-to-cooling measurement."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "Optical-AGN denominator for maintenance-heating follow-up",
  "slug": "m1_rp3_maintenance_heating",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}
codex
The supplement’s counts are also traceable to the topic source files, not invented ad hoc. I’m doing one last pass over the remaining topic source JSONs to make sure the quoted fractions and medians match the cited local results before I summarize any weaknesses.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "card_id": "p1",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p1_outflow_escape_recycling/figures/m2_p1_outflow_escape_recycling_figure1.pdf",
  "full_proposal_requires": "resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.",
  "high_excitation_agn": {
    "fraction": 0.074,
    "k": 4440,
    "n": 60000,
    "se": 0.0010686751923136733
  },
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "median_log_sSFR_all": -10.140585,
  "median_log_sSFR_high_excitation": -11.53205,
  "method": "source-first-paper-adjudication",
  "pilot_question": "How large is the SDSS high-excitation optical-AGN denominator that would need resolved kinematics to test escape versus recycling?",
  "proposal_title": "Escape versus recycling: the fate of AGN-driven multiphase outflows",
  "result_bullets": [
    "High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).",
    "Their median log sSFR is -11.53, compared with -10.14 for the full denominator.",
    "SDSS does not measure escape velocity or multiphase outflow velocities here; the pilot supplies a denominator for resolved follow-up rather than an escape/recycling result."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "SDSS high-excitation AGN denominator for outflow escape tests",
  "slug": "m2_p1_outflow_escape_recycling",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "agn_fraction_range": [
    0.0027030347708563705,
    0.5202082816761716
  ],
  "card_id": "p3",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/figures/m3_p3_simulation_validation_figure1.pdf",
  "full_proposal_requires": "simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.",
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "method": "debate-map-to-wiki-rebuild",
  "pilot_question": "What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation?",
  "proposal_title": "Forward-modelled validation of cosmological feedback prescriptions",
  "quenched_fraction_range": [
    0.005283204324855633,
    0.7292338209769402
  ],
  "result_bullets": [
    "The pilot writes 15 mass-redshift cells with n >= 50 as a compact validation vector.",
    "Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.",
    "The output is an observed target vector for simulation forward modelling, not a direct simulation comparison."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "SDSS target vector for feedback-model validation",
  "slug": "m3_p3_simulation_validation",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "target_vector_cells": [
    {
      "agn_fraction": 0.002902757619738752,
      "mass_bin": "8.0-9.5",
      "median_u_minus_r": 1.5324300000000015,
      "n": 6201,
      "quenched_fraction": 0.006450572488308337,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.0006105006105006105,
      "mass_bin": "8.0-9.5",
      "median_u_minus_r": 1.378694999999999,
      "n": 1638,
      "quenched_fraction": 0.0006105006105006105,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.01,
      "mass_bin": "8.0-9.5",
      "median_u_minus_r": 1.0446000000000009,
      "n": 300,
      "quenched_fraction": 0.006666666666666667,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.030219018574993067,
      "mass_bin": "9.5-10.0",
      "median_u_minus_r": 1.8540899999999991,
      "n": 3607,
      "quenched_fraction": 0.06099251455503188,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.008417230566100017,
      "mass_bin": "9.5-10.0",
      "median_u_minus_r": 1.6964299999999994,
      "n": 6059,
      "quenched_fraction": 0.013038455190625516,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.0013717421124828531,
      "mass_bin": "9.5-10.0",
      "median_u_minus_r": 1.5156199999999984,
      "n": 2187,
      "quenched_fraction": 0.003200731595793324,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.15361242403781228,
      "mass_bin": "10.0-10.5",
      "median_u_minus_r": 2.2637100000000006,
      "n": 2962,
      "quenched_fraction": 0.25557056043214044,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.09022556390977443,
      "mass_bin": "10.0-10.5",
      "median_u_minus_r": 2.119389999999999,
      "n": 7581,
      "quenched_fraction": 0.160928637382931,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.03968346328406843,
      "mass_bin": "10.0-10.5",
      "median_u_minus_r": 1.9204700000000017,
      "n": 8593,
      "quenched_fraction": 0.06202723146747353,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.42955145118733506,
      "mass_bin": "10.5-11.0",
      "median_u_minus_r": 2.6227300000000007,
      "n": 1895,
      "quenched_fraction": 0.5810026385224274,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.2968719260279363,
      "mass_bin": "10.5-11.0",
      "median_u_minus_r": 2.5802999999999994,
      "n": 5083,
      "quenched_fraction": 0.45130828251032856,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.2089037622959132,
      "mass_bin": "10.5-11.0",
      "median_u_minus_r": 2.45496,
      "n": 9861,
      "quenched_fraction": 0.3260318426123111,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.6102564102564103,
      "mass_bin": "11.0-12.5",
      "median_u_minus_r": 2.83066,
      "n": 390,
      "quenched_fraction": 0.8564102564102564,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.5629691409507923,
      "mass_bin": "11.0-12.5",
      "median_u_minus_r": 2.850570000000001,
      "n": 1199,
      "quenched_fraction": 0.804837364470392,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.484860883797054,
      "mass_bin": "11.0-12.5",
      "median_u_minus_r": 2.8379250000000003,
      "n": 2444,
      "quenched_fraction": 0.6718494271685761,
      "z_bin": "0.08-0.12"
    }
  ]
}
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "agn_fraction_in_denominator": {
    "fraction": 0.5486699360974885,
    "k": 3692,
    "n": 6729,
    "se": 0.006066349807598532
  },
  "card_id": "p2",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p2_gas_depletion_efficiency/figures/m3_p2_gas_depletion_efficiency_figure1.pdf",
  "full_proposal_requires": "CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.",
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "massive_transition_quenched_rows": 6729,
  "median_log_lha_denominator": 40.06117405071403,
  "median_log_lha_offset_vs_massive_sf": -0.6585859816891073,
  "method": "debate-map-to-wiki-rebuild",
  "pilot_question": "How many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction/depletion-time follow-up?",
  "proposal_title": "Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies",
  "result_bullets": [
    "The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.",
    "Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.",
    "The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.",
    "SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "Optical denominator for gas-fraction versus efficiency tests",
  "slug": "m3_p2_gas_depletion_efficiency",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}
 succeeded in 0ms:
{
  "card_id": "p2",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p2_radio_jet_environment/figures/m2_p2_radio_jet_environment_figure1.pdf",
  "full_proposal_requires": "radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.",
  "high_density_massive_agn": {
    "fraction": 0.5085836909871244,
    "k": 948,
    "n": 1864,
    "se": 0.011579319665266517
  },
  "high_minus_low_ci": [
    0.11189880364416133,
    0.1702164814837969
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "low_density_massive_agn": {
    "fraction": 0.3667152221412964,
    "k": 1007,
    "n": 2746,
    "se": 0.009196312633686535
  },
  "massive_rows": 9298,
  "method": "source-first-paper-adjudication",
  "pilot_question": "Does a local-density proxy modulate the optical AGN fraction in massive SDSS hosts, motivating environment-stratified radio/X-ray jet-coupling follow-up?",
  "proposal_title": "Environmental dependence of radio-jet coupling efficiency in galaxy gas",
  "result_bullets": [
    "Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.",
    "The bootstrap high-minus-low interval is [0.112, 0.170].",
    "This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "Environment proxy for optical AGN in massive SDSS hosts",
  "slug": "m2_p2_radio_jet_environment",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}
 succeeded in 0ms:
{
  "card_id": "p1",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p1_multiphase_census/figures/m3_p1_multiphase_census_figure1.pdf",
  "full_proposal_requires": "ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.",
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "method": "debate-map-to-wiki-rebuild",
  "pilot_question": "How strongly do simple optical tracer definitions change the inferred AGN/feedback-candidate prevalence in one common SDSS denominator?",
  "prevalence_ratio_widest_to_narrowest": 3.080775840903511,
  "proposal_title": "A multiphase, common-denominator census of AGN-driven outflows",
  "result_bullets": [
    "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.",
    "The widest-to-narrowest prevalence ratio is 3.1, before adding molecular, neutral, or X-ray/radio phases.",
    "This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "Common-denominator optical tracer census in SDSS",
  "slug": "m3_p1_multiphase_census",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "tracer_prevalence": {
    "BPT AGN": {
      "fraction": 0.13576666666666667,
      "k": 8146,
      "n": 60000,
      "se": 0.0013984162404239596
    },
    "high [NII]/Ha": {
      "fraction": 0.19161666666666666,
      "k": 11497,
      "n": 60000,
      "se": 0.0016067551136904373
    },
    "high [OIII]/Hb": {
      "fraction": 0.31698333333333334,
      "k": 19019,
      "n": 60000,
      "se": 0.0018995828477248288
    },
    "low-sSFR+emission": {
      "fraction": 0.20683333333333334,
      "k": 12410,
      "n": 60000,
      "se": 0.0016535482331215075
    },
    "red+emission": {
      "fraction": 0.4182666666666667,
      "k": 25096,
      "n": 60000,
      "se": 0.002013784423344193
    }
  }
}
codex
I have the core traceability on the headline counts. The remaining risk is a smaller one: a few derived percentages and physical scale numbers may be correct but are not explicitly anchored to a local analysis artifact or citation, which matters for this package even if the compilation succeeds.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
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
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/figures/figure2_matched_offsets.pdf" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
%PDF-1.4
%�� ��
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
8 0 obj
<< /Font 3 0 R /XObject 7 0 R /ExtGState 4 0 R /Pattern 5 0 R
/Shading 6 0 R /ProcSet [ /PDF /Text /ImageB /ImageC /ImageI ] >>
endobj
11 0 obj
<< /Type /Page /Parent 2 0 R /Resources 8 0 R /MediaBox [ 0 0 756 316.8 ]
/Contents 9 0 R /Annots 10 0 R >>
endobj
9 0 obj
<< /Length 12 0 R /Filter /FlateDecode >>
stream
x�͜M������<�����>� ��"l@��l��4+K+[ɿ�[���F��`�3�4���Ϫ&��n�zss���w��Ϻ���澣�-���m�?��_����ۮK!���:�&㳝>���c�G��.X�S��׺�M§��w�w����/>}j���J%S��`l�?��������<X4�]��2��hQ�#�:k�
9����j�tߔ�b0�mtq"Idr.d�ĲTګF����ZoA��)�R��ʂq;Dww]�y�6L�V!��F�c*u;`
Ů+dB�i�Z*���,�Q6�`�ODUQ����dW-@vYo�#�Ħ�`b�ĮE��
�-P@Gd�rquM�R6���@+yKx-��%�c�ji��JL��V���7{p�;��ƣ����J�\K8G���|ݬ������8ϙ��%��E�	�e\[�&)[,�W̩��)��x�@�	V�*I�E�����g�� [ «�HJM�I�d
q(�������KX�;Rx��Kd)1αg���E�)��(��a r-�ַ�� C�S��6�*1bfl��[p�o	���hJ�X-�$�W�7�� 0;�!�H�0UB ��Zp�o	��`�ՐBV|���Y4�}����%��F #� l�j����TL��,A�k}S�
ͮc��,%�Jb�H��9��7��`�b2'Ŷ���&K-��7��9�EѸ|����>:攜F���Z�1�]�ukW�`���͡��%��E�d9���$Q����f�J�`C@
Y��1��(G�z�
˿��� [ z,�P#%
{y�%7�J�^�"xŰK��$��[NkS���M64 �d��m]I���p�o	��`d�OQm�U�㈂e�n%o	�e�l�ǲ��
a��Rط�Z�ޜt)�����^�R�sVƣ����Z�e����ܫ�O�ru����ײ^6����^��b�PkySx
�e!�$=���Aoe_��Z�^˲�%�r�n�J
�m��]K��
�-X/$G�7I�f��Zɛ�kX�G���j§�9�Q�-�,�cBr*�d�S����/�松��ecC��a-%�ɻ�@WuSp
	��7��^W�"GC�!V���yBd�z�AK�$K!�9�R�עv/ld�)�*�a����lI <�F���0%�� ��Ǟ��|�����IZ3���w�?��R�;g�]G����m�G� l(�y���s�.}�����w�O!}��e��<ey%���/�_��M�{����oϻp�J��~�������o������G�7w��?��vO������z��"Ti�k������')�5n��p;��!3�IJZw��XT�Y����^p��:̖�2�WyK��RV���}F#gt��N
��m'om��`�� �>�{�ZZ5��`%c6e��g�#��c���X�D$)x�q���@%��$�C����	�u"aU:Uպ/�}�?۱I)�CA)r�~�z���r�j�A�cG�`]�~@
`K���t���X��jEO��)ִj���x�s䩞~��J9�6����K�hʤ.y<֥�a��j��/���u�<�����Md
�s�ڍ
�<���C��
���|:`��������|�{��в�)}q{�fl/�w�*�Wv�j=k�����8��Q!\<c���߾~9��Sh� �y������L�l04-��r��#���Au�*�;��$h������vݛ�2-"E�LV���
V�֌��3
�\D��m�21j�����N['�D������*z�z�;��R�^�/X���h#���[7/��|��;X��i�OL�)%�C)'���C�I��S�W��C���0�������N�y$5�������0I�*�������=Vxd�W?��������3�P���P����wP:y��a[RA���D�g_gv0	����`ę�m�B����y
�t�պ��j�1�p��4������1���1(s�}���x��:�v�8"%F�&�*��лr���r�j���
��}�.=x����U���Uu���x�ݾxs}��#�sԿ�F�\�؋�7�f�_U��J���^ב��f����Px��Q3b�����"��� �0C���}��p�w�N�mFe���/�2Rfuĭ��xV���y�rV$�͑��'d���T����Gy. D$�H��3���;�$jNTi�|��*b�
��1_��XH�\��8,��;��YƏ���K(ʺ���ǈ8�#�;����G�w�3]MԵ�j?Z2D�ǝ����?b�+�!D����n�
F!�tV�#�8Ə��e�ֺ�jiݾ<)��t�������${��/��*�֓M�=80��y�l�J&���n���N_9�j
y���~��2�mҙ�r�r��E����d��ϋL�49�M�\��DIl��"r2c�w4'a�>��dV���Gi�G�/W��r�����xƂvY�!��R�<u��N0j���ɴ9��!��˩	��nBu]��}'��'�w�e�q���8����7�i�|��G�C��l�9�s��3����11�]�Z��_p>���|���7�:Lf����J<X�O��'y|��b���t���!���f9J�+��%�&.r�/3����J�ڱ����6�?[����se7���XQ�����`[%�a�a9�c㤡mh<.C�n%����-y�^��:��GtTPxL�N�ꐍN7���K�"-� $u:mڵi~?�f�S>���&�o�%�CF�<G���*5X�;2��q{��四�ٓ_��n?ޣ)�?ݾ{w���]�������z���#��?���:���f�~c�B̑@"����×dK��6�����Z�nV�������[;r<8&�"�0�%l��σ��$zD���?n�7�����NtGX��o6�O�W��*a4��2� �����b8�anX�x��KT�b����
�GK�8�?0����z�יd�ȝ����
.ƹ���JK�Զ��J5�2<k����Z�T���]C�%���u���Y�,���1�ʇ�����g�,XE^��]�}�JNV&}�2N��^?��E!r8勨r�g?V
v��0Ϋq�
�A92��ƙd�e1�r>2��k�l��XφF���<��Ά(�
�j,�� 9��l���ђ2^ϼ�8�t�uP��CX��Z��$Om먪T#*ó&�^��Q@�%����!bC*�g����a�g����������
endstream
endobj
12 0 obj
3296
endobj
10 0 obj
[ ]
endobj
18 0 obj
<< /Length 96 /Filter /FlateDecode >>
stream
x�=�9� {^���?�c��oE<���I�0��[B�7�<Aȇ
tad�&}���^j�(X3f:3�L�3��'��:�R�L~>��p��*�0
endstream
endobj
16 0 obj
<< /Type /Font /BaseFont /GCWXDV+DejaVuSans-Oblique /FirstChar 0
/LastChar 255 /FontDescriptor 15 0 R /Subtype /Type3
/Name /GCWXDV+DejaVuSans-Oblique /FontBBox [ -1016 -351 1660 1068 ]
/FontMatrix [ 0.001 0 0 0.001 0 0 ] /CharProcs 17 0 R
/Encoding << /Type /Encoding /Differences [ 77 /M ] >> /Widths 14 0 R >>
endobj
15 0 obj
<< /Type /FontDescriptor /FontName /GCWXDV+DejaVuSans-Oblique /Flags 96
/FontBBox [ -1016 -351 1660 1068 ] /Ascent 929 /Descent -236 /CapHeight 0
/XHeight 0 /ItalicAngle 0 /StemV 0 /MaxWidth 1350 >>
endobj
14 0 obj
[ 600 600 600 600 600 600 600 600 600 600 600 600 600 600 600 600 600 600
600 600 600 600 600 600 600 600 600 600 600 600 600 600 318 401 460 838 636
950 780 275 390 390 500 838 318 361 318 337 636 636 636 636 636 636 636 636
636 636 337 337 838 838 838 531 1000 684 686 698 770 632 575 775 752 295
295 656 557 863 748 787 603 787 695 635 611 732 684 989 685 611 685 390 337
390 838 500 500 613 635 550 635 615 352 635 634 278 278 579 278 974 634 612
635 635 411 521 392 634 592 818 592 592 525 636 337 636 838 600 636 600 318
352 518 1000 500 500 500 1350 635 400 1070 600 685 600 600 318 318 518 518
590 500 1000 500 1000 521 400 1028 600 525 611 318 401 636 636 636 636 337
500 500 1000 471 617 838 361 1000 500 500 838 401 401 500 636 636 318 500
401 471 617 969 969 969 531 684 684 684 684 684 684 974 698 632 632 632 632
295 295 295 295 775 748 787 787 787 787 787 838 787 732 732 732 732 611 608
630 613 613 613 613 613 613 995 550 615 615 615 615 278 278 278 278 612 634
612 612 612 612 612 838 612 634 634 634 634 592 635 592 ]
endobj
17 0 obj
<< /M 18 0 R >>
endobj
23 0 obj
<< /Length 91 /Filter /FlateDecode >>
stream
x�5��
�0D{���8������m�-�=��l`d��#����pSLRN�wj�7;�%��4�z.�q����Q$��D�˕g�_|>ob
endstream
endobj
24 0 obj
<< /Length 76 /Filter /FlateDecode >>
stream
x�357U0P�� ���
�F�
)�\@>������L̀,CKd���!�eba��26���"X@lM����4 5
endstream
endobj
25 0 obj
<< /Length 247 /Filter /FlateDecode >>
stream
x�MQIn�0���� ���yO�A���%��#K\���D^�P�B���F^	���֜���?�F��?T[ 1Q$tQ7�H7�
�~��W��X�w+�[:v������*�B<���HZ�D��=��sCt� �>7!Di�^�����um4��6�'��G���I���)f�l��m*V2
7����TFZ�6�2���2ZOv�&���'��q�.;;b���>��|����i���qA"4ť�g���x� �O\&
endstream
endobj
26 0 obj
<< /Length 90 /Filter /FlateDecode >>
stream
x�=��
�0C�L��S�TU��׆|z�[ȸ	�څ�o��'u`]^Bd��;�Jf��&��$q�D�;MJ����������
endstream
endobj
27 0 obj
<< /Length 77 /Filter /FlateDecode >>
stream
x�5��
�0�L�8�P���>���-D|�3�z�p�L�|�����8P��Lhڳ��$���#�'�ҫb��E�ɞ
endstream
endobj
28 0 obj
<< /Length 232 /Filter /FlateDecode >>
stream
x�=�Kr!C��BG �<�J͢�����l����qg����afP���C�`;���g@N�.t)p�ڄs|�Û
����l�H���L!�0&Il�I�6�hr�ܪT�Lk���rw��kږ½���8�T9�*k�6�Ek�F�ϣ�h�Y*�7�M]�Û��Y����\��,���÷�W��*��ʄ�R���9�����p���z�G{&Hpu� U����Sz�S�$����W
endstream
endobj
29 0 obj
<< /Length 341 /Filter /FlateDecode >>
stream
x�5R;қA�S��Y��y�ɤ�s�6;,�B��x�!�Q��%O0^'�w�<��ǻ�Z�T��6m��X�&
�F,��Ǿ%�xj�=iLF$q����z�)�߀4mN%I��[Î/2HzRÒ����V�	scM$#�V����3\�c$��$����i�c�%2O��ů��Z�1���@�6�l'3�E��$7qM���Xs��PR侻���^�����+!��Z�1COY�d�A	T�� 3�׾0N�F	wj��+����$��vVJ��9�e�9�d�;&l����=���7��-�+�9�d��E�����)�%�C�<�����������(~#
endstream
endobj
30 0 obj
<< /Length 307 /Filter /FlateDecode >>
stream
x�=�Kn1C�>�.��ٞ�(����'%��Ej��LYS�4����p���;l�ff�Z������b�|��F]Y'��f:��Q96M���,��.x�&�[�?�Р�5.	7tW�e)4c���{��2�jL]lR�{<^DU��G�"c���A	�J�hZ��wEA���{	���jȲ���;)f��tR.n�!�����kB���+%�H؆3r'�h������ލK��h!��n�.`�S:EbdNr�i�UN�Pӹý�lEC)s���_��k�lxJ���&KV�ۨN�<���Z�t
endstream
endobj
31 0 obj
<< /Length 232 /Filter /FlateDecode >>
stream
x�5QIn�0���� ��'Š����R�@%��%bc#/1�9����5�&~grW�,O�G­�I���^v���e?3��VΤƓ�E6=<2�%:0�u�fډ�!�#R�F�����*�S���m��s��m��Nv{�I��疬�e���X=Q�K1}��l�'��(��l>j�D�(g����(���g�U!h]ݧmc�FJ�ӿ
MM��D	g�4��Ͻ���N!T
endstream
endobj
32 0 obj
<< /Length 231 /Filter /FlateDecode >>
stream
x�5O9�!�y�>0U�@����6�����N��!���x�##�f��Zd f�SLſ�����"��a��p֬�n���v��X�6��Y^��L�Wg.�ci��9�n�]��u��SXG0��t�Ô sT��Ɏ2��8�'�����,v9~�6�!��*z�6���y�rA�]��E��% 	�Qb��_�vt�(sB�A.!��*��P����RQp�>�謟�_\-
endstream
endobj
33 0 obj
<< /Length 249 /Filter /FlateDecode >>
stream
x�=P;�D!�9�/�$�#pF�-f�߮�)PL~�3$��G1���%������B�n��� �CR �z�t�6�:�3?a7c��E1��t�=&9��
�se�VH'��"��3�)�*{�x,��6['�=� �RR�ɥ���?mʔ
:f�,��dM8˻IR��2��v"}�<ȣ:�dMά#���Oۙ�p�_�dN��t����΃9���6M�����i*/R�Z�~u����g�d����Z"
endstream
endobj
34 0 obj
<< /Length 395 /Filter /FlateDecode >>
stream
x�=RKn�@��\����yRUݼ�okCR�*��1�0}ʐ��K]q�ɷ^�[<�|.[Z�y����%>�ܗ�!�]t.�8G�2�*D�ͪѡ�B���N��}9��/��װ
��=2A�$�)B�nQ�Aa���P�Y��Q���2jo��c�	�BmH��@ D�T���g$��gb`�Ѳ�TD�{�ǈ�Ψ��D�>OM�(�L-V�nS_����|t*�4���U��X�y�9�H���l!�:n���3�2�`K9`���G��Yu����t���pL��~��O�t�Z�u�r�@�MA��F���2>��)z�,���F3�a�����r�4�k"�X"��bD��ls=��L��9���l�֡�33*!�ں�j�@v���p��?3�m
endstream
endobj
35 0 obj
<< /Length 74 /Filter /FlateDecode >>
stream
x��0�P0P040S047R076R015QH1�	���\0�0��,,�`Ad3�l#SS�������fp� Q�
endstream
endobj
36 0 obj
<< /Length 136 /Filter /FlateDecode >>
stream
x�M�A1�y��@ @x�VU��_K�v�ɀlQ�%�x�����E6g�_R)b!�Op�0S�)w�c��q�j,�hx^K�M�-w-����o���G�m�
E�-B�l��2�|�Gu�i����l��� �l4I
endstream
endobj
37 0 obj
<< /Length 249 /Filter /FlateDecode >>
stream
x�MQI�0���@!^���C�C�����9	�����X1�,=��!s7�~�ٻYz������"SQ�R�.bB]�ϡ�=�kY���9,��s���3�c}I2���!NuZ�¸kb��Z�<��n�Ffe&�
�dB��� ��,�662Y��
�
Z`שQ��+��	t�VĪ����v7C-��}��hV�`��K�Xx_�>���v�Bz�M;"�
�2;-+�{��n��?�R��������\�
endstream
endobj
38 0 obj
<< /Length 94 /Filter /FlateDecode >>
stream
x�E��� �TA	

�O&�����2|`���yF�&^XJc�P�@��r-��p'��T���wi�IU)ܤy�g&��y�c��c�#<
endstream
endobj
39 0 obj
<< /Length 341 /Filter /FlateDecode >>
stream
x�ERKnD1ۿSp�Hᗐ󴪺��[�L���	`lx�S�dʰ�%#$הO}"C���4r$"��I	v���kK��쑨�����F��Z��ѥ͢Q���9�����{���z\H���!��P�,e�r
%A[�w����+�a�k.��e2����\�}�b�.���� ������6)h U��I£�znv�l�U�� 30r��%[��� �}]�E���+@QY@���v��1�Hp���p<řpK8�@���z�%��/W����	u�d/����B�w� ^dí������<��gErF�ԋ8:!�Z�9��ҠZ�\7��m#��W���/\��K��
endstream
endobj
40 0 obj
<< /Length 164 /Filter /FlateDecode >>
stream
x�E��q1C�%0�
����������AzBbO°\WqatÏ�-3
G���2c��X '����Ѥ�v�����b���\/:"̒�@#|:�Ǔ��3�t^�!��**�na.��@�R�ԏ�Qꚡ�*+kj�W�]J�>.�2NݽZὕ�=��?v:�
endstream
endobj
41 0 obj
<< /Length 54 /Filter /FlateDecode >>
stream
x�363T0P0�T026Q064b�C.������@�r���s`�r�2�� 2
endstream
endobj
42 0 obj
<< /Length 72 /Filter /FlateDecode >>
stream
x�32�P0P�4�&
�f
)�\@����B.H�����%���g�� m� D���D����J %��
endstream
endobj
43 0 obj
<< /Length 47 /Filter /FlateDecode >>
stream
x�32�P0P�4�&
�f
)�\�V.L,�іp
"��� �g
'
endstream
endobj
44 0 obj
<< /Length 258 /Filter /FlateDecode >>

exec
/bin/zsh -lc "rg -n \"33\\.6%|94\\.9%|2\\.03, -1\\.63, and -0\\.58|1\\.2--6\\.5 kpc|0\\.66 dex|0\\.430|0\\.607|0\\.509|0\\.367|0\\.520|0\\.136 to 0\\.418|0\\.005-0\\.729|0\\.003-0\\.520|96\\.6% target coverage\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot | sed -n '1,240p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 286ms:
 transition from disk-dominated to bulge-dominated systems \citep{schawinski2010,bluck2014,belfiore2016}. Single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, an ambiguity that requires spatially resolved integral-field spectroscopy to resolve \citep{penny2018,cheung2016}. The robustness interval in Table~\ref{tab:robust} is a 95\% confidence interval on the median offset.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/briefs/cycle_08_gemini_deep_research_prompt.md:250:Tracer census & tracer prevalence in 60k sample (0.136 to 0.418) & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/briefs/cycle_08_gemini_deep_research_prompt.md:271:We isolate the BPT-defined AGN/composite duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the BPT-defined AGN/composite fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The BPT-defined AGN/composite fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. See the next subsection for the related radio-jet baseline that uses the same projected-density proxy. The follow-up ingredients are X-ray cavity or cooling-luminosity measurements, radio jet powers \citep[e.g.,][]{hardcastle2020}, halo-selected parent catalogues, and nondetection modelling. Those observables are missing here; this entry remains an optical baseline only, and future follow-up requires those real observables before any physical inference.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/briefs/cycle_08_gemini_deep_research_prompt.md:293:We define the environment-stratified optical denominator that future radio and X-ray work could test. This subsection reuses the same projected-neighbor ranking described in the relative neighbor-count baseline above and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has a BPT-defined AGN/composite fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The follow-up ingredients are radio jet morphology and age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/briefs/cycle_08_gemini_deep_research_prompt.md:304:In this optical-emission-line denominator, the 11.0--12.5 dex peak is consistent with a selection-function effect: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is concentrated in that mass bin. It must not be interpreted as a universal physical threshold. We identify the mass bin where a future gas-inclusive study should look for a selection-sensitive change in incidence. The note measures the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the BPT-defined AGN/composite incidence peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The follow-up ingredients are gas fractions, baryon deficits, halo masses, central velocity dispersion proxies \citep{piotrowska2022}, stellar-feedback observables, and high-redshift extensions. The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

codex
I found one class of statement that is less well anchored than the headline counts: the manuscript’s “marginal distribution checks” and the rough fiber-scale physical conversion are not sitting in the core analysis summary the way the pair counts are. I’m narrowing that down so I can separate true issues from merely derived-but-still-defensible prose.
exec
/bin/zsh -lc "rg -n \"33\\.6%|94\\.9%|2\\.03|1\\.63|0\\.58|1\\.2--6\\.5 kpc|0\\.02<z<0\\.12\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z | sed -n '1,200p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "rg -n \"marginal distribution checks|percentage points|fiber subtends|3-arcsec fiber\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z | sed -n '1,200p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_HANDOFF.md:84:- Cached-vs-public marginal differences did not exceed 5 percentage points in redshift, stellar mass, or sSFR, but the cache remains capped and non-random.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py:213:The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps {pct(selection['ssfr_low_bin_reference']['sn_ge_3_retention_vs_parent'], 1)}\% of the $-12<\log {{\rm sSFR}}<-11$ parent bin but {pct(selection['ssfr_star_forming_bin_reference']['sn_ge_3_retention_vs_parent'], 1)}\% of the $-10<\log {{\rm sSFR}}<-9.5$ bin. Cached-versus-public marginal checks show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are {fmt(red['max_abs_fraction_difference_pp'],2)}, {fmt(mass['max_abs_fraction_difference_pp'],2)}, and {fmt(ssfr['max_abs_fraction_difference_pp'],2)} percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.tex:42:The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Cached-versus-public marginal checks show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.

 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex:32:SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex:45:Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:19:300651860866394112,817416838731294720,0.06630035,0.06603366,10.5895,10.59393,-12.4401,-9.749212,-2.6908879999999993,0.012946986695848872
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:31:300772257389635584,537155719502260224,0.09433588,0.09423524,10.58039,10.57784,-11.85066,-10.01092,-1.839739999999999,0.00599207590147562
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:41:301770889244993536,304120550224062464,0.0910074,0.09017465,11.21189,11.1938,-11.34586,-10.58408,-0.7617799999999999,0.04555730094247591
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:53:301803874593826816,431242509688006656,0.08343904,0.08314648,10.57659,10.58064,-11.44055,-9.758401,-1.6821490000000008,0.013353148400878222
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:69:301895958692653056,498866598887581696,0.07830796,0.07817154,10.58655,10.58526,-12.00934,-10.47476,-1.53458,0.005709238780625923
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:72:302867931618895872,877210207141259264,0.04389971,0.04376845,10.58005,10.57589,-11.81593,-10.06208,-1.75385,0.009019099207355958
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:82:303012242520041472,418863938860509184,0.06219585,0.06379889,11.15574,11.13997,-12.03271,-10.2765,-1.7562099999999994,0.06754389868463058
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:108:305225558973769728,652021154734696448,0.09780669,0.0978003,10.72617,10.72036,-10.58541,-10.34131,-0.24409999999999954,0.010469986552027312
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:123:306261299900213248,836576379205085184,0.1118258,0.1126462,11.14847,11.13731,-12.0375,-10.27778,-1.7597199999999997,0.03725225117489175
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:124:306275593551374336,690203345394100224,0.1101132,0.1103974,10.58889,10.58749,-10.57275,-10.09302,-0.47973,0.011152819736263295
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:145:307443275168507904,533739811316459520,0.08830596,0.08781177,11.14035,11.14568,-12.24111,-10.20589,-2.0352200000000007,0.021191400062089964
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:147:307464715645249536,727487512800421888,0.09687928,0.09689704,10.7074,10.70233,-11.63718,-9.883742,-1.753438000000001,0.009159168372236712
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:149:307468838813853696,816287091070625792,0.09786262,0.09840455,10.93343,10.93041,-12.36126,-10.72271,-1.6385500000000004,0.021418468658687035
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:154:307490004412688384,422334821637842944,0.09692178,0.09695334,10.58793,10.58997,-10.64634,-9.992068,-0.6542720000000006,0.0038681519434767427
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:157:307499350261524480,695944715270383616,0.06544796,0.06525312,10.57971,10.58382,-11.4596,-10.03035,-1.4292499999999997,0.010502314621170888
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:187:308615903581333504,397466610064975872,0.09523287,0.09627782,11.19568,11.16186,-12.03989,-10.33877,-1.7011199999999995,0.07285550305716164
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:253:310886395025582080,661045116307269632,0.06570604,0.0658004,10.73212,10.73333,-12.03554,-10.65189,-1.3836499999999994,0.004214568254573669
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:308:314169812882319360,391985818941548544,0.07286128,0.07265304,10.79368,10.78618,-10.51519,-9.929798,-0.5853920000000006,0.015682272906599737
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:317:314224238707894272,519151489529178112,0.03726012,0.03747749,10.06055,10.05741,-11.73125,-10.09289,-1.6383599999999987,0.01005207229822852
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:332:314295706963699712,660912625156122624,0.06956788,0.06763776,11.49433,11.39312,-11.76818,-11.18301,-0.5851699999999997,0.1966989917861539
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:349:315356454565472256,774731597931898880,0.1034376,0.1035869,10.81376,10.81133,-11.63957,-9.881322,-1.758248,0.00719285006317615
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:358:315380918699190272,731945751197804544,0.1016575,0.1016924,11.11267,11.12107,-12.32185,-10.28574,-2.036109999999999,0.01519190066388903
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:365:315408406489884672,751064609472931840,0.07645808,0.07647738,10.98871,10.98639,-10.58155,-9.642256,-0.9392940000000003,0.004244261839738755
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:406:317678074139273216,497727779870107648,0.1181091,0.1180694,10.79774,10.79081,-12.197,-10.16495,-2.03205,0.012576793225731948
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:505:324360361794889728,809660608445179904,0.1045799,0.1045382,10.73476,10.74293,-10.8904,-11.47455,0.5841500000000011,0.014804912273251486
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:545:327690781307463680,377249619869984768,0.04841816,0.04849259,10.55864,10.5589,-12.20054,-10.16206,-2.03848,0.0028834743980331026
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:586:328859831693764608,550659369948178432,0.08458514,0.08507065,11.11697,11.13532,-11.20032,-10.6185,-0.5818200000000004,0.037912156941622685
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:638:332251831373686784,318640976497240064,0.0791698,0.07895771,10.69178,10.69411,-11.84748,-9.812727,-2.0347529999999985,0.009129630885568882
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:640:332278219652753408,521382123710474240,0.1112847,0.111239,10.58114,10.57875,-11.09388,-11.58069,0.4868100000000002,0.004646648577871087
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:687:334518749036046336,346881377918019584,0.1023198,0.1022637,10.58944,10.59297,-11.25897,-10.03189,-1.227079999999999,0.006711387624774918
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:699:335603142311831552,618171858650425344,0.04837273,0.04807405,10.58116,10.57895,-11.60196,-10.3806,-1.2213600000000007,0.01209169363626816
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:711:336659218465581056,711584993666689024,0.08903117,0.08885861,10.58626,10.58783,-12.17476,-10.29722,-1.8775399999999998,0.007177153608211657
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:716:336684232355112960,460584627631843328,0.08689459,0.08660433,11.06221,11.07384,-12.44941,-10.41089,-2.03852,0.02370884279792425
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:723:336753226709755904,506767964909889536,0.1009769,0.1013303,10.8483,10.84792,-10.47161,-10.58639,0.11477999999999966,0.013526466907264471
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:732:336794733273704448,733077148629231616,0.09133449,0.08919995,11.34324,11.36209,-11.63293,-11.49764,-0.13528999999999947,0.08838015337663567
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:764:338944832808445952,319872704129820672,0.07898407,0.07898251,10.4785,10.47925,-10.77985,-10.58824,-0.19160999999999895,0.0013524947248701852
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:776:340058908703877120,748762781964068864,0.05477432,0.05452603,10.42628,10.42353,-11.24818,-10.66127,-0.5869099999999996,0.01070643683798067
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:803:341309876833642496,675605129042356224,0.05027221,0.05040107,10.5624,10.56103,-12.03678,-12.26,0.22321999999999953,0.005509586364103515
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:842:344644146213971968,476408798139934720,0.05449581,0.05411638,10.89544,10.88005,-12.2,-10.56505,-1.63495,0.03129078010838514
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:844:344671634004666368,478536079553619968,0.1194745,0.119381,10.842,10.84764,-11.78681,-10.15463,-1.63218,0.010771155922824138
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:845:344676032051177472,660982169266579456,0.1193331,0.1188173,11.18115,11.19167,-11.46608,-12.04688,0.5808,0.027348884478331625
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:848:344688676434896896,841100869083621376,0.05632764,0.05667125,10.58705,10.58959,-11.9755,-10.2824,-1.6930999999999994,0.013909178582474464
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:882:347955056592578560,854696605574522880,0.06866409,0.06832001,10.72485,10.72934,-11.65367,-10.02331,-1.6303599999999996,0.015441202199763126
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:918:349180462234626048,310874025519769600,0.03507327,0.03902899,11.2698,11.31267,-11.34968,-10.76822,-0.5814599999999999,0.16979425035601803
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:935:350316802049337344,806154540742109184,0.09974685,0.0997948,10.8683,10.86958,-12.58989,-10.55208,-2.0378100000000003,0.002945739964762473
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:945:351327803393730560,500027958212192256,0.1188628,0.1191019,10.86444,10.87307,-11.6319,-9.83318,-1.7987199999999994,0.01803508729550519
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:987:367057978005678080,421125078114134016,0.06133258,0.06145959,10.79049,10.78158,-11.67451,-9.642901,-2.0316089999999996,0.016770186287740452
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1049:369393064264886272,621539662950852608,0.04136416,0.0409258,10.59105,10.58656,-12.08026,-10.44257,-1.637690000000001,0.018607100216740707
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1063:370425227013810176,601344932967376896,0.07701115,0.07718708,10.73626,10.73685,-11.63496,-10.75245,-0.8825099999999999,0.0068086129520672865
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1089:371576420956137472,728460855972227072,0.08830133,0.08821988,10.10559,10.10088,-11.51158,-9.872133,-1.6394470000000005,0.0090385923532786
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1093:371616278252644352,739837771354499072,0.07730743,0.07757486,11.1113,11.1228,-12.09709,-10.0571,-2.0399899999999995,0.023102926909070867
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1104:372791381271275520,408822096077023232,0.08737984,0.08729729,10.61161,10.61026,-12.03,-10.48016,-1.5498399999999997,0.003984074657600769
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1137:374974460685477888,872709905260242944,0.1103629,0.1099052,10.90645,10.9008,-12.39175,-10.75696,-1.6347900000000006,0.020241639873190612
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1158:376134440084072448,821972944065423360,0.09385329,0.09340917,10.95429,10.96456,-12.28929,-10.58646,-1.7028299999999987,0.02511072397046939
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1171:377218283788593152,332141605333002240,0.04793756,0.04783935,10.92282,10.94308,-12.15303,-10.12229,-2.0307399999999998,0.03669242167577336
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1219:379429676499625984,389723849014405120,0.04697433,0.04720536,10.59026,10.58476,-12.04445,-9.656276,-2.3881739999999994,0.013273087474934423
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1290:381841999893915648,836653894774843392,0.1135119,0.1128905,11.06824,11.08957,-12.39461,-10.3581,-2.03651,0.04517650511335387
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1294:382832939748059136,661020652173551616,0.02691544,0.02723799,10.75211,10.72154,-11.6384,-10.74431,-0.8940900000000003,0.05643738977138704
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1300:382917602143397888,479669126017607680,0.08225531,0.08227051,10.55604,10.55359,-11.97158,-9.941514,-2.0300659999999997,0.004451932412607758
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1336:385101776975587328,862441565363136512,0.1135538,0.1129852,11.14718,11.14269,-11.17756,-10.5854,-0.5921599999999998,0.023191824882753856
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1353:386232624701532160,868175795443492864,0.1064801,0.1066715,10.71437,10.71734,-10.44167,-10.58879,0.14711999999999925,0.009064254531073259
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1382:387478096514672640,452618939457890304,0.1174917,0.1173136,10.62354,10.62615,-11.6375,-9.990217,-1.6472829999999998,0.008274042081312199
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1423:389641385642321920,826519145708283904,0.0307668,0.03032968,10.64989,10.68131,-12.19899,-10.56063,-1.6383600000000005,0.059020145025078644
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1427:389681517816735744,695944715270383616,0.06509413,0.06525312,10.58771,10.58382,-12.05915,-10.03035,-2.0288000000000004,0.00927635109987546
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1437:389727422427195392,507814150223718400,0.04767711,0.04901946,10.90574,10.90475,-12.21905,-10.58611,-1.6329399999999996,0.0513438981463192
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1452:392947067451893760,664319737332787200,0.07761791,0.08051206,11.49666,11.51236,-12.87737,-11.24156,-1.635810000000001,0.11419075377684279
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1455:392956963056543744,683465813402871808,0.1048808,0.1048499,10.37592,10.37783,-10.6795,-10.09034,-0.5891600000000015,0.003638092010549057
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1464:392986374992586752,376090184741054464,0.09974442,0.09951239,10.791,10.79017,-11.46028,-9.825039,-1.6352409999999988,0.008994781828776692
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1509:395245321564743680,814135895614580736,0.06690627,0.0641873,11.15,11.16055,-12.59065,-12.004,-0.5866500000000006,0.1056593950977897
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1510:395247245710092288,335644648875780096,0.0832296,0.0853492,11.21936,11.21702,-12.54438,-11.63843,-0.9059500000000007,0.081133804429776
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1522:395356097361242112,809642466503321600,0.0702078,0.07011583,10.63389,10.63267,-11.64742,-10.58783,-1.05959,0.004146169650781211
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1545:398618899744057344,308543335813900288,0.1118252,0.1117112,10.71644,10.71672,-11.12093,-10.53525,-0.58568,0.004386883227283813
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1642:408729737100290048,443692831198963712,0.06786909,0.06657331,10.99078,11.01062,-12.085,-10.05115,-2.033850000000001,0.06108245640311426
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1658:408853707036321792,557483489839048704,0.1029307,0.1029437,10.58076,10.57282,-11.91854,-10.1211,-1.79744,0.014313115734451426
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1668:409900167412606976,648602497987930112,0.0568578,0.05695676,10.58138,10.58726,-12.455,-9.868137,-2.5868629999999992,0.011248418964478705
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1698:412249824046376960,662162770195671040,0.02800389,0.02805412,10.42931,10.42384,-11.66322,-10.58374,-1.0794800000000002,0.010039918853380523
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1727:417819126342379520,829941105704331264,0.1197745,0.1197753,10.8513,10.84407,-12.03172,-10.48274,-1.5489800000000002,0.013025405794331124
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1801:423428835757811712,681243700151478272,0.08539932,0.08554,10.59095,10.58908,-11.96373,-9.902144,-2.061586,0.006345784103546636
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1806:423498654746175488,737614008835663872,0.05553861,0.05575849,10.89882,10.86938,-12.03396,-11.41107,-0.6228899999999999,0.053700166689258144
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1807:424474196471474176,621512724915972096,0.09128816,0.0913012,11.01351,11.00965,-10.68025,-10.58763,-0.09261999999999837,0.00697191254522717
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1813:424499760116819968,574319218477000704,0.08167449,0.08141486,10.52453,10.52228,-11.63333,-10.37852,-1.2548100000000009,0.01072054584397569
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1825:425674313429968896,335644648875780096,0.08533692,0.0853492,11.22567,11.21702,-11.76991,-11.63843,-0.13147999999999982,0.015590671403662652
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1860:428999780727810048,481961058022483968,0.06049024,0.06058823,10.57867,10.58185,-10.30507,-10.89368,0.5886099999999992,0.006844877130227852
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1882:431252130414749696,871589227882637312,0.06591836,0.06567503,10.31028,10.30999,-10.58768,-10.1812,-0.4064800000000002,0.009316237253156294
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1914:432514919569582080,470740265875826688,0.080727,0.08078738,10.58255,10.58557,-11.13801,-10.51691,-0.6211000000000002,0.005910081436480252
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1946:435764525682157568,711584993666689024,0.08873614,0.08885861,10.5895,10.58783,-10.37796,-10.29722,-0.08074000000000048,0.005564965105045225
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1961:435873927089121280,380556121078786048,0.08778825,0.08665504,11.19137,11.19045,-11.91698,-10.28146,-1.6355200000000014,0.04334998477222717
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1970:436876406849300480,728629081251276800,0.07284614,0.07296586,11.05472,11.04106,-12.04826,-10.4118,-1.6364600000000014,0.02503138780918345
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1971:436884928064415744,727345400922531840,0.07187823,0.07196379,10.67374,10.67639,-12.0335,-9.893,-2.1404999999999994,0.005787029188370765
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:1982:436970140215568384,304120550224062464,0.0906756,0.09017465,11.18628,11.1938,-11.98611,-10.58408,-1.4020299999999999,0.023457264665072548
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2048:440335745123641344,442610085127022592,0.108567,0.1087367,10.95671,10.9618,-11.63064,-12.05124,0.4206000000000003,0.011232538666976112
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2080:442552360766564352,669986069936105472,0.08089914,0.08105174,10.65154,10.65294,-12.03,-12.01154,-0.018459999999999255,0.006355239025719304
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2131:444741488232916992,507814150223718400,0.04990106,0.04901946,10.91443,10.90475,-12.3315,-10.58611,-1.7453900000000004,0.03794509058283827
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2138:444787942599190528,626138920073062400,0.04304825,0.04291684,10.58027,10.57995,-11.73673,-10.00108,-1.7356499999999997,0.0050562753184555595
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2141:444808833320118272,536012232241211392,0.04762413,0.04833313,11.02549,11.04772,-12.03916,-11.15102,-0.8881399999999999,0.04835759562750618
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2167:446000429600368640,507814150223718400,0.04801672,0.04901946,10.91011,10.90475,-11.6492,-10.58611,-1.0630900000000008,0.03952854555659506
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2176:447035894306727936,506747898822682624,0.04543603,0.04522578,10.39538,10.39777,-12.03521,-10.48295,-1.5522599999999986,0.009117773508754012
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2187:447109561585788928,512303456216705024,0.04449842,0.04422837,10.58632,10.58859,-12.27083,-10.1306,-2.1402300000000007,0.011103534880654086
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2194:447154916440434688,449309134983030784,0.0770366,0.07695176,10.7692,10.76961,-11.63466,-10.13885,-1.4958100000000005,0.0033261617454503007
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2205:448196153868052480,593367981896001536,0.07694832,0.07797395,11.1543,11.14703,-10.55412,-9.969646,-0.5844740000000002,0.04133577809129463
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2209:448217319466887168,611405739574978560,0.04515335,0.04593188,10.57324,10.58265,-10.38614,-10.74238,0.35624000000000144,0.034250087012365475
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2237:449408365907437568,395245871320557568,0.1049872,0.1049317,10.81425,10.80805,-12.03333,-12.00937,-0.02395999999999887,0.011369446091339039
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2254:451532621885761536,715056427994998784,0.1005143,0.1006477,10.36794,10.3739,-10.58441,-9.892201,-0.6922090000000001,0.011886747632804447
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2264:451636525734586368,335644648875780096,0.0844375,0.0853492,11.19451,11.21702,-12.29943,-11.63843,-0.6609999999999996,0.05347108499620811
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2273:452656597731141632,336677910163253248,0.08734393,0.08753174,10.58039,10.58152,-11.83381,-10.1102,-1.723609999999999,0.00746231478100135
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2285:452736037446248448,441444602784802816,0.05894068,0.0589913,10.89382,10.88848,-12.16888,-10.13309,-2.0357900000000004,0.009813068428840265
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2286:452752255242758144,871451239173351424,0.08063623,0.08127526,10.81358,10.81022,-12.24022,-10.20333,-2.0368900000000014,0.0251665163256936
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2325:456031549058476032,322178930708604928,0.1001817,0.1003528,10.97305,10.97562,-12.03378,-10.33102,-1.7027599999999996,0.008013452065110374
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2354:458303689904384000,746578326851708928,0.04133281,0.04129125,10.54099,10.54455,-11.07574,-11.66182,0.5860800000000008,0.00660743136240942
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2358:458349319636936704,843360640222390272,0.04669286,0.04640814,10.58219,10.59071,-10.81117,-10.67106,-0.14010999999999996,0.01881648782029786
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2367:458413915945068544,648639056749553664,0.06255095,0.06266215,10.42696,10.42044,-11.63202,-10.24459,-1.3874300000000002,0.01249173135364622
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2396:460600570550446080,666696056301447168,0.0424447,0.04223987,10.28051,10.28635,-11.84835,-10.21259,-1.6357599999999994,0.013114958917895301
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2427:462855393115138048,310853409676748800,0.04004455,0.04037981,10.70646,10.70468,-10.78032,-10.1927,-0.5876199999999994,0.013210826926111476
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2463:464016484792821760,304120550224062464,0.08983727,0.09017465,11.20081,11.1938,-12.26092,-10.58408,-1.6768400000000003,0.018050439236744865
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2483:465168215891273728,600265487376476160,0.05230851,0.05216701,11.0671,11.04865,-12.13925,-12.03981,-0.0994400000000013,0.033676243993662765
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2496:466200932992968704,828707173797226496,0.06810625,0.06793619,10.87527,10.87971,-12.27113,-10.2313,-2.0398300000000003,0.010307443422692655
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2508:467302367776237568,335644648875780096,0.08497741,0.0853492,11.20368,11.21702,-11.76504,-11.63843,-0.12661000000000122,0.027920747673733367
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2518:467373561154136064,864839051037927424,0.04774244,0.04685219,10.81216,10.81063,-11.63198,-10.2076,-1.424380000000001,0.03414230356507058
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2530:468526948868450304,752248783479269376,0.03997033,0.039802,10.71402,10.72022,-12.03895,-10.51916,-1.5197900000000004,0.012890599570757978
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2600:474155074180900864,720593294597318656,0.08897402,0.0888733,10.84432,10.84862,-10.17781,-12.21333,2.03552,0.008650774972637587
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2601:474160571739039744,349108719100913664,0.08823182,0.08841213,10.58733,10.58498,-12.66842,-9.834327,-2.8340929999999993,0.008088979710037912
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2617:475188889821145088,452647251882305536,0.05832079,0.05867875,10.40309,10.39898,-11.63258,-10.23996,-1.3926200000000009,0.015558363864386604
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2661:476378286692263936,631759628614526976,0.04394583,0.04405877,10.54282,10.55096,-12.03564,-10.29046,-1.7451800000000013,0.01528709131349572
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2677:477556964365199360,611405739574978560,0.04576771,0.04593188,10.58654,10.58265,-11.89107,-10.74238,-1.1486899999999984,0.009407271714147594
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2696:479672699430397952,807303809717004288,0.04469848,0.0445213,10.86751,10.87054,-12.03812,-10.22944,-1.808679999999999,0.008698878273266606
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2733:481989370446899200,830951831818496000,0.08703817,0.08698086,10.5835,10.58191,-11.55517,-10.78356,-0.7716100000000008,0.003606205000663702
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2748:483023460075857920,435824174187964416,0.07282138,0.07300083,10.51921,10.52446,-10.58576,-9.598103,-0.9876570000000005,0.011683917368550007
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2771:483162273418864640,431351636217063424,0.06786653,0.06806018,10.60568,10.60564,-11.63346,-10.40486,-1.2286000000000001,0.00740285021705766
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2786:484239246014572544,335644648875780096,0.08469012,0.0853492,11.20312,11.21702,-11.92327,-11.63843,-0.28484000000000087,0.03552235736706737
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2827:486497917893371904,631692283527325696,0.07197358,0.07199785,10.58595,10.58656,-12.0125,-10.70973,-1.3027699999999989,0.0014382038697925593
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2830:486520183003834368,448251954083162112,0.08597001,0.08560841,10.62456,10.62887,-12.03182,-10.04143,-1.9903899999999997,0.015854200181240282
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2839:487516615231956992,335644648875780096,0.08386636,0.0853492,11.2374,11.21702,-12.416,-11.63843,-0.7775700000000008,0.06753566118044847
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2856:487675219784263680,319818553182152704,0.11964,0.118277,11.16547,11.16968,-10.97358,-10.3912,-0.5823800000000006,0.05265144046139735
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2914:491019384567916544,646432062538016768,0.06292854,0.06268489,10.58313,10.58628,-12.10464,-10.14787,-1.9567700000000006,0.010906517592787221
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2967:495459487432337408,563092923386718208,0.09248472,0.09269308,10.86967,10.86978,-11.6375,-10.10618,-1.5313199999999991,0.007967271544083564
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:2998:497686548184066048,623750231212713984,0.09635983,0.09631256,10.72656,10.72623,-10.79332,-10.20663,-0.586689999999999,0.001902242454869475
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3054:500065341607536640,504489776682919936,0.03206512,0.0310755,10.89995,10.88288,-10.80447,-12.43798,1.6335099999999994,0.04875243824510697
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3090:502283056829196288,871536451324504064,0.1191078,0.1192213,10.80805,10.80331,-11.99828,-9.96732,-2.0309599999999985,0.009578431237975898
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3109:503289384477419520,841100869083621376,0.05656838,0.05667125,10.59144,10.58959,-12.03301,-10.2824,-1.75061,0.005154753140359007
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3111:503308351052998656,578869815733676032,0.08668981,0.08682404,10.66896,10.67323,-10.75909,-10.17287,-0.5862200000000009,0.009246948179595668
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3117:503345184692529152,828835266901862400,0.1183299,0.1180841,11.06778,11.06403,-11.7787,-10.14718,-1.63152,0.011572677453702995
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3131:503389165157640192,862441565363136512,0.1129858,0.1129852,11.14245,11.14269,-12.3,-10.5854,-1.7146000000000008,0.0004329853154214481
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3136:503414728802985984,433607283734243328,0.09427845,0.09395572,11.00813,11.01103,-12.16667,-10.1303,-2.03637,0.013397427099513533
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3168:505558501985118208,566399704691140608,0.07160375,0.07137419,10.45325,10.45297,-10.58571,-9.921229,-0.6644810000000003,0.008789688386996602
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3176:505595335624648704,622663913707694080,0.05706123,0.05732391,10.35734,10.35569,-12.032,-10.04376,-1.9882399999999993,0.010472013788227954
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3230:507785837799303168,341289260990621696,0.051484,0.0514957,10.72712,10.72962,-12.31535,-10.28357,-2.0317800000000013,0.004526083095898176
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3243:507886992869058560,641768482475632640,0.0695712,0.06971401,10.60432,10.61211,-12.05714,-10.58482,-1.4723199999999999,0.015058610459178506
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3249:507933996991145984,731926509744318464,0.111236,0.1112617,10.5893,10.59324,-11.13654,-10.21749,-0.9190500000000004,0.007165858074424662
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3280:511237754554705920,833337492844341248,0.08860658,0.08860146,10.55575,10.55646,-11.6352,-11.2345,-0.4006999999999987,0.001294003356391601
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3288:511260019665168384,752169893519976448,0.0546794,0.05450666,10.58523,10.58573,-12.37011,-10.04288,-2.32723,0.0066643480589305875
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3309:512337266199259136,489815694196631552,0.09649888,0.09656971,11.00707,10.99572,-12.03093,-10.59061,-1.4403199999999998,0.02062632811051877
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3387:518053077647910912,846723496955373568,0.03397788,0.03416925,10.27913,10.27383,-12.03187,-10.87714,-1.154729999999999,0.012028505791326518
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3391:519045111779190784,322111860499310592,0.07798377,0.07815591,10.58963,10.5942,-11.09248,-9.952649,-1.139831000000001,0.010539692217205653
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3447:522491805820807168,388463258882828288,0.05897574,0.0593444,11.10943,11.09359,-12.03375,-10.81322,-1.2205300000000001,0.03182691853250709
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3466:523597364796090368,505556028083955712,0.08468409,0.08501991,10.58899,10.58811,-11.96316,-10.01354,-1.9496199999999995,0.012934642249986094
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3487:525950319528536064,455021647561254912,0.06161162,0.06178009,10.58871,10.59487,-11.96204,-10.06725,-1.8947900000000004,0.012830892467698335
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3497:526973690160637952,572000623080269824,0.04094305,0.04051564,10.81833,10.81053,-10.58806,-10.74063,0.15256999999999898,0.02155004945098688
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3500:527016845992028160,508960391146006528,0.02875791,0.02937611,10.91494,10.91197,-12.17667,-10.14563,-2.031039999999999,0.024229606976560104
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3509:528052585962170368,658677318033631232,0.05652208,0.05660537,10.56206,10.56371,-11.63441,-9.791232,-1.843178,0.004355832196626144
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3518:528131201043556352,497790726910797824,0.109277,0.109311,10.93004,10.92968,-10.58266,-11.51649,0.9338299999999986,0.001452526180714152
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3523:528186176624945152,336717767459760128,0.07103709,0.07067633,10.58851,10.58709,-12.33103,-10.34208,-1.9889500000000009,0.014025754485234816
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3589:534872857461680128,821972944065423360,0.09333181,0.09340917,10.9659,10.96456,-10.70269,-10.58646,-0.11622999999999983,0.003817435103753724
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3592:534881928432609280,726255229774882816,0.07016639,0.07046705,10.59488,10.58648,-10.41642,-10.18116,-0.23526000000000025,0.01900276276415035
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3623:540525996898543616,308566700435990528,0.0949465,0.09521819,11.23964,11.23815,-12.03302,-11.97689,-0.056130000000001345,0.010726968282732473
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3638:541632379115038720,506767964909889536,0.1009131,0.1013303,10.85405,10.84792,-12.56141,-10.58639,-1.9750200000000007,0.01939843979070943
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3653:543950699650639872,541589498161555456,0.09841932,0.09841134,10.58451,10.5834,-12.10467,-10.47306,-1.6316100000000002,0.0020228778511671513
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3677:547214874560718848,299552899363530752,0.09132698,0.09113582,10.58013,10.57846,-11.64779,-10.26259,-1.385200000000001,0.00790244917925433
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3740:551805061047543808,621539662950852608,0.04127379,0.0409258,10.58219,10.58656,-12.2807,-10.44257,-1.8381299999999996,0.015457491509692556
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3782:554003260105582592,314272892097423360,0.1141575,0.1143529,10.97482,10.96457,-11.63454,-9.434346,-2.2001939999999998,0.01991957384285381
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3799:554081050553247744,862441565363136512,0.1134261,0.1129852,11.15109,11.14269,-11.13899,-10.5854,-0.5535899999999998,0.02265102050112919
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3830:556238291695855616,690203345394100224,0.1105313,0.1103974,10.58263,10.58749,-12.15549,-10.09302,-2.062470000000001,0.010142000452687323
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3851:556329276283054080,727396253335316480,0.09892336,0.09894381,10.58267,10.58772,-12.02828,-9.983129,-2.0451510000000006,0.009131464088126259
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3875:557399652077430784,815250526416431104,0.08185336,0.08245505,11.15354,11.17127,-11.63682,-11.03065,-0.6061700000000005,0.039361123802682224
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3922:560766906370385920,737509280353118208,0.0857488,0.08565351,10.56157,10.5609,-10.58974,-10.47544,-0.11430000000000007,0.003837357587181379
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3934:560823806097123328,513456294175205376,0.03111667,0.03102311,10.58702,10.57701,-12.0955,-10.6912,-1.4042999999999992,0.018384960499916298
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3939:560840298771539968,591098039351928832,0.035471,0.0359304,10.23953,10.2556,-11.635,-10.14295,-1.492049999999999,0.03386101872848495
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:3984:564152856639203328,821983114547980288,0.08551911,0.08620997,11.23945,11.22327,-12.03256,-12.16598,0.1334199999999992,0.03933347318042195
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4004:565286998219188224,646432062538016768,0.06257332,0.06268489,10.58518,10.58628,-10.9519,-10.14787,-0.8040300000000009,0.004702826842799369
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4039:566455779784157184,645209954860427264,0.1038932,0.103879,10.60451,10.60617,-11.63424,-9.913744,-1.7204960000000007,0.003039472953294836
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4086:568733148578342912,307417436645255168,0.04977014,0.05050373,10.89252,10.87995,-12.28846,-10.65638,-1.6320800000000002,0.03604446904774402
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4098:569749092373129216,862441565363136512,0.1121667,0.1129852,11.15874,11.14269,-11.2,-10.5854,-0.6145999999999994,0.04260326294317504
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4101:569751566274291712,395210686948468736,0.1055475,0.1052344,10.58024,10.58011,-10.54286,-9.733591,-0.8092689999999987,0.011970907741707126
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4151:571968187487250432,354711824869910528,0.07411547,0.07432002,10.58946,10.59911,-11.83385,-10.24737,-1.58648,0.01906262490973325
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4156:572002822103525376,310874025519769600,0.03814163,0.03902899,11.27575,11.31267,-12.03945,-10.76822,-1.271230000000001,0.0746639975140324
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4200:574222736331663360,304063925375232000,0.07142476,0.07119782,10.44584,10.44979,-12.22113,-10.19002,-2.03111,0.011220380746326841
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4223:574382715273504768,877088711106390016,0.05073064,0.05089269,10.67691,10.65935,-11.63727,-10.7296,-0.9076699999999995,0.03223638633824145
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4256:576534178124818432,420084115430205440,0.04841463,0.04869162,10.50933,10.50638,-12.03409,-10.13214,-1.9019500000000011,0.011847228942776023
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4289:577713679173183488,509020864285534208,0.04743769,0.04647997,10.88612,10.89077,-12.06092,-10.42141,-1.6395099999999996,0.037556220298081255
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4295:577753536469690368,404223110997370880,0.09917583,0.09887126,11.0945,11.09393,-12.11435,-10.07982,-2.03453,0.011687746615951743
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4297:578720282152298496,324314732062337024,0.02025704,0.02104147,9.492315,9.495244,-11.6376,-9.954148,-1.6834520000000008,0.03044651961384963
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4300:578726879222065152,579895386160785408,0.09395057,0.09431977,10.51057,10.50853,-12.03645,-9.436444,-2.6000060000000005,0.014583788600537514
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4301:578728803367413760,844462076146509824,0.07596976,0.07591069,10.4549,10.452,-12.05789,-10.02567,-2.0322200000000006,0.005691633226268009
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4304:578745845797644288,307505397575477248,0.09770793,0.09776416,10.65001,10.65002,-10.5874,-10.39308,-0.19432000000000116,0.0021495335137890316
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4325:579848382038697984,389723849014405120,0.04738384,0.04720536,10.57668,10.58476,-11.61089,-9.656276,-1.9546139999999994,0.016076246193215155
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4365:582152683079624704,619406884717225984,0.02383637,0.02386499,10.58104,10.59055,-11.60307,-10.39727,-1.2058,0.0171678499008328
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4375:582239819376125952,843339199745648640,0.07813819,0.07834846,10.83343,10.83595,-12.03421,-10.37397,-1.66024,0.009231348254709695
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4380:583238730018482176,676738725513816064,0.07494491,0.07517625,10.88852,10.87357,-12.24906,-10.61588,-1.6331799999999994,0.028348138338716692
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv:4424:585574642572355584,382891488742238208,0.08113416,0.08124943,10.58409,10.58042,-12.15287,-10.56861,-1.5842600000000004,0.007945519472486758

exec
/bin/zsh -lc "rg -n \"0\\.430|0\\.607|0\\.509|0\\.367|0\\.520|0\\.549|0\\.66 dex|0\\.136 to 0\\.418|0\\.005-0\\.729|0\\.003-0\\.520\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z | sed -n '1,200p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/data/source_analysis_results.json:27:    "Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/analysis_results.json:13:    "fraction": 0.6073748902546093,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/analysis_results.json:25:    "The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex:56:\item Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_aas.tex:23:\item The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:7:    0.5202082816761716
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:21:  "peak_agn_fraction": 0.5202082816761716,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json:34:    "The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex:57:\item The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p2_radio_jet_environment/analysis_results.json:27:    "Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_aas.tex:22:\item Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:4:    0.5202082816761716
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/data/source_analysis_results.json:19:    "Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex:57:\item Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json:20:    "Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json:21:    "The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json:13:    "fraction": 0.6073748902546093,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/data/source_analysis_results.json:25:    "The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/data/source_analysis_results.json:11:    "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex:57:\item Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex:58:\item The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json:4:    0.5202082816761716
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json:19:    "Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex:57:\item The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p1_multiphase_census/analysis_results.json:11:    "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_aas.tex:23:\item Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p2_gas_depletion_efficiency/analysis_results.json:20:    "Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p2_gas_depletion_efficiency/analysis_results.json:21:    "The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_aas.tex:22:\item Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_aas.tex:23:\item Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_aas.tex:24:\item The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p3_feedback_transition_mass/analysis_results.json:7:    0.5202082816761716
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p3_feedback_transition_mass/analysis_results.json:21:  "peak_agn_fraction": 0.5202082816761716,
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p3_feedback_transition_mass/analysis_results.json:34:    "The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex:56:\item Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_aas.tex:23:\item The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:71:\item The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:116:\item Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:140:\item The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:162:\item Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:186:\item Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:187:\item The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:210:\item Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.

codex
I’ve narrowed the remaining provenance question to a small set of derived statements, mostly the cached-vs-public diagnostic and the approximate fiber-scale conversion. I’m checking the selection script now, because if that script explicitly encodes the `specObjID` cap and the bin-difference numbers, then those claims are fine; if not, I’ll flag them as provenance gaps rather than data errors.
exec
/bin/zsh -lc "rg -n \"specObjID|33\\.6%|94\\.9%|2\\.03|1\\.63|0\\.58|1\\.2--6\\.5|3-arcsec|cache budget|workflow validation\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_HANDOFF.md /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json | sed -n '1,240p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_HANDOFF.md:83:- Four-line selection is sSFR-dependent: S/N>=3 keeps 33.6% of the `-12 < log sSFR < -11` parent bin and 94.9% of the `-10 < log sSFR < -9.5` parent bin.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py:201:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{{york2000,sdssdr17,brinchmann2004}}. The cached analysis table is capped at {fmt(selection['cached_rows'])} rows and ordered by \texttt{{specObjID}}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains {fmt(selection['strict_sdss_sn_ge_3_total'])} rows, so the cache covers {pct(selection['cached_coverage_of_strict_sdss_sn_ge_3'])}\% of that strict parent.

exec
/bin/zsh -lc "sed -n '1,280p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
#!/usr/bin/env python3
"""Build the local flagship decision package.

Outputs:
- polished RP-1 flagship AASTeX draft/PDF source tree
- combined supplementary denominator/proxy atlas for the other eight active drafts
- package manifest before compile/audit

Safety: local files under the handoff tree only. No public/live/wiki/DB/deploy/git/external submission side effects.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind")
RUN = BASE / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z"
OUT_ID = "RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z"
OUT = RUN / "decision-package" / OUT_ID


def read_json(path: Path) -> Any:
    return json.loads(path.read_text())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def clean_text(x: Any) -> str:
    s = str(x)
    replacements = {
        "—": "--",
        "–": "-",
        "−": "-",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "≈": "about",
        "≥": ">=",
        "≤": "<=",
        "α": "alpha",
        "β": "beta",
        "λ": "lambda",
    }
    for a, b in replacements.items():
        s = s.replace(a, b)
    return s


def tex_escape(x: Any) -> str:
    s = clean_text(x)
    out: list[str] = []
    for ch in s:
        if ch == "\\":
            out.append(r"\textbackslash{}")
        elif ch == "&":
            out.append(r"\&")
        elif ch == "%":
            out.append(r"\%")
        elif ch == "$":
            out.append(r"\$")
        elif ch == "#":
            out.append(r"\#")
        elif ch == "_":
            out.append(r"\_")
        elif ch == "{":
            out.append(r"\{")
        elif ch == "}":
            out.append(r"\}")
        elif ch == "~":
            out.append(r"\textasciitilde{}")
        elif ch == "^":
            out.append(r"\textasciicircum{}")
        else:
            out.append(ch)
    return "".join(out)


def fmt(x: Any, nd: int = 3) -> str:
    if x is None or x == "":
        return "--"
    if isinstance(x, int):
        return f"{x:,}"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return tex_escape(x)


def pct(x: float, nd: int = 1) -> str:
    return f"{100*x:.{nd}f}"


def copy(src: Path, dst: Path) -> dict[str, Any]:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return {"source": str(src), "dest": str(dst), "bytes": dst.stat().st_size, "sha256": sha256(dst)}


def itemize(lines: list[str]) -> str:
    return "\\begin{itemize}\n" + "\n".join(f"\\item {line}" for line in lines) + "\n\\end{itemize}\n"


def selection_table(selection: dict[str, Any]) -> str:
    rows = []
    for rec in selection["stage_counts"]:
        cached = rec.get("cached_sample_count_at_matching_stage") or "--"
        rows.append(
            f"{tex_escape(rec['stage_label'])} & {fmt(rec['sdss_dr17_count'])} & {fmt(cached)} & {fmt(rec.get('retention_vs_spectro_z_parent'), 3)} " + r"\\"
        )
    return "\n".join(rows)


def common_bibliography(extra: str = "") -> str:
    return r"""
\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
""" + extra + "\\end{thebibliography}\n"


def flagship_tex(selection: dict[str, Any], represent: dict[str, Any], rp1: dict[str, Any], gmatch: dict[str, Any], gbpt: dict[str, Any]) -> str:
    base = gmatch["key_results"]["rp1_baseline_bpt_agn_sn3_nearest_replacement"]
    cal = gmatch["key_results"]["rp1_mass_z_moderate_caliper"]
    norepl = gmatch["key_results"]["rp1_greedy_without_replacement"]
    sn10 = gbpt["matched_bpt_agn_sn10"]
    sey = gbpt["matched_nii_seyfert_like_proxy_sn3"]
    rows = [
        ("Broad BPT AGN, S/N$\\geq3$, nearest SF control with replacement", base["matched_pairs"], base["median_delta_log_sSFR"], base.get("median_delta_ci95_low"), base.get("median_delta_ci95_high"), "Preferred association estimate"),
        ("Moderate mass--redshift caliper", cal["matched_pairs"], cal["median_delta_log_sSFR"], None, None, "96.6% target coverage"),
        ("Greedy no-replacement stress test", norepl["matched_pairs"], norepl["median_delta_log_sSFR"], None, None, "Poorer balance; diagnostic only"),
        ("Broad BPT AGN, S/N$\\geq10$", sn10["matched_pairs"], sn10["median_delta_log_sSFR_target_minus_control"], None, None, "Line-S/N sensitivity"),
        ("N II Seyfert-like proxy, S/N$\\geq3$", sey["matched_pairs"], sey["median_delta_log_sSFR_target_minus_control"], None, None, "Subclass sensitivity"),
    ]
    robust_rows = []
    for label, n, val, lo, hi, note in rows:
        ci = f"[{fmt(lo)},{fmt(hi)}]" if lo is not None and hi is not None else "--"
        robust_rows.append(f"{label} & {fmt(n)} & {fmt(val)} & {ci} & {tex_escape(note)} " + r"\\")
    red = represent["dimension_summary"]["redshift"]
    mass = represent["dimension_summary"]["stellar_mass"]
    ssfr = represent["dimension_summary"]["ssfr"]
    return rf"""\documentclass[twocolumn]{{aastex631}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\shorttitle{{Selection-aware SDSS optical AGN/sSFR pilot}}
\shortauthors{{NebulaMind local decision package}}
\begin{{document}}

\title{{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Pilot}}
\author{{NebulaMind Research Autopilot}}
\affiliation{{Local reproducible decision package; public SDSS DR17 data only}}

\begin{{abstract}}
We present a local, selection-aware SDSS DR17 pilot measuring the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of {fmt(selection['strict_sdss_sn_ge_3_total'])} galaxies. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift. The preferred matched comparison yields {fmt(base['matched_pairs'])} pairs and a median $\Delta\log {{\rm sSFR}}$ of {fmt(base['median_delta_log_sSFR'])} dex, with a bootstrap interval of [{fmt(base.get('median_delta_ci95_low'))},{fmt(base.get('median_delta_ci95_high'))}] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
\end{{abstract}}

\keywords{{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}}

\section{{Question and claim boundary}}
This polished local draft is the flagship output from the nine-paper Galaxy Evolution integration. It asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish causal AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.

The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and LINER-like ionization can contaminate broad low-ionization classes \citep{{stasinska2008,stasinska2015}}. Therefore the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\section{{Data and shared selection}}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{{york2000,sdssdr17,brinchmann2004}}. The cached analysis table is capped at {fmt(selection['cached_rows'])} rows and ordered by \texttt{{specObjID}}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains {fmt(selection['strict_sdss_sn_ge_3_total'])} rows, so the cache covers {pct(selection['cached_coverage_of_strict_sdss_sn_ge_3'])}\% of that strict parent.

\begin{{deluxetable*}}{{lrrr}}
\tabletypesize{{\scriptsize}}
\tablecaption{{Selection cascade for the flagship denominator.\label{{tab:selection}}}}
\tablehead{{\colhead{{Selection stage}} & \colhead{{Public DR17 rows}} & \colhead{{Cached rows}} & \colhead{{Retention vs. spectro-z parent}}}}
\startdata
{selection_table(selection)}
\enddata
\tablecomments{{Counts are read-only public SDSS DR17 count queries plus the local cached CSV. Cached rows are shown only where the cache applies.}}
\end{{deluxetable*}}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps {pct(selection['ssfr_low_bin_reference']['sn_ge_3_retention_vs_parent'], 1)}\% of the $-12<\log {{\rm sSFR}}<-11$ parent bin but {pct(selection['ssfr_star_forming_bin_reference']['sn_ge_3_retention_vs_parent'], 1)}\% of the $-10<\log {{\rm sSFR}}<-9.5$ bin. Cached-versus-public marginal checks show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are {fmt(red['max_abs_fraction_difference_pp'],2)}, {fmt(mass['max_abs_fraction_difference_pp'],2)}, and {fmt(ssfr['max_abs_fraction_difference_pp'],2)} percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.

\section{{Classification and matching}}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}}. The cached denominator contains {fmt(rp1['bpt_counts']['star-forming'])} star-forming galaxies, {fmt(rp1['bpt_counts']['intermediate'])} intermediate/composite galaxies, {fmt(rp1['bpt_counts']['agn'])} broad optical AGN, and {fmt(rp1['bpt_counts']['unclassified'])} unclassified objects. Each broad optical AGN host is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.

\begin{{figure*}}
\centering
\includegraphics[width=0.72\textwidth]{{../figures/fig-bpt.pdf}}
\caption{{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}}
\label{{fig:bpt}}
\end{{figure*}}

\section{{Matched-control result}}
The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the optical AGN hosts relative to star-forming controls.

\begin{{deluxetable*}}{{lrrrr}}
\tabletypesize{{\scriptsize}}
\tablecaption{{Robustness ladder for matched catalog-sSFR offsets.\label{{tab:robust}}}}
\tablehead{{\colhead{{Variant}} & \colhead{{$N$ pairs}} & \colhead{{Median $\Delta\log {{\rm sSFR}}$}} & \colhead{{95\% interval}} & \colhead{{Interpretation}}}}
\startdata
{chr(10).join(robust_rows)}
\enddata
\tablecomments{{$\Delta\log {{\rm sSFR}}$ is target minus matched star-forming control. All values are conditional on the optical emission-line denominator.}}
\end{{deluxetable*}}

\begin{{figure*}}
\centering
\includegraphics[width=0.86\textwidth]{{../figures/fig-matched-offsets.pdf}}
\caption{{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT AGN hosts minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions.}}
\label{{fig:offsets}}
\end{{figure*}}

\section{{Interpretation}}
The flagship result is a useful SDSS short-paper result because it is directly measured, reproducible, and falsifiable inside the stated denominator. The median offset is large and survives a moderate mass--redshift caliper. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude to roughly half the preferred broad-BPT estimate. That sensitivity means the safest wording is: broad optical BPT AGN classification is associated with lower catalog sSFR in this capped SDSS emission-line sample. Claims about causal quenching require additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{{Conclusion}}
RP-1 should be the flagship paper from the current local package. It should be polished further as a concise, selection-aware association paper. The other eight active topics should be packaged as a supplementary denominator/proxy atlas, not as independent causal feedback papers, because their original claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables not present in the current SDSS-only analysis.

\section{{Local reproducibility}}
This PDF was generated by local decision package \texttt{{{tex_escape(OUT_ID)}}}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.

{common_bibliography()}
\end{{document}}
"""


def supplement_tex(selection: dict[str, Any], proxy_papers: list[dict[str, Any]]) -> str:
    sections = []
    for idx, p in enumerate(proxy_papers, 1):
        data = p["data"]
        bullets = [tex_escape(x) for x in data.get("result_bullets", [])]
        sections.append(rf"""
\subsection{{{tex_escape(p['title'])}}}
\textbf{{Measured SDSS question.}} {tex_escape(data.get('pilot_question', 'Bounded SDSS denominator/proxy question.'))}

\textbf{{Result summary.}}
{itemize(bullets)}

\textbf{{Missing observables for the full proposal.}} {tex_escape(data.get('full_proposal_requires', 'additional non-SDSS data'))}

\textbf{{Interpretation guard.}} {tex_escape(data.get('interpretation_guard', 'Guarded SDSS-only proxy or denominator.'))}

\begin{{figure}}
\centering
\includegraphics[width=\columnwidth]{{../figures/{p['fig_name']}}}
\caption{{SDSS optical denominator/proxy diagnostic for {tex_escape(p['slug'])}. This is a follow-up target definition or baseline, not a physical-feedback proof.}}
\label{{fig:{p['label']}}}
\end{{figure}}

exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/FLAGSHIP_REVIEW_DECISION_20260709T013510Z.md" in /Users/duhokim/NebulaMind/NebulaMind
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

codex
ACTUAL_RESEARCH_CODEX_KUN_REVIEW_CYCLE_16

**Findings**
- Low: [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:30) includes the exact `1.2--6.5 kpc` fiber-span claim, but that number is not backed by the flagship package’s own analysis JSON and is only indirectly traceable through upstream prompt/brief scaffolding. For strict provenance, either cite the derivation explicitly or soften it to a qualitative “few-kpc central aperture across the redshift range.”
- Low: [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:50) reports the `33.6%`, `94.9%`, and cached-vs-public bin-difference diagnostics as “public counts,” but the direct provenance lives in upstream integration artifacts rather than inside the candidate package itself. If this manuscript is meant to stand alone, add an explicit local provenance note or move the diagnostic into a cited supplement sentence.

**Verification**
- The core invariants are consistent with local data: `8,146` matched pairs, median offset `-1.309 dex`, bootstrap interval `[-1.334,-1.283]`, `60,000` cached rows, `249,917` strict parent, and `24.0%` coverage all match [analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json) and the integration build inputs.
- The supplement’s extra counts and fractions are also traceable to local source-analysis files, including the environment, maintenance-heating, outflow, tracer, gas-depletion, and simulation notes.
- I found no mock/synthetic/fake/placeholder/toy data use in the manuscript text.
- Compile audit shows no fatal TeX failures; only underfull `\hbox` warnings remain.

**Candidate-safe edits**
1. Replace the exact `1.2--6.5 kpc` span with a qualitative aperture statement, or add a source note for the derivation.
2. Add one short provenance sentence for the cached-vs-public marginal diagnostics, naming the local integration artifact that computed them.
tokens used
173,755
ACTUAL_RESEARCH_CODEX_KUN_REVIEW_CYCLE_16

**Findings**
- Low: [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:30) includes the exact `1.2--6.5 kpc` fiber-span claim, but that number is not backed by the flagship package’s own analysis JSON and is only indirectly traceable through upstream prompt/brief scaffolding. For strict provenance, either cite the derivation explicitly or soften it to a qualitative “few-kpc central aperture across the redshift range.”
- Low: [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex:50) reports the `33.6%`, `94.9%`, and cached-vs-public bin-difference diagnostics as “public counts,” but the direct provenance lives in upstream integration artifacts rather than inside the candidate package itself. If this manuscript is meant to stand alone, add an explicit local provenance note or move the diagnostic into a cited supplement sentence.

**Verification**
- The core invariants are consistent with local data: `8,146` matched pairs, median offset `-1.309 dex`, bootstrap interval `[-1.334,-1.283]`, `60,000` cached rows, `249,917` strict parent, and `24.0%` coverage all match [analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json) and the integration build inputs.
- The supplement’s extra counts and fractions are also traceable to local source-analysis files, including the environment, maintenance-heating, outflow, tracer, gas-depletion, and simulation notes.
- I found no mock/synthetic/fake/placeholder/toy data use in the manuscript text.
- Compile audit shows no fatal TeX failures; only underfull `\hbox` warnings remain.

**Candidate-safe edits**
1. Replace the exact `1.2--6.5 kpc` span with a qualitative aperture statement, or add a source note for the derivation.
2. Add one short provenance sentence for the cached-vs-public marginal diagnostics, naming the local integration artifact that computed them.


# command_result
exit_code=0
elapsed_s=192.5
timed_out=False
finished_utc=2026-07-09T16:15:25Z
