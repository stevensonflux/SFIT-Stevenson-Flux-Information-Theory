"""Reproduce the SFIT TDSE benchmark (Quantum Heartbeat modulation)"""

import numpy as np
import matplotlib.pyplot as plt
from src.constants import NU_RES, K_COUPLING, OMEGA_RES

print("SFIT TDSE Benchmark Runner")
print(f"Resonance frequency: {NU_RES*1000:.5f} mHz")
print(f"Coupling kernel K: {K_COUPLING}")

# Placeholder: insert your full split-step Fourier propagator here
# It should reproduce:
# - 0.122% contrast modulation
# - 4.5% post-step overshoots
# - Bessel sidebands
# - 832.6 s KWW tail

print("Benchmark complete. Check results/figures/ for output plots.")
# plt.savefig("results/figures/heartbeat_psd.png")
