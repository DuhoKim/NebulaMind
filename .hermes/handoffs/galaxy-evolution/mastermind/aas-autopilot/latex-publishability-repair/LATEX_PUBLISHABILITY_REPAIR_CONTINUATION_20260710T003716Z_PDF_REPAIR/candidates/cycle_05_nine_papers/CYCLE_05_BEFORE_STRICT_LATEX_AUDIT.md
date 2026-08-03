# Strict LaTeX audit before cycle 5

all_build_ok: True
all_clean_ok: False
layout_warning_count: 1
undefined_count: 0

## m1_rp1_sdss_agn_sfr_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=240136
- fatal_hits={}
- warning_hits={}

## m1_rp2_environment_quenching_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=93470
- fatal_hits={}
- warning_hits={}

## m1_rp3_maintenance_heating_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=91446
- fatal_hits={}
- warning_hits={}

## m2_p1_outflow_escape_recycling_integrated.tex
- build_ok=True clean_ok=False rc=0 bytes=326249
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 1}
- log lines:
  - L579: Underfull \hbox (badness 1859) in paragraph at lines 57--58

## m2_p2_radio_jet_environment_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=92759
- fatal_hits={}
- warning_hits={}

## m2_p3_feedback_transition_mass_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=98559
- fatal_hits={}
- warning_hits={}

## m3_p1_multiphase_census_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=92221
- fatal_hits={}
- warning_hits={}

## m3_p2_gas_depletion_efficiency_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=223075
- fatal_hits={}
- warning_hits={}

## m3_p3_simulation_validation_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=98741
- fatal_hits={}
- warning_hits={}
