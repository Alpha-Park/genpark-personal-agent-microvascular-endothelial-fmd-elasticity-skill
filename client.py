# -*- coding: utf-8 -*-
"""Personal Agent Microvascular Endothelial FMD Elasticity Skill.

Zero-dependency Flow-Mediated Dilation (FMD) brachial shear stress modeler,
endothelial nitric oxide bioavailability indexer, and estimated Pulse Wave Velocity (ePWV) calculator.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentMicrovascularEndothelialFmdElasticity:
    """Quantitative endothelial health and arterial stiffness engine based on
    clinical Flow-Mediated Dilation (FMD) criteria and the European Heart Journal ePWV algorithm."""

    def evaluate_brachial_fmd_and_vascular_age(
        self,
        baseline_diameter_mm: float = 4.10,
        peak_hyperemic_diameter_mm: float = 4.45,
        chronological_age: int = 42,
        sex: str = "male"
    ) -> Dict[str, Any]:
        """Calculates brachial Flow-Mediated Dilation (FMD %), nitric oxide (NO) bioavailability,
        and vascular biological age differential."""
        base_d = max(2.0, min(8.0, float(baseline_diameter_mm)))
        peak_d = max(base_d, float(peak_hyperemic_diameter_mm))
        age = max(18, int(chronological_age))

        # FMD % = ((Peak - Baseline) / Baseline) * 100
        fmd_pct = round(((peak_d - base_d) / base_d) * 100.0, 2)

        # Endothelial Function Classification (Corretti et al. JACC standard)
        if fmd_pct >= 10.0:
            tier = "Superior Endothelial Function / High Nitric Oxide Bioavailability"
            cv_risk = "Low risk of coronary atherogenesis; optimal shear-stress vasodilation"
        elif fmd_pct >= 7.0:
            tier = "Normal / Healthy Vascular Endothelium"
            cv_risk = "Normative physiological endothelial nitric oxide synthase (eNOS) signaling"
        elif fmd_pct >= 4.0:
            tier = "Mild-to-Moderate Endothelial Dysfunction"
            cv_risk = "Early microvascular impairment; sub-clinical oxidative uncoupling of eNOS"
        else:
            tier = "Severe Endothelial Dysfunction"
            cv_risk = "Elevated hazard ratio for acute coronary syndromes and microvascular events"

        # Vascular Biological Age Differential:
        # Reference normative FMD at age 40 ~ 7.5%
        # Empirical slope: ~1.8 years younger per +1.0% FMD above reference
        fmd_delta = fmd_pct - 7.5
        vascular_age_shift = round(-1.8 * fmd_delta, 1)
        estimated_vascular_age = max(18.0, round(age + vascular_age_shift, 1))

        return {
            "baseline_brachial_diameter_mm": base_d,
            "peak_hyperemic_diameter_mm": peak_d,
            "flow_mediated_dilation_fmd_pct": f"{fmd_pct}%",
            "endothelial_health_tier": tier,
            "cardiovascular_risk_assessment": cv_risk,
            "chronological_age": age,
            "estimated_vascular_biological_age": estimated_vascular_age,
            "vascular_age_delta_years": f"{'+' if vascular_age_shift > 0 else ''}{vascular_age_shift} years",
            "enos_coupling_recommendation": (
                "Execute 3x weekly Zone 2 aerobic sessions to generate laminar pulsatile shear stress, "
                "supplement with dietary nitrates (beetroot extract) and L-citrulline (6g/day)."
                if fmd_pct < 7.5 else
                "Preserve current vascular elasticity and endothelial responsiveness."
            )
        }

    def estimate_pulse_wave_velocity_and_arterial_stiffness(
        self,
        age: int = 42,
        mean_arterial_pressure: float = 93.3
    ) -> Dict[str, Any]:
        """Calculates estimated Pulse Wave Velocity (ePWV in m/s) using the European Heart Journal
        validated consensus equation to assess central aortic stiffening."""
        a = max(18.0, min(95.0, float(age)))
        map_val = max(50.0, min(160.0, float(mean_arterial_pressure)))

        # European Heart Journal ePWV validated equation:
        # ePWV = 9.587 - 0.402*Age + 4.560e-3*Age^2 - 2.621e-5*Age^2*MAP + 3.176e-3*Age*MAP - 1.832e-2*MAP
        epwv = (
            9.587
            - 0.402 * a
            + 4.560e-3 * (a ** 2)
            - 2.621e-5 * (a ** 2) * map_val
            + 3.176e-3 * a * map_val
            - 1.832e-2 * map_val
        )
        epwv_rounded = round(max(3.0, epwv), 2)

        # Arterial Stiffness Classification:
        # Clinical benchmark: ePWV > 10.0 m/s indicates significant aortic stiffness and end-organ damage risk
        if epwv_rounded < 7.5:
            stiffness_tier = "High Arterial Compliance / Highly Elastic Aorta"
        elif epwv_rounded <= 10.0:
            stiffness_tier = "Normative Physiological Age-Associated Elasticity"
        else:
            stiffness_tier = "Clinically Significant Arterial Stiffness (Target Organ Risk)"

        return {
            "chronological_age": int(a),
            "mean_arterial_pressure_map": round(map_val, 1),
            "estimated_pulse_wave_velocity_epwv_m_s": epwv_rounded,
            "arterial_stiffness_classification": stiffness_tier,
            "elevated_stiffness_threshold_exceeded": epwv_rounded > 10.0,
            "biomechanical_summary": "Aortic pulse wave velocity reflects elastic fiber fragmentation and collagen deposition in the media layer."
        }
