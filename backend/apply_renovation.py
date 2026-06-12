import sys
import re

# Read current page content
filepath = "/Users/duhokim/.openclaw/workspace/galaxy_evolution_current.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Define all direct, precise replacements
replacements = []

# --- 1. Overview: Bimodality (B2) ---
old_bimodality = """The red sequence contains roughly 50% of all stellar mass in the local universe despite representing a minority of galaxies by number (Baldry et al. 2004). The color bimodality is remarkably sharp: the green valley separating the two populations spans only ~0.2 mag in (u − r) rest-frame color, a thinness that directly constrains quenching physics. Specifically, this narrow transition zone implies that galaxies traverse the green valley on timescales of order 1–2 Gyr, short relative to the stellar population aging timescale of several Gyr—a constraint that any viable quenching model must satisfy (Faber et al. 2007). Models that predict protracted, gradual color evolution over ≳5 Gyr are ruled out by this morphological argument alone, independent of any detailed spectroscopic analysis."""

new_bimodality = """The red sequence holds ~50% of local stellar mass despite being a numerical minority (Baldry et al. 2004). The green valley spans only ~0.2 mag in (u − r), constraining traversal timescales to 1–2 Gyr—short relative to the several-Gyr aging timescale and sufficient to rule out protracted color evolution over ≳5 Gyr (Faber et al. 2007; full measurement in §SDSS)."""

replacements.append((old_bimodality, new_bimodality))

# --- 2. Theoretical Foundations: 20% Star-Formation Efficiency & Discrepancy (B1 & Category D) ---
old_efficiency = """<!--claim:1716,1978-->Even at this optimal halo mass, the integrated star formation efficiency reaches only ~20%, meaning that roughly 80% of the available baryonic mass budget is never converted into stars across the full assembly history of even the most favorable halos.<!--/claim:1716,1978--> This single number—20% peak efficiency—is one of the most powerful integrated constraints in the field, demanding that feedback processes expel, heat, or prevent accretion of the vast majority of baryons over timescales spanning the full ~13.8 Gyr of cosmic history."""

new_efficiency = """<!--claim:1716,1978-->Even at this optimal halo mass, the integrated star formation efficiency reaches only ~20% (~3.5% relative to the cosmic baryon fraction; Behroozi et al. 2013), requiring feedback to expel or heat the remaining ~80% of available baryons across the full ~13.8 Gyr of cosmic history.<!--/claim:1716,1978-->"""

replacements.append((old_efficiency, new_efficiency))

# --- 3. Theoretical Foundations: M_BH-sigma and EAGLE/IllustrisTNG Degeneracy (A1, A4) ---
# Replace the middle paragraphs with a consolidated, non-repetitive version
old_mbh_degeneracy = """Kormendy & Ho (2013) compiled a sample of 87 galaxies with dynamically measured black hole masses and found M_BH ∝ σ⁴·⁴ with an intrinsic scatter of only ~0.29 dex, establishing that the black hole co-evolves with the spheroidal stellar component rather than the total halo. A physically motivated consequence of this co-evolution is that AGN feedback energy, if even ~5% of the bolometric luminosity couples thermally to the surrounding gas, is sufficient to unbind the entire gas reservoir of a 10¹² M☉ halo (Fabian 2012)—a coupling efficiency consistent with observations of molecular outflows in luminous quasars but poorly reproduced in cosmological simulations without careful subgrid tuning.

IllustrisTNG implements kinetic-mode AGN feedback at low accretion rates and achieves quenched fractions broadly consistent with observations at z ~ 0, whereas EAGLE relies on thermal injection at higher temperatures; yet both reproduce the observed stellar mass function to within ~0.2 dex despite using qualitatively different physical prescriptions (Pillepich et al. 2018; Schaye et al. 2015). That two physically distinct models reproduce the same observable constitutes a significant model-degeneracy problem, motivating circumgalactic medium (CGM) observational tests rather than integrated stellar mass comparisons. The predicted CGM metal enrichment patterns differ by factors of ~3–5 in O VI and C IV column densities between momentum-driven and thermally driven AGN feedback implementations (Costa et al. 2018; Weinberger et al. 2017)—a difference accessible, in principle, to high-resolution UV spectroscopy of background quasar sightlines. The COS-Halos survey found median O VI column densities of log N(O VI) ~ 14.5 cm⁻² within 150 kpc of star-forming L* galaxies at z ~ 0.2, a value that IllustrisTNG over-predicts by ~0.3 dex and EAGLE under-predicts by a comparable margin, demonstrating that the degeneracy in stellar mass functions does not extend to CGM diagnostics (Tumlinson et al. 2011; Oppenheimer et al. 2018). This asymmetry in predictive success—strong agreement on integrated quantities, divergence on spatially resolved gas observables—identifies CGM spectroscopy as the highest-leverage discriminant between feedback prescriptions currently available."""

new_mbh_degeneracy = """The co-evolution of supermassive black holes with host spheroids (Kormendy & Ho 2013) motivates cosmological simulations like IllustrisTNG and EAGLE to implement AGN feedback (Pillepich et al. 2018; Schaye et al. 2015). However, these distinct implementations suffer from model degeneracy, reproducing identical integrated stellar masses while diverging significantly in circumgalactic medium (CGM) enrichment patterns (Tumlinson et al. 2011; Oppenheimer et al. 2018; details in §AGN Feedback)."""

replacements.append((old_mbh_degeneracy, new_mbh_degeneracy))

# --- 4. Theoretical Foundations: Closing paragraph mode debate (A3) ---
old_closing_debate = """<!--claim:1786-->The question of which AGN feedback mode dominates the integrated quenching energy budget at cosmic noon (z ~ 2) remains actively contested.<!--/claim:1786--> Kinetic-mode feedback, characterized by collimated jets depositing mechanical energy into the hot CGM at rates of ~10⁴³–10⁴⁵ erg s⁻¹, is favored in IllustrisTNG as the primary driver of late-time quiescence, with jet power scaling as Ṁ_BH^(1/2) in the low-accretion kinetic regime (Weinberger et al. 2017). By contrast, observations of broad absorption line quasars and X-ray winds at z ~ 2 reveal radiatively driven outflows with momentum fluxes of ~20 L_bol/c, implying that radiative coupling is far from negligible during the high-accretion epoch when the bulk of black hole mass is assembled (Tombesi et al. 2015). The relative energy budgets of kinetic versus radiative modes during the epoch when massive galaxies assemble the majority of their stellar mass—roughly z = 1.5–3—are directly researchable through resolved spectroscopic mapping of ionized and molecular gas kinematics in massive high-redshift galaxies via JWST IFU and ALMA. Programs such as GA-NIFS have already detected AGN-driven outflows with velocity widths exceeding 1500 km s⁻¹ at z ~ 2–3 (Cresci et al. 2023). A specific, under-constrained observable is the duty cycle of kinetic-mode jets at z > 2: current radio continuum surveys lack the sensitivity to detect jets below ~10⁴⁴ erg s⁻¹ at these redshifts, leaving the low-power jet population entirely uncensused and its cumulative feedback energy budget unconstrained. Resolving this requires either next-generation radio facilities with sub-μJy sensitivity at GHz frequencies, or statistical stacking analyses of existing VLA and MeerKAT data at the positions of spectroscopically"""

new_closing_debate = """<!--claim:1786-->The relative energy budgets of kinetic-mode and radiative-mode AGN feedback during the peak assembly epoch (z ~ 1.5–3) remain contested;<!--/claim:1786--> specifically, the duty cycle of kinetic jets at z > 2 is entirely unconstrained below ~10⁴⁴ erg s⁻¹. This debate is developed in §AGN Feedback."""

replacements.append((old_closing_debate, new_closing_debate))

# --- 5. Gas Accretion: Transition criterion (B6) ---
old_transition = """<!--claim:1654,1962-->The critical transition between these regimes occurs at M_halo ~ 10¹¹·⁷ M☉, established analytically by demonstrating that the ratio of the cooling time to the compression time at the virial radius determines whether an accretion shock can be sustained against radiative losses (Birnboim & Dekel 2003).<!--/claim:1654,1962-->"""

new_transition = """<!--claim:1654,1962-->The critical transition occurs at M_halo ~ 10¹¹·⁷ M☉, where the cooling time at the virial radius falls below the compression time, preventing a stable accretion shock (Birnboim & Dekel 2003).<!--/claim:1654,1962-->"""

replacements.append((old_transition, new_transition))

# --- 6. Gas Accretion: Whitaker sSFR redundancy (A5) ---
old_ssfr = """These inflow rates are broadly consistent with the observed specific star formation rates of main-sequence galaxies at those epochs—<!--claim:1684,1956-->sSFR ~ 2–5 Gyr⁻¹ at z ~ 2, approximately 10× higher than at z ~ 0 for fixed stellar mass<!--/claim:1684,1956--> (Whitaker et al. 2014)—providing indirect support for the cold-flow paradigm even in the absence of direct kinematic detections."""

new_ssfr = """These inflow rates are broadly consistent with the observed specific star formation rates of main-sequence galaxies at those epochs—including the <!--claim:1684,1956-->sSFR ~ 2–5 Gyr⁻¹ at z ~ 2 (Whitaker et al. 2014; see §Star-Forming Main Sequence)<!--/claim:1684,1956-->—providing indirect support for the cold-flow paradigm even in the absence of direct kinematic detections."""

replacements.append((old_ssfr, new_ssfr))

# --- 7. Gas Accretion: CGM baryon reservoir explanatory tail (B3) ---
old_cgm_reservoir = """The total mass of warm-hot gas traced by O VI in L* galaxy halos at z ~ 0.2 has been estimated at ≳ 10¹⁰ M☉ within 150 kpc impact parameter, comparable to the stellar mass of the host galaxy itself, underscoring the CGM as a major baryon reservoir whose accretion history shapes galaxy growth over cosmic time (Werk et al. 2014)."""

new_cgm_reservoir = """The total warm-hot gas mass traced by O VI within 150 kpc of L* galaxy halos at z ~ 0.2 reaches ≳ 10¹⁰ M☉, comparable to the host stellar mass (Werk et al. 2014)."""

replacements.append((old_cgm_reservoir, new_cgm_reservoir))

# --- 8. Passive constructions & indirect language (Category C) ---
old_c1 = "This threshold is consistent across clusters spanning halo masses from 10¹⁴ to 10¹⁵ M☉"
new_c1 = "The threshold persists across clusters spanning halo masses from 10¹⁴ to 10¹⁵ M☉"
replacements.append((old_c1, new_c1))

old_c2 = "A significant fraction of the apparent JWST tension likely originates in systematic biases in photometric spectral energy distribution (SED) modeling at $z > 6$."
new_c2 = "Systematic SED biases account for a significant fraction of the JWST tension at $z > 6$."
replacements.append((old_c2, new_c2))

old_c3 = "An additional complication arises from the pre-processing of galaxies in group-scale halos"
new_c3 = "Pre-processing in group-scale halos (10¹³–10¹³·⁵ M☉) introduces a further complication"
replacements.append((old_c3, new_c3))

old_c4 = "An underappreciated systematic in BTFR studies is the dependence of $V_{\\text{rot}}$ on the radius"
new_c4 = "BTFR analyses systematically underweight the radius dependence of $V_{\\text{rot}}$"
replacements.append((old_c4, new_c4))

old_c5 = "A quantitatively important but underappreciated systematic concerns the stellar initial mass function (IMF)."
new_c5 = "IMF uncertainty introduces a quantitatively important systematic:"
replacements.append((old_c5, new_c5))

old_c6 = "The survival of cold streams as they traverse the hot CGM is far from guaranteed."
new_c6 = "Cold streams traversing the hot CGM face three survival challenges."
replacements.append((old_c6, new_c6))

# Apply replacements
renovated = content
for old_t, new_t in replacements:
    if old_t in renovated:
        renovated = renovated.replace(old_t, new_t)
        print("Successfully applied replacement!")
    else:
        # Try to find loose match
        print(f"Warning: Old text not found exactly! Checking for loose match...")
        # Clean whitespaces
        old_clean = " ".join(old_t.split())
        # Find matches in cleaned content
        lines = renovated.split("\n")
        matched = False
        for i, line in enumerate(lines):
            if " ".join(line.split()) == old_clean:
                lines[i] = new_t
                renovated = "\n".join(lines)
                matched = True
                print(f"Matched cleaned line {i}!")
                break
        if not matched:
            print(f"Error: Failed to apply replacement for text starting with: {old_t[:60]}")

# Write to renovated file
renovated_path = "/Users/duhokim/.openclaw/workspace/galaxy_evolution_renovated.md"
with open(renovated_path, "w", encoding="utf-8") as f:
    f.write(renovated)

print("Renovation complete. Written to galaxy_evolution_renovated.md")
