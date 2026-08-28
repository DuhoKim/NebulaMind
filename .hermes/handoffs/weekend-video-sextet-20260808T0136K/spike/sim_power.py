import numpy as np
import scipy.stats as stats
import time

def generate_catalog(N, A=0.0):
    # Uniform points on sphere
    phi = np.random.uniform(0, 2*np.pi, N)
    costheta = np.random.uniform(-1, 1, N)
    sintheta = np.sqrt(1 - costheta**2)
    x = sintheta * np.cos(phi)
    y = sintheta * np.sin(phi)
    z = costheta
    vecs = np.vstack([x,y,z]).T
    
    # Injected axis: Z-axis (0, 0, 1)
    axis = np.array([0, 0, 1])
    cos_angles = vecs.dot(axis)
    
    # Prob of +1
    p_plus = 0.5 + (A / 2.0) * cos_angles
    p_plus = np.clip(p_plus, 0, 1)
    
    # Generate signs
    signs = np.where(np.random.rand(N) < p_plus, 1, -1)
    return cos_angles, signs

def compute_stats(cos_angles, signs):
    M = np.mean(signs)
    D = np.mean(signs * cos_angles)
    return M, D

def permutation_pvalue(cos_angles, signs, n_perm=1000):
    M, D_obs = compute_stats(cos_angles, signs)
    
    # Fast permutation:
    # Shuffle signs
    shuffled_signs = np.copy(signs)
    D_null = np.zeros(n_perm)
    for i in range(n_perm):
        np.random.shuffle(shuffled_signs)
        D_null[i] = np.mean(shuffled_signs * cos_angles)
        
    p_val = np.mean(np.abs(D_null) >= np.abs(D_obs))
    return D_obs, p_val

def test_null_size(N=10000, trials=1000):
    p_vals = []
    for _ in range(trials):
        cos_angles, signs = generate_catalog(N, A=0.0)
        _, p = permutation_pvalue(cos_angles, signs, n_perm=1000)
        p_vals.append(p)
    p_vals = np.array(p_vals)
    fpr_05 = np.mean(p_vals <= 0.05)
    fpr_01 = np.mean(p_vals <= 0.01)
    print(f"Null size check (N={N}, trials={trials}):")
    print(f"  Fraction p <= 0.05: {fpr_05:.4f} (Expected 0.05)")
    print(f"  Fraction p <= 0.01: {fpr_01:.4f} (Expected 0.01)")
    
    # KS test for uniformity
    _, ks_p = stats.kstest(p_vals, 'uniform')
    print(f"  KS test for uniform distribution p-value: {ks_p:.4f}")

def compute_power_curve():
    N_list = [10000, 30000, 100000, 200000]
    A_list = [0.01, 0.02, 0.04, 0.08]
    trials = 500
    n_perm = 500
    
    print("\nPower Curve (Fraction of p < 0.001):")
    print(f"{'N':<10} | {'A=0.01':<10} | {'A=0.02':<10} | {'A=0.04':<10} | {'A=0.08':<10}")
    print("-" * 60)
    
    for N in N_list:
        row = [str(N)]
        for A in A_list:
            # We use analytical permutation p-value for speed in power curve
            # p_val = 2 * (1 - norm.cdf(|D| / std_D))
            # Variance of D under permutation: 
            # Var(D) = (mean(cos^2) - mean(cos)^2) / (N-1) * (1 - M^2)
            power = 0
            for _ in range(trials):
                cos_angles, signs = generate_catalog(N, A)
                M, D_obs = compute_stats(cos_angles, signs)
                
                var_cos = np.var(cos_angles)
                var_D = var_cos * (1 - M**2) / (N - 1)
                std_D = np.sqrt(var_D)
                z = np.abs(D_obs) / std_D
                p_val = 2 * (1 - stats.norm.cdf(z))
                
                if p_val < 0.001:
                    power += 1
            row.append(f"{power/trials:.3f}")
        print(f"{row[0]:<10} | {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10}")

def test_unbiasedness(N=100000, A=0.04):
    cos_angles, signs = generate_catalog(N, A)
    M, D = compute_stats(cos_angles, signs)
    # The expected value of D is (A / 2) * mean(cos^2) * 2 = A * mean(cos^2)
    # On a sphere, mean(cos^2) = 1/3
    expected_D = A / 3.0
    print("\nUnbiasedness check:")
    print(f"  Injected Amplitude A: {A}")
    print(f"  Expected D (A/3):     {expected_D:.6f}")
    print(f"  Recovered D:          {D:.6f}")
    print(f"  Implied A (3*D):      {3*D:.6f}")

if __name__ == '__main__':
    t0 = time.time()
    test_null_size(N=5000, trials=1000)
    test_unbiasedness(N=500000, A=0.04)
    compute_power_curve()
    print(f"\nCompleted in {time.time() - t0:.2f} seconds.")
