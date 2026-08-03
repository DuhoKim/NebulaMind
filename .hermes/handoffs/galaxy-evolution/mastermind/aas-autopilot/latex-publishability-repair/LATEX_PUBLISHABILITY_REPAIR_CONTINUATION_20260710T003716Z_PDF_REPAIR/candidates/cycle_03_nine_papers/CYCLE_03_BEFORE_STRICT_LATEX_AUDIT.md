# Strict LaTeX audit before cycle 3

all_build_ok: True
all_clean_ok: False
layout_warning_count: 5
undefined_count: 0

## m1_rp1_sdss_agn_sfr_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=239222
- fatal_hits={}
- warning_hits={}

## m1_rp2_environment_quenching_integrated.tex
- build_ok=True clean_ok=False rc=0 bytes=91929
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 4}
- log lines:
  - L578: Underfull \hbox (badness 1019) in paragraph at lines 57--58
  - L583: Underfull \hbox (badness 3919) in paragraph at lines 57--58
  - L590: Underfull \hbox (badness 1178) in paragraph at lines 57--58
  - L597: Underfull \hbox (badness 1931) in paragraph at lines 72--73

## m1_rp3_maintenance_heating_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=90962
- fatal_hits={}
- warning_hits={}

## m2_p1_outflow_escape_recycling_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=322914
- fatal_hits={}
- warning_hits={}

## m2_p2_radio_jet_environment_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=90973
- fatal_hits={}
- warning_hits={}

## m2_p3_feedback_transition_mass_integrated.tex
- build_ok=True clean_ok=False rc=0 bytes=96337
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 1}
- log lines:
  - L582: Underfull \hbox (badness 1194) in paragraph at lines 77--78

## m3_p1_multiphase_census_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=90433
- fatal_hits={}
- warning_hits={}

## m3_p2_gas_depletion_efficiency_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=222457
- fatal_hits={}
- warning_hits={}

## m3_p3_simulation_validation_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=98300
- fatal_hits={}
- warning_hits={}
