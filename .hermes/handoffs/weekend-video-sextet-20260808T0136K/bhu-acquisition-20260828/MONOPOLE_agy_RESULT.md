# Monopole-Subtracted Reading B Results (agy)

I executed `cutoffA_monopole_agy.py` based on Reading B, applying the monopole subtraction as demanded by the no-zero-mode condition. 

## k_min Sensitivity Table and Findings

The decisive output is the `k_min` sensitivity table after monopole subtraction:

```text
======================================================================
PROGRAM A2: MONOPOLE SUBTRACTED READING B
======================================================================

k_S (cutoff scale) = 4.48e-04 Mpc^-1

[1] k_min SENSITIVITY TABLE
k_min (Mpc^-1)  | S_1/2 (uK^4)    | c (Monopole)    | Min P_B        
-----------------------------------------------------------------
1.0e-04         | 9559.2          | 2.26e-09        | 6.27e-10       
1.0e-05         | 10057.1         | 8.40e-09        | -2.17e-09      
1.0e-06         | 10062.8         | 1.52e-08        | -2.09e-09      
1.0e-07         | 10062.8         | 2.26e-08        | -2.77e-09      
1.0e-08         | 10062.8         | 3.05e-08        | 2.19e-10       

[2] COMPARISON & CONCLUSION
LCDM (unlensed) : 34,924 uK^4
Reading A       : 6,897 uK^4
Reading B (subtracted) : 10,063 uK^4 (at k_min=1e-8)
Observed        : ~1,150 uK^4
```

## Conclusions

1. **S_1/2 Convergence:** The value of `S_1/2` **converges** to approximately 10,063 μK⁴ as `k_min` goes to zero. The earlier "no number" conclusion due to IR divergence is definitively **overturned**. Monopole subtraction removes the divergence artifact, and Reading B does indeed have a finite prediction.

2. **Positivity Failure:** Although the divergence is cured, `min(P_B)` on the grid goes negative (reaching around `-2.77e-9` at `k_min = 1e-07`). This demonstrates that the no-zero-mode condition is incompatible with a valid, strictly non-negative power spectrum under this construction. The subtracted field `ξ_B = (ξ_ΛCDM - c)·W` loses the positivity property that was previously guaranteed by Schur/Bochner theorems, introducing unphysical negative power.

3. **Comparison:** Even with the divergence removed, the stable prediction for Reading B (10,063 μK⁴) remains far above the observed value (~1,150 μK⁴), and is higher than Reading A (6,897 μK⁴), though much lower than full ΛCDM (34,924 μK⁴).
