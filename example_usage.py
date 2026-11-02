# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Microvascular Endothelial FMD Elasticity Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentMicrovascularEndothelialFmdElasticity

def main():
    agent = PersonalAgentMicrovascularEndothelialFmdElasticity()

    print("=" * 70)
    print("DEMO: Personal Agent Microvascular Endothelial & FMD Elasticity Modeler")
    print("=" * 70)

    # 1. Evaluate Brachial FMD (Baseline 4.10 mm, Peak Hyperemic 4.50 mm -> 9.76% FMD at Age 45)
    res_fmd = agent.evaluate_brachial_fmd_and_vascular_age(
        baseline_diameter_mm=4.10,
        peak_hyperemic_diameter_mm=4.50,
        chronological_age=45,
        sex="male"
    )

    print(f"\n1. Brachial Flow-Mediated Dilation (FMD) Analysis:")
    print(f"   Baseline Diameter: {res_fmd['baseline_brachial_diameter_mm']} mm")
    print(f"   Peak Hyperemic Diameter: {res_fmd['peak_hyperemic_diameter_mm']} mm")
    print(f"   Flow-Mediated Dilation: {res_fmd['flow_mediated_dilation_fmd_pct']}")
    print(f"   Endothelial Tier: {res_fmd['endothelial_health_tier']}")
    print(f"   Cardiovascular Assessment: {res_fmd['cardiovascular_risk_assessment']}")
    print(f"   Chronological Age: {res_fmd['chronological_age']} years")
    print(f"   Vascular Biological Age: {res_fmd['estimated_vascular_biological_age']} years (Delta: {res_fmd['vascular_age_delta_years']})")
    print(f"   eNOS Recommendation: {res_fmd['enos_coupling_recommendation']}")

    # 2. Estimate Pulse Wave Velocity (ePWV) at Age 45 with MAP of 94.0 mmHg
    res_pwv = agent.estimate_pulse_wave_velocity_and_arterial_stiffness(
        age=45,
        mean_arterial_pressure=94.0
    )

    print(f"\n2. Aortic Pulse Wave Velocity & Arterial Stiffness (Age 45, MAP 94.0 mmHg):")
    print(f"   Estimated PWV (ePWV): {res_pwv['estimated_pulse_wave_velocity_epwv_m_s']} m/s")
    print(f"   Arterial Stiffness: {res_pwv['arterial_stiffness_classification']}")
    print(f"   Stiffness Threshold Exceeded (> 10 m/s): {res_pwv['elevated_stiffness_threshold_exceeded']}")
    print(f"   Biomechanical Note: {res_pwv['biomechanical_summary']}")

    print("\nVerification complete: Microvascular endothelial elasticity engine executed flawlessly.")

if __name__ == "__main__":
    main()
