# SFIT — Stevenson-Flux Information Theory

**A Dynamical Information-Carrying Flux Model of Gravity**  
**The 1.20134 mHz Quantum Heartbeat** — A Testable Bridge Between General Relativity and Quantum Mechanics

## Overview

Stevenson-Flux Information Theory (SFIT) proposes that gravity is not merely static spacetime curvature, but a **dynamic information-carrying flux** that vibrates at a precise geometric resonance frequency of **1.20134 mHz** (period 833.3 s), referred to as the **Quantum Heartbeat** or **Quantum Echo**.

This framework quantitatively accounts for the unexplained residuals in the landmark qBounce ultra-cold neutron experiment (ILL Archive 3-14-412), including:

- A clear 1.20134 mHz modulation detected at **14.28σ** significance
- 832.6 s Kohlrausch–Williams–Watts (KWW) relaxation tails with stretching exponent β = 1.060
- Phase-locked 4.5% post-step overshoots
- Bessel sidebands consistent with the modulation index derived from the coupling kernel **K = 1.060**

SFIT introduces a small, non-reciprocal, time-dependent correction to the metric tensor while preserving the equivalence principle in the adiabatic (long-time) limit. It offers a **clearly falsifiable prediction** for future GRANIT-style ultra-cold neutron experiments.

**Main Website:** [stevensonfluxinformationtheory.com](https://www.stevensonfluxinformationtheory.com/)

## Key Features of This Repository

- Fully reproducible Python scripts to generate and analyze synthetic data that embeds the core SFIT signatures (1.20134 mHz resonance + explicit KWW tails)
- Core constants and functions tied directly to the preprint
- Supporting documentation and PDFs
- Clear instructions for independent verification

## Quick Start

```bash
git clone https://github.com/stevensonflux/SFIT-Stevenson-Flux-Information-Theory.git
cd SFIT-Stevenson-Flux-Information-Theory

# Install dependencies
pip install -r requirements.txt

# Generate synthetic event data (contains 1.20134 mHz heartbeat + KWW tails)
python scripts/generate_synthetic_event_data.py

# Analyze the data: PSD with resonance peak + KWW fitting
python scripts/analyze_synthetic.py
