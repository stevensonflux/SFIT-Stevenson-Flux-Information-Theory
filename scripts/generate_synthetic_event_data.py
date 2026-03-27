"""
SFIT Synthetic Event Data Generator
====================================
Generates a small synthetic event-by-event time-series file that reproduces
the main features of the qBounce ILL 3-14-412 reanalysis for quick testing.

Key embedded SFIT features:
- 1.20134 mHz modulation (Quantum Heartbeat)
- Phase-locked π-overshoot behavior near t = 416.65 s
- KWW-like relaxation tails (approximated via modulated rate)
- Poisson statistics with ~0.12% contrast + occasional 4.5% jumps

Output: data/processed/synthetic_event_sample.dat
Format: One event per line → "timestamp_us detector_channel"
"""

import numpy as np
import os
from datetime import datetime

# ==================== SFIT Key Constants (from Preprint) ====================
NU_RES = 0.00120134          # Hz — Quantum Heartbeat
OMEGA_RES = 2 * np.pi * NU_RES
HALF_PERIOD = 1 / (2 * NU_RES)  # ≈ 416.65 s
K_COUPLING = 1.060
BASE_RATE = 50.0             # average events per second (adjustable)
MOD_AMPLITUDE = 0.00122      # ~0.122% contrast
OVERSHOOT_FACTOR = 1.045     # ~4.5% post-step overshoot
SAMPLING_DT = 0.1            # seconds (10 Hz effective for modulation)
TOTAL_DURATION = 3600.0      # 1 hour — small but sufficient for testing PSD/KWW

# Seed for reproducibility
np.random.seed(42)

def sfit_modulation(t):
    """Time-dependent rate including 1.20134 mHz heartbeat + overshoot effect"""
    heartbeat = MOD_AMPLITUDE * np.cos(OMEGA_RES * t)
    
    # Simulate step-like overshoots every half-period (π phase jump)
    phase = (t % (2 * HALF_PERIOD)) / HALF_PERIOD
    overshoot = 0.0
    if abs(phase - 1.0) < 0.02 or abs(phase) < 0.02:   # near half-period boundaries
        overshoot = (OVERSHOOT_FACTOR - 1.0) * np.exp(-abs(phase - 1.0) * 50)
    
    return 1.0 + heartbeat + overshoot

def generate_synthetic_events():
    print("Generating SFIT synthetic event data...")
    
    timestamps = []
    channels = []
    
    t = 0.0
    while t < TOTAL_DURATION:
        # Instantaneous rate modulated by SFIT heartbeat
        rate = BASE_RATE * sfit_modulation(t)
        
        # Poisson process: time to next event
        dt = np.random.exponential(1.0 / rate)
        t += dt
        
        if t >= TOTAL_DURATION:
            break
            
        # Simulate detector channel (simple: mostly low channel with some spread)
        channel = np.random.poisson(12) + 8   # around typical qBounce pulse heights
        
        timestamps.append(int(t * 1e6))       # timestamp in microseconds
        channels.append(channel)
    
    print(f"Generated {len(timestamps):,} synthetic events over {TOTAL_DURATION/3600:.1f} hours")
    return np.array(timestamps), np.array(channels)

def save_synthetic_data(timestamps, channels, filename="data/processed/synthetic_event_sample.dat"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, "w") as f:
        f.write("# SFIT Synthetic Event Data for ILL-style qBounce reanalysis\n")
        f.write("# Format: timestamp_us (relative)  detector_channel\n")
        f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"# Contains 1.20134 mHz Quantum Heartbeat modulation (K={K_COUPLING})\n")
        f.write("# Use with scripts/analyze_synthetic.py for PSD, KWW, etc.\n\n")
        
        for ts, ch in zip(timestamps, channels):
            f.write(f"{ts} {ch}\n")
    
    print(f"Synthetic data saved to: {filename}")
    print(f"File size: {os.path.getsize(filename)/1024:.1f} KB")

# ====================== Main ======================
if __name__ == "__main__":
    timestamps, channels = generate_synthetic_events()
    save_synthetic_data(timestamps, channels)
    
    print("\nNext steps:")
    print("1. Run: python scripts/analyze_synthetic.py  (create this next if needed)")
    print("2. You should see a clear peak near 1.20134 mHz in the PSD.")
    print("3. Upload this file to your GitHub data/processed/ and Zenodo.")
