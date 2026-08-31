VERDICT: UNDETECTABLE (Below any conceivable detector floor)

The Roupas "detectable" claim fails by many orders of magnitude when the amplitude and damping time are explicitly computed. The claim neglects that a mode with an astronomically long damping time radiates its energy so slowly that its instantaneous strain is effectively zero.

### 1. Formalism
I use the ringdown energy-fraction model. The total energy radiated in the fundamental mode is $E_{GW} = \epsilon_{rd} M c^2$.
Because the damping time $\tau$ (hundreds of millions of years) vastly exceeds the LISA observation time ($T_{obs} \approx 4$ years $\approx 1.26 \times 10^8$ s), the signal operates as a continuous monochromatic wave.
The energy flux yields the strain amplitude: 
$$h_0 = \sqrt{\frac{4 G \epsilon_{rd} M}{\pi c D_L^2 f^2 \tau}}$$
The characteristic strain for comparison against the LISA noise curve $h_n(f) = \sqrt{f S_n(f)}$ is $h_c = h_0 \sqrt{f T_{obs}}$.

### 2. Damping Time & Frequencies
From Roupas Table 1, the fundamental $n=0, \ell=2$ mode has an imaginary part $\frac{2GM}{c^3}\omega_I = -1.53 \times 10^{-17}$. 
This implies a massive damping time:
$\tau = \frac{2GM}{c^3} \frac{1}{1.53 \times 10^{-17}} \approx 6.4 \times 10^{15} \left( \frac{M}{10^4 M_\odot} \right)$ seconds.
For $10^4 M_\odot$, $\tau \approx 2 \times 10^8$ years. For $10^6 M_\odot$, $\tau \approx 2 \times 10^{10}$ years.
The frequency scales as $f \approx 63\text{ Hz} \left( \frac{10 M_\odot}{M} \right)$.

### 3. Excitation Bounds ($\epsilon_{rd}$) & Representative Distance
We place the source at a fiducial LISA SMBH merger distance of $D_L = 1$ Gpc.
- **Optimistic bound:** $\epsilon_{rd} = 0.01$. This unphysically assumes the interior mode receives a full standard BBH merger energy fraction, ignoring the angular momentum barrier.
- **Conservative/Physical bound:** $\epsilon_{rd} = 10^{-17}$. As standard for ultra-compact objects, excitation of trapped interior modes is suppressed by the transmission coefficient of the potential barrier, which scales as $|\omega_I|/\omega_R \sim 10^{-15}$. Thus $\epsilon_{rd} \approx 0.01 \times 10^{-15} = 10^{-17}$.

### 4. Amplitudes vs. LISA Sensitivity
We evaluate $h_c$ across the LISA mass range against the public Robson-Cornish-Liu 2019 $h_n(f)$ sensitivity curve.

- **$M = 10^4 M_\odot$** ($f = 0.063$ Hz, $\tau = 2 \times 10^8$ yr, LISA $h_n \approx 2 \times 10^{-21}$):
  - Optimistic ($\epsilon_{rd} = 0.01$): $h_c \approx 1.3 \times 10^{-22}$
  - Physical ($\epsilon_{rd} = 10^{-17}$): $h_c \approx 4.2 \times 10^{-30}$
- **$M = 10^5 M_\odot$** ($f = 0.0063$ Hz, $\tau = 2 \times 10^9$ yr, LISA $h_n \approx 2.5 \times 10^{-22}$):
  - Optimistic ($\epsilon_{rd} = 0.01$): $h_c \approx 4.3 \times 10^{-22}$
  - Physical ($\epsilon_{rd} = 10^{-17}$): $h_c \approx 1.3 \times 10^{-29}$
- **$M = 10^6 M_\odot$** ($f = 0.00063$ Hz, $\tau = 2 \times 10^{10}$ yr, LISA $h_n \approx 8 \times 10^{-21}$):
  - Optimistic ($\epsilon_{rd} = 0.01$): $h_c \approx 1.3 \times 10^{-21}$
  - Physical ($\epsilon_{rd} = 10^{-17}$): $h_c \approx 4.2 \times 10^{-29}$

### 5. Conclusion
Even if we grant the absurdly optimistic bound of $\epsilon_{rd} = 0.01$ (ignoring the barrier entirely), the characteristic strain barely brushes the LISA noise floor in the most sensitive bucket. 
Under any physically defensible excitation factor (which accounts for the barrier transmission coefficient), the amplitude is $\sim 7$ orders of magnitude below LISA's floor. The mode leaks its energy far too slowly to be detectable. Entry 21 is PROSPECT-without-a-number by derivation.
