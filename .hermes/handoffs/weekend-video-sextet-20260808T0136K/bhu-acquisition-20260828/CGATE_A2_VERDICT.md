FINDING_CONFIRMED_BOTH

SIGNIFICANCE: DEFECT

# Independent A2 verdict: Roupas (2022)

## Bottom line

F1 is arithmetically real. Roupas's eigenvalue is an angular frequency, but Section 4 and Figure 5 express the corresponding angular rate in `Hz`; the quoted 63 is (\omega_R\) in s\(^{-1}\), while the cyclic frequency is 10.0 Hz. This is worth reporting as a quantitative unit/conversion defect, although the audit overstates its detector consequence: the corrected value is at Advanced LIGO's approximate 10 Hz design edge, not cleanly beyond a universal 20 Hz wall. It does not overturn the paper's broad mode-camouflage conclusion.

F2 independently stands. A relation proportional to (1/M) intersects a finite LISA band in a finite mass interval. The paper states only a lower mass threshold and later claims the entire astrophysical frequency range is in LISA's range; both formulations omit the high-mass exit from the band.

I ran `python3 a2_roupas_audit.py`: it returned 10/10 and exit 0. The pinned text hash is `82f0d604d5b43c86ad893af052cf03dfaafda73e681b80e8123f51ec2789a2ab`.

## F1: angular rate printed as Hz

The paper defines the perturbation as

> `psi_l(r,t) = e^{-i omega t} phi_l(r)`

and its wave equation contains (\omega^2/c^2). Thus (\omega) is angular frequency. Table 1 labels its real entries as

> `(2 G M_bullet / c^3) omega_R`

and gives 0.0062 for (n=0,\ell=2). Figure 4 likewise says the frequency is shown "in dimensions (c^3/2GM_\bullet)." There is no normalization mismatch with the usual dimensionless Schwarzschild (M\omega): multiplying that convention by two gives the paper's (2M\omega) convention.

Using independent arithmetic (SI values (c=299792458\ {m m\,s^{-1}}), (G=6.67430\times10^{-11}), (M_\odot=1.98847\times10^{30}\ {m kg})):

\[
\frac{c^3}{2G(10M_\odot)}=1.0151\times10^4\ {m s^{-1}},
\]

\[
\omega_R=0.0062(1.0151\times10^4)=62.94\ {m s^{-1}},
\qquad
f=\frac{\omega_R}{2\pi}=10.02\ {m Hz}.
\]

Section 4 says instead:

> "The highest possible fundamental mode ... is 63 Hz (Figure 5)"

The number 63 therefore reproduces the angular rate exactly, but `Hz` is the wrong unit. I also downloaded the original arXiv source, rather than relying only on the LaTeXML text. It contains `63{\rm Hz}`, `50{\rm Hz}`, and `10{\rm Hz}` verbatim and calls the Figure 5 asset `omegaR_M_Hz_l-2.eps`. This is not conversion damage.

### Positive control

The control is sound. The standard Schwarzschild gravitational (\ell=2,n=0) mode is

\[
GM\omega/c^3\simeq0.37367-0.08896i.
\]

For (10M_\odot), its real cyclic frequency is

\[
f=\frac{0.37367}{2\pi}\frac{c^3}{GM}=1207.5\ {m Hz}.
\]

Treating (\omega) itself as Hz gives 7587 Hz. The established review value is approximately 1.2 kHz for a 10-solar-mass Schwarzschild hole, so only the (2\pi) conversion passes. See [Kokkotas & Schmidt, *Quasi-Normal Modes of Stars and Black Holes*](https://link.springer.com/article/10.12942/lrr-1999-2), which gives (M\omega\approx(0.37,-0.09)) and 1.2 kHz for (10M_\odot).

### The Discussion's 10 Hz

The proposed inference is plausible but not demonstrable. Section 5 prints

> "the mode frequencies ... namely (10^{-6}{\rm Hz}\lesssim\omega_R\lesssim10{\rm Hz})"

and (63/(2\pi)=10.03), an excellent numerical match. But Section 4 also gives the same upper range as 50 Hz immediately before saying 63 Hz. Because the endpoints are already inconsistent and coarsely rounded, 10 Hz could be an unannounced correction, a typo, or rough order-of-magnitude prose. It supports the diagnosis circumstantially; it is not evidence that the author knowingly applied (2\pi). F1 does not need that inference.

The unexplained 50 has no innocent reading that removes F1. The table fixes 62.94 s\(^{-1}\) at the stated 10-solar-mass endpoint. Fifty is neither that value nor (62.94/(2\pi)); it is best treated as rough/inconsistent rounding. It cannot explain a factor-(2\pi) unit mismatch.

### Detector consequence and significance

Audit check 3 is not defensible at its stated precision. A 20 Hz lower analysis cutoff is conventional for many searches, but it is not a detector-independent physical boundary and is not supplied by Roupas. Advanced LIGO is described as designed for 10 Hz to 5 kHz and as "usable to 10 Hz" ([LIGO detector sensitivity paper](https://dcc-backup.ligo.org/LIGO-P1500260/public); [Advanced LIGO design paper](https://dcc-llo.ligo.org/LIGO-P0900255/public)). Accordingly:

- Literal 63 Hz is comfortably in the instrument band.
- Corrected 10.02 Hz is on the nominal design boundary and may be below practical search cutoffs, but it is not cleanly "outside" without specifying an observing run, noise curve, waveform amplitude, and analysis.

I still classify F1 as **DEFECT**, not merely **SLIP**, because the factor-(2\pi) mistake is systematic in a plotted physical-frequency quantity and in multiple numerical frequency claims, and those claims are used to discuss detector coverage. The defensible claim is a quantitative frequency/unit defect that weakens the stated LIGO justification—not a decisive reversal of detectability. The qualitative conclusion may survive because amplitude is unknown and mode camouflage is a separate argument.

## F2: LISA requires a band, not an unbounded floor

The paper says:

> "for (M_\bullet\gtrsim10^4M_\odot) the fundamental mode ... lies within ... (\sim10^{-1}-10^{-5}\,\mathrm{Hz}) of ... LISA"

With the physically correct cyclic frequency,

\[
f(M)=10.02\,\mathrm{Hz}\left(\frac{10M_\odot}{M}\right).
\]

Solving (10^{-5}\le f\le10^{-1}\) gives approximately

\[
1.00\times10^3M_\odot\le M\le1.00\times10^7M_\odot.
\]

Thus (f(10^9M_\odot)=1.00\times10^{-7}\) Hz, about 100 times below the paper's quoted LISA floor. Even adopting the paper's erroneous no-(2\pi) numerical convention gives (6.29\times10^{-7}) at (10^9M_\odot), still about 16 times below the floor, with a finite window of roughly (6.3\times10^3) to (6.3\times10^7M_\odot). F2 is therefore independent of F1.

The lower threshold (10^4M_\odot) is a tolerable order-of-magnitude sufficient threshold near the high-frequency edge; the defect is its unbounded `\gtrsim` formulation and the Discussion's stronger statement that the astrophysical range lies inside LISA's range. The paper itself analyzes (10\) through (10^9M_\odot), so the omitted upper bound matters internally.

## Reproduction checks 5 and 6

The amplitude grep is honest. Section 4 explicitly says:

> "the excitation factors of its quasi-normal modes ... have to be calculated. This is an involved task, that this work urges the community to perform."

It then says detection may require "developing the appropriate technology ... provided they exist." No ringdown excitation amplitude is derived.

The rate regex in the script is narrow, so its assertion is stronger than that regex alone proves. I separately searched the full body for `rate(s)`, event/occurrence/incidence, mergers, population, abundance, number density, formation, and per-time language. The merger mentions only describe the source scenario; there is no event-rate, merger-rate, abundance, population, or expected-count estimate. References whose titles contain `formation` do not change that result. Check 6's substantive conclusion is correct even though its automated proof should use broader patterns or manual confirmation.

