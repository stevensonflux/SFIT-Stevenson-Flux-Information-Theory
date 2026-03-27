# SFIT — Stevenson-Flux Information Theory

**A Dynamic Information-Carrying Flux Model of Gravity**  
**The 1.20134 mHz Quantum Heartbeat** — A Testable Bridge Between General Relativity and Quantum Mechanics

## Overview

Stevenson-Flux Information Theory (SFIT) proposes that gravity is a **dynamic information-carrying flux** vibrating at a precise geometric resonance frequency of **1.20134 mHz** (period 833.3 s), known as the **Quantum Heartbeat**.

This theory quantitatively explains the unexplained residuals observed in the qBounce ultra-cold neutron experiment (ILL Archive 3-14-412), including:
- A clear 1.20134 mHz modulation detected at **14.28σ** significance
- 832.6 s KWW (stretched exponential) relaxation tails with β = 1.060
- Phase-locked 4.5% post-step overshoots
- Bessel sidebands consistent with the modulation index from K = 1.060

SFIT adds a small non-reciprocal, time-dependent correction to the metric tensor while preserving the equivalence principle in the adiabatic limit. It provides a **clearly falsifiable prediction** for future GRANIT-style experiments.

**Main Website:** [stevensonfluxinformationtheory.com](https://www.stevensonfluxinformationtheory.com/)

## Quick Start

```bash
git clone https://github.com/stevensonflux/SFIT-Stevenson-Flux-Information-Theory.git
cd SFIT-Stevenson-Flux-Information-Theory

pip install -r requirements.txt

# Generate synthetic data (includes 1.20134 mHz heartbeat + explicit KWW tails)
python scripts/generate_synthetic_event_data.py

# Analyze: PSD with resonance peak + KWW fitting
python scripts/analyze_synthetic.py
