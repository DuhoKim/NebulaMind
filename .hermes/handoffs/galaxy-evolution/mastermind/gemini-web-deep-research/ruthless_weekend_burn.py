#!/usr/bin/env python3
import subprocess
import time
from pathlib import Path
import os
import sys

BASE_DIR = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research")
REQUESTS_DIR = BASE_DIR / "requests"
OUTPUTS_DIR = BASE_DIR / "outputs"
CAPTURE_SCRIPT = BASE_DIR / "capture_current.py"

REQUESTS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

TOPICS = [
    "AGN feedback mechanisms in the Perseus Cluster",
    "Ram pressure stripping effects in the Virgo Cluster",
    "Observational constraints on the M-sigma relation for high-redshift galaxies",
    "JWST discoveries regarding z>10 galaxy mass functions",
    "The role of major mergers in triggering quasar activity",
    "Cold gas accretion streams in cosmic web filaments",
    "Inside-out quenching in local spiral galaxies",
    "Morphological transformation in galaxy groups vs clusters",
    "The effect of dark matter halo assembly bias on galaxy quenching",
    "Stellar mass downsizing in the early universe",
    "Supernova feedback and galactic winds in dwarf galaxies",
    "Dust obscuration in starburst galaxies at cosmic noon",
    "The fraction of quiescent galaxies as a function of environment at z=2",
    "Radio-mode AGN feedback in brightest cluster galaxies (BCGs)",
    "Quasar-driven outflows and their impact on molecular gas reservoirs",
    "The correlation between bulge mass and specific star formation rate",
    "Evolution of the cosmic star formation rate density",
    "Lyman-alpha emitters as tracers of early galaxy formation",
    "The impact of reionization on dwarf galaxy formation",
    "Metallicity gradients in local and high-redshift galaxies",
    "The role of magnetic fields in regulating star formation in spiral disks",
    "Gas stripping mechanisms in the Coma Cluster",
    "The connection between post-starburst (E+A) galaxies and AGN",
    "Tidal disruption events and their relation to galaxy properties",
    "The origin of the red sequence in galaxy clusters",
    "The green valley: transition timescales and mechanisms",
    "Satellite galaxy quenching in Milky Way-mass halos",
    "The impact of the environment on the mass-metallicity relation",
    "Evidence for positive AGN feedback triggering star formation",
    "The role of bars in driving secular evolution in disk galaxies",
    "Kinematics of gas in merging galaxies using ALMA data",
    "The buildup of the stellar halo in massive galaxies",
    "Globular cluster populations as tracers of galaxy assembly history",
    "The missing satellites problem and proposed astrophysical solutions",
    "The core-cusp problem in dwarf spheroidal galaxies",
    "Ultrafaint dwarf galaxies as probes of dark matter models",
    "The survival of stellar streams in the Milky Way halo",
    "The properties of thick disks in edge-on spiral galaxies",
    "The star formation history of the Magellanic Clouds",
    "The impact of cosmic rays on galactic outflows",
    "The physics of the circumgalactic medium (CGM) in simulated galaxies",
    "Observational constraints on the temperature of the CGM",
    "The distribution of metals in the intergalactic medium",
    "The evolution of the galaxy stellar mass function since z=4",
    "The role of minor mergers in driving size growth of elliptical galaxies",
    "The fundamental plane of elliptical galaxies and its evolution",
    "The properties of ultra-diffuse galaxies (UDGs) in various environments",
    "The connection between dark matter halo spin and galaxy morphology",
    "The impact of feedback on the structure of dark matter halos",
    "The use of weak gravitational lensing to measure dark matter halo masses",
    "The role of active galactic nuclei in shaping the circumgalactic medium",
    "The connection between galaxy properties and the topology of the cosmic web",
    "The evolution of the mass-size relation for early-type galaxies",
    "The fraction of barred galaxies as a function of redshift",
    "The role of turbulence in regulating star formation in molecular clouds",
    "The initial mass function (IMF) variations in different galactic environments",
    "The properties of high-velocity clouds and their connection to galactic accretion",
    "The evolution of the dust-to-gas ratio in galaxies",
    "The impact of stellar multiplicity on galaxy evolution models",
    "The use of machine learning to classify galaxy morphologies in large surveys",
    "The connection between the circumgalactic medium and the cosmic web",
    "The role of cosmic dust in shaping the spectral energy distributions of galaxies",
    "The properties of star-forming regions in distant galaxies using JWST",
    "The evolution of the neutral hydrogen (HI) mass function",
    "The connection between galaxy kinematics and their star formation histories",
    "The impact of active galactic nuclei on the interstellar medium of their host galaxies",
    "The properties of Lyman-break galaxies at z>6",
    "The role of magnetic fields in launching galactic outflows",
    "The connection between galaxy mergers and the triggering of starbursts",
    "The evolution of the galaxy luminosity function in the rest-frame UV",
    "The properties of submillimeter galaxies (SMGs) and their evolutionary paths",
    "The impact of environmental density on the morphology-density relation",
    "The role of secular evolution in the formation of pseudobulges",
    "The properties of dwarf irregular galaxies in the Local Group",
    "The connection between dark matter halo concentration and galaxy properties",
    "The evolution of the Tully-Fisher relation",
    "The impact of active galactic nuclei on the star formation efficiency of galaxies",
    "The properties of extreme emission line galaxies",
    "The role of cosmic voids in galaxy evolution",
    "The connection between galaxy properties and their X-ray emission",
    "The evolution of the mass-metallicity relation for star-forming galaxies",
    "The impact of stellar feedback on the properties of dwarf galaxies",
    "The properties of galaxies hosting gamma-ray bursts",
    "The role of the circumgalactic medium in the baryon cycle of galaxies",
    "The connection between galaxy mergers and the growth of supermassive black holes",
    "The evolution of the fraction of interacting galaxies",
    "The impact of the environment on the star formation rate of galaxies",
    "The properties of galaxies hosting fast radio bursts",
    "The role of active galactic nuclei in driving the evolution of the intergalactic medium",
    "The connection between galaxy properties and their radio emission",
    "The evolution of the size-luminosity relation for early-type galaxies",
    "The impact of dark matter self-interactions on the structure of galaxy clusters",
    "The properties of galaxies in the local universe using the SDSS",
    "The role of the circumgalactic medium in regulating the star formation histories of galaxies",
    "The connection between galaxy properties and their dust content",
    "The evolution of the fraction of star-forming galaxies in clusters",
    "The impact of active galactic nuclei on the temperature of the circumgalactic medium",
    "The properties of galaxies at the epoch of reionization using JWST",
    "The role of the intergalactic medium in fueling star formation in galaxies",
    "The connection between galaxy properties and their position in the cosmic web"
]

TEMPLATE = """# Gemini-web Deep Research prompt

Marker to require in Gemini output: `GEMINI_WEB_RT_DEEP_RESEARCH_OUTPUT_DONE`

## Task
You are assisting a supervised NebulaMind research-topic quality pass.
Topic: {topic}

Please provide a comprehensive, systematic deep research literature review of the last 10 years of observational and theoretical data regarding this topic. 

## Required output format
1. `Topic Overview`
2. `Prior studies/reviews to verify locally` (bullet list of 10-15 high leverage papers with DOI/arXiv links)
3. `What the literature appears to establish`
4. `What remains unknown or heavily debated`
5. `Data/survey plan or Observational Constraints`
6. `Overclaim risks and wording guardrails`

Finish with the exact standalone marker:
`GEMINI_WEB_RT_DEEP_RESEARCH_OUTPUT_DONE`
"""

def run_apple_script(script: str):
    subprocess.run(["osascript", "-e", script], check=True)

def copy_to_clipboard(text: str):
    subprocess.run("pbcopy", universal_newlines=True, input=text, check=True)

print(f"Starting 8-hour ruthless burn. {len(TOPICS)} topics queued.")

for i, topic in enumerate(TOPICS):
    req_id = f"REQ_100{i:02d}_WEEKEND_BURN"
    prompt_file = f"{req_id}_PROMPT.md"
    output_file = f"{req_id}_OUTPUT.md"
    
    prompt_path = REQUESTS_DIR / prompt_file
    output_path = OUTPUTS_DIR / output_file
    
    if output_path.exists():
        print(f"Skipping {prompt_file}, output exists.")
        continue
        
    print(f"--- [{i+1}/{len(TOPICS)}] Processing {req_id}: {topic} ---")
    prompt_content = TEMPLATE.format(topic=topic)
    prompt_path.write_text(prompt_content, encoding="utf-8")
    
    copy_to_clipboard(prompt_content)
    
    try:
        run_apple_script('tell application "Google Chrome" to activate')
        run_apple_script('tell application "Google Chrome" to tell window 1 to make new tab with properties {URL:"https://gemini.google.com/app"}')
        time.sleep(5)
        run_apple_script('tell application "System Events" to keystroke "v" using {command down}')
        time.sleep(1)
        run_apple_script('tell application "System Events" to key code 36')
        
        print("Waiting for generation... (up to 30 mins)")
        # Run capture script
        subprocess.run(["python3", str(CAPTURE_SCRIPT), str(output_path)], check=True)
        print(f"Completed {req_id}\n")
    except Exception as e:
        print(f"Error during {req_id}: {e}")
        time.sleep(10)
        
    time.sleep(5) # brief pause before next tab
