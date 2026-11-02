---
name: genpark-personal-agent-microvascular-endothelial-fmd-elasticity-skill
version: "1.0.0"
description: "Zero-dependency Flow-Mediated Dilation (FMD) brachial shear stress modeler, endothelial nitric oxide bioavailability indexer, and estimated Pulse Wave Velocity (ePWV) calculator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Microvascular Endothelial FMD Elasticity Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI assistants to evaluate microvascular and macrovascular endothelial health, compute reactive hyperemia Flow-Mediated Dilation (FMD %) of the brachial artery, estimate vascular biological age vs. chronological age, and calculate central aortic stiffness via estimated Pulse Wave Velocity (ePWV).

## Agent In-Context Capabilities

- **FMD Mathematical Evaluation**: Accurately computes reactive hyperemic dilation percentage following cuff occlusion release against Corretti et al. JACC clinical standards.
- **Vascular Biological Age Modeling**: Translates endothelial nitric oxide synthase (eNOS) uncoupling or enhancement into biological vascular age shifts.
- **Aortic Arterial Stiffness (ePWV)**: Uses European Heart Journal validated consensus mathematics combining chronological age and Mean Arterial Pressure ($MAP$).

## Tools Summary

1. `evaluate_brachial_fmd_and_vascular_age`: Computes FMD %, endothelial health tier, and estimated vascular biological age.
2. `estimate_pulse_wave_velocity_and_arterial_stiffness`: Computes ePWV in m/s and evaluates central arterial stiffness threshold ($> 10.0$ m/s).
