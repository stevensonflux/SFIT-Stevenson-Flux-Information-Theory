"""SFIT physical constants and parameters (from Preprint)"""

NU_RES = 0.00120134          # Hz — Quantum Heartbeat resonance
K_COUPLING = 1.060           # Refined coupling kernel
TAU_KWW = 832.6              # s — KWW relaxation time
BETA_KWW = K_COUPLING        # Stretched exponent equals K
ALPHA_MOD = 0.00122          # Metric perturbation amplitude
R_EARTH = 6371000.0          # m
G_EARTH = 9.80665            # m/s²
M_NEUTRON = 1.67492749804e-27  # kg

# Derived
OMEGA_RES = 2 * 3.1415926535 * NU_RES
HALF_PERIOD = 1 / (2 * NU_RES)   # ≈ 416.65 s — expected π-phase overshoot time
